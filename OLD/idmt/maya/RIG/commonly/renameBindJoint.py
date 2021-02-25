#-*- coding: utf-8 -*-
import maya.cmds as rig
from RIG.selectJoint import SK_selectSkinJnt 

def SK_renameSkinJoint():
    legs = rig.ls('*_ankle_drv_jnt')
    arms = rig.ls('*_wrist_drv_jnt')
    
    for Leg in legs:
        legPrefix = Leg.split('_')[0]
        legPrefixName = legPrefix+'_Leg'
        legPrefixMidName = legPrefix+'Leg'        
        upBendJnt = rig.ls(legPrefix+'leg_bend'+'*'+'jnt')
        upLen = len(upBendJnt)
        upBendJnt.insert(0,upBendJnt[0].replace('1_jnt','0_startJnt'))
        for i,Jnt in enumerate(upBendJnt):
            rig.rename(Jnt,legPrefixName+str(i+1)+'_jnt')
        
        downBendJnt = rig.ls(legPrefix+'knee_bend'+'*'+'jnt')
        downLen = len(downBendJnt)    
        downBendJnt.insert(0,rig.rename(legPrefixMidName+'_MidJoint_jnt',legPrefixName+'1_jnt'))
        for i,Jnt in enumerate(downBendJnt):
            rig.rename(Jnt,legPrefixName+str(i+upLen+2)+'_jnt')
            
        rig.rename(Leg,legPrefixName+str(downLen+upLen+3)+'_jnt')
        
    for arm in arms:
        armPrefix = arm.split('_')[0]
        armPrefixName = armPrefix+'_Arm'
        armPrefixMidName = armPrefix+'Arm'  
        upBendJnt = rig.ls(armPrefix+'upArm_bend'+'*'+'jnt')
        upLen = len(upBendJnt)
        upBendJnt.insert(0,upBendJnt[0].replace('1_jnt','0_startJnt'))
        for i,Jnt in enumerate(upBendJnt):
            rig.rename(Jnt,armPrefixName+str(i+1)+'_jnt')
        
        downBendJnt = rig.ls(armPrefix+'elbow_bend'+'*'+'jnt')
        downLen = len(downBendJnt)    
        downBendJnt.insert(0,rig.rename(armPrefixMidName+'_MidJoint_jnt',armPrefixName+'1_jnt'))
        for i,Jnt in enumerate(downBendJnt):
            rig.rename(Jnt,armPrefixName+str(i+upLen+2)+'_jnt')
            
        rig.rename(arm,armPrefixName+str(downLen+upLen+3)+'_jnt')
        
        
#    对腰,脖子,头 ,改名
    allSkinJoints = SK_selectSkinJnt()
    rig.select(cl = True)
    
    midJoint = []
    for jnt in allSkinJoints:
        if not ('Rt' in jnt or 'Lf' in jnt):
            midJoint.append(jnt)     
    
    waistJoint = []
    for jnt in midJoint:
        if('waist' in jnt):
            waistJoint.append(jnt)    
    
    waistJoint.insert(0,'hip_jnt')
    waistJoint.append('chest1_jnt')
    
    for i,jnt in enumerate(waistJoint):
        rig.rename(jnt,'spline'+str(i+1)+'_jnt')
    
    rig.rename('lower_jaw_jnt','head_jawLow_jnt')
    rig.rename('upper_jaw_jnt','head_jawUp_jnt')
    