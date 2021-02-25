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
    #  Data    : 2017_04
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
        mc.rowColumnLayout(numberOfColumns=5)
        mc.iconTextCheckBox(al='left', bgc=[0.2, 0.3, 0.1],olc=[0, 1 ,0],width=80, height=30,style='iconAndTextVertical', image1='light.png', label='lightGroup' )
        mc.button(label=u'Add', width=50, height=30, bgc=[0.13, 0.15, 0.25], command='from idmt.maya.py_common import GA_ArnoldAttrTools\nreload(GA_ArnoldAttrTools)\nGA_ArnoldAttrTools.GA_ArnoldAttrTools().GA_ArnoldAttrAction("add","lightGroup")')
        mc.button(label=u'Remove',width=50, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.py_common import GA_ArnoldAttrTools\nreload(GA_ArnoldAttrTools)\nGA_ArnoldAttrTools.GA_ArnoldAttrTools().GA_ArnoldAttrAction("remove","lightGroup")')
        mc.button(label=u'Select',width=50, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.py_common import GA_ArnoldAttrTools\nreload(GA_ArnoldAttrTools)\nGA_ArnoldAttrTools.GA_ArnoldAttrTools().GA_ArnoldAttrAction("select","lightGroup")')
        mc.button(label=u'DeleteAll',width=80, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.py_common import GA_ArnoldAttrTools\nreload(GA_ArnoldAttrTools)\nGA_ArnoldAttrTools.GA_ArnoldAttrTools().GA_ArnoldAttrDelete("lightGroup")')
        mc.setParent('..')
        #objID 属性【通用】
        mc.rowColumnLayout(numberOfColumns=5)
        mc.iconTextCheckBox(al='left', bgc=[0.2, 0.3, 0.1],olc=[0, 1 ,0],width=80, height=30,style='iconAndTextVertical', image1='plane.png', label='MeshID' )
        mc.button(label=u'Add', width=50, height=30, bgc=[0.13, 0.15, 0.25], command='from idmt.maya.py_common import GA_ArnoldAttrTools\nreload(GA_ArnoldAttrTools)\nGA_ArnoldAttrTools.GA_ArnoldAttrTools().GA_ArnoldAttrAction("add","meshID")')
        mc.button(label=u'Remove',width=50, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.py_common import GA_ArnoldAttrTools\nreload(GA_ArnoldAttrTools)\nGA_ArnoldAttrTools.GA_ArnoldAttrTools().GA_ArnoldAttrAction("remove","meshID")')
        mc.button(label=u'Select',width=50, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.py_common import GA_ArnoldAttrTools\nreload(GA_ArnoldAttrTools)\nGA_ArnoldAttrTools.GA_ArnoldAttrTools().GA_ArnoldAttrAction("select","meshID")')
        mc.button(label=u'DeleteAll',width=80, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.py_common import GA_ArnoldAttrTools\nreload(GA_ArnoldAttrTools)\nGA_ArnoldAttrTools.GA_ArnoldAttrTools().GA_ArnoldAttrDelete("meshID")')
        mc.setParent('..')
        mc.setParent('..')
        ##参数设定
        mc.frameLayout(label=u'参数设定', bgc=[0, 0, 0.0], borderStyle='in', cll=0,cl=0)
        mc.rowLayout(numberOfColumns=3)
        mc.intSliderGrp('lightGroup',l='litGroup', columnWidth3=[50,20,55],field=1, min=0, max=7)
        mc.button(label=u'set', width=50, height=30, bgc=[0.13, 0.15, 0.25], command='from idmt.maya.py_common import GA_ArnoldAttrTools\nreload(GA_ArnoldAttrTools)\nGA_ArnoldAttrTools.GA_ArnoldAttrTools().GA_ArnoldIDASet("set","lightGroup")')
        mc.button(label=u'select', width=50, height=30, bgc=[0, 0, 0], command='from idmt.maya.py_common import GA_ArnoldAttrTools\nreload(GA_ArnoldAttrTools)\nGA_ArnoldAttrTools.GA_ArnoldAttrTools().GA_ArnoldIDASet("select","lightGroup")')
        mc.setParent('..')
        mc.rowLayout(numberOfColumns=3)
        mc.colorSliderGrp('meshID',l='meshID', columnWidth3=[50,20,55],rgb=(0,0,0))
        mc.button(label=u'set', width=50, height=30, bgc=[0.13, 0.15, 0.25], command='from idmt.maya.py_common import GA_ArnoldAttrTools\nreload(GA_ArnoldAttrTools)\nGA_ArnoldAttrTools.GA_ArnoldAttrTools().GA_ArnoldIDASet("set","meshID")')
        mc.button(label=u'select', width=50, height=30, bgc=[0, 0, 0], command='from idmt.maya.py_common import GA_ArnoldAttrTools\nreload(GA_ArnoldAttrTools)\nGA_ArnoldAttrTools.GA_ArnoldAttrTools().GA_ArnoldIDASet("select","meshID")')
        mc.setParent('..')
        mc.setParent('..')
        #属性开关面板
        mc.frameLayout(label=u'属性开关', bgc=[0, 0, 0.0], borderStyle='in', cll=0,cl=0)
        mc.rowColumnLayout(numberOfColumns=3)
        mc.iconTextCheckBox(al='left', bgc=[0.2, 0.3, 0.1],olc=[0, 1 ,0],width=80, height=30,style='iconAndTextVertical', image1='plane.png', label='Opaque' )
        mc.button(label=u'On', width=80, height=30, bgc=[0.13, 0.15, 0.25], command='from idmt.maya.py_common import GA_ArnoldAttrTools\nreload(GA_ArnoldAttrTools)\nGA_ArnoldAttrTools.GA_ArnoldAttrTools().GA_AttrKey("aiOpaque",1,"mesh")')
        mc.button(label=u'Off',width=80, height=30,bgc=[0, 0, 0.0], command='from idmt.maya.py_common import GA_ArnoldAttrTools\nreload(GA_ArnoldAttrTools)\nGA_ArnoldAttrTools.GA_ArnoldAttrTools().GA_AttrKey("aiOpaque",0,"mesh")')
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
            attr='mtoa_constant_lightGroup'
        else:
            attr=self.GA_AttrInfo()
        return attr
    #------------------------------#
    # 【辅】【删除所有arnold属性】
    #  Author  : 韩虹
    #  Data    : 2017_07
        #------------------------------#
    def GA_ArnoldAttrDelete(self,attrtype='lightGroup'):
        if attrtype in['lightGroup']:
            objs=mc.ls(lt=1,l=1)
        else:
            objs=mc.ls(type='mesh',l=1)
        if not objs:
            mc.error(u'文件中缺少【%s】属性物体' %attrtype)
        for obj in objs:
            Attrs=mc.listAttr(obj)
            for attr in Attrs:
                if  attrtype in['lightGroup'] and 'mtoa_constant_lightGroup' in attr or 'id' in attr or 'ID' in attr:
                    try:
                        mc.deleteAttr(obj, at=attr)
                    except:
                        mc.warning(u'无法删除【%s】的【%s】属性' %(obj,attr))
                if attrtype in['meshID'] and 'mtoa_constant_' in attr and mc.objExists(obj+'.'+attr):
                    try:
                        mc.deleteAttr(obj, at=attr)
                    except:
                        mc.warning(u'无法删除【%s】的【%s】属性' %(obj,attr))
        result=u'===========已删除【%s】相关属性======='%attrtype
        return result



    #------------------------------#
    # 【核】【选择，删除，添加arnold属性】
    #  Author  : 韩虹
    #  Data    : 2016_03
        #------------------------------#
    def GA_ArnoldAttrAction(self,line='select',attrtype='lightGroup'):
        attr=self.GA_ArnoldAttrInfo(attrtype)
        if attrtype=='lightGroup':
            num=mc.intSliderGrp(attrtype,q=1,v=1)
        else:
            num=mc.colorSliderGrp(attrtype,q=1,rgb=1)
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
                    tr=mc.listRelatives(obj,p=1,f=1,type='transform')
                    if tr:
                        objList.append(tr[0])
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
            objs=mc.ls(sl=1,l=1,tr=1)
            if not objs:
                mc.error(u'未选择物体，请选择')
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
                if shape:
                    for sha in shape:
                        if  mc.nodeType(sha) in objType and sha not in meshList:
                            meshList.append(sha)
            if not meshList and attrtype=='lightGroup':
                mc.error(u'所选择物体没有灯光物体，请重新选择')
            if not meshList and attrtype!='lightGroup':
                mc.error(u'所筢物体没有polygon物体，请重新选择')
            for mesh in meshList:
                if attrtype=='lightGroup' and line=='add':
                    try:
                        mc.addAttr(mesh,longName=attr,at='long')
                        mc.setAttr((mesh+'.'+attr),num)
                        inf=u'==================已添加选择物体的【%s】属性====================='%attrtype
                        print inf
                    except:
                        pass
                if attrtype!='lightGroup' and line=='add':
                    try:
                        mc.addAttr(mesh,longName=attr,at='double3')
                        mc.addAttr(mesh,longName=attr+'X',at='double',p=attr)
                        mc.addAttr(mesh,longName=attr+'Y',at='double',p=attr)
                        mc.addAttr(mesh,longName=attr+'Z',at='double',p=attr)
                        mc.setAttr((mesh+'.'+attr+'X'),num[0])
                        mc.setAttr((mesh+'.'+attr+'Y'),num[1])
                        mc.setAttr((mesh+'.'+attr+'Z'),num[2])
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
    #  Data    : 2017_04
        #------------------------------#
    def GA_ArnoldIDASet(self,line='select',attrtype='lightGroup'):
        attr=self.GA_ArnoldAttrInfo(attrtype)
        if attrtype=='lightGroup':
            num=mc.intSliderGrp(attrtype,q=1,v=1)
        else:
            num=mc.colorSliderGrp(attrtype,q=1,rgb=1)
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
                if  mc.objExists(obj+'.'+attr) and obj not in objList and attrtype=='lightGroup' and mc.getAttr(obj+'.'+attr)==num:
                    tr=mc.listRelatives(obj,p=1,f=1,type='transform')
                    if tr:
                        objList.append(tr[0])
                if mc.objExists(obj+'.'+attr) and obj not in objList and attrtype!='lightGroup' and mc.getAttr(obj+'.'+attr+'X')==num[0] and mc.getAttr(obj+'.'+attr+'Y')==num[1] and mc.getAttr(obj+'.'+attr+'Z')==num[2]:
                    tr=mc.listRelatives(obj,p=1,f=1,type='transform')
                    if tr:
                        objList.append(tr[0])
            if not objList:
                mc.error(u'文件中没有【%s】属性物体，请检查'% attr)
            mc.select(objList)
            print u'\n'
            print u'==========================已选择有【%s】为【%s】的物体==========================' % attrtype %num
            print '=========================================='
            for ob in objList:
                print u'==============【%s】============='%ob
            print '=========================================='
        if attr and line=='set':
            meshList=[]
            objs=mc.ls(sl=1,l=1,tr=1)
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
                if shape:
                    for sha in shape:
                        if mc.nodeType(sha) in objType and sha not in meshList:
                            meshList.append(sha)
            if not meshList and attrtype=='lightGroup':
                mc.error(u'所选择物体没有灯光物体，请重新选择')
            if not meshList and attrtype!='lightGroup':
                mc.error(u'所筢物体没有polygon物体，请重新选择')

            for mesh in meshList:
                if attrtype!='lightGroup' and mc.objExists(mesh+'.'+attr)!=True:
                    try:
                        mc.addAttr(mesh,longName=attr,at='double3')
                        mc.addAttr(mesh,longName=attr+'X',at='double',p=attr)
                        mc.addAttr(mesh,longName=attr+'Y',at='double',p=attr)
                        mc.addAttr(mesh,longName=attr+'Z',at='double',p=attr)
                        mc.setAttr((mesh+'.'+attr+'X'),num[0])
                        mc.setAttr((mesh+'.'+attr+'Y'),num[1])
                        mc.setAttr((mesh+'.'+attr+'Z'),num[2])
                    except:
                        pass
                if attrtype=='lightGroup' and mc.objExists(obj+'.'+attr)!=True:
                    try:
                        mc.addAttr(mesh,longName=attr,at='long')
                        mc.setAttr((mesh+'.'+attr),num)
                    except:
                        pass
                if attrtype=='lightGroup' and mc.objExists(obj+'.'+attr):
                    try:
                        mc.setAttr((mesh+'.'+attr),num)
                    except:
                        pass
                if attrtype!='lightGroup' and mc.objExists(obj+'.'+attr):
                    try:
                        mc.setAttr((mesh+'.'+attr+'X'),num[0])
                        mc.setAttr((mesh+'.'+attr+'Y'),num[1])
                        mc.setAttr((mesh+'.'+attr+'Z'),num[2])
                    except:
                        pass
        return 0
    def AttrTools_Create_Button(self):
        global AttrName
        AttrName=mc.textField("AttrToolsName",q=1, tx=1)
        return AttrName

    def AttrCreat_UI(self):
        form = mc.setParent(q=True)
        mc.formLayout(form, e=True, width=20)
        t=mc.text(label=u'属性名')
        mc.textField('AttrToolsName',w=30,tx='')
        mc.setFocus('AttrToolsName')
        b1=mc.button(l='Apply',c='reload(GA_ArnoldAttrTools)\nGA_ArnoldAttrTools.GA_ArnoldAttrTools().AttrTools_Create_Button()\nmc.layoutDialog(dismiss="Abort")')
        mc.formLayout(form, edit=True,attachForm=[(t, 'top', 5), (t, 'left', 5), (t, 'right', 5),('AttrToolsName','left',5),('AttrToolsName','right',5),(b1,'left',25),(b1,'right',25)],
                                        attachNone=[(t, 'bottom'), ('AttrToolsName', 'bottom'), (b1, 'bottom')],
                                        attachControl=[('AttrToolsName', 'top', 5, t), (b1, 'top', 5, 'AttrToolsName')])
        form
    def GA_AttrInfo(self):
        objs=mc.ls(sl=1,l=1)
        if not objs:
            mc.error(u'====please select============')
        global AttrName
        AttrName=''
        mc.layoutDialog(ui='reload(GA_ArnoldAttrTools)\nGA_ArnoldAttrTools.GA_ArnoldAttrTools().AttrCreat_UI()',t=u'创建模型ID属性')
        AttrName='mtoa_constant_'+AttrName
        return AttrName
# 打开关闭属性
    def GA_AttrKey(self,attrtype='aiOpaque',keytype=1,objtype='mesh'):
        objs=mc.ls(sl=1,tr=1,l=1)
        meshList=[]
        if not objs:
            mc.error('not select,please select')
        for obj in objs:
            meshs=mc.listRelatives(obj,type=objtype,f=1)
            if not meshs:
                continue
            for mesh in meshs:
                if mc.objExists(mesh+'.'+attrtype) and mesh not in meshList:
                    meshList.append(mesh)
        if not meshList:
            mc.error(u'所选择的物体没有【%s】属性，请检查' %attrtype)
        for mesh in meshList:
            try:
                mc.setAttr((mesh+'.'+attrtype),keytype)
            except:
                mc.warning(u'无法设置【%s】' %(mesh+'.'+attrtype))
                pass
        return keytype
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









