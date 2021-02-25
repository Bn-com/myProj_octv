#coding:utf-8
import maya.cmds as cmds
def createHairBeardIKCtrl():
    #aotu CreateHair/bread IK Ctrls
    #选择需要打splineIK的第一个Jnt执行这个命令
    
    fsJntsel=cmds.ls(sl=True,r=True);
    print 'fristJnt:',fsJntsel
    endJntsel=cmds.select(fsJntsel,hi=True)
    allJnt=cmds.ls(sl=True,fl=True)
    print 'allJnt:',allJnt#allJntOrder
    endJntsel=allJnt[-1];
    print 'EndJnt:',allJnt #allJntOrder
    cmds.setAttr(endJntsel+'.jointOrientX', 0)
    cmds.setAttr(endJntsel+'.jointOrientY', 0)
    cmds.setAttr(endJntsel+'.jointOrientZ', 0)
    
    #[2]prefixName,copy出另外一套Jnt用于做次级IK,createIKSpline
    #比如select -r joint1 joint2 joint_3 joint4 joint5 joint6;
    cmds.select(clear=True)
    cmds.select(allJnt)
    xiahua='_'
    t=0
    obj=cmds.ls(sl=True,r=True)
    lenth=len(obj)
    for t in range(0,lenth):  
        if xiahua not in obj[t]:        
            pnewname=str(fsJntsel[0])
            print t,'can not find "_",so define prefix name:'+pnewname;
            t=t+1
        else:
             print t,'JointName:',obj[t],'ThisJointHave"_"'
             for i in range(0,lenth):
                 newname=obj[t]
                 lenth1=len(newname)
                 if xiahua==newname[i]:
                     pnewname=newname[0:i]+'_'
                     print '-----so the prefix name is:',pnewname
                     break
                        
    #复制
    cmds.select(clear=True)
    cmds.select(allJnt)
    #这个前缀关系到后面的选择（4）
    dupJnt=cmds.duplicate(rr=True,name=pnewname+'secJnt#');
    cmds.select(dupJnt[0],deselect=True)
    cmds.parent(world=True)
    #------------splineIk
    try:
        cmds.ikHandle(name=pnewname+'ikHandle',startJoint=fsJntsel[0],endEffector=endJntsel,numSpans=3,solver='ikSplineSolver',
    rootOnCurve=True,parentCurve=True,createCurve=True,simplifyCurve=False,twistType='linear')
    except:
        pass
    #(3)-------------------rename------
    #cmds.nodeType('effector1')
    cmds.select(pnewname+'ikHandle')
    ikcv=cmds.ls(sl=True,r=True)
    ikcvSel=cmds.listConnections(ikcv,type='nurbsCurve')
    ikcvName=cmds.rename(ikcvSel,pnewname+'curve')
    
    effectSel =cmds.listConnections(ikcv,type='ikEffector')
    effectName=cmds.rename(effectSel,pnewname+'effector')
    
    #(4)---secJnt skin with Ikcurve------把ik线条与新复制的一套IKjoint蒙皮---
    cmds.select(pnewname+'secJnt*')
    cmds.select(ikcvName,add=True)
    cmds.skinCluster(toSelectedBones=True,maximumInfluences=10,skinMethod=3,dropoffRate=4,removeUnusedInfluence=True)
    #(5)----create Ctrls
    cmds.select(d=1)
    cmds.select(pnewname+'secJnt*',r=True)
    mesh=cmds.ls(sl=True)
    length=len(mesh)
    u=1
    GRPsec01=cmds.group(em=True,n='GRP_'+pnewname+'secCtrls')
    for u in range(length):
        cvpo=cmds.xform(mesh[u],q=1,ws=1,t=1)
        cvName=cmds.circle(r=1,n=pnewname+'ctrl_'+mesh[u])
        cvNameoo=cvName[0]
        cvGrpExp=cmds.group(r=1,n=pnewname+"grp_exp_"+'ctrl_'+mesh[u])
        cvGrp=cmds.group(r=1,n=pnewname+"grp_"+'ctrl_'+mesh[u])
        
       
        cmds.parentConstraint(mesh[u],cvGrp,mo=0,weight=1)#注意mo=0
        cmds.select(cvGrp)
        cmds.pickWalk(d='down')
        cmds.pickWalk(d='right')
        cmds.delete()
        cmds.parentConstraint(cvNameoo,mesh[u],mo=1,weight=1)#注意mo=1
        cmds.scaleConstraint (cvNameoo,mesh[u],mo=1,weight=1)
       
        cmds.setAttr(cvNameoo+'Shape'+'.overrideEnabled',1)
        cmds.setAttr(cvNameoo+'Shape'+'.overrideColor',6)
        cmds.select(cvNameoo+'.cv[0:7]')
        cmds.rotate(0,90,0,r=1)
        cmds.select(cvGrp)
        cmds.parent(cvGrp,GRPsec01)
       
    #(6)createBigCtrls
    MCtrl=cmds.curve(d=1,p=[(-1,1,1),(-1,1,-1),(1,1,-1),(1,1,1),(-1,1,1),(-1,-1,1),(-1,-1,-1),(-1,1,-1),
    (-1,1,1),(-1,-1,1),(1,-1,1),(1,1,1),(1,1,-1),(1,-1,-1),(1,-1,1),(1,-1,-1),(-1,-1,-1)],k=[0,1,2,3,4,5,6,7,
    8,9,10,11,12,13,14,15,16])
    
    MCtrlShape=cmds.listRelatives(MCtrl,s=True)[0]
    cmds.setAttr(MCtrlShape+'.overrideEnabled',1)
    cmds.setAttr(MCtrlShape+'.overrideColor',17)
    
    MCtrlName=cmds.rename(MCtrl,pnewname+'M_ctrl')#newName
    cmds.setAttr(MCtrlName+'.sx',0.2)
    cmds.setAttr(MCtrlName+'.sy',0.8)
    cmds.setAttr(MCtrlName+'.sx',0.8)
    cmds.makeIdentity(MCtrlName,apply=True,t=1,r=1,s=1)
    #MEL.eval('Delete'History:')
    for HideAttr in ('.sx','.sy','.sz','.visibility'):
        cmds.setAttr(MCtrlName+HideAttr,keyable=False,channelBox=False,lock=True)
    MCtrlPri=cmds.group(n=pnewname+'main_ctrlPri')
    MCtrlCon=cmds.group(n=pnewname+'main_ctrlCon')
    MCtrlDrn=cmds.group(n=pnewname+'main_ctrlDrn')
    MCtrlEnv=cmds.group(n=pnewname+'main_ctrlEnv')
    cmds.select(cl=True)
    MCtrlSec=cmds.group(n=pnewname+'main_ctrlSec',empty=True)
    cmds.parent(MCtrlSec,MCtrlName)
    cmds.select(cl=True)
    #
    #
    for i in range(0,lenth):
        cmds.addAttr(MCtrlName,ln=('JntInf_'+str(i+1)),attributeType='float',defaultValue=1.0/(lenth-1)*i,keyable=True)
        
    cmds.parentConstraint(endJntsel,MCtrlEnv,mo=0)
    cmds.listConnections(MCtrlEnv,type='parentConstraint')
    lsParentsCons=cmds.listRelatives(MCtrlEnv,type='parentConstraint')
    cmds.select(lsParentsCons)
    cmds.delete()
    #--------------------connectTransfor--useExpression-----------
    exp=''
    k=0
    for k in range(0,length):
        exp+=pnewname+'grp_exp_'+'ctrl_'+mesh[k]+'.translateX='+MCtrlName+'.translateX*'+MCtrlName+'.JntInf_'+str(k+1)+';\n'
        exp+=pnewname+'grp_exp_'+'ctrl_'+mesh[k]+'.translateY='+MCtrlName+'.translateY*'+MCtrlName+'.JntInf_'+str(k+1)+';\n'
        exp+=pnewname+'grp_exp_'+'ctrl_'+mesh[k]+'.translateZ='+MCtrlName+'.translateZ*'+MCtrlName+'.JntInf_'+str(k+1)+';\n'
    cmds.expression(s=exp,n='pnewname'+'expCon')
    
    #(7)clear up outline----
    
    cmds.select(fsJntsel)
    grp02=cmds.group(n='GRP_'+fsJntsel[0])
    cmds.select(dupJnt)
    grp03=cmds.group(n='GRP_'+dupJnt[0])
    
    cmds.select(MCtrlEnv,grp02,grp03,GRPsec01)
    
    cmds.group(n='GRP_allCtrl'+fsJntsel[0]) 