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

def CJW_createFacialCtrlSets():       
    LookCtrls = ['c_Rt_up_eyelids_CTRL', 'c_Rt_dn_eyelids_CTRL', 'c_Lf_up_eyelids_CTRL', 'c_Lf_dn_eyelids_CTRL',
                 'c_Rt_eyelids_CTRL', 'c_Lf_eyelids_CTRL','c_eye_M', 'c_Rt_eye_M', 'c_Lf_eye_M', 'c_Rt_spec_M', 'c_Lf_spec_M']
    LookSet = [LookCtrl for LookCtrl in LookCtrls if rig.objExists(LookCtrl)]
    BrowsCtrls = ['c_Rt_eyebrows_01_CTRL', 'c_Rt_eyebrows_02_CTRL', 'c_Rt_eyebrows_03_CTRL','c_Rt_eyebrows_CTRL',
                 'c_Lf_eyebrows_01_CTRL', 'c_Lf_eyebrows_02_CTRL', 'c_Lf_eyebrows_03_CTRL','c_Lf_eyebrows_CTRL']
    BrowsSet = [BrowsCtrl for BrowsCtrl in BrowsCtrls if rig.objExists(BrowsCtrl)]
    LipsCtrls = ['c_muothLip_01_second_CTRL', 'c_muothLip_02_second_CTRL', 'c_muothLip_03_second_CTRL', 'c_muothLip_04_second_CTRL', 'c_muothLip_05_second_CTRL', 'c_muothLip_06_second_CTRL', 'c_muothLip_07_second_CTRL', 
                 'c_muothLip_08_second_CTRL','c_muothLip_09_second_CTRL', 'c_muothLip_10_second_CTRL', 'c_muothLip_11_second_CTRL', 'c_muothLip_12_second_CTRL', 'c_muothLip_13_second_CTRL', 'c_muothLip_14_second_CTRL', 
                 'c_up_mouthLip_CTRL', 'c_Rt_mouthLip_CTRL', 'c_Lf_mouthLip_CTRL', 'c_dn_mouthLip_CTRL']
    LipsSet = [LipsCtrl for LipsCtrl in LipsCtrls if rig.objExists(LipsCtrl)]
    MouthCtrls = ['c_up_mouthLip_CTRL', 'c_Rt_mouthLip_CTRL', 'c_Lf_mouthLip_CTRL', 'c_dn_mouthLip_CTRL','c_mouthLip_CTRL','c_jaw_dn_CTRL', 'c_mouth_CTRL',
                  'c_Rt_eyeStretch_CTRL', 'c_Lf_eyeStretch_CTRL','c_nose_CTRL', 'c_Rt_nosewing_CTRL', 'c_Lf_nosewing_CTRL', 'c_nose_M_CTRL']
    MouthSet = [MouthCtrl for MouthCtrl in MouthCtrls if rig.objExists(MouthCtrl)]
    OtherCtrls = ['c_tongue_CTRL','c_tongue_joint9', 'c_tongue_joint8', 'c_tongue_joint7', 'c_tongue_joint6', 'c_tongue_joint5', 'c_tongue_joint4', 'c_tongue_joint3', 'c_tongue_joint2', 'c_tongue_joint1',
                  'UpperTooth_Ctrl', 'UpperTooth_second01_Ctrl', 'UpperTooth_second02_Ctrl', 'UpperTooth_second03_Ctrl', 'UpperTooth_second04_Ctrl', 'UpperTooth_second05_Ctrl', 'LowerTooth_Ctrl', 'LowerTooth_second01_Ctrl', 'LowerTooth_second02_Ctrl', 'LowerTooth_second03_Ctrl', 'LowerTooth_second04_Ctrl', 'LowerTooth_second05_Ctrl']
    OtherSet = [OtherCtrl for OtherCtrl in OtherCtrls if rig.objExists(OtherCtrl)]    
    
    
    
    rig.select(cl=1) 
    ALLFacialCtrlSETS = ['All_FacialSet','LookSet','BrowsSet','LipsSet','MouthSet','OtherSet']
    for facePieceSet in  ALLFacialCtrlSETS:
        if rig.objExists(facePieceSet):
            rig.delete(facePieceSet)
        rig.sets(name = facePieceSet)
       
    if not LookSet==[]:
        rig.sets(LookSet,addElement = 'LookSet')
    if not BrowsSet==[]:        
        rig.sets(BrowsSet,addElement = 'BrowsSet')
    if not LipsSet==[]:      
        rig.sets(LipsSet,addElement = 'LipsSet')
    if not MouthSet==[]:      
        rig.sets(MouthSet,addElement = 'MouthSet')   
    if not OtherSet==[]:      
        rig.sets(OtherSet,addElement = 'OtherSet') 
        
    if not rig.objExists('CtrlSet'):
        rig.sets(name = 'CtrlSet')
    rig.sets('LookSet','BrowsSet','LipsSet','MouthSet','OtherSet',addElement = 'All_FacialSet')
    rig.sets('All_FacialSet',addElement='CtrlSet')    
    
def CJW_createCtrlSets():
    BodyCtrls = ['Master','Character','waist_Ctrl','root_waist_ikCtrl','mid_waist_ikCtrl','waist_FK1_ctrl','top_waist_ikCtrl',
'waist_FK2_ctrl','neck_FK_ctrl','head_ctrl']
    BodySet = [BodyCtrl for BodyCtrl in BodyCtrls if rig.objExists(BodyCtrl)]
    Lf_ArmCtrls = ['Lf_shoulder','LfArm_UpArm_FK','LfupArm1_bend','LfArm_Elbow_FK','Lfelbow1_bend','LfArm_Wrist_FK',
'LfArm_Pole_ctrl','LfArm_Wrist_IK','LfArm_Switch','LfArm_wristMid_FK']
    Lf_ArmSet = [Lf_ArmCtrl for Lf_ArmCtrl in Lf_ArmCtrls if rig.objExists(Lf_ArmCtrl)]    
    Rt_ArmCtrls = ['Rt_shoulder','RtArm_UpArm_FK','RtupArm1_bend','RtArm_Elbow_FK','Rtelbow1_bend','RtArm_Wrist_FK',
'RtArm_Pole_ctrl','RtArm_Wrist_IK','RtArm_Switch','RtArm_wristMid_FK']
    Rt_ArmSet = [Rt_ArmCtrl for Rt_ArmCtrl in Rt_ArmCtrls if rig.objExists(Rt_ArmCtrl)]
    Lf_FingerCtrls = ['Lf_thumb1','Lf_thumb2','Lf_thumb3','Lf_index1','Lf_index2','Lf_index3',
'Lf_mid1','Lf_mid2','Lf_mid3','Lf_ring1','Lf_ring2','Lf_ring3','Lf_pinky1','Lf_pinky2','Lf_pinky3'] 
    Lf_FingerSet = [Lf_FingerCtrl for Lf_FingerCtrl in Lf_FingerCtrls if rig.objExists(Lf_FingerCtrl)]
    Rt_FingerCtrls = ['Rt_thumb1','Rt_thumb2','Rt_thumb3','Rt_index1','Rt_index2','Rt_index3',
'Rt_mid1','Rt_mid2','Rt_mid3','Rt_ring1','Rt_ring2','Rt_ring3','Rt_pinky1','Rt_pinky2','Rt_pinky3'] 
    Rt_FingerSet = [Rt_FingerCtrl for Rt_FingerCtrl in Rt_FingerCtrls if rig.objExists(Rt_FingerCtrl)]    
    Lf_LegCtrls = ['LfLeg_Leg_IK','LfLeg_foot','Lfknee1_bend','LfLeg_Pole_ctrl','Lfleg1_bend','LfLeg_hip_ctrl',
'LfLeg_Ankle_FK','LfLeg_Knee_FK','LfLeg_Leg_FK','LfLeg_Switch','LfLeg_Pole_ctrl','LfLegLeg_ball_FK']
    Lf_LegSet = [Lf_LegCtrl for Lf_LegCtrl in Lf_LegCtrls if rig.objExists(Lf_LegCtrl)]
    Rt_LegCtrls = ['RtLeg_Leg_IK','RtLeg_foot','Rtknee1_bend','RtLeg_Pole_ctqwrl','Rtleg1_bend','RtLeg_hip_ctrl',
'RtLeg_Ankle_FK','RtLeg_Knee_FK','RtLeg_Leg_FK','RtLeg_Switch','RtLeg_Pole_ctrl','RtLegLeg_ball_FK']
    Rt_LegSet = [Rt_LegCtrl for Rt_LegCtrl in Rt_LegCtrls if rig.objExists(Rt_LegCtrl)] 
    Lf_ToesCtrls = ['Lf_Toe_index1','Lf_Toe_index2','Lf_Toe_index3','Lf_Toe_mid1','Lf_Toe_mid2','Lf_Toe_mid3',
'Lf_Toe_ring1','Lf_Toe_ring2','Lf_Toe_ring3','Lf_Toe_pinky1','Lf_Toe_pinky2','Lf_Toe_pinky3','Lf_Toe_thumb1','Lf_Toe_thumb2','Lf_Toe_thumb3']
    Lf_ToesSet = [Lf_ToesCtrl for Lf_ToesCtrl in Lf_ToesCtrls if rig.objExists(Lf_ToesCtrl)]
    Rt_ToesCtrls = ['Rt_Toe_index1','Rt_Toe_index2','Rt_Toe_index3','Rt_Toe_mid1','Rt_Toe_mid2','Rt_Toe_mid3',
'Rt_Toe_ring1','Rt_Toe_ring2','Rt_Toe_ring3','Rt_Toe_pinky1','Rt_Toe_pinky2','Rt_Toe_pinky3','Rt_Toe_thumb1','Rt_Toe_thumb2','Rt_Toe_thumb3']
    Rt_ToesSet = [Rt_ToesCtrl for Rt_ToesCtrl in Rt_ToesCtrls if rig.objExists(Rt_ToesCtrl)]
    rig.select(cl=1)
    ALLBODYSETS = ['All_BodySet','BodySet','Lf_ArmSet','Rt_ArmSet','Lf_FingerSet','Rt_FingerSet','Lf_LegSet','Rt_LegSet','Lf_ToesSet','Rt_ToesSet']       
    for bodyPieceSet in ALLBODYSETS:
        if rig.objExists(bodyPieceSet):
            rig.delete(bodyPieceSet)
        rig.sets(name = bodyPieceSet)
            
    if not BodySet==[]:
        rig.sets(BodySet,addElement = 'BodySet')
    if not Lf_ArmSet==[]:        
        rig.sets(Lf_ArmSet,addElement = 'Lf_ArmSet')
    if not Rt_ArmSet==[]:      
        rig.sets(Rt_ArmSet,addElement = 'Rt_ArmSet')
    if not Lf_FingerSet==[]:      
        rig.sets(Lf_FingerSet,addElement = 'Lf_FingerSet')
    if not Rt_FingerSet==[]:      
        rig.sets(Rt_FingerSet,addElement = 'Rt_FingerSet') 
    if not Lf_LegSet==[]:           
        rig.sets(Lf_LegSet,addElement = 'Lf_LegSet')  
    if not Rt_LegSet==[]:        
        rig.sets(Rt_LegSet,addElement = 'Rt_LegSet')
    if not Lf_ToesSet==[]:      
        rig.sets(Lf_ToesSet,addElement = 'Lf_ToesSet')  
    if not Rt_ToesSet==[]:        
        rig.sets(Rt_ToesSet,addElement = 'Rt_ToesSet')
        
    if not rig.objExists('CtrlSet'):
        rig.sets(name = 'CtrlSet')           
    rig.sets('BodySet','Lf_ArmSet','Rt_ArmSet','Lf_FingerSet','Rt_FingerSet',
'Lf_LegSet','Rt_LegSet','Lf_ToesSet','Rt_ToesSet',addElement = 'All_BodySet')
    rig.sets('All_BodySet',addElement='CtrlSet')
     
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
 
        