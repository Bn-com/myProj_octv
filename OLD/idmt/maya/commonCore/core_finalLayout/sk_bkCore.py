# -*- coding: utf-8 -*-
# 【通用】【FinalLayout 共同调用的功能】
#  Author : 沈康
#  Data   : 2014_08

import maya.cmds as mc
import maya.mel as mel
from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
reload(sk_infoConfig)

class sk_bkCore(object):
    
    def __init__(self):
        pass

    #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【核心】【所有指定物体 BK，确保动画正确】
    #  Author  : 沈康
    #  Data    : 2013_08_23
    #------------------------------#  
    # BK执行函数 
    # animType 1 全部曲线  | 2 动画层处理
    def sk_bkPerform(self, preFrame = 10 , posFrame = 10 , simulation = 1 , animType = 2 ,step = 1 ):
        import time
        mc.cycleCheck(evaluation = 0)

        # 路径动画
        print u'\n=================【%s】开始处理================='%(u'路径动画')
        print u'---开始时间.:%s'%(time.strftime("%Y-%m-%d %H:%M:%S"))
        print u'---请耐心等待...\n'
        self.sk_bakeMotionPaths()
        print u'---结束时间.:%s'%(time.strftime("%Y-%m-%d %H:%M:%S"))
        print u'=================【%s】处理完毕=================\n'%(u'路径动画')
        
        # 寻找非参考的约束物体
        constrainAllInfos = self.sk_constraintsObjsGet()
        constrainTargets  = constrainAllInfos[0]
        constrainNodes    = constrainAllInfos[1]

        # 约束BK
        print u'\n=================【%s】开始处理================='%(u'约束类型')
        print u'---开始时间.:%s'%(time.strftime("%Y-%m-%d %H:%M:%S"))
        print u'---待处理数量:%s'%(str(len(constrainTargets)))
        print u'---请耐心等待...\n'
        self.sk_bkCore(constrainTargets , preFrame = preFrame , posFrame = posFrame , simulation = 1 , step = step )

        print u'---结束时间.:%s'%(time.strftime("%Y-%m-%d %H:%M:%S"))
        print u'=================【%s】处理完毕=================\n'%(u'约束类型')

        # 删除约束
        constraintConfigs = [x for x in (constrainNodes) if not mc.referenceQuery(x,inr=1)]
        for cons in constraintConfigs:
            ref = mc.referenceQuery(cons,isNodeReferenced = 1)
            if not ref:
                mc.delete(cons)
        
        nurbsCurves = mc.ls(type = 'nurbsCurve',l = 1)
        needCtrls = []
        attrs = ['.tx','.ty','.tz','.rx','.ry','.rz','.sx','.sy','.sz','.v']

        if nurbsCurves:
            ctrlCurves = mc.listRelatives(nurbsCurves,ap = 1, type = 'transform',f = 1)
            for obj in ctrlCurves:
                if not mc.ls(obj):
                    continue
                # bk过的不处理
                if obj in constrainTargets:
                    continue
                # 对于没有动的控制器特殊处理,为动画曲线导出做准备
                if self.sk_curveSpecialCheck(obj):
                    mc.setKeyframe(obj)
                    continue
                
                # 控制器处理,处理方案1
                if animType == 1:
                    settable = 0
                    # 只处理有keyable属性的
                    for attr in attrs:
                        state = mc.getAttr((obj + attr),settable = 1 )
                        if state:
                            settable = 1
                        if settable:
                            break
                    if settable: 
                        needCtrls.append(obj)
                    
            # 控制器处理，处理方法2：只处理动画层影响的控制器
            if animType == 2:
                animLayers = mc.ls(type = 'animLayer')
                if animLayers:
                    checkObjs = mc.listConnections(animLayers,type = 'transform')
                    if checkObjs:
                        needCtrls = list(set(checkObjs))
        
        print u'\n=================【%s】开始处理================='%(u'控制器类型')
        print u'---开始时间.:%s'%(time.strftime("%Y-%m-%d %H:%M:%S"))
        print u'---待处理数量:%s'%(str(len(needCtrls)))
        print u'---请耐心等待...\n'
        if needCtrls:
            self.sk_bkCore(needCtrls , preFrame , posFrame , simulation,step= step)

        print u'---结束时间.:%s'%(time.strftime("%Y-%m-%d %H:%M:%S"))
        print u'=================【%s】处理完毕=================\n'%(u'控制器类型')
        
        # 备份文件
        fileName = mc.file(q=1,exn = 1)
        #newName = fileName.split('.')[0] + '_baked.' + fileName.split('.')[-1]
        #mc.file(rename = newName)
        #mc.file(s = 1 ,f = 1)

        print u'\n=================【All Done!!!】=================\n'
                
    # BK核心函数,支持动画层
    def sk_bkCore(self , bkSourceobjs , preFrame = 10 , posFrame = 10 , simulation = 1 ,step = 1,returnObjs = []):
        if bkSourceobjs:
            if not mc.ls(bkSourceobjs):
                errorInfo = u'===待约束物体中，有物体不存在==='
                print bkSourceobjs
                sk_infoConfig.sk_infoConfig().checkErrorWindows(errorInfo)
                sk_infoConfig.errorCode = errorInfo
                mc.error(errorInfo)
        else:
            return []
        if not returnObjs:
            returnObjs = bkSourceobjs
            
        io = (mc.playbackOptions(q=1, minTime=1)-preFrame, mc.playbackOptions(q=1, maxTime=1)+posFrame)

        # 改进版，不bake，而是给新locator bake
        # 删除locators
        locators = mc.ls('FOOD_BakeAnim*',type = 'transform')
        if locators:
            mc.delete(locators)
        # 数值传递到locators
        locators = []
        constraintTemp = []
        for i in range(len(bkSourceobjs)):
            locTemp = mc.spaceLocator()
            locTemp = mc.rename(locTemp[0] , ('FOOD_BakeAnim_BakeAnim_' + str(i)))
            # 父子约束
            cons = mc.parentConstraint(bkSourceobjs[i] , locTemp , maintainOffset = 0)
            constraintTemp.append(cons[0])
            # 缩放约束
            cons = mc.scaleConstraint(bkSourceobjs[i] , locTemp , maintainOffset = 0)
            constraintTemp.append(cons[0])
            
            locators.append(locTemp)
        # 一次烘焙
        mc.bakeResults(locators,  t=io,
                simulation = simulation,
                sampleBy=step,
                disableImplicitControl=1,
                preserveOutsideKeys=1,
                sparseAnimCurveBake=1,
                removeBakedAttributeFromLayer=0,
                bakeOnOverrideLayer=0,
                controlPoints=0,
                shape=1)
        print u'---预BK完毕\n'
        import datetime
        print u'---当前时间.:%s'%(datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"))
        mc.delete(constraintTemp)
        print u'---当前时间.:%s'%(datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"))
        print u'---预约束处理完毕\n'
        
        # 重新约束物体
        attrs = ['.tx','.ty','.tz','.rx','.ry','.rz','.sx','.sy','.sz']
        #locators = mc.ls('FOOD_BakeAnim*',type = 'transform')
        if locators:
            for i in range(len(locators)):
                # 打断t和r属性
                for attr in attrs:
                    if not mc.getAttr((bkSourceobjs[i] + attr),settable = 1):
                        continue
                    self.checkDeleteConnection(bkSourceobjs[i] + attr)
                locatorGrp = locators[i]
                #  父子约束 ,cam已经锁住
                if 'cam_' in bkSourceobjs[i]:
                    continue
                
                #print u'----------------'
                #print locatorGrp
                #print bkSourceobjs[i].split('|')[-1]
                
                # 位移检测
                skipTranslateAxis = []
                checkTAttr = ['.tx','.ty','.tz']
                for j in range(3):
                    passAttr = ['x','y','z']
                    tState = mc.getAttr((bkSourceobjs[i] + checkTAttr[j]),settable = 1)

                    if tState:
                        pass
                    else:
                        skipTranslateAxis.append(passAttr[j])
                # 旋转检测
                skipRotateAxis = []
                checkRAttr = ['.rx','.ry','.rz']
                for k in range(3):
                    passAttr = ['x','y','z']
                    rState = mc.getAttr((bkSourceobjs[i] + checkRAttr[k]),settable = 1)
                    if rState:
                        pass
                    else:
                        skipRotateAxis.append(passAttr[k])
                # 缩放检测
                skipScaleAxis = []
                checkRAttr = ['.sx','.sy','.sz']
                for k in range(3):
                    passAttr = ['x','y','z']
                    sState = mc.getAttr((bkSourceobjs[i] + checkRAttr[k]),settable = 1)
                    if sState:
                        pass
                    else:
                        skipScaleAxis.append(passAttr[k])
                        
                #print u'----------------'
                #print locatorGrp
                #print bkSourceobjs[i].split('|')[-1]
                        
                # 父子约束
                if skipTranslateAxis and skipRotateAxis == []:
                    mc.parentConstraint(locatorGrp , bkSourceobjs[i] , skipTranslate = skipTranslateAxis , maintainOffset = 0)
                if skipTranslateAxis == [] and skipRotateAxis:
                    mc.parentConstraint(locatorGrp , bkSourceobjs[i] , skipRotate = skipRotateAxis , maintainOffset = 0)
                if skipTranslateAxis and skipRotateAxis:
                    # 修正全忽略的问题，全部忽略再去创建约束会报错
                    if (skipTranslateAxis == ['x','y','z']) and (skipRotateAxis == ['x','y','z']):
                        pass
                    else:
                        mc.parentConstraint(locatorGrp , bkSourceobjs[i] , skipTranslate = skipTranslateAxis, skipRotate = skipRotateAxis , maintainOffset = 0)
                if skipTranslateAxis == [] and skipRotateAxis == []:
                    mc.parentConstraint(locatorGrp , bkSourceobjs[i] , maintainOffset = 0)
                    
                # scale约束
                if skipScaleAxis == []:
                    try:
                        mc.scaleConstraint(locatorGrp , bkSourceobjs[i])
                    except:
                        pass
                else:
                    # xyz都忽略时，还需要scale约束吗
                    if skipScaleAxis != ['x','y','z']:
                        try:
                            mc.scaleConstraint(locatorGrp , bkSourceobjs[i] , skip = skipScaleAxis )
                        except:
                            pass
                        
            # 二次烘焙
            mc.bakeResults(bkSourceobjs,    t=io,
                    simulation = simulation,
                    sampleBy=step,
                    disableImplicitControl=1,
                    preserveOutsideKeys=1,
                    sparseAnimCurveBake=1,
                    removeBakedAttributeFromLayer=0,
                    bakeOnOverrideLayer=0,
                    controlPoints=0,
                    shape=1)
            
            print u'---清理临时信息开始\n'
            mc.delete(locators)
            print u'---清理临时信息完毕\n'
            
            #self.checkAnimCurvesFix()

            print(u'\n==========【约束】【烘焙】【成功】=========')
            print u'\n'


    #------------------------------#
    # 【辅助】修正动画曲线的欧拉翻转
    #------------------------------#   
    def checkAnimCurvesFix(self):
        animCurvs = mc.ls(type = 'animCurve')
        checkRotGrps = {}
        rotateKey = '_rotate'
        for animC in animCurvs:
            checkKeys = checkRotGrps.keys()
            inr = mc.referenceQuery(animC,inr=1)
            if inr:
                continue
            if rotateKey not in animC:
                continue
            baseObj = animC.split(rotateKey)[0]
            if baseObj not in checkKeys:
                checkRotGrps[baseObj] = []
            if animC not in checkRotGrps[baseObj]:
                checkRotGrps[baseObj].append(animC)
        
        if not checkRotGrps.keys():
            return
        
        for obj in checkRotGrps.keys():
            rotateCurves = checkRotGrps[obj]
            animKey = ''
            for animC in rotateCurves:
                animKey = animKey + animC + ' '
            mel.eval('filterCurve %s'%animKey)
    
    #------------------------------#
    # 【辅助】完全断开指定属性
    #------------------------------#     
    # 完全断开指定属性
    def checkDeleteConnection(self , attr ):
        # 被输入方
        if mc.connectionInfo(attr , isDestination = 1):
            destination = mc.connectionInfo(attr , getExactDestination = 1)
            srcConn = mc.listConnections(destination, s = 1, d = 0 , type = 'character')
            if srcConn:
                # 断开
                mc.character(destination , e = 1 ,rm = srcConn[0])
            
            sArr = mc.ls(destination , ro = 1)
            if sArr:
                src = mc.connectionInfo(destination , sourceFromDestination = 1)
                if src:
                    mc.disconnectAttr(src , destination)
            else:
                mc.delete(destination , icn = 1)

    #------------------------------#
    # 【辅助】获取所有约束物体及约束信息
    #------------------------------#     
    # 获取所有约束物体及约束信息
    def sk_constraintsObjsGet(self):
        constraintsAll = mc.ls(type='constraint')
        nodeTypeConfig = ['transform','joint']
        #约束烘焙
        if not constraintsAll:
            return [[],[]]

        tobake= []
        needConstraints = []
        
        # 处理非参考的物体
        constraints = [x for x in constraintsAll if not mc.referenceQuery(x,inr=1)]
        for constraint in constraints:
            objs = mc.listHistory(constraint)
            for checkType in nodeTypeConfig:
                temp = mc.listConnections(constraint,s = 1 ,type = checkType)
                if temp:
                    objs = objs + temp
            plugs = []
            for obj in objs:
                checkState = 0
                if (mc.nodeType(obj) in nodeTypeConfig) and mc.nodeType(obj) != "constraint":
                    # 不接受cam
                    shape = mc.listRelatives( obj , s=1 ,ni = 1,f = 1)
                    if shape:
                        if mc.nodeType(shape[0]) != 'camera':
                            checkState = 1
                    else:
                        checkState = 1
                if not checkState:
                    continue
                # 进行属性检测
                attrs = ['.tx','.ty','.tz','.rx','.ry','.rz','.sx','.sy','.sz']
                consState = 0
                for attr in attrs:
                    cons = mc.listConnections((obj + attr),s=1)
                    if cons:
                        consState = 1
                        break
                if consState:
                    plugs.append(mc.ls(obj,l=1)[0])
                    needConstraints.append(constraint)
            plugs = list(set(plugs))
            tobake+= plugs
        # 处理参考的_ct_an物体
        constraintRefs = [x for x in constraintsAll if mc.referenceQuery(x,inr=1)]
        for constraint in constraintRefs:
            objs = mc.listHistory(constraint)
            for checkType in nodeTypeConfig:
                temp = mc.listConnections(constraint,s = 1 ,type = checkType)
                if temp:
                    objs = objs + temp
            plugs = []
            for obj in objs:
                checkState = 0
                if (mc.nodeType(obj) in nodeTypeConfig) and mc.nodeType(obj) != "constraint":
                    # 不接受cam
                    shape = mc.listRelatives( obj , s=1 ,ni = 1,f = 1)
                    if shape:
                        if mc.nodeType(shape[0]) != 'camera':
                            if '_ct_an' in obj or mc.ls(obj + '.ct_an'):
                                checkState = 1
                    else:
                        if '_ct_an' in obj or mc.ls(obj + '.ct_an'):
                            checkState = 1
                if not checkState:
                    continue
                # 进行属性检测
                attrs = ['.tx','.ty','.tz','.rx','.ry','.rz','.sx','.sy','.sz']
                consState = 0
                for attr in attrs:
                    cons = mc.listConnections((obj + attr),s=1)
                    if cons:
                        consState = 1
                        break
                if consState:
                    plugs.append(mc.ls(obj,l=1)[0])
                    needConstraints.append(constraint)
            plugs = list(set(plugs))
            tobake+= plugs
            
        constraintTargets = list(set(tobake))
        constraints = list(set(needConstraints))
        
        return [constraintTargets,constraints]
            
    #------------------------------#
    # 【辅助】特殊控制器处理
    #------------------------------#     
    # 特殊控制器，单帧、无K帧的优化处理
    # 1 为没有动画信息的 | 0 为有动画信息的 
    def sk_curveSpecialCheck(self,curve):
        noKeyNum = 0
        attrsAll = mc.listAttr(curve , keyable = 1)
        if not attrsAll:
            return 1
        for attr in attrsAll:
            if not mc.ls(curve + '.' + attr):
                continue
            animCurve = mc.listConnections((curve + '.' + attr), s = 1, type = 'animCurve')
            # 无动画曲线时,判断无K帧信息
            if not animCurve:
                # 无属性连接时
                if not mc.listConnections((curve + '.' + attr), s = 1):
                    noKeyNum = noKeyNum + 1
            # 有动画曲线时，只有一帧的为无K帧信息
            else:
                animCurve = animCurve[0]
                # 获取点信息
                timePoints = mc.keyframe(animCurve, q=1, tc=1)
                # 参考的会为空
                if not timePoints:
                    continue
                # 只有单帧
                if len(timePoints) == 1:
                    noKeyNum = noKeyNum + 1
                else:
                    # 多帧判断是否所有属性一致
                    valuePoints = mc.keyframe(animCurve, q=1, vc=1)
                    if len(list(set(valuePoints))) == 1:
                        noKeyNum = noKeyNum + 1
        # 完全不需要空值
        if noKeyNum == len(attrsAll):
            return 1
        else:
            return 0

    #------------------------------#
    # 【核心】 【CAM_BK】
    # steoMode 立体测试模式,不锁立体属性
    #------------------------------#
    # 处理镜头内cam
    def sk_sceneCameraBK(self ,shotInfos = [],shotType = sk_infoConfig.sk_infoConfig().checkShotType() , stereoCam = 0,stereoMode = 1,step = 1,bkCam = '' ):
        if not shotInfos:
            shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        else:
            shotInfo = shotInfos
        camBase = ''
        camFind = 1
        if bkCam:
            camBase = bkCam
        else:
            if shotType == 2:
                camBase = 'cam_' + str(shotInfo[1]) + '_' + str(shotInfo[2])
            if shotType == 3:
                camBase = 'cam_' + str(shotInfo[1]) + '_' + str(shotInfo[2]) + '_' + str(shotInfo[3])
            if '.' in camBase:
                camBase = camBase.split('.')[0]
            if stereoMode:
                camBase += '_stCam'
            # 判断cam在不在
            if not camBase:
                camFind = 0
            if not mc.ls(camBase):
                camFind = 0
            else:
                if len(mc.ls(camBase)) != 1:
                    camFind = 0
        if not camFind:
            #errorInfo = (u'==========No Correct Cam[%s],or More Than One Cam[%s],please Fix the Camera Name=========='%(camBase,camBase))
            errorInfo = (u'==========未找到正版cam[%s],或cam名字不合法==========\n'%camBase)
            print errorInfo
            sk_infoConfig.sk_infoConfig().checkErrorWindows(errorInfo)
            sk_infoConfig.errorCode = errorInfo
            mc.error(errorInfo)

        # 准备工作
        # 时间轴信息
        io = (mc.playbackOptions(q=1, minTime=1)-10, mc.playbackOptions(q=1, maxTime=1)+10)

        # 一次BK开始
        locTemp = mc.spaceLocator()
        cons = mc.parentConstraint(camBase , locTemp , maintainOffset = 0)

        # 一次烘焙
        mc.bakeResults(locTemp,  t = io,
                simulation = 0,
                sampleBy=step,
                disableImplicitControl=1,
                preserveOutsideKeys=1,
                sparseAnimCurveBake=1,
                removeBakedAttributeFromLayer=0,
                bakeOnOverrideLayer=0,
                controlPoints=0,
                shape=1)
        mc.delete(cons)

        # 复制出信息
        camNeed = (camBase.split('|')[-1] + '_baked')
        checkCam = mc.ls(camNeed,l=1)
        if checkCam:
            mc.delete(checkCam)
        if stereoMode:
            pluginName = 'stereoCamera'
            if not mc.pluginInfo(pluginName,q= 1,loaded = 1):
                mc.loadPlugin(pluginName)
            from maya.app.stereo import stereoCameraRig
            camNew = stereoCameraRig.createStereoCameraRig(rigName='StereoCamera')
            camNew = mc.rename(camNew[0],camNeed)
            shapesOld = mc.listRelatives(camBase,s=1,f=1)
            shapesNew = mc.listRelatives(camNew,s=1,f=1)
            for i in range(len(shapesOld)):
                # 连接
                self.sk_bakeStereoCameraConnect(shapesOld[i],shapesNew[i])
        else:
            camNew = mc.duplicate(camBase,returnRootsOnly = 1,inputConnections = 1)
            camNew = mc.rename(camNew[0],camNeed.split('|')[-1])

        # cam mode不需要sx,sy,sz和v
        noNeedList = ['.sx','.sy','.sz','.v']
        for checkAttr in noNeedList:
            camAttr = camNew + checkAttr
            cons = mc.listConnections(camAttr,s=1,d=0,plugs=1)
            mc.setAttr(camAttr,l=0)
            if cons:
                mc.disconnectAttr(cons[0],camAttr)
            lockState = mc.getAttr(camAttr,l=1)
            if lockState:
                tempAttr = mc.connectionInfo(camAttr,gla=1)
                if tempAttr:
                    mc.setAttr(tempAttr,l=0)
            mc.setAttr(camAttr,1)

        # 清理目标camera物体
        chilrdNodes = mc.listRelatives(camNew,ad = 1,f=1)
        for checkNode in chilrdNodes:
            if not mc.ls(checkNode):
                continue
            checkType = mc.nodeType(checkNode)
            if checkType in ['camera','stereoRigFrustum','stereoRigCamera']:
                continue
            deleteState = 1
            if checkType in ['transform']:
                child = mc.listRelatives(checkNode,s=1,f=1)
                if not child:
                    deleteState = 0
                else:
                    for checkChild in child:
                        checkType = mc.nodeType(checkChild)
                        if checkType in ['camera','stereoRigFrustum','stereoRigCamera']:
                            deleteState = 0
            if deleteState:
                mc.delete(checkNode)
        # 解锁
        from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools
        reload(sk_sceneTools)
        sk_sceneTools.sk_sceneTools().checkLockObjs([camNeed],0,1)

        # 祛除translate和rotate的约束
        if shotInfo[0] !='nj':
            camNewFull = mc.ls(camNew,l=1)[0]
            if len(camNewFull.split('|')) != 2:
                mc.parent(camNew,world = 1)
            for attr in ['.tx','.ty','.tz','.rx','.ry','.rz']:
                mc.setAttr((camNew + attr), lock = False)
                consAttr = mc.listConnections((camNew + attr),s=1,d=0,plugs=1)
                if not consAttr:
                    continue
                mc.disconnectAttr(consAttr[0],(camNew + attr))

        # 二次BK开始
        cons = mc.parentConstraint(locTemp , camNew , maintainOffset = 0)

        # 二次烘焙
        mc.bakeResults(camNew,  t=io,
                simulation = 0,
                sampleBy=step,
                disableImplicitControl = 1 ,
                preserveOutsideKeys = 1 ,
                sparseAnimCurveBake = 1 ,
                removeBakedAttributeFromLayer = 0 ,
                bakeOnOverrideLayer = 0 ,
                controlPoints = 0 ,
                shape = 1 )

        if stereoMode:
            camShape = mc.listRelatives(camNew,s = 1,ni=1)[0]
            childGrps = mc.listRelatives(camNew,c=1,type = 'transform')
            leftGrp = ''
            rightGrp = ''
            for checkGrp in childGrps:
                if 'Left' in checkGrp:
                    leftGrp = checkGrp
                if 'Right' in checkGrp:
                    rightGrp = checkGrp
            # 重新处理立体连接
            leftGrpAttr = '%s|%s.tx'%(camNew,leftGrp)
            tempAttr = mc.connectionInfo(leftGrpAttr,gla=1)
            if tempAttr:
                mc.setAttr(tempAttr,l=0)
            cons = mc.listConnections(leftGrpAttr,s=1,d=0,plugs=1)
            if shotInfo[0] in ['do6'] and cons:
                mel.eval('source "channelBoxCommand.mel"')
                mel.eval('CBunlockAttr %s'%leftGrpAttr)
            if cons:
                mc.disconnectAttr(cons[0],leftGrpAttr)
            mc.expression(s = '%s=-0.5*%s.interaxialSeparation'%(leftGrpAttr,camShape),o = leftGrp )

            rightGrpAttr = '%s|%s.tx'%(camNew,rightGrp)
            tempAttr = mc.connectionInfo(rightGrpAttr,gla=1)
            if tempAttr:
                mc.setAttr(tempAttr,l=0)
            cons = mc.listConnections(rightGrpAttr,s=1,d=0,plugs=1)
            if shotInfo[0] =='do6' and cons:
                mel.eval('source "channelBoxCommand.mel"')
                mel.eval('CBunlockAttr %s' %rightGrpAttr)
            if cons:
                mc.disconnectAttr(cons[0],rightGrpAttr)
            mc.expression(s = '%s=0.5*%s.interaxialSeparation'%(rightGrpAttr,camShape),o = rightGrp )

            # pairx
            rigShape = mc.listRelatives(camNew,s=1,type = 'stereoRigCamera')[0]
            rigFrustum = mc.listRelatives(camNew,s=1,type = 'stereoRigFrustum')[0]
            print '------------tMode'
            print camShape
            print rigShape
            mc.connectAttr('%s.zeroParallax'%camShape,'%s.zeroParallax'%camNew,f=1)
            mc.connectAttr('%s.zeroParallax'%camShape,'%s.zeroParallax'%rigFrustum,f=1)

            # center
            attrs = ['.filmOffsetLeftCam','.filmOffsetRightCam','.interaxialSeparation','.stereo','.toeInAdjust']
            centerPre = camNeed
            centerShape = centerPre + 'CenterCamShape'
            centerGrp = centerPre
            for attr in attrs:
                mc.setAttr((centerGrp + attr),l = 0)
                mc.connectAttr((centerShape + attr),(centerGrp + attr) ,f = 1)
        cons = mc.listConnections(camNew,s = 1 ,type = 'constraint')
        if cons:
            cons = list(set(cons))
            mc.delete(cons)
        # 清理shape的某些信息
        camNewShape = mc.listRelatives(camNew,s=1,type = 'camera',f=1)
        shapeCons = mc.listConnections(camNewShape,s=1,d=0,c=1,plugs=1)
        if shapeCons:
            consNum = len(shapeCons)
            for num in range(consNum/2):
                consAttr = shapeCons[num*2+1]
                if '>' in consAttr:
                    consAttr = consAttr.split('>')[-1]
                consNode = consAttr.split('.')[0]
                # 判断
                nodeType = mc.nodeType(consNode)
                if 'animCurve' in nodeType:
                    continue
                checkAttr = shapeCons[num*2+1]
                if (not mc.referenceQuery(checkAttr.split('.')[0],inr = 1)) and mc.getAttr(checkAttr,l=1):
                    mc.setAttr(checkAttr,l=0)
                checkAttr = shapeCons[num*2]
                if (not mc.referenceQuery(checkAttr.split('.')[0],inr = 1)) and mc.getAttr(checkAttr,l=1):
                    mc.setAttr(checkAttr,l=0)
                # 断开
                mc.disconnectAttr(shapeCons[num*2+1],shapeCons[num*2])

        # 善后，清理
        mc.delete(locTemp)

        # 属性
        baseShape = mc.listRelatives(camBase,s=1,f=1)[0]
        newShape = mc.listRelatives(camNew,s=1,type = 'camera',f=1)[0]
        fixAttrList = ['.horizontalFilmAperture','.verticalFilmAperture','.filmFit']
        for attr in fixAttrList:
            newAttr = newShape + attr
            if not mc.ls(newAttr):
                continue
            oldAttr = baseShape + attr
            mc.setAttr(newAttr,l=0)
            mc.setAttr(newAttr,mc.getAttr(oldAttr))

        # 处理scale,属性打1
        for attr in ['.sx','.sy','.sz']:
            cons = mc.listConnections((camNew + attr),s=1,d=0,plugs=1)
            if cons:
                mc.disconnectAttr(cons[0],(camNew + attr))
            mc.setAttr((camNew + attr),l=0)
            mc.setAttr((camNew + attr),1)

        # 恢复立体连接
        # 锁、出组
        fixCamList = []
        if stereoMode:
            camShapes = mc.listRelatives(camNew,ad=1,type='camera',f=1)
            fixCamList = mc.listRelatives(camShapes,p=1,type='transform',f=1)
        sk_sceneTools.sk_sceneTools().checkLockObjs(fixCamList,1,1)
        for checkCam in fixCamList:
            attrs = mc.listAttr(checkCam,k=1)
            if not attrs:
                continue
            for attr in attrs:
                mc.setAttr((checkCam + '.' +attr),l = 1)

    #------------------------------#
    # 【辅助】动画曲线BK
    #------------------------------#
    def sk_bakeMotionPaths(self, preFrame = 10 , posFrame = 10 , simulation = 1 ,step = 1):
        motionPaths = mc.ls(type='motionPath')
        if motionPaths:
            #剔除参考类动画曲线
            motionPaths = [x for x in motionPaths if not mc.referenceQuery(x,inr=1)]
            tobake= []
            for motionPath in motionPaths:
                objs = mc.listConnections(motionPath,destination = 1,type = 'transform')
                objs = list(set(objs))
                tobake+= [x for x in objs if x != motionPaths]    
            io = (mc.playbackOptions(q=1, minTime=1)-preFrame, mc.playbackOptions(q=1, maxTime=1)+posFrame)
        
            mc.bakeResults(tobake,    t=io,
                        simulation = simulation,
                        sampleBy=step,
                        disableImplicitControl=1,
                        preserveOutsideKeys=1,
                        sparseAnimCurveBake=1,
                        removeBakedAttributeFromLayer=0,
                        bakeOnOverrideLayer=0,
                        controlPoints=0,
                        shape=1)
            mc.delete(motionPaths)
            #self.checkAnimCurvesFix()
            print(u'===成功烘焙路径动画===')
        else:
            print(u'===没有路径动画===')
            
    # 立体摄像机处理
    def sk_bakeStereoCameraConnect(self,source,target):
        # needAttrs
        needAttrs = ['filmFit','focalLength','horizontalFilmAperture','verticalFilmAperture','overscan','interaxialSeparation','zeroParallax']
        for attr in needAttrs:
            sourceAttr = '%s.%s'%(source,attr)
            targetAttr = '%s.%s'%(target,attr)
            checkNodeType = mc.nodeType(target)
            if checkNodeType in ['stereoRigFrustum'] and not mc.ls(targetAttr):
                continue
            if attr in ['interaxialSeparation','zeroParallax'] and not mc.ls(sourceAttr):
                continue
            cons = mc.listConnections(targetAttr,s=1,d=0)
            if cons:
                continue
            mc.setAttr(targetAttr,mc.getAttr(sourceAttr))
        # 初始化
        checkNodeType = mc.nodeType(source)
        if checkNodeType in ['stereoRigFrustum']:
            return
        attrs = mc.listAttr(source,write = 1,connectable = 1)
        for attr in attrs:
            sourceAttr = '%s.%s'%(source,attr)
            targetAttr = '%s.%s'%(target,attr)
            if not mc.ls(targetAttr):
                continue
            cons = mc.listConnections(targetAttr,destination = 0,s=1)
            if not cons:
                continue
            try:
                mc.disconnectAttr(sourceAttr,targetAttr)
            except:
                pass
        # 连接
        attrs = mc.listConnections(source,connections = 1,plugs = 1,destination = 0,s=1)
        if not attrs:
            return
        for i in range(len(attrs)/2):
            sourceAttr = attrs[2*i+1]
            checkKey = source.split('|')[-1]
            checkSource =  sourceAttr.split('|')[-1].split('.')[0]
            if checkSource == checkKey:
                continue
            targetAttr = ('%s.%s')%(target,attrs[2*i].split('.')[-1])
            cons = mc.listConnections(targetAttr,s=1,d=0,plugs = 1)
            if cons:
                if sourceAttr == cons[0]:
                    continue
            mc.connectAttr(sourceAttr,targetAttr,f=1)
        # 属性
        addAttrList = ['displayFilmGate','displayResolution','displayGateMask','displayFieldChart','stereo']
        addAttrList +=['displaySafeAction','displaySafeTitle','displayFilmPivot','displayFilmOrigin','overscan']
        for checkAttr in addAttrList:
            sourceAttr = '%s.%s'%(source,checkAttr)
            targetAttr = '%s.%s'%(target,checkAttr)
            if not mc.ls(sourceAttr):
                continue
            cons = mc.listConnections(targetAttr,s=1,d=0,plugs =1)
            if cons:
                mc.disconnectAttr(cons[0],targetAttr)
            mc.setAttr(targetAttr,mc.getAttr(sourceAttr))



