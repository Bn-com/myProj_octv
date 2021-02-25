# -*- coding: utf-8 -*-
# 【通用】【do6项目】
#  Author : 沈康
#  Data   : 2017

#-----------------------------------------#
# idp 分 角色/道具/场景 和 asset自身的idp
#-------角色/道具/场景的需要额外处理
# 如 aovCPRGBCreate()
#-------asset自身的idp
# set组明名: namespace:aiMSK_idpName_TypeRGB
# 如:mi_c002002Teethless_h:aiMSK_TL_CHRR

import maya.cmds as mc
import maya.mel as mel
import time
from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
reload(sk_infoConfig)

class sk_renderLayer_do6x(object):

    def __init__(self):
        self.dataBase = 'L:/Projects/DiveollyDive6/Project/data'
        self.lightDataPath = self.dataBase + '/lighting'
        self.aovFilePath = self.lightDataPath + '/do6_aov.ma'
        self.exportRoot = 'D:/do6RLFiles'
        self.matteShader = 'sk_matteShader'
        self.emptyLayer = ''
        self.emptyLayer2 = ''

    def baseSettings(self,renderer = 'ar'):
        mc.setAttr('defaultRenderLayer.renderable',0)
        if renderer in ['ar']:
            if not mc.pluginInfo('mtoa.mll',q=1,loaded = 1):
                mc.loadPlugin('mtoa.mll')
            import mtoa
            mtoa.core.createOptions()
            import mtoa.cmds.registerArnoldRenderer
            mtoa.cmds.registerArnoldRenderer.registerArnoldRenderer()
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'arnold', type='string')
        if renderer in ['sw']:
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'mayaSoftware', type='string')
        # 标准设置
        mc.setAttr('defaultRenderGlobals.imageFormat', 7)
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

        if renderer in ['ar']:
            mc.setAttr('defaultArnoldDriver.halfPrecision', 0)
            mc.setAttr('defaultArnoldDriver.aiTranslator','tif',type='string')
            mc.setAttr('defaultArnoldDriver.tiffCompression',0)
            mc.setAttr('defaultArnoldRenderOptions.lock_sampling_noise', 0)
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

        # 修正相机namespace
        from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools
        reload(sk_sceneTools)
        sk_sceneTools.sk_sceneTools().sk_sceneAssetNamespaceConfig()
        from idmt.maya.commonCore.core_renderLayer import sk_renderLayerCore
        reload(sk_renderLayerCore)
        sk_renderLayerCore.sk_renderLayerCore().camRefFix()

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
        mc.setAttr('CAM:stereoCameraRightShape.renderable',1)
        mc.setAttr('CAM:stereoCameraLeftShape.renderable',1)

        # 所有mel关闭
        mc.setAttr('defaultRenderGlobals.preMel','',type='string')
        mc.setAttr('defaultRenderGlobals.postMel','',type='string')

        if renderer in ['ar']:
        # yeti config
            yetiPath = 'C:\\tools\LocalTools\\3partPlugin\\2014\Yeti\\1.3.5\\bin'
            mc.setAttr('defaultArnoldRenderOptions.procedural_searchpath',yetiPath,type='string')
        '''
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
        '''
        # 更新信息
        sk_renderLayerCore.sk_renderLayerCore().blendShapeUpdateInfo()
        # 处理背包
        #self.bagWeaponFix()
        self.fixWeaponNanObjs()
        # 处理smooth
        from idmt.maya.commonCore.core_mayaCommon import sk_smoothSet
        reload(sk_smoothSet)
        sk_smoothSet.sk_smoothSet().smoothSetDoSmooth(disModify = 0)

    # sky场景分层
    def skyFix(self):
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
        mc.setAttr('CAM:stereoCameraRightShape.renderable',1)
        mc.setAttr('CAM:stereoCameraLeftShape.renderable',1)

        # 所有mel关闭
        mc.setAttr('defaultRenderGlobals.preMel','',type='string')
        mc.setAttr('defaultRenderGlobals.postMel','',type='string')

    # 场景模型，场景代理，场景灯光，角色模型，角色灯光，角色毛发，道具模型
    def objectList(self):
        objListDict = {}
        # 场景模型,mesh上的grp
        setMeshObjs = mc.listRelatives('SET_GRP',ad=1,type='mesh',f=1)
        if setMeshObjs:
            setMeshObjs = mc.listRelatives(setMeshObjs,p=1,type='transform',f=1)
            setMeshObjs = list(set(setMeshObjs))
        else:
            setMeshObjs = []
        objListDict['setMeshObjs'] = setMeshObjs

        # 场景地面
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

        # 角色模型
        chrMeshObjs = mc.listRelatives('CHR_GRP',ad=1,type='mesh',f=1)
        if chrMeshObjs:
            chrMeshObjs = mc.listRelatives(chrMeshObjs,p=1,type='transform',f=1)
            chrMeshObjs = list(set(chrMeshObjs))
        else:
            chrMeshObjs = []
        objListDict['chrMeshObjs'] = chrMeshObjs

        # 角色头发
        hairObjs = mc.ls(type = 'xgmPalette')
        objListDict['hairObjs'] = hairObjs

        # 道具模型
        prpMeshObjs = mc.listRelatives('PRP_GRP',ad=1,type='mesh',f=1)
        if prpMeshObjs:
            prpMeshObjs = mc.listRelatives(prpMeshObjs,p=1,type='transform',f=1)
            prpMeshObjs = list(set(prpMeshObjs))
        else:
            prpMeshObjs = []
        objListDict['prpMeshObjs'] = prpMeshObjs

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

        # 场景灯光 CO
        setLight = mc.ls('*:SET_LIGHTING_COLOR')
        if not mc.ls(setLight):
            setLight = []
        setLight = self.lightCheckNeed(setLight)
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
    def lightCheckNeed(self,checkLightGrps):
        lgtGrps = mc.ls(checkLightGrps,l=1)
        needGrps = []
        for checkGrp in lgtGrps:
            needState = 1
            for checkKey in  ['|CHR_GRP|','|PRP_GRP|','|SET_GRP|']:
                if checkKey in checkGrp:
                    needState = 0
            if needState:
                needGrps.append(checkGrp)
        return needGrps

    # AOV处理
    def aovConfig(self,force = 0):
        aovState = 0
        aovNodes = mc.ls(type= 'aiAOV')
        if aovNodes:
            aovState = 1
        if not aovState or force:
            print '----------aovFile'
            print self.aovFilePath
            mc.file(self.aovFilePath,i=1)

    # aov清理
    def aovClean(self):
        aovNodes = mc.ls(type= 'aiAOV')
        if aovNodes:
            mc.delete(aovNodes)

    # 导入灯光
    def lgtImport(self,lgtType='chr',update = 0):
        if lgtType in ['bg']:
            lgtType = 'set'
        finalNs = 'rlLGT_%s'%lgtType
        finalRN = 'rlLGT_%sRN'%lgtType
        if mc.ls('*:%s_LIGHTING'%(lgtType.upper())) and (not update):
            return
        basePath = '%s/%s'%(self.lightDataPath,lgtType.upper())
        if lgtType in ['fog']:
            basePath = '%s/%s'%(self.lightDataPath,'chr'.upper())
        shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()

        shotLgtPath = '%s/%s/%s'%(basePath,shotInfos[1],shotInfos[2])
        shotLgtFile = '%s_base_%s_%s.ma'%(lgtType,shotInfos[1],shotInfos[2])
        sceneLgtPath = '%s/%s'%(basePath,shotInfos[1])
        seceneLgtFile = '%s_base_%s.ma'%(lgtType,shotInfos[1])

        lgtShotFile = '%s/%s'%(shotLgtPath,shotLgtFile)
        lgtSceneFile = '%s/%s'%(sceneLgtPath,seceneLgtFile)
        lgtbaseFile = '%s/%s_base.ma'%(basePath,lgtType)

        needFile = ''
        loadState = 0
        import os

        #优先读ma,后读mb
        lgtShotFileNeed = lgtShotFile
        if not os.path.exists(lgtShotFileNeed):
            lgtShotFileNeed = lgtShotFileNeed.replace('.ma','.mb')

        lgtSceneFileNeed = lgtSceneFile
        if not os.path.exists(lgtSceneFileNeed):
            lgtSceneFileNeed = lgtSceneFileNeed.replace('.ma','.mb')

        lgtbaseFileNeed = lgtbaseFile
        if not os.path.exists(lgtbaseFileNeed):
            lgtbaseFileNeed = lgtbaseFileNeed.replace('.ma','.mb')

        if os.path.exists(lgtShotFileNeed):
            needFile = lgtShotFileNeed
            loadState = 1
        else:
            if os.path.exists(lgtSceneFileNeed):
                needFile = lgtSceneFileNeed
                loadState = 2
        if loadState in [0]:
            needFile = lgtbaseFileNeed
        print '-----lightFile'
        print needFile
        if lgtType in ['fog']:
            lgtRoot = mc.ls('%s:CHR_FOG'%finalNs)
            if lgtRoot:
                mc.delete(lgtRoot)
                ns = finalNs
                mc.namespace(force = 1 ,moveNamespace = [(':' + ns) , ':'])
                mc.namespace(removeNamespace= (':' + ns))
        #mc.file(needFile,i=1,namespace = finalNs)
        if mc.ls(finalRN) and update:
            mc.file(needFile,loadReference = finalRN )
        else:
            #mc.file(needFile, r=1, namespace = finalNs ,referenceNode = finalRN )
            mc.file(needFile, r=1, namespace = finalNs )
        # 修正焦散属性
        fixGrp = mc.ls('%s:*_CAU'%finalNs,l=1) + mc.ls('%s:*_FOG'%finalNs,l=1)
        if fixGrp:
            fixLights = mc.listRelatives(fixGrp,ad=1,type='light',f=1)
            if not fixLights:
                fixLights = []
            for checkLight in fixLights:
                cons = mc.listConnections(checkLight+'.aiFilters',s=1,d=0,plugs=1)
                if not cons:
                    continue
                fixTxShader = cons[0].split('.')[0]
                cons = mc.listConnections(fixTxShader+'.slidemap',s=1,d=0,plugs=1)
                if not cons:
                    continue
                fixFileNode = cons[0].split('.')[0]
                nodeAttr = fixFileNode+'.frameOffset'
                if not mc.ls(nodeAttr):
                    continue
                mc.setAttr(nodeAttr,0)
        if lgtType in ['fog']:
            mc.file(needFile,importReference = 1, f = 1)

    # fog 约束处理
    def chrFogLocFix(self):
        locFaceDict = {'olly':['MSH_c_hi_periscope_13_ca_',89],
                       'beth':['MSH_c_hi_periscope_5_ca_',160],
                       'jlL2':['MSH_c_hi_oscarB4_5_',12],
                       'jlL1':['MSH_c_hi_oscarB3_5_',12],
                       'jlMouth':['MSH_c_hi_suona_1',0],
                       'jlR1':['MSH_c_hi_oscarB2_5_',12],
                       'jlR2':['MSH_c_hi_oscarB1_2_',12]}
        abcNsKey = 'sysTemp_mesh:'
        oldCons = mc.ls('loc_*_pointOnPolyConstraint*',type='pointOnPolyConstraint')
        if oldCons:mc.delete(oldCons)
        # 处理约束
        for checkKey in locFaceDict.keys():
            # locator
            locNeed = mc.ls('*:loc_%s'%checkKey,type = 'transform')
            locNeed = locNeed[0]
            # face
            needObj = ''
            faceObjs = mc.ls('*:%s'%locFaceDict[checkKey][0],type = 'transform')
            if not faceObjs:
                continue
            for checkObj in faceObjs:
                if abcNsKey in checkObj:
                    continue
                if checkKey in ['beth','olly'] and checkKey not in checkObj.split(':')[0]:
                    continue
                if checkKey[:2] in ['jl'] and 'c020' not in checkObj.split(':')[0]:
                    continue
                needObj = checkObj
            if not needObj:
                continue
            print needObj+'.vtx[%s]'%locFaceDict[checkKey][1]
            # 约束
            mc.select(needObj+'.vtx[%s]'%locFaceDict[checkKey][1])
            mc.select(locNeed,add = 1)
            mel.eval('doCreatePointOnPolyConstraintArgList 2 {   "0" ,"0" ,"0" ,"1" ,"" ,"1" ,"0" ,"0" ,"0" ,"0" };')
        mc.select(cl=1)

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
        import os
        if not os.path.exists(vfxFolder):
            return
        allFiles = os.listdir(vfxFolder.replace('/','\\'))
        if not allFiles:
            return
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
        dustFile = 'L:/Projects/DiveollyDive6/Project/data/FxCache/MS/EF/dust_base.ma'
        needFiles.append(dustFile)
        # 导入
        for num in range(len(needFiles)):
            print '--------'
            print needFiles[num]
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
    def do6AutoCreateRenderLayers(self,refImport = 0,rlName = ''):
        import time
        self.cleanUnknown()
        from idmt.maya.commonPerform.projectTools import sk_renderFileCheck_base
        reload(sk_renderFileCheck_base)
        rlCheckBase = sk_renderFileCheck_base.sk_renderFileCheck_base()
        print '---------Do6 Auto Step 000---------'
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
        print '---------All Reference Loaded---------'
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
            print '---------Sart Reference Import---------'
            sk_referenceConfig.sk_referenceConfig().checkRefAllImport()
        fileBase = mc.file(exn=1,q=1).split('/')[-1]
        fileBase = '%s/%s'%(localRoot,fileBase)
        mc.file(rename = fileBase)
        mc.file(s=1,f=1)
        fileNameNow = mc.file(exn=1,q=1)
        lostLayers = []
        print '---------Do6 Auto Step 001---------'
        print '\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'
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
        print '---------Do6 Auto Step 002---------'
        print '\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'
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
        print '---------Do6 Auto Step 003---------'
        print '\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'
        # ALLIDP
        if rlName in ['','allidp']:
            print "\n\n\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n\n\n"
            if rlName in ['']:
                self.cleanRL(reOpen = fileNameNow)
            self.rlAllIdp()
            self.cleanUnknown()
            lostLayers = self.lostRenderLayers(lostLayers)
            errorImage = rlCheckBase.checkRenderFileImagePath(shotInfos,errorImage)
            fileName = '%s/%s_ALLIDP_lr_c001.mb'%(localRoot,shotID)
            print fileName
            print "\n\n\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n\n\n"
            mc.file(rename = fileName)
            mc.file(s=1,f=1,type = 'mayaBinary')
        print '---------Do6 Auto Step 005---------'
        print '\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'
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
            fileName = '%s/%s_CHRSHD_lr_c001.mb'%(localRoot,shotID)
            mc.file(rename = fileName)
            mc.file(s=1,f=1,type = 'mayaBinary')
        print '---------Do6 Auto Step 006---------'
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
        print '---------Do6 Auto Step 006a---------'
        # CHRHOLO
        if rlName in ['','chrholo']:
            if rlName in ['']:
                self.cleanRL(reOpen = fileNameNow)
            self.rlCHR_HOLO()
            self.cleanUnknown()
            errorImage = rlCheckBase.checkRenderFileImagePath(shotInfos,errorImage)
            if self.emptyRenderLayerState():
                fileName = '%s/%s_HOLOGRAM_lr_c001.ma'%(localRoot,shotID)
                mc.file(rename = fileName)
                mc.file(s=1,f=1,type = 'mayaAscii')
        print fileName
        return
        print '---------Do6 Auto Step 006b---------'
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
        print '---------Do6 Auto Step 007---------'
        print '\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'
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
        print '---------Do6 Auto Step 008---------'
        print '\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'
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
        print '---------Do6 Auto Step 009---------'
        print '\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'
        mc.sysFile(fileNameNow,delete = 1)
        # errorList
        if lostLayers:
            print u'-------以下渲染层按照规则没有创建:'
            for layer in lostLayers:
                if not layer:
                    continue
                print layer
        if errorImage.keys():
            for checkNode in errorImage.keys():
                print u'-----路径错误，注意修复'
                print checkNode
                print errorImage[checkNode]
            print u'-----请修复上述路径错误-----'
            mc.error()
        print '\n---OutPath'
        print localRoot
        print '------------All Finish------------'

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

    #----------------------------#
    # 单个分层区
    #--------------#
    # CHR_CLR
    def rlCHR(self,aovForce = 0,printMode = 0):
        if printMode:print '\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'
        # 初始化
        self.baseSettings()
        # 导入light
        self.lgtImport('chr',update = 1)
        # objType
        objDict  = self.objectList()
        setMeshObjs = objDict['setMeshObjs']
        setFloorObjs = objDict['setFloorObjs']
        setAssObjs = objDict['setAssObjs']
        chrMeshObjs = objDict['chrMeshObjs']
        hairObjs = objDict['hairObjs']
        prpMeshObjs = objDict['prpMeshObjs']
        chrLight_clr = objDict['chrLight_clr']
        chrLight_sky = objDict['chrLight_sky']
        # 导入aov
        self.aovConfig(aovForce)
        #mc.setAttr('defaultArnoldRenderOptions.use_existing_tiled_textures',1)
        # RL start
        layerName = 'CHRCLR'
        rlObjs = chrMeshObjs + prpMeshObjs + chrLight_clr + chrLight_sky
        if not rlObjs:
            print (u'===============!!!No Objects 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
            self.emptyLayer = layerName
            return
        if not (chrLight_clr + chrLight_sky):
            print (u'===============!!!No Lights 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
            self.emptyLayer = layerName
            return
        if mc.ls(layerName):
            mc.delete(layerName)
        mc.createRenderLayer(rlObjs , name=layerName , noRecurse=1 , makeCurrent=1)
        # sample values
        baseNode = 'defaultArnoldRenderOptions'
        attrDict = {'.AASamples':5,'.GIDiffuseSamples':3,'.GIGlossySamples':2,
                    '.GIRefractionSamples':2,'.GISssSamples':5,'.GIVolumeSamples':2,
                    '.GIDiffuseDepth':2,'.GIGlossyDepth':2,'.GIReflectionDepth':2,'.GIRefractionDepth':2}
        for checkAttr in attrDict.keys():
            nodeAttr = baseNode + checkAttr
            mc.editRenderLayerAdjustment(nodeAttr)
            mc.setAttr(nodeAttr,attrDict[checkAttr])
        # format
        checkAttr = 'defaultArnoldDriver.tiffFormat'
        mc.editRenderLayerAdjustment(checkAttr)
        mc.setAttr(checkAttr,1)
        # 清理未知节点
        self.cleanUnknown()
        print (u'===============!!!Done 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
        if printMode:print '\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'
        print '\n'

    #--------------#
    # CHR_RGB  [素模]
    def rlCHR_RGB(self,printMode = 0):
        if printMode:print '\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'
        # 初始化
        self.baseSettings()
        # 素模
        from idmt.maya.commonCore.core_renderLayer import sk_renderLayerCore
        reload(sk_renderLayerCore)
        sk_renderLayerCore.sk_renderLayerCore().masterLayerLambertShader(shaderType='ar')
        # 导入light
        self.lgtImport(lgtType = 'chr' ,update = 1)
        # objType
        objDict  = self.objectList()
        setMeshObjs = objDict['setMeshObjs']
        setFloorObjs = objDict['setFloorObjs']
        setAssObjs = objDict['setAssObjs']
        chrMeshObjs = objDict['chrMeshObjs']
        hairObjs = objDict['hairObjs']
        prpMeshObjs = objDict['prpMeshObjs']
        chrLight_rgb = objDict['chrLight_rgb']
        # RL start
        layerName = 'CHRRGB'
        rlObjs = chrMeshObjs + prpMeshObjs + chrLight_rgb
        if not rlObjs:
            print (u'===============!!!No Objects 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
            self.emptyLayer = layerName
            return
        if not chrLight_rgb:
            print (u'===============!!!No Lights 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
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
        attrDict = {'.AASamples':5,'.GIDiffuseSamples':3,'.GIGlossySamples':0,
                    '.GIRefractionSamples':0,'.GISssSamples':0,'.GIVolumeSamples':0,
                    '.GIDiffuseDepth':0,'.GIGlossyDepth':0,'.GIReflectionDepth':0,'.GIRefractionDepth':0}
        for checkAttr in attrDict.keys():
            nodeAttr = baseNode + checkAttr
            mc.editRenderLayerAdjustment(nodeAttr)
            mc.setAttr(nodeAttr,attrDict[checkAttr])
        # 清理未知节点
        self.cleanUnknown()
        print (u'===============!!!Done 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
        if printMode:print '\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'
        print '\n'

    #--------------#
    # CHR_SHD  [素模] 没有地面就不创建
    def rlCHR_SHD(self,printMode= 0):
        if printMode:print '\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'
        # 初始化
        self.baseSettings()
        # 素模
        from idmt.maya.commonCore.core_renderLayer import sk_renderLayerCore
        reload(sk_renderLayerCore)
        sk_renderLayerCore.sk_renderLayerCore().masterLayerLambertShader(shaderType='ar')
        # 导入light
        self.lgtImport(lgtType = 'chr' , update = 1)
        # objType
        objDict  = self.objectList()
        setMeshObjs = objDict['setMeshObjs']
        setFloorObjs = objDict['setFloorObjs']
        setAssObjs = objDict['setAssObjs']
        chrMeshObjs = objDict['chrMeshObjs']
        hairObjs = objDict['hairObjs']
        prpMeshObjs = objDict['prpMeshObjs']
        chrLight_key = objDict['chrLight_key']
        # 导入aov
        self.aovConfig()
        # RL start
        layerName = 'CHRSHD'
        rlObjs = chrMeshObjs + prpMeshObjs + setFloorObjs + chrLight_key
        if not rlObjs:
            print (u'===============!!!No Objects 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
            self.emptyLayer = layerName
            return
        if not setFloorObjs:
            print (u'===============!!!No Ground 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
            self.emptyLayer = layerName
            return
        if not chrLight_key:
            print (u'===============!!!No Lights 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
            self.emptyLayer = layerName
            return
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
        attrDict = {'.AASamples':5,'.GIDiffuseSamples':3,'.GIGlossySamples':0,
                    '.GIRefractionSamples':0,'.GISssSamples':0,'.GIVolumeSamples':0,
                    '.GIDiffuseDepth':0,'.GIGlossyDepth':0,'.GIReflectionDepth':0,'.GIRefractionDepth':0}
        for checkAttr in attrDict.keys():
            nodeAttr = baseNode + checkAttr
            mc.editRenderLayerAdjustment(nodeAttr)
            mc.setAttr(nodeAttr,attrDict[checkAttr])
        # Ground
        meshes = []
        if setFloorObjs:
            meshes = mc.listRelatives(setFloorObjs,ad=1,type='mesh',f=1)
        if meshes:
            meshSGList = mc.listConnections(meshes,s=0,d=1,type='shadingEngine')
            if meshSGList:
                sk_renderLayerCore.sk_renderLayerCore().masterLayerLambertShader(coNode = 'base_GroundShader',
                        shaderType='aiShadowCatcher',justSGList = meshSGList,msLayer=0,Adjustment = 0)
        # pv
        for obj in (chrMeshObjs+prpMeshObjs):
            mesh = mc.listRelatives(obj,s=1,ni=1,type='mesh',f=1)
            if not mesh:
                continue
            needMesh = mesh[0]
            meshAttr = needMesh + '.primaryVisibility'
            mc.editRenderLayerAdjustment(meshAttr)
            mc.setAttr(meshAttr,0)
        for obj in setFloorObjs:
            mesh = mc.listRelatives(obj,s=1,ni=1,type='mesh',f=1)
            if not mesh:
                continue
            needMesh = mesh[0]
            meshAttr = needMesh + '.castsShadows'
            mc.editRenderLayerAdjustment(meshAttr)
            mc.setAttr(meshAttr,0)
        # 清理未知节点
        self.cleanUnknown()
        print (u'===============!!!Done 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
        if printMode:print '\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'
        print '\n'

    #--------------#
    # CHR_CAU  [素模] # 使用matte材质球
    def rlCHR_CAU(self,printMode = 0):
        if printMode:print '\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'
        # 初始化
        self.baseSettings()
        # 素模
        from idmt.maya.commonCore.core_renderLayer import sk_renderLayerCore
        reload(sk_renderLayerCore)
        sk_renderLayerCore.sk_renderLayerCore().masterLayerLambertShader(shaderType='ar')
        # 导入light
        self.lgtImport(lgtType = 'chr' , update = 1)
        # objType
        objDict  = self.objectList()
        setMeshObjs = objDict['setMeshObjs']
        setFloorObjs = objDict['setFloorObjs']
        setAssObjs = objDict['setAssObjs']
        chrMeshObjs = objDict['chrMeshObjs']
        hairObjs = objDict['hairObjs']
        prpMeshObjs = objDict['prpMeshObjs']
        chrLight_cau = objDict['chrLight_cau']
        # RL start
        layerName = 'CHRCAU'
        rlObjs = chrMeshObjs + prpMeshObjs + chrLight_cau
        if not rlObjs:
            print (u'===============!!!No Objects 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
            self.emptyLayer = layerName
            return
        if not chrLight_cau:
            print (u'===============!!!No Lights 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
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
        print (u'===============!!!Done 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
        if printMode:print '\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'
        print '\n'

    #--------------#
    # CHR_ENV
    def rlCHR_ENV(self,printMode = 0):
        createState = self.chrEnvCreateState()
        if not createState:
            return
        if printMode:print '\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'
        # 初始化
        self.baseSettings()
        # 素模
        from idmt.maya.commonCore.core_renderLayer import sk_renderLayerCore
        reload(sk_renderLayerCore)
        sk_renderLayerCore.sk_renderLayerCore().masterLayerLambertShader(shaderType='ar')
        # 导入light
        self.lgtImport(lgtType = 'bg' , update = 1)
        # objType
        objDict  = self.objectList()
        setMeshObjs = objDict['setMeshObjs']
        setFloorObjs = objDict['setFloorObjs']
        setAssObjs = objDict['setAssObjs']
        chrMeshObjs = objDict['chrMeshObjs']
        hairObjs = objDict['hairObjs']
        prpMeshObjs = objDict['prpMeshObjs']
        setLight_clr = objDict['setLight_rgb']
        # RL start
        layerName = 'CHRENV'
        rlObjs = chrMeshObjs + prpMeshObjs + setLight_clr
        if not rlObjs:
            print (u'===============!!!No Objects 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
            self.emptyLayer = layerName
            return
        if not setLight_clr:
            print (u'===============!!!No Lights 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
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
        attrDict = {'.AASamples':5,'.GIDiffuseSamples':3,'.GIGlossySamples':0,
                    '.GIRefractionSamples':0,'.GISssSamples':0,'.GIVolumeSamples':0,
                    '.GIDiffuseDepth':0,'.GIGlossyDepth':0,'.GIReflectionDepth':0,'.GIRefractionDepth':0}
        for checkAttr in attrDict.keys():
            nodeAttr = baseNode + checkAttr
            mc.editRenderLayerAdjustment(nodeAttr)
            mc.setAttr(nodeAttr,attrDict[checkAttr])
        # 清理未知节点
        self.cleanUnknown()
        print (u'===============!!!Done 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
        if printMode:print '\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'
        print '\n'

    #--------------#
    # 是否使用chrenv
    def chrEnvCreateState(self):
        nsList = mc.namespaceInfo(listOnlyNamespaces=1)
        nsList.remove('UI')
        nsList.remove('shared')
        setsNsList = ['s606001','s613001','s614001','s634001',
                      's617001','s617002','s625001','s626001',
                      's627001','s627002']
        needState = 0
        for checkNs in nsList:
            if '_' not in checkNs:
                continue
            checkKey = checkNs.split('_')[1]
            if len(checkKey) <= 7:
                continue
            if checkKey[:7] in setsNsList:
                needState = 1
        return needState

    #--------------#
    # CHR_FOG
    def rlCHR_FOG(self,printMode = 0):
        # 判断要不要创建
        rlNeedState = 0
        shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
        if shotInfos[1] in ['006','008','012','016']:
            rlNeedState = 1
        if not rlNeedState:
            return
        if printMode:print '\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'
        # 初始化
        self.baseSettings()
        # 素模
        from idmt.maya.commonCore.core_renderLayer import sk_renderLayerCore
        reload(sk_renderLayerCore)
        sk_renderLayerCore.sk_renderLayerCore().masterLayerLambertShader(shaderType='ar')
        # 导入light
        self.lgtImport(lgtType = 'fog' , update = 1)
        # 处理loc
        self.chrFogLocFix()
        # objType
        objDict  = self.objectList()
        setMeshObjs = objDict['setMeshObjs']
        ollyGrp = mc.ls('do6_c601*olly**:MODEL',l=1)
        bethGrp = mc.ls('do6_c602*beth*:MODEL',l=1)
        jlGrp = mc.ls('do6_c020001JiaoLong*:MODEL',l=1)
        ollyLoc = mc.ls('*:loc_olly',l=1)
        bethLoc = mc.ls('*:loc_beth',l=1)
        jlLoc = mc.ls('*:loc_jinglongGrp',l=1)
        fixObjs = mc.ls('do6_c602*beth*:MSH_c_hi_periscope_2_ca_',l=1) + \
            mc.ls('do6_c602*beth*:MSH_c_hi_periscope_3_ca_',l=1) + \
            mc.ls('do6_c602*beth*:MSH_c_hi_periscope_4_ca_',l=1) + \
            mc.ls('do6_c602*beth*:MSH_c_hi_periscope_5_ca_',l=1) + \
            mc.ls('do6_c601*olly*:MSH_c_hi_periscope_1_ca_',l=1) + \
            mc.ls('do6_c601*olly*:MSH_c_hi_periscope_2_ca_',l=1) + \
            mc.ls('do6_c601*olly*:MSH_c_hi_periscope_12_ca_',l=1) + \
            mc.ls('do6_c601*olly*:MSH_c_hi_periscope_13_ca_',l=1)  + \
            mc.ls('do6_c020001JiaoLong*:MSH_c_hi_suona_1',l=1) + \
            mc.ls('do6_c020001JiaoLong*:MSH_c_hi_oscarB1_1_',l=1) + \
            mc.ls('do6_c020001JiaoLong*:MSH_c_hi_oscarB1_2_',l=1) + \
            mc.ls('do6_c020001JiaoLong*:MSH_c_hi_oscarB1_3_',l=1) + \
            mc.ls('do6_c020001JiaoLong*:MSH_c_hi_oscarB1_4_',l=1) + \
            mc.ls('do6_c020001JiaoLong*:MSH_c_hi_oscarB1_5_',l=1) + \
            mc.ls('do6_c020001JiaoLong*:MSH_c_hi_oscarB2_1_',l=1) + \
            mc.ls('do6_c020001JiaoLong*:MSH_c_hi_oscarB2_2_',l=1) + \
            mc.ls('do6_c020001JiaoLong*:MSH_c_hi_oscarB2_3_',l=1) + \
            mc.ls('do6_c020001JiaoLong*:MSH_c_hi_oscarB2_4_',l=1) + \
            mc.ls('do6_c020001JiaoLong*:MSH_c_hi_oscarB2_5_',l=1) + \
            mc.ls('do6_c020001JiaoLong*:MSH_c_hi_oscarB3_1_',l=1) + \
            mc.ls('do6_c020001JiaoLong*:MSH_c_hi_oscarB3_2_',l=1) + \
            mc.ls('do6_c020001JiaoLong*:MSH_c_hi_oscarB3_3_',l=1) + \
            mc.ls('do6_c020001JiaoLong*:MSH_c_hi_oscarB3_4_',l=1) + \
            mc.ls('do6_c020001JiaoLong*:MSH_c_hi_oscarB3_5_',l=1) + \
            mc.ls('do6_c020001JiaoLong*:MSH_c_hi_oscarB4_1_',l=1) + \
            mc.ls('do6_c020001JiaoLong*:MSH_c_hi_oscarB4_2_',l=1) + \
            mc.ls('do6_c020001JiaoLong*:MSH_c_hi_oscarB4_3_',l=1) + \
            mc.ls('do6_c020001JiaoLong*:MSH_c_hi_oscarB4_4_',l=1) + \
            mc.ls('do6_c020001JiaoLong*:MSH_c_hi_oscarB4_5_',l=1)
        for fixObj in fixObjs:
            checkMesh = mc.listRelatives(fixObj,s=1,ni=1,type='mesh',f=1)
            mc.setAttr(checkMesh[0]+'.castsShadows',0)
        print '-------fogObjs:'
        print ollyGrp
        print bethGrp
        print jlGrp
        print ollyLoc
        print bethLoc
        print jlLoc
        # start RL
        #--------------#
        # FOGRGB
        layerName = 'FOGRGB'
        rlObjs = ollyGrp + bethGrp + jlGrp + setMeshObjs + ollyLoc + bethLoc + jlLoc
        if not rlObjs:
            print (u'===============!!!No Objects 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
            self.emptyLayer = layerName
            return
        if not (ollyLoc + bethLoc + jlLoc):
            print (u'===============!!!No Lights 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
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
        attrDict = {'.AASamples':4,'.GIDiffuseSamples':4,'.GIGlossySamples':0,
                    '.GIRefractionSamples':0,'.GISssSamples':0,'.GIVolumeSamples':0,
                    '.GIDiffuseDepth':2,'.GIGlossyDepth':0,'.GIReflectionDepth':0,'.GIRefractionDepth':0}
        for checkAttr in attrDict.keys():
            nodeAttr = baseNode + checkAttr
            mc.editRenderLayerAdjustment(nodeAttr)
            mc.setAttr(nodeAttr,attrDict[checkAttr])
        # 处理aiVolume
        checkAttr = 'defaultArnoldRenderOptions.atmosphere'
        cons = mc.listConnections(checkAttr,s=1,d=0,plugs=1)
        if cons:
            mc.editRenderLayerAdjustment(checkAttr)
            mc.disconnectAttr(cons[0],checkAttr)
        # light fix
        lightNodes = mc.listRelatives(ollyLoc + bethLoc,ad = 1,type = 'light',f=1)
        if not lightNodes:
            lightNodes = []
        for lightNode in lightNodes:
            lightAttr = lightNode + '.aiExposure'
            mc.editRenderLayerAdjustment(lightAttr)
            mc.setAttr(lightAttr,1.5)
        print (u'===============!!!Done 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
        if printMode:print '\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'
        #--------------#
        # CHRFOG
        layerName = 'CHRFOG'
        rlObjs = ollyGrp + bethGrp + jlGrp +setMeshObjs + ollyLoc + bethLoc
        if not rlObjs:
            print (u'===============!!!No Objects 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
            self.emptyLayer = layerName
            return
        if not (ollyGrp + bethGrp):
            print (u'===============!!!No Lights 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
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
        # light
        for checkLoc in (ollyLoc + bethLoc):
            lightShapes = mc.listRelatives(checkLoc,ad=1,type = 'light',f=1)
            if not lightShapes:
                continue
            for checkLight in lightShapes:
                lightAttr = checkLight + '.aiExposure'
                mc.editRenderLayerAdjustment(lightAttr)
                mc.setAttr(lightAttr,0)
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
        fixAttr = 'base_cleanShader.aiEnableMatte'
        mc.editRenderLayerAdjustment(fixAttr)
        mc.setAttr(fixAttr,1)
        fixAttr = 'base_cleanShader.color'
        mc.editRenderLayerAdjustment(fixAttr)
        mc.setAttr(fixAttr,0,0,0,type='double3')
        print (u'===============!!!Done 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
        if printMode:print '\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'
        #--------------#
        # JLHFOG
        layerName = 'JLHFOG'
        rlObjs = ollyGrp + bethGrp + jlGrp + setMeshObjs + jlLoc
        if not rlObjs:
            print (u'===============!!!No Objects 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
            self.emptyLayer = layerName
            return
        if not jlGrp:
            print (u'===============!!!No Lights 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
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
        # light
        for checkLoc in (ollyLoc + bethLoc):
            lightShapes = mc.listRelatives(checkLoc,ad=1,type = 'light',f=1)
            if not lightShapes:
                continue
            for checkLight in lightShapes:
                lightAttr = checkLight + '.aiExposure'
                mc.editRenderLayerAdjustment(lightAttr)
                mc.setAttr(lightAttr,0)
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
        print (u'===============!!!Done 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
        if printMode:print '\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'

        # 清理未知节点
        self.cleanUnknown()
        print '\n'

    #-----------#
    # glass screen
    def rlCHR_HOLO(self,printMode = 0):
       # 物体
        glassObjs = mc.ls('*_c601*Bag*:MSH_c_hi_headset_1_',type='transform',l=1) \
                 + mc.ls('*_c602*Bag*:MSH_c_hi_headset_1_',type='transform',l=1) \
                 + mc.ls('*_p018*Bag*:MSH_c_hi_headset_1_',type='transform',l=1) \
                 + mc.ls('*_p028*Bag*:MSH_c_hi_headset_1_',type='transform',l=1)
        glassObjs = self.renderObjCheck(glassObjs)
        screenObjs = mc.ls('*_c601*Bag*:MSH_c_hi_screen_3_',type='transform',l=1) \
                 + mc.ls('*_c602*Bag*:MSH_c_hi_screen_3_',type='transform',l=1)   \
                 + mc.ls('*_p018*Bag*:MSH_c_hi_screen_3_',type='transform',l=1) \
                 + mc.ls('*_p028*Bag*:MSH_c_hi_screen_3_',type='transform',l=1)
        screenObjs = self.renderObjCheck(screenObjs)
        if not (glassObjs + screenObjs):
            return
        if printMode:print '\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'
        # 初始化
        self.baseSettings(renderer = 'sw')
        # objType
        objDict  = self.objectList()
        setMeshObjs = objDict['setMeshObjs']
        setAssObjs = objDict['setAssObjs']
        chrMeshObjs = objDict['chrMeshObjs']
        prpMeshObjs = objDict['prpMeshObjs']
        skipMeshes = mc.listRelatives((glassObjs + screenObjs),s=1,ni=1,type='mesh',f=1)
        skipSGList = mc.listConnections(skipMeshes,s=0,d=1,type = 'shadingEngine')
        # smooth
        smsNodes = mc.ls('foodSMS_*' ,type = 'polySmoothFace')
        if smsNodes:
            mc.delete(smsNodes)
        for smsObj in (glassObjs+screenObjs):
            mc.select(smsObj)
            polyNewNode = mc.polySmooth(smsObj,  mth=0, dv=2, bnr=1, c=1, kb=0, ksb=1, khe=0, kt=1, kmb=1, suv=1, peh=0, sl=1, dpe=1, ps=0.1, ro=1, ch=1)
            mc.rename(polyNewNode[0],('foodSMS_' + polyNewNode[0]))
        # 素模
        from idmt.maya.commonCore.core_renderLayer import sk_renderLayerCorex
        reload(sk_renderLayerCorex)
        sk_renderLayerCorex.sk_renderLayerCorex().masterLayerLambertShader(shaderType='lambert',skipSGList = skipSGList)
        # Screen
        layerName = 'Screen'
        rlObjs = chrMeshObjs + prpMeshObjs
        if not glassObjs:
            print (u'===============!!!No Objects 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
            self.emptyLayer = layerName
        if mc.ls(layerName):
            mc.delete(layerName)
        mc.createRenderLayer(rlObjs , name=layerName , noRecurse=1 , makeCurrent=1)
        justMeshes = mc.listRelatives(glassObjs,s=1,ni=1,type='mesh',f=1)
        justSGList = mc.listConnections(justMeshes,s=0,d=1,type = 'shadingEngine')
        from idmt.maya.commonCore.core_renderLayer import sk_renderLayerCore
        reload(sk_renderLayerCore)
        sk_renderLayerCore.sk_renderLayerCore().masterLayerLambertShader(shaderType='lambert',justSGList = justSGList,msLayer = 0,Adjustment = 1)
        print (u'===============!!!Done 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
        if printMode:print '\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'
        # Glasses
        layerName = 'Glasses'
        rlObjs = chrMeshObjs + prpMeshObjs
        if not glassObjs:
            print (u'===============!!!No Objects 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
            self.emptyLayer = layerName
        if mc.ls(layerName):
            mc.delete(layerName)
        mc.createRenderLayer(rlObjs , name=layerName , noRecurse=1 , makeCurrent=1)
        justMeshes = mc.listRelatives(screenObjs,s=1,ni=1,type='mesh',f=1)
        justSGList = mc.listConnections(justMeshes,s=0,d=1,type = 'shadingEngine')
        from idmt.maya.commonCore.core_renderLayer import sk_renderLayerCore
        reload(sk_renderLayerCore)
        sk_renderLayerCore.sk_renderLayerCore().masterLayerLambertShader(shaderType='lambert',justSGList = justSGList,msLayer = 0,Adjustment = 1)
        print (u'===============!!!Done 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
        if printMode:print '\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'

    #----------------#
    # BG_CLR
    def rlBG(self,aovForce=0,printMode = 0):
        if printMode:print '\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'
        # 初始化
        self.baseSettings()
        # 导入light
        self.lgtImport(lgtType = 'bg' , update = 1)
        # objType
        objDict  = self.objectList()
        setMeshObjs = objDict['setMeshObjs']
        setFloorObjs = objDict['setFloorObjs']
        setAssObjs = objDict['setAssObjs']
        chrMeshObjs = objDict['chrMeshObjs']
        hairObjs = objDict['hairObjs']
        prpMeshObjs = objDict['prpMeshObjs']
        setLight_clr = objDict['setLight_clr']
        # 导入aov
        self.aovConfig(aovForce)
        #mc.setAttr('defaultArnoldRenderOptions.use_existing_tiled_textures',1)
        # RL start
        layerName = 'BGCLR'
        rlObjs = setMeshObjs + setAssObjs + setLight_clr
        if not rlObjs:
            print (u'===============!!!No Objects 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
            self.emptyLayer = layerName
            return
        if not setLight_clr:
            print (u'===============!!!No Lights 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
            self.emptyLayer = layerName
            return
        if mc.ls(layerName):
            mc.delete(layerName)
        mc.createRenderLayer(rlObjs , name=layerName , noRecurse=1 , makeCurrent=1)
        # sample values
        baseNode = 'defaultArnoldRenderOptions'
        attrDict = {'.AASamples':5,'.GIDiffuseSamples':3,'.GIGlossySamples':2,
                    '.GIRefractionSamples':2,'.GISssSamples':2,'.GIVolumeSamples':2,
                    '.GIDiffuseDepth':2,'.GIGlossyDepth':2,'.GIReflectionDepth':2,'.GIRefractionDepth':2}
        for checkAttr in attrDict.keys():
            nodeAttr = baseNode + checkAttr
            mc.editRenderLayerAdjustment(nodeAttr)
            mc.setAttr(nodeAttr,attrDict[checkAttr])
        if mc.ls('*_s613001*:MODEL'):
            nodeAttr = 'defaultArnoldRenderOptions.AASamples'
            mc.setAttr(nodeAttr,4)
        # format
        checkAttr = 'defaultArnoldDriver.tiffFormat'
        mc.editRenderLayerAdjustment(checkAttr)
        mc.setAttr(checkAttr,1)
        # 清理未知节点
        self.cleanUnknown()
        print (u'===============!!!Done 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
        if printMode:print '\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'
        print '\n'

    #--------------#
    # BG_RGB [素模]
    def rlBG_RGB(self,printMode = 1):
        if printMode:print '\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'
        # 初始化
        self.baseSettings()
        # 素模
        from idmt.maya.commonCore.core_renderLayer import sk_renderLayerCore
        reload(sk_renderLayerCore)
        sk_renderLayerCore.sk_renderLayerCore().masterLayerLambertShader(shaderType='ar')
        # 导入light
        self.lgtImport(lgtType = 'bg' , update = 1)
        # objType
        objDict  = self.objectList()
        setMeshObjs = objDict['setMeshObjs']
        setFloorObjs = objDict['setFloorObjs']
        setAssObjs = objDict['setAssObjs']
        chrMeshObjs = objDict['chrMeshObjs']
        hairObjs = objDict['hairObjs']
        prpMeshObjs = objDict['prpMeshObjs']
        setLight_rgb = objDict['setLight_rgb']
        # RL start
        layerName = 'BGRGB'
        rlObjs = setMeshObjs + setAssObjs + setLight_rgb
        if not rlObjs:
            print (u'===============!!!No Objects 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
            self.emptyLayer = layerName
            return
        if not setLight_rgb:
            print (u'===============!!!No Lights 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
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
        attrDict = {'.AASamples':5,'.GIDiffuseSamples':3,'.GIGlossySamples':0,
                    '.GIRefractionSamples':0,'.GISssSamples':0,'.GIVolumeSamples':0,
                    '.GIDiffuseDepth':0,'.GIGlossyDepth':0,'.GIReflectionDepth':0,'.GIRefractionDepth':0}
        for checkAttr in attrDict.keys():
            nodeAttr = baseNode + checkAttr
            mc.editRenderLayerAdjustment(nodeAttr)
            mc.setAttr(nodeAttr,attrDict[checkAttr])
        # 清理未知节点
        self.cleanUnknown()
        print (u'===============!!!Done 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
        if printMode:print '\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'
        print '\n'

    #--------------#
    # BG_FOG [素模]
    def rlBG_FOG(self,printMode = 0):
        if printMode:print '\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'
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
            print (u'===============!!!No Objects 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
            self.emptyLayer = layerName
            return
        if not envLight_fog:
            print (u'===============!!!No Lights 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
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
        print (u'===============!!!Done 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
        if printMode:print '\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'
        print '\n'

    #--------------#
    # BG_CAU [素模]
    def rlBG_CAU(self,printMode = 0):
        if printMode:print '\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'
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
            print (u'===============!!!No Objects 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
            self.emptyLayer = layerName
            return
        if not envLight_cau:
            print (u'===============!!!No Lights 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
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
        print (u'===============!!!Done 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
        if printMode:print '\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'
        print '\n'

    #--------------#
    # BG_VFX  [素模]  # 使用matte材质球
    def rlBG_VFX(self,printMode = 0):
        if printMode:print '\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'
        # 初始化
        self.baseSettings()
        # 素模
        from idmt.maya.commonCore.core_renderLayer import sk_renderLayerCore
        reload(sk_renderLayerCore)
        sk_renderLayerCore.sk_renderLayerCore().masterLayerLambertShader(coNode=self.matteShader,shaderType='surfaceShader')
        # vfx文件导入
        self.vfxImport()
        if printMode:print '-------001'
        # 导入light
        self.lgtImport(lgtType = 'bg',update = 1)
        if printMode:print '-------002'
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
            print (u'===============!!!No Objects 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
            self.emptyLayer2 = layerName
            createState = 0
        if not fishGrp:
            print (u'===============!!!No Objects 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
            self.emptyLayer2 = layerName
            createState = 0
        if not setLight_clr:
            print (u'===============!!!No Lights 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
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
            print (u'===============!!!No Objects 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
            self.emptyLayer = layerName
            createState = 0
        if not dustGrp:
            print (u'===============!!!No Objects 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
            self.emptyLayer = layerName
            createState = 0
        if not setLight_clr:
            print (u'===============!!!No Lights 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
            self.emptyLayer = layerName
            createState = 0
        if createState:
            if mc.ls(layerName):
                mc.delete(layerName)
            if printMode:print '-------003'
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
        print (u'===============!!!Done 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
        if printMode:print '\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'
        print '\n'

    #-----------#
    # all idp Layer [素模]
    def rlAllIdp(self,printMode = 0):
        if printMode:print '\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'
        # 初始化
        self.baseSettings()
        # 素模
        from idmt.maya.commonCore.core_renderLayer import sk_renderLayerCore
        reload(sk_renderLayerCore)
        sk_renderLayerCore.sk_renderLayerCore().masterLayerLambertShader(shaderType='ar')
        # 导入light
        #self.lgtImport()
        # objType
        objDict  = self.objectList()
        setMeshObjs = objDict['setMeshObjs']
        setFloorObjs = objDict['setFloorObjs']
        setAssObjs = objDict['setAssObjs']
        chrMeshObjs = objDict['chrMeshObjs']
        hairObjs = objDict['hairObjs']
        prpMeshObjs = objDict['prpMeshObjs']
        # 删除aov
        self.aovClean()
        #-----------#
        # all idp [素模]
        layerName = 'ALLIDP'
        rlObjs = chrMeshObjs + prpMeshObjs + setMeshObjs + setAssObjs
        if not rlObjs:
            print (u'===============!!!No Objects 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
            self.emptyLayer = layerName
            return
        if mc.ls(layerName):
            mc.delete(layerName)
        mc.createRenderLayer(rlObjs , name=layerName , noRecurse=1 , makeCurrent=1)
        # rgb
        #-----------#
        # chr,prp,set  RGB [素模]
        rgbList = self.aovCreateRGBNodes()
        cpsAov = self.aovRGBCreatCore([chrMeshObjs,prpMeshObjs,setMeshObjs],rgbList,'Cps',aiSetMode = 0 )
        for checkAov in cpsAov:
            aovAttr = checkAov + '.enabled'
            mc.editRenderLayerAdjustment(aovAttr)
            mc.setAttr(aovAttr,1)
        #-----------#
        # chr idp [素模]
        layerName = 'CHRIDP'
        rlObjs = chrMeshObjs + prpMeshObjs
        if not rlObjs:
            print (u'===============!!!No Objects 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
            self.emptyLayer = layerName
            return
        if mc.ls(layerName):
            mc.delete(layerName)
        mc.createRenderLayer(rlObjs , name=layerName , noRecurse=1 , makeCurrent=1)
        chrAov = []
        for checkType in ['c','p']:
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
        print (u'===============!!!Done 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
        #-----------#
        # bg idp [素模]
        layerName = 'BGIDP'
        rlObjs = setMeshObjs + setAssObjs
        if not rlObjs:
            print (u'===============!!!No Objects 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
            self.emptyLayer = layerName
            return
        if mc.ls(layerName):
            mc.delete(layerName)
        mc.createRenderLayer(rlObjs , name=layerName , noRecurse=1 , makeCurrent=1)
        setAov = []
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
        # sample values
        baseNode = 'defaultArnoldRenderOptions'
        attrDict = {'.AASamples':5,'.GIDiffuseSamples':0,'.GIGlossySamples':0,
                    '.GIRefractionSamples':0,'.GISssSamples':0,'.GIVolumeSamples':0,
                    '.GIDiffuseDepth':0,'.GIGlossyDepth':0,'.GIReflectionDepth':0,'.GIRefractionDepth':0}
        for checkAttr in attrDict.keys():
            nodeAttr = baseNode + checkAttr
            mc.setAttr(nodeAttr,attrDict[checkAttr])
        if printMode:print '\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'

    #------------------#
    # 获取所有aiMsk的信息
    # set组明名: namespace:aiMSK_idpName_TypeRGB
    # 如:mi_c002002Teethless_h:aiMSK_TL_CHRR
    def aovRGBGetSetList2(self,assetType):
        allSetList = mc.ls('*:aiMSK_*',type = 'objectSet')
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
    # set组明名: namespace:aiMSK_idpName_TypeRGB
    # 如:mi_c002002Teethless_h:aiMSK_TL_CHRR
    def aovRGBGetSetList(self,assetType):
        allSetList = mc.ls('*:aiMSK_*',type = 'objectSet')
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
    def aovCreateRGBNodes(self):
        # rebuild rgb
        RColor = 'R_aiColor_do6'
        GColor = 'G_aiColor_do6'
        BColor = 'B_aiColor_do6'
        RColorTR = 'R_aiColor_TR_do6'
        GColorTR = 'G_aiColor_TR_do6'
        BColorTR = 'B_aiColor_TR_do6'

        if not mc.ls(RColor):
            mc.shadingNode('aiUserDataColor', asShader=1,name = RColor)
        if not mc.ls(GColor):
            mc.shadingNode('aiUserDataColor', asShader=1,name = GColor)
        if not mc.ls(BColor):
            mc.shadingNode('aiUserDataColor', asShader=1,name = BColor)
        if not mc.ls(RColorTR):
            mc.shadingNode('aiStandard', asShader=1,name = RColorTR)
        if not mc.ls(GColorTR):
            mc.shadingNode('aiStandard', asShader=1,name = GColorTR)
        if not mc.ls(BColorTR):
            mc.shadingNode('aiStandard', asShader=1,name = BColorTR)

        mc.setAttr(RColor+'.defaultValue',1,0,0,typ='double3')
        mc.setAttr(GColor+'.defaultValue',0,1,0,typ='double3')
        mc.setAttr(BColor+'.defaultValue',0,0,1,typ='double3')
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
            print '-------'
            print aovName
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
            #print '--------switchInfo'
            #print aiMasksSets[aiSetNum:aiSetNum+cycleNum]
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
                    if checkType in ['mesh']:
                        obj = mc.listRelatives(obj,p=1,type='transform',f=1)[0]
                    shape = mc.listRelatives(obj,s=1,type = 'mesh',ni=1,f=1)
                    if not shape:
                        continue
                    shape = shape[0]
                    inpt = mc.getAttr(tSwitch+'.input',s=1)
                    mc.connectAttr(shape+'.instObjGroups[0]',tSwitch+'.input['+str(inpt)+'].inShape',f=1)

                    noTrState = mc.getAttr(shape+'.aiOpaque')
                    #if noTrState:
                    mc.connectAttr(aiColor+'.outColor',tSwitch+'.input['+str(inpt)+'].inTriple',f=1)
                    #else:
                    #    mc.connectAttr(aiColors[num % cycleNum + cycleNum]+'.outColor',tSwitch+'.input['+str(inpt)+'].inTriple',f=1)
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

    #-------------#
    # 环境球创建
    def rlSkyEnv(self,forceBuild = 0,printMode = 0):
        if printMode:print '\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'
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
            print '-----[%s]_[Start]!!!'%shotID
            if printMode:print '\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'
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
                print '-----[%s]_[Pass]!!!'%shotID
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
            print '-----[%s]_[Done]!!!'%shotID
        print '-----[ALL]_[Done]!!!'
        if printMode:print '\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'

    #-----------------------------#
    # 背包处理
    def bagWeaponFix(self):
        # shotList
        shotList = ['009_0350', '009_0400', '009_0410', '009_0420', '009_0440',
                     '009_0460', '009_0480', '009_0492', '009_0500', '009_0520',
                     '009_0560', '009_0570', '009_0590', '009_0600', '009_0610',
                     '009_0630', '009_0640', '009_0650', '009_0660', '009_0670',
                     '009_0680', '009_0690', '009_0700', '009_0710', '009_0720',
                     '009_0730', '009_0740', '009_0750', '009_0760', '009_0770',
                     '009_0780', '009_0790', '009_0805', '009_0812', '009_0820',
                     '009_0850', '009_0880', '009_0960', '009_0980', '009_0990',
                     '009_1000', '010_0005', '010_0010', '010_0100', '010_0110',
                     '010_0210', '010_0220', '010_0240', '010_0260', '010_0270',
                     '010_0280', '010_0290', '010_0310', '010_0330', '010_0340',
                     '010_0350', '010_0360', '010_0370', '010_0380', '010_0390',
                     '010_0400', '012_0020', '012_0400', '012_0410', '012_0500',
                     '012_0520', '012_0530', '012_0540', '012_0550', '012_0570',
                     '012_0600', '018_0010', '018_0020', '018_0030', '018_0040',
                     '018_0070', '018_0080', '018_0090', '018_0100', '018_0110',
                     '018_0120', '018_0130', '018_0140', '018_0145', '018_0150',
                     '018_0160', '018_0170', '018_0600', '018_0630', '018_0640',
                     '021_1070', '021_1090', '021_1100', '024_0190', '024_0200',
                     '024_0290', '024_0320', '024_0350', '024_0370', '024_0390',
                     '024_0400', '024_0430', '024_0440', '024_0450', '024_0570',
                     '024_0580', '024_0590', '024_0601', '024_0603', '024_0660',
                     '024_0680', '024_0690', '024_0710', '024_0730', '024_0740',
                     '024_0760', '024_0870', '024_0890', '024_0910', '024_0920',
                     '024_1030', '026a_0100', '026a_0120', '026a_0130', '026a_0280',
                     '026a_0290', '026a_0310', '026a_0320', '026a_0360', '026a_0440',
                     '026b_0180', '026b_0200', '026b_0210', '026b_0220', '026b_0370',
                     '026b_0420', '026b_0430', '026b_0440', '026b_0445', '026b_0450',
                     '026b_0455', '026b_0500', '026b_0540', '026b_0610', '026b_0640',
                     '026b_0670', '026b_0960', '026b_0980', '026b_1040', '026b_1120',
                     '026b_1125', '026b_1140', '026b_1160', '026b_1190', '026b_1260',
                     '027_0690', '027_0700', '027_0710', '027_0730']
        shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
        shotNID = '%s_%s'%(shotInfos[1],shotInfos[2])
        if shotNID in shotList:
            return
        # fix
        checkNsList = ['p018001','p028001','c601002','c602002']
        nsList = mc.namespaceInfo(listOnlyNamespaces=1)
        for checkNs in nsList:
            if '_sysTemp_' in checkNs:
                continue
            needState = 0
            for checkKey in checkNsList:
                if checkKey in checkNs:
                    needState = 1
            if not needState:
                continue
            checkGrp = mc.ls('%s:MSH_c_hi_weapon'%checkNs,l=1)
            if checkGrp:
                mc.setAttr(checkGrp[0]+'.v',0)

    # NaN处理
    def fixWeaponNanObjs(self,save = 0):
        errorObjs = []
        attrList = ['.tx','.ty','.tz','.rx','.ry','.rz','.sx','.sy','.sz']
        modelGrp = mc.ls('*:MSH_c_hi_weapon',type = 'transform',l=1)
        if not modelGrp:
            return
        checkGrps = mc.listRelatives(modelGrp,ad=1,type='transform',f=1)
        if not checkGrps:
            return
        for checkGrp in checkGrps:
            errorState = 0
            for attr in attrList:
                value = mc.getAttr(checkGrp+attr)
                if value != value:
                    errorState = 1
                if errorState:
                    if checkGrp not in errorObjs:
                        errorObjs.append(checkGrp)
                    continue
        for checkObj in errorObjs:
            mc.setAttr(checkObj+'.v',0)
        if save:
            mc.file(s=1,f=1)