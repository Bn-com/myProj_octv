#-*- coding: utf-8 -*-
import maya.cmds as rig
from RIG.selectJoint import SK_selectSkinJnt

def SK_getRelativeCurve(curversList= [],keyName =[]):
    if(1 == len(keyName)):
        allCurve = []
        for curveContorl in curversList:
            if(keyName[0] in curveContorl):
                allCurve.append(curveContorl)
    else:
        allCurve = []
        LfCurve = []
        RtCurve = []
        for keyStr in keyName:
            for curveContorl in curversList:
                if(keyStr in curveContorl):
                    if('Lf' in curveContorl.split('_')[0]):
                        LfCurve.append(curveContorl)  
                    if('Rt' in curveContorl.split('_')[0]):
                        RtCurve.append(curveContorl) 
        allCurve.extend(LfCurve)
        allCurve.extend(RtCurve)                                 
                            
    return allCurve
 
    
def SK_orderControlCurveSet():
    reOrderList = []
    allCtrls = rig.sets('bodySet',q = True)
    allCtrlsSet = set(allCtrls)
    
    orderLists = [['Master'],['Character'],['waist_Ctrl'],['root_waist_ikCtrl'],['waist_FK1_ctrl'],['waist_FK2_ctrl'],['mid_waist_ikCtrl'],['top_waist_ikCtrl'],\
                 ['neck_FK_ctrl'],['head_ctrl'],['_shoulder','Arm_UpArm_FK','Arm_Elbow_FK','_Wrist_FK','Arm_Pole_ctrl','Arm_Wrist_IK','Arm_Switch'],\
                 ['Leg_Pole_ctrl','Leg_Leg_IK','Leg_foot','Leg_Leg_FK','Leg_Knee_FK','Leg_Ankle_FK','Leg_ball_FK','Leg_Switch'],['upArm1_bend','elbow1_bend',\
                 'leg1_bend','knee1_bend'],] 
    
    for conCurve in orderLists:
        curveLs = SK_getRelativeCurve(allCtrls,conCurve)
        reOrderList.extend(curveLs)
        
    reOrderListSet = set(reOrderList)
    orderSets = allCtrlsSet - reOrderListSet
    tempList = []
    tempList.extend(orderSets)
    tempList.sort()
    reOrderList.extend(tempList)
    rig.delete('bodySet') 
       
    rig.sets(reOrderList,n = 'bodySet')


def SK_footHandFingerSet(fingers = []):
    allCurs = []
   
    if fingers:
        for fin in fingers:
            curs = rig.listConnections(fin,s = False,d = True,type = 'joint')
            for cur in curs:
                if not (rig.getAttr(cur+'.visibility')):
                    allCurs.append(cur)
        
    return allCurs   


def SK_createBodySets():
    def SK_removeSameObj(sour = [],des = []):
        for obj in des:
            if(obj in sour):
                sour.remove(obj)
    nurs = [rig.listRelatives(nur,p = True)[0] for nur in rig.ls(type = 'nurbsCurve') if rig.attributeQuery('ctrl',node = rig.listRelatives(nur,p = True)[0],ex = True)]
    
    bend0s = rig.ls('*0_bend')
    if bend0s:
        SK_removeSameObj(nurs,bend0s)
        
    bend2s = rig.ls('*2_bend')
    if bend2s:
        SK_removeSameObj(nurs,bend2s)
        
    handFings = rig.ls('*_hand_drv')
    if handFings:
        removeCurve = SK_footHandFingerSet(handFings)
        SK_removeSameObj(nurs,removeCurve)
        
    footFings = rig.ls('*_foot_drv')
    if footFings:
        removeCurve = SK_footHandFingerSet(footFings)
        SK_removeSameObj(nurs,removeCurve)
    
#    nurs.remove('mid_waist_ikCtrl')    
    nurs.append('waist4_FK')
    nurs.append('waist2_FK') 
    nurs.append('Character')

       
    if(rig.objExists('bodySet')):
        rig.delete('bodySet')
    nurs = [nur for nur in nurs if rig.objExists(nur)]
    
    rig.sets(nurs,n = 'bodySet')
    SK_orderControlCurveSet()
        
     
def SK_createJointSet():
    allBindJoints = SK_selectSkinJnt()
    rig.select(cl = True)
    
    LfArmJnts = []
    RtArmJnts = []
    LfLegJnts = []
    RtLegJnts = []
    LfFingerJnts = []
    RtFingerJnts = []
    LfToeFingerJnts = []
    RtToeFingerJnts = []
    shoulderJnts = []
    splineJnts = []
    headJnts = []
    armMids = []
    LegMids = []
    body = []
    allSets = []
    
    for jnt in allBindJoints:
        if('Arm1_jnt' in jnt):
            armMids.append(jnt)
        if('Leg1_jnt' in jnt):
            LegMids.append(jnt)
        
        if('Arm' in jnt and 'Lf' in jnt.split('_')[0]):
            LfArmJnts.append(jnt)
        elif('Arm' in jnt and 'Rt' in jnt.split('_')[0]):
            RtArmJnts.append(jnt)
        elif('Leg' in jnt and 'Lf' in jnt.split('_')[0]):
            LfLegJnts.append(jnt)        
        elif('Leg' in jnt and 'Rt' in jnt.split('_')[0]):
            RtLegJnts.append(jnt)          
        elif('Toe' in jnt and 'Lf' in jnt.split('_')[0]):
            LfToeFingerJnts.append(jnt)        
        elif('Toe' in jnt and 'Rt' in jnt.split('_')[0]):
            RtToeFingerJnts.append(jnt) 
        elif('clavicle' in jnt):
            shoulderJnts.append(jnt)        
        elif('spline' in jnt):
            splineJnts.append(jnt)
        elif('neck' in jnt or 'head'in jnt):
            headJnts.append(jnt)
        else:
            if('Lf' in jnt.split('_')[0]):
                LfFingerJnts.append(jnt)
            elif('Rt' in jnt.split('_')[0]):
                RtFingerJnts.append(jnt)   
        
    armMids.append(splineJnts[-1])
    armMids.extend(shoulderJnts)
    LegMids.append(splineJnts[0])

    
    if(LfArmJnts):
        LfArmJnts.extend(armMids)
    if(RtArmJnts):
        RtArmJnts.extend(armMids) 
        
    if(LfLegJnts):
        LfLegJnts.extend(LegMids)
    if(RtLegJnts):
        RtLegJnts.extend(LegMids)
    
        
    body.extend(splineJnts)
    body.extend(headJnts)
    body.extend(armMids)
    body.extend(LegMids)
    
    if(LfArmJnts):
        allSets.append(rig.sets(LfArmJnts,n = 'Lf_Arm_Set'))
    if(RtArmJnts):    
        allSets.append(rig.sets(RtArmJnts,n = 'Rt_Arm_Set'))
    if(LfLegJnts): 
        allSets.append(rig.sets(LfLegJnts,n = 'Lf_Leg_Set'))
    if(RtLegJnts): 
        allSets.append(rig.sets(RtLegJnts,n = 'Rt_Leg_Set'))
    if(LfFingerJnts): 
        allSets.append(rig.sets(LfFingerJnts,n = 'Lf_Finger_Set'))
    if(RtFingerJnts): 
        allSets.append(rig.sets(RtFingerJnts,n = 'Rt_Finger_Set'))
    if(LfToeFingerJnts): 
        allSets.append(rig.sets(LfToeFingerJnts,n = 'Lf_ToeFinger_Set'))
    if(RtToeFingerJnts): 
        allSets.append(rig.sets(RtToeFingerJnts,n = 'Rt_ToeFinger_Set'))
    if(body): 
        allSets.append(rig.sets(body,n = 'body_Set'))
    rig.sets(allSets,n = 'Influence_Joint')
 
        