# -*- coding: utf-8 -*-

import maya.cmds as mc

def stretch_attr():

	if not mc.pluginInfo('stretchMesh_2014_x64',loaded = 1,q = 1):
	    mc.loadPlugin('stretchMesh_2014_x64')	
	    
	curves=mc.ls(type='transform',l=1)
	needCurs=[]
	if curves:
	    for cur in curves:          
	        shape = mc.listRelatives(cur,ad=1,f=1,ni=1,type='nurbsCurve')
	        if shape:
	            if cur not in needCurs:
	                needCurs.append(cur) 
	                
	                
	CurNeeds=[]
	if needCurs:       
	    for node in needCurs:
	        if mc.objExists(node+'.Stretch_Mesh'):                                          
	            CurNeeds.append(node) 
	          
	
	result=mc.confirmDialog( title=u'Stretch_Mesh属性修改', message=u'确认修改Stretch_Mesh全部属性吗', button=['ON','OFF'], defaultButton='Yes', cancelButton='No', dismissString='No' )
	
	if result == 'ON':
	    Stretch_on(CurNeeds)
	if result == 'OFF':
	    Stretch_off(CurNeeds)	
	    
def Stretch_on(NeedMeshes):
    si=0
    for node in NeedMeshes:
        if mc.getAttr(node+'.Stretch_Mesh')==0:
            mc.setAttr(node+'.Stretch_Mesh',1)
        else:
            pass
        si=1
    if si==1:
        print u'Stretch_Mesh属性已全部开启'
          
            
def Stretch_off(NeedMeshes):
    si=0     
    for node in NeedMeshes:
        print 'ok'
        if mc.getAttr(node+'.Stretch_Mesh')==1:
            mc.setAttr(node+'.Stretch_Mesh',0)
        else:
            pass
    si=0
    if si==0:
        print u'Stretch_Mesh属性已全部关闭'



	
	