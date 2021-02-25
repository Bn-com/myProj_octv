#-*- coding: utf-8 -*-

import maya.cmds as rig
import RIG.WDface.WD_MainClass as CA

class eyeToHead():
    def __init__(self):
        self.faceRig = CA.getRigGrp().createGrp()
        self.grp = 'Eye_Control_GRP'
        self.rigDeformGrp = 'Head_FaceDeformers_GRP'
        
    def followSetup(self):
        eye = 'Eye_M'
        eyeParent = rig.listRelatives(eye, p = True)[0]
        rig.addAttr(eye, at = 'enum', ln = 'eyeFollow', en = 'on:off:', dv = 0, k = True)
        
        parentNode = rig.parentConstraint(self.rigDeformGrp, eyeParent, mo = True)[0]
        rig.connectAttr(eye+'.eyeFollow', parentNode+'.'+self.rigDeformGrp+'W0')
                                 
    def done(self):
        rig.parent(self.grp, self.faceRig)
        self.followSetup()
