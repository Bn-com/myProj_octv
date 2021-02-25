# -*- coding: utf-8 -*-
# Copyright (C) 2000-2010 IDMT. All rights reserved.
'''
Utility Functions for Maya File Reference
'''
__author__	= 'huangzhongwei@idmt.com.cn'
__date__	= '2010-12-31'

import idmt.maya.path
import maya.cmds as cmds
import maya.OpenMaya as OpenMaya
import os
import re

def MakeDollarPath(envName = 'IDMT_PROJECTS'):
	rs = True

	envValue = os.getenv(envName, '')
	references = cmds.file(query = True, reference = True)
	for reference in references:
		unresolvedName = cmds.referenceQuery(reference, filename = True, unresolvedName = True, withoutCopyNumber = True)
		if re.compile(r'^\${' + envName + '}', re.IGNORECASE).search(unresolvedName) != None:
			continue
		dollarPath = idmt.maya.path.GetDollarPath(unresolvedName)
		if unresolvedName == dollarPath:
			if envValue == '':
				OpenMaya.MGlobal.displayError(u'没有设置 %s 环境变量' % (envName))
				return False
			OpenMaya.MGlobal.displayError(u'所有reference必须指向%s\n%s' % (envValue, reference))
			rs = False
		else:
			expandName = cmds.workspace(expandName = dollarPath)
			if os.path.isfile(expandName):
				unloaded = cmds.referenceQuery(reference, nodes = True) == []

				node = cmds.file(reference, query = True, referenceNode = True)
				cmds.file(dollarPath, loadReference = node)

				unresolvedName = cmds.referenceQuery(node, filename = True, unresolvedName = True, withoutCopyNumber = True)
				if re.compile(r'^\${' + envName + '}', re.IGNORECASE).search(unresolvedName) == None:
					cmds.file(dollarPath, loadReference = node)
				unresolvedName = cmds.referenceQuery(node, filename = True, unresolvedName = True, withoutCopyNumber = True)
				if re.compile(r'^\${' + envName + '}', re.IGNORECASE).search(unresolvedName) == None:
					OpenMaya.MGlobal.displayError(u'不能修改参考文件的路径：%s' % (reference))
					rs = False
				if unloaded == True:
					cmds.file(unloadReference = node)
			else:
				OpenMaya.MGlobal.displayError(u'所有reference必须指向%s\n%s' % (envValue, reference))
				rs = False

	return rs

def ListAssets(topReferences = None):
	'''List all referenced files, duplicates removed, sorted'''
	references = []

	if topReferences != None:
		for i in range(len(topReferences)):
			topReferences[i] = cmds.referenceQuery(topReferences[i], referenceNode = True)
	nodes = cmds.ls(type = 'reference')
	for node in nodes:
		if topReferences != None:
			topReference = ''
			try:
				topReference = cmds.referenceQuery(node, referenceNode = True, topReference = True)
			except:
				continue
			if node == topReference:
				continue
			if not topReference in topReferences:
				continue
		filename = ''
		try:
			filename = cmds.referenceQuery(node, filename = True, withoutCopyNumber = True)
		except:
			continue
		if not filename in references:
			references.append(filename)
	references.sort()

	return references

def CheckReferenceForRomaFinishing():
	'''Check reference for ROMA finishing: can not nested; only _RND or _LRND'''
	rs = True
	topReferences = []
	nodes = cmds.ls(type = 'reference')
	for node in nodes:
		topReference = ''
		filename = ''
		try:
			topReference = cmds.referenceQuery(node, referenceNode = True, topReference = True)
		except:
			continue
		if node != topReference:
			try:
				filename = cmds.referenceQuery(topReference, filename = True)
			except:
				continue
			if not filename in topReferences:
				topReferences.append(filename)
				OpenMaya.MGlobal.displayError(u'不能嵌套参考：%s' % (filename))
			rs = False
			continue

		try:
			filename = cmds.referenceQuery(node, filename = True)
		except:
			continue
		if re.search(r'_L?RND\.', filename) == None:
			OpenMaya.MGlobal.displayError(u'只能参考_RND或者_LRND文件：%s' % (filename))
			rs = False
			continue
		if re.compile(r'/scenes/characters/([^/]+/){3}[^/]+$', re.IGNORECASE).search(filename) != None:
			OpenMaya.MGlobal.displayError(u'角色需要参考fixed 文件夹里面的文件：%s' % (filename))
			rs = False
			continue
	if rs:
		OpenMaya.MGlobal.displayInfo(u'OK，没问题')
	return rs