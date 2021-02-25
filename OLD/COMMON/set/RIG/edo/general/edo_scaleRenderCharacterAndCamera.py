#-*- coding: utf-8 -*-
import maya.cmds as cmds
import maya.mel as mel
def edo_scaleRenderCharacterAndCamera(mode=1):
    sels=cmds.ls(sl=1)
    if sels==None or sels==[]:
        cmds.confirmDialog( title='选择错误', message='请先选择所有的模型,再选所有摄像机的组', button='god it',defaultButton='Yes', cancelButton='No', dismissString='No')
        return False
    mesh=sels[0]
    cam=sels[1]
    cmds.select(mesh)
    clus=mel.eval("newCluster \" -envelope 1\";")
    cn=cmds.rename(clus[1],'CLUS_renderGlobalScale')
    parentc=cmds.parentConstraint(cn,cam,mo=1)
    scalec=cmds.scaleConstraint(cn,cam,mo=1)
    if mode==1:
        cmds.setAttr(cn+'.sx',100)
        cmds.setAttr(cn+'.sy',100)
        cmds.setAttr(cn+'.sz',100)
    if mode==0:
        cluspo=cmds.xform(cn,q=1,ws=1,rp=1)
        cmds.xform(cn,ws=1,t=[-cluspo[0],-cluspo[1],-cluspo[2]])