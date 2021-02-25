import maya.cmds as cmds
def edo_addCarRigRotateXex():
    exjnts=cmds.ls('*_JNT_EX')
    for jnt in exjnts:
        ##jnt=exjnts[0]
        print jnt
        cmds.addAttr(jnt,ln='rotateXex',at='double')
        cmds.setAttr(jnt+'.rotateXex',cb=1,k=0)
        ex=cmds.expression('car_motion',q=1,string=1)
        newex=ex.replace(jnt+'.rotateX',jnt+'.rotateXex')
        cmds.expression('car_motion',e=1,string=newex)
        cmds.connectAttr(jnt+'.rotateXex',jnt+'.rotateX',f=1)

def edo_addWheelRock():
    sels=cmds.ls(sl=1)
    for i in sels:
        cmds.addAttr(i,ln='wheelRock',at='double',min=-5,max=5)
        cmds.setAttr(i+'.wheelRock',keyable=True)
        fix=i.replace('wheel_C','')
        jnt=fix+'JNT'
        cmds.connectAttr(i+'.wheelRock',jnt+'.ry',f=1)
        
def edo_addWheelShake():
   sels=cmds.ls(sl=1)
   for i in sels:
       #i=sels[0]
       cmds.group(i,n='GRP_'+i)
       cmds.addAttr(i,ln='wheelShakeSpeed',at='double')
       cmds.setAttr(i+'.wheelShakeSpeed',keyable=True)
       cmds.addAttr(i,ln='wheelShakeScale',at='double')
       cmds.setAttr(i+'.wheelShakeScale',keyable=True)
       ex='GRP_'+i+".rotateZ=noise(frame*"+i+".wheelShakeSpeed)*"+i+".wheelShakeScale;"
       cmds.expression(n=i+'_shake_ex',s=ex,o='',ae=1,uc='all')

def edo_addCarRigGlobalScaleCtrl():
    ctrl=cmds.circle(n='globalScaleCtrl',nr=(0,1,0))[0]
    cmds.parent(ctrl,'MIS')
    cmds.parent('Car_Con_Left_UP',ctrl)
    cmds.setAttr(ctrl+'Shape.overrideEnabled',1)
    cmds.setAttr(ctrl+'Shape.overrideColor',6)


def edo_addAimWheelRig():
    sels=cmds.ls(sl=1)
    center=sels[0]
    aim=sels[1]
    cpox=cmds.getAttr(center+'.tx')
    cpoy=cmds.getAttr(center+'.ty')
    cpoz=cmds.getAttr(center+'.tz')
    apox=cmds.getAttr(aim+'.tx')
    apoy=cmds.getAttr(aim+'.ty')
    apoz=cmds.getAttr(aim+'.tz')
    cmds.select(cl=1)
    cmds.joint(p=[cpox,cpoy,cpoz],n='centerWheelJoint')
    cmds.joint(p=[apox,apoy,apoz],n='aimWheelJoint')
    cmds.joint('centerWheelJoint',e=1,zso=1,oj='xyz',sao='yup')
    cmds.delete(sels)
    cmds.circle(n='centerWheelCtrl',nr=[1,0,0])
    cmds.group(n='GRP_centerWheelCtrl')
    cmds.parent('GRP_centerWheelCtrl','centerWheelJoint')
    cmds.setAttr('GRP_centerWheelCtrl.tx',0)
    cmds.setAttr('GRP_centerWheelCtrl.ty',0)
    cmds.setAttr('GRP_centerWheelCtrl.tz',0)
    cmds.setAttr('GRP_centerWheelCtrl.rx',0)
    cmds.setAttr('GRP_centerWheelCtrl.ry',0)
    cmds.setAttr('GRP_centerWheelCtrl.rz',0)
    cmds.parent('GRP_centerWheelCtrl','Chassis_Con')
    cmds.parent('centerWheelJoint','centerWheelCtrl')
    cmds.addAttr('centerWheelCtrl',ln='rotateScale',at='double')
    cmds.setAttr('centerWheelCtrl.rotateScale',keyable=True)
    cmds.setAttr('centerWheelCtrl.rotateScale',-0.4)
    cmds.setAttr('centerWheelCtrl.ry',lock=1,keyable=0,channelBox=0)
    cmds.setAttr('centerWheelCtrl.rz',lock=1,keyable=0,channelBox=0)
    cmds.connectAttr('centerWheelCtrl.rotateScale','Front_Rotate_MD.input2X',f=1)
    cmds.connectAttr('centerWheelCtrl.rx','MIS.FnRo',f=1)

def edo_addLfWheel():
    sels=cmds.ls(sl=1)
    addlocators(['Lf_Mid'])
    cmds.select(sels[0],r=1)        
    SK_addWheel(['Lf_Mid'])
    cmds.addAttr('Lf_Mid_wheel_C',ln='snapeFloor',at='bool')
    cmds.setAttr('Lf_Mid_wheel_C.snapeFloor',keyable=True)
    cmds.setAttr('Lf_Mid_wheel_C.snapeFloor',1)
    cmds.connectAttr('Lf_Mid_wheel_C.snapeFloor','Lf_Mid_JNT.Lock',f=1)
    
def edo_addRtWheel():
    sels=cmds.ls(sl=1)
    addlocators(['Rt_Mid'])
    cmds.select(sels[0],r=1)        
    SK_addWheel(['Rt_Mid'])
    cmds.addAttr('Rt_Mid_wheel_C',ln='snapeFloor',at='bool')
    cmds.setAttr('Rt_Mid_wheel_C.snapeFloor',keyable=True)
    cmds.setAttr('Rt_Mid_wheel_C.snapeFloor',1)
    cmds.connectAttr('Rt_Mid_wheel_C.snapeFloor','Rt_Mid_JNT.Lock',f=1)