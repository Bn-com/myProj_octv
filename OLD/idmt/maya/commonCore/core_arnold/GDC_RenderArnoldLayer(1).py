# -*- coding: utf-8 -*-
# 【通用】【核心】【Arnold 渲染工具】
#  Author : 韩虹
#  Data   : 2014_08
# import sys
# sys.path.append('D:\\food\pyp\common')

import maya.cmds as mc
import maya.mel as mel

from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
reload(sk_referenceConfig)

from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
reload(sk_infoConfig)

import re
class GDC_RenderArnold(object):
    def __init__(self):
        pass
    #----------------------------------------------------------------------------------------------------------#      #----------------------------------------------------------#
    def RenderArnoldUI(self):
    # 窗口
        if mc.window('GDC_RenderArnold', exists=True):
            mc.deleteUI('GDC_RenderArnold')
        mc.window('GDC_RenderArnold', title=u'Arnold 渲染面板',
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
        mc.button(label=u'广告位招租', bgc=[0.13, 0.15, 0.25], height=120, command='')        
        mc.setParent('..')
         # AOV面板
        child2 = mc.columnLayout(adjustableColumn=True)
        mc.frameLayout(label='Select', bgc=[0, 0, 0.0], borderStyle='in', cll=1,cl=1)
        mc.rowColumnLayout(numberOfColumns=3)
        collectionocc = mc.radioCollection()
        # occ
        occset = mc.checkBox('hhcheckocc', label='OCC', visible=1, v=1,
                             bgc=[0.13, 0.15, 0.25], height=30, width=130)
        mc.button(label=u'创建', bgc=[
                  0, 0, 0.0], width=110, height=30, command='from idmt.maya.GDC_common import GDC_RenderArnoldLayer\nreload(GDC_RenderArnoldLayer)\nGDC_RenderArnoldLayer.GDC_RenderArnold().ArnoldAOVCreat(AOVtype="AO")')
        mc.button(
            label=u'删除', bgc=[0, 0, 0.0], width=110, height=30, command='from idmt.maya.GDC_common import GDC_RenderArnoldLayer\nreload(GDC_RenderArnoldLayer)\nGDC_RenderArnoldLayer.GDC_RenderArnold().ArnoldAOVAODelete()')
        collectionnormal = mc.radioCollection()
        # normal
        normalset = mc.checkBox('hhchecknormal',label='Normal', visible=1, v=1,
                             bgc=[0.13, 0.15, 0.25], height=30, width=130)
        mc.button(label=u'创建', bgc=[
                  0, 0, 0.0], width=110, height=30, command='from idmt.maya.GDC_common import GDC_RenderArnoldLayer\nreload(GDC_RenderArnoldLayer)\nGDC_RenderArnoldLayer.GDC_RenderArnold().ArnoldAOVCreat(AOVtype="Normal")')
        mc.button(
            label=u'删除', bgc=[0, 0, 0.0], width=110, height=30, command='from idmt.maya.GDC_common import GDC_RenderArnoldLayer\nreload(GDC_RenderArnoldLayer)\nGDC_RenderArnoldLayer.GDC_RenderArnold().ArnoldAOVDelete(AOVtype="Normal")')
        collectionfre = mc.radioCollection()
        # fre
        freset = mc.checkBox('hhcheckfre',label='Fre', visible=1, v=1,
                             bgc=[0.13, 0.15, 0.25], height=30, width=130)
        mc.button(label=u'创建', bgc=[
                  0, 0, 0.0], width=110, height=30, command='from idmt.maya.GDC_common import GDC_RenderArnoldLayer\nreload(GDC_RenderArnoldLayer)\nGDC_RenderArnoldLayer.GDC_RenderArnold().ArnoldAOVCreat(AOVtype="Fre")')
        mc.button(
            label=u'删除', bgc=[0, 0, 0.0], width=110, height=30, command='from idmt.maya.GDC_common import GDC_RenderArnoldLayer\nreload(GDC_RenderArnoldLayer)\nGDC_RenderArnoldLayer.GDC_RenderArnold().ArnoldAOVDelete(AOVtype="Fre")')
        collectionkey = mc.radioCollection()
        # KeyLight
#        keyset = mc.checkBox('hhcheckkey',label='KeyLight', visible=1,
#                             v=1, bgc=[0.13, 0.15, 0.25], height=30, width=130)
#        mc.button(label=u'创建', bgc=[
#                  0, 0, 0.0], width=110, height=30, command='from idmt.maya.GDC_common import GDC_RenderArnoldLayer\nreload(GDC_RenderArnoldLayer)\nGDC_RenderArnoldLayer.GDC_RenderArnold().ArnoldAOVKeyLight()')
#        mc.button(
#            label=u'删除', bgc=[0, 0, 0.0], width=110, height=30, command='from idmt.maya.GDC_common import GDC_RenderArnoldLayer\nreload(GDC_RenderArnoldLayer)\nGDC_RenderArnoldLayer.GDC_RenderArnold().ArnoldAOVKeyDelete()')
#        collectionzdp = mc.radioCollection()
        #SSS
        SSSset = mc.checkBox('hhcheckSSS',label='SSS', visible=1,
                             v=1, bgc=[0.13, 0.15, 0.25], height=30, width=130)
        mc.button(label=u'创建', bgc=[
                  0, 0, 0.0], width=110, height=30, command='from idmt.maya.GDC_common import GDC_RenderArnoldLayer\nreload(GDC_RenderArnoldLayer)\nGDC_RenderArnoldLayer.GDC_RenderArnold().ArnoldAOVCreat(AOVtype="sss")')
        mc.button(
            label=u'删除', bgc=[0, 0, 0.0], width=110, height=30, command='from idmt.maya.GDC_common import GDC_RenderArnoldLayer\nreload(GDC_RenderArnoldLayer)\nGDC_RenderArnoldLayer.GDC_RenderArnold().ArnoldAOVZdepDelete(AOVtype="sss")')
                
        collectionzdp = mc.radioCollection()        
        # Shadow
        shadowset = mc.checkBox('hhcheckshadow',label='Shadow', visible=1,
                             v=0, bgc=[0.13, 0.15, 0.25], height=30, width=130)
        mc.button(label=u'创建', bgc=[
                  0, 0, 0.0], width=110, height=30, command='from idmt.maya.GDC_common import GDC_RenderArnoldLayer\nreload(GDC_RenderArnoldLayer)\nGDC_RenderArnoldLayer.GDC_RenderArnold().ArnoldAOVCreat(AOVtype="Shadow")')
        mc.button(
            label=u'删除', bgc=[0, 0, 0.0], width=110, height=30, command='from idmt.maya.GDC_common import GDC_RenderArnoldLayer\nreload(GDC_RenderArnoldLayer)\nGDC_RenderArnoldLayer.GDC_RenderArnold().ArnoldAOVDelete(AOVtype="Shadow")')
        collectionzdp = mc.radioCollection()
        # zdepth
        zdepthset = mc.checkBox('hhcheckzdep',label='Zdepth', visible=1, v=0,
                             bgc=[0.13, 0.15, 0.25], height=30, width=130)
        mc.button(label=u'创建', bgc=[
                  0, 0, 0.0], width=110, height=30, command='from idmt.maya.GDC_common import GDC_RenderArnoldLayer\nreload(GDC_RenderArnoldLayer)\nGDC_RenderArnoldLayer.GDC_RenderArnold().ArnoldAOVCreat(AOVtype="Zdp")')
        mc.button(
            label=u'删除', bgc=[0, 0, 0.0], width=110, height=30, command='from idmt.maya.GDC_common import GDC_RenderArnoldLayer\nreload(GDC_RenderArnoldLayer)\nGDC_RenderArnoldLayer.GDC_RenderArnold().ArnoldAOVDelete(AOVtype="Zdp")')
        # motionvector
        zdepthset = mc.checkBox('hhcheckmov',label='motionvector', visible=1, v=0,
                             bgc=[0.13, 0.15, 0.25], height=30, width=130)
        mc.button(label=u'创建', bgc=[
                  0, 0, 0.0], width=110, height=30, command='from idmt.maya.GDC_common import GDC_RenderArnoldLayer\nreload(GDC_RenderArnoldLayer)\nGDC_RenderArnoldLayer.GDC_RenderArnold().ArnoldAOVCreat(AOVtype="motionvector")')
        mc.button(
            label=u'删除', bgc=[0, 0, 0.0], width=110, height=30, command='from idmt.maya.GDC_common import GDC_RenderArnoldLayer\nreload(GDC_RenderArnoldLayer)\nGDC_RenderArnoldLayer.GDC_RenderArnold().ArnoldAOVZdepDelete(AOVtype="motionvector")')

        collectionid01 = mc.radioCollection()
        mc.setParent('..')
        mc.setParent('..')  
        # 一键式创建AOV层
        mc.frameLayout(label=u'一键式创建（删除）工具', bgc=[0, 0, 0.0], borderStyle='in',cll=1,cl=1)
        mc.rowColumnLayout(numberOfColumns=3)
        mc.button(label=u'创建渲染层', width=130, height=30,
                  bgc=[0.13, 0.15, 0.25], command='from idmt.maya.GDC_common import GDC_RenderArnoldLayer\nreload(GDC_RenderArnoldLayer)\nGDC_RenderArnoldLayer.GDC_RenderArnold().ArnoldRendererLayerCreat()')
        mc.button(label=u'删除所有AOV', width=110,
                  height=30, bgc=[0, 0, 0.0], command='from idmt.maya.GDC_common import GDC_RenderArnoldLayer\nreload(GDC_RenderArnoldLayer)\nGDC_RenderArnoldLayer.GDC_RenderArnold().ArnoldALLDelete(nodetype="aiAOV")')
        mc.button(label=u'删除所有渲染层', width=110,
                  height=30, bgc=[0, 0, 0.0], command='from idmt.maya.GDC_common import GDC_RenderArnoldLayer\nreload(GDC_RenderArnoldLayer)\nGDC_RenderArnoldLayer.GDC_RenderArnold().ArnoldALLDelete(nodetype="renderLayer")')                  
        mc.setParent('..')
        mc.setParent('..')        
        mc.frameLayout(label=u'IDP创建工具', bgc=[0, 0, 0.0], borderStyle='in',cll=1,cl=1)
        mc.rowColumnLayout(numberOfColumns=2)
        mc.button(label=u'角色ID创建（PS:需要在参考状态）', width=180, height=30,
                  bgc=[0.13, 0.15, 0.25], command='from idmt.maya.GDC_common import GDC_RenderArnoldLayer\nreload(GDC_RenderArnoldLayer)\nGDC_RenderArnoldLayer.GDC_RenderArnold().ArnoldRendererSettings("03")\nGDC_RenderArnoldLayer.GDC_RenderArnold().csl_IDRenderLayerCreatAll(type="chr",ref=1)') 
        mc.button(label=u'场景ID创建（PS:需要在参考状态）', width=180, height=30,
                  bgc=[0, 0, 0.0], command='from idmt.maya.GDC_common import GDC_RenderArnoldLayer\nreload(GDC_RenderArnoldLayer)\nGDC_RenderArnoldLayer.GDC_RenderArnold().ArnoldRendererSettings("03")\nGDC_RenderArnoldLayer.GDC_RenderArnold().csl_IDRenderLayerCreatAll(type="set",ref=0)')                             
                                  
        mc.setParent('..')
        mc.setParent('..')
        mc.frameLayout(label=u'分层工具', bgc=[0, 0, 0.0], borderStyle='in',cll=1,cl=1)
        mc.rowColumnLayout(numberOfColumns=2)
        mc.button(label=u'Arnold渲染设置', width=180, height=30,
                  bgc=[0.13, 0.6, 0.25], command='from idmt.maya.GDC_common import GDC_RenderArnoldLayer\nreload(GDC_RenderArnoldLayer)\nGDC_RenderArnoldLayer.GDC_RenderArnold().ArnoldRendererSettings("03")')         
        mc.button(label=u'color', width=180, height=30,
                  bgc=[0, 0, 0.0], command='from idmt.maya.GDC_common import GDC_RenderArnoldLayer\nreload(GDC_RenderArnoldLayer)\nGDC_RenderArnoldLayer.GDC_RenderArnold().csl_ArnoldRenderLayerCreat(layername="color")')  
        mc.button(label=u'motionblur', width=180, height=30,
                  bgc=[0.13, 0.15, 0.25], command='from idmt.maya.GDC_common import GDC_RenderArnoldLayer\nreload(GDC_RenderArnoldLayer)\nGDC_RenderArnoldLayer.GDC_RenderArnold().csl_ArnoldRenderLayerCreat(layername="motionblur")') 
        mc.button(label=u'id', width=180, height=30,
                  bgc=[0, 0, 0.0], command='from idmt.maya.GDC_common import GDC_RenderArnoldLayer\nreload(GDC_RenderArnoldLayer)\nGDC_RenderArnoldLayer.GDC_RenderArnold().csl_ArnoldRenderLayerCreat(layername="id")')                     
        mc.setParent('..')
        mc.setParent('..')
        mc.frameLayout(label=u'常用工具', bgc=[0, 0, 0.0], borderStyle='in',cll=1,cl=1)
        mc.rowColumnLayout(numberOfColumns=2)
        mc.button(label=u'smooth', width=180, height=30,
                  bgc=[0, 0, 0.0], command='from idmt.maya.GDC_common import GDC_RenderArnoldLayer\nreload(GDC_RenderArnoldLayer)\nGDC_RenderArnoldLayer.GDC_RenderArnold().csl_SmoothSet()')             
        mc.button(label=u'检测前期是否上传贴图信息', width=180, height=30,
                  bgc=[0.13, 0.6, 0.25], command='from idmt.maya.ShunLiu_common import csl_checkin\nreload(csl_checkin)\ncsl_checkin.csl_checkin().csl_ImageRecordCheck(type="quarter",server=1)\ncsl_checkin.csl_checkin().csl_ImageRecordCheck(type="half",server=1)\ncsl_checkin.csl_checkin().csl_ImageRecordCheck(type="full",server=1)')         
        mc.button(label=u'全尺寸贴图', width=180, height=30,
                  bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_checkin\nreload(csl_checkin)\ncsl_checkin.csl_checkin().csl_ImageSizeRead(Type="full")')         
        mc.button(label=u'半尺寸贴图（1/4)', width=180, height=30,
                  bgc=[0.13, 0.15, 0.25], command='from idmt.maya.ShunLiu_common import csl_checkin\nreload(csl_checkin)\ncsl_checkin.csl_checkin().csl_ImageSizeRead(Type="half")')  
        mc.button(label=u'1/4尺寸贴图（1/16)', width=180, height=30,
                  bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_checkin\nreload(csl_checkin)\ncsl_checkin.csl_checkin().csl_ImageSizeRead(Type="quarter")') 
        mc.button(label=u'ms_anim转tx', width=180, height=30,
                  bgc=[0.13, 0.6, 0.25], command='from idmt.maya.ShunLiu_common import csl_checkin\nreload(csl_checkin)\ncsl_checkin.csl_checkin().tr()')                     
##        mc.button(label=u'贴图尺寸转换并上传贴图信息', width=180, height=30,
##                  bgc=[0.6, 0.15, 0.25], command='from idmt.maya.ShunLiu_common import csl_checkin\nreload(csl_checkin)\ncsl_checkin.csl_checkin().csl_ImageSizeCover(type="quarter",server=1)\ncsl_checkin.csl_checkin().csl_ImageSizeCover(type="half",server=1)')                                     
        mc.setParent('..')
        mc.setParent('..')        
        mc.setParent('..')                
        # 渲染常用工具组
        child3 = mc.columnLayout(adjustableColumn=True)
        mc.frameLayout(label=u'IDP输出工具', bgc=[0, 0, 0.0], borderStyle='etchedIn', cll=1,cl=1)
        mc.rowColumnLayout(numberOfColumns=4)
        mc.button(label=u'输出角色id01',width=90,height=30,bgc=[0.13, 0.15, 0.25],command='from idmt.maya.GDC_common import GDC_RenderArnoldLayer\nreload(GDC_RenderArnoldLayer)\nGDC_RenderArnoldLayer.GDC_RenderArnold().csl_RGBInfoExport(id=\'id01\')')
        mc.button(label=u'输出角色id02',width=90,height=30,bgc=[0.13, 0.15, 0.25],command='from idmt.maya.GDC_common import GDC_RenderArnoldLayer\nreload(GDC_RenderArnoldLayer)\nGDC_RenderArnoldLayer.GDC_RenderArnold().csl_RGBInfoExport(id=\'id02\')')
        mc.button(label=u'输出角色id03',width=90,height=30,bgc=[0.13, 0.15, 0.25],command='from idmt.maya.GDC_common import GDC_RenderArnoldLayer\nreload(GDC_RenderArnoldLayer)\nGDC_RenderArnoldLayer.GDC_RenderArnold().csl_RGBInfoExport(id=\'id03\')') 
        mc.button(label=u'输出角色id04',width=90,height=30,bgc=[0.13, 0.15, 0.25],command='from idmt.maya.GDC_common import GDC_RenderArnoldLayer\nreload(GDC_RenderArnoldLayer)\nGDC_RenderArnoldLayer.GDC_RenderArnold().csl_RGBInfoExport(id=\'id04\')')                 
        mc.button(label=u'输出场景id11',width=90,height=30,bgc=[0.0, 0.0, 0.0],command='from idmt.maya.GDC_common import GDC_RenderArnoldLayer\nreload(GDC_RenderArnoldLayer)\nGDC_RenderArnoldLayer.GDC_RenderArnold().csl_RGBInfoExport(id=\'id11\')')
        mc.button(label=u'输出场景id12',width=90,height=30,bgc=[0.0, 0.0, 0.0],command='from idmt.maya.GDC_common import GDC_RenderArnoldLayer\nreload(GDC_RenderArnoldLayer)\nGDC_RenderArnoldLayer.GDC_RenderArnold().csl_RGBInfoExport(id=\'id12\')')
        mc.button(label=u'输出场景id13',width=90,height=30,bgc=[0.0, 0.0, 0.0],command='from idmt.maya.GDC_common import GDC_RenderArnoldLayer\nreload(GDC_RenderArnoldLayer)\nGDC_RenderArnoldLayer.GDC_RenderArnold().csl_RGBInfoExport(id=\'id13\')')        
        mc.button(label=u'输出场景id14',width=90,height=30,bgc=[0.0, 0.0, 0.0],command='from idmt.maya.GDC_common import GDC_RenderArnoldLayer\nreload(GDC_RenderArnoldLayer)\nGDC_RenderArnoldLayer.GDC_RenderArnold().csl_RGBInfoExport(id=\'id14\')')         
        mc.button(label=u'ID材质输出前检测',width=90,height=30,bgc=[0.1, 0.6, 0.25],command='from idmt.maya.GDC_common import GDC_RenderArnoldLayer\nreload(GDC_RenderArnoldLayer)\nGDC_RenderArnoldLayer.GDC_RenderArnold().csl_RGBInfoExportTest()')
        mc.setParent('..')
        mc.setParent('..')        
        #idp材质工具    
        mc.frameLayout(label=u'IDP材质工具', bgc=[0, 0, 0.0], borderStyle='in', cll=1,cl=1)
        mc.rowColumnLayout(numberOfColumns=4) 
        mc.button(label=u'R',width=90,height=30,bgc=[1,0,0],command='from idmt.maya.GDC_common import GDC_RenderArnoldLayer\nreload(GDC_RenderArnoldLayer)\nGDC_RenderArnoldLayer.GDC_RenderArnold().ArnoldRendererSettings("03")\nGDC_RenderArnoldLayer.GDC_RenderArnold().ArnoldIDCreat(idpShader="ArnoldIdpR")')
        mc.button(label=u'G',width=90,height=30,bgc=[0,1,0],command='from idmt.maya.GDC_common import GDC_RenderArnoldLayer\nreload(GDC_RenderArnoldLayer)\nGDC_RenderArnoldLayer.GDC_RenderArnold().ArnoldRendererSettings("03")\nGDC_RenderArnoldLayer.GDC_RenderArnold().ArnoldIDCreat(idpShader="ArnoldIdpG")')
        mc.button(label=u'B',width=90,height=30,bgc=[0,0,1],command='from idmt.maya.GDC_common import GDC_RenderArnoldLayer\nreload(GDC_RenderArnoldLayer)\nGDC_RenderArnoldLayer.GDC_RenderArnold().ArnoldRendererSettings("03")\nGDC_RenderArnoldLayer.GDC_RenderArnold().ArnoldIDCreat(idpShader="ArnoldIdpB")')
        mc.button(label=u'M',width=90,height=30,bgc=[0,0,0],command='from idmt.maya.GDC_common import GDC_RenderArnoldLayer\nreload(GDC_RenderArnoldLayer)\nGDC_RenderArnoldLayer.GDC_RenderArnold().ArnoldRendererSettings("03")\nGDC_RenderArnoldLayer.GDC_RenderArnold().ArnoldIDCreat(idpShader="ArnoldIdpM")')
        mc.button(label=u'Y',width=90,height=30,bgc=[1,1,0],command='from idmt.maya.GDC_common import GDC_RenderArnoldLayer\nreload(GDC_RenderArnoldLayer)\nGDC_RenderArnoldLayer.GDC_RenderArnold().ArnoldRendererSettings("03")\nGDC_RenderArnoldLayer.GDC_RenderArnold().ArnoldIDCreat(idpShader="ArnoldIdpY")') 
        mc.button(label=u'C',width=90,height=30,bgc=[0,1,1],command='from idmt.maya.GDC_common import GDC_RenderArnoldLayer\nreload(GDC_RenderArnoldLayer)\nGDC_RenderArnoldLayer.GDC_RenderArnold().ArnoldRendererSettings("03")\nGDC_RenderArnoldLayer.GDC_RenderArnold().ArnoldIDCreat(idpShader="ArnoldIdpC")') 
        mc.button(label=u'K',width=90,height=30,bgc=[1,0,1],command='from idmt.maya.GDC_common import GDC_RenderArnoldLayer\nreload(GDC_RenderArnoldLayer)\nGDC_RenderArnoldLayer.GDC_RenderArnold().ArnoldRendererSettings("03")\nGDC_RenderArnoldLayer.GDC_RenderArnold().ArnoldIDCreat(idpShader="ArnoldIdpK")')                 
        mc.setParent('..')
        mc.setParent('..')        
        
        #置换专用材质工具
        mc.frameLayout(label=u'置换专用材质工具', bgc=[0, 0, 0.0], borderStyle='in', cll=1,cl=1)
        mc.rowColumnLayout(numberOfColumns=4) 
        mc.button(label=u'R',width=90,height=30,bgc=[1,0,0],command='from idmt.maya.GDC_common import GDC_RenderArnoldLayer\nreload(GDC_RenderArnoldLayer)\nGDC_RenderArnoldLayer.GDC_RenderArnold().P5_ArnoldDisMatCreat(idpShader="ArnoldIdpR01")')
        mc.button(label=u'G',width=90,height=30,bgc=[0,1,0],command='from idmt.maya.GDC_common import GDC_RenderArnoldLayer\nreload(GDC_RenderArnoldLayer)\nGDC_RenderArnoldLayer.GDC_RenderArnold().P5_ArnoldDisMatCreat(idpShader="ArnoldIdpG")')
        mc.button(label=u'B',width=90,height=30,bgc=[0,0,1],command='from idmt.maya.GDC_common import GDC_RenderArnoldLayer\nreload(GDC_RenderArnoldLayer)\nGDC_RenderArnoldLayer.GDC_RenderArnold().P5_ArnoldDisMatCreat(idpShader="ArnoldIdpB")')
        mc.button(label=u'M',width=90,height=30,bgc=[0,0,0],command='from idmt.maya.GDC_common import GDC_RenderArnoldLayer\nreload(GDC_RenderArnoldLayer)\nGDC_RenderArnoldLayer.GDC_RenderArnold().P5_ArnoldDisMatCreat(idpShader="ArnoldIdpM")')   
        mc.button(label=u'Y',width=90,height=30,bgc=[1,1,0],command='from idmt.maya.GDC_common import GDC_RenderArnoldLayer\nreload(GDC_RenderArnoldLayer)\nGDC_RenderArnoldLayer.GDC_RenderArnold().P5_ArnoldDisMatCreat(idpShader="ArnoldIdpY")') 
        mc.button(label=u'C',width=90,height=30,bgc=[0,1,1],command='from idmt.maya.GDC_common import GDC_RenderArnoldLayer\nreload(GDC_RenderArnoldLayer)\nGDC_RenderArnoldLayer.GDC_RenderArnold().P5_ArnoldDisMatCreat(idpShader="ArnoldIdpC")') 
        mc.button(label=u'K',width=90,height=30,bgc=[1,0,1],command='from idmt.maya.GDC_common import GDC_RenderArnoldLayer\nreload(GDC_RenderArnoldLayer)\nGDC_RenderArnoldLayer.GDC_RenderArnold().P5_ArnoldDisMatCreat(idpShader="ArnoldIdpK")')                              
        mc.button(label=u'Lam',width=90,height=30,bgc=[0.5,0.5,0.5],command='from idmt.maya.GDC_common import GDC_RenderArnoldLayer\nreload(GDC_RenderArnoldLayer)\nGDC_RenderArnoldLayer.GDC_RenderArnold().P5_ArnoldDisMatCreat(idpShader="ArnoldLambert")')
        mc.button(label=u'Occ',width=90,height=30,bgc=[1,1,1],command='from idmt.maya.GDC_common import GDC_RenderArnoldLayer\nreload(GDC_RenderArnoldLayer)\nGDC_RenderArnoldLayer.GDC_RenderArnold().P5_ArnoldDisMatCreat(idpShader="ArnoldOcc")')   
        mc.button(label=u'Normal',width=90,height=30,bgc=[0.4,0.55,0.9],command='from idmt.maya.GDC_common import GDC_RenderArnoldLayer\nreload(GDC_RenderArnoldLayer)\nGDC_RenderArnoldLayer.GDC_RenderArnold().P5_ArnoldDisMatCreat(idpShader="ArnoldNormal")')                       
        mc.setParent('..')        
        mc.tabLayout(tabs, edit=True, tabLabel=(
            (child1, u'渲染流程'), (child2, 'Arnold AOV'), (child3, u'渲染工具')))
        mc.showWindow('GDC_RenderArnold')    
    #----------------------------------------------------------#
    #Arnold 设置
    def ArnoldRendererSettings(self,AA=3,form='03'):
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
        
        if(form=='01'):
            mc.setAttr('defaultArnoldDriver.halfPrecision', 1)
            mc.setAttr('defaultArnoldDriver.tiled', 0)
            mc.setAttr('defaultArnoldDriver.autocrop', 1)
            mc.setAttr('defaultArnoldRenderOptions.AASamples', 4)
            #添加Exr合并（HH添加)
            mc.setAttr('defaultArnoldDriver.aiTranslator','exr',type='string')            
            mc.setAttr ('defaultArnoldDriver.mergeAOVs', 1) 
            mc.setAttr ('defaultArnoldRenderOptions.aovMode',1)
        elif(form=='02'):
            mc.setAttr('defaultArnoldDriver.halfPrecision', 1)
            mc.setAttr('defaultArnoldDriver.tiled', 0)
            mc.setAttr('defaultArnoldDriver.autocrop', 1)
            mc.setAttr('defaultArnoldRenderOptions.AASamples', 4)
            mc.setAttr('defaultArnoldDriver.aiTranslator','tif',type='string')
            mc.setAttr('defaultArnoldDriver.tiffFormat',0)
            mc.setAttr('defaultArnoldDriver.tiffCompression',1) 
            mc.setAttr ('defaultArnoldDriver.mergeAOVs', 0)
            mc.setAttr ('defaultArnoldRenderOptions.aovMode',1)
        elif(form=='03'):
            mc.setAttr('defaultArnoldDriver.halfPrecision', 1)
            mc.setAttr('defaultArnoldDriver.tiled', 0)
            mc.setAttr('defaultArnoldDriver.autocrop', 1)
            mc.setAttr('defaultArnoldRenderOptions.AASamples', 5)
            mc.setAttr('defaultArnoldRenderOptions.GIDiffuseSamples', 0)
            mc.setAttr('defaultArnoldRenderOptions.GIGlossySamples', 0)
            mc.setAttr('defaultArnoldRenderOptions.GIRefractionSamples', 0)
            mc.setAttr('defaultArnoldRenderOptions.sssBssrdfSamples', 3)
            mc.setAttr('defaultArnoldRenderOptions.lock_sampling_noise', 1)
            mc.setAttr('defaultArnoldRenderOptions.use_sample_clamp', 1)
            mc.setAttr('defaultArnoldRenderOptions.AASampleClamp', 1.5) 
            mc.setAttr('defaultArnoldRenderOptions.GITotalDepth', 5) 
            mc.setAttr('defaultArnoldRenderOptions.use_existing_tiled_textures', 1)                                                                                              
            mc.setAttr('defaultArnoldDriver.aiTranslator','tif',type='string')
            mc.setAttr('defaultArnoldDriver.tiffFormat',0)            
            mc.setAttr('defaultArnoldDriver.tiffCompression',1) 
            
            mc.setAttr ('defaultArnoldDriver.mergeAOVs', 0)  
            mc.setAttr ('defaultArnoldRenderOptions.aovMode',1)

        elif(form=='04'):
            mc.setAttr('defaultArnoldDriver.halfPrecision', 1)
            mc.setAttr('defaultArnoldDriver.tiled', 0)
            mc.setAttr('defaultArnoldDriver.autocrop', 1)
            mc.setAttr('defaultArnoldRenderOptions.AASamples', 5)
            mc.setAttr('defaultArnoldRenderOptions.GIDiffuseSamples', 0)
            mc.setAttr('defaultArnoldRenderOptions.GIGlossySamples', 0)
            mc.setAttr('defaultArnoldRenderOptions.GIRefractionSamples', 0)
            mc.setAttr('defaultArnoldRenderOptions.sssBssrdfSamples', 1)
            mc.setAttr('defaultArnoldRenderOptions.lock_sampling_noise', 1)
            mc.setAttr('defaultArnoldRenderOptions.use_sample_clamp', 1)
            mc.setAttr('defaultArnoldRenderOptions.AASampleClamp', 1.5) 
            mc.setAttr('defaultArnoldRenderOptions.GITotalDepth', 5) 
            mc.setAttr('defaultArnoldRenderOptions.use_existing_tiled_textures', 1)                                                                                              
            mc.setAttr('defaultArnoldDriver.aiTranslator','tif',type='string')
            mc.setAttr('defaultArnoldDriver.tiffFormat',0)            
            mc.setAttr('defaultArnoldDriver.tiffCompression',1) 
            
            mc.setAttr ('defaultArnoldDriver.mergeAOVs', 0) 
            mc.setAttr ('defaultArnoldRenderOptions.aovMode',1)
        elif(form=='05'):
            mc.setAttr('defaultArnoldDriver.halfPrecision', 1)
            mc.setAttr('defaultArnoldDriver.tiled', 0)
            mc.setAttr('defaultArnoldDriver.autocrop', 1)
            mc.setAttr('defaultArnoldRenderOptions.AASamples', 3)
            mc.setAttr('defaultArnoldRenderOptions.GIDiffuseSamples', 0)
            mc.setAttr('defaultArnoldRenderOptions.GIGlossySamples', 0)
            mc.setAttr('defaultArnoldRenderOptions.GIRefractionSamples', 0)
            mc.setAttr('defaultArnoldRenderOptions.sssBssrdfSamples', 0)
            mc.setAttr('defaultArnoldRenderOptions.lock_sampling_noise', 1)
            mc.setAttr('defaultArnoldRenderOptions.use_sample_clamp', 1)
            mc.setAttr('defaultArnoldRenderOptions.AASampleClamp', 1.5) 
            mc.setAttr('defaultArnoldRenderOptions.GITotalDepth', 5) 
            mc.setAttr('defaultArnoldRenderOptions.use_existing_tiled_textures', 1)                                                                                              
            mc.setAttr('defaultArnoldDriver.aiTranslator','tif',type='string')
            mc.setAttr('defaultArnoldDriver.tiffFormat',0)            
            mc.setAttr('defaultArnoldDriver.tiffCompression',1) 
            
            mc.setAttr ('defaultArnoldDriver.mergeAOVs', 0)    
            mc.setAttr ('defaultArnoldRenderOptions.aovMode',1)
        elif(form=='05'):
            mc.setAttr('defaultArnoldDriver.halfPrecision', 1)
            mc.setAttr('defaultArnoldDriver.tiled', 0)
            mc.setAttr('defaultArnoldDriver.autocrop', 1)
            mc.setAttr('defaultArnoldRenderOptions.AASamples', 3)
            mc.setAttr('defaultArnoldRenderOptions.GIDiffuseSamples', 0)
            mc.setAttr('defaultArnoldRenderOptions.GIGlossySamples', 0)
            mc.setAttr('defaultArnoldRenderOptions.GIRefractionSamples', 0)
            mc.setAttr('defaultArnoldRenderOptions.sssBssrdfSamples', 0)
            mc.setAttr('defaultArnoldRenderOptions.lock_sampling_noise', 1)
            mc.setAttr('defaultArnoldRenderOptions.use_sample_clamp', 1)
            mc.setAttr('defaultArnoldRenderOptions.AASampleClamp', 1.5) 
            mc.setAttr('defaultArnoldRenderOptions.GITotalDepth', 5) 
            mc.setAttr('defaultArnoldRenderOptions.use_existing_tiled_textures', 1)                                                                                              
            mc.setAttr('defaultArnoldDriver.aiTranslator','tif',type='string')
            mc.setAttr('defaultArnoldDriver.tiffFormat',0)            
            mc.setAttr('defaultArnoldDriver.tiffCompression',1) 
            
            mc.setAttr ('defaultArnoldDriver.mergeAOVs', 0)               
        elif(form=='shadow'):
            mc.setAttr('defaultArnoldDriver.halfPrecision', 1)
            mc.setAttr('defaultArnoldDriver.tiled', 0)
            mc.setAttr('defaultArnoldDriver.autocrop', 1)
            mc.setAttr('defaultArnoldRenderOptions.AASamples', 3)
            mc.setAttr('defaultArnoldRenderOptions.GIDiffuseSamples', 0)
            mc.setAttr('defaultArnoldRenderOptions.GIGlossySamples', 0)
            mc.setAttr('defaultArnoldRenderOptions.GIRefractionSamples', 0)
            mc.setAttr('defaultArnoldRenderOptions.sssBssrdfSamples', 0)
            mc.setAttr('defaultArnoldRenderOptions.lock_sampling_noise', 1)
            mc.setAttr('defaultArnoldRenderOptions.use_sample_clamp', 1)
            mc.setAttr('defaultArnoldRenderOptions.AASampleClamp', 1.5) 
            mc.setAttr('defaultArnoldRenderOptions.GITotalDepth', 5) 
            mc.setAttr('defaultArnoldRenderOptions.use_existing_tiled_textures', 1)                                                                                              
            mc.setAttr('defaultArnoldDriver.aiTranslator','tif',type='string')
            mc.setAttr('defaultArnoldDriver.tiffFormat',0)            
            mc.setAttr('defaultArnoldDriver.tiffCompression',1) 
            
            mc.setAttr ('defaultArnoldDriver.mergeAOVs', 0)  
            mc.setAttr ('defaultArnoldRenderOptions.aovMode',1)
        elif(form=='mob'):
            mc.setAttr('defaultArnoldDriver.halfPrecision', 1)
            mc.setAttr('defaultArnoldDriver.tiled', 0)
            mc.setAttr('defaultArnoldDriver.autocrop', 1)
            mc.setAttr('defaultArnoldRenderOptions.AASamples', 3)
            mc.setAttr('defaultArnoldRenderOptions.GIDiffuseSamples', 0)
            mc.setAttr('defaultArnoldRenderOptions.GIGlossySamples', 0)
            mc.setAttr('defaultArnoldRenderOptions.GIRefractionSamples', 0)
            mc.setAttr('defaultArnoldRenderOptions.sssBssrdfSamples', 0)
            mc.setAttr('defaultArnoldRenderOptions.lock_sampling_noise', 1)
            mc.setAttr('defaultArnoldRenderOptions.use_sample_clamp', 1)
            mc.setAttr('defaultArnoldRenderOptions.AASampleClamp', 1.5) 
            mc.setAttr('defaultArnoldRenderOptions.GITotalDepth', 5) 
            mc.setAttr('defaultArnoldRenderOptions.use_existing_tiled_textures', 1)                                                                                              
            mc.setAttr('defaultArnoldDriver.aiTranslator','exr',type='string')
            mc.setAttr ('defaultArnoldDriver.exrCompression', 3)
            mc.setAttr ('defaultArnoldRenderOptions.aovMode',1)                                      
    #----------------------------------------------------------#    
    #motionblur渲染层创建
    def csl_ArnoldRenderLayerCreat(self,layername='motionblur'):
        objselect=mc.ls(sl=1,l=1)
        from idmt.maya.GDC_common import GDC_RenderArnoldLayer
        reload(GDC_RenderArnoldLayer)
        self.ArnoldRendererSettings('04')
        mc.select(objselect)
           	    	
      #创建渲染层 
        mel.eval('source "//file-cluster/GDC/Resource/Support/Maya/projects/ShunLiu/CSL_RenderToolsMR.mel";CSL_RenderTools_ArnoldCreat(\"' + layername + '\");')
        mc.select(objselect)
        if layername=='motionblur':
            self.ArnoldMotionBlurShaderCreate()
            mc.setAttr('defaultArnoldRenderOptions.motion_blur_enable',1);            
        else :
            mc.setAttr('defaultArnoldRenderOptions.motion_blur_enable',0);
            return  layername  
#motionblur 材质球                   	              
    def ArnoldMotionBlurShaderCreate(self):
        #----------------------#
        # shader
        #----------------------#
        #motionBlur
        obj=mc.ls(sl=1,l=1)            
        mblurShader = 'SHD_mov_arnold'
        if mc.ls( mblurShader ):
            mc.delete(mblurShader)
        mblurSG = 'SHD_mov_arnoldSG'
        if mc.ls( mblurSG ):
            mc.delete( mblurSG )
        mblurShader = mc.shadingNode ('aiMotionVector', asShader=True, name= mblurShader)  
        mblurSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=( mblurSG ))
        mc.connectAttr(('%s.%s') % (mblurShader , 'outColor') , ('%s.%s') % (mblurSG , 'surfaceShader'), f=True)
        try:
            mc.setAttr ((mblurShader+'.raw'), 1)
        except:
            pass                     
        mc.select(obj)
        mc.sets(obj,e = 1 , forceElement = mblurSG)
        mc.setAttr('defaultArnoldRenderOptions.motion_blur_enable',1);
         
 
        #----------------------#
        # AOVPSS 创建（Zdp,AO,Normal,Shadow,Fre)
    def ArnoldAOVCreat(self,AOVtype='Zdp',passtype=int('5')):
        #Arnold 外部AOV 创建        
        if  AOVtype in ['Zdp','AO','Normal','Shadow','Fre']:
            self.ArnoldShaderAssign(AOVtype,transparency=0)
            AOVShader = 'SHD_'+AOVtype+'_arnold'
            # AOV Pass Creat
            AOVArnoldPass = 'ZDAOV_'+AOVtype
            if mc.ls(AOVArnoldPass) :
                if mc.nodeType(AOVArnoldPass) =='aiAOV':
                    pass
                else:
                    mc.delete(AOVArnoldPass)
                    mc.createNode('aiAOV',name = AOVArnoldPass)
            else:
                mc.createNode('aiAOV',name = AOVArnoldPass )
            mc.setAttr((AOVArnoldPass + '.name'),AOVtype,type = 'string')
            mc.setAttr((AOVArnoldPass + '.type'),passtype) 
            # connect
            try:
                mc.disconnectAttr(('%s.%s') % ('defaultArnoldDriver' , 'message') , ('%s.%s') % (AOVArnoldPass , 'outputs[0].driver'))
            except:
                pass
            mc.connectAttr(('%s.%s') % ('defaultArnoldDriver' , 'message') , ('%s.%s') % (AOVArnoldPass , 'outputs[0].driver'), f=True)
            try:
                mc.disconnectAttr(('%s.%s') % ( 'defaultArnoldFilter' , 'message') , ('%s.%s') % (AOVArnoldPass , 'outputs[0].filter'))
            except:
                pass
            mc.connectAttr(('%s.%s') % ( 'defaultArnoldFilter' , 'message') , ('%s.%s') % (AOVArnoldPass , 'outputs[0].filter'), f=True)
            try:
                mc.disconnectAttr(('%s.%s') % ( AOVShader , 'outColor') , ('%s.%s') % (AOVArnoldPass, 'defaultValue'))
            except:
                pass
            mc.connectAttr(('%s.%s') % ( AOVShader , 'outColor') , ('%s.%s') % (AOVArnoldPass, 'defaultValue'), f=True)
            if  AOVtype=='Zdp':
                zdpDriver='zdpAovDirver'
                if mc.ls(zdpDriver):
                    mc.delete(zdpDriver)
                mc.shadingNode('aiAOVDriver',asUtility=1,n=zdpDriver)                                 
                try:
                    mc.disconnectAttr(('%s.%s') % ('defaultArnoldDriver' , 'message') , ('%s.%s') % (AOVArnoldPass , 'outputs[0].driver'))
                except:
                    pass
                mc.connectAttr(('%s.%s') % (zdpDriver , 'message') , ('%s.%s') % (AOVArnoldPass , 'outputs[0].driver'), f=True) 
 
 
                try:
                    mc.disconnectAttr(('%s.%s') % ( AOVArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[0]'))
                except:
                    pass
                mc.connectAttr(('%s.%s') % ( AOVArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[0]'), f=True)  

                mc.setAttr((zdpDriver+'.aiTranslator'),'exr',type='string')
                mc.setAttr ((zdpDriver+'.exrCompression'), 3)
                mc.setAttr ((zdpDriver+'.halfPrecision'), 1)
                mc.setAttr ((zdpDriver+'.autocrop'), 1)
                mc.setAttr ((AOVArnoldPass+'.type'), 4)

            if  AOVtype=='AO':
                try:
                    mc.disconnectAttr(('%s.%s') % ( AOVArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[1]'))
                except:
                    pass
                mc.connectAttr(('%s.%s') % ( AOVArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[1]'), f=True)                 
            if  AOVtype=='Normal':
                try:
                    mc.disconnectAttr(('%s.%s') % ( AOVArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[2]'))
                except:
                    pass
                mc.connectAttr(('%s.%s') % ( AOVArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[2]'), f=True)
            if  AOVtype=='Shadow':
                try:
                    mc.disconnectAttr(('%s.%s') % ( AOVArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[3]'))
                except:
                    pass
                mc.connectAttr(('%s.%s') % ( AOVArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[3]'), f=True)
            if  AOVtype=='Fre':
                try:
                    mc.disconnectAttr(('%s.%s') % ( AOVArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[4]'))
                except:
                    pass
                mc.connectAttr(('%s.%s') % ( AOVArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[4]'), f=True)
            mc.setAttr ('defaultArnoldDriver.mergeAOVs', 0)
            mc.setAttr('defaultArnoldDriver.prefix','<RenderLayer>_<RenderPass>/<Scene>_<RenderLayer>_<RenderPass>',type='string') 
            mc.setAttr('defaultArnoldDriver.aiTranslator','tif',type='string')
            mc.setAttr('defaultArnoldDriver.tiffFormat',0)            
            mc.setAttr('defaultArnoldDriver.tiffCompression',1) 
        #Arnold 内部AOV创建
        if  AOVtype in ['sss','Z','motionvector','opacity']:
            ArnoldPass = 'aiAOV_'+AOVtype
            if mc.ls(ArnoldPass) :
                if mc.nodeType(ArnoldPass) =='aiAOV':
                    pass
                else:
                    mc.delete(ArnoldPass)
                    mc.createNode('aiAOV',name = ArnoldPass)
            else:
                mc.createNode('aiAOV',name = ArnoldPass )
            mc.setAttr((ArnoldPass + '.name'),AOVtype,type = 'string')
            mc.setAttr((ArnoldPass + '.type'),5)   
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
#
            #connect
            try:
                mc.disconnectAttr(('%s.%s') % ('defaultArnoldDriver' , 'message') , ('%s.%s') % (ArnoldPass , 'outputs[0].driver'))
            except:
                pass
            mc.connectAttr(('%s.%s') % ('defaultArnoldDriver' , 'message') , ('%s.%s') % (ArnoldPass , 'outputs[0].driver'), f=True)
            try:
                mc.disconnectAttr(('%s.%s') % ( aiAOVFilter_Closset , 'message') , ('%s.%s') % (ArnoldPass, 'outputs[0].filter'))
            except:
                pass
            mc.connectAttr(('%s.%s') % ( aiAOVFilter_Closset , 'message') , ('%s.%s') % (ArnoldPass, 'outputs[0].filter'), f=True)
            if AOVtype=='sss':
                try:
                    mc.disconnectAttr(('%s.%s') % ( ArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[21]'))
                except:
                    pass
                mc.connectAttr(('%s.%s') % ( ArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[21]'), f=True)       
            if AOVtype=='motionvector':
                try:
                    mc.disconnectAttr(('%s.%s') % ( ArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[22]'))
                except:
                    pass
                mc.connectAttr(('%s.%s') % ( ArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[22]'), f=True)  
                mc.setAttr('defaultArnoldRenderOptions.ignoreMotionBlur',1)
                mc.setAttr('defaultArnoldRenderOptions.motion_blur_enable',1)
                mc.setAttr('defaultArnoldRenderOptions.range_type',0)
            mc.setAttr ('defaultArnoldDriver.mergeAOVs', 0)
            mc.setAttr('defaultArnoldDriver.prefix','<RenderLayer>_<RenderPass>/<Scene>_<RenderLayer>_<RenderPass>',type='string')               

            if AOVtype=='opacity':
                try:
                    mc.disconnectAttr(('%s.%s') % ( ArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[23]'))
                except:
                    pass
                mc.connectAttr(('%s.%s') % ( ArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[23]'), f=True)                               

            if AOVtype=='Z':
                try:
                    mc.disconnectAttr(('%s.%s') % ( ArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[24]'))
                except:
                    pass
                mc.connectAttr(('%s.%s') % ( ArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[24]'), f=True)          

        
    #渲染层创建
    def ArnoldRendererLayerCreat(self):
        from idmt.maya.GDC_common import GDC_RenderArnoldLayer
        reload(GDC_RenderArnoldLayer)
        GDC_RenderArnoldLayer.GDC_RenderArnold().ArnoldRendererSettings('03')
           	    	
      #创建渲染层 
        mel.eval('source "//file-cluster/GDC/Resource/Support/Maya/projects/ShunLiu/CSL_RenderToolsMR.mel";CSL_RenderTools_Arnold();')   	
    	#创建pass
        occpass=mc.checkBox('hhcheckocc',q=1,v=1)
        normalpass=mc.checkBox('hhchecknormal',q=1,v=1)
        frepass=mc.checkBox('hhcheckfre',q=1,v=1)
#        keypass=mc.checkBox('hhcheckkey',q=1,v=1)
        SSSpass=mc.checkBox('hhcheckSSS',q=1,v=1)
        shadowpass=mc.checkBox('hhcheckshadow',q=1,v=1)
        zdppass=mc.checkBox('hhcheckzdep',q=1,v=1)
        movpass=mc.checkBox('hhcheckmov',q=1,v=1)
        #id01pass=mc.checkBox('hhcheckid01',q=1,v=1)
        #occ
        if occpass == True :
        	from idmt.maya.GDC_common import GDC_RenderArnoldLayer
        	reload(GDC_RenderArnoldLayer)
        	GDC_RenderArnoldLayer.GDC_RenderArnold().ArnoldAOVCreat(AOVtype="AO")
        #normal
        if normalpass == True :
        	from idmt.maya.GDC_common import GDC_RenderArnoldLayer
        	reload(GDC_RenderArnoldLayer)
        	GDC_RenderArnoldLayer.GDC_RenderArnold().ArnoldAOVCreat(AOVtype="Normal")
        #fre
        if frepass == True :
        	from idmt.maya.GDC_common import GDC_RenderArnoldLayer
        	reload(GDC_RenderArnoldLayer)
        	GDC_RenderArnoldLayer.GDC_RenderArnold().ArnoldAOVCreat(AOVtype="Fre")
        #keyl
#        if keypass == True :
#        	from idmt.maya.GDC_common import GDC_RenderArnoldLayer
#        	reload(GDC_RenderArnoldLayer)
#        	GDC_RenderArnoldLayer.GDC_RenderArnold().ArnoldAOVKeyLight()
        if SSSpass == True :
        	from idmt.maya.GDC_common import GDC_RenderArnoldLayer
        	reload(GDC_RenderArnoldLayer)
        	GDC_RenderArnoldLayer.GDC_RenderArnold().ArnoldAOVCreat(AOVtype="SSS")
        if shadowpass == True :
        	from idmt.maya.GDC_common import GDC_RenderArnoldLayer
        	reload(GDC_RenderArnoldLayer)
        	GDC_RenderArnoldLayer.GDC_RenderArnold().ArnoldAOVCreat(AOVtype="Shadow")
        #zdp
        if zdppass == True :
        	from idmt.maya.GDC_common import GDC_RenderArnoldLayer
        	reload(GDC_RenderArnoldLayer)
        	GDC_RenderArnoldLayer.GDC_RenderArnold().ArnoldAOVCreat(AOVtype='Zdp') 
        #zdp
        if movpass == True :
        	from idmt.maya.GDC_common import GDC_RenderArnoldLayer
        	reload(GDC_RenderArnoldLayer)
        	GDC_RenderArnoldLayer.GDC_RenderArnold().ArnoldAOVCreat(AOVtype='motionvector') 
 
    #----------------------------------------------------------#
    #删除文件中AOV（AO）
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
    #删除文件中AOV（normal）
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
    #删除文件中AOV（Fre）
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
    #删除文件中AOV（Key）
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
    #删除文件中AOV（Shadow） 
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
    #删除文件中AOV（zdep）            
    def ArnoldAOVDelete(self,AOVtype='Zdp'):
        AOVShader = 'SHD_'+AOVtype+'_arnold'
        AOVArnoldPass = 'ZDAOV_'+AOVtype
        AOVShaderSG= AOVShader+'SG'       
        if mc.ls(AOVShader) :
            mc.delete(AOVShader) 
        if mc.ls(AOVArnoldPass) :
            mc.delete(AOVArnoldPass)  
        if mc.ls(AOVShaderSG) :
            mc.delete(AOVShaderSG)                                     
    #删除文件中AOV（zdep arnold默认）            
    def ArnoldAOVZdepDelete(self,AOVtype='sss'):
        occArnoldPass = 'aiAOV_'+AOVtype
        if mc.ls(occArnoldPass) :
            mc.delete(occArnoldPass)
    #删除文件中所有AOV（渲染层）
    def ArnoldALLDelete(self,nodetype='aiAOV'):
        Info = mc.ls(type=nodetype)  
        if nodetype=='renderLayer':
            Info.remove('defaultRenderLayer')
            mc.editRenderLayerGlobals(currentRenderLayer='defaultRenderLayer')
        if mc.ls(Info) :
                mc.delete(Info)            
                                                  
    #带置换节点的物体赋idp            
    def P5_ArnoldDisMatCreat(self,idpShader):
        meshs=mc.ls(sl=1,type='transform')

        #self.ArnoldRendererSettings('03')      
        if(idpShader=='ArnoldIdpR01'):
            if mc.objExists(idpShader)==0:
                mc.shadingNode('aiUtility', asShader=True,n=idpShader)
                mc.setAttr((idpShader+".shadeMode"),2 )
                mc.setAttr((idpShader+".colorMode"),0 )
                mc.setAttr((idpShader+'.color'),1,0,0)
                mc.setAttr((idpShader+'.hardwareColor'),1,0,0)                
        elif(idpShader=='ArnoldIdpG'):
            if mc.objExists(idpShader)==0:
                mc.shadingNode('aiUtility', asShader=True,n=idpShader)
                mc.setAttr((idpShader+".shadeMode"),2 )
                mc.setAttr((idpShader+".colorMode"),0 )        
                mc.setAttr((idpShader+'.color'),0,1,0)
                mc.setAttr((idpShader+'.hardwareColor'),0,1,0)
        elif(idpShader=='ArnoldIdpB'):
            if mc.objExists(idpShader)==0:
                mc.shadingNode('aiUtility', asShader=True,n=idpShader)
                mc.setAttr((idpShader+".shadeMode"),2 )
                mc.setAttr((idpShader+".colorMode"),0 )        
                mc.setAttr((idpShader+'.color'),0,0,1)
                mc.setAttr((idpShader+'.hardwareColor'),0,0,1)
        elif(idpShader=='ArnoldIdpY'):
            if mc.objExists(idpShader)==0:
                mc.shadingNode('aiUtility', asShader=True,n=idpShader)
    
                mc.setAttr((idpShader+".shadeMode"),2 )
                mc.setAttr((idpShader+".colorMode"),0 )        
                mc.setAttr((idpShader+'.color'),1,1,0)
                mc.setAttr((idpShader+'.hardwareColor'),1,1,0) 

        elif(idpShader=='ArnoldIdpC'):
            if mc.objExists(idpShader)==0:
                mc.shadingNode('aiUtility', asShader=True,n=idpShader)
    
                mc.setAttr((idpShader+".shadeMode"),2 )
                mc.setAttr((idpShader+".colorMode"),0 )        
                mc.setAttr((idpShader+'.color'),0,1,0)
                mc.setAttr((idpShader+'.hardwareColor'),0,0,0) 
                
        elif(idpShader=='ArnoldIdpK'):
            if mc.objExists(idpShader)==0:
                mc.shadingNode('aiUtility', asShader=True,n=idpShader)
    
                mc.setAttr((idpShader+".shadeMode"),2 )
                mc.setAttr((idpShader+".colorMode"),0 )        
                mc.setAttr((idpShader+'.color'),0,0,0)
                mc.setAttr((idpShader+'.hardwareColor'),0,0,0)                                 
        elif(idpShader=='ArnoldLambert'):
            if mc.objExists(idpShader)==0:
                mc.shadingNode('aiUtility', asShader=True,n=idpShader)
                mc.setAttr((idpShader+".colorMode"),0 ) 
                mc.setAttr((idpShader+".shadeMode"),1 )                      
                mc.setAttr((idpShader+'.color'),1,1,1)
                mc.setAttr((idpShader+'.hardwareColor'),1,1,1)
        elif(idpShader=='ArnoldOcc'):
            if mc.objExists(idpShader)==0:
                mc.shadingNode('aiAmbientOcclusion', asShader=True,n=idpShader)
                mc.setAttr((idpShader+".samples"),4 ) 
                mc.setAttr((idpShader+".falloff"),0.05 )                      
                mc.setAttr((idpShader+'.spread'),0.8)   
        elif(idpShader=='ArnoldNormal'):
            if mc.objExists(idpShader)==0:
                mc.shadingNode('aiUtility', asShader=True,n=idpShader)
                mc.setAttr((idpShader+".shadeMode"),2 ) 
                mc.setAttr((idpShader+".colorMode"),3 ) 
                mc.setAttr((idpShader+'.color'),1,1,1)  
                mc.setAttr((idpShader+'.hardwareColor'),0,0,0) 
        elif(idpShader=='ArnoldIdpM'):
            if mc.objExists(idpShader)==0:
                mc.shadingNode('aiStandard', asShader=True,n=idpShader)
                mc.setAttr((idpShader+'.aiEnableMatte'),1)
        idSG=idpShader+'SG'
        if mc.objExists(idSG)==0:
            mc.sets(renderable=1,noSurfaceShader=1,em=1,n=idSG)
        cons=mc.listConnections('%s.outColor' % idpShader)
        if cons!=None:
            if(cons[0]!=idSG):
                mc.disconnectAttr(('%s.outColor' % idpShader), ('%s.surfaceShader' % cons[0]))
                mc.connectAttr(('%s.outColor' % idpShader),('%s.surfaceShader' % idSG))                                                                                
#####
#        SGS=mc.ls(type='shadingEngine')
#        SGS.remove('initialParticleSE')
#        SGS.remove('initialShadingGroup') 
#        for SG in SGS:
#            buf = mc.listConnections(( SG + '.surfaceShader'), connections=1, plugs=1)
#            if buf:
#                for i in range(len(buf) / 2):
#                    shape = buf[i + 1].split('.')[0]
#                    if mc.nodeType(shape) != 'renderLayer':
#                        try:
#                            mc.disconnectAttr(buf[i + 1], buf[i])
#                        except:
#                            pass
#            mc.connectAttr((idpShader+'.outColor'), ( SG + '.surfaceShader'), f=True) 
        if meshs:
            for mesh in meshs:
                shapes = mc.listRelatives(mesh, ad=1, ni=1, type='mesh', f=1)
                if not shapes:
                    continue
                msg=mc.listConnections(shapes[0],s=0,type = 'shadingEngine')
                if not msg:
                    continue
                else:
                    DisCon=mc.listConnections((msg[0]+'.displacementShader'),connections=1, plugs=1)
                    if not DisCon:
                        mc.select(mesh)
                        mc.sets(mesh,e=1,forceElement=idSG) 
                    else:
                        newSG=mc.sets(renderable=1,noSurfaceShader=1,em=1,n=(msg[0]+'01'))
                        mc.connectAttr(('%s.outColor' % idpShader),('%s.surfaceShader' % newSG))
                        mc.connectAttr(DisCon[1],('%s.displacementShader' % newSG))
                        mc.select(mesh)
                        cmd1="`"+"sets -e -forceElement"+" "+newSG+"`"
                        cmd= "catch("+cmd1+")"
                        mel.eval(cmd)                     
        else:
            print(u'请选择物体')
    # 普通idp                                 
    def ArnoldIDCreat(self,idpShader):
        sels=mc.ls(sl=True)
        #from idmt.maya.GDC_common import GDC_RenderArnoldLayer
        #reload(GDC_RenderArnoldLayer)
        #GDC_RenderArnoldLayer.GDC_RenderArnold().ArnoldRendererSettings('02')
        if mc.objExists(idpShader)==0:
            mc.shadingNode('aiUtility', asShader=True,n=idpShader)
        idpSG=idpShader+'SG'
        if mc.objExists(idpSG)==0:
            mc.sets(renderable=1,noSurfaceShader=1,em=1,n=idpSG)
        cons=mc.listConnections('%s.outColor' % idpShader)
        if cons!=None:
            if(cons[0]!=idpSG):
                mc.disconnectAttr(('%s.outColor' % idpShader), ('%s.surfaceShader' % cons[0]))
                mc.connectAttr(('%s.outColor' % idpShader),('%s.surfaceShader' % idpSG))
        else:
            mc.connectAttr(('%s.outColor' % idpShader),('%s.surfaceShader' % idpSG))
        mc.setAttr((idpShader+".shadeMode"),2 )
        mc.setAttr((idpShader+".colorMode"),0 )
        if(idpShader=='ArnoldIdpR'):
            mc.setAttr((idpShader+'.color'),1,0,0)
            mc.setAttr((idpShader+'.hardwareColor'),1,0,0)
        elif(idpShader=='ArnoldIdpG'):
            mc.setAttr((idpShader+'.color'),0,1,0)
            mc.setAttr((idpShader+'.hardwareColor'),0,1,0)
        elif(idpShader=='ArnoldIdpB'):
            mc.setAttr((idpShader+'.color'),0,0,1)
            mc.setAttr((idpShader+'.hardwareColor'),0,0,1) 
        elif(idpShader=='ArnoldIdpM'):
            mc.setAttr((idpShader+'.color'),0,0,0)
            mc.setAttr((idpShader+'.hardwareColor'),0,0,0) 
        elif(idpShader=='ArnoldIdpY'):
            mc.setAttr((idpShader+'.color'),1,1,0)
            mc.setAttr((idpShader+'.hardwareColor'),1,1,0) 
        elif(idpShader=='ArnoldIdpC'):
            mc.setAttr((idpShader+'.color'),0,1,1)
            mc.setAttr((idpShader+'.hardwareColor'),0,1,1) 
        elif(idpShader=='ArnoldIdpK'):
            mc.setAttr((idpShader+'.color'),1,0,1)
            mc.setAttr((idpShader+'.hardwareColor'),1,0,1)
        else:
            print(u'请正确输入IDP类型')
                                                                    
        mc.select(sels)
        try:
            mc.sets(e = 1 , forceElement = idpSG)
        except:
            print(u'===有物体无法赋予材质===')
            print(sels)
            mc.error(u'===有物体无法赋予材质===')         
#        cmd1="`"+"sets -e -forceElement"+" "+idpSG+"`"
#        cmd= "catch("+cmd1+")"
#        mel.eval(cmd) 
#材质球创建
    def ArnoldShaderAssign(self,shaderType='Shadow',transparency=0):
        meshs=mc.ls(sl=1,l=1)
        if transparency==0:
            Shade='SHD_'+shaderType+'_arnold'
            SG=Shade+'SG'
            #删除已有材质球和SG节点
            if mc.objExists(Shade):
                mc.delete(Shade)
            if mc.objExists(SG):
                mc.delete(SG) 
            #创建新材质球和SG节点
            if shaderType=='AO':
                mc.shadingNode('aiAmbientOcclusion', asShader=True,n=Shade)
            if shaderType=='Shadow':
                mc.shadingNode('aiShadowCatcher', asShader=True,n=Shade)    
            else:
                mc.shadingNode('aiUtility', asShader=True,n=Shade)
            mc.sets(renderable=1,noSurfaceShader=1,em=1,n=SG)
            mc.connectAttr(('%s.outColor' % Shade),('%s.surfaceShader' % SG))
            if meshs:
                mc.sets(meshs,e=1, forceElement = SG)
            else:
                pass            
            if shaderType=='Zdp': 
                #节点
                setRange='csl_setRange_arnold'
                express='csl_expression_arnold'
                multiply='csl_multiplyDivide_arnold'
                samplerInfo='csl_samplerInfo_arnold'
                #创建节点
                if mc.objExists(setRange):
                    mc.delete(setRange)
                if mc.objExists(multiply):
                    mc.delete(multiply) 
                if mc.objExists(samplerInfo):
                    mc.delete(samplerInfo) 
                if mc.objExists(express):
                    mc.delete(express)     
                #创建节点
                #mc.shadingNode('aiUtility', asShader=True,n=Shade)
                mc.shadingNode('setRange',asUtility=True,n=setRange)
                mc.shadingNode('multiplyDivide',asUtility=True,n=multiply)
                mc.shadingNode('samplerInfo',asUtility=True,n=samplerInfo)  
                #添加shade节点
                mc.setAttr((Shade+'.shadeMode'),2)
                mc.addAttr(Shade,sn='black',longName='black',nn='Black',attributeType='double')
                mc.addAttr(Shade,sn='write',longName='write',nn='Write',attributeType='double')
                mc.addAttr(Shade,sn='farClipPlane',longName='farClipPlane',nn='Far Clip Plane',attributeType='double')
                mc.addAttr(Shade,sn='nearClipPlane',longName='nearClipPlane',nn='Near Clip Plane',attributeType='double')
                #shade参数设置
                mc.setAttr((Shade+'.shade_mode'),2)
                mc.setAttr((Shade+'.black'),1)
                mc.setAttr((Shade+'.write'),-1)
                mc.setAttr((Shade+'.farClipPlane'),800)
                mc.setAttr((Shade+'.nearClipPlane'),1)
                #range设置
                mc.setAttr((setRange+".ai_max"), 1,0,0)
                #multiply设置
                mc.setAttr((multiply+".i2"), -1,1,1)
                mc.setAttr((multiply+'.input2X'),-1)
                #express创建
                expCommon=setRange+'.oldMinX='+Shade+'.nearClipPlane;\n'+setRange+'.oldMaxX='+Shade+'.farClipPlane;'
                mc.expression (n=express,s=expCommon)
                #连接节点
                #setRange 与Shade连接
                mc.connectAttr((setRange+'.outValueX'),(Shade+'.colorR'),f=1)
                mc.connectAttr((setRange+'.outValueX'),(Shade+'.colorG'),f=1)
                mc.connectAttr((setRange+'.outValueX'),(Shade+'.colorB'),f=1)
                mc.connectAttr((Shade+'.write'),(setRange+'.maxX'),f=1)
                mc.connectAttr((Shade+'.black'),(setRange+'.minX'),f=1)
                #multiplyDivide 与multiply连接
                mc.connectAttr((multiply+'.outputX'),(setRange+'.valueX'),f=1)
                #samplerInfo与multiplyDivide连接
                mc.connectAttr((samplerInfo+'.pointCameraZ'),(multiply+'.input1X'),f=1)
    #AO材质
            if shaderType=='AO':
                mc.setAttr ((Shade+'.falloff'),0.05)
                mc.setAttr ((Shade+'.samples'),4)
    #Normal 材质
            if shaderType=='Normal':
                mc.setAttr ((Shade+'.shadeMode'),2)
                mc.setAttr ((Shade+'.colorMode'),3)
            if shaderType=='Fre':
                FNRamp = 'SHD_Fresnel_ramp_arnold'
                FNSample = 'SHD_Fresnel_Sample_arnold'
                if mc.ls( FNRamp ):
                    mc.delete(FNRamp)
                if mc.ls( FNSample ):
                    mc.delete(FNSample)                
                mc.shadingNode ('ramp', asShader=True, name= FNRamp)  
                mc.shadingNode ('samplerInfo', asShader=True, name= FNSample)
                mc.removeMultiInstance((FNRamp + '.colorEntryList[1]') , b = 1)
                mc.setAttr((Shade + '.shadeMode'),2)
                mc.setAttr((FNRamp + '.interpolation'),3)
                mc.setAttr((FNRamp + '.colorEntryList[2].position'),1)
                mc.setAttr((FNRamp + '.colorEntryList[0].position'),0)
                mc.setAttr((FNRamp + '.colorEntryList[2].color'),0,0,0,type = 'double3')
                mc.setAttr((FNRamp + '.colorEntryList[0].color'),1,1,1,type = 'double3') 
                mc.connectAttr(('%s.%s') % (FNSample , 'facingRatio') , ('%s.%s') % (FNRamp , 'uCoord'), f=True)
                mc.connectAttr(('%s.%s') % (FNSample , 'facingRatio') , ('%s.%s') % (FNRamp , 'vCoord'), f=True)
                mc.connectAttr(('%s.%s') % (FNRamp , 'outColor') , ('%s.%s') % (Shade , 'color'), f=True)                       
    #Shadow材质
            if shaderType=='Shadow':
                mc.setAttr((Shade + '.backgroundColor'),0,0,0,type = 'double3') 
                mc.setAttr((Shade + '.shadowColor'),1,1,1,type = 'double3')
                mc.setAttr((Shade + '.hardwareColor'),0,1,0,type = 'double3')                
            if shaderType=='Lambert':
                mc.setAttr((Shade + '.shadeMode'),1) 
                mc.setAttr((Shade + '.color'),1,1,1,type = 'double3')                                                                   
    #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【通用】 【RGB信息导出】
    # author:韩虹
    #------------------------------#        
    def csl_RGBInfoExportTest(self):
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        if shotInfo[0] in ['csl','do5']:
            shader = mc.ls(mat=1)
            for shade in shader:
                if mc.nodeType(shade)!='aiUtility' and 'ArnoldIdp' not in shade and shade!='particleCloud1' and shade!='lambert1' and shade!='shaderGlow1':
                    print('a')
                    mc.error (shade+':'+u'该材质命名不正确，或者非aiUtility材质')
                else:
                    SGNodes = mc.listConnections(shade,d=1,type = 'shadingEngine')
                    if not SGNodes:
                        mc.error(u'===请清理无用材质===') 
    #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【通用】 【RGB信息导出】
    # author:韩虹
    #------------------------------#
    def csl_RGBInfoExport(self,id):
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        if shotInfo[0]=='csl' or shotInfo[0]=='do5':
            self.csl_RGBInfoExportTest()
        self.csl_ArnoldIdinfoDelete(id)               
        shader = mc.ls(mat=1)
        for shade in shader:
            if shade!='particleCloud1' and shade!='lambert1' and shade!='shaderGlow1':
                if('IdpR' in shade):
                    mc.select(shade)
                    self.ydRLayerRGBInfoExport(id,"R",1)
                elif('IdpG' in shade):
                    mc.select(shade)
                    self.ydRLayerRGBInfoExport(id,"G",1)
                elif('IdpB' in shade):
                    mc.select(shade)
                    self.ydRLayerRGBInfoExport(id,"B",1)                               
                elif('IdpM' in shade):
                    mc.select(shade)
                    self.ydRLayerRGBInfoExport(id,"M",1)             
                elif('IdpY' in shade):
                    mc.select(shade)
                    self.ydRLayerRGBInfoExport(id,"Y",1)               
                elif('IdpC' in shade):
                    mc.select(shade)
                    self.ydRLayerRGBInfoExport(id,"C",1)              
                elif('IdpK' in shade):
                    self.ydRLayerRGBInfoExport(id,"K",1)

    def csl_IDRenderCreat(self,objname,layername):
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refNamespace = refInfos[2][0]
        specialType = 0
        for ns in refNamespace:
            if '_' not in ns:
                continue
            if ns.split('_')[1][specialType] in ['c']:
                objname = ns.split('_')[1]
                layer=objname+'_'+layername
                if mc.objExists(ns + ':MSH_all'):
                    needMeshFull = mc.ls((ns + ':MSH_all'),l = 1)[0]
                    mc.select(clear=1) 
                    mc.select(needMeshFull)
                    mc.createRenderLayer(name = layer, noRecurse=1, makeCurrent=1)
        mc.setAttr("defaultRenderLayer.renderable", 0)  

    def csl_ChaIdCreat(self,LayerName='id01'):  
        id=self.csl_RGBObjectsConfig(LayerName, server = 1)        
        if id!=None:
        #csl_IDRenderCreat(objname,layername='id01')
            idColor=id[0]
            objSet=id[1]
            for i in range(len(idColor)):
                objs=objSet[i]
                for obj in objs:
                    objSets=''
                    if mc.nodeType(obj)=='mesh' and  re.search(('_.f'), obj)==None:
                        objSets=mc.listRelatives( obj, p=True,f=1 )[0]
                    else:
                        objSets=mc.ls(obj,l=1)
                    mc.select(objSets)
                    if idColor[i]==[1,0,0]:
                        self.ArnoldIDCreat(idpShader="ArnoldIdpR")
                    if idColor[i]==[0,1,0]:
                        self.ArnoldIDCreat(idpShader="ArnoldIdpG")
                    if idColor[i]==[0,0,1]:
                        self.ArnoldIDCreat(idpShader="ArnoldIdpB")                        
                    if idColor[i]==[0,0,0]:
                        self.ArnoldIDCreat(idpShader="ArnoldIdpM")
                    if idColor[i]==[1,1,0]:
                        self.ArnoldIDCreat(idpShader="ArnoldIdpY")
                    if idColor[i]==[0,1,1]:
                        self.ArnoldIDCreat(idpShader="ArnoldIdpC")                                        
                    if idColor[i]==[1,0,1]:
                        self.ArnoldIDCreat(idpShader="ArnoldIdpK")
        else:
            print('缺少id信息，请检查')

    def csl_IDRenderCreatAll(self,refInfos,objType,layername):
        refNamespace = refInfos[2][0]
        specialType = 0
        mc.select(clear=1)
        info=[] 
        for ns in refNamespace:
            if '_' not in ns:
                continue
            if ns.split('_')[1][specialType] in ['c']:
                objname = ns.split('_')[1]
                if mc.objExists(ns + ':MSH_all'):
                    needMeshFull = mc.ls((ns + ':MSH_all'),l = 1)[0]
                    info.append(needMeshFull)
        layer=objType+layername
        if info:
            mc.createRenderLayer(info,name = layer, noRecurse=1, makeCurrent=1)
            mc.editRenderLayerGlobals(currentRenderLayer=layer)
            mc.select(info)        
            self.csl_ChaIdCreat(layername)
        mc.setAttr("defaultRenderLayer.renderable", 0)  
 #导入参考       
    def csl_RefIm(self):
        refPath=mc.file(q=1,r=1)
        if len(refPath)!=0:
            for r in refPath:
                refRN=mc.file(r,q=1,rfn=1)
                if(mc.file(r,q=1,dr=1)):
                    mc.file(refRN,loadReference=1)
                mc.file(r,ir=1) 
#创建相应IDP层（角色，场景）               
#    def csl_IDRenderLayerCreatAll(self,type='cha'):
#        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
#        refNamespace = mc.namespaceInfo(listOnlyNamespaces=1)
#        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
#        self.csl_RefIm()
#        mel.eval('source "zzjUtilityTools.mel";lighting_DeleteUnusedNode()')    
#        specialType = 0
#        mc.select(clear=1) 
#        objselect=[]
#        objs=[]
#        if type=='cha':
#            for ns in refNamespace:
#                if '_' not in ns:
#                    continue
#                if ns.split('_')[1][specialType] in ['c']:
#                    objname = ns.split('_')[1]
#                    objs.append(objname)
#                    if mc.objExists(ns + ':MSH_all'):
#                        needMeshFull = mc.ls((ns + ':MSH_all'),l = 1)[0]
#                        objselect.append(needMeshFull)
#            mc.select(clear=1)
#            mc.select(objselect)        
#            layer='cha_id01'
#            mc.createRenderLayer(name = layer, noRecurse=1, makeCurrent=1)
#            self.csl_RGBApply('id01')
#            mc.select(clear=1)
#            mc.select(objselect)        
#            layer='cha_id02'
#            mc.createRenderLayer(name = layer, noRecurse=1, makeCurrent=1)
#            self.csl_RGBApply('id02')
#            mc.select(clear=1)
#            mc.select(objselect)        
#            layer='cha_id03'
#            mc.createRenderLayer(name = layer, noRecurse=1, makeCurrent=1)
#            self.csl_RGBApply('id03') 
#        if type=='env':
#            for ns in refNamespace:
#                if '_' not in ns:
#                    continue
#                if ns.split('_')[1][specialType] in ['s', 'S']:
#                    objname = ns.split('_')[1]
#                    objs.append(objname)
#                    if mc.objExists(ns + ':MSH_all'):
#                        needMeshFull = mc.ls((ns + ':MSH_all'),l = 1)[0]
#                        objselect.append(needMeshFull)
#            mc.select(clear=1)
#            mc.select(objselect)        
#            layer='env_id11'
#            mc.createRenderLayer(name = layer, noRecurse=1, makeCurrent=1)
#            self.csl_RGBApply('id11')
#            mc.select(clear=1)
#            mc.select(objselect)        
#            layer='env_id12'
#            mc.createRenderLayer(name = layer, noRecurse=1, makeCurrent=1)
#            self.csl_RGBApply('id12')
#            mc.select(clear=1)
#            mc.select(objselect)        
#            layer='env_id13'
#            mc.createRenderLayer(name = layer, noRecurse=1, makeCurrent=1)
#            self.csl_RGBApply('id13')                   
#     
#        mc.setAttr("defaultRenderLayer.renderable", 0)
#        (u'===============!!!End 【%s】!!!===============' % (u'IDP已经创建完成'))
#        result = [objselect,objs]
#        return result         
    def csl_IDRenderLayerCreatAll(self,type='chr',ref=1):
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refNamespace = mc.namespaceInfo(listOnlyNamespaces=1)
        specialType=0
        if mc.objExists('CAM'):
            refNamespace .remove('CAM')
        if mc.objExists('UI'):
            refNamespace .remove('UI')  
        if mc.objExists('shared'):
            refNamespace .remove('shared')              
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        if ref==1:
            self.csl_RefIm()
        mel.eval('source "zzjUtilityTools.mel";lighting_DeleteUnusedNode()')    
        specialType = 0
        mc.select(clear=1) 
        objselect=[]
        objs=[]
        if type=='chr':
            for ns in refNamespace:
                if '_' not in ns:
                    continue
                if ns.split('_')[1][specialType] in ['c']:
                    objname = ns.split('_')[1]
                    if mc.objExists(ns + ':MSH_all'):
                        needMeshFull = mc.ls((ns + ':MSH_all'),l = 1)[0]
                        for i in range(10):
                            idserpath=serverPath+'data/RLayerInfo/RGB/id0'+str(i)+'/'
                            if idserpath.split('/')[-2] in mc.getFileList(folder=serverPath+'data/RLayerInfo/RGB/')and objname in mc.getFileList(folder=idserpath):
                                idLayer='chr_id0'+str(i)
                                if mc.objExists(idLayer):
                                    mc.editRenderLayerMembers(idLayer,needMeshFull,noRecurse=0)
                                    mc.editRenderLayerGlobals(currentRenderLayer=idLayer)
                                else:
                                    mc.createRenderLayer(needMeshFull,name=idLayer, noRecurse=1, makeCurrent=1)
                                comm='self.csl_RGBApply("id0'+str(i)+ '")' 
                                mc.select(needMeshFull)
                                eval(comm)
                            else:
                                pass
                                                    
        if type=='set':
            for ns in refNamespace:
                if '_' not in ns:
                    continue
                if ns.split('_')[1][specialType] in ['s', 'S']:
                    objname = ns.split('_')[1]
                    if mc.objExists(ns + ':MODEL'):
                        needMeshFull = mc.ls((ns + ':MODEL'),l = 1)[0]
                        for i in range(10):
                            idserpath=serverPath+'data/RLayerInfo/RGB/id1'+str(i)+'/'
                            if idserpath.split('/')[-2] in mc.getFileList(folder=serverPath+'data/RLayerInfo/RGB/')and objname in mc.getFileList(folder=idserpath):
                                idLayer='set_id1'+str(i)
                                if mc.objExists(idLayer):
                                    mc.editRenderLayerMembers(idLayer,needMeshFull,noRecurse=0)
                                    mc.editRenderLayerGlobals(currentRenderLayer=idLayer)
                                else:
                                    mc.createRenderLayer(needMeshFull,name=idLayer, noRecurse=1, makeCurrent=1)
                                comm='self.csl_RGBApply("id1'+str(i)+ '")' 
                                mc.select(needMeshFull)
                                eval(comm)
                            else:
                                pass                                
        mc.setAttr("defaultRenderLayer.renderable", 0)
        mc.editRenderLayerGlobals(currentRenderLayer="defaultRenderLayer")
        return 0

    def csl_RGBObjectsConfig(self, LayerName = 'id01', specialType = 0 , server = 1,cache=0 ):
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
            if ns.split('_')[1][specialType] in ['c','p','s']:
                assetName = ns.split('_')[1]
                allInfos = self.csl_RGBInfoImport(LayerName,assetName,server)
                for info in allInfos:
                    # color
                    shaderColor.append([float(info[0].split('|')[0]),float(info[0].split('|')[1]),float(info[0].split('|')[2])])
                    # 处理meshes
                    needMeshes = []
                    for k in range(len(info)):
                        if k == 0:
                            continue
                        if '|' not in info[k]:
                            if mc.objExists(ns + ':' + info[k]):
                                needMeshFull = mc.ls(( ns + ':' + info[k]),l = 1)[0]
                                needMeshes.append(needMeshFull)
                        else:
                            # 全面启动长名
                            needMesh = info[k].replace('|',('|' + ns + ':'))
                            if not mc.ls('*' + needMesh):
                                continue
                            needMeshFull = mc.ls(('*' + needMesh),l = 1)[0]
                            needMeshes.append(needMeshFull)
                    needMeshes = mc.ls(needMeshes , l = 1)
                    shaderMeshes.append(needMeshes)
        result = [shaderColor,shaderMeshes]
        return result   
        
    def csl_RGBInfoImport(self,LayerName = 'id01', assetName = '' ,server = 0):
        # 路径
        if server:
            serverPath = sk_infoConfig.sk_infoConfig().checkLayerInfoServerPath('RGB', LayerName)
            filePath = serverPath + assetName + '\\' 
        else:
            localPath = sk_infoConfig.sk_infoConfig().checkLayerInfoLocalPath('RGB', LayerName)
            filePath = localPath + assetName + '\\' 

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
        
    def csl_RGBApply(self,LayerName ='id01',specialType = 0):
        namespace=mc.namespaceInfo(listOnlyNamespaces=1)
        for ns in namespace:
            if '_' not in ns:
                continue
            if ns.split('_')[1][specialType] in ['c','p']:
                objname = ns.split('_')[1]
                needMeshFull=''
                if mc.objExists(ns + ':MSH_all'):
                    needMeshFull = mc.ls((ns + ':MSH_all'),l = 1)[0]
                allInfos = self.csl_RGBInfoImport(LayerName,objname,server=1)
                if allInfos:
                    self.csl_ChaIdCreat(LayerName)
                else:
                    if needMeshFull:
                        mc.select(needMeshFull)
                        self.ArnoldIDCreat(idpShader="ArnoldIdpM")
            if ns.split('_')[1][specialType] in ['s', 'S']:
                objname = ns.split('_')[1]
                if mc.objExists(ns + ':MODEL'):
                    needMeshFull = mc.ls((ns + ':MODEL'),l = 1)[0]
                allInfos = self.csl_RGBInfoImport(LayerName,objname,server=1)
                if allInfos:
                    self.csl_ChaIdCreat(LayerName)
                else:
                    mc.select(needMeshFull)
                    self.ArnoldIDCreat(idpShader="ArnoldIdpM")
        return 0     

    def csl_ArnoldmeshInfo(self,meshtype='s'):
        meshs=mc.ls(type='mesh',l=1)
        meshList=[]
        namespaces=mc.namespaceInfo(listOnlyNamespaces=1)
        for i in range(len(meshs)):
            for j in range(len(namespaces)) :
                if namespaces[j] in meshs[i] and namespaces[j].split('_')[1][0]==meshtype:
                    meshP=mc.listRelatives(meshs[i],p=1,f=1)
                    if meshP:
                        meshList.append(meshP[0])
        return meshList

#读取smooth信息，并设置smooth 
    def csl_FinalSmoothSet(self,smoothInfo='smooth_2',renderusing='arnold',tangents=1):
        Sets=mc.ls(set=1)
        smoothNum=int(smoothInfo.split('_')[-1])
        for set in Sets:
            if re.search(smoothInfo,set)!=None:
                objs=mc.sets(set,q=1)
                if objs:
                    for obj in objs:
                        objfull=mc.ls(obj,l=1)
                        meshs=mc.listRelatives(objfull,s=1,f=1,type='mesh')
                        if meshs:
                            for mesh in meshs:
                                if smoothNum==0:
                                     mc.setAttr((mesh+'.aiSubdivType'),0)
                                else:                             
                                    mc.setAttr((mesh+'.aiSubdivType'),1)
                                    mc.setAttr((mesh+'.aiSubdivIterations'),smoothNum)
                                    if tangents==1:
                                        mc.setAttr((mesh+'.aiSubdivSmoothDerivs'),1)
                                    if tangents==0:
                                        mc.setAttr((mesh+'.aiSubdivSmoothDerivs'),0)                                                                                  
                                    
        print(u'===============!!!已经设置 【%s】!!!===============' % smoothInfo)
        return 0 

    def csl_SmoothSet(self):
        self.csl_FinalSmoothSet(smoothInfo='smooth_0',renderusing='arnold',tangents=0)
        self.csl_FinalSmoothSet(smoothInfo='smooth_1',renderusing='arnold',tangents=0) 
        self.csl_FinalSmoothSet(smoothInfo='smooth_2',renderusing='arnold',tangents=0)
        return 0
                                                          
 

    # 读文件
    def csl_ArnoldcheckFileRead(self, path):
        print(u'>>>>>>[read]')
        print(path)
        txt = open(path, 'r');
        try:
            fileContent = txt.readlines()
            print('Loading........')
        finally:
            txt.close()
        result = []
        for info in fileContent:
            if '\r\n' in info:
                result.append(info.split('\r\n')[0])
            else:
                result.append(info)
        return result  

#删除id信息
    def csl_ArnoldIdinfoDelete(self,id='id01'):
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        idserpath=serverPath+'data/RLayerInfo/RGB/'+id+'/'
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        if  shotInfo[1] in mc.getFileList(folder=idserpath):
            hispath=idserpath+shotInfo[1]+'/his'
            mc.sysFile(hispath, makeDir=True)
            mc.sysFile(hispath,copy=shotInfo[1])
            mc.sysFile((idserpath+shotInfo[1]),delete=1)
        return 0    
    #--------------------------#
    # 自sk_renderLayerCore
    # 分层信息输出
    # 数据结构：第一行，字符串，|分割三个通道信息；从第二行开始，每行一个mesh
    def ydRLayerRGBInfoExport(self, LayerName='FullBody', exportType='all', update = 0,openIt = False):
        localPath = sk_infoConfig.sk_infoConfig().checkLayerInfoLocalPath('RGB', LayerName)
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        import os
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
        
                                                                                                                                                                        