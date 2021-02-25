# -*- coding: utf-8 -*-
# 【顺溜】【工具】
#  Author : 韩虹
#  Data   : 2014_08
# import sys
# sys.path.append('D:\\food\pyp\common')


#顺溜项目常用工具

import maya.cmds as mc
import maya.mel as mel


class csl_toolComnnons(object):
    def __init__(self):
        
        pass
    #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【UI】【属性添加工具面板】
    #  Author  : 韩虹
    #  Data    : 2014_11
    #------------------------------#  
#UI篇       
    def csl_gdAttrToolsUI(self):
        if mc.window('csl_AttrActionWin', exists=True):
            mc.deleteUI('csl_AttrActionWin')
        mc.window('csl_AttrActionWin', title=u'物体属性面板',
                  width=150, height=180, sizeable=True)
                  
         # 面板
        mc.columnLayout( adjustableColumn=0)

        mc.frameLayout(label=u'通用属性', bgc=[0, 0, 0.0], borderStyle='in', cll=0,cl=0)
##GD属性
        mc.rowColumnLayout(numberOfColumns=2)
        mc.rowColumnLayout(numberOfColumns=4)
        mc.iconTextCheckBox(al='left', bgc=[0.2, 0.3, 0.1],olc=[0, 1 ,0],width=65, height=30,style='iconAndTextVertical', image1='plane.png', label='GD' )
        mc.button(label=u'Add', width=50, height=30, bgc=[0.13, 0.15, 0.25], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="add",attrtype="GD")')
        mc.button(label=u'Remove',width=50, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="remove",attrtype="GD")')
        mc.button(label=u'Select',width=60, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="select",attrtype="GD")')
        mc.setParent('..')

#alembic 属性【通用】
        mc.rowColumnLayout(numberOfColumns=4)
        mc.iconTextCheckBox(al='left', bgc=[0.2, 0.3, 0.1],olc=[0, 1 ,0],width=65, height=30,style='iconAndTextVertical', image1='plane.png', label='alembic' )
        mc.button(label=u'Add', width=50, height=30, bgc=[0.13, 0.15, 0.25], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="add",attrtype="alembic")')
        mc.button(label=u'Remove',width=50, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="remove",attrtype="alembic")')
        mc.button(label=u'Select',width=60, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="select",attrtype="alembic")')
        mc.setParent('..')
#bake属性
        mc.rowColumnLayout(numberOfColumns=4)
        mc.iconTextCheckBox(al='left', bgc=[0.2, 0.3, 0.1],olc=[0, 1 ,0],width=65, height=30,style='iconAndTextVertical', image1='plane.png', label='clothBake' )
        mc.button(label=u'Add', width=50, height=30, bgc=[0.13, 0.15, 0.25], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_TRAttrAction(line="add",attrtype="clothbake")')
        mc.button(label=u'Remove',width=50, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_TRAttrAction(line="remove",attrtype="clothbake")')
        mc.button(label=u'Select',width=60, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_TRAttrAction(line="select",attrtype="clothbake")')
        mc.setParent('..')
#norender 属性【通用】
        mc.rowColumnLayout(numberOfColumns=4)
        mc.iconTextCheckBox(al='left', bgc=[0.2, 0.3, 0.1],olc=[0, 1 ,0],width=65, height=30,style='iconAndTextVertical', image1='plane.png', label='nr' )
        mc.button(label=u'Add', width=50, height=30, bgc=[0.13, 0.15, 0.25], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="add",attrtype="_nr_")')
        mc.button(label=u'Remove',width=50, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="remove",attrtype="_nr_")')
        mc.button(label=u'Select',width=60, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="select",attrtype="_nr_")')
        mc.setParent('..')
#rgb norender属性【通用】
        mc.rowColumnLayout(numberOfColumns=4)
        mc.iconTextCheckBox(al='left', bgc=[0.2, 0.3, 0.1],olc=[0, 1 ,0],width=65, height=30,style='iconAndTextVertical', image1='plane.png', label='norgb' )
        mc.button(label=u'Add', width=50, height=30, bgc=[0.13, 0.15, 0.25], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="add",attrtype="_norgb")')
        mc.button(label=u'Remove',width=50, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="remove",attrtype="_norgb")')
        mc.button(label=u'Select',width=60, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="select",attrtype="_norgb")')
        mc.setParent('..')
#wing 翅膀属性【通用】
        mc.rowColumnLayout(numberOfColumns=4)
        mc.iconTextCheckBox(al='left', bgc=[0.2, 0.3, 0.1],olc=[0, 1 ,0],width=65, height=30,style='iconAndTextVertical', image1='plane.png', label='wing' )
        mc.button(label=u'Add', width=50, height=30, bgc=[0.13, 0.15, 0.25], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="add",attrtype="wing")')
        mc.button(label=u'Remove',width=50, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="remove",attrtype="wing")')
        mc.button(label=u'Select',width=60, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="select",attrtype="wing")')
        mc.setParent('..')
#是否连接透贴属性【通用】
        mc.rowColumnLayout(numberOfColumns=4)
        mc.iconTextCheckBox(al='left', bgc=[0.2, 0.3, 0.1],olc=[0, 1 ,0],width=65, height=30,style='iconAndTextVertical', image1='plane.png', label='Tra' )
        mc.button(label=u'Add', width=50, height=30, bgc=[0.13, 0.15, 0.25], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="add",attrtype="Tra")')
        mc.button(label=u'Remove',width=50, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="remove",attrtype="Tra")')
        mc.button(label=u'Select',width=60, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="select",attrtype="Tra")')
        mc.setParent('..')
#鱼群 属性【通用】
        mc.rowColumnLayout(numberOfColumns=4)
        mc.iconTextCheckBox(al='left', bgc=[0.2, 0.3, 0.1],olc=[0, 1 ,0],width=65, height=30,style='iconAndTextVertical', image1='plane.png', label='cluster' )
        mc.button(label=u'Add', width=50, height=30, bgc=[0.13, 0.15, 0.25], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="add",attrtype="cluster")')
        mc.button(label=u'Remove',width=50, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="remove",attrtype="cluster")')
        mc.button(label=u'Select',width=60, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="select",attrtype="cluster")')
        mc.setParent('..')
#UV免检 属性【通用】
        mc.rowColumnLayout(numberOfColumns=4)
        mc.iconTextCheckBox(al='left', bgc=[0.2, 0.3, 0.1],olc=[0, 1 ,0],width=65, height=30,style='iconAndTextVertical', image1='plane.png', label=u'UV免检' )
        mc.button(label=u'Add', width=50, height=30, bgc=[0.13, 0.15, 0.25], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="add",attrtype="UV")')
        mc.button(label=u'Remove',width=50, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="remove",attrtype="UV")')
        mc.button(label=u'Select',width=60, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="select",attrtype="UV")')
        mc.setParent('..')
        #meshlight属性（CSL项目要求）        
        mc.rowColumnLayout(numberOfColumns=4)         
        mc.iconTextCheckBox(al='left', bgc=[0.2, 0.3, 0.1],olc=[0, 1 ,0],width=65, height=30,style='iconAndTextVertical', image1='light.png', label='MLight' )
        mc.button(label=u'Add', width=50, height=30, bgc=[0.13, 0.15, 0.25], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="add",attrtype="MLight")')
        mc.button(label=u'Remove',width=50, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="remove",attrtype="MLight")')
        mc.button(label=u'Select',width=60, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="select",attrtype="MLight")')
        mc.setParent('..')
        #hide属性（NJ项目要求）
        mc.rowColumnLayout(numberOfColumns=4)
        mc.iconTextCheckBox(al='left', bgc=[0.2, 0.3, 0.1],olc=[0, 1 ,0],width=65, height=30,style='iconAndTextVertical', image1='plane.png', label='Hide' )
        mc.button(label=u'Add', width=50, height=30, bgc=[0.13, 0.15, 0.25], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="add",attrtype="Hide")')
        mc.button(label=u'Remove',width=50, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="remove",attrtype="Hide")')
        mc.button(label=u'Select',width=60, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="select",attrtype="Hide")')
        mc.setParent('..')        

        #plane属性（shunliu项目要求）
        mc.rowColumnLayout(numberOfColumns=4)
        mc.iconTextCheckBox(al='left', bgc=[0.2, 0.3, 0.1],olc=[0, 1 ,0],width=65, height=30,style='iconAndTextVertical', image1='plane.png', label='unHide' )
        mc.button(label=u'Add', width=50, height=30, bgc=[0.13, 0.15, 0.25], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="add",attrtype="unHide")')
        mc.button(label=u'Remove',width=50, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="remove",attrtype="unHide")')
        mc.button(label=u'Select',width=60, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="select",attrtype="unHide")')
        mc.setParent('..')               


        #til属性（乐高项目要求）
        mc.rowColumnLayout(numberOfColumns=4)
        mc.iconTextCheckBox(al='left', bgc=[0.2, 0.3, 0.1],olc=[0, 1 ,0],width=65, height=30,style='iconAndTextVertical', image1='plane.png', label='tile' )
        mc.button(label=u'Add', width=50, height=30, bgc=[0.13, 0.15, 0.25], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="add",attrtype="tile")')
        mc.button(label=u'Remove',width=50, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="remove",attrtype="tile")')
        mc.button(label=u'Select',width=60, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="select",attrtype="tile")')
        mc.setParent('..')               

                
        mc.rowColumnLayout(numberOfColumns=4)
        mc.iconTextCheckBox(al='left', bgc=[0.2, 0.3, 0.1],olc=[0, 1 ,0],width=65, height=30,style='iconAndTextVertical', image1='plane.png', label='shave' )
        mc.button(label=u'Add', width=50, height=30, bgc=[0.13, 0.15, 0.25], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="add",attrtype="shavesys")')
        mc.button(label=u'Remove',width=50, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="remove",attrtype="shavesys")')
        mc.button(label=u'Select',width=60, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="select",attrtype="shavesys")')
        mc.setParent('..')        

        
        mc.rowColumnLayout(numberOfColumns=4)
        mc.iconTextCheckBox(al='left', bgc=[0.2, 0.3, 0.1],olc=[0, 1 ,0],width=65, height=30,style='iconAndTextVertical', image1='plane.png', label='tree' )
        mc.button(label=u'Add', width=50, height=30, bgc=[0.13, 0.15, 0.25], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_TRAttrAction("add","tree")')
        mc.button(label=u'Remove',width=50, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_TRAttrAction("remove","tree")')
        mc.button(label=u'Select',width=60, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_TRAttrAction("select","tree")')
        mc.setParent('..')        

        mc.rowColumnLayout(numberOfColumns=4)
        mc.iconTextCheckBox(al='left', bgc=[0.2, 0.3, 0.1],olc=[0, 1 ,0],width=65, height=30,style='iconAndTextVertical', image1='plane.png', label='eye' )
        mc.button(label=u'Add', width=50, height=30, bgc=[0.13, 0.15, 0.25], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction("add","eye")')
        mc.button(label=u'Remove',width=50, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction("remove","eye")')
        mc.button(label=u'Select',width=60, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction("select","eye")')
        mc.setParent('..')
        mc.setParent('..')
        mc.setParent('..')
        mc.setParent('..')
        mc.frameLayout(label=u'渲染代理属性', bgc=[0, 0, 0.0], borderStyle='in', cll=0,cl=0)
# 渲染代理属性
        mc.rowColumnLayout(numberOfColumns=2)
        mc.rowColumnLayout(numberOfColumns=4)
        mc.iconTextCheckBox(al='left', bgc=[0.2, 0.3, 0.1],olc=[0, 1 ,0],width=65, height=30,style='iconAndTextVertical', image1='plane.png', label='proxy01' )
        mc.button(label=u'Add', width=50, height=30, bgc=[0.13, 0.15, 0.25], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="add",attrtype="proxy01")')
        mc.button(label=u'Remove',width=50, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="remove",attrtype="proxy01")')
        mc.button(label=u'Select',width=60, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="select",attrtype="proxy01")')
        mc.setParent('..')
        mc.rowColumnLayout(numberOfColumns=4)
        mc.iconTextCheckBox(al='left', bgc=[0.2, 0.3, 0.1],olc=[0, 1 ,0],width=65, height=30,style='iconAndTextVertical', image1='plane.png', label='proxy02' )
        mc.button(label=u'Add', width=50, height=30, bgc=[0.13, 0.15, 0.25], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="add",attrtype="proxy02")')
        mc.button(label=u'Remove',width=50, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="remove",attrtype="proxy02")')
        mc.button(label=u'Select',width=60, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="select",attrtype="proxy02")')
        mc.setParent('..')
        mc.rowColumnLayout(numberOfColumns=4)
        mc.iconTextCheckBox(al='left', bgc=[0.2, 0.3, 0.1],olc=[0, 1 ,0],width=65, height=30,style='iconAndTextVertical', image1='plane.png', label='proxy03' )
        mc.button(label=u'Add', width=50, height=30, bgc=[0.13, 0.15, 0.25], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="add",attrtype="proxy03")')
        mc.button(label=u'Remove',width=50, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="remove",attrtype="proxy03")')
        mc.button(label=u'Select',width=60, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="select",attrtype="proxy03")')
        mc.setParent('..')
        mc.rowColumnLayout(numberOfColumns=4)
        mc.iconTextCheckBox(al='left', bgc=[0.2, 0.3, 0.1],olc=[0, 1 ,0],width=65, height=30,style='iconAndTextVertical', image1='plane.png', label='proxy04' )
        mc.button(label=u'Add', width=50, height=30, bgc=[0.13, 0.15, 0.25], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="add",attrtype="proxy04")')
        mc.button(label=u'Remove',width=50, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="remove",attrtype="proxy04")')
        mc.button(label=u'Select',width=60, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="select",attrtype="proxy04")')
        mc.setParent('..')
        mc.setParent('..')
        mc.setParent('..')
        mc.setParent('..')
        mc.frameLayout(label=u'灯光属性', bgc=[0, 0, 0.0], borderStyle='in', cll=0,cl=0)
##灯光属性
        mc.rowColumnLayout(numberOfColumns=3)
        mc.rowColumnLayout(numberOfColumns=3)
        mc.iconTextCheckBox(al='left', bgc=[0.2, 0.3, 0.1],olc=[0, 1 ,0],width=60, height=30,style='iconAndTextVertical', image1='light.png', label='keylight01' )
        mc.button(label=u'Add', width=40, height=30, bgc=[0.13, 0.15, 0.25], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().gdc_LtAttrAction("add","keylight_01")')
        mc.button(label=u'Remove',width=50, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().gdc_LtAttrAction("remove","keylight_01")')
        mc.setParent('..')
        mc.rowColumnLayout(numberOfColumns=3)
        mc.iconTextCheckBox(al='left', bgc=[0.2, 0.3, 0.1],olc=[0, 1 ,0],width=60, height=30,style='iconAndTextVertical', image1='light.png', label='keylight02' )
        mc.button(label=u'Add', width=40, height=30, bgc=[0.13, 0.15, 0.25], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().gdc_LtAttrAction("add","keylight_02")')
        mc.button(label=u'Remove',width=50, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().gdc_LtAttrAction("remove","keylight_02")')
        mc.setParent('..')
        mc.rowColumnLayout(numberOfColumns=3)
        mc.iconTextCheckBox(al='left', bgc=[0.2, 0.3, 0.1],olc=[0, 1 ,0],width=60, height=30,style='iconAndTextVertical', image1='light.png', label='keylight03' )
        mc.button(label=u'Add', width=40, height=30, bgc=[0.13, 0.15, 0.25], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().gdc_LtAttrAction("add","keylight_03")')
        mc.button(label=u'Remove',width=50, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().gdc_LtAttrAction("remove","keylight_03")')
        mc.setParent('..')

        mc.rowColumnLayout(numberOfColumns=3)
        mc.iconTextCheckBox(al='left', bgc=[0.2, 0.3, 0.1],olc=[0, 1 ,0],width=60, height=30,style='iconAndTextVertical', image1='light.png', label='fillight01' )
        mc.button(label=u'Add', width=40, height=30, bgc=[0.13, 0.15, 0.25], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().gdc_LtAttrAction("add","fillight_01")')
        mc.button(label=u'Remove',width=50, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().gdc_LtAttrAction("remove","fillight_01")')
        mc.setParent('..')
        mc.rowColumnLayout(numberOfColumns=3)
        mc.iconTextCheckBox(al='left', bgc=[0.2, 0.3, 0.1],olc=[0, 1 ,0],width=60, height=30,style='iconAndTextVertical', image1='light.png', label='fillight02' )
        mc.button(label=u'Add', width=40, height=30, bgc=[0.13, 0.15, 0.25], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().gdc_LtAttrAction("add","fillight_02")')
        mc.button(label=u'Remove',width=50, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().gdc_LtAttrAction("remove","fillight_02")')
        mc.setParent('..')
        mc.rowColumnLayout(numberOfColumns=3)
        mc.iconTextCheckBox(al='left', bgc=[0.2, 0.3, 0.1],olc=[0, 1 ,0],width=60, height=30,style='iconAndTextVertical', image1='light.png', label='fillight03' )
        mc.button(label=u'Add', width=40, height=30, bgc=[0.13, 0.15, 0.25], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().gdc_LtAttrAction("add","fillight_03")')
        mc.button(label=u'Remove',width=50, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().gdc_LtAttrAction("remove","fillight_03")')
        mc.setParent('..')

        mc.rowColumnLayout(numberOfColumns=3)
        mc.iconTextCheckBox(al='left', bgc=[0.2, 0.3, 0.1],olc=[0, 1 ,0],width=60, height=30,style='iconAndTextVertical', image1='light.png', label='rimlight01' )
        mc.button(label=u'Add', width=40, height=30, bgc=[0.13, 0.15, 0.25], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().gdc_LtAttrAction("add","rimlight_01")')
        mc.button(label=u'Remove',width=50, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().gdc_LtAttrAction("remove","rimlight_01")')
        mc.setParent('..')
        mc.rowColumnLayout(numberOfColumns=3)
        mc.iconTextCheckBox(al='left', bgc=[0.2, 0.3, 0.1],olc=[0, 1 ,0],width=60, height=30,style='iconAndTextVertical', image1='light.png', label='rimlight02' )
        mc.button(label=u'Add', width=40, height=30, bgc=[0.13, 0.15, 0.25], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().gdc_LtAttrAction("add","rimlight_02")')
        mc.button(label=u'Remove',width=50, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().gdc_LtAttrAction("remove","rimlight_02")')
        mc.setParent('..')
        mc.rowColumnLayout(numberOfColumns=3)
        mc.iconTextCheckBox(al='left', bgc=[0.2, 0.3, 0.1],olc=[0, 1 ,0],width=60, height=30,style='iconAndTextVertical', image1='light.png', label='rimlight03' )
        mc.button(label=u'Add', width=40, height=30, bgc=[0.13, 0.15, 0.25], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().gdc_LtAttrAction("add","rimlight_03")')
        mc.button(label=u'Remove',width=50, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().gdc_LtAttrAction("remove","rimlight_03")')
        mc.setParent('..')

        mc.rowColumnLayout(numberOfColumns=3)
        mc.iconTextCheckBox(al='left', bgc=[0.2, 0.3, 0.1],olc=[0, 1 ,0],width=60, height=30,style='iconAndTextVertical', image1='light.png', label='bouncelight01' )
        mc.button(label=u'Add', width=40, height=30, bgc=[0.13, 0.15, 0.25], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().gdc_LtAttrAction("add","bouncelight_01")')
        mc.button(label=u'Remove',width=50, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().gdc_LtAttrAction("remove","bouncelight_01")')
        mc.setParent('..')
        mc.rowColumnLayout(numberOfColumns=3)
        mc.iconTextCheckBox(al='left', bgc=[0.2, 0.3, 0.1],olc=[0, 1 ,0],width=60, height=30,style='iconAndTextVertical', image1='light.png', label='bouncelight02' )
        mc.button(label=u'Add', width=40, height=30, bgc=[0.13, 0.15, 0.25], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().gdc_LtAttrAction("add","bouncelight_02")')
        mc.button(label=u'Remove',width=50, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().gdc_LtAttrAction("remove","bouncelight_02")')
        mc.setParent('..')
        mc.rowColumnLayout(numberOfColumns=3)
        mc.iconTextCheckBox(al='left', bgc=[0.2, 0.3, 0.1],olc=[0, 1 ,0],width=60, height=30,style='iconAndTextVertical', image1='light.png', label='bouncelight03' )
        mc.button(label=u'Add', width=40, height=30, bgc=[0.13, 0.15, 0.25], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().gdc_LtAttrAction("add","bouncelight_03")')
        mc.button(label=u'Remove',width=50, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().gdc_LtAttrAction("remove","bouncelight_03")')
        mc.setParent('..')
        mc.setParent('..')
        mc.setParent('..')

        mc.columnLayout( adjustableColumn=0)
        mc.frameLayout(label=u'NJ2017项目专用属性', bgc=[0, 0, 0.0], borderStyle='in', cll=0,cl=0)
        mc.rowColumnLayout(numberOfColumns=2)
        mc.rowColumnLayout(numberOfColumns=4)
        mc.iconTextCheckBox(al='left', bgc=[0.2, 0.3, 0.1],olc=[0, 1 ,0],width=65, height=30,style='iconAndTextVertical', image1='plane.png', label='SKY' )
        mc.button(label=u'Add', width=50, height=30, bgc=[0.13, 0.15, 0.25], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_TRAttrAction(line="add",attrtype="SKY")')
        mc.button(label=u'Remove',width=50, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_TRAttrAction(line="remove",attrtype="SKY")')
        mc.button(label=u'Select',width=60, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_TRAttrAction(line="select",attrtype="SKY")')
        mc.setParent('..')
        mc.rowColumnLayout(numberOfColumns=4)
        mc.iconTextCheckBox(al='left', bgc=[0.2, 0.3, 0.1],olc=[0, 1 ,0],width=65, height=30,style='iconAndTextVertical', image1='plane.png', label='billboard' )
        mc.button(label=u'Add', width=50, height=30, bgc=[0.13, 0.15, 0.25], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="add",attrtype="billboard")')
        mc.button(label=u'Remove',width=50, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="remove",attrtype="billboard")')
        mc.button(label=u'Select',width=60, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="select",attrtype="billboard")')
        mc.setParent('..')
        mc.rowColumnLayout(numberOfColumns=4)
        mc.iconTextCheckBox(al='left', bgc=[0.2, 0.3, 0.1],olc=[0, 1 ,0],width=65, height=30,style='iconAndTextVertical', image1='plane.png', label='nosmoothV' )
        mc.button(label=u'Add', width=50, height=30, bgc=[0.13, 0.15, 0.25], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="add",attrtype="nosmoothV")')
        mc.button(label=u'Remove',width=50, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="remove",attrtype="nosmoothV")')
        mc.button(label=u'Select',width=60, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="select",attrtype="nosmoothV")')
        mc.setParent('..')
        mc.rowColumnLayout(numberOfColumns=4)
        mc.iconTextCheckBox(al='left', bgc=[0.2, 0.3, 0.1],olc=[0, 1 ,0],width=65, height=30,style='iconAndTextVertical', image1='plane.png', label='CHR' )
        mc.button(label=u'Add', width=50, height=30, bgc=[0.13, 0.15, 0.25], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_TRAttrAction("add","CHR")')
        mc.button(label=u'Remove',width=50, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_TRAttrAction("remove","CHR")')
        mc.button(label=u'Select',width=60, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_TRAttrAction("select","CHR")')
        mc.setParent('..')
        mc.rowColumnLayout(numberOfColumns=4)
        mc.iconTextCheckBox(al='left', bgc=[0.2, 0.3, 0.1],olc=[0, 1 ,0],width=65, height=30,style='iconAndTextVertical', image1='plane.png', label='SET' )
        mc.button(label=u'Add', width=50, height=30, bgc=[0.13, 0.15, 0.25], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_TRAttrAction("add","SET")')
        mc.button(label=u'Remove',width=50, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_TRAttrAction("remove","SET")')
        mc.button(label=u'Select',width=60, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_TRAttrAction("select","SET")')
        mc.setParent('..')
        mc.setParent('..')
        mc.setParent('..')
        mc.columnLayout( adjustableColumn=0)
        mc.frameLayout(label=u'NJ2015项目专用属性', bgc=[0, 0, 0.0], borderStyle='in', cll=1,cl=1)
        mc.rowColumnLayout(numberOfColumns=1)        
        mc.iconTextCheckBox(height=10,label='NJ')          
        #windows属性（NJ项目要求）
        mc.rowColumnLayout(numberOfColumns=2)
        mc.rowColumnLayout(numberOfColumns=4)
        mc.iconTextCheckBox(al='left', bgc=[0.2, 0.3, 0.1],olc=[0, 1 ,0],width=65, height=30,style='iconAndTextVertical', image1='cone.png', label='Win' )
        mc.button(label=u'Add', width=50, height=30, bgc=[0.13, 0.15, 0.25], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="add",attrtype="Win")')
        mc.button(label=u'Remove',width=50, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="remove",attrtype="Win")')
        mc.button(label=u'Select',width=60, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="select",attrtype="Win")')
        mc.setParent('..')        

        #wall属性（NJ项目要求）
        mc.rowColumnLayout(numberOfColumns=4)
        mc.iconTextCheckBox(al='left', bgc=[0.2, 0.3, 0.1],olc=[0, 1 ,0],width=65, height=30,style='iconAndTextVertical', image1='plane.png', label='Wall' )
        mc.button(label=u'Add', width=50, height=30, bgc=[0.13, 0.15, 0.25], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="add",attrtype="Wall")')
        mc.button(label=u'Remove',width=50, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="remove",attrtype="Wall")')
        mc.button(label=u'Select',width=60, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="select",attrtype="Wall")')
        mc.setParent('..')
        #lantern属性（NJ项目要求）
        mc.rowColumnLayout(numberOfColumns=4)
        mc.iconTextCheckBox(al='left', bgc=[0.2, 0.3, 0.1],olc=[0, 1 ,0],width=65, height=30,style='iconAndTextVertical', image1='plane.png', label='lantern' )
        mc.button(label=u'Add', width=50, height=30, bgc=[0.13, 0.15, 0.25], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="add",attrtype="lantern")')
        mc.button(label=u'Remove',width=50, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="remove",attrtype="lantern")')
        mc.button(label=u'Select',width=60, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="select",attrtype="lantern")')
        mc.setParent('..')
        #属性（NJ项目要求）
        mc.rowColumnLayout(numberOfColumns=4)
        mc.iconTextCheckBox(al='left', bgc=[0.2, 0.3, 0.1],olc=[0, 1 ,0],width=65, height=30,style='iconAndTextVertical', image1='plane.png', label='roof' )
        mc.button(label=u'Add', width=50, height=30, bgc=[0.13, 0.15, 0.25], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="add",attrtype="roof")')
        mc.button(label=u'Remove',width=50, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="remove",attrtype="roof")')
        mc.button(label=u'Select',width=60, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="select",attrtype="roof")')
        mc.setParent('..')        

        #hide属性（NJ项目要求）
        mc.rowColumnLayout(numberOfColumns=4)
        mc.iconTextCheckBox(al='left', bgc=[0.2, 0.3, 0.1],olc=[0, 1 ,0],width=65, height=30,style='iconAndTextVertical', image1='light.png', label='billboard' )
        mc.button(label=u'Add', width=50, height=30, bgc=[0.13, 0.15, 0.25], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_LightAttrAction(line="add",attrtype="billboard",lightpye="volumeLight")')
        mc.button(label=u'Remove',width=50, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_LightAttrAction(line="remove",attrtype="billboard",lightpye="volumeLight")')
        mc.button(label=u'Select',width=60, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_LightAttrAction(line="select",attrtype="billboard",lightpye="volumeLight")')
        mc.setParent('..')        

        #hide属性（NJ项目要求）
        mc.rowColumnLayout(numberOfColumns=4)
        mc.iconTextCheckBox(al='left', bgc=[0.2, 0.3, 0.1],olc=[0, 1 ,0],width=65, height=30,style='iconAndTextVertical', image1='light.png', label='winlight' )
        mc.button(label=u'Add', width=50, height=30, bgc=[0.13, 0.15, 0.25], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_LightAttrAction(line="add",attrtype="winlight",lightpye="areaLight")')
        mc.button(label=u'Remove',width=50, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_LightAttrAction(line="remove",attrtype="winlight",lightpye="areaLight")')
        mc.button(label=u'Select',width=60, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_LightAttrAction(line="select",attrtype="winlight",lightpye="areaLight")')
        mc.setParent('..')

        mc.rowColumnLayout(numberOfColumns=4)
        mc.iconTextCheckBox(al='left', bgc=[0.2, 0.3, 0.1],olc=[0, 1 ,0],width=65, height=30,style='iconAndTextVertical', image1='plane.png', label='lanLamp' )
        mc.button(label=u'Add', width=50, height=30, bgc=[0.13, 0.15, 0.25], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="add",attrtype="lanternLamp")')
        mc.button(label=u'Remove',width=50, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="remove",attrtype="lanternLamp")')
        mc.button(label=u'Select',width=60, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="select",attrtype="lanternLamp")')
        mc.setParent('..')

        
        mc.rowColumnLayout(numberOfColumns=4)
        mc.iconTextCheckBox(al='left', bgc=[0.2, 0.3, 0.1],olc=[0, 1 ,0],width=65, height=30,style='iconAndTextVertical', image1='plane.png', label='lanBall' )
        mc.button(label=u'Add', width=50, height=30, bgc=[0.13, 0.15, 0.25], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="add",attrtype="lanternBall")')
        mc.button(label=u'Remove',width=50, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="remove",attrtype="lanternBall")')
        mc.button(label=u'Select',width=60, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="select",attrtype="lanternBall")')
        mc.setParent('..')

        
        mc.rowColumnLayout(numberOfColumns=4)
        mc.iconTextCheckBox(al='left', bgc=[0.2, 0.3, 0.1],olc=[0, 1 ,0],width=65, height=30,style='iconAndTextVertical', image1='light.png', label='volume' )
        mc.button(label=u'Add', width=50, height=30, bgc=[0.13, 0.15, 0.25], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_LightAttrAction(line="add",attrtype="volumeLight",lightpye="volumeLight")')
        mc.button(label=u'Remove',width=50, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_LightAttrAction(line="remove",attrtype="volumeLight",lightpye="volumeLight")')
        mc.button(label=u'Select',width=60, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_LightAttrAction(line="select",attrtype="volumeLight",lightpye="volumeLight")')
        mc.setParent('..')        


        
        mc.rowColumnLayout(numberOfColumns=4)
        mc.iconTextCheckBox(al='left', bgc=[0.2, 0.3, 0.1],olc=[0, 1 ,0],width=65, height=30,style='iconAndTextVertical', image1='plane.png', label='MoA' )
        mc.button(label=u'Add', width=50, height=30, bgc=[0.13, 0.15, 0.25], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="add",attrtype="MoA")')
        mc.button(label=u'Remove',width=50, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="remove",attrtype="MoA")')
        mc.button(label=u'Select',width=60, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="select",attrtype="MoA")')
        mc.setParent('..')        

                  
        mc.rowColumnLayout(numberOfColumns=4)
        mc.iconTextCheckBox(al='left', bgc=[0.2, 0.3, 0.1],olc=[0, 1 ,0],width=65, height=30,style='iconAndTextVertical', image1='plane.png', label='FX' )
        mc.button(label=u'Add', width=50, height=30, bgc=[0.13, 0.15, 0.25], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="add",attrtype="FX")')
        mc.button(label=u'Remove',width=50, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="remove",attrtype="FX")')
        mc.button(label=u'Select',width=60, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="select",attrtype="FX")')
        mc.setParent('..')        

        
        #woodwall属性（NJ项目要求）        
        mc.rowColumnLayout(numberOfColumns=4)
        mc.iconTextCheckBox(al='left', bgc=[0.2, 0.3, 0.1],olc=[0, 1 ,0],width=65, height=30,style='iconAndTextVertical', image1='plane.png', label='woodwall' )
        mc.button(label=u'Add', width=50, height=30, bgc=[0.13, 0.15, 0.25], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="add",attrtype="woodwall")')
        mc.button(label=u'Remove',width=50, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="remove",attrtype="woodwall")')
        mc.button(label=u'Select',width=60, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_AttrAction(line="select",attrtype="woodwall")')
        mc.setParent('..')

        mc.showWindow('csl_AttrActionWin') 

    def csl_gdAttrSetUI(self):
        if mc.window(u'tree', exists=True):
            mc.deleteUI('csl_gdAttrSetWin')
        mc.window('csl_gdAttrSetWin', title=u'Tree ctrl 显示（隐藏）',
                  width=150, height=180, sizeable=True)
                  
         # 面板
        mc.columnLayout( adjustableColumn=True ) 
        mc.rowColumnLayout(numberOfColumns=2)
        mc.button(label=u'显示', width=50, height=30, bgc=[0.13, 0.15, 0.25], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_setattr(attrtype="aiStandIn",attr="visibility",num=1)')
        mc.button(label=u'隐藏',width=50, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_toolCommons\nreload(csl_toolCommons)\ncsl_toolCommons.csl_toolComnnons().csl_setattr(attrtype="aiStandIn",attr="visibility",num=0)')

        mc.showWindow('csl_gdAttrSetWin') 
    #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【核】【属性添加工具】
    #  Author  : 韩虹
    #  Data    : 2014_11
    #------------------------------#  
    #添加（删减）物体属性（)
    def csl_AttrAction(self,line='add',attrtype='GD',printMode = 0):
        if line=='select':
            objs=mc.ls(type='transform',l=1)
            if objs :
                objList=[]
                for obj in objs:
                    if mc.objExists(obj+'.'+attrtype):
                        objList.append(obj)
                if objList:
                    mc.select(objList)
                    print u'\n'
                    print u'==========================已选择有【%s】属性的物体==========================' % attrtype
                    print u'\n'
                else:
                    print u'\n'
                    print u'==========================文件中没有【%s】属性的物体==========================' % attrtype
                    print u'\n'
            else:
                mc.warning(u'没有选择物体，请选择物体' )                                         
        else:
            meshList=[]
            objs=mc.ls(sl=1,type='transform',l=1)
            for obj in objs:
                meshcs=mc.listRelatives(obj,ad=1,f=1)
                if not meshcs:
                    meshcs = []
                for meshc in meshcs:
                    if mc.nodeType(meshc) in ['mesh','light']:
                        checkAttr = meshc + '.intermediateObject'
                        if mc.ls(checkAttr) and mc.getAttr(checkAttr):
                            continue
                        meshList.append(meshc)
                    if 'light' in mc.nodeType(meshc).lower():
                        meshList.append(meshc)
            if meshList:
                for mesh in meshList:
                    objs=mc.listRelatives(mesh,p=1,f=1)
                    checkObj = objs[0]
                    if line=='add':
                        checkAttr = checkObj+'.'+attrtype
                        if mc.ls(checkAttr):
                            lockState = mc.getAttr(checkAttr,l=1)
                            if not lockState:
                                mc.setAttr((objs[0]+'.'+attrtype),1)
                        else:
                            mc.addAttr(objs[0],ln=attrtype,at='double',dv=1,k=1)
                    if printMode:
                        print u'==========================已添加选择物体的【%s】属性==========================' % attrtype
                    if mc.objExists(objs[0]) and  line=='remove':
                        obj=objs[0]
                        try:
                             mc.deleteAttr(objs[0],at=attrtype)            
                        except:
                             pass                          
            else:
                mc.warning( u'没有选择物体，或者所选择的物体是空组，请选择有效物体' )                             
                       
        return 0           
    #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【附】【属性添加工具】#添加（删减）灯光属性（)
    #  Author  : 韩虹
    #  Data    : 2014_11
    #------------------------------#  
    def csl_LightAttrAction(self,line='add',attrtype='volumeLight',lightpye='volumeLight'):       
        if line=='select':
            objs=mc.ls(type=lightpye,l=1)
            LightList=[] 
            if objs :
                LightList=[]
                for obj in objs:
                    Light=mc.listRelatives(obj,p = 1,f=1)
                    if Light and mc.objExists(Light[0]+'.'+attrtype):
                        LightList.append(Light[0])
                try: 
                    mc.select(LightList)
                    print u'\n'
                    print u'==========================已选择有【%s】属性的物体==========================' % attrtype
                    print u'\n'
                except:
                    print u'\n'
                    print u'==========================文件中没有【%s】属性的物体==========================' % attrtype
                    print u'\n'
            else:
                mc.warning(u'没有选择灯光，请选择灯光' )                                         
        else:
            LightList=[]
            objs=mc.ls(sl=1,type='transform',l=1)
            if objs:                     
                for obj in objs:
                     Lights=mc.listRelatives(obj,ad=1,f=1)
                     if Lights:
                         for Light in Lights: 
                             if mc.nodeType(Light)==lightpye:
                               LightList.append(Light)                     
            if LightList:
                for light in LightList:
                    objs=mc.listRelatives(light,p=1,f=1)
                    if mc.objExists(objs[0]) and  line=='add':
                        try:
                            mc.setAttr((objs[0]+'.'+attrtype),1)             
                        except:
                            mc.addAttr(objs[0],ln=attrtype,at='double',dv=1,k=1)
                    print u'==========================已添加选择物体的【%s】属性==========================' % attrtype 
                    if mc.objExists(objs[0]) and  line=='remove':
                        obj=objs[0]
                        try:
                             mc.deleteAttr(objs[0],at=attrtype)            
                        except:
                             pass                          
            else:
                mc.warning( u'没有选择物体，或者所选择的物体是空组，请选择有效物体' )                             
                       
        return 0

    #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【附】【属性添加工具】#添加（删减）tree属性（);通用于给所有选择的tr物体添加该属性
    #  Author  : 韩虹
    #  Data    : 2014_11
    #------------------------------#
    def csl_TRAttrAction(self,line='add',attrtype='tree'):
        if line=='select':
            objs=mc.ls(tr=1,l=1)
            LightList=[]
            if objs :
                for obj in objs:
                    if mc.objExists(obj+'.'+attrtype):
                        LightList.append(obj)
            if LightList:
                mc.select(LightList)
                print u'\n'
                print u'==========================已选择有【%s】属性的物体==========================' % attrtype
                print u'\n'
            else:
                print u'\n'
                mc.error(u'==========================文件中没有【%s】属性的物体==========================' % attrtype)
                print u'\n'

        else:
            objs=mc.ls(sl=1,type='transform',l=1)
            if objs:
                for obj in objs:
                    if line=='add' and mc.objExists(obj+'.'+attrtype)==False:
                        try:
                            mc.setAttr((obj+'.'+attrtype),1)
                        except:
                            mc.addAttr(obj,ln=attrtype,at='double',dv=1,k=1)
                    print u'==========================已添加选择物体的【%s】属性==========================' % attrtype
                    if line=='remove':
                        try:
                             mc.deleteAttr(obj,at=attrtype)
                        except:
                             pass
            else:
                mc.warning( u'没有选择物体，或者所选择的物体是空组，请选择有效物体' )

        return 0
    #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【附】【属性添加工具】#添加（删减）Arnold渲染代理属性（)
    #  Author  : 韩虹
    #  Data    : 2014_11
    #------------------------------#  
    def csl_setattr(self,attrtype='aiStandIn',attr='visibility',num=1):
        objs=mc.ls(type=attrtype ,l=1)
        if objs:
            for obj in objs:
                Arnold=mc.listRelatives(obj,p = 1,f=1)
                if Arnold and mc.nodeType(Arnold[0])=='transform':
                    mc.setAttr((Arnold[0]+'.'+attr),int(num))         
    #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【通用】参考导入 
    #  Author  : 韩虹
    #  Data    : 2015_02_04
    #------------------------------#  
    def csl_RefImp(self):
        errorInfo=[]
        refPath=mc.file(q=1,r=1)
        if refPath:
            for ref in refPath:
                refRN=mc.file(ref,q=1,rfn=1)
                if mc.file(ref,q=1,dr=1):
                    try:
                        mc.file(loadReference=refRN)
                    except:
                        print (u'===============!!!无法LoadReference【%s】 请检查文件!!!===============' %refRN) 
                try:                                               
                    mc.file(ref,ir=1) 
                except:
                    print (u'===============!!!无法层入【%s】参考 请检查文件!!!===============' %refRN)                  
        shortName=mc.file(q=1,sn=1,shn=1)
        TempPath='D:/Info_Temp/refImort/'
        fileType=''
        if shortName.split('.')[-1]=='mb':
            fileType='mayaBinary'
        else:
            fileType='mayaAscii'                                    
        mc.sysFile(TempPath, makeDir=True) 
        mc.file(rename=(TempPath+shortName))                
        mc.file(save=1,type =fileType,f = 1)            
        print (u'===============!!!【%s】参考导入结束!!!===============' %(TempPath+shortName))  
        return 0
   #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【附】【属性添加工具】#添加（删减）灯光属性（)
    #  Author  : 韩虹
    #  Data    : 2016_08
    #------------------------------#
    def gdc_LtAttrAction(self,line='add',attrtype='keylight'):
        if line=='select':
            objs=mc.ls(lt=1,l=1)
            LightList=[]
            if objs :
                LightList=[]
                for obj in objs:
                    Light=mc.listRelatives(obj,p = 1,f=1)
                    if Light and mc.objExists(Light[0]+'.'+attrtype):
                        LightList.append(Light[0])
                try:
                    mc.select(LightList)
                    print u'\n'
                    print u'==========================已选择有【%s】属性的物体==========================' % attrtype
                    print u'\n'
                except:
                    print u'\n'
                    print u'==========================文件中没有【%s】属性的物体==========================' % attrtype
                    print u'\n'
            else:
                mc.warning(u'没有选择灯光，请选择灯光' )
        else:
            LightList=[]
            objs=mc.ls(sl=1,type='transform',l=1)
            lights=mc.ls(lt=1,l=1)
            for lgt in lights:
                Light=mc.listRelatives(lgt,p = 1,ad=1,f=1)
                if Light and Light[0] in objs:
                    LightList.append(Light[0])
            if LightList:
                for light in LightList:
                    if mc.objExists(light) and  line=='add' and mc.objExists(light+'.'+attrtype)==0:
                        try:
                            mc.setAttr((light+'.'+attrtype),1)
                        except:
                            mc.addAttr(light,ln=attrtype,at='double',dv=1,k=1)
                    print u'==========================已添加选择物体的【%s】属性==========================' % attrtype
                    if mc.objExists(light) and  line=='remove':
                        obj=light
                        try:
                             mc.deleteAttr(light,at=attrtype)
                        except:
                             pass
            else:
                mc.warning( u'没有选择物体，或者所选择的物体是空组，请选择有效物体' )

            return 0
     
                                    