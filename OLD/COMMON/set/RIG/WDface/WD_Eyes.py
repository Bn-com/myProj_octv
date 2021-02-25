#-*- coding: utf-8 -*-

import maya.cmds as rig
import RIG.WDface.WD_MainClass as CA
import maya.OpenMaya as om
import re

class RigStart():
    def __init__(self):
        self.model = []
        self.eye = 'Eye_Control_GRP'
        self.axis = 'Y'
        self.scale = 1.0
        
    def getData(self):
        GRP = CA.getRigGrp()
        self.rigGrp = GRP.createGrp()
        GRP.grp = self.eye+'_Loc'
        self.aimLoctorGrp = GRP.createGrp()
        
        self.allCons = [con for con in rig.listConnections(self.eye+'.CTRLCurve', s = False, d = True)]
        jnts = [jnt for jnt in rig.listConnections(self.eye+'.CTRLJoint', s = False, d = True)]
        
        if 1 == len(jnts):
            self.jnts = [jnt for jnt in jnts if not re.match('\ALf_|\ARt_',jnt)]
            
        else:
            self.jnts = [jnt for jnt in jnts if re.match('\ALf_|\ARt_',jnt)] 
    
    
        self.lips = [con for con in self.allCons if re.match('.+Lid_\d+M',con)]

    def getScale(self):
        self.scale = CA.distance().getScale(self.allCons[0], self.jnts[0], 0.269401452279) 
          
    #--------------------------------------------------------------------- 对眼睛骨骼aim约束
    def aimEye(self):
        for jnt in self.jnts:
            jntParent = rig.listRelatives(jnt, p = True)[0]
            jntMat = rig.getAttr(jnt+'.worldMatrix')
            locGrp = rig.group(empty = True, n = jnt+'_Loc_GRP')
            rig.xform(locGrp, m = jntMat)
            
            origenTranslate = rig.getAttr(locGrp+'.translate'+self.axis)
            rig.setAttr(locGrp+'.translate'+self.axis, origenTranslate + self.scale*2)
            
            aimNode = rig.aimConstraint(jnt.replace('Joint', 'M') ,jnt, aimVector = (0, 0, 1), upVector = (0, 1, 0), worldUpType = 'object', worldUpObject = locGrp, mo = False) 
            
            curMat = rig.getAttr(jnt+'.worldMatrix')
            conGrp = rig.group(empty = True, n = jnt+'_CTRL_GRP')
            rig.xform(conGrp, m = curMat)
            rig.parent(conGrp, jntParent)
            
            con = jnt.replace('Joint', 'M')#得到控制器名字
            rig.addAttr(con, at = 'float', ln = 'eyelidFollow', dv = 0, min = 0, k = True)
            MD = rig.createNode('multiplyDivide', n = jnt+'_rotate_MD', ss = True)
            rig.connectAttr(jnt+'.rotate', MD+'.input1')
            rig.connectAttr(con+'.eyelidFollow', MD+'.input2X')
            rig.connectAttr(con+'.eyelidFollow', MD+'.input2Y')
            rig.connectAttr(con+'.eyelidFollow', MD+'.input2Z')
            rig.connectAttr(MD+'.output', conGrp+'.rotate')
            
            
            rig.parent(locGrp ,self.aimLoctorGrp)
            
    
    #-------------------------------------------------------------------- 增加眼皮设置
    def eyeLid(self):
        self.newAddJnts = []
        for lip in self.lips:
            rig.select(cl = True)
            pos = rig.xform(lip, q = True, t = True, ws = True)
            Njnt = rig.joint(p = pos, n = lip+'_Joint')
#            self.newAddJnts.append(Njnt)
            rig.hide(Njnt)
            NjntGrp = rig.group(Njnt, n = Njnt+'_GRP')
            
            jntTemp = re.compile('_UpLid_|_DnLid_').sub('_Eye_',lip)
            jnt = re.compile('M\Z').sub('Joint',jntTemp)
            lipGrp = rig.group(empty = True, n = lip+'_GRP')
            lipGrpUp = rig.group(lipGrp, n = lip+'_GRP_UP')
            lipGrpTop = rig.group(lipGrpUp, n = lip+'_GRP_TOP')
            jntParent = rig.listRelatives(jnt, p = True)[0]
            jntMat = rig.getAttr(jnt+'.worldMatrix')
            rig.xform(lipGrpTop, m = jntMat)
            aimNode = rig.aimConstraint(lip ,lipGrpTop, aimVector = (0, 0, 1), upVector = (0, 1, 0), worldUpType = 'object', worldUpObject = jnt+'_Loc_GRP') 
            rig.delete(aimNode)
            
            lipCon = CA.addGrp().grp(lip,'AimRotate')#增加 组
            
            #连接旋转和位移
            rig.connectAttr(lip+'.rotateZ', lipGrp+'.rotateZ')
            rig.connectAttr(lip+'.scaleX', lipGrp+'.scaleX')
            rig.connectAttr(lip+'.scaleZ', lipGrp+'.scaleZ')
            translateMD = rig.createNode('multiplyDivide', n = lip +'_translate_MD', ss = True)
            lipRoateGrp = rig.listRelatives(lip, p = True)[0]
            print lipRoateGrp
            rig.addAttr(lipRoateGrp, at = 'float', ln = 'Move', dv = -157/self.scale, k = True)
            rig.connectAttr(lip+'.translateY', translateMD+'.input1X')
            rig.connectAttr(lipRoateGrp+'.Move', translateMD+'.input2X')            
            rig.connectAttr(translateMD+'.outputX', lipGrpUp+'.rotateX')                 
            
            rig.parent(lipGrpTop, lipCon, jnt+'_CTRL_GRP')
            rig.parent(NjntGrp, lipGrp)
                  
        jnts = [jnt for jnt in rig.listConnections(self.eye+'.CTRLJoint', s = False, d = True)]#列出眼睛控制器骨骼，注意:不包含新增加的眼皮骨骼
        for jnt in jnts:
            con = re.compile('Joint\Z').sub('M',jnt)#得到控制器名字
            lipCon = CA.addGrp().grp(con,'freeze')#增加 组
    
    def extraAddLid(self):
        exLids = [con for con in self.allCons if re.match('.+LidMin_\d+M',con)]
        print exLids
        for lid in exLids:
            if re.match('Lf_', lid):
                LR = 'Lf_'
            else:
                LR = 'Rt_'
                
            if re.match('\w\w_Up', lid):
                UD = 'Up'
            elif re.match('\w\w_Dn', lid):
                UD = 'Dn'
            else:
                UD = None
                
            pos = rig.xform(lid, q = True, t = True)
            rig.select(cl = True)
            jnt = rig.joint(p = pos ,n = lid+'_Joint')#创建骨骼
            rig.parent(jnt, lid)
            rig.hide(jnt)
            self.newAddJnts.append(jnt)
            
            ConGrp = CA.addGrp().grp(lid, 'Rotate')
            
            if UD:
                parentJnt = LR+UD+'Lid_0M_GRP_UP'
                mat = rig.getAttr(parentJnt+'.worldMatrix')
                grp = rig.group(empty = True, n = ConGrp+'_Rotate')
                rig.xform(grp, m = mat)
                rig.parent(ConGrp, grp)                
                rig.parent(grp, LR+UD+'Lid_0M_GRP')
                
                parentLid = rig.listRelatives(lid, p = True)[0]
                if re.match('\w+_2M\Z', lid):
                    v = 1
                else:
                    v = -0.3
                rig.addAttr(parentLid, at = 'float', ln = 'RotateRX', k = True, dv = v)
#                rig.addAttr(parentLid, at = 'float', ln = 'RotateRY', k = True, dv = 1)
#                rig.addAttr(parentLid, at = 'float', ln = 'RotateRZ', k = True, dv = 1)
                RotateRoMD = rig.createNode('multiplyDivide', n = lid+'_Roate_MD')
                rig.connectAttr(parentJnt+'.rotate', RotateRoMD+'.input2')
                rig.connectAttr(parentLid+'.RotateRX', RotateRoMD+'.input1X')
#                rig.connectAttr(parentLid+'.RotateRY', RotateRoMD+'.input1Y')
#                rig.connectAttr(parentLid+'.RotateRZ', RotateRoMD+'.input1Z')
                rig.connectAttr(RotateRoMD+'.output', grp+'.rotate') 
                
#                rig.parent(ConGrp, LR+UD+'Lid_0M_GRP')
            else:
                parentJnt = LR+'Eye_0Joint_CTRL_GRP'
                rig.parent(ConGrp, parentJnt)
    
    def Groups(self):
        rig.parent(self.aimLoctorGrp, self.eye)
        
    
        #连接visibility属性
        Connect = CA.connectAttribute()
        Connect.sourceAttr = 'conVis'
        Connect.targetAttr = 'visibility'
        Connect.connect(self.eye, [rig.listRelatives(con, p = True)[0] for con in self.allCons])
        
    #创建Set
    def skinSet(self):
        InfSets = CA.addSets()
            
        infs = rig.listConnections(self.eye+'.CTRLJoint', s = False, d = True)
        for inf in infs:
            if re.match('\ALf_', inf):
                InfSets.componentSets = 'Face_LfEye_Sets'
                InfSets.startAdd(inf)    
            if re.match('\ARt_', inf):   
                InfSets.componentSets = 'Face_RtEye_Sets'
                InfSets.startAdd(inf)   
                
 
        InfSets.componentSets = 'Face_BsMesh_Sets'
        InfSets.startAdd(self.newAddJnts)                    

    #增加rigging属性
    def addRiggingAttr(self):
        rig.addAttr(self.eye, at = 'long', ln = 'rigging', dv = 1)

        
    def done(self):
        self.getData()
        self.getScale()
        self.addRiggingAttr()
        self.aimEye()
        self.eyeLid()
        self.extraAddLid()
        self.Groups()
        self.skinSet()
    