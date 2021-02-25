#-*- coding: utf-8 -*-

import maya.cmds as rig
import RIG.WDface.WD_MainClass as CA

class teethToHead():
    def __init__(self):
        self.jaw = 'Dn_LipMove_Up'
        self.grp = 'DnTooth_M_Freeze_GRP_Top'
        

               
    def addControl(self):
        jawCon = 'JawMain_M'
        jawJnt = 'Jaw_Joint'
        jawConParent = rig.listRelatives(jawCon, p = True)[0]
        
        rig.addAttr(jawConParent, at = 'float', ln = 'UpTeeth', k = True)
        rig.setAttr(jawConParent+'.UpTeeth',l = True)        
        rig.addAttr(jawConParent, at = 'float', ln = 'UpTeethRX', k = True, dv = 1)
        rig.addAttr(jawConParent, at = 'float', ln = 'UpTeethRY', k = True, dv = 1)
        rig.addAttr(jawConParent, at = 'float', ln = 'UpTeethRZ', k = True, dv = 1)
        rig.addAttr(jawConParent, at = 'float', ln = 'DnTeethRX', k = True)
        rig.addAttr(jawConParent, at = 'float', ln = 'DnTeethRY', k = True)
        rig.addAttr(jawConParent, at = 'float', ln = 'DnTeethRZ', k = True)
        rig.addAttr(jawConParent, at = 'float', ln = 'DnTeethTZ', k = True, dv = 0.5)
        
        DnTeethGrp = rig.group(self.grp, n = self.grp+'_Rotate')
        rig.xform(DnTeethGrp, os = True, piv = (0, 0, 0))
        DnTeethRoMD = rig.createNode('multiplyDivide', n = self.grp+'_RoateDn_MD')
        rig.connectAttr(self.jaw+'.rotate', DnTeethRoMD+'.input2')
        rig.connectAttr(jawConParent+'.DnTeethRX', DnTeethRoMD+'.input1X')
        rig.connectAttr(jawConParent+'.DnTeethRY', DnTeethRoMD+'.input1Y')
        rig.connectAttr(jawConParent+'.DnTeethRZ', DnTeethRoMD+'.input1Z')
        
        rig.connectAttr(DnTeethRoMD+'.output', DnTeethGrp+'.rotate') 
        
        
        DnTeethTrMD = rig.createNode('multiplyDivide', n = self.grp+'_Translate_MD')
        rig.connectAttr(jawJnt+'.tz', DnTeethTrMD+'.input1X')  
        rig.connectAttr(jawConParent+'.DnTeethTZ', DnTeethTrMD+'.input2X') 
        rig.connectAttr(DnTeethTrMD+'.outputX', DnTeethGrp+'.tz')
        
        #下压床旋转设置
        UpGrp = 'UpTooth_M_Freeze_GRP_Top'
        UpJnt = 'Jaw_Swivle_Joint_UP'
        UpJntMat = rig.getAttr(UpJnt+'.worldMatrix')
        UpNewGrp = rig.group(empty = True, n = UpGrp+'_GRP')
        UpNewGrpTop = rig.group(UpNewGrp, n = UpGrp+'_TOPGRP')
        rig.xform(UpNewGrpTop, m = UpJntMat)

        UpTeethRoMD = rig.createNode('multiplyDivide', n = self.grp+'_RoateUp_MD')
        rig.connectAttr(UpJnt+'.rotate', UpTeethRoMD+'.input2')
        rig.connectAttr(jawConParent+'.UpTeethRX', UpTeethRoMD+'.input1X')
        rig.connectAttr(jawConParent+'.UpTeethRY', UpTeethRoMD+'.input1Y')
        rig.connectAttr(jawConParent+'.UpTeethRZ', UpTeethRoMD+'.input1Z')
        rig.connectAttr(UpTeethRoMD+'.output', UpNewGrp+'.rotate') 
        
        rig.parent(UpNewGrpTop, rig.listRelatives(UpGrp, p = True)[0])
        rig.parent(UpGrp, UpNewGrp)
#        rig.connectAttr(UpJnt+'.rotate', UpNewGrp+'.rotate')
#        rig.parent(UpGrp, UpNewGrp)

                                         
    def done(self):
        rig.parent(self.grp, self.jaw)
        self.addControl()