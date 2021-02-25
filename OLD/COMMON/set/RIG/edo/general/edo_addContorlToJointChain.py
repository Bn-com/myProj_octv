def edo_gdcfrig2012_createCtrl(name,shape='box',colorid=17):
    #name='tail_ik_ctrl0'
    #colorid=13
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

def edo_addContorlToJoint(jnt):
    #jnt='tail_jnt0'
    fkctrlname=jnt.replace('joint','fk_ctrl').replace('jnt','fk_ctrl').replace('JNT','FK_CTRL').replace('JOINT','FK_CTRL')
    ikctrlname=jnt.replace('joint','ik_ctrl').replace('jnt','ik_ctrl').replace('JNT','IK_CTRL').replace('JOINT','IK_CTRL')
    edo_gdcfrig2012_createCtrl(fkctrlname,'box',6)
    edo_gdcfrig2012_createCtrl(ikctrlname,'circle',13)
    cmds.parent('GRP_'+ikctrlname,fkctrlname)
    cmds.parent('GRP_'+fkctrlname,jnt)
    cmds.setAttr('GRP_'+fkctrlname+'.tx',0)
    cmds.setAttr('GRP_'+fkctrlname+'.ty',0)
    cmds.setAttr('GRP_'+fkctrlname+'.tz',0)
    cmds.setAttr('GRP_'+fkctrlname+'.rx',0)
    cmds.setAttr('GRP_'+fkctrlname+'.ry',0)
    cmds.setAttr('GRP_'+fkctrlname+'.rz',0)
    cmds.parent('GRP_'+fkctrlname,w=1)
    cmds.setAttr(ikctrlname+'.rz',90)
    cmds.makeIdentity(ikctrlname,apply=1,t=1,r=1,s=1,n=0)
    cmds.parentConstraint(ikctrlname,jnt,mo=0)
    cmds.scaleConstraint(ikctrlname,jnt,mo=1)
    return fkctrlname
    

def edo_addContorlToJointChain():
    cmds.select(hi=1)
    sels=cmds.ls(sl=1,type='joint')
    name=''
    firstCtrl=''
    for sel in sels:
        #sel='tail_jnt0'
        fkctrlname=edo_addContorlToJoint(sel)
        if not name=='':
            cmds.parent('GRP_'+fkctrlname,name)
        name=fkctrlname
        if firstCtrl=='':
            firstCtrl='GRP_'+fkctrlname
    return firstCtrl