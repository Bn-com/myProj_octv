#-*- coding: utf-8 -*-
import maya.cmds as rig
from RIG.nurbsCurveCon import *
from RIG.commonly.base import *

def SK_createShoulder(jntObj):
    objJnt = jntObj
    endJoint = rig.listRelatives(objJnt,c = True)[0]
    LR = jntObj.split('_')[0]
    prefix = LR+'Shoulder'
    ikCon = LR+'Arm_Wrist_IK'    
    AllGrp = LR+'Arm_ALL_CTRL_GRP'
    scaleVal = rig.getAttr(ikCon+'.scaleVal')
    axisX = rig.getAttr(objJnt+'.tx')
    
#   create Controllers
    shoulderCon = rig.rename(SK_b32(6),LR+'_shoulder')
#    rig.move(0,12.659587,0,shoulderCon+'.scalePivot',shoulderCon+'.rotatePivot')
#    rig.move(0,0,0,shoulderCon,rpr = True)
    rig.setAttr(shoulderCon+'.scale',0.135*scaleVal,0.135*scaleVal,0.135*scaleVal)
#    rig.setAttr(shoulderCon+'.rx',-90)
#    rig.setAttr(shoulderCon+'.rz',90)
    SK_freezeObj(shoulderCon)
    if(0 > axisX):
        rig.setAttr(shoulderCon+'.sy',-1)
#       将位移统一
        rig.setAttr(shoulderCon+'.sx',-1)
        rig.setAttr(shoulderCon+'.sz',-1)
#        SK_freezeObj(shoulderCon)
    
    shoulderConGrp = rig.group(shoulderCon,n = shoulderCon+'_GRP')
    SK_snapToObj(objJnt,shoulderConGrp)

#   create Ik system
    shoulderIK = rig.ikHandle(sj = objJnt,ee = endJoint,n = prefix+'_IKHandle')[0]
    rig.parent(shoulderIK,shoulderCon)
    rig.parent(AllGrp,endJoint)
    rig.pointConstraint(shoulderCon,objJnt)
    SK_hideLockAll(shoulderCon,0,0)

#   hide IKHandle
    rig.setAttr(shoulderIK+'.visibility',0)

