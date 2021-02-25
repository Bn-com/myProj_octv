#-*- coding: utf-8 -*-
from RIG.face.controlers import CreateControler
from RIG.simulation.simulationMain import SM_warning
from maya.cmds import *


def SK_SKTOCON(objs):
    Con = CreateControler(13)
    N = len(objs)
    for i,obj in enumerate(objs):
        M = getAttr(obj+'.worldMatrix')
        
        conName = Con.SK_b08(obj.replace(obj.split('_')[-1],str(i)+'_M'))
        setAttr(conName+'.rz',90)
        makeIdentity(conName,apply = True,s = True,r = True,t = True)
        conGrp = group(conName,n = conName+'_GRP')
        xform(conGrp,matrix = M)
        parentConstraint(conName,obj,mo = True)
        
        if 0 != i:
            parent(conGrp,obj.replace(obj.split('_')[-1],str(i-1)+'_M'))
                

def buildSKTOCON():
    objs = ls(sl = True)
    if objs:
        #--------------------------------------------------------------检测骨骼命名是否正确
        obj = objs[0]
        pre = obj.split('_')
        if(len(pre) > 1):
            SK_SKTOCON(objs)
            
        else:
            SM_warning(u'骨骼命名有问题!!!!!!!!!!!!\n正确的命名为：前缀_后缀   例如：Jaw_JNT')
   
            
            
            