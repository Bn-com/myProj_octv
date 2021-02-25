# -*- coding: utf-8 -*-

'''
Created on 2013-8-1

@author: shenkang
'''
#  Mender:韩虹
#  Data  :2014_08
# 顺溜项目添加了场
import maya.cmds as mc
import maya.mel as mel
import os
import re
import idmt.pipeline.db
from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
reload(sk_infoConfig)
from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
reload(sk_referenceConfig)
from idmt.maya.commonCore.core_baseCommon import sk_infoCore
reload(sk_infoCore)

class sk_animFileCheck(object):
    def __init__(self):
        # namespace清理
        self.serverPreKey = ['z:','Z:','l:','L:']
    
    #-----------------------------------------------------------------------------------------------------#
    #-----------------------------------------#
    # 文件Asset 参考检测系统    #-----------------------------------------#
    # backType 0 返回缺失的参考信息  | 1 报错缺失的参考信息
    def shotAssetRefCheck(self,checkType = 'an',backType = 0 ,shotType = 0,printMode = 0 , igKey = [],returnMode = 0):
        if not shotType:
            shotType = sk_infoConfig.sk_infoConfig().checkShotType()

        errorList = []

        print u'------------------------正在检测参考信息------------------------'
        
        fileType = ''
        if checkType == 'an':
            fileType = 'anim'
        if checkType == 'lr':
            fileType = 'render'

        if printMode: print '--------001'

        refInfo = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refPaths = refInfo[1][0]
        
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        projAssetBasePath = sk_infoConfig.sk_infoConfig().checkProjectServerPath() 
        fileFormat = sk_infoConfig.sk_infoConfig().checkProjectFileFormat(shotInfo[0],shotInfo = [shotInfo[0],shotInfo[1],shotInfo[2],'rg'])
        
        # 获取服务器端asset信息
        fileInfo= shotInfo[0] + '_' + str(shotInfo[1]) + '_' + str(shotInfo[2])
        if shotType in [3]:
            fileInfo= shotInfo[0] + '_' + str(shotInfo[1]) + '_' + str(shotInfo[2]) +'_' + str(shotInfo[3])
        anim = idmt.pipeline.db.GetAnimByFilename(fileInfo)
        assets = anim.GetAssetNameInAnim()

        # 某些镜头会有空白list
        '''
        if not assets:
            errorList = [u'\n[No Server Data|]服务器端未发现asset列表']
            if returnMode:
                return errorList
            else:
                print errorList[0]
                mc.error()
        '''

        refLowerPaths = []
        for refPath in refPaths:
            checkInfo = refPath.lower()
            for checkKey in self.serverPreKey:
                if checkKey in checkInfo:
                    checkInfo = checkInfo.replace(checkKey,'//file-cluster/gdc')
                if checkKey in projAssetBasePath:
                    projAssetBasePath = projAssetBasePath.replace(checkKey,'//file-cluster/gdc')
            refLowerPaths.append(checkInfo)

        # 豁免的asset
        noNeedKeys = []
        if shotInfo[0] == 'zm':
            noNeedKeys = ['SplashOut_Above' ,'SplashIn_Above']
        if shotInfo[0] == 'nj':
            noNeedKeys=[]
            for i in range(10):
                noNeedKeys.append('me'+str(i))
        noNeedKeys.append(u'_cam.m')

        # 丢失的参考
        assetLostID = []
        assetLostPath = []
        for i in range(len(assets)):
            mycode = ''
            if anim.projectName in ['YODA','Ninjago','Xyj']:
                mycode = '/' + assets[i].code
            myFileType = fileType
            if anim.projectName in ['YODA','Ninjago','Xyj'] and assets[i].asset_type == 'sets':
                myFileType = 'tex'
            if shotInfo[0] in ['mi'] and assets[i].asset_type == 'sets':#=====add by zhangben 2016.3.7
                myFileType = u'(gpu|%s)'%fileType
            gpuKey = '_'
            if assets[i].asset_type == 'sets':
                gpuKey = '(_|_GPU_)'
            assetNeed = projAssetBasePath + 'scenes/' + assets[i].asset_type + mycode + '/' + assets[i].asset_name + '/master/' + shotInfo[0] + '_' + assets[i].asset_name + gpuKey + 'h_ms_' + myFileType + fileFormat
            pattern = '^' + projAssetBasePath + 'scenes/' + assets[i].asset_type + mycode + '/' + assets[i].asset_name + '/master/' + shotInfo[0] + '_' + assets[i].asset_name + gpuKey + '[hml]_ms_' + myFileType + re.escape(fileFormat) + '$'
            if assets[i].asset_sep != '':
                assetNeed = projAssetBasePath + 'scenes/' + assets[i].asset_type + mycode + '/' + assets[i].asset_name + '/master/' + shotInfo[0] + '_' + assets[i].asset_name + '_' + assets[i].asset_sep +  gpuKey + 'h_ms_' + myFileType + re.escape(fileFormat) + '$'
                pattern = '^' + projAssetBasePath + 'scenes/' + assets[i].asset_type + mycode + '/' + assets[i].asset_name + '/master/' + shotInfo[0] + '_' + assets[i].asset_name + '_' + assets[i].asset_sep + gpuKey + '[hml]_ms_' + myFileType + re.escape(fileFormat) + '$'
            checkRef = 0
            for refPath in refLowerPaths:
                if printMode:print '-----------------------------LostTest'
                if printMode:print pattern
                if printMode:print refPath
                if re.search(pattern, refPath, re.IGNORECASE) != None:
                    checkRef = 1
                    if printMode:print checkRef
                    break
                if printMode:print checkRef
            if checkRef == 0 and assets[i].asset_name[0]!='m':
                assetLostID.append(assets[i].asset_name)
                assetLostPath.append(assetNeed)

        # 多余的参考     
        assetMorePath = []
        for j in range(len(refLowerPaths)):
            refPath = refLowerPaths[j]
            checkRef = 0
            for i in range(len(assets)):
                mycode = ''
                if anim.projectName in ['YODA','Ninjago','Xyj']:
                    mycode = '/' + assets[i].code
                myFileType = fileType
                if anim.projectName in ['YODA','Ninjago','Xyj'] and assets[i].asset_type == 'sets':
                    myFileType = 'tex'
                if anim.projectName in ['MiniTiger'] and assets[i].asset_type == 'sets':#=====add by zhangben 2016.3.7
                    myFileType = u'(gpu|%s)'%fileType
                gpuKey = '_'
                if assets[i].asset_type == 'sets':
                    gpuKey = '(_|_GPU_)'
                pattern = '^' + projAssetBasePath + 'scenes/' + assets[i].asset_type + mycode + '/' + assets[i].asset_name + '/master/' + shotInfo[0] + '_' + assets[i].asset_name + gpuKey + '[hml]_ms_' + myFileType + re.escape(fileFormat) + '$'
                if assets[i].asset_sep != '':
                    pattern = '^' + projAssetBasePath + 'scenes/' + assets[i].asset_type + mycode + '/' + assets[i].asset_name + '/master/' + shotInfo[0] + '_' + assets[i].asset_name + '_' + assets[i].asset_sep + gpuKey + '[hml]_ms_' + myFileType + re.escape(fileFormat) + '$'
                if printMode:print '-----------------------------MoreTest'
                if printMode:print pattern
                if printMode:print refPath
                if re.search(pattern, refPath, re.IGNORECASE) != None:
                    checkRef = 1
                    if printMode:print checkRef
                    break
                if printMode:print checkRef
            if checkRef == 0:
                if noNeedKeys:
                    checkKey = 0
                    for key in noNeedKeys:
                        if key.lower() in refPaths[j].lower():
                            checkKey = 1
                    if not checkKey:
                        assetMorePath.append(refPaths[j])
                else:
                    assetMorePath.append(refPaths[j])
        #print '---------------errorList'
        #print assetLostPath
        #print assetMorePath
        if (assetLostPath + assetMorePath):
            if shotInfo[0] in ['tf']:
                # 返回消息模式
                if backType == 0:
                    return [assetLostID,assetLostPath,assetMorePath]
                # 报错模式
                if backType == 1:
                    shotCameraCheck = self.shotCameraCheck()
                    shotDisplayLayerCheck = self.shotDisplayLayerCheck()
                    shotReferenceShareNodesCheck = self.shotReferenceShareNodesCheck()
                    shotReferenceLoadCheck = self.shotReferenceLoadCheck()
                    if assetLostPath:
                        print u'\n'
                        print u'------------------------本文件中以下参考【丢失】------------------------'
                        for j in range(len(assetLostPath)):
                            print assetLostID[j]
                            print assetLostPath[j]
                        print u'------------------------本文件中以上参考【丢失】------------------------'
                        print(u'=======！！！本文件丢失参考，请加载必要且正确的参考！！！=======')
                        os.putenv('zwCalimeroCheckinReferenceErr', '-%d' % len(assetLostPath))
                        print u'\n'
                        #mc.error(u'=======！！！本文件参考不正确，请检查好再check in！！！=======')
                        #print u'\n'
                    if assetLostPath:
                        print (u'=======！！！本文件不正确，请检查好再check in！！！=======')
                        mc.error(u'')
                    print u'\n'
                    print(u'------------------------参考检测完成------------------------')
                    print u'\n'
            else:
                # 返回消息模式
                if backType == 0:
                    return [assetLostID,assetLostPath,assetMorePath]
                # 报错模式
                if backType == 1:
                    if assetLostPath:
                        print u'\n'
                        errorInfo = sk_infoCore.sk_infoCore().sk_infoCore(64)
                        print errorInfo
                        for j in range(len(assetLostPath)):
                            print assetLostID[j]
                            print assetLostPath[j]
                            errorList.append(u'[Lost Asset|对比缺少参考] %s'%assetLostPath[j])
                    if assetMorePath:
                        print '\n'
                        errorInfo = sk_infoCore.sk_infoCore().sk_infoCore(65)
                        print errorInfo
                        for j in range(len(assetMorePath)):
                            print assetMorePath[j]
                            errorList.append(u'[More Asset|对比多余参考] %s'%assetMorePath[j])
                    print u'\n'
                    if not returnMode:
                        errorInfo = sk_infoCore.sk_infoCore().sk_infoCore(66)
                        print errorInfo
                        sk_infoConfig.errorCode = errorInfo
                        mc.error()
                    else:
                        return errorList
                
        print u'------------------------参考检测完成------------------------'
        return 0

    #-----------------------------------------------------------------------------------------------------#
    #-----------------------------------------#
    # 本地参考
    #-----------------------------------------#
    def checkLocakAssetRef(self):
        refInfo = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refPaths = refInfo[1][0]

        localPaths = []
        serverKeyList = ['//file-cluster/gdc/','z:/','l:']
        for path in refPaths:
            errorState = 0
            for checkKey in serverKeyList:
                if checkKey in path.lower():
                    errorState = 1
            if not errorState:
                localPaths.append(path)
        if localPaths:
            print '\n'
            errorInfo = sk_infoCore.sk_infoCore().sk_infoCore(66)
            print errorInfo
            for info in localPaths:
                print info
            print errorInfo
            sk_infoConfig.errorCode = errorInfo
            mc.error()

    # 非production 参考
    def checkNotServerAssetRef(self,returnMode = 0):
        refInfo = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refPaths = refInfo[1][0]
        projServerBase =sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        errorPath = []
        ZPre = '//file-cluster/gdc'
        for path in refPaths:
            if projServerBase.lower() not in path.lower():
                if ZPre in projServerBase.lower():
                    checkState = 0
                    for checkPre in ['z:','l:']:
                        newPathBase = projServerBase.lower().replace(ZPre,checkPre)
                        if newPathBase.lower() not in path.lower():
                            checkState += 1
                    if checkState == 2:
                        errorPath.append(path)
                else:
                    if 'l:' not in projServerBase.lower():
                        errorPath.append(path)
            if '/history/' in path.lower():
                errorPath.append(path)
        if errorPath:
            if not returnMode:
                print '\n'
                errorInfo = sk_infoCore.sk_infoCore().sk_infoCore(66)
                print errorInfo
                for info in errorPath:
                    print info
                print errorInfo
                sk_infoConfig.errorCode = errorInfo
                mc.error()
            else:
                errorInfos = []
                for errorPath in errorPath:
                    errorInfos.append(u'[Server Error|不是合法Server路径] %s'%errorPath)
                return errorInfos
        else:
            return []

    #----------------------------------------#
    #从指定渲染层获取物体
    def shotGrpsFromNorenderL(self,norenderL = ['norender','VFX_REF']):
        disLayerGrps = []
        for checkL in norenderL:
            if not mc.ls(checkL,type = 'displayLayer'):
                continue
            tempGrps = mc.editDisplayLayerMembers(checkL,fullNames = 1,q=1)
            if not tempGrps:
                tempGrps = []
            disLayerGrps += tempGrps
        return disLayerGrps

    #-----------------------------------------------------------------------------------------------------#
    #-----------------------------------------#
    # 文件Asset shader检测
    #-----------------------------------------#
    def shotAssetShaderCheck(self,returnMode = 0):
        localSGNodes = []
        # norender豁免
        disLayerGrps = self.shotGrpsFromNorenderL()
        noRMeshes = []
        for checkNode in disLayerGrps:
            checkType = mc.nodeType(checkNode)
            if checkType in ['mesh']:
                noRMeshes.append(checkNode)
            if checkType in ['transform']:
                mesh = mc.listRelatives(checkNode,s=1,ni=1,type = 'mesh',f=1)
                if mesh:
                    noRMeshes.append(mesh[0])
        # SG过滤
        sgNodes = mc.ls(type = 'shadingEngine')
        checkRenderAttrs = ['surfaceShader','volumeShader','displacementShader','aiSurfaceShader','aiVolumeShader','miMaterialShader']
        for checkNode in sgNodes:
            if checkNode in ['initialShadingGroup','initialParticleSE']:
                continue
            inr = mc.referenceQuery(checkNode,inr=1)
            if not inr:
                localSGNodes.append(checkNode)
            else:
                inrState = 0
                for checkAttr in checkRenderAttrs:
                    objAttr = '%s.%s'%(checkNode,checkAttr)
                    if not mc.ls(objAttr):
                        continue
                    sourceNode = mc.listConnections(objAttr,s=1,d=0)
                    if not sourceNode:
                        continue
                    inr = mc.referenceQuery(sourceNode[0],inr=1)
                    if not inr:
                        inrState = 1
                if inrState:
                    localSGNodes.append(checkNode)
        errorMeshes = []
        errorSgList = []
        for checkSg in  localSGNodes:
            sgMeshes = mc.sets(checkSg,q=1)
            if not sgMeshes:
                continue
            sgMeshes = mc.ls(sgMeshes,l=1)
            for checkMesh in sgMeshes:
                inr = mc.referenceQuery(checkMesh,inr = 1)
                if not inr:
                    continue
                if checkMesh in noRMeshes:
                    continue
                if ':%s|'%sk_infoConfig.sk_infoConfig().renderGrp not in checkMesh:
                    continue
                if '|CHR_GRP|' in checkMesh:
                    continue
                if '|PRP_GRP|' in checkMesh:
                    continue
                errorMeshes.append(u'[Error LocalShader|本地贴图物体] %s'%checkMesh)
                errorSgList.append(u'[Error LocalShader|本地贴图材质] %s'%checkSg)
        if returnMode:
            return (errorMeshes+errorSgList)

    #-----------------------------------------------------------------------------------------------------#
    #-----------------------------------------#
    # 文件Asset 贴图检测 assetMode 1:assetMode ; 0:an,ly ; -1:lr
    #-----------------------------------------#
    def shotAssetTextureCheck(self,assetMode = 0,returnMode = 0,printMode = 0,cacheChek = 0):
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        norenderL = ['norender','VFX_REF']
        nodeDict = {'file':'.fileTextureName','aiImage':'.filename','aiStandIn':'.dso'}

        if shotInfo[0] in ['Yak']:
            nodeDict = {'file':'.fileTextureName','aiImage':'.filename'}

        if cacheChek:
            nodeDict['AlembicNode'] = '.abc_File'
            nodeDict['cacheFile'] = '.cachePath'
        fileNodes = []
        for nodeType in nodeDict.keys():
            fileNodes += mc.ls(type = nodeType)
        if not fileNodes:
            return []
        errorNodes = []
        errorPaths = []
        errorList = []
        projServerPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath(checkMode = 1)
        import os
        # 豁免清单
        disLayerGrps = self.shotGrpsFromNorenderL()
        noRMeshes = []
        for checkNode in disLayerGrps:
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
            # 检测信息
            baseKey = '/project/sourceimages/'
            if checkType in ['aiStandIn','AlembicNode','cacheFile']:
                baseKey = '/project/data/'
            # 获取贴图路径
            imagePath = mc.getAttr(keyAttr,x=1)
            if imagePath in [''] and mc.ls(fileNode + '.' + extraAttr):
                imagePath = mc.getAttr(fileNode + '.' + extraAttr)
            if assetMode:
                imagePath = mc.workspace(expandName = imagePath)
            # 获取绝对路径
            if imagePath:
                realPath = self.checkRealPath(imagePath)
            else:
                realPath = ''
            if skipKey in realPath:
                continue
            if os.path.exists(realPath):
                if (fileNode not in errorNodes):
                    if projServerPath.lower() not in realPath.lower():
                        if printMode:print '-----0\n%s'%fileNode
                        errorNodes.append(fileNode)
                        errorPaths.append(imagePath)
                    if baseKey not in imagePath.lower():
                        if printMode:print '-----1\n%s'%fileNode
                        errorNodes.append(fileNode)
                        errorPaths.append(imagePath)
            else:
                # 是否参考模式
                refState = mc.referenceQuery(fileNode,inr = 1)
                if not refState and assetMode in [0,1]:
                    # 是否所有物体都在norender层
                    noRenderState = self.shotFileNorenderCheck(fileNode,noRMeshes)
                    if noRenderState and (fileNode not in errorNodes):
                        if printMode:print '-----2\n%s'%fileNode
                        errorNodes.append(fileNode)
                        errorPaths.append(u'%s\n使用上面贴图的物体有不在norender层的'%imagePath)
                    continue
                else:
                    if (fileNode not in errorNodes):
                        if printMode:print '-----3\n%s'%fileNode
                        errorNodes.append(fileNode)
                        errorPaths.append(imagePath)
        if errorPaths:
            errorInfo = sk_infoCore.sk_infoCore().sk_infoCore(67)
            if not returnMode:
                print errorInfo
            for i in range(len(errorPaths)):
                if not returnMode:
                    print errorNodes[i]
                    print errorPaths[i]
                else:
                    errorList.append(u'[Error TexNode|有问题的贴图] %s'%errorNodes[i])
                    errorList.append(u'[Error TexPath|相关贴图路径] %s'%errorPaths[i])
            if not returnMode:
                print errorInfo
                errorInfo = sk_infoCore.sk_infoCore().sk_infoCore(68)
                print(errorInfo)
                mc.error()
            else:
                return errorList
        return []

    #------------------------------#
    # 配套修正相对路径，环境变量为绝对路径
    def checkRealPath(self,checkPath):
        realPath = checkPath
        envKey = '${IDMT_PROJECTS}'
        if envKey in realPath:
            realPath = realPath.replace(envKey,'z:/Projects')
        for checkKey in self.serverPreKey:
            if checkKey in realPath:
                realPath = realPath.replace(checkKey,'//file-cluster/GDC')
        return realPath

    #------------------------------#
    # 查询file节点的物体是否都在norender层
    def shotFileNorenderCheck(self,checkFileNode,noRMeshes):
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
        checkState = len(sgMeshes)
        for checkMesh in sgMeshes:
            if checkMesh in noRMeshes:
                checkState -= 1
        # 只要有一个不在norender里，就需要报错
        return checkState

    #-----------------------------------------------------------------------------------------------------#
    #-----------------------------------------#
    # 文件相机检测，命名规则为cam_ep_sc
    #-----------------------------------------#
    def shotCameraCheck(self):
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        shotType = sk_infoConfig.sk_infoConfig().checkShotType()
        camSourceName = 'cam_' + str(shotInfo[1]) + '_' + str(shotInfo[2])
        if shotType == 3:
            camSourceName += '_' + str(shotInfo[3])
        camList = mc.ls(camSourceName,l=1,type= 'transform')
        needCam = []
        for cam in camList:
            shape = mc.listRelatives(cam,f=1,s=1,ni=1,type = 'camera')
            if shape:
                needCam = [cam]
                mc.rename(shape[0],camSourceName+'Shape')
        return needCam

    #-----------------------------------------------------------------------------------------------------#
    #-----------------------------------------#
    # 文件显示层检测，命名规则为唯一隐藏层为norender,其他层不能隐藏且名字不能以layer为名 OK
    #-----------------------------------------#
    def shotDisplayLayerCheck(self,returnMode = 1,deleteMode = 0):
        Nlayer=[]
        Dlayer=[]
        # norender统一继承
        nrLayer = 'norender'
        keepList = ['norender','near','mid','far','defaultLayer']
        skipList = ['near','mid','far']
        from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools
        reload(sk_sceneTools)
        sk_sceneTools.sk_sceneTools().checkHideObjs2Norender(nrLayer,skipList)
        #displayLayers = mc.listConnections('layerManager.displayLayerId')
        displayLayers = mc.ls(type = 'displayLayer')
        for layer in displayLayers:
            checkType = mc.nodeType(layer)
            if checkType not in ['displayLayer']:
                continue
            inr = mc.referenceQuery(layer,inr=1)
            if inr:
                continue
            if layer in keepList:
                continue
            mc.setAttr(layer + '.displayType',0)
            displayVisibility = mc.getAttr(layer + '.visibility')
            if not displayVisibility :
                if layer.lower() not in keepList and layer.lower() != "pv":
                    Nlayer.append(u'[more displayL|多余显示层] %s'%layer)
            else:
                if re.compile(r'^layer[0-9]', re.IGNORECASE).search(layer) != None:
                    Dlayer.append(u'[more displayL|多余显示层] %s'%layer)
        print '--------s'
        print Nlayer
        print Dlayer
        if Nlayer or Dlayer :
            if returnMode:
                return Nlayer+Dlayer
            else:
                if deleteMode:
                    for checkLayer in (Nlayer+Dlayer):
                        if '] ' in checkLayer:
                            checkLayer = checkLayer.split('] ')[-1]
                        if mc.ls(checkLayer):
                            mc.lockNode(checkLayer,l=0)
                            mc.delete(checkLayer)
                else:
                    mc.error(u'=======！！！本文件显示层命名有问题！！！=======')

    #-----------------------------------------------------------------------------------------------------#
    #-----------------------------------------#
    # 非参考物体(norender显示层的物体不被检测)
    #-----------------------------------------#
    def shotNoRefNodesCheck(self):
        noRefMeshes = []
        # 获取显示层物体
        disLayerGrps = self.shotGrpsFromNorenderL()
        # 检测
        checkMeshes = mc.ls(type = 'mesh',l=1)
        for checkMesh in checkMeshes:
            isRef = mc.referenceQuery(checkMesh,inr = 1)
            if isRef:
                continue
            checkGrp = mc.listRelatives(checkMesh,p=1,f=1)[0]
            if mc.nodeType(checkGrp) in ['fosterParent']:
                continue
            if '|goldLine_Grp|' in checkGrp:
                continue
            if not disLayerGrps:
                noRefMeshes.append(u'[Not Ref|非参考] %s'%checkGrp)
            else:
                norenderState = 0
                for checkRoot in disLayerGrps:
                    if checkRoot in checkGrp and checkGrp.split(checkRoot)[0] in ['']:
                        norenderState = 1
                        break
                if norenderState:
                    continue
                else:
                    noRefMeshes.append(u'[Not Ref|非参考] %s'%checkGrp)
        return [noRefMeshes,disLayerGrps]

    #-----------------------------------------------#
    # 场景referenceEdit check
    def shotRefEditCheck(self,returnMode = 1):
        errorObjs = []
        refNodes = mc.ls(type='reference')
        modifyInfos = []
        for refNode in refNodes:
            # 排除无用的和不符合条件的
            if '_' not in refNode:
                continue
            refPath = ''
            try:
                refPath = mc.referenceQuery(refNode,filename=1)
            except:
                pass
            if not refPath:
                continue
            checkInfos = refNode.split('_')
            if checkInfos[1][0] not in ['s','S']:
                continue
            # 获取
            checkTypes = ['connectAttr']
            for checkType in checkTypes:
                modifyInfos += mc.referenceQuery( refNode ,failedEdits = 0 , successfulEdits = 1 ,editCommand = checkType , editStrings = 1)
        # 处理
        for checkInfo in modifyInfos:
            errorState = 0
            if 'connectAttr' in checkInfo and ('"modelPanel' in checkInfo and 'ViewSelectedSet.d' in checkInfo):
                errorState = 1
            if errorState:
                errorObj = checkInfo.split('"')[1]
                if '.' in errorObj:
                    errorObj = errorObj.split('.')[0]
                errorObjs.append(u'[Ref Broken|参考被破坏请重建] %s'%errorObj)
        if returnMode:
            return errorObjs
        else:
            if errorObjs:
                errorInfo = u'-----Error Reference Edit Obj!|所列物体所在参考被改坏,请重新备份旧动画、创建新参考移植'
                print errorInfo
                for checkObj in errorObjs:
                    print checkObj
                print errorInfo
                mc.error()

    #-------------------------------------------------------------------------------------
    #-------------文件参考是否使用shareNodes方式检测----------------------------
    #-------------------------------------------------------------------------------------
    def shotReferenceShareNodesCheck(self) :
        wrongReference=[]
        referenceFiles = mc.file(q=1,r=1)
        for rf in referenceFiles :
            shareNodes = mc.file(rf,q=1,shd=1);
            if shareNodes :
                wrongReference.append(rf)
        if wrongReference :
            return wrongReference

    #-------------------------------------------------------------------------------------
    #-------------文件参考是否加载检测----------------------------
    #-------------------------------------------------------------------------------------
    def shotReferenceLoadCheck(self) :
        wrongReference=[]
        referenceFiles = mc.file(q=1,r=1)
        for rf in referenceFiles :
            referenceLoad = mc.referenceQuery(rf,il=1)
            if not referenceLoad :
                wrongReference.append(u'[NoLoad Ref|未加载参考] %s'%rf)
        if wrongReference :
            return wrongReference

    # 隐藏的物体检测
    def checkHideObj(self):
        transNodes = mc.ls(type = 'transform',l=1)
        hideObjs = []
        for checkNode in transNodes:
            inr = mc.referenceQuery(checkNode,inr=1)
            if not inr:
                continue
            if ':%s|'%(sk_infoConfig.sk_infoConfig().renderGrp) not in checkNode:
                continue
            if not mc.getAttr(checkNode+'.v'):
                hideObjs.append(checkNode)
        return hideObjs

    # 获取list
    def steCamesGetShotCamList(self,shotInfos = []):
        if not shotInfos:
            shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
        camInfos = sk_infoConfig.sk_infoConfig().checkReadShotCamData(shotInfos)
        if not camInfos:
            camList = ['base']
        else:
            camList = camInfos.split(';')
        return camList

