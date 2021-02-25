#-*- coding: utf-8 -*-
import maya.cmds as rig
from RIG.commonly.base import SK_hideLockAll,SK_showLockAll


def SK_findAllIKJoints():
    AllIkJnts = []
    AllIkHandes = rig.ls(type = 'ikHandle')
    for handle in AllIkHandes:
        startJnt =  rig.ikHandle(handle,q = True,sj = True)
        endJnt = rig.listConnections(rig.ikHandle(handle,q = True,ee = True),d = False,s = True,type = 'joint')[0]
        AllIkJnts.append(startJnt)
        AllIkJnts.append(endJnt)
        while(True):
            temUpJnt = rig.listRelatives(endJnt,p = True,type = 'joint')[0]
            if(startJnt  == temUpJnt):
                break
            else:
                endJnt = temUpJnt
                AllIkJnts.append(endJnt)
    return AllIkJnts


def SK_lockAllJoint(Lock = True):
    removeTransform = []
    removeTransform.extend(rig.ls('*_IK_Anim'))
    removeTransform.extend(SK_findAllIKJoints())
    removeTransform.extend(rig.sets('bodySet',q = True))
    removeTransform.extend(rig.listCameras())    
    setRemoveTransform = set(removeTransform)
    
    allTransform = rig.ls(rig.listRelatives('Master',c = True,ad = True),type = 'transform')
    deformTransform = rig.ls(rig.listRelatives('LegArm_deformers',c = True,ad = True),type = 'transform')
    allTransform.extend(deformTransform)
    setAllTransform = set(allTransform)
    LockObjSet = setAllTransform - setRemoveTransform
    
    if(Lock):
        for Jnt in LockObjSet:
            SK_hideLockAll(Jnt,1,1,1,['twist'])
    else:
        for Jnt in LockObjSet:
            SK_showLockAll(Jnt)
