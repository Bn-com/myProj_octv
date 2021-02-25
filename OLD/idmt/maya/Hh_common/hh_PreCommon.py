# -*- coding: utf-8 -*-

import maya.cmds as mc
import maya.mel as mel
from idmt.maya.commonCore.core_renderLayer import sk_renderLayerCore
reload(sk_renderLayerCore)

class hh_CheckCommon(object):
    def __init__(self):
        pass
    #----------------------------------------------------------------------------------------------------------#      #----------------------------------------------------------#
    def hh_CheckUI(self):
    # 窗口
        if mc.window('hh_CheckTools', exists=True):
            mc.deleteUI('hh_CheckTools')
        mc.window('hh_CheckTools', title=u'文件检查及整理工具',
                  width=320, height=350, sizeable=True)
         # 面板
        form = mc.formLayout()
         # 切换面板
        tabs = mc.tabLayout('tabArnold',innerMarginWidth=5, innerMarginHeight=5)
        mc.formLayout(
            form, edit=True, attachForm=((tabs, 'top', 0), (tabs, 'left', 0), (tabs, 'bottom', 0), (tabs, 'right', 0)))
         # tab_渲染工具
        child1 = mc.columnLayout(adjustableColumn=True)
        mc.image(
            image='//file-cluster/GDC/Resource/Support/Maya/icons/HH/arnold.png')
        mc.button(label=u'创建Project', bgc=[0, 0, 0.0], height=50, command='mel.eval(\'zwSetProject\')')
        mc.button(label=u'另存文件', bgc=[0, 0, 0.0], height=50, command='mel.eval(\'source \"//file-cluster/GDC/Resource/Support/Maya/projects/ShunLiu/CSL_RenderToolsMR.mel\";CSL_HHSavefile();\')')
        mc.button(label=u'创建AOV', bgc=[0, 0, 0.0], height=50, command='mc.tabLayout("tabArnold", edit=True, selectTabIndex=2)')
        mc.button(label=u'提交网渲', bgc=[0, 0, 0.0], height=50, command='mel.eval(\'source \"//file-cluster/GDC/Resource/Support/Maya/2013/MusterCheckin.mel\";MusterCheckin();\')')
        mc.setParent('..')
         # AOV面板
        child2 = mc.columnLayout(adjustableColumn=True)
        mc.frameLayout(label='Select', bgc=[0, 0, 0.0], borderStyle='in', cll=1)
        mc.rowColumnLayout(numberOfColumns=3)
        collectionocc = mc.radioCollection()
        # occ
        occset = mc.checkBox('hhcheckocc', label='OCC', visible=1, v=1,
                             bgc=[0.13, 0.15, 0.25], height=30, width=130)
        mc.button(label=u'创建', bgc=[
                  0, 0, 0.0], width=110, height=30, command='from idmt.maya.Hh_common import hh_RenderArnoldLayer\nreload(hh_RenderArnoldLayer)\nhh_RenderArnoldLayer.hh_RenderArnold().ArnoldAOVAOCreate()')
        mc.button(
            label=u'删除', bgc=[0, 0, 0.0], width=110, height=30, command='from idmt.maya.Hh_common import hh_RenderArnoldLayer\nreload(hh_RenderArnoldLayer)\nhh_RenderArnoldLayer.hh_RenderArnold().ArnoldAOVAODelete()')
        collectionnormal = mc.radioCollection()
        # normal
        normalset = mc.checkBox('hhchecknormal',label='Normal', visible=1, v=1,
                             bgc=[0.13, 0.15, 0.25], height=30, width=130)
        mc.button(label=u'创建', bgc=[
                  0, 0, 0.0], width=110, height=30, command='from idmt.maya.Hh_common import hh_RenderArnoldLayer\nreload(hh_RenderArnoldLayer)\nhh_RenderArnoldLayer.hh_RenderArnold().ArnoldAOVNomalCreate()')
        mc.button(
            label=u'删除', bgc=[0, 0, 0.0], width=110, height=30, command='from idmt.maya.Hh_common import hh_RenderArnoldLayer\nreload(hh_RenderArnoldLayer)\nhh_RenderArnoldLayer.hh_RenderArnold().ArnoldAOVNMDelete()')
        collectionfre = mc.radioCollection()
        # fre
        freset = mc.checkBox('hhcheckfre',label='Fre', visible=1, v=1,
                             bgc=[0.13, 0.15, 0.25], height=30, width=130)
        mc.button(label=u'创建', bgc=[
                  0, 0, 0.0], width=110, height=30, command='from idmt.maya.Hh_common import hh_RenderArnoldLayer\nreload(hh_RenderArnoldLayer)\nhh_RenderArnoldLayer.hh_RenderArnold().ArnoldAOVFreCreate()')
        mc.button(
            label=u'删除', bgc=[0, 0, 0.0], width=110, height=30, command='from idmt.maya.Hh_common import hh_RenderArnoldLayer\nreload(hh_RenderArnoldLayer)\nhh_RenderArnoldLayer.hh_RenderArnold().ArnoldAOVFreDelete()')
        collectionkey = mc.radioCollection()
        # KeyLight
        keyset = mc.checkBox('hhcheckkey',label='KeyLight', visible=1,
                             v=1, bgc=[0.13, 0.15, 0.25], height=30, width=130)
        mc.button(label=u'创建', bgc=[
                  0, 0, 0.0], width=110, height=30, command='from idmt.maya.Hh_common import hh_RenderArnoldLayer\nreload(hh_RenderArnoldLayer)\nhh_RenderArnoldLayer.hh_RenderArnold().ArnoldAOVKeyLight()')
        mc.button(
            label=u'删除', bgc=[0, 0, 0.0], width=110, height=30, command='from idmt.maya.Hh_common import hh_RenderArnoldLayer\nreload(hh_RenderArnoldLayer)\nhh_RenderArnoldLayer.hh_RenderArnold().ArnoldAOVKeyDelete()')
        collectionzdp = mc.radioCollection()
        # Shadow
        shadowset = mc.checkBox('hhcheckshadow',label='Shadow', visible=1,
                             v=1, bgc=[0.13, 0.15, 0.25], height=30, width=130)
        mc.button(label=u'创建', bgc=[
                  0, 0, 0.0], width=110, height=30, command='from idmt.maya.Hh_common import hh_RenderArnoldLayer\nreload(hh_RenderArnoldLayer)\nhh_RenderArnoldLayer.hh_RenderArnold().ArnoldAOVShadowCreat()')
        mc.button(
            label=u'删除', bgc=[0, 0, 0.0], width=110, height=30, command='from idmt.maya.Hh_common import hh_RenderArnoldLayer\nreload(hh_RenderArnoldLayer)\nhh_RenderArnoldLayer.hh_RenderArnold().ArnoldAOVShadowDelete()')
        collectionzdp = mc.radioCollection()
        # zdepth
        zdepthset = mc.checkBox('hhcheckzdep',label='Zdepth', visible=1, v=1,
                             bgc=[0.13, 0.15, 0.25], height=30, width=130)
        mc.button(label=u'创建', bgc=[
                  0, 0, 0.0], width=110, height=30, command='from idmt.maya.Hh_common import hh_RenderArnoldLayer\nreload(hh_RenderArnoldLayer)\nhh_RenderArnoldLayer.hh_RenderArnold().ArnoldAOVZdepthCreat()')
        mc.button(
            label=u'删除', bgc=[0, 0, 0.0], width=110, height=30, command='from idmt.maya.Hh_common import hh_RenderArnoldLayer\nreload(hh_RenderArnoldLayer)\nhh_RenderArnoldLayer.hh_RenderArnold().ArnoldAOVZdepDelete()')
        collectionid01 = mc.radioCollection()
        # id01
        id01set = mc.checkBox('hhcheckid01',label='id01', visible=1, v=1,
                             bgc=[0.13, 0.15, 0.25], height=30, width=130)
        mc.button(label=u'创建', bgc=[
                  0, 0, 0.0], width=110, height=30, command='')
        mc.button(
            label=u'删除', bgc=[0, 0, 0.0], width=110, height=30, command='')
        mc.setParent('..')
        mc.setParent('..')
        # 一键式创建AOV层
        mc.frameLayout(label=u'一键式创建（删除）工具', bgc=[0, 0, 0.0], borderStyle='in')
        mc.rowColumnLayout(numberOfColumns=2)
        mc.button(label=u'创建渲染层', width=180, height=30,
                  bgc=[0.13, 0.15, 0.25], command='from idmt.maya.Hh_common import hh_RenderArnoldLayer\nreload(hh_RenderArnoldLayer)\nhh_RenderArnoldLayer.hh_RenderArnold().ArnoldRendererLayerCreat()')
        mc.button(label=u'删除所有AOV及渲染层', width=170,
                  height=30, bgc=[0, 0, 0.0], command='from idmt.maya.Hh_common import hh_RenderArnoldLayer\nreload(hh_RenderArnoldLayer)\nhh_RenderArnoldLayer.hh_RenderArnold().ArnoldAOVALLDelete()')
        mc.setParent('..')
        mc.setParent('..')
        mc.setParent('..')
        # 渲染常用工具组
        child3 = mc.rowColumnLayout(numberOfColumns=2)
        mc.button(label=u'创建', bgc=[
                  0, 0, 0.0], width=100, height=30, command='')
        mc.setParent('..')
        mc.tabLayout(tabs, edit=True, tabLabel=(
            (child1, u'前期文件检查'), (child2, '动画文件检查'), (child3, u'渲染文件检查')))
        mc.showWindow('hh_RenderArnold')
    
        #Arnold 设置（调自程序 sk_renderLayerCore),备用
        def ArnoldRendererSettings(self):
            print (u'===============!!!Start 【%s】!!!===============' % (u'Arnold设置'))
            print 'Working...'
            
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
            #添加Exr合并（HH添加)
            mc.setAttr ('defaultArnoldDriver.mergeAOVs', 1)  
    
            
            print (u'===============!!!Done  【%s】!!!===============' % (u'Arnold设置'))
            print '\n'
    #----------------------------------------------------------#
    #Arnold 设置（调自程序 sk_renderLayerCore),备用
    def ArnoldRendererSettings(self):
        print (u'===============!!!Start 【%s】!!!===============' % (u'Arnold设置'))
        print 'Working...'
        
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
        #添加Exr合并（HH添加)
        mc.setAttr ('defaultArnoldDriver.mergeAOVs', 1)  

        
        print (u'===============!!!Done  【%s】!!!===============' % (u'Arnold设置'))
        print '\n'
    #----------------------------------------------------------#
    def ArnoldAOVAOCreate(self):
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
        #AO pass creat
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
        #connect
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
         
		
		#nomal
    def ArnoldAOVNomalCreate(self):
		    #----------------------#
		    # shader
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
		    # nomal pass creat
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
				#connect
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
        # fresel
    def ArnoldAOVFreCreate(self):
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
        #Fre Pass Creat
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
        #connect   
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
    def ArnoldAOVKeyLight(self):
        keyLightShader = 'SHD_KeyLight_arnold'
        if mc.ls( keyLightShader ):
            mc.delete(keyLightShader)
        keyLightSG = 'SHD_KeyLight_arnold_SG'
        if mc.ls( keyLightSG ):
            mc.delete(keyLightSG)
        keyLightShader = mc.shadingNode ('aiStandard', asShader=True, name= keyLightShader)  
        keyLightSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=( keyLightSG ))
        mc.connectAttr(('%s.%s') % (keyLightShader , 'outColor') , ('%s.%s') % (keyLightSG , 'surfaceShader'), f=True)
        # keyLight Pass Creat
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
        # connect
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
    def ArnoldAOVShadowCreat(self):
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
        # shadow Pass Creat
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
        # connect
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
        #----------------------#
        # Z
    def ArnoldAOVZdepthCreat(self):
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
        #connect
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
    #渲染层创建
    def ArnoldRendererLayerCreat(self):
        from idmt.maya.Hh_common import hh_RenderArnoldLayer
        reload(hh_RenderArnoldLayer)
        hh_RenderArnoldLayer.hh_RenderArnold().ArnoldRendererSettings()
           	    	
      #创建渲染层 
        mel.eval('source "//file-cluster/GDC/Resource/Support/Maya/projects/ShunLiu/CSL_RenderToolsMR.mel";CSL_RenderTools_Arnold();')   	
    	#创建pass
        occpass=mc.checkBox('hhcheckocc',q=1,v=1)
        normalpass=mc.checkBox('hhchecknormal',q=1,v=1)
        frepass=mc.checkBox('hhcheckfre',q=1,v=1)
        keypass=mc.checkBox('hhcheckkey',q=1,v=1)
        shadowpass=mc.checkBox('hhcheckshadow',q=1,v=1)
        zdppass=mc.checkBox('hhcheckzdep',q=1,v=1)
        id01pass=mc.checkBox('hhcheckid01',q=1,v=1)
        #occ
        if occpass == True :
        	from idmt.maya.Hh_common import hh_RenderArnoldLayer
        	reload(hh_RenderArnoldLayer)
        	hh_RenderArnoldLayer.hh_RenderArnold().ArnoldAOVAOCreate()
        #normal
        if normalpass == True :
        	from idmt.maya.Hh_common import hh_RenderArnoldLayer
        	reload(hh_RenderArnoldLayer)
        	hh_RenderArnoldLayer.hh_RenderArnold().ArnoldAOVNomalCreate()
        #fre
        if frepass == True :
        	from idmt.maya.Hh_common import hh_RenderArnoldLayer
        	reload(hh_RenderArnoldLayer)
        	hh_RenderArnoldLayer.hh_RenderArnold().ArnoldAOVFreCreate()
        #keyl
        if keypass == True :
        	from idmt.maya.Hh_common import hh_RenderArnoldLayer
        	reload(hh_RenderArnoldLayer)
        	hh_RenderArnoldLayer.hh_RenderArnold().ArnoldAOVKeyLight()
        #shadow
        if shadowpass == True :
        	from idmt.maya.Hh_common import hh_RenderArnoldLayer
        	reload(hh_RenderArnoldLayer)
        	hh_RenderArnoldLayer.hh_RenderArnold().ArnoldAOVShadowCreat()
        #zdp
        if zdppass == True :
        	from idmt.maya.Hh_common import hh_RenderArnoldLayer
        	reload(hh_RenderArnoldLayer)
        	hh_RenderArnoldLayer.hh_RenderArnold().ArnoldAOVZdepthCreat()    
    #----------------------------------------------------------#
    def ArnoldAOVAODelete(self):
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
        #----------------------#
        #AO pass creat
        occArnoldPass = 'aiAOV_Occ'
        if mc.ls(occArnoldPass) :
            mc.delete(occArnoldPass)
    def ArnoldAOVAODelete(self):
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
        #----------------------#
        #AO pass creat
        occArnoldPass = 'aiAOV_Occ'
        if mc.ls(occArnoldPass) :
            mc.delete(occArnoldPass)
    def ArnoldAOVNMDelete(self):
        #----------------------#
        # shader
        #----------------------#
        # occ
        AOShader = 'SHD_NM_arnold'
        if mc.ls( AOShader ):
            mc.delete(AOShader)
        AOSG = 'SHD_NM_arnold_SG'
        if mc.ls( AOSG ):
            mc.delete( AOSG )
        #----------------------#
        #AO pass creat
        occArnoldPass = 'aiAOV_Normal'
        if mc.ls(occArnoldPass) :
            mc.delete(occArnoldPass)
    def ArnoldAOVFreDelete(self):
        #----------------------#
        # shader
        #----------------------#
        # Fre
        AOShader = 'SHD_Fresnel_arnold'
        if mc.ls( AOShader ):
            mc.delete(AOShader)
        AOSG = 'SHD_Fresnel_arnold_SG'
        if mc.ls( AOSG ):
            mc.delete( AOSG )
        #----------------------#
        occArnoldPass = 'aiAOV_Fresnel'
        if mc.ls(occArnoldPass) :
            mc.delete(occArnoldPass)
    def ArnoldAOVKeyDelete(self):
        # KeyLight
        AOShader = 'SHD_KeyLight_arnold'
        if mc.ls( AOShader ):
            mc.delete(AOShader)
        AOSG = 'SHD_KeyLight_arnold_SG'
        if mc.ls( AOSG ):
            mc.delete( AOSG )
        #----------------------#
        #AO pass creat
        occArnoldPass = 'aiAOV_KeyLight'
        if mc.ls(occArnoldPass) :
            mc.delete(occArnoldPass)
    def ArnoldAOVShadowDelete(self):
        #----------------------#
        # shader
        #----------------------#
        # occ
        AOShader = 'SHD_Shadow_arnold'
        if mc.ls( AOShader ):
            mc.delete(AOShader)
        AOSG = 'SHD_Shadow_arnold_SG'
        if mc.ls( AOSG ):
            mc.delete( AOSG )
        #----------------------#
        #AO pass creat
        occArnoldPass = 'aiAOV_Shadow'
        if mc.ls(occArnoldPass) :
            mc.delete(occArnoldPass)
    def ArnoldAOVZdepDelete(self):
        occArnoldPass = 'aiAOV_Z'
        if mc.ls(occArnoldPass) :
            mc.delete(occArnoldPass)
    def ArnoldAOVALLDelete(self):
        passType = mc.ls(type='aiAOV')
        if mc.ls(passType) :
            mc.delete(passType)