#-*- coding: utf-8 -*-
import maya.cmds as rig
import re
from RIG.nurbsCurveCon import *
from RIG.commonly.base import *


def SK_createTwist(jntObj):
    prefix = jntObj.split('_')[0]
    IKFKblend = prefix+'_IKFK_blendCon'
    
    sourceGrp = rig.connectionInfo(jntObj+'.ctrl', sfd=True)
    sourceGrpName = sourceGrp.split('.')[0]
    allCtrls = [i.split('.')[0] for i in rig.connectionInfo(sourceGrp, dfs=True) if 'nurbsCurve' == rig.nodeType(rig.listRelatives(i.split('.')[0],c = True)[0]) ]
    ikCon = ''
    ikRotate = ''
    fkCon = ''
    fkUpCon = ''
    switchCon = ''
    for con in allCtrls:
        if('_IK' in con):
            ikCon = con
        if('_Pole_ctrl' in con):
            ikRotate = con
            rig.addAttr(ikRotate,ln = 'twistPlacement',at = 'enum',en = 'front:side:',dv = 0,k = True)
            rig.addAttr(ikRotate,ln = 'addTwist',at = 'float',k = True)
        if('_UpArm_FK' in con or '_Leg_FK' in con):
            fkUpCon = con
            rig.addAttr(fkUpCon,ln = 'twistPlacement',at = 'enum',en = 'front:side:',dv = 0,k = True)
            rig.addAttr(fkUpCon,ln = 'addTwist',at = 'float',k = True)
        if('_Wrist_FK' in con or '_Ankle_FK' in con):
            fkCon = con 
        if('_Switch' in con):
            switchCon = con
            
    wristJnt = rig.listConnections(ikCon+'.scale',s = False,d = True,scn = True,type = 'joint')[0]
    lowJnt = rig.listRelatives(wristJnt,p = True)[0]
    midJnt = rig.listRelatives(lowJnt,p = True)[0]
    lowJntRoGrp = lowJnt.split('_')[0]+lowJnt.split('_')[1]+'_bendRotateGrp'
    midJntRotGrp = midJnt.split('_')[0]+midJnt.split('_')[1]+'_bendRotateGrp' 

#   find rotateBend and connect
    upRoJnt = rig.listRelatives(midJnt,p = True)[0]
    midRojnt = midJnt
#    rig.parent(lowJntRoGrp,lowJnt)
    copyLowJntRoGrp = rig.duplicate(lowJntRoGrp,rr = True,n = lowJntRoGrp+'_orientConstraint')[0]
    rig.parent(midJntRotGrp,upRoJnt)
    copyMidJntRotGrp = rig.duplicate(midJntRotGrp,rr = True,n = midJntRotGrp+'_orientConstraint')[0] 
    

    rig.makeIdentity(copyLowJntRoGrp,t = True,r = True,s = True)
    orientLowGrp = rig.duplicate(copyLowJntRoGrp,rr = True,n = copyLowJntRoGrp+'_ORIENT')[0]
    rig.makeIdentity(copyMidJntRotGrp,t = True,r = True,s = True) 
    orientMidGrp = rig.duplicate(copyMidJntRotGrp,rr = True,n = copyMidJntRotGrp+'_ORIENT')[0]
    rig.orientConstraint(orientLowGrp,copyLowJntRoGrp,mo = True)  
    rig.orientConstraint(orientMidGrp,copyMidJntRotGrp,mo = True) 
    rig.connectAttr(wristJnt+'.rotate',orientLowGrp+'.rotate') 
    rig.connectAttr(midJnt+'.rotate',orientMidGrp+'.rotate') 

#    增加乘除节点：左边乘以-1右边乘以1         
    upMD = rig.createNode('multiplyDivide',ss = True,n = prefix+'_MD')
    upSC = rig.createNode('choice',ss = True,n = prefix+'_SC')
    rig.addAttr(upMD,ln = 'normal',at = 'double',dv = 0)
    rig.addAttr(upMD,ln = 'zero',at = 'double',dv = 0)
    rig.addAttr(upMD,ln = 'up',at = 'double',dv = 180)
    rig.addAttr(upMD,ln = 'down',at = 'double',dv = -180)
    if 'Lf' in prefix:
        rig.setAttr(upMD+'.input2X',-1)
    else:
        rig.setAttr(upMD+'.input2X',1)        
    rig.connectAttr(copyMidJntRotGrp+'.rx',upMD+'.input1X')
    rig.connectAttr(upMD+'.outputX',upSC+'.input[0]')
    rig.connectAttr(upMD+'.zero',upSC+'.input[1]')
    rig.connectAttr(upMD+'.up',upSC+'.input[2]')
    rig.connectAttr(upMD+'.down',upSC+'.input[3]')
    
    rig.addAttr(midJntRotGrp,ln = 'inputData',at = 'double')
    rig.connectAttr(midJntRotGrp+'.inputData',midJntRotGrp+'.rotateX')    
    rig.connectAttr(upSC+'.output',midJntRotGrp+'.inputData')
    rig.connectAttr(switchCon+'.expertUp',upSC+'.selector')   

    
    lowMD = rig.createNode('multiplyDivide',ss = True,n = prefix+'_MD') 
    lowSC = rig.createNode('choice',ss = True,n = prefix+'_SC')
    rig.addAttr(lowMD,ln = 'normal',at = 'double',dv = 0)
    rig.addAttr(lowMD,ln = 'zero',at = 'double',dv = 0)
    rig.addAttr(lowMD,ln = 'low',at = 'double',dv = 180)
    rig.addAttr(lowMD,ln = 'down',at = 'double',dv = -180)
    if 'Lf' in prefix:
        rig.setAttr(lowMD+'.input2X',1)
    else:
        rig.setAttr(lowMD+'.input2X',-1)   
    rig.connectAttr(copyLowJntRoGrp+'.rx',lowMD+'.input1X')
    rig.connectAttr(lowMD+'.outputX',lowSC+'.input[0]')
    rig.connectAttr(lowMD+'.zero',lowSC+'.input[1]')
    rig.connectAttr(lowMD+'.low',lowSC+'.input[2]')
    rig.connectAttr(lowMD+'.down',lowSC+'.input[3]')
    
    rig.addAttr(lowJntRoGrp,ln = 'inputData',at = 'double')
    rig.connectAttr(lowJntRoGrp+'.inputData',lowJntRoGrp+'.rotateX')    
    rig.connectAttr(lowSC+'.output',lowJntRoGrp+'.inputData')
    rig.connectAttr(switchCon+'.expertLow',lowSC+'.selector')     

#   set twist value
    MPANodes = rig.listConnections(midJntRotGrp+'.rx', s = False,d = True,scn = True)
    MPANodes.sort()

    MDNodes = [rig.listConnections(md,s = False,d = True,scn = True,type = 'multiplyDivide')[0] for md in MPANodes]
    midNodes = [MDNode.split('_')[1] for MDNode in MDNodes]
    newNodes = []
    for i,j in enumerate(midNodes):
        index = midNodes.index(str(i))
        newNodes.append(MDNodes[index])
    attrs = []
    mdValues = []
    for md in newNodes:
        mdAttr = rig.listConnections(md+'.input2X',s = True,d = False,scn = True,p = True)[0]
        attrs.append(mdAttr)
        values = rig.getAttr(mdAttr)
        mdValues.append(values)
    
    remdValues = mdValues[::-1]
    for i,attr in enumerate(attrs):
        rig.setAttr(attr,remdValues[i])        

    BTAnode = rig.listConnections(MPANodes[0],s = True,d = False,scn = True,type = 'blendTwoAttr')[0]
    rig.connectAttr(ikRotate+'.addTwist',BTAnode+'.input[1]')
    rig.connectAttr(fkUpCon+'.addTwist',BTAnode+'.input[0]')
    rig.connectAttr(IKFKblend+'.IKFK',BTAnode+'.attributesBlender')
#   twist placement connect
    upBTA = rig.createNode('blendTwoAttr',n = prefix+'_BTA')
    rig.connectAttr(ikRotate+'.twistPlacement',upBTA+'.input[1]')
    rig.connectAttr(fkUpCon+'.twistPlacement',upBTA+'.input[0]')    
    rig.connectAttr(IKFKblend+'.IKFK',upBTA+'.attributesBlender')  
    
    lowBTA = rig.createNode('blendTwoAttr',n = prefix+'_BTA')
    rig.connectAttr(switchCon+'.twistPlacement',lowBTA+'.input[1]')
    rig.connectAttr(switchCon+'.twistPlacement',lowBTA+'.input[0]')    
    rig.connectAttr(IKFKblend+'.IKFK',lowBTA+'.attributesBlender')

    
    rig.addAttr(copyLowJntRoGrp,ln = 'orderTwist',at = 'long',dv = 3)  
    rig.addAttr(copyMidJntRotGrp,ln = 'orderTwist',at = 'long',dv = 3)
    rig.addAttr(copyLowJntRoGrp,ln = 'temOrder',at = 'long',dv = 1)  
    rig.addAttr(copyMidJntRotGrp,ln = 'temOrder',at = 'long',dv = 1)
    upMidBTA = rig.createNode('blendTwoAttr',n = prefix+'_BTA')         
    lowMidBTA = rig.createNode('blendTwoAttr',n = prefix+'_BTA')
    rig.connectAttr(copyMidJntRotGrp+'.orderTwist',lowMidBTA+'.input[0]')
    rig.connectAttr(copyLowJntRoGrp+'.orderTwist',upMidBTA+'.input[0]')
    rig.connectAttr(upBTA+'.output',lowMidBTA+'.attributesBlender') 
    rig.connectAttr(lowBTA+'.output',upMidBTA+'.attributesBlender')     
       
    rig.setAttr(upMidBTA+'.input[1]',0)    
    rig.setAttr(lowMidBTA+'.input[1]',0)
    rig.connectAttr(lowMidBTA+'.output',copyMidJntRotGrp+'.temOrder')
    rig.connectAttr(copyMidJntRotGrp+'.temOrder',copyMidJntRotGrp+'.rotateOrder')        
    rig.connectAttr(upMidBTA+'.output',copyLowJntRoGrp+'.temOrder')   
    rig.connectAttr(copyLowJntRoGrp+'.temOrder',copyLowJntRoGrp+'.rotateOrder')            
#   up joint set
    MPANodes = rig.listConnections(lowJntRoGrp+'.rx', s = False,d = True,scn = True)
    BTAnode = rig.listConnections(MPANodes[0],s = True,d = False,scn = True,type = 'blendTwoAttr')[0]
    MPANodes.sort()
    MDNodes = [rig.listConnections(md,s = False,d = True,scn = True,type = 'multiplyDivide')[0] for md in MPANodes]
    rig.connectAttr(switchCon+'.addTwist',BTAnode+'.input[1]')
    rig.connectAttr(switchCon+'.addTwist',BTAnode+'.input[0]')
    rig.connectAttr(IKFKblend+'.IKFK',BTAnode+'.attributesBlender') 
    
