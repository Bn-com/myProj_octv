#-*- coding: utf-8 -*-
import maya.cmds as rig
from RIG.face.faceTemp import FC_ControlPosition
from RIG.face.faceFinish import FC_FaceSetup
from RIG.face.baseClass import *
from RIG.face.controlers import CreateControler


def SK_AddEyeSetup(sign = False):
    if sign:
        faceEye = FC_ControlPosition(True,True,True,True,True,True,False)
        faceEyeGrp = rig.group(n = 'Face_Eye_Grp',empty = True)        
        faceEye.FaceCon = 'head_jnt'
        faceEye.grpName = faceEyeGrp
        faceEye.addEye(True)
    else:
        Lock = LockHideAttr(True,True,False,False)
        faceEyeSetup = FC_FaceSetup(True,True,True,True,True,True,False)
        faceEyeSetup.scaleVal = 1
        faceEyeSetup.faceRig = 'head_jnt'
        faceGrp = rig.group(n = 'Face_Scale_Grp',empty = True)
        faceEyeSetup.eyeSetup(False,False)
        
        rig.delete('Face_Eye_Grp')
        rig.delete('Lf_EYE_JNT_P','Rt_EYE_JNT_P')
        rig.parent('Face_Scale_Grp','face_deformers')
#        锁定不需要K帧的属性
        Lock.hideAndLockObj('eye_M')
        Lock.hideAndLockObj('Lf_eye_M')
        Lock.hideAndLockObj('Rt_eye_M')
    
def SK_removeEyeSetup():
    removeObjs = [u'eye_GoupB', u'Eye_LOC_GRP', u'Eye_JNT_GRPR', u'Eye_JNT_GRPL',u'Face_Scale_Grp']
    for obj in removeObjs:
        if(rig.objExists(obj)):
            rig.delete(obj)
