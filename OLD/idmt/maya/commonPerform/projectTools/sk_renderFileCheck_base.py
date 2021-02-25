# -*- coding: utf-8 -*-
# 【通用】【mi项目工具】
#  Author : 沈康
#  Data   : 2016

import maya.cmds as mc
import maya.mel as mel
from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
reload(sk_infoConfig)

class sk_renderFileCheck_base(object):
    def __init__(self):
        pass

    def checkPerform(self,returnMode = 1,printMode = 0):
        fileNameNow = mc.file(exn=1,q=1).split('/')[-1]
        # 开始处理
        from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools
        reload(sk_sceneTools)
        from idmt.maya.commonCore.core_mayaCommon import sk_animFileCheck
        reload(sk_animFileCheck)

        shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()

        errorInfoList = []

        rgbFile = 0
        if 'RGB_' in fileNameNow:
            rgbFile = 1

        # FPS
        errorList = sk_sceneTools.sk_sceneTools().sk_sceneImportFrame(
            'FPS', checkMode=1, returnMode=returnMode)
        if errorList:
            errorInfoList = errorInfoList + errorList

        # 检测非server参考
        errorList = sk_animFileCheck.sk_animFileCheck().checkNotServerAssetRef(
            returnMode=returnMode)
        if errorList:
            errorInfoList = errorInfoList + errorList

        # 贴图检测
        if not rgbFile:
            errorList = sk_animFileCheck.sk_animFileCheck().shotAssetTextureCheck(assetMode = -1 ,returnMode = returnMode,printMode = printMode)
            if errorList:
                errorInfoList = errorInfoList + errorList

        # cameras
        cameraNodes = mc.ls(type = 'camera')
        renderNum = 0
        for checkCam in cameraNodes:
            if mc.getAttr(checkCam+'.renderable'):
                renderNum += 1
        if renderNum == 0:
            errorInfoList += [u'------ No Camera to Render !!!']
            errorInfoList += [u'------ 没有相机用于渲染 !!!']
        maxCamNum = 1

        # 定制检测
        if shotInfos[0] in ['mi']:
            maxCamNum = 2

            # AssetList
            #errorList = sk_animFileCheck.sk_animFileCheck().shotAssetRefCheck(
            #    'lr', 1, returnMode=returnMode)
            #if errorList:
            #    errorInfoList = errorInfoList + errorList

            # RenderLayer数量
            '''
            needRenderLayers = []
            rLayers = mc.ls(type = 'renderLayer')
            for checkLayer in rLayers:
                inr = mc.referenceQuery(checkLayer,inr = 1)
                if inr:
                    continue
                if 'defaultRenderLayer' in checkLayer:
                    mc.setAttr(checkLayer+'.renderable',0)
                    continue
                needRenderLayers.append(checkLayer)
            if len(needRenderLayers) > 4:
                errorInfoList += [u'------RenderLayer Numbers > 4 !!!']
            '''

            # 参数

            attrList = ['AASamples','GIDiffuseSamples','GIGlossySamples','GIRefractionSamples',
                        'GISssSamples','GIVolumeSamples','GIDiffuseDepth']
            for checkAttr in attrList:
                maxValue = 16
                if shotInfos[1] in ['200'] and shotInfos[2] in ['0520']:
                    maxValue = 16
                needAttr = 'defaultArnoldRenderOptions.'+checkAttr
                if not mc.ls(needAttr):
                    continue
                value = mc.getAttr(needAttr)
                if value > maxValue:
                    errorInfoList += [u'------%s > %s | now: [%s]!!!'%(checkAttr,maxValue,value)]

            checkAttr = 'defaultArnoldRenderOptions.use_existing_tiled_textures'
            if mc.ls(checkAttr) and not mc.getAttr(checkAttr):
                errorInfoList += [u'------%s is off !!!'%checkAttr]
                errorInfoList += [u'------[Arnold渲染参数.tx关闭了]%s!!!'%checkAttr]

        if renderNum > maxCamNum:
            errorInfoList += [u'------ Too Many Cameras to Render !!!']
            errorInfoList += [u'------ 太多相机开启了render选项 !!!']

        if errorInfoList:
            errorInfo = u'\n--------请处理好这些错误--------'
            print errorInfo
            for errorLine in errorInfoList:
                print errorLine
            errorInfo = u'--------请处理好这些错误--------\n'
            print errorInfo
            mc.error()

        if shotInfos[0] in ['mi']:
            # 文件名
            filePre = '<RenderLayer>/<RenderPass>/<Scene>_<RenderLayer>_<RenderPass>'
            mc.setAttr('defaultRenderGlobals.imageFilePrefix',filePre,type= 'string')

            # 参数
            mc.setAttr('defaultRenderGlobals.animation', 1)
            mc.setAttr('defaultRenderGlobals.putFrameBeforeExt', 1)
            mc.setAttr('defaultRenderGlobals.periodInExt', 1)
            mc.setAttr('defaultRenderGlobals.extensionPadding', 4)

            mc.setAttr('defaultArnoldDriver.aiTranslator','exr',type = 'string')
            mc.setAttr('defaultArnoldDriver.exrCompression',2)

            mc.setAttr('defaultResolution.width', 2048)
            mc.setAttr('defaultResolution.height', 858)
            mc.setAttr('defaultResolution.deviceAspectRatio', 2.387)
            mc.setAttr('defaultResolution.pixelAspect', 1)

            yetiPath = 'Z:\\Resource\\Development\\Maya\\GDC\\3partPlugin\\2014\\Yeti1.3.5Maya2014\\bin'
            mc.setAttr('defaultArnoldRenderOptions.procedural_searchpath',yetiPath,type='string')

        print u'\n------------Sucess Check Done------------\n'

    #----------------#
    # 检测灯光文件非法路径
    def checkRenderFileImagePath(self,shotInfos = [],baseData = {}):
        checkNodes = mc.ls(type='file') + mc.ls(type='aiImage') + mc.ls(type = 'aiStandIn')
        projFolder = sk_infoConfig.sk_infoConfig().checkProjectServerPath(dirInfo = shotInfos)
        projBase = projFolder.split('/Projects/')[-1]
        dataFolder = sk_infoConfig.sk_infoConfig().checkShotDataInfoPath(server=1,infoMode=2.5,shotInfos=shotInfos)
        dataBase = dataFolder.split('/Projects/')[-1].split('/data/')[0]
        sourceImageKey = ('%ssourceimages'%projBase).lower()
        lightFolderKey = ('%s/data/lighting'%dataBase).lower()
        dsoFolderKey = ('%s/data/ArnoldStandIn'%dataBase).lower()
        fxFolderKey = ('%s/data/FxCache'%dataBase).lower()
        errorNodes = baseData
        for checkNode in checkNodes:
            checkType = mc.nodeType(checkNode)
            keyAttr = '.fileTextureName'
            if checkType in ['aiImage']:
                keyAttr = '.filename'
            if checkType in ['aiStandIn']:
                keyAttr = '.dso'
            imgPath = mc.getAttr(checkNode+keyAttr)
            realPath = mc.workspace(expandName = imgPath)
            realCheckPath = realPath.lower()
            checkState = 0
            if checkType in ['file','aiImage']:
                if sourceImageKey in realCheckPath:
                    checkState = 1
                if lightFolderKey in realCheckPath:
                    checkState = 1
                if fxFolderKey in realCheckPath:
                    checkState = 1
            if checkType in ['aiStandIn']:
                if dsoFolderKey in realCheckPath:
                    checkState = 1
            if '_scratch' in realCheckPath:
                checkState = 0
            if not checkState:
                if checkNode not in errorNodes.keys():
                    errorNodes[checkNode] = realPath
        return errorNodes
