# -*- coding: utf-8 -*-
# 【通用】【工具】【Vray属性工具】
#  Author : 韩虹
#  Data   : 2016_03_18
# import sys
# sys.path.append('D:\\food\pyp\common')
import maya.cmds as mc
import maya.mel as mel
class GDC_VrayAttrTools(object):
    def __init__(self):

        pass
    #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【UI】【属性添加工具面板】
    #  Author  : 韩虹
    #  Data    : 2014_11
    #------------------------------#
#UI篇
    def GDC_VrayAttrWin(self):
        if mc.window('csl_AttrActionWin', exists=True):
            mc.deleteUI('csl_AttrActionWin')
        mc.window('csl_AttrActionWin', title=u'物体属性面板',
                  width=150, height=180, sizeable=True)
         # 面板
        mc.columnLayout( adjustableColumn=True )
        mc.frameLayout(label=u'通用属性', bgc=[0, 0, 0.0], borderStyle='in', cll=0,cl=0)
        ##Subdivision属性
        mc.rowColumnLayout(numberOfColumns=4)
        mc.iconTextCheckBox(al='left', bgc=[0.2, 0.3, 0.1],olc=[0, 1 ,0],width=80, height=30,style='iconAndTextVertical', image1='plane.png', label='Subdivision' )
        mc.button(label=u'Add', width=50, height=30, bgc=[0.13, 0.15, 0.25], command='from idmt.maya.py_common import GDC_VrayAttrTools\nreload(GDC_VrayAttrTools)\nGDC_VrayAttrTools.GDC_VrayAttrTools().VrayAttrAction(line="add",attrtype="vray_subdivision")')
        mc.button(label=u'Remove',width=50, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.py_common import GDC_VrayAttrTools\nreload(GDC_VrayAttrTools)\nGDC_VrayAttrTools.GDC_VrayAttrTools().VrayAttrAction(line="remove",attrtype="vray_subdivision")')
        mc.button(label=u'Select',width=50, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.py_common import GDC_VrayAttrTools\nreload(GDC_VrayAttrTools)\nGDC_VrayAttrTools.GDC_VrayAttrTools().VrayAttrAction(line="select",attrtype="vray_subdivision")')
        mc.setParent('..')
        #objID 属性【通用】
        mc.rowColumnLayout(numberOfColumns=4)
        mc.iconTextCheckBox(al='left', bgc=[0.2, 0.3, 0.1],olc=[0, 1 ,0],width=80, height=30,style='iconAndTextVertical', image1='plane.png', label='objID' )
        mc.button(label=u'Add', width=50, height=30, bgc=[0.13, 0.15, 0.25], command='from idmt.maya.py_common import GDC_VrayAttrTools\nreload(GDC_VrayAttrTools)\nGDC_VrayAttrTools.GDC_VrayAttrTools().VrayAttrAction(line="add",attrtype="vray_objectID")')
        mc.button(label=u'Remove',width=50, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.py_common import GDC_VrayAttrTools\nreload(GDC_VrayAttrTools)\nGDC_VrayAttrTools.GDC_VrayAttrTools().VrayAttrAction(line="remove",attrtype="vray_objectID")')
        mc.button(label=u'Select',width=50, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.py_common import GDC_VrayAttrTools\nreload(GDC_VrayAttrTools)\nGDC_VrayAttrTools.GDC_VrayAttrTools().VrayAttrAction(line="select",attrtype="vray_objectID")')
        mc.setParent('..')
        #mc.intSliderGrp('objID',l='objID',al='left', field=1, min=0, max=15)
        #materialID 属性【通用】
        mc.rowColumnLayout(numberOfColumns=4)
        mc.iconTextCheckBox(al='left', bgc=[0.2, 0.3, 0.1],olc=[0, 1 ,0],width=80, height=30,style='iconAndTextVertical', image1='sphere.png', label='materialID' )
        mc.button(label=u'Add', width=50, height=30, bgc=[0.13, 0.15, 0.25], command='from idmt.maya.py_common import GDC_VrayAttrTools\nreload(GDC_VrayAttrTools)\nGDC_VrayAttrTools.GDC_VrayAttrTools().VrayAttrAction(line="add",attrtype="vray_material_id")')
        mc.button(label=u'Remove',width=50, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.py_common import GDC_VrayAttrTools\nreload(GDC_VrayAttrTools)\nGDC_VrayAttrTools.GDC_VrayAttrTools().VrayAttrAction(line="remove",attrtype="vray_material_id")')
        mc.button(label=u'Select',width=50, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.py_common import GDC_VrayAttrTools\nreload(GDC_VrayAttrTools)\nGDC_VrayAttrTools.GDC_VrayAttrTools().VrayAttrAction(line="select",attrtype="vray_material_id")')
        mc.setParent('..')
        mc.setParent('..')
        mc.frameLayout(label=u'参数设定', bgc=[0, 0, 0.0], borderStyle='in', cll=0,cl=0)
        mc.rowLayout(numberOfColumns=3)
        mc.intSliderGrp('vrayObjectID',l='objID', columnWidth3=[30,30,55],field=1, min=0, max=15)
        mc.button(label=u'set', width=50, height=30, bgc=[0.13, 0.15, 0.25], command='from idmt.maya.py_common import GDC_VrayAttrTools\nreload(GDC_VrayAttrTools)\nGDC_VrayAttrTools.GDC_VrayAttrTools().VrayIDASet("set","vray_objectID")')
        mc.button(label=u'select', width=50, height=30, bgc=[0, 0, 0], command='from idmt.maya.py_common import GDC_VrayAttrTools\nreload(GDC_VrayAttrTools)\nGDC_VrayAttrTools.GDC_VrayAttrTools().VrayIDASet("select","vray_objectID")')
        mc.setParent('..')
        mc.rowLayout(numberOfColumns=3)
        mc.colorSliderGrp('vrayMaterialId',l='matID', columnWidth3=[30,30,55],rgb=(0,0,0))
        mc.button(label=u'set', width=50, height=30, bgc=[0.13, 0.15, 0.25], command='from idmt.maya.py_common import GDC_VrayAttrTools\nreload(GDC_VrayAttrTools)\nGDC_VrayAttrTools.GDC_VrayAttrTools().VrayIDASet("set","vray_material_id")')
        mc.button(label=u'select', width=50, height=30, bgc=[0, 0, 0], command='from idmt.maya.py_common import GDC_VrayAttrTools\nreload(GDC_VrayAttrTools)\nGDC_VrayAttrTools.GDC_VrayAttrTools().VrayIDASet("select","vray_material_id")')
        mc.setParent('..')
        mc.showWindow('csl_AttrActionWin')
    #------------------------------#
    # 【辅】【Vray属性】
    #  Author  : 韩虹
    #  Data    : 2016_03
    #------------------------------#
    def VrayAttrInfo(self,attrtype='vray_objectID'):
        attr=''
        if  attrtype=='vray_objectID':
            attr='vrayObjectID'
            objtype=['mesh']
        if attrtype=='vray_subdivision':
            attr='vraySubdivEnable'
            objtype=['mesh']
        if attrtype=='vray_material_id':
            attr='vrayMaterialId'
            objtype=['VRayMtl','VRaySkinMtl','VRaySwitchMtl','VRayMtlHair3','VRayMtl2Sided','VRayLightMtl']
        return [attr,objtype]
    #------------------------------#
    # 【核】【选择，删除，添加Vary属性】
    #  Author  : 韩虹
    #  Data    : 2016_03
        #------------------------------#
    def VrayAttrAction(self,line='select',attrtype='vray_objectID'):
        attr=self.VrayAttrInfo(attrtype)[0]
        if attr and line=='select':
            objs=mc.ls(type='transform',l=1)+mc.ls(type='VRayMtl')+mc.ls(type='VRaySkinMtl')+mc.ls(type='VRaySwitchMtl')+mc.ls(type='VRayMtlHair3')+mc.ls(type='VRayMtl2Sided')
            objList=[]
            if objs :
                objList=[]
                for obj in objs:
                    if attrtype in ['vray_objectID','vray_material_id'] and mc.objExists(obj+'.'+attr):
                        objList.append(obj)
                    if attrtype in ['vray_subdivision'] and mc.ls(mc.listRelatives(obj,s=1,f=1)) and mc.objExists(mc.listRelatives(obj,s=1,f=1)[0]+'.'+attr):
                        objList.append(obj)
                if objList:
                    mc.select(objList)
                    print u'\n'
                    print u'==========================已选择有【%s】属性的物体==========================' % attrtype
                    print '=========================================='
                    for ob in objList:
                        print u'==============【%s】============='%ob
                    print '=========================================='
                    print u'\n'
                else:
                    print u'\n'
                    print u'==========================文件中没有【%s】属性的物体==========================' % attrtype
                    print u'\n'
        if attr and line in ['add','remove']:
            meshList=[]
            objs=mc.ls(sl=1,l=1)
            if objs:
                for obj in objs:
                    if attrtype in ['vray_subdivision']:
                        meshcs=mc.listRelatives(obj,s=1,f=1)
                        if meshcs:
                            for meshc in meshcs:
                                if mc.nodeType(meshc) in self.VrayAttrInfo(attrtype)[1]:
                                    meshList.append(meshc)
                    if attrtype in ['vray_objectID']:
                        meshcs=mc.listRelatives(obj,s=1,f=1)
                        if meshcs and mc.nodeType(meshcs) in self.VrayAttrInfo(attrtype)[1]:
                            meshList.append(obj)
                    if attrtype in ['vray_material_id']:
                        if mc.nodeType(obj) in self.VrayAttrInfo(attrtype)[1]:
                            meshList.append(obj)
            if meshList:
                for mesh in meshList:
                    cmd=''
                    inf=''
                    if line=='add':
                        cmd= 'vray addAttributesFromGroup ' + mesh+' '+attrtype+' 1'
                        inf=u'==================已添加选择物体的【%s】属性====================='%attrtype
                    if line=='remove':
                        cmd= 'vray addAttributesFromGroup ' + mesh+' '+attrtype+' 0'
                        inf=u'==================已删除选择物体的【%s】属性====================='%attrtype

                    try:
                        mel.eval(cmd)
                        print inf
                    except:
                        pass
            else:
                mc.warning( u'没有选择物体，或者所选择的物体没有该vray属性选择，请选择有效物体')

    #------------------------------#
    # 【核】【设定ID参数】
    #  Author  : 韩虹
    #  Data    : 2016_03
        #------------------------------#
    def VrayIDASet(self,line='select',attrtype='vray_objectID'):
        attr=self.VrayAttrInfo(attrtype)[0]
        if attr in ['vrayMaterialId']:
            ID=mc.colorSliderGrp(attr,q=1,rgb=1)
        else:
            ID=mc.intSliderGrp(attr,q=1,v=1)
        if attr and line=='select':
            objs=mc.ls(type='transform',l=1)+mc.ls(type='VRayMtl')+mc.ls(type='VRaySkinMtl')+mc.ls(type='VRaySwitchMtl')+mc.ls(type='VRayMtlHair3')+mc.ls(type='VRayMtl2Sided')+mc.ls(type='VRayLightMtl')
            objList=[]
            if objs :
                objList=[]
                for obj in objs:
                    if attrtype in ['vray_objectID','vray_material_id'] and mc.objExists(obj+'.'+attr) and mc.getAttr(obj+'.'+attr)==ID:
                        objList.append(obj)
                if objList:
                    mc.select(objList)
                    print u'\n'
                    print u'==========================已选择【%s】的物体==========================' %(attr+' '+str(ID))
                    print '=========================================='
                    for ob in objList:
                        print u'==============【%s】============='%ob
                    print '=========================================='
                    print u'\n'
                else:
                    print u'\n'
                    mc.warning(u'==========================文件中没有【%s】的物体==========================' % (attrtype+' '+str(ID)))
                    mc.error(u'==========================文件中没有【%s】的物体==========================' % (attrtype+' '+str(ID)))
                    print u'\n'
        if attr and line=='set':
            objs=mc.ls(sl=1,l=1)
            if objs:
                for obj in objs:
                    cmd= 'vray addAttributesFromGroup ' + obj+' '+attrtype+' 1'
                    try:
                        mel.eval(cmd)
                        if attr in ['vrayMaterialId']:
                            mc.setAttr((obj+'.vrayColorId'),ID[0],ID[1],ID[2])
                        else:
                            mc.setAttr((obj+'.'+attr),ID)
                        print obj
                    except:
                        pass
            else:
                print u'\n'
                mc.warning(u'没有选择物体，或者所选择的物体没有该vray属性选择，请选择有效物体')
                print u'\n'
        return 0







