

import maya.cmds as mc
import maya.mel as mel
from idmt.maya.commonCore.core_renderLayer import sk_renderLayerCore
reload(sk_renderLayerCore)


def hh_RenderArnoldUI():
    # 窗口
    if mc.window('hh_RenderArnold', exists=True):
        mc.deleteUI('hh_RenderArnold')
    mc.window('hh_RenderArnold', title=u'Arnold 渲染面板',
              width=320, height=350, sizeable=True)
     # 面板
    form = mc.formLayout()
     # 切换面板
    tabs = mc.tabLayout(innerMarginWidth=5, innerMarginHeight=5)
    mc.formLayout(
        form, edit=True, attachForm=((tabs, 'top', 0), (tabs, 'left', 0), (tabs, 'bottom', 0), (tabs, 'right', 0)))
     # tab_渲染工具
    child1 = mc.columnLayout(adjustableColumn=True)
    mc.image(
        image='//file-cluster/GDC/Resource/Support/Maya/icons/HH/arnold.png')
    mc.button(label=u'创建Project', bgc=[0, 0, 0.0], height=50, command='')
    mc.button(label=u'另存文件', bgc=[0, 0, 0.0], height=50, command='')
    mc.button(label=u'创建AOV', bgc=[0, 0, 0.0], height=50, command='')
    mc.button(label=u'提交网渲', bgc=[0, 0, 0.0], height=50, command='')
    mc.setParent('..')
     # AOV面板
    child2 = mc.columnLayout(adjustableColumn=True)
    mc.frameLayout(label='Select', bgc=[0, 0, 0.0], borderStyle='in', cll=1)
    mc.rowColumnLayout(numberOfColumns=3)
    collectionocc = cmds.radioCollection()
    # occ
    occset = mc.checkBox(label='OCC', visible=1, v=1,
                         bgc=[0.13, 0.15, 0.25], height=30, width=120)
    mc.button(label=u'创建', bgc=[
              0, 0, 0.0], width=100, height=30, command='')
    mc.button(
        label=u'删除', bgc=[0, 0, 0.0], width=100, height=30, command='')
    collectionnormal = cmds.radioCollection()
    # normal
    occset = mc.checkBox(label='Normal', visible=1, v=1,
                         bgc=[0.13, 0.15, 0.25], height=30, width=120)
    mc.button(label=u'创建', bgc=[
              0, 0, 0.0], width=100, height=30, command='')
    mc.button(
        label=u'删除', bgc=[0, 0, 0.0], width=100, height=30, command='')
    collectionfre = cmds.radioCollection()
    # fre
    freset = mc.checkBox(label='Fre', visible=1, v=1,
                         bgc=[0.13, 0.15, 0.25], height=30, width=120)
    mc.button(label=u'创建', bgc=[
              0, 0, 0.0], width=100, height=30, command='')
    mc.button(
        label=u'删除', bgc=[0, 0, 0.0], width=100, height=30, command='')
    collectionkey = cmds.radioCollection()
    # KeyLight
    freset = mc.checkBox(label='KeyLight', visible=1,
                         v=1, bgc=[0.13, 0.15, 0.25], height=30, width=120)
    mc.button(label=u'创建', bgc=[
              0, 0, 0.0], width=100, height=30, command='')
    mc.button(
        label=u'删除', bgc=[0, 0, 0.0], width=100, height=30, command='')
    collectionzdp = cmds.radioCollection()
    # zdepth
    freset = mc.checkBox(label='Zdepth', visible=1, v=1,
                         bgc=[0.13, 0.15, 0.25], height=30, width=120)
    mc.button(label=u'创建', bgc=[
              0, 0, 0.0], width=100, height=30, command='')
    mc.button(
        label=u'删除', bgc=[0, 0, 0.0], width=100, height=30, command='')
    collectionid01 = cmds.radioCollection()
    # id01
    freset = mc.checkBox(label='id01', visible=1, v=1,
                         bgc=[0.13, 0.15, 0.25], height=30, width=120)
    mc.button(label=u'创建', bgc=[
              0, 0, 0.0], width=100, height=30, command='')
    mc.button(
        label=u'删除', bgc=[0, 0, 0.0], width=100, height=30, command='')
    mc.setParent('..')
    mc.setParent('..')
    # 一键式创建AOV层
    mc.frameLayout(label=u'一键式创建（删除）工具', bgc=[0, 0, 0.0], borderStyle='in')
    mc.rowColumnLayout(numberOfColumns=2)
    mc.button(label=u'创建渲染层', width=160, height=30,
              bgc=[0.13, 0.15, 0.25], command='')
    mc.button(label=u'删除所有AOV及渲染层', width=160,
              height=30, bgc=[0, 0, 0.0], command='')
    mc.setParent('..')
    mc.setParent('..')
    mc.setParent('..')
    # 渲染常用工具组
    child3 = mc.rowColumnLayout(numberOfColumns=2)
    mc.button(label=u'创建', bgc=[
              0, 0, 0.0], width=100, height=30, command='')
    mc.setParent('..')
    mc.tabLayout(tabs, edit=True, tabLabel=(
        (child1, u'渲染流程'), (child2, 'Arnold AOV'), (child3, u'渲染工具')))
    mc.showWindow('hh_RenderArnold')
