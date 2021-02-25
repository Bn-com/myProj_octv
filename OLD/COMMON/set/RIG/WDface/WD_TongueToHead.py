#-*- coding: utf-8 -*-

import maya.cmds as rig

class tongueToHead():
    def __init__(self):
        self.jaw = 'Dn_LipMove_Up'
        self.grp = 'Tongue_Control_GRP'
        

    def addControl(self):
        jawCon = 'JawMain_M'
        jawJnt = 'Jaw_Joint'
        jawConParent = rig.listRelatives(jawCon, p = True)[0]
        
        rig.addAttr(jawConParent, at = 'float', ln = 'tongue', k = True)
        rig.setAttr(jawConParent+'.tongue',l = True)        
        rig.addAttr(jawConParent, at = 'float', ln = 'tongueRX', k = True)
        rig.addAttr(jawConParent, at = 'float', ln = 'tongueRY', k = True)
        rig.addAttr(jawConParent, at = 'float', ln = 'tongueRZ', k = True)
        rig.addAttr(jawConParent, at = 'float', ln = 'tongueTZ', k = True, dv = 0.5)
        
        tongueGrp = rig.group(self.grp, n = self.grp+'_Rotate')
        rig.xform(tongueGrp, os = True, piv = (0, 0, 0))
        tongueRoMD = rig.createNode('multiplyDivide', n = self.grp+'_Roate_MD')
        rig.connectAttr(self.jaw+'.rotate', tongueRoMD+'.input2')
        rig.connectAttr(jawConParent+'.tongueRX', tongueRoMD+'.input1X')
        rig.connectAttr(jawConParent+'.tongueRY', tongueRoMD+'.input1Y')
        rig.connectAttr(jawConParent+'.tongueRZ', tongueRoMD+'.input1Z')
        
        rig.connectAttr(tongueRoMD+'.output', tongueGrp+'.rotate') 
        
        
        tongueTrMD = rig.createNode('multiplyDivide', n = self.grp+'_Translate_MD')
        rig.connectAttr(jawJnt+'.tz', tongueTrMD+'.input1X')  
        rig.connectAttr(jawConParent+'.tongueTZ', tongueTrMD+'.input2X') 
        rig.connectAttr(tongueTrMD+'.outputX', tongueGrp+'.tz')
        
                                 
    def done(self):
        rig.parent(self.grp, self.jaw)
        self.addControl()
    