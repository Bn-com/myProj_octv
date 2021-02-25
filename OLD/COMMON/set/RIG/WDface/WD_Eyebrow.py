#-*- coding: utf-8 -*-

import maya.cmds as rig
import RIG.WDface.WD_MainClass as CA

class RigStart():
    def __init__(self):
        self.model = []
        print 'eyebrow'
        self.grp = 'Eyebrow_Control_GRP'
    
    def done(self):
        pass
#        rig.group(empty = True, n = self.grp)