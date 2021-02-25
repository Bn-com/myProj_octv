import maya.cmds as mc
import sys

a=mc.ls(type='mesh',l=1)
for i in a:
    c=i.split('|')[1]
    if c=="SET_GRP" or c=="CHR_GRP" or c=="PRP_GRP" :           
        shape=i
        shadeSGs=mc.listConnections(shape,type='shadingEngine',d=1)       
        tex=""
        if shadeSGs:
            shadeSG=shadeSGs[0]
            shade=mc.listConnections((shadeSG+".surfaceShader"),s=1,d=0)
            if shade:
                shade = shade[0]
            #nodeType = mc.nodeType(mat)
            try:
                tex=mc.listConnections((shade+".transparency"),s=1,d=0,p=1)
            except:
                tex=mc.listConnections((shade+".outTransparency"),s=1,d=0,p=1)
            if tex:
                mc.select(shape,add=1)