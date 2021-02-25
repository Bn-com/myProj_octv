import maya.cmds as cmds
#edo_addArmLegIkTipCtrl(['Lf1Leg_ALL_CTRL_GRP','Rt1Leg_ALL_CTRL_GRP'])
def edo_addArmLegIkTipCtrlCmd():
    sels=cmds.ls(sl=1)
    if sels:
        edo_addArmLegIkTipCtrl(sels)

def edo_addArmLegIkTipCtrl(parentGrp=['LfLeg_ALL_CTRL_GRP','RtLeg_ALL_CTRL_GRP','LfArm_ALL_CTRL_GRP','RtArm_ALL_CTRL_GRP']):
    for grp in parentGrp:
        #grp='Lf1Leg_ALL_CTRL_GRP'
        if cmds.objExists(grp):
            ctrl=grp.replace('_GRP','')
            edo_gdcfrig2012_createCtrl(ctrl,'box',13)
            ctrlGrp='GRP_'+ctrl
            cmds.xform(ctrlGrp,ws=1,t=cmds.xform(grp,q=1,ws=1,t=1))
            p=cmds.listRelatives(grp,p=1,pa=1)[0]
            ggrp=cmds.group(grp,n='GRP_'+grp)
            cmds.parent(ggrp,ctrl)
            cmds.parent(ctrlGrp,p)
            
#edo_gdcfrig2012_createCtrl('facialCtrlPanle_FRAME','square',6)
def edo_gdcfrig2012_createCtrl(name,shape='box',colorid=17):
    #name='ctrl'
    #colorid=17
    if shape=='box':
        cmds.curve(n=name,d=1,p=[[-0.5,-0.5,-0.5],[0.5,-0.5,-0.5],[0.5,-0.5,0.5],[-0.5,-0.5,0.5],[-0.5,-0.5,-0.5],[-0.5,0.5,-0.5],[0.5,0.5,-0.5],[0.5,-0.5,-0.5],[0.5,0.5,-0.5],[0.5,0.5,0.5],[0.5,-0.5,0.5],[0.5,0.5,0.5],[-0.5,0.5,0.5],[-0.5,-0.5,0.5],[-0.5,0.5,0.5],[-0.5,0.5,-0.5]])
    if shape=='circle':
        cmds.delete(cmds.circle(ch=1,o=1,nr=[0,1,0],n=name)[1])
    if shape=='square':
        cmds.curve(n=name,d=1,p=[[-10,-10,0],[-10,10,0],[10,10,0],[10,-10,0],[-10,-10,0]])
    cmds.group(name,n='GRP_'+name)
    ss=cmds.listRelatives(name,s=1)[0]
    cmds.rename(ss,name+'Shape')
    cmds.setAttr(name+'Shape.overrideEnabled',1)
    cmds.setAttr(name+'Shape.ovc',colorid)
