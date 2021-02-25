# Name:"GDC IK/FK for Calimero" 
# Author:GDC(Idmt)
# Time:2012.11.23
# 版权所有 请勿转载
# -*- coding: utf-8 -*-
import maya.cmds as rig
import os
import pickle
import tempfile

def Calimero_IKFKSwithCon(obj):
    #obj='LfArm_Wrist_FK'
    selCtrl = obj
    sourceGrp = rig.connectionInfo(selCtrl+'.ctrl', sfd=True)
    sourceGrpName = sourceGrp.split('.')[0]
    allCtrls = [i.split('.')[0] for i in rig.connectionInfo(sourceGrp, dfs=True)]
    
    ns=Calimero_getNamespace(selCtrl)
    calimerofeetrig=ns+'GRP_calimeroFeetRigging'
    
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

        Calimero_IKFK_ResetValue(ikCon)
    
        loctorPosition = rig.xform(locPos,q = True,t = True,ws = True)
        rig.xform(poleCon,t = loctorPosition,ws = True)
        
        UpAddTwist = rig.getAttr(fkUp+'.addTwist')
        UpPlacement = rig.getAttr(fkUp+'.twistPlacement')
        rig.setAttr(poleCon+'.addTwist',UpAddTwist)   
        rig.setAttr(poleCon+'.twistPlacement',UpPlacement)
        
        if ArmLeg:
            if rig.objExists(calimerofeetrig):
                rig.setAttr(ikCon+'.Open_Toe',rig.getAttr(fkCon+'.Open_Toe'))
                rig.setAttr(ikCon+'.RaiseToe',rig.getAttr(fkCon+'.RaiseToe'))
                rig.setAttr(ikCon+'.SwivelToe',rig.getAttr(fkCon+'.SwivelToe'))
                rig.setAttr(ikCon+'.original_swivelToe',fkBallRoate[1])
                rig.setAttr(ikCon+'.original_raistToe',fkBallRoate[2])
            else:
                rig.setAttr(ikCon+'.swivelToe',fkBallRoate[1])
                rig.setAttr(ikCon+'.raiseToe',fkBallRoate[2])
        else:
            rig.setAttr(ikCon+'.swivelToe',fkBallRoate[1])
            rig.setAttr(ikCon+'.raiseToe',fkBallRoate[1])
              
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
            if rig.objExists(calimerofeetrig):
                rig.setAttr(fkCon+'.Open_Toe',rig.getAttr(ikCon+'.Open_Toe'))
                rig.setAttr(fkCon+'.RaiseToe',rig.getAttr(ikCon+'.RaiseToe'))
                rig.setAttr(fkCon+'.SwivelToe',rig.getAttr(ikCon+'.SwivelToe'))
        else:
            rig.setAttr(fkball+'.ry',0)
            rig.setAttr(fkball+'.rz',0)  
            
        
        UpAddTwist = rig.getAttr(poleCon+'.addTwist')
        UpPlacement = rig.getAttr(poleCon+'.twistPlacement')
        rig.setAttr(fkUp+'.addTwist',UpAddTwist)   
        rig.setAttr(fkUp+'.twistPlacement',UpPlacement) 
    
                  
        print 'TO FK'
        rig.select(fkCon)
    
def Calimero_getNamespace(obj):
    #obj='aa:bb:cc:dd'
    list=obj.split(':')
    ns=''
    for i in range(0,len(list)-1):
        ns=ns+list[i]+':'
    print ns
    return ns
        

def Calimero_IKFK_ResetValue(obj):
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
 
 
def Calimero_IKToLockSwithCon(selCtrl):
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



def Calimero_IKFKSwitchCommand():
    selObjs = rig.ls(sl = True)
    if(selObjs):
        for switchObj in selObjs:      
            objNurbs = switchObj
            nurbsCurve = rig.listRelatives(objNurbs,s = True)
            if(nurbsCurve):
                if('nurbsCurve' == rig.nodeType(nurbsCurve[0]) and rig.attributeQuery('ctrl',node = objNurbs,ex = True)):
                    if ('_IKFK_blendCon' in rig.connectionInfo(objNurbs+'.ctrl', sfd=True)):
                        if ('_Pole_ctrl' in objNurbs):
                            Calimero_IKToLockSwithCon(objNurbs)
                        else:
                            Calimero_IKFKSwithCon(objNurbs)
                            
                            
#      *****************************************
def Calimero_creatConDefaultPos(savePos = True):
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

def Calimero_GDCAnimRigUI():
    GDCRigGUI='autoAnim'
    if rig.window(GDCRigGUI,exists=True):
        rig.deleteUI(GDCRigGUI)
    rig.window(GDCRigGUI,title='GDC IK/FK for Calimero',menuBar=True,w=170,h=130,minimizeButton=True,maximizeButton=True)
    rig.columnLayout(rs=6,columnAttach=('both',10),w=170,h=130,)
    rig.text ("",h=2,)
    rig.button(l = u'IK/FK_Switch', w=150,h=40,c = 'Calimero_IKFKSwitchCommand()')
    rig.button(l = u'ik/fk Start_Pose', w=150,h=32.5,c = 'Calimero_creatConDefaultPos(False)')
    rig.text(l = "Presents by GDC",w=150,h=10,)
    rig.text(l = "GDC-IDMT 2012 (C)\n",w=150,h=10,)
    rig.window(GDCRigGUI,e=True,w=170,h=130,)
    rig.showWindow(GDCRigGUI)    

Calimero_GDCAnimRigUI()