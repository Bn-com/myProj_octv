# -*- coding: utf-8 -*-

import maya.cmds as mc
import maya.mel as mel
from idmt.maya.commonCore.core_renderLayer import sk_renderLayerCore
reload(sk_renderLayerCore)


def hh_RenderArnoldTUI():
    # 窗口
    if mc.window('hh_RenderArnold', exists=True):
        mc.deleteUI('hh_RenderArnold')
    mc.window('hh_RenderArnold', title=u'Arnold 渲染面板',
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
              0, 0, 0.0], width=110, height=30, command='from idmt.maya.Hh_common import hh_RenderArnoldLayer\nreload(hh_RenderArnoldLayer)\nhh_RenderArnoldLayer.hh_RenderArnoldLayer().ArnoldAOVAOCreate()')
    mc.button(
        label=u'删除', bgc=[0, 0, 0.0], width=110, height=30, command='')
    collectionnormal = mc.radioCollection()
    # normal
    normalset = mc.checkBox('hhchecknormal',label='Normal', visible=1, v=1,
                         bgc=[0.13, 0.15, 0.25], height=30, width=130)
    mc.button(label=u'创建', bgc=[
              0, 0, 0.0], width=110, height=30, command='from idmt.maya.Hh_common import hh_RenderArnoldLayer\nreload(hh_RenderArnoldLayer)\nhh_RenderArnoldLayer.hh_RenderArnoldLayer().ArnoldAOVNomalCreate()')
    mc.button(
        label=u'删除', bgc=[0, 0, 0.0], width=110, height=30, command='')
    collectionfre = mc.radioCollection()
    # fre
    freset = mc.checkBox('hhcheckfre',label='Fre', visible=1, v=1,
                         bgc=[0.13, 0.15, 0.25], height=30, width=130)
    mc.button(label=u'创建', bgc=[
              0, 0, 0.0], width=110, height=30, command='from idmt.maya.Hh_common import hh_RenderArnoldLayer\nreload(hh_RenderArnoldLayer)\nhh_RenderArnoldLayer.hh_RenderArnoldLayer().ArnoldAOVFreCreate()')
    mc.button(
        label=u'删除', bgc=[0, 0, 0.0], width=110, height=30, command='')
    collectionkey = mc.radioCollection()
    # KeyLight
    keyset = mc.checkBox('hhcheckkey',label='KeyLight', visible=1,
                         v=1, bgc=[0.13, 0.15, 0.25], height=30, width=130)
    mc.button(label=u'创建', bgc=[
              0, 0, 0.0], width=110, height=30, command='from idmt.maya.Hh_common import hh_RenderArnoldLayer\nreload(hh_RenderArnoldLayer)\nhh_RenderArnoldLayer.hh_RenderArnoldLayer().ArnoldAOVKeyLight()')
    mc.button(
        label=u'删除', bgc=[0, 0, 0.0], width=110, height=30, command='')
    collectionzdp = mc.radioCollection()
    # Shadow
    keyset = mc.checkBox('hhcheckshadow',label='Shadow', visible=1,
                         v=1, bgc=[0.13, 0.15, 0.25], height=30, width=130)
    mc.button(label=u'创建', bgc=[
              0, 0, 0.0], width=110, height=30, command='from idmt.maya.Hh_common import hh_RenderArnoldLayer\nreload(hh_RenderArnoldLayer)\nhh_RenderArnoldLayer.hh_RenderArnoldLayer().ArnoldAOVShadowCreat()')
    mc.button(
        label=u'删除', bgc=[0, 0, 0.0], width=110, height=30, command='')
    collectionzdp = mc.radioCollection()
    # zdepth
    zdepthset = mc.checkBox('hhcheckzdep',label='Zdepth', visible=1, v=1,
                         bgc=[0.13, 0.15, 0.25], height=30, width=130)
    mc.button(label=u'创建', bgc=[
              0, 0, 0.0], width=110, height=30, command='from idmt.maya.Hh_common import hh_RenderArnoldLayer\nreload(hh_RenderArnoldLayer)\nhh_RenderArnoldLayer.hh_RenderArnoldLayer().ArnoldAOVZdepthCreat()')
    mc.button(
        label=u'删除', bgc=[0, 0, 0.0], width=110, height=30, command='')
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
              bgc=[0.13, 0.15, 0.25], command='from idmt.maya.Hh_common import hh_RenderArnoldLayer\nreload(hh_RenderArnoldLayer)\nhh_RenderArnoldLayer.hh_RenderArnoldLayer().ArnoldRendererLayerCreat()')
    mc.button(label=u'删除所有AOV及渲染层', width=170,
              height=30, bgc=[0, 0, 0.0], command='')
    mc.setParent('..')
    mc.setParent('..')
    mc.setParent('..')
    # 渲染常用工具组
    child3 = mc.rowColumnLayout(numberOfColumns=2)
    mc.frameLayout(label='IDP输出工具', bgc=[0, 0, 0.0], borderStyle='in', cll=1)
    mc.rowColumnLayout(numberOfColumns=2)
    mc.button(label=u'输出角色id01',width=180,height=30,bgc=[0,0,0],command='')
    mc.button(label=u'输出角色id02',width=180,height=30,bgc=[0,0,0],command='')
    mc.button(label=u'输出场景id11',width=180,height=30,bgc=[0,0,0],command='')
    mc.button(label=u'输出场景id12',width=180,height=30,bgc=[0,0,0],command='')
    mc.setParent('..')
    #idp材质工具    
    mc.frameLayout(label='IDP材质工具', bgc=[0, 0, 0.0], borderStyle='in', cll=1)
    mc.rowColumnLayout(numberOfColumns=4) 
    mc.button(label=u'R',width=180,height=30,bgc=[1,0,0],command='')
    mc.button(label=u'G',width=180,height=30,bgc=[0,1,0],command='')
    mc.button(label=u'B',width=180,height=30,bgc=[0,0,1],command='')
    mc.button(label=u'A',width=180,height=30,bgc=[1,1,1],command='') 
    mc.button(label=u'A',width=180,height=30,bgc=[1,1,0],command='') 
    mc.button(label=u'A',width=180,height=30,bgc=[0,1,1],command='') 
    mc.button(label=u'A',width=180,height=30,bgc=[1,0,1],command='')                 
    mc.setParent('..')
    mc.tabLayout(tabs, edit=True, tabLabel=(
        (child1, u'渲染流程'), (child2, 'Arnold AOV'), (child3, u'渲染工具')))
    mc.showWindow('hh_RenderArnold')
hh_RenderArnoldTUI()

