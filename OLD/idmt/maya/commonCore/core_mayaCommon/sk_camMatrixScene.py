# -*- coding: utf-8 -*-

'''
Created on 2013-7-5

@author: shenkang
'''

import maya.cmds as mc
import maya.mel as mel

import sys,os
import math
import sk_infoConfig
reload(sk_infoConfig)

class sk_camMatrixScene(object):
    def __init__(self):
        self.ppType = 'GDC'

    # 矩阵转换，内部transform转换
    def sk_transformPoint(self,pt , matrix):
        res = [0.0,0.0,0.0]
        if(len(pt)== 3 and len(matrix)==16):
            res[0] = pt[0] * matrix[0] + pt[1] * matrix[4] + pt[2] * matrix[8] + matrix[12]
            res[1] = pt[0] * matrix[1] + pt[1] * matrix[5] + pt[2] * matrix[9] + matrix[13]
            res[2] = pt[0] * matrix[2] + pt[1] * matrix[6] + pt[2] * matrix[10] + matrix[14]
            return res
        else:
            #mc.warning(unicode('=====point格式 & matrix格式   【不对】  =====','utf8'))
            mc.warning(u'=====point格式 & matrix格式   【不对】  =====')
    
    # 反余切
    def sk_cot(self,x):
        return math.cosh(x) / math.sinh(x)
    
    def sk_getInstanceIndex(self,nodeTransform):
        paths = mc.ls(nodeTransform , allPaths = 1)
        checkState = 0
        for i in range(len(paths)):
            if paths[i] in nodeTransform.split('|')[-1]:
                return i
        if not checkState:
            return -1
    
    # 仅仅获取指定距离的极限距离
    def sk_getPointLimitXY(self,ptOG,camNodeTransform):
        camNodeShape = mc.listRelatives(camNodeTransform,c=1)[0]
        # 水平视角光圈（英寸转毫米）（半长）
        horizontalAspectCam = mc.getAttr((camNodeShape + '.horizontalFilmAperture'))*25.4 / 2 
        # 垂直视角光圈（半长）
        verticalAspectCam = mc.getAttr((camNodeShape + '.verticalFilmAperture'))*25.4 / 2
        # 焦距
        focalLengthCam = mc.getAttr((camNodeShape + '.focalLength'))
        # 长宽比
        deviceAspectRatioCame = mc.getAttr('defaultResolution.deviceAspectRatio')
        
        # X轴方向极限弧度
        angleX = math.atan( horizontalAspectCam / focalLengthCam ) 
        # Y轴方向极限弧度
        angleY = math.atan( verticalAspectCam / focalLengthCam ) 
    
        # world转cam的matrix
        camMatrix = mc.getAttr(camNodeTransform  + '.worldInverseMatrix[' + str(self.sk_getInstanceIndex(camNodeTransform)) + ']')
        
        ptCam = self.sk_transformPoint( ptOG , camMatrix )
        
        ptCamX = ptCam[2]  * math.tan(angleX)
        ptCamY = ptCam[2] * math.tan(angleY) * (horizontalAspectCam/verticalAspectCam) / deviceAspectRatioCame
        
        return [ptCamX,ptCamY]
        
    # 判断点    
    # 需要加入切片距离判断，控制最远点
    def sk_pointInCamMatrix(self,ptOG,camNodeTransform):
        # camNodeTransform = 'cam'
        camNodeShape = mc.listRelatives(camNodeTransform,c=1)[0]
        # camNodeShape = 'camShape'
        
        inCam = 0
        
        # 摄像机缩放
        scaleCam = mc.getAttr((camNodeShape + '.cameraScale'))
        # 水平视角光圈（英寸转毫米）（半长）
        horizontalAspectCam = mc.getAttr((camNodeShape + '.horizontalFilmAperture'))*25.4 / 2 
        # 垂直视角光圈（半长）
        verticalAspectCam = mc.getAttr((camNodeShape + '.verticalFilmAperture'))*25.4 / 2
        # 焦距
        focalLengthCam = mc.getAttr((camNodeShape + '.focalLength'))
        # 长宽比
        deviceAspectRatioCame = mc.getAttr('defaultResolution.deviceAspectRatio')
        # 近切片
        plane_nearCam = mc.getAttr((camNodeShape + '.nearClipPlane'))
        # 远切片
        plane_farCam = mc.getAttr((camNodeShape + '.farClipPlane'))
        
        # X轴方向极限弧度
        angleX = math.atan( horizontalAspectCam / focalLengthCam ) 
        # Y轴方向极限弧度
        angleY = math.atan( verticalAspectCam / focalLengthCam ) 
        
        # 这是object转world的matrix，并非我们需要的转cam的matrix
        # camMatrix = mc.xform(camNodeTransform , query = 1 , matrix = 1 , objectSpace = 1)
        
        # world转cam的matrix
        camMatrix = mc.getAttr(camNodeTransform  + '.worldInverseMatrix[' + str(self.sk_getInstanceIndex(camNodeTransform)) + ']')
        # ptOG = [0,0,0]
        # 查询点世界坐标
        # mc.xform(mc.ls(sl=1)[0],q = 1,t= 1,ws=1)
        # L坐标
        # ptOG = [mc.getAttr('L.translateX'),mc.getAttr('L.translateY'),mc.getAttr('L.translateZ')]
        ptCam = self.sk_transformPoint( ptOG , camMatrix )
        
        # 新功能
        # 按摄像机屏幕分10个区域
        #  1    在摄像机内
        # -10   摄像机背后
        # -1    摄像机左端
        # -2    摄像机右端
        # -3    摄像机上端
        # -4    摄像机下端
        # -5    摄像机左上
        # -6    摄像机右下
        # -7    摄像机左下
        # -8    摄像机右上
        
        if ptCam[2]<0:
            # 切片算法
            if (ptCam[2]* -1)>= plane_nearCam and (ptCam[2]*-1) <=plane_farCam:
                # X极限值
                ptCamX = ptCam[2]  * math.tan(angleX)
                # Y极限值
                ptCamY = ptCam[2] * math.tan(angleY) * (horizontalAspectCam/verticalAspectCam) / deviceAspectRatioCame
                
                if abs(ptCam[0]) <= abs(ptCamX)  and abs(ptCam[1]) <= abs(ptCamY):
                    inCam = 1
                    # print(unicode('===该点在摄像机视角内===','utf8'))
                else:
                    # 摄像机左端
                    if ptCam[0] < -1*abs(ptCamX) and abs(ptCam[1]) <= abs(ptCamY):
                        inCam = -1
                    # 摄像机右端
                    if ptCam[0] > 1*abs(ptCamX) and abs(ptCam[1]) <= abs(ptCamY):
                        inCam = -2
                    # 摄像机上端
                    if abs(ptCam[0]) <= abs(ptCamX) and ptCam[1] > 1*abs(ptCamY):
                        inCam = -3
                    # 摄像机下端
                    if abs(ptCam[0]) <= abs(ptCamX) and ptCam[1] < -1*abs(ptCamY):
                        inCam = -4
                    # 摄像机左上端
                    if ptCam[0] < -1*abs(ptCamX) and ptCam[1] > 1*abs(ptCamY):
                        inCam = -5           
                    # 摄像机右下端
                    if ptCam[0] > 1*abs(ptCamX) and ptCam[1] < -1*abs(ptCamY):
                        inCam = -6   
                    # 摄像机左下端
                    if ptCam[0] < -1*abs(ptCamX) and ptCam[1] < -1*abs(ptCamY):
                        inCam = -7           
                    # 摄像机右上端
                    if ptCam[0] > 1*abs(ptCamX) and ptCam[1] > 1*abs(ptCamY):
                        inCam = -8               
                    #pass
                    # print(unicode('<<<该点已超出摄像机视角>>>','utf8'))
            else:
                pass
                # print(unicode('<<<该点已超出摄像机视角>>>','utf8'))
        else:
            inCam = -10
            # print(unicode('<<<该点在摄像机背部>>>','utf8'))
        # 返回结果
        return inCam
            
    # 指定点处理
    def sk_pointTest(self,cam = 'cam'):
        ptOG = [mc.getAttr('L.translateX'),mc.getAttr('L.translateY'),mc.getAttr('L.translateZ')]
        result = self.sk_pointInCamMatrix(cam,ptOG)
        return result
        
    # 所有点检测
    # 优化方式：乱序执行
    def sk_meshCamAllPointsCheck(self,meshGrp,cam = 'cam'):
        import sk_pyCommon
        reload(sk_pyCommon)
        # 获取线
        ptNum = mc.polyEvaluate(meshGrp, vertex=1)
        # 创建indexIist
        sourceList = []
        for i in range(ptNum):
            sourceList.append(i)
        randList = sk_pyCommon.sk_pyCommon().checkRandomList(sourceList)
        for j in range(ptNum):
            pointOG = mc.pointPosition((meshGrp + '.pt[' + str(randList[j]) + ']'),w=1)
            result = self.sk_pointInCamMatrix(pointOG,cam)
            if result:
                return result

    # bbox顶点信息判断处理
    # outCam 值：     0    未知            |    1    不在摄像机            |    -1    在摄像机内
    def sk_bboxPTInfoConfig(self,ptResult = []):
        outCam = 0 
        if ptResult:
            # 边境数据
            lrtbGrpInfo = [[-1,-5,-7],[-2,-6,-8],[-3,-5,-8],[-5,-6,-7]]
            lrtpNum = [0,0,0,0]
            # 交叉数据
            crossGrp = [-1,-2,-3,-4,-5,-6,-7,-8]
            crossNum = [0,0,0,0,0,0,0,0]
            for i in range(len(ptResult)):
                # 边境检测和交叉检测
                for j in range(len(lrtbGrpInfo)):
                    if ptResult[i] in lrtbGrpInfo[j]:
                        lrtpNum[j] = lrtpNum[j] + 1
                # 交叉检测
                for j in range(len(crossGrp)):
                    if ptResult[i] == crossGrp[j]:
                        crossNum[j] = crossNum[j] + 1
            # 8个顶点在同一侧的，必然不在摄像机范围内
            for n in range(len(lrtbGrpInfo)):
                if lrtpNum[n] == 8:
                    outCam = 1
            # 4个顶点在-3区，4个顶点在-4区，则在inCam
            # 4个顶点在-1区，4个顶点在-2区，则在inCam
            # 4个顶点在-5区，4个顶点在-6区，则在inCam
            # 4个顶点在-7区，4个顶点在-8区，则在inCam
            for n in range(len(crossGrp)/2):
                areaNum = crossNum[2*n] + crossNum[2*n+1]
                if areaNum == 8 :
                    # 基本上，只要8个顶点，有一个顶点在任意点的对面，则在inCam
                    if crossNum[2*n] != 0 and crossNum[2*n+1] != 0:
                        outCam = -1
            # 还需要处理，4顶点在-3&-8|-5，另外4顶点在-4&-6|-7的情况，这种在inCam
        return outCam   
        
    # 场景内几何体判断
    # 目前只判断最简单的，首先对自身中心判断
    # 对于看不到的物体，需要优化判断，首先对摄像机背部的忽略
    # 新增bbox一级判断处理，忽略掉一些重复判断
    def sk_meshCamMatrixCheck(self,meshGrp,cam = 'cam'):
        # 获取obj的中心点
        #info = mc.xform(meshGrp,q = 1 , pivots = 1 ,ws = 1)
        info = mc.objectCenter(meshGrp)
        pointObj = [info[0],info[1],info[2]]
        result = self.sk_pointInCamMatrix(pointObj,cam)
        inCam = 0
        # 中心在其中
        if result == 1:
            inCam = 1
            return inCam
        # 中心不在其中
        else:
            # 对bbox进行处理,必须使用简约版bbox，不然无法得到精确的bbox的范围，尤其对freeze后的物体
            bboxMatrix = mc.exactWorldBoundingBox(meshGrp , ignoreInvisible =  1)
            checkBBox = 0
            infoPTAll = []
            # 获取bbox8点，如果8点都不在摄像机内，直接排除；
            # 然后根据在摄像机内的点情况判断inCam
            # 点1
            pointBBox = [bboxMatrix[0],bboxMatrix[1],bboxMatrix[2]]
            result = self.sk_pointInCamMatrix(pointBBox,cam)
            if result == 1:
                checkBBox = checkBBox + 1
            else:
                infoPTAll.append(result)
            # 点2
            pointBBox = [bboxMatrix[0],bboxMatrix[1],bboxMatrix[5]]
            result = self.sk_pointInCamMatrix(pointBBox,cam)
            if result == 1:
                checkBBox = checkBBox + 1
            else:
                infoPTAll.append(result)
            # 点3
            pointBBox = [bboxMatrix[0],bboxMatrix[4],bboxMatrix[2]]
            result = self.sk_pointInCamMatrix(pointBBox,cam)
            if result == 1:
                checkBBox = checkBBox + 1
            else:
                infoPTAll.append(result)
            # 点4
            pointBBox = [bboxMatrix[0],bboxMatrix[4],bboxMatrix[5]]
            result = self.sk_pointInCamMatrix(pointBBox,cam)
            if result == 1:
                checkBBox = checkBBox + 1
            else:
                infoPTAll.append(result)
            # 点5
            pointBBox = [bboxMatrix[3],bboxMatrix[1],bboxMatrix[2]]
            result = self.sk_pointInCamMatrix(pointBBox,cam)
            if result == 1:
                checkBBox = checkBBox + 1
            else:
                infoPTAll.append(result)
            # 点6
            pointBBox = [bboxMatrix[3],bboxMatrix[1],bboxMatrix[5]]
            result = self.sk_pointInCamMatrix(pointBBox,cam)
            if result == 1:
                checkBBox = checkBBox + 1
            else:
                infoPTAll.append(result)
            # 点7
            pointBBox = [bboxMatrix[3],bboxMatrix[4],bboxMatrix[2]]
            result = self.sk_pointInCamMatrix(pointBBox,cam)
            if result == 1:
                checkBBox = checkBBox + 1
            else:
                infoPTAll.append(result)
            # 点8
            pointBBox = [bboxMatrix[3],bboxMatrix[4],bboxMatrix[5]]
            result = self.sk_pointInCamMatrix(pointBBox,cam)
            if result == 1:
                checkBBox = checkBBox + 1
            else:
                infoPTAll.append(result)
            # 8个点都不在
            if checkBBox == 0:
                if result == -10:
                    # 背后处理为不在cam
                    inCam = 0
                else:
                    # 判断bbox一边倒的情况
                    # 需要排查
                    sideCheck = self.sk_bboxPTInfoConfig(infoPTAll)
                    if sideCheck:
                        inCam = 0
                    if sideCheck == -1:
                        inCam = 1
                    if sideCheck == 0:
                        check = self.sk_meshCamAllPointsCheck(meshGrp,cam)
                        if check == 1:
                            inCam = 1
                        else:
                            inCam = 0
            # 4个以上的bbox点在摄像机内，物体必在摄像机内
            if checkBBox >= 4:
                inCam = 1
                return inCam
            # 1-3个点在，进行进一步判断
            if checkBBox >= 1 and checkBBox <= 3:
                # 判断
                check = self.sk_meshCamAllPointsCheck(meshGrp,cam)
                if check == 1:
                    inCam = 1
                else:
                    inCam = 0
        return inCam

    # 场景内几何体判断
    # 特殊情况判断，线在摄像机内
    def sk_meshCamMatrixCheckLevelLine(self,meshGrp,cam = 'cam'):
        # 获取线
        edgeNum = mc.polyEvaluate(meshGrp, edge=1)
        # 标记
        inCam = 0
        # 获取点
        for i in range(edgeNum):
            pointInfo = mc.polyInfo((meshGrp + '.e[' + str(i) + ']'),edgeToVertex = 1)[0].split(':')[1].split(' ')
            needID = []
            for info in pointInfo:
                if info != '' and '\n' not in info:
                    needID.append(info)
            if len(needID) == 2:
                # camMatrix
                # world转cam的matrix
                camMatrix = mc.getAttr(cam  + '.worldInverseMatrix[' + str(self.sk_getInstanceIndex(cam)) + ']')      
                # A信息
                pointAOG =  mc.pointPosition((meshGrp + '.pt[' + needID[0] + ']'),w=1)
                pointACam = self.sk_transformPoint( pointAOG , camMatrix )
                # B信息
                pointBOG =  mc.pointPosition((meshGrp + '.pt[' + needID[1] + ']'),w=1)
                pointBCam = self.sk_transformPoint( pointBOG , camMatrix )

    # 单帧场景内全局检测
    def sk_sceneMeshCamMatrixCheckSingle(self,objs = [],cam = 'cam'):
        # 镜头内物体
        objInCam = []
        # 镜头外物体
        objNotInCam = []
        # 全场隐藏物体
        objHide = []
        # 默认所有模型
        tempObjs = []
        if objs == []:
            meshes = mc.ls(type = 'mesh')
            for mesh in meshes:
                grp = mc.listRelatives(mesh,p = 1,f=1,type = 'transform')
                if grp:
                    # 对.v属性进行判断，首先判断是否有关键帧
                    if mc.findKeyframe(grp[0],curve=True,at='visibility'):
                        tempObjs.append(grp[0])
                    # 没有关键帧，再判断是显示还是隐藏
                    else:
                        # 显示，放判断里
                        if mc.getAttr((grp[0]+'.v')) == 1:
                            tempObjs.append(grp[0])
                        # 隐藏，放隐藏里
                        else:
                            objHide.append(grp[0])
            objs = tempObjs
        # 开始处理
        for grp in objs:

            # 剔除不存在的
            if mc.objExists(grp.split('|')[-1]):
                # 判断是否隐藏
                if mc.getAttr(grp + '.v') == 1:
                    check = self.sk_meshCamMatrixCheck(grp,cam)
                    if check == 1:
                        objInCam.append(grp)
                    else:
                        objNotInCam.append(grp)
                # 隐藏则记录到不在摄像机组，下轮判断
                else:
                    objNotInCam.append(grp)
        # 输出
        result = []
        result.append(objInCam)
        result.append(objNotInCam)
        result.append(objHide)
        return result
    
    # 序列帧场景全局检测
    # 加入分段检测机制，默认是4段
    # 有个缺陷，对于极少数特殊情况没有处理，即两点都不在视野内但中间线条在视野内的未处理，但这种情况几乎不会出现
    # 返回数据结构：[objInCam,objNotInCam,objHide]
    def sk_sceneMeshCamMatrixCheckSequence(self,startFrame = 1,endFrame = 24,cam = 'cam',objs = [],splitType = 4,refMode = 0):
        # 获取当前帧
        frameNow = mc.currentTime(q=1)
        # 确保帧数整数
        startFrame = int(startFrame)
        endFrame = int(endFrame)
        print u'===================== [%s] Frames,Please Wait...====================='%(endFrame)
        print '\n'
        # 进行优化，所有模型全部进layer然后隐藏
        import sk_pyCommon
        reload(sk_pyCommon)
        # 存在set即删掉
        '''
        if mc.objExists('food_temp_Grp'):
            grpChildren = mc.listRelatives('food_temp_Grp',c = 1)
            if grpChildren:
                for grp in grpChildren:
                    mc.parent(grp,world = 1)
            mc.delete('food_temp_Grp')
        rootGrps = mc.ls(assemblies=True)
        foodGrp = mc.group(name='food_temp_Grp',em = 1)
        mc.parent(rootGrps,foodGrp)
        mc.setAttr((foodGrp + '.v'),0)
        '''
        # 处理分段信息
        firstCheckFrame = []
        for i in range(splitType) :
            splitFrame = startFrame + (i+1)*(endFrame-startFrame+1)/splitType
            if splitFrame <endFrame:
                firstCheckFrame.append(splitFrame)
        firstCheckFrame.append(endFrame)
        # 最初检测
        mc.currentTime(startFrame)
        checkStill = self.sk_sceneMeshCamMatrixCheckSingle(objs,cam)
        # 输出信息
        frame = mc.currentTime(q = 1)
        print u'===================== Frame [%s] Checked Done ====================='%(frame)
        # 镜头内物体,镜头外物体,全场隐藏物体
        objInCam = checkStill[0]
        objNotInCam = checkStill[1]
        objHide = checkStill[2]
        print (u'[inCam]:    ' + str(len(objInCam)))
        print (u'[outCam]:   ' + str(len(objNotInCam)))
        # 开始交叉检测，即跳至最后再调至最前,同时保留firstCheckFrame给第二阶段用
        changeID = 1
        firstCheckFrameList = firstCheckFrame[:]
        inCamNsList = []
        for i in range(len(firstCheckFrameList)):
            # 奇数情况下，取末尾
            if changeID % 2 == 1:
                chooseID = -1
            # 偶数情况下，或者只有一个数的时候，取首位
            if changeID % 2 == 0 or len(firstCheckFrameList) == 1:
                chooseID = 0
            # 判断处理
            mc.currentTime(firstCheckFrameList[chooseID])
            objNotInCam_Temp = []
            for grp in objNotInCam:
                check = self.sk_meshCamMatrixCheck(grp,cam)
                tempGrp =  grp.split('|')[-1]
                if check == 1:
                    objInCam.append(grp)
                    if refMode:
                        checkNs =  tempGrp[:-1*(len(tempGrp.split(':')[-1])+1)]
                        if checkNs in inCamNsList:
                            continue
                        inCamNsList.append(checkNs)
                else:
                    #checkLv2 = self.sk_meshCamMatrixCheckLevelLine(grp,cam)
                    #if checkLv2:
                    #    objInCam.append(grp)
                    if refMode:
                        checkNs = tempGrp[:-1*(len(tempGrp.split(':')[-1])+1)]
                        inState = 0
                        for ns in inCamNsList:
                            if ns != checkNs:
                                continue
                            objInCam.append(grp)
                            inState = 1
                        if not inState:
                            objNotInCam_Temp.append(grp)
                    else:
                        objNotInCam_Temp.append(grp)
            # 检测完毕，更新not及firstCheckFrameList
            objNotInCam = objNotInCam_Temp
            firstCheckFrameList.remove(firstCheckFrameList[chooseID])
            # 输出信息
            frame = mc.currentTime(q = 1)
        print u'===================== Frame [%s] Checked Done ====================='%(frame)
        print (u'[inCam]:    ' + str(len(objInCam)))
        print (u'[outCam]:   ' + str(len(objNotInCam)))
        print objNotInCam
        # 第二阶段检测，屏蔽第一阶段的帧数
        for i in range(1,(endFrame - startFrame)):
            # 屏蔽第一阶段
            if (startFrame + i) in firstCheckFrame:
                continue
            mc.currentTime(startFrame + i)
            objNotInCam_Temp = []
            # print len(objNotInCam)
            # check
            checkNs = ''
            for grp in objNotInCam:
                tempGrp =  grp.split('|')[-1]
                check = self.sk_meshCamMatrixCheck(grp,cam)
                if check == 1:
                    objInCam.append(grp)
                    if refMode:
                        checkNs =  tempGrp[:-1*(len(tempGrp.split(':')[-1])+1)]
                        if checkNs in inCamNsList:
                            continue
                        inCamNsList.append(checkNs)
                else:
                    if refMode:
                        checkNs = tempGrp[:-1*(len(tempGrp.split(':')[-1])+1)]
                        inState = 0
                        for ns in inCamNsList:
                            if ns != checkNs:
                                continue
                            objInCam.append(grp)
                            inState = 1
                        if not inState:
                            objNotInCam_Temp.append(grp)
                    else:
                        objNotInCam_Temp.append(grp)
            # 检测完毕，更新not
            objNotInCam = objNotInCam_Temp
            # 输出信息
            frame = mc.currentTime(q = 1)
        print u'===================== Frame [%s] Checked Done ====================='%(frame)
        print (u'[inCam]:    ' + str(len(objInCam)))
        print (u'[outCam]:   ' + str(len(objNotInCam)))
  
        # 还原时间轴
        mc.currentTime(frameNow)
        # 删除displayLayer
        #mc.showHidden('food_temp_DL')
        #mc.delete('food_temp_DL')
        print u'===========[Congratulations] All Frames Checked Done==========='
        result = []
        
        print u'======[OutCamObjs]======='
        print objInCam
        print objNotInCam
        print u'========================='
        
        result.append(objInCam)
        result.append(objNotInCam)
        result.append(objHide)
        #result.append(foodGrp)
        return result
    
    # 处理返回信息
    def sk_sceneMeshCamConfig(self,startFrame = 1,endFrame = 24,cam = 'cam',objs = [],splitType = 4):
        # 获取物体
        meshGrpInfo = self.sk_sceneMeshCamMatrixCheckSequence(startFrame,endFrame,cam,objs,splitType)
        self.sk_sceneCamInfoSetConfig(meshGrpInfo)
    
    # set信息处理
    def sk_sceneCamInfoSetConfig(self,meshGrpInfo):
        objInCam = meshGrpInfo[0]
        objNotInCam = meshGrpInfo[1]
        objHide = meshGrpInfo[2]
        #foodGrp = meshGrpInfo[3]

        import sk_pyCommon
        reload(sk_pyCommon)
        # 创建set组
        if mc.objExists('viewSet_ObjsInfo'):
            mc.delete('viewSet_ObjsInfo')
        mc.createNode('objectSet', n='viewSet_ObjsInfo')
        if mc.objExists('viewSet_InCam_Set'):
            mc.delete('viewSet_InCam_Set')
        mc.createNode('objectSet', n='viewSet_InCam_Set')
        mc.sets('viewSet_InCam_Set', e=1, addElement='viewSet_ObjsInfo')
        if mc.objExists('viewSet_OutCam_Set'):
            mc.delete('viewSet_OutCam_Set')
        mc.createNode('objectSet', n='viewSet_OutCam_Set')
        mc.sets('viewSet_OutCam_Set', e=1, addElement='viewSet_ObjsInfo')
        if mc.objExists('viewSet_Hide_Set'):
            mc.delete('viewSet_Hide_Set')
        mc.createNode('objectSet', n='viewSet_Hide_Set')
        mc.sets('viewSet_Hide_Set', e=1, addElement='viewSet_ObjsInfo')
        
        if objInCam:
            # set组
            mc.sets(objInCam , e=1 , addElement='viewSet_InCam_Set')

        if objNotInCam or objHide:
            # 不在视野的set组
            if objNotInCam:
                mc.sets(objNotInCam , e=1 , addElement='viewSet_OutCam_Set')
            # 隐藏物体Set组
            if objHide:
                mc.sets(objHide , e=1 , addElement='viewSet_Hide_Set')
            mc.hide('viewSet_OutCam_Set')
            for obj in objNotInCam:
                try:
                    mc.setAttr((obj+'.v'),0)
                except:
                    pass
                try:
                    mc.setAttr((obj+'.lodVisibility'),0)
                except:
                    pass
        #if foodGrp:
        #    mc.ungroup(foodGrp)

    # 后台处理函数
    def sk_sceneMeshCamConfigBatch(self,checkIn = 1):
        # 获取起始帧
        frameStart = mc.playbackOptions(min=1,q=1)
        frameEnd = mc.playbackOptions(max=1,q=1)
        # 获取镜头信息
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        camName = 'CAM:cam_' + shotInfo[1] + '_' + shotInfo[2] + '_baked'
        objs = []
        # 执行检测
        self.sk_sceneMeshCamConfig(frameStart,frameEnd,camName,objs)
        # 特殊处理
        if shotInfo[0] == 'zm':
            # 显示海洋
            seaObj = mc.ls('*:*_sea_*',type = 'transform') + mc.ls('*_sea_*',type = 'transform')
            if seaObj:
                for obj in seaObj:
                    try:
                        mc.setAttr((obj+'.v'),1)
                    except:
                        pass
                    try:
                        mc.setAttr((obj+'.lodVisibility'),1)
                    except:
                        pass
                    
        intList = ['0','1','2','3','4','5','6','7','8','9']
        # 镜头文件输出数据
        if shotInfo[1][0] in intList and shotInfo[2][0] in intList:
            inObjs = mc.sets('viewSet_InCam_Set', q = 1)
            outObjs = mc.sets('viewSet_OutCam_Set', q = 1)
            hideObjs = mc.sets('viewSet_Hide_Set', q = 1)
            if inObjs == None:
                inObjs = []
            if outObjs == None:
                outObjs = []
            if hideObjs == None:
                hideObjs = []
                
            # 本地输出
            #localInfoPath = sk_infoConfig.sk_infoConfig().checkLocalInfoPath()
            #localCamObjsInfoPath = localInfoPath + '/' + 'camInOutInfo' + '/' + str(shotInfo[0]) + '/' + str(shotInfo[1]) + '/' + shotInfo[2] + '/'
            localCamObjsInfoPath = sk_infoConfig.sk_infoConfig().checkShotDataInfoPath(server=0,infoMode=5)
            mc.sysFile(localCamObjsInfoPath, makeDir=True)
            sk_infoConfig.sk_infoConfig().checkFileWrite((localCamObjsInfoPath + 'viewSet_InCam_Set.txt'),inObjs)
            sk_infoConfig.sk_infoConfig().checkFileWrite((localCamObjsInfoPath + 'viewSet_OutCam_Set.txt'),outObjs)
            sk_infoConfig.sk_infoConfig().checkFileWrite((localCamObjsInfoPath + 'viewSet_Hide_Set.txt'),hideObjs)
            
            # update
            #serverInfoPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
            #serverCamObjsInfoPath = serverInfoPath + '/data/camInOutInfo/' + str(shotInfo[0]) + '/' + str(shotInfo[1]) + '/' + shotInfo[2] + '/'
            serverCamObjsInfoPath = sk_infoConfig.sk_infoConfig().checkShotDataInfoPath(server=1,infoMode=5)
            # 显示信息上传
            fileInfo = 'viewSet_InCam_Set.txt'
            from commonCore.core_baseCommon import pySysFile
            reload(pySysFile)
            if self.ppType == 'GDC':
                updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localCamObjsInfoPath + fileInfo) + '"' + ' ' + '"' + (serverCamObjsInfoPath + fileInfo) + '"' + ' true'
                mel.eval(updateAnimCMD)
            if self.ppType == 'AAS':
                pySysFile.pySysFile('copy',[(localCamObjsInfoPath + fileInfo)],[(serverCamObjsInfoPath + fileInfo)])
            # 摄像机外信息上传
            fileInfo = 'viewSet_OutCam_Set.txt'
            if self.ppType == 'GDC':
                updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localCamObjsInfoPath + fileInfo) + '"' + ' ' + '"' + (serverCamObjsInfoPath + fileInfo) + '"' + ' true'
                mel.eval(updateAnimCMD)
            if self.ppType == 'AAS':
                pySysFile.pySysFile('copy',[(localCamObjsInfoPath + fileInfo)],[(serverCamObjsInfoPath + fileInfo)])
            # 隐藏信息上传
            fileInfo = 'viewSet_Hide_Set.txt'
            if self.ppType == 'GDC':
                updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localCamObjsInfoPath + fileInfo) + '"' + ' ' + '"' + (serverCamObjsInfoPath + fileInfo) + '"' + ' true'
                mel.eval(updateAnimCMD)
            if self.ppType == 'AAS':
                pySysFile.pySysFile('copy',[(localCamObjsInfoPath + fileInfo)],[(serverCamObjsInfoPath + fileInfo)])
                
            print u'========================[%s_%s][Cam Check Info][Update to Server]Done========================'%(str(shotInfo[1]),str(shotInfo[2]))
        # check in
        if checkIn:
            import os
            userName = os.environ['USERNAME']
            projectInfo = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(shotInfo[0])
            fileInfo = '1|' + projectInfo + '|' + shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2] + '_' + shotInfo[3] + '_' + shotInfo[4] + '|' + userName
            checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
            #print checkOutCmd
            mel.eval(checkOutCmd)
            # checkIn
            mel.eval('idmtProject -checkin -description \"FinalLayout Base File | View Sight Configed\"')
        
        # 成功代码
        return 0
    
    # 从网络更新camInOut信息
    def sk_sceneCamServerInfoImport(self):
        import os
        import sk_infoConfig
        reload(sk_infoConfig)
        # 从服务器端读文件
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        #serverInfoPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        #serverCamObjsInfoPath = serverInfoPath + '/data/camInOutInfo/' + str(shotInfo[0]) + '/' + str(shotInfo[1]) + '/' + shotInfo[2] + '/'
        serverCamObjsInfoPath = sk_infoConfig.sk_infoConfig().checkShotDataInfoPath(server=1,infoMode=5)
        camInInfo = 'viewSet_InCam_Set.txt'
        camOutInfo = 'viewSet_OutCam_Set.txt'
        camHideInfo = 'viewSet_Hide_Set.txt'
        if os.path.exists(serverCamObjsInfoPath + camInInfo) and os.path.exists(serverCamObjsInfoPath + camHideInfo) and os.path.exists(serverCamObjsInfoPath + camOutInfo):
            camInObjs = sk_infoConfig.sk_infoConfig().checkFileRead(serverCamObjsInfoPath + camInInfo)
            camOutObjs = sk_infoConfig.sk_infoConfig().checkFileRead(serverCamObjsInfoPath + camOutInfo)
            camHideObjs = sk_infoConfig.sk_infoConfig().checkFileRead(serverCamObjsInfoPath + camHideInfo)
            meshGrpInfo = [camInObjs,camOutObjs,camHideObjs,[]]
            self.sk_sceneCamInfoSetConfig(meshGrpInfo)
        else:
            errorInfo =  u'====================[%s_%s]服务器端没有cam数据===================='%(str(shotInfo[0]),str(shotInfo[1]))
            print errorInfo
            sk_infoConfig.errorCode = errorInfo
            mc.error()

    # outCAM显示隐藏
    def sk_sceneOutCamVOnOff(self):
        # 切换隐藏物体
        if mc.ls('viewSet_OutCam_Set'):
            objOutCam = mc.sets('viewSet_OutCam_Set', q=1)
            if objOutCam:
                vState = mc.getAttr(objOutCam[0] + '.v')
                vLodState = mc.getAttr(objOutCam[0] + '.lodVisibility')
                # 显示
                if vState == 0 or vLodState == 0:
                    mc.showHidden('viewSet_OutCam_Set')
                    for obj in objOutCam:
                        try:
                            mc.setAttr((obj+'.v'),1)
                        except:
                            pass
                        try:
                            mc.setAttr((obj+'.lodVisibility'),1)
                        except:
                            pass
                # 隐藏
                else:
                    mc.hide('viewSet_OutCam_Set')
                    for obj in objOutCam:
                        try:
                            mc.setAttr((obj+'.v'),0)
                        except:
                            pass
                        try:
                            mc.setAttr((obj+'.lodVisibility'),0)
                        except:
                            pass
        # 修正显示物体
        if mc.ls('viewSet_InCam_Set'):
            objInCam = mc.sets('viewSet_InCam_Set', q=1)
            if objInCam:
                for obj in objInCam:
                    try:
                        mc.setAttr((obj + '.v'),1)
                    except:
                        pass
                    try:
                        mc.setAttr((obj + '.lodVisibility'),1)
                    except:
                        pass
                
    # 测试光线角度
    def skTestGetLightDir(self,eyeCircle , masterLight , sourceRotate = [0,0,0] ,ltBase = [[1,0],[0.7071,0.7071],[0,1],[-0.7071,0.7071],[-1,0],[-0.7071,-0.7071],[0,-1],[0.7071,-0.7071]] ,ltID = [1,5,3,8,2,7,4,6]):
        #eyeCircle = 'nurbsCircle1'
        #masterLight = 'areaLight1'
        needPlane = mc.duplicate(eyeCircle)[0]
        needMLight = mc.duplicate(masterLight)[0]
        mc.parent(needMLight,needPlane)
        rotateAttrs = ['.rx','.ry','.rz']
        for attr in rotateAttrs:
            index = rotateAttrs.index(attr)
            mc.setAttr((needPlane+attr),(sourceRotate[index]))
        # 沿放射方向前进，推算来自方向
        poseSource = [mc.getAttr(needMLight + '.tx'),mc.getAttr(needMLight + '.tz')]
        mc.move(0,0,-5,needMLight,r = 1, os = 1 ,wd = 1)
        poseTarget = [mc.getAttr(needMLight + '.tx'),mc.getAttr(needMLight + '.tz')]
        vectorComeFrom = [(poseSource[0] - poseTarget[0]),(poseSource[1] - poseTarget[1])]
        mc.delete(needPlane)
        # 计算圆周最近点
        radius = pow((pow(vectorComeFrom[0],2)+pow(vectorComeFrom[1],2)),0.5)
        # 获取距离信息
        disInfos = []
        for i in range(len(ltBase)):
            distance = pow((pow((vectorComeFrom[0]-radius*ltBase[i][0]),2) + pow((vectorComeFrom[1]-radius*ltBase[i][1]),2)),0.5)
            disInfos.append(distance)
        minIndex = disInfos.index(min(disInfos))
        ltNeedID = ltID[minIndex]
        # 灯光处理
        mc.setAttr((eyeCircle + '.lightCtrl'),ltNeedID)
        frameNow = mc.currentTime(q = 1)
        mc.currentTime(frameNow + 1)
        mc.currentTime(frameNow)
        
# camera相关工具集
class cameraTools(object):
    def __init__(self):
        self.ppType = 'GDC'
    
    # goldenLine Create
    def camGoldenLineCreate(self,cameraGrp,projSimp = '',lenthScale = 5,thickScale = 5,viewState = 1,rebuild = 0,printMode = 0):
        goldallGrp = 'goldLine_Grp'
        if not mc.ls(goldallGrp):
            mc.group(n = goldallGrp,em = 1)
        # 创建
        if printMode:print '------000'
        
        camLines = self.camBaseLinesBuild(cameraGrp,rebuild)
        
        if printMode:print '------001'
        
        goldenGrp = camLines[0]
        topLine   = camLines[1]
        downLine  = camLines[2]
        leftLine  = camLines[3]
        rightLine = camLines[4]
        rootGrp   = camLines[5]
        try:
            mc.parent(goldenGrp,goldallGrp)
        except:
            pass
        # 计算
        ptPosition = mc.xform( rootGrp , ws = 1,t= 1,q = 1)
        
        if printMode:print '----------003'
        
        limitInfos = sk_camMatrixScene().sk_getPointLimitXY(ptPosition,cameraGrp)
        
        if printMode:print '----------005'
        
        limitX = abs(limitInfos[0])
        limitY = abs(limitInfos[1])
        # 校正
        mc.setAttr((topLine   + '.ty'),l = 0)
        mc.setAttr((downLine  + '.ty'),l = 0)
        mc.setAttr((leftLine  + '.tx'),l = 0)
        mc.setAttr((rightLine + '.tx'),l = 0)
        mc.setAttr((topLine   + '.ty'),limitY/3)
        mc.setAttr((downLine  + '.ty'),-1*limitY/3)
        mc.setAttr((leftLine  + '.tx'),-1*limitX/3)
        mc.setAttr((rightLine + '.tx'),limitX/3)
        # 项目标配
        if projSimp:
            projInfos = sk_infoConfig.sk_infoConfig().checkProjCamSetting(projSimp)
            lenthScale = projInfos[4]
            thickScale = projInfos[5]
        # 粗细
        if lenthScale:
            for attr in ['.sy']:
                mc.setAttr((leftLine + attr),l=0)
                mc.setAttr((rightLine + attr),l=0)
                mc.setAttr((leftLine + attr),lenthScale)
                mc.setAttr((rightLine + attr),lenthScale)
            for attr in ['.sx']:
                mc.setAttr((topLine + attr),l=0)
                mc.setAttr((downLine + attr),l=0)
                mc.setAttr((topLine + attr),lenthScale)
                mc.setAttr((downLine + attr),lenthScale)
        if thickScale:
            for attr in ['.sx','.sz']:
                mc.setAttr((leftLine + attr),l = 0)
                mc.setAttr((rightLine + attr),l = 0)
                mc.setAttr((leftLine + attr),thickScale)
                mc.setAttr((rightLine + attr),thickScale)
            for attr in ['.sy','.sz']:
                mc.setAttr((topLine + attr),l = 0)
                mc.setAttr((downLine + attr),l = 0)
                mc.setAttr((topLine + attr),thickScale)
                mc.setAttr((downLine + attr),thickScale)
        # view
        mc.setAttr((goldenGrp + '.v'),l = 0)
        mc.setAttr((goldenGrp + '.v'),viewState)

        # add block mesh
        if self.ppType in ['GDC']:
            blockGrp = self.camBlockMeshAdd(cameraGrp)
            blockMesh = mc.listRelatives(blockGrp,s=1,ni=1,type = 'mesh')[0]
            mc.setAttr((blockMesh + '.overrideEnabled') , 1)
            mc.setAttr((blockMesh + '.overrideDisplayType') , 2)
        # lock
        for attr in ['.tx','.ty','.tz','.rx','.ry','.rz','.sx','.sy','.sz']:
            mc.setAttr((topLine + attr),l = 1)
            mc.setAttr((downLine + attr),l = 1)
            mc.setAttr((leftLine + attr),l = 1)
            mc.setAttr((rightLine + attr),l = 1)
            if self.ppType in ['GDC']:
                mc.setAttr((blockGrp + attr),l = 1)
        for grp in [topLine,downLine,leftLine,rightLine]:
            mesh = mc.listRelatives(grp,s=1,ni=1,type = 'mesh')[0]
            mc.setAttr((mesh + '.overrideEnabled') , 1)
            mc.setAttr((mesh + '.overrideDisplayType') , 2)
        
        mc.select(cl = 1)

    # 加挡板
    def camBlockMeshAdd(self,camName):
        camName = camName.split('|')[-1]
        camBlockBase = 'camBlock_base'
        camBlockName = '%s_%s'%(camBlockBase,camName)
        serverPath = '//file-cluster/gdc/Resource/Support/cam/camBlock_templete.mb'
        blockGrps = mc.ls(camBlockName,type = 'transform')
        if mc.ls(blockGrps):
            needCamBlockGrp = blockGrps[0]
        else:
            blockGrps = mc.ls('%s_*'%(camBlockBase),type = 'transform')
            if not blockGrps:
                if mc.ls('camBlockShader'):
                    mc.delete('camBlockShader')
                # 导入
                import time
                timeNow = time.ctime().split(" ")[3].replace(":", "_")
                import datetime
                msTime = datetime.datetime.now().microsecond
                timeNow += str(msTime / 100000)
                temNs = 'food' + timeNow
                mc.file(serverPath, i=1 , loadReferenceDepth="none", namespace = temNs , type='mayaBinary' , preserveReferences=1 , options="v=0")
                # 删除namespace
                mc.namespace(force=1 , moveNamespace=[(':' + temNs) , ':'])
                mc.namespace(removeNamespace=(':' + temNs))
                blockGrps = [camBlockBase]
            # 打组
            tempGrp = mc.duplicate(blockGrps[0],rr=1)[0]
            tempGrp = mc.parent(tempGrp,'goldenTemp_%s'%camName)
            needCamBlockGrp = mc.rename(tempGrp,camBlockName)
            for attr in ['tx','ty','tz','rx','ry','rz','sx','sy','sz']:
                checkAttr = '%s.%s'%(needCamBlockGrp,attr)
                mc.setAttr(checkAttr,l=0)
                setValue = 0
                if attr in ['tz']:
                    setValue = 0.1
                if attr in ['sx','sy','sz']:
                    setValue = 1
                mc.setAttr(checkAttr,setValue)
        if mc.ls(camBlockBase):
            mc.delete(camBlockBase)
        return needCamBlockGrp
        
    # createBaseCrossGroup
    def camBaseLinesBuild(self,cameraGrp,rebuild = 0,printMode = 0):
        ns = ''
        if ':' in cameraGrp:
            camName = cameraGrp.split(':')[-1]
            ns = cameraGrp[:-1*len(camName)]
        else:
            camName = cameraGrp
        camName = camName.split('|')[-1]
            
        if printMode:print '------c001'
        
        if ns:
            goldenGrp = '%s%s_%s'%(ns,'goldenTemp',camName)
            rootGrp   = '%s%s_%s'%(ns,'rootTemp',camName)
            topLine   = '%s%s_%s'%(ns,'topLineTemp',camName)
            downLine  = '%s%s_%s'%(ns,'downLineTemp',camName)
            leftLine  = '%s%s_%s'%(ns,'leftLineTemp',camName)
            rightLine = '%s%s_%s'%(ns,'rightLineTemp',camName)
        else:
            goldenGrp = '%s_%s'%('goldenTemp',camName)
            rootGrp   = '%s_%s'%('rootTemp',camName)
            topLine   = '%s_%s'%('topLineTemp',camName)
            downLine  = '%s_%s'%('downLineTemp',camName)
            leftLine  = '%s_%s'%('leftLineTemp',camName)
            rightLine = '%s_%s'%('rightLineTemp',camName)
            
        if printMode:print '------c002';

        camNodeShape = mc.listRelatives(cameraGrp,s = 1,type = 'camera')[0]
        plane_nearCam = mc.getAttr((camNodeShape + '.nearClipPlane'))
        if printMode:print '------c002'
        maxLenth = 1
        lenScale = 1.2
        if plane_nearCam >= maxLenth:
            lenScale = 1+ plane_nearCam/maxLenth
            maxLenth = plane_nearCam + maxLenth
        if self.ppType in ['GDC']:
            lenScale *= 5
            
        if printMode:print '------c003'
        
        if rebuild:
            if mc.ls(goldenGrp):
                mc.delete(goldenGrp)
        else:
            if mc.ls(goldenGrp):
                if abs(mc.getAttr(goldenGrp+'.tz')) > plane_nearCam :
                    return [goldenGrp,topLine,downLine,leftLine,rightLine,rootGrp]
                else:
                    mc.delete(goldenGrp)
                    
        if printMode:print '------c005'
        
        mc.group(name = goldenGrp, em = 1)
        mc.group(name = rootGrp, em = 1)
        if printMode:print '------c006'
        boxShader = 'camGoldenLineShader'
        boxSG     = 'camGoldenLineSG'
        if not mc.ls(boxShader):
            boxShader = mc.shadingNode('lambert', asShader=True, name=boxShader)
            boxSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=boxSG)
            mc.connectAttr((boxShader + '.outColor'), (boxSG + '.surfaceShader'))
            colorValue = [0,1,0]
            trasValue  = [1,1,1]
            ambienValue = [1,1,1]
            if self.ppType in ['GDC']:
                colorValue = [1,1,1]
                trasValue  = [0.875,0.875,0.875]
                ambienValue = [0,0,0]
            mc.setAttr((boxShader + '.color'), colorValue[0], colorValue[1], colorValue[2], type='double3')
            mc.setAttr((boxShader + '.transparency'), trasValue[0], trasValue[1], trasValue[2], type='double3')
            mc.setAttr((boxShader + '.ambientColor'), ambienValue[0], ambienValue[1], ambienValue[2], type='double3')

        if printMode:print '------c006'
        
        mc.polyCube(name = topLine)
        for i in [1,2,3,4,5]:
            mc.delete('%s.f[%s]'%(topLine,i))
        mc.select(topLine)
        mel.eval("DeleteHistory")
        mc.sets(topLine, e=1, forceElement=boxSG)
        mc.setAttr((topLine + '.sx'),1.1*lenScale)
        mc.setAttr((topLine + '.sy'),0.001*lenScale)
        mc.setAttr((topLine + '.sz'),0.001*lenScale)
        mc.makeIdentity(topLine,apply = 1,translate = 1,rotate = 1,scale = 1)
        mc.parent(topLine,rootGrp)

        if printMode:print '------c007'
        
        mc.polyCube(name = downLine)
        for i in [1,2,3,4,5]:
            mc.delete('%s.f[%s]'%(downLine,i))
        mc.select(downLine)
        mel.eval("DeleteHistory")
        mc.sets(downLine, e=1, forceElement=boxSG)
        mc.setAttr((downLine + '.sx'),1.1*lenScale)
        mc.setAttr((downLine + '.sy'),0.001*lenScale)
        mc.setAttr((downLine + '.sz'),0.001*lenScale)
        mc.makeIdentity(downLine,apply = 1,translate = 1,rotate = 1,scale = 1)
        mc.parent(downLine,rootGrp)
        
        if printMode:print '------c008'
        
        mc.polyCube(name = leftLine)
        for i in [1,2,3,4,5]:
            mc.delete('%s.f[%s]'%(leftLine,i))
        mc.select(leftLine)
        mel.eval("DeleteHistory")
        mc.sets(leftLine, e=1, forceElement=boxSG)
        mc.setAttr((leftLine + '.sx'),0.65*lenScale)
        mc.setAttr((leftLine + '.sy'),0.001*lenScale)
        mc.setAttr((leftLine + '.sz'),0.001*lenScale)
        mc.setAttr((leftLine + '.rz'),90)
        mc.makeIdentity(leftLine,apply = 1,translate = 1,rotate = 1,scale = 1)
        mc.parent(leftLine,rootGrp)
        
        if printMode:print '------c009'
        
        mc.polyCube(name = rightLine)
        for i in [1,2,3,4,5]:
            mc.delete('%s.f[%s]'%(rightLine,i))
        mc.select(rightLine)
        mel.eval("DeleteHistory")
        mc.sets(rightLine, e=1, forceElement=boxSG)
        mc.setAttr((rightLine + '.sx'),0.65*lenScale)
        mc.setAttr((rightLine + '.sy'),0.001*lenScale)
        mc.setAttr((rightLine + '.sz'),0.001*lenScale)
        mc.setAttr((rightLine + '.rz'),90)
        mc.makeIdentity(rightLine,apply = 1,translate = 1,rotate = 1,scale = 1)
        mc.parent(rightLine,rootGrp)

        if printMode:print '------c010'
        
        mc.parent(rootGrp,goldenGrp)
        mc.setAttr((rootGrp+'.tz'),-1*maxLenth)
        
        # 约束
        mc.parent(goldenGrp,cameraGrp)
        for attr in ['.tx','.ty','.tz','.rx','.ry','.rz']:
            mc.setAttr((goldenGrp+ attr),0)
        for attr in ['.sx','.sy','.sz']:
            mc.setAttr((goldenGrp+ attr),1)
        mc.parent(goldenGrp,world = 1)
        mc.parentConstraint(cameraGrp,goldenGrp, maintainOffset = 0)
        #mc.scaleConstraint(cameraGrp,goldenGrp, maintainOffset = 0)
        
        # 渲染属性
        for obj in [goldenGrp,topLine,downLine,leftLine,rightLine]:
            shape = mc.listRelatives(obj,s=1,ni=1,type = 'mesh')
            if not shape:
                continue
            shape = shape[0]
            for attr in ['castsShadows','receiveShadows','motionBlur','primaryVisibility','smoothShading','visibleInReflections','visibleInRefractions','doubleSided']:
                mc.setAttr((shape + '.' + attr),0)

        '''
        # 表达式处理
        goldenGrpLenthExp = '%s_LengthExp'%(goldenGrp)
        if mc.ls(goldenGrpLenthExp,type = 'expression'):
            mc.delete(goldenGrpLenthExp)
        cmd = '%s.translateZ = -1 * (%s.nearClipPlane + 1)'%(goldenGrp,camNodeShape)
        exp = mc.expression(s = cmd)
        mc.rename(exp,goldenGrpLenthExp)
        '''
        # 焦距自动表达式
        mc.setAttr('%s.sx'%goldenGrp,l=1)
        mc.setAttr('%s.sy'%goldenGrp,l=1)
        checkAttr = '%s.sz'%goldenGrp
        cons = mc.listConnections(checkAttr,s=1,d=0,type = 'expression')
        if cons:
            mc.delete(cons)
        flAttr = '%s.focalLength'%camNodeShape
        flValue = mc.getAttr(flAttr)
        cmd = '%s = %s / %s;'%(checkAttr,flAttr,str(flValue))
        mc.expression(s = cmd)

        return [goldenGrp,topLine,downLine,leftLine,rightLine,rootGrp]

    # 获取指定相机的三分线组
    def getGoldenGrpFromCam(self,camGrp,printMode = 0):
        goldenGrp = ''
        if printMode: print '----------r001'
        camShape = mc.listRelatives(camGrp,s=1,ni=1,type = 'camera')
        consEx = mc.listConnections(camShape,s=0,d=1,type = 'expression')
        if printMode: print '----------r002\n%s'%consEx
        if not consEx:
            return
        consNodes = mc.listConnections(consEx,s=0,d=1,type = 'transform')
        if printMode: print '----------r003\n%s'%consNodes
        if not consNodes:
            return
        for checkNode in consNodes:
            if 'goldenTemp_' not in checkNode:
                continue
            goldenGrp = checkNode
            if printMode: print checkNode
        return goldenGrp