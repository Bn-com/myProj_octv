import maya.cmds as rig
from RIG.commonly.base import SK_getSkinCluster

def SK_copyWeightToOtherObj():
    objs = rig.ls(sl = True)
    if objs:
        sourObj = objs[0]
        skinClusterS = SK_getSkinCluster(sourObj)
        for obj in objs:
            if obj != sourObj:
                skinClusterT = SK_getSkinCluster(obj)
                if skinClusterT:
                    rig.copySkinWeights(ss = skinClusterS,ds = skinClusterT,noMirror = True,surfaceAssociation = 'closestPoint',influenceAssociation = 'closestJoint')