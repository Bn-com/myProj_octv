# -*- coding: utf-8 -*-
import maya.cmds as rig
import maya.mel as mel
import os
import pickle
import tempfile

def SK_IKFKSwithCon(obj):
    selCtrl = obj
    sourceGrp = rig.connectionInfo(selCtrl+'.ctrl', sfd=True)
    sourceGrpName = sourceGrp.split('.')[0]
    allCtrls = [i.split('.')[0] for i in rig.connectionInfo(sourceGrp, dfs=True)]
    
    
    ArmLeg = True
    ikCon = ''
    fkCon = ''
    locPos = ''
    poleCon = ''
    rotatePoleCon = ''
    fkUp = ''
    fkLow = ''
    fkball = ''
    ikJointUp = ''
    ikJointLow = ''
    ikJointDown = ''
    
    
    for con in allCtrls:
        attrs = rig.listAttr(con,ud = True)      
        
        if('_Leg_IK' in con):
            ikCon = con
    
        if('_Ankle_FK' in con):
            fkCon = con    

        if('_Pole' in con):
            poleCon = con
            
        if('_RotatePole_' in con and 'ctrl' == con.split('_')[-1]):
            rotatePoleCon = con
            
        if('_Leg_FK' in con):
            fkUp = con
            
        if('_Knee_FK' in con):
            fkLow = con
    
        if('_PoleVectorPos' in con):
            locPos = con  
            
        if('_ball_FK' in con):
            fkball = con  
            
        if  ('joint' == rig.nodeType(con)):
            ikJointUp =  con
            ikJointLow = rig.listRelatives(con,c = True)[0]
            ikJointDown = rig.listRelatives(ikJointLow,c = True)[0]
            
    if ('Arm_' in selCtrl):
        ArmLeg = False
        
        for con in allCtrls:
            attrs = rig.listAttr(con,ud = True)

            if('_Wrist_IK' in con):
                ikCon = con
        
            if('_Wrist_FK' in con):
                fkCon = con      
            
            if('_Pole' in con):
                poleCon = con
                
            if('_RotatePole_' in con and 'ctrl' == con.split('_')[-1]):
                rotatePoleCon = con
                
            if('_UpArm_FK' in con):
                fkUp = con
                
            if('_Elbow_FK' in con):
                fkLow = con
        
            if('_PoleVectorPos' in con):
                locPos = con  
                
            if('_wristMid_FK' in con):
                fkball = con

                
            if  ('joint' == rig.nodeType(con)):
                ikJointUp =  con
                ikJointLow = rig.listRelatives(con,c = True)[0]
                ikJointDown = rig.listRelatives(ikJointLow,c = True)[0]
        
    ikPosition = fkCon
    if not ('Arm_' in selCtrl):
        suffix = ikJointUp.split(':')[-1]
        if 'Lf' == suffix.split('_')[0]:
            ikPosition = ikJointUp.replace(suffix,'Lf_heel_drv')
        if 'Rt' == suffix.split('_')[0]:
            ikPosition = ikJointUp.replace(suffix,'Rt_heel_drv')
            
    FKballConstraint = rig.listConnections(fkball,s = False,d = True,type = 'orientConstraint')[0]
    fkballJoint = rig.listConnections(FKballConstraint,s = False,d = True,type = 'joint')[0]
    skinJoint = rig.listRelatives(fkballJoint,p = True)[0]
    
    ikOrientConstraint = rig.listConnections(fkCon,s = False,d = True,type = 'orientConstraint')[0]
    ikfkOreint = rig.listConnections(ikOrientConstraint,s = False,d = True)[0]

            
    ikFk = rig.getAttr(sourceGrpName+'.IKFK')
    print ikFk
    
    if not (1 == ikFk): 
        fkBallRoate = rig.xform(fkball,q = True,ro = True)
              
        fkRotate = rig.xform(ikfkOreint,q = True,ro = True,ws = True)
      
        print ikPosition
        DownPos = rig.xform(ikPosition,q = True,t= True,ws = True)
        rig.xform(ikCon,t = DownPos,ws = True)
        
        movePole = rig.xform(locPos,q = True,rp = True,ws = True)
        rig.xform(poleCon,t = movePole,ws = True)
        
        IKFKAttr = rig.connectionInfo(sourceGrpName+'.IKFK',sfd = True)
        if IKFKAttr:
            rig.setAttr(IKFKAttr,1)
        else:
            rig.setAttr(sourceGrpName+'.IKFK',1)           
        
        rig.xform(ikCon,ro = fkRotate,ws = True)

        SK_IKFK_ResetValue(ikCon)
    
        loctorPosition = rig.xform(locPos,q = True,t = True,ws = True)
        rig.xform(poleCon,t = loctorPosition,ws = True)
        
        rig.setAttr(ikCon+'.swivelToe',fkBallRoate[1])
        rig.setAttr(ikCon+'.raiseToe',fkBallRoate[2])        
        
        UpAddTwist = rig.getAttr(fkUp+'.addTwist')
        UpPlacement = rig.getAttr(fkUp+'.twistPlacement')
        rig.setAttr(poleCon+'.addTwist',UpAddTwist)   
        rig.setAttr(poleCon+'.twistPlacement',UpPlacement) 
              
        print 'TO IK'
        rig.select(ikCon)

    
    else:
        ikUpRotate = rig.xform(ikJointUp,q = True,ro = True,ws = True)
        ikLoRotate = rig.getAttr(ikJointLow+'.ry')
        ikConRotate = rig.xform(skinJoint,ro = True,q = True,ws = True)
     

        FKballConstraint = rig.listConnections(fkball,s = False,d = True,type = 'orientConstraint')[0]
        fkballJoint = rig.listConnections(FKballConstraint,s = False,d = True,type = 'joint')[0]
        ballRotate = rig.xform(fkballJoint,q = True,ro = True)
        
        IKFKAttr = rig.connectionInfo(sourceGrpName+'.IKFK',sfd = True)
        if IKFKAttr:
            rig.setAttr(IKFKAttr,0)
        else:
            rig.setAttr(sourceGrpName+'.IKFK',0)  
        
        rig.xform(fkUp,ro = ikUpRotate,ws = True)
        rig.setAttr(fkLow+'.ry',ikLoRotate) 
        rig.xform(fkCon,ro = ikConRotate,ws = True)  
 
        if ArmLeg:            
            rig.setAttr(fkball+'.ry',ballRotate[1])
            rig.setAttr(fkball+'.rz',ballRotate[2])
        else:
            rig.setAttr(fkball+'.ry',0)
            rig.setAttr(fkball+'.rz',0)  
            
        
        UpAddTwist = rig.getAttr(poleCon+'.addTwist')
        UpPlacement = rig.getAttr(poleCon+'.twistPlacement')
        rig.setAttr(fkUp+'.addTwist',UpAddTwist)   
        rig.setAttr(fkUp+'.twistPlacement',UpPlacement) 
    
                  
        print 'TO FK'
        rig.select(fkCon)
    

def SK_IKFK_ResetValue(obj):
    attrs = ['roll' , 'toeLift', 'toeStraight' ,'raiseToe' ,'swivelToe' ,'raiseToeTip','swivelToeTip','side','swivel', 'raiseBall', 'swivelBall', 'raiseHeel' ,'swivelHee']
    fillterAttr = [attr for attr in attrs if(rig.attributeQuery(attr,node = obj,ex = True))]
    if fillterAttr:
        for attr in fillterAttr:
            if('toeLift' == attr):
                rig.setAttr(obj+'.'+attr,30)
            elif('toeStraight' == attr):
                rig.setAttr(obj+'.'+attr,60)
            else:
                rig.setAttr(obj+'.'+attr,0)
 
 
def SK_IKToLockSwithCon(selCtrl):
    poleCon = ''
    switchCon = ''
    jnts = ''
    
    sourceGrp = rig.connectionInfo(selCtrl+'.ctrl', sfd=True)
    sourceGrpName = sourceGrp.split('.')[0]
    allCtrls = [i.split('.')[0] for i in rig.connectionInfo(sourceGrp, dfs=True)]
    for nurbsControl in allCtrls:
        if('_Pole_ctrl' in nurbsControl):
            poleCon = nurbsControl
            
        if('_Switch' in nurbsControl):
            switchCon = nurbsControl    
        
        if(rig.nodeType(nurbsControl) == 'joint'):
            jnts = rig.listRelatives(nurbsControl,c = True)[0]
        
        
    selAttr = rig.getAttr(poleCon+'.follow')

    if (1 == selAttr):
        polePos = rig.xform(jnts,q = True,t = True,ws = True)
        upLen = rig.getAttr(sourceGrpName+'.outUpSize')
        lowLen = rig.getAttr(sourceGrpName+'.outLowSize')
        origUpLen = rig.getAttr(sourceGrpName+'.upSize')
        origLowLen = rig.getAttr(sourceGrpName+'.lowSize')        
        
        if('Leg' in poleCon):
            rig.setAttr(poleCon+'.follow',2)
            rig.xform(poleCon,t = polePos,ws = True) 
            
        else:
            rig.setAttr(poleCon+'.follow',2)
            rig.xform(poleCon,t = polePos,ws = True)     
            
        currentUpLen = (upLen - origUpLen)*10
        currentLowLen = (lowLen - origLowLen)*10
        if('Rt' in sourceGrpName.split('_')[0]):
            currentUpLen = currentUpLen*-1
            currentLowLen = currentLowLen*-1
            
        rig.setAttr(switchCon+'.Stretch',0)
        rig.setAttr(switchCon+'.KneeSlide',0)        
        
        rig.setAttr(switchCon+'.UpLegth',currentUpLen)
        rig.setAttr(switchCon+'.LowLength',currentLowLen)
    
        
        
    else:
        polePos = rig.xform(jnts,q = True,t = True,ws = True)      
        
        rig.setAttr(poleCon+'.follow',1)
        rig.xform(poleCon,t = polePos,ws = True)      
        
        rig.setAttr(switchCon+'.UpLegth',0)
        rig.setAttr(switchCon+'.LowLength',0) 
        rig.setAttr(switchCon+'.Stretch',0)
        rig.setAttr(switchCon+'.KneeSlide',0)                



def SK_IKFKSwitchCommand():
    selObjs = rig.ls(sl = True)
    if(selObjs):
        for switchObj in selObjs:      
            objNurbs = switchObj
            nurbsCurve = rig.listRelatives(objNurbs,s = True)
            if(nurbsCurve):
                if('nurbsCurve' == rig.nodeType(nurbsCurve[0]) and rig.attributeQuery('ctrl',node = objNurbs,ex = True)):
                    if ('_IKFK_blendCon' in rig.connectionInfo(objNurbs+'.ctrl', sfd=True)):
                        if ('_Pole_ctrl' in objNurbs):
                            SK_IKToLockSwithCon(objNurbs)
                        else:
                            SK_IKFKSwithCon(objNurbs)
                else:
                    mel.eval('source "Z:/Resource/Support/OEM/2013/woAnimTsmIKFKSwitch.mel"')
                    mel.eval('woAnimTsmIKFKSwitch()')
                            
                            
#      *****************************************
def SK_creatConDefaultPos(savePos = True):
    filePath = tempfile.gettempdir()+'/PosFile.txt'
    if savePos:
        cons = rig.sets('bodySet',q = True)
        posData = []
        for con in cons:
            temPosData = []
            attrs = rig.listAttr(con,k = True)
            kattrs = rig.listAttr(con,cb = True)
            
            if kattrs:
                attrs.extend(kattrs)
            
            for attr in attrs:
                temAttrPosData = []
                datainfo = rig.getAttr(con+'.'+attr)
                temAttrPosData.append(con+'.'+attr)
                temAttrPosData.append(datainfo) 
                temPosData.append(temAttrPosData)                
            posData.append(temPosData) 
            
        newFile = open(filePath,'w')
        pickle.dump(posData,newFile)
        newFile.close()
        getData = open(filePath,'r')
        getDate = getData.read()
        getData.close()
        if not (rig.attributeQuery('conPos',node = 'CharacterShape',ex = True)):
            rig.addAttr('CharacterShape',ln = 'conPos',dt = 'string')
        rig.setAttr('CharacterShape.conPos',getDate,type = 'string')
        os.remove(filePath)    
        
    else:
        selControlers = rig.ls(sl = True)
        if selControlers:
            for slCon in selControlers:
                temPrefix = slCon.split(':')
                if (1 == len(temPrefix)):
                    prefix = ''
                else:
                    prefix = slCon.replace(temPrefix[-1],'')  
                          
                newFile = open(filePath,'w')
                newFile.write(rig.getAttr(prefix+'CharacterShape.conPos'))
                newFile.close()
                readFile = open(filePath,'r')
                posData = pickle.load(readFile)
                readFile.close()
                os.remove(filePath)
                for data in posData:
                    for attrdata in data:
                        rig.setAttr(prefix+attrdata[0],attrdata[1])  

def SK_IDMTAnimRigUI():
    IDMTRigGUI='autoAnim'
    if rig.window(IDMTRigGUI,exists=True):
        rig.deleteUI(IDMTRigGUI)
    rig.window(IDMTRigGUI,title='IDMT 2009 Anim',menuBar=True,wh=  (400,500),minimizeButton=True,maximizeButton=True)
    rig.columnLayout()
    rig.button(l = u'环球IKFK切换',w = 80,c = 'SK_IKFKSwitchCommand()')
    rig.button(l = u'恢复初始pose',w = 80,c = 'SK_creatConDefaultPos(False)')
    rig.button(l = u'北极熊项目IKFK切换',w = 120,c = 'North_IKFKSwitch()')    
    rig.window(IDMTRigGUI,e=True,wh=(80,100))
    rig.showWindow(IDMTRigGUI)    

SK_IDMTAnimRigUI()

def North_IKFKSwitch():
    selectCtrls = rig.ls(sl=1)
    for selectCtrl in selectCtrls:
        prefix = selectCtrl.split(':')
        TheNameSpace=""
        
        if len(prefix)>1:
            for i in range(len(prefix)-1):
                TheNameSpace=TheNameSpace+prefix[i]+":"
        
        if len(prefix)==1:
            TheNameSpace=""    
        
        if selectCtrl==TheNameSpace+'IKCurveArm_L' or selectCtrl==TheNameSpace+'IKPoleVectorCurveArm_L':
            #左臂IK => FK
            IKShoulder_L = rig.xform(TheNameSpace+"IKShoulder_L",q = True,ro = True,ws = True)
            IKElbow_L = rig.xform(TheNameSpace+"IKElbow_L",q = True,ro = True,ws = True)
            IKWrist_L = rig.xform(TheNameSpace+"IKWrist_L",q = True,ro = True,ws = True)
            rig.setAttr(TheNameSpace+'FKIK_Switch_Arm_L.FKIKBlend',0)
            rig.xform(TheNameSpace+"FKCurveShoulder_L",ro = IKShoulder_L,ws = True)
            rig.xform(TheNameSpace+"FKCurveElbow_L",ro = IKElbow_L,ws = True)
            rig.xform(TheNameSpace+"FKCurveWrist_L",ro = IKWrist_L,ws = True)
            rig.select(TheNameSpace+'FKCurveWrist_L')
        if selectCtrl==TheNameSpace+'FKCurveWrist_L' or selectCtrl==TheNameSpace+'FKCurveElbow_L' or selectCtrl==TheNameSpace+'FKCurveShoulder_L':
            #左臂FK => IK
            LfArm_Wrist_FK_T = rig.xform(TheNameSpace+"IKCurveArm_L_Locator",q = True,t = True,ws = True)
            LfArm_Wrist_FK_R = rig.xform(TheNameSpace+"IKCurveArm_L_Locator",q = True,ro = True,ws = True)
            Locator = rig.xform(TheNameSpace+"FKPoleVectorCurveArm_L",q = True,t = True,ws = True)
            rig.setAttr(TheNameSpace+'FKIK_Switch_Arm_L.FKIKBlend',10)
            rig.setAttr(TheNameSpace+'FKCurveWrist_L.rotate',0,0,0)
            rig.xform(TheNameSpace+"IKCurveArm_L",t = LfArm_Wrist_FK_T,ws = True)
            rig.xform(TheNameSpace+"IKCurveArm_L",ro = LfArm_Wrist_FK_R,ws = True)
            #rig.xform("IKCurveArm_L",ro = (-LfArm_Wrist_FK_R[0],-LfArm_Wrist_FK_R[1]+0.39,LfArm_Wrist_FK_R[2]-180.11),ws = True)
            rig.xform(TheNameSpace+"IKPoleVectorCurveArm_L",t = Locator,ws = True)
            rig.select(TheNameSpace+'IKCurveArm_L')       
        if selectCtrl==TheNameSpace+'IKCurveArm_R' or selectCtrl==TheNameSpace+'IKPoleVectorCurveArm_R':
            #右臂IK => FK
            IKShoulder_R = rig.xform(TheNameSpace+"IKShoulder_R",q = True,ro = True,ws = True)
            IKElbow_R = rig.xform(TheNameSpace+"IKElbow_R",q = True,ro = True,ws = True)
            IKWrist_R = rig.xform(TheNameSpace+"IKWrist_R",q = True,ro = True,ws = True)
            rig.setAttr(TheNameSpace+'FKIK_Switch_Arm_R.FKIKBlend',0)
            rig.xform(TheNameSpace+"FKCurveShoulder_R",ro = IKShoulder_R,ws = True)
            rig.xform(TheNameSpace+"FKCurveElbow_R",ro = IKElbow_R,ws = True)
            rig.xform(TheNameSpace+"FKCurveWrist_R",ro = IKWrist_R,ws = True)
            rig.select(TheNameSpace+'FKCurveWrist_R')
        if selectCtrl==TheNameSpace+'FKCurveWrist_R' or selectCtrl==TheNameSpace+'FKCurveElbow_R' or selectCtrl==TheNameSpace+'FKCurveShoulder_R':
            #右臂FK => IK
            RtArm_Wrist_FK_T = rig.xform(TheNameSpace+"IKCurveArm_R_Locator",q = True,t = True,ws = True)
            RtArm_Wrist_FK_R = rig.xform(TheNameSpace+"IKCurveArm_R_Locator",q = True,ro = True,ws = True)
            Locator = rig.xform(TheNameSpace+"FKPoleVectorCurveArm_R",q = True,t = True,ws = True)
            rig.setAttr(TheNameSpace+'FKIK_Switch_Arm_R.FKIKBlend',10)
            rig.setAttr(TheNameSpace+'FKCurveWrist_R.rotate',0,0,0)
            rig.xform(TheNameSpace+"IKCurveArm_R",t = RtArm_Wrist_FK_T,ws = True)
            rig.xform(TheNameSpace+"IKCurveArm_R",ro = RtArm_Wrist_FK_R,ws = True)
            rig.xform(TheNameSpace+"IKPoleVectorCurveArm_R",t = Locator,ws = True)
            rig.select(TheNameSpace+'IKCurveArm_R')
           
        if selectCtrl==TheNameSpace+'IKCurveLeg_L' or selectCtrl==TheNameSpace+'IKPoleVectorCurveLeg_L':
            #左腿IK => FK
            IKHip_L = rig.xform(TheNameSpace+"IKHip_L",q = True,ro = True,ws = True)
            IKKnee_L = rig.xform(TheNameSpace+"IKKnee_L",q = True,ro = True,ws = True)
            IKAnkle_L = rig.xform(TheNameSpace+"IKAnkle_L",q = True,ro = True,ws = True)
            IKMiddleToe1_L = rig.xform(TheNameSpace+"IKMiddleToe1_L",q = True,ro = True,ws = True)
            rig.setAttr(TheNameSpace+'FKIK_Switch_Leg_L.FKIKBlend',0)
            rig.xform(TheNameSpace+"FKCurveHip_L",ro = IKHip_L,ws = True)
            rig.xform(TheNameSpace+"FKCurveKnee_L",ro = IKKnee_L,ws = True)
            rig.xform(TheNameSpace+"FKCurveAnkle_L",ro = IKAnkle_L,ws = True)
            rig.xform(TheNameSpace+"FKCurveMiddleToe1_L",ro = IKMiddleToe1_L,ws = True)
            rig.select(TheNameSpace+'FKCurveAnkle_L')
               
        if selectCtrl==TheNameSpace+'FKCurveAnkle_L' or selectCtrl==TheNameSpace+'FKCurveKnee_L' or selectCtrl==TheNameSpace+'FKCurveHip_L':
            #左腿FK => IK
            AlignIKToAnkle_L_T = rig.xform(TheNameSpace+"AlignIKToAnkle_L",q = True,t = True,ws = True)
            AlignIKToAnkle_L_R = rig.xform(TheNameSpace+"AlignIKToAnkle_L",q = True,ro = True,ws = True)
            Locator = rig.xform(TheNameSpace+"FKPoleVectorCurveLeg_L",q = True,t = True,ws = True)
            rig.setAttr(TheNameSpace+'FKIK_Switch_Leg_L.FKIKBlend',10)
            rig.setAttr(TheNameSpace+'FKCurveAnkle_L.rotate',0,0,0)
            rig.xform(TheNameSpace+"IKCurveLeg_L",t = AlignIKToAnkle_L_T,ws = True)
            rig.xform(TheNameSpace+"IKCurveLeg_L",ro = AlignIKToAnkle_L_R,ws = True)
            rig.xform(TheNameSpace+"IKPoleVectorCurveLeg_L",t = Locator,ws = True)
            rig.select(TheNameSpace+'IKCurveLeg_L')
            rig.setAttr(TheNameSpace+'IKCurveLeg_L.roll',0)
            rig.setAttr(TheNameSpace+'IKCurveLeg_L.toeTap',0)
            rig.setAttr(TheNameSpace+'IKCurveLeg_L.toeLift',0)
            rig.setAttr(TheNameSpace+'IKCurveLeg_L.lean',0)
            rig.setAttr(TheNameSpace+'IKCurveLeg_L.toeTwist',0)
            rig.setAttr(TheNameSpace+'IKCurveLeg_L.toeLean',0)
            rig.setAttr(TheNameSpace+'IKCurveLeg_L.toeSpin',0)
            rig.setAttr(TheNameSpace+'IKCurveLeg_L.side',0)
            rig.setAttr(TheNameSpace+'IKCurveLeg_L.heelSpin',0)
            
        if selectCtrl==TheNameSpace+'IKCurveLeg_R' or selectCtrl==TheNameSpace+'IKPoleVectorCurveLeg_R':
            #右腿IK => FK
            IKHip_R = rig.xform(TheNameSpace+"IKHip_R",q = True,ro = True,ws = True)
            IKKnee_R = rig.xform(TheNameSpace+"IKKnee_R",q = True,ro = True,ws = True)
            IKAnkle_R = rig.xform(TheNameSpace+"IKAnkle_R",q = True,ro = True,ws = True)
            IKMiddleToe1_R = rig.xform(TheNameSpace+"IKMiddleToe1_R",q = True,ro = True,ws = True)
            rig.setAttr(TheNameSpace+'FKIK_Switch_Leg_R.FKIKBlend',0)
            rig.xform(TheNameSpace+"FKCurveHip_R",ro = IKHip_R,ws = True)
            rig.xform(TheNameSpace+"FKCurveKnee_R",ro = IKKnee_R,ws = True)
            rig.xform(TheNameSpace+"FKCurveAnkle_R",ro = IKAnkle_R,ws = True)
            rig.xform(TheNameSpace+"FKCurveMiddleToe1_R",ro = IKMiddleToe1_R,ws = True)
            rig.select(TheNameSpace+'FKCurveAnkle_R')
               
        if selectCtrl==TheNameSpace+'FKCurveAnkle_R' or selectCtrl==TheNameSpace+'FKCurveKnee_R' or selectCtrl==TheNameSpace+'FKCurveHip_R':
            #右腿FK => IK
            AlignIKToAnkle_R_T = rig.xform(TheNameSpace+"AlignIKToAnkle_R",q = True,t = True,ws = True)
            AlignIKToAnkle_R_R = rig.xform(TheNameSpace+"AlignIKToAnkle_R",q = True,ro = True,ws = True)
            Locator = rig.xform(TheNameSpace+"FKPoleVectorCurveLeg_R",q = True,t = True,ws = True)
            rig.setAttr(TheNameSpace+'FKIK_Switch_Leg_R.FKIKBlend',10)
            rig.setAttr(TheNameSpace+'FKCurveAnkle_R.rotate',0,0,0)
            rig.xform(TheNameSpace+"IKCurveLeg_R",t = AlignIKToAnkle_R_T,ws = True)
            rig.xform(TheNameSpace+"IKCurveLeg_R",ro = AlignIKToAnkle_R_R,ws = True)
            rig.xform(TheNameSpace+"IKPoleVectorCurveLeg_R",t = Locator,ws = True)
            rig.select(TheNameSpace+'IKCurveLeg_R')
            rig.setAttr(TheNameSpace+'IKCurveLeg_R.roll',0)
            rig.setAttr(TheNameSpace+'IKCurveLeg_R.toeTap',0)
            rig.setAttr(TheNameSpace+'IKCurveLeg_R.toeLift',0)
            rig.setAttr(TheNameSpace+'IKCurveLeg_R.lean',0)
            rig.setAttr(TheNameSpace+'IKCurveLeg_R.toeTwist',0)
            rig.setAttr(TheNameSpace+'IKCurveLeg_R.toeLean',0)
            rig.setAttr(TheNameSpace+'IKCurveLeg_R.toeSpin',0)
            rig.setAttr(TheNameSpace+'IKCurveLeg_R.side',0)
            rig.setAttr(TheNameSpace+'IKCurveLeg_R.heelSpin',0)              