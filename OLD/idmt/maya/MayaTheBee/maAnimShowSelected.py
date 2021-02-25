# -*- coding: utf-8 -*-
# Copyright (C) 2000-2012 IDMT. All rights reserved.
'''
tools name:
1)
2)
'''
__author__ = 'wanshoulong'
__date__    = ''

import maya.cmds as cmds
import os
import sys

def maAnimShowSelected ():
	allGroup=[]
	selGroup=[]
	selectObj = cmds.ls(sl=1,l=1)
	
	allRef = cmds.file(q=1,r=1)
	for ref in allRef:
		refNodes = cmds.referenceQuery(ref,n=1)
		allGroup.append(refNodes[0])
	allGroup=set(allGroup)
		
	if len(selectObj) :
		for obj in selectObj:
			if cmds.referenceQuery(obj,inr=1) :
				refNodes = cmds.referenceQuery(obj,n=1)
				selGroup.append(refNodes[0])
		selGroup = list(set(selGroup))
		for goup in allGroup:
			if not selGroup.count(goup) and not cmds.getAttr(goup+'.lodVisibility',l=1): 
				cmds.setAttr(goup+'.lodVisibility',0)
	else:
		for othergroup in allGroup:
			if not cmds.getAttr(othergroup+'.lodVisibility',l=1) :
				cmds.setAttr(othergroup+'.lodVisibility',1)