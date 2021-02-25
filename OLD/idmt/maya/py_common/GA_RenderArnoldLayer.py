# -*- coding: utf-8 -*-

import maya.cmds as mc
import maya.mel as mel
import pymel.core as pm
import os

from idmt.maya.commonCore.core_renderLayer import sk_renderLayerCore
reload(sk_renderLayerCore)



from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
reload(sk_referenceConfig)

from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
reload(sk_infoConfig)

from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools
reload(sk_sceneTools)

import re
class GA_RenderArnold(object):
    def __init__(self):
        pass
    #----------------------------------------------------------------------------------------------------------#      #----------------------------------------------------------#
        #------------------------------#
    # 【渲染】【Arnold渲染工具】
    #  Author  : 韩虹
    #  Data    : 2017_04_18
    #------------------------------#

    def RenderArnoldUI(self):
    # 窗口
        if mc.window('GA_RenderArnold', exists=True):
            mc.deleteUI('GA_RenderArnold')
        mc.window('GA_RenderArnold', title=u'Arnold 渲染面板',
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
            image='//file-cluster/GDC/Resource/Support/Maya/icons/GA/arnold.png')
        mc.button(label=u'创建Project', bgc=[0, 0, 0.0], height=50, command='mel.eval(\'zwSetProject\')')
        mc.button(label=u'另存文件', bgc=[0, 0, 0.0], height=50, command='mel.eval(\'source \"//file-cluster/GDC/Resource/Support/Maya/projects/ShunLiu/CSL_RenderToolsMR.mel\";CSL_GASavefile();\')')
        mc.button(label=u'创建AOV', bgc=[0, 0, 0.0], height=50, command='mc.tabLayout("tabArnold", edit=True, selectTabIndex=2)')
        mc.button(label=u'提交网渲', bgc=[0, 0, 0.0], height=50, command='mel.eval(\'source \"//file-cluster/GDC/Resource/Support/Maya/2013/MusterCheckin.mel\";MusterCheckin();\')')
        mc.button(label=u'广告位招租', bgc=[0.13, 0.15, 0.25], height=120, command='')        
        mc.setParent('..')
         # AOV面板
        child2 = mc.columnLayout(adjustableColumn=True)
        mc.frameLayout(label='Select', bgc=[0, 0, 0.0], borderStyle='in', cll=1,cl=0)
        mc.rowColumnLayout(numberOfColumns=3)
        collectionocc = mc.radioCollection()
        # occ
        occset = mc.checkBox('GAcheckAO', label='AO', visible=1, v=1,
                             bgc=[0.13, 0.15, 0.25], height=30, width=130)
        mc.button(label=u'创建', bgc=[
                  0, 0, 0.0], width=110, height=30, command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().GA_ArnoldAOVCreat("AO")')
        mc.button(
            label=u'删除', bgc=[0, 0, 0.0], width=110, height=30, command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().ArnoldAOVDeleteD("AO")')
        collectionnormal = mc.radioCollection()
        # N
        normalset = mc.checkBox('GAcheckN',label='N', visible=1, v=1,
                             bgc=[0.13, 0.15, 0.25], height=30, width=130)
        mc.button(label=u'创建', bgc=[
                  0, 0, 0.0], width=110, height=30, command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().GA_ArnoldAOVCreat("N")')
        mc.button(
            label=u'删除', bgc=[0, 0, 0.0], width=110, height=30, command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().ArnoldAOVDeleteD("N")')
        collectionfre = mc.radioCollection()
        # P
        normalset = mc.checkBox('GAcheckP',label='P', visible=1, v=1,
                             bgc=[0.13, 0.15, 0.25], height=30, width=130)
        mc.button(label=u'创建', bgc=[
                  0, 0, 0.0], width=110, height=30, command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().GA_ArnoldAOVCreat("P")')
        mc.button(
            label=u'删除', bgc=[0, 0, 0.0], width=110, height=30, command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().ArnoldAOVDeleteD("P")')
        collectionfre = mc.radioCollection()

        # fre
        freset = mc.checkBox('GAcheckFre',label='Fre', visible=1, v=1,
                             bgc=[0.13, 0.15, 0.25], height=30, width=130)
        mc.button(label=u'创建', bgc=[
                  0, 0, 0.0], width=110, height=30, command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().GA_ArnoldAOVCreat("Fre")')
        mc.button(
            label=u'删除', bgc=[0, 0, 0.0], width=110, height=30, command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().ArnoldAOVDeleteD("Fre")')
        collectionkey = mc.radioCollection()

        # Z
        normalset = mc.checkBox('GAcheckZ',label='Z', visible=1, v=1,
                             bgc=[0.13, 0.15, 0.25], height=30, width=130)
        mc.button(label=u'创建', bgc=[
                  0, 0, 0.0], width=110, height=30, command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().GA_ArnoldAOVCreat("Z")')
        mc.button(
            label=u'删除', bgc=[0, 0, 0.0], width=110, height=30, command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().ArnoldAOVDeleteD("Z")')
        collectionfre = mc.radioCollection()

        SSSset = mc.checkBox('GAcheckSSS',label='SSS', visible=1,
                             v=1, bgc=[0.13, 0.15, 0.25], height=30, width=130)
        mc.button(label=u'创建', bgc=[
                  0, 0, 0.0], width=110, height=30, command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().GA_ArnoldAOVCreat("sss")')
        mc.button(
            label=u'删除', bgc=[0, 0, 0.0], width=110, height=30, command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().ArnoldAOVDeleteD("sss")')
                
        collectionzdp = mc.radioCollection()        

        # zdepth
        zdepthset = mc.checkBox('GAcheckZdp',label='Zdp', visible=1, v=1,
                             bgc=[0.13, 0.15, 0.25], height=30, width=130)
        mc.button(label=u'创建', bgc=[
                  0, 0, 0.0], width=110, height=30, command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().GA_ArnoldAOVCreat("Zdp")')
        mc.button(
            label=u'删除', bgc=[0, 0, 0.0], width=110, height=30, command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().ArnoldAOVDeleteD("Zdp")')
        # light_all
        shadowset = mc.checkBox('GAchecklight_all',label='light_all', visible=1,
                             v=1, bgc=[0.13, 0.15, 0.25], height=30, width=130)
        mc.button(label=u'创建', bgc=[
                  0, 0, 0.0], width=110, height=30, command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().GA_ArnoldAOVCreat("light_all")')
        mc.button(
            label=u'删除', bgc=[0, 0, 0.0], width=110, height=30, command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().ArnoldAOVDeleteD("light_all")')
        collectionzdp = mc.radioCollection()
        # lightgroup
        shadowset = mc.checkBox('GAchecklight_group',label='lightgroup', visible=1,
                             v=1, bgc=[0.13, 0.15, 0.25], height=30, width=130)
        mc.button(label=u'创建', bgc=[
                  0, 0, 0.0], width=110, height=30, command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().GA_speAOVCreat("light_group")')
        mc.button(
            label=u'删除', bgc=[0, 0, 0.0], width=110, height=30, command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().ArnoldAOVDeleteD("light_group")')
        collectionzdp = mc.radioCollection()

        # meshID
        shadowset = mc.checkBox('GAcheckmeshID',label='meshID', visible=1,
                             v=1, bgc=[0.13, 0.15, 0.25], height=30, width=130)
        mc.button(label=u'创建', bgc=[
                  0, 0, 0.0], width=110, height=30, command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().GA_speAOVCreat("meshID")')
        mc.button(
            label=u'删除', bgc=[0, 0, 0.0], width=110, height=30, command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().ArnoldAOVDeleteD("meshID")')
        collectionzdp = mc.radioCollection()

        # direct_diffuse
        shadowset = mc.checkBox('GAcheckdirect_diffuse',label='direct_diffuse', visible=1,
                             v=1, bgc=[0.13, 0.15, 0.25], height=30, width=130)
        mc.button(label=u'创建', bgc=[
                  0, 0, 0.0], width=110, height=30, command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().GA_ArnoldAOVCreat("direct_diffuse")')
        mc.button(
            label=u'删除', bgc=[0, 0, 0.0], width=110, height=30, command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().ArnoldAOVDeleteD("direct_diffuse")')
        collectionzdp = mc.radioCollection()

        # direct_specular
        shadowset = mc.checkBox('GAcheckdirect_specular',label='direct_specular', visible=1,
                             v=1, bgc=[0.13, 0.15, 0.25], height=30, width=130)
        mc.button(label=u'创建', bgc=[
                  0, 0, 0.0], width=110, height=30, command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().GA_ArnoldAOVCreat("direct_specular")')
        mc.button(
            label=u'删除', bgc=[0, 0, 0.0], width=110, height=30, command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().ArnoldAOVDeleteD("direct_specular")')
        collectionzdp = mc.radioCollection()

        # indirect_diffuse
        shadowset = mc.checkBox('GAcheckindirect_diffuse',label='indirect_diffuse', visible=1,
                             v=1, bgc=[0.13, 0.15, 0.25], height=30, width=130)
        mc.button(label=u'创建', bgc=[
                  0, 0, 0.0], width=110, height=30, command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().GA_ArnoldAOVCreat("indirect_diffuse")')
        mc.button(
            label=u'删除', bgc=[0, 0, 0.0], width=110, height=30, command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().ArnoldAOVDeleteD("indirect_diffuse")')
        collectionzdp = mc.radioCollection()
        # indirect_specular
        shadowset = mc.checkBox('GAcheckindirect_specular',label='indirect_specular', visible=1,
                             v=1, bgc=[0.13, 0.15, 0.25], height=30, width=130)
        mc.button(label=u'创建', bgc=[
                  0, 0, 0.0], width=110, height=30, command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().GA_ArnoldAOVCreat("indirect_specular")')
        mc.button(
            label=u'删除', bgc=[0, 0, 0.0], width=110, height=30, command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().ArnoldAOVDeleteD("indirect_specular")')
        collectionzdp = mc.radioCollection()
        # emission
        shadowset = mc.checkBox('GAcheckemission',label='emission', visible=1,
                             v=1, bgc=[0.13, 0.15, 0.25], height=30, width=130)
        mc.button(label=u'创建', bgc=[
                  0, 0, 0.0], width=110, height=30, command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().GA_ArnoldAOVCreat("emission")')
        mc.button(
            label=u'删除', bgc=[0, 0, 0.0], width=110, height=30, command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().ArnoldAOVDeleteD("emission")')
        collectionzdp = mc.radioCollection()
        # reflection
        shadowset = mc.checkBox('GAcheckreflection',label='reflection', visible=1,
                             v=1, bgc=[0.13, 0.15, 0.25], height=30, width=130)
        mc.button(label=u'创建', bgc=[
                  0, 0, 0.0], width=110, height=30, command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().GA_ArnoldAOVCreat("reflection")')
        mc.button(
            label=u'删除', bgc=[0, 0, 0.0], width=110, height=30, command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().ArnoldAOVDeleteD("reflection")')
        collectionzdp = mc.radioCollection()
        # refraction
        shadowset = mc.checkBox('GAcheckrefraction',label='refraction', visible=1,
                             v=1, bgc=[0.13, 0.15, 0.25], height=30, width=130)
        mc.button(label=u'创建', bgc=[
                  0, 0, 0.0], width=110, height=30, command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().GA_ArnoldAOVCreat("refraction")')
        mc.button(
            label=u'删除', bgc=[0, 0, 0.0], width=110, height=30, command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().ArnoldAOVDeleteD("refraction")')
        collectionzdp = mc.radioCollection()
        # Shadow
        shadowset = mc.checkBox('GAcheckShadow',label='Shadow', visible=1,
                             v=0, bgc=[0.13, 0.15, 0.25], height=30, width=130)
        mc.button(label=u'创建', bgc=[
                  0, 0, 0.0], width=110, height=30, command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().GA_ArnoldAOVCreat("Shadow")')
        mc.button(
            label=u'删除', bgc=[0, 0, 0.0], width=110, height=30, command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().ArnoldAOVDeleteD("Shadow")')
        collectionzdp = mc.radioCollection()

        # motionvector
        zdepthset = mc.checkBox('GAcheckmotionvector',label='motionvector', visible=1, v=0,
                             bgc=[0.13, 0.15, 0.25], height=30, width=130)
        mc.button(label=u'创建', bgc=[
                  0, 0, 0.0], width=110, height=30, command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().GA_ArnoldAOVCreat("motionvector")')
        mc.button(
            label=u'删除', bgc=[0, 0, 0.0], width=110, height=30, command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().ArnoldAOVDeleteD("motionvector")')

        collectionid01 = mc.radioCollection()
        mc.setParent('..')
        mc.setParent('..')  
        # 一键式创建AOV层
        mc.frameLayout(label=u'一键式创建（删除）工具', bgc=[0, 0, 0.0], borderStyle='in',cll=1,cl=0)
        mc.rowColumnLayout(numberOfColumns=3)
        mc.button(label=u'创建渲染层', width=130, height=30,
                  bgc=[0.13, 0.15, 0.25], command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().GA_ArnoldRendererLayerCreat()')
        mc.button(label=u'删除所有AOV', width=110,
                  height=30, bgc=[0, 0, 0.0], command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().ArnoldALLDelete(nodetype="aiAOV")')
        mc.button(label=u'删除所有渲染层', width=110,
                  height=30, bgc=[0, 0, 0.0], command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().ArnoldALLDelete(nodetype="renderLayer")')
        mc.setParent('..')
        mc.setParent('..')
        mc.frameLayout(label=u'常用工具', bgc=[0, 0, 0.0], borderStyle='in',cll=1,cl=0)
        mc.rowColumnLayout(numberOfColumns=2)
        mc.button(label=u'Arnold渲染设置', width=180, height=30,
                  bgc=[0.13, 0.6, 0.25], command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().GA_ArnldSetting("Yak",2)')
        mc.button(label=u'smooth', width=180, height=30,
                  bgc=[0, 0, 0.0], command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().csl_SmoothSet()')
        mc.setParent('..')
        mc.setParent('..')        
        mc.setParent('..')                
        # 渲染常用工具组
        child3 = mc.columnLayout(adjustableColumn=True)
        mc.frameLayout(label=u'IDP输出工具', bgc=[0, 0, 0.0], borderStyle='etchedIn', cll=1,cl=1)
        mc.rowColumnLayout(numberOfColumns=4)
        mc.button(label=u'输出角色id01',width=90,height=30,bgc=[0.13, 0.15, 0.25],command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().csl_RGBInfoExport(id=\'id01\')')
        mc.button(label=u'输出角色id02',width=90,height=30,bgc=[0.13, 0.15, 0.25],command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().csl_RGBInfoExport(id=\'id02\')')
        mc.button(label=u'输出角色id03',width=90,height=30,bgc=[0.13, 0.15, 0.25],command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().csl_RGBInfoExport(id=\'id03\')') 
        mc.button(label=u'输出角色id04',width=90,height=30,bgc=[0.13, 0.15, 0.25],command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().csl_RGBInfoExport(id=\'id04\')')                 
        mc.button(label=u'输出场景id11',width=90,height=30,bgc=[0.0, 0.0, 0.0],command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().csl_RGBInfoExport(id=\'id11\')')
        mc.button(label=u'输出场景id12',width=90,height=30,bgc=[0.0, 0.0, 0.0],command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().csl_RGBInfoExport(id=\'id12\')')
        mc.button(label=u'输出场景id13',width=90,height=30,bgc=[0.0, 0.0, 0.0],command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().csl_RGBInfoExport(id=\'id13\')')        
        mc.button(label=u'输出场景id14',width=90,height=30,bgc=[0.0, 0.0, 0.0],command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().csl_RGBInfoExport(id=\'id14\')')         
        mc.button(label=u'ID材质输出前检测',width=90,height=30,bgc=[0.1, 0.6, 0.25],command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().csl_RGBInfoExportTest()')
        mc.setParent('..')
        mc.setParent('..')        
        #idp材质工具    
        mc.frameLayout(label=u'IDP材质工具', bgc=[0, 0, 0.0], borderStyle='in', cll=1,cl=1)
        mc.rowColumnLayout(numberOfColumns=4) 
        mc.button(label=u'R',width=90,height=30,bgc=[1,0,0],command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().ArnoldIDCreat(idpShader="ArnoldIdpR")')
        mc.button(label=u'G',width=90,height=30,bgc=[0,1,0],command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().ArnoldIDCreat(idpShader="ArnoldIdpG")')
        mc.button(label=u'B',width=90,height=30,bgc=[0,0,1],command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().ArnoldIDCreat(idpShader="ArnoldIdpB")')
        mc.button(label=u'M',width=90,height=30,bgc=[0,0,0],command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().ArnoldIDCreat(idpShader="ArnoldIdpM")')
        mc.button(label=u'A',width=90,height=30,bgc=[1,1,1],command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().ArnoldIDCreat(idpShader="ArnoldIdpA")')
        #mc.button(label=u'Y',width=90,height=30,bgc=[1,1,0],command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().ArnoldIDCreat(idpShader="ArnoldIdpY")')
        #mc.button(label=u'C',width=90,height=30,bgc=[0,1,1],command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().ArnoldIDCreat(idpShader="ArnoldIdpC")')
        #mc.button(label=u'K',width=90,height=30,bgc=[1,0,1],command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().ArnoldIDCreat(idpShader="ArnoldIdpK")')
        mc.setParent('..')
        mc.setParent('..')

        #置换专用材质工具
        mc.frameLayout(label=u'置换专用材质工具', bgc=[0, 0, 0.0], borderStyle='in', cll=1,cl=1)
        mc.rowColumnLayout(numberOfColumns=4)
        mc.button(label=u'R',width=90,height=30,bgc=[1,0,0],command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().P5_ArnoldDisMatCreat(idpShader="ArnoldIdpR01")')
        mc.button(label=u'G',width=90,height=30,bgc=[0,1,0],command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().P5_ArnoldDisMatCreat(idpShader="ArnoldIdpG")')
        mc.button(label=u'B',width=90,height=30,bgc=[0,0,1],command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().P5_ArnoldDisMatCreat(idpShader="ArnoldIdpB")')
        mc.button(label=u'M',width=90,height=30,bgc=[0,0,0],command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().P5_ArnoldDisMatCreat(idpShader="ArnoldIdpM")')
        mc.button(label=u'Y',width=90,height=30,bgc=[1,1,0],command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().P5_ArnoldDisMatCreat(idpShader="ArnoldIdpY")')
        mc.button(label=u'C',width=90,height=30,bgc=[0,1,1],command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().P5_ArnoldDisMatCreat(idpShader="ArnoldIdpC")')
        mc.button(label=u'K',width=90,height=30,bgc=[1,0,1],command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().P5_ArnoldDisMatCreat(idpShader="ArnoldIdpK")')
        mc.button(label=u'Lam',width=90,height=30,bgc=[0.5,0.5,0.5],command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().P5_ArnoldDisMatCreat(idpShader="ArnoldLambert")')
        mc.button(label=u'Occ',width=90,height=30,bgc=[1,1,1],command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().P5_ArnoldDisMatCreat(idpShader="ArnoldOcc")')
        mc.button(label=u'Normal',width=90,height=30,bgc=[0.4,0.55,0.9],command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().P5_ArnoldDisMatCreat(idpShader="ArnoldNormal")')
        mc.setParent('..')
        mc.setParent('..')

        #ID属性添加工具
        mc.frameLayout(label=u'角色ID属性工具', bgc=[0, 0, 0], borderStyle='etchedIn', cll=1,cl=0)
        mc.rowColumnLayout(numberOfColumns=5)
        mc.iconTextCheckBox(al='left', bgc=[0.2, 0.3, 0.1],olc=[0, 1 ,0],width=80, height=30,style='iconAndTextVertical', image1='plane.png', label='chrID01' )
        mc.button(label=u'R', width=50, height=30, bgc=[1, 0, 0], command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().GA_ArnoldIDSet("set","R","chrID01")')
        mc.button(label=u'G',width=50, height=30,bgc=[0, 1, 0.0], command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().GA_ArnoldIDSet("set","G","chrID01")')
        mc.button(label=u'B',width=50, height=30,bgc=[0, 0, 1], command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().GA_ArnoldIDSet("set","B","chrID01")')
        mc.button(label=u'delete',width=80, height=30,bgc=[0, 0, 0], command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().GA_ArnoldIDSet("del","","chrID01")')
        #chrID02
        mc.iconTextCheckBox(al='left', bgc=[0.2, 0.3, 0.1],olc=[0, 1 ,0],width=80, height=30,style='iconAndTextVertical', image1='plane.png', label='chrID02' )
        mc.button(label=u'R', width=50, height=30, bgc=[1, 0, 0], command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().GA_ArnoldIDSet("set","R","chrID02")')
        mc.button(label=u'G',width=50, height=30,bgc=[0, 1, 0.0], command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().GA_ArnoldIDSet("set","G","chrID02")')
        mc.button(label=u'B',width=50, height=30,bgc=[0, 0, 1], command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().GA_ArnoldIDSet("set","B","chrID02")')
        mc.button(label=u'delete',width=80, height=30,bgc=[0, 0, 0], command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().GA_ArnoldIDSet("del","","chrID02")')        

        #chrID03
        mc.iconTextCheckBox(al='left', bgc=[0.2, 0.3, 0.1],olc=[0, 1 ,0],width=80, height=30,style='iconAndTextVertical', image1='plane.png', label='chrID03' )
        mc.button(label=u'R', width=50, height=30, bgc=[1, 0, 0], command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().GA_ArnoldIDSet("set","R","chrID03")')
        mc.button(label=u'G',width=50, height=30,bgc=[0, 1, 0.0], command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().GA_ArnoldIDSet("set","G","chrID03")')
        mc.button(label=u'B',width=50, height=30,bgc=[0, 0, 1], command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().GA_ArnoldIDSet("set","B","chrID03")')
        mc.button(label=u'delete',width=80, height=30,bgc=[0, 0, 0], command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().GA_ArnoldIDSet("del","","chrID03")')  

        #chrID04
        mc.iconTextCheckBox(al='left', bgc=[0.2, 0.3, 0.1],olc=[0, 1 ,0],width=80, height=30,style='iconAndTextVertical', image1='plane.png', label='chrID04' )
        mc.button(label=u'R', width=50, height=30, bgc=[1, 0, 0], command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().GA_ArnoldIDSet("set","R","chrID04")')
        mc.button(label=u'G',width=50, height=30,bgc=[0, 1, 0.0], command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().GA_ArnoldIDSet("set","G","chrID04")')
        mc.button(label=u'B',width=50, height=30,bgc=[0, 0, 1], command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().GA_ArnoldIDSet("set","B","chrID04")')
        mc.button(label=u'delete',width=80, height=30,bgc=[0, 0, 0], command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().GA_ArnoldIDSet("del","","chrID04")')  
        mc.setParent('..')
        mc.setParent('..')
        #setID01
        mc.frameLayout(label=u'场景ID属性工具', bgc=[0, 0, 0], borderStyle='etchedIn', cll=1,cl=0)
        mc.rowColumnLayout(numberOfColumns=5)
        mc.iconTextCheckBox(al='left', bgc=[0.13, 0.15, 0.25],olc=[0, 1 ,0],width=80, height=30,style='iconAndTextVertical', image1='plane.png', label='setID01' )
        mc.button(label=u'R', width=50, height=30, bgc=[1, 0, 0], command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().GA_ArnoldIDSet("set","R","setID01")')
        mc.button(label=u'G',width=50, height=30,bgc=[0, 1, 0.0], command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().GA_ArnoldIDSet("set","G","setID01")')
        mc.button(label=u'B',width=50, height=30,bgc=[0, 0, 1], command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().GA_ArnoldIDSet("set","B","setID01")')
        mc.button(label=u'delete',width=80, height=30,bgc=[0, 0, 0], command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().GA_ArnoldIDSet("del","","setID01")')
        #setID02
        mc.iconTextCheckBox(al='left', bgc=[0.13, 0.15, 0.25],olc=[0, 1 ,0],width=80, height=30,style='iconAndTextVertical', image1='plane.png', label='setID02' )
        mc.button(label=u'R', width=50, height=30, bgc=[1, 0, 0], command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().GA_ArnoldIDSet("set","R","setID02")')
        mc.button(label=u'G',width=50, height=30,bgc=[0, 1, 0.0], command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().GA_ArnoldIDSet("set","G","setID02")')
        mc.button(label=u'B',width=50, height=30,bgc=[0, 0, 1], command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().GA_ArnoldIDSet("set","B","setID02")')
        mc.button(label=u'delete',width=80, height=30,bgc=[0, 0, 0], command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().GA_ArnoldIDSet("del","","setID02")')  
        #setID03
        mc.iconTextCheckBox(al='left', bgc=[0.13, 0.15, 0.25],olc=[0, 1 ,0],width=80, height=30,style='iconAndTextVertical', image1='plane.png', label='setID03' )
        mc.button(label=u'R', width=50, height=30, bgc=[1, 0, 0], command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().GA_ArnoldIDSet("set","R","setID03")')
        mc.button(label=u'G',width=50, height=30,bgc=[0, 1, 0.0], command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().GA_ArnoldIDSet("set","G","setID03")')
        mc.button(label=u'B',width=50, height=30,bgc=[0, 0, 1], command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().GA_ArnoldIDSet("set","B","setID03")')
        mc.button(label=u'delete',width=80, height=30,bgc=[0, 0, 0], command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().GA_ArnoldIDSet("del","","setID03")')
        #setID04
        mc.iconTextCheckBox(al='left', bgc=[0.13, 0.15, 0.25],olc=[0, 1 ,0],width=80, height=30,style='iconAndTextVertical', image1='plane.png', label='setID04' )
        mc.button(label=u'R', width=50, height=30, bgc=[1, 0, 0], command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().GA_ArnoldIDSet("set","R","setID04")')
        mc.button(label=u'G',width=50, height=30,bgc=[0, 1, 0.0], command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().GA_ArnoldIDSet("set","G","setID04")')
        mc.button(label=u'B',width=50, height=30,bgc=[0, 0, 1], command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().GA_ArnoldIDSet("set","B","setID04")')
        mc.button(label=u'delete',width=80, height=30,bgc=[0, 0, 0], command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().GA_ArnoldIDSet("del","","setID04")')  
        #setID05
        mc.iconTextCheckBox(al='left', bgc=[0.13, 0.15, 0.25],olc=[0, 1 ,0],width=80, height=30,style='iconAndTextVertical', image1='plane.png', label='setID05')
        mc.button(label=u'R', width=50, height=30, bgc=[1, 0, 0], command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().GA_ArnoldIDSet("set","R","setID05")')
        mc.button(label=u'G',width=50, height=30,bgc=[0, 1, 0.0], command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().GA_ArnoldIDSet("set","G","setID05")')
        mc.button(label=u'B',width=50, height=30,bgc=[0, 0, 1], command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().GA_ArnoldIDSet("set","B","setID05")')
        mc.button(label=u'delete',width=80, height=30,bgc=[0, 0, 0], command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().GA_ArnoldIDSet("del","","setID05")')  
        mc.setParent('..')
        mc.setParent('..')
        mc.setParent('..')

        # 应P4需求整合
        child4 = mc.columnLayout(adjustableColumn=True)
        mc.frameLayout(label=u'常用渲染层工具', bgc=[0, 0, 0.0], borderStyle='etchedIn', cll=0,cl=1)
        mc.rowColumnLayout(numberOfColumns=4)
        mc.button(label=u'CHR_CO',width=90,height=30,bgc=[0.13, 0.15, 0.25],command='from idmt.maya.Lion import Lion_renderLayer;reload(Lion_renderLayer);Lion_renderLayer.Lion_renderLayer().Lion_CHRcolorCreate()')
        mc.button(label=u'BG__CO',width=90,height=30,bgc=[0.13, 0.15, 0.25],command='from idmt.maya.Lion import Lion_renderLayer;reload(Lion_renderLayer);Lion_renderLayer.Lion_renderLayer().Lion_SETcolorCreate()')
        mc.button(label=u'CHR_IDP',width=90,height=30,bgc=[0.13, 0.15, 0.25],command='from idmt.maya.Lion import Lion_renderLayer;reload(Lion_renderLayer);Lion_renderLayer.Lion_renderLayer().Lion_CHRidpCreate()')
        mc.button(label=u'BG__IDP',width=90,height=30,bgc=[0.13, 0.15, 0.25],command='from idmt.maya.Lion import Lion_renderLayer;reload(Lion_renderLayer);Lion_renderLayer.Lion_renderLayer().Lion_SETidpCreate()')
        mc.button(label=u'ZDepth',width=90,height=30,bgc=[0.0, 0.0, 0.0],command='import Other.minitiger.BD_ysRenderlayerSetup as bdyrs;reload(bdyrs)\nbdyrs.ysCreateRenderLayer(u\'Depth\')')
        mc.button(label=u'Shadow',width=90,height=30,bgc=[0.0, 0.0, 0.0],command='from idmt.maya.Lion import Lion_renderLayer;reload(Lion_renderLayer);Lion_renderLayer.Lion_renderLayer().Lion_SHrl_Create()')
        mc.button(label=u'Coming',width=90,height=30,bgc=[0.0, 0.0, 0.0],command='print "Hello Baby"')
        mc.button(label=u'Smooth',width=90,height=30,bgc=[0.0, 0.5, 0.0],command='from idmt.maya.commonCore.core_mayaCommon import sk_smoothSet;reload(sk_smoothSet);sk_smoothSet.sk_smoothSet().smoothSetDoSmooth(disModify  = 0)')
        #====add by zhangben 2016.06.15 ,add Old ZDepth Mode tools

        mc.setParent('..')
        mc.setParent('..')
        mc.setParent('..')
        #DOD6 基本渲染工具
        child5 = mc.columnLayout(adjustableColumn=True)
        mc.frameLayout(label=u'DOD6渲染工具', bgc=[0, 0, 0.0], borderStyle='etchedIn', cll=0,cl=1)
        mc.rowColumnLayout(numberOfColumns=4)
        mc.button(label=u'chr',width=90,height=30,bgc=[0.13, 0.15, 0.25],command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().DO6RenderLayerCreat("co","chr",1,1,1,2)')
        mc.button(label=u'set',width=90,height=30,bgc=[0.13, 0.15, 0.25],command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().DO6RenderLayerCreat("co","set",1,1,1,2)')
        mc.button(label=u'cauSetIdp',width=90,height=30,bgc=[0.13, 0.15, 0.25],command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().DO6RenderLayerCreat("caustic","",1,1,1,2)')
        #mc.button(label=u'chrLightIdp',width=90,height=30,bgc=[0.13, 0.15, 0.25],command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().DO6RenderLayerCreat("light","chr",1,1,1,2)')
        mc.button(label=u'All_idp',width=90,height=30,bgc=[0.13, 0.15, 0.25],command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().DO6RenderLayerCreat("id31","",1,1,1,2)')
        mc.button(label=u'shadowAO',width=90,height=30,bgc=[0.13, 0.15, 0.25],command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().DO6RenderLayerCreat("shadow","",1,1,1,2)')
        mc.button(label=u'motionBlur',width=90,height=30,bgc=[0.13, 0.15, 0.25],command='from idmt.maya.py_common import GA_RenderArnoldLayer\nreload(GA_RenderArnoldLayer)\nGA_RenderArnoldLayer.GA_RenderArnold().DO6RenderLayerCreat("motionblur","",1,1,1,2)')
        mc.tabLayout(tabs, edit=True, tabLabel=(
            (child2, 'Arnold AOV'),(child1, u'渲染流程'), (child3, u'渲染工具'),(child4, u'常用渲染层'),(child5, u'DOD6渲染工')))
        mc.showWindow('GA_RenderArnold')    
    #----------------------------------------------------------------------------------------------------------#      #----------------------------------------------------------#
        #------------------------------#
    # 【渲染】【Arnold渲染设置】【可以根据项目需求添加参数】
    #  Author  : 韩虹
    #  Data    : 2017_04_18
    #------------------------------#

    def GA_ArnoldRendererSettings(self,form='Yak'):
        print (u'===============!!!Start 【%s】!!!===============' % (u'Arnold设置'))
        print 'Working...'
        
        mc.setAttr('defaultRenderGlobals.imageFormat', 7)   
        try:
           mc.loadPlugin('mtoa',qt=1)
        except:
            pass
        # 开启窗口，创建各种UI
        #mel.eval('unifiedRenderGlobalsWindow')
        renderglobal=mc.getAttr('defaultRenderGlobals.currentRenderer')
        if renderglobal!='arnold':
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'arnold', type='string')
    # 下来所需的节点提前创建
        import mtoa
        mtoa.core.createOptions()
        import mtoa.cmds.registerArnoldRenderer
        mtoa.cmds.registerArnoldRenderer.registerArnoldRenderer()
        samplingInfo=['defaultArnoldRenderOptions.AASamples','defaultArnoldRenderOptions.GIDiffuseSamples','defaultArnoldRenderOptions.GIGlossySamples','defaultArnoldRenderOptions.GIRefractionSamples','defaultArnoldRenderOptions.GISssSamples','defaultArnoldRenderOptions.GIVolumeSamples','defaultArnoldRenderOptions.lock_sampling_noise','defaultArnoldRenderOptions.sssUseAutobump']
        sampYak=[5,2,2,2,2,0,1,1]
        imageFormat=['defaultArnoldDriver.aiTranslator']
        imageYak=['exr']
        clamping=['defaultArnoldRenderOptions.use_sample_clamp','defaultArnoldRenderOptions.use_sample_clamp_AOVs','defaultArnoldRenderOptions.AASampleClamp']
        clamYak=[1,0,1.5]
        filter=['defaultArnoldFilter.width']
        filtYak=[2]
        rayDepth=['defaultArnoldRenderOptions.GITotalDepth','defaultArnoldRenderOptions.GIDiffuseDepth','defaultArnoldRenderOptions.GIGlossyDepth','defaultArnoldRenderOptions.GIReflectionDepth','defaultArnoldRenderOptions.GIRefractionDepth','defaultArnoldRenderOptions.GIVolumeDepth','defaultArnoldRenderOptions.autoTransparencyDepth','defaultArnoldRenderOptions.autoTransparencyThreshold']
        rayYak=[3,1,1,2,2,0,2,0.990]
        motionblur=['defaultArnoldRenderOptions.motion_blur_enable']
        motionYak=[0]
        tex=['defaultArnoldRenderOptions.use_existing_tiled_textures']
        texYak=[1]
        AOV=['defaultArnoldDriver.mergeAOVs','defaultArnoldRenderOptions.aovMode','defaultArnoldDriver.prefix']
        AOVYak=[1,1,'']
        strInfo=['defaultArnoldDriver.aiTranslator','defaultArnoldDriver.prefix']
        infos=[samplingInfo,imageFormat,clamping,filter,rayDepth,motionblur,tex,AOV]
        infoYak=[]
        if form=='Yak':
            infoYak=[sampYak,imageYak,clamYak,filtYak,rayYak,motionYak,texYak,AOVYak]
        if form in ['Yak']:
            for i in range(len(infos)):
                for j in range(len(infos[i])):
                    typeinfo=infos[i][j]
                    typNum=infoYak[i][j]
                    if typeinfo not in strInfo:
                        mc.setAttr(typeinfo,typNum)
                    else:
                        mc.setAttr(typeinfo,typNum,type='string')
            mc.setAttr('defaultArnoldDriver.halfPrecision',1)
            mc.setAttr('defaultArnoldDriver.autocrop',1)

        if (form=='shadow'):
            mc.setAttr('defaultArnoldDriver.halfPrecision', 1)
            mc.setAttr('defaultArnoldDriver.tiled', 0)
            mc.setAttr('defaultArnoldDriver.autocrop', 1)
            mc.setAttr('defaultArnoldRenderOptions.AASamples', 3)
            mc.setAttr('defaultArnoldRenderOptions.GIDiffuseSamples', 0)
            mc.setAttr('defaultArnoldRenderOptions.GIGlossySamples', 0)
            mc.setAttr('defaultArnoldRenderOptions.GIRefractionSamples', 0)
            if mc.ls('defaultArnoldRenderOptions.sssBssrdfSamples'):
                mc.setAttr('defaultArnoldRenderOptions.sssBssrdfSamples', 0)
            mc.setAttr('defaultArnoldRenderOptions.lock_sampling_noise', 1)
            mc.setAttr('defaultArnoldRenderOptions.use_sample_clamp', 1)
            mc.setAttr('defaultArnoldRenderOptions.AASampleClamp', 1.5) 
            mc.setAttr('defaultArnoldRenderOptions.GITotalDepth', 3)
            mc.setAttr('defaultArnoldRenderOptions.autoTransparencyDepth', 2)
            mc.setAttr('defaultArnoldRenderOptions.use_existing_tiled_textures', 1)                                                                                              
            #mc.setAttr('defaultArnoldDriver.aiTranslator','tif',type='string')
            #mc.setAttr('defaultArnoldDriver.tiffFormat',0)
            #mc.setAttr('defaultArnoldDriver.tiffCompression',1)
            
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
            if mc.ls('defaultArnoldRenderOptions.sssBssrdfSamples'):
                mc.setAttr('defaultArnoldRenderOptions.sssBssrdfSamples', 0)
            mc.setAttr('defaultArnoldRenderOptions.lock_sampling_noise', 1)
            mc.setAttr('defaultArnoldRenderOptions.use_sample_clamp', 1)
            mc.setAttr('defaultArnoldRenderOptions.AASampleClamp', 1.5) 
            mc.setAttr('defaultArnoldRenderOptions.GITotalDepth', 3)
            mc.setAttr('defaultArnoldRenderOptions.autoTransparencyDepth', 2)
            mc.setAttr('defaultArnoldRenderOptions.use_existing_tiled_textures', 1)                                                                                              
            mc.setAttr('defaultArnoldDriver.aiTranslator','exr',type='string')
            mc.setAttr ('defaultArnoldDriver.exrCompression', 3)
            mc.setAttr ('defaultArnoldRenderOptions.aovMode',1)                                      
    #----------------------------------------------------------#    
    #----------------------------------------------------------------------------------------------------------#      #----------------------------------------------------------#
        #------------------------------#
    # 【渲染】【渲染相机设置
    #  Author  : 韩虹
    #  Data    : 2017_04_18
    #------------------------------#
    def GA_camSet(self,shotType=2):
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        shot=''
        if shotType==2:
            shot=shotInfo[1]+'_'+shotInfo[2]
        if shotType==3:
            shot=shotInfo[1]+'_'+shotInfo[2]+'_'+shotInfo[3]
        cam='CAM:cam_'+shot+'_baked'
        if mc.objExists(cam)!=True:
            mc.error(u'文件中缺少正确命名的相机【%s】' %cam)
        shap=mc.listRelatives(cam,s=1,f=1)
        ca=mc.ls(ca=1,l=1)
        if not ca:
            mc.error(u'文件中没有相机，请检查')
        for camm in ca:
            if camm!=shap[0]:
                mc.setAttr(camm+'.renderable',0)
            else:
                mc.setAttr(camm+'.renderable',1)
        return cam
    #----------------------------------------------------------#
    #----------------------------------------------------------------------------------------------------------#      #----------------------------------------------------------#
        #------------------------------#
    # 【渲染】【渲染帧数及渲染尺寸设置】
    #  Author  : 韩虹
    #  Data    : 2017_04_18
    #------------------------------#
    def GA_FileSet(self,shotType=2):
        import idmt.pipeline.db
        shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
        if shotType == 2:
            shot = shotInfos[0] + '_' + shotInfos[1] + '_' + shotInfos[2]
        if shotType == 3:
            shot = shotInfos[0] + '_' + shotInfos[1] + '_' + shotInfos[2] + '_' + shotInfos[3]

        anim = idmt.pipeline.db.GetAnimByFilename(shot)
        startFrame = anim.frmStart
        endFrame = anim.frmEnd
        fpsFrame = anim.fps
        resW = anim.resolutionW
        resH = anim.resolutionH
        # 分辨率
        mc.setAttr(('defaultResolution.width'), resW)
        mc.setAttr(('defaultResolution.height'), resH)
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
            preStartFrame = startFrame - 12
            mc.playbackOptions(animationStartTime=preStartFrame)
            # 结束帧
            mc.playbackOptions(max=endFrame)
            # 结束预留
            posEndFrame = endFrame + 12
            mc.playbackOptions(animationEndTime=posEndFrame)
        # 设置帧播放模式每帧
        mc.playbackOptions(playbackSpeed=0)

        # 允许undo
        mc.undoInfo(state=True, infinity=True)
        # 设置当前帧数
        mc.currentTime(startFrame)
        # 设置
        mel.eval('setMayaSoftwareFrameExt(3, 0)')
        # 设置渲染帧数
        mc.setAttr('defaultRenderGlobals.startFrame',startFrame)
        mc.setAttr('defaultRenderGlobals.endFrame',endFrame)
        return shot

    #----------------------------------------------------------#
    #----------------------------------------------------------------------------------------------------------#      #----------------------------------------------------------#
        #------------------------------#
    # 【渲染】【项目arnold渲染设置】
    #  Author  : 韩虹
    #  Data    : 2017_04_18
    #------------------------------#
    def GA_ArnldSetting(self,form='Yak',shotType=2):
        self.GA_ArnoldRendererSettings(form)
        self.GA_camSet(shotType)
        self.GA_FileSet(shotType)
        print u'===============!!!End 【Arnold设置】!!!==============='
        return 0


    #motionblur渲染层创建
    def csl_ArnoldRenderLayerCreat(self,layername='motionblur'):
        objselect=mc.ls(sl=1,l=1)
        from idmt.maya.py_common import GA_RenderArnoldLayer
        reload(GA_RenderArnoldLayer)
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
        try:                     
          mc.select(obj)
          mc.sets(obj,e = 1 , forceElement = mblurSG)
          mc.setAttr('defaultArnoldRenderOptions.motion_blur_enable',1);
        except:
          pass
        
    #----------------------------------------------------------#
    #----------------------------------------------------------------------------------------------------------#      #----------------------------------------------------------#
        #------------------------------#
    # 【渲染】【核心】【创建AOV通道】
    #  Author  : 韩虹
    #  Data    : 2017_04_18
    #------------------------------#
    def GA_ArnoldAOVCreat(self,AOVtype='Zdp',form='Yak'):
        objs=mc.ls(sl=1,l=1)
        mc.select(cl=1)
        AOVList01=['AO','Zdp','Normal','Shadow','Fre','light_all']
        data01=[5,6,5,5,5,6]
        filter01=['gaussian','gaussian','gaussian','gaussian','gaussian','gaussian']
        #外部AOV，需要创建材质球
        AOVList02=['N','P','Z','direct_diffuse','direct_specular','emission','indirect_diffuse','indirect_specular','motionvector','reflection','refraction','sss','light_group','meshID']
        data02=[7,8,4,5,5,5,5,5,5,5,5,5,5,6]
        filter02=['closest','closest','closest','gaussian','gaussian','gaussian','gaussian','gaussian','gaussian','gaussian','gaussian','gaussian','gaussian','gaussian']
        AOVList=AOVList01+AOVList02
        data=data01+data02
        filter=filter01+filter02
        AOVArnoldPass=''
        if AOVtype in AOVList:
            for i in range(len(AOVList)):
                if AOVList[i]==AOVtype and AOVtype in AOVList01:
                    AOVShader=self.GA_ArnoldShaderAssign(AOVtype,0)
                    AOVArnoldPass = 'ZDAOV_'+AOVtype
                    if mc.ls(AOVArnoldPass) :
                        if mc.nodeType(AOVArnoldPass) =='aiAOV':
                            pass
                        else:
                            mc.delete(AOVArnoldPass)
                            mc.createNode('aiAOV',name = AOVArnoldPass)
                    else:
                        mc.createNode('aiAOV',name = AOVArnoldPass )

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


                    try:
                        mc.disconnectAttr(('%s.%s') % ( AOVArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , ('aovList['+str(i)+']')))

                    except:
                        pass
                    mc.connectAttr(('%s.%s') % ( AOVArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , ('aovList['+str(i)+']')), f=True)
                    #设置
                    mc.setAttr(AOVArnoldPass+'.name',AOVtype,type='string')
                    mc.setAttr('defaultArnoldDriver.prefix','',type='string')
                    if data[i] !=6:
                        mc.setAttr((AOVArnoldPass+'.type'),data[i])
                    if filter[i]!='gaussian':
                        aiAOVFilterN =  'defaultArnoldFilter_'+filter[i]
                        if mc.ls(aiAOVFilterN) :
                            if mc.nodeType(aiAOVFilterN) =='aiAOVFilter':
                                pass
                            else:
                                mc.delete(aiAOVFilterN)
                                mc.createNode('aiAOVFilter',name = aiAOVFilterN)
                        else:
                            aiAOVFilterN =  'defaultArnoldFilter_'+filter[i]
                            mc.createNode('aiAOVFilter',name = aiAOVFilterN )
                        try:
                            mc.connectAttr(('%s.%s') % ( aiAOVFilterN , 'message') , ('%s.%s') % (AOVArnoldPass,('outputs[0].filter')), f=True)
                            mc.setAttr((aiAOVFilterN+'.aiTranslator'),'closest',type='string')
                        except:
                            pass
                if AOVList[i]==AOVtype and AOVtype in AOVList02:
                    AOVArnoldPass = 'ZDAOV_'+AOVtype
                    if mc.ls(AOVArnoldPass) :
                        if mc.nodeType(AOVArnoldPass) =='aiAOV':
                            pass
                        else:
                            mc.delete(AOVArnoldPass)
                            mc.createNode('aiAOV',name = AOVArnoldPass)
                    else:
                        mc.createNode('aiAOV',name = AOVArnoldPass )

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
                        mc.disconnectAttr(('%s.%s') % ( AOVArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , ('aovList['+str(i)+']')))
                    except:
                        pass
                    mc.connectAttr(('%s.%s') % ( AOVArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , ('aovList['+str(i)+']')), f=True)

                    #设置
                    mc.setAttr(AOVArnoldPass+'.name',AOVtype,type='string')
                    mc.setAttr('defaultArnoldDriver.prefix','',type='string')
                    if data[i] !=5:
                        mc.setAttr((AOVArnoldPass+'.type'),data[i])
                    if filter[i]!='gaussian':
                        aiAOVFilterN =  'defaultArnoldFilter_'+filter[i]
                        if mc.ls(aiAOVFilterN) :
                            if mc.nodeType(aiAOVFilterN) =='aiAOVFilter':
                                pass
                            else:
                                mc.delete(aiAOVFilterN)
                                mc.createNode('aiAOVFilter',name = aiAOVFilterN)
                        else:
                            aiAOVFilterN =  'defaultArnoldFilter_'+filter[i]
                            mc.createNode('aiAOVFilter',name = aiAOVFilterN )
                        try:
                            mc.connectAttr(('%s.%s') % ( aiAOVFilterN , 'message') , ('%s.%s') % (AOVArnoldPass,('outputs[0].filter')), f=True)
                            mc.setAttr((aiAOVFilterN+'.aiTranslator'),'closest',type='string')
                        except:
                            pass
        return AOVArnoldPass

    #----------------------------------------------------------#
    #----------------------------------------------------------------------------------------------------------#      #----------------------------------------------------------#
        #------------------------------#
    # 【渲染】【核心】【创建特殊AOV通道】
    #  Author  : 韩虹
    #  Data    : 2017_04_18
    #------------------------------#
    def GA_speAOVCreat(self,AOVtype='meshID'):
       typeList=self.GA_AttrRead(AOVtype)
       if AOVtype in ['meshID','chrID','setID'] and typeList:
           for i in range(len(typeList)):
               shadeN='SHD_'+typeList[i]+'alSurface_arnold'
               if mc.objExists(shadeN):
                   mc.delete(shadeN)
               shade=self.GA_ArnoldShaderAssign(shaderType='meshID',transparency=0)
               shade=mc.rename(shade,shadeN)
               mc.setAttr((shade+'.colorAttrName'),typeList[i],type='string')
               AOVArnoldPass=self.GA_ArnoldAOVCreat('meshID')
               AOVArnoldPassN='aiAOV_'+typeList[i]
               AOVArnoldPass=mc.rename(AOVArnoldPass,AOVArnoldPassN)
               mc.setAttr(AOVArnoldPass+'.name','meshID'+'_'+str(typeList[i]),type='string')
               try:
                   mc.connectAttr(('%s.%s') % (shade , 'outColor') , ('%s.%s') % (AOVArnoldPass,'defaultValue'), f=True)
               except:
                   pass
               try:
                   mc.disconnectAttr(('%s.%s') % ( AOVArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[19]'))
               except:
                   pass
               mc.connectAttr(('%s.%s') % ( AOVArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , ('aovList['+str(i+1000)+']')), f=True)
       if AOVtype=='light_group' and typeList:
            for i in range(len(typeList)):
                AOVArnoldPass=self.GA_ArnoldAOVCreat(AOVtype)
                AOVArnoldPassN='aiAOV_'+AOVtype+'_'+str(typeList[i])
                AOVArnoldPass=mc.rename(AOVArnoldPass,AOVArnoldPassN)
                mc.setAttr(AOVArnoldPass+'.name',AOVtype+'_'+str(typeList[i]),type='string')
                try:
                    mc.disconnectAttr(('%s.%s') % ( AOVArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[18]'))
                except:
                   pass
                mc.connectAttr(('%s.%s') % ( AOVArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , ('aovList['+str(i+2000)+']')), f=True)



    #----------------------------------------------------------#
    #----------------------------------------------------------------------------------------------------------#      #----------------------------------------------------------#
        #------------------------------#
    # 【渲染】【辅助】【读取特殊属性，为特殊AOV作准备】
    #  Author  : 韩虹
    #  Data    : 2017_04_18
    #------------------------------#
    def GA_AttrRead(self,AOVtype='meshID'):
        typeList=[]
        if AOVtype=='light_group':
            lights=mc.ls(lt=1,l=1)+mc.ls(type='aiAreaLight',l=1)+mc.ls(type='aiSkyDomeLight',l=1)+mc.ls(type='aiSkyDomeLight',l=1)+mc.ls(type='aiPhotometricLight',l=1)
            if not lights:
                mc.error(u'文件中缺少灯光物体，请检查')
            for ligt in lights:
                if mc.objExists(ligt+'.mtoa_constant_lightGroup') and mc.getAttr(ligt+'.mtoa_constant_lightGroup')!='':
                    Num=mc.getAttr(ligt+'.mtoa_constant_lightGroup')
                    if Num not in typeList:
                        typeList.append(Num)
        if AOVtype=='meshID':
            meshs=mc.ls(type='mesh',l=1)
            if not meshs:
                mc.error(u'文件中缺少polygon物体，请检查')
            for mesh in meshs:
                if mc.listAttr(mesh,st='mtoa_constant_*'):
                    Attrs=mc.listAttr(mesh,st='mtoa_constant_*')
                    for Attr in Attrs:
                        AttrN=Attr.split('mtoa_constant_')[-1]
                        if AttrN=='':
                            try:
                                mc.deleteAttr(mesh, at=Attr)
                            except:
                                pass
                            mc.error(u'【%s】模型ID【%s】问题' %(mesh,Attr))
                        if AttrN not in typeList and AttrN!='' and AttrN[-1] not in ['X','Y','Z']:
                            typeList.append(AttrN)
        if AOVtype in ['chrID','setID']:
            sty='mtoa_constant_'+AOVtype+'*'
            meshs=mc.ls(type='mesh',l=1)
            if not meshs:
                mc.error(u'文件中缺少polygon物体，请检查')
            for mesh in meshs:
                if mc.listAttr(mesh,st=sty):
                    Attrs=mc.listAttr(mesh,st=sty)
                    for Attr in Attrs:
                        AttrN=Attr.split('mtoa_constant_')[-1]
                        if AttrN not in typeList and AttrN!='' and AttrN[-1] not in ['X','Y','Z']:
                            typeList.append(AttrN)

        return typeList

    #----------------------------------------------------------#
    #----------------------------------------------------------------------------------------------------------#      #----------------------------------------------------------#
        #------------------------------#
    # 【渲染】【辅】【删除相应AOV通道及材质节点】
    #  Author  : 韩虹
    #  Data    : 2017_04_24
    #------------------------------#
        def ArnoldAOVDeleteD(self,AOVtype='AO'):
            Shade='SHD_'+AOVtype+'_arnold'
            SG=Shade+'_SG'
            ArnoldPass='ZDAOV_'+AOVtype
            if AOVtype in ['meshID','light_group']:
                ArnoldPass=[]
                typeList=self.GA_AttrRead(AOVtype)
                for i in range(len(typeList)):
                    Pass=''
                    if AOVtype=='meshID':
                        Pass='aiAOV_'+typeList[i]
                    if AOVtype=='light_group':
                        Pass='aiAOV_'+AOVtype+'_'+typeList[i]
                    if Pass not in ArnoldPass:
                        ArnoldPass.append(Pass)
            Infos=[Shade,SG,ArnoldPass]
            if not Infos:
                mc.error(u'文件中没有【%s】AOV通道及相关节点，请检查'%AOVtype)
            for i in range(len(Infos)):
                if mc.ls(Infos[i]) and AOVtype not  in ['meshID','light_group']:
                    mc.delete(Infos[i])
                if AOVtype in ['meshID','light_group'] and i !=2 and mc.ls(Infos[i]):
                    mc.delete(Infos[i])
                if AOVtype in ['meshID','light_group'] and i ==2:
                    for j in  Infos[i]:
                        if mc.ls(Infos[i][j]):
                            mc.delete(Infos[i][j])
            print u'==========已删除[%s】AOV通道及相关节点=========='%AOVtype


    def GA_ArnoldShaderAssign(self,shaderType='Shadow',transparency=0):
        meshs=mc.ls(sl=1,l=1)
        if transparency==0:
            Shade='SHD_'+shaderType+'_arnold'
            SG=Shade+'SG'
            #删除已有材质球和SG节点
            if mc.objExists(Shade):
                mc.delete(Shade)
            if mc.objExists(SG):
                mc.delete(SG)
            ##创建新材质球和SG节点
            if shaderType=='AO':
                mc.shadingNode('aiAmbientOcclusion', asShader=True,n=Shade)
            elif shaderType=='Shadow':
                mc.shadingNode('aiShadowCatcher', asShader=True,n=Shade)
            elif shaderType in ['reflection','caustic']:
                mc.shadingNode('aiStandard', asShader=True,n=Shade)
            elif shaderType=='meshID':
                mc.shadingNode('aiUserDataColor',asShader=True,n=Shade)
            elif shaderType=='light_all':
                mc.shadingNode('alSurface',asShader=True,n=Shade)
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
    #反射材质
            if shaderType=='reflection':
                mc.setAttr ((Shade+'.Kd'),0)
                mc.setAttr ((Shade+'.Ks'),1)
                mc.setAttr ((Shade+'.Ks'),1)
                mc.setAttr ((Shade+'.specularRoughness'),1)
                mc.setAttr ((Shade+'.specularFresnel'),1)
                mc.setAttr ((Shade+'.Kr'),1)
                mc.setAttr ((Shade+'.Fresnel'),1)
                mc.setAttr ((Shade+'.Krn'),1)

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
            if shaderType=='caustic':
                mc.setAttr((Shade + '.color'),1,1,1,type = 'double3')
                mc.setAttr((Shade + '.Kd'),0.7)
                mc.setAttr((Shade + '.FresnelAffectDiff'),1)
                mc.setAttr((Shade + '.Ks'),0)
            if shaderType=='light_all':
                #mc.setAttr((Shade + '.diffuseColor'),1,1,1,type = 'double3')
                mc.setAttr(Shade +'.specular1Strength',0)
                AttrList=['aovDiffuseColor','aovDirectDiffuse','aovDirectDiffuseRaw','aovIndirectDiffuse','aovIndirectDiffuseRaw','aovDirectBacklight','aovIndirectBacklight','aovDirectSpecular',
                'aovIndirectSpecular','aovDirectSpecular2','aovIndirectSpecular2','aovSingleScatter','aovSss','aovRefraction','aovEmission','aovUv','aovDepth','aovId1','aovId2','aovId3',
                'aovId4','aovId5','aovId6','aovId7','aovId8','aovShadowGroup1','aovShadowGroup2','aovShadowGroup3','aovShadowGroup4','aovShadowGroup5','aovShadowGroup6','aovShadowGroup7',
                'aovShadowGroup8']
                for i in range(len(AttrList)):
                    mc.setAttr((Shade +'.'+AttrList[i]),'',type='string')
            if shaderType=='meshID':
                mc.setAttr((Shade + '.defaultValue'),0,0,0,type = 'double3')
        return Shade



    #渲染层创建
    def GA_ArnoldRendererLayerCreat(self):
        self.GA_ArnldSetting('Yak',2)
        # 渲染设置
        AOVList01=['AO','Zdp','Normal','Shadow','Fre','lightall']
        AOVList02=['N','P','Z','direct_diffuse','direct_specular','emission','indirect_diffuse','indirect_specular','motionvector','reflection','refraction','sss','light_group','meshID']
        AOVtypeLists=AOVList01+AOVList02
        #创建pass
        for i in range(len(AOVtypeLists)):
            GAcheck='GAcheck'+AOVtypeLists[i]
            if mc.checkBox(GAcheck, exists=1) and  mc.checkBox(GAcheck,q=1,v=1)==True:
                self.GA_ArnoldAOVCreat(AOVtypeLists[i])
      #创建渲染层 
        mel.eval('source "//file-cluster/GDC/Resource/Support/Maya/projects/ShunLiu/CSL_RenderToolsMR.mel";CSL_RenderTools_Arnold();')
        print u'=========已创建渲染层========='
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
        else:#add by zhangben 2017/12/05 check lambert can not assign
            print("There Need Create A Connections on plus{}".format(idSG))
#####
#        SGS=mc.ls(type='shadingEngine')
#        SGS.remove('initialParticleSE')
#        SGS.remove('initialShadingGroup') 
#        for SG in SGS:
#            print SG
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
            print u'请选择物体'
    def ArnoldIDCreat(self,idpShader):
        sels=mc.ls(sl=True)
        #from idmt.maya.py_common import GA_RenderArnoldLayer
        #reload(GA_RenderArnoldLayer)
        #GA_RenderArnoldLayer.GA_RenderArnold().ArnoldRendererSettings('02')
        if mc.objExists(idpShader)==0:
            mc.shadingNode('aiStandard', asShader=True,n=idpShader)
        idpSG=idpShader+'SG'
        if mc.objExists(idpSG)==0:
            mc.sets(renderable=1,noSurfaceShader=1,em=1,n=idpSG)
        cons=mc.listConnections('%s.outColor' % idpShader)
        if cons!=None:
            #print 'sss'
            if(cons[0]!=idpSG):
                mc.disconnectAttr(('%s.outColor' % idpShader), ('%s.surfaceShader' % cons[0]))
                mc.connectAttr(('%s.outColor' % idpShader),('%s.surfaceShader' % idpSG))
        else:
            mc.connectAttr(('%s.outColor' % idpShader),('%s.surfaceShader' % idpSG))
        #mc.setAttr((idpShader+".shadeMode"),2 )
        #mc.setAttr((idpShader+".colorMode"),0 )

        mc.setAttr((idpShader+".FresnelAffectDiff"),0 )
        mc.setAttr((idpShader+".Kd"),1 )
        if(idpShader=='ArnoldIdpR'):
            mc.setAttr((idpShader+'.color'),1,0,0)
            mc.setAttr((idpShader+".aiEnableMatte"),1 )
            mc.setAttr((idpShader+".aiMatteColor"),1,0,0 )
            mc.setAttr((idpShader+".aiMatteColorA"),0 )
            #mc.setAttr((idpShader+'.hardwareColor'),1,0,0)
        elif(idpShader=='ArnoldIdpG'):
            mc.setAttr((idpShader+'.color'),0,1,0)
            mc.setAttr((idpShader+".aiEnableMatte"),1 )
            mc.setAttr((idpShader+".aiMatteColor"),0,1,0 )
            mc.setAttr((idpShader+".aiMatteColorA"),0 )
            #mc.setAttr((idpShader+'.hardwareColor'),0,1,0)
        elif(idpShader=='ArnoldIdpB'):
            mc.setAttr((idpShader+'.color'),0,0,1)
            mc.setAttr((idpShader+".aiEnableMatte"),1 )
            mc.setAttr((idpShader+".aiMatteColor"),0,0,1 )
            mc.setAttr((idpShader+".aiMatteColorA"),0 )
            #mc.setAttr((idpShader+'.hardwareColor'),0,0,1)
        elif(idpShader=='ArnoldIdpM'):
            mc.setAttr((idpShader+'.color'),0,0,0)
            mc.setAttr((idpShader+".aiEnableMatte"),1 )
            mc.setAttr((idpShader+".aiMatteColor"),0,0,0 )
            mc.setAttr((idpShader+".aiMatteColorA"),0 )
            #mc.setAttr((idpShader+'.hardwareColor'),0,0,0)
        elif(idpShader=='ArnoldIdpA'):
            mc.setAttr((idpShader+'.color'),1,1,1)
            mc.setAttr((idpShader+'.opacity'),1,1,1)
            mc.setAttr((idpShader+".aiEnableMatte"),1 )
            mc.setAttr((idpShader+".aiMatteColor"),0,0,0 )
            mc.setAttr((idpShader+".aiMatteColorA"),1 )
            #mc.setAttr((idpShader+'.hardwareColor'),0,0,0)
        elif(idpShader=='ArnoldIdpY'):
            mc.setAttr((idpShader+'.color'),1,1,0)
            #mc.setAttr((idpShader+'.hardwareColor'),1,1,0)
        elif(idpShader=='ArnoldIdpC'):
            mc.setAttr((idpShader+'.color'),0,1,1)
            #mc.setAttr((idpShader+'.hardwareColor'),0,1,1)
        elif(idpShader=='ArnoldIdpK'):
            mc.setAttr((idpShader+'.color'),1,0,1)
            #mc.setAttr((idpShader+'.hardwareColor'),1,0,1)
        else:
            print u'请正确输入IDP类型'
                                                                    
        mc.select(sels)
        try:
            mc.sets(e = 1 , forceElement = idpSG)
            mc.sets(e = 1 , forceElement = idpSG)
            mc.sets(e = 1 , forceElement = idpSG)
        except:
            print u'===有物体无法赋予材质==='
            print sels
            mc.warning(u'===有物体无法赋予材质===')         
#        cmd1="`"+"sets -e -forceElement"+" "+idpSG+"`"
#        cmd= "catch("+cmd1+")"
#        mel.eval(cmd) 

    #导出RGB信息                
    def csl_RGBInfoExportTest(self):
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        if shotInfo[0]=='csl' or shotInfo[0]=='do5':
            shader = mc.ls(mat=1)
            for shade in shader:
                if mc.nodeType(shade)!='aiUtility' and 'ArnoldIdp' not in shade and shade!='particleCloud1' and shade!='lambert1' and shade!='shaderGlow1':
                    print 'a'
                    mc.error (shade+':'+u'该材质命名不正确，或者非aiUtility材质')
                else:
                    SGNodes = mc.listConnections(shade,d=1,type = 'shadingEngine')
                    if not SGNodes:
                        mc.error(u'===请清理无用材质===') 
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
                    from idmt.maya.commonCore.core_renderLayer import sk_renderLayerCore
                    reload(sk_renderLayerCore)
                    sk_renderLayerCore.sk_renderLayerCore().ydRLayerRGBInfoExport(id,"R",1)
                elif('IdpG' in shade):
                    mc.select(shade)
                    from idmt.maya.commonCore.core_renderLayer import sk_renderLayerCore
                    reload(sk_renderLayerCore)
                    sk_renderLayerCore.sk_renderLayerCore().ydRLayerRGBInfoExport(id,"G",1)
                elif('IdpB' in shade):
                    mc.select(shade)
                    from idmt.maya.commonCore.core_renderLayer import sk_renderLayerCore
                    reload(sk_renderLayerCore)
                    sk_renderLayerCore.sk_renderLayerCore().ydRLayerRGBInfoExport(id,"B",1)                               
                elif('IdpM' in shade):
                    mc.select(shade)
                    from idmt.maya.commonCore.core_renderLayer import sk_renderLayerCore
                    reload(sk_renderLayerCore)
                    sk_renderLayerCore.sk_renderLayerCore().ydRLayerRGBInfoExport(id,"M",1)             
                elif('IdpY' in shade):
                    mc.select(shade)
                    from idmt.maya.commonCore.core_renderLayer import sk_renderLayerCore
                    reload(sk_renderLayerCore)
                    sk_renderLayerCore.sk_renderLayerCore().ydRLayerRGBInfoExport(id,"Y",1)               
                elif('IdpC' in shade):
                    mc.select(shade)
                    from idmt.maya.commonCore.core_renderLayer import sk_renderLayerCore
                    reload(sk_renderLayerCore)
                    sk_renderLayerCore.sk_renderLayerCore().ydRLayerRGBInfoExport(id,"C",1)              
                elif('IdpK' in shade):
                    mc.select(shade)
                    from idmt.maya.commonCore.core_renderLayer import sk_renderLayerCore
                    reload(sk_renderLayerCore)
                    sk_renderLayerCore.sk_renderLayerCore().ydRLayerRGBInfoExport(id,"K",1)
                elif('IdpA' in shade):
                    mc.select(shade)
                    from idmt.maya.commonCore.core_renderLayer import sk_renderLayerCore
                    reload(sk_renderLayerCore)
                    sk_renderLayerCore.sk_renderLayerCore().ydRLayerRGBInfoExport(id,"A",1)
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
                    if idColor[i]==[1,1,1]:
                        self.ArnoldIDCreat(idpShader="ArnoldIdpA")
        else:
            print '缺少id信息，请检查'

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
        while mc.file(q=1,r=1): 
          refPath=mc.file(q=1,r=1)
          if len(refPath)!=0:
              for r in refPath:
                  refRN=mc.file(r,q=1,rfn=1)
                  if(mc.file(r,q=1,dr=1)):
                      mc.file(refRN,loadReference=1)
                  mc.file(r,ir=1) 

    def csl_IDRenderLayerCreatAll(self,type='chr',ref=1):
        allRef = pm.system.listReferences()

        mapMatte = False
        for ref in allRef:
            if str(ref).find('csl_S012004WoodhouseGroup') > -1:
                mapMatte = True

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
                            print '------'
                            print idserpath
                            if idserpath.split('/')[-2] in mc.getFileList(folder=serverPath+'data/RLayerInfo/RGB/'):
                                folderFiles = mc.getFileList(folder=idserpath)
                                if folderFiles:
                                    for f in folderFiles:
                                      if re.match(objname,f,re.IGNORECASE):
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
                        needMeshFull = mc.ls((ns + ':MODEL'),l = 1)
                        needMeshFull += mc.ls((ns + ':*' + ':MODEL'),l = 1)#[0]  参考下面还有参考的情况
                        for i in range(10):
                            idserpath=serverPath+'data/RLayerInfo/RGB/id1'+str(i)+'/'
                            print '------'
                            print idserpath
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
            if mapMatte:
                rLayers = pm.ls('set_id*',type = 'renderLayer')
                
                for rLayer in rLayers:
                    rLayer.setCurrent() 
                    matteSg = self.csl_createMatteNode()
                    try:
                        pm.select('*S012004WoodhouseGroup*:MSH_c_hi_abatis*.f[120:121]', r = True)
                        pm.sets(matteSg,forceElement = True)
                    except:
                        pass

        mc.setAttr("defaultRenderLayer.renderable", 0)
        mc.editRenderLayerGlobals(currentRenderLayer="defaultRenderLayer")
        return 0

    def csl_createMatteNode(self):
        sg = ''
        if pm.objExists('S012004WoodhouseGroup_door_aiStandard_matte_SG'):
            sg = pm.PyNode('S012004WoodhouseGroup_door_aiStandard_matte_SG')
        else:
            fsl = pm.shadingNode('aiUtility', asShader=True, name= 'S012004WoodhouseGroup_door_aiStandard_matte')
            fsl.shadeMode.set(2)
            fsl.color.set(0,0,0)
            sg = pm.sets(renderable=True, noSurfaceShader=True,empty=True, name= fsl.name() + '_SG')
            fsl.outColor >> sg.surfaceShader

            fileNode = pm.createNode('file', name=fsl + '_file')
            fileNode.fileTextureName.set(r'//file-cluster/GDC/Projects/ShunLiu/Project/data/tx/Wire.png')
            fileNode.outAlpha >> fsl.opacity
        return sg



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
            if ns.split('_')[1][specialType] in ['c','p','s','C','P','S']:
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

        #print filePath
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
                if mc.ls(ns + ':MSH_all'):
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
                if namespaces[j] in meshs[i] and namespaces[j].split('_')[1][0].lower()==meshtype:
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
                                    try:
                                        mc.setAttr((mesh+'.aiSubdivType'),0)
                                    except:
                                        print(u'===============!!!物体中没有这个属性 【%s】!!!===============' % mesh+'.aiSubdivType')
                                else:                             
                                    mc.setAttr((mesh+'.aiSubdivType'),1)
                                    mc.setAttr((mesh+'.aiSubdivIterations'),smoothNum)
                                    if tangents==1:
                                        mc.setAttr((mesh+'.aiSubdivSmoothDerivs'),1)
                                    if tangents==0:
                                        mc.setAttr((mesh+'.aiSubdivSmoothDerivs'),0)                                                                                  
                                    
        print (u'===============!!!已经设置 【%s】!!!===============' % smoothInfo)
        return 0 

    def csl_SmoothSet(self):
        self.csl_FinalSmoothSet(smoothInfo='smooth_0',renderusing='arnold',tangents=0)
        self.csl_FinalSmoothSet(smoothInfo='smooth_1',renderusing='arnold',tangents=0) 
        self.csl_FinalSmoothSet(smoothInfo='smooth_2',renderusing='arnold',tangents=0)
        return 0
                                                          
 

    # 读文件
    def GA_ArnoldcheckFileRead(self, path):
        print u'>>>>>>[read]'
        print path
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
    def GA_ArnoldIdinfoDelete(self,id='id01'):
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        idserpath=serverPath+'data/RLayerInfo/RGB/'+id+'/'
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        if  mc.getFileList(folder=idserpath) and shotInfo[1] in mc.getFileList(folder=idserpath):
            hispath=idserpath+shotInfo[1]+'/his'
            mc.sysFile(hispath, makeDir=True)
            mc.sysFile(hispath,copy=shotInfo[1])
            mc.sysFile((idserpath+shotInfo[1]),delete=1)
        return 0

    #----------------------------------------------------------------------------------------------------------#      #----------------------------------------------------------#
        #------------------------------#
    # 【渲染】【Arnold渲染设置】【可以根据项目需求添加参数】
    #  Author  : 韩虹
    #  Data    : 2017_07_07
    #------------------------------#
    #根据不同渲染层类型设置
    def GA_DO6ArnoldRendererSettings(self,renderLayer='co',layertype='chr'):
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        print (u'===============!!!Start 【%s】!!!===============' % (u'Arnold设置'))
        print 'Working...'
        #加载arnold
        mc.setAttr('defaultRenderGlobals.imageFormat', 7)
        try:
           mc.loadPlugin('mtoa',qt=1)
        except:
            pass
        # 开启窗口，创建各种UI
        #mel.eval('unifiedRenderGlobalsWindow')
        renderglobal=mc.getAttr('defaultRenderGlobals.currentRenderer')
        if renderglobal!='arnold':
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'arnold', type='string')
        # 下来所需的节点提前创建
        import mtoa
        mtoa.core.createOptions()
        import mtoa.cmds.registerArnoldRenderer
        mtoa.cmds.registerArnoldRenderer.registerArnoldRenderer()
        samplingInfo=['defaultArnoldRenderOptions.AASamples','defaultArnoldRenderOptions.GIDiffuseSamples','defaultArnoldRenderOptions.GIGlossySamples','defaultArnoldRenderOptions.GIRefractionSamples','defaultArnoldRenderOptions.GISssSamples','defaultArnoldRenderOptions.GIVolumeSamples','defaultArnoldRenderOptions.lock_sampling_noise','defaultArnoldRenderOptions.sssUseAutobump']
        sampYak=[5,2,2,2,2,0,1,1]
        if shotInfo[0] in ['do6'] and renderLayer=='co' and layertype=='set':
            sampYak=[5,2,2,2,4,0,1,1]
        if shotInfo[0] in ['do6'] and renderLayer=='co' and layertype=='chr':
            sampYak=[5,2,2,2,3,0,0,0]
        if shotInfo[0] in ['do6'] and renderLayer in ['shadow','caustic','id31']:
            sampYak=[5,0,0,0,0,0,1,1]
        imageFormat=['defaultArnoldDriver.aiTranslator']
        imageYak=['exr']
        clamping=['defaultArnoldRenderOptions.use_sample_clamp','defaultArnoldRenderOptions.use_sample_clamp_AOVs','defaultArnoldRenderOptions.AASampleClamp']
        clamYak=[1,0,1.5]
        if shotInfo[0] in ['do6']:
            clamYak=[0,0,10]
        filterw=['defaultArnoldFilter.width']
        filtYak=[2]
        rayDepth=['defaultArnoldRenderOptions.GITotalDepth','defaultArnoldRenderOptions.GIDiffuseDepth','defaultArnoldRenderOptions.GIGlossyDepth','defaultArnoldRenderOptions.GIReflectionDepth','defaultArnoldRenderOptions.GIRefractionDepth','defaultArnoldRenderOptions.GIVolumeDepth','defaultArnoldRenderOptions.autoTransparencyDepth','defaultArnoldRenderOptions.autoTransparencyThreshold']
        rayYak=[3,1,1,2,2,0,2,0.990]
        motionblur=['defaultArnoldRenderOptions.motion_blur_enable','defaultArnoldRenderOptions.ignoreMotionBlur','defaultArnoldRenderOptions.range_type']
        motionYak=[0,0,1]
        if renderLayer=='motionblur':
            motionYak=[1,1,0]
        tex=['defaultArnoldRenderOptions.use_existing_tiled_textures']
        texYak=[1]
        AOV=['defaultArnoldDriver.mergeAOVs','defaultArnoldRenderOptions.aovMode','defaultArnoldDriver.prefix']
        AOVYak=[1,1,'']
        strInfo=['defaultArnoldDriver.aiTranslator','defaultArnoldDriver.prefix']
        infos=[samplingInfo,imageFormat,clamping,filterw,rayDepth,motionblur,tex,AOV]
        infoYak=[sampYak,imageYak,clamYak,filtYak,rayYak,motionYak,texYak,AOVYak]
        if shotInfo[0] in ['do6']:
            infoYak=[sampYak,imageYak,clamYak,filtYak,rayYak,motionYak,texYak,AOVYak]
        for i in range(len(infos)):
            for j in range(len(infos[i])):
                typeinfo=infos[i][j]
                typNum=infoYak[i][j]
                if typeinfo not in strInfo:
                    mc.setAttr(typeinfo,typNum)
                else:
                    mc.setAttr(typeinfo,typNum,type='string')
            mc.setAttr('defaultArnoldDriver.halfPrecision',1)
            mc.setAttr('defaultArnoldDriver.autocrop',1)
        result=u'================渲染参数已设置================'
        return result
    #----------------------------------------------------------------------------------------------------------#      #----------------------------------------------------------#
        #------------------------------#
    # 【渲染】【创建渲染层】【可以根据项目需求添加参数】
    #  Author  : 韩虹
    #  Data    : 2017_07_07
    #------------------------------#
    #根据不同渲染层类型设置
    #dele 是否删除AOV及渲染层
    #sm 是否smooth
    def DO6RenderLayerCreat(self,renderLayer='co',layertype='chr',dele=1,sm=1,save=1,shotType=2):
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        #渲染设置
        if renderLayer !='motionblur':
            self.GA_DO6ArnoldRendererSettings(renderLayer,layertype)

        if renderLayer in ['co']:
            objs=mc.ls(sl=1,l=1,tr=1)
            if not objs:
                mc.warning(u'请选择')
                mc.error(u'======请选择=====')
        elif renderLayer in ['caustic']:
            meshInfo=self.GA_MeshInfo('obj')
            objs=meshInfo[2]
            if not objs:
                mc.error(u'文件中缺少可渲染场景物体，请检查')
        else:
            meshInfo=self.GA_MeshInfo('obj')
            objs=meshInfo[0]+meshInfo[1]+meshInfo[2]
            if not objs:
                mc.error(u'文件中缺少可渲染物体，请检查')
        #删除渲染层及AOV
        if dele==1:
            self.ArnoldALLDelete(nodetype="aiAOV")
            self.ArnoldALLDelete(nodetype="renderLayer")
        #smooth
        if sm==1:
            self.csl_SmoothSet()
        mc.editRenderLayerGlobals(currentRenderLayer='defaultRenderLayer')

        #赋材质
        '''
        if renderLayer not in ['co','shadow','caustic','id31'] :
            self.csl_RefIm()
            meshInfo=self.GA_MeshInfo('obj')
            objs=meshInfo[0]+meshInfo[1]+meshInfo[2]
            if not objs:
                mc.error(u'文件中缺少可渲染物体，请检查')
            mc.select(objs)
            self.GA_ArnoldShaderAssign('Lambert',0)
        '''
        if renderLayer=='co':
            self.meshIDTransferD()
        if renderLayer=='shadow':
            self.csl_RefIm()
            meshInfo=self.GA_MeshInfo('mesh')
            chr=meshInfo[0]+meshInfo[1]
            set=meshInfo[2]
            if not chr:
                mc.error(u'文件中缺少可渲染角色或道具物体')
            if not set:
                mc.error(u'文件中缺少可渲染场景物体，请检查')
            for ch in chr:
                mc.setAttr((ch+'.primaryVisibility'),0)
            for se in set:
                mc.setAttr((se+'.castsShadows'),0)
                mc.setAttr((se+'.receiveShadows'),1)
            print u'=====shadow属性已经设置 #Arnold 设置====='
            mc.select(objs)
            self.GA_ArnoldShaderAssign('Shadow',0)
            print u'=====已赋shadow材质球====='
        if renderLayer=='caustic':
            self.csl_RefIm()
            mc.select(objs)
            self.GA_ArnoldShaderAssign('caustic',0)
        if renderLayer=='id31':
            self.csl_RefIm()
            if meshInfo==[[],[],[]]:
                mc.error(u'=====文件中缺少可渲染物体，请检查=====')
            idcolor=['ArnoldIdpR','ArnoldIdpG','ArnoldIdpB']
            for i in range(len(idcolor)):
                mc.select(meshInfo[i])
                try:
                    self.GA_ArnoldShaderAssign(idcolor[i])
                except:
                    pass
        if renderLayer=='motionblur':
            self.csl_RefIm()
            meshInfo=self.GA_MeshInfo('mesh')
            meshs=meshInfo[0]+meshInfo[1]+meshInfo[2]
            if not mc.ls(meshs):
                mc.error(u'=====文件中缺少可渲染物体，请检查=====')
            for mesh in objs:
                mc.setAttr((mesh+'.castsShadows'),1)
                mc.setAttr((mesh+'.receiveShadows'),1)
                mc.setAttr((mesh+'.primaryVisibility'),1)
            mc.select(objs)
            self.ArnoldMotionBlurShaderCreate()
            mc.setAttr("defaultRenderLayer.renderable", 0)
            mc.setAttr('defaultArnoldRenderOptions.motion_blur_enable',1)
            mc.setAttr('defaultArnoldRenderOptions.ignoreMotionBlur',1)
            mc.setAttr('defaultArnoldRenderOptions.motion_blur_enable',1)
            mc.setAttr('defaultArnoldRenderOptions.range_type',0)
            self.GA_ArnoldRendererSettings('mob')
        #创建AOV
        AOVs=[]
        if shotInfo[0] in ['do6'] and layertype == 'chr' and renderLayer in ['co']:
            typeListMesh=self.GA_AttrRead('chrID')
            AOVs=['AO','Fre','Normal','indirect_diffuse','direct_specular','sss','light_all','light_group','chrID']
            if not typeListMesh:
                AOVs.remove('chrID')
            print AOVs
        if shotInfo[0] in ['do6'] and layertype == 'set' and renderLayer in ['co']:
            AOVs=['AO','Fre','N','P','Shadow','Z','Zdp','indirect_diffuse','direct_diffuse','direct_specular','sss']
        if shotInfo[0] in ['do6'] and renderLayer == 'shadow':
            AOVs=['AO']
        if shotInfo[0] in ['do6'] and renderLayer in ['id31']:
            AOVs=['light_all','light_group']
            typeListLight=self.GA_AttrRead('light_group')
            if not typeListLight:
                AOVs.remove('light_all')
                AOVs.remove('light_group')
        if shotInfo[0] in ['do6'] and renderLayer in ['caustic']:
            AOVs=["setID"]
            typeListMesh=self.GA_AttrRead('setID')
            if not typeListMesh:
                AOVs.remove('setID')
        if AOVs:
            for aov in AOVs:
                if aov not in ['meshID','light_group','chrID','setID']:
                    self.GA_ArnoldAOVCreat(aov)
                else:
                    self.GA_speAOVCreat(aov)
        renderName=renderLayer
        if layertype=='chr' and renderLayer=='co':
            renderName='chr'
        if layertype=='set' and renderLayer=='co':
            renderName='set'
        if layertype=='shadow':
            renderName='shadow'
        if layertype=='caustic':
            renderName='caustic'
        #创建渲染层
        mc.createRenderLayer(objs,name=renderName, noRecurse=1, makeCurrent=1)
        #返回defaultRenderLayer
        mc.editRenderLayerGlobals(currentRenderLayer='defaultRenderLayer')
        mc.setAttr("defaultRenderLayer.renderable", 0)
        print u'========================【%s】渲染层已创建========================' %(renderName)
        if save==1:
            tempath=''
            if os.path.exists('E:'):
                tempath='E:/Info_Temp/render/'
            else:
                tempath='D:/Info_Temp/render/'
            shotName=''
            if shotType==2:
                tempath=tempath+shotInfo[0]+'/'+shotInfo[1]+'/'+shotInfo[2]+'/'
            if shotType==3:
                tempath=tempath+shotInfo[0]+'/'+shotInfo[1]+'/'+shotInfo[2]+'/'+shotInfo[3]+'/'
            mc.sysFile(tempath, makeDir=True)
            shotName=shotInfo[0]+'_'+shotInfo[1]+'_'+shotInfo[2]
            if shotType==3:
                shotName=shotInfo[0]+'_'+shotInfo[1]+'_'+shotInfo[2]+'_'+shotInfo[3]
            shotName=shotName+'_'+renderName+'_lr_c001'
            mc.file(rename=(tempath+shotName))
            fileTypeAll='mayaBinary'
            fileForm='.mb'
            if shotInfo[0] in ['do6']:
                mc.file(rename=(tempath+shotName+fileForm))
                mc.file(save=1,type = fileTypeAll,f = 1)
            print u'========================【%s】========================' %(tempath+shotName+fileForm)
        return 0
    #------------------------------#
    # 【辅】【判断角色，场景，道具polygon物体】
    #  Author  : 韩虹
    #  Data    : 2017_07
        #------------------------------#
    def GA_MeshInfo(self,ty='mesh'):
        if ty=='mesh':
            meshs=mc.ls(type='mesh',l=1)
        else:
            meshs=mc.ls(tr=1,l=1)
        if not meshs:
            mc.error(u'文件中没有polygon物体，请检查')
        meshchr=[]
        meshpro=[]
        meshset=[]
        for mesh in meshs:
            if ty =='mesh' and 'SET_GRP' in mesh and mesh not in meshset and 'MODEL' in mesh:
                meshset.append(mesh)
            if ty =='mesh' and 'CHR_GRP' in mesh and mesh not in meshchr and 'MODEL' in mesh:
                meshchr.append(mesh)
            if ty =='mesh' and 'PRP_GRP' in mesh and mesh not in meshpro and 'MODEL' in mesh:
                meshpro.append(mesh)
            if ty!='mesh' and 'SET_GRP' in mesh and mesh not in meshset and 'MODEL' in mesh and mc.listRelatives(mesh,s=1,type='mesh'):
                meshset.append(mesh)
            if ty!='mesh' and 'CHR_GRP' in mesh and mesh not in meshchr and 'MODEL' in mesh and mc.listRelatives(mesh,s=1,type='mesh'):
                meshchr.append(mesh)
            if ty!='mesh' and 'PRP_GRP' in mesh and mesh not in meshpro and 'MODEL' in mesh and mc.listRelatives(mesh,s=1,type='mesh'):
                meshpro.append(mesh)
        result=[meshchr,meshpro,meshset]
        return result
    #------------------------------#
    # 【辅】【设置参数】【用于shadow】
    #  Author  : 韩虹
    #  Data    : 2017_07
        #------------------------------#
    def GA_MeshSet(self,renderLayer='shadow'):
        meshInfo=self.GA_MeshInfo('mesh')
        if not meshInfo:
            mc.error(u'文件中没有可渲染模型，请检查')
        chr=meshInfo[0]+meshInfo[1]
        set=meshInfo[2]
        if not chr:
            mc.error(u'文件中没有可渲染角色或道具模型，请检查')
        if not set:
            mc.error(u'文件中没有可渲染场景模型，请检查')
        for ch in chr:
            mc.setAttr((ch+'.primaryVisibility'),0)
        for se in set:
            mc.setAttr((se+'.castsShadows'),0)
            mc.setAttr((se+'.receiveShadows'),1)
        return 0
    #------------------------------#
    # 【辅】【mesh信息】
    #  Author  : 韩虹
    #  Data    : 2017_07
        #------------------------------#
    def GA_meshInfoRead(self,ty='mesh'):
        meshs=mc.ls(type='mesh',l=1)
        if not meshs:
            mc.error(u'文件中没有polygon物体，请检查')
        meshchr=[]
        meshpro=[]
        meshset=[]
        for mesh in meshs:
            if ty=='mesh' and 'SET_GRP' in mesh and mesh not in meshset and 'MODEL' in mesh:
                meshset.append(mesh)
            if ty=='mesh' and 'CHR_GRP' in mesh and mesh not in meshchr and 'MODEL' in mesh:
                meshchr.append(mesh)
            if ty=='mesh' and 'PRP_GRP' in mesh and mesh not in meshpro and 'MODEL' in mesh:
                meshpro.append(mesh)
            if ty!='mesh' and 'SET_GRP' in mesh and mesh not in meshset and 'MODEL' in mesh and mc.listRelatives(mesh,p=1,type='transform'):
                objs=mc.listRelatives(mesh,p=1,type='transform',f=1)
                meshset.append(objs[0])
            if ty!='mesh' and 'CHR_GRP' in mesh and mesh not in meshchr and 'MODEL' in mesh and mc.listRelatives(mesh,p=1,type='transform'):
                objs=mc.listRelatives(mesh,p=1,type='transform',f=1)
                meshset.append(objs[0])
            if ty!='mesh' and 'PRP_GRP' in mesh and mesh not in meshpro and 'MODEL' in mesh and mc.listRelatives(mesh,p=1,type='transform'):
                objs=mc.listRelatives(mesh,p=1,type='transform',f=1)
                meshset.append(objs[0])
        result=[meshchr,meshpro,meshset]
        return result
    #------------------------------#
    # 【通用】【物体添加ID属性】
    #  Author  : 韩虹
    #  Data    : 2017_07
        #------------------------------#
    def GA_ArnoldIDSet(self,line='del',idtype='G',id='chrId01'):
        num=[]
        if idtype=='R':
            num=[1,0,0]
        if idtype=='G':
            num=[0,1,0]
        if idtype=='B':
            num=[0,0,1]
        objs=mc.ls(sl=1,l=1,tr=1)
        if not objs:
            mc.error(u'============please select============')
        attr='mtoa_constant_'+id
        for obj in objs:
            meshs=mc.listRelatives(obj,s=1,f=1,type='mesh')
            if line=='set' and meshs and  not mc.objExists(meshs[0]+'.'+attr):
                try:
                    mc.addAttr(meshs[0],longName=attr,at='double3')
                    mc.addAttr(meshs[0],longName=attr+'X',at='double',p=attr)
                    mc.addAttr(meshs[0],longName=attr+'Y',at='double',p=attr)
                    mc.addAttr(meshs[0],longName=attr+'Z',at='double',p=attr)
                    mc.setAttr((meshs[0]+'.'+attr+'X'),num[0])
                    mc.setAttr((meshs[0]+'.'+attr+'Y'),num[1])
                    mc.setAttr((meshs[0]+'.'+attr+'Z'),num[2])
                except:
                    pass
            if line=='set' and meshs and   mc.objExists(meshs[0]+'.'+attr):
                try:
                    mc.setAttr((meshs[0]+'.'+attr+'X'),num[0])
                    mc.setAttr((meshs[0]+'.'+attr+'Y'),num[1])
                    mc.setAttr((meshs[0]+'.'+attr+'Z'),num[2])
                except:
                    pass
            if line=='del' and meshs and   mc.objExists(meshs[0]+'.'+attr):
                try:
                    mc.deleteAttr(meshs[0], at=attr)
                except:
                    pass
        return 0
    #------------------------------#
    # 【通用】【物体添加ID属性】
    #  Author  : 韩虹
    #  Data    : 2017_07
        #------------------------------#
    def GA_ArnoldIDDelempty(self):
        objs=mc.ls(type='mesh',l=1)
        if not objs:
            mc.error(u'============文件中缺少polygon物============')
        attr='mtoa_constant_'
        for obj in objs:
            if mc.objExists(obj+'.'+attr):
                try:
                    mc.deleteAttr(obj, at=attr)
                except:
                    pass
            Attrs=mc.sys
            if mc.objExists(obj+'.'+attr):
                try:
                    mc.deleteAttr(obj, at=attr)
                except:
                    pass
        return 0
    #------------------------------#
    # 【辅】【shapeDeformed meshID属性传递】
    #  Author  : 韩虹
    ##  Data    : 2017_05
        #------------------------------#
    def meshIDTransferD(self):
        objList=[]
        IDLists=[]
        meshs=mc.ls(type='mesh',l=1)
        for i  in range(len(meshs)):
            Attrs=mc.listAttr(meshs[i], r=True ,st='mtoa_constant_*')
            objs=mc.listRelatives(meshs[i],p=1,f=1)
            if 'Deformed' not in meshs[i] and Attrs and  len (Attrs)>3 and objs and objs[0] not in objList:
                objList.append(objs[0])
                IDLists.append([Attrs[0],[Attrs[1],mc.getAttr(meshs[i]+'.'+Attrs[1])],[Attrs[2],mc.getAttr(meshs[i]+'.'+Attrs[2])],[Attrs[3],mc.getAttr(meshs[i]+'.'+Attrs[3])]])
        if not objList:
            mc.error(u'文件中没有meshID属性物体')
        for j in range(len(objList)):
            shapes=mc.listRelatives(objList[j],s=1,f=1,type='mesh')
            if mc.objExists(shapes[0]+'.'+IDLists[j][0]):
                for shape in shapes:
                    if  'Deformed' in shape and not mc.objExists(shape+'.'+IDLists[j][0]):
                        try:
                            mc.addAttr(shape,longName=IDLists[j][0],at='double3')
                            mc.addAttr(shape,longName=IDLists[j][1][0],at='double',p=IDLists[j][0])
                            mc.addAttr(shape,longName=IDLists[j][2][0],at='double',p=IDLists[j][0])
                            mc.addAttr(shape,longName=IDLists[j][3][0],at='double',p=IDLists[j][0])
                            mc.setAttr((shape+'.'+IDLists[j][1][0]),IDLists[j][1][1])
                            mc.setAttr((shape+'.'+IDLists[j][2][0]),IDLists[j][2][1])
                            mc.setAttr((shape+'.'+IDLists[j][3][0]),IDLists[j][3][1])
                            print(u'已传递【%s】的meshID属性' %shape)
                        except:
                            mc.warning(u'【%s】无法添加【%s】属性，请检查' %shape %IDLists[j][0])
        return 0
