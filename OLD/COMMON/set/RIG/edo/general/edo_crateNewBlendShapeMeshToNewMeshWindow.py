#-*- coding: utf-8 -*-
import maya.cmds as cm
import maya.mel  as mel
global edo_crateNewBlendShapeMeshToNewMesh_org
global edo_crateNewBlendShapeMeshToNewMesh_new

def edo_crateNewBlendShapeMeshToNewMeshWindow():
    if cm.window("crateNewBlendShapeMeshToNewMeshWindow",ex=1):
        cm.deleteUI("crateNewBlendShapeMeshToNewMeshWindow")
    cm.window("crateNewBlendShapeMeshToNewMeshWindow",title="crateNewBlendShapeMeshToNewMesh")

    cm.columnLayout( columnAttach=('both', 5), rowSpacing=2, columnWidth=350)

    cm.button('crateNewBlendShapeMeshToNewMeshBT1',label='load orgMesh',bgc=(0.9,0.7,0.1),c='edo_checkBT1()')
    cm.text( label='=====================================' )

    cm.button('crateNewBlendShapeMeshToNewMeshBT2',label='load newMesh',bgc=(0.9,0.7,0.1),c='edo_checkBT2()')
    cm.text( label='=====================================' )

    cm.text( label='and the last,please select the all blendShapeMesh')
    cm.button('crateNewBlendShapeMeshToNewMeshBT3',label='start',bgc=(0.5,0.8,1),c='edo_edo_crateNewBlendShapeMeshToNewMesh()')

    cm.window("crateNewBlendShapeMeshToNewMeshWindow",e=1,widthHeight=(360,160))
    cm.showWindow("crateNewBlendShapeMeshToNewMeshWindow");
edo_crateNewBlendShapeMeshToNewMeshWindow();


def edo_checkBT1():
    global edo_crateNewBlendShapeMeshToNewMesh_org
    global edo_crateNewBlendShapeMeshToNewMesh_new
    edo_crateNewBlendShapeMeshToNewMesh_org=cm.ls(sl=1)
    if len(edo_crateNewBlendShapeMeshToNewMesh_org)==1:
        print edo_crateNewBlendShapeMeshToNewMesh_org[0]
        cm.button('crateNewBlendShapeMeshToNewMeshBT1',e=1,bgc=(0.2,0.8,0.1),label=edo_crateNewBlendShapeMeshToNewMesh_org[0])
    else:
        cm.confirmDialog( title='error', message='please Select onlyOne OrgMesh', button='Yes', defaultButton='Yes', cancelButton='YES', dismissString='YES' )
        return;
       
def edo_checkBT2():
    global edo_crateNewBlendShapeMeshToNewMesh_org
    global edo_crateNewBlendShapeMeshToNewMesh_new
    edo_crateNewBlendShapeMeshToNewMesh_new=cm.ls(sl=1)
    if len(edo_crateNewBlendShapeMeshToNewMesh_new)==1:
        print edo_crateNewBlendShapeMeshToNewMesh_new[0]
        cm.button('crateNewBlendShapeMeshToNewMeshBT2',e=1,bgc=(0.2,0.8,0.1),label=edo_crateNewBlendShapeMeshToNewMesh_new[0])
    else:
        cm.confirmDialog( title='error', message='please Select onlyOne NewMesh', button='Yes', defaultButton='Yes', cancelButton='YES', dismissString='YES' )
        return;
        
def edo_transferTransformation(source,target):
    cm.setAttr(target+".tx",cm.getAttr(source+".tx"))
    cm.setAttr(target+".ty",cm.getAttr(source+".ty"))  
    cm.setAttr(target+".tz",cm.getAttr(source+".tz"))
    cm.setAttr(target+".rx",cm.getAttr(source+".rx"))
    cm.setAttr(target+".ry",cm.getAttr(source+".ry"))
    cm.setAttr(target+".rz",cm.getAttr(source+".rz"))
    cm.setAttr(target+".sx",cm.getAttr(source+".sx"))
    cm.setAttr(target+".sy",cm.getAttr(source+".sy"))
    cm.setAttr(target+".sz",cm.getAttr(source+".sz"))

def edo_edo_crateNewBlendShapeMeshToNewMesh():
    global edo_crateNewBlendShapeMeshToNewMesh_org
    global edo_crateNewBlendShapeMeshToNewMesh_new
    allbs=cm.ls(sl=1);
    if len(allbs)>0:
        print allbs
        grp=cm.createNode('transform', n='GRP_newBlendShape')
        edo_transferTransformation(edo_crateNewBlendShapeMeshToNewMesh_org[0],edo_crateNewBlendShapeMeshToNewMesh_new[0])
        cm.select(edo_crateNewBlendShapeMeshToNewMesh_new[0],r=1)
        cm.select(edo_crateNewBlendShapeMeshToNewMesh_org[0],add=1)
        mel.eval('CreateWrap');
        cm.select(allbs,r=1)
        cm.select(edo_crateNewBlendShapeMeshToNewMesh_org[0],add=1)
        bsnode=cm.blendShape(frontOfChain=1,origin='local')
        for bs in allbs:
            ##bs=allbs[0]
            bsattr=bsnode[0]+'.'+bs
            cm.setAttr(bsattr,1)
            newbs=cm.duplicate(edo_crateNewBlendShapeMeshToNewMesh_new[0],n=edo_crateNewBlendShapeMeshToNewMesh_new[0]+"_"+bs)
            edo_transferTransformation(bs,newbs[0])
            cm.parent(newbs[0],grp)
            cm.setAttr(bsattr,0)
        cm.select(edo_crateNewBlendShapeMeshToNewMesh_new[0],edo_crateNewBlendShapeMeshToNewMesh_org[0])
        mel.eval('DeleteHistory')
        cm.button('crateNewBlendShapeMeshToNewMeshBT1',e=1,label='load orgMesh',bgc=(0.9,0.7,0.1))
        cm.button('crateNewBlendShapeMeshToNewMeshBT2',e=1,label='load newMesh',bgc=(0.9,0.7,0.1))
        cm.showWindow("crateNewBlendShapeMeshToNewMeshWindow");
    else:
        cm.confirmDialog( title='error', message='please Select the all blendShapeMesh(blend For Org)', button='Yes', defaultButton='Yes', cancelButton='YES', dismissString='YES' )
        return;
