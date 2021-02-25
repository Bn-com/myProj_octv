#-*- coding: utf-8 -*-

import maya.cmds as rig
import RIG.WDface.WD_MainClass as CA
from RIG.face.controlers import CreateControler

class ConnectVis():
    def __init__(self):
        self.con = 'JawMain_M'
        self.attrs = ['microControls', 'macroControls', 'mainControls', 'tongueControls', 'teethControls', 'earControls', 'eyeControls']
        self.groups = [u'Eyebrow_Control_GRP', u'Main_Control_GRP',u'Head_Control_GRP', u'Tooth_Control_GRP', u'Tongue_Control_GRP', u'Eye_Control_GRP', u'Ear_Control_GRP']
    
    
    def getConnectAttr(self, grp):
        if 'Eyebrow_Control_GRP' == grp:
            if not rig.attributeQuery('mainControls',node = self.con,ex = True):
                rig.addAttr(self.con, at = 'enum',ln = 'mainControls' , en = 'off:on:', k = True) 
                
            rig.connectAttr(self.con+'.mainControls', grp+'.mainVis') 
            rig.setAttr(self.con+'.mainControls', k = False, cb = True) 
            
            if not rig.attributeQuery('macroControls',node = self.con,ex = True):
                rig.addAttr(self.con, at = 'enum',ln = 'macroControls' , en = 'off:on:', k = True) 
                
            rig.connectAttr(self.con+'.macroControls', grp+'.macroVis') 
            rig.setAttr(self.con+'.macroControls', k = False, cb = True)         
        
        elif 'Head_Control_GRP' == grp:
            if not rig.attributeQuery('mainControls',node = self.con,ex = True):
                rig.addAttr(self.con, at = 'enum',ln = 'mainControls' , en = 'off:on:', dv = True, k = True) 
                
            rig.connectAttr(self.con+'.mainControls', grp+'.mainVis') 
            rig.setAttr(self.con+'.mainControls', k = False, cb = True)            
            
            if not rig.attributeQuery('macroControls',node = self.con,ex = True):
                rig.addAttr(self.con, at = 'enum',ln = 'macroControls' , en = 'off:on:', k = True) 
                
            rig.connectAttr(self.con+'.macroControls', grp+'.macroVis') 
            rig.setAttr(self.con+'.macroControls', k = False, cb = True) 
        
        elif 'Tooth_Control_GRP' == grp:
            if not rig.attributeQuery('teethControls',node = self.con,ex = True):
                rig.addAttr(self.con, at = 'enum',ln = 'teethControls' , en = 'off:on:', k = True) 
                
            rig.connectAttr(self.con+'.teethControls', grp+'.conVis') 
            rig.setAttr(self.con+'.teethControls', k = False, cb = True) 
        
        
        elif 'Tongue_Control_GRP' == grp:
            if not rig.attributeQuery('tongueControls',node = self.con,ex = True):
                rig.addAttr(self.con, at = 'enum',ln = 'tongueControls' , en = 'off:on:', k = True) 
                
            rig.connectAttr(self.con+'.tongueControls', grp+'.conVis') 
            rig.setAttr(self.con+'.tongueControls', k = False, cb = True) 
        
        
        elif 'Eye_Control_GRP' == grp:
            if not rig.attributeQuery('eyeControls',node = self.con,ex = True):
                rig.addAttr(self.con, at = 'enum',ln = 'eyeControls' , en = 'off:on:', k = True) 
                
            rig.connectAttr(self.con+'.eyeControls', grp+'.conVis') 
            rig.setAttr(self.con+'.eyeControls', k = False, cb = True) 
            
        elif 'Ear_Control_GRP' == grp:
            if not rig.attributeQuery('earControls',node = self.con,ex = True):
                rig.addAttr(self.con, at = 'enum',ln = 'earControls' , en = 'off:on:', k = True) 
                
            rig.connectAttr(self.con+'.earControls', grp+'.conVis') 
            rig.setAttr(self.con+'.earControls', k = False, cb = True) 
        
        elif 'Main_Control_GRP' == grp:
            if not rig.attributeQuery('microControls',node = self.con,ex = True) and rig.objExists('Head_Control_GRP'):
                rig.addAttr(self.con, at = 'enum',ln = 'microControls' , en = 'off:on:', k = True) 
                
            rig.connectAttr(self.con+'.microControls', grp+'.smallVis') 
            rig.setAttr(self.con+'.microControls', k = False, cb = True) 

    def Connect(self):
        for grp in self.groups:
            if rig.objExists(grp):
                self.getConnectAttr(grp)
                
    def breakVis(self):
        conAttr = rig.listRelatives(self.con, p = True)[0]+'.visibility'
        plug = rig.listConnections(conAttr, d = False, s = True, p = True)[0]
        rig.disconnectAttr(plug, conAttr)
        
    def hideObj(self):  
        pass
                      
    def done(self):
        self.breakVis()
        self.Connect()
    