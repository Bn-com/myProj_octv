#-*- coding: utf-8 -*-
import maya.cmds as rig
from RIG.face.baseClass import *
from RIG.face.controlers import CreateControler

def SK_AddJawSetup():

    if rig.objExists('head_jawLow_jnt'):
        obj = 'head_jawLow_jnt'
        unLock = unLockAttr(False,False,False)
        Lock = LockHideAttr(False,False,False,False)
        unLock.unLockObj(obj)
        print obj
        
#        创建控制器
        scaleVal = rig.getAttr('LfArm_Wrist_IK.scaleVal')
        controller = CreateControler(13,(4*scaleVal,4*scaleVal,4*scaleVal))
        con = controller.SK_b15('jaw_ctrl')
        conGrpA = rig.group(con,n = con+'_GRPA')
        conGrpB = rig.group(conGrpA,n = con+'_GRPB')
        rig.setAttr(conGrpB+'.ry',90)
        rig.makeIdentity(conGrpB,apply = True,s = True,r = True,t = True)
        
        mJaw = rig.getAttr(obj+'.worldMatrix')
        rig.xform(conGrpB,matrix = mJaw)
        
        rig.parent(conGrpB,'head_jnt')
        rig.orientConstraint(con,obj)
        Lock.hideAndLockObj(obj)
        Lock.hideAndLockObj(conGrpA)
        Lock.hideAndLockObj(conGrpB)
        Lock.hideInvertAttr(con,[u'rotateX', u'rotateY', u'rotateZ'])
        
def SK_removeJawSetup():
    if rig.objExists('jaw_ctrl_GRPB'):
        rig.delete('jaw_ctrl_GRPB')