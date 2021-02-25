#***************************************************************************
# Script Name: mi_setupFix
# Author: Justin.CHan
# Created: 2015-12-24
# Description: ##
#
#***************************************************************************
# -*- coding: utf-8 -*-
import maya.cmds as mc
def mi_setupFix():
    AA = mc.ls('*_shoulder_GRP')
    chest =  'chest1_jnt'
    CharacterCon = 'Character'
    for aa in AA:
        prefix = aa.split('_')[0]
        shoulderCon = prefix+'_shoulder'
        Ctrl = prefix+'_shoulder'
        CtrlGRP = prefix+'Arm_ALL_CTRL_GRP'
        CtrlGRP_GRP = CtrlGRP+'_GRP'
        Constraint = prefix+'Arm_ALL_CTRL_GRP_orientConstraint1'
        ArmAllConGRP = mc.group(CtrlGRP,n = CtrlGRP_GRP )
        mc.setAttr(ArmAllConGRP+'.rotatePivot',0,0,0)
        mc.setAttr(ArmAllConGRP+'.scalePivot',0,0,0)
        mc.setAttr(Constraint+'.w0',l=0)
        mc.disconnectAttr(Ctrl+'.Arm_follow',Constraint+'.w0')
        shoulderGRP_OrientConstraint = mc.orientConstraint(CharacterCon,ArmAllConGRP,mo = True)[0]
        inSelectGrp = mc.group(empty = True,n = prefix+'Arm_inShoulder_select')
        outSelectGrp = mc.group(empty = True,n = prefix+'Arm_outShoulder_select')
        selNode = mc.createNode('choice',n = prefix+'_ArmShoulder_SC',ss = True)
        mc.setAttr(inSelectGrp+'.translate',0,0,0)
        mc.setAttr(inSelectGrp+'.rotate',0,57.296,0)
        mc.setAttr(inSelectGrp+'.scale',0,0,1)
        mc.connectAttr(inSelectGrp+'.translate',selNode+'.input[0]')
        mc.connectAttr(inSelectGrp+'.rotate',selNode+'.input[1]')
        mc.connectAttr(inSelectGrp+'.scale',selNode+'.input[2]')
        mc.connectAttr(shoulderCon+'.Arm_follow',selNode+'.selector')
        mc.connectAttr(selNode+'.output',outSelectGrp+'.translate')
        mc.connectAttr(outSelectGrp+'.ty',Constraint+'.chest1_jntW0')
        mc.connectAttr(outSelectGrp+'.tz',shoulderGRP_OrientConstraint+'.'+CharacterCon+'W0')
        selectGrp = mc.group(inSelectGrp,outSelectGrp,n = prefix+'_ShoulderSelect_Grp')
        mc.parent(selectGrp,shoulderCon)
        mc.addAttr(Ctrl+'.Arm_follow',e=1,enumName =  'on:chest:world:')
mi_setupFix()