# -*- coding: utf-8 -*-
# 【通用】【viewport设置】
#  Author : 韩虹
#  Data   : 2015_09_09
#  
# import sys
# sys.path.append('D:\\food\pyp\common')






import maya.cmds as mc
import maya.mel as mel
import os
import re
from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
reload(sk_infoConfig)
from idmt.maya.commonCore.core_finalLayout import sk_cacheFinalLayout
reload(sk_cacheFinalLayout)
from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools
reload(sk_sceneTools)
from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
reload(sk_referenceConfig)
import idmt
class gdc_viewport(object):
    def __init__(self):
        pass
        
    #----------------------------------------------------------------------------------------------#
    

    #----------------------------------------------------------------------------------------------#
#---------------------------------------------------
#切换viewport ，并设置相应参数 
#  Author : 韩虹
#  Data   : 2015_09_09
#-----------------------
#---
    def gdc_viewportset(self):
        mc.ActivateViewport20() 
        mel.eval('buildRendererMenu MayaWindow|formLayout1|viewPanes|modelPanel4|menu31 modelPanel4')                
        mc.ActivateViewport20() 
        mc.ActivateViewport20() 
        mc.setAttr('hardwareRenderingGlobals.consolidateWorld',1)        
        mc.setAttr('hardwareRenderingGlobals.maxHardwareLights',4)        
        mc.setAttr('hardwareRenderingGlobals.transparencyAlgorithm',0)       
        mc.setAttr('hardwareRenderingGlobals.enableTextureMaxRes',1)        
        mc.setAttr('hardwareRenderingGlobals.textureMaxResolution',1024)        
        #mel.eval('AEReloadAllTextures')
        #mel.eval('generateAllUvTilePreviews')
        mel.eval('ogs -rebakeTextures')        
        mc.setAttr('hardwareRenderingGlobals.ssaoEnable',1)        
        mc.setAttr('hardwareRenderingGlobals.ssaoAmount',1.6)
#---------------------------------------------------
#viewport 显示,dis=0,显示OCC，dis=1,显示材质及灯光
#  Author : 韩虹
#  Data   : 2015_09_09
#-----------------------
    def gdc_viewportDis(self,dis=0):
        #from idmt.maya.commonCore.core_mayaCommon import sk_smoothSet
        #reload(sk_smoothSet)
        #shotInfo=sk_infoConfig.sk_infoConfig().checkShotInfo()
        '''
        if shotInfo[0] in ['tf']:
            sk_smoothSet.sk_smoothSet().smoothSetDoSmooth(1)
        '''
        self.gdc_viewportset()
        mel.eval('updateShowMenu MayaWindow|formLayout1|viewPanes|modelPanel4|menu30 modelPanel4 "modelPanel4" "Playblast Display"')
        mel.eval('modelEditor -e -allObjects 0 modelPanel4')
        mel.eval('modelEditor -e -polymeshes 1 modelPanel4')
        mel.eval('modelEditor -e -nurbsSurfaces true modelPanel4')
        if dis==1:
            #隐藏所有灯光
            light=mc.ls(lt=1,l=1)            
            for lig in light:
                li=mc.listRelatives(lig,p=1,f=1)
                if li:
                    mc.setAttr((li[0]+'.v'),0) 
            #创建环境灯            
            litname='vip_amb'
            if mc.objExists(litname):
                mc.delete(litname)                
            amb=mc.shadingNode('ambientLight', asShader=True)
            mc.connectAttr((amb+'.instObjGroups'),'defaultLightSet.dagSetMembers',nextAvailable=1)
            mc.setAttr((amb+'.intensity'),1.5)
            mc.setAttr((amb+'.color'),1,0.772381,0.462)    
            lit=mc.listRelatives(amb,p=1,f=1)
            if lit:
                mc.rename(lit[0],litname)
            #灯光显示                       
            mc.DisplayLight()
            
        if dis==0:
            #赋Lambert材质
            for i in range(1):
                state=mc.layoutDialog(ui=self.vicheckbox)
                if state is None:
                    state = mc.layoutDialog(ui=self.vicheckbox)
                if state == 'Abort':
                    break
                elif state == 'Continue':
                    pass
                objs=mc.ls(type='transform',l=1)
                meshs=[]
                if objs:
                    for obj in objs:
                        mesh=mc.listRelatives(obj,s=1,f=1)
                        if mesh and mc.nodeType(mesh[0])=='mesh':
                            meshs.append(obj)
                shade='vip_lambert'
                SG=shade+'SG'
                if mc.ls(shade):
                    mc.delete(shade)
                if mc.ls(SG):
                    mc.delete(SG)  
                mc.shadingNode('lambert', asShader=True,n=shade)
                mc.sets(renderable=1,noSurfaceShader=1,em=1,n=SG)
                try:
                    mc.connectAttr(('%s.outColor' % shade),('%s.surfaceShader' % SG))
                except:
                    pass 
                mc.setAttr((shade+'.ambientColor'),1,1,1)
                mc.select(meshs)
                mc.sets(meshs,e=1,forceElement=SG)
                #shade显示
                mc.DisplayShaded()
        mc.select(cl=1)
        return 0 
    
#    def gdc_viewportOcc(self):    
    def vicheckbox(self):
        # Get the dialog's formLayout.
        #
        form = mc.setParent(q=True)
        # layoutDialog's are not resizable, so hard code a size here,
        # to make sure all UI elements are visible.
        #
        mc.formLayout(form, e=True, width=300)
        t = mc.text(l=u'会赋OCC材质，请确认是否继续，完成后，请不要覆盖maya文件')
        b1 = mc.button(l='Abort', c='mc.layoutDialog( dismiss="Abort" )' )
#        b2 = mc.button(l='Skip', c='mc.layoutDialog( dismiss="Skip" )' )
        b2 = mc.button(l='Continue', c='mc.layoutDialog( dismiss="Continue" )' )
#        cb1 = mc.checkBox(label='Remember my choice')
        spacer = 15
        top = 15
        edge1 = 5
        edge=50
        mc.formLayout(form, edit=True,
                                        attachForm=[(t, 'top', top), (t, 'left', edge1), (t, 'right', edge), (b1, 'left', edge)],
                                        attachNone=[(t, 'bottom'), (b1, 'bottom'), (b2, 'bottom')],
                                        attachControl=[(b1, 'top', spacer, t), (b2, 'top', spacer, t)],
                                        attachPosition=[(b1, 'right', spacer, 33), (b2, 'left', spacer, 33), (b2, 'right', spacer, 66)])               

        
        
        

                                                                                                                                                                                                                                                 