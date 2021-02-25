# -*- coding: utf-8 -*-
# 【通用】【sw项目检查工具】
#  Author : 虞丰盛
#  Data   : 2018
import  maya.cmds as mc
import maya.mel as mel
import idmt.pipeline.db
import re

class yu_checkTools(object):
    def __init__(self):
        # namespace清理
        pass

    def checkCamTools(self,returnMode = 0):

        self.fileName=mc.file(q=1,sn=1,shn=1)
        errorList = []
        if 'Lay' in self.fileName or 'Ani' in self.fileName:
            EPNo=re.compile('EP[0-9][0-9][0-9]')
            EPNo=EPNo.findall(self.fileName)[0]
            SNo=re.compile('S[0-9][0-9][0-9]')
            SNo=SNo.findall(self.fileName)[0]
            transforms=mc.ls(type='transform')
            camName=''
            errContent=[]
            camTemp=''
            frmStart=''
            frmEnd=''
            #得到相机名称
            for cam in transforms:
                if EPNo in cam and SNo in cam:
                    camName=cam
                    continue
            
            anim=idmt.pipeline.db.GetAnimByFilename(self.fileName)
            startFrame=anim.frmStart
            endFrame=anim.frmEnd
            resW=anim.resolutionW
            resH=anim.resolutionH
            renSetW=mc.getAttr('defaultResolution.width')
            renSetH=mc.getAttr('defaultResolution.height')
            fpsFrame=anim.fps
            timeMode=mc.currentUnit(q=1,time=1)
            if camName =='':
                errContent+=[u'相机命名不正确！']
                #error(errContent)
            else:
                camTemp=camName.split('_')
                frmStart=camTemp[3]
                frmEnd=camTemp[4]
                frmStart=float(frmStart)
                frmEnd=float(frmEnd)

            if len(camName)>0:
                if frmStart!=startFrame or frmEnd!=endFrame:
                    errContent+=[u'相机帧数不正确！']
                    #error(errContent)

            if renSetW !=resW or renSetH !=renSetH:
                errContent+=[u'分辨率不正确！']

            if 'pal' not in timeMode:
                errContent+=[u'帧率不正确！请设置为%s' %fpsFrame]

            if len(errContent)>0:
                if not returnMode:
                    mc.error(errContent)
                else:
                    errorList.append(errContent)
                    return errorList
        return []

    def shotAssetTextureCheckCmd(self,assetMode = 0,returnMode = 0,printMode = 1,cacheChek = 0,projStyle = 0):
        from idmt.maya.commonCore.core_mayaCommon import sk_animFileCheck
        reload(sk_animFileCheck)
        from idmt.maya.commonCore.core_baseCommon import sk_infoCore
        reload(sk_infoCore)

        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        nodeDict = {'file':'.fileTextureName','aiImage':'.filename','aiStandIn':'.dso'}

        fileNodes = []
        for nodeType in nodeDict.keys():
            fileNodes += mc.ls(type = nodeType)
        if not fileNodes:
            return []
        errorNodes = []
        errorPaths = []
        errorList = []
        projServerPath = 'Z:/SW_S3_Pipeline/03_Main-Production'
        import os
        # 豁免清单
        disLayerGrps = ['norender']
        noRMeshes = []
        for checkNode in disLayerGrps:
            if not mc.ls(checkNode):
                continue
            checkType = mc.nodeType(checkNode)
            if checkType in ['mesh']:
                noRMeshes.append(checkNode)
            if checkType in ['transform']:
                mesh = mc.listRelatives(checkNode,s=1,ni=1,type = 'mesh',f=1)
                if mesh:
                    noRMeshes.append(mesh[0])
        extraAttr = sk_infoConfig.sk_infoConfig().bkImgAttr
        skipKey = '.<udim>.'
        # 检测
        for fileNode in fileNodes:
            checkType = mc.nodeType(fileNode)
            keyAttr = fileNode + nodeDict[checkType]
            baseKey = '/maps/'
            # 获取贴图路径
            imagePath = mc.getAttr(keyAttr,x=1)
            if imagePath in [''] and mc.ls(fileNode + '.' + extraAttr):
                imagePath = mc.getAttr(fileNode + '.' + extraAttr)
            if assetMode:
                imagePath = mc.workspace(expandName = imagePath)
            # 获取绝对路径
            if imagePath:
                #realPath = sk_animFileCheck.sk_animFileCheck().checkRealPath(imagePath)
                realPath = imagePath
            else:
                realPath = ''
            if skipKey in realPath:
                continue
            # 判断路径是否存在
            if os.path.exists(realPath):
                if fileNode not in errorNodes:
                    if projServerPath.lower() not in realPath.lower():
                        if printMode:print('-----0a\n%s'%fileNode)
                        errorNodes.append(fileNode)
                        errorPaths.append(imagePath)
                    if baseKey not in imagePath.lower():
                        baseKey = '/map/'
                        if baseKey not in imagePath.lower():
                            if printMode:print('-----1a\n%s'%fileNode)
                            errorNodes.append(fileNode)
                            errorPaths.append(imagePath)
            else:
                # 是否参考模式
                refState = mc.referenceQuery(fileNode,inr = 1)
                if not refState and assetMode in [0,1]:
                    # 是否所有物体都在norender层
                    noRenderState = self.shotFileNorenderCheck(fileNode,noRMeshes)
                    if noRenderState and (fileNode not in errorNodes):
                        if printMode:print('-----2b\n%s'%fileNode)
                        errorNodes.append(fileNode)
                        errorPaths.append(u'%s\n使用上面贴图的物体有不在norender层的'%imagePath)

                    #新增加把非参考的节点加入报错数组
                    elif noRenderState==0 and (fileNode not in errorNodes):
                        if printMode:print('-----3b\n%s'%fileNode)
                        errorNodes.append(fileNode)
                        errorPaths.append(imagePath)
                    continue
                else:
                    if fileNode not in errorNodes:
                        if printMode:print('-----4b\n%s'%fileNode)
                        errorNodes.append(fileNode)
                        errorPaths.append(imagePath)
        if errorPaths:
            errorInfo = sk_infoCore.sk_infoCore().sk_infoCore(67)
            if not returnMode:
                print(errorInfo)
            for i in range(len(errorPaths)):
                if not returnMode:
                    print(errorNodes[i])
                    print(errorPaths[i])
                else:
                    errorList.append(u'[Error TexNode|有问题的贴图] %s'%errorNodes[i])
                    errorList.append(u'[Error TexPath|相关贴图路径] %s'%errorPaths[i])
            if not returnMode:
                #print(errorInfo)
                #errorInfo = sk_infoCore.sk_infoCore().sk_infoCore(68)
                #print(errorInfo)
                print '\n'
                mc.error(errorInfo)
            else:
                return errorList
        return []

    #------------------------------#
    # 查询file节点的物体是否都在norender层
    def shotFileNorenderCheck(self,checkFileNode,noRMeshes):
        checkState = 0
        from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools
        reload(sk_sceneTools)
        fileTargetNodes = sk_sceneTools.sk_sceneTools().sk_getConsNodes([checkFileNode],st=0,dt=1)
        SGNodes = []
        for checkNode in fileTargetNodes:
            checkType = mc.nodeType(checkNode)
            if checkType not in ['shadingEngine']:
                continue
            SGNodes.append(checkNode)
        if not SGNodes:
            return 0
        sgMeshes = mc.sets(SGNodes,q=1)
        if not sgMeshes:
            return 0
        sgMeshes = mc.ls(sgMeshes,l=1)
        # 对比查询
        checkNum = len(sgMeshes)
        tempNum = checkNum
        for checkMesh in sgMeshes:
            if checkMesh in noRMeshes:
                tempNum -= 1
        if checkNum != tempNum:
            checkState = 1
        # 只要有一个不在norender里，就需要报错
        return checkState

    def deleteExp(self):
        exps=mc.ls(type='expression')
        scripts=mc.ls(type='script')
        i=0
        for exp in exps:
            if 'frameCounterUpdate' in exp:
                mc.delete(exp)
                i=1
            if 'timeCodeUpdate' in exp:
                mc.delete(exp)
                i=1
        for spt in scripts:
            if 'noUpdate' in scripts:
                mc.delete(spt)
                i=1
        if i>0:
            print(u'-----已经清除frameCounterUpdate、timeCodeUpdate表达式和noUpdate script-----'),