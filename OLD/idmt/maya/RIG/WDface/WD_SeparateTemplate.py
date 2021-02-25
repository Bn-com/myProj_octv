#-*- coding: utf-8 -*-

import maya.cmds as rig

class separateTemplate():
    def __init__(self):
        self.jntScale = rig.jointDisplayScale(q = True)#获得骨骼缩放值
        self.grps = [u'Main_Control_GRP', u'Ear_Control_GRP', u'Eye_Control_GRP', u'Eyebrow_Control_GRP', u'Tongue_Control_GRP', u'Tooth_Control_GRP', u'Head_Control_GRP']
        
    
    
    def startSeparate(self):
        #得到控制器
        conAndJnt = []
        for grp in self.grps:
            if rig.objExists(grp):
                transCons = rig.listConnections(grp, s = False, d = True, type = 'transform')
                if transCons:
                    cons = [con for con in transCons if rig.attributeQuery('sign', node = con, ex = True)]
                else:
                    cons = []
                 
                jnts = rig.listConnections(grp, s = False, d = True, type = 'joint')
                if cons:
                    conAndJnt.extend(cons)
                if jnts:
                    conAndJnt.extend(jnts)
        
        #得到位置信息
        conPositionInfo = []    
        for jnt in  conAndJnt:
            if rig.nodeType(jnt) == 'joint':
                pos = rig.joint(jnt, q = True, p = True)
                conPositionInfo.append(pos)                
            else:
                pos = rig.xform(jnt, q = True, t = True, ws = True)
                conPositionInfo.append(pos)   
        
        
        #将控制器归零
        conScale = rig.xform('Head_FaceRig_Control_GRP', q = True, s = True, wd = True)#获得控制器缩放值

        rig.xform('Head_FaceRig_Control_GRP', t = (0, 0, 0), ws = True)    
        rig.xform('Head_FaceRig_Control_GRP', s = (1, 1, 1), ws = True)   


        #重新设置控制器位置    
        for i,jnt in enumerate(conAndJnt):
            
            if rig.nodeType(jnt) == 'joint':
                rig.joint(jnt, e = True, p = conPositionInfo[i],co = True)
                rig.setAttr(jnt+'.radius', self.jntScale*conScale[0]*10)
            else:
                rig.xform(jnt, t = conPositionInfo[i], ws = True)
                
                conShapes = rig.listRelatives(jnt, s = True)
                for conShape in conShapes:
                    rig.scaleComponents( conScale[0], conScale[1], conScale[2], conShape+'.cv[*]', pivot = conPositionInfo[i])
    
    #将主要组P到外面
    def upParentGrp(self):
        for grp in self.grps:
            if rig.objExists(grp):
                rig.parent(grp, w = True)
        
             
    def done(self):
        self.startSeparate()
        print '刷新模版'