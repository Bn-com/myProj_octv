import maya.cmds as cmds
def edo_addSingleIkCtrlCmd():
    sels=cmds.ls(sl=1,type='joint')
    if sels:
        for sel in sels:
            edo_addSingleIkCtrl(sel)

def edo_addSingleIkCtrl(jnt):
    #jnt='Lf1_tipleg_drv_jnt_IK'
    basejnt=cmds.listRelatives(jnt,c=1,type='joint',pa=1)[0]
    hd=cmds.ikHandle(sj=jnt,ee=basejnt,sol='ikRPsolver',n=jnt.replace('_jnt','_ikhandle').replace('_joint','_ikhandle').replace('_JNT','_ikhandle'))
    hdgrp=cmds.group(hd[0],n='GRP_'+hd[0])
    cmds.xform(hdgrp,ws=1,piv=cmds.xform(hd[0],q=1,ws=1,t=1))
    basectrl=basejnt.replace('_jnt','_CTRL').replace('_joint','_CTRL').replace('_JNT','_CTRL')
    tipctrl=jnt.replace('_jnt','_CTRL').replace('_joint','_CTRL').replace('_JNT','_CTRL')
    tipallctrl=jnt.replace('_jnt','_ALL_CTRL').replace('_joint','_ALL_CTRL').replace('_JNT','_ALL_CTRL')
    edo_gdcfrig2012_createCtrl(basectrl,'box',6)
    basectrlgrp='GRP_'+basectrl
    edo_gdcfrig2012_createCtrl(tipctrl,'box',13)
    tipctrlgrp='GRP_'+tipctrl
    edo_gdcfrig2012_createCtrl(tipallctrl,'box',6)
    tipallctrlgrp='GRP_'+tipallctrl
    cmds.xform(basectrlgrp,ws=1,t=cmds.xform(basejnt,q=1,ws=1,t=1))
    cmds.xform(tipctrlgrp,ws=1,t=cmds.xform(jnt,q=1,ws=1,t=1))
    cmds.xform(tipallctrlgrp,ws=1,t=cmds.xform(jnt,q=1,ws=1,t=1))
    cmds.parent(hdgrp,basectrl)
    cmds.parent(jnt,tipctrl)
    cmds.parent(basectrlgrp,tipallctrl)
    cmds.parent(tipctrlgrp,tipallctrl)
    #addAttr
    cmds.addAttr(basectrl,ln='AutoStretch',at='double',min=0,max=1)
    cmds.setAttr(basectrl+'.AutoStretch',e=1,k=1)
    cmds.addAttr(basectrl,ln='reverseValue',at='double',min=-1,max=1)
    cmds.setAttr(basectrl+'.reverseValue',e=1,k=1)
    cmds.setAttr(basectrl+'.reverseValue',1)
    tiploc=cmds.spaceLocator(n=jnt.replace('_jnt','_LOC').replace('_joint','_LOC').replace('_JNT','_LOC'))
    baseloc=cmds.spaceLocator(n=basejnt.replace('_jnt','_LOC').replace('_joint','_LOC').replace('_JNT','_LOC'))
    cmds.parent(tiploc[0],tipctrl)
    cmds.parent(baseloc[0],basectrl)
    edo_setZeroTransform(tiploc[0])
    edo_setZeroTransform(baseloc[0])
    dis=cmds.createNode('distanceBetween',n=jnt.replace('_jnt','_distance').replace('_joint','_distance').replace('_JNT','_distance'))
    cmds.connectAttr(tiploc[0]+'.worldPosition',dis+'.point1',f=1)
    cmds.connectAttr(baseloc[0]+'.worldPosition',dis+'.point2',f=1)
    orglen=cmds.getAttr(basejnt+'.tx')
    globalmd=cmds.createNode('multiplyDivide',n='GLOBALSCALE_'+hd[0]+'_multiplyDivide')
    globalloc=cmds.spaceLocator(n=globalmd.replace('_multiplyDivide','_LOC'))
    cmds.connectAttr(globalloc[0]+'.sy',globalmd+'.input1X',f=1)
    cmds.setAttr(globalmd+'.input2X',orglen)
    cmds.setAttr(globalmd+'.operation',1)
    stretchmd=cmds.createNode('multiplyDivide',n='STRETCH_'+hd[0]+'_multiplyDivide')
    cmds.connectAttr(globalmd+'.outputX',stretchmd+'.input2X',f=1)
    reversemd=cmds.createNode('multiplyDivide',n='REVERSE_'+hd[0]+'_multiplyDivide')
    cmds.connectAttr(dis+'.distance',reversemd+'.input1X',f=1)
    cmds.connectAttr(basectrl+'.reverseValue',reversemd+'.input2X',f=1)
    cmds.connectAttr(reversemd+'.outputX',stretchmd+'.input1X',f=1)
    cmds.setAttr(stretchmd+'.operation',2)
    finalmd=cmds.createNode('multiplyDivide',n='FINAL_'+hd[0]+'_multiplyDivide')
    cmds.setAttr(finalmd+'.input1X',orglen)
    cmds.connectAttr(stretchmd+'.outputX',finalmd+'.input2X',f=1)
    blendnode=cmds.createNode('blendTwoAttr',n='AUTOSTRETCH_'+hd[0]+'_blendTwoAttr')
    cmds.connectAttr(basectrl+'.AutoStretch',blendnode+'.attributesBlender')
    cmds.setAttr(blendnode+'.input[0]',orglen)
    cmds.connectAttr(finalmd+'.outputX',blendnode+'.input[1]',f=1)
    cmds.connectAttr(blendnode+'.output',basejnt+'.tx',f=1)
    
    
def edo_setZeroTransform(obj):
    #obj=tiploc[0]
    cmds.setAttr(obj+'.tx',e=1,l=0)
    cmds.setAttr(obj+'.tx',0)
    cmds.setAttr(obj+'.ty',e=1,l=0)
    cmds.setAttr(obj+'.ty',0)
    cmds.setAttr(obj+'.tz',e=1,l=0)
    cmds.setAttr(obj+'.tz',0)
    cmds.setAttr(obj+'.rx',e=1,l=0)
    cmds.setAttr(obj+'.rx',0)
    cmds.setAttr(obj+'.ry',e=1,l=0)
    cmds.setAttr(obj+'.ry',0)
    cmds.setAttr(obj+'.rz',e=1,l=0)
    cmds.setAttr(obj+'.rz',0) 
    cmds.setAttr(obj+'.sx',e=1,l=0)
    cmds.setAttr(obj+'.sx',0)
    cmds.setAttr(obj+'.sy',e=1,l=0)
    cmds.setAttr(obj+'.sy',0)
    cmds.setAttr(obj+'.sz',e=1,l=0)
    cmds.setAttr(obj+'.sz',0)
     
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