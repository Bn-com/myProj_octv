# -*- coding: utf-8 -*-

'''
Created on 2014-01-24

@author: shenkang
'''

import maya.cmds as mc
import maya.mel as mel
import idmt.pipeline.db

# shader import 
# file nodes ,for tga ,filter off ,for map ,filter config minmap


class idmtRLArnoldConfig(object):
    def __init__(self):
        pass
    
    #----------------------------------------------------------#
    # 渲染标准设置
    def idmtRLCommonConfig(self):
        print(u'===============!!!Start 【%s】!!!===============' % (u'标准设置'))
        print('Working...')
        # Camera
        from idmt.maya.commonCore.core_mayaCommon import sk_hbExportCam
        reload(sk_hbExportCam)
        # sk_hbExportCam.sk_hbExportCam().camServerReference()   

        # 开启窗口，创建各种UI
        #mel.eval('unifiedRenderGlobalsWindow')

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
        from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
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
        mc.setAttr('defaultRenderGlobals.animation',1)
        mc.setAttr('defaultRenderGlobals.putFrameBeforeExt',1)
        mc.setAttr('defaultRenderGlobals.periodInExt',1)
        mc.setAttr('defaultRenderGlobals.extensionPadding',4)
        if mc.getAttr('defaultRenderGlobals.outFormatControl') == 1:
            mc.setAttr('defaultRenderGlobals.outFormatControl',0)

        # mel.eval("prefWndUnitsChanged \"time\";")

        print(u'===============!!!Done  【%s】!!!===============' % u'标准设置')
        
    #----------------------------------------------------------#
    # mr 产品级设置    
    def idmtMentalRayProductionLevel(self):
        print(u'===============!!!Start 【%s】!!!===============' % (u'MR设置'))
        print('Working...')
        
        mc.setAttr('defaultRenderGlobals.imageFormat', 7)   
        try:
            mel.eval('loadPlugin "Mayatomr"')
        except:
            pass
        mc.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')
        # 开启窗口，创建各种UI，该死的MR，为啥不直接生成，非要延时。。
        #mel.eval('unifiedRenderGlobalsWindow')
        # 创建UI
        #mel.eval('mentalrayUI ""')

        # 创建miDefaultOptions节点
        mel.eval('miCreateDefaultNodes')
        # 读取之前创建的production_preset
        mel.eval('nodePreset -load "miDefaultOptions" "production_mi"')
        
        # 删除天光，关闭FG
        mc.setAttr('miDefaultOptions.finalGather',0)
        try:
            mel.eval('miDeleteSunSky')
        except:
            pass
        
        # 默认image format
        #mel.eval("editRenderLayerAdjustment \"defaultRenderGlobals.imageFormat\";")
        if mc.optionMenuGrp('imageMenuMentalRay', exists=1):
            mc.optionMenuGrp('imageMenuMentalRay', e=1, value = 'OpenEXR (exr)')
            try:
                mel.eval('changeMentalRayImageFormat')
            except:
                pass
        
        mc.setAttr('miDefaultOptions.maxSamples',2)

        print(u'===============!!!Done  【%s】!!!===============' % (u'MR设置'))
        
    #----------------------------------------------------------#
    # arnold 设置    
    def idmtArnoldRendererSettings(self):
        print(u'===============!!!Start 【%s】!!!===============' % (u'Arnold设置'))
        print('Working...')
        
        mc.setAttr('defaultRenderGlobals.imageFormat', 7)   
        try:
            mel.eval('loadPlugin "mtoa"')
        except:
            pass
        # 开启窗口，创建各种UI
        #mel.eval('unifiedRenderGlobalsWindow')
        mc.setAttr('defaultRenderGlobals.currentRenderer', 'arnold', type='string')
        # 下来所需的节点提前创建
        import mtoa
        mtoa.core.createOptions()
        import mtoa.cmds.registerArnoldRenderer
        mtoa.cmds.registerArnoldRenderer.registerArnoldRenderer()

        mc.setAttr('defaultArnoldDriver.halfPrecision', 1)
        mc.setAttr('defaultArnoldDriver.tiled', 0)
        mc.setAttr('defaultArnoldDriver.autocrop', 1)
        mc.setAttr('defaultArnoldRenderOptions.AASamples', 4)

        
        print(u'===============!!!Done  【%s】!!!===============' % (u'Arnold设置'))

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
        mc.setAttr((keyLightArnoldPass + '.type'),4)
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
        mc.setAttr((shadowArnoldPass + '.type'),4)
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
        

    #----------------------------------------------------------#
    # 获取有透明贴图的物体
    def idmtRLTransparencyObjsOld(self):
        transparencySG = []
        errorNameSG = []
        doNotNeedSG = ['_ao_' , '_nm_' , '_light_' , '_rim_' , '_spec_']
        # 获取file节点
        SGNodes = mc.ls(type = 'shadingEngine')
        for SGNode in SGNodes:
            doNot = 0 
            transState = 0
            for doNotNeed in doNotNeedSG:
                if doNotNeed in  SGNode.lower():
                    doNot = doNot + 1
            # 剔除不要的分层SG节点，只保留原始SG
            if doNot == 0:
                # 获取shader
                shaderNode = mc.listConnections( SGNode + '.surfaceShader')
                if shaderNode:
                    # 获取提供透明属性的上级连接的节点
                    transpancyNode = ''
                    if mc.nodeType(shaderNode) != 'surfaceShader':
                        if mc.objExists(shaderNode[0] + '.transparency'):
                            transpancyAttr = mc.ls(shaderNode[0] + '.transparency')
                            transpancyNode = mc.listConnections(transpancyAttr[0], plugs = 1 , connections = 1 ,destination = 0 )
                    else:
                        transpancyAttr = mc.ls(shaderNode[0] + '.outTransparency')
                        transpancyNode = mc.listConnections(transpancyAttr[0], plugs = 1 , connections = 1 ,destination = 0 )
                    # 存在透明通道，则保存
                    if transpancyNode:
                        transpancyNode = mc.listConnections(transpancyAttr[0] , plugs = 1)
                        # SG节点命名判断
                        # 遵循'SHD_..._keyInfo_SG'
                        if ':' in SGNode:
                            #meshes = mc.listConnections(SGNode,type = 'mesh')
                            meshes = mc.sets(SGNode,q=1)
                            #记录信息
                            transparencySG.append([SGNode,meshes,transpancyNode[0]])
                        else:
                            #meshes = mc.listConnections(SGNode,type = 'mesh')
                            meshes = mc.sets(SGNode,q=1)
                            #记录信息
                            transparencySG.append([SGNode,meshes,transpancyNode[0]])

        return transparencySG

    #----------------------------------------------------------#
    # 获取有透明贴图的物体,通过参考获取服务器端数据
    # refNamespaceMode 0 Ref Mode | 1 Namespace Mode
    def idmtRLTransparencyObjs(self, refNamespaceMode = 1):
        from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
        reload(sk_referenceConfig)
        from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
        reload(sk_infoConfig)
        import os
        
        allAssetInfo = []
        allAssetNsInfo = []
        
        transpancySGNodesAll = []
        transpancyMeshesAll = []
        transpancyNodesAll = []
        
        # refInfo
        if refNamespaceMode == 0:
            refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
            refNodes = refInfos[0][0]
            refPaths = refInfos[1][0]
            refns    = refInfos[2][0]

            if refNodes:
                allAssetInfo = []
                for i in range(len(refNodes)):
                    # 非cam
                    if '_' in refNodes[i]:
                        assetFileName = refPaths[i].split('/')[-1]
                        assetInfo = assetFileName.split('_')
                        assetInfoNeed = assetInfo[0] + '_' + assetInfo[1] + '_' + assetInfo[2]
                        allAssetInfo.append(assetInfoNeed)
                        allAssetNsInfo.append(refns[i])
      
        # Namespace Mode
        if refNamespaceMode == 1:
            nsList = mc.namespaceInfo( listOnlyNamespaces = 1 )
            if 'UI' in nsList:
                nsList.remove('UI')
            if 'shared' in nsList:
                nsList.remove('shared')
            if nsList:
                for i in range(len(nsList)):
                    ns = nsList[i]
                    # 只要一级namespace
                    if '_' in ns and ":" not in ns:
                        assetInfo = ns.split('_')
                        if len(assetInfo) == 2:
                            assetInfoNeed = assetInfo[0] + '_' + assetInfo[1] + '_h'
                        if len(assetInfo) > 2:
                            assetInfoNeed = assetInfo[0] + '_' + assetInfo[1] + '_' + assetInfo[2]
                        allAssetInfo.append(assetInfoNeed)
                        allAssetNsInfo.append(ns)
                        
        print(allAssetInfo)
        print(allAssetNsInfo)
                        
        if allAssetInfo:
            # 获得asset的trans信息
            serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
            for asset in allAssetInfo:
                id = allAssetInfo.index(asset)
                assetInfo = asset.split('_')
                ns = allAssetNsInfo[id]
                serverTransPath = serverPath + 'data/AssetInfos/transShaderInfo/' + assetInfo[0] + '/' + str(assetInfo[1]) + '/' + str(assetInfo[2]) + '/'
                print(serverTransPath)
                # asset SG 信息
                assetTransSGNodes = []
                if os.path.exists(serverTransPath + 'transSGNodes.txt'):
                    assetTransSGNodesTemp = sk_infoConfig.sk_infoConfig().checkFileRead(serverTransPath + 'transSGNodes.txt')
                    for info in assetTransSGNodesTemp:
                        assetTransSGNodes.append( ns + ':' + info)
                # asset Mesh 信息
                assetTransMeshesTemp = []
                if os.path.exists(serverTransPath + 'transMeshes.txt'):
                    assetTransMeshesTemp = sk_infoConfig.sk_infoConfig().checkFileRead(serverTransPath + 'transMeshes.txt')
                # asset Shader Node 信息
                assetTransNodes = []
                if os.path.exists(serverTransPath + 'transNodes.txt'):
                    assetTransNodesTemp = sk_infoConfig.sk_infoConfig().checkFileRead(serverTransPath + 'transNodes.txt')
                    for info in assetTransNodesTemp:
                        if info[:6] == '[food]':
                            #assetTransNodes.append( float(info[7:]) )
                            assetTransNodes.append(info)
                        else:
                            assetTransNodes.append( ns + ':' + info)
                assetTransMeshes = []
                # 处理assetTransMeshesTemp,恢复namespace
                if assetTransMeshesTemp:
                    for lineInfo in assetTransMeshesTemp:
                        needInfo = []
                        if ', ' not in lineInfo:
                            tempInfo = ns + ':' + str(lineInfo[3:-2])
                            needInfo.append(tempInfo)
                        else:
                            allInfos = lineInfo.split(', ')
                            for j in range(len(allInfos)):
                                tempInfo = ''
                                if j == 0 or j == (len(allInfos)-1):
                                    if j == 0:
                                        tempInfo = ns + ':' + allInfos[j][3:-1]
                                    else:
                                        tempInfo = ns + ':' + allInfos[j][2:-2]
                                else:
                                    tempInfo = ns + ':' + allInfos[j][2:-1]
                                needInfo.append(tempInfo)
                        assetTransMeshes.append(needInfo)
                
                # 记录信息
                transpancySGNodesAll = transpancySGNodesAll + assetTransSGNodes
                transpancyMeshesAll  = transpancyMeshesAll + assetTransMeshes
                transpancyNodesAll   = transpancyNodesAll + assetTransNodes
                        
        result  = []
        result.append(transpancySGNodesAll)
        result.append(transpancyMeshesAll)
        result.append(transpancyNodesAll)
        return result
    
    #----------------------------------------------------------#
    # 获取有置换贴图的物体
    def idmtRLDisplacementObjsOld(self):
        displacementSG = []
        errorNameSG = []
        
        displacementSGNodesAll = []
        displacementMeshesAll = []
        displacementNodesAll = []
        
        # 获取file节点
        SGNodes = mc.ls(type = 'shadingEngine')
        for SGNode in SGNodes:
            # 判断SG节点是否有置换连接
            displacementCheck = 0
            checkDisNo1 = mc.listConnections((SGNode + '.displacementShader'),s = 1)
            if checkDisNo1:
                displacementCheck = 1
            if mc.objExists(SGNode + '.miDisplacementShader'):
                checkDisNo2 = mc.listConnections((SGNode + '.miDisplacementShader'),s = 1)
                if checkDisNo2:
                    displacementCheck = 2
            if displacementCheck:
                needDisplacementSG = SGNode
                needDisplacementMeshes = mc.sets(SGNode,q=1)
                if displacementCheck == 1:
                    needDisplacementShader = mc.listConnections((SGNode + '.displacementShader'),s = 1)[0]
                if displacementCheck == 2:
                    needDisplacementShader = mc.listConnections((SGNode + '.miDisplacementShader'),s = 1)[0]
                displacementSG.append( [ needDisplacementSG , needDisplacementMeshes , needDisplacementShader ] )

        return displacementSG
    
    
    #----------------------------------------------------------#
    # 获取有置换贴图的物体,通过参考获取服务器端数据
    # refNamespaceMode 0 Ref Mode | 1 Namespace Mode
    def idmtRLDisplacementObjs(self, refNamespaceMode = 1):
        from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
        reload(sk_referenceConfig)
        from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
        reload(sk_infoConfig)
        import os
        
        allAssetInfo = []
        allAssetNsInfo = []
        
        displacementSGNodesAll = []
        displacementMeshesAll = []
        displacementNodesAll = []
        
        # refInfo
        if refNamespaceMode == 0:
            refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
            refNodes = refInfos[0][0]
            refPaths = refInfos[1][0]
            refns    = refInfos[2][0]

            if refNodes:
                allAssetInfo = []
                for i in range(len(refNodes)):
                    # 非cam
                    if '_' in refNodes[i]:
                        assetFileName = refPaths[i].split('/')[-1]
                        assetInfo = assetFileName.split('_')
                        assetInfoNeed = assetInfo[0] + '_' + assetInfo[1] + '_' + assetInfo[2]
                        allAssetInfo.append(assetInfoNeed)
                        allAssetNsInfo.append(refns[i])
      
        # Namespace Mode
        if refNamespaceMode == 1:
            nsList = mc.namespaceInfo( listOnlyNamespaces = 1 )
            if 'UI' in nsList:
                nsList.remove('UI')
            if 'shared' in nsList:
                nsList.remove('shared')
            if nsList:
                for i in range(len(nsList)):
                    ns = nsList[i]
                    # 只要一级namespace
                    if '_' in ns and ":" not in ns:
                        assetInfo = ns.split('_')
                        if len(assetInfo) == 2:
                            assetInfoNeed = assetInfo[0] + '_' + assetInfo[1] + '_h'
                        if len(assetInfo) > 2:
                            assetInfoNeed = assetInfo[0] + '_' + assetInfo[1] + '_' + assetInfo[2]
                        allAssetInfo.append(assetInfoNeed)
                        allAssetNsInfo.append(ns)
                        
        print(allAssetInfo)
        print(allAssetNsInfo)
                        
        if allAssetInfo:
            # 获得asset的trans信息
            serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
            for asset in allAssetInfo:
                id = allAssetInfo.index(asset)
                assetInfo = asset.split('_')
                ns = allAssetNsInfo[id]
                serverTransPath = serverPath + 'data/AssetInfos/displacementShaderInfo/' + assetInfo[0] + '/' + str(assetInfo[1]) + '/' + str(assetInfo[2]) + '/'
                print(serverTransPath)
                # asset SG 信息
                assetTransSGNodes = []
                if os.path.exists(serverTransPath + 'displacementSGNodes.txt'):
                    assetTransSGNodesTemp = sk_infoConfig.sk_infoConfig().checkFileRead(serverTransPath + 'displacementSGNodes.txt')
                    for info in assetTransSGNodesTemp:
                        assetTransSGNodes.append( ns + ':' + info)
                # asset Mesh 信息
                assetTransMeshesTemp = []
                if os.path.exists(serverTransPath + 'displacementMeshes.txt'):
                    assetTransMeshesTemp = sk_infoConfig.sk_infoConfig().checkFileRead(serverTransPath + 'displacementMeshes.txt')
                # asset Shader Node 信息
                assetTransNodes = []
                if os.path.exists(serverTransPath + 'displacementNodes.txt'):
                    assetTransNodesTemp = sk_infoConfig.sk_infoConfig().checkFileRead(serverTransPath + 'displacementNodes.txt')
                    for info in assetTransNodesTemp:
                        assetTransNodes.append( ns + ':' + info)
                assetTransMeshes = []
                # 处理assetTransMeshesTemp,恢复namespace
                if assetTransMeshesTemp:
                    for lineInfo in assetTransMeshesTemp:
                        needInfo = []
                        if ', ' not in lineInfo:
                            tempInfo = ns + ':' + str(lineInfo[3:-2])
                            needInfo.append(tempInfo)
                        else:
                            allInfos = lineInfo.split(', ')
                            for j in range(len(allInfos)):
                                tempInfo = ''
                                if j == 0 or j == (len(allInfos)-1):
                                    if j == 0:
                                        tempInfo = ns + ':' + allInfos[j][3:-1]
                                    else:
                                        tempInfo = ns + ':' + allInfos[j][2:-2]
                                else:
                                    tempInfo = ns + ':' + allInfos[j][2:-1]
                                needInfo.append(tempInfo)
                        assetTransMeshes.append(needInfo)
                
                # 记录信息
                displacementSGNodesAll = displacementSGNodesAll + assetTransSGNodes
                displacementMeshesAll  = displacementMeshesAll + assetTransMeshes
                displacementNodesAll   = displacementNodesAll + assetTransNodes
                        
        result  = []
        result.append(displacementSGNodesAll)
        result.append(displacementMeshesAll)
        result.append(displacementNodesAll)
        return result
