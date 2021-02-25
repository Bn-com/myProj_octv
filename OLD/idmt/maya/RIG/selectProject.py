#-*- coding: utf-8 -*-

import maya.cmds as rig
import maya.cmds as cmds
import maya.OpenMaya as om
from RIG.face.baseClass import *
from RIG.face.controlers import CreateControler
from RIG.commonly.resetControllerDefaultPose import SK_creatConDefaultPos

def SK_SelectProject(OrigenRB,WoodliesRB,WinxTVRB,MotionBuilder):
    if rig.radioButton(OrigenRB,q = True,sl = True):
        SK_Default_config()
    elif rig.radioButton(WoodliesRB,q = True,sl = True):
        SK_Woodlies_config()
    elif rig.radioButton(WinxTVRB,q = True,sl = True):
        SK_WinxTV_config()
    elif rig.radioButton(MotionBuilder,q = True,sl = True):
        SK_MotionBuilder_config()
    #modify_vetion_bug
    #edo_modifyMayaVersionBug()

def edo_modifyMayaVersionBug():
    mg=om.MGlobal()
    version=mg.mayaVersion()
    version=version[0:4]
    if version=='2011':
        print 'modify 2011 shoulder control x axis bug'
        rp=cmds.ls(type='ikRPsolver')
        cmds.connectAttr(rp[0]+'.message','RtShoulder_IKHandle.ikSolver',f=1)
        cmds.connectAttr(rp[0]+'.message','LfShoulder_IKHandle.ikSolver',f=1)
    if version=='2012':
        print 'modify 2012 shoulder control x axis bug'
        rp=cmds.ls(type='ikRPsolver')
        cmds.connectAttr(rp[0]+'.message','RtShoulder_IKHandle.ikSolver',f=1)
        cmds.connectAttr(rp[0]+'.message','LfShoulder_IKHandle.ikSolver',f=1)
            
#===============================================================================
# 增加脚趾驱动关键帧    
#===============================================================================
def SK_AddToesetDrivenKeyframe():
    unLock = unLockAttr(False,False,False)
    Lock = LockHideAttr(False,False,False)

    footJnts = rig.ls('*_foot_drv')
    handJnts = rig.ls('*_hand_drv')
    footJnts.extend(handJnts)#增加手指驱动
    for jnt in footJnts:
        allCons = rig.listConnections(jnt+'.ctrl',s = False,d = True)#得到所有脚趾控制器
        mainCtrls = []
        if allCons:#脚趾是否有控制器
            for con in allCons:#找到脚趾的第一个控制器
                if(con[-1] == '1'):
                    mainCtrls.append(con)
        
        if mainCtrls:#是否存在脚趾控制器
            for mainCon in mainCtrls:#迭代脚趾的第一个控制器
                conPre = mainCon.replace(mainCon[-1],'')#得到脚趾的前缀，注意：不能超过10根脚趾
                relativeCons = [con for con in allCons if conPre in con]#得到脚趾的个数
                if relativeCons:
                    rig.addAttr(mainCon,at = 'float',ln = 'curl',min = -10,max = 10,dv = 0,k = True)#增加脚趾弯曲属性
                    
                    for con in relativeCons:
                        con_low = rig.listRelatives(con,p = True)[0]#得到此控制器上的组
                        unLock.unLockObj(con_low)#解开属性
                        rig.setDrivenKeyframe(con_low+'.rotateZ',currentDriver = mainCon+'.curl',dv = 0,v = 0)#增加驱动关键帧
                        rig.setDrivenKeyframe(con_low+'.rotateZ',currentDriver = mainCon+'.curl',dv = 10,v = -90)#增加驱动关键帧
                        rig.setDrivenKeyframe(con_low+'.rotateZ',currentDriver = mainCon+'.curl',dv = -10,v = 90)#增加驱动关键帧
                        Lock.hideAndLockObj(con_low)#锁定属性           
 
 
 
 
def SK_IKHandPivot():
    Lock = LockHideAttr(True,True,False,False)
    newcons = CreateControler()
    handIK = rig.ls('*Arm_Wrist_IK')
    
    if handIK:
        for ikcon in handIK:
            #增加旋转属性
            rig.addAttr(ikcon,at = 'float',ln = 'pivotIKRX',k = True)
            rig.addAttr(ikcon,at = 'float',ln = 'pivotIKRY',k = True)
            rig.addAttr(ikcon,at = 'float',ln = 'pivotIKRZ',k = True)
            
            
            val = rig.getAttr(ikcon+'.scaleVal')#获得缩放值
            newcons.setObjScale((val,val,val))
            con = newcons.SK_b01(ikcon+'_Pivot')
            jointFinger = ikcon[0:2]+'_mid2_jnt'#手指骨骼
            pos = rig.xform(jointFinger,q = True,t = True,ws = True)#旋转轴心点位置
            rig.xform(con,t = pos,ws = True)
            
            ikConChild = rig.listRelatives(ikcon,c = True,type = 'transform')#获得IK控制器下的物体
            
            rig.parent(con,ikcon)
            rig.makeIdentity(con,apply = True,t = True,s = True,r = True)
            rig.parent(ikConChild,con)  
            
            Switch = ikcon[0:2]+'Arm_Switch'
            rig.addAttr(Switch,at = 'enum',ln = 'pivotIK',en = 'OFF:ON:',k = False)
            rig.connectAttr(Switch+'.pivotIK',con+'.visibility')
            Lock.hideAndLockObj(con) 
            
            #连接旋转属性
            rig.connectAttr(ikcon+'.pivotIKRX',con+'.rx')
            rig.connectAttr(ikcon+'.pivotIKRY',con+'.ry')
            rig.connectAttr(ikcon+'.pivotIKRZ',con+'.rz')
            
            

def edo_freeAllCtrlAxis():
    print 'edo_freeAllCtrlAxis'
    cmds.setAttr('LfArm_Elbow_FK.rx',k=1,l=0)
    cmds.setAttr('LfArm_Elbow_FK.rz',k=1,l=0)
    cmds.setAttr('LfLeg_Knee_FK.rx',k=1,l=0)
    cmds.setAttr('LfLeg_Knee_FK.rz',k=1,l=0)
    cmds.setAttr('RtArm_Elbow_FK.rx',k=1,l=0)
    cmds.setAttr('RtArm_Elbow_FK.rz',k=1,l=0)
    cmds.setAttr('RtLeg_Knee_FK.rx',k=1,l=0)
    cmds.setAttr('RtLeg_Knee_FK.rz',k=1,l=0)
    cmds.setAttr('Lf_Leg5_jnt.rx',l=0)
    cmds.setAttr('Lf_Leg5_jnt.ry',l=0)
    cmds.setAttr('Lf_Leg5_jnt.rz',l=0)
    cmds.setAttr('Rt_Leg5_jnt.rx',l=0)
    cmds.setAttr('Rt_Leg5_jnt.ry',l=0)
    cmds.setAttr('Rt_Leg5_jnt.rz',l=0)
    cmds.setAttr('Lf_Arm5_jnt.rx',l=0)
    cmds.setAttr('Lf_Arm5_jnt.ry',l=0)
    cmds.setAttr('Lf_Arm5_jnt.rz',l=0)
    cmds.setAttr('Rt_Arm5_jnt.rx',l=0)
    cmds.setAttr('Rt_Arm5_jnt.ry',l=0)
    cmds.setAttr('Rt_Arm5_jnt.rz',l=0)
    cmds.setAttr('Lf_wristMid_toe_con_Grp.rx',l=0,k=1)
    cmds.setAttr('Lf_wristMid_toe_con_Grp.ry',l=0,k=1)
    cmds.setAttr('Lf_wristMid_toe_con_Grp.rz',l=0,k=1)
    cmds.setAttr('Rt_wristMid_toe_con_Grp.rx',l=0,k=1)
    cmds.setAttr('Rt_wristMid_toe_con_Grp.ry',l=0,k=1)
    cmds.setAttr('Rt_wristMid_toe_con_Grp.rz',l=0,k=1)
    cmds.setAttr('Lf_ball_toe_con_Grp.rx',l=0,k=1)
    cmds.setAttr('Lf_ball_toe_con_Grp.ry',l=0,k=1)
    cmds.setAttr('Lf_ball_toe_con_Grp.rz',l=0,k=1)
    cmds.setAttr('Rt_ball_toe_con_Grp.rx',l=0,k=1)
    cmds.setAttr('Rt_ball_toe_con_Grp.ry',l=0,k=1)
    cmds.setAttr('Rt_ball_toe_con_Grp.rz',l=0,k=1) 
    cmds.addAttr('LfArm_Wrist_IK',ln='twistToe',at='double')
    cmds.setAttr('LfArm_Wrist_IK.raiseToe',l=0,k=1)
    cmds.setAttr('LfArm_Wrist_IK.swivelToe',l=0,k=1)
    cmds.setAttr('LfArm_Wrist_IK.twistToe',l=0,k=1)
    cmds.setAttr('LfArm_wristMid_FKShape.v',1)
    cmds.setAttr('LfArm_wristMid_FK.rx',l=0,k=1)
    cmds.setAttr('RtArm_wristMid_FKShape.v',1)
    cmds.setAttr('RtArm_wristMid_FK.rx',l=0,k=1)
    cmds.setAttr('LfLegLeg_ball_FK.rx',l=0,k=1)
    cmds.setAttr('RtLegLeg_ball_FK.rx',l=0,k=1)
    cmds.addAttr('RtArm_Wrist_IK',ln='twistToe',at='double')
    cmds.setAttr('RtArm_Wrist_IK.raiseToe',l=0,k=1)
    cmds.setAttr('RtArm_Wrist_IK.swivelToe',l=0,k=1)
    cmds.setAttr('RtArm_Wrist_IK.twistToe',l=0,k=1)
    cmds.addAttr('LfLeg_Leg_IK',ln='twistToe',at='double')
    cmds.setAttr('LfLeg_Leg_IK.raiseToe',l=0,k=1)
    cmds.setAttr('LfLeg_Leg_IK.swivelToe',l=0,k=1)
    cmds.setAttr('LfLeg_Leg_IK.twistToe',l=0,k=1)
    cmds.addAttr('RtLeg_Leg_IK',ln='twistToe',at='double')
    cmds.setAttr('RtLeg_Leg_IK.raiseToe',l=0,k=1)
    cmds.setAttr('RtLeg_Leg_IK.swivelToe',l=0,k=1)
    cmds.setAttr('RtLeg_Leg_IK.twistToe',l=0,k=1)
    #connect_drv_jnt
    #LeftArm
    cmds.setAttr('Lf_elbow_drv_jnt.rx',l=0)
    cmds.setAttr('Lf_elbow_drv_jnt.ry',l=0)
    cmds.setAttr('Lf_elbow_drv_jnt.rz',l=0)
    cmds.connectAttr('LfArm_PB1.outRotateX','Lf_elbow_drv_jnt.rotateX',f=1)
    cmds.connectAttr('LfArm_PB1.outRotateY','Lf_elbow_drv_jnt.rotateY',f=1)
    cmds.connectAttr('LfArm_PB1.outRotateZ','Lf_elbow_drv_jnt.rotateZ',f=1)
    cmds.setAttr('Lf_elbow_drv_jnt.rx',l=1)
    cmds.setAttr('Lf_elbow_drv_jnt.ry',l=1)
    cmds.setAttr('Lf_elbow_drv_jnt.rz',l=1)
    #RightArm
    cmds.setAttr('Rt_elbow_drv_jnt.rx',l=0)
    cmds.setAttr('Rt_elbow_drv_jnt.ry',l=0)
    cmds.setAttr('Rt_elbow_drv_jnt.rz',l=0)
    cmds.connectAttr('RtArm_PB1.outRotateX','Rt_elbow_drv_jnt.rotateX',f=1)
    cmds.connectAttr('RtArm_PB1.outRotateY','Rt_elbow_drv_jnt.rotateY',f=1)
    cmds.connectAttr('RtArm_PB1.outRotateZ','Rt_elbow_drv_jnt.rotateZ',f=1)
    cmds.setAttr('Rt_elbow_drv_jnt.rx',l=1)
    cmds.setAttr('Rt_elbow_drv_jnt.ry',l=1)
    cmds.setAttr('Rt_elbow_drv_jnt.rz',l=1)
    #LeftLeg
    cmds.setAttr('Lf_knee_drv_jnt.rx',l=0)
    cmds.setAttr('Lf_knee_drv_jnt.ry',l=0)
    cmds.setAttr('Lf_knee_drv_jnt.rz',l=0)
    cmds.connectAttr('LfLeg_PB1.outRotateX','Lf_knee_drv_jnt.rotateX',f=1)
    cmds.connectAttr('LfLeg_PB1.outRotateY','Lf_knee_drv_jnt.rotateY',f=1)
    cmds.connectAttr('LfLeg_PB1.outRotateZ','Lf_knee_drv_jnt.rotateZ',f=1)
    cmds.setAttr('Lf_knee_drv_jnt.rx',l=1)
    cmds.setAttr('Lf_knee_drv_jnt.ry',l=1)
    cmds.setAttr('Lf_knee_drv_jnt.rz',l=1)
    #RightLeg
    cmds.setAttr('Rt_knee_drv_jnt.rx',l=0)
    cmds.setAttr('Rt_knee_drv_jnt.ry',l=0)
    cmds.setAttr('Rt_knee_drv_jnt.rz',l=0)
    cmds.connectAttr('RtLeg_PB1.outRotateX','Rt_knee_drv_jnt.rotateX',f=1)
    cmds.connectAttr('RtLeg_PB1.outRotateY','Rt_knee_drv_jnt.rotateY',f=1)
    cmds.connectAttr('RtLeg_PB1.outRotateZ','Rt_knee_drv_jnt.rotateZ',f=1)
    cmds.setAttr('Rt_knee_drv_jnt.rx',l=1)
    cmds.setAttr('Rt_knee_drv_jnt.ry',l=1)
    cmds.setAttr('Rt_knee_drv_jnt.rz',l=1)
    
def edo_connectionHalfJoint():
    print 'edo_connectionHalfJoint'
    #LfArm
    cmds.connectAttr('Lf_elbow_drv_jnt.rx','LfArm_MD11.input1X',f=1)
    cmds.connectAttr('Lf_elbow_drv_jnt.ry','LfArm_MD11.input1Y',f=1)
    cmds.connectAttr('Lf_elbow_drv_jnt.rz','LfArm_MD11.input1Z',f=1)
    cmds.setAttr('LfArm_MD11.input2X',0.5)
    cmds.setAttr('LfArm_MD11.input2Y',0.5)
    cmds.setAttr('LfArm_MD11.input2Z',0.5)
    cmds.connectAttr('LfArm_MD11.outputX','Lf_Arm5_jnt.rx',f=1)
    cmds.connectAttr('LfArm_MD11.outputY','Lf_Arm5_jnt.ry',f=1)
    cmds.connectAttr('LfArm_MD11.outputZ','Lf_Arm5_jnt.rz',f=1)
    cmds.connectAttr('LfArm_Wrist_IK.twistToe','Lf_wristMid_toe_con_Grp.rx',f=1)
    #LfLeg
    cmds.connectAttr('Lf_knee_drv_jnt.rx','LfLeg_MD11.input1X',f=1)
    cmds.connectAttr('Lf_knee_drv_jnt.ry','LfLeg_MD11.input1Y',f=1)
    cmds.connectAttr('Lf_knee_drv_jnt.rz','LfLeg_MD11.input1Z',f=1)
    cmds.setAttr('LfLeg_MD11.input2X',0.5)
    cmds.setAttr('LfLeg_MD11.input2Y',0.5)
    cmds.setAttr('LfLeg_MD11.input2Z',0.5)
    cmds.connectAttr('LfLeg_MD11.outputX','Lf_Leg5_jnt.rx',f=1)
    cmds.connectAttr('LfLeg_MD11.outputY','Lf_Leg5_jnt.ry',f=1)
    cmds.connectAttr('LfLeg_MD11.outputZ','Lf_Leg5_jnt.rz',f=1)
    cmds.connectAttr('LfLeg_Leg_IK.twistToe','Lf_ball_toe_con_Grp.rx',f=1)
    #RtArm
    cmds.connectAttr('Rt_elbow_drv_jnt.rx','RtArm_MD18.input1X',f=1)
    cmds.connectAttr('Rt_elbow_drv_jnt.ry','RtArm_MD18.input1Y',f=1)
    cmds.connectAttr('Rt_elbow_drv_jnt.rz','RtArm_MD18.input1Z',f=1)
    cmds.setAttr('RtArm_MD18.input2X',0.5)
    cmds.setAttr('RtArm_MD18.input2Y',0.5)
    cmds.setAttr('RtArm_MD18.input2Z',0.5)
    cmds.connectAttr('RtArm_MD18.outputX','Rt_Arm5_jnt.rx',f=1)
    cmds.connectAttr('RtArm_MD18.outputY','Rt_Arm5_jnt.ry',f=1)
    cmds.connectAttr('RtArm_MD18.outputZ','Rt_Arm5_jnt.rz',f=1)
    cmds.connectAttr('RtArm_Wrist_IK.twistToe','Rt_wristMid_toe_con_Grp.rx',f=1)
    #RtLeg
    cmds.connectAttr('Rt_knee_drv_jnt.rx','RtLeg_MD18.input1X',f=1)
    cmds.connectAttr('Rt_knee_drv_jnt.ry','RtLeg_MD18.input1Y',f=1)
    cmds.connectAttr('Rt_knee_drv_jnt.rz','RtLeg_MD18.input1Z',f=1)
    cmds.setAttr('RtLeg_MD18.input2X',0.5)
    cmds.setAttr('RtLeg_MD18.input2Y',0.5)
    cmds.setAttr('RtLeg_MD18.input2Z',0.5)
    cmds.connectAttr('RtLeg_MD18.outputX','Rt_Leg5_jnt.rx',f=1)
    cmds.connectAttr('RtLeg_MD18.outputY','Rt_Leg5_jnt.ry',f=1)
    cmds.connectAttr('RtLeg_MD18.outputZ','Rt_Leg5_jnt.rz',f=1)
    cmds.connectAttr('RtLeg_Leg_IK.twistToe','Rt_ball_toe_con_Grp.rx',f=1)
    

def edo_createLocation():
    print 'edo_createLocation'
    #LfArm
    cmds.duplicate('LfArm_UpArm_FK',n='LfArm_UpArm_FK_location',po=1)
    cmds.sets('LfArm_UpArm_FK_location',rm='bodySet')
    cmds.parentConstraint('Lf_upArm_drv_jnt','LfArm_UpArm_FK_location',st=['x','y','z'],mo=1)
    cmds.duplicate('LfArm_Elbow_FK',n='LfArm_Elbow_FK_location',po=1)
    cmds.sets('LfArm_Elbow_FK_location',rm='bodySet')
    cmds.parentConstraint('Lf_elbow_drv_jnt','LfArm_Elbow_FK_location',st=['x','y','z'],mo=1)
    cmds.duplicate('LfArm_Wrist_FK',n='LfArm_Wrist_FK_location',po=1)
    cmds.sets('LfArm_Wrist_FK_location',rm='bodySet')
    cmds.parentConstraint('Lf_Arm9_jnt','LfArm_Wrist_FK_location',st=['x','y','z'],mo=1) 
    cmds.duplicate('LfArm_wristMid_FK',n='LfArm_wristMid_FK_location',po=1)
    cmds.sets('LfArm_wristMid_FK_location',rm='bodySet')
    cmds.parentConstraint('Lf_hand_drv','LfArm_wristMid_FK_location',st=['x','y','z'],mo=1)
    cmds.duplicate('LfArm_Pole_ctrl',n='LfArm_Pole_ctrl_location',po=1)
    cmds.sets('LfArm_Pole_ctrl_location',rm='bodySet')
    cmds.parentConstraint('Lf_Arm5_jnt','LfArm_Pole_ctrl_location',sr=['x','y','z'],mo=0)
    cmds.duplicate('LfArm_Wrist_IK',n='LfArm_Wrist_IK_location',po=1)
    cmds.sets('LfArm_Wrist_IK_location',rm='bodySet')
    cmds.parentConstraint('Lf_Arm9_jnt','LfArm_Wrist_IK_location',mo=1)
    #RtArm
    cmds.duplicate('RtArm_UpArm_FK',n='RtArm_UpArm_FK_location',po=1)
    cmds.sets('RtArm_UpArm_FK_location',rm='bodySet')
    cmds.parentConstraint('Rt_upArm_drv_jnt','RtArm_UpArm_FK_location',st=['x','y','z'],mo=1)
    cmds.duplicate('RtArm_Elbow_FK',n='RtArm_Elbow_FK_location',po=1)
    cmds.sets('RtArm_Elbow_FK_location',rm='bodySet')
    cmds.parentConstraint('Rt_elbow_drv_jnt','RtArm_Elbow_FK_location',st=['x','y','z'],mo=1)
    cmds.duplicate('RtArm_Wrist_FK',n='RtArm_Wrist_FK_location',po=1)
    cmds.sets('RtArm_Wrist_FK_location',rm='bodySet')
    cmds.parentConstraint('Rt_Arm9_jnt','RtArm_Wrist_FK_location',st=['x','y','z'],mo=1) 
    cmds.duplicate('RtArm_wristMid_FK',n='RtArm_wristMid_FK_location',po=1)
    cmds.sets('RtArm_wristMid_FK_location',rm='bodySet')
    cmds.parentConstraint('Rt_hand_drv','RtArm_wristMid_FK_location',st=['x','y','z'],mo=1)
    cmds.duplicate('RtArm_Pole_ctrl',n='RtArm_Pole_ctrl_location',po=1)
    cmds.sets('RtArm_Pole_ctrl_location',rm='bodySet')
    cmds.parentConstraint('Rt_Arm5_jnt','RtArm_Pole_ctrl_location',sr=['x','y','z'],mo=0)
    cmds.duplicate('RtArm_Wrist_IK',n='RtArm_Wrist_IK_location',po=1)
    cmds.sets('RtArm_Wrist_IK_location',rm='bodySet')
    cmds.parentConstraint('Rt_Arm9_jnt','RtArm_Wrist_IK_location',mo=1)
    #LfLeg
    cmds.duplicate('LfLeg_Leg_FK',n='LfLeg_Leg_FK_location',po=1)
    cmds.sets('LfLeg_Leg_FK_location',rm='bodySet')
    cmds.parentConstraint('Lf_leg_drv_jnt','LfLeg_Leg_FK_location',st=['x','y','z'],mo=1)
    cmds.duplicate('LfLeg_Knee_FK',n='LfLeg_Knee_FK_location',po=1)
    cmds.sets('LfLeg_Knee_FK_location',rm='bodySet')
    cmds.parentConstraint('Lf_knee_drv_jnt','LfLeg_Knee_FK_location',st=['x','y','z'],mo=1)
    cmds.duplicate('LfLeg_Ankle_FK',n='LfLeg_Ankle_FK_location',po=1)
    cmds.sets('LfLeg_Ankle_FK_location',rm='bodySet')
    cmds.parentConstraint('Lf_Leg9_jnt','LfLeg_Ankle_FK_location',st=['x','y','z'],mo=1) 
    cmds.duplicate('LfLegLeg_ball_FK',n='LfLegLeg_ball_FK_location',po=1)
    cmds.sets('LfLegLeg_ball_FK_location',rm='bodySet')
    cmds.parentConstraint('Lf_foot_drv','LfLegLeg_ball_FK_location',st=['x','y','z'],mo=1)
    cmds.duplicate('LfLeg_Pole_ctrl',n='LfLeg_Pole_ctrl_location',po=1)
    cmds.sets('LfLeg_Pole_ctrl_location',rm='bodySet')
    cmds.parentConstraint('Lf_Leg5_jnt','LfLeg_Pole_ctrl_location',sr=['x','y','z'],mo=0)
    cmds.duplicate('LfLeg_Leg_IK',n='LfLeg_Leg_IK_location',po=1)
    cmds.sets('LfLeg_Leg_IK_location',rm='bodySet')
    cmds.parentConstraint('Lf_heel_drv','LfLeg_Leg_IK_location',mo=1)
    #RtLeg
    cmds.duplicate('RtLeg_Leg_FK',n='RtLeg_Leg_FK_location',po=1)
    cmds.sets('RtLeg_Leg_FK_location',rm='bodySet')
    cmds.parentConstraint('Rt_leg_drv_jnt','RtLeg_Leg_FK_location',st=['x','y','z'],mo=1)
    cmds.duplicate('RtLeg_Knee_FK',n='RtLeg_Knee_FK_location',po=1)
    cmds.sets('RtLeg_Knee_FK_location',rm='bodySet')
    cmds.parentConstraint('Rt_knee_drv_jnt','RtLeg_Knee_FK_location',st=['x','y','z'],mo=1)
    cmds.duplicate('RtLeg_Ankle_FK',n='RtLeg_Ankle_FK_location',po=1)
    cmds.sets('RtLeg_Ankle_FK_location',rm='bodySet')
    cmds.parentConstraint('Rt_Leg9_jnt','RtLeg_Ankle_FK_location',st=['x','y','z'],mo=1) 
    cmds.duplicate('RtLegLeg_ball_FK',n='RtLegLeg_ball_FK_location',po=1)
    cmds.sets('RtLegLeg_ball_FK_location',rm='bodySet')
    cmds.parentConstraint('Rt_foot_drv','RtLegLeg_ball_FK_location',st=['x','y','z'],mo=1)
    cmds.duplicate('RtLeg_Pole_ctrl',n='RtLeg_Pole_ctrl_location',po=1)
    cmds.sets('RtLeg_Pole_ctrl_location',rm='bodySet')
    cmds.parentConstraint('Rt_Leg5_jnt','RtLeg_Pole_ctrl_location',sr=['x','y','z'],mo=0)
    cmds.duplicate('RtLeg_Leg_IK',n='RtLeg_Leg_IK_location',po=1)
    cmds.sets('RtLeg_Leg_IK_location',rm='bodySet')
    cmds.parentConstraint('Rt_heel_drv','RtLeg_Leg_IK_location',mo=1)
        
#===============================================================================
# 选择配置
#===============================================================================
#缺省配置
def SK_Default_config():
    print 'Default'

#Woodlies项目配置    
def SK_Woodlies_config():
    print 'woodlies'
    SK_AddToesetDrivenKeyframe()
    SK_IKHandPivot()
    SK_creatConDefaultPos()#创建恢复初始pose
    
#WinxTV项目配置  
def SK_WinxTV_config():
    print 'WinTV'
      
def SK_MotionBuilder_config():
    print 'MotionBuilder..'
    edo_freeAllCtrlAxis()
    edo_connectionHalfJoint()
    edo_createLocation()
    cmds.select(cl=1)
