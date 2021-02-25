# -*- coding: utf-8 -*-
# Copyright (C) 2000-2010 IDMT. All rights reserved.
'''
Functions for Muster
'''
__author__	= 'huangzhongwei@idmt.com.cn'
__date__	= '2011-03-01'

import maya.cmds
import maya.mel
import maya.OpenMaya
import os
import re
import datetime

def GetRenderableCameraCount():
	'''
	获取renderable camera，用于检查，通常不能多于3
	'''
	count = 0
	cameras = maya.cmds.ls(cameras = True)
	if cameras != None:
		for camera in cameras:
			if maya.cmds.getAttr('%s.renderable' % (camera)):
				count = count + 1
	return count

def GetMax():
	'''
	设置每个任务最多使用多少个节点
	'''
	max = 20
	mode = maya.mel.eval('zwGetMode ""')
	if mode == 'effect':
		max = 10
	project = maya.mel.eval('zwGetProject ""')
	if project == 'ROMA':
		max = 10
	elif project == 'Zorro':
		max = 8
	elif project == 'PigPig':
		max = 0
	return max

def CheckTexture(renderer = 'MayaMan'):
	'''
	检查贴图是否存在丢失、空格
	'''
	rs = True

	nodes = maya.cmds.ls(typ = 'file')
	if nodes != None:
		for node in nodes:
			fileTextureName = maya.cmds.getAttr(r'%s.fileTextureName' % (node))
			if fileTextureName == '':
				continue
			path = maya.cmds.workspace(expandName = fileTextureName)
			if not os.path.isfile(path):
				maya.OpenMaya.MGlobal.displayWarning(u'贴图丢失：\t%s.fileTextureName\t%s' % (node, fileTextureName))
				rs = False
			elif renderer == 'MayaMan':
				filename = os.path.basename(path)
				if re.search(r'\s', filename) != None:
					maya.OpenMaya.MGlobal.displayWarning(u'贴图文件名有空格：\t%s.fileTextureName\t%s' % (node, fileTextureName))
					rs = False
	return rs

def GetExpectedFrames(framecheck = False, dest = '', layer = ''):
	'''
	得到-expectedframes参数
	'''
	expectedframes = ''

	if not framecheck:
		return expectedframes

	if maya.cmds.about(apiVersion = True) < 200900:
		return expectedframes

	if layer == '':
		renderLayers = maya.cmds.listConnections('renderLayerManager.renderLayerId')
		for renderLayer in renderLayers:
			if maya.cmds.getAttr('%s.renderable' % (renderLayer)):
				if layer == '':
					layer = renderLayer
					break
	if layer == '':
		return expectedframes

	buf = maya.cmds.renderSettings(firstImageName = True, lyr = layer)
	prefix = re.sub(r'(\..*)+$', '.', buf[0])
	expectedframes = r' -framecheck Scene -expectedframes "%s" -recursion 2' % (os.path.join(dest, prefix).replace('/', '\\'))

	return expectedframes

def CheckLodGroup():
	'''
	lodGroup 要连到渲染摄像机
	'''
	rs = True
	lodGroups = maya.cmds.ls(typ = 'lodGroup')
	if lodGroups != None:
		for lodGroup in lodGroups:
			cameras = maya.cmds.listConnections('%s.cameraMatrix' % (lodGroup), destination = False, t = 'camera')
			if cameras == None:
				rs = False
				maya.OpenMaya.MGlobal.displayError(u'%s 应该连接到渲染摄像机' % (lodGroup))
				continue
			for camera in cameras:
				if not maya.cmds.getAttr('%s.renderable' % (camera)):
					rs = False
					maya.OpenMaya.MGlobal.displayError(u'%s 应该连接到渲染摄像机' % (lodGroup))
					break

	return rs

def CheckShadowMap():
	rs = True

	start = maya.cmds.optionVar(query = 'musterCheckinStart')
	end = maya.cmds.optionVar(query = 'musterCheckinEnd')
	if start == end:
		return rs
	lights = maya.cmds.ls(lights = True)
	if lights == None:
		return rs
	for light in lights:
		if not maya.cmds.objExists(r'%s.useDepthMapShadows' % light):
			continue
		if not maya.cmds.getAttr(r'%s.useDepthMapShadows' % light):
			continue
		parents = maya.cmds.listRelatives(light, parent = True)
		if not maya.cmds.getAttr(r'%s.visibility' % parents[0]):
			continue
		if not maya.cmds.objExists(r'%s.MayaManAttsNode' % parents[0]):
			continue
		MayaManAttsNodes = maya.cmds.listConnections(r'%s.MayaManAttsNode' % parents[0])
		if MayaManAttsNodes == None:
			continue
		for MayaManAttsNode in MayaManAttsNodes:
			if not maya.cmds.getAttr('%s.mmla_UseCustomShadowMap' % MayaManAttsNode):
				rs = False
				maya.OpenMaya.MGlobal.displayError(u'需要预先生成%s 的Shadow Map' % parents[0])
				continue
			mmla_CustomMapFile = maya.cmds.getAttr('%s.mmla_CustomMapFile' % MayaManAttsNode)
			if mmla_CustomMapFile == '':
				rs = False
				maya.OpenMaya.MGlobal.displayError(u'需要预先生成%s 的Shadow Map' % parents[0])
				continue

	return rs

def texMirrow():
	import win32api
	import win32file

	nodes = maya.cmds.ls(typ = 'file')

	if not maya.cmds.about(batch = True):
		maya.cmds.progressWindow(maxValue = len(nodes)+1, t = 'Mirror Texture', isInterruptable = True)

	for i in range(len(nodes)):
		node = nodes[i]

		if not maya.cmds.about(batch = True):
			if maya.cmds.progressWindow(query = True, isCancelled = True):
				maya.cmds.progressWindow(endProgress = True)
				break
			maya.cmds.progressWindow(edit = True, progress = i + 1, status = str(i + 1) + '/' + str(len(nodes)) + '    ' + nodes[i])

		path = maya.cmds.getAttr(r'%s.fileTextureName' % (node))
		path = maya.cmds.workspace(expandName = path)
		path = path.replace('/', '\\')

		files = []
		texMirrow9 = re.sub(r'^\\\\', r'\\\\file-cluster\\GDC\\Netrender\\Scenes\\texMirrow9\\', path) + '.tif'
		files.append(texMirrow9)
		files.append(re.sub(r'[^/\\]+$', r'prman\\\g<0>.pX.pY.mU.tex', texMirrow9))
		files.append(re.sub(r'[^/\\]+$', r'prman\\\g<0>.mU.tex', texMirrow9))

		for source in files:
			if not os.path.isfile(source):
				continue
			#lock = source + '.lock'
			#if os.path.isfile(lock):
			#	continue
			try:
				ss = os.stat(source)
			except:
				break
			if ss.st_size != 0:
				for i in (1, 2, 3, 5, 6, 7):
					dest = source.replace('\\texMirrow9\\', '\\texMirrow%d\\' % i)
					#lock = dest + '.lock'
					#if os.path.isfile(lock):
					#	continue
					if os.path.isfile(dest):
						try:
							sd = os.stat(dest)
						except:
							continue
						if ss.st_size != sd.st_size:
							print 'copy \"%s\" \"%s\"' % (source, dest)
							try:
								win32file.CopyFileW(source, dest, False)
							except:
								msg = win32api.FormatMessageW(win32api.GetLastError())
								maya.OpenMaya.MGlobal.displayWarning(msg)
								sceneName = maya.cmds.file(query=True, sceneName = True, shortName = True)
								fo = open(r'\\192.168.2.10\ftp$\texMirrow.txt', "a")
								fo.write('%s\t%s\t%s\r\n%s\r\n%s\r\n\r\n' % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), os.getenv('USERNAME'), sceneName, dest, msg))
								fo.close()
					else:
						try:
							dirname = os.path.dirname(dest)
							if not os.path.isdir(dirname):
								os.makedirs(dirname)
							win32file.CopyFileW(source, dest, False)
						except:
							pass

	if not maya.cmds.about(batch = True):
		maya.cmds.progressWindow(endProgress = True)

def texMirrowAll():
	import win32api
	import win32file

	for root, dirs, filenames in os.walk(r'\\file-cluster\GDC\Netrender\Scenes\texMirrow9'):
		for filename in filenames:
			if re.compile(r'\.lock$', re.IGNORECASE).search(filename) != None:
				continue
			if re.compile(r'\.tif(\..*)?$', re.IGNORECASE).search(filename) != None:
				source = os.path.join(root, filename)
				lock = source + '.lock'
				if os.path.isfile(lock):
					continue
				try:
					ss = os.stat(source)
				except:
					continue
				if ss.st_size != 0:
					for i in (1, 2, 3, 5, 6, 7):
						dest = source.replace('\\texMirrow9\\', '\\texMirrow%d\\' % i)
						#lock = dest + '.lock'
						#if os.path.isfile(lock):
						#	continue
						if os.path.isfile(dest):
							try:
								sd = os.stat(dest)
							except:
								continue
							if ss.st_size != sd.st_size:
								print 'copy \"%s\" \"%s\"' % (source, dest)
								try:
									win32file.CopyFileW(source, dest, False)
								except:
									msg = win32api.FormatMessageW(win32api.GetLastError())
									maya.OpenMaya.MGlobal.displayError(msg)
									sceneName = maya.cmds.file(query=True, sceneName = True, shortName = True)
									fo = open(r'\\192.168.2.10\ftp$\texMirrow1.txt', "a")
									fo.write('%s\r\n%s\r\n\r\n' % (dest, msg))
									fo.close()


def MayaManTexturePreRenderScript():
	if maya.cmds.objExists('MayaManNugget'):
		PreRenderScript = maya.cmds.getAttr('MayaManNugget.PreRenderScript')
		command = r'python "try:\n\treload(roma)\nexcept:\n\timport idmt.maya.roma as roma\nroma.MayaManTexture(True)"'
		pattern = re.escape(command)
		if re.search(pattern, PreRenderScript, re.IGNORECASE) == None:
			PreRenderScript = '%s\n\n%s' % (PreRenderScript, command)
			maya.cmds.setAttr('MayaManNugget.PreRenderScript', PreRenderScript, typ = 'string')

def CheckUseRayTraceShadows():
	rs = True

	lights = maya.cmds.ls(lights = True)
	if lights == None:
		return rs
	for light in lights:
		if not maya.cmds.objExists(r'%s.useDepthMapShadows' % light):
			continue
		if not maya.cmds.objExists(r'%s.useRayTraceShadows' % light):
			continue
		if not maya.cmds.getAttr(r'%s.useRayTraceShadows' % light):
			continue
		parents = maya.cmds.listRelatives(light, parent = True)
		if not maya.cmds.getAttr(r'%s.visibility' % parents[0]):
			continue
		rs = False
		maya.OpenMaya.MGlobal.displayError(u'%s 勾选了Use Ray Trace Shadows，应该勾选Use Depth Map Shadows' % parents[0])
		continue

	return rs

def GetFrames(framesStr):
	m = re.search(r"^(-?\d+)(-(-?\d+))?$", framesStr)
	return m.groups()