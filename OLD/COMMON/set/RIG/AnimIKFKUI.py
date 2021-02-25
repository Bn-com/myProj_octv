# -*- coding: utf-8 -*-
import maya.cmds as rig
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
    rig.button(l = u'IKFK切换',w = 80,c = 'SK_IKFKSwitchCommand()')
    rig.button(l = u'恢复初始pose',w = 80,c = 'SK_creatConDefaultPos(False)')
    rig.window(IDMTRigGUI,e=True,wh=(80,100))
    rig.showWindow(IDMTRigGUI)    

SK_IDMTAnimRigUI()

