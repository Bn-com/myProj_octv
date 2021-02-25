# -*- coding: gbk -*-
import maya.mel as mel
import maya.cmds as cmds


def rename(para):
	newName='_'.join(['LGT','env',para,'light'])

	allLight=cmds.ls(sl=1,type='light',dag=1)
	allLightNames=[]
	for light in allLight:
		allLightNames.append(cmds.listRelatives(light,p=1)[0])
	for light in allLightNames:
		cmds.rename(light,newName)
