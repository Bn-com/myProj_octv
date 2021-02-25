# -*- coding: utf-8 -*-
# Copyright (C) 2000-2010 IDMT. All rights reserved.
'''
GDC UI
'''
__author__	= 'huangzhongwei@idmt.com.cn'
__date__	= '2011-10-09'

import maya.cmds

def CreateUI():
	if maya.cmds.menu('menuGDC', exists = True):
		maya.cmds.deleteUI('menuGDC', menu = True)
	gMainWindow = 'MayaWindow'	# global string $gMainWindow;
	menuGDC = maya.cmds.menu('menuGDC', label = 'GDC', parent = gMainWindow, tearOff = True, allowOptionBoxes = True)
	maya.cmds.menuItem(parent = menuGDC, label = 'Toggle Maps...', command = 'import idmt.maya.ToggleMaps\nidmt.maya.ToggleMaps.ToggleMaps().showWindow()')

def DeleteUI():
	if maya.cmds.menu('menuGDC', exists = True):
		maya.cmds.deleteUI('menuGDC', menu = True)