#-*- coding: utf-8 -*-
import maya.cmds as rig
import math
from RIG.simulation.simulationMain import SM_warning
from RIG.commonly.base import SK_getSkinCluster

def detectInfluenceObj():
    objs = rig.ls(sl = True)
    if(objs):
        dis = 0.001
        disObj = ''
        disObjNum = 0
        obj = objs[0]

        skin = SK_getSkinCluster(obj)
        
        if skin:
            infs = rig.skinCluster(skin,q = True,inf = True)
            infsPos = []
            for inf in infs:
                pos = rig.xform(inf,q = True,t = True,ws = True)
                infsPos.append(pos)
                
            for i,pos in enumerate(infsPos):
                for j,curPos in enumerate(infsPos):
                    currentDis = math.pow(math.pow(pos[0]-curPos[0],2)+math.pow(pos[1]-curPos[1],2)+math.pow(pos[2]-curPos[2],2),0.5)
                    if(currentDis < dis and i != j):
                        disObj += infs[i]+'--->'+infs[j]+'\n'
                        disObjNum += 1
                        
            if (disObjNum != 0):
                disStr =  u'重叠的骨骼为:\n'+disObj  
            else:
                disStr = u'没有找到重叠的骨骼'
                        
            SM_warning(u'骨骼的个数为:'+str(len(infs))+'\n'+disStr)
        
        else:
            SM_warning(u'没有找到skinCluster节点，请确认:'+obj+u'已经被蒙皮')