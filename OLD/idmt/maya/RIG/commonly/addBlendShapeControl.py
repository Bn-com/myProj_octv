#-*- coding: utf-8 -*-
import maya.cmds as rig
from RIG.commonly.base import *


def SK_createBlendShapeCon(JNTS = []):

    for UpJnt in JNTS:
        sign = UpJnt.split('_')[0]+UpJnt.split('_')[1]
        UpGrp = rig.listRelatives(UpJnt,p = True)[0]
        
        scaleValCon = UpGrp.split('_')[0]
        if ('Arm' in scaleValCon):
            scaleValCon = scaleValCon+'_Wrist_IK'
        else:
            scaleValCon = scaleValCon+'_Leg_IK'   
        scaleVal = rig.getAttr(scaleValCon +'.scaleVal') 
        
        UpGrpJnt = rig.listRelatives(UpGrp,p = True)[0]
        dnJnt = sign+'_MidJoint_jnt'
        Loc = sign+'_Curve2_LocShape'
        
        BSsphere = rig.sphere(n = sign+'_Nurbs_Project',ch = False,o = 1,ax = (0,0,-1),r = 0.2,nsp = 4,ssw = 90,endSweep = 270)[0]
        BSsphereShape = rig.listRelatives(BSsphere,s = True)[0]
        rig.setAttr(BSsphere+'.visibility',0)

        if ('Lf' in sign):
            rig.setAttr(BSsphere+'.ry',180)
        SK_freezeObj(BSsphere) 
        SK_snapToObj(UpGrp,BSsphere)
        rig.parent(BSsphere,UpGrpJnt)
        rig.rebuildSurface(BSsphere,ch = False,rpo = 1,rt = 0,end = 1,kr = 0,kc = 0,su = 6,du = 3,sv = 6,dv = 3,tol = 0.01,fr = 0,dir = 2)
        
        CPS = rig.createNode('closestPointOnSurface',n = sign+'_CPS',ss = True)
        rig.connectAttr(BSsphereShape+'.worldSpace',CPS+'.inputSurface')
        rig.connectAttr(Loc+'.worldPosition[0]',CPS+'.inPosition')
        rig.addAttr(UpGrp,at = 'float',ln = 'Up',min = 0,max = 1,k = True)
        rig.addAttr(UpGrp,at = 'float',ln = 'Dn',min = 0,max = 1,k = True)
        rig.addAttr(UpGrp,at = 'float',ln = 'Fn',min = 0,max = 1,k = True)
        rig.addAttr(UpGrp,at = 'float',ln = 'Bc',min = 0,max = 1,k = True)
                
        UpPOF = rig.createNode('pointOnSurfaceInfo',n = sign+'_Up_POF')
        rig.connectAttr(BSsphereShape+'.worldSpace',UpPOF+'.inputSurface')
        rig.setAttr(UpPOF+'.parameterU',0.5)
        rig.setAttr(UpPOF+'.parameterV',1)
        DnPOF = rig.createNode('pointOnSurfaceInfo',n = sign+'_Dn_POF')
        rig.connectAttr(BSsphereShape+'.worldSpace',DnPOF+'.inputSurface')
        rig.setAttr(DnPOF+'.parameterU',0.5)
        rig.setAttr(DnPOF+'.parameterV',0)
        FnPOF = rig.createNode('pointOnSurfaceInfo',n = sign+'_Fn_POF')
        rig.connectAttr(BSsphereShape+'.worldSpace',FnPOF+'.inputSurface')
        rig.setAttr(FnPOF+'.parameterU',1)
        rig.setAttr(FnPOF+'.parameterV',1)
        BcPOF = rig.createNode('pointOnSurfaceInfo',n = sign+'_Bc_POF')
        rig.connectAttr(BSsphereShape+'.worldSpace',BcPOF+'.inputSurface')
        rig.setAttr(BcPOF+'.parameterU',0)
        rig.setAttr(BcPOF+'.parameterV',0)
        
        UpDSB = rig.createNode('distanceBetween',n = sign+'_Up_DSB',ss = True)
        DnDSB = rig.createNode('distanceBetween',n = sign+'_Dn_DSB',ss = True)
        FnDSB = rig.createNode('distanceBetween',n = sign+'_Fn_DSB',ss = True)
        BcDSB = rig.createNode('distanceBetween',n = sign+'_Bc_DSB',ss = True) 
        
        if ('Lf' in sign):
            rig.setAttr(BSsphere+'.sy',-1) 
        rig.xform(BSsphere,s = (scaleVal,scaleVal,scaleVal),wd  = True,r = True)  
        
        rig.connectAttr(UpPOF+'.result.position',UpDSB+'.point1')     
        rig.connectAttr(CPS+'.position',UpDSB+'.point2')        
        disLength = rig.getAttr(UpDSB+'.distance')
        LengthMD = rig.createNode('multiplyDivide',n = sign+'_MD')
        rig.connectAttr('ScaleConstraints_GRP.scaleX',LengthMD+'.input1X')
        rig.setAttr(LengthMD+'.input2X',disLength)
        UpRV = rig.createNode('remapValue',n = sign+'_Up_RV',ss = True)
        rig.setAttr(UpRV+'.inputMin',0)
        rig.connectAttr(LengthMD+'.outputX',UpRV+'.inputMax')
        rig.setAttr(UpRV+'.outputMin',0)
        rig.setAttr(UpRV+'.outputMax',1)
        rig.setAttr(UpRV+'.value[0].value_Position',0)
        rig.setAttr(UpRV+'.value[0].value_FloatValue',1)
        rig.setAttr(UpRV+'.value[1].value_Position',1)
        rig.setAttr(UpRV+'.value[1].value_FloatValue',0)
        rig.connectAttr(UpRV+'.outValue',UpGrp+'.Up')
        rig.connectAttr(UpDSB+'.distance',UpRV+'.inputValue') 
         
        rig.connectAttr(DnPOF+'.result.position',DnDSB+'.point1')     
        rig.connectAttr(CPS+'.position',DnDSB+'.point2')        
        DnRV = rig.createNode('remapValue',n = sign+'_Dn_RV',ss = True)
        rig.setAttr(DnRV+'.inputMin',0)
        rig.connectAttr(LengthMD+'.outputX',DnRV+'.inputMax')
        rig.setAttr(DnRV+'.outputMin',0)
        rig.setAttr(DnRV+'.outputMax',1)
        rig.setAttr(DnRV+'.value[0].value_Position',0)
        rig.setAttr(DnRV+'.value[0].value_FloatValue',1)
        rig.setAttr(DnRV+'.value[1].value_Position',1)
        rig.setAttr(DnRV+'.value[1].value_FloatValue',0)
        rig.connectAttr(DnRV+'.outValue',UpGrp+'.Dn')
        rig.connectAttr(DnDSB+'.distance',DnRV+'.inputValue') 
        
        rig.connectAttr(FnPOF+'.result.position',FnDSB+'.point1')     
        rig.connectAttr(CPS+'.position',FnDSB+'.point2')        
        FnRV = rig.createNode('remapValue',n = sign+'_Fn_RV',ss = True)
        rig.setAttr(FnRV+'.inputMin',0)
        rig.connectAttr(LengthMD+'.outputX',FnRV+'.inputMax')
        rig.setAttr(FnRV+'.outputMin',0)
        rig.setAttr(FnRV+'.outputMax',1)
        rig.setAttr(FnRV+'.value[0].value_Position',0)
        rig.setAttr(FnRV+'.value[0].value_FloatValue',1)
        rig.setAttr(FnRV+'.value[1].value_Position',1)
        rig.setAttr(FnRV+'.value[1].value_FloatValue',0)
        rig.connectAttr(FnRV+'.outValue',UpGrp+'.Fn')
        rig.connectAttr(FnDSB+'.distance',FnRV+'.inputValue') 
        
        rig.connectAttr(BcPOF+'.result.position',BcDSB+'.point1')     
        rig.connectAttr(CPS+'.position',BcDSB+'.point2')        
        BcRV = rig.createNode('remapValue',n = sign+'_Bc_RV',ss = True)
        rig.setAttr(BcRV+'.inputMin',0)
        rig.connectAttr(LengthMD+'.outputX',BcRV+'.inputMax')
        rig.setAttr(BcRV+'.outputMin',0)
        rig.setAttr(BcRV+'.outputMax',1)
        rig.setAttr(BcRV+'.value[0].value_Position',0)
        rig.setAttr(BcRV+'.value[0].value_FloatValue',1)
        rig.setAttr(BcRV+'.value[1].value_Position',1)
        rig.setAttr(BcRV+'.value[1].value_FloatValue',0)
        rig.connectAttr(BcRV+'.outValue',UpGrp+'.Bc')
        rig.connectAttr(BcDSB+'.distance',BcRV+'.inputValue')    


        