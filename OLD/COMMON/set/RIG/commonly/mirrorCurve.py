#-*- coding: utf-8 -*-
import maya.cmds as rig

def SK_MirrorCurveControl(curves = []):    
    for cur in curves:        
        shapeSource = rig.listRelatives(cur,s = True)[0]
        
        if shapeSource:
            if('nurbsCurve' == rig.nodeType(shapeSource)):
                if('Lf' in shapeSource):
                    shapeDes = shapeSource.replace('Lf','Rt',3)
                else:
                    shapeDes = shapeSource.replace('Rt','Lf',3)            
                
                form =    rig.getAttr(shapeSource+'.form')
                spans =   rig.getAttr(shapeSource+'.spans')
                degrees = rig.getAttr(shapeSource+'.degree')
        
                numCv=len(rig.ls(shapeDes+'.cv[*]',fl = True))
                for i in range(numCv+1):
                    pos=rig.xform(shapeSource+'.cv['+str(i)+']',q = True,ws = True,t = True)
                    rig.xform(shapeDes+'.cv['+str(i)+']',t = (pos[0]*-1,pos[1],pos[2]),ws = True)
                

def SK_MirrorCurveControlCmd(LR = True):
    if LR:
        setCons = [con for con in rig.sets('bodySet',q = True) if ('Lf' in con.split('_')[0])]
        SK_MirrorCurveControl(setCons)
    else:
        setCons = [con for con in rig.sets('bodySet',q = True) if ('Rt' in con.split('_')[0])]
        SK_MirrorCurveControl(setCons)        
        
        
        
