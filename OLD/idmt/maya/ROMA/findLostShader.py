#	if finishing update the cache ,lighting files may be lost the shader , fLS function can find the missed shader.
import maya.mel as mel
import string
from maya.cmds import *
def fLS():
    transforms=ls(sl=1,type='transform')
    if transforms!=None:
    	for trans in transforms:
    		shapes = ls(trans,type='shape',dag=1)
    		if len(shapes)==2 and (getAttr(shapes[0]+".intermediateObject")+getAttr(shapes[1]+".intermediateObject")):
    			condition0=getAttr(shapes[0]+".intermediateObject") and listConnections(shapes[0],s=0,d=1,type='shadingEngine')!=None
    			condition1=getAttr(shapes[1]+".intermediateObject") and listConnections(shapes[1],s=0,d=1,type='shadingEngine')!=None

    			if (condition0+condition1==1):
    				if condition0:
    					select(shapes[0])
    					setAttr(shapes[0]+".intermediateObject",0)
    					mel.eval("hyperShade -smn \"\"")
    					mats=ls(sl=1)
    					for b in mats:
    						mel.eval("hyperShade -objects \"\"")
    						objs=ls(sl=1)
    						objList=[]
    						for c in objs:
    							if string.find(c,shapes[0]) !=-1:
    								objList.append(c)
    						finalList=[]
    						select(cl=1)
    						for d in objList:
    							tmp=d.replace(shapes[0],shapes[1])
    							select(tmp,add=1)
    						cmd="hyperShade -assign "+b
    						mel.eval(cmd)
    					setAttr(shapes[0]+".intermediateObject",1)
