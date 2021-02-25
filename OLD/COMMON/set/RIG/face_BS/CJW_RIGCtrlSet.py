# -*- coding: utf-8 -*-
import maya.cmds as mc
import maya.mel as mel
import re
import headfile
AutoRigPath = headfile.__file__.replace('headfile.py','RIG/').replace('\\','/')

def CJW_RIGSetWIn(self):
    ui = AutoRigPath+'face_BS/CJW_RIGCtrlSet.myuis'
    if mc.window('CJW_RIGCtrlSetWin', ex=1):
        mc.deleteUI('CJW_RIGCtrlSetWin')
    mui = mc.loadUI(f=ui)
    mc.showWindow(mui)

    
def CJW_RIGCtrlSetTool():
    set = 'CtrlSet'
    mc.select(cl=1)
    if not mc.objExists(set):
        mc.sets(name = 'BodySet')
        mc.sets(name = 'Lf_ArmSet')
        mc.sets(name = 'Rt_ArmSet')
        mc.sets(name = 'Lf_FingerSet')
        mc.sets(name = 'Rt_FingerSet')
        mc.sets(name = 'Lf_LegSet')
        mc.sets(name = 'Rt_LetSet')
        mc.sets(name = 'Lf_ToesSet')
        mc.sets(name = 'Rt_ToesSet') 
        mc.sets(name = 'CtrlSet')
        mc.sets(name = 'All_BodySet')
        mc.sets('BodySet','Lf_ArmSet','Rt_ArmSet','Lf_FingerSet','Rt_FingerSet',
                'Lf_LegSet','Rt_LetSet','Lf_ToesSet','Rt_ToesSet',addElement='All_BodySet')        
        mc.sets('All_BodySet',addElement='CtrlSet')
        mc.sets(name = 'LookSet')
        mc.sets(name = 'BrowsSet')
        mc.sets(name = 'LipsSet')
        mc.sets(name = 'MouthSet')
        mc.sets(name = 'All_FacialSet')
        mc.sets('LookSet','BrowsSet','LipsSet','MouthSet',addElement='All_FacialSet')        
        mc.sets('All_FacialSet',addElement='CtrlSet')        