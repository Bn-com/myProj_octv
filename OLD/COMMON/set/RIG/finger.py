#-*- coding: utf-8 -*-
import maya.cmds as rig
from RIG.commonly.base import *
from RIG.nurbsCurveCon import *


def SK_createFinger(jntObj):
    LR = jntObj.split('_')[0]
    selJnt = jntObj
#   add ctrol Attr
    rig.addAttr(selJnt,ln = 'ctrl',at = 'float',)    
    prefix = LR
    rootFingers = ''
    conFingers = ''
    parentControl = selJnt
    
    ikCon = prefix+'Leg_Leg_IK'
    if('_hand_' in selJnt):
        ikCon = prefix+'Arm_Wrist_IK'
        jntObj = rig.listRelatives(jntObj,p = True)[0]
        temJoints = [jnt for jnt in rig.listRelatives(rig.listRelatives(selJnt,p = True)[0],c = True) if rig.listRelatives(jnt,c = True,type = 'joint')]
        rootFingers = [jnt for jnt in temJoints if ('Root_' in jnt)]
        thumbFinger = [jnt for jnt in temJoints if ('_thumb' in jnt)]
        conFingers = [rig.listRelatives(jnt,c = True)[0] for jnt in rootFingers]
        if thumbFinger:
            conFingers.append(thumbFinger[0])    
    
    else:
        temJoints = [jnt for jnt in rig.listRelatives(selJnt,c = True) if rig.listRelatives(jnt,c = True,type = 'joint')]
        rootFingers = [jnt for jnt in temJoints if ('Root_' in jnt)]
        thumbFinger = [jnt for jnt in temJoints if ('_thumb' in jnt)]
        conFingers = [rig.listRelatives(jnt,c = True)[0] for jnt in rootFingers]
        if thumbFinger:
            conFingers.append(thumbFinger[0]) 
            
#    X axis
    scaleVal = rig.getAttr(ikCon+'.scaleVal') 
    pointAxisX = rig.getAttr(selJnt+'.tx')
    
        
#    finger setup
    for finger in conFingers:
        rootFinger = finger
        parentControl = selJnt
        
        curveName = SK_b33(6)
        curveName = rig.rename(curveName,rootFinger.replace('_jnt',''))
        rig.setAttr(curveName+'.rx',-180)
        rig.setAttr(curveName+'.scale',0.2*scaleVal,0.2*scaleVal,0.2*scaleVal)            
        SK_freezeObj(curveName)
        if pointAxisX > 0:
            rig.setAttr(curveName+'.sy',-1)
            SK_freezeObj(curveName)
        
#        隐藏并锁Scale和visibility属性
        SK_hideLockAll(curveName,0,0)
        
        curveNameGrpLow = rig.group(curveName,n = curveName+'_Low')
        rig.xform(curveNameGrpLow,os = True ,piv = (0,0,0))  
        curveNameGrpUp = rig.group(curveNameGrpLow,n = curveName+'_Up') 
        rig.xform(curveNameGrpUp,os = True ,piv = (0,0,0)) 
        
        if(('_hand_' in selJnt) and ('_thumb' in curveName)):
            rig.parent(curveNameGrpUp,rig.listRelatives(parentControl,p = True)[0])
        else:
            rig.parent(curveNameGrpUp,parentControl)

        parentControl =  curveName      
        SK_snapToObj(finger,curveNameGrpUp)        
        rig.connectAttr(selJnt+'.ctrl',curveName+'.ctrl')         
        rig.parentConstraint(curveName,finger,mo = True)        
        

        
        segFingers = rig.listRelatives(finger,c = True,ad = True,type = 'joint')[::-1]
        if segFingers:
            segFingersSize = len(segFingers)
            for i,subFinger in enumerate(segFingers):                    
                if not (i== segFingersSize-1):
                    curveName = SK_b33(6)
                    curveName = rig.rename(curveName,subFinger.replace('_jnt',''))
                    rig.setAttr(curveName+'.rx',180)
                    rig.setAttr(curveName+'.scale',0.2*scaleVal,0.2*scaleVal,0.2*scaleVal)            
                    SK_freezeObj(curveName)

                    if pointAxisX > 0:
                        rig.setAttr(curveName+'.sy',-1)
                        SK_freezeObj(curveName)
                    
#                   锁定并隐藏部分属性：
                    SK_hideLockAll(curveName,1,0)
                    rig.setAttr(curveName+'.tx',cb = False,k = True,l = False)
                    
                    curveNameGrpLow = rig.group(curveName,n = curveName+'_Low') 
                    rig.xform(curveNameGrpLow,os = True ,piv = (0,0,0))  
                    curveNameGrpUp = rig.group(curveNameGrpLow,n = curveName+'_Up') 
                    rig.xform(curveNameGrpUp,os = True ,piv = (0,0,0)) 
                    rig.parent(curveNameGrpUp,parentControl) 
                    parentControl =  curveName  
                    SK_snapToObj(subFinger,curveNameGrpUp)      
                    rig.connectAttr(selJnt+'.ctrl',curveName+'.ctrl') 
                    
                    rig.parentConstraint(curveName,subFinger)
 
        
#    create aimConstraint
    for rootJnt in rootFingers:
        jntAimGrp = rig.group(empty = True,n = rootJnt+'_AimGrp')
        SK_snapToObj(rootJnt,jntAimGrp)
        rig.parent(jntAimGrp,rootJnt)
        rig.setAttr(jntAimGrp+'.ty',0.5*scaleVal)
        rig.parent(jntAimGrp,jntObj)
        
        fingerSecond = rig.listRelatives(rootJnt,c = True)[0]
        fingerCon = fingerSecond.replace('_jnt','')
        rig.aimConstraint(fingerCon,rootJnt,mo = True,aimVector = (1,0,0),worldUpType = 'object',worldUpObject = jntAimGrp)
        
        

        

