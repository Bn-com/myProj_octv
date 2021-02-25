#-*- coding: utf-8 -*-
import maya.cmds as rig


def SK_selectSkinJnt():
    jnts = rig.select(rig.ls('*_jnt'))
    removeJnt = SK_removeExceptJnt()
    addJnt = SK_addExceptJnt()
    
    hands = rig.ls('*_hand_drv')
    if hands:
        for hand in hands:
            handJnts = rig.listConnections(hand+'.ctrl',s = False,d = True)
            if not handJnts:
                rig.select(hand,add = True)
  
    
    foots = rig.ls('*_foot_drv')
    if foots:
        for foot in foots:
            footJnts = rig.listConnections(foot+'.ctrl',s = False,d = True)
            if not footJnts:
                rig.select(foot,add = True)
   
    skinJnts = rig.ls(sl = True)
    if(removeJnt):
        rig.select(removeJnt,d = True)
    if(addJnt):
        rig.select(addJnt,add = True)
    skinJnts = rig.ls(sl = True)
    return skinJnts


def SK_removeExceptJnt():
    removeJnts = []
    
    elbow = (rig.ls('*_elbow_drv_jnt'))
    arm = (rig.ls('*_upArm_drv_jnt'))
    leg = (rig.ls('*_leg_drv_jnt'))
    knee = (rig.ls('*_knee_drv_jnt'))
    shoulder = rig.ls('*_clavicle2_jnt')
    
    if elbow:
        removeJnts.extend(elbow)
    if arm:
        removeJnts.extend(arm)
    if leg:
        removeJnts.extend(leg)
    if knee:
        removeJnts.extend(knee)
    if shoulder:
        removeJnts.extend(shoulder)
    
    removeJnts.append('chest2_jnt')    
    removeJnts.append('chest3_jnt')    
    removeJnts.append(rig.ls('waist*_jnt',type = 'joint')[-1])
    removeJnts.append('head_end_jnt')    
    removeJnts.append('lower_jaw_end_jnt') 
    removeJnts.append('upper_jaw_end_jnt')         
    removeJnts.append(rig.ls('neck*_jnt',type = 'joint')[-1])
    
    return removeJnts

    
def SK_addExceptJnt():
    addJnts = []
    
#    bendJnts = (rig.ls('*_bend0_startJnt')) 
#    if bendJnts:
#        addJnts.extend(bendJnts)
        
    return addJnts
