#-*- coding: utf-8 -*-

import maya.cmds as rig
import RIG.WDface.WD_MainClass as CA
import re


class createConSets():
    def __init__(self):
        self.allGroups = [u'Main_Control_GRP', u'Ear_Control_GRP', u'Eye_Control_GRP', u'Tongue_Control_GRP', u'Tooth_Control_GRP', u'Head_Control_GRP'] 
 
    def startCreateSet(self):
        consSet = CA.addSets()
        consSet.faceSets = 'face_controls_Sets'
        
        
        for grp in self.allGroups:
            if rig.objExists(grp):#如果组存在
                if 'Head_Control_GRP' == grp:
                    cons = rig.listConnections(grp+'.CTRLBsCurve', s = False, d = True)
                    MacroCons = rig.listConnections(grp+'.CTRLMacroCurve', s = False, d = True)
                    cons.extend(MacroCons)
                    
                else:
                    cons = rig.listConnections(grp+'.CTRLCurve', s = False, d = True)
                
                if cons:
                    consSet.componentSets = 'Face_'+grp.split('_')[0]+'_sets'
                    consSet.startAdd(self.exceptCons(cons))
                    
    def exceptCons(self, cons):#排除控制器
        allCons = [con for con in cons if not re.match('\w+_Back_\d+M', con)]#忽略背面控制器
        
        
        return allCons
        
            
            
            
            
    def done(self):
        self.startCreateSet()
    