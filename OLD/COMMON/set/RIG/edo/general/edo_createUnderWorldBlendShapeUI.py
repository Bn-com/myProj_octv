# -*- coding: utf-8 -*-
import maya.cmds as cmds
def edo_createUnderWorldBlendShape(input,org,un,unbase,bss):
    ##input='input'
    ##org='org'
    ##un='un'
    ##unbase='un'
    ##bss=['bs']
    if input=='' or org=='' or un=='' or unbase=='' or bss==None or bss==['']:
        cmds.confirmDialog( title='error', message='defome mesh are not enough!', button='got it!',defaultButton='Yes', cancelButton='No', dismissString='No')
        return False
    inputshape=cmds.listRelatives(input,s=1,ni=1)
    inputtype=cmds.nodeType(inputshape)
    orgshape=cmds.listRelatives(org,s=1,ni=1)
    orgtype=cmds.nodeType(orgshape)
    for bs in bss:
        #bs=bss[0]
        bsshape=cmds.listRelatives(bs,s=1,ni=1)
        bstype=cmds.nodeType(bsshape)
        if not inputtype==orgtype==bstype:
            cmds.confirmDialog( title='error', message='input,original and blendshapes\'s type is different,check it and try again!', button='got it!',defaultButton='Yes', cancelButton='No', dismissString='No')
            return False
    unshape=cmds.listRelatives(un,s=1,ni=1)
    untype=cmds.nodeType(unshape)
    unbshape=cmds.listRelatives(unbase,s=1,ni=1)
    unbtype=cmds.nodeType(unbshape)
    if not untype==unbtype:
        cmds.confirmDialog( title='error', message='underworld dirven mesh and underworld base mesh\'s type is different,check it and try again!', button='got it!',defaultButton='Yes', cancelButton='No', dismissString='No')
        return False
    uwbs=cmds.deformer(input,type='underworldBlendShape')
    cmds.connectAttr(org+'.outMesh',uwbs[0]+'.orm')
    if untype=='mesh':
        cmds.connectAttr(un+'.outMesh',uwbs[0]+'.ugm')
    if untype=='nurbsSurface':
        cmds.connectAttr(un+'.local',uwbs[0]+'.ugm')
    if unbtype=='mesh':
        cmds.connectAttr(unbase+'.outMesh',uwbs[0]+'.ubm')
    if unbtype=='nurbsSurface':
        cmds.connectAttr(unbase+'.local',uwbs[0]+'.ubm')
    index=0
    for bs in bss:
        ##bs=bss[0]
        attrname=bs.replace('|','_')
        cmds.connectAttr(bs+'.outMesh',uwbs[0]+'.bst['+str(index)+'].bsm')
        cmds.addAttr(uwbs[0],ln=attrname,at='double',min=0,max=1,dv=0)
        cmds.setAttr(uwbs[0]+'.'+attrname,e=1,keyable=1)
        cmds.connectAttr(uwbs[0]+'.'+attrname,uwbs[0]+'.bst['+str(index)+'].bsv')
        index+=1

def edo_loadDeformMesh():
    nodetype=''
    sels=cmds.ls(sl=1)
    if sels==None:
        cmds.confirmDialog( title='error', message='please select something,and try again!', button='got it!',defaultButton='Yes', cancelButton='No', dismissString='No')
        return False
    if not len(sels)==1:
        cmds.confirmDialog( title='error', message='you must select only one object,please try again!', button='got it!',defaultButton='Yes', cancelButton='No', dismissString='No')
        return False
    shape=cmds.listRelatives(sels,s=1,ni=1)
    if shape==None:
        nodetype=cmds.nodeType(sels[0])
        if not nodetype=='mesh' and not nodetype=='nurbsCurve':
            cmds.confirmDialog( title='error', message='you must select nurbsCurve or mesh,please check you selected and try again!', button='got it!',defaultButton='Yes', cancelButton='No', dismissString='No')
            return False
        cmds.textFieldButtonGrp('deform_Mesh',e=1,text=sels[0])
        return True
    if not len(shape)==1:
        cmds.confirmDialog( title='error', message='select object have two shape node,please select the shape node,and try again!', button='got it!',defaultButton='Yes', cancelButton='No', dismissString='No')
        return False
    nodetype=cmds.nodeType(shape)
    if not nodetype=='mesh' and not nodetype=='nurbsCurve':
        cmds.confirmDialog( title='error', message='you must select nurbsCurve or mesh,please check you selected and try again!', button='got it!',defaultButton='Yes', cancelButton='No', dismissString='No')
        return False
    cmds.textFieldButtonGrp('deform_Mesh',e=1,text=sels[0])
    return True
    
def edo_loadorgMesh():
    nodetype=''
    sels=cmds.ls(sl=1)
    if sels==None:
        cmds.confirmDialog( title='error', message='please select something,and try again!', button='got it!',defaultButton='Yes', cancelButton='No', dismissString='No')
        return False
    if not len(sels)==1:
        cmds.confirmDialog( title='error', message='you must select only one object,please try again!', button='got it!',defaultButton='Yes', cancelButton='No', dismissString='No')
        return False
    shape=cmds.listRelatives(sels,s=1,ni=1)
    if shape==None:
        nodetype=cmds.nodeType(sels[0])
        if not nodetype=='mesh' and not nodetype=='nurbsCurve':
            cmds.confirmDialog( title='error', message='you must select nurbsCurve or mesh,please check you selected and try again!', button='got it!',defaultButton='Yes', cancelButton='No', dismissString='No')
            return False
        cmds.textFieldButtonGrp('original_Mesh',e=1,text=sels[0])
        return True
    if not len(shape)==1:
        cmds.confirmDialog( title='error', message='select object have two shape node,please select the shape node,and try again!', button='got it!',defaultButton='Yes', cancelButton='No', dismissString='No')
        return False
    nodetype=cmds.nodeType(shape)
    if not nodetype=='mesh' and not nodetype=='nurbsCurve':
        cmds.confirmDialog( title='error', message='you must select nurbsCurve or mesh,please check you selected and try again!', button='got it!',defaultButton='Yes', cancelButton='No', dismissString='No')
        return False
    cmds.textFieldButtonGrp('original_Mesh',e=1,text=sels[0])
    return True
    
def edo_loaduwMesh():
    nodetype=''
    sels=cmds.ls(sl=1)
    if sels==None:
        cmds.confirmDialog( title='error', message='please select something,and try again!', button='got it!',defaultButton='Yes', cancelButton='No', dismissString='No')
        return False
    if not len(sels)==1:
        cmds.confirmDialog( title='error', message='you must select only one object,please try again!', button='got it!',defaultButton='Yes', cancelButton='No', dismissString='No')
        return False
    shape=cmds.listRelatives(sels,s=1,ni=1)
    if shape==None:
        nodetype=cmds.nodeType(sels[0])
        if not nodetype=='mesh' and not nodetype=='nurbsSurface':
            cmds.confirmDialog( title='error', message='you must select nurbsSurface or mesh,please check you selected and try again!', button='got it!',defaultButton='Yes', cancelButton='No', dismissString='No')
            return False
        cmds.textFieldButtonGrp('underworld_dirven_Mesh',e=1,text=sels[0])
        return True
    if not len(shape)==1:
        cmds.confirmDialog( title='error', message='select object have two shape node,please select the shape node,and try again!', button='got it!',defaultButton='Yes', cancelButton='No', dismissString='No')
        return False
    nodetype=cmds.nodeType(shape)
    if not nodetype=='mesh' and not nodetype=='nurbsSurface':
        cmds.confirmDialog( title='error', message='you must select nurbsSurface or mesh,please check you selected and try again!', button='got it!',defaultButton='Yes', cancelButton='No', dismissString='No')
        return False
    cmds.textFieldButtonGrp('underworld_dirven_Mesh',e=1,text=sels[0])
    return True
    
def edo_loaduwbMesh():
    nodetype=''
    sels=cmds.ls(sl=1)
    if sels==None:
        cmds.confirmDialog( title='error', message='please select something,and try again!', button='got it!',defaultButton='Yes', cancelButton='No', dismissString='No')
        return False
    if not len(sels)==1:
        cmds.confirmDialog( title='error', message='you must select only one object,please try again!', button='got it!',defaultButton='Yes', cancelButton='No', dismissString='No')
        return False
    shape=cmds.listRelatives(sels,s=1,ni=1)
    if shape==None:
        nodetype=cmds.nodeType(sels[0])
        if not nodetype=='mesh' and not nodetype=='nurbsSurface':
            cmds.confirmDialog( title='error', message='you must select nurbsSurface or mesh,please check you selected and try again!', button='got it!',defaultButton='Yes', cancelButton='No', dismissString='No')
            return False
        cmds.textFieldButtonGrp('underworld_base_Mesh',e=1,text=sels[0])
        return True
    if not len(shape)==1:
        cmds.confirmDialog( title='error', message='select object have two shape node,please select the shape node,and try again!', button='got it!',defaultButton='Yes', cancelButton='No', dismissString='No')
        return False
    nodetype=cmds.nodeType(shape)
    if not nodetype=='mesh' and not nodetype=='nurbsSurface':
        cmds.confirmDialog( title='error', message='you must select nurbsSurface or mesh,please check you selected and try again!', button='got it!',defaultButton='Yes', cancelButton='No', dismissString='No')
        return False
    cmds.textFieldButtonGrp('underworld_base_Mesh',e=1,text=sels[0])
    return True

def edo_loadbsMesh():
    allbs=[]
    nodetype=''
    sels=cmds.ls(sl=1)
    if sels==None:
        cmds.confirmDialog( title='error', message='please select something,and try again!', button='got it!',defaultButton='Yes', cancelButton='No', dismissString='No')
        return False
    for sel in sels:
        shape=cmds.listRelatives(sel,s=1,ni=1)
        if shape==None:
            nodetype=cmds.nodeType(sels[0])
            if not nodetype=='mesh' and not nodetype=='nurbsCurve':
                cmds.confirmDialog( title='error', message='you must select nurbsCurves or meshs,please check you selected and try again!', button='got it!',defaultButton='Yes', cancelButton='No', dismissString='No')
                return False
            allbs.append(sel)
            return True
        if not len(shape)==1:
            cmds.confirmDialog( title='error', message='select object have two shape node,please select the shape node,and try again!', button='got it!',defaultButton='Yes', cancelButton='No', dismissString='No')
            return False
        nodetype=cmds.nodeType(shape)
        if not nodetype=='mesh' and not nodetype=='nurbsCurve':
            cmds.confirmDialog( title='error', message='you must select nurbsCurve or mesh,please check you selected and try again!', button='got it!',defaultButton='Yes', cancelButton='No', dismissString='No')
            return False    
        allbs.append(sel)
    txt=edo_strArrayToStr(allbs,',')
    cmds.textFieldButtonGrp('blendShape_Meshes',e=1,text=txt)
    return True

def edo_strArrayToStr(array,flag):
    txt=''
    for a in array:
        txt=txt+flag+a
    return txt[1:]
       
##edo_createUnderWorldBlendShape('input','org','un','unbase',['bs_up','bs_dn','bs_rt','bs_lf'])
def edo_finalButtonCmd():
    input=cmds.textFieldButtonGrp('deform_Mesh',q=1,text=1)
    org=cmds.textFieldButtonGrp('original_Mesh',q=1,text=1)
    un=cmds.textFieldButtonGrp('underworld_dirven_Mesh',q=1,text=1)
    unbase=cmds.textFieldButtonGrp('underworld_base_Mesh',q=1,text=1)
    bsstr=cmds.textFieldButtonGrp('blendShape_Meshes',q=1,text=1)
    bss=bsstr.split(',')
    edo_createUnderWorldBlendShape(input,org,un,unbase,bss)


def edo_createUnderWorldBlendShapeUI():
    cmds.loadPlugin('underworldBlendShape.mll',qt=1)
    if cmds.window('edo_createUnderworldBlendShapeUI',ex=1):
        cmds.deleteUI('edo_createUnderworldBlendShapeUI')
    cmds.window('edo_createUnderworldBlendShapeUI',t='edo_createUnderworldBlendShapeUI',w=500,h=100)
    cmds.columnLayout('edo_createUnderworldBlendShapeCL',adjustableColumn=True,rs=5)
    cmds.textFieldButtonGrp('deform_Mesh', label='deform Mesh:            ',text='',buttonLabel='load selected',bc='edo_loadDeformMesh()')
    cmds.textFieldButtonGrp('original_Mesh', label='original Mesh:          ',text='',buttonLabel='load selected',bc='edo_loadorgMesh()')
    cmds.textFieldButtonGrp('underworld_dirven_Mesh', label='underworld dirven Mesh: ',text='',buttonLabel='load selected',bc='edo_loaduwMesh()')
    cmds.textFieldButtonGrp('underworld_base_Mesh', label='underworld base Mesh:   ',text='',buttonLabel='load selected',bc='edo_loaduwbMesh()')
    cmds.textFieldButtonGrp('blendShape_Meshes', label='blendShape Meshes:   ',text='',buttonLabel='load selected',bc='edo_loadbsMesh()')
    cmds.button('createButton',l='create underworldBlendShape deformer',ann='',c='edo_finalButtonCmd()')
    cmds.showWindow('edo_createUnderworldBlendShapeUI')
    cmds.window('edo_createUnderworldBlendShapeUI',e=1,w=500,h=100)
edo_createUnderWorldBlendShapeUI()