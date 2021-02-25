# -*- coding: utf-8 -*-

'''
Created on 2014-3-20

@author: shenkang
'''
import maya.cmds as mc
import maya.mel as mel
import idmt.pipeline.db

# shader import
# file nodes ,for tga ,filter off ,for map ,filter config minmap

from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
reload(sk_infoConfig)

class sk_renderLayer_ShunLiu(object):

    def __init__(self):
        pass

    # UIZMRenderLayer
    def sk_UIZoomWhiteDolphinRenderLayersLayers(self):
        # 窗口
        if mc.window("sk_sceneUIZoomWhiteDolphinRenderLayers", ex=1):
            mc.deleteUI("sk_sceneUIZoomWhiteDolphinRenderLayers", window=True)
        mc.window("sk_sceneUIZoomWhiteDolphinRenderLayers", title="ShunLiu RenderLayers Tools", widthHeight=(500, 350), menuBar=0)
        # 主界面
        mc.columnLayout()

        # 分解创建
        mc.frameLayout(label=u'[MR]RenderLayers Ganeral | 通用设置', borderStyle='etchedOut', width=500)

        mc.rowLayout(numberOfColumns=4, columnWidth4=(100, 100, 100, 100))
        mc.button(l=u'工程目录设置', bgc=[0.3, 0.3, 0.3], width=100, height=25, c='mel.eval(\'source "//file-cluster/GDC/Resource/Support/Maya/projects/VickytheViking/vvSetProject.mel"\')\nmel.eval(\"vvSetProject\")')
        mc.button(l=u'Zdepth设置', bgc=[0.3, 0.3, 0.3], width=100, height=25, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.slRLConfig().slRLayerZdepthDistanceConfigUI()')
        mc.button(l=u'', bgc=[0.3, 0.3, 0.3], width=100, height=25)
        mc.button(l=u'', bgc=[0.3, 0.3, 0.3], width=100, height=25)
        mc.setParent("..")

        mc.setParent("..")

        # 分解创建
        mc.frameLayout(label=u'[MR]RenderLayers Manual | 手动创建RenderLayers', borderStyle='etchedOut', width=500)

        mc.rowLayout(numberOfColumns=4, columnWidth4=(100, 100, 100, 100))
        mc.button(l=u'[CHR]CAUSTICS', bgc=[0.1, 0.1, 0.1], width=100, height=25, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.slRLConfig().slRLSpeficCreate(\"CHR_CAUSTICS\")')
        mc.button(l=u'[BG]CAUSTICS', bgc=[0.1, 0.1, 0.1], width=100, height=25, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.slRLConfig().slRLSpeficCreate(\"BG_CAUSTICS\")')
        mc.button(l=u'[FG]CO', bgc=[0.1, 0.1, 0.1], width=100, height=25, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.slRLConfig().slRLSpeficCreate(\"FG_CO\")')
        mc.button(l=u'[BG]CO', bgc=[0.1, 0.1, 0.1], width=100, height=25, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.slRLConfig().slRLSpeficCreate(\"BG_CO\")')
        mc.setParent("..")

        mc.rowLayout(numberOfColumns=4, columnWidth4=(100, 100, 100, 100))
        mc.button(l=u'[ALL]Zdepth', bgc=[0.1, 0.1, 0.1], width=100, height=25, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.slRLConfig().slRLSpeficCreate(\"ALL_ZDEPTH\")')
        mc.button(l=u'[ALL]Mask01', bgc=[0.1, 0.1, 0.1], width=100, height=25, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.slRLConfig().slRLSpeficCreate(\"ALL_MASK01\")')
        mc.button(l=u'[BG]Mask', bgc=[0.1, 0.1, 0.1], width=100, height=25, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.slRLConfig().slRLSpeficCreate(\"BG_MASK02\")')
        mc.button(l=u'[SEA]CP', bgc=[0.1, 0.1, 0.1], width=100, height=25, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.slRLConfig().slRLSpeficCreate(\"SEA_CP\")')
        mc.setParent("..")

        mc.rowLayout(numberOfColumns=4, columnWidth4=(100, 100, 100, 100))
        mc.button(l=u'[==wait==]', bgc=[0.1, 0.1, 0.1], width=100, height=25)
        mc.button(l=u'[FG]LGT', bgc=[0.1, 0.1, 0.1], width=100, height=25, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.slRLConfig().slRLSpeficCreate(\"FG_LGT\")')
        mc.button(l=u'[SEA]SHDW', bgc=[0.1, 0.1, 0.1], width=100, height=25, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.slRLConfig().slRLSpeficCreate(\"SEA_SHDW\")')
        mc.button(l=u'[SEA]MSK', bgc=[0.1, 0.1, 0.1], width=100, height=25, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.slRLConfig().slRLSpeficCreate(\"SEA_MSK\")')
        mc.setParent("..")

        mc.rowLayout(numberOfColumns=4, columnWidth4=(100, 100, 100, 100))
        mc.button(l=u'[CHR]LGTR', bgc=[0.1, 0.1, 0.1], width=100, height=25, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.slRLConfig().slRLSpeficCreate(\"CHR_LGTR\")')
        mc.button(l=u'[CHR]LGTL', bgc=[0.1, 0.1, 0.1], width=100, height=25, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.slRLConfig().slRLSpeficCreate(\"CHR_LGTL\")')
        mc.button(l=u'[CHR]LGTB', bgc=[0.1, 0.1, 0.1], width=100, height=25, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.slRLConfig().slRLSpeficCreate(\"CHR_LGTB\")')
        mc.button(l=u'[CHR]LGTKEY', bgc=[0.1, 0.1, 0.1], width=100, height=25, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.slRLConfig().slRLSpeficCreate(\"CHR_LGTKEY\")')
        mc.setParent("..")

        mc.rowLayout(numberOfColumns=4, columnWidth4=(100, 100, 100, 100))
        mc.button(l=u'[ALL]PREVIEW', bgc=[0.1, 0.1, 0.1], width=100, height=25, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.slRLConfig().slRLSpeficCreate(\"ALL_PREVIEW\")')
        mc.button(l=u'[ALL]NM', bgc=[0.1, 0.1, 0.1], width=100, height=25, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.slRLConfig().slRLSpeficCreate(\"ALL_NM\")')
        mc.button(l=u'[CHR]LINE', bgc=[0.1, 0.1, 0.1], width=100, height=25, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.slRLConfig().slRLSpeficCreate(\"CHR_LINE\")')
        mc.button(l=u'[BG]Zdepth', bgc=[0.1, 0.1, 0.1], width=100, height=25, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.slRLConfig().slRLSpeficCreate(\"BG_ZDEPTH\")')
        mc.setParent("..")

        mc.setParent("..")

        # Arnold
        mc.frameLayout(label=u'[Arnold]RenderLayers Manual | 手动创建RenderLayers', borderStyle='etchedOut', width=500)

        mc.rowLayout(numberOfColumns=4, columnWidth4=(100, 100, 100, 100))
        mc.button(l=u'[Main]AO层', bgc=[0.1, 0.1, 0.1], width=100, height=25, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.slRLConfig().slRLSpeficCreate(\"ALL_AO\",\"\",0,1)')
        mc.button(l=u'[Main]NM层', bgc=[0.1, 0.1, 0.1], width=100, height=25, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.slRLConfig().slRLSpeficCreate(\"ALL_NM\",\"\",0,1)')
        mc.button(l=u'[==wait==]', bgc=[0.1, 0.1, 0.1], width=100, height=25)
        mc.button(l=u'[==wait==]', bgc=[0.1, 0.1, 0.1], width=100, height=25)
        mc.setParent("..")

        mc.setParent("..")

        mc.frameLayout(label=u'[Tools]RenderLayers Other Tools ', borderStyle='etchedOut', width=500)
        mc.rowLayout(numberOfColumns=4, columnWidth4=(100, 100, 100, 100))
        mc.button(l=u'[Shader]R', bgc=[0.8, 0.1, 0.1], width=100, height=25, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.slRLConfig().zmRGBMShaderCreate(\"R\")')
        mc.button(l=u'[Shader]G', bgc=[0.1, 0.8, 0.1], width=100, height=25, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.slRLConfig().zmRGBMShaderCreate(\"G\")')
        mc.button(l=u'[Shader]B', bgc=[0.1, 0.6, 0.8], width=100, height=25, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.slRLConfig().zmRGBMShaderCreate(\"B\")')
        mc.button(l=u'[Shader]M', bgc=[0.0, 0.0, 0.0], width=100, height=25, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.slRLConfig().zmRGBMShaderCreate(\"M\")')
        mc.setParent("..")
        mc.setParent("..")

        mc.setParent("..")
        mc.showWindow("sk_sceneUIZoomWhiteDolphinRenderLayers")

    # Auto Create
    def slRLAutoCreate(self, render2D=1, PFX=1):
        print ('=================================================================')
        print '====================!!!Start AutoRenderLayer!!!===================='

        # Back To MasterLayer
        mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')
        # clean renderlayer
        from idmt.maya.commonCore.core_mayaCommon import sceneTools
        reload(sceneTools)
        sceneTools.sceneTools().checkCleanRenderLayers()
        # clean unknown nodes
        sceneTools.sceneTools().checkDonotNodeCleanBase(0)
        # renderpass Create
        self.slRLRenderPass()
        # common Setting
        self.slRLCommonConfig()
        # arnold Setting
        self.arnoldRendererSettings()
        # mr Setting
        self.mentalRayProductionLevel()

        # Step 1：RGB,BW,SPEC,RIM

        # Color
        self.slRLCOCreate()
        # Ambient Occlusion
        self.slRLAOCreate()
        # Normal
        self.slRLNMCreate()
        # SPEC
        self.slRLSPECCreate()
        # RIM
        self.slRLRIMLIGHTCreate()
        # Light
        self.slRLLIGHTCreate()
        # ZDepth
        self.slRLZDEPTHCreate()

        # smoothSet
        self.slRLDoSmooth()
        # Back To MasterLayer
        mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')
        # Unrender MasterLayer
        mc.setAttr("defaultRenderLayer.renderable", 0)
        # mc.setAttr
        # common Setting
        self.slRLCommonConfig()
        # save
        self.slRLSave('auto_01')

        # Step 2：Light,ZDepth,BG_RGB

        # smoothSet
        self.slRLDoSmooth()
        # Back To MasterLayer
        mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')
        # Unrender MasterLayer
        mc.setAttr("defaultRenderLayer.renderable", 0)
        # camSetting
        self.slRLCamSetting()
        # common Setting
        # self.slRLCommonConfig()
        # save
        self.slRLSave('auto_02')

        print '=======================!!!All Done!!!======================='
        print ('===========================================================')

    # Create Single Render Layer
    def slRLSpeficCreate(self, renderLayer, saveMode='', selectMode=0, renderSetting =[0,1]):
        print (u'===============!!!Start 【%s】!!!===============' % (renderLayer))
        print 'Working...'

        from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools
        reload(sk_sceneTools)

        # Back To MasterLayer
        mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')

        cacheFiles = mc.ls(type='cacheFile')
        # clean Unknwon Nodes
        #sk_sceneTools.sk_sceneTools().checkDonotNodeCleanBase(0)

        # common Setting
        self.slRLCommonConfig()

        # mr Setting
        if renderSetting[0]:
            self.mentalRayProductionLevel()

        # arnold Setting
        if renderSetting[1]:
            self.arnoldRendererSettings()

        # 指定层
        BGType = renderLayer.split('_')[0]
        layerType = renderLayer.split('_')[1]
        try:
            mc.delete(renderLayer)
        except:
            pass

        # self.slRLExrConfig()
        '''
        # 优先处理master层
        if layerType not in ['COLOR', 'CO', 'SHADOW', 'PREVIEW', 'LGTR', 'LGTL', 'LGTB', 'LGTKEY'] and renderLayer not in ['SEA_SHDW', 'SEA_MSK']:
            print u'======================================================================'
            self.slRLMasterCleanCreate('')
            print u'======================================================================'
        '''
        # color
        if layerType == 'COLOR':
            if mc.ls(BGType + '_' + layerType):
                mc.delete(BGType + '_' + layerType)
            self.slRLColorCreate(BGType, selectObjType=selectMode)

        # smoothSet
        #self.slRLDoSmooth()
        # Back To MasterLayer
        mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')
        # UnRender MasterLayer
        mc.setAttr("defaultRenderLayer.renderable", 0)
        # camSetting
        self.slRLCamSetting()
        # common Setting
        # self.slRLCommonConfig()

        if cacheFiles:
            for cache in cacheFiles:
                mc.setAttr((cache + '.enable'), 1)

        if saveMode:
            self.slRLSave(saveMode)

        print (u'===============!!!Done  【%s】!!!===============' % ('renderLayer'))
        print '\n'

    # Save File
    def slRLSave(self, mode):
        print (u'===============!!!Start 【%s】!!!===============' % ('Save'))
        print 'Working...'
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        pathLocal = sk_infoConfig.sk_infoConfig().checkRenderLayerLocalPath()
        fileName = pathLocal + shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2]
        if mode == 'auto_01':
            fileType = '_l4AllLayer_c001.ma'
        if mode == 'auto_02':
            fileType = '_l3AllLayer_c001.ma'
        fileName = fileName + fileType
        mc.file(rename=fileName)
        mc.file(save=1)
        print (u'===============!!!Done  【%s】!!!===============' % ('Save'))
        print '\n'

    # Import Camera
    def zmCamImport(self):
        camGrp = mc.ls('CAM_GRP')
        if camGrp:
            mc.delete(camGrp)

    # camSetting
    def slRLCamSetting(self):
        # 处理cam
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        camName = 'CAM:cam_' + str(shotInfo[1]) + '_' + str(shotInfo[2]) + '_baked'
        if mc.ls(camName, type='transform'):
            camShape = mc.listRelatives(mc.ls(camName, type='transform')[0], ni=1, c=1)[0]
            mc.setAttr((camShape + '.renderable'), 1)
            try:
                mc.setAttr(('perspShape.renderable'), 0)
            except:
                pass
        else:
            mc.error('===============未找到有效CAM【%s】===============' % camName)

    # Create renderPass
    def slRLRenderPass(self):
        print (u'===============!!!Start 【%s】!!!===============' % ('RenderPass'))
        print 'Working...'

        # shadow
        ex_rsShadow = mc.ls('shadow', type='renderPass')
        if ex_rsShadow:
            ex_rsShadow = 'shadow'
        else:
            renderPass = mc.shadingNode('renderPass', asRendering=1)
        configType = [1, 'SHD', 3, 256, 0, 1, 'Illumination', 1, 1, 0, 0, 0, 0, 1, 0, 10, 0, 10]
        self.slRLRenderPassConfig(renderPass, configType)
        mc.rename(renderPass, 'shadow')
        print (u'===============!!!Done  【%s】!!!===============' % ('RenderPass'))
        print '\n'

    #----------------------------------------------------------#
    #----------------------------------------------------------#
    # 物体分类清单
    # import后不用参考时也可以处理
    # 使用条件：sk_sceneConfig.sk_sceneConfig().sk_sceneReorganize(0)
    def slRLObjectsTList(self, objType=1, objs=[]):
        refCHR = []
        refPROP = []
        refSET = []

        if mc.ls('CHR_GRP'):
            if mc.listRelatives('CHR_GRP', c=1, f=1, type='transform'):
                refCHR = mc.listRelatives('CHR_GRP', c=1, f=1, type='transform')
        if mc.ls('PRP_GRP'):
            if mc.listRelatives('PRP_GRP', c=1, f=1, type='transform'):
                refPROP = mc.listRelatives('PRP_GRP', c=1, f=1, type='transform')

        if mc.ls('SET_GRP'):
            if mc.listRelatives('SET_GRP', c=1, f=1, type='transform'):
                refSET = mc.listRelatives('SET_GRP', c=1, f=1, type='transform')
        
        # 避免某些特殊处理，单独划出下级物体获取方法
        for i in range(3):
            needInfo = []
            if i == 0:
                refGrps = refCHR
            if i == 1:
                refGrps = refPROP
            if i == 2:
                refGrps = refSET
            if refGrps:
                needNodes = mc.listRelatives(refGrps, ad=1, type='mesh', f=1) + mc.listRelatives(refGrps, ad=1, type='aiStandIn', f=1)
                if needNodes:
                    needInfo = mc.listRelatives(needNodes, p=1, type='transform', f=1)

            if i == 0:
                refCHR = needInfo
            if i == 1:
                refPROP = needInfo
            if i == 2:
                refSET = needInfo


        # 鱼群支持
        fishGrp = 'fishGeo_grp'
        if mc.objExists(fishGrp):
            meshes = mc.listRelatives(fishGrp, ad=1, type='mesh')
            if meshes:
                for mesh in meshes:
                    refPROP.append(mc.listRelatives(mesh, p=1, tyep='transform')[0])

        result = []
        result.append(list(set(refCHR)))
        result.append(list(set(refPROP)))
        result.append(list(set(refSET)))
        return result
    
    # 渲染标准设置
    def slRLCommonConfig(self):
        print (u'===============!!!Start 【%s】!!!===============' % (u'标准设置'))
        print 'Working...'
        # Camera
        from idmt.maya.commonCore.core_mayaCommon import sk_hbExportCam
        reload(sk_hbExportCam)
        # sk_hbExportCam.sk_hbExportCam().camServerReference()

        # 开启窗口，创建各种UI
        # mel.eval('unifiedRenderGlobalsWindow')

        # 标准设置
        mc.setAttr('defaultRenderQuality.edgeAntiAliasing', 1)
        mc.setAttr('defaultRenderGlobals.animation', 1)
        mc.setAttr('defaultRenderGlobals.outFormatControl', 0)
        mc.setAttr('defaultRenderGlobals.extensionPadding', 4)
        mc.setAttr('defaultRenderGlobals.imageFilePrefix', '<Layer>/<Scene>_<Layer>', type='string')
        mc.setAttr('defaultResolution.width', 1920)
        mc.setAttr('defaultResolution.height', 1080)
        mc.setAttr('defaultResolution.deviceAspectRatio', 1.777)
        mc.setAttr('defaultResolution.pixelAspect', 1.00)
        mc.evalDeferred('import maya.cmds as mc\nmc.setAttr((\'defaultResolution.pixelAspect\'),1)', lowestPriority=1)
        mc.setAttr('defaultResolution.dotsPerInch', 72)
        mc.setAttr('defaultRenderQuality.edgeAntiAliasing', 1)
        # 开始处理
        shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
        shot = shotInfos[0] + '_' + shotInfos[1] + '_' + shotInfos[2]
        anim = idmt.pipeline.db.GetAnimByFilename(shot)
        startFrame = anim.frmStart
        endFrame = anim.frmEnd
        fpsFrame = anim.fps
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

        # mel.eval("prefWndUnitsChanged \"time\";")

        print (u'===============!!!Done  【%s】!!!===============' % u'标准设置')
        print '\n'

    # mr 产品级设置
    def mentalRayProductionLevel(self):
        print (u'===============!!!Start 【%s】!!!===============' % (u'MR设置'))
        print 'Working...'

        mc.setAttr('defaultRenderGlobals.imageFormat', 7)
        try:
            mel.eval('loadPlugin "Mayatomr"')
        except:
            pass
        mc.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')
        # 开启窗口，创建各种UI，该死的MR，为啥不直接生成，非要延时。。
        # mel.eval('unifiedRenderGlobalsWindow')
        # 创建UI
        #mel.eval('mentalrayUI ""')

        # 创建miDefaultOptions节点
        mel.eval('miCreateDefaultNodes')
        # 读取之前创建的production_preset
        mel.eval('nodePreset -load "miDefaultOptions" "production_mi"')

        # 删除天光，关闭FG
        mc.setAttr('miDefaultOptions.finalGather', 0)
        try:
            mel.eval('miDeleteSunSky')
        except:
            pass

        # 默认image format
        # exr
        #mc.editRenderLayerAdjustment('defaultRenderGlobals.imageFormat')
        mc.setAttr('defaultRenderGlobals.imageFormat', 51)
        mc.setAttr('defaultRenderGlobals.imfkey', 'exr', type='string')
        mc.setAttr('mentalrayGlobals.imageCompression', 4)
        mc.setAttr('mentalrayGlobals.compressionQuality', 0)

        mc.setAttr('miDefaultOptions.maxSamples', 2)
        try:
            mc.setAttr('miDefaultOptions.minSamples', 0)
        except:
            pass

        mc.setAttr('miDefaultOptions.filter', 2)

        print (u'===============!!!Done  【%s】!!!===============' % (u'MR设置'))
        print '\n'

    # arnold 设置
    def arnoldRendererSettings(self):
        print (u'===============!!!Start 【%s】!!!===============' % (u'Arnold设置'))
        print 'Working...'

        mc.setAttr('defaultRenderGlobals.imageFormat', 7)
        try:
            mel.eval('loadPlugin "mtoa"')
        except:
            pass
        # 开启窗口，创建各种UI
        # mel.eval('unifiedRenderGlobalsWindow')
        mc.setAttr('defaultRenderGlobals.currentRenderer', 'arnold', type='string')
        # 下来所需的节点提前创建
        import mtoa
        mtoa.core.createOptions()
        import mtoa.cmds.registerArnoldRenderer
        mtoa.cmds.registerArnoldRenderer.registerArnoldRenderer()

        # setting
        mc.setAttr('defaultArnoldDriver.halfPrecision',1)
        mc.setAttr('defaultArnoldDriver.tiled', 0)
        mc.setAttr('defaultArnoldDriver.autocrop',1)
        mc.setAttr('defaultArnoldRenderOptions.AASamples',4)
        mc.setAttr('defaultArnoldRenderOptions.GIDiffuseSamples',0)
        mc.setAttr('defaultArnoldRenderOptions.GIGlossySamples',0)
        mc.setAttr('defaultArnoldRenderOptions.GIRefractionSamples',0)
        mc.setAttr('defaultArnoldRenderOptions.sssBssrdfSamples',3)
        mc.setAttr('defaultArnoldRenderOptions.lock_sampling_noise',1)
        mc.setAttr('defaultArnoldRenderOptions.textureAutomip',1)
        mc.setAttr('defaultArnoldRenderOptions.textureAcceptUnmipped',1)
        mc.setAttr('defaultArnoldRenderOptions.use_existing_tiled_textures',1)

        print (u'===============!!!Done  【%s】!!!===============' % (u'Arnold设置'))
        print '\n'


    #----------------------------------------------------------#
    # arnold renderpass 创建
    def slRLArnoldRenderpassCreate(self):
        #----------------------#
        # shader
        #----------------------#
        # occ
        AOShader = 'SHD_AO_arnold'
        if mc.ls( AOShader ):
            mc.delete(AOShader)
        AOSG = 'SHD_AO_arnold_SG'
        if mc.ls( AOSG ):
            mc.delete( AOSG )
        AOShader = mc.shadingNode ('aiAmbientOcclusion', asShader=True, name= AOShader)  
        AOSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=( AOSG ))
        mc.connectAttr(('%s.%s') % (AOShader , 'outColor') , ('%s.%s') % (AOSG , 'surfaceShader'), f=True)
        #----------------------#
        # nomal
        NMShader = 'SHD_NM_arnold'
        if mc.ls( NMShader ):
            mc.delete(NMShader)
        NMSG = 'SHD_NM_arnold_SG'
        if mc.ls( NMSG ):
            mc.delete( NMSG )
        NMShader = mc.shadingNode ('aiUtility', asShader=True, name= NMShader)  
        NMSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=( NMSG ))
        mc.setAttr((NMShader + '.shadeMode') , 2)
        mc.setAttr((NMShader + '.colorMode') , 3)
        mc.connectAttr(('%s.%s') % (NMShader , 'outColor') , ('%s.%s') % (NMSG , 'surfaceShader'), f=True)
        #----------------------#
        # fresnel
        FNShader = 'SHD_Fresnel_arnold'
        if mc.ls( FNShader ):
            mc.delete(FNShader)
        FNRamp = 'SHD_Fresnel_ramp_arnold'
        if mc.ls( FNRamp ):
            mc.delete(FNRamp)
        FNSample = 'SHD_Fresnel_Sample_arnold'
        if mc.ls( FNSample ):
            mc.delete(FNSample)
        FNSG = 'SHD_Fresnel_arnold_SG'
        if mc.ls( FNSG ):
            mc.delete( FNSG )
        FNShader = mc.shadingNode ('aiUtility', asShader=True, name= FNShader)  
        FNRamp = mc.shadingNode ('ramp', asShader=True, name= FNRamp)  
        FNSample = mc.shadingNode ('samplerInfo', asShader=True, name= FNSample)  
        FNSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=( FNSG ))
        mc.removeMultiInstance((FNRamp + '.colorEntryList[1]') , b = 1)
        mc.setAttr((FNShader + '.shadeMode'),2)
        mc.setAttr((FNRamp + '.interpolation'),3)
        mc.setAttr((FNRamp + '.colorEntryList[2].position'),1)
        mc.setAttr((FNRamp + '.colorEntryList[0].position'),0)
        mc.setAttr((FNRamp + '.colorEntryList[2].color'),0,0,0,type = 'double3')
        mc.setAttr((FNRamp + '.colorEntryList[0].color'),1,1,1,type = 'double3')
        mc.connectAttr(('%s.%s') % (FNShader , 'outColor') , ('%s.%s') % (FNSG , 'surfaceShader'), f=True)
        mc.connectAttr(('%s.%s') % (FNSample , 'facingRatio') , ('%s.%s') % (FNRamp , 'uCoord'), f=True)
        mc.connectAttr(('%s.%s') % (FNSample , 'facingRatio') , ('%s.%s') % (FNRamp , 'vCoord'), f=True)
        mc.connectAttr(('%s.%s') % (FNRamp , 'outColor') , ('%s.%s') % (FNShader , 'color'), f=True)
        #----------------------#
        # keyLight
        keyLightShader = 'SHD_KeyLight_arnold'
        if mc.ls( keyLightShader ):
            mc.delete(keyLightShader)
        keyLightSG = 'SHD_KeyLight_arnold_SG'
        if mc.ls( keyLightSG ):
            mc.delete(keyLightSG)
        keyLightShader = mc.shadingNode ('aiStandard', asShader=True, name= keyLightShader)  
        keyLightSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=( keyLightSG ))
        mc.connectAttr(('%s.%s') % (keyLightShader , 'outColor') , ('%s.%s') % (keyLightSG , 'surfaceShader'), f=True)
        #----------------------#
        # shadow
        shadowShader = 'SHD_Shadow_arnold'
        if mc.ls( shadowShader ):
            mc.delete(shadowShader)
        shadowSG = 'SHD_Shadow_arnold_SG'
        if mc.ls( shadowSG ):
            mc.delete(shadowSG)
        shadowShader = mc.shadingNode ('aiShadowCatcher', asShader=True, name= shadowShader)  
        shadowSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=( shadowSG ))
        mc.setAttr((shadowShader + '.backgroundColor'),1,1,1,type = 'double3')
        mc.connectAttr(('%s.%s') % (shadowShader , 'outColor') , ('%s.%s') % (shadowSG , 'surfaceShader'), f=True)
        
        #----------------------#
        # dirver
        #----------------------#
        mc.setAttr('defaultArnoldDriver.mergeAOVs',1)
        # renderpass
        #----------------------#
        # Z
        ZArnoldPass = 'aiAOV_Z'
        if mc.ls(ZArnoldPass) :
            if mc.nodeType(ZArnoldPass) =='aiAOV':
                pass
            else:
                mc.delete(ZArnoldPass)
                mc.createNode('aiAOV',name = ZArnoldPass)
        else:
            mc.createNode('aiAOV',name = ZArnoldPass )
        mc.setAttr((ZArnoldPass + '.name'),'Z',type = 'string')
        mc.setAttr((ZArnoldPass + '.type'),4)
        #----------------------#
        # occ
        occArnoldPass = 'aiAOV_Occ'
        if mc.ls(occArnoldPass) :
            if mc.nodeType(occArnoldPass) =='aiAOV':
                pass
            else:
                mc.delete(occArnoldPass)
                mc.createNode('aiAOV',name = occArnoldPass)
        else:
            mc.createNode('aiAOV',name = occArnoldPass )
        mc.setAttr((occArnoldPass + '.name'),'occ',type = 'string')
        mc.setAttr((occArnoldPass + '.type'),5)
        #----------------------#
        # normal
        nmArnoldPass = 'aiAOV_Normal'
        if mc.ls(nmArnoldPass) :
            if mc.nodeType(nmArnoldPass) =='aiAOV':
                pass
            else:
                mc.delete(nmArnoldPass)
                mc.createNode('aiAOV',name = nmArnoldPass)
        else:
            mc.createNode('aiAOV',name = nmArnoldPass )
        mc.setAttr((nmArnoldPass + '.name'),'normal',type = 'string')
        mc.setAttr((nmArnoldPass + '.type'),5)
        #----------------------#
        # frese1
        fresenlArnoldPass = 'aiAOV_Fresnel'
        if mc.ls(fresenlArnoldPass) :
            if mc.nodeType(fresenlArnoldPass) =='aiAOV':
                pass
            else:
                mc.delete(fresenlArnoldPass)
                mc.createNode('aiAOV',name = fresenlArnoldPass)
        else:
            mc.createNode('aiAOV',name = fresenlArnoldPass )
        mc.setAttr((fresenlArnoldPass + '.name'),'fresnel',type = 'string')
        mc.setAttr((fresenlArnoldPass + '.type'),5)
        #----------------------#
        # keyLight
        keyLightArnoldPass = 'aiAOV_KeyLight'
        if mc.ls(keyLightArnoldPass) :
            if mc.nodeType(keyLightArnoldPass) =='aiAOV':
                pass
            else:
                mc.delete(keyLightArnoldPass)
                mc.createNode('aiAOV',name = keyLightArnoldPass)
        else:
            mc.createNode('aiAOV',name = keyLightArnoldPass )
        mc.setAttr((keyLightArnoldPass + '.name'),'KeyLight',type = 'string')
        mc.setAttr((keyLightArnoldPass + '.type'),5)
        #----------------------#
        # shadow
        shadowArnoldPass = 'aiAOV_Shadow'
        if mc.ls(shadowArnoldPass) :
            if mc.nodeType(shadowArnoldPass) =='aiAOV':
                pass
            else:
                mc.delete(shadowArnoldPass)
                mc.createNode('aiAOV',name = shadowArnoldPass)
        else:
            mc.createNode('aiAOV',name = shadowArnoldPass )
        mc.setAttr((shadowArnoldPass + '.name'),'shadow',type = 'string')
        mc.setAttr((shadowArnoldPass + '.type'),5)
        #----------------------#
        # aiAOVFilter
        # closset
        aiAOVFilter_Closset =  'defaultArnoldFilter_Closset'
        if mc.ls(aiAOVFilter_Closset) :
            if mc.nodeType(aiAOVFilter_Closset) =='aiAOVFilter':
                pass
            else:
                mc.delete(aiAOVFilter_Closset)
                mc.createNode('aiAOVFilter',name = aiAOVFilter_Closset)
        else:
            mc.createNode('aiAOVFilter',name = aiAOVFilter_Closset )

        #----------------------#
        # 连接
        #----------------------#
        # Z
        try:
            mc.disconnectAttr(('%s.%s') % ('defaultArnoldDriver' , 'message') , ('%s.%s') % (ZArnoldPass , 'outputs[0].driver'))
        except:
            pass
        mc.connectAttr(('%s.%s') % ('defaultArnoldDriver' , 'message') , ('%s.%s') % (ZArnoldPass , 'outputs[0].driver'), f=True)
        try:
            mc.disconnectAttr(('%s.%s') % ( aiAOVFilter_Closset , 'message') , ('%s.%s') % (ZArnoldPass, 'outputs[0].filter'))
        except:
            pass
        mc.connectAttr(('%s.%s') % ( aiAOVFilter_Closset , 'message') , ('%s.%s') % (ZArnoldPass, 'outputs[0].filter'), f=True)
        try:
            mc.disconnectAttr(('%s.%s') % ( ZArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[0]'))
        except:
            pass
        mc.connectAttr(('%s.%s') % ( ZArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[0]'), f=True)
        #----------------------#
        # occ
        try:
            mc.disconnectAttr(('%s.%s') % ('defaultArnoldDriver' , 'message') , ('%s.%s') % (occArnoldPass , 'outputs[0].driver'))
        except:
            pass
        mc.connectAttr(('%s.%s') % ('defaultArnoldDriver' , 'message') , ('%s.%s') % (occArnoldPass , 'outputs[0].driver'), f=True)
        try:
            mc.disconnectAttr(('%s.%s') % ( 'defaultArnoldFilter' , 'message') , ('%s.%s') % (occArnoldPass, 'outputs[0].filter'))
        except:
            pass
        mc.connectAttr(('%s.%s') % ( 'defaultArnoldFilter' , 'message') , ('%s.%s') % (occArnoldPass, 'outputs[0].filter'), f=True)
        try:
            mc.disconnectAttr(('%s.%s') % ( AOShader , 'outColor') , ('%s.%s') % (occArnoldPass, 'defaultValue'))
        except:
            pass
        mc.connectAttr(('%s.%s') % ( AOShader , 'outColor') , ('%s.%s') % (occArnoldPass, 'defaultValue'), f=True)
        mc.setAttr((AOShader + '.samples'),4)
        try:
            mc.disconnectAttr(('%s.%s') % ( occArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[1]'))
        except:
            pass
        mc.connectAttr(('%s.%s') % ( occArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[1]'), f=True)
        #----------------------#
        # normal
        try:
            mc.disconnectAttr(('%s.%s') % ('defaultArnoldDriver' , 'message') , ('%s.%s') % (nmArnoldPass , 'outputs[0].driver'))
        except:
            pass
        mc.connectAttr(('%s.%s') % ('defaultArnoldDriver' , 'message') , ('%s.%s') % (nmArnoldPass , 'outputs[0].driver'), f=True)
        try:
            mc.disconnectAttr(('%s.%s') % ( 'defaultArnoldFilter' , 'message') , ('%s.%s') % (nmArnoldPass , 'outputs[0].filter'))
        except:
            pass
        mc.connectAttr(('%s.%s') % ( 'defaultArnoldFilter' , 'message') , ('%s.%s') % (nmArnoldPass , 'outputs[0].filter'), f=True)
        try:
            mc.disconnectAttr(('%s.%s') % ( NMShader , 'outColor') , ('%s.%s') % (nmArnoldPass, 'defaultValue'))
        except:
            pass
        mc.connectAttr(('%s.%s') % ( NMShader , 'outColor') , ('%s.%s') % (nmArnoldPass, 'defaultValue'), f=True)
        try:
            mc.disconnectAttr(('%s.%s') % ( nmArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[2]'))
        except:
            pass
        mc.connectAttr(('%s.%s') % ( nmArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[2]'), f=True)
        #----------------------#
        # frese
        try:
            mc.disconnectAttr(('%s.%s') % ('defaultArnoldDriver' , 'message') , ('%s.%s') % (fresenlArnoldPass , 'outputs[0].driver'))
        except:
            pass
        mc.connectAttr(('%s.%s') % ('defaultArnoldDriver' , 'message') , ('%s.%s') % (fresenlArnoldPass , 'outputs[0].driver'), f=True)
        try:
            mc.disconnectAttr(('%s.%s') % ( 'defaultArnoldFilter' , 'message') , ('%s.%s') % (fresenlArnoldPass , 'outputs[0].filter'))
        except:
            pass
        mc.connectAttr(('%s.%s') % ( 'defaultArnoldFilter' , 'message') , ('%s.%s') % (fresenlArnoldPass , 'outputs[0].filter'), f=True)
        try:
            mc.disconnectAttr(('%s.%s') % ( FNShader , 'outColor') , ('%s.%s') % (fresenlArnoldPass, 'defaultValue'))
        except:
            pass
        mc.connectAttr(('%s.%s') % ( FNShader , 'outColor') , ('%s.%s') % (fresenlArnoldPass, 'defaultValue'), f=True)
        try:
            mc.disconnectAttr(('%s.%s') % ( fresenlArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[3]'))
        except:
            pass
        mc.connectAttr(('%s.%s') % ( fresenlArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[3]'), f=True)
        #----------------------#
        # keyLight
        try:
            mc.disconnectAttr(('%s.%s') % ('defaultArnoldDriver' , 'message') , ('%s.%s') % (keyLightArnoldPass , 'outputs[0].driver'))
        except:
            pass
        mc.connectAttr(('%s.%s') % ('defaultArnoldDriver' , 'message') , ('%s.%s') % (keyLightArnoldPass , 'outputs[0].driver'), f=True)
        try:
            mc.disconnectAttr(('%s.%s') % ( 'defaultArnoldFilter' , 'message') , ('%s.%s') % (keyLightArnoldPass , 'outputs[0].filter'))
        except:
            pass
        mc.connectAttr(('%s.%s') % ( 'defaultArnoldFilter' , 'message') , ('%s.%s') % (keyLightArnoldPass , 'outputs[0].filter'), f=True)
        try:
            mc.disconnectAttr(('%s.%s') % ( keyLightShader , 'outColor') , ('%s.%s') % (keyLightArnoldPass, 'defaultValue'))
        except:
            pass
        mc.connectAttr(('%s.%s') % ( keyLightShader , 'outColor') , ('%s.%s') % (keyLightArnoldPass, 'defaultValue'), f=True)
        try:
            mc.disconnectAttr(('%s.%s') % ( keyLightArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[4]'))
        except:
            pass
        mc.connectAttr(('%s.%s') % ( keyLightArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[4]'), f=True)
        #----------------------#
        # shadow
        try:
            mc.disconnectAttr(('%s.%s') % ('defaultArnoldDriver' , 'message') , ('%s.%s') % (shadowArnoldPass , 'outputs[0].driver'))
        except:
            pass
        mc.connectAttr(('%s.%s') % ('defaultArnoldDriver' , 'message') , ('%s.%s') % (shadowArnoldPass , 'outputs[0].driver'), f=True)
        try:
            mc.disconnectAttr(('%s.%s') % ( 'defaultArnoldFilter' , 'message') , ('%s.%s') % (shadowArnoldPass , 'outputs[0].filter'))
        except:
            pass
        mc.connectAttr(('%s.%s') % ( 'defaultArnoldFilter' , 'message') , ('%s.%s') % (shadowArnoldPass , 'outputs[0].filter'), f=True)
        try:
            mc.disconnectAttr(('%s.%s') % ( shadowShader , 'outColor') , ('%s.%s') % (shadowArnoldPass, 'defaultValue'))
        except:
            pass
        mc.connectAttr(('%s.%s') % ( shadowShader , 'outColor') , ('%s.%s') % (shadowArnoldPass, 'defaultValue'), f=True)
        try:
            mc.disconnectAttr(('%s.%s') % ( shadowArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[5]'))
        except:
            pass
        mc.connectAttr(('%s.%s') % ( shadowArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[5]'), f=True)
        
        
    # smoothSet
    def slRLDoSmooth(self, layerType=1):
        from idmt.maya.commonCore.core_mayaCommon import sk_smoothSet
        reload(sk_smoothSet)
        # 非PFX层用
        if layerType == 1:
            sk_smoothSet.sk_smoothSet().smoothSetDoSmooth()

    # 断开所有SG节点的连接
    def slRLSGNodesDisConnections(self):
        sgNodes = mc.ls(type='shadingEngine')
        if sgNodes:
            for sgNode in sgNodes:
                if sgNode == "initialShadingGroup":
                    continue
                if sgNode == "initialParticleSE":
                    continue
                # 获取dagSetMembers连接信息,返回列表必定为2的倍数
                buf = mc.listConnections((sgNode + '.dagSetMembers'), connections=1, plugs=1)
                if buf:
                    for i in range(len(buf) / 2):
                        shape = buf[i + 1].split('.')[0]
                        if mc.nodeType(shape) != 'renderLayer':
                            try:
                                mc.disconnectAttr(buf[i + 1], buf[i])
                            except:
                                pass
                # 获取memberWireframeColor连接信息,返回列表必定为2的倍数
                buf = mc.listConnections((sgNode + '.memberWireframeColor'), connections=1, plugs=1)
                if buf:
                    for i in range(len(buf) / 2):
                        shape = buf[i + 1].split('.')[0]
                        if mc.nodeType(shape) != 'renderLayer':
                            try:
                                mc.disconnectAttr(buf[i + 1], buf[i])
                            except:
                                pass

    # 透明属性连接
    def slRLTransShaderConnectiion(self, transpancyNode, transShader, transShaderAttr):
        if transpancyNode[:6] == '[food]':
            transValue = float(transpancyNode[7:])
            try:
                transpancyConnections = mc.listConnections((transShader + '.' + transShaderAttr), s=1, plugs=1)
                mc.disconnectAttr(('%s') % (transpancyConnections[0]), ('%s.%s') % (transShader, transShaderAttr))
            except:
                pass
            mc.setAttr((transShader + '.' + transShaderAttr), transValue, transValue, transValue, type='double3')
        else:
            if mc.nodeType(transpancyNode.split('.')[0]) in['layeredShader', 'surfaceShader', 'ramp', 'file', 'reverse']:
                if mc.nodeType(transpancyNode.split('.')[0]) in ['layeredShader', 'surfaceShader']:
                    try:
                        mc.disconnectAttr(('%s.%s') % (transpancyNode.split('.')[0], transShaderAttr), ('%s.%s') % (transShader, transShaderAttr))
                    except:
                        pass
                    mc.connectAttr(('%s.%s') % (transpancyNode.split('.')[0], transShaderAttr), ('%s.%s') % (transShader, transShaderAttr), f=True)
                if mc.nodeType(transpancyNode.split('.')[0]) in ['ramp', 'file']:
                    try:
                        mc.disconnectAttr(('%s.%s') % (transpancyNode.split('.')[0], 'outColor'), ('%s.%s') % (transShader, transShaderAttr))
                    except:
                        pass
                    mc.connectAttr(('%s.%s') % (transpancyNode.split('.')[0], 'outColor'), ('%s.%s') % (transShader, transShaderAttr), f=True)
                if mc.nodeType(transpancyNode.split('.')[0]) in ['reverse', ]:
                    try:
                        mc.disconnectAttr(('%s.%s') % (transpancyNode.split('.')[0], 'output'), ('%s.%s') % (transShader, transShaderAttr))
                    except:
                        pass
                    mc.connectAttr(('%s.%s') % (transpancyNode.split('.')[0], 'output'), ('%s.%s') % (transShader, transShaderAttr), f=True)
            else:
                try:
                    mc.disconnectAttr(('%s.%s') % (transpancyNode.split('.')[0], 'outAlpha'), ('%s.%s') % (transShader, transShaderAttr))
                except:
                    pass
                mc.connectAttr(('%s.%s') % (transpancyNode.split('.')[0], 'outAlpha'), ('%s.%s') % (transShader, transShaderAttr), f=True)

    # 非CO之类的层，主层给个临时材质球，避免材质出错
    def slRLMasterCleanCreate(self, layerType='', selectObjType=0):
        print (u'===============!!!Start 【%s】!!!===============' % (u'MasterTemp层'))
        print 'Working...'

        # 物体
        objs = self.slRLObjectsTList()
        refCHR = objs[0]
        refPROP = objs[1]
        refSET = objs[2]

        rlObjs = refCHR + refPROP + refSET

        layerType = 'MasterTemp'

        # 灯光
        lights = mc.ls(type='light')

        # 选取模式
        if selectObjType == 1:
            rlObjs = mc.ls(sl=1)

        if rlObjs:

            # 断开所有SG连接
            self.slRLSGNodesDisConnections()

            # 通用材质
            shaderNode = 'SHD_' + layerType + '_Shader'
            if mc.ls(shaderNode):
                mc.delete(shaderNode)
            shaderSG = 'SHD_' + layerType + '_SG'
            if mc.ls(shaderSG):
                mc.delete(shaderSG)
            shaderNode = mc.shadingNode('lambert', asShader=True, name=shaderNode)
            shaderSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=shaderSG)
            mc.connectAttr((shaderNode + '.outColor'), (shaderSG + '.surfaceShader'))

            # 优先全局着色
            for obj in rlObjs:
                try:
                    mc.sets(obj, e=1, forceElement=shaderSG)
                except:
                    # 获取物体面数
                    faceNum = mc.polyEvaluate(obj, face=1)
                    mc.sets((obj + u'.f[:' + str(faceNum - 1) + u']'), e=1, forceElement=shaderSG)

            print (u'===============!!!Done  【%s】!!!===============' % (u'%MasterTemp层'))
            print '\n'

    # 分层信息输出
    def slRLayerInfoExport(self, layerType='RGB', LayerName='myRGB', exportType='all'):
        localPath = sk_infoConfig.sk_infoConfig().checkLayerInfoLocalPath(layerType, LayerName)

        fileName = layerType + '_' + exportType + '_geo.txt'
        filePath = localPath + fileName
        # 输出物体
        objs = mc.ls(sl=1)
        if objs:
            sk_infoConfig.sk_infoConfig().checkFileWrite(filePath, objs)

    # 分层信息读取
    def slRLayerInfoImport(self, layerType='RGB', LayerName='myRGB', exportType='all'):
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        serverPath = sk_infoConfig.sk_infoConfig().checkLayerInfoServerPath(layerType, LayerName)

        # 读文件
        fileName = layerType + '_' + exportType + '_geo.txt'
        filePath = serverPath + fileName
        import os
        if os.path.exists(filePath):
            objs = sk_infoConfig.sk_infoConfig().checkFileRead(filePath)
            return objs
        else:
            mc.error(u'===========指定信息文件【%s】不存在===========' % fileName)

    # 获取文件内所有RGB素材信息
    def slRLayerRGBObjectsConfig(self, checkType):
        # 获取所有服务器端素材信息
        from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools
        reload(sk_sceneTools)
        serverPath = sk_infoConfig.sk_infoConfig().checkLayerInfoServerPath('RGB')[:-6]
        allSolution = mc.getFileList(folder=serverPath)
        if 'myRGB' in allSolution:
            allSolution.remove('allAsset')
        # 获取本文件内指定类型信息
        # 每个元素为2单位的list，其一为文件内的namespace，其二为标准asset的namespace
        assetFileInfo = sk_infoConfig.sk_infoConfig().checkAsset2FileObjsConfig(checkType)
        if allSolution and assetFileInfo:
            # 获取文件内需要的asstNamespace及对应的标准namespace
            assetFileNamespaces = []
            assetRealNames = []
            for assetFile in assetFileInfo:
                assetFileNamespaces.append(assetFile[0])
                assetRealNames.append(assetFile[1])
            # 记录
            assetFileAll = []
            assetFileR = []
            assetFileG = []
            assetFileB = []
            # 应该先从服务器端方案信息里筛选
            for solution in allSolution:
                assetAllInfo = self.slRLayerInfoImport(layerType='RGB', LayerName=solution, exportType='all')
                if assetAllInfo:
                    solutionNamespace = assetAllInfo[0].split(':')[0]
                    # print solutionNamespace
                    # print assetRealNames
                    # 方案内asset在文件内的真实asset内时进行换算名字
                    if solutionNamespace in assetRealNames:
                        infoIndex = assetRealNames.index(solutionNamespace)
                        assetFileNamespace = assetFileNamespaces[infoIndex]
                        assetRInfo = self.slRLayerInfoImport(layerType='RGB', LayerName=solution, exportType='R')
                        assetGInfo = self.slRLayerInfoImport(layerType='RGB', LayerName=solution, exportType='G')
                        assetBInfo = self.slRLayerInfoImport(layerType='RGB', LayerName=solution, exportType='B')
                        # 处理成本文件信息
                        for obj in assetAllInfo:
                            assetFileAll.append((assetFileNamespace + ':' + obj[(len(solutionNamespace) + 1):]))
                        if assetRInfo:
                            for obj in assetRInfo:
                                assetFileR.append((assetFileNamespace + ':' + obj[(len(solutionNamespace) + 1):]))
                        if assetGInfo:
                            for obj in assetGInfo:
                                assetFileG.append((assetFileNamespace + ':' + obj[(len(solutionNamespace) + 1):]))
                        if assetBInfo:
                            for obj in assetBInfo:
                                assetFileB.append((assetFileNamespace + ':' + obj[(len(solutionNamespace) + 1):]))
                    else:
                        pass
            # 统一记录
            needFileObjInfo = [assetFileAll, assetFileR, assetFileG, assetFileB]
            return needFileObjInfo

    # 删除SET reference
    def slRLayerSetReferenceDel(self):
        from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
        reload(sk_referenceConfig)
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refNodes = refInfos[0][0]
        refPaths = refInfos[1][0]
        if refNodes:
            for ref in refNodes:
                if '_' in ref:
                    if ref.split('_')[1][0] in ['s', 'S']:
                        # 删除参考
                        mc.file(rfn=ref, removeReference=1)

    # 处理exr压缩格式
    def slRLayerExrWriteMode(self):
        # 获取文件前缀名
        fileName = mc.renderSettings(fin=1, lin=1, lut=1)
        filePreName = fileName[0].split('.')[0]
        fileNameType = fileName[0].split('.')[-1]
        if fileNameType == 'iff':
            frameCurrect = mc.currentTime(q=1)
            # 处理成四位string
            frameString = ''
            if (frameCurrect / 1000) >= 1:
                frameString = str(frameCurrect).split('.')[0]
            else:
                if (frameCurrect / 100) >= 1:
                    frameString = '0' + str(frameCurrect).split('.')[0]
                else:
                    if (frameCurrect / 10) >= 1:
                        frameString = '00' + str(frameCurrect).split('.')[0]
                    else:
                        frameString = '000' + str(frameCurrect).split('.')[0]
            fileFullName = filePreName + '.' + frameString + '.' + fileNameType

    # Zdepth distance UI
    def slRLayerZdepthDistanceConfigUI(self):
        if mc.window('Zdepth_Distance_UI', q=True, exists=True):
            mc.deleteUI('Zdepth_Distance_UI')
        mc.window('Zdepth_Distance_UI', t=(unicode('Zdepth_Distance_UI', 'utf8')), wh=[320, 90], mb=True)

        # 主界面
        mc.columnLayout()

        # 分解创建
        mc.frameLayout(label=u'Zdepth_Distance', borderStyle='etchedOut', width=320)

        mc.rowLayout()
        mc.intFieldGrp('Zdepth_Distance_Value', l=u'距离设置: ', value1=15000)
        mc.setParent("..")

        mc.setParent("..")

        mc.rowLayout()
        mc.button(label=u'[变更设置]', width=320, c='sk_renderLayer_ZoomWhiteDolphin.slRLConfig().slRLayerZdepthDistanceConfig()')
        mc.setParent("..")

        mc.showWindow()

    # Zdepth distance Config
    def slRLayerZdepthDistanceConfig(self):
        value = mc.intFieldGrp('Zdepth_Distance_Value', value=1, q=1)[0]
        samplerInfoNodes = mc.ls(type='samplerInfo')
        if samplerInfoNodes:
            for node in samplerInfoNodes:
                if mc.objExists(node + '.FarClipCalimero'):
                    mc.setAttr((node + '.FarClipCalimero'), value)

    # 选取模式
    def slRLSelectMode(self):
        # 选取模式
        rlObjs = []
        selObjs = mc.ls(sl=1,l=1)
        if not selObjs:
            mc.error('======请选取物体======')
        for selObj in selObjs:
            checkObjs = mc.listRelatives(selObj, ad = 1 ,type = 'mesh')
            if not checkObjs:
                mc.error('======请选取有效物体======')
            for checkObj in checkObjs:
                rlObjs.append(mc.listRelatives(checkObj,p=1))
        return rlObjs

    #-------------------------------------------------------------------------------------------#
    # 渲染层开始
    #-------------------------------------------------------------------------------------------#
    
    # 角色层开始
    def slRLColorCreate(self, layerType, selectObjType=0):
        # 获取物体
        # 物体
        objs = self.slRLObjectsTList()
        refCHR = objs[0]
        refPROP = objs[1]
        refSET = objs[2]
        refSKY = objs[3]
        refSEA = objs[4]

        # 灯光
        specallights = []

        lights = mc.ls(type='light')
        if lights:
            for light in lights:
                specallights.append(light)
        # 物体
        rlObjs = []
        print '----'
        print layerType
        if layerType == 'ALL':
            rlObjs = refCHR + refPROP + refSET
            layerName = 'ALL_CO'
        if layerType == 'CHR':
            rlObjs = refCHR + refPROP
            layerName = 'CHR_CO'
        if layerType == 'BG':
            rlObjs = refSET
            layerName = 'BG_CO'

        # 选取模式
        if selectObjType == 1:
            rlObjs = self.slRLSelectMode()
        
        # 准备建层
        if rlObjs:
            if mc.ls(layerName):
                mc.delete(layerName)    
            mc.createRenderLayer(rlObjs , name=layerName , noRecurse=1 , makeCurrent=1)
            
            # renderpass
            self.slRLArnoldRenderpassCreate()
            
            # 层名
            fileName = mc.file(exn=1,q=1)
            fileName = fileName.split('/')[-1].split('.')[0]
            layerImageName = fileName + layerName
            mc.editRenderLayerAdjustment('defaultRenderGlobals.imageFilePrefix')
            mc.setAttr('defaultRenderGlobals.imageFilePrefix',layerImageName,type = 'string')
                
            print (u'===============!!!Done 【Arnold】【%s】!!!===============' % (u'%s_层' % layerName))
            print '\n'
            
        else:
            print (u'===============!!!Error  【%s】无物体!!!===============' % (u'%s_COLOR层' % layerType))
            print '\n'
                    

        
        
        
    
