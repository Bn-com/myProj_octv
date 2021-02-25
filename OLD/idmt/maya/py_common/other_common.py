# -*- coding: utf-8 -*-

import sys,os
import maya.cmds as mc
'''
【通用：显示隐藏工具】
对选取的参考物体进行显示并隐藏其他参考物体，不选时显示所有
Author: 万寿龙
2013.5.8 沈康更新
'''
def sl_animShowSelected ():
	allGroup=[]
	selGroup=[]
	selectObj = mc.ls(sl=1,l=1)
	
	allRef = mc.file(q=1,r=1)
	for ref in allRef:
		refNodes = mc.referenceQuery(ref,n=1)
		#对没有载入的参考进行过滤，这样可以通用所有环节，下同
		if refNodes :
			allGroup.append(refNodes[0])
	allGroup=set(allGroup)
		
	if len(selectObj) :
		for obj in selectObj:
			if mc.referenceQuery(obj,inr=1) :
				refNodes = mc.referenceQuery(obj,n=1)
				if refNodes:
					selGroup.append(refNodes[0])
		selGroup = list(set(selGroup))
		for goup in allGroup:
			if not selGroup.count(goup) and not mc.getAttr(goup+'.lodVisibility',l=1): 
				g = sl_topParent(goup)
				mc.setAttr(g+'.lodVisibility',0)
	else:
		for othergroup in allGroup:
			if not mc.getAttr(othergroup+'.lodVisibility',l=1) :
				g = sl_topParent(othergroup)
				mc.setAttr(g+'.lodVisibility',1)
				mc.setAttr(othergroup+'.lodVisibility',1)

def sl_topParent(obj):  
	varA = mc.listRelatives(obj,p=True)  
	if varA:
		while(len(varA) > 0):  
			varB = varA[0]  
			varA = mc.listRelatives(varA[0],p=True) 
			if not varA:
				return varB 
	else:
		return obj
'''
【通用：删除海龟节点】
删除文件内海龟渲染器节点
Author: 未知
2013.5.9 沈康更新，加入判断海龟文件是否存在
'''
def com_deleteTurtleNodes():
	turtleNodes = mc.ls( 'Turtle*')
	if turtleNodes:
		for node in turtleNodes:
			mc.lockNode( node, lock=False )
			mc.delete( node )