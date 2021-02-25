#-*- coding: utf-8 -*-
import maya.cmds as rig
from RIG.commonly.restoreJoint import SK_restoreJoint,SK_createPaintJoint
from RIG.legArm import *
from RIG.finger import SK_createFinger
from RIG.shoulder import SK_createShoulder
from RIG.body import SK_stretchSplineIK
from RIG.head import SK_neckRig
from RIG.commonly.base import *
from RIG.commonly.twist import SK_createTwist
from RIG.commonly.sets import SK_createBodySets,SK_createJointSet,CJW_createCtrlSets
from RIG.commonly.resetControllerDefaultPose import SK_creatConDefaultPos
from RIG.commonly.renameBindJoint import SK_renameSkinJoint
from RIG.commonly.lockTransform import SK_lockAllJoint
from RIG.commonly.addBlendShapeControl import SK_createBlendShapeCon


#execfile('Z:/Resource/Groups/Production/Modeling/Rigging 2009 Development Plan/BodyRiggingTools/script/RIG/mainWindow/gdc_bodyRig2009_mainWindow.py')

def SK_createLegArm(selObjs = []):
    
    if not selObjs:
        selObjs = rig.ls(sl = True)
    selLs = [jnt for jnt in selObjs if(('joint' == rig.nodeType(jnt)) and(('leg' in jnt) or ('upArm' in jnt)))]
    if selLs:
        for jnt in selLs:
            SK_createLeg(jnt)    


def SK_createFootWrist(selObjs = []):
    if not selObjs:
        selObjs = rig.ls(sl = True)
    selLs = [jnt for jnt in selObjs if(('joint' == rig.nodeType(jnt)) and(('ankle' in jnt) or ('wrist' in jnt)))]
    if selLs:
        for jnt in selLs:
            SK_createFoot(jnt)  


def SK_createToeHand(selObjs = []):
    if not selObjs:
        selObjs = rig.ls(sl = True) 
    selLs = [jnt for jnt in selObjs if(('joint' == rig.nodeType(jnt)) and(('hand' in jnt) or ('foot' in jnt)))]
    if selLs:
        for jnt in selLs:
            SK_createFinger(jnt)     


def SK_createShoulderPart(selObjs = []):
    if not selObjs:
        selObjs = rig.ls(sl = True) 
    selLs = [jnt for jnt in selObjs if(('joint' == rig.nodeType(jnt)) and('_clavicle' in jnt))]
    if selLs:
        for jnt in selLs: 
            SK_createShoulder(jnt)           
              

def SK_createMidLeg(selObjs = []):
    if not selObjs:
        selObjs = rig.ls(sl = True) 
    selLs = [jnt for jnt in selObjs if(('joint' == rig.nodeType(jnt)) and (('_upArm' in jnt) or ('_knee' in jnt) or ('_leg' in jnt) or ('_elbow' in jnt)))]
    if selLs:
        for jnt in selLs:
            splitStr = jnt.split('_')
            jntName = splitStr[0]+splitStr[1]
            SK_createSplitJointRig(jnt,jntName,4) 


def SK_createLegArmTwist(selObjs = []):
    if not selObjs:
        selObjs = rig.ls(sl = True)
    selLs = [jnt for jnt in selObjs if('nurbsCurve' == rig.nodeType(rig.listRelatives(jnt,s = True)[0]))]
    if selLs:
        for jnt in selLs:
            SK_createTwist(jnt)
   
def createHipCtrl():
    if rig.objExists('AutoHip_LocatorGRP_ALL')!=True:
        rig.group(em = True,name = 'AutoHip_LocatorGRP_ALL')
        rig.group(em = True,n='AutoHip_Character_Loc_Co_GRP',parent = 'AutoHip_LocatorGRP_ALL')
        rig.group(em = True,n='AutoHip_root_waist_ikCtrl_Loc_Co_GRP',parent = 'AutoHip_LocatorGRP_ALL')
        rig.parentConstraint ('Character','AutoHip_Character_Loc_Co_GRP',mo=1, weight=1)
        rig.parentConstraint ('root_waist_ikCtrl','AutoHip_root_waist_ikCtrl_Loc_Co_GRP',mo=1, weight=1)
        rig.setAttr('AutoHip_LocatorGRP_ALL.visibility',0)
        
    hipJoints = rig.ls('*hip_drv')
    
    if hipJoints:
        for hip in hipJoints:
            prefix = hip.split('_')[0]
            ikCon = prefix + 'Leg_Leg_IK'
            ikConLocator01 = ikCon+'_AutoHip_Locator'
            ikConLocator03 = ikCon+'_AutoHip_Pole_Locator'
            IKAutoHip_LcGRP = ikCon+'_AutoHip_Locator_GRP'
            IKAutoHipPole_Lc_Aim_GRP = ikCon+'_AutoHip_Pole_Locator_GRP_AimGRP_GRP'
            
            hipCtrl = rig.rename(SK_b32(6),(prefix+'Leg_hip_ctrl'))
            scaleVal = rig.getAttr(ikCon+'.scaleVal')
            rig.setAttr(hipCtrl+'.scale',scaleVal,scaleVal,scaleVal)
            SK_freezeObj(hipCtrl)
            AutoHipAttr ='autoFollowIK'
            hipCtrlAutoAttr = hipCtrl + '.' + AutoHipAttr
            rig.setAttr(hipCtrl+'.visibility',lock= True ,keyable = False , channelBox = False)
            #rig.addAttr(hipCtrl,ln = 'Auto_Follow_IK',at = 'enum',en = 'off:on:')
            rig.addAttr (hipCtrl,ln = AutoHipAttr , at ='double' ,min = 0, max= 10, dv = 0)
            rig.setAttr(hipCtrlAutoAttr,e=1,keyable = 1)
            hipCtrlGRP = rig.group(hipCtrl,n=hipCtrl+'_GRP')
            hipAllCtrlGrp = rig.group(hipCtrlGRP,n=hipCtrlGRP+'_ALL')              
            rig.setAttr(hipCtrl+'.translateX',2)
            rig.setAttr(hipCtrl+'.rotateZ',-90)
            rig.setAttr(hipCtrl+'.scale',0.15,0.15,0.15)
            SK_freezeObj(hipCtrl) 
            rig.setAttr(hipCtrl+'.rotatePivot',0,0,0)
            rig.setAttr(hipCtrl+'.scalePivot',0,0,0) 
            
            AutoHip_IK_GRP = rig.group(em=True,n = prefix+'_autoHip_IK_GRP',parent = hipAllCtrlGrp,relative=1)
            AutoHip_FK_GRP = rig.group(em=True,n = prefix+'_autoHip_FK_GRP',parent = hipAllCtrlGrp,relative=1)
            OrientConstraint1 = rig.orientConstraint(AutoHip_IK_GRP,AutoHip_FK_GRP,hipCtrlGRP,mo=1, weight=1 )[0]
            #AutoHipMD = rig.createNode('multiplyDivide',n = hipCtrl+'_MD',ss = True)
            AutoHipUC = rig.createNode('unitConversion',n = hipCtrl+'_UC',ss = True)
            rig.setAttr(AutoHipUC+'.conversionFactor',0.1)                            
            rig.connectAttr(hipCtrlAutoAttr,AutoHipUC+'.input')
            rig.connectAttr(AutoHipUC+'.output',OrientConstraint1+'.'+AutoHip_IK_GRP+'W0')            
            AutoHipRV = rig.createNode('reverse',n = hipCtrl+'_reverse',ss = True)
            rig.connectAttr(AutoHipUC+'.output',AutoHipRV+'.inputX')                          
            rig.connectAttr(AutoHipRV+'.outputX',OrientConstraint1+'.'+AutoHip_FK_GRP+'W1')                
            if 'Lf' in prefix:
                xformHip = rig.xform(hip,q=1,ws=1,sp=1)
                rig.setAttr(hipAllCtrlGrp+'.scale',1,1,1)
                rig.setAttr(hipAllCtrlGrp+'.translate',xformHip[0],xformHip[1],xformHip[2])
                rig.parent(prefix+'Leg_ALL_CTRL_GRP',hipCtrl)
                hipCtrlJoint = rig.duplicate(hip,n = hip+'_jnt',po=1) 
                rig.parent (hipCtrlJoint,hipCtrl)
            if 'Rt' in prefix:
                xformHip = rig.xform(hip,q=1,ws=1,sp=1)
                rig.setAttr(hipAllCtrlGrp+'.scale',-1,1,1)
                rig.setAttr(hipAllCtrlGrp+'.translate',xformHip[0],xformHip[1],xformHip[2])  
                rig.parent(prefix+'Leg_ALL_CTRL_GRP',hipCtrl)
                hipCtrlJoint = rig.duplicate(hip,n = hip+'_jnt',po=1) 
                rig.parent (hipCtrlJoint,hipCtrl)  
            

            rig.parent(IKAutoHip_LcGRP,'AutoHip_Character_Loc_Co_GRP')  
            rig.parent(IKAutoHipPole_Lc_Aim_GRP,'AutoHip_root_waist_ikCtrl_Loc_Co_GRP') 
                                
            AimConstraint1 = rig.aimConstraint(ikConLocator01,AutoHip_IK_GRP,mo=1,weight= 1,worldUpType='object',worldUpObject=ikConLocator03)[0]   
   
def SK_combination():
    master = 'Character'
    waist = 'root_waist_ikCtrl'
    waistIK = 'root_waist_ikCtrl'
    waistIKUp = 'top_waist_ikCtrl'  
    neckJnt =   'chest2_jnt'
    neckJntUp = 'chest3_jnt'
    torso = 'waist_IKfollow_Ctrl'
    headJnt = 'head_jnt'
    
#   完成腿部合并
    hips = rig.ls('*hip_ctrl_GRP_ALL') 
    
    if hips:
        rig.parent(hips,waistIK)
        for hip in hips:
            #leg=legs[1]
            prefix = hip.split('_')[0]
            ikCon = prefix+'_Leg_IK'
            ikConGrp = prefix+'_Leg_IK_Constraint'
            poleGrp = prefix+'_Pole_ctrl_GRP'  

#           增加膝盖follow控制          
            poleGrpConstraint = rig.parentConstraint(master,poleGrp,mo = True)[0]
            poleCurve = rig.listRelatives(poleGrp,c = True)[0]
            rig.connectAttr(poleCurve+'.world',poleGrpConstraint+'.'+master+'W0')
                        
            rig.parentConstraint(master,ikConGrp,mo = True)     
            
            inSelectGrp = rig.group(empty = True,n = prefix+'Leg_inPole_select')
            outSelectGrp = rig.group(empty = True,n = prefix+'Leg_outPole_select')
            selNode = rig.createNode('choice',n = prefix+'_SC',ss = True)
            rig.setAttr(inSelectGrp+'.translate',1,0,0)
            rig.setAttr(inSelectGrp+'.rotate',0,57.296,57.296)
            rig.setAttr(inSelectGrp+'.scale',0,0,1)  
            rig.setAttr(inSelectGrp+'.shear',0,0,0) 
            rig.connectAttr(inSelectGrp+'.translate',selNode+'.input[0]')    
            rig.connectAttr(inSelectGrp+'.rotate',selNode+'.input[1]')  
            rig.connectAttr(inSelectGrp+'.scale',selNode+'.input[2]')  
            rig.connectAttr(inSelectGrp+'.shear',selNode+'.input[3]') 
            rig.connectAttr(poleCurve+'.follow',selNode+'.selector') 
            rig.connectAttr(selNode+'.output',outSelectGrp+'.translate')            
            rig.connectAttr(outSelectGrp+'.tx',poleCurve+'.aimRotate') 
            rig.connectAttr(outSelectGrp+'.ty',poleCurve+'.LockKnee')   
            rig.connectAttr(outSelectGrp+'.tz',poleCurve+'.world')
            
            selectGrp = rig.group(inSelectGrp,outSelectGrp,n = prefix+'_upSelect_Grp') 
            rig.parent(selectGrp,ikCon) 
            SK_hideLockAll(selectGrp) 
            SK_hideLockAll(inSelectGrp)
            SK_hideLockAll(outSelectGrp)    
#           将手部IKFK控制放到waist_Ctrl控制器上                
#            rig.addAttr(waist,ln = prefix+'_IKFK',at = 'float',maxValue = 1,minValue = 0,dv = 1,k = True)
#            rig.connectAttr(waist+'.'+prefix+'_IKFK',prefix+'_IKFK_blendCon'+'.IKFK')          
            Roll_GRP = rig.group(em=True,name = (prefix+'_roll_GRP'))
            rig.parent(Roll_GRP,ikCon)
            rig.setAttr(Roll_GRP+'.translate',0,0,0)
            IKconDs = rig.listRelatives(ikCon,children=1,type = 'transform')
            rig.parent (IKconDs, Roll_GRP)
            ClampNote = rig.createNode('clamp',n = prefix+'_clamp',ss = True)
            rig.setAttr((ClampNote+'.maxR'),0)
            rig.connectAttr((ikCon+'.roll'),(ClampNote+'.minR'))
            rig.connectAttr((ikCon+'.roll'),(ClampNote+'.inputR'))
            rig.connectAttr((ClampNote+'.outputR'),(Roll_GRP+'.rotateX'))            
            
    '''
    Ankle_Roll_exp = rig.expression( s='RtLeg_roll_GRP.rotateX = min(0,RtLeg_Leg_IK.roll);\nLfLeg_roll_GRP.rotateX = min(0,LfLeg_Leg_IK.roll);' ,name = 'Ankle_Roll_exp')
    rig.disconnectAttr('time1.outTime',Ankle_Roll_exp+'.time')
    '''
            
            
#   完成肩膀和胳膊合åïﾾ?
    shoulders = rig.ls('*_shoulder_GRP') 
    chest =  'chest1_jnt'  
    if shoulders:
        rig.parent(shoulders,neckJnt)
        for shoulder in shoulders:
            #shoulder = shoulders[0]
            prefix = shoulder.split('_')[0]
            shoulderJnt = prefix+'_clavicle1_jnt'
            shoulderCon = prefix+'_shoulder'
            ArmAllCon = prefix+'Arm_ALL_CTRL_GRP'
            ikCon = prefix+'Arm_Wrist_IK'
            ikWrist = prefix+'Arm_Switch'
            ikConGrp = prefix+'Arm_Wrist_IK_Constraint'
            poleGrp = prefix+'Arm_Pole_ctrl_GRP'  
            
            rig.parent(shoulderJnt,neckJnt)
            
            ikConstraint = rig.parentConstraint(ArmAllCon,waist,master,neckJnt,headJnt,ikConGrp,mo = True)[0]  

#           增加肩膀follo控制           
            rig.addAttr(shoulderCon,ln = 'armFollow',at = 'enum',en = 'on:off:',dv = 1,k = True) 
            shoulderParent = rig.orientConstraint(chest,ArmAllCon,mo = True)[0] 
            rig.connectAttr(shoulderCon+'.armFollow',shoulderParent+'.'+chest+'W0')              
            
#           增加手部follow控制
            outSelectGrp = rig.group(empty = True,n = prefix+'Arm_outHand_select')
            inSelectGrp = rig.group(empty = True,n = prefix+'Arm_inHand_select')
            selNode = SK_createCompoundAttrs(outSelectGrp,5)      
            rig.connectAttr(ikWrist+'.follow',selNode+'.selector') 
            rig.connectAttr(outSelectGrp+'.bess0',ikConstraint+'.'+ArmAllCon+'W0') 
            rig.connectAttr(outSelectGrp+'.bess1',ikConstraint+'.'+waist+'W1')   
            rig.connectAttr(outSelectGrp+'.bess2',ikConstraint+'.'+master+'W2')
            rig.connectAttr(outSelectGrp+'.bess3',ikConstraint+'.'+neckJnt+'W3')
            rig.connectAttr(outSelectGrp+'.bess4',ikConstraint+'.'+headJnt+'W4')
            
            selectGrp = rig.group(inSelectGrp,outSelectGrp,n = prefix+'_select_Grp') 
            rig.parent(selectGrp,ikCon) 
            SK_hideLockAll(selectGrp) 
            SK_hideLockAll(inSelectGrp)
            SK_hideLockAll(outSelectGrp)                        
#           增加肘部follow控制
            poleGrpConstraint = rig.parentConstraint(master,poleGrp,mo = True)[0]
            poleCurve = rig.listRelatives(poleGrp,c = True)[0]
            rig.connectAttr(poleCurve+'.world',poleGrpConstraint+'.'+master+'W0')
                        
            rig.parentConstraint(master,ikConGrp,mo = True)     
            
            inSelectGrp = rig.group(empty = True,n = prefix+'Leg_inPole_select')
            outSelectGrp = rig.group(empty = True,n = prefix+'Leg_outPole_select')
            selNode = rig.createNode('choice',n = prefix+'_SC',ss = True)
            rig.setAttr(inSelectGrp+'.translate',1,0,0)
            rig.setAttr(inSelectGrp+'.rotate',0,57.296,57.296)
            rig.setAttr(inSelectGrp+'.scale',0,0,1)  
            rig.setAttr(inSelectGrp+'.shear',0,0,0) 
            rig.connectAttr(inSelectGrp+'.translate',selNode+'.input[0]')    
            rig.connectAttr(inSelectGrp+'.rotate',selNode+'.input[1]')  
            rig.connectAttr(inSelectGrp+'.scale',selNode+'.input[2]')  
            rig.connectAttr(inSelectGrp+'.shear',selNode+'.input[3]') 
            rig.connectAttr(poleCurve+'.follow',selNode+'.selector') 
            rig.connectAttr(selNode+'.output',outSelectGrp+'.translate')            
            rig.connectAttr(outSelectGrp+'.tx',poleCurve+'.aimRotate') 
            rig.connectAttr(outSelectGrp+'.ty',poleCurve+'.LockKnee')   
            rig.connectAttr(outSelectGrp+'.tz',poleCurve+'.world')
            
            selectGrp = rig.group(inSelectGrp,outSelectGrp,n = prefix+'_upSelect_Grp') 
            rig.parent(selectGrp,ikCon) 
            SK_hideLockAll(selectGrp) 
            SK_hideLockAll(inSelectGrp)
            SK_hideLockAll(outSelectGrp) 

#    将脚部IKFK控制放到waist_Ctrl控制器上                       
#            rig.addAttr(waist,ln = prefix+'Arm_IKFK',at = 'float',maxValue = 1,minValue = 0,dv = 1,k = True)
#            rig.connectAttr(waist+'.'+prefix+'Arm_IKFK',prefix+'Arm_IKFK_blendCon'+'.IKFK') 

#   connect head
    rig.parent('neck_GRP',neckJntUp)
    
#   connect chest
    rig.parent('chest1_jnt','curve_end_SkinJoint_waist')
    
#   connect waist
    rig.parent('waist_Ctrl_GRP',master)
#   delete joints
    rig.delete(rig.ls('*_hip_drv'))
    rig.delete(rig.ls('*_upArm_drv'))
    
#    增加Master控制åïﾾ?
    rig.parent('waist_Ctrl_GRP',w = True)
    masterCurve = rig.duplicate('Character',n = 'Master')[0] 
    rig.setAttr(masterCurve+'.scale',1.3,1.3,1.3)
    rig.makeIdentity(masterCurve,apply = True,s = True,t = True,r = True)
    rig.parent('Character',masterCurve)
    rig.parent('waist_Ctrl_GRP','Character')
#   连接腰部缩放组ãﾀ?
    rig.connectAttr(masterCurve+'.scale','master_refer_GRP.scale')
    
#   显示胳膊轴向ïïﾾ?
def SK_displayArmAixs():
    jointDis = [u'LfupArm_bend4_endJnt', u'Lf_Arm4_jnt', u'Lf_Arm3_jnt', u'Lf_Arm2_jnt', u'Lf_Arm1_jnt', u'Lfelbow_bend4_endJnt', u'Lf_Arm8_jnt', u'Lf_Arm7_jnt', u'Lf_Arm6_jnt', u'Lfelbow_bend0_startJnt']
    for jnt in jointDis:
        rig.setAttr(jnt+'.displayLocalAxis',1)
        
#   创建层级çïﾾ?
def SK_createHierarchyGrp():
    def SK_createGrp(grpName):
        getName = rig.group(n = grpName,empty = True)
        return getName

    CHR = SK_createGrp('CHR')
    RIG = SK_createGrp('RIG')
    MODE = SK_createGrp('MODEL')
    FX = SK_createGrp('FX')
    DEFORMERS = SK_createGrp('DEFORMERS')
    rig.parent(MODE,FX,RIG,DEFORMERS,CHR)
    
    body_rig = SK_createGrp('body_rig')
    face_rig = SK_createGrp('face_rig')
    other_rig = SK_createGrp('others_rig')
    rig.parent(body_rig,face_rig,other_rig,RIG)
    
    body_deformer = SK_createGrp('body_deformers')
    face_deformer = SK_createGrp('face_deformers')
    other_deformer = SK_createGrp('others_deformers')
    rig.parent(body_deformer,face_deformer,other_deformer,DEFORMERS)
    
    rig.parent('Master',body_rig)
    rig.parent('LegArm_deformers',body_deformer)   
#   增加CacheSet
    rig.select(cl = True)
    MESHES = rig.sets(n = 'MESHES')
    rig.sets(MESHES,n = 'CACHE_OBJS')
    
    rig.parent('AutoHip_LocatorGRP_ALL',body_deformer)
#   将twist值设äïﾾ?
def SK_SetTwistValue():
    elbows = rig.ls('*elbow_bend1_jnt')
    knees = rig.ls('*knee_bend1_jnt')
    elbows.extend(knees)
    if elbows:
        for jnt in elbows:
            rig.setAttr(jnt+'.twist',0)    
def SK_ScaleObj():
    grpName = 'ScaleConstraints_GRP'
    GrpScale = rig.group(n = grpName,empty = True)
    rig.scaleConstraint('chest1_jnt',grpName,mo = True)
    rig.parent(grpName,'LegArm_deformers')

def SK_combinationFinal():
    SK_restoreJoint()
    SK_separateJoint()
    SK_createLegArm(rig.ls('*_leg_drv'))
    SK_createLegArm(rig.ls('*_upArm_drv'))
    SK_createFootWrist(rig.ls('*_ankle_drv'))
    SK_createFootWrist(rig.ls('*_wrist_drv'))   
    SK_createToeHand(rig.ls('*_foot_drv'))
    SK_createToeHand(rig.ls('*_hand_drv'))      
    SK_createShoulderPart(rig.ls('*_clavicle1_jnt'))    
    SK_stretchSplineIK()
    SK_neckRig()
    createHipCtrl()
    SK_combination()
    SK_createMidLeg(rig.ls('*_knee_drv_jnt'))
    SK_createMidLeg(rig.ls('*_leg_drv_jnt'))   
    SK_createMidLeg(rig.ls('*_elbow_drv_jnt'))
    SK_createMidLeg(rig.ls('*_upArm_drv_jnt')) 
    SK_createLegArmTwist(rig.ls('*_Pole_ctrl')) 
    SK_ScaleObj()
    SK_createBlendShapeCon(rig.ls('*_upArm_drv_jnt'))  
    SK_createBlendShapeCon(rig.ls('*_leg_drv_jnt'))
    #SK_createPaintJoint()
    CJW_createCtrlSets()
    SK_createBodySets()
    SK_creatConDefaultPos()
    SK_SetTwistValue()
    SK_renameSkinJoint()
    SK_createJointSet()
    SK_lockAllJoint()
    SK_createHierarchyGrp()
    #gdc_bodyRig2009_mainWindow()
    #SK_displayArmAixs()
    rig.select(cl = True)
