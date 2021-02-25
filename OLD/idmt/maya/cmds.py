# -*- coding: utf-8 -*-

'''
like cmds in maya
'''
__author__	= 'huangzhongwei'
__date__	= '2010-10-22'

import os
import __builtin__
import maya.cmds
import maya.OpenMaya as OpenMaya

def list(buf):
	if buf == None:
		buf = []
	return buf

def len(buf):
	return __builtin__.len(list(buf))

def evalSetAttr(attr, value):
	command = r''
	if type(value) == str or type(value) == unicode:
		value = value.replace('\\', '\\\\')
		value = value.replace('\"', '\\\"')
		command = r'setAttr -type "string" "%s" "%s"' % (attr, value)
	else:
		command = r'setAttr "' + attr + '" ' + str(value)
	OpenMaya.MGlobal.executeCommand(command, True)

def setAttr(attr, value):
	'''
setAttr:
1)even attr not exists, lock, connected, referenced
2)only set if new value != old value
	'''

	if not maya.cmds.objExists(attr):
		return False

	oldValue = maya.cmds.getAttr(attr)
	if maya.cmds.getAttr(attr, typ = True) in ['float', 'double']:
		if value >= oldValue-0.0001 and value <= oldValue+0.0001:
			return True
	else:
		if oldValue == value:
			return True

	buf = maya.cmds.listConnections(attr, destination = False)
	if buf != None:
		return False

	if maya.cmds.getAttr(attr, lock = True):
		if maya.cmds.reference(attr, isNodeReferenced = True):
			return False

		lockNode = maya.cmds.lockNode(attr, query = True)
		if lockNode[0]:
			maya.cmds.lockNode(attr, lock = False)
		maya.cmds.setAttr(attr, lock = False)

		evalSetAttr(attr, value)

		maya.cmds.setAttr(attr, lock = True)
		if lockNode[0]:
			maya.cmds.lockNode(attr, lock = True)
	else:
		evalSetAttr(attr, value)

	rs = maya.cmds.getAttr(attr) == value

	return rs

def UnlockTransform(nodes = None, leaf = False):
	if nodes == None:
		nodes = maya.cmds.ls(selection = True, long = True)
	if nodes == None:
		return
	for node in nodes:
		if maya.cmds.nodeType(node) == 'transform':
			if not maya.cmds.referenceQuery(node, isNodeReferenced = True):
				for attr in ('translateX', 'translateY', 'translateZ', 'rotateX', 'rotateY', 'rotateZ', 'scaleX', 'scaleY', 'scaleZ', 'visibility'):
					maya.cmds.setAttr(node + '.' + attr, keyable = True, lock = False)
		if leaf:
			children = maya.cmds.listRelatives(node, c = True, fullPath = True)
			if children != None:
				UnlockTransform(children, True)

def listObjWithAttr(attr):
	objWithAttr = []

	objs = maya.cmds.ls()
	for i in range(len(objs)):
		if maya.cmds.attributeQuery(attr, node = objs[i], exists = True):
			objWithAttr.append(objs[i])

	return objWithAttr

def abspath(module, type, file):
	folder = os.path.dirname(module)
	if not os.path.isdir(folder):
		while True:
			folder = os.path.dirname(folder)
			if os.path.isdir(folder):
				break
		subFolder = os.path.join(folder, type)
		if not os.path.isdir(subFolder):
			folder = os.path.dirname(folder)
		folder = os.path.join(folder, type)
	path = os.path.join(folder, file)
	return path