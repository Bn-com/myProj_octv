# -*- coding: utf-8 -*-
# Copyright (C) 2000-2010 IDMT. All rights reserved.
'''
关于cache的系列函数
'''
__author__	= 'huangzhongwei@idmt.com.cn'
__date__	= '2011-03-18'

import idmt.maya.cmds
import idmt.maya.path
import maya.cmds
import maya.mel
import maya.OpenMaya
import os
import re

def UploadCacheFile(cacheType = 'geo'):
	'''
	上传nCloth Cache
	'''
	rs = True

	folder = maya.mel.eval('zwGetPath "%sCache" ""' % cacheType)
	if folder == '':
		maya.OpenMaya.MGlobal.displayError(u'文件命名不规范')
		return False
	caches = maya.cmds.ls(type = 'cacheFile')
	if caches == None:
		return rs
	done = []
	for cache in caches:
		if cacheType == 'nCloth':
			nodes = maya.cmds.listConnections(cache, type = cacheType)
			if nodes == None:
				continue
		source = maya.cmds.getAttr('%s.cachePath' % (cache))
		source = source.replace('\\', '/')
		source = re.sub('/$', '', source)
		dest = folder
		if not source in done:
			maya.mel.eval('zwXcopyEx "%s" "%s" true true' % (source, dest))
			done.append(source)
		maya.cmds.setAttr('%s.cachePath' % (cache), dest, type = 'string')

	return True

def UploadCacheFileForRender(cacheType = 'Geo'):
	'''
	上传GeoCache
	'''
	rs = True

	folder = maya.mel.eval('zwGetPath "%sCache" ""' % cacheType)
	if folder == '':
		maya.OpenMaya.MGlobal.displayError(u'文件命名不规范')
		return False
	project =  maya.mel.eval('zwGetProject ""')
	caches = maya.cmds.ls(type = 'cacheFile')
	if caches == None:
		return rs
	done = []
	for cache in caches:
		if cacheType == 'nCloth':
			nodes = maya.cmds.listConnections(cache, type = cacheType)
			if nodes == None:
				continue
		source = maya.cmds.getAttr('%s.cachePath' % (cache))
		source = source.replace('\\', '/')
		if cacheType == 'Geo':	# render
			if re.search('^//file-cluster/GDC/Projects/%s/Project/data/' % project, source, re.IGNORECASE) != None:
				continue
		source = re.sub('/$', '', source)
		dest = folder
		if not source in done:
			maya.mel.eval('zwXcopyEx "%s" "%s" true true' % (source, dest))
			done.append(source)
		maya.cmds.setAttr('%s.cachePath' % (cache), dest, type = 'string')

	return True

#def UploadCacheFileForRender():
#	maya.mel.eval('source zwGetPath.mel')
#	return UploadCacheFile('Geo')

def UploadCacheFileForNinjago():
	return UploadCacheFileForRender()

def CheckUNC():
	rs = True

	nodes = maya.cmds.ls(type = 'cacheFile')
	if nodes != None:
		for node in nodes:
			path = maya.cmds.getAttr('%s.cachePath' % (node))
			if path != None:
				if re.search(':', path) != None and re.compile(r'L:', re.IGNORECASE).search(path) == None:
					rs = False
					maya.OpenMaya.MGlobal.displayWarning(u'应该使用//file-cluster/GDC 这样的UNC 路径。节点：%s\t路径：%s' % (node, path))

	if maya.cmds.pluginInfo('shaveNode', query = True, loaded = True):
		nodes = maya.cmds.ls(type = 'shaveGlobals')
		if nodes != None:
			for node in nodes:
				path = maya.cmds.getAttr('%s.tmpDir' % (node))
				if re.search(':', path) != None and re.compile(r'L:', re.IGNORECASE).search(path) == None:
					rs = False
					maya.OpenMaya.MGlobal.displayWarning(u'应该使用//file-cluster/GDC 这样的UNC 路径。节点：%s\t路径：%s' % (node, path))

	if not rs:
		maya.OpenMaya.MGlobal.displayWarning(u'请使用菜单命令来解决以上问题：IDMT -> TD Tools -> Cache: Z: => //file-cluster/GDC')

	return rs

def MakeUNC():
	nodes = maya.cmds.ls(type = 'cacheFile')
	if nodes != None:
		for node in nodes:
			source = maya.cmds.getAttr('%s.cachePath' % (node))
			if not os.path.isdir(source):
				continue
			source = re.sub(r'/\\$', '', source)
			dest = idmt.maya.path.GetFullPath(source)
			idmt.maya.cmds.setAttr('%s.cachePath' % (node), dest)

	if maya.cmds.pluginInfo('shaveNode', query = True, loaded = True):
		nodes = maya.cmds.ls(type = 'shaveGlobals')
		if nodes != None:
			for node in nodes:
				source = maya.cmds.getAttr('%s.tmpDir' % (node))
				if not os.path.isdir(source):
					continue
				source = re.sub(r'/\\$', '', source)
				dest = idmt.maya.path.GetFullPath(source)
				idmt.maya.cmds.setAttr('%s.tmpDir' % (node), dest)

def ImportDiskCache():
	sceneName = maya.cmds.file(query=True, sceneName = True, shortName = True)

	hairFolder = maya.mel.eval('zwGetPath \"hair\" \"%s\"' % sceneName)
	hairs = []
	if os.path.isdir(hairFolder):
		hairs = os.listdir(hairFolder)

	tempDir = maya.cmds.diskCache(query = True, tempDir = True)

	diskCaches = maya.cmds.ls(type = 'diskCache')
	for diskCache in diskCaches:
		hiddenCacheName = maya.cmds.getAttr(diskCache + '.hiddenCacheName')
		temp = tempDir + '/' + hiddenCacheName
		if not os.path.isfile(temp):
			for i in range(len(hairs)-1, -1, -1):
				if re.sub(r'^[^\.]+\.[^_]+', '', hairs[i]) == re.sub('^[^_]+', '', hiddenCacheName):
					maya.OpenMaya.MGlobal.executeCommand('sysFile -copy \"%s\" \"%s/%s\"' % (temp, hairFolder, hairs[i]), True)
					break

		cacheName = re.sub('^[^_]+', sceneName, hiddenCacheName)
		if os.path.isfile(temp):
			data = '%s/data/%s' % (maya.cmds.workspace(query = True, rootDirectory = True), cacheName)
			if not os.path.isfile(data):
				maya.OpenMaya.MGlobal.executeCommand('sysFile -copy \"%s\" \"%s\"' % (data, temp), True)

		idmt.maya.cmds.setAttr(diskCache + '.cacheName', cacheName)
