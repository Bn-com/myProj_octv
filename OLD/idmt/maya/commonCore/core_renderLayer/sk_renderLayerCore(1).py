# -*- coding: utf-8 -*-

'''
Created on 2014-01-24

@author: shenkang
'''

import maya.cmds as mc
import maya.mel as mel
import idmt.pipeline.db
import os,re
from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
reload(sk_infoConfig)

# shader import 
# file nodes ,for tga ,filter off ,for map ,filter config minmap


class sk_renderLayerCore(object):
    def __init__(self):
        pass
    #----------------------------------------------------------------------------------------------------------#
    
    #----------------------------------------------------------#
    # 渲染标准设置
    def idmtRLCommonConfig(self):
        print(u'===============!!!Start 【%s】!!!===============' % u'标准设置')
        print('Working...')
        # Camera
        from idmt.maya.commonCore.core_mayaCommon import sk_hbExportCam
        reload(sk_hbExportCam)
        # sk_hbExportCam.sk_hbExportCam().camServerReference()   

        # 开启窗口，创建各种UI
        #mel.eval('unifiedRenderGlobalsWindow')

        # IKR开启
        mc.setAttr('defaultRenderGlobals.preMel',"ikSystem -e -sol 1",type = 'string')

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
        print('\n')
        
    #----------------------------------------------------------------------------------------------------------#  
    #----------------------------------------------------------#
    # mr 产品级设置    
    def idmtMentalRayProductionLevel(self):
        print(u'===============!!!Start 【%s】!!!===============' % u'MR设置')
        print('Working...')
        
        mc.setAttr('defaultRenderGlobals.imageFormat', 7)
           
        if not(mc.pluginInfo("Mayatomr.mll",query=1,loaded=1)):
            mel.eval('loadPlugin "Mayatomr"')
            
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

        print(u'===============!!!Done  【%s】!!!===============' %u'MR设置')
        print('\n')
        
    #----------------------------------------------------------------------------------------------------------#
    #----------------------------------------------------------#
    # arnold 设置    
    def idmtArnoldRendererSettings(self):
        print(u'===============!!!Start 【%s】!!!===============' %u'Arnold设置')
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

        
        print(u'===============!!!Done  【%s】!!!===============' %u'Arnold设置')
        print('\n')

    #----------------------------------------------------------------------------------------------------------#
    #----------------------------------------------------------#
    # arnold renderpass 创建
    def idmtRLArnoldRenderpassCreate(self):
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
        mc.connectAttr('%s.%s'%(AOShader , 'outColor') , '%s.%s'%(AOSG , 'surfaceShader'), f=True)
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
        mc.connectAttr('%s.%s'%(NMShader , 'outColor') , '%s.%s'%(NMSG , 'surfaceShader'), f=True)
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
        mc.connectAttr('%s.%s'%(FNShader , 'outColor') , '%s.%s'%(FNSG , 'surfaceShader'), f=True)
        mc.connectAttr('%s.%s'%(FNSample , 'facingRatio') , '%s.%s'%(FNRamp , 'uCoord'), f=True)
        mc.connectAttr('%s.%s'%(FNSample , 'facingRatio') , '%s.%s'%(FNRamp , 'vCoord'), f=True)
        mc.connectAttr('%s.%s'%(FNRamp , 'outColor') , '%s.%s'%(FNShader , 'color'), f=True)
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
        mc.connectAttr('%s.%s'%(keyLightShader , 'outColor') , '%s.%s'%(keyLightSG , 'surfaceShader'), f=True)
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
        mc.connectAttr('%s.%s'%(shadowShader , 'outColor') , '%s.%s'%(shadowSG , 'surfaceShader'), f=True)
        
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
            mc.disconnectAttr('%s.%s'%('defaultArnoldDriver' , 'message') , '%s.%s'%(ZArnoldPass , 'outputs[0].driver'))
        except:
            pass
        mc.connectAttr('%s.%s'%('defaultArnoldDriver' , 'message') , '%s.%s'%(ZArnoldPass , 'outputs[0].driver'), f=True)
        try:
            mc.disconnectAttr('%s.%s'%( aiAOVFilter_Closset , 'message') , '%s.%s'%(ZArnoldPass, 'outputs[0].filter'))
        except:
            pass
        mc.connectAttr('%s.%s'%( aiAOVFilter_Closset , 'message') , '%s.%s'%(ZArnoldPass, 'outputs[0].filter'), f=True)
        try:
            mc.disconnectAttr('%s.%s'%( ZArnoldPass , 'message') , '%s.%s'%('defaultArnoldRenderOptions' , 'aovList[0]'))
        except:
            pass
        mc.connectAttr('%s.%s'%( ZArnoldPass , 'message') , '%s.%s'%('defaultArnoldRenderOptions' , 'aovList[0]'), f=True)
        #----------------------#
        # occ
        try:
            mc.disconnectAttr('%s.%s'%('defaultArnoldDriver' , 'message') , '%s.%s'%(occArnoldPass , 'outputs[0].driver'))
        except:
            pass
        mc.connectAttr('%s.%s'%('defaultArnoldDriver' , 'message') , '%s.%s'%(occArnoldPass , 'outputs[0].driver'), f=True)
        try:
            mc.disconnectAttr('%s.%s'%( 'defaultArnoldFilter' , 'message') , '%s.%s'%(occArnoldPass, 'outputs[0].filter'))
        except:
            pass
        mc.connectAttr('%s.%s'%( 'defaultArnoldFilter' , 'message') , '%s.%s'%(occArnoldPass, 'outputs[0].filter'), f=True)
        try:
            mc.disconnectAttr('%s.%s'%( AOShader , 'outColor') , '%s.%s'%(occArnoldPass, 'defaultValue'))
        except:
            pass
        mc.connectAttr('%s.%s'%( AOShader , 'outColor') , '%s.%s'%(occArnoldPass, 'defaultValue'), f=True)
        mc.setAttr((AOShader + '.samples'),4)
        try:
            mc.disconnectAttr('%s.%s'%( occArnoldPass , 'message') , '%s.%s'%('defaultArnoldRenderOptions' , 'aovList[1]'))
        except:
            pass
        mc.connectAttr('%s.%s'%( occArnoldPass , 'message') , '%s.%s'%('defaultArnoldRenderOptions' , 'aovList[1]'), f=True)
        #----------------------#
        # normal
        try:
            mc.disconnectAttr('%s.%s'%('defaultArnoldDriver' , 'message') , '%s.%s'%(nmArnoldPass , 'outputs[0].driver'))
        except:
            pass
        mc.connectAttr('%s.%s'%('defaultArnoldDriver' , 'message') , '%s.%s'%(nmArnoldPass , 'outputs[0].driver'), f=True)
        try:
            mc.disconnectAttr('%s.%s'%( 'defaultArnoldFilter' , 'message') , '%s.%s'%(nmArnoldPass , 'outputs[0].filter'))
        except:
            pass
        mc.connectAttr('%s.%s'%( 'defaultArnoldFilter' , 'message') , '%s.%s'%(nmArnoldPass , 'outputs[0].filter'), f=True)
        try:
            mc.disconnectAttr('%s.%s'%( NMShader , 'outColor') , '%s.%s'%(nmArnoldPass, 'defaultValue'))
        except:
            pass
        mc.connectAttr('%s.%s'%( NMShader , 'outColor') , '%s.%s'%(nmArnoldPass, 'defaultValue'), f=True)
        try:
            mc.disconnectAttr('%s.%s'%( nmArnoldPass , 'message') , '%s.%s'%('defaultArnoldRenderOptions' , 'aovList[2]'))
        except:
            pass
        mc.connectAttr('%s.%s'%( nmArnoldPass , 'message') , '%s.%s'%('defaultArnoldRenderOptions' , 'aovList[2]'), f=True)
        #----------------------#
        # frese
        try:
            mc.disconnectAttr('%s.%s'%('defaultArnoldDriver' , 'message') , '%s.%s'%(fresenlArnoldPass , 'outputs[0].driver'))
        except:
            pass
        mc.connectAttr('%s.%s'%('defaultArnoldDriver' , 'message') , '%s.%s'%(fresenlArnoldPass , 'outputs[0].driver'), f=True)
        try:
            mc.disconnectAttr('%s.%s'%( 'defaultArnoldFilter' , 'message') , '%s.%s'%(fresenlArnoldPass , 'outputs[0].filter'))
        except:
            pass
        mc.connectAttr('%s.%s'%( 'defaultArnoldFilter' , 'message') , '%s.%s'%(fresenlArnoldPass , 'outputs[0].filter'), f=True)
        try:
            mc.disconnectAttr('%s.%s'%( FNShader , 'outColor') , '%s.%s'%(fresenlArnoldPass, 'defaultValue'))
        except:
            pass
        mc.connectAttr('%s.%s'%( FNShader , 'outColor') , '%s.%s'%(fresenlArnoldPass, 'defaultValue'), f=True)
        try:
            mc.disconnectAttr('%s.%s'%( fresenlArnoldPass , 'message') , '%s.%s'%('defaultArnoldRenderOptions' , 'aovList[3]'))
        except:
            pass
        mc.connectAttr('%s.%s'%( fresenlArnoldPass , 'message') , '%s.%s'%('defaultArnoldRenderOptions' , 'aovList[3]'), f=True)
        #----------------------#
        # keyLight
        try:
            mc.disconnectAttr('%s.%s'%('defaultArnoldDriver' , 'message') , '%s.%s'%(keyLightArnoldPass , 'outputs[0].driver'))
        except:
            pass
        mc.connectAttr('%s.%s'%('defaultArnoldDriver' , 'message') , '%s.%s'%(keyLightArnoldPass , 'outputs[0].driver'), f=True)
        try:
            mc.disconnectAttr('%s.%s'%( 'defaultArnoldFilter' , 'message') , '%s.%s'%(keyLightArnoldPass , 'outputs[0].filter'))
        except:
            pass
        mc.connectAttr('%s.%s'%( 'defaultArnoldFilter' , 'message') , '%s.%s'%(keyLightArnoldPass , 'outputs[0].filter'), f=True)
        try:
            mc.disconnectAttr('%s.%s'%( keyLightShader , 'outColor') , '%s.%s'%(keyLightArnoldPass, 'defaultValue'))
        except:
            pass
        mc.connectAttr('%s.%s'%( keyLightShader , 'outColor') , '%s.%s'%(keyLightArnoldPass, 'defaultValue'), f=True)
        try:
            mc.disconnectAttr('%s.%s'%( keyLightArnoldPass , 'message') , '%s.%s'%('defaultArnoldRenderOptions' , 'aovList[4]'))
        except:
            pass
        mc.connectAttr('%s.%s'%( keyLightArnoldPass , 'message') , '%s.%s'%('defaultArnoldRenderOptions' , 'aovList[4]'), f=True)
        #----------------------#
        # shadow
        try:
            mc.disconnectAttr('%s.%s'%('defaultArnoldDriver' , 'message') , '%s.%s'%(shadowArnoldPass , 'outputs[0].driver'))
        except:
            pass
        mc.connectAttr('%s.%s'%('defaultArnoldDriver' , 'message') , '%s.%s'%(shadowArnoldPass , 'outputs[0].driver'), f=True)
        try:
            mc.disconnectAttr('%s.%s'%( 'defaultArnoldFilter' , 'message') , '%s.%s'%(shadowArnoldPass , 'outputs[0].filter'))
        except:
            pass
        mc.connectAttr('%s.%s'%( 'defaultArnoldFilter' , 'message') , '%s.%s'%(shadowArnoldPass , 'outputs[0].filter'), f=True)
        try:
            mc.disconnectAttr('%s.%s'%( shadowShader , 'outColor') , '%s.%s'%(shadowArnoldPass, 'defaultValue'))
        except:
            pass
        mc.connectAttr('%s.%s'%( shadowShader , 'outColor') , '%s.%s'%(shadowArnoldPass, 'defaultValue'), f=True)
        try:
            mc.disconnectAttr('%s.%s'%( shadowArnoldPass , 'message') , '%s.%s'%('defaultArnoldRenderOptions' , 'aovList[5]'))
        except:
            pass
        mc.connectAttr('%s.%s'%( shadowArnoldPass , 'message') , '%s.%s'%('defaultArnoldRenderOptions' , 'aovList[5]'), f=True)
        

    #----------------------------------------------------------------------------------------------------------#
    #----------------------------------------------------------#
    # arnold RGB 系统
    #----------------------------------------------------------#
    # RGB Base创建
    def idmtArnoldRGBBaseSetup(self):
        shaderKey = ['R' ,'G' ,'B']
        colorInfo = [[1,0,0],[0,1,0],[0,0,1]]
        
        for i in range(len(shaderKey)):
            redShader = 'IDMT_' + shaderKey[i] + '_Arnold'
            if mc.ls(redShader):
                mc.delete(redShader)
            redShader = mc.shadingNode ('aiUtility', asShader=True, name= redShader)  
            mc.setAttr(redShader + '.shadeMode',2)
            mc.setAttr(redShader + '.color',colorInfo[i][0],colorInfo[i][1],colorInfo[i][2],type = 'double3')
    
    #----------------------------------------------------------#
    # 赋予材质模式
    def idmtArnoldRGBCreate(self,RGBType = 'R'):
        # 获取选取物体的SG
        selObjs = mc.ls(sl = 1,l = 1)
        selMeshes = []
        if selObjs:
            selMeshes = mc.listRelatives(selObjs,ni = 1 ,s = 1 ,type = 'mesh')
        if selMeshes:
            # 获取Shader
            needShaders = []
            needSGNodes = []
            for mesh in selMeshes:
                SGNodes = mc.listConnections(mesh,d = 1 ,type = 'shadingEngine')
                if not SGNodes:
                    continue
                for SGNode in SGNodes:
                    shader = mc.listConnections((SGNode + '.surfaceShader'),s = 1)
                    if shader:
                        needShaders.append(shader[0])
                        needSGNodes.append(SGNode)
            # 处理连接
            if needShaders:
                for shader in needShaders:
                    RGBConnectNode = 'IDMT_aiWC_' + shader
                    if mc.ls(RGBConnectNode):
                        mc.delete(RGBConnectNode)
                        
                    RGBConnectUtility = 'IDMT_aiAU_' + shader
                    if mc.ls(RGBConnectUtility):
                        mc.delete(RGBConnectUtility)
                        
                    RGBConnectNode = mc.shadingNode ('aiWriteColor', asShader=True, name= RGBConnectNode)
                    RGBConnectUtility = mc.shadingNode ('aiUtility', asShader=True, name= RGBConnectUtility)
                    mc.setAttr(RGBConnectUtility + '.shadeMode',2)
                    
                    mc.connectAttr((shader + '.outColor'),(RGBConnectNode + '.beauty'),f = 1)
                    mc.connectAttr(('IDMT_' + RGBType + '_Arnold' + '.outColor'),(RGBConnectNode + '.input'),f = 1)
                    mc.connectAttr((RGBConnectNode + '.outColor'),(RGBConnectUtility + '.color'),f = 1)
                    mc.connectAttr((RGBConnectUtility + '.outColor'),(needSGNodes[needShaders.index(shader)] + '.surfaceShader'),f = 1)

    
    #----------------------------------------------------------#
    # UI
    #----------------------------------------------------------#
    def idmtArnoldRGBUI(self):
        # 窗口
        if mc.window ("idmtArnoldRGBUI", ex=1):
            mc.deleteUI("idmtArnoldRGBUI", window=True)
        mc.window("idmtArnoldRGBUI", title="idmtArnoldRGBUI", widthHeight=(180, 200), menuBar=0)
        # 主界面
        mc.columnLayout()

        # Arnold加载
        mc.rowLayout()
        mc.button(label=u'【Arnold】【构建】', backgroundColor=[0.0, 0.0, 0.0], width=160, height=30, c='sk_renderLayerCore.sk_renderLayerCore().idmtArnoldRendererSettings()')
        mc.setParent("..")

        # RGB创建
        mc.rowLayout()
        mc.button(label=u'【RGB】【构建】', backgroundColor=[0.0, 0.0, 0.0], width=160, height=30, c='sk_renderLayerCore.sk_renderLayerCore().idmtArnoldRGBBaseSetup()')
        mc.setParent("..")
        
        # R创建
        mc.rowLayout()
        mc.button(label=u'【R】【赋色】', backgroundColor=[1.0, 0.0, 0.0], width=160, height=30, c='sk_renderLayerCore.sk_renderLayerCore().idmtArnoldRGBCreate(\"R\")')
        mc.setParent("..")
        
        # G创建
        mc.rowLayout()
        mc.button(label=u'【G】【赋色】', backgroundColor=[0.0, 1.0, 0.0], width=160, height=30, c='sk_renderLayerCore.sk_renderLayerCore().idmtArnoldRGBCreate(\"G\")')
        mc.setParent("..")
        
        # B创建
        mc.rowLayout()
        mc.button(label=u'【B】【赋色】', backgroundColor=[0.0, 0.0, 1.0], width=160, height=30, c='sk_renderLayerCore.sk_renderLayerCore().idmtArnoldRGBCreate(\"B\")')
        mc.setParent("..")
        
        mc.setParent("..")
        mc.showWindow("idmtArnoldRGBUI")


    #----------------------------------------------------------------------------------------------------------#
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
    
    #----------------------------------------------------------------------------------------#
    # 【通用：RGB分层输出系统】
    # Author : 沈  康
    # Data   : 2013_11_18/2014_05_10
    # Data   : 2014_5_28/2014_06_10
    #-------------------------------------------------#
    def ydRLayerRGBOutPutUI(self):
        # 窗口
        if mc.window ("sk_ydRGBOutPutTools",ex=1):
            mc.deleteUI( "sk_ydRGBOutPutTools", window=True )
        mc.window("sk_ydRGBOutPutTools",title="ydRGBOutputTools", widthHeight=(180, 300),menuBar=0)

        # 面板
        form = mc.formLayout()
        # 切换面板
        tabs = mc.tabLayout(innerMarginWidth=5, innerMarginHeight=5)
        mc.formLayout( form, edit=True, attachForm=((tabs, 'top', 0), (tabs, 'left', 0), (tabs, 'bottom', 0), (tabs, 'right', 0)) )
        
        # FullBody类
        child1 = mc.rowColumnLayout()
        
        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0,0,0],label = (unicode('【FBR】【Asset】测试', 'utf8')),c = 'from idmt.maya.commonPerform.renderLayers import sk_renderLayer_Yoda\nreload(sk_renderLayer_Yoda)\nsk_renderLayer_Yoda.sk_renderLayer_Yoda().ydRLayerRGBInfoAssetTest(\"FullBody\",1,1)')
        mc.setParent("..")   

        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0,0,0.0],label = (unicode('===【RGBM】创建===', 'utf8')),c = 'from idmt.maya.commonPerform.renderLayers import sk_renderLayer_Yoda\nreload(sk_renderLayer_Yoda)\nsk_renderLayer_Yoda.sk_renderLayer_Yoda().ydRLRGBBaseShaderCreate(1)')
        mc.setParent("..")  

        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [.8,0,0],label = (unicode('【R】【选材质球】输出', 'utf8')),c = 'from idmt.maya.commonPerform.renderLayers import sk_renderLayer_Yoda\nreload(sk_renderLayer_Yoda)\nsk_renderLayer_Yoda.sk_renderLayer_Yoda().ydRLayerRGBInfoExport(\"FullBody\",\"R\",1)')
        mc.setParent("..")  

        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0,0.8,0],label = (unicode('【G】【选材质球】输出', 'utf8')),c = 'from idmt.maya.commonPerform.renderLayers import sk_renderLayer_Yoda\nreload(sk_renderLayer_Yoda)\nsk_renderLayer_Yoda.sk_renderLayer_Yoda().ydRLayerRGBInfoExport(\"FullBody\",\"G\",1)')
        mc.setParent("..")   

        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0,0.3,0.8],label = (unicode('【B】【选材质球】输出', 'utf8')),c = 'from idmt.maya.commonPerform.renderLayers import sk_renderLayer_Yoda\nreload(sk_renderLayer_Yoda)\nsk_renderLayer_Yoda.sk_renderLayer_Yoda().ydRLayerRGBInfoExport(\"FullBody\",\"B\",1)')
        mc.setParent("..")   

        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0.65,0.65,0.65],label = (unicode('【M】【选材质球】输出', 'utf8')),c = 'from idmt.maya.commonPerform.renderLayers import sk_renderLayer_Yoda\nreload(sk_renderLayer_Yoda)\nsk_renderLayer_Yoda.sk_renderLayer_Yoda().ydRLayerRGBInfoExport(\"FullBody\",\"M\",1)')
        mc.setParent("..")   
        
        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0,0,0.0],label = (unicode('===FullBody===', 'utf8')))
        mc.setParent("..")  

        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0,0,0],label = (unicode('【FBR】【信息】【清理】', 'utf8')),c = 'from idmt.maya.commonPerform.renderLayers import sk_renderLayer_Yoda\nreload(sk_renderLayer_Yoda)\nsk_renderLayer_Yoda.sk_renderLayer_Yoda().ydRLayerRGBInfoClean(\"FullBody\",1)')
        mc.setParent("..")  
        mc.setParent("..") 
        
        # ShortParts类
        child2 = mc.rowColumnLayout()
        
        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0,0,0],label = (unicode('【SPR】【Asset】测试', 'utf8')),c = 'from idmt.maya.commonPerform.renderLayers import sk_renderLayer_Yoda\nreload(sk_renderLayer_Yoda)\nsk_renderLayer_Yoda.sk_renderLayer_Yoda().ydRLayerRGBInfoAssetTest(\"ShortParts\",1,1)')
        mc.setParent("..")   
    
        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0,0,0.0],label = (unicode('===【RGBM】创建===', 'utf8')),c = 'from idmt.maya.commonPerform.renderLayers import sk_renderLayer_Yoda\nreload(sk_renderLayer_Yoda)\nsk_renderLayer_Yoda.sk_renderLayer_Yoda().ydRLRGBBaseShaderCreate(1)')
        mc.setParent("..")   
        
        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [.8,0,0],label = (unicode('【R】【选材质球】输出', 'utf8')),c = 'from idmt.maya.commonPerform.renderLayers import sk_renderLayer_Yoda\nreload(sk_renderLayer_Yoda)\nsk_renderLayer_Yoda.sk_renderLayer_Yoda().ydRLayerRGBInfoExport(\"ShortParts\",\"R\",1)')
        mc.setParent("..")  

        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0,0.8,0],label = (unicode('【G】【选材质球】输出', 'utf8')),c = 'from idmt.maya.commonPerform.renderLayers import sk_renderLayer_Yoda\nreload(sk_renderLayer_Yoda)\nsk_renderLayer_Yoda.sk_renderLayer_Yoda().ydRLayerRGBInfoExport(\"ShortParts\",\"G\",1)')
        mc.setParent("..")   

        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0,0.3,0.8],label = (unicode('【B】【选材质球】输出', 'utf8')),c = 'from idmt.maya.commonPerform.renderLayers import sk_renderLayer_Yoda\nreload(sk_renderLayer_Yoda)\nsk_renderLayer_Yoda.sk_renderLayer_Yoda().ydRLayerRGBInfoExport(\"ShortParts\",\"B\",1)')
        mc.setParent("..")   

        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0.7,0.7,0.7],label = (unicode('【M】【选材质球】输出', 'utf8')),c = 'from idmt.maya.commonPerform.renderLayers import sk_renderLayer_Yoda\nreload(sk_renderLayer_Yoda)\nsk_renderLayer_Yoda.sk_renderLayer_Yoda().ydRLayerRGBInfoExport(\"ShortParts\",\"M\",1)')
        mc.setParent("..")   
        
        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0,0,0.0],label = (unicode('===ShortParts===', 'utf8')))
        mc.setParent("..")   
        
        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0,0,0],label = (unicode('【SPR】【信息】【清理】', 'utf8')),c = 'from idmt.maya.commonPerform.renderLayers import sk_renderLayer_Yoda\nreload(sk_renderLayer_Yoda)\nsk_renderLayer_Yoda.sk_renderLayer_Yoda().ydRLayerRGBInfoClean(\"ShortParts\",1)')
        mc.setParent("..")   
        
        mc.setParent("..") 
        
        mc.tabLayout( tabs, edit=True, tabLabel=((child1, unicode('===FullBody===', 'utf8')), (child2, unicode('===ShortParts===', 'utf8'))) )
        
        mc.showWindow( "sk_ydRGBOutPutTools" )

    #--------------------------#
    # 标准材质球创建
    def ydRLRGBBaseShaderCreate(self,RGBMode = 0):
        for i in range(4):
            # color
            if i == 0:
                key = 'R'
                colors = [1.0 , 0.0 , 0.0]
            if i == 1:
                key = 'G'
                colors = [0.0 , 1.0 , 0.0]
            if i == 2:
                key = 'M'
                colors = [0.0 , 0.0 , 1.0]
            if i == 3:
                key = 'B'
                colors = [0.0 , 0.0 , 0.0]
            # 创建材质球
            shaderTest = 'SHD_testIDP_' + key + '_Shader'
            if mc.ls(shaderTest):
                mc.delete(shaderTest)
            SGTest = 'SHD_testIDP_' + key + '_SG'
            if mc.ls(SGTest):
                mc.delete(SGTest)
            shaderTest = mc.shadingNode('lambert', asShader=True, name = shaderTest)
            SGTest = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name = SGTest)
            # 连接
            mc.setAttr((shaderTest + '.matteOpacityMode'), 2)
            if RGBMode:
                if colors[0] or colors[1] or colors[2]:
                    mc.setAttr((shaderTest + '.matteOpacity'), 0)
            mc.setAttr((shaderTest + '.color'), colors[0], colors[1], colors[2], type='double3')
            mc.setAttr((shaderTest + '.ambientColor'), 1, 1, 1, type='double3')
            mc.setAttr((shaderTest + '.diffuse'), 1)
            mc.connectAttr((shaderTest + '.outColor'), (SGTest + '.surfaceShader'))

    #--------------------------#
    # 分层信息输出
    # 数据结构：第一行，字符串，|分割三个通道信息；从第二行开始，每行一个mesh
    def ydRLayerRGBInfoExport(self, LayerName='FullBody', exportType='all', update = 0,openIt = False):
        localPath = sk_infoConfig.sk_infoConfig().checkLayerInfoLocalPath('RGB', LayerName)
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()

        fileName = 'RGB' + '_'+ shotInfo[1] + '_' + exportType + '_geo.txt'
        filePath = localPath + shotInfo[1] + '\\'+ fileName
        mc.sysFile((localPath + shotInfo[1] + '\\'),makeDir = 1)
        # 输出物体
        shader = mc.ls(sl=1)
        if not shader:
            mc.error(u'===请选中有效材质球=1==')
        if mc.nodeType(shader[0]) not in ['lambert','surfaceShader','aiUtility',u'aiStandard']:
            mc.error(u'===请选中有效材质球=2==')
        if mc.nodeType(shader[0]) in ['lambert','aiUtility',u'aiStandard']:
            colorInfo = mc.getAttr(shader[0] + '.color')
        if mc.nodeType(shader[0]) == 'surfaceShader':
            colorInfo = mc.getAttr(shader[0] + '.outColor')
        shaderColor = str(colorInfo[0][0]) + '|' + str(colorInfo[0][1]) + '|' + str(colorInfo[0][2])
        SGNodes = mc.listConnections(shader,d=1,type = 'shadingEngine')
        if not SGNodes:
            mc.error(u'===请选中有效材质球=3==')
        meshes = mc.sets(SGNodes,q=1)
        meshes = mc.ls(meshes, l = 1)
        if not meshes:
            mc.error(u'===请选中有效材质球=4==')
        # outputInfo
        outPutInfo = [shaderColor]
        for mesh in meshes:
            outPutInfo = outPutInfo + [mesh]
        sk_infoConfig.sk_infoConfig().checkFileWrite(filePath, outPutInfo)
        # update
        if update:
        # 本地及服务器端路径
            # 此处路径问题
            serverPath = sk_infoConfig.sk_infoConfig().checkLayerInfoServerPath('RGB', LayerName)
            serverFilePath = serverPath + shotInfo[1] + '\\' + fileName
            updateCMD = 'zwSysFile "copy" ' + '"' + (filePath.replace('\\', '/')) + '"' + ' ' + '"' + (serverFilePath.replace('\\', '/')) + '"' + ' true'
            mel.eval(updateCMD)
            # 注册数据库
            projName = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(shotInfo[0])
            userName = mel.eval('getenv \"USERNAME\"')
            info = projName + '|' + shotInfo[1] + '|' + userName
            mc.idmtService('RgbInput', info)
            
        print(u'========[%s]_[%s]_[输出]完毕！！！========'%(LayerName,exportType))
        if openIt:
            openPath = os.path.normpath(serverPath + shotInfo[1])
            os.startfile(openPath)
    #--------------------------#
    # 分层信息类别清空
    def ydRLayerRGBInfoClean(self,LayerName='FullBody' ,server  = 0 ):
        # 路径
        if server:
            filePath = sk_infoConfig.sk_infoConfig().checkLayerInfoServerPath('RGB', LayerName)

        else:
            filePath = sk_infoConfig.sk_infoConfig().checkLayerInfoLocalPath('RGB', LayerName)
        
        print(filePath.replace('\\','/')[:-1])
        delCmd = 'zwSysFile(\"rd\",\"' + filePath.replace('\\','/')[:-1] + '\",\"\",1)'
        mel.eval(delCmd)
        
        print(u'========[%s]_[清理]完毕！！！========'%LayerName)
        
    #--------------------------#
    # 分层信息验证
    # 创建材质球,不支持透明贴图
    def ydRLayerRGBInfoAssetTest(self,LayerName='FullBody' ,server  = 0 , RGBMode = 0):
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        
        allInfos = self.ydRLayerRGBInfoImport(LayerName , shotInfo[1] , server)
        
        if not allInfos:
            print(u'=========本Asset没有有效IDP信息=========')
            mc.error(u'=========本Asset没有有效IDP信息=========')
            
        # 分层
        meshes = mc.ls(type = 'mesh',l=1)
        needMeshes = []
        for mesh in meshes:
            if '|MODEL|' in mesh:
                obj = mc.listRelatives(mesh,p = 1 ,type = 'transform',f = 1)
                if obj:
                    needMeshes.append(mesh)
        meshes = needMeshes
        objs = mc.listRelatives(meshes,p = 1, type = 'transform' ,f = 1)
        objs = list(set(objs))
        
        if mc.ls(LayerName):
            mc.delete(LayerName)
        
        mc.createRenderLayer(objs, name = LayerName, noRecurse=1, makeCurrent=1)
        
        # 给与基本matte
        shaderMatte = 'SHD_testIDP_' + LayerName + '_Matte_Shader'
        if mc.ls(shaderMatte):
            mc.delete(shaderMatte)
        MatteSG = 'SHD_testIDP_' + LayerName + '_Matte_SG'
        if mc.ls(MatteSG):
            mc.delete(MatteSG)
        shaderMatte = mc.shadingNode('lambert', asShader=True, name = shaderMatte)
        MatteSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name = MatteSG)
        
        mc.setAttr((shaderMatte + '.color'), 0, 0, 0, type='double3')
        mc.setAttr((shaderMatte + '.ambientColor'), 1, 1, 1, type='double3')
        mc.setAttr((shaderMatte + '.diffuse'), 1)
        mc.setAttr((shaderMatte + '.matteOpacityMode'), 0)
        mc.connectAttr((shaderMatte + '.outColor'), (MatteSG + '.surfaceShader'))
        
        try:
            mc.sets(meshes,e = 1 , forceElement = MatteSG)
        except:
            for mesh in meshes:
                try:
                    mc.sets(mesh,e = 1 , forceElement = MatteSG)
                except:
                    print(mesh)
                    mc.error(u'===请检查本行上方，其无法正常着色===')
                
        # RGBA
        for i in range(len(allInfos)):
            info = allInfos[i]
            # color
            colors = info[0].split('|')
            colors = [float(colors[0]),float(colors[1]),float(colors[2])]
            # mesh
            meshes = info[1:]
            # 创建材质球
            shaderTest = 'SHD_testIDP_' + str(i) + '_' +  LayerName + '_Shader'
            if mc.ls(shaderTest):
                mc.delete(shaderTest)
            SGTest = 'SHD_testIDP_' + str(i) + '_' +  LayerName + '_SG'
            if mc.ls(SGTest):
                mc.delete(SGTest)
            shaderTest = mc.shadingNode('lambert', asShader=True, name = shaderTest)
            SGTest = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name = SGTest)
            # 连接
            mc.setAttr((shaderTest + '.matteOpacityMode'), 2)
            if RGBMode:
                if colors[0] or colors[1] or colors[2]:
                    mc.setAttr((shaderTest + '.matteOpacity'), 0)
            mc.setAttr((shaderTest + '.color'), colors[0], colors[1], colors[2], type='double3')
            mc.setAttr((shaderTest + '.ambientColor'), 1, 1, 1, type='double3')
            mc.setAttr((shaderTest + '.diffuse'), 1)
            mc.connectAttr((shaderTest + '.outColor'), (SGTest + '.surfaceShader'))
            # 赋予材质
            mc.sets(meshes, e=1, forceElement = SGTest)
            
        print(u'----------[RGB_%s]    Done!!!----------'%LayerName)

    #----------------------------------------------------------------------------------------#
    # 【通用：RGB分层读取系统】
    # Author : 沈  康
    # Data   : 2013_11_18/2014_05_10
    # Data   : 2014_5_28/2014_06_10
    #----------------------------------------------------------------------------------------#
    #--------------------------#
    # 分层信息读取
    def ydRLayerRGBInfoImport(self,LayerName = 'FullBody', assetName = '' ,server = 0):
        # 路径
        if server:
            serverPath = sk_infoConfig.sk_infoConfig().checkLayerInfoServerPath('RGB', LayerName)
            filePath = serverPath + assetName + '\\' 
        else:
            localPath = sk_infoConfig.sk_infoConfig().checkLayerInfoLocalPath('RGB', LayerName)
            filePath = localPath + assetName + '\\' 
            
        #print(filePath)
        alllFiles = mc.getFileList(folder = filePath)

        if not alllFiles:
            return []
        
        # 读文件
        result = []
        for fileName in alllFiles:
            if fileName[-4:] != '.txt':
                continue
            result.append(sk_infoConfig.sk_infoConfig().checkFileRead(filePath + fileName))
        return result

    #--------------------------#
    # 获取文件内所有asset的RGB素材信息
    # specialType 为SK之类的特殊asset编号提供，偏移到第二位判断asset类别
    # 数据结构：两个list
    # 第一个list，多个颜色信息的组合，每个颜色信息也是个list记录RGB通道信息
    # 第二个list，与第一个list对应，每个元素是对应颜色信息的meshlist(有根据namespace调整信息)
    # namespace使用条件：文件整理过，namespace通过reference路径变更过结构
    # 改版：无视参考模式
    def ydRLayerRGBObjectsConfig(self, LayerName = 'FullBody', specialType = 0 , server = 1 ):
        from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
        reload(sk_referenceConfig)
        shaderColor = []
        shaderMeshes = []
        #refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        #refNamespace = refInfos[2][0]
        needNamespaces = mc.namespaceInfo(listOnlyNamespaces=1)
        for ns in needNamespaces:
            if '_' not in ns:
                continue
            if ns.split('_')[1][specialType] in ['c','p','s'] or ns.split('_')[1][specialType] in ['C','P','S'] :
                assetName = ns.split('_')[1]
                allInfos = self.ydRLayerRGBInfoImport(LayerName,assetName,server)
                for info in allInfos:
                    # color
                    shaderColor.append([float(info[0].split('|')[0]),float(info[0].split('|')[1]),float(info[0].split('|')[2])])
                    # 处理meshes
                    needMeshes = []
                    for k in range(len(info)):
                        checkMesh = ''
                        if k == 0:
                            continue
                        if '|' not in info[k]:
                            if mc.objExists(ns + ':' + info[k]):
                                needMeshFull = mc.ls(( ns + ':' + info[k]),l = 1)[0]
                                checkMesh = needMeshFull
                        else:
                            # 全面启动长名
                            needMesh = info[k].replace('|',('|' + ns + ':'))
                            if not mc.ls('*' + needMesh):
                                continue
                            needMeshFull = mc.ls(('|*' + needMesh),l = 1)[0]
                            checkMesh = needMeshFull
                        if checkMesh:
                            if '.f[' in checkMesh:
                                faceNum = mc.polyEvaluate(checkMesh.split('.f[')[0], face=1)
                                if checkMesh == (checkMesh.split('.f[')[0] + '.f[0:' + str(faceNum - 1) + ']'):
                                    shape = mc.listRelatives(checkMesh.split('.f[')[0],s = 1,ni = 1, type = 'mesh',f = 1)[0]
                                    needMeshes.append(shape)
                                else:
                                    needMeshes.append(checkMesh)
                            else:
                                needMeshes.append(checkMesh)
                    needMeshes = mc.ls(needMeshes , l = 1)
                    shaderMeshes.append(needMeshes)
        result = [shaderColor,shaderMeshes]
        return result


    #----------------------------------------------------------------------------------------#
    # 【通用：数据读取函数】
    # Author : 沈  康
    # Data   : 2014_07_23/2014_07_23
    #-------------------------------------------------#
    
    #--------------------------------#
    # 读取excel信息
    def checkRLReadEXcle(self,shotType = 2):
        # 处理excel信息？
        # 读文件名，获取项目及镜头号
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()  

        projFullName = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(shotInfo[0])

        #serverPath = '//file-cluster/GDC/Projects/' + projFullName + '/' + projFullName +  '_scratch/TD/ExcelInfo/' + str(shotInfo[1]) + '/' 
        serverPath = '//file-cluster/GDC/Projects/' + projFullName + '/Reference/Product manager/Render/ExcelInfo/' + str(shotInfo[1]) + '/' 
        serverExcelPath = serverPath + shotInfo[0].upper() + str(shotInfo[1]) + '_TimeOfDay.xls'
        
        print('-----')
        print(serverExcelPath)
        
        import os
        if not os.path.exists(serverExcelPath):
            print(u'=======本集Excel文件不存在，请联系环节负责人处理=====')
            print(u'=======  目前只支持Excel 2000-2003的版本    =====')
            mc.error(u'=======本集Excel文件不存在，请联系环节负责人处理=====')

        import xlrd
        reload(xlrd)
        # shotAllData = xlrd.open_workbook(serverExcelPath).sheets()[0] 0是第一页表格
        shotAllData = xlrd.open_workbook(serverExcelPath).sheets()[0]  
        
        shotData = []
        
        # 定位行数
        # 先找场名
        rowMax = shotAllData.nrows
        rowID = []
        for i in range(rowMax):
            shotID = self.checkRLExcelInfoConfig(shotAllData.row_values(i)[0])
            # 场
            checkInfo = shotInfo[2]
            if shotID == checkInfo:
                rowID.append(i)
        
        if not rowID:
            print(u'=====本镜头信息不在指定表格内，请联系环节负责人处理=====')
            mc.error(u'=====本镜头信息不在指定表格内，请联系环节负责人处理=====')
        
        if shotType == 2:
            # 读行数，具体的是镜头号加多少，视表格内容定
            shotData = shotAllData.row_values(shotID)  
        
        if shotType == 3:
            # 找镜头号
            needID = 0
            for line in rowID:
                shotID = self.checkRLExcelInfoConfig(shotAllData.row_values(line)[1])
                # 镜头号
                checkInfo = shotInfo[3]
                if shotID == checkInfo:
                    needID = line
                    break
            
            if not needID:
                print(u'=====本镜头信息不在指定表格内，请联系环节负责人处理=====')
                mc.error(u'=====本镜头信息不在指定表格内，请联系环节负责人处理=====')
    
            # 读行数，具体的是镜头号加多少，视表格内容定
            shotData = shotAllData.row_values(needID)  
        
        return shotData

    #--------------------------------#
    # 处理表格信息
    def checkRLExcelInfoConfig(self,info):
        info = str(info)
        while info[-1] in [';',' ']:
            info = info[:-1]
        while '.' in info:
            info = info.split('.')[0]
        return info
    
    #--------------------------------#
    # 数据库版本
    def checkRLShotInfoData(self,project,shotInfo,shotType=3):
        import pyodbc
        #project = 'Ninjago'
        cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=192.168.168.16;DATABASE=idmtPlex_%s;UID=EWAUser;PWD=hk#$G#324f'%(project))
        cursor = cnxn.cursor()
        
        cmd_tk = 'exec idmtPlex_' + project + '.dbo.usp_TD0001 \'' + shotInfo[0] + '\',\'' + shotInfo[1]  + '\',\'' + shotInfo[2]  + '\''
        data = cursor.execute(cmd_tk).fetchone()
        
        return data
    #----------------------------------------------------------------------------------------#
    # 【通用：反选面处理函数】
    # 根据选面物体信息获取物体剩余面信息
    # 处理maya bug
    # Author : 沈  康
    # Data   : 2014_07_28/2014_08_01
    #-------------------------------------------------#
    # 根据选面物体信息获取物体剩余面信息
    def checkRLFaceObjReverse( self, checkMeshes):
        if not checkMeshes:
            return []
        meshesReverse = []
        # 核心算法：基于原理
        '''
        meshGrpInfos  = {}
        for mesh in checkMeshes:
            if '.f[' not in mesh:
                continue
            keys = meshGrpInfos.keys()
            if mesh.split('.f[')[0] not in keys:
                meshGrpInfos[mesh.split('.f[')[0]] = []
            meshGrpInfos[mesh.split('.f[')[0]].append(mesh)
        if meshGrpInfos:
            grpKeys = meshGrpInfos.keys()
            for grp in grpKeys:
                faceNum = mc.polyEvaluate(grp, face=1)
                usedNum = []
                # 记录物体
                for mesh in meshGrpInfos[grp]:
                    for i in range(faceNum):
                        if ':' in mesh.split('.f[')[-1]:
                            checkMin = int(mesh.split('.f[')[-1].split(':')[0])
                            checkMax = int(mesh.split('.f[')[-1].split(':')[-1].split(']')[0])
                            if (i >= checkMin and i <= checkMax):
                                if i not in usedNum:
                                    usedNum.append(i)
                        else:
                            if i == int(mesh.split('.f[')[-1].split(']')[0]):
                                if i not in usedNum:
                                    usedNum.append(i)
                # 处理反转数据
                for j in range(faceNum):
                    if j not in usedNum:
                        meshesReverse.append(grp + '.f[' + str(j) + ']')
        # 精简长度
        if meshesReverse:
            mc.select(meshesReverse)
            meshesReverse = mc.ls(sl = 1,l = 1)
        '''
        # 新算法：基于maya操作
        checkGrps = []
        for mesh in checkMeshes:
            if '.f[' in mesh:
                checkGrps.append(mesh.split('.f[')[0])
            else:
                if mc.nodeType(mesh) == 'transform':
                    grp = mesh
                else:
                    grp = mc.listRelatives(mesh,p=1,type = 'transform',f = 1)[0]
                checkGrps.append(grp)
        checkGrps = list(set(checkGrps))
        checkAllFaces = []
        for grp in checkGrps:
            faceNum = mc.polyEvaluate(grp, face=1)
            checkAllFaces.append(grp + '.f[0:' + str(faceNum-1) + ']')
        mc.select(checkMeshes)
        mc.select(checkAllFaces,tgl = 1)
        meshesReverse = mc.ls(sl = 1,l = 1)
        return meshesReverse

    #--------------------------------------------#
    # 镜头外物体处理
    def getObjsNotInCamera(self,targetCam):
        frameSart = mc.playbackOptions(min=1,q=1)
        frameEnd = mc.playbackOptions(max=1,q=1)
        #targetCam = 'CAM:cam_test4_001_002_baked'
        #---------------------#
        # persp处理
        perspCam = 'persp'
        langPerspCam = mc.ls(perspCam,l=1)[0]
        if '|%s|%s'%(targetCam,perspCam) not in langPerspCam:
            mc.parent(perspCam,targetCam)
        # camera视角 但后台不支持
        # mc.lookThru( refCame )
        # 属性
        attrList = ['.tx','.ty','.tz','.rx','.ry','.rz','.sx','.sy','.sz']
        attrList += ['.nearClipPlane','.farClipPlane','.overscan','.horizontalFilmAperture','.verticalFilmAperture','.focalLength']
        for attr in attrList:
            checkAttr = 'persp' + attr
            cons = mc.listConnections(checkAttr,s=1,d=0,plugs=1)
            if cons:
                mc.disconnectAttr(cons[0],checkAttr)
            if attr in ['.tx','.ty','.tz','.rx','.ry','.rz']:
                mc.setAttr(checkAttr,0)
            if attr in ['.sx','.sy','.sz']:
                mc.setAttr(checkAttr,1)
            if attr in ['.nearClipPlane','.farClipPlane','.overscan','.horizontalFilmAperture','.verticalFilmAperture']:
                mc.setAttr(checkAttr,mc.getAttr(targetCam+attr))
            if attr in ['.focalLength']:
                mc.connectAttr(targetCam+attr,checkAttr)
        #---------------------#
        # 检索
        inCamObjs = []
        import maya.OpenMaya as om
        import maya.OpenMayaUI as omUI
        view = omUI.M3dView.active3dView()
        for frameNum in range(int(frameSart),int(frameEnd+1)):
            mc.currentTime(frameNum)
            om.MGlobal.selectFromScreen( 0, 0, view.portWidth(), view.portHeight(), om.MGlobal.kReplaceList)
            objsNow = mc.ls(sl = 1,l=1)
            inCamObjs += objsNow
        if inCamObjs:
            inCamObjs = list(set(inCamObjs))
        #---------------------#
        # 排除
        meshes = mc.ls(type = 'mesh',l=1)
        meshGrps = mc.listRelatives(meshes,p=1,type = 'transform',f=1)
        if not meshGrps:
            meshGrps = []
        noNeedGrps = []
        for checkGrp in meshGrps:
            if checkGrp in inCamObjs:
                continue
            noNeedGrps.append(checkGrp)
        mc.select(cl=1)
        #---------------------#
        # 解锁哈
        mc.parent(perspCam,world = 1)
        #---------------------#
        # 显示层处理
        disLayer = 'outCamLayer'
        if mc.ls(disLayer,type = 'displayLayer'):
            mc.delete(disLayer)
        mc.createDisplayLayer(name = disLayer)
        if noNeedGrps:
            mc.editDisplayLayerMembers(disLayer,noNeedGrps,noRecurse = 1)
        return noNeedGrps

    #------------------------------#
    # shape节点更新
    def blendShapeUpdateInfo(self):
        # 回到masterLayer
        mc.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
        # 获取物体
        modelGrps = mc.ls('*:MODEL',l=1)
        needMeshes = mc.listRelatives(modelGrps,ad=1,s=1,type='mesh',f=1)
        if not needMeshes:
            return
        needGrps = mc.listRelatives(needMeshes,p=1,type='transform',f=1)
        needGrps = list(set(needGrps))
        rootGrps = ['CHR_GRP','PRP_GRP','SET_GRP']
        from idmt.maya.commonCore.core_mayaCommon import sk_backCmd
        reload(sk_backCmd)
        # 处理
        for checkGrp in needGrps:
            fixState = 0
            for checkKey in rootGrps:
                if checkKey in checkGrp:
                    fixState = 1
            if fixState:
                sk_backCmd.sk_backCmd().transAttrUpdate(checkGrp)

    #---------------------------#
    # masterLayer 素模 ,继承 置换、透明
    def masterLayerLambertShader(self,rebuild = 0,coNode = '',shaderType = 'lambert',vfxMode = 1,msLayer = 1,Adjustment = 0,justSGList = [],skipSGList = []):
        #'创建的基础材质球名称'
        if shaderType in ['ar']:
            shaderType = 'aiStandard'
        if not coNode:
            coNode = 'base_cleanShader'
        if mc.ls(coNode):
            if rebuild:
                mc.delete(coNode)
                coNode = mc.shadingNode(shaderType, asShader=True, name=coNode)
        else:
            coNode = mc.shadingNode(shaderType, asShader=True, name=coNode)
        if shaderType in ['lambert']:
            mc.setAttr(coNode+'.color',1,1,1,type='double3')
            mc.setAttr(coNode+'.diffuse',0)
            mc.setAttr(coNode+'.matteOpacityMode',0)
        if shaderType in ['surfaceShader']:
            mc.setAttr(coNode+'.outMatteOpacity',0,0,0,type='double3')
        if shaderType in ['aiStandard']:
            mc.setAttr(coNode+'.color',1,1,1,type='double3')
            mc.setAttr(coNode+'.Kd',1)
        # mesh
        meshes = mc.ls(type='mesh',l=1)
        needSgNodes = []
        for mesh in meshes:
            if '|Alembic_T_Grp|' in mesh:
                continue
            if mc.getAttr(mesh+'.intermediateObject'):
                continue
            if vfxMode and '|VFX_GRP|' in mesh:
                continue
            sgNodes = mc.listConnections(mesh,s=0,d=1,type = 'shadingEngine')
            if not sgNodes:
                continue
            for checkSG in sgNodes:
                if checkSG in ['initialShadingGroup']:
                    continue
                if checkSG not in needSgNodes:
                    needSgNodes.append(checkSG)
        # 回masterLayer处理
        if msLayer:
            mc.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
        print('------001')
        print(justSGList)
        print('------002')
        print(skipSGList)
        for sgNode in needSgNodes:
            if justSGList and sgNode not in justSGList:
                continue
            if skipSGList and sgNode in skipSGList:
                continue
            sgAttr = sgNode + '.surfaceShader'
            if not msLayer and Adjustment:
                mc.editRenderLayerAdjustment(sgAttr)
            cons = mc.listConnections(sgAttr,s=1,d=0,plugs=1)
            if cons:
                mc.disconnectAttr(cons[0],sgAttr)
            try:
                mc.connectAttr(coNode + '.outColor',sgAttr)
            except:
                print('------nodeConnectFailed')
                print(coNode)
                print(sgAttr)
                mc.error()

    #  data/lighting copy
    def lgtUpdateUI(self):
        uiName = 'sk_lightDataUpdateUI'
        if mc.window (uiName, ex=1):
            mc.deleteUI(uiName, window=True)
        bH = 22.5
        baseCmd = 'from idmt.maya.commonCore.core_renderLayer import sk_renderLayerCore;reload(sk_renderLayerCore);sk_renderLayerCore.sk_renderLayerCore()'
        mc.window(uiName, title="lightDataUpdate", widthHeight=(280, 170), menuBar=0)
        # 主界面
        mc.columnLayout(adjustableColumn=1, columnOffset=['both', 0])

        # 文件更新
        mc.frameLayout( 'sk_lightDataUpda_fileCope1',label=u'===文件更新[上排源]===', collapse = 0,
                        collapsable = 1,borderStyle='etchedIn', bgc = [0.1,0.1,0.1])
        rowNum = 3
        rowHigh = bH*rowNum + 2*(rowNum-1)
        mc.rowColumnLayout(numberOfRows=rowNum,height = rowHigh)
        # 查找文件
        mc.textFieldButtonGrp('sk_lightDataUpdate_SFile',text=u'请选取要复制文件', buttonLabel=u'选文件',bc = '%s.lgtUpdateSelectFile(0)'%baseCmd )
        # 目标目录
        mc.textFieldButtonGrp('sk_lightDataUpdate_TFolder',text=u'请选取目标路径', buttonLabel=u'选路径',bc = '%s.lgtUpdateSelectFile(0.5)'%baseCmd )
        # 执行上传
        mc.button('File Update',bgc = [0.1,0.1,0.1],h = 20,c = '%s.lgtUpdateButton(0)'%baseCmd )
        mc.setParent( '..' )

        mc.setParent( '..' )

        # 文件夹更新
        mc.frameLayout( 'sk_lightDataUpda_fileCope2',label=u'===文件夹更新[上排源]===', collapse = 0,
                        collapsable = 1,borderStyle='etchedIn', bgc = [0.1,0.1,0.1])
        rowNum = 3
        rowHigh = bH*rowNum + 2*(rowNum-1)
        mc.rowColumnLayout(numberOfRows=rowNum,height = rowHigh)
        # 查找文件
        mc.textFieldButtonGrp('sk_lightDataUpdate_SFile2',text=u'请选取要复制文件夹', buttonLabel=u'选文件',bc = '%s.lgtUpdateSelectFile(1)'%baseCmd )
        # 目标目录
        mc.textFieldButtonGrp('sk_lightDataUpdate_TFolder2',text=u'请选取目标路径', buttonLabel=u'选路径',bc = '%s.lgtUpdateSelectFile(1.5)'%baseCmd )
        # 执行上传
        mc.button('Folder Update',bgc = [0.6,0.6,0.6],h = 20,c = '%s.lgtUpdateButton(1)'%baseCmd )
        mc.setParent( '..' )

        mc.setParent( '..' )
        mc.showWindow(uiName)

    # 选取文件 0 文件, 1 文件夹
    def lgtUpdateSelectFile(self,mode = 0):
        if mode in [0]:
            fileName = mc.fileDialog2(fileMode = 1)
            if not fileName:
                return
            mc.textFieldButtonGrp('sk_lightDataUpdate_SFile',e=1,text = fileName[0])
        if mode in [0.5]:
            fileName = mc.fileDialog2(fileMode = 3)
            if not fileName:
                return
            mc.textFieldButtonGrp('sk_lightDataUpdate_TFolder',e=1,text = fileName[0])
        if mode in [1]:
            fileName = mc.fileDialog2(fileMode = 3)
            if not fileName:
                return
            mc.textFieldButtonGrp('sk_lightDataUpdate_SFile2',e=1,text = fileName[0])
        if mode in [1.5]:
            fileName = mc.fileDialog2(fileMode = 3)
            if not fileName:
                return
            mc.textFieldButtonGrp('sk_lightDataUpdate_TFolder2',e=1,text = fileName[0])

    # 执行update
    def lgtUpdateButton(self,mode = 0):
        import os
        if mode in [0]:
            sourceFile = mc.textFieldButtonGrp('sk_lightDataUpdate_SFile',q=1,text = 1)
        if mode in [1]:
            sourceFile = mc.textFieldButtonGrp('sk_lightDataUpdate_SFile2',q=1,text = 1)
        if not os.path.exists(sourceFile):
            print(u'---选取的文件不存在---')
            mc.error()
        if mode in [0]:
            targetPath = mc.textFieldButtonGrp('sk_lightDataUpdate_TFolder',q=1,text = 1)
        if mode in [1]:
            targetPath = mc.textFieldButtonGrp('sk_lightDataUpdate_TFolder2',q=1,text = 1)
        if not os.path.exists(targetPath):
            print(u'---选取的路径不存在---')
            mc.error()
        targetFile = '%s/%s'%(targetPath,sourceFile.split('/')[-1])
        from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
        reload(sk_infoConfig)
        if mode in [0]:
            sk_infoConfig.sk_infoConfig().checkServerFileSystem('copy',sourceFile,targetFile)
        if mode in [1]:
            sk_infoConfig.sk_infoConfig().checkServerFileSystem('xcopy',sourceFile,targetFile)
        print('\n--------sourceFile')
        print(sourceFile)
        print('--------targetPath')
        print(targetFile)
        print('--------Copy Done--------')

    # 相机参考namespace修正
    def camRefFix(self):
        refNodes = mc.ls(type = 'reference')
        for checkRef in refNodes:
            try:
                refPath = mc.referenceQuery(checkRef,filename = 1)
                refNs = mc.referenceQuery(checkRef,namespace = 1)
                if '_cam.' in refPath and refNs not in [':CAM']:
                    mc.file(refPath, e=1, ns='CAM')
            except:
                pass
