# -*- coding: utf-8 -*-
import maya.cmds as mc
import maya.mel as mel

def North_Arm_Follw():
	if mc.objExists('FKCurveScapula_L'):
		Ctrl_L = 'FKCurveScapula_L'
		Ctrl_L_Attr = 'FKCurveScapula_L.Arm_follow'
		if mc.objExists(Ctrl_L_Attr)!=True:
		    mc.addAttr(Ctrl_L,ln = 'Arm_follow',at = 'enum',en = 'on:off:')
		    mc.setAttr(Ctrl_L_Attr,e=1,keyable = 1)
		    mc.delete('FKParentConstraintElbow_L_parentConstraint1')
		    mc.parentConstraint('FKShoulder_L','FKDrawElbow_L',mo=1)
		    OC_FKJoint = mc.orientConstraint('Chest_M','FKParentConstraintElbow_L',mo=1)
		    OC_FKCtrl = mc.orientConstraint('Chest_M','FKExtraShoulder_L',mo=1)
		    mc.connectAttr(Ctrl_L_Attr,(OC_FKJoint[0]+'.Chest_MW0'))
		    mc.connectAttr(Ctrl_L_Attr,(OC_FKCtrl[0]+'.Chest_MW0'))
		    mc.select (cl=1)
		    
	if mc.objExists('FKCurveScapula_R'):
		Ctrl_R = 'FKCurveScapula_R'
		Ctrl_R_Attr = 'FKCurveScapula_R.Arm_follow'
		if mc.objExists(Ctrl_R_Attr)!=True:
		    mc.addAttr(Ctrl_R,ln = 'Arm_follow',at = 'enum',en = 'on:off:')
		    mc.setAttr(Ctrl_R_Attr,e=1,keyable = 1)
		    mc.delete('FKParentConstraintElbow_R_parentConstraint1')
		    mc.parentConstraint('FKShoulder_R','FKDrawElbow_R',mo=1)
		    OC_FKJoint = mc.orientConstraint('Chest_M','FKParentConstraintElbow_R',mo=1)
		    OC_FKCtrl = mc.orientConstraint('Chest_M','FKExtraShoulder_R',mo=1)
		    mc.connectAttr(Ctrl_R_Attr,(OC_FKJoint[0]+'.Chest_MW0'))
		    mc.connectAttr(Ctrl_R_Attr,(OC_FKCtrl[0]+'.Chest_MW0'))
		    mc.select (cl=1)

	if mc.objExists('FKCurveScapul_L'):
		Ctrl_L = 'FKCurveScapul_L'
		Ctrl_L_Attr = 'FKCurveScapul_L.Arm_follow'
		if mc.objExists(Ctrl_L_Attr)!=True:
		    mc.addAttr(Ctrl_L,ln = 'Arm_follow',at = 'enum',en = 'on:off:')
		    mc.setAttr(Ctrl_L_Attr,e=1,keyable = 1)
		    mc.delete('FKParentConstraintElbow_L_parentConstraint1')
		    mc.parentConstraint('FKShoulder_L','FKDrawElbow_L',mo=1)
		    OC_FKJoint = mc.orientConstraint('Chest_M','FKParentConstraintElbow_L',mo=1)
		    OC_FKCtrl = mc.orientConstraint('Chest_M','FKExtraShoulder_L',mo=1)
		    mc.connectAttr(Ctrl_L_Attr,(OC_FKJoint[0]+'.Chest_MW0'))
		    mc.connectAttr(Ctrl_L_Attr,(OC_FKCtrl[0]+'.Chest_MW0'))
		    mc.select (cl=1)

	if mc.objExists('FKCurveScapul_R'):
		Ctrl_R = 'FKCurveScapul_R'
		Ctrl_R_Attr = 'FKCurveScapul_R.Arm_follow'
		if mc.objExists(Ctrl_R_Attr)!=True:
		    mc.addAttr(Ctrl_R,ln = 'Arm_follow',at = 'enum',en = 'on:off:')
		    mc.setAttr(Ctrl_R_Attr,e=1,keyable = 1)
		    mc.delete('FKParentConstraintElbow_R_parentConstraint1')
		    mc.parentConstraint('FKShoulder_R','FKDrawElbow_R',mo=1)
		    OC_FKJoint = mc.orientConstraint('Chest_M','FKParentConstraintElbow_R',mo=1)
		    OC_FKCtrl = mc.orientConstraint('Chest_M','FKExtraShoulder_R',mo=1)
		    mc.connectAttr(Ctrl_R_Attr,(OC_FKJoint[0]+'.Chest_MW0'))
		    mc.connectAttr(Ctrl_R_Attr,(OC_FKCtrl[0]+'.Chest_MW0'))
		    mc.select (cl=1)

	else:
		mc.error(u'===========【！！！注意肩膀控制器名称有异！！！】===========')
		    	    
def North_FMcam():
	FM_cams = 'FM_facialCtrl_cam*'
	if mc.objExists(FM_cams)!=True:
		FM_cam = mc.camera(name = 'FM_facialCtrl_cam',orthographic = 1,orthographicWidth = '5')
		PintC_FM = mc.pointConstraint ('FacialCurve',FM_cam[0],offset =(0,0,0))
		mc.delete(PintC_FM)
		mc.setAttr ((FM_cam[0]+'.translateZ'),5)
		mc.setAttr ((FM_cam[0]+'.visibility'),0)
		mc.parent (FM_cam[0],'FacialCurve')
		mc.select (cl=1)
		
def North_IKPole():
	Ctrl_L = 'IKPoleVectorCurveLeg_L'
	Ctrl_L_Attr = 'IKPoleVectorCurveLeg_L.Auto'
	Ctrl_L_GRP = 'IKPoleVectorCurveLeg_L_GRP'	
	Hip_L = 'Hip_L'
	xformHip = mc.xform(Hip_L,q=1,ws=1,sp=1)	
	Leg_IK = 'IKCurveLeg_L'
	if mc.objExists(Ctrl_L_Attr) != True:
		mc.addAttr(Ctrl_L,ln = 'Auto',at = 'enum',en = 'off:on:')
		mc.setAttr(Ctrl_L_Attr,e=1,keyable = 1)
		mc.setAttr(Ctrl_L_Attr,1)
		mc.group(em=True, name = Ctrl_L_GRP)
		mc.setAttr(Ctrl_L_GRP+'.translate',xformHip[0],xformHip[1],xformHip[2])
		mc.parent(Ctrl_L_GRP,'IKPoleVectorExtraLeg_L')
		mc.makeIdentity( Ctrl_L_GRP,apply=True, t=1, r=1, s=1, n=2 )
		mc.parent(Ctrl_L,Ctrl_L_GRP)
		Locator = mc.spaceLocator(n = Ctrl_L+'_Auto_Lc')[0]
		mc.parent(Locator,Leg_IK)
		mc.setAttr(Locator+'.translate',-1,0,0)
		mc.setAttr(Locator+'.visibility',0)		
		ACo = mc.aimConstraint(Leg_IK,Ctrl_L_GRP,mo=1,weight= 1,worldUpType='object',worldUpObject=Locator)[0]
		mc.connectAttr(Ctrl_L_Attr,(ACo+'.'+Leg_IK+'W0')) 
		mc.select (cl=1)
	Ctrl_R = 'IKPoleVectorCurveLeg_R'
	Ctrl_R_Attr = 'IKPoleVectorCurveLeg_R.Auto'
	Ctrl_R_GRP = 'IKPoleVectorCurveLeg_R_GRP'	
	Hip_R = 'Hip_R'
	xformHip = mc.xform(Hip_R,q=1,ws=1,sp=1)	
	Leg_IK = 'IKCurveLeg_R'
	if mc.objExists(Ctrl_R_Attr) != True:
		mc.addAttr(Ctrl_R,ln = 'Auto',at = 'enum',en = 'off:on:')
		mc.setAttr(Ctrl_R_Attr,e=1,keyable = 1)
		mc.setAttr(Ctrl_R_Attr,1)
		mc.group(em=True, name = Ctrl_R_GRP)
		mc.setAttr(Ctrl_R_GRP+'.translate',xformHip[0],xformHip[1],xformHip[2])
		mc.parent(Ctrl_R_GRP,'IKPoleVectorExtraLeg_R')
		mc.makeIdentity( Ctrl_R_GRP,apply=True, t=1, r=1, s=1, n=2 )
		mc.parent(Ctrl_R,Ctrl_R_GRP)
		Locator = mc.spaceLocator(n = Ctrl_R+'_Auto_Lc')[0]
		mc.parent(Locator,Leg_IK)
		mc.setAttr(Locator+'.translate',-1,0,0)
		mc.setAttr(Locator+'.visibility',0)		
		ACo = mc.aimConstraint(Leg_IK,Ctrl_R_GRP,mo=1,weight= 1,worldUpType='object',worldUpObject=Locator)[0]
		mc.connectAttr(Ctrl_R_Attr,(ACo+'.'+Leg_IK+'W0')) 	
		mc.select (cl=1)
		
def North_PloeLocator():
	if mc.objExists('FKPoleVectorCurveArm_L')!=True:		
		mc.spaceLocator(position=(0,0,0),name = 'FKPoleVectorCurveArm_L')
		mc.parent ('FKPoleVectorCurveArm_L','IKPoleVectorCurveArm_L')
		mc.setAttr ('FKPoleVectorCurveArm_L.translate',0,0,0)
		mc.parent ('FKPoleVectorCurveArm_L','FKCurveShoulder_L')
		mc.setAttr('FKPoleVectorCurveArm_L.visibility',0)
	if mc.objExists('IKCurveArm_L_Locator')!=True:			
		mc.spaceLocator(position=(0,0,0),name = 'IKCurveArm_L_Locator')
		mc.parent ('IKCurveArm_L_Locator','IKCurveArm_L')
		mc.setAttr ('IKCurveArm_L_Locator.translate',0,0,0)
		mc.parent ('IKCurveArm_L_Locator','FKCurveWrist_L')	
		mc.setAttr('IKCurveArm_L_Locator.visibility',0)
	if mc.objExists('FKPoleVectorCurveArm_R')!=True:		
		mc.spaceLocator(position=(0,0,0),name = 'FKPoleVectorCurveArm_R')
		mc.parent ('FKPoleVectorCurveArm_R','IKPoleVectorCurveArm_R')
		mc.setAttr ('FKPoleVectorCurveArm_R.translate',0,0,0)
		mc.parent ('FKPoleVectorCurveArm_R','FKCurveShoulder_R')
		mc.setAttr('FKPoleVectorCurveArm_R.visibility',0)
	if mc.objExists('IKCurveArm_R_Locator')!=True:		
		mc.spaceLocator(position=(0,0,0),name = 'IKCurveArm_R_Locator')
		mc.parent ('IKCurveArm_R_Locator','IKCurveArm_R')
		mc.setAttr ('IKCurveArm_R_Locator.translate',0,0,0)
		mc.parent ('IKCurveArm_R_Locator','FKCurveWrist_R')
		mc.setAttr('IKCurveArm_R_Locator.visibility',0)	
		
	if mc.objExists('FKPoleVectorCurveLeg_L')!=True:	
		mc.spaceLocator(position=(0,0,0),name = 'FKPoleVectorCurveLeg_L')
		mc.parent ('FKPoleVectorCurveLeg_L','IKPoleVectorCurveLeg_L')
		mc.setAttr ('FKPoleVectorCurveLeg_L.translate',0,0,0)
		mc.parent ('FKPoleVectorCurveLeg_L','FKCurveHip_L')
		mc.setAttr('FKPoleVectorCurveLeg_L.visibility',0)	
				
	if mc.objExists('IKCurveLeg_L_Locator')!=True:			
		mc.spaceLocator(position=(0,0,0),name = 'IKCurveLeg_L_Locator')
		mc.parent ('IKCurveLeg_L_Locator','IKCurveLeg_L')
		mc.setAttr ('IKCurveLeg_L_Locator.translate',0,0,0)
		mc.parent ('IKCurveLeg_L_Locator','FKCurveAnkle_L')
		mc.setAttr('IKCurveLeg_L_Locator.visibility',0)	
				
	if mc.objExists('FKPoleVectorCurveLeg_R')!=True:			
		mc.spaceLocator(position=(0,0,0),name = 'FKPoleVectorCurveLeg_R')
		mc.parent ('FKPoleVectorCurveLeg_R','IKPoleVectorCurveLeg_R')
		mc.setAttr ('FKPoleVectorCurveLeg_R.translate',0,0,0)
		mc.parent ('FKPoleVectorCurveLeg_R','FKCurveHip_R')	
		mc.setAttr('FKPoleVectorCurveLeg_R.visibility',0)	
				
	if mc.objExists('IKCurveLeg_R_Locator')!=True:		
		mc.spaceLocator(position=(0,0,0),name = 'IKCurveLeg_R_Locator')
		mc.parent ('IKCurveLeg_R_Locator','IKCurveLeg_R')
		mc.setAttr ('IKCurveLeg_R_Locator.translate',0,0,0)
		mc.parent ('IKCurveLeg_R_Locator','FKCurveAnkle_R')
		mc.setAttr('IKCurveLeg_R_Locator.visibility',0)	
	try:
		mc.setAttr('FKCurveMiddleToe1_R.rotateX',k = 1,l = 0)
		mc.setAttr('FKCurveMiddleToe1_R.rotateY',k = 1,l = 0)
		mc.transformLimits('FKCurveMiddleToe1_R',erx=(0,0),ery=(0,0),erz=(0,0),rx=(0,0),ry=(0,0),rz=(0,0))
	except:
		pass
	try:
		mc.setAttr('FKCurveMiddleToe1_L.rotateX',k = 1,l = 0)
		mc.setAttr('FKCurveMiddleToe1_L.rotateY',k = 1,l = 0)
		mc.transformLimits('FKCurveMiddleToe1_L',erx=(0,0),ery=(0,0),erz=(0,0),rx=(0,0),ry=(0,0),rz=(0,0))
	except:
		pass
	
def North_eyeSlidersControl():
	CtrlNames = ['r_eye_Sliders','l_eye_Sliders']
	AttrNames = ['LowSqueeze','UpNeutral','LowNeutral','Tight','UpAngry',
'LowAngry','UpHappy','LowHappy','UpSad','LowSad','Squeeze','UpSqueeze',
'LowThickness','UpThickness','EyeTopOffset','EyeBottomOffset','EyeDamp']
	for CtrlName in CtrlNames:
	    if mc.objExists(CtrlName+'.setUp')!=True:
	        mc.addAttr(CtrlName,ln = 'setUp',at = 'long')
	        for AttrName in AttrNames:
	            sourceAttr = CtrlName+'.'+AttrName
	            disAttr = mc.listConnections(CtrlName+'.'+AttrName , s = 0, d=1, plugs = 1)[0]
	            if 'l_eye_' in CtrlName:
	                clampNode = mc.createNode('clamp',n = AttrName+'_clamp_L')  
	            if 'r_eye_' in CtrlName:
	                clampNode = mc.createNode('clamp',n = AttrName+'_clamp_R')                                     
	            mc.setAttr(clampNode+'.minR',0)
	            mc.setAttr(clampNode+'.maxR',1)
	            if 'EyeBottomOffset' in AttrName:
	                mc.setAttr(clampNode+'.minR',-1)
	            if 'EyeTopOffset' in AttrName:
                	mc.setAttr(clampNode+'.minR',-1)                                
	            mc.connectAttr(sourceAttr,clampNode+'.inputR')
	            mc.disconnectAttr(sourceAttr,disAttr)
	            mc.connectAttr(clampNode+'.outputR',disAttr)
	            mc.select(cl=1)
            print u'===成功添加0~1锁定范围==='
        else:
			mc.warning(u'=====已添加0~1锁定范围=====')	