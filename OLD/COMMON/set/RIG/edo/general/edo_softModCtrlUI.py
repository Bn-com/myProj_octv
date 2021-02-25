import maya.cmds as cmds
def edo_addSoftModCtrl(ctrlName,falloffRadius):
    sels=cmds.ls(sl=1)
    meshs=[]
    for i in sels:
        #i=sels[0]
        mesh=cmds.listRelatives(i,s=1,ni=1)[0]
        if cmds.nodeType(mesh)=='mesh':
            meshs.append(mesh)
    if (cmds.objExists(ctrlName+'_deformer') or cmds.objExists(ctrlName+'_weightCtrl') or cmds.objExists(ctrlName+'_Ctrl') or cmds.objExists(ctrlName+'_loc') or cmds.objExists(ctrlName+'_softModHandle') or cmds.objExists('GRP_'+ctrlName+'_weightCtrl') or cmds.objExists('GRP_'+ctrlName+'_Ctrl')):
        cmds.confirmDialog( title='scene is not clear', message='this scene is not clear,the program create some node\'name is already exists!you must use oher name or delete the exists nodes in this scene!', button='got it!',defaultButton='Yes', cancelButton='No', dismissString='No')
        return 0
    cmds.deformer(meshs,type='softMod',name=ctrlName+'_softModDeformer')
    index=0
    for mesh in meshs:
        cmds.connectAttr(mesh+'.worldMatrix',ctrlName+'_softModDeformer.geomMatrix['+str(index)+']',f=1)
        index+=1
    cmds.delete(cmds.circle(nr=(0,1,0),r=1.5,n=ctrlName+'_weightCtrl')[1])
    cmds.delete(cmds.circle(nr=(0,1,0),r=1,n=ctrlName+'_Ctrl')[1])
    cmds.setAttr(ctrlName+'_weightCtrlShape.overrideEnabled',1)
    cmds.setAttr(ctrlName+'_weightCtrlShape.ovc',17)
    cmds.setAttr(ctrlName+'_CtrlShape.overrideEnabled',1)
    cmds.setAttr(ctrlName+'_CtrlShape.ovc',13)
    cmds.spaceLocator(n=ctrlName+'_loc')
    cmds.parent(ctrlName+'_loc',ctrlName+'_weightCtrl')
    cmds.group(ctrlName+'_Ctrl',n='GRP_'+ctrlName+'_Ctrl')
    cmds.group(ctrlName+'_weightCtrl',n='GRP_'+ctrlName+'_weightCtrl')
    cmds.parent('GRP_'+ctrlName+'_Ctrl',ctrlName+'_weightCtrl')
    cmds.setAttr(ctrlName+'_loc.v',0)
    cmds.createNode('softModHandle',n=ctrlName+'_softModHandle',p=ctrlName+'_Ctrl')
    cmds.addAttr(ctrlName+'_Ctrl',ln='falloffRadius',at='double',min=0)
    cmds.setAttr(ctrlName+'_Ctrl.falloffRadius',falloffRadius,keyable=1)
    cmds.connectAttr(ctrlName+'_softModHandle.softModTransforms',ctrlName+'_softModDeformer.softModXforms',f=1)
    cmds.connectAttr(ctrlName+'_Ctrl.worldMatrix',ctrlName+'_softModDeformer.matrix',f=1)
    cmds.connectAttr(ctrlName+'_Ctrl.parentInverseMatrix',ctrlName+'_softModDeformer.bindPreMatrix',f=1)
    cmds.connectAttr(ctrlName+'_locShape.worldPosition',ctrlName+'_softModDeformer.falloffCenter',f=1)
    cmds.connectAttr(ctrlName+'_Ctrl.falloffRadius',ctrlName+'_softModDeformer.falloffRadius',f=1)
    return 1

def edo_createSoftModCtrlCmd():
    ctrlname=cmds.textField('edo_softModCtrlUItextField',q=1,text=1)
    if (ctrlname==''):
        cmds.confirmDialog( title='filed the ctrlName first', message='please filed the ctrl name first in the textFiled!', button='got it!',defaultButton='Yes', cancelButton='No', dismissString='No')
        return 0
    falloffRadius=cmds.floatSliderButtonGrp('edo_softModCtrlUIfloatSliderButtonGrp',q=1,v=1)
    edo_addSoftModCtrl(ctrlname,falloffRadius)
    
def edo_softModCtrlUI():
    if cmds.window('edo_softModCtrlUI',ex=1):
        cmds.deleteUI('edo_softModCtrlUI')
    cmds.window('edo_softModCtrlUI',t='add softModCtrlUI',w=400,h=120)
    cmds.columnLayout('edo_softModCtrlUILayout',adjustableColumn=True,rs=10)
    cmds.text('edo_softModCtrlUIText',l='filed the ctrl name:')
    cmds.textField('edo_softModCtrlUItextField')
    cmds.floatSliderButtonGrp('edo_softModCtrlUIfloatSliderButtonGrp',cw4=[65,40,120,40],ct4=['left','left','left','left'],label='falloffRadius',field=True, buttonLabel='create',bc='edo_createSoftModCtrlCmd()')
    cmds.showWindow('edo_softModCtrlUI')
    cmds.window('edo_softModCtrlUI',e=1,w=300,h=100)
edo_softModCtrlUI()