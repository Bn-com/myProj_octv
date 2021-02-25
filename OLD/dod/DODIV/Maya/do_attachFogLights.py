import maya.cmds as mc
from pymel.core import *


def do_attachFogLights():
    sels = ls( sl = True )
    
    for sel in sels:
        new = duplicate(sel)
        setAttr(new[0] + '.tx', lock = False)
        setAttr(new[0] + '.ty', lock = False)
        setAttr(new[0] + '.tz', lock = False)
        setAttr(new[0] + '.rx', lock = False)
        setAttr(new[0] + '.ry', lock = False)
        setAttr(new[0] + '.rz', lock = False)
        setAttr(new[0] + '.sx', lock = False)
        setAttr(new[0] + '.sy', lock = False)
        setAttr(new[0] + '.sz', lock = False)
        xform(new[0],centerPivots = True)
        parent( new[0], world=True )
      
        newObject = importFile('//file-cluster/GDC/Projects/DiveollyDive4/DiveollyDive4_Scratch/Render/lights/fog_light/fog_light.mb',returnNewNodes = True)
        fog_light = ''
        for n in newObject:
            if n.nodeType() == 'transform':
                fog_light = n.root()
                
        con = parentConstraint(new[0],fog_light)
        delete(con)
        delete(new[0])
        p = sel.getParent()
        parent(fog_light,p)
        setAttr(fog_light + '.rx', 180)

if __name__ == "__main__":
    do_attachFogLights()