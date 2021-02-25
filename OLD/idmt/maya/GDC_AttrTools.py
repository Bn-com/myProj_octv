# -*- coding: utf-8 -*-
# 【顺溜】【工具】
#  Author : 韩虹
#  Data   : 2015_12
# import sys


#属性工具

import maya.cmds as mc
import maya.mel as mel


class GDC_AttrTools(object):
    def __init__(self):

        pass
    #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【UI】【属性添加工具面板】
    #  Author  : 韩虹
    #  Data    : 2015_12
    #------------------------------#
#UI篇
#动画相关属性

    def gdc_AttrToolsAnmUI(self):
        if mc.window('GDC_AttrActionWin', exists=True):
            mc.deleteUI('GDC_AttrActionWin')
        mc.window('GDC_AttrActionWin', title=u'物体属性面板',
                  width=150, height=180, sizeable=True)

         # 面板
        mc.columnLayout( adjustableColumn=True )

        mc.frameLayout(label=u'通用属性', bgc=[0, 0, 0.0], borderStyle='in', cll=0,cl=0)
        mc.rowColumnLayout(numberOfColumns=4)
        mc.iconTextCheckBox(al='left', bgc=[0.2, 0.3, 0.1],olc=[0, 1 ,0],width=45, height=30,style='iconAndTextVertical', image1='plane.png', label='GD' )
        mc.button(label=u'Add', width=50, height=30, bgc=[0.13, 0.15, 0.25], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="add",attrtype="GD")')
        mc.button(label=u'Remove',width=50, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="remove",attrtype="GD")')
        mc.button(label=u'Select',width=50, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="select",attrtype="GD")')
        mc.setParent('..')