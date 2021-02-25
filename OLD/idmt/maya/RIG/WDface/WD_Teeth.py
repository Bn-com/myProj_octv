#-*- coding: utf-8 -*-

import maya.cmds as rig
import RIG.WDface.WD_MainClass as CA
from RIG.face.controlers import CreateControler

class RigStart():
    def __init__(self):
        self.model = []
        self.grp = 'Tooth_Control_GRP'
        
        print 'teeth'
    
    
    def getData(self):
        self.jnts = [con for con in rig.listConnections(self.grp+'.CTRLJoint', s = False, d = True)]
        self.scale = CA.distance().getScale(self.jnts[0], self.jnts[-1], 0.35)
        
        self.Connect = CA.connectAttribute()
        self.Connect.attrType = 'long'
        self.Connect.sourceAttr = 'CTRLCurve'  
        self.Connect.targetAttr = 'CTRLCurve'      
    
    def setupTeeth(self):
        allCons = []
        conGrps = []
        ConObj = CreateControler(13, (0.1*self.scale, 0.1*self.scale, 0.1*self.scale))
        ConObj.signValue = 54861
        for i,jnt in enumerate(self.jnts):
            jntMat = rig.getAttr(jnt+'.worldMatrix')
            con = ConObj.SK_b08(jnt.split('_')[0]+'_M')
            allCons.append(con)
            rig.xform(con, ro = (90, 0, 0), wd = True)
            rig.makeIdentity(apply = True, r = True)
            rig.xform(con, m = jntMat)
            
            conGrp = CA.addGrp().grp(con, 'Freeze')
            conGrps.append(conGrp)
            
            rig.parentConstraint(con, jnt, mo = True)
            rig.scaleConstraint(con, jnt, mo = True)
        
        self.Connect.connect(self.grp, allCons)#连接控制器属性
        newGrp = rig.group(conGrps, n = self.grp+'_CTRLGrp')
        rig.parent(newGrp, self.grp)
    
    
        #连接visibility属性
        Connect = CA.connectAttribute()
        Connect.sourceAttr = 'conVis'
        Connect.targetAttr = 'visibility'
        Connect.connect(self.grp, [rig.listRelatives(con, p = True)[0] for con in allCons])
        

    def Groups(self):
        rig.parent(self.grp, CA.getRigGrp().createGrp())
        
    #创建Set
    def skinSet(self):
        infs = rig.listConnections(self.grp+'.CTRLJoint', s = False, d = True)
        InfSets = CA.addSets()
        InfSets.componentSets = 'Face_UpTeeth_Sets'
        InfSets.startAdd(infs[0])
        InfSets.componentSets = 'Face_DnTeeth_Sets'
        InfSets.startAdd(infs[1])
    
    #增加rigging属性
    def addRiggingAttr(self):
        rig.addAttr(self.grp, at = 'long', ln = 'rigging', dv = 1)
                      
    def done(self):
        self.getData()
        self.addRiggingAttr()
        self.setupTeeth()
        self.Groups()
        self.skinSet()
    