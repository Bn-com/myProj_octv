#-*- coding: utf-8 -*-
import maya.cmds as rig
from RIG.commonly.base import *
from RIG.nurbsCurveCon import *
import math


def SK_createLegSetupNode(prefix,startJoint,endJoint,ikCon,fkCon,ikfk,ikfkReverse,XYZ,distanceA,distanceB,distanceAB):
#===============================================================================
#    createAttr
#===============================================================================
    plugNodes = []
    attrName = ['Stretch','KneeSlide','UpLegth','LowLength']
    for attr in attrName:
         rig.addAttr(ikfk,ln = attr,at = 'float',k = True)
         plugNodes.append(ikfk+'.'+attr)

    plugNodes.append(ikfk+'.AutoStretch')
    plugNodes.append(ikCon+'.LockKnee')
    
    kneeTx = rig.getAttr(startJoint+'.'+XYZ)
    ankleTx = rig.getAttr(endJoint+'.'+XYZ)
#   将骨骼的初始长度放到FK控制器上，主要用于IK 到 LOCK 的切换。
    rig.addAttr(ikfk,ln = 'upSize',at = 'float',dv = kneeTx)
    rig.addAttr(ikfk,ln = 'lowSize',at = 'float',dv = ankleTx)  

      
    stretch = plugNodes[0]
    kneeSlide = plugNodes[1]
    upLength = plugNodes[2]    
    lowLength = plugNodes[3]
    autoStretch = plugNodes[4]
    lockKnee = plugNodes[5]  
     
    #create Plug-nodes
    scaleValue = rig.createNode('multiplyDivide',n = prefix+'_MD',ss = True)
    scaleNum = kneeTx + ankleTx
    rig.setAttr(scaleValue+'.input1X',scaleNum)
    rig.setAttr(scaleValue+'.input1X',0.1)
   
    
#   Axis X
    if(kneeTx < 0):
         stretchNagativeMD = rig.createNode('multiplyDivide',n = prefix+'_MD',ss = True)
         rig.setAttr(stretchNagativeMD+'.input1X',-1)
         rig.connectAttr(stretch,stretchNagativeMD+'.input2X')
         stretch = stretchNagativeMD+'.outputX'
         
         kneeSlideNagativeMD = rig.createNode('multiplyDivide',n = prefix+'_MD',ss = True)
         rig.setAttr(kneeSlideNagativeMD+'.input1X',-1)
         rig.connectAttr(kneeSlide,kneeSlideNagativeMD+'.input2X')
         kneeSlide = kneeSlideNagativeMD+'.outputX'
         
         upLengthNagativeMD = rig.createNode('multiplyDivide',n = prefix+'_MD',ss = True)
         rig.setAttr(upLengthNagativeMD+'.input1X',-1)
         rig.connectAttr(upLength,upLengthNagativeMD+'.input2X')
         upLength = upLengthNagativeMD+'.outputX'
         
         lowLengthNagativeMD = rig.createNode('multiplyDivide',n = prefix+'_MD',ss = True)
         rig.setAttr(lowLengthNagativeMD+'.input1X',-1)
         rig.connectAttr(lowLength,lowLengthNagativeMD+'.input2X')
         lowLength= lowLengthNagativeMD+'.outputX'
    
    
#===============================================================================
#    createNode    
#===============================================================================
    UpLengthMD = rig.createNode('multiplyDivide',n = prefix+'_MD',ss = True)
    rig.connectAttr(scaleValue+'.output',UpLengthMD+'.input1')
    rig.connectAttr(upLength,UpLengthMD+'.input2X')
        
    LowLengthMD = rig.createNode('multiplyDivide',n = prefix+'_MD',ss = True)
    rig.connectAttr(scaleValue+'.output',LowLengthMD+'.input1')
    rig.connectAttr(lowLength,LowLengthMD+'.input2X')
    
    UpLengthPMA = rig.createNode('plusMinusAverage',n = prefix+'_PMA',ss = True)
    rig.connectAttr(UpLengthMD+'.outputX',UpLengthPMA+'.input1D[0]')
    rig.setAttr(UpLengthPMA+'.input1D[1]',kneeTx)
        
    LowLengthPMA = rig.createNode('plusMinusAverage',n = prefix+'_PMA',ss = True)
    rig.connectAttr(LowLengthMD+'.outputX',LowLengthPMA+'.input1D[0]')
    rig.setAttr(LowLengthPMA+'.input1D[1]',ankleTx)
    
    UpStretchMPA = rig.createNode('plusMinusAverage',n = prefix+'_PMA',ss = True)
    rig.connectAttr(UpLengthPMA+'.output1D',UpStretchMPA+'.input1D[0]')
    rig.connectAttr(stretch,UpStretchMPA+'.input1D[1]')
        
    LowStretchMPA = rig.createNode('plusMinusAverage',n = prefix+'_PMA',ss = True)
    rig.connectAttr(LowLengthPMA+'.output1D',LowStretchMPA+'.input1D[0]')
    rig.connectAttr(stretch,LowStretchMPA+'.input1D[1]')
    
    stretchCondition = rig.createNode('condition',n = prefix+'_CDT',ss = True)  
    rig.setAttr(stretchCondition+'.colorIfFalseR',1)
    rig.setAttr(stretchCondition+'.operation',2)
    
    StretchDistanceMD = rig.createNode('multiplyDivide',n = prefix+'_MD',ss = True)   
    rig.connectAttr(distanceAB+'.distance',StretchDistanceMD+'.input1X')
    rig.setAttr(StretchDistanceMD+'.operation',2)
     
    AutoStretchMD = rig.createNode('multiplyDivide',n = prefix+'_MD',ss = True)
    rig.connectAttr(StretchDistanceMD+'.output',AutoStretchMD+'.input2')
    rig.connectAttr(autoStretch,AutoStretchMD+'.input1X')
    
    rig.connectAttr(AutoStretchMD+'.outputX',stretchCondition+'.colorIfTrueR')
    rig.connectAttr(AutoStretchMD+'.outputX',stretchCondition+'.firstTerm')
    rig.setAttr(stretchCondition+'.secondTerm',1)
    
    UpAutoStretchValueMD = rig.createNode('multiplyDivide',n = prefix+'_MD',ss = True)
    rig.connectAttr(stretchCondition+'.outColorR',UpAutoStretchValueMD+'.input1X')

        
    LowAutoStretchValueMD = rig.createNode('multiplyDivide',n = prefix+'_MD',ss = True)
    rig.connectAttr(stretchCondition+'.outColorR',LowAutoStretchValueMD+'.input1X')
  
    
    KneeSildeMD = rig.createNode('multiplyDivide',n = prefix+'_MD',ss = True)
    rig.connectAttr(scaleValue+'.output',KneeSildeMD+'.input1')
    rig.connectAttr(kneeSlide,KneeSildeMD+'.input2X')

    UnKneeSildeMD = rig.createNode('multiplyDivide',n = prefix+'_MD',ss = True)
    rig.connectAttr(KneeSildeMD+'.output',UnKneeSildeMD+'.input1')
    rig.setAttr(UnKneeSildeMD+'.input2X',-1) 
    
    UpKneeSildeMPA = rig.createNode('plusMinusAverage',n = prefix+'_PMA',ss = True)
    rig.connectAttr(KneeSildeMD+'.outputX',UpKneeSildeMPA+'.input1D[0]')
    rig.connectAttr(UpStretchMPA+'.output1D',UpKneeSildeMPA+'.input1D[1]')
    
    LowKneeSildeMPA = rig.createNode('plusMinusAverage',n = prefix+'_PMA',ss = True)
    rig.connectAttr(UnKneeSildeMD+'.outputX',LowKneeSildeMPA+'.input1D[0]')
    rig.connectAttr(LowStretchMPA+'.output1D',LowKneeSildeMPA+'.input1D[1]')
    
    rig.connectAttr(UpKneeSildeMPA+'.output1D',UpAutoStretchValueMD+'.input2X')
    rig.connectAttr(LowKneeSildeMPA+'.output1D',LowAutoStretchValueMD+'.input2X')
    
    UPLowPlus = rig.createNode('plusMinusAverage',n = prefix+'_PMA',ss = True)
    rig.connectAttr(UpKneeSildeMPA+'.output1D',UPLowPlus+'.input1D[0]')
    rig.connectAttr(LowKneeSildeMPA+'.output1D',UPLowPlus+'.input1D[1]')
    
    UpBlendBC = rig.createNode('blendColors',n = prefix+'_BCS',ss = True)
    rig.connectAttr(UpAutoStretchValueMD+'.output',UpBlendBC+'.color2')
    rig.connectAttr(distanceA+'.distance',UpBlendBC+'.color1R')
    rig.connectAttr(lockKnee,UpBlendBC+'.blender')
    
    LowBlendBC = rig.createNode('blendColors',n = prefix+'_BCS',ss = True)
    rig.connectAttr(LowAutoStretchValueMD+'.output',LowBlendBC+'.color2')
    rig.connectAttr(distanceB+'.distance',LowBlendBC+'.color1R')
    rig.connectAttr(lockKnee,LowBlendBC+'.blender')
    
    

    rig.connectAttr(UPLowPlus+'.output1D',StretchDistanceMD+'.input2X')
    rig.connectAttr(UpBlendBC+'.outputR',startJoint+'.'+XYZ)
    rig.connectAttr(LowBlendBC+'.outputR',endJoint+'.'+XYZ)

#   在FK控制器上增加两个属性，用于存储缩放后骨骼的长度
    rig.addAttr(ikfk,ln = 'outUpSize',at = 'float',k = True)
    rig.addAttr(ikfk,ln = 'outLowSize',at = 'float',k = True)
    rig.connectAttr(UpBlendBC+'.outputR',ikfk+'.outUpSize')
    rig.connectAttr(LowBlendBC+'.outputR',ikfk+'.outLowSize')   
    
    if(kneeTx < 0):
        UnDistanceAMD = rig.createNode('multiplyDivide',n = prefix+'_MD')
        rig.connectAttr(distanceA+'.distance',UnDistanceAMD+'.input1X')
        rig.setAttr(UnDistanceAMD+'.input2X',-1)
        rig.connectAttr(UnDistanceAMD+'.outputX',UpBlendBC+'.color1R',f = True)
        
        UnDistanceBMD = rig.createNode('multiplyDivide',n = prefix+'_MD')
        rig.connectAttr(distanceB+'.distance',UnDistanceBMD+'.input1X')
        rig.setAttr(UnDistanceBMD+'.input2X',-1)
        rig.connectAttr(UnDistanceBMD+'.outputX',LowBlendBC+'.color1R',f = True)
        
        UnDistanceABMD = rig.createNode('multiplyDivide',n = prefix+'_MD')
        rig.connectAttr(distanceAB+'.distance',UnDistanceABMD+'.input1X')
        rig.setAttr(UnDistanceABMD+'.input2X',-1)
        rig.connectAttr(UnDistanceABMD+'.outputX',StretchDistanceMD+'.input1X',f = True)
 

def SK_createLeg(jntObj):
    jointListName = ['_jnt','_jnt_IK','_jnt_FK']
    controlCurveName = ['_Leg_FK','_Knee_FK','_Ankle_FK','_Leg_IK']
    legHeelPointer = '_heel_drv'
    
    origeJoints = []
    inputJoint = jntObj
    leg = inputJoint
    
    if('Arm_' in leg):
       controlCurveName = ['_UpArm_FK','_Elbow_FK','_Wrist_FK','_Wrist_IK'] 
    origeJoints.append(leg)
    knee = rig.listRelatives(leg,c = True)[0]
    origeJoints.append(knee)
    ankle = rig.listRelatives(knee,c = True)[0]
    origeJoints.append(ankle)
    
#    get leg Position
    legPos = []
    legPos.append(rig.xform(leg,q = True,ws = True,rp = True))
    legPos.append(rig.xform(knee,q = True,ws = True,rp = True))    
    legPos.append(rig.xform(ankle,q = True,ws = True,rp = True))   
    
    
#    create IK and FK Joint
    skJoints = SK_duplicateJoint(origeJoints,jointListName[0])
    ikJoints = SK_duplicateJoint(origeJoints,jointListName[1])
    fkJoints = SK_duplicateJoint(origeJoints,jointListName[2])
    
    prefix = origeJoints[0]
    prefixName = origeJoints[0].split('_')[0]+'Leg'
    if('Arm_' in leg):
       prefixName = origeJoints[0].split('_')[0]+'Arm'
    
#    create constraint
    jntConstraints = []
    conIkBlendGrp = rig.group(empty = True,n = prefixName+'_IKFK_blendCon')
    rig.addAttr(conIkBlendGrp,ln = 'toeLift',at = 'float',dv = 30,k = True)
    rig.addAttr(conIkBlendGrp,ln = 'toeStraight',at = 'float',dv = 60,k = True)
    rig.addAttr(conIkBlendGrp,ln = 'ctrl',at = 'float',min = 0,max = 1, dv = 1) 
    rig.addAttr(conIkBlendGrp,ln = 'AutoStretch',at = 'float',min = 0,max = 1, dv = 0)      
    rig.addAttr(conIkBlendGrp,ln = 'IKFK_vis',at = 'float',min = 0,max = 1, dv = 0,k = True)
    rig.addAttr(conIkBlendGrp,ln = 'IKFKBlend',at = 'float',min = 0,max = 1, dv = 0,k = True)
    rig.addAttr(conIkBlendGrp,ln = 'IKFK',at = 'bool', dv = 0,k = True) 
    rig.connectAttr(conIkBlendGrp+'.IKFK',conIkBlendGrp+'.IKFKBlend')  
    rig.connectAttr(conIkBlendGrp+'.IKFK',conIkBlendGrp+'.IKFK_vis')   
    
    rig.addAttr(ikJoints[0],ln = 'ctrl',at = 'float',min = 0,max = 1, dv = 1,k = True)
    rig.connectAttr(conIkBlendGrp+'.ctrl',ikJoints[0]+'.ctrl')     
    reverseNode = rig.createNode('reverse',n = prefixName+'_RV')
    rig.connectAttr(conIkBlendGrp+'.IKFKBlend',reverseNode+'.inputX')
    SK_snapToObj(skJoints[0],conIkBlendGrp)
    for i,jnt in enumerate(ikJoints):
#        JointIKFKConstraint = rig.orientConstraint(ikJoints[i],fkJoints[i],skJoints[i])[0]
#        jntConstraints.append(JointIKFKConstraint)
#        rig.connectAttr(conIkBlendGrp+'.IKFKBlend',JointIKFKConstraint+'.'+ikJoints[i]+'W0')
#        rig.connectAttr(reverseNode+'.outputX',JointIKFKConstraint+'.'+fkJoints[i]+'W1') 
        
        blendColor = rig.createNode('pairBlend',n =  prefixName+'_PB')
        rig.connectAttr(reverseNode+'.outputX',blendColor+'.weight') 
        rig.connectAttr(ikJoints[i]+'.translate',blendColor+'.inTranslate1')           
        rig.connectAttr(ikJoints[i]+'.rotate',blendColor+'.inRotate1')       
        rig.connectAttr(fkJoints[i]+'.translate',blendColor+'.inTranslate2')           
        rig.connectAttr(fkJoints[i]+'.rotate',blendColor+'.inRotate2') 
        rig.connectAttr(blendColor+'.outTranslate',skJoints[i]+'.translate')          
        rig.connectAttr(blendColor+'.outRotateX',skJoints[i]+'.rotateX')
        rig.connectAttr(blendColor+'.outRotateY',skJoints[i]+'.rotateY')
        rig.connectAttr(blendColor+'.outRotateZ',skJoints[i]+'.rotateZ')                     
#    create Iksystem
    locPoleVector = rig.spaceLocator(n = prefixName+'_poleVector')[0]
    ikHanleName = rig.ikHandle(sj = ikJoints[0],ee = ikJoints[2],n = prefixName+'_IKhandle',sol = 'ikRPsolver')[0] 
    SK_snapToObj(ikJoints[1],locPoleVector) 
    poleVectorConsName = rig.poleVectorConstraint(locPoleVector,ikHanleName)[0]
    
#    create global controller Scale
    jointPos1 = rig.xform(ikJoints[0],q = True,t = True,ws = True)
    jointPos2 = rig.xform(ikJoints[2],q = True,t = True,ws = True)
    scaleVal  = math.sqrt(math.pow((jointPos1[0]-jointPos2[0]),2)+ math.pow((jointPos1[1]-jointPos2[1]),2)+ math.pow((jointPos1[2]-jointPos2[2]),2))/11.4802792549
 
#create controller
    FKconScale = 0.1
    ikAnkleCon = SK_b01(13)
    rig.setAttr(ikAnkleCon+'.visibility',cb = False,k = False)
    SK_AddAttributes(ikAnkleCon,'Leg')
    rig.setAttr(ikAnkleCon+'.scale',scaleVal,scaleVal,scaleVal)
    SK_freezeObj(ikAnkleCon)
    rig.setAttr(ikAnkleCon+'.scaleVal',scaleVal)
    rig.connectAttr(conIkBlendGrp+'.ctrl',ikAnkleCon+'.ctrl')
    rig.setAttr(ikAnkleCon+'.ctrl',cb = False,k = False)
    ikanklecon = rig.rename(ikAnkleCon,prefixName+controlCurveName[3])
    
    IKFKSwithIkCon = rig.group(ikanklecon, n = ikanklecon+'_IKFK_GRP')    
    ikankleconConstraint = rig.group(IKFKSwithIkCon,n = ikanklecon+'_Anim')
    rig.parent(ikanklecon,ikankleconConstraint)
    ikankleconAnim = rig.group(ikankleconConstraint,n = ikanklecon+'_Constraint')
    ikankleconGRP = rig.group(ikankleconAnim,n = ikanklecon+'_GRP')
    
    ikLegPos = rig.xform(ikJoints[2],q = True,t = True,ws = True)
    if not ('Arm_' in leg):
        ikLegPos = rig.xform(prefix.split('_')[0]+legHeelPointer,q = True,t = True,ws = True)
    rig.xform(ikankleconGRP,t = ikLegPos,ws = True)
#    SK_snapToObj(ikJoints[2],ikankleconGRP)
    rig.parent(ikHanleName,ikanklecon)
    
    fkLegCon = SK_b29(6)
    rig.connectAttr(conIkBlendGrp+'.ctrl',fkLegCon+'.ctrl')
    fkLegCon = rig.rename(fkLegCon,prefixName+controlCurveName[0])
    rig.setAttr(fkLegCon+'.scale',FKconScale*scaleVal,FKconScale*scaleVal,FKconScale*scaleVal)
    rig.setAttr(fkLegCon+'.rz',90)
    SK_freezeObj(fkLegCon)
    fkLegConGRP = rig.group(fkLegCon,n = fkLegCon+'_GRP')
    SK_snapToObj(fkJoints[0],fkLegConGRP)
    rig.parentConstraint(fkLegCon,fkJoints[0])

    
    fkKneeCon = SK_b29(6)
    rig.connectAttr(conIkBlendGrp+'.ctrl',fkKneeCon+'.ctrl')
    fkKneeCon = rig.rename(fkKneeCon,prefixName+controlCurveName[1])
    rig.setAttr(fkKneeCon+'.scale',FKconScale*scaleVal,FKconScale*scaleVal,FKconScale*scaleVal)
    rig.setAttr(fkKneeCon+'.rz',90)
    SK_freezeObj(fkKneeCon)
    fkKneeConGRP = rig.group(fkKneeCon,n = fkKneeCon+'_GRP' )
    SK_snapToObj(fkJoints[1],fkKneeConGRP)
    rig.parentConstraint(fkKneeCon,fkJoints[1])

    
    fkAnkleCon = SK_b29(13)
    rig.setAttr(fkAnkleCon+'.visibility',cb = False,k = False)
    rig.connectAttr(conIkBlendGrp+'.ctrl',fkAnkleCon+'.ctrl')
    fkAnkleCon = rig.rename(fkAnkleCon,prefixName+controlCurveName[2])
    rig.setAttr(fkAnkleCon+'.scale',FKconScale*scaleVal,FKconScale*scaleVal,FKconScale*scaleVal)
    rig.setAttr(fkAnkleCon+'.rz',90)
    SK_freezeObj(fkAnkleCon)    
    fkAnkleConGRP = rig.group(fkAnkleCon,n = fkAnkleCon+'_GRP')
    SK_snapToObj(fkJoints[2],fkAnkleConGRP)
    rig.orientConstraint(fkAnkleCon,IKFKSwithIkCon,mo = True)
    rig.parentConstraint(fkAnkleCon,fkJoints[2])

    
    rig.parent(fkAnkleConGRP,fkKneeCon)
    rig.parent(fkKneeConGRP,fkLegCon)
    

#===============================================================================
#    create stretch system
#===============================================================================
    
#    创建Locator
    
    legLoc = rig.spaceLocator(n =  prefixName+'_Locator')[0]
    rig.pointConstraint(ikJoints[0],legLoc,mo = False)
    
    ankleLoc = rig.spaceLocator(n =  prefixName+'_Locator')[0]
    rig.pointConstraint(ikHanleName ,ankleLoc,mo = False)
    
    locatorDistaneceGrp = rig.group(empty = True,n =  prefixName+'_locDistanceGrp')
    SK_snapToObj(prefix,locatorDistaneceGrp)
    SK_freezeObj(locatorDistaneceGrp)
    rig.parent(legLoc,locPoleVector,ankleLoc,locatorDistaneceGrp)
#   create distanceBetweenNode
    ankleLegDis = rig.createNode('distanceBetween',n =  prefixName+'_DBT',ss = True)
    kneeLegDis = rig.createNode('distanceBetween',n =  prefixName+'_DBT',ss = True)
    ankleKneeDis = rig.createNode('distanceBetween',n =  prefixName+'_DBT',ss = True)
   
    locPoleVectorShape = rig.listRelatives(locPoleVector,s = True)[0]
    legLocShape = rig.listRelatives(legLoc,s = True)[0]
    ankleLocShape = rig.listRelatives(ankleLoc,s = True)[0]    

    rig.connectAttr(locPoleVector+'.translate',ankleKneeDis+'.point1')
    rig.connectAttr(locPoleVector+'.translate',kneeLegDis+'.point1')
  
    rig.connectAttr(ankleLoc +'.translate',ankleLegDis+'.point1')
    rig.connectAttr(ankleLoc +'.translate',ankleKneeDis+'.point2')
    
    rig.connectAttr(legLoc+'.translate',ankleLegDis+'.point2')
    rig.connectAttr(legLoc+'.translate',kneeLegDis+'.point2')
   
    XYZ = SK_jointOrientation(ikJoints[1])
    AxisValue = rig.getAttr(ikJoints[1]+'.'+XYZ)
    SK_createLegSetupNode(prefixName,ikJoints[1],ikJoints[2],ikanklecon,fkAnkleCon,conIkBlendGrp,reverseNode,XYZ,kneeLegDis,ankleKneeDis,ankleLegDis)


#   poleVector Setup    
    poleCurve = ''
    try:
        poleCurve = rig.curve(d = 1,p = [legPos[0],legPos[1],legPos[2]],k = [0,1,2],n =  prefixName+'_locatorPoleVector')
    except:
        pass
    poleVecPos = rig.getAttr(ankleLegDis+'.distance')
    rig.moveVertexAlongDirection(poleCurve+'.cv[1]',n = poleVecPos/3)
    poleVtxPos = rig.pointPosition(poleCurve+'.cv[1]')
    assisetPoleLoc = rig.spaceLocator(n =  prefixName+'_PoleVectorPos')[0]
    rig.addAttr(assisetPoleLoc,ln = 'ctrl',at = 'float',min = 0,max = 1, dv = 1,k = True)
    rig.connectAttr(conIkBlendGrp+'.ctrl',assisetPoleLoc+'.ctrl')
    rig.move(poleVtxPos[0],poleVtxPos[1],poleVtxPos[2],assisetPoleLoc)   
    rig.parent(assisetPoleLoc,fkJoints[0])
    rig.move(poleVtxPos[0],poleVtxPos[1],poleVtxPos[2],locPoleVector)
    
#    rotatePoleCurve = rig.group(empty = True,n = prefixName+'_RotatePole_ctrl')
    rotatePoleCurveUp = rig.group(empty = True,n = prefixName+'_RotatePole_Up')
    rotatePoleCurveGrp = rig.group(rotatePoleCurveUp,n = prefixName+'_RotatePole_Aim') 
    rotatePoleCurveAimGrp = rig.group(rotatePoleCurveGrp,n = rotatePoleCurveGrp+'_Grp')
    SK_snapToObj(prefix,rotatePoleCurveAimGrp)

    
    matrixLoc = rig.spaceLocator(n =  prefixName+'_Matrixlocate')[0]
    rig.setAttr(matrixLoc+'.visibility',0)   
    if(AxisValue < 0 ):
        rig.moveVertexAlongDirection(poleCurve+'.cv[2]', v = poleVecPos/12 )
    else:
        rig.moveVertexAlongDirection(poleCurve+'.cv[2]', v = -poleVecPos/12 )   
    matrixLocPos = rig.pointPosition(poleCurve+'.cv[2]')
    rig.setAttr(matrixLoc+'.translate',matrixLocPos[0],matrixLocPos[1],matrixLocPos[2])
  
#   如果是腿，将Locater移到heel位置
    rig.parent(matrixLoc,skJoints[2])
    if not ('Arm_' in leg):
        heelName = origeJoints[0].split('_')[0]+'_heel_drv'
        heelPos =  rig.xform(heelName,q = True,t = True,ws = False)
        rig.setAttr(matrixLoc +'.tx',heelPos[0])  
        rig.setAttr(matrixLoc+'.tz',heelPos[2])        
         
    rig.parent(matrixLoc,ikanklecon)
    SK_hideLockAll(matrixLoc)
    rig.delete(poleCurve)

    poleVectorControl = SK_b12(13)
    rig.addAttr(poleVectorControl,ln = 'LockKnee',at = 'bool',dv = 0,k = False)
    rig.addAttr(poleVectorControl,ln = 'aimRotate',at = 'enum',en = 'off:on:', dv = 1,k = False)
    rig.addAttr(poleVectorControl,ln = 'world',at = 'enum',en = 'off:on:', dv = 0,k = False)
    
    rig.addAttr(poleVectorControl,ln = 'follow',at = 'enum',en = 'auto:lock:world:normal:', dv = 0,k = True)
#    如果是胳膊，将此属性的初始值设为3
    if('Arm_' in leg):
        rig.setAttr(poleVectorControl+'.follow',3) 
#       将胳膊上的极向量控制器放大一点
        rig.setAttr(poleVectorControl+'.scale',1.8,1.8,1.8)
        SK_freezeObj(poleVectorControl)
    
    
    rig.connectAttr(conIkBlendGrp+'.ctrl',poleVectorControl+'.ctrl')
    poleVectorControl = rig.rename(poleVectorControl,prefixName+'_Pole_ctrl')
    rig.setAttr(poleVectorControl+'.scale',scaleVal*0.5,scaleVal*0.5,scaleVal*0.5)
    SK_freezeObj(poleVectorControl)
    poleVectorControlGrp  = rig.group(poleVectorControl,n = poleVectorControl+'_GRP')
    rig.move(poleVtxPos[0],poleVtxPos[1],poleVtxPos[2],poleVectorControlGrp)
    rig.parent(poleVectorControlGrp,rotatePoleCurveUp)

   
#        aim constraint
    upAim = 1
    if((AxisValue < 0 and 'Arm_' in leg) or (AxisValue > 0 and '_leg_' in leg)):
        upAim = -1
    poleAimConstraint = rig.aimConstraint(ikanklecon,rotatePoleCurveGrp,mo = True,aimVector = (1,0,0),upVector = (0,upAim,0),worldUpType = 'object',worldUpObject = matrixLoc)[0]

#   ploe切换
    poleReverse = rig.createNode('reverse',n =  prefixName+'_RV',ss = True)
    rig.pointConstraint(poleVectorControl,locPoleVector,mo = True)
    
#    connect IK_FK translate
    rig.connectAttr(ikJoints[1]+'.'+XYZ,fkKneeConGRP+'.'+XYZ)
    rig.connectAttr(ikJoints[2]+'.'+XYZ,fkAnkleConGRP+'.'+XYZ)
    
#   connect IKFK attribute 
    controlAllGrp = rig.group(empty = True,n =  prefixName+'_ALL_CTRL_GRP')
    rig.move(legPos[0][0],legPos[0][1],legPos[0][2],controlAllGrp)
    rig.parent(controlAllGrp,fkJoints[0])
    SK_freezeObj(controlAllGrp)
    rig.parent(controlAllGrp,w = True)
    rig.parent(skJoints[0],ikJoints[0],fkJoints[0],conIkBlendGrp,rotatePoleCurveAimGrp,locatorDistaneceGrp,ikankleconGRP,rotatePoleCurveAimGrp,fkLegConGRP,controlAllGrp)
    
#   IKFK切换隐藏
    ctrlsReverseNode = rig.createNode('reverse',n =  prefixName+'_RV',ss = True)
    rig.connectAttr(conIkBlendGrp+'.IKFK_vis',ctrlsReverseNode+'.inputX')
    rig.connectAttr(ctrlsReverseNode+'.outputX',fkLegConGRP +'.visibility')
    rig.connectAttr(conIkBlendGrp+'.IKFK_vis',ikankleconConstraint +'.visibility') 
    rig.connectAttr(conIkBlendGrp+'.IKFK_vis',rotatePoleCurveAimGrp +'.visibility')  
   
    
    kneeMD = rig.createNode('multiplyDivide',n = prefixName+'_MD',ss = True)
    rig.connectAttr(poleVectorControl+'.LockKnee',kneeMD+'.input1X')
    rig.connectAttr(poleReverse+'.outputX',kneeMD+'.input2X')
    rig.connectAttr(kneeMD+'.outputX',ikanklecon+'.LockKnee')
        
    rig.setAttr(ikanklecon+'.LockKnee',cb = False,k = False)
    
#   极向量旋转控制器自动向上
    poleSetRange = rig.createNode('setRange',n = prefixName+'_SR',ss = True)
    poleDistance = rig.getAttr(ankleLegDis+'.distance')
    poleDistanceMin = poleDistance/4 
            
    poleRoMD = rig.createNode('multiplyDivide',n = prefixName+'_MD',ss = True)
    rig.setAttr(poleRoMD+'.input1X',-70)
    if('Arm_' in leg): 
        rig.setAttr(poleVectorControl+'.aimRotate',0)
        rig.setAttr(poleRoMD+'.input1X',70)
    rig.connectAttr(poleVectorControl+'.aimRotate',poleRoMD+'.input2X')
    rig.connectAttr(poleRoMD+'.input2X',poleAimConstraint+'.'+ikanklecon+'W0')
    rig.connectAttr(poleRoMD+'.outputX',poleSetRange+'.minX',)
        
    rig.connectAttr(ankleLegDis+'.distance',poleSetRange+'.valueX')
    rig.setAttr(poleSetRange+'.oldMinX',poleDistanceMin)    
    rig.setAttr(poleSetRange+'.oldMaxX',poleDistance)
    rig.connectAttr(poleSetRange+'.outValueX',rotatePoleCurveUp+'.ry')
    
#   增加过渡骨骼
    MidJnt = rig.duplicate(skJoints[1],parentOnly = True,n = prefixName+'_MidJoint_jnt')[0]
    skMidJntRadius = rig.getAttr(skJoints[1]+'.radius')
    rig.setAttr(MidJnt+'.radius',skMidJntRadius*2)
    rig.setAttr(MidJnt+'.overrideEnabled',1)
    rig.setAttr(MidJnt+'.overrideColor',20)    
    skMidMD = rig.createNode('multiplyDivide',n = prefixName+'_MD',ss = True)
    rig.setAttr(skMidMD+'.input2X',0.5)
    rig.setAttr(skMidMD+'.input2Y',0.5)    
    rig.setAttr(skMidMD+'.input2Z',0.5)    
    rig.connectAttr(skJoints[1]+'.rx',skMidMD+'.input1X')
    rig.connectAttr(skJoints[1]+'.ry',skMidMD+'.input1Y')
    rig.connectAttr(skJoints[1]+'.rz',skMidMD+'.input1Z')        
    rig.connectAttr(skMidMD+'.outputX',MidJnt+'.rx')
    rig.connectAttr(skMidMD+'.outputY',MidJnt+'.ry')
    rig.connectAttr(skMidMD+'.outputZ',MidJnt+'.rz')        
    rig.connectAttr(skJoints[1]+'.tx',MidJnt+'.tx')    
    
#  hide ctrl attribute
    SK_hideLockAll(fkLegCon,1,0)
    
    SK_hideLockAll(fkKneeCon)
#    rig.setAttr(fkKneeCon+'.rx',k = True,l = False)
    rig.setAttr(fkKneeCon+'.ry',k = True,l = False)
#    rig.setAttr(fkKneeCon+'.rz',k = True,l = False)
    
    rig.setAttr(fkAnkleCon+'.tx',cb = False,k = False,l = True)
    rig.setAttr(fkAnkleCon+'.ty',cb = False,k = False,l = True)
    rig.setAttr(fkAnkleCon+'.tz',cb = False,k = False,l = True)
    rig.setAttr(fkAnkleCon+'.sx',cb = False,k = False)
    rig.setAttr(fkAnkleCon+'.sy',cb = False,k = False)
    rig.setAttr(fkAnkleCon+'.sz',cb = False,k = False)
    rig.setAttr(fkAnkleCon+'.ctrl',cb = False,k = False,l = True)
    
    SK_hideLockAll(poleVectorControl,0)
    rig.setAttr(poleVectorControl+'.follow  ',k = True,l = False) 
    rig.setAttr(ikJoints[0]+'.visibility',0)  
    rig.setAttr(fkJoints[0]+'.visibility',0)  
    
    rig.setAttr(locatorDistaneceGrp+'.visibility',0)    
    SK_hideLockAll(locatorDistaneceGrp)   

    
#    增加极向量指向
    SK_addAnnotation(prefixName,poleVectorControl,skJoints[1],conIkBlendGrp)
    try:
        rig.setAttr('*Arm_Wrist_*K.scaleX', keyable= True, lock =False)
        rig.setAttr('*Arm_Wrist_*K.scaleY', keyable= True, lock =False)
        rig.setAttr('*Arm_Wrist_*K.scaleZ', keyable= True, lock =False)
    except:
        pass

    try:
        rig.setAttr('*Leg_Ankle_FK.scaleX', keyable= True, lock =False)
        rig.setAttr('*Leg_Ankle_FK.scaleY', keyable= True, lock =False)
        rig.setAttr('*Leg_Ankle_FK.scaleZ', keyable= True, lock =False)
    except:
        pass

    try:
        rig.setAttr('*Leg_Leg_IK.scaleX', keyable= True, lock =False)  
        rig.setAttr('*Leg_Leg_IK.scaleY', keyable= True, lock =False)
        rig.setAttr('*Leg_Leg_IK.scaleZ', keyable= True, lock =False)   
    except:
        pass       
def SK_createFoot(jntObj):
    foot = jntObj
    LR = jntObj.split('_')[0]
    prefix = LR
    
    ikCon = prefix+'Leg_Leg_IK'
    fkAnkleCon = prefix+'Leg_Ankle_FK'    
    ankle = LR+'_ankle_drv_jnt'
    heel = LR+'_heel_drv'
    outSide = LR+'_foot_outside_refer'
    inSide =  LR+'_foot_inside_refer'
    footEnd =  LR+'_foot_end_drv'
    ball = LR+'_foot_drv'
    conName = 'ball'
    ikName = 'Leg'
    poleCtrl = prefix + 'Leg_Pole_ctrl'
    Leg_RotatePole_Aim = prefix + 'Leg_RotatePole_Aim'
    
    if('_wrist_' in foot):
        ikCon = prefix+'Arm_Wrist_IK'
        fkAnkleCon = prefix+'Arm_Wrist_FK'   
        ankle = LR+'_wrist_drv_jnt'
        heel = rig.group(empty = True,n = LR+'_wrist_heel_refer')
        outSide = rig.group(empty = True,n = LR+'_wrist_outside_refer')
        inSide =  rig.group(empty = True,n = LR+'_wrist_inside_refer')
        footEnd =  LR+'_handEnd_drv'
        ball = LR+'_hand_drv' 
        conName = 'wristMid'
        ikName = 'Arm'
    IKFKBlend = rig.connectionInfo(ikCon+'.ctrl',sfd = True).split('.')[0]    
    scaleVal = rig.getAttr(ikCon+'.scaleVal')
   
    ballConGrp = rig.group(empty = True,n = prefix+'_'+conName+'_con_Grp')
    ballGrp = rig.group(ballConGrp,n = prefix+'_'+conName+'_Grp')
    SK_snapToObj(ball,ballGrp)
    toeConGrp = rig.group(empty = True,n = prefix+'_'+conName+'_toe_con_Grp')
    toeGrp = rig.group(toeConGrp,n = prefix+'_'+conName+'_toe_Grp')
    SK_snapToObj(ball,toeGrp)  
    toeTipConGrp = rig.group(empty = True,n = prefix+'_'+conName+'_toeTip_con_Grp')
    toeTipGrp = rig.group(toeTipConGrp,n = prefix+'_'+conName+'_toeTip_Grp')
    SK_snapToObj(footEnd,toeTipGrp)   
    outSideConGrp = rig.group(empty = True,n = prefix+'_'+conName+'_outSide_con_Grp')
    outSideGrp = rig.group(outSideConGrp,n = prefix+'_'+conName+'_outSide_Grp')
    SK_snapToObj(outSide,outSideGrp)
    rig.parent(outSideGrp,heel)
    SK_freezeObj(outSideGrp)
    rig.parent(outSideGrp,w = True)
    inSideConGrp = rig.group(empty = True,n = prefix+'_'+conName+'_inSide_con_Grp')
    inSideGrp = rig.group(inSideConGrp,n = prefix+'_'+conName+'_inSide_Grp')
    SK_snapToObj(inSide,inSideGrp)
    rig.parent(inSideGrp,heel)
    SK_freezeObj(inSideGrp)
    rig.parent(inSideGrp,w = True)
    
    midRoConGrp = rig.group(empty = True,n = prefix+'_'+conName+'_midRo_con_Grp')
    midRoSideGrp = rig.group(midRoConGrp,n = prefix+'_'+conName+'_midRo_Grp')
    tipToePos = rig.xform(footEnd,q = True,t = True,ws = True)
    ballPos = rig.xform(ball,q = True,t = True,ws = True)
    currentGrpPos = []
    currentGrpPos.append((tipToePos[0]+ballPos[0])/2)
    currentGrpPos.append((tipToePos[1]+ballPos[1])/2)    
    currentGrpPos.append((tipToePos[2]+ballPos[2])/2) 
    rig.xform(midRoSideGrp,t = currentGrpPos,ws = True)
    rig.parent(midRoSideGrp,heel)
    SK_freezeObj(midRoSideGrp)

    #   使  swivel旋转为世界坐标  
    if('Rt' == prefix):
        rig.xform(midRoSideGrp,ro = (180,0,0),ws = True) 
    else:
        rig.xform(midRoSideGrp,ro = (0,0,0),ws = True)        
     
    rig.parent(midRoSideGrp,w = True)

    #   增加    Swivel控制属性。
    heelConGrp = rig.group(empty = True,n = prefix+'_'+conName+'_heel_con_Grp')
    heelGrp = rig.group(heelConGrp,n = prefix+'_'+conName+'_heel_Grp')
    SK_snapToObj(heel,heelGrp)
    midConGrp = rig.group(empty = True,n = prefix+'_'+conName+'_mid_con_Grp')
    midGrp = rig.group(midConGrp,n = prefix+'_'+conName+'_mid_Grp')
    SK_snapToObj(ball,midGrp)
    #   增加 脚部控制
    if not ('_wrist_' in foot):
        footConGrp = rig.rename(SK_b12(6),prefix+'Leg_foot')
        rig.setAttr(footConGrp+'.scale',1.2*scaleVal,1.2*scaleVal,1.2*scaleVal)
        SK_freezeObj(footConGrp)
        footGrp = rig.group(footConGrp,n = footConGrp+'_Grp')
        rig.xform(footGrp,t = rig.xform(ankle,q = True,t = True,ws = True),ws = True)
        #        SK_snapToObj(ankle,footGrp)   
        
            
        #   empty hierarchy
        rig.parent(ballGrp,toeGrp,toeTipConGrp)
        rig.parent(toeTipGrp,heelConGrp)
        rig.parent(heelGrp,outSideConGrp) 
        rig.parent(outSideGrp,inSideConGrp) 
        rig.parent(inSideGrp,midRoConGrp)
        rig.parent(midRoSideGrp,midConGrp)
        rig.parent(midGrp,footConGrp)
        
    else:
        rig.parent(ballGrp,toeGrp,toeTipConGrp)
        rig.parent(toeTipGrp,heelConGrp)
        rig.parent(heelGrp,outSideConGrp) 
        rig.parent(outSideGrp,inSideConGrp) 
        rig.parent(inSideGrp,midRoConGrp)
        rig.parent(midRoSideGrp,midConGrp)
        #   create IK
    rig.parent(ball,heel,ankle)
    

    ballIK = rig.ikHandle(ee = ball,sj = ankle,solver = 'ikRPsolver',n = prefix+'_'+conName+'_ball_IKHandle')[0]
    toeIK = rig.ikHandle(sj = ball,ee = footEnd,solver = 'ikRPsolver',n = prefix+'_'+conName+'_toe_IKHandle')[0]
    rig.connectAttr(IKFKBlend+'.IKFKBlend',ballIK+'.ikBlend')
    rig.connectAttr(IKFKBlend+'.IKFKBlend',toeIK+'.ikBlend')    
    rig.parent(prefix+ikName+'_IKhandle',ballIK,ballConGrp)
    rig.parent(toeIK,toeConGrp)

    #   create Node 
    if not ('_wrist_' in foot):
        rollRange = rig.createNode('setRange',n = prefix+'_SR',ss = True)
        rig.setAttr(rollRange+'.maxX',1)
        rig.setAttr(rollRange+'.maxY',1)    
        rig.setAttr(rollRange+'.maxY',1)    
        rig.connectAttr(ikCon+'.roll',rollRange+'.valueX')
        rig.connectAttr(ikCon+'.roll',rollRange+'.valueY')
        rig.connectAttr(IKFKBlend+'.toeLift',rollRange+'.oldMaxX')
        rig.connectAttr(IKFKBlend+'.toeLift',rollRange+'.oldMinY')    
        rig.connectAttr(IKFKBlend+'.toeStraight',rollRange+'.oldMaxY')   
        
        outRangPMA = rig.createNode('plusMinusAverage',n = prefix+'_MPA',ss = True) 
        rig.setAttr(outRangPMA+'.operation',2)
        rig.setAttr(outRangPMA+'.input1D[0]',1)
        rig.connectAttr(rollRange+'.outValueY',outRangPMA+'.input1D[1]')
        
        rollOutputMD = rig.createNode('multiplyDivide',n = prefix+'_MD',ss = True)
        rig.connectAttr(outRangPMA+'.output1D',rollOutputMD+'.input1X')
        rig.connectAttr(rollRange+'.outValueX',rollOutputMD+'.input2X')
        
        rollOutputMD1 = rig.createNode('multiplyDivide',n = prefix+'_MD',ss = True)
        rig.connectAttr(ikCon+'.roll',rollOutputMD1+'.input1X')
        rig.connectAttr(ikCon+'.roll',rollOutputMD1+'.input1Y')
        rig.connectAttr(ikCon+'.roll',rollOutputMD1+'.input1Z')
        rig.connectAttr(rollOutputMD+'.outputX',rollOutputMD1+'.input2X')
        rig.connectAttr(rollRange+'.outValueY',rollOutputMD1+'.input2Y')   
        
        ballMPA = rig.createNode('plusMinusAverage',n = prefix+'_MPA',ss = True) 
        rig.connectAttr(rollOutputMD1+'.outputX',ballMPA+'.input1D[0]')
        rig.connectAttr(ikCon+'.raiseBall',ballMPA+'.input1D[1]')
        
        toeMPA = rig.createNode('plusMinusAverage',n = prefix+'_MPA',ss = True) 
        rig.connectAttr(rollOutputMD1+'.outputY',toeMPA+'.input1D[0]')
        rig.connectAttr(ikCon+'.raiseToeTip',toeMPA+'.input1D[1]')
        
        reverseRoateMD = rig.createNode('multiplyDivide',n = prefix+'_MD',ss = True)    
        rig.connectAttr(ballMPA+'.output1D',reverseRoateMD+'.input1X')
        rig.connectAttr(toeMPA+'.output1D',reverseRoateMD+'.input1Y')
        rig.setAttr(reverseRoateMD+'.input2X',-1)
        rig.setAttr(reverseRoateMD+'.input2Y',-1)  
          
        rig.connectAttr(reverseRoateMD+'.outputX',ballConGrp+'.rz')
        rig.connectAttr(reverseRoateMD+'.outputY',toeTipConGrp+'.rz')
        

        #       增加Slide控制 
        prefix =  ikCon.split('_')[0]
        slideCondiNode = rig.createNode('condition',n = prefix+'_CDT',ss = True)
        slideMD = rig.createNode('multiplyDivide',n = prefix+'_MD',ss = True)
        
        rig.connectAttr(ikCon+'.side',slideCondiNode+'.firstTerm')
        rig.setAttr(slideCondiNode+'.operation',2)    
        rig.setAttr(slideCondiNode+'.colorIfTrueR',0)
        rig.setAttr(slideCondiNode+'.colorIfFalseR',1)
        rig.setAttr(slideCondiNode+'.colorIfTrueG',1)
        rig.setAttr(slideCondiNode+'.colorIfFalseG',0)
        rig.connectAttr(slideCondiNode+'.outColorR',slideMD+'.input2X')
        rig.connectAttr(slideCondiNode+'.outColorG',slideMD+'.input2Y')        
        rig.connectAttr(ikCon+'.side',slideMD+'.input1X')
        rig.connectAttr(ikCon+'.side',slideMD+'.input1Y')
        rig.connectAttr(slideMD+'.outputY',inSideConGrp+'.rz')
        rig.connectAttr(slideMD+'.outputX',outSideConGrp+'.rz')
        
    else:
        reverseRoateMD = rig.createNode('multiplyDivide',n = prefix+'_MD',ss = True)    
        rig.connectAttr(ikCon+'.raiseBall',reverseRoateMD+'.input1X')
        rig.setAttr(reverseRoateMD+'.input2X',-1)
        rig.connectAttr(reverseRoateMD+'.outputX',ballConGrp+'.rz')
        rig.connectAttr(ikCon+'.raiseToeTip',toeTipConGrp+'.rz')

        rig.setAttr(ikCon+'.side',cb = False,k = False,l = False)        
        rig.setAttr(ikCon+'.swivel',cb = False,k = False,l = False)  
        rig.setAttr(ikCon+'.swivelBall',cb = False,k = False,l = False) 
        rig.setAttr(ikCon+'.raiseHeel',cb = False,k = False,l = False)
        rig.setAttr(ikCon+'.swivelHeel',cb = False,k = False,l = False)
        rig.setAttr(ikCon+'.swivelToeTip',cb = False,k = False,l = False)
        rig.setAttr(ikCon+'.raiseToe',cb = False,k = False,l = False)
        rig.setAttr(ikCon+'.swivelToe',cb = False,k = False,l = False)
        rig.setAttr(ikCon+'.roll',cb = False,k = False,l = False)
        rig.setAttr(ikCon+'.raiseToeTip',cb = False,k = False,l = False)
    
    rig.connectAttr(ikCon+'.swivelBall',midConGrp+'.ry')
    rig.connectAttr(ikCon+'.raiseHeel',heelConGrp+'.rx')
    rig.connectAttr(ikCon+'.swivelHeel',heelConGrp+'.ry')
    rig.connectAttr(ikCon+'.swivelToeTip',toeTipConGrp+'.ry')
    rig.connectAttr(ikCon+'.raiseToe',toeConGrp+'.rz')
    rig.connectAttr(ikCon+'.swivelToe',toeConGrp+'.ry')
    rig.connectAttr(ikCon+'.swivel',midRoConGrp+'.ry')    

    
    #   create FKcontrol
    fkCon = SK_b29(6) 
    fkCon = rig.rename(fkCon,prefix+ikName+'_'+conName+'_FK') 
    rig.setAttr(fkCon+'.rz',90)
    SK_freezeObj(fkCon)
    rig.setAttr(fkCon+'.scale',0.06*scaleVal,0.06*scaleVal,0.06*scaleVal)
    SK_freezeObj(fkCon)
    fkConGrp = rig.group(fkCon,n = fkCon+'_GRP')
    SK_snapToObj(ball,fkConGrp)
    ballOrient = rig.orientConstraint(fkCon,ball)[0]
    IKFKBlendReverse = [node for node in rig.connectionInfo(IKFKBlend+'.IKFKBlend',dfs = True) if('reverse' == rig.nodeType(node.split('.')[0]))][0].split('.')[0]
    rig.connectAttr(IKFKBlendReverse+'.outputX',ballOrient+'.'+fkCon+'W0')
    
    rig.connectAttr(IKFKBlend+'.ctrl',fkCon+'.ctrl')
    rig.setAttr(fkCon+'.visibility',cb = False,k = False)
    SK_hideLockAll(fkCon,1,0)   
    rig.setAttr(fkCon+'.rx',cb = False,k = False,l = True)
    
    if('_wrist_' in foot):
        fkConShape = rig.listRelatives(fkCon,s = True)[0]
        rig.setAttr(fkConShape+'.visibility',0) 
        #        rig.renameAttr(ikCon+'.raiseBall', 'bend' )
        rig.delete(heel,outSide,inSide)
        
    
    sourceGrp = rig.connectionInfo(fkCon+'.ctrl', sfd=True)
    allCtrls = [i.split('.')[0] for i in rig.connectionInfo(sourceGrp, dfs=True)]
    ankleFk = [i for i in allCtrls if(('_Wrist_FK' in i) or ('_Ankle_FK' in i))][0]  

    rig.parent(fkConGrp,ankleFk)
    if ('_wrist_' in foot): 
        rig.parent(midGrp,ikCon)
    else:
        rig.parent(footGrp,ikCon)
    

    HandsAndFeet_Scale_MD = rig.createNode('multiplyDivide',n = prefix+'Scale_MD',ss = True)    
    rig.connectAttr(ikCon+'.scale',HandsAndFeet_Scale_MD+'.input1')
    rig.connectAttr(ankleFk+'.scale',HandsAndFeet_Scale_MD+'.input2')       
    rig.connectAttr(HandsAndFeet_Scale_MD+'.output',ankle+'.scale')
    scaleJointConnectAttrs = rig.listConnections(ankle+'.scale',destination=1,source=0,p=1)
    try:
        for scaleJointConnectAttr in scaleJointConnectAttrs:
            rig.disconnectAttr(ankle+'.scale',scaleJointConnectAttr)
    except:
        pass
    ikCon_Childrens = rig.listRelatives(ikCon,children=1,f=1,type = 'transform')   
    ikConChildernGRP = rig.group(ikCon_Childrens,name=ikCon+'_childernGRP' )
    rig.setAttr(ikConChildernGRP+'.rotatePivot',0,0,0)
    rig.setAttr(ikConChildernGRP+'.scalePivot',0,0,0)    
    rig.connectAttr(ankleFk+'.scale',ikConChildernGRP+'.scale')  
      
    #   hide Attribute
    rig.setAttr(midGrp+'.visibility',0)
    SK_hideLockAll(midGrp) 
   
    if ('_wrist_' in foot):
        fingers = rig.listRelatives(ball.replace('hand','wrist'),c = True)
        if(fingers):
            rig.parent(fingers,ankle)
            scaleJointConnectAttrs = rig.listConnections(ankle+'.scale',destination=1,source=0,p=1)
            try:
                for scaleJointConnectAttr in scaleJointConnectAttrs:
                    rig.disconnectAttr(ankle+'.scale',scaleJointConnectAttr)
            except:
                pass 
                        
    #    增加拉伸显示控制
    SK_addLockDisplayControlCure(ankle,scaleVal,fkAnkleCon)

    #    增加新的控制器，用于将脚部和手部的IKFK属性，和部分不常用 的属性放到新的控制器上。
    SK_addIKFKswitchControl(ikCon,ankleFk,ankle,scaleVal)

    #    添加胯部自动联动。
    if not ('_wrist_' in foot):    
        IKAutoHip_Lc = rig.spaceLocator(n = ikCon+'_AutoHip_Locator')[0]
        IKAutoHip_LcGRP = rig.group(IKAutoHip_Lc,n = (IKAutoHip_Lc+'_GRP'),parent = ikCon,relative = 1)
        IKAutoHipMatrixlocate_Lc = rig.duplicate(IKAutoHip_Lc,n = IKAutoHip_Lc+'_Matrixlocate')[0]
        rig.parent(IKAutoHipMatrixlocate_Lc,IKAutoHip_Lc)
        if 'LfLeg' in IKAutoHipMatrixlocate_Lc:
            rig.setAttr((IKAutoHipMatrixlocate_Lc+'.translateX'),1)
        if 'RtLeg' in IKAutoHipMatrixlocate_Lc:
            rig.setAttr((IKAutoHipMatrixlocate_Lc+'.translateX'),-1)
        rig.connectAttr(ikCon+'.translate',IKAutoHip_Lc+'.translate')
        rig.connectAttr(ikCon+'.rotate',IKAutoHip_Lc+'.rotate')    
        rig.connectAttr(ikCon+'.scale',IKAutoHip_Lc+'.scale') 
        
        IKAutoHipPole_Lc = rig.spaceLocator(n = ikCon+'_AutoHip_Pole_Locator')[0]
        IKAutoHipPole_LcGRP = rig.group(IKAutoHipPole_Lc,n = IKAutoHipPole_Lc+'_GRP',parent = poleCtrl,relative = 1)   
        IKAutoHipPole_Lc_Aim_GRP = rig.group(em=True, name = IKAutoHipPole_LcGRP+'_AimGRP',parent = Leg_RotatePole_Aim,relative = 1)
        rig.parent(IKAutoHipPole_LcGRP,IKAutoHipPole_Lc_Aim_GRP)
        rig.aimConstraint(IKAutoHip_Lc,IKAutoHipPole_Lc_Aim_GRP,mo=1,weight= 1,worldUpType='object',worldUpObject=IKAutoHipMatrixlocate_Lc)[0]
        rig.group(IKAutoHipPole_Lc_Aim_GRP,n=IKAutoHipPole_Lc_Aim_GRP+'_GRP',parent = Leg_RotatePole_Aim+'_Grp',relative = 1)
        rig.connectAttr(poleCtrl+'.translate',IKAutoHipPole_Lc+'.translate')
        rig.connectAttr(poleCtrl+'.rotate',IKAutoHipPole_Lc+'.rotate')    
        rig.connectAttr(poleCtrl+'.scale',IKAutoHipPole_Lc+'.scale')    
    
    
def SK_addLockDisplayControlCure(jnt,scaleVal,fkCon):
    midJnt = rig.listRelatives(jnt,p = True)[0]
    upJnt = rig.listRelatives(midJnt,p = True)[0] 
#   找到极向量控制
    sourceGrp = rig.connectionInfo(fkCon+'.ctrl', sfd=True)
    allCtrls = [i.split('.')[0] for i in rig.connectionInfo(sourceGrp, dfs=True)]
    poleCon = [i for i in allCtrls if(('_Pole_' in i) and rig.attributeQuery('LockKnee',node = i,ex = True))][0]  
#    查找腿部和肘部缩放值
    midValue = rig.getAttr(sourceGrp.split('.')[0]+'.upSize')
    upValue = rig.getAttr(sourceGrp.split('.')[0]+'.lowSize')
    
#   创建控制器
    midName = rig.rename(SK_b05(6),midJnt.replace('drv_jnt','display'))
    rig.setAttr(midName+'.rz',90)
    rig.setAttr(midName+'.scale',0.3*scaleVal,0.3*scaleVal,0.3*scaleVal)
    SK_freezeObj(midName)
    SK_snapToObj(upJnt,midName)
    rig.parent(midName,upJnt)
    SK_freezeObj(midName)
    rig.setAttr(midName+'.tx',midValue)
    rig.setAttr(midName+'.template',1)
    
    upName = rig.rename(SK_b05(6),upJnt.replace('drv_jnt','display'))
    rig.setAttr(upName+'.rz',90)
    rig.setAttr(upName+'.scale',0.3*scaleVal,0.3*scaleVal,0.3*scaleVal)
    SK_freezeObj(upName)
    SK_snapToObj(midJnt,upName)
    rig.parent(upName,midJnt)
    SK_freezeObj(upName)
    rig.setAttr(upName+'.tx',upValue)
    rig.setAttr(upName+'.template',1)   

#   连接隐藏属性
    if poleCon:
        poleMD = rig.listConnections(poleCon+'.LockKnee',s = False,d = True,type = 'multiplyDivide')[0]
        rig.connectAttr(poleMD+'.outputX',upName+'.visibility')
        rig.connectAttr(poleMD+'.outputX',midName+'.visibility')
       

def SK_addIKFKswitchControl(ikCon,fkCon,parentObj,scaleVal):
    conName = rig.rename(SK_b31(18),ikCon.split('_')[0]+'_Switch')
    rig.setAttr(conName+'.scale',scaleVal*0.4,scaleVal*0.4,scaleVal*0.4)
    pos = rig.xform(parentObj,q = True,t = True,ws = True)
    rig.xform(conName,t = pos,ws = True)
    rig.parent(conName,parentObj)
    rig.move(0,0,-1*scaleVal,conName,r = True)
    SK_freezeObj(conName)
    SK_hideLockAll(conName)
    
    IKFKBlend = ikCon.split('_')[0]+'_IKFK_blendCon'
    rig.connectAttr(IKFKBlend+'.ctrl',conName+'.ctrl')
    

    rig.addAttr(conName,ln = 'Stretch',at = 'float',k = True)
    rig.addAttr(conName,ln = 'KneeSlide',at = 'float',k = True)
    rig.addAttr(conName,ln = 'UpLegth',at = 'float',k = True)
    rig.addAttr(conName,ln = 'LowLength',at = 'float',k = True)
    rig.addAttr(conName,ln = 'AutoStretch',at = 'float',min = 0,max = 1,k = True)
    rig.addAttr(conName,ln = 'follow',at = 'enum',en = 'Arm:Torso:World:Chest:Head:',dv = 2,k = True)
    rig.addAttr(conName,ln = 'ankleVis',at = 'enum',en = 'off:on:',k = True)
#    如果不是胳膊，将此属性隐藏   
    if not('_Wrist_' in ikCon):
        rig.setAttr(conName+'.follow',cb = False,k = False)
        
        rig.addAttr(conName,ln = 'toeLift',at = 'float',dv = 30,k = True)
        rig.addAttr(conName,ln = 'toeStraight',at = 'float',dv = 60,k = True)
        rig.connectAttr(conName+'.toeLift',IKFKBlend+'.toeLift')
        rig.connectAttr(conName+'.toeStraight',IKFKBlend+'.toeStraight')
        
    rig.addAttr(conName,ln = 'twistPlacement',at = 'enum',en = 'front:side:',dv = 1,k = True)
    rig.addAttr(conName,ln = 'addTwist',at = 'float',k = True)
    
    rig.addAttr(conName,ln = 'IKFK',at = 'enum',en = 'off:on:',dv = 1,k = True)
#    如果是胳膊，将此属性的初始值设为3
    if('_Wrist_' in ikCon):
        rig.setAttr(conName+'.IKFK',0)
        rig.setAttr(conName+'.ankleVis',cb = False,k = False)
        

    rig.addAttr(conName,ln = 'expertUp',at = 'enum',en = 'Normal:Zero:Up:Down:',dv = 0,k = True)
    rig.addAttr(conName,ln = 'expertLow',at = 'enum',en = 'Normal:Zero:Up:Down:',dv = 0,k = True)
#   连接属性    
    rig.connectAttr(conName+'.Stretch',IKFKBlend+'.Stretch')
    rig.connectAttr(conName+'.KneeSlide',IKFKBlend+'.KneeSlide')
    rig.connectAttr(conName+'.UpLegth',IKFKBlend+'.UpLegth')
    rig.connectAttr(conName+'.LowLength',IKFKBlend+'.LowLength')
    rig.connectAttr(conName+'.AutoStretch',IKFKBlend+'.AutoStretch')
#    rig.connectAttr(conName+'.Start_Pole',IKFKBlend+'.PoleSwitch')
    rig.connectAttr(conName+'.IKFK',IKFKBlend+'.IKFK')

    if not('_Wrist_' in ikCon):
        conFoot = ikCon.split('_')[0]+'_foot'
        rig.connectAttr(conName+'.ankleVis',conFoot+'.visibility')  
        SK_hideLockAll(conFoot,1,0) 
#   隐藏被连接属性
    
    rig.setAttr(IKFKBlend+'.AutoStretch',cb = False,l = False,k = False)

def SK_addAnnotation(prefix,pole,midJnt,IKFKGrp):
    poleShape = rig.listRelatives(pole,s = True)[0]
    annotationNameShape = rig.createNode('annotationShape', n = prefix+'_annotationShape',ss = True)
    annotationNameParent = rig.rename(rig.listRelatives(annotationNameShape,p = True)[0],prefix+'_annotation')
    SK_snapToObj(midJnt,annotationNameParent)
    rig.parent(annotationNameParent,midJnt)
    rig.connectAttr(poleShape+'.worldMatrix[0]',annotationNameShape+'.dagObjectMatrix[0]')
    rig.connectAttr(IKFKGrp+'.IKFK',annotationNameParent+'.visibility')
    
    rig.setAttr(annotationNameParent+'.overrideEnabled',1)
    rig.setAttr(annotationNameParent+'.overrideDisplayType',2)    
    
    
    
    
    
  
