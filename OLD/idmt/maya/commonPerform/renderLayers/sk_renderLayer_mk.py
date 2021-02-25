# -*- coding: utf-8 -*-
# 【通用】【mk项目】
#  Author : 沈康
#  Data   : 2017
import maya.cmds as mc
import maya.mel as mel
from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
reload(sk_infoConfig)

class sk_renderLayer_mk(object):

    def __init__(self):
        self.aovFilePath = 'Z:/Projects/MonkeyKing/MonkeyKing_Scratch/TD/AOV/mk_AOV.mb'

    def baseSettings(self):
        if not mc.pluginInfo('mtoa.mll',q=1,loaded = 1):
            mc.loadPlugin('mtoa.mll')
        import mtoa
        mtoa.core.createOptions()
        import mtoa.cmds.registerArnoldRenderer
        mtoa.cmds.registerArnoldRenderer.registerArnoldRenderer()
        mc.setAttr('defaultRenderGlobals.currentRenderer', 'arnold', type='string')
        # 标准设置
        mc.setAttr('defaultRenderGlobals.imageFormat', 7)
        mc.setAttr('defaultArnoldDriver.halfPrecision', 0)

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

        # arnold配置
        mc.setAttr('defaultArnoldRenderOptions.lock_sampling_noise', 0)

        # camera
        cameras = mc.ls(type = 'camera',l=1)
        for camShape in cameras:
            mc.setAttr((camShape + '.renderable'),0)
        mc.setAttr('CAM:stereoCameraRightShape.renderable',1)
        mc.setAttr('CAM:stereoCameraLeftShape.renderable',1)

        # yeti config
        yetiPath = 'C:\\tools\LocalTools\\3partPlugin\\2016\Yeti\\2.0.24\\bin'
        mc.setAttr('defaultArnoldRenderOptions.procedural_searchpath',yetiPath,type='string')
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
        from idmt.maya.commonCore.core_renderLayer import sk_renderLayerCore
        reload(sk_renderLayerCore)
        sk_renderLayerCore.sk_renderLayerCore().blendShapeUpdateInfo()

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
        # 场景代理
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
        # 角色模型
        chrMeshObjs = mc.listRelatives('CHR_GRP',ad=1,type='mesh',f=1)
        if chrMeshObjs:
            chrMeshObjs = mc.listRelatives(chrMeshObjs,p=1,type='transform',f=1)
            chrMeshObjs = list(set(chrMeshObjs))
        else:
            chrMeshObjs = []
        otherMeshes = mc.ls('mk_cBullKingBnew_TShirt*:*',type='mesh',l=1)
        if otherMeshes:
            otherObjs = mc.listRelatives(otherMeshes,p=1,type='transform',f=1)
            otherObjs = list(set(otherObjs))
        else:
            otherObjs = []
        objListDict['chrMeshObjs'] = chrMeshObjs + otherObjs
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
        # 场景灯光 大组
        setLight = ['set_Light']
        if not mc.ls(setLight):
            setLight = []
        objListDict['setLight'] = setLight
        # 角色灯光 大组
        chrLight = ['chr_Light']
        if not mc.ls(chrLight):
            chrLight = []
        objListDict['chrLight'] = chrLight
        return objListDict

    # AOV处理
    def aovConfig(self,force = 0):
        aovState = 0
        aovNodes = mc.ls(type= 'aiAOV')
        if aovNodes:
            aovState = 1
        if not aovState or force:
            mc.file(self.aovFilePath,i=1)

    # aov清理
    def aovClean(self):
        aovNodes = mc.ls(type= 'aiAOV')
        if aovNodes:
            mc.delete(aovNodes)

    def rlBG(self,aovForce=0):
        # objType
        objDict  = self.objectList()
        setMeshObjs = objDict['setMeshObjs']
        setAssObjs = objDict['setAssObjs']
        chrMeshObjs = objDict['chrMeshObjs']
        hairObjs = objDict['hairObjs']
        prpMeshObjs = objDict['prpMeshObjs']
        setLight = objDict['setLight']
        chrLight = objDict['chrLight']
        self.baseSettings()
        # 导入aov
        self.aovConfig(aovForce)
        # 导入场景灯
        # RL start
        layerName = 'BG'
        rlObjs = setMeshObjs + setAssObjs + setLight
        if not rlObjs:
            print (u'===============!!!No Objects 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
            return
        if mc.ls(layerName):
            mc.delete(layerName)
        mc.createRenderLayer(rlObjs , name=layerName , noRecurse=1 , makeCurrent=1)
        # sample values
        baseNode = 'defaultArnoldRenderOptions'
        attrDict = {'.AASamples':6,'.GIDiffuseSamples':8,'.GIGlossySamples':4,
                    '.GIRefractionSamples':2,'.GISssSamples':2,'.GIVolumeSamples':2}
        for checkAttr in attrDict.keys():
            nodeAttr = baseNode + checkAttr
            print attrDict[checkAttr]
            mc.editRenderLayerAdjustment(nodeAttr)
            mc.setAttr(nodeAttr,attrDict[checkAttr])
        # 渲染属性
        for checkObj in setAssObjs:
            checkShape = mc.listRelatives(checkObj,s=1,f=1,ni=1)[0]
            mc.setAttr(checkShape+'.overridePrimaryVisibility',1)
            mc.setAttr(checkShape+'.primaryVisibility',0)
        print (u'===============!!!Done 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
        print '\n'

    def rlCHR(self,aovForce = 0):
        # objType
        objDict  = self.objectList()
        setMeshObjs = objDict['setMeshObjs']
        setAssObjs = objDict['setAssObjs']
        chrMeshObjs = objDict['chrMeshObjs']
        hairObjs = objDict['hairObjs']
        prpMeshObjs = objDict['prpMeshObjs']
        setLight = objDict['setLight']
        chrLight = objDict['chrLight']
        self.baseSettings()
        # 导入aov
        self.aovConfig(aovForce)
        # 导入角色灯
        # RL start
        layerName = 'CHR'
        rlObjs = chrMeshObjs + prpMeshObjs + setMeshObjs + chrLight
        if not rlObjs:
            print (u'===============!!!No Objects 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
            return
        if mc.ls(layerName):
            mc.delete(layerName)
        mc.createRenderLayer(rlObjs , name=layerName , noRecurse=1 , makeCurrent=1)
        # sample values
        baseNode = 'defaultArnoldRenderOptions'
        attrDict = {'.AASamples':6,'.GIDiffuseSamples':8,'.GIGlossySamples':4,
                    '.GIRefractionSamples':2,'.GISssSamples':8,'.GIVolumeSamples':2}
        for checkAttr in attrDict.keys():
            nodeAttr = baseNode + checkAttr
            mc.editRenderLayerAdjustment(nodeAttr)
            mc.setAttr(nodeAttr,attrDict[checkAttr])
        # 渲染属性
        for checkObj in setMeshObjs:
            checkShape = mc.listRelatives(checkObj,s=1,f=1,ni=1)[0]
            checkAttr = checkShape+'.aiMatte'
            mc.editRenderLayerAdjustment(checkAttr)
            mc.setAttr(checkAttr,1)
        print (u'===============!!!Done 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
        print '\n'

    def rlAss(self,aovForce = 0):
        # objType
        objDict  = self.objectList()
        setMeshObjs = objDict['setMeshObjs']
        setAssObjs = objDict['setAssObjs']
        chrMeshObjs = objDict['chrMeshObjs']
        hairObjs = objDict['hairObjs']
        prpMeshObjs = objDict['prpMeshObjs']
        setLight = objDict['setLight']
        chrLight = objDict['chrLight']
        self.baseSettings()
        # 导入aov
        self.aovConfig(aovForce)
        # 导入场景灯
        # RL start
        layerName = 'ASS'
        rlObjs = setAssObjs + setMeshObjs + setLight
        if not rlObjs:
            print (u'===============!!!No Objects 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
            return
        if mc.ls(layerName):
            mc.delete(layerName)
        mc.createRenderLayer(rlObjs , name=layerName , noRecurse=1 , makeCurrent=1)
        # 渲染属性
        for checkObj in setMeshObjs:
            checkShape = mc.listRelatives(checkObj,s=1,f=1,ni=1)[0]
            checkAttr = checkShape+'.aiMatte'
            mc.editRenderLayerAdjustment(checkAttr)
            mc.setAttr(checkAttr,1)
        # sample values
        baseNode = 'defaultArnoldRenderOptions'
        attrDict = {'.AASamples':6,'.GIDiffuseSamples':8,'.GIGlossySamples':4,
                    '.GIRefractionSamples':2,'.GISssSamples':2,'.GIVolumeSamples':2}
        for checkAttr in attrDict.keys():
            nodeAttr = baseNode + checkAttr
            mc.editRenderLayerAdjustment(nodeAttr)
            mc.setAttr(nodeAttr,attrDict[checkAttr])
        # aov属性
        needAovList = ['direct_diffuse','direct_specular','indirect_diffuse','indirect_specular']
        for checkAov in mc.ls(type='aiAOV'):
            aovName = mc.getAttr(checkAov+'.name')
            checkAttr = checkAov+'.enabled'
            if aovName not in needAovList:
                mc.editRenderLayerAdjustment(checkAttr)
                mc.setAttr(checkAttr,0)
        print (u'===============!!!Done 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
        print '\n'

    def rlHair(self,aovForce = 0):
        # objType
        objDict  = self.objectList()
        setMeshObjs = objDict['setMeshObjs']
        setAssObjs = objDict['setAssObjs']
        chrMeshObjs = objDict['chrMeshObjs']
        hairObjs = objDict['hairObjs']
        prpMeshObjs = objDict['prpMeshObjs']
        setLight = objDict['setLight']
        chrLight = objDict['chrLight']
        self.baseSettings()
        # 导入aov
        self.aovConfig(aovForce)
        # 导入场景灯
        # RL start
        layerName = 'HAIR'
        rlObjs = hairObjs + setMeshObjs + chrMeshObjs + prpMeshObjs + chrLight
        if not rlObjs:
            print (u'===============!!!No Objects 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
            return
        if mc.ls(layerName):
            mc.delete(layerName)
        mc.createRenderLayer(rlObjs , name=layerName , noRecurse=1 , makeCurrent=1)
        # 渲染属性
        for checkObj in (setMeshObjs+chrMeshObjs+prpMeshObjs):
            checkShape = mc.listRelatives(checkObj,s=1,f=1,ni=1)[0]
            checkAttr = checkShape+'.aiMatte'
            mc.editRenderLayerAdjustment(checkAttr)
            mc.setAttr(checkAttr,1)
        # sample values
        baseNode = 'defaultArnoldRenderOptions'
        attrDict = {'.AASamples':6,'.GIDiffuseSamples':8,'.GIGlossySamples':4,
                    '.GIRefractionSamples':2,'.GISssSamples':2,'.GIVolumeSamples':2}
        for checkAttr in attrDict.keys():
            nodeAttr = baseNode + checkAttr
            mc.editRenderLayerAdjustment(nodeAttr)
            mc.setAttr(nodeAttr,attrDict[checkAttr])
        # aov属性
        needAovList = ['AO','Normal','direct_diffuse','direct_specular','fre','motionvector']
        for checkAov in mc.ls(type='aiAOV'):
            aovName = mc.getAttr(checkAov+'.name')
            checkAttr = checkAov+'.enabled'
            if aovName not in needAovList:
                mc.editRenderLayerAdjustment(checkAttr)
                mc.setAttr(checkAttr,0)
        print (u'===============!!!Done 【RL】【%s】!!!===============' % (u'%s_层' % layerName))
        print '\n'