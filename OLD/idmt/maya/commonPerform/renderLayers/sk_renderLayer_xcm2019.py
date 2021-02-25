# -*- coding: utf-8 -*-
# 【通用】【xcm2019项目】
#  Author : 沈康
#  Data   : 2018

#-----------------------------------------#
# idp 分 角色/道具/场景 和 asset自身的idp
#-------角色/道具/场景的需要额外处理
# 如 aovCPRGBCreate()
#-------asset自身的idp
# set组明名: namespace:aiMsk_idpName_TypeRGB
# 如:mi_c002002Teethless_h:aiMsk_TL_CHRR

import maya.cmds as mc
import maya.mel as mel
import time
from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
reload(sk_infoConfig)

class sk_renderLayer_xcm2019(object):

    def __init__(self):
        self.dataBase = u'Y:/XCM_2019DY/XCM_2019DY_交换空间'
        self.lightDataPath = self.dataBase + '/Lighting'
        self.projStyle = 2
        self.exportRoot = 'D:/xcmRLFiles'
        self.matteShader = 'sk_matteShader'
        self.emptyLayer = ''
        self.emptyLayer2 = ''

    def baseSettings(self,renderer = 'ar',format = ''):
        mc.setAttr('defaultRenderLayer.renderable',0)
        if renderer in ['ar']:
            if not mc.pluginInfo('mtoa.mll',q=1,loaded = 1):
                mc.loadPlugin('mtoa.mll')
            import mtoa
            mtoa.core.createOptions()
            import mtoa.cmds.registerArnoldRenderer
            mtoa.cmds.registerArnoldRenderer.registerArnoldRenderer()
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'arnold', type='string')
            mc.setAttr('defaultArnoldRenderOptions.autotx',0)
        if renderer in ['sw']:
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'mayaSoftware', type='string')
        # 标准设置
        mc.setAttr('defaultRenderGlobals.imageFormat', 7)
        mc.setAttr('defaultRenderQuality.edgeAntiAliasing', 1)
        mc.setAttr('defaultRenderGlobals.animation', 1)
        mc.setAttr('defaultRenderGlobals.outFormatControl', 0)
        mc.setAttr('defaultRenderGlobals.extensionPadding', 4)
        mc.setAttr('defaultRenderGlobals.imageFilePrefix','<Camera>/<RenderLayer>/<Scene>_<RenderLayer>',type = 'string')
        mc.setAttr('defaultResolution.deviceAspectRatio', 2.387)
        mc.setAttr('defaultResolution.pixelAspect', 1.00)
        mc.evalDeferred('import maya.cmds as mc;mc.setAttr((\'defaultResolution.pixelAspect\'),1)', lowestPriority=1)
        mc.setAttr('defaultResolution.dotsPerInch', 72)
        mc.setAttr('defaultRenderQuality.edgeAntiAliasing', 1)

        if renderer in ['ar']:
            mc.setAttr('defaultArnoldDriver.halfPrecision', 0)
            if not format:
                mc.setAttr('defaultArnoldDriver.aiTranslator','exr',type='string')
                mc.setAttr('defaultArnoldDriver.exrCompression',3)
            else:
                mc.setAttr('defaultArnoldDriver.aiTranslator',format,type='string')
            mc.setAttr('defaultArnoldDriver.tiffCompression',0)
            mc.setAttr('defaultArnoldRenderOptions.lock_sampling_noise', 0)
            mc.setAttr('defaultArnoldDriver.mergeAOVs',1)
            mc.setAttr('defaultArnoldRenderOptions.indirectSampleClamp',1.5)
            mc.setAttr('defaultArnoldFilter.width', 2)
        if renderer in ['sw']:
            mc.setAttr('defaultRenderGlobals.imageFormat', 4)
            mc.setAttr('defaultRenderGlobals.imageFilePrefix','<RenderLayer>/<Scene>_<RenderLayer>',type = 'string')
            # software产品级
            mc.setAttr(('defaultRenderQuality' + '.edgeAntiAliasing'),0)
            mc.setAttr(('defaultRenderQuality' + '.useMultiPixelFilter'),1)
            mc.setAttr(('defaultRenderQuality' + '.shadingSamples'),2)
            mc.setAttr(('defaultRenderQuality' + '.maxShadingSamples'),8)
            mc.setAttr(('defaultRenderQuality' + '.visibilitySamples'),1)
            mc.setAttr(('defaultRenderQuality' + '.maxVisibilitySamples'),4)
            mc.setAttr(('defaultRenderQuality' + '.redThreshold'),0.4)
            mc.setAttr(('defaultRenderQuality' + '.greenThreshold'),0.3)
            mc.setAttr(('defaultRenderQuality' + '.blueThreshold'),0.6)
            mc.setAttr(('defaultRenderQuality' + '.reflections'),10)
            mc.setAttr(('defaultRenderQuality' + '.refractions'),10)
            mc.setAttr(('defaultRenderQuality' + '.shadows'),10)

        from idmt.maya.commonCore.core_renderLayer import sk_renderLayerCore
        reload(sk_renderLayerCore)
        '''
        # 修正相机namespace
        from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools
        reload(sk_sceneTools)
        sk_sceneTools.sk_sceneTools().sk_sceneAssetNamespaceConfig(projStyle = self.projStyle)
        sk_renderLayerCore.sk_renderLayerCore().camRefFix()
        '''

        # 开始处理
        shotID = sk_infoConfig.sk_infoConfig().checkShotID()
        import idmt.pipeline.db
        anim = idmt.pipeline.db.GetAnimByFilename(shotID)
        startFrame = anim.frmStart
        endFrame = anim.frmEnd
        fpsFrame = anim.fps
        resW = anim.resolutionW
        resH = anim.resolutionH
        # res
        mc.setAttr('defaultResolution.width', resW)
        mc.setAttr('defaultResolution.height', resH)
        # FPS
        if fpsFrame == 25:
            mc.currentUnit(time='pal')
        if fpsFrame == 24:
            mc.currentUnit(time='film')
        if fpsFrame == 30:
            mc.currentUnit(time='ntsc')
        # frame
        if startFrame and fpsFrame:
            # 起始帧
            mc.playbackOptions(min=startFrame)
            # 起始预留
            preStartFrame = startFrame - 10
            mc.playbackOptions(animationStartTime=preStartFrame)
            # 结束帧
            mc.playbackOptions(max=endFrame)
            # 结束预留
            posEndFrame = endFrame + 10
            mc.playbackOptions(animationEndTime=posEndFrame)
            # 渲染范围设置
            mc.setAttr('defaultRenderGlobals.startFrame', startFrame)
            mc.setAttr('defaultRenderGlobals.endFrame', endFrame)

        # 格式命名
        # 原先调用菜单，现在直接改节点
        mc.setAttr('defaultRenderGlobals.animation', 1)
        mc.setAttr('defaultRenderGlobals.putFrameBeforeExt', 1)
        mc.setAttr('defaultRenderGlobals.periodInExt', 1)
        mc.setAttr('defaultRenderGlobals.extensionPadding', 4)
        if mc.getAttr('defaultRenderGlobals.outFormatControl') == 1:
            mc.setAttr('defaultRenderGlobals.outFormatControl', 0)

        # camera
        cameras = mc.ls(type = 'camera',l=1)
        for camShape in cameras:
            mc.setAttr((camShape + '.renderable'),0)
            if 'CenterCamShape' in camShape:
                mc.setAttr(camShape + '.farClipPlane',1000000)
        renderCams = mc.ls('CAM:*',type = 'camera')
        for checkShape in renderCams:
            if mc.nodeType(checkShape) in ['camera']:
                mc.setAttr('%s.renderable'%checkShape,1)

        # 所有mel关闭
        mc.setAttr('defaultRenderGlobals.preMel','',type='string')
        mc.setAttr('defaultRenderGlobals.postMel','',type='string')

        # yeti config
        if mc.ls(type = 'pgYetiMaya'):
            if renderer in ['ar']:
                yetiPath = 'C:\\tools\LocalTools\\3partPlugin\\2017\Yeti\\2.2.1\\bin'
                mc.setAttr('defaultArnoldRenderOptions.procedural_searchpath',yetiPath,type='string')
            # yetiPremel
            fixAttr = 'defaultRenderGlobals.preMel'
            preMel = mc.getAttr(fixAttr)
            preKey = 'pgYetiPreRender'
            if preKey not in preMel:
                if preMel:
                    if ';' in preMel[-1]:
                        newInfo = preMel + preKey
                    else:
                        newInfo = preMel + ';' + preKey
                else:
                    newInfo = preKey
                mc.setAttr(fixAttr,newInfo,type = 'string')

        # 更新信息
        sk_renderLayerCore.sk_renderLayerCore().blendShapeUpdateInfo()
        # 处理smooth
        from idmt.maya.commonCore.core_mayaCommon import sk_smoothSet
        reload(sk_smoothSet)
        sk_smoothSet.sk_smoothSet().smoothSetDoSmooth(disModify = 0,projStyle = 2)

    # sky 分为分层
    def skyFix(self,renderer = 'ar'):
        # 加载相机
        from idmt.maya.commonCore.core_mayaCommon import sk_hbExportCam
        reload(sk_hbExportCam);
        sk_hbExportCam.sk_hbExportCam().camServerReference()
        # 标准设置
        mc.setAttr('defaultRenderQuality.edgeAntiAliasing', 1)
        mc.setAttr('defaultRenderGlobals.animation', 1)
        mc.setAttr('defaultRenderGlobals.outFormatControl', 0)
        mc.setAttr('defaultRenderGlobals.extensionPadding', 4)
        mc.setAttr('defaultRenderGlobals.imageFilePrefix','<RenderLayer>_<RenderPass>/<Scene>_<RenderLayer>_<RenderPass>',type = 'string')
        mc.setAttr('defaultResolution.deviceAspectRatio', 2.387)
        mc.setAttr('defaultResolution.pixelAspect', 1.00)
        mc.evalDeferred('import maya.cmds as mc;mc.setAttr((\'defaultResolution.pixelAspect\'),1)', lowestPriority=1)
        mc.setAttr('defaultResolution.dotsPerInch', 72)
        mc.setAttr('defaultRenderQuality.edgeAntiAliasing', 1)

        # 开始处理
        from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
        reload(sk_infoConfig)
        shotID = sk_infoConfig.sk_infoConfig().checkShotID()
        import idmt.pipeline.db
        anim = idmt.pipeline.db.GetAnimByFilename(shotID)
        startFrame = anim.frmStart
        endFrame = anim.frmEnd
        fpsFrame = anim.fps
        resW = anim.resolutionW
        resH = anim.resolutionH
        # res
        mc.setAttr('defaultResolution.width', resW)
        mc.setAttr('defaultResolution.height', resH)
        # FPS
        if fpsFrame == 25:
            mc.currentUnit(time='pal')
        if fpsFrame == 24:
            mc.currentUnit(time='film')
        if fpsFrame == 30:
            mc.currentUnit(time='ntsc')
        # frame
        if startFrame and fpsFrame:
            # 起始帧
            mc.playbackOptions(min=startFrame)
            # 起始预留
            preStartFrame = startFrame - 10
            mc.playbackOptions(animationStartTime=preStartFrame)
            # 结束帧
            mc.playbackOptions(max=endFrame)
            # 结束预留
            posEndFrame = endFrame + 10
            mc.playbackOptions(animationEndTime=posEndFrame)
            # 渲染范围设置
            mc.setAttr('defaultRenderGlobals.startFrame', startFrame)
            mc.setAttr('defaultRenderGlobals.endFrame', endFrame)

        # 格式命名
        # 原先调用菜单，现在直接改节点
        mc.setAttr('defaultRenderGlobals.animation', 1)
        mc.setAttr('defaultRenderGlobals.putFrameBeforeExt', 1)
        mc.setAttr('defaultRenderGlobals.periodInExt', 1)
        mc.setAttr('defaultRenderGlobals.extensionPadding', 4)
        if mc.getAttr('defaultRenderGlobals.outFormatControl') == 1:
            mc.setAttr('defaultRenderGlobals.outFormatControl', 0)

        # camera
        cameras = mc.ls(type = 'camera',l=1)
        for camShape in cameras:
            mc.setAttr((camShape + '.renderable'),0)
            if 'CenterCamShape' in camShape:
                mc.setAttr(camShape + '.farClipPlane',1000000)
        renderCams = mc.ls('CAM:*',type = 'camera')
        for checkShape in renderCams:
            if mc.nodeType(checkShape) in ['camera']:
                mc.setAttr('%s.renderable'%checkShape,1)

        # 所有mel关闭
        mc.setAttr('defaultRenderGlobals.preMel','',type='string')
        mc.setAttr('defaultRenderGlobals.postMel','',type='string')

        # yeti config
        if mc.ls(type = 'pgYetiMaya'):
            if renderer in ['ar']:
                yetiPath = 'C:\\tools\LocalTools\\3partPlugin\\2017\Yeti\\2.2.1\\bin'
                mc.setAttr('defaultArnoldRenderOptions.procedural_searchpath',yetiPath,type='string')
            # yetiPremel
            fixAttr = 'defaultRenderGlobals.preMel'
            preMel = mc.getAttr(fixAttr)
            preKey = 'pgYetiPreRender'
            if preKey not in preMel:
                if preMel:
                    if ';' in preMel[-1]:
                        newInfo = preMel + preKey
                    else:
                        newInfo = preMel + ';' + preKey
                else:
                    newInfo = preKey
                mc.setAttr(fixAttr,newInfo,type = 'string')

    # 场景模型，场景代理，场景灯光，角色模型，角色灯光，角色毛发，道具模型
    def objectList(self):
        objListDict = {}
        #-----------------------#
        # 角色模型
        chrMeshObjs = mc.listRelatives('CHR_GRP',ad=1,type='mesh',f=1)
        if chrMeshObjs:
            chrMeshObjs = mc.listRelatives(chrMeshObjs,p=1,type='transform',f=1)
            chrMeshObjs = list(set(chrMeshObjs))
        else:
            chrMeshObjs = []
        objListDict['chrMeshObjs'] = chrMeshObjs
        #-----------------------#
        # 道具模型
        prpMeshObjs = mc.listRelatives('PRP_GRP',ad=1,type='mesh',f=1)
        if prpMeshObjs:
            prpMeshObjs = mc.listRelatives(prpMeshObjs,p=1,type='transform',f=1)
            prpMeshObjs = list(set(prpMeshObjs))
        else:
            prpMeshObjs = []
        objListDict['prpMeshObjs'] = prpMeshObjs
        #-----------------------#
        # 场景模型,mesh上的grp
        setMeshObjs = mc.listRelatives('SET_GRP',ad=1,type='mesh',f=1)
        if setMeshObjs:
            setMeshObjs = mc.listRelatives(setMeshObjs,p=1,type='transform',f=1)
            setMeshObjs = list(set(setMeshObjs))
        else:
            setMeshObjs = []
        objListDict['setMeshObjs'] = setMeshObjs
        #-----------------------#
        # 场景天空组
        setAssObjs = []
        tempObjs = mc.listRelatives('SET_GRP',ad=1,type='transform',f=1)
        if tempObjs:
            for checkObj in tempObjs:
                shape = mc.listRelatives(checkObj,s=1,type = 'aiStandIn',f=1)
                if shape:
                    setAssObjs.append(checkObj)
        else:
            setAssObjs = []
        objListDict['setAssObjs'] = setAssObjs
        #-----------------------#
        # 场景代理
        setSkyObjs = []
        skyInfos = mc.ls('*:Sky',type='transform',l=1)
        if skyInfos:
            skyInfos = mc.listRelatives('*:Sky',ad=1,type='transform',f=1)
            if skyInfos:
                skyMeshes = mc.listRelatives(tempObjs,ad=1,type='mesh',f=1)
                if skyMeshes:
                    setSkyObjs = mc.listRelatives(skyMeshes,p=1,type='transform',f=1)
                else:
                    setSkyObjs = []
        objListDict['setSkyObjs'] = setSkyObjs
        #-----------------------#
        # 毛发
        furObjs = mc.ls(type = 'pgYetiMaya',l=1) \
                  + mc.ls(type = 'pfxHair',l=1) \
                  + mc.ls(type = 'shaveHair',l=1)
        chrFur = []
        prpFur = []
        setFur = []
        for checkObj in furObjs:
            objGrp = mc.listRelatives(checkObj,p=1,type='transform',f=1)[0]
            checkNs = checkObj.split('|')[-1].split(':')[0]
            if 'CH_' in checkNs:
                chrFur.append(objGrp)
            if 'PR_' in checkNs:
                prpFur.append(objGrp)
            if 'BG_' in checkNs:
                setFur.append(objGrp)
        objListDict['chrFurObjs'] = chrFur
        objListDict['prpFurObjs'] = prpFur
        objListDict['setFurObjs'] = setFur
        #-----------------------#
        # 场景地面
        floorObjs = []
        groundSets = mc.ls('*:GROUND',type = 'objectSet')
        if groundSets:
            for groundSet in groundSets:
                objs = mc.sets(groundSet,q=1)
                if not objs:
                    continue
                for obj in objs:
                    checkType = mc.nodeType(obj)
                    if checkType in ['mesh']:
                        obj = mc.listRelatives(obj,p=1,type='transform',f=1)[0]
                    if obj in floorObjs:
                        continue
                    floorObjs += [obj]
        else:
            floorObjs = []
        objListDict['setFloorObjs'] = floorObjs
        #-----------------------#
        # 角色灯光 CO
        chrLight = mc.ls('*:CHR_LIGHTING_COLOR*',type='transform',l=1)
        if not mc.ls(chrLight):
            chrLight = []
        chrLight = self.lightCheckNeed(chrLight)
        objListDict['chrLight_clr'] = chrLight

        # 角色灯光 LGT
        chrLight = mc.ls('*:CHR_LIGHTING_RGB*',type='transform',l=1)
        if not mc.ls(chrLight):
            chrLight = []
        chrLight = self.lightCheckNeed(chrLight)
        objListDict['chrLight_rgb'] = chrLight

        # CHR_CAU
        envLight = mc.ls('*:CHR_CAU')
        if not mc.ls(envLight):
            envLight = []
        envLight = self.lightCheckNeed(envLight)
        objListDict['chrLight_cau'] = envLight

        # 角色天光
        skyLight = mc.ls('*:SKY_DOME')
        if not mc.ls(skyLight):
            skyLight = []
        skyLight = self.lightCheckNeed(skyLight)
        objListDict['chrLight_sky'] = skyLight

        # CHR_FOG
        chrFogLight = mc.ls('*:CHR_FOG')
        if not mc.ls(chrFogLight):
            chrFogLight = []
        chrFogLight = self.lightCheckNeed(chrFogLight)
        objListDict['chrLight_fog'] = chrFogLight

        # CHR SHD KEY
        chrKeyLight = mc.ls('*:SUN_KEY')
        if not mc.ls(chrKeyLight):
            chrKeyLight = []
        chrKeyLight = self.lightCheckNeed(chrKeyLight)
        objListDict['chrLight_key'] = chrKeyLight

        #-----------------------#
        # 场景灯光 CO
        setLight = mc.ls('*:LIGHTS',l=1)
        if not mc.ls(setLight):
            setLight = []
        setLight = self.lightCheckNeed(setLight,checkType = 'bg')
        objListDict['setLight_clr'] = setLight

        # 场景灯光 LGT
        setLight = mc.ls('*:SET_LIGHTING_RGB')
        if not mc.ls(setLight):
            setLight = []
        setLight = self.lightCheckNeed(setLight)
        objListDict['setLight_rgb'] = setLight

        # ENV_Fog
        envLight = mc.ls('*:*ENV_FOG')
        if not mc.ls(envLight):
            envLight = []
        envLight = self.lightCheckNeed(envLight)
        objListDict['envLight_fog'] = envLight

        # ENV_CAU
        envLight = mc.ls('*:*ENV_CAU')
        if not mc.ls(envLight):
            envLight = []
        envLight = self.lightCheckNeed(envLight)
        objListDict['envLight_cau'] = envLight

        # VFX
        fishGrp = mc.ls('FX_Fish',l=1)
        objListDict['vfxObjs_fish'] = fishGrp

        dustGrp = mc.ls('FX_Dust',l=1)
        objListDict['vfxObjs_dust'] = dustGrp

        stoneGrp = mc.ls('FX_Dust',l=1)
        objListDict['vfxObjs_stone'] = stoneGrp

        return objListDict

    # blendAbc过滤
    def renderObjCheck(self,checkObjs):
        needObjs = []
        for checkObj in checkObjs:
            if '|Alembic_T_Grp|' in checkObj:
                continue
            needObjs.append(checkObj)
        return  needObjs

    # light过滤
    def lightCheckNeed(self,checkLightGrps,checkType = ''):
        lgtGrps = mc.ls(checkLightGrps,l=1)
        rootKeyList = []
        needGrps = []
        for checkGrp in lgtGrps:
            needState = 0
            if checkType in ['bg']:
                rootKeyList = '|SET_GRP|'
            for checkKey in  rootKeyList:
                if checkKey in checkGrp:
                    needState = 1
            if needState:
                needGrps.append(checkGrp)
        return needGrps

    # aov清理
    def aovClean(self):
        aovNodes = mc.ls(type= 'aiAOV')
        if aovNodes:
            mc.delete(aovNodes)

    # 导入灯光
    def lgtImport(self,lgtType='chr'):
        if lgtType in ['bg']:
            lgtType = 'set'
        basePath = self.lightDataPath
        shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()

        shotLgtPath = '%s/%s/%s'%(basePath,shotInfos[2],shotInfos[3])
        shotLgtFile = '%s_light_%s_%s.ma'%(lgtType,shotInfos[2],shotInfos[3])
        sceneLgtPath = '%s/%s'%(basePath,shotInfos[2])
        sceneLgtFile = '%s_light_%s.ma'%(lgtType,shotInfos[2])

        lgtShotFile = '%s/%s'%(shotLgtPath,shotLgtFile)
        lgtSceneFile = '%s/%s'%(sceneLgtPath,sceneLgtFile)
        lgtbaseFile = '%s/%s_light_base.ma'%(basePath,lgtType)

        needFile = ''
        loadState = 0
        import os

        # 优先读ma,后读mb
        lgtShotFileNeed = lgtShotFile
        if not os.path.exists(lgtShotFileNeed):
            lgtShotFileNeed = lgtShotFileNeed

        lgtSceneFileNeed = lgtSceneFile
        if not os.path.exists(lgtSceneFileNeed):
            lgtSceneFileNeed = lgtSceneFileNeed

        lgtbaseFileNeed = lgtbaseFile
        if not os.path.exists(lgtbaseFileNeed):
            lgtbaseFileNeed = lgtbaseFileNeed

        if os.path.exists(lgtShotFileNeed):
            needFile = lgtShotFileNeed
            loadState = 1
        else:
            if os.path.exists(lgtSceneFileNeed):
                needFile = lgtSceneFileNeed
                loadState = 2
        if loadState in [0]:
            needFile = lgtbaseFileNeed
        print('-----lightFile')
        print(needFile)
        lgtNs = 'skLgtNs'
        # 清理旧的
        lgtRootGrp = 'Light_juese'
        loadAttr = 'skLoaded'
        lgtLoadAttr = '%s.%s'%(lgtRootGrp,loadAttr)
        if mc.ls(lgtLoadAttr):
            mc.delete(lgtRootGrp)
        # 导入
        mc.file(needFile,i=1,namespace = lgtNs)
        # 清理ns
        mc.namespace(force = 1 ,moveNamespace = [(':' + lgtNs) , ':'])
        mc.namespace(removeNamespace= (':' + lgtNs))
        # 已导入的角色灯上标记
        mc.addAttr(lgtRootGrp, ln=loadAttr , at='double',dv = 1)
        mc.setAttr(lgtLoadAttr, e=True, keyable=True)
        return [lgtRootGrp]

    # 导入特效文件
    def vfxImport(self):
        vfxGrp = '|OTC_GRP|VFX_GRP'
        # 清理
        checkGrps = mc.listRelatives(vfxGrp,c=1,type='transform',f=1)
        if checkGrps:
            mc.delete(checkGrps)
        # 准备
        shotID = sk_infoConfig.sk_infoConfig().checkShotID()
        projectFolder = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        shotIDFolder = sk_infoConfig.sk_infoConfig().checkShotIDFolder()
        vfxFolder = '%sscenes/Animation/%s/effect'%(projectFolder,shotIDFolder)
        shotInfos = shotID.split('_')
        allFiles = []
        import os
        if os.path.exists(vfxFolder):
            allFiles = os.listdir(vfxFolder.replace('/','\\'))
        # 筛选
        nsBase = 'do6VfxTemp'
        needFiles = []
        for checkFile in allFiles:
            if checkFile.split('.')[-1] not in ['mb']:
                continue
            if shotID not in checkFile:
                continue
            checkInfo = checkFile.split(shotID)[-1]
            if '_' not in checkInfo:
                continue
            if checkInfo.split('_')[1][-4:] not in ['Base']:
                continue
            needFiles.append('%s/%s'%(vfxFolder,checkFile))
        # dust
        dustRoot = 'L:/Projects/DiveollyDive6/Project/data/FxCache/MS/EF'
        tempFile = '%s/%s/%s/dust_base_%s_%s.ma'%(dustRoot,shotInfos[1],shotInfos[2],shotInfos[1],shotInfos[2])
        if os.path.exists(tempFile):
            dustFile = tempFile
        else:
            tempFile = '%s/%s/dust_base_%s.ma'%(dustRoot,shotInfos[1],shotInfos[1])
            if os.path.exists(tempFile):
                dustFile = tempFile
            else:
                tempFile = '%s/dust_base.ma'%dustRoot
                dustFile = tempFile
        needFiles.append(dustFile)
        # 导入
        for num in range(len(needFiles)):
            print('--------')
            print(needFiles[num])
            try:
                mc.file(needFiles[num],i=1,namespace = '%s_%s'%(nsBase,str(num)))
            except:
                pass
        # 合并
        fishGrp = mc.ls('do6VfxTemp*:FX_Fish',type = 'transform',l=1)
        if fishGrp and '|%s|'%vfxGrp.split('|')[2] not in fishGrp[:9]:
            mc.parent(fishGrp,vfxGrp)
        dustGrp = mc.ls('do6VfxTemp*:FX_Dust',type = 'transform',l=1)
        if dustGrp and '|%s|'%vfxGrp.split('|')[2] not in dustGrp[:9]:
            mc.parent(dustGrp,vfxGrp)
        stoneGrp = mc.ls('do6VfxTemp*:FX_Stone',type = 'transform',l=1)
        if stoneGrp and '|%s|'%vfxGrp.split('|')[2] not in stoneGrp[:9]:
            mc.parent(stoneGrp,vfxGrp)
        # 清理ns
        from idmt.maya.py_common import sk_pyCommon
        reload(sk_pyCommon)
        for num in range(len(needFiles)):
            sk_pyCommon.sk_pyCommon().sk_deleteNamespace('%s_%s'%(nsBase,str(num)))

    # matte shader
    def matteShaderConfig(self):
        #matteShader = 'sk_matteShader'
        #if not mc.ls(matteShader,type = 'aiStandard'):
        #    matteShader = mc.shadingNode('aiStandard', asShader=True, name=matteShader)
        #mc.setAttr(matteShader + '.aiEnableMatte',1)
        matteShader = self.matteShader
        if not mc.ls(matteShader,type = 'surfaceShader'):
            matteShader = mc.shadingNode('surfaceShader', asShader=True, name=matteShader)
        mc.setAttr(matteShader + '.outMatteOpacity',0,0,0,type='double3')
        return matteShader

    # clean renderLayer
    def cleanRL(self,reOpen = ''):
        if reOpen:
            mc.file(reOpen,o=1,f=1)
        else:
            mc.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
            rls = mc.ls(type = 'renderLayer')
            for rl in rls:
                if 'defaultRenderLayer' in rl:
                    continue
                inr = mc.referenceQuery(rl,inr=1)
                if inr:
                    continue
                if ':' in rl:
                    continue
                mc.delete(rl)
            # cons
            cons = mc.listConnections('defaultRenderLayer',s=1,d=0,plugs=1,c=1)
            for num in range(len(cons)/2):
                inputAttr = cons[2*num+1]
                outputAttr = cons[2*num]
                if inputAttr.split('.')[0] in ['renderLayerManager']:
                    continue
                mc.disconnectAttr(inputAttr,outputAttr)
            # aov清理
            cleanAovs = mc.ls('msk*',type = 'aiAOV')
            if cleanAovs:mc.delete(cleanAovs)
            # 清理
            mel.eval('MLdeleteUnused')
        mc.currentTime(1005)

    # 清理未知节点
    def cleanUnknown(self):
        # 清理未知节点
        unknownNodes = mc.ls(type='unknown')
        for node in unknownNodes:
            if mc.ls(node):
                mc.lockNode(node, l=0)
                mc.delete(node)

    #--------------#
    # Auto Create All
    def xcm2019AutoCreateRenderLayers(self,refImport = 0,rlName = ''):
        import time
        self.cleanUnknown()
        return
        from idmt.maya.commonPerform.projectTools import sk_renderFileCheck_base
        reload(sk_renderFileCheck_base)
        rlCheckBase = sk_renderFileCheck_base.sk_renderFileCheck_base()
        print('---------Do6 Auto Step 000---------')
        # root
        shotID = sk_infoConfig.sk_infoConfig().checkShotID()
        shotInfos = shotID.split('_')
        errorImage = {}
        localRoot = '%s/%s/%s'%(self.exportRoot,shotInfos[1],shotInfos[2])
        import os
        if not os.path.exists(localRoot):
            os.makedirs(localRoot)
        from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
        reload(sk_referenceConfig)
        sk_referenceConfig.sk_referenceConfig().checkRefUnload2Load()
        print('---------All Reference Loaded---------')
        # 三相机显示层继承
        from idmt.maya.commonCore.core_finalLayout import sk_cacheFinalLayout
        reload(sk_cacheFinalLayout)
        sk_cacheFinalLayout.sk_cacheFinalLayout().displayLayerInfoImport()
        # 删掉不需要的
        from idmt.maya.commonPerform.projectTools import sk_projTools_base
        reload(sk_projTools_base)
        sk_projTools_base.sk_projTools_base().sdDelConfig()
        # 参考导入
        if refImport:
            print('---------Sart Reference Import---------')
            sk_referenceConfig.sk_referenceConfig().checkRefAllImport()
        fileBase = mc.file(exn=1,q=1).split('/')[-1]
        fileBase = '%s/%s'%(localRoot,fileBase)
        mc.file(rename = fileBase)
        mc.file(s=1,f=1)
        fileNameNow = mc.file(exn=1,q=1)
        fileName = ''
        lostLayers = []
        print('---------Do6 Auto Step 001---------')
        print('\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n')
        # CHRCLR
        if rlName in ['','chrclr']:
            #if rlName in ['']:
            #    self.cleanRL(reOpen = fileNameNow)
            self.rlCHR()
            self.cleanUnknown()
            lostLayers = self.lostRenderLayers(lostLayers)
            errorImage = rlCheckBase.checkRenderFileImagePath(shotInfos,errorImage)
            fileName = '%s/%s_CHRCLR_lr_c001.mb'%(localRoot,shotID)
            mc.file(rename = fileName)
            mc.file(s=1,f=1,type = 'mayaBinary')
        print('---------Do6 Auto Step 002---------')
        print('\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n')
        # BGCLR
        if rlName in ['','bgclr']:
            if rlName in ['']:
                self.cleanRL(reOpen = fileNameNow)
            self.rlBG()
            self.cleanUnknown()
            lostLayers = self.lostRenderLayers(lostLayers)
            fileName = '%s/%s_BGCLR_lr_c001.mb'%(localRoot,shotID)
            mc.file(rename = fileName)
            mc.file(s=1,f=1,type = 'mayaBinary')
        print('---------Do6 Auto Step 003---------')
        print('\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n')
        # ALLIDP
        if rlName in ['','allidp']:
            if rlName in ['']:
                self.cleanRL(reOpen = fileNameNow)
            self.rlAllIdp()
            self.cleanUnknown()
            lostLayers = self.lostRenderLayers(lostLayers)
            errorImage = rlCheckBase.checkRenderFileImagePath(shotInfos,errorImage)
            fileName = '%s/%s_ALLIDP_lr_c001.mb'%(localRoot,shotID)
            mc.file(rename = fileName)
            mc.file(s=1,f=1,type = 'mayaBinary')
        print('---------Do6 Auto Step 005---------')
        print('\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n')
        # CHRRGB
        if rlName in ['','chrrgb']:
            if rlName in ['']:
                self.cleanRL(reOpen = fileNameNow)
            self.rlCHR_RGB()
            lostLayers = self.lostRenderLayers(lostLayers)
            self.rlCHR_CAU()
            lostLayers = self.lostRenderLayers(lostLayers)
            self.cleanUnknown()
            errorImage = rlCheckBase.checkRenderFileImagePath(shotInfos,errorImage)
            fileName = '%s/%s_CHRRGB_lr_c001.mb'%(localRoot,shotID)
            mc.file(rename = fileName)
            mc.file(s=1,f=1,type = 'mayaBinary')
        # CHRSHD
        if rlName in ['','chrshd']:
            if rlName in ['']:
                self.cleanRL(reOpen = fileNameNow)
            self.rlCHR_SHD()
            lostLayers = self.lostRenderLayers(lostLayers)
            errorImage = rlCheckBase.checkRenderFileImagePath(shotInfos,errorImage)
            if self.emptyRenderLayerState():
                fileName = '%s/%s_CHRSHD_lr_c001.mb'%(localRoot,shotID)
                mc.file(rename = fileName)
                mc.file(s=1,f=1,type = 'mayaBinary')
        print('---------Do6 Auto Step 006---------')
        # CHRENV
        createState = self.chrEnvCreateState()
        if createState and rlName in ['','chrenv']:
            if rlName in ['']:
                self.cleanRL(reOpen = fileNameNow)
            self.rlCHR_ENV()
            self.cleanUnknown()
            errorImage = rlCheckBase.checkRenderFileImagePath(shotInfos,errorImage)
            fileName = '%s/%s_CHRENV_lr_c001.mb'%(localRoot,shotID)
            mc.file(rename = fileName)
            mc.file(s=1,f=1,type = 'mayaBinary')
        print('---------Do6 Auto Step 006a---------')
        # CHRHOLO
        if rlName in ['','chrholo']:
            if rlName in ['']:
                self.cleanRL(reOpen = fileNameNow)
            self.rlCHR_HOLO()
            self.cleanUnknown()
            errorImage = rlCheckBase.checkRenderFileImagePath(shotInfos,errorImage)
            if self.emptyRenderLayerState():
                fileName = '%s/%s_HOLOGRAM_lr_c001.mb'%(localRoot,shotID)
                mc.file(rename = fileName)
                mc.file(s=1,f=1,type = 'mayaBinary')
        print('---------Do6 Auto Step 006b---------')
        # CHRcreemAdd
        if rlName in ['','screenAdd']:
            if rlName in ['']:
                self.cleanRL(reOpen = fileNameNow)
            self.rlCHR_screenAddTools()
            self.cleanUnknown()
            errorImage = rlCheckBase.checkRenderFileImagePath(shotInfos,errorImage)
            if self.emptyRenderLayerState():
                fileName = '%s/%s_ScreenAdd_lr_c001.mb'%(localRoot,shotID)
                mc.file(rename = fileName)
                mc.file(s=1,f=1,type = 'mayaBinary')
        print('---------Do6 Auto Step 006c---------')
        # CHRFOG
        if rlName in ['','chrfog']:
            if rlName in ['']:
                self.cleanRL(reOpen = fileNameNow)
            self.rlCHR_FOG()
            self.cleanUnknown()
            errorImage = rlCheckBase.checkRenderFileImagePath(shotInfos,errorImage)
            if self.emptyRenderLayerState():
                fileName = '%s/%s_CHRFOG_lr_c001.mb'%(localRoot,shotID)
                mc.file(rename = fileName)
                mc.file(s=1,f=1,type = 'mayaBinary')
        print('---------Do6 Auto Step 007---------')
        # greenEye
        print('\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n')
        createState = self.greenEyesCreateState()
        if createState and rlName in ['','greeneyes']:
            if rlName in ['']:
                self.cleanRL(reOpen = fileNameNow)
            self.rlGreenEyes()
            self.cleanUnknown()
            errorImage = rlCheckBase.checkRenderFileImagePath(shotInfos,errorImage)
            fileName = '%s/%s_greenEyes_lr_c001.mb'%(localRoot,shotID)
            mc.file(rename = fileName)
            mc.file(s=1,f=1,type = 'mayaBinary')
        print('---------Do6 Auto Step 007b---------')
        print('\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n')
        # BGENV
        if rlName in ['','bgenv']:
            if rlName in ['']:
                self.cleanRL(reOpen = fileNameNow)
            self.rlBG_RGB()
            lostLayers = self.lostRenderLayers(lostLayers)
            self.rlBG_FOG()
            lostLayers = self.lostRenderLayers(lostLayers)
            self.rlBG_CAU()
            lostLayers = self.lostRenderLayers(lostLayers)
            self.cleanUnknown()
            errorImage = rlCheckBase.checkRenderFileImagePath(shotInfos,errorImage)
            fileName = '%s/%s_BGENV_lr_c001.mb'%(localRoot,shotID)
            mc.file(rename = fileName)
            mc.file(s=1,f=1,type = 'mayaBinary')
        print('---------Do6 Auto Step 008---------')
        print('\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n')
        # BGVFX
        if rlName in ['','bgvfx']:
            if rlName in ['']:
                self.cleanRL(reOpen = fileNameNow)
            self.rlBG_VFX()
            lostLayers = self.lostRenderLayers(lostLayers)
            self.cleanUnknown()
            errorImage = rlCheckBase.checkRenderFileImagePath(shotInfos,errorImage)
            if self.emptyRenderLayerState():
                fileName = '%s/%s_BGVFX_lr_c001.mb'%(localRoot,shotID)
                mc.file(rename = fileName)
                mc.file(s=1,f=1,type = 'mayaBinary')
        print('---------Do6 Auto Step 009---------')
        print('\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n')
        if fileNameNow != fileName:
            mc.sysFile(fileNameNow,delete = 1)
        print('---------006')
        print(os.path.exists(fileName))
        # errorList
        if lostLayers:
            print(u'-------以下渲染层按照规则没有创建:')
            for layer in lostLayers:
                if not layer:
                    continue
                print(layer)
        if errorImage.keys():
            for checkNode in errorImage.keys():
                print(u'-----路径错误，注意修复')
                print(checkNode)
                print(errorImage[checkNode])
            print(u'-----请修复上述路径错误-----')
            mc.error()
        print('\n---OutPath')
        print(localRoot)
        print('------------All Finish------------')

    # 未分的层收集
    def lostRenderLayers(self,lostLayers = []):
        if self.emptyLayer not in lostLayers:
            lostLayers.append(self.emptyLayer)
        if self.emptyLayer2 not in lostLayers:
            lostLayers.append(self.emptyLayer2)
        return lostLayers

    # 判断是否空文件 只有非必出的文件应用此状态
    def emptyRenderLayerState(self):
        rls = mc.ls(type = 'renderLayer')
        needLys = []
        for checkRL in rls:
            inr = mc.referenceQuery(checkRL,inr = 1)
            if inr:
                continue
            if 'defaultRenderLayer' in checkRL:
                continue
            needLys.append(checkRL)
        return needLys

    # AOV处理
    def aovConfig(self,aovType = '',deleteOld = 1):
        attrKey = 'skMode'
        # 清理原先的
        if deleteOld:
            aovNodes = mc.ls(type= 'aiAOV')
            for aovNode in aovNodes:
                aovAttr = '%s.%s'%(aovNode,attrKey)
                inrState = mc.referenceQuery(aovNode,inr = 1)
                if inrState:
                    continue
                if not mc.ls(aovAttr):
                    continue
                mc.delete(aovNode)
        # 导入
        aovFile = u'%s/%s_aov.ma'%(self.lightDataPath,aovType)
        if aovFile:
            tempNs = 'sk_temp_light'
            print aovFile
            mc.file( aovFile , i=1, namespace = tempNs )
            mc.namespace(force = 1 ,moveNamespace = [(':' + tempNs) , ':'])
            mc.namespace(removeNamespace= (':' + tempNs))
            # 加属性
            aovNodes = mc.ls(type= 'aiAOV')
            for aovNode in aovNodes:
                mc.addAttr(aovNode,ln = attrKey,at = 'double',dv=1,k=1)

    #----------------------------#
    # 单个分层区
    #--------------#
    # CHR_CLR
    def rlCHR_CO(self,aovForce = 0,printMode = 0):
        if printMode:print('\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n')
        # 初始化
        self.baseSettings()
        # objType
        objDict  = self.objectList()
        setMeshObjs = objDict['setMeshObjs']
        setAssObjs = objDict['setAssObjs']
        skyObjs = objDict['setSkyObjs']
        chrMeshObjs = objDict['chrMeshObjs']
        prpMeshObjs = objDict['prpMeshObjs']
        setLight_clr = objDict['setLight_clr']
        # 需要导入角色灯
        chrLight_clr = self.lgtImport('chr')
        # 导入aov
        self.aovConfig(aovType = 'chr_co')
        mc.setAttr('defaultArnoldRenderOptions.use_existing_tiled_textures',0)
        # RL start
        layerName = 'CHR_CO'
        # 该死的maya 2017，通过物体清单加各种错误，物体数量限制？
        rlObjs =  ['CHR_GRP'] + ['PRP_GRP'] + ['SET_GRP']  + chrLight_clr
        if not rlObjs:
            print(u'\n===============!!!No Objects 【RL】【%s】!!!===============\n' % (u'%s_层' % layerName))
            self.emptyLayer = layerName
            return
        if not chrLight_clr:
            print(u'\n===============!!!No Lights 【RL】【%s】!!!===============\n' % (u'%s_层' % layerName))
            self.emptyLayer = layerName
            return
        if mc.ls(layerName):
            mc.delete(layerName)
        mc.createRenderLayer(rlObjs , name=layerName , noRecurse=1 , makeCurrent=1)
        # sample values
        baseNode = 'defaultArnoldRenderOptions'
        attrDict = {'.AASamples':6,'.GIDiffuseSamples':2,'.GISpecularSamples':2,
                    '.GITransmissionSamples':2,'.GISssSamples':3,'.GIVolumeSamples':2,
                    '.GITotalDepth':10,'.GIDiffuseDepth':2,'.GISpecularDepth':2,'.GITransmissionDepth':2}
        for checkAttr in attrDict.keys():
            nodeAttr = baseNode + checkAttr
            mc.editRenderLayerAdjustment(nodeAttr)
            mc.setAttr(nodeAttr,attrDict[checkAttr])
        # pv
        for obj in setMeshObjs:
            mesh = mc.listRelatives(obj,s=1,type='mesh',ni=1,f=1)
            if not mesh:
                continue
            needMesh = mesh[0]
            meshAttr = needMesh + '.primaryVisibility'
            mc.editRenderLayerAdjustment(meshAttr)
            mc.setAttr(meshAttr,0)
        for checkObj in setAssObjs:
            checkShape = mc.listRelatives(checkObj,s=1,f=1,ni=1)[0]
            mc.setAttr(checkShape+'.overridePrimaryVisibility',1)
            mc.setAttr(checkShape+'.primaryVisibility',0)
        # format
        checkAttr = 'defaultArnoldDriver.tiffFormat'
        mc.editRenderLayerAdjustment(checkAttr)
        mc.setAttr(checkAttr,1)
        # fix
        for obj in setLight_clr:
            objAttr = obj+'.v'
            mc.editRenderLayerAdjustment(objAttr)
            mc.setAttr(objAttr,0)
        # 清理未知节点
        self.cleanUnknown()
        print(u'===============!!!Done 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
        if printMode:print('\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n')
        print('\n')

    #----------------#
    # BG_CLR
    def rlBG_CO(self,printMode = 0):
        if printMode:print('\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n')
        # 初始化
        self.baseSettings()
        # objType
        objDict  = self.objectList()
        setMeshObjs = objDict['setMeshObjs']
        setAssObjs = objDict['setAssObjs']
        skyObjs = objDict['setSkyObjs']
        chrMeshObjs = objDict['chrMeshObjs']
        prpMeshObjs = objDict['prpMeshObjs']
        setLight_clr = objDict['setLight_clr']
        # 导入aov
        self.aovConfig(aovType = 'bg_co')
        mc.setAttr('defaultArnoldRenderOptions.use_existing_tiled_textures',0)
        # RL start
        layerName = 'BG_CO'
        rlObjs = ['CHR_GRP'] + ['PRP_GRP'] + ['SET_GRP'] + setLight_clr
        if not rlObjs:
            print(u'\n===============!!!No Objects 【RL】【%s】!!!===============\n' % (u'%s_层' % layerName))
            self.emptyLayer = layerName
            return
        if not setLight_clr:
            print(u'\n===============!!!No Lights 【RL】【%s】!!!===============\n' % (u'%s_层' % layerName))
            self.emptyLayer = layerName
            return
        if mc.ls(layerName):
            mc.delete(layerName)
        mc.createRenderLayer(rlObjs , name=layerName , noRecurse=1 , makeCurrent=1)
        # sample values
        baseNode = 'defaultArnoldRenderOptions'
        attrDict = {'.AASamples':6,'.GIDiffuseSamples':2,'.GISpecularSamples':2,
                    '.GITransmissionSamples':2,'.GISssSamples':3,'.GIVolumeSamples':2,
                    '.GITotalDepth':10,'.GIDiffuseDepth':2,'.GISpecularDepth':2,'.GITransmissionDepth':2}
        for checkAttr in attrDict.keys():
            nodeAttr = baseNode + checkAttr
            mc.editRenderLayerAdjustment(nodeAttr)
            mc.setAttr(nodeAttr,attrDict[checkAttr])
        # pv
        for obj in (chrMeshObjs + prpMeshObjs + skyObjs):
            mesh = mc.listRelatives(obj,s=1,ni=1,type='mesh',f=1)
            if not mesh:
                continue
            needMesh = mesh[0]
            meshAttr = needMesh + '.primaryVisibility'
            mc.editRenderLayerAdjustment(meshAttr)
            mc.setAttr(meshAttr,0)
        # fur hide
        furGrps = mc.ls('*:FUR',l=1)
        for checkGrp in furGrps:
            checkAttr = checkGrp+'.v'
            mc.editRenderLayerAdjustment(checkAttr)
            mc.setAttr(checkAttr,0)
        # format
        checkAttr = 'defaultArnoldDriver.tiffFormat'
        mc.editRenderLayerAdjustment(checkAttr)
        mc.setAttr(checkAttr,1)
        # 清理未知节点
        self.cleanUnknown()
        print(u'===============!!!Done 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
        if printMode:print('\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n')
        print('\n')

    #--------------#
    # BG_fzc [素模]
    def rlBG_fzc(self,printMode = 1):
        if printMode:print('\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n')
        # 初始化
        self.baseSettings()
        # 素模
        from idmt.maya.commonCore.core_renderLayer import sk_renderLayerCore
        reload(sk_renderLayerCore)
        sk_renderLayerCore.sk_renderLayerCore().masterLayerLambertShader(shaderType='ar')
        # objType
        objDict  = self.objectList()
        setMeshObjs = objDict['setMeshObjs']
        setAssObjs = objDict['setAssObjs']
        skyObjs = objDict['setSkyObjs']
        setLight_clr = objDict['setLight_clr']
        # 导入aov
        self.aovConfig(aovType = 'bg_fzc')
        mc.setAttr('defaultArnoldRenderOptions.use_existing_tiled_textures',0)
        # RL start
        layerName = 'BGfzc'
        rlObjs = ['SET_GRP']
        if not rlObjs:
            print(u'===============!!!No Objects 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
            self.emptyLayer = layerName
            return
        if mc.ls(layerName):
            mc.delete(layerName)
        mc.createRenderLayer(rlObjs , name=layerName , noRecurse=1 , makeCurrent=1)
        # sample values
        baseNode = 'defaultArnoldRenderOptions'
        attrDict = {'.AASamples':6,'.GIDiffuseSamples':0,'.GISpecularSamples':0,
                    '.GITransmissionSamples':0,'.GISssSamples':0,'.GIVolumeSamples':0,
                    '.GITotalDepth':10,'.GIDiffuseDepth':2,'.GISpecularDepth':2,'.GITransmissionDepth':2}
        for checkAttr in attrDict.keys():
            nodeAttr = baseNode + checkAttr
            mc.editRenderLayerAdjustment(nodeAttr)
            mc.setAttr(nodeAttr,attrDict[checkAttr])
        # pv
        for obj in skyObjs:
            mesh = mc.listRelatives(obj,s=1,ni=1,type='mesh',f=1)
            if not mesh:
                continue
            needMesh = mesh[0]
            meshAttr = needMesh + '.primaryVisibility'
            mc.editRenderLayerAdjustment(meshAttr)
            mc.setAttr(meshAttr,0)
        # fix
        for obj in setLight_clr:
            objAttr = obj+'.v'
            mc.editRenderLayerAdjustment(objAttr)
            mc.setAttr(objAttr,0)
        # 清理未知节点
        self.cleanUnknown()
        print(u'===============!!!Done 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
        if printMode:print('\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n')
        print('\n')

    #--------------#
    # BG_FOG [素模]
    def rlBG_FOG(self,printMode = 0):
        if printMode:print('\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n')
        # 初始化
        self.baseSettings()
        # 素模
        from idmt.maya.commonCore.core_renderLayer import sk_renderLayerCore
        reload(sk_renderLayerCore)
        sk_renderLayerCore.sk_renderLayerCore().masterLayerLambertShader(shaderType='ar')
        # 导入light
        self.lgtImport(lgtType = 'bg',update = 1)
        # matte
        matteShader = self.matteShaderConfig()
        # objType
        objDict  = self.objectList()
        setMeshObjs = objDict['setMeshObjs']
        setFloorObjs = objDict['setFloorObjs']
        setAssObjs = objDict['setAssObjs']
        chrMeshObjs = objDict['chrMeshObjs']
        hairObjs = objDict['hairObjs']
        prpMeshObjs = objDict['prpMeshObjs']
        envLight_fog = objDict['envLight_fog']
        # RL start
        layerName = 'BGFOG'
        rlObjs = setMeshObjs + setAssObjs + envLight_fog
        if not rlObjs:
            print(u'===============!!!No Objects 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
            self.emptyLayer = layerName
            return
        if not envLight_fog:
            print(u'===============!!!No Lights 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
            self.emptyLayer = layerName
            return
        if mc.ls(layerName):
            mc.delete(layerName)
        mc.createRenderLayer(rlObjs , name=layerName , noRecurse=1 , makeCurrent=1)
        # aov
        aovAttr = 'defaultArnoldRenderOptions.aovMode'
        mc.editRenderLayerAdjustment(aovAttr)
        mc.setAttr(aovAttr,0)
        # sample values
        baseNode = 'defaultArnoldRenderOptions'
        attrDict = {'.AASamples':5,'.GIDiffuseSamples':0,'.GIGlossySamples':0,
                    '.GIRefractionSamples':0,'.GISssSamples':0,'.GIVolumeSamples':0,
                    '.GIDiffuseDepth':0,'.GIGlossyDepth':0,'.GIReflectionDepth':0,'.GIRefractionDepth':0}
        for checkAttr in attrDict.keys():
            nodeAttr = baseNode + checkAttr
            mc.editRenderLayerAdjustment(nodeAttr)
            mc.setAttr(nodeAttr,attrDict[checkAttr])
        # 处理aiVolume
        fixNode = ''
        needRebuild = 0
        checkAttr = 'defaultArnoldRenderOptions.atmosphere'
        mc.editRenderLayerAdjustment(checkAttr)
        cons = mc.listConnections(checkAttr,s=1,d=0,plugs=1)
        if cons:
            consNode = cons[0].split('.')[0]
            checkType = mc.nodeType(consNode)
            if checkType in ['aiVolumeScattering']:
                fixNode = consNode
            else:
                needRebuild = 1
                mc.disconnectAttr(cons[0],checkAttr)
        else:
            needRebuild = 1
        if needRebuild:
            fixNode = mc.shadingNode('aiVolumeScattering', asShader=True)
            mc.connectAttr(fixNode+'.message',checkAttr)
        fixAttr = fixNode + '.density'
        mc.editRenderLayerAdjustment(fixAttr)
        mc.setAttr(fixAttr,0.5)
        fixAttr = fixNode + '.samples'
        mc.editRenderLayerAdjustment(fixAttr)
        mc.setAttr(fixAttr,10)
        # pv
        fixSGList = []
        for obj in setMeshObjs:
            mesh = mc.listRelatives(obj,s=1,ni=1,type='mesh',f=1)
            if not mesh:
                continue
            needMesh = mesh[0]
            # shader
            sgNodeList = mc.listConnections(needMesh,s=0,d=1,type='shadingEngine')
            if sgNodeList:
                fixSGList += sgNodeList
        # shader
        if fixSGList:
            fixSGList = list(set(fixSGList))
            for checkSG in fixSGList:
                SGAttr = checkSG + '.surfaceShader'
                mc.editRenderLayerAdjustment(SGAttr)
                cons = mc.listConnections(SGAttr,s=1,d=0,plugs=1)
                if cons:
                    mc.disconnectAttr(cons[0],SGAttr)
                mc.connectAttr(matteShader + '.outColor',SGAttr)
        # 清理未知节点
        self.cleanUnknown()
        print(u'===============!!!Done 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
        if printMode:print('\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n')
        print('\n')

    #--------------#
    # BG_CAU [素模]
    def rlBG_CAU(self,printMode = 0):
        if printMode:print('\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n')
        # 初始化
        self.baseSettings()
        # 素模
        from idmt.maya.commonCore.core_renderLayer import sk_renderLayerCore
        reload(sk_renderLayerCore)
        sk_renderLayerCore.sk_renderLayerCore().masterLayerLambertShader(shaderType='ar')
        # 导入light
        self.lgtImport(lgtType = 'bg',update = 1)
        # objType
        objDict  = self.objectList()
        setMeshObjs = objDict['setMeshObjs']
        setFloorObjs = objDict['setFloorObjs']
        setAssObjs = objDict['setAssObjs']
        chrMeshObjs = objDict['chrMeshObjs']
        hairObjs = objDict['hairObjs']
        prpMeshObjs = objDict['prpMeshObjs']
        envLight_cau = objDict['envLight_cau']
        # RL start
        layerName = 'BGCAU'
        rlObjs = setMeshObjs + setAssObjs + envLight_cau
        if not rlObjs:
            print(u'===============!!!No Objects 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
            self.emptyLayer = layerName
            return
        if not envLight_cau:
            print(u'===============!!!No Lights 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
            self.emptyLayer = layerName
            return
        if mc.ls(layerName):
            mc.delete(layerName)
        mc.createRenderLayer(rlObjs , name=layerName , noRecurse=1 , makeCurrent=1)
        # aov
        aovAttr = 'defaultArnoldRenderOptions.aovMode'
        mc.editRenderLayerAdjustment(aovAttr)
        mc.setAttr(aovAttr,0)
        # sample values
        baseNode = 'defaultArnoldRenderOptions'
        attrDict = {'.AASamples':5,'.GIDiffuseSamples':0,'.GIGlossySamples':0,
                    '.GIRefractionSamples':0,'.GISssSamples':0,'.GIVolumeSamples':0,
                    '.GIDiffuseDepth':0,'.GIGlossyDepth':0,'.GIReflectionDepth':0,'.GIRefractionDepth':0}
        for checkAttr in attrDict.keys():
            nodeAttr = baseNode + checkAttr
            mc.editRenderLayerAdjustment(nodeAttr)
            mc.setAttr(nodeAttr,attrDict[checkAttr])
        # 清理未知节点
        self.cleanUnknown()
        print(u'===============!!!Done 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
        if printMode:print('\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n')
        print('\n')

    #--------------#
    # BG_VFX  [素模]  # 使用matte材质球
    def rlBG_VFX(self,printMode = 0):
        if printMode:print('\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n')
        # 初始化
        self.baseSettings()
        # 素模
        from idmt.maya.commonCore.core_renderLayer import sk_renderLayerCore
        reload(sk_renderLayerCore)
        sk_renderLayerCore.sk_renderLayerCore().masterLayerLambertShader(coNode=self.matteShader,shaderType='surfaceShader')
        # aiMatte
        for checkMesh in mc.ls(type='mesh',l=1):
            if mc.getAttr(checkMesh+'.intermediateObject'):
                continue
            mc.setAttr(checkMesh+'.aiMatte',1)
        # vfx文件导入
        self.vfxImport()
        if printMode:print('-------001')
        # 导入light
        self.lgtImport(lgtType = 'bg',update = 1)
        if printMode:print('-------002')
        # objType
        objDict  = self.objectList()
        setMeshObjs  = objDict['setMeshObjs']
        chrMeshObjs = objDict['chrMeshObjs']
        prpMeshObjs = objDict['prpMeshObjs']
        setLight_clr = objDict['setLight_clr']
        fishGrp  = objDict['vfxObjs_fish']
        dustGrp  = objDict['vfxObjs_dust']
        stoneGrp = objDict['vfxObjs_stone']
        # 导入aov
        self.aovConfig()
        #----------------------#
        # RL start : BGFSH
        layerName = 'BGFSH'
        createState = 1
        rlObjs = chrMeshObjs + prpMeshObjs + setMeshObjs + setLight_clr + fishGrp
        if not rlObjs:
            print(u'===============!!!No Objects 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
            self.emptyLayer2 = layerName
            createState = 0
        if not fishGrp:
            print(u'===============!!!No Objects 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
            self.emptyLayer2 = layerName
            createState = 0
        if not setLight_clr:
            print(u'===============!!!No Lights 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
            self.emptyLayer2 = layerName
            createState = 0
        if createState:
            if mc.ls(layerName):
                mc.delete(layerName)
            mc.createRenderLayer(rlObjs , name=layerName , noRecurse=1 , makeCurrent=1)
            # ao
            aovList = mc.ls(type = 'aiAOV')
            for checkAov in aovList:
                aovAttr = checkAov + '.enabled'
                mc.editRenderLayerAdjustment(aovAttr)
                if checkAov in ['ZDAOV_AO']:
                    mc.setAttr(aovAttr,1)
                else:
                    mc.setAttr(aovAttr,0)
            # sample values
            baseNode = 'defaultArnoldRenderOptions'
            attrDict = {'.AASamples':4,'.GIDiffuseSamples':0,'.GIGlossySamples':0,
                        '.GIRefractionSamples':0,'.GISssSamples':0,'.GIVolumeSamples':0,
                        '.GIDiffuseDepth':0,'.GIGlossyDepth':0,'.GIReflectionDepth':0,'.GIRefractionDepth':0}
            for checkAttr in attrDict.keys():
                nodeAttr = baseNode + checkAttr
                mc.editRenderLayerAdjustment(nodeAttr)
                mc.setAttr(nodeAttr,attrDict[checkAttr])
        #----------------------#
        # RL start : BGDUT
        layerName = 'BGDUT'
        createState = 1
        rlObjs = chrMeshObjs + prpMeshObjs + setMeshObjs + setLight_clr + dustGrp
        if not rlObjs:
            print(u'===============!!!No Objects 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
            self.emptyLayer = layerName
            createState = 0
        if not dustGrp:
            print(u'===============!!!No Objects 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
            self.emptyLayer = layerName
            createState = 0
        if not setLight_clr:
            print(u'===============!!!No Lights 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
            self.emptyLayer = layerName
            createState = 0
        if createState:
            if mc.ls(layerName):
                mc.delete(layerName)
            if printMode:print('-------003')
            mc.createRenderLayer(rlObjs , name=layerName , noRecurse=1 , makeCurrent=1)
            # Zaov
            aovList = mc.ls(type = 'aiAOV')
            for checkAov in aovList:
                aovAttr = checkAov + '.enabled'
                mc.editRenderLayerAdjustment(aovAttr)
                if checkAov in ['ZDAOV_Z']:
                    mc.setAttr(aovAttr,1)
                else:
                    mc.setAttr(aovAttr,0)
            # sample values
            baseNode = 'defaultArnoldRenderOptions'
            attrDict = {'.AASamples':4,'.GIDiffuseSamples':4,'.GIGlossySamples':2,
                        '.GIRefractionSamples':2,'.GISssSamples':2,'.GIVolumeSamples':0,
                        '.GIDiffuseDepth':2,'.GIGlossyDepth':2,'.GIReflectionDepth':2,'.GIRefractionDepth':2}
            for checkAttr in attrDict.keys():
                nodeAttr = baseNode + checkAttr
                mc.editRenderLayerAdjustment(nodeAttr)
                mc.setAttr(nodeAttr,attrDict[checkAttr])
            # 做约束
            volumeGrp = mc.ls('Dust_volumeSystem',type = 'volumeAxisField',l=1)
            if volumeGrp:
                volumeGrp = volumeGrp[0]
                camGrp = mc.ls('CAM:*_baked',type = 'transform',l=1)
                camGrp = camGrp[0]
                for attr in ['.tx','.ty','.tz','.rx','.ry','.rz']:
                    checkAttr = volumeGrp + attr
                    cons = mc.listConnections(checkAttr,s=1,d=0,plugs=1)
                    if cons:
                        mc.disconnectAttr(cons[0],checkAttr)
                mc.parentConstraint(camGrp , volumeGrp , maintainOffset = 0)
        # 清理未知节点
        self.cleanUnknown()
        print(u'===============!!!Done 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
        if printMode:print('\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n')
        print('\n')

    #-----------#
    # 自身idp,仅限角色道具
    def rlSelfAovCreate(self):
        aovList = []
        aovDict = {
                   '_skinEye':['aiMsk_body','aiMsk_cloth','aiMsk_eye'],
                   '_cloth':['aiMsk_shangyi','aiMsk_kuzi','aiMsk_xiezi'],
                   '_mouth':['aiMsk_yayin','aiMsk_yachi','aiMsk_shetou'],
                   #'_hair':['aiMsk_toufa','aiMsk_meimao','aiMsk_huzi'],
                   '_bag':['aiMsk_maozi','aiMsk_xiangji','aiMsk_bao']
                  }
        rgbList = self.aovCreateRGBNodes()
        for checkKey in aovDict.keys():
            aovName = checkKey
            rgbObjList = []
            for num in range(len(aovDict[checkKey])):
                checkObjs = []
                checkSetKey = aovDict[checkKey][num]
                checkSets = mc.ls('CH_*:'+checkSetKey) + mc.ls('PRO_*:'+checkSetKey)
                if checkSets:
                    checkObjs = mc.sets(checkSets,q=1)
                    if not checkObjs:
                        checkObjs = []
                rgbObjList.append(checkObjs)
            aovList += self.aovRGBCreatCore(rgbObjList,rgbList,aovName,aiSetMode = 0 )
        return aovList

    #-----------#
    # 按namespace类型,仅限角色 | 换算法
    def rlDifAovCreate(self,mode = 'chr'):
        aovList = []
        namespaces = mc.namespaceInfo(listOnlyNamespaces=1)
        namespaces.remove('UI')
        namespaces.remove('shared')
        if not namespaces:
            return aovList
        modeKey = 'CH_'
        if mode in ['prp']:
            modeKey = 'PRO_'
        if mode in ['set']:
            modeKey = 'BG_'
        # 参考筛选
        needNsList = []
        for checkNs in namespaces:
            if '_sysTemp' in checkNs:
                continue
            if not mc.ls(checkNs+':*',type='transform'):
                continue
            if modeKey in checkNs:
                needNsList.append(checkNs)
        if not needNsList:
            return aovList
        # 3类别找物体
        typeList = ['pgYetiMaya','mesh']
        nsNum = len(needNsList)
        if nsNum%3:
            cycleNum = int(nsNum/3)+1
        else:
            cycleNum = int(nsNum/3)
        for checkNum in range(cycleNum):
            aovName = '_%sSelf%s'%(mode,checkNum)
            rgbList = self.aovCreateRGBNodes(addKey = '%s_'%aovName)
            RList = self.getNsRenderObjs(needNsList[checkNum*3],typeList)
            GList = []
            if checkNum*3+1 < nsNum:
                GList = self.getNsRenderObjs(needNsList[checkNum*3+1],typeList)
            BList = []
            if checkNum*3+2 < nsNum:
                BList = self.getNsRenderObjs(needNsList[checkNum*3+2],typeList)
            aovList += self.aovRGBCreatCore([RList,GList,BList],rgbList,aovName,aiSetMode = 0 )
        return aovList

    # 获取物体
    def getNsRenderObjs(self,checkNs,needTypeList):
        tempNodes = []
        if needTypeList:
            for checkType in needTypeList:
                tempNodes += mc.ls(checkNs+':*',type = checkType,l=1)
            tempNodes = mc.listRelatives(tempNodes,p=1,type='transform',f=1)
        else:
            checkNodes = mc.ls(checkNs+':*',type = 'transform',l=1)
            for checkGrp in checkNodes:
                shape = mc.listRelatives(checkGrp,s=1,ni=1)
                if not shape:
                    continue
                tempNodes.append(checkGrp)
        if not tempNodes:
            tempNodes = []
        needObjs = tempNodes
        return needObjs

    #-----------#
    # all idp Layer [素模]
    def rlAll_Idp(self,printMode = 0):
        if printMode:print('\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n')
        # 初始化
        self.baseSettings()
        mc.setAttr('defaultRenderGlobals.imageFilePrefix','<RenderLayer>_<RenderPass>/<Scene>_<RenderLayer>_<RenderPass>',type = 'string')
        # 素模
        from idmt.maya.commonCore.core_renderLayer import sk_renderLayerCore
        reload(sk_renderLayerCore)
        sk_renderLayerCore.sk_renderLayerCore().masterLayerLambertShader(shaderType='ar')
        # 导入light
        #self.lgtImport()
        # objType
        objDict  = self.objectList()
        setMeshObjs = objDict['setMeshObjs']
        setAssObjs = objDict['setAssObjs']
        skyObjs = objDict['setSkyObjs']
        chrMeshObjs = objDict['chrMeshObjs']
        prpMeshObjs = objDict['prpMeshObjs']
        setLight_clr = objDict['setLight_clr']
        chrFurObjs = objDict['chrFurObjs']
        prpFurObjs = objDict['prpFurObjs']
        setFurObjs = objDict['setFurObjs']
        # light
        for obj in setLight_clr:
            objAttr = obj+'.v'
            mc.setAttr(objAttr,0)
        # 删除aov
        self.aovClean()
        #-----------#
        # all idp [素模]
        layerName = 'ALLIDP'
        rlObjs = ['CHR_GRP'] + ['PRP_GRP'] + ['SET_GRP']
        if not rlObjs:
            print(u'===============!!!No Objects 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
            self.emptyLayer = layerName
            return
        if mc.ls(layerName):
            mc.delete(layerName)
        if rlObjs:
            mc.createRenderLayer(rlObjs , name=layerName , noRecurse=1 , makeCurrent=1)
            # rgb
            #-----------#
            # chr,prp,set  RGB [素模]
            rgbList = self.aovCreateRGBNodes()
            cpsAov = self.aovRGBCreatCore([(chrMeshObjs+chrFurObjs),(prpMeshObjs+prpFurObjs),(setMeshObjs+setFurObjs+setFurObjs)],rgbList,'Cps',aiSetMode = 0 )
            for checkAov in cpsAov:
                aovAttr = checkAov + '.enabled'
                mc.editRenderLayerAdjustment(aovAttr)
                mc.setAttr(aovAttr,1)
        #-----------#
        # chr idp [素模]
        layerName = 'CHRIDP'
        rlObjs = chrMeshObjs + prpMeshObjs + chrFurObjs + prpFurObjs
        if not rlObjs:
            print(u'===============!!!No Objects 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
            self.emptyLayer = layerName
            return
        if mc.ls(layerName):
            mc.delete(layerName)
        if rlObjs:
            mc.createRenderLayer(rlObjs , name=layerName , noRecurse=1 , makeCurrent=1)
            chrAov = []
            chrAov += self.rlDifAovCreate()
            chrAov += self.rlSelfAovCreate()
            rgbList = self.aovCreateRGBNodes()
            for checkType in ['p']:
                needSetList = self.aovRGBGetSetList(checkType)
                layerInfos = needSetList.keys()
                for layerInfo in layerInfos:
                    chrAov += self.aovRGBCreatCore(needSetList[layerInfo],rgbList,layerInfo,aiSetMode = 1  )
            for checkAov in chrAov:
                aovAttr = checkAov + '.enabled'
                mc.editRenderLayerAdjustment(aovAttr)
                mc.setAttr(aovAttr,1)
        # 清理未知节点
        self.cleanUnknown()
        print(u'===============!!!Done 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
        #-----------#
        # bg idp [素模]
        layerName = 'BGIDP'
        rlObjs = setMeshObjs + setAssObjs
        if not rlObjs:
            print(u'===============!!!No Objects 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
            self.emptyLayer = layerName
        if mc.ls(layerName):
            mc.delete(layerName)
        if rlObjs:
            mc.createRenderLayer(rlObjs , name=layerName , noRecurse=1 , makeCurrent=1)
            setAov = []
            rgbList = self.aovCreateRGBNodes()
            for checkType in ['s']:
                needSetList = self.aovRGBGetSetList(checkType)
                layerInfos = needSetList.keys()
                for layerInfo in layerInfos:
                    setAov += self.aovRGBCreatCore(needSetList[layerInfo],rgbList,layerInfo,aiSetMode = 1  )
            for checkAov in setAov:
                aovAttr = checkAov + '.enabled'
                mc.editRenderLayerAdjustment(aovAttr)
                mc.setAttr(aovAttr,1)

        # 回masterLayer
        mc.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
        aovList = mc.ls(type = 'aiAOV')
        for checkAov in aovList:
            aovAttr = checkAov + '.enabled'
            mc.setAttr(aovAttr,0)
        # 格式
        mc.setAttr('defaultArnoldDriver.aiTranslator','png',type = 'string')
        # sample values
        baseNode = 'defaultArnoldRenderOptions'
        attrDict = {'.AASamples':6,'.GIDiffuseSamples':0,'.GISpecularSamples':0,
                    '.GITransmissionSamples':0,'.GISssSamples':0,'.GIVolumeSamples':0,
                    '.GITotalDepth':0,'.GIDiffuseDepth':0,'.GISpecularDepth':0,'.GITransmissionDepth':0}
        for checkAttr in attrDict.keys():
            nodeAttr = baseNode + checkAttr
            mc.setAttr(nodeAttr,attrDict[checkAttr])
        if printMode:print('\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n')

    #------------------#
    # hair 渲染层模式
    def rlHairIdp(self,printMode = 0):
        if printMode:print('\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n')
        # 初始化
        self.baseSettings()
        mc.setAttr('defaultRenderGlobals.imageFilePrefix','<RenderLayer>_<RenderPass>/<Scene>_<RenderLayer>_<RenderPass>',type = 'string')
        # 素模
        from idmt.maya.commonCore.core_renderLayer import sk_renderLayerCore
        reload(sk_renderLayerCore)
        sk_renderLayerCore.sk_renderLayerCore().masterLayerLambertShader(shaderType='ar')
        # obj
        hairSetList = ['aiMsk_toufa','aiMsk_meimao','aiMsk_huzi']
        RGBHairObjs = []
        for checkSet in hairSetList:
            needSGNodes = []
            checkSet = mc.ls('*:'+checkSet)
            if not checkSet:
                RGBHairObjs.append([])
                continue
            needObjs = mc.sets(checkSet,q=1)
            if not needObjs:
                needObjs = []
            RGBHairObjs.append(needObjs)
        # RL
        rlBase = 'hairRL'
        rgbList = ['R','G','B']
        for num in range(len(RGBHairObjs)):
            layerName = '%s_%s'%(rlBase,rgbList[num])
            if mc.ls(layerName):
                mc.delete(layerName)
            rlObjs = RGBHairObjs[num]
            if rlObjs:
                mc.createRenderLayer(rlObjs , name=layerName , noRecurse=1 , makeCurrent=1)
        # 格式
        mc.setAttr('defaultArnoldDriver.aiTranslator','png',type = 'string')
        # sample values
        baseNode = 'defaultArnoldRenderOptions'
        attrDict = {'.AASamples':5,'.GIDiffuseSamples':0,'.GISpecularSamples':0,
                    '.GITransmissionSamples':0,'.GISssSamples':0,'.GIVolumeSamples':0,
                    '.GITotalDepth':0,'.GIDiffuseDepth':0,'.GISpecularDepth':0,'.GITransmissionDepth':0}
        for checkAttr in attrDict.keys():
            nodeAttr = baseNode + checkAttr
            mc.setAttr(nodeAttr,attrDict[checkAttr])
        if printMode:print('\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n')

    #------------------#
    # 获取所有aiMsk的信息
    # set组明名: namespace:aiMsk_idpName_TypeRGB
    # 如:mi_c002002Teethless_h:aiMsk_TL_CHRR
    def aovRGBGetSetList2(self,assetType):
        allSetList = mc.ls('*:aiMsk_*',type = 'objectSet') + mc.ls('*:aiMSk_*',type = 'objectSet')
        aiSetList = {}
        assetDict = {}
        # 加载
        for checkSet in allSetList:
            setTypeKey = checkSet.split('_')[-1][:-1]
            needState = 0
            if assetType in ['c','C'] and setTypeKey.lower() in ['chr']:
                needState = 1
            if assetType in ['p','P'] and setTypeKey.lower() in ['prp']:
                needState = 1
            if assetType in ['s','S'] and setTypeKey.lower() in ['set']:
                needState = 1
            if not needState:
                continue
            aovKey = checkSet.split(':')[-1].split('_')[1]
            ns = checkSet.split(':')[0]
            assetID = ns.split('_')[1]
            key = '%s_%s'%(aovKey,ns)
            assetID_key = '%s_%s'%(aovKey,assetID)
            assetKeys = assetDict.keys()
            if aovKey not in assetKeys:
                assetDict[aovKey] = [[assetID_key,key]]
            else:
                if [assetID_key,key] not in assetDict[aovKey]:
                    assetDict[aovKey].append([assetID_key,key])
            checkKeys = aiSetList.keys()
            if key not in checkKeys:
                aiSetList[key] = [checkSet]
            else:
                aiSetList[key].append(checkSet)
        # 修正重复
        fixedDict = {}
        for aovKey in assetDict.keys():
            if len(assetDict[aovKey]) == 1:
                fixedDict[aovKey] =  aiSetList[assetDict[aovKey][0][-1]]
            else:
                for num in range(len(assetDict[aovKey])):
                    if num == 0:
                        fixedDict[aovKey] =  aiSetList[assetDict[aovKey][0][-1]]
                    else:
                        fixedDict['%s%s'%(aovKey,str(num))] =  aiSetList[assetDict[aovKey][num][-1]]
        aiSetList = fixedDict
        # 排序
        checkSetKeys = aiSetList.keys()
        for checkKey in checkSetKeys:
            if not aiSetList[checkKey]:
                continue
            setName = aiSetList[checkKey][0]
            nsType = setName.split('_')[1][0].lower()
            setList = aiSetList[checkKey]
            tempList = ['','','','','',nsType]
            for checkSet in setList:
                if checkSet[-1] in ['R']:
                    tempList[0] = checkSet
                if checkSet[-1] in ['G']:
                    tempList[1] = checkSet
                if checkSet[-1] in ['B']:
                    tempList[2] = checkSet
                if checkSet[-1] in ['A']:
                    tempList[3] = checkSet
                if checkSet[-1] in ['M']:
                    tempList[4] = checkSet
            aiSetList[checkKey] = tempList

        return aiSetList

    #------------------#
    # 获取所有aiMsk的信息
    # set组明名: namespace:aiMsk_idpName_TypeRGB
    # 如:mi_c002002Teethless_h:aiMsk_TL_CHRR
    def aovRGBGetSetList(self,assetType):
        allSetList = mc.ls('*:aiMsk_*',type = 'objectSet') + mc.ls('*:aiMSK_*',type = 'objectSet')
        aiSetList = {}
        assetDict = {}
        # 加载
        for checkSet in allSetList:
            setTypeKey = checkSet.split('_')[-1][:-1]
            needState = 0
            if assetType in ['c','C'] and setTypeKey.lower() in ['chr']:
                needState = 1
            if assetType in ['p','P'] and setTypeKey.lower() in ['prp']:
                needState = 1
            if assetType in ['s','S'] and setTypeKey.lower() in ['set']:
                needState = 1
            if not needState:
                continue
            aovKey = checkSet.split(':')[-1].split('_')[1]
            ns = checkSet.split(':')[0]
            assetID = ns.split('_')[1]
            key = '%s_%s'%(aovKey,ns)
            assetID_key = '%s_%s'%(aovKey,assetID)
            assetKeys = assetDict.keys()
            if aovKey not in assetKeys:
                assetDict[aovKey] = [[assetID_key,key]]
            else:
                if [assetID_key,key] not in assetDict[aovKey]:
                    assetDict[aovKey].append([assetID_key,key])
            checkKeys = aiSetList.keys()
            if key not in checkKeys:
                aiSetList[key] = [checkSet]
            else:
                aiSetList[key].append(checkSet)
        # 修正重复
        fixedDict = {}
        for aovKey in assetDict.keys():
            if len(assetDict[aovKey]) == 1:
                fixedDict[aovKey] =  aiSetList[assetDict[aovKey][0][-1]]
            else:
                for num in range(len(assetDict[aovKey])):
                    if num == 0:
                        fixedDict[aovKey] =  aiSetList[assetDict[aovKey][0][-1]]
                    else:
                        fixedDict['%s%s'%(aovKey,str(num))] =  aiSetList[assetDict[aovKey][num][-1]]
        aiSetList = fixedDict
        # 排序
        checkSetKeys = aiSetList.keys()
        for checkKey in checkSetKeys:
            if not aiSetList[checkKey]:
                continue
            setName = aiSetList[checkKey][0]
            nsType = setName.split('_')[1][0].lower()
            setList = aiSetList[checkKey]
            tempList = ['','','',nsType]
            for checkSet in setList:
                if checkSet[-1] in ['R']:
                    tempList[0] = checkSet
                if checkSet[-1] in ['G']:
                    tempList[1] = checkSet
                if checkSet[-1] in ['B']:
                    tempList[2] = checkSet
            aiSetList[checkKey] = tempList

        return aiSetList

    #----------------------------------------------------#
    # [核心] rgb Base Shader
    # 某些情况下,如果msk有冲突，各个idp结果不对，互相干扰，就每个idp一套rgb
    def aovCreateRGBNodes(self,transCreate = 0,addKey = ''):
        # rebuild rgb
        RColor = 'R_aiColor_%sxcm2019'%addKey
        GColor = 'G_aiColor_%sxcm2019'%addKey
        BColor = 'B_aiColor_%sxcm2019'%addKey
        RColorTR = 'R_aiColor_TR_%sxcm2019'%addKey
        GColorTR = 'G_aiColor_TR_%sxcm2019'%addKey
        BColorTR = 'B_aiColor_TR_%sxcm2019'%addKey

        if not mc.ls(RColor):
            mc.shadingNode('aiUserDataColor', asShader=1,name = RColor)
        if not mc.ls(GColor):
            mc.shadingNode('aiUserDataColor', asShader=1,name = GColor)
        if not mc.ls(BColor):
            mc.shadingNode('aiUserDataColor', asShader=1,name = BColor)
        if transCreate:
            if not mc.ls(RColorTR):
                mc.shadingNode('aiStandard', asShader=1,name = RColorTR)
            if not mc.ls(GColorTR):
                mc.shadingNode('aiStandard', asShader=1,name = GColorTR)
            if not mc.ls(BColorTR):
                mc.shadingNode('aiStandard', asShader=1,name = BColorTR)

        mc.setAttr(RColor+'.defaultValue',1,0,0,typ='double3')
        mc.setAttr(GColor+'.defaultValue',0,1,0,typ='double3')
        mc.setAttr(BColor+'.defaultValue',0,0,1,typ='double3')
        if transCreate:
            mc.setAttr(RColorTR+'.color',1,0,0,typ='double3')
            mc.setAttr(RColorTR+'.emissionColor',1,0,0,typ='double3')
            mc.setAttr(RColorTR+'.Kd',1)
            mc.setAttr(RColorTR+'.Kt',1)
            mc.setAttr(RColorTR+'.emission',1)
            mc.setAttr(GColorTR+'.color',0,1,0,typ='double3')
            mc.setAttr(GColorTR+'.emissionColor',0,1,0,typ='double3')
            mc.setAttr(GColorTR+'.Kd',1)
            mc.setAttr(GColorTR+'.Kt',1)
            mc.setAttr(GColorTR+'.emission',1)
            mc.setAttr(BColorTR+'.color',0,0,1,typ='double3')
            mc.setAttr(BColorTR+'.emissionColor',0,0,1,typ='double3')
            mc.setAttr(BColorTR+'.Kd',1)
            mc.setAttr(BColorTR+'.Kt',1)
            mc.setAttr(BColorTR+'.emission',1)

        return [RColor,GColor,BColor,RColorTR,GColorTR,BColorTR]

    #----------------------------------------------------#
    # [核心]Transparency Type
    # aiSetList 最多3个元素一套
    # aiColors  [RColor,GColor,BColor]
    # aiSetMode 为1时，aiSetList为三个set的名字的list ; 为0时,aiSetList为三个objlist的list
    def aovRGBCreatCore(self,aiSetList,aiColors,layerInfo,aiSetMode = 1):
        aovFinalList = []

        cycleNum = 3
        aiMasksSets = aiSetList[:cycleNum]
        if not mc.objExists('defaultArnoldDriver'):
            import mtoa.core as core
            core.createOptions()
        # start
        for aiSetNum in xrange(0, len(aiMasksSets), cycleNum):
            aovName = layerInfo
            print('-------')
            print(aovName)
            customAOV = 'msk%s'%aovName
            if mc.ls(customAOV):
                mc.delete(customAOV)

            tSwitch = 'RGB_Switch_%s'%customAOV
            if mc.ls(tSwitch):
                mc.delete(tSwitch)
            tSwitch = mc.shadingNode('tripleShadingSwitch',au=1,name = tSwitch)
            mc.setAttr(tSwitch+'.default',0,0,0,typ='double3')

            aiUshader = 'RGB_aiUtility_%s'%customAOV
            if mc.ls(aiUshader):
                mc.delete(aiUshader)
            aiUshader = mc.shadingNode('aiUtility', asShader=1,name = aiUshader)
            mc.setAttr(aiUshader+'.shadeMode',2)

            mc.connectAttr(tSwitch+'.output', aiUshader+'.color',f=1)
            #print('--------switchInfo')
            #print(aiMasksSets[aiSetNum:aiSetNum+cycleNum])
            for num, setName in enumerate( aiMasksSets[aiSetNum:aiSetNum+cycleNum] ):
                if not mc.ls(setName):
                    continue
                aiColor = aiColors[num % cycleNum]
                if aiSetMode:
                    checkObjs = mc.sets(setName,q=1)
                else:
                    checkObjs = setName
                if not checkObjs:
                    continue
                for obj in checkObjs:
                    checkType = mc.nodeType(obj)
                    if checkType not in ['transform']:
                        obj = mc.listRelatives(obj,p=1,type='transform',f=1)[0]
                    shapeNode = mc.listRelatives(obj,s=1,ni=1,f=1)
                    if not shapeNode:
                        continue
                    shapeNode = shapeNode[0]
                    checkType = mc.nodeType(shapeNode)
                    inpt = mc.getAttr(tSwitch+'.input',s=1)
                    if checkType in ['mesh']:
                        mc.connectAttr(shapeNode+'.instObjGroups[0]',tSwitch+'.input['+str(inpt)+'].inShape',f=1)

                        noTrState = mc.getAttr(shapeNode+'.aiOpaque')
                        #if noTrState:
                        mc.connectAttr(aiColor+'.outColor',tSwitch+'.input['+str(inpt)+'].inTriple',f=1)
                        #else:
                        #    mc.connectAttr(aiColors[num % cycleNum + cycleNum]+'.outColor',tSwitch+'.input['+str(inpt)+'].inTriple',f=1)
                    if checkType in ['pgYetiMaya','shaveHair','pfxHair']:
                        SGNode = mc.listConnections(shapeNode,s=0,d=1,type = 'shadingEngine')
                        if not SGNode:
                            continue
                        SGNode = SGNode[0]
                        consIndex = self.getAovIndexByName(SGNode,customAOV)
                        checkSGAttr = SGNode+'.aiCustomAOVs[%s].aovInput'%(str(consIndex))
                        cons = mc.listConnections(checkSGAttr,s=1,d=0,plugs=1)
                        if cons:
                            mc.disconnectAttr(cons[0],checkSGAttr)
                        mc.connectAttr((aiColor+'.outColor'),checkSGAttr,f=1)
                        mc.connectAttr(aiColor+'.outColor',tSwitch+'.input['+str(inpt)+'].inTriple',f=1)
            # AOV'S
            aovListSize = mc.getAttr('defaultArnoldRenderOptions.aovList',s=1)
            for checkNum in range(aovListSize):
                cons = mc.listConnections('defaultArnoldRenderOptions.aovList[%s]'%str(checkNum),s=1,d=0)
                if not cons:
                    aovListSize = checkNum
                    break

            customAOV = mc.createNode('aiAOV',n=customAOV, skipSelect=True)
            mc.setAttr(customAOV+'.name',customAOV,type='string')
            mc.connectAttr(customAOV+'.message','defaultArnoldRenderOptions.aovList['+ str(aovListSize)+']',f=1)
            mc.connectAttr('defaultArnoldDriver.message',customAOV+'.outputs[0].driver', f=1)
            mc.connectAttr('defaultArnoldFilter.message',customAOV+'.outputs[0].filter', f=1)
            # connect to default shader
            mc.connectAttr(aiUshader+'.outColor',customAOV+'.defaultValue',f=1)

            aovFinalList.append(customAOV)

        return aovFinalList

    # 获取SG的aov_channel
    def getAovIndexByName(self,sgNode, aovName):
        import pymel.core as pm
        sg = pm.nt.ShadingEngine(sgNode)
        lastIndex = -1
        nextIndex = None
        for at in sg.aiCustomAOVs:
            currIndex = at.index()
            if at.aovName.get() == aovName:
                return currIndex
            if nextIndex is None and currIndex > (lastIndex +1):
                nextIndex = lastIndex +1
            lastIndex = currIndex
        if nextIndex is None:
            nextIndex = lastIndex +1
        at = sg.aiCustomAOVs[nextIndex]
        at.aovName.set(aovName)
        return nextIndex

    #-------------#
    # 环境球创建
    def rlSkyEnv(self,forceBuild = 0,printMode = 0):
        if printMode:print('\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n')
        # 读取表格
        needShotIDList = []
        import xlrd
        import os
        excelFile = 'L:/Projects/DiveollyDive6/Project/data/lighting/skyEnvShotList.xls'
        excelData = xlrd.open_workbook(excelFile)
        excelInfos = excelData.sheets()[0]
        cell_01_Infos = excelInfos.col_values(0)
        cell_02_Infos = excelInfos.col_values(1)
        cell_03_Infos = excelInfos.col_values(2)
        for num in range(len(cell_01_Infos)):
            if num in [0]:
                continue
            newShotID = '%s_%s'%(cell_01_Infos[num],cell_02_Infos[num])
            if newShotID not in needShotIDList:
                needShotIDList.append(newShotID)
        # 批量处理
        baseSkyFile = 'L:/Projects/DiveollyDive6/Project/data/lighting/sky/do6_s645006Sky_l1SKY_lr_c001.mb'
        localPublishFolder = '%s/skyFiles'%self.exportRoot
        if not os.path.exists(localPublishFolder):
            os.makedirs(localPublishFolder)
        from idmt.maya.commonCore.core_mayaCommon import sk_hbExportCam
        reload(sk_hbExportCam)
        for num in range(len(needShotIDList)):
            shotID = needShotIDList[num]
            print('-----[%s]_[Start]!!!'%shotID)
            if printMode:print('\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n')
            shotInfos = ['do6',shotID.split('_')[0],shotID.split('_')[1]]
            localRoot = '%s/%s/%s'%(self.exportRoot,shotInfos[1],shotInfos[2])
            if not os.path.exists(localRoot):
                os.makedirs(localRoot)
            shotSkyFile = 'do6_%s_l1SKY_lr_c001.mb'%shotID
            localSkyFile = '%s/%s'%(localRoot,shotSkyFile)
            localPublishFile = '%s/%s'%(localPublishFolder,shotSkyFile)
            if cell_03_Infos[num+1] in ['Y'] and not forceBuild:
                # 更新
                mc.sysFile(localSkyFile,copy = localPublishFile)
                print('-----[%s]_[Pass]!!!'%shotID)
                continue
            # 开始处理
            mc.file(baseSkyFile,o=1,f=1)
            # 改名
            mc.file(rename = localSkyFile)
            # 镜头参考修正
            sk_hbExportCam.sk_hbExportCam().camServerReference()
            # 初始化
            self.baseSettings()
            # 相机属性
            cameras = mc.ls(type = 'camera',l=1)
            for camShape in cameras:
                if 'CenterCamShape' not in camShape:
                    continue
                mc.setAttr(camShape + '.farClipPlane',10000000)
            # 输出
            mc.file(s=1,type = 'mayaBinary',f=1)
            mc.sysFile(localSkyFile,copy = localPublishFile)
            print('-----[%s]_[Done]!!!'%shotID)
        print('-----[ALL]_[Done]!!!')
        if printMode:print('\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n')

