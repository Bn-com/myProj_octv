#-*- coding: utf-8 -*-
import maya.cmds as rig
import math

def softModToCluster():
    softTransform = rig.ls(sl = True)[0]
    solftMod = rig.listConnections(softTransform,s = False,d = True,type = 'softMod')[0]
    modifModel = rig.listConnections(solftMod,s = False,d = True,type = 'mesh')
    
    if modifModel:
        origPos = rig.xform(softTransform,q = True,t = True,wd = True)
        
        for mesh in modifModel:
            prePos = []
            curPos = []
            weights = []
            vtxs = rig.ls(mesh+'.vtx[*]',fl = True)
            
            rig.xform(softTransform,t = (0,0,0),wd = True)
            for vtx in vtxs:
                pos = rig.xform(vtx,q = True,t = True,wd = True)
                prePos.append(pos)
                
            rig.xform(softTransform,t = (0,1,0),wd = True)
            for vtx in vtxs:
                pos = rig.xform(vtx,q = True,t = True,wd = True)
                curPos.append(pos)  
                
            weights = [math.pow(math.pow(pos[0]-curPos[i][0],2)+math.pow(pos[1]-curPos[i][1],2)+math.pow(pos[2]-curPos[i][2],2),0.5) for i,pos in enumerate(prePos)]
            rig.xform(softTransform,t = (0,0,0),wd = True)
            
            CLS = rig.cluster(mesh,n = mesh+'_CLS')
            for i,vtx in enumerate(vtxs):
                rig.percent(CLS[0],vtx,v = weights[i])
                
        rig.xform(softTransform,t = origPos,wd = True)
    