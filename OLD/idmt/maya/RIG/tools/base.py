#-*- coding: utf-8 -*-
import maya.cmds as rig

def resetClusterPos():
    CLS = rig.ls(sl = True)
    if CLS:
        for CL in CLS:
            CLSShape = rig.listRelatives(CL,s = True)[0]
            pos = rig.xform(CL,q = True,piv = True,ws = True)
            rig.setAttr(CLSShape+'.originX',pos[0])
            rig.setAttr(CLSShape+'.originY',pos[1])
            rig.setAttr(CLSShape+'.originZ',pos[2])
    
    
    
def TL_CloseDisplayLocalAxis():#关闭场景中局部旋转轴向显示
    allObjs = rig.ls(type = 'transform')
    for obj in allObjs:
        rig.setAttr(obj+'.displayLocalAxis',0)