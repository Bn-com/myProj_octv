# -*- coding: utf-8 -*-

import maya.cmds as mc
import maya.mel as mel


class norch_toolComnnons(object):
    def __init__(self):
        
        pass
  
    def norch_gdAttrToolsUI(self):
        if mc.window('norch_AttrActionWin', exists=True):
            mc.deleteUI('norch_AttrActionWin')
        mc.window('norch_AttrActionWin', title=u'物体属性面板',
                  width=150, height=180, sizeable=True)
                  
         # 面板
        mc.columnLayout( adjustableColumn=True ) 
        mc.rowColumnLayout(numberOfColumns=4)
        mc.iconTextCheckBox(al='left', bgc=[0.2, 0.3, 0.1],olc=[0, 1 ,0],width=45, height=30,style='iconAndTextVertical', image1='plane.png', label='alembic' )
        mc.button(label=u'Add', width=50, height=30, bgc=[0.13, 0.15, 0.25], command='from idmt.maya.norch import norch_toolCommons\nreload(norch_toolCommons)\nnorch_toolCommons.norch_toolComnnons().norch_AttrAction(line="add",attrtype="alembic")')
        mc.button(label=u'Remove',width=50, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.norch import norch_toolCommons\nreload(norch_toolCommons)\nnorch_toolCommons.norch_toolComnnons().norch_AttrAction(line="remove",attrtype="alembic")')
        mc.button(label=u'Select',width=50, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.norch import norch_toolCommons\nreload(norch_toolCommons)\nnorch_toolCommons.norch_toolComnnons().norch_AttrAction(line="select",attrtype="alembic")')
        mc.setParent('..') 
        mc.setParent('..') 
        
        mc.columnLayout( adjustableColumn=True ) 
        mc.rowColumnLayout(numberOfColumns=4)
        mc.iconTextCheckBox(al='left', bgc=[0.2, 0.3, 0.1],olc=[0, 1 ,0],width=45, height=30,style='iconAndTextVertical', image1='plane.png', label='shavesys' )
        mc.button(label=u'Add', width=50, height=30, bgc=[0.13, 0.15, 0.25], command='from idmt.maya.norch import norch_toolCommons\nreload(norch_toolCommons)\nnorch_toolCommons.norch_toolComnnons().norch_AttrAction(line="add",attrtype="shavesys")')
        mc.button(label=u'Remove',width=50, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.norch import norch_toolCommons\nreload(norch_toolCommons)\nnorch_toolCommons.norch_toolComnnons().norch_AttrAction(line="remove",attrtype="shavesys")')
        mc.button(label=u'Select',width=50, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.norch import norch_toolCommons\nreload(norch_toolCommons)\nnorch_toolCommons.norch_toolComnnons().norch_AttrAction(line="select",attrtype="shavesys")')
        mc.setParent('..') 
        mc.setParent('..')         

        mc.columnLayout( adjustableColumn=True ) 
        mc.rowColumnLayout(numberOfColumns=4)
        mc.iconTextCheckBox(al='left', bgc=[0.2, 0.3, 0.1],olc=[0, 1 ,0],width=45, height=30,style='iconAndTextVertical', image1='plane.png', label='abc_curve' )
        mc.button(label=u'Add', width=50, height=30, bgc=[0.13, 0.15, 0.25], command='from idmt.maya.norch import norch_toolCommons\nreload(norch_toolCommons)\nnorch_toolCommons.norch_toolComnnons().norch_AttrAction(line="add",attrtype="abc_curve")')
        mc.button(label=u'Remove',width=50, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.norch import norch_toolCommons\nreload(norch_toolCommons)\nnorch_toolCommons.norch_toolComnnons().norch_AttrAction(line="remove",attrtype="abc_curve")')
        mc.button(label=u'Select',width=50, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.norch import norch_toolCommons\nreload(norch_toolCommons)\nnorch_toolCommons.norch_toolComnnons().norch_AttrAction(line="select",attrtype="abc_curve")')
        mc.setParent('..') 
        mc.setParent('..') 
                      
        mc.showWindow('norch_AttrActionWin') 
 
    def norch_AttrAction(self,line='add',attrtype='ABC'):       
        if line=='select':
            objs=mc.ls(type='transform',l=1)
            objList=[] 
            if objs :
                objList=[]
                for obj in objs:
                    if mc.objExists(obj+'.'+attrtype):
                        objList.append(obj)
                try: 
                    mc.select(objList)
                    print u'\n'
                    print u'==========================已选择有【%s】属性的物体==========================' % attrtype
                    print u'\n'
                except:
                    print u'\n'
                    print u'==========================文件中没有【%s】属性的物体==========================' % attrtype
                    print u'\n'
            else:
                mc.warning(u'没有选择物体，请选择物体' )                                         
        else:
            meshList=[]
            objs=mc.ls(sl=1,type='transform',l=1)
            if objs:                     
                for obj in objs:
                     meshcs=mc.listRelatives(obj,ad=1,f=1)
                     if meshcs:
                         for meshc in meshcs: 
                             if mc.nodeType(meshc)=='mesh' or mc.nodeType(meshc)=='nurbsCurve':                                 
                                 meshList.append(meshc)                     
            if meshList:
                for mesh in meshList:
                    objs=mc.listRelatives(mesh,p=1,f=1)
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
  