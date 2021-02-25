#-*- coding: utf-8 -*-

import maya.cmds as rig
import RIG.WDface.WD_MainClass as CA
from RIG.face.controlers import CreateControler

class RigStart():
    def __init__(self):
        self.model = []
        print 'tongue'
        self.grp = 'Tongue_Control_GRP'
        
    
    
    def getData(self):
        self.jnts = [con for con in rig.listConnections(self.grp+'.CTRLJoint', s = False, d = True)]
        self.jnts =  CA.order().startOrder(self.jnts)#对数组进行排序
        self.scale = CA.distance().getScale(self.jnts[0], self.jnts[-1], 1.24976436649)
        
        self.Connect = CA.connectAttribute()
        self.Connect.attrType = 'long'
        self.Connect.sourceAttr = 'CTRLCurve'  
        self.Connect.targetAttr = 'CTRLCurve'        
    
    def setupTongue(self):
        #对骨骼校正轴向
        oj = 'zyx'
        secondaryAxisOrient = 'yup'
        orientJoints = [jnt for jnt in self.jnts]#排除不需要校正轴向的骨骼
        for jnt in orientJoints:
            rig.joint(jnt,e = True, oj = oj, secondaryAxisOrient = secondaryAxisOrient, ch = False, zso = True)
        rig.joint(self.jnts[-1],e = True, oj = 'none', ch = False, zso = True)
        
        
        #生成控制器并增加父子约束
        allCons = []
        preCon  = ''
        ConObj = CreateControler(13, (0.1*self.scale, 0.1*self.scale, 0.1*self.scale))
        ConObj.signValue = 32547
        for i,jnt in enumerate(self.jnts):
            jntMat = rig.getAttr(jnt+'.worldMatrix')
            con = ConObj.SK_b08(jnt.split('_')[0]+'_'+str(i)+'M')
            allCons.append(con)
            rig.xform(con, ro = (90, 0, 0), wd = True)
            rig.makeIdentity(apply = True, r = True)
            rig.xform(con, m = jntMat)
            
            conGrp = CA.addGrp().grp(con, 'Freeze')
            if i != 0:
                rig.parent(conGrp, preCon)
            preCon = con
            
            rig.parentConstraint(con, jnt, mo = True)
        
        self.Connect.connect(self.grp, allCons)#连接控制器属性
        
        #连接visibility属性
        self.Connect.sourceAttr = 'conVis'
        self.Connect.targetAttr = 'visibility'
        self.Connect.connect(self.grp, [rig.listRelatives(con, p = True)[0] for con in allCons])
        
    #创建Set
    def skinSet(self):
        InfSets = CA.addSets()
        InfSets.componentSets = 'Face_Tongue_Sets'
        infs = self.jnts
        InfSets.startAdd(infs)
    
    def Groups(self):
        rig.parent('Tongue_0M_Freeze_GRP_Top', self.grp)
        rig.parent(self.grp, CA.getRigGrp().createGrp())
    
    #增加rigging属性
    def addRiggingAttr(self):
        rig.addAttr(self.grp, at = 'long', ln = 'rigging', dv = 1)
                              
    def done(self):
        self.getData()
        self.addRiggingAttr()
        self.setupTongue()
        self.Groups()
        self.skinSet()
    