# -*- coding: utf-8 -*-
# 【通用】【工具】【Vray属性工具】
#  Author : 韩虹
#  Data   : 2016_03_18
# import sys
# sys.path.append('D:\\food\pyp\common')
import maya.cmds as mc
import maya.mel as mel
class GA_ArnoldAttrTools(object):
    def __init__(self):

        pass
    #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【UI】【属性添加工具面板】
    #  Author  : 韩虹
    #  Data    : 2014_11
    #------------------------------#
#UI篇
    def GA_ArnoldAttrToolsWin(self):
        if mc.window('GA_ArnoldAttrToolsWin', exists=True):
            mc.deleteUI('GA_ArnoldAttrToolsWin')
        mc.window('GA_ArnoldAttrToolsWin', title=u'属性面板',
                  width=150, height=180, sizeable=True)
         # 面板
        mc.columnLayout( adjustableColumn=True )
        mc.frameLayout(label=u'通用属性', bgc=[0, 0, 0.0], borderStyle='in', cll=0,cl=0)
        #lightID 属性
        mc.rowColumnLayout(numberOfColumns=4)
        mc.iconTextCheckBox(al='left', bgc=[0.2, 0.3, 0.1],olc=[0, 1 ,0],width=80, height=30,style='iconAndTextVertical', image1='light.png', label='lightGroup' )
        mc.button(label=u'Add', width=50, height=30, bgc=[0.13, 0.15, 0.25], command='from idmt.maya.py_common import GA_ArnoldAttrTools\nreload(GA_ArnoldAttrTools)\nGA_ArnoldAttrTools.GA_ArnoldAttrTools().GA_ArnoldAttrAction("add","lightGroup")')
        mc.button(label=u'Remove',width=50, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.py_common import GA_ArnoldAttrTools\nreload(GA_ArnoldAttrTools)\nGA_ArnoldAttrTools.GA_ArnoldAttrTools().GA_ArnoldAttrAction("remove","lightGroup")')
        mc.button(label=u'Select',width=50, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.py_common import GA_ArnoldAttrTools\nreload(GA_ArnoldAttrTools)\nGA_ArnoldAttrTools.GA_ArnoldAttrTools().GA_ArnoldAttrAction("select","lightGroup")')
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
        mc.showWindow('GA_ArnoldAttrToolsWin')
    #------------------------------#
    # 【辅】【Vray属性】
    #  Author  : 韩虹
    #  Data    : 2016_03
    #------------------------------#
    def GA_ArnoldAttrInfo(self,attrtype='lightGroup'):
        attr=''
        if  attrtype=='lightGroup':
            attr=['mtoa_constant_lightGroup']
        if attrtype=='idR':
            attr='mtoa_constant_idR'
        if attrtype=='idG':
            attr='mtoa_constant_idG'
        if attrtype=='idB':
            attr='mtoa_constant_idB'
        if attrtype=='idM':
            attr='mtoa_constant_idM'
        return attr
    #------------------------------#
    # 【核】【选择，删除，添加Vary属性】
    #  Author  : 韩虹
    #  Data    : 2016_03
        #------------------------------#
    def GA_ArnoldAttrAction(self,line='select',attrtype='lightGroup'):
        attr=self.GA_ArnoldAttrInfo(attrtype)
        if attr and line=='select':
            objs=[]
            if attrtype=='lightGroup':
                objs=mc.ls(lt=1,l=1)
            else:
                objs=mc.ls(type='mesh',l=1)
            if not objs:
                mc.error(u'文件中缺少相应物体，请检查')
            objList=[]
            for obj in objs:
                if  mc.objExists(obj+'.'+attr) and obj not in objList:
                    objList.append(obj)
            if not objList:
                mc.error(u'文件中没有【%s】属性物体，请检查'% attrtype)
            mc.select(objList)
            print u'\n'
            print u'==========================已选择有【%s】属性的物体==========================' % attrtype
            print '=========================================='
            for ob in objList:
                print u'==============【%s】============='%ob
            print '=========================================='

        if attr and line in ['add','remove']:
            meshList=[]
            objs=mc.ls(sl=1,l=1)
            if not objs:
                mc.error('未选择物体，请选择')
            objType=[]
            if attrtype=='lightGroup':
                Lits=mc.ls(lt=1,l=1)
                if not Lits:
                    mc.error(u'文件中没有灯光物体，请检查')
                for lit in Lits:
                    typ=mc.nodeType(lit)
                    if typ not in objType:
                        objType.append(typ)
            else:
                objType=['mesh']
            for obj in objs:
                shape=mc.listRelatives(obj,s=1,f=1)
                if shape and mc.nodeType(shape[0]) in objType and shape[0] not in meshList:
                    meshList.append()
            if not meshList and attrtype=='lightGroup':
                mc.error(u'所选择物体没有灯光物体，请重新选择')
            if not meshList and attrtype!='lightGroup':
                mc.error(u'所筢物体没有polygon物体，请重新选择')
            for mesh in meshList:
                if attrtype=='lightGroup' and line=='and':
                    try:
                        mc.addAttr(mesh,longName=attr,at='long')
                        inf=u'==================已添加选择物体的【%s】属性====================='%attrtype
                        print inf
                    except:
                        pass
                if attrtype!='lightGroup' and line=='and':
                    try:
                        mc.addAttr(mesh,ln=attr,at='double3')
                        inf=u'==================已添加选择物体的【%s】属性====================='%attrtype
                        print inf
                    except:
                        pass
                if  line=='remove':
                    try:
                        mc.deleteAttr(mesh, at=attr)
                        inf=u'==================已删除选择物体的【%s】属性====================='%attrtype
                        print inf
                    except:
                        pass

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







