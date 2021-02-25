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
class GA_RedShiftTools(object):
    def __init__(self):
        pass
    #----------------------------------------------------------------------------------------------------------#      #----------------------------------------------------------#
        #------------------------------#
    # 【渲染】【Redshift渲染工具】
    #  Author  : 韩虹
    #  Data    : 2017_04_18
    #------------------------------#

    def GA_RedShiftToolsUI(self):
    # 窗口
        if mc.window('GA_RenderRedshift', exists=True):
            mc.deleteUI('GA_RenderRedshift')
        mc.window('GA_RenderRedshift', title=u'Redshift 工具面板',
                  width=320, height=350, sizeable=True)
         # 面板
        form = mc.formLayout()
         # 切换面板
        tabs = mc.tabLayout('tabRedshift',innerMarginWidth=3, innerMarginHeight=3)
        mc.formLayout(
            form, edit=True, attachForm=((tabs, 'top', 0), (tabs, 'left', 0), (tabs, 'bottom', 0), (tabs, 'right', 0)))
         # tab_渲染工具
        child1 = mc.columnLayout(adjustableColumn=True)
        mc.image(
            image='//file-cluster/GDC/Resource/Support/Maya/icons/GA/sun01.png')
        mc.frameLayout(label=u'预设工具', bgc=[0, 0, 0.0], borderStyle='in', cll=0,cl=0)
        mc.rowColumnLayout(numberOfColumns=1)
        mc.button(label=u'HDR', bgc=[0, 0, 0.0],width=360, height=50, command='from idmt.maya.GA import GA_PresetRedshift\nreload(GA_PresetRedshift)\nGA_PresetRedshift.main()')
        mc.button(label=u'材质预设', bgc=[0, 0, 0.0],width=360, height=50, command='from idmt.maya.GA import GA_nodePresets\nreload(GA_nodePresets)\nGA_nodePresets.main()')
        mc.button(label=u'Transfer', bgc=[0, 0, 0.0], width=360,height=50, command='from idmt.maya.GA import GA_shaderTransfer\nreload(GA_shaderTransfer)\nGA_shaderTransfer.main()')
        mc.setParent('..')
        mc.setParent('..')
        mc.frameLayout(label=u'灯光命名工具', bgc=[0, 0, 0.0], borderStyle='in', cll=1,cl=1)
        mc.rowColumnLayout(numberOfColumns=4)
        mc.button(label=u'chrkeyLight',width=90,height=30,bgc=[0.7,0.3,0.2],command='from idmt.maya.GA import GA_PreCheck\nreload(GA_PreCheck)\nGA_PreCheck.GA_PreCheck().GA_PreLightRename("RS","key","chr")')
        mc.button(label=u'chrfilLight',width=90,height=30,bgc=[0.3,0.7,0.2],command='from idmt.maya.GA import GA_PreCheck\nreload(GA_PreCheck)\nGA_PreCheck.GA_PreCheck().GA_PreLightRename("RS","fill","chr")')
        mc.button(label=u'chrrimLight',width=90,height=30,bgc=[0.2,0.3,0.7],command='from idmt.maya.GA import GA_PreCheck\nreload(GA_PreCheck)\nGA_PreCheck.GA_PreCheck().GA_PreLightRename("RS","rim","chr")')
        mc.button(label=u'chrrsDomeLight',width=90,height=30,bgc=[0.1,0.2,0.4],command='from idmt.maya.GA import GA_PreCheck\nreload(GA_PreCheck)\nGA_PreCheck.GA_PreCheck().GA_PreLightRename("RS","rs","chr")')

        mc.button(label=u'setkeyLight',width=90,height=30,bgc=[0.7,0.3,0.2],command='from idmt.maya.GA import GA_PreCheck\nreload(GA_PreCheck)\nGA_PreCheck.GA_PreCheck().GA_PreLightRename("RS","key","set")')
        mc.button(label=u'setfilLight',width=90,height=30,bgc=[0.3,0.7,0.2],command='from idmt.maya.GA import GA_PreCheck\nreload(GA_PreCheck)\nGA_PreCheck.GA_PreCheck().GA_PreLightRename("RS","fill","set")')
        mc.button(label=u'setrimLight',width=90,height=30,bgc=[0.2,0.3,0.7],command='from idmt.maya.GA import GA_PreCheck\nreload(GA_PreCheck)\nGA_PreCheck.GA_PreCheck().GA_PreLightRename("RS","rim","set")')
        mc.button(label=u'setrsDomeLight',width=90,height=30,bgc=[0.1,0.2,0.4],command='from idmt.maya.GA import GA_PreCheck\nreload(GA_PreCheck)\nGA_PreCheck.GA_PreCheck().GA_PreLightRename("RS","rs","set")')
        mc.setParent('..')
        mc.setParent('..')
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
                  0, 0, 0.0], width=110, height=30, command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RSAOVCreat("AO","creat")')
        mc.button(
            label=u'删除', bgc=[0, 0, 0.0], width=110, height=30, command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RSAOVCreat("AO","delete")')
        collectionnormal = mc.radioCollection()
        # Normal
        normalset = mc.checkBox('GAcheckN',label='N', visible=1, v=1,
                             bgc=[0.13, 0.15, 0.25], height=30, width=130)
        mc.button(label=u'创建', bgc=[
                  0, 0, 0.0], width=110, height=30, command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RSAOVCreat("N","creat")')
        mc.button(
            label=u'删除', bgc=[0, 0, 0.0], width=110, height=30, command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RSAOVCreat("N","delete")')
        collectionfre = mc.radioCollection()
        # P
        Pset = mc.checkBox('GAcheckP',label='P', visible=1, v=1,
                             bgc=[0.13, 0.15, 0.25], height=30, width=130)
        mc.button(label=u'创建', bgc=[
                  0, 0, 0.0], width=110, height=30, command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RSAOVCreat("P","creat")')
        mc.button(
            label=u'删除', bgc=[0, 0, 0.0], width=110, height=30, command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RSAOVCreat("P","delete")')
        collectionfre = mc.radioCollection()

        # Z
        Zset = mc.checkBox('GAcheckZ',label='Z', visible=1, v=1,
                             bgc=[0.13, 0.15, 0.25], height=30, width=130)
        mc.button(label=u'创建', bgc=[
                  0, 0, 0.0], width=110, height=30, command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RSAOVCreat("Z","creat")')
        mc.button(
            label=u'删除', bgc=[0, 0, 0.0], width=110, height=30, command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RSAOVCreat("Z","delete")')
        collectionkey = mc.radioCollection()

        # SSS
        SSSset = mc.checkBox('GAcheckSSS',label='SSS', visible=1, v=1,
                             bgc=[0.13, 0.15, 0.25], height=30, width=130)
        mc.button(label=u'创建', bgc=[
                  0, 0, 0.0], width=110, height=30, command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RSAOVCreat("SSS","creat")')
        mc.button(
            label=u'删除', bgc=[0, 0, 0.0], width=110, height=30, command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RSAOVCreat("SSS","delete")')
        collectionfre = mc.radioCollection()
        #DiffuseLighting
        Difset = mc.checkBox('GAcheckDiffuseLighting',label='DiffuseLighting', visible=1,
                             v=1, bgc=[0.13, 0.15, 0.25], height=30, width=130)
        mc.button(label=u'创建', bgc=[
                  0, 0, 0.0], width=110, height=30, command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RSAOVCreat("DiffuseLighting","creat")')
        mc.button(
            label=u'删除', bgc=[0, 0, 0.0], width=110, height=30, command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RSAOVCreat("DiffuseLighting","delete")')
                
        collectionzdp = mc.radioCollection()        
        #DiffuseFilter
        Difset = mc.checkBox('GAcheckDiffuseFilter',label='DiffuseFilter', visible=1,
                             v=1, bgc=[0.13, 0.15, 0.25], height=30, width=130)
        mc.button(label=u'创建', bgc=[
                  0, 0, 0.0], width=110, height=30, command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RSAOVCreat("DiffuseFilter","creat")')
        mc.button(
            label=u'删除', bgc=[0, 0, 0.0], width=110, height=30, command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RSAOVCreat("DiffuseFilter","delete")')

        collectionzdp = mc.radioCollection()

        # Emission
        zdepthset = mc.checkBox('GAcheckEmission',label='Emission', visible=1, v=1,
                             bgc=[0.13, 0.15, 0.25], height=30, width=130)
        mc.button(label=u'创建', bgc=[
                  0, 0, 0.0], width=110, height=30, command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RSAOVCreat("Emission","creat")')
        mc.button(
            label=u'删除', bgc=[0, 0, 0.0], width=110, height=30, command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RSAOVCreat("Emission","delete")')
        # GI
        shadowset = mc.checkBox('GAcheckGI',label='GI', visible=1,
                             v=1, bgc=[0.13, 0.15, 0.25], height=30, width=130)
        mc.button(label=u'创建', bgc=[
                  0, 0, 0.0], width=110, height=30, command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RSAOVCreat("GI","creat")')
        mc.button(
            label=u'删除', bgc=[0, 0, 0.0], width=110, height=30, command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RSAOVCreat("GI","delete")')
        collectionzdp = mc.radioCollection()
        # GIRaw
        shadowset = mc.checkBox('GAcheckGIRaw',label='GIRaw', visible=1,
                             v=1, bgc=[0.13, 0.15, 0.25], height=30, width=130)
        mc.button(label=u'创建', bgc=[
                  0, 0, 0.0], width=110, height=30, command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RSAOVCreat("GIRaw","creat")')
        mc.button(
            label=u'删除', bgc=[0, 0, 0.0], width=110, height=30, command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RSAOVCreat("GIRaw","delete")')
        collectionzdp = mc.radioCollection()

        # Matte
        shadowset = mc.checkBox('GAcheckMatte',label='Matte', visible=1,
                             v=1, bgc=[0.13, 0.15, 0.25], height=30, width=130)
        mc.button(label=u'创建', bgc=[
                  0, 0, 0.0], width=110, height=30, command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RSAOVCreat("Matte","creat")')
        mc.button(
            label=u'删除', bgc=[0, 0, 0.0], width=110, height=30, command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RSAOVCreat("Matte","delete")')
        collectionzdp = mc.radioCollection()

        # MotionVectors
        shadowset = mc.checkBox('GAcheckMotionVectors',label='MotionVectors', visible=1,
                             v=0, bgc=[0.13, 0.15, 0.25], height=30, width=130)
        mc.button(label=u'创建', bgc=[
                  0, 0, 0.0], width=110, height=30, command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RSAOVCreat("MotionVectors","creat")')
        mc.button(
            label=u'删除', bgc=[0, 0, 0.0], width=110, height=30, command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RSAOVCreat("MotionVectors","delete")')
        '''
        collectionzdp = mc.radioCollection()

        # ObjectID

        shadowset = mc.checkBox('GAcheckID',label='ObjectID', visible=1,
                             v=1, bgc=[0.13, 0.15, 0.25], height=30, width=130)
        mc.button(label=u'创建', bgc=[
                  0, 0, 0.0], width=110, height=30, command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RSAOVCreat("ID","creat")')
        mc.button(
            label=u'删除', bgc=[0, 0, 0.0], width=110, height=30, command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RSAOVCreat("ID","delete")')
     '''
        collectionzdp = mc.radioCollection()

        # chrID
        shadowset = mc.checkBox('GAcheckchrID',label='chrID', visible=1,
                             v=1, bgc=[0.13, 0.15, 0.25], height=30, width=130)
        mc.button(label=u'创建', bgc=[
                  0, 0, 0.0], width=110, height=30, command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RSAOVCreatSP("PuzzleMatte","creat","chrID")')
        mc.button(
            label=u'删除', bgc=[0, 0, 0.0], width=110, height=30, command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RSAOVCreatSP("PuzzleMatte","delete","chrID")')
        collectionzdp = mc.radioCollection()


        # setID
        shadowset = mc.checkBox('GAchecksetID',label='setID', visible=1,
                             v=1, bgc=[0.13, 0.15, 0.25], height=30, width=130)
        mc.button(label=u'创建', bgc=[
                  0, 0, 0.0], width=110, height=30, command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RSAOVCreatSP("PuzzleMatte","creat","setID")')
        mc.button(
            label=u'删除', bgc=[0, 0, 0.0], width=110, height=30, command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RSAOVCreatSP("PuzzleMatte","delete","setID")')
        collectionzdp = mc.radioCollection()

        # Reflections
        shadowset = mc.checkBox('GAcheckReflections',label='Reflections', visible=1,
                             v=1, bgc=[0.13, 0.15, 0.25], height=30, width=130)
        mc.button(label=u'创建', bgc=[
                  0, 0, 0.0], width=110, height=30, command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RSAOVCreat("Reflections","creat")')
        mc.button(
            label=u'删除', bgc=[0, 0, 0.0], width=110, height=30, command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RSAOVCreat("Reflections","delete")')
        collectionzdp = mc.radioCollection()
        # Refractions
        shadowset = mc.checkBox('GAcheckRefractions',label='Refractions', visible=1,
                             v=1, bgc=[0.13, 0.15, 0.25], height=30, width=130)
        mc.button(label=u'创建', bgc=[
                  0, 0, 0.0], width=110, height=30, command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RSAOVCreat("Refractions","creat")')
        mc.button(
            label=u'删除', bgc=[0, 0, 0.0], width=110, height=30, command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RSAOVCreat("Refractions","delete")')
        collectionzdp = mc.radioCollection()
        # Shadows
        shadowset = mc.checkBox('GAcheckShadows',label='Shadows', visible=1,
                             v=0, bgc=[0.13, 0.15, 0.25], height=30, width=130)
        mc.button(label=u'创建', bgc=[
                  0, 0, 0.0], width=110, height=30, command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RSAOVCreat("Shadows","creat")')
        mc.button(
            label=u'删除', bgc=[0, 0, 0.0], width=110, height=30, command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RSAOVCreat("Shadows","delete")')
        collectionzdp = mc.radioCollection()
        # SpecularLighting
        shadowset = mc.checkBox('GAcheckSpecularLighting',label='SpecularLighting', visible=1,
                             v=1, bgc=[0.13, 0.15, 0.25], height=30, width=130)
        mc.button(label=u'创建', bgc=[
                  0, 0, 0.0], width=110, height=30, command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RSAOVCreat("SpecularLighting","creat")')
        mc.button(
            label=u'删除', bgc=[0, 0, 0.0], width=110, height=30, command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RSAOVCreat("SpecularLighting","delete")')
        collectionzdp = mc.radioCollection()

        # VolumeLighting
        zdepthset = mc.checkBox('GAcheckVolumeLighting',label='VolumeLighting', visible=1, v=0,
                             bgc=[0.13, 0.15, 0.25], height=30, width=130)
        mc.button(label=u'创建', bgc=[
                  0, 0, 0.0], width=110, height=30, command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RSAOVCreat("VolumeLighting","creat")')
        mc.button(
            label=u'删除', bgc=[0, 0, 0.0], width=110, height=30, command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RSAOVCreat("VolumeLighting","delete")')

        collectionid01 = mc.radioCollection()
        mc.setParent('..')

        mc.setParent('..')
        # 一键式创建AOV层
        mc.frameLayout(label=u'一键式创建（删除）工具', bgc=[0, 0, 0.0], borderStyle='in',cll=1,cl=0)
        mc.rowColumnLayout(numberOfColumns=3)
        mc.button(label=u'创建渲染层', width=130, height=30,
                  bgc=[0.13, 0.15, 0.25], command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RedshiftRendererLayerCreat()')
        mc.button(label=u'删除所有AOV', width=110,
                  height=30, bgc=[0, 0, 0.0], command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().RedShiftALLDelete("RedshiftAOV")')
        mc.button(label=u'删除所有渲染层', width=110,
                  height=30, bgc=[0, 0, 0.0], command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().RedShiftALLDelete("renderLayer")')
        mc.setParent('..')
        mc.setParent('..')
        mc.frameLayout(label=u'常用工具', bgc=[0, 0, 0.0], borderStyle='in',cll=1,cl=0)
        mc.rowColumnLayout(numberOfColumns=2)
        mc.button(label=u'Redshift渲染设置(前期)', width=180, height=30,
                  bgc=[0.13, 0.6, 0.25], command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_rsRendererSettings("co",2,0)')
        mc.button(label=u'Redshift渲染设置(渲染)', width=180, height=30,
                  bgc=[0, 0, 0.0], command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_rsRendererSettings("co",2,1)')
        mc.button(label=u'smooth', width=180, height=30,
                  bgc=[0.5, 0.5, 0.5], command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RSmoothSet()')
        mc.setParent('..')
        mc.setParent('..')        
        mc.setParent('..')                
        # 渲染常用工具组
        child3 = mc.columnLayout(adjustableColumn=True)
        #idp材质工具
        mc.frameLayout(label=u'IDP材质工具', bgc=[0, 0, 0.0], borderStyle='in', cll=1,cl=1)
        mc.rowColumnLayout(numberOfColumns=4)
        mc.button(label=u'R',width=90,height=30,bgc=[1,0,0],command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RSIDCreat("RSIdpR")')
        mc.button(label=u'G',width=90,height=30,bgc=[0,1,0],command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RSIDCreat("RSIdpG")')
        mc.button(label=u'B',width=90,height=30,bgc=[0,0,1],command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RSIDCreat("RSIdpB")')
        mc.button(label=u'M',width=90,height=30,bgc=[0,0,0],command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RSIDCreat("RSIdpM")')
        mc.button(label=u'A',width=90,height=30,bgc=[1,1,1],command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RSIDCreat("RSIdpA")')
        mc.setParent('..')
        mc.setParent('..')
        #ID属性添加工具
        mc.frameLayout(label=u'角色ID属性工具', bgc=[0, 0, 0], borderStyle='etchedIn', cll=1,cl=0)
        mc.rowColumnLayout(numberOfColumns=5)
        mc.iconTextCheckBox(al='left', bgc=[0.2, 0.3, 0.1],olc=[0, 1 ,0],width=80, height=30,style='iconAndTextVertical', image1='plane.png', label='chrID01' )
        mc.button(label=u'R', width=50, height=30, bgc=[1, 0, 0], command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RedshitIDSet("objectID","chrID01","R")')
        mc.button(label=u'G',width=50, height=30,bgc=[0, 1, 0.0], command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RedshitIDSet("objectID","chrID01","G")')
        mc.button(label=u'B',width=50, height=30,bgc=[0, 0, 1], command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RedshitIDSet("objectID","chrID01","B")')
        mc.button(label=u'M',width=80, height=30,bgc=[0, 0, 0], command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RedshitIDSet("objectID","chrID01","M")')
        #chrID02
        mc.iconTextCheckBox(al='left', bgc=[0.2, 0.3, 0.1],olc=[0, 1 ,0],width=80, height=30,style='iconAndTextVertical', image1='plane.png', label='chrID02' )
        mc.button(label=u'R', width=50, height=30, bgc=[1, 0, 0], command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RedshitIDSet("objectID","chrID02","R")')
        mc.button(label=u'G',width=50, height=30,bgc=[0, 1, 0.0], command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RedshitIDSet("objectID","chrID02","G")')
        mc.button(label=u'B',width=50, height=30,bgc=[0, 0, 1], command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RedshitIDSet("objectID","chrID02","B")')
        mc.button(label=u'M',width=80, height=30,bgc=[0, 0, 0], command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RedshitIDSet("objectID","chrID01","M")')

        #chrID03
        mc.iconTextCheckBox(al='left', bgc=[0.2, 0.3, 0.1],olc=[0, 1 ,0],width=80, height=30,style='iconAndTextVertical', image1='plane.png', label='chrID03' )
        mc.button(label=u'R', width=50, height=30, bgc=[1, 0, 0], command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RedshitIDSet("objectID","chrID03","R")')
        mc.button(label=u'G',width=50, height=30,bgc=[0, 1, 0.0], command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RedshitIDSet("objectID","chrID03","G")')
        mc.button(label=u'B',width=50, height=30,bgc=[0, 0, 1], command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RedshitIDSet("objectID","chrID03","B")')
        mc.button(label=u'M',width=80, height=30,bgc=[0, 0, 0], command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RedshitIDSet("objectID","chrID03","M")')

        #chrID04
        mc.iconTextCheckBox(al='left', bgc=[0.2, 0.3, 0.1],olc=[0, 1 ,0],width=80, height=30,style='iconAndTextVertical', image1='plane.png', label='chrID04' )
        mc.button(label=u'R', width=50, height=30, bgc=[1, 0, 0], command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RedshitIDSet("objectID","chrID04","R")')
        mc.button(label=u'G',width=50, height=30,bgc=[0, 1, 0.0], command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RedshitIDSet("objectID","chrID04","G")')
        mc.button(label=u'B',width=50, height=30,bgc=[0, 0, 1], command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RedshitIDSet("objectID","chrID04","B")')
        mc.button(label=u'M',width=80, height=30,bgc=[0, 0, 0], command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RedshitIDSet("objectID","chrID04","M")')
        mc.setParent('..')
        mc.setParent('..')
        #setID01
        mc.frameLayout(label=u'场景ID属性工具', bgc=[0, 0, 0], borderStyle='etchedIn', cll=1,cl=0)
        mc.rowColumnLayout(numberOfColumns=5)
        mc.iconTextCheckBox(al='left', bgc=[0.13, 0.15, 0.25],olc=[0, 1 ,0],width=80, height=30,style='iconAndTextVertical', image1='plane.png', label='setID01' )
        mc.button(label=u'R', width=50, height=30, bgc=[1, 0, 0], command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RedshitIDSet("objectID","setID01","R")')
        mc.button(label=u'G',width=50, height=30,bgc=[0, 1, 0.0], command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RedshitIDSet("objectID","setID01","G")')
        mc.button(label=u'B',width=50, height=30,bgc=[0, 0, 1], command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RedshitIDSet("objectID","setID01","B")')
        mc.button(label=u'M',width=80, height=30,bgc=[0, 0, 0], command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RedshitIDSet("objectID","setID01","M")')
        #setID02
        mc.iconTextCheckBox(al='left', bgc=[0.13, 0.15, 0.25],olc=[0, 1 ,0],width=80, height=30,style='iconAndTextVertical', image1='plane.png', label='setID02' )
        mc.button(label=u'R', width=50, height=30, bgc=[1, 0, 0], command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RedshitIDSet("objectID","setID02","R")')
        mc.button(label=u'G',width=50, height=30,bgc=[0, 1, 0.0], command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RedshitIDSet("objectID","setID02","G")')
        mc.button(label=u'B',width=50, height=30,bgc=[0, 0, 1], command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RedshitIDSet("objectID","setID02","B")')
        mc.button(label=u'M',width=80, height=30,bgc=[0, 0, 0], command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RedshitIDSet("objectID","setID02","M")')
        #setID03
        mc.iconTextCheckBox(al='left', bgc=[0.13, 0.15, 0.25],olc=[0, 1 ,0],width=80, height=30,style='iconAndTextVertical', image1='plane.png', label='setID03' )
        mc.button(label=u'R', width=50, height=30, bgc=[1, 0, 0], command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RedshitIDSet("objectID","setID03","R")')
        mc.button(label=u'G',width=50, height=30,bgc=[0, 1, 0.0], command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RedshitIDSet("objectID","setID03","G")')
        mc.button(label=u'B',width=50, height=30,bgc=[0, 0, 1], command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RedshitIDSet("objectID","setID03","B")')
        mc.button(label=u'M',width=80, height=30,bgc=[0, 0, 0], command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RedshitIDSet("objectID","setID03","M")')
        #setID04
        mc.iconTextCheckBox(al='left', bgc=[0.13, 0.15, 0.25],olc=[0, 1 ,0],width=80, height=30,style='iconAndTextVertical', image1='plane.png', label='setID04' )
        mc.button(label=u'R', width=50, height=30, bgc=[1, 0, 0], command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RedshitIDSet("objectID","setID04","R")')
        mc.button(label=u'G',width=50, height=30,bgc=[0, 1, 0.0], command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RedshitIDSet("objectID","setID04","G")')
        mc.button(label=u'B',width=50, height=30,bgc=[0, 0, 1], command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RedshitIDSet("objectID","setID04","B")')
        mc.button(label=u'M',width=80, height=30,bgc=[0, 0, 0], command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RedshitIDSet("objectID","setID04","M")')
        #setID05
        mc.iconTextCheckBox(al='left', bgc=[0.13, 0.15, 0.25],olc=[0, 1 ,0],width=80, height=30,style='iconAndTextVertical', image1='plane.png', label='setID05')
        mc.button(label=u'R', width=50, height=30, bgc=[1, 0, 0], command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RedshitIDSet("objectID","setID05","R")')
        mc.button(label=u'G',width=50, height=30,bgc=[0, 1, 0.0], command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RedshitIDSet("objectID","setID05","G")')
        mc.button(label=u'B',width=50, height=30,bgc=[0, 0, 1], command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RedshitIDSet("objectID","setID05","B")')
        mc.button(label=u'M',width=80, height=30,bgc=[0, 0, 0], command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RedshitIDSet("objectID","setID05","M")')
        mc.setParent('..')
        mc.setParent('..')
        mc.setParent('..')

        # DDZ项目渲染工具
        child4 = mc.columnLayout(adjustableColumn=True)
        mc.frameLayout(label=u'DDZ项目渲染层工具', bgc=[0, 0, 0.0], borderStyle='etchedIn', cll=0,cl=1)
        mc.rowColumnLayout(numberOfColumns=4)
        mc.button(label=u'CHRCO',width=90,height=30,bgc=[0.13, 0.15, 0.25],command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RSRenderLayerCreat("co","chr",0,1,1,1,2,1,1)')
        mc.button(label=u'SETCO',width=90,height=30,bgc=[0.13, 0.15, 0.25],command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RSRenderLayerCreat("co","set",0,1,1,1,2,1,1)')
        mc.button(label=u'ChrLight',width=90,height=30,bgc=[0.13, 0.15, 0.25],command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RSRenderLayerCreat("light","chr",0,1,1,1,2,1,1)')
        mc.button(label=u'IDP31',width=90,height=30,bgc=[0.13, 0.15, 0.25],command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RSRenderLayerCreat("id31","",0,1,1,1,2,1,1)')
        mc.button(label=u'优化(渲染)',width=90,height=30,bgc=[0.13, 0.6, 0.25],command='from idmt.maya.GA import DDZ_FileFix\nreload(DDZ_FileFix)\nDDZ_FileFix.DDZ_FileFix().ddz_renderFileFIX(1,2,1)')
        mc.setParent('..')
        mc.setParent('..')
        mc.frameLayout(label=u'DDZ项目渲染工具(适用于前期及渲染测试)', bgc=[0, 0, 0.0], borderStyle='etchedIn', cll=1,cl=1)
        mc.rowColumnLayout(numberOfColumns=4)
        mc.button(label=u'CHRCO',width=90,height=30,bgc=[0.13, 0.15, 0.25],command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RSRenderLayerCreat("co","chr",1,1,1,0,2,0)')
        mc.button(label=u'SETCO',width=90,height=30,bgc=[0.13, 0.15, 0.25],command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RSRenderLayerCreat("co","set",1,1,1,0,2,0)')
        mc.button(label=u'CHRLight',width=90,height=30,bgc=[0.13, 0.15, 0.25],command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RSRenderLayerCreat("light","chr",1,1,1,0,2,0)')
        mc.button(label=u'勾选AO',width=90,height=30,bgc=[0.13, 0.15, 0.25],command='from idmt.maya.GA import GA_RedShiftRender\nreload(GA_RedShiftRender)\nGA_RedShiftRender.GA_RedShiftRender().GA_RSAOSet(1)')
        mc.setParent('..')
        mc.setParent('..')
        mc.setParent('..')
        mc.tabLayout(tabs, edit=True, tabLabel=(
            (child2, 'Redshift AOV'),(child1, u'预设工具'),(child3, u'常用工具'),(child4, u'DDZ渲染工具')))
        mc.showWindow('GA_RenderRedshift')    
