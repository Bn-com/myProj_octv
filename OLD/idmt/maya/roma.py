# -*- coding: utf-8 -*-
# Copyright (C) 2000-2010 IDMT. All rights reserved.
'''
Tools for ROMA
'''
__author__	= 'huangzhongwei@idmt.com.cn'
__date__	= '2011-01-14'

from functools import partial
import datetime
import idmt.maya.cmds
import idmt.maya.path
import idmt.maya.customIDMTSetup
import maya.cmds
import maya.mel
import maya.OpenMaya
import os
import shutil
import re

import xpath
import xml.dom.minidom

def FixRiFilters(MotionBeginRif = ''):
	'''
	wrote by huangzhongwei
	'''
	if not maya.cmds.objExists('MayaManNugget'):
		return False
	
	folder = r'%s/plugins/windows/rman/32bit' % (os.getenv('PIPELINE_SCRIPTS').replace('\\', '/'))

	no = maya.cmds.MayaManInfo(getarraysize = 'RiFilter')
	for i in range(no-1, -1, -1):
		curRiFilter = maya.cmds.MayaManInfo(getrawstring = ('RiFilter', i))
		curRifName = os.path.basename(curRiFilter)
		
		delete = False
		for j in range(i):
			oldRiFilter = maya.cmds.MayaManInfo(getrawstring = ('RiFilter', j))
			oldRifName = os.path.basename(oldRiFilter)
			if re.compile(r'^(MotionBeginBeautyRif|MotionBeginRif)\.dll$', re.IGNORECASE).search(curRifName) != None:
				if re.compile(r'^(MotionBeginBeautyRif|MotionBeginRif)\.dll$', re.IGNORECASE).search(oldRifName) != None:
					delete = True
					break
			else:
				if re.compile(r'^%s$' % (re.escape(curRifName)), re.IGNORECASE).search(oldRifName) != None:
					delete = True
					break
		if delete:
			maya.OpenMaya.MGlobal.executeCommand(r'MayaManSetData -delarrayelement "RiFilter" %d' % (i), True)
			maya.OpenMaya.MGlobal.executeCommand(r'MayaManSetData -delarrayelement "RiFilterActive" %d' % (i), True)
			maya.OpenMaya.MGlobal.executeCommand(r'MayaManSetData -delarrayelement "RiFilterArgs" %d' % (i), True)
		else:
			if re.compile(r'^(MotionBeginBeautyRif|MotionBeginRif)\.dll$', re.IGNORECASE).search(curRifName) != None:
				if re.compile(r'^(MotionBeginBeautyRif|MotionBeginRif)\.dll$', re.IGNORECASE).search(MotionBeginRif) != None:
					newRiFilter = r'%s/%s' % (folder, MotionBeginRif)
				else:
					sceneName = maya.cmds.file(query=True, sceneName = True, shortName = True)
					if re.compile(r'_motionVector_', re.IGNORECASE).search(sceneName) != None:
						newRiFilter = r'%s/MotionBeginRif.dll' % (folder)
					else:
						newRiFilter = r'%s/MotionBeginBeautyRif.dll' % (folder)
			else:
				newRiFilter = r'%s/%s' % (folder, curRifName)
			if curRiFilter != newRiFilter:
				if os.path.isfile(newRiFilter):
					maya.OpenMaya.MGlobal.executeCommand(r'MayaManSetData -setstring "RiFilter" "%s" %d' % (newRiFilter, i), True)

	return True

def AddRiFilter(RifName, RiFilterArgs = ''):
	'''
	wrote by huangzhongwei
	'''
	if not maya.cmds.objExists('MayaManNugget'):
		return False
	
	FixRiFilters(RifName)

	find = False
	no = maya.cmds.MayaManInfo(getarraysize = 'RiFilter')
	for i in range(no):
		curRiFilter = maya.cmds.MayaManInfo(getrawstring = ('RiFilter', i))
		curRifName = os.path.basename(curRiFilter)
		if re.compile(r'^%s$' % (re.escape(RifName)), re.IGNORECASE).search(curRifName) != None:
			find = True
			break

	if find:
		return True

	RiFilter = r'%s/plugins/windows/rman/32bit/%s' % (os.getenv('PIPELINE_SCRIPTS').replace('\\', '/'), RifName)

	maya.OpenMaya.MGlobal.executeCommand(r'MayaManSetData -appendstring "RiFilter"       "%s"' % (RiFilter), True)
	maya.OpenMaya.MGlobal.executeCommand(r'MayaManSetData -appendbool   "RiFilterActive" 1', True)
	maya.OpenMaya.MGlobal.executeCommand(r'MayaManSetData -appendstring "RiFilterArgs"   "%s"' % (RiFilterArgs), True)

	if not maya.cmds.about(batch = True):
		if maya.cmds.scriptTable('rifFilters', exists = True):
			maya.cmds.scriptTable('rifFilters', edit = True, insertRow = no + 1)

	return True

def AddMotionBeginRif():
	'''
	wrote by huangzhongwei
	'''
	if not AddRiFilter('MotionBeginRif.dll'):
		return False
	
	idmt.maya.cmds.setAttr('MayaManNugget.MotionBlurOn', 1)
	idmt.maya.cmds.setAttr('MayaManNugget.MotionBlurVal', 100)
	idmt.maya.cmds.setAttr('MayaManNugget.VertexBlurOn', 1)
	idmt.maya.cmds.setAttr('MayaManNugget.VertexBlurVal', 100)
	idmt.maya.cmds.setAttr('MayaManNugget.CameraBlurOn', 1)
	idmt.maya.cmds.setAttr('MayaManNugget.CameraBlurVal', 100)

	return True

def ChangeEye(newEye = 'right'):
	'''
	wrote by huangzhongwei
	'''
	oldEye = ''
	oldShort = ''
	newShort = ''
	oldCamera = ''
	newCamera = ''
	oldName = u''
	newName = u''
	if newEye == 'left':
		oldEye = 'right'
		oldShort = 'R'
		newShort = 'L'
		oldCamera = 'camera_stereoRx'
		newCamera = 'original_camera'
		oldName = u'右'
		newName = u'左'
	elif newEye == 'right':
		oldEye = 'left'
		oldShort = 'L'
		newShort = 'R'
		oldCamera = 'original_camera'
		newCamera = 'camera_stereoRx'
		oldName = u'左'
		newName = u'右'

	# unbake renderable
	cameras = maya.cmds.ls(cameras = True)
	for camera in cameras:
		connections = maya.cmds.listConnections(r'%s.renderable' % (camera), connections = True, plugs = True, destination = False)
		if connections == None:
			continue
		for i in range(0, len(connections), 2):
			lock = maya.cmds.getAttr(connections[i], lock = True)
			if lock:
				maya.cmds.setAttr(connections[i], lock = False)
			maya.OpenMaya.MGlobal.executeCommand(r'disconnectAttr "%s" "%s"' % (connections[i+1], connections[i]), True)
			if lock:
				maya.cmds.setAttr(connections[i], lock = True)

	# filename
	sceneName = maya.cmds.file(query=True, sceneName = True, shortName =True)
	if re.compile(r'^lighting_', re.IGNORECASE).search(sceneName) != None:
		if re.compile(r'_[LR]\.', re.IGNORECASE).search(sceneName) == None:
			maya.OpenMaya.MGlobal.displayError(u'文件命名不规范')
			return
	sceneName = re.compile(r'_[LR]\.', re.IGNORECASE).sub(r'_%s.' % (newShort), sceneName)

	# import camera
	folder = maya.mel.eval('zwGetPath("stereo_cams_approved", "")')
	if folder == '':
		maya.OpenMaya.MGlobal.displayError(u'文件命名不规范')
		return
	path = ''
	filenames = []
	if os.path.isdir(folder):
		files = os.listdir(folder)
		for filename in files:
			if re.compile(r'_%sx[\._].*m[ab]$' % (newShort), re.IGNORECASE).search(filename) != None:
				filenames.append(filename)
	if len(filenames) == 0:
		maya.OpenMaya.MGlobal.displayError(u'找不到%s眼摄像机文件' % (newName))
		return
	elif len(filenames) == 1:
		path = os.path.join(folder, filenames[0])
	else:
		filename = maya.cmds.confirmDialog(title = u'转%s眼工具' % newName, message= u'多于一个%s眼摄像机文件，请选择：' % newName, button = filenames, dismissString = '')
		if filename == '':
			return
		path = os.path.join(folder, filename)

	if not maya.cmds.objExists(oldCamera):
		maya.OpenMaya.MGlobal.displayError(u'找不到%s眼摄像机，不能转换成%s眼' % (oldName, newName))
		return
	if maya.cmds.objExists(newCamera):
		maya.OpenMaya.MGlobal.executeCommand(r'delete "%s"' % (newCamera), True)

	allCamBefore = maya.cmds.ls(cameras = True)
	maya.OpenMaya.MGlobal.executeCommand(r'file -import "%s"' % (path), True)

	# rename camera
	if not maya.cmds.objExists(newCamera):
		allCamAfter = maya.cmds.ls(cameras = True)
		for camera in allCamAfter:
			if camera not in allCamBefore:
				newCamTrans = maya.cmds.listRelatives(camera, parent = True)[0]
				maya.OpenMaya.MGlobal.executeCommand(r'rename "%s" "%s"' % (newCamTrans, newCamera), True)
				break

	# set camera
	allCamAfter = maya.cmds.ls(cameras = True)
	for camera in allCamAfter:
		if re.compile(r'_idpass_', re.IGNORECASE).search(sceneName) != None:
			idmt.maya.cmds.setAttr(r'%s.mask' % (camera), 0)
		elif re.compile(r'_occlusionNormal_', re.IGNORECASE).search(sceneName) != None:
			backgroundColor = maya.cmds.getAttr(r'%s.backgroundColor' % (camera))
			if backgroundColor[0][0] != 1.0 or backgroundColor[0][1] != 1.0 or backgroundColor[0][1] != 1.0:
				maya.OpenMaya.MGlobal.executeCommand(r'setAttr "%s.backgroundColor" -type double3 1 1 1' % (camera), True)

	#attr = 'nearClipPlane'
	#idmt.maya.cmds.setAttr(r'%s.%s' % (newCamera, attr), max(maya.cmds.getAttr(r'%s.%s' % (oldCamera, attr)), 0.001))
	#attrs = ('farClipPlane', 'bestFitClippingPlanes', 'image', 'depth', 'overscan')
	#for attr in attrs:
	#	idmt.maya.cmds.setAttr(r'%s.%s' % (newCamera, attr), maya.cmds.getAttr(r'%s.%s' % (oldCamera, attr)))
	attrs = ('nearClipPlane', 'farClipPlane', 'bestFitClippingPlanes', 'image', 'depth', 'overscan')
	for attr in attrs:
		maya.cmds.connectAttr(r'%s.%s' % (oldCamera, attr), r'%s.%s' % (newCamera, attr), force = True)
		maya.cmds.disconnectAttr(r'%s.%s' % (oldCamera, attr), r'%s.%s' % (newCamera, attr))
	idmt.maya.cmds.setAttr(r'%s.renderable' % (oldCamera), 0)
	idmt.maya.cmds.setAttr(r'%s.renderable' % (newCamera), 1)

	# lodGroup
	oldCameraShape = maya.cmds.listRelatives(oldCamera, shapes = True)
	lodGroups = maya.cmds.listConnections('%s.worldMatrix' % (oldCameraShape[0]), plugs = True, source = False, t = 'lodGroup')
	if lodGroups != None:
		newCameraShape = maya.cmds.listRelatives(newCamera, shapes = True)
		for lodGroup in lodGroups:
			maya.cmds.connectAttr('%s.worldMatrix' % (newCameraShape[0]), lodGroup, force = True)

	# layer
	layers = maya.cmds.listConnections('renderLayerManager.renderLayerId')
	for layer in layers:
		new = layer.replace(r'_%s' % (oldEye), r'_%s' % (newEye))
		if new != layer:
			maya.OpenMaya.MGlobal.executeCommand(r'rename "%s" "%s"' % (layer, new), True)
	
	if maya.cmds.objExists('MayaManNugget'):
		# Output Directories
		old = maya.cmds.getAttr('MayaManNugget.ImageOutputDir')
		old = old.replace('\\', '/')
		new = old.replace(r'/footage_%s/' % (oldShort), r'/footage_%s/' % (newShort))
		idmt.maya.cmds.setAttr('MayaManNugget.ImageOutputDir', new)
	
		# Extra Output Channels
		EOTypes = maya.cmds.MayaManInfo(getarraysize = 'EOType')
		for i in range(EOTypes):
			old = maya.cmds.MayaManInfo(getrawstring = ('EOPath', i))
			old = old.replace('\\', '/')
			new = old.replace(r'_%s' % (oldEye), r'_%s' % (newEye))
			new = new.replace(r'/footage_%s/' % (oldShort), r'/footage_%s/' % (newShort))
			if new != old:
				maya.OpenMaya.MGlobal.executeCommand(r'MayaManSetData -setstring "EOPath" "%s" %d' % (new, i), True)
		if not maya.cmds.about(batch = True):
			if maya.cmds.scriptTable('chansList', exists = True):
				maya.mel.eval('mayaManExtraChannelsRefreshList')

	# rename
	maya.mel.eval(r'file -rename "%s"' % (sceneName))

	if not maya.cmds.about(batch = True):
		import win32con
		import win32clipboard	
		win32clipboard.OpenClipboard()
		win32clipboard.EmptyClipboard()
		win32clipboard.SetClipboardData(win32con.CF_UNICODETEXT, sceneName) 
		win32clipboard.CloseClipboard()
		maya.cmds.confirmDialog(button = 'OK', message = u'1）已经更改为“%s”眼相机，\n\n2）文件已重命名，新名字在剪切板，确认后请存盘' %(newName))

def ModifyRib(folder):
	'''
	修改rib文件里面的路径
	'''
	folder = idmt.maya.path.GetFullPath(folder)
	folder = folder.replace('/', '\\')
	for root, dirs, files in os.walk(folder):
		for rib in files:
			if re.compile(r'\.rib$', re.IGNORECASE).search(rib) == None:
				continue
			if re.compile(r'shave', re.IGNORECASE).search(rib) != None:
				if re.compile(r'\.1\.rib$', re.IGNORECASE).search(rib) == None:
					continue
			source = root + "\\" + rib
			
			backupFile = re.compile(r'.*\PRJ_roma\\', re.IGNORECASE).sub(r'\\\\file-cluster\\GDC\\Netrender\\Maya_Even\\T150\\ribs\\%s\\' % (datetime.datetime.now().strftime('%Y%m%d')), source)
			if backupFile == source:
				backupFile = r'\\\\file-cluster\\GDC\\Netrender\\Maya_Even\\T150\\ribs\\%s\\%s\\%s' % (datetime.datetime.now().strftime('%Y%m%d'), os.getenv('COMPUTERNAME'), source.replace(':', '$'))
			if not os.path.isfile(backupFile):
				backupFolder = re.sub(r'[/\\][^/\\]*$', '', backupFile)
				if not os.path.isdir(backupFolder):
					os.makedirs(backupFolder)
				shutil.copy(source, backupFile)
			
			tempRib = os.getenv('TEMP') + "\\" + rib
			if os.path.isfile(tempRib):
				os.remove(tempRib)
			command = "\\\\file-cluster\\GDC\\Resource\\Support\\Pixar\\RenderManProServer-13.5.2\\bin\\catrib.exe -ascii -o \"%s\" \"%s\"" % (tempRib, source)
			print command;
			os.popen(command).read()
			
			try:
				temp = os.getenv('TEMP') + "\\temp.rib"
				if os.path.isfile(temp):
					os.remove(temp)

				find = False
				fi = open(tempRib, "r")
				fo = open(temp, "w")
				while True:
					oldLine = fi.readline()
					if not oldLine:
						break
					newLine = re.compile(r'"[^"]*MC_roma/', re.IGNORECASE).sub(r'"//file-cluster/GDC/Projects/ROMA/PRJ_roma/MC_roma/', oldLine)
					newLine = re.compile(r'\"scenes/', re.IGNORECASE).sub(r'"//file-cluster/GDC/Projects/ROMA/PRJ_roma/MC_roma/scenes/', newLine)
					#newLine = re.compile(r'\"(//file-cluster/GDC/Projects/ROMA/PRJ_roma/MC_roma/)?scenes/props/Vegetation/grass/smallGrass01/foliage/ribs/grassClump01B_GR_01.rib\"', re.IGNORECASE).sub(r'"//file-cluster/GDC/Projects/ROMA/PRJ_roma/MC_roma/scenes/props/Vegetation/miscFoliage/grassClump01B/foliage/ribs/grassClump01B_GR_01/grassClump01B_GR_01.rib"', newLine)
					#newLine = re.compile(r'\"(//file-cluster/GDC/Projects/ROMA/PRJ_roma/MC_roma/)?scenes/props/Vegetation/grass/smallGrass02/foliage/ribs/grassclump01B_04.rib\"', re.IGNORECASE).sub(r'"//file-cluster/GDC/Projects/ROMA/PRJ_roma/MC_roma/scenes/props/Vegetation/miscFoliage/grassClump01B/foliage/ribs/grassclump01B_04/grassclump01B_04.rib"', newLine)
					if re.compile(r'\\Projects\\ROMA\\PRJ_roma\\MC_roma\\ribexport\\', re.IGNORECASE).search(source) != None:
						newLine = re.compile(r'\[\"([^/][^\"]+\.tex)\"]', re.IGNORECASE).sub(r'["//file-cluster/GDC/Projects/ROMA/PRJ_roma/MC_roma/ribexport/tex_cache/prman/\g<1>"]', newLine)
						newLine = re.compile(r'\"(texturing_Roma_[a-z0-9]+_[a-z0-9]+_RND/[^\"]+)\"', re.IGNORECASE).sub(r'"//file-cluster/GDC/Projects/ROMA/PRJ_roma/MC_roma/ribexport/\g<1>"', newLine)
					newLine = re.compile(r'\[\"([^/]+\.rib)\"\]', re.IGNORECASE).sub(r'["%s/\g<1>"]' % (root.replace('\\', '/')), newLine)
					newLine = re.compile(r'\[\"ribs/([^\"]+)\"\]', re.IGNORECASE).sub(r'["%s/\g<1>"]' % (root.replace('\\', '/')), newLine)
					if oldLine != newLine:
						find = True
					fo.write(newLine)
				fi.close()
				fo.close()
				if find:
					maya.mel.eval(r'zwSysFile "move" "%s" "%s" true' % (temp.replace('\\', '\\\\'), source.replace('\\', '\\\\')))
				else:
					os.remove(temp)
				os.remove(tempRib)
			except:
				pass

def FixedReference(envName = 'MC_roma'):
	'''
	environment, fixed
	'''
	rs = True

	envValue = os.getenv(envName, '')
	references = maya.cmds.file(query = True, reference = True)
	for reference in references:
		unresolvedName = maya.cmds.referenceQuery(reference, filename = True, unresolvedName = True, withoutCopyNumber = True)
		if re.compile(r'^\${' + envName + '}', re.IGNORECASE).search(unresolvedName) != None and re.compile(r'/scenes/characters/([^/]+/){3}[^/]+$', re.IGNORECASE).search(unresolvedName) == None:
			continue
		if re.compile(r'/scenes/characters/([^/]+/){3}[^/]+$', re.IGNORECASE).search(unresolvedName) != None:
			unresolvedName = re.sub('([^/]+)$', 'fixed/\g<1>', unresolvedName)
		dollarPath = idmt.maya.path.GetDollarPath(unresolvedName)
		if re.compile(r'^\${' + envName + '}', re.IGNORECASE).search(dollarPath) == None:
			if envValue == '':
				maya.OpenMaya.MGlobal.displayError(u'没有设置 %s 环境变量' % (envName))
				return False
			maya.OpenMaya.MGlobal.displayError(u'所有reference必须指向%s\n%s' % (envValue, reference))
			rs = False
		else:
			expandName = maya.cmds.workspace(expandName = dollarPath)
			if os.path.isfile(expandName):
				unloaded = maya.cmds.referenceQuery(reference, nodes = True) == []

				node = maya.cmds.file(reference, query = True, referenceNode = True)
				maya.cmds.file(dollarPath, loadReference = node)

				unresolvedName = maya.cmds.referenceQuery(node, filename = True, unresolvedName = True, withoutCopyNumber = True)
				if re.compile(r'^\${' + envName + '}', re.IGNORECASE).search(unresolvedName) == None:
					maya.cmds.file(dollarPath, loadReference = node)
				unresolvedName = maya.cmds.referenceQuery(node, filename = True, unresolvedName = True, withoutCopyNumber = True)
				if re.compile(r'^\${' + envName + '}', re.IGNORECASE).search(unresolvedName) == None:
					maya.OpenMaya.MGlobal.displayError(u'不能修改参考文件的路径：%s' % (reference))
					rs = False
				if unloaded == True:
					maya.cmds.file(unloadReference = node)
			else:
				maya.OpenMaya.MGlobal.displayError(u'所有reference必须指向%s\n%s' % (envValue, reference))
				rs = False

	return rs

def FixTextureFilename():
	'''
	remove space
	'''
	ress = ('4k', '2k', '1k', '512', '256')
	files = maya.cmds.ls(type = 'file')

	# filename
	sceneName = maya.cmds.file(query=True, sceneName = True, shortName =True)
	preRes = '4k'
	if re.compile(r'_owl0', re.IGNORECASE).search(sceneName) != None:
		preRes = '2k'
	for node in files:
		fileTextureName = maya.cmds.getAttr('%s.fileTextureName' % (node))
		filename = os.path.basename(fileTextureName)
		
		sourceimages = re.compile(r'/scenes/', re.IGNORECASE).sub('/sourceimages/', fileTextureName)
		if sourceimages != fileTextureName:
			sourceimages = os.path.join(os.path.dirname(sourceimages), preRes, filename)
			path = maya.cmds.workspace(expandName = sourceimages)
			if os.path.isfile(path):
				maya.OpenMaya.MGlobal.executeCommand(r'setAttr -type "string" "%s.fileTextureName" "%s"' % (node, sourceimages.replace('\\', '/')), True)
				fileTextureName = sourceimages
		
		path = maya.cmds.workspace(expandName = fileTextureName)
		folder = os.path.dirname(path)
		newName = filename
		newName = re.sub('\s*_\s*', '_', newName)
		newName = re.sub('\s*\.\s*', '.', newName)
		newName = re.sub('^\s+|\s+$', '', newName)
		newName = re.sub('\s+', '_', newName)
		newName = re.compile(r'\.tif4$', re.IGNORECASE).sub('.tif', newName)
		if newName != filename:
			for res in ress:
				oldPath = os.path.join(os.path.dirname(folder), res, filename)
				newPath = os.path.join(os.path.dirname(folder), res, newName)
				if os.path.isfile(oldPath) and not os.path.isfile(newPath):
					maya.mel.eval(r'zwSysFile "ren" "%s" "%s" true' % (oldPath.replace('\\', '/'), newPath.replace('\\', '/')))
					if not os.path.isfile(newPath):
						maya.mel.eval(r'zwSysFile "copy" "%s" "%s" true' % (oldPath.replace('\\', '/'), newPath.replace('\\', '/')))
			newPath = os.path.join(os.path.dirname(path), newName)
			if os.path.isfile(path) and not os.path.isfile(newPath):
				maya.mel.eval(r'zwSysFile "ren" "%s" "%s" true' % (path.replace('\\', '/'), newPath.replace('\\', '/')))
				if not os.path.isfile(newPath):
					maya.mel.eval(r'zwSysFile "copy" "%s" "%s" true' % (path.replace('\\', '/'), newPath.replace('\\', '/')))
			if os.path.isfile(newPath):
				maya.OpenMaya.MGlobal.executeCommand(r'setAttr -type "string" "%s.fileTextureName" "%s"' % (node, os.path.join(os.path.dirname(fileTextureName), newName).replace('\\', '/')), True)

def FixOwlTexture():
	'''
	remove space
	'''
	ress = ('4k', '2k', '1k', '512', '256')
	files = maya.cmds.ls(type = 'file')

	for node in files:
		fileTextureName = maya.cmds.getAttr('%s.fileTextureName' % (node))
		filename = os.path.basename(fileTextureName)
		
		sourceimages = re.compile(r'/scenes/', re.IGNORECASE).sub('/sourceimages/', fileTextureName)
		if sourceimages != fileTextureName:
			sourceimages = os.path.join(os.path.dirname(sourceimages), '2k', filename)
			path = maya.cmds.workspace(expandName = sourceimages)
			if os.path.isfile(path):
				maya.OpenMaya.MGlobal.executeCommand(r'setAttr -type "string" "%s.fileTextureName" "%s"' % (node, sourceimages.replace('\\', '/')), True)
				fileTextureName = sourceimages

def Modeling2Texturing():
	'''
	Modeling2Texturing
	'''
	references = maya.mel.eval('sceneEditor -query -selectItem $gReferenceEditorPanel')
	if references == None:
		references = []
	if len(references) == 0:
		references = maya.cmds.file(query = True, reference = True)
	if references == None:
		return

	for reference in references:
		modeling = maya.cmds.referenceQuery(reference, filename = True, unresolvedName = True, withoutCopyNumber = True)
		folder = re.sub(r'/modeling/.*', '', modeling)
		if folder == modeling:
			continue
		folder = re.compile(r'/characters/.*$', re.IGNORECASE).sub('\g<0>/fixed', folder)
		folder = maya.cmds.workspace(expandName = folder)
		if not os.path.isdir(folder):
			continue
		files = os.listdir(folder)
		for filename in files:
			if re.compile(r'^texturing_.*_RND\.m[ab]$', re.IGNORECASE).search(filename) != None:
				texturing = os.path.join(folder, filename)
				texturing = idmt.maya.path.GetDollarPath(texturing)
				node = maya.cmds.file(reference, query = True, referenceNode = True)
				maya.cmds.file(texturing, loadReference = node)
				break

def Modeling2Foliage():
	'''
	Modeling2Texturing
	'''
	references = maya.mel.eval('sceneEditor -query -selectItem $gReferenceEditorPanel')
	if references == None:
		references = []
	if len(references) == 0:
		references = maya.cmds.file(query = True, reference = True)
	if references == None:
		return

	for reference in references:
		modeling = maya.cmds.referenceQuery(reference, filename = True, unresolvedName = True, withoutCopyNumber = True)
		folder = re.sub(r'/modeling/.*', '/foliage', modeling)
		if folder == modeling:
			continue
		folder = maya.cmds.workspace(expandName = folder)
		if not os.path.isdir(folder):
			continue
		files = os.listdir(folder)
		for filename in files:
			if re.compile(r'^foliage_.*_RND\.m[ab]$', re.IGNORECASE).search(filename) != None:
				texturing = os.path.join(folder, filename)
				texturing = idmt.maya.path.GetDollarPath(texturing)
				node = maya.cmds.file(reference, query = True, referenceNode = True)
				maya.cmds.file(texturing, loadReference = node)
				break

def Hig2Rnd():
	'''
	Hig2Rnd
	'''
	references = maya.mel.eval('sceneEditor -query -selectItem $gReferenceEditorPanel')
	if references == None:
		references = []
	if len(references) == 0:
		references = maya.cmds.file(query = True, reference = True)
	if references == None:
		return

	for reference in references:
		hig = maya.cmds.referenceQuery(reference, filename = True, unresolvedName = True, withoutCopyNumber = True)
		rnd = hig
		rnd = re.compile(r'(/scenes/characters/([^/]+/){3})([^/]+)$', re.IGNORECASE).sub('\g<1>fixed/\g<3>', rnd)
		rnd = re.sub(r'_HIG', '_RND', rnd)
		rnd = re.sub(r'setup_', 'texturing_', rnd)
		rnd = idmt.maya.path.GetDollarPath(rnd)
		if rnd != hig and os.path.isfile(maya.cmds.workspace(expandName = rnd)):
			node = maya.cmds.file(reference, query = True, referenceNode = True)
			maya.cmds.file(rnd, loadReference = node)

def Rnd2Prx():
	'''
	Rnd2Prx
	'''
	references = maya.mel.eval('sceneEditor -query -selectItem $gReferenceEditorPanel')
	if references == None:
		references = []
	if len(references) == 0:
		references = maya.cmds.file(query = True, reference = True)
	if references == None:
		return

	for reference in references:
		rnd = maya.cmds.referenceQuery(reference, filename = True, unresolvedName = True, withoutCopyNumber = True)
		prx = rnd
		prx = re.compile(r'/foliage/[^_]+_([^/]+)$', re.IGNORECASE).sub('/modeling/modeling_\g<1>', prx)
		prx = re.sub(r'_RND', '_PRX', prx)
		prx = idmt.maya.path.GetDollarPath(prx)
		if prx != rnd and os.path.isfile(maya.cmds.workspace(expandName = prx)):
			node = maya.cmds.file(reference, query = True, referenceNode = True)
			maya.cmds.file(prx, loadReference = node)

def GetPartByEpisode(episode = None):
	part = ''

	if episode == None:
		sceneName = maya.cmds.file(query=True, sceneName = True)
		m = re.compile(r'[/\\](\d{4}\.\d{2}\.\d{2}-\d{2}\.\d{2}\.\d{2}@)?([0-9a-z]+_([0-9a-z]+)(_[0-9a-z]+)*)\.[0-9a-z]+$', re.IGNORECASE).search(sceneName)
		if m == None:
			return part
		episode = m.group(3)

	dom = xml.dom.minidom.parse(r'\\file-cluster\GDC\Projects\ROMA\ROMA_Scratch\roma_dfs.xml')
	doc = dom.documentElement
	path = "//row[translate(sq, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz')='%s']/part" % episode.lower()
	parts = xpath.findvalues(path, doc)
	if len(parts) == 1:
		part = parts[0]

	return part

def GetShaveRibPath(episode = None):
	part = ''

	if episode == None:
		sceneName = maya.cmds.file(query=True, sceneName = True)
		m = re.compile(r'[/\\](\d{4}\.\d{2}\.\d{2}-\d{2}\.\d{2}\.\d{2}@)?([0-9a-z]+_([0-9a-z]+)(_[0-9a-z]+)*)\.[0-9a-z]+$', re.IGNORECASE).search(sceneName)
		if m == None:
			return part
		episode = m.group(3)

	part = GetPartByEpisode(episode)
	
	#if part == 'partA':
	#	part = 'partB'
	#elif part == 'partB':
	#	part = 'partC'
	#elif part == 'partC':
	#	part = 'partD'
	#elif part == 'partD':
	#	part = 'partE'
	#elif part == 'partE':
	#	part = 'partA'
	#else:
	#	return ''
	if part == '':
		return ''

	path = '//file-cluster/GDC/Netrender/Scenes/ROMA/ShaveRib/%s/sq_%s' % (part, episode)

	return path

def GetRibPath():
	part = ''

	sceneName = maya.cmds.file(query=True, sceneName = True)
	if sceneName == '':
		sceneName = os.getenv('sceneName', '')
	m = re.compile(r'[/\\](\d{4}\.\d{2}\.\d{2}-\d{2}\.\d{2}\.\d{2}@)?([0-9a-z]+_([0-9a-z]+)_([0-9a-z]+)(_[0-9a-z]+)*)\.[0-9a-z]+$', re.IGNORECASE).search(sceneName)
	if m == None:
		return part
	sq = m.group(3)
	sc = m.group(4)

	part = GetPartByEpisode(sq)
	if part == '':
		return ''

	path = '//file-cluster/GDC/Netrender/Scenes/ROMA/Rib/%s/sq_%s/sc_%s' % (part, sq, sc)

	return path

def autoSetForRendering():
	'''
	建层工具，覆盖RBW的
	'''
	sceneName = maya.cmds.file(query=True, sceneName = True)
	m = re.compile(r'[/\\](\d{4}\.\d{2}\.\d{2}-\d{2}\.\d{2}\.\d{2}@)?([0-9a-z]+_([0-9a-z]+)(_[0-9a-z]+)*)\.[0-9a-z]+$', re.IGNORECASE).search(sceneName)
	if m == None:
		maya.OpenMaya.MGlobal.displayError(u'文件命名不规范')
		return
	episode = m.group(3)
	if re.search('_(ptc|occlusion)_', sceneName, re.IGNORECASE) != None:
		part = GetPartByEpisode(episode)
		if part == '':
			maya.OpenMaya.MGlobal.displayError(u'不能根据场次指定ptc路径，请联系TD')
			return

	import RBW.SC.lighting.autoSetForRendering
	RBW.SC.lighting.autoSetForRendering.autoSetForRendering()

	idmt.maya.cmds.setAttr('defaultRenderGlobals.extensionPadding', 4)
	idmt.maya.cmds.setAttr('MayaManNugget.ExternalTextureCache', 2)

	sceneName = maya.cmds.file(query=True, sceneName = True)
	if re.search('_(env|veg)[^_]*_ptc_', sceneName, re.IGNORECASE) != None:
		idmt.maya.cmds.setAttr('MayaManNugget.ShadingRate', 8.0)
		idmt.maya.cmds.setAttr('MayaManNugget.PixelSamplesX', 1.0)
		idmt.maya.cmds.setAttr('MayaManNugget.PixelSamplesY', 1.0)
		idmt.maya.cmds.setAttr('defaultResolution.width', 1024)
		idmt.maya.cmds.setAttr('defaultResolution.height', 436)

	parity = 'Even'
	sceneName = maya.cmds.file(query=True, sceneName = True)
	m = re.compile(r'[/\\](\d{4}\.\d{2}\.\d{2}-\d{2}\.\d{2}\.\d{2}@)?([0-9a-z]+_([0-9a-z]+)(_[0-9a-z]+)*)\.[0-9a-z]+$', re.IGNORECASE).search(sceneName)
	if m == None:
		return
	sceneName = m.group(2).replace('_ptc_', '_occlusion_')
	episode = m.group(3)
	episodeStr = re.sub(r'[^0-9]+$', '', episode)
	m = re.search('[13579]$', episodeStr)
	if(m != None):
		parity = 'Odd'

	old = maya.cmds.getAttr('MayaManNugget.UserRibOptions')
	##UserRibOptions = old.replace(r'"$(PROJECTDIR)/mayaman/ptc/$(SCENENAME).$(FRAME).ptc"', r'"//file-cluster/GDC/Netrender/Scenes/renderTex/ptc/%s/%s/%s.$(FRAME).ptc"' % (parity, sceneName, sceneName))
	#UserRibOptions = re.compile(r'Attribute \"user\" \"string filename\" \[\"[^\"]+\"\]').sub(r'Attribute "user" "string filename" ["//file-cluster/GDC/Netrender/Scenes/renderTex/ptc/%s/%s/%s.$(FRAME).ptc"]' % (parity, sceneName, sceneName), old)

	#if UserRibOptions != old:
	#	folder = r'//file-cluster/GDC/Netrender/Scenes/renderTex/ptc/%s/%s' % (parity, sceneName)
	#	if not os.path.isdir(folder):
	#		os.makedirs(folder)
	#	maya.cmds.setAttr('MayaManNugget.UserRibOptions', UserRibOptions, type = 'string')
	
	part = GetPartByEpisode(episode)
	ptcFolderOld =   r'//file-cluster/GDC/Netrender/Scenes/renderTex/ptc/%s/%s' % (parity, sceneName)
	ptcFolderNew =   r'//file-cluster/GDC/Netrender/Scenes/ROMA/ptc/%s/sq_%s/%s' % (part, episode, sceneName)
	#ptcFolder = ''
	#if os.path.isdir(ptcFolderNew) or not os.path.isdir(ptcFolderOld):
	#	ptcFolder = ptcFolderNew
	#else:
	#	ptcFolder = ptcFolderOld
	ptcFolder = ptcFolderNew
	UserRibOptions = re.compile(r'Attribute \"user\" \"string filename\" \[\"[^\"]+\"\]').sub(r'Attribute "user" "string filename" ["%s/%s.$(FRAME).ptc"]' % (ptcFolder, sceneName), old)
	if UserRibOptions != old:
		if not os.path.isdir(ptcFolder):
			os.makedirs(ptcFolder)
		maya.cmds.setAttr('MayaManNugget.UserRibOptions', UserRibOptions, type = 'string')

	sceneName = maya.cmds.file(query=True, sceneName = True)
	if re.search('_contactOcclusion_|_occlusion_', sceneName) != None:
		idmt.maya.cmds.setAttr('MayaManNugget.MinShadowBias', 0.2)
	
	if re.search('_occlusion_', sceneName) != None:
		old = maya.cmds.getAttr('MayaManNugget.UserRibOptions')
		UserRibOptions = re.compile(r'Attribute \"user\" \"float samplebase\" \[[^\]]+\]').sub(r'Attribute "user" "float samplebase" [1]', old)
		if UserRibOptions != old:
			maya.cmds.setAttr('MayaManNugget.UserRibOptions', UserRibOptions, type = 'string')
	
	m = re.compile(r'[/\\](\d{4}\.\d{2}\.\d{2}-\d{2}\.\d{2}\.\d{2}@)?[0-9a-z]+_([0-9a-z]+)_([0-9a-z]+)_([0-9a-z]+)_idpass\d*_(L|R)\.[0-9a-z]+$', re.IGNORECASE).search(sceneName)
	if m != None:
		episode = m.group(2)
		scene = m.group(3)
		character = m.group(4)
		LR = m.group(5).upper()
		LeftRight = 'left'
		if LR == 'R':
			LeftRight = 'right'
		EOChannels = []
		MatteNodes = maya.cmds.ls(type = 'MatteNode')
		if MatteNodes != None:
			for MatteNode in MatteNodes:
				for i in range(1, 41):
					if i in EOChannels:
						continue
					matteColor = maya.cmds.getAttr('%s.matteColor%02d' % (MatteNode, i))
					if matteColor[0][0] >= 0.001 or matteColor[0][1] >= 0.001 or matteColor[0][2] >= 0.001:
						EOChannels.append(i)
					else:
						connections = maya.cmds.listConnections('%s.matteColor%02d' % (MatteNode, i), destination = False)
						if connections != None:
							if len(connections) > 0:
								EOChannels.append(i)
		EOChannels.sort()
		for EOChannel in EOChannels:
			find = False
			noOfElements = maya.cmds.MayaManInfo(getarraysize = 'EOType')
			for i in range(noOfElements):
				if maya.cmds.MayaManInfo(getrawstring = ['EOChannel', i]) == '__matteColor%02d' % (EOChannel):
					find = True
					break
			if not find:
				maya.mel.eval('MayaManAddExtraOutputChannel(\"__matteColor%02d\", 1, true, 0, 0, 1, 0, 65535, 0, 65535, \"\", 0, 0, \"\", \"\", \"\", \"\")' % (EOChannel))
				EOPath = '$(PROJECTDIR)/images/sq_%s/sc_%s/footage_%s/%s/idpass%02d/sq_%s_sc_%s_%s_idp%02d_%s' % (episode, scene, LR, character, EOChannel, episode, scene, character, EOChannel, LeftRight)
				maya.cmds.MayaManSetData(setstring = ['EOPath', EOPath, noOfElements])
		if not maya.cmds.about(batch = True):
			if maya.cmds.scriptTable('chansList', exists = True):
				maya.mel.eval('mayaManExtraChannelsRefreshList')
	FixRiFilters()

def DelTmp(delete = False):
	'''
	整理lighting的tmp，只保留3个版本
	'''
	size = 0
	SHOT_roma = r'\\file-cluster\GDC\Projects\ROMA\PRJ_roma\SHOT_roma'
	scenes = os.listdir(SHOT_roma)
	for scene in scenes:
		if re.compile(r'^sq_', re.IGNORECASE).search(scene) == None:
			continue
		path = os.path.join(SHOT_roma, scene)
		if not os.path.isdir(path):
			continue
		shots = os.listdir(path)
		for shot in shots:
			path = os.path.join(SHOT_roma, scene, shot, r'scenes\lighting')
			if not os.path.isdir(path):
				continue
			characters = os.listdir(path)
			for character in characters:
				path = os.path.join(SHOT_roma, scene, shot, r'scenes\lighting', character)
				if not os.path.isdir(path):
					continue
				LRs = os.listdir(path)
				for LR in LRs:
					path = os.path.join(SHOT_roma, scene, shot, r'scenes\lighting', character, LR, 'tmp')
					if not os.path.isdir(path):
						continue
					tmpFilenames = os.listdir(path)
					filenames = os.listdir(os.path.join(SHOT_roma, scene, shot, r'scenes\lighting', character, LR))
					for filename in filenames:
						old = []
						for tmpFilename in tmpFilenames:
							s = re.sub(r'^\d{4}\.\d{2}\.\d{2}-\d{2}\.\d{2}\.\d{2}@', '', tmpFilename)
							if not (s != tmpFilename and s == filename):
								continue
							old.append(tmpFilename)
						if len(old) <= 3:
							continue
						old.sort()
						
						date_string = re.sub(r'@.*$', '', old[len(old)-1])
						d0 = datetime.datetime.strptime(date_string, '%Y.%m.%d-%H.%M.%S')
						i7 = -1
						for i in range(len(old)-2, -1, -1):
							date_string = re.sub(r'@.*$', '', old[i])
							d1 = datetime.datetime.strptime(date_string, '%Y.%m.%d-%H.%M.%S')
							dTime = d0 - d1
							if dTime.days >= 7:
								i7 = i
								break

						if i7 == -1:
							i7 = 0
						elif i7 > len(old)-3:
							i7 = len(old)-3
						for i in range(len(old)-2):
							if i == i7:
								continue
							tmp = os.path.join(SHOT_roma, scene, shot, r'scenes\lighting', character, LR, 'tmp', old[i])
							if not os.path.isfile(tmp):
								continue
							statinfo = os.stat(tmp)
							size = size + statinfo.st_size
							print tmp
							if delete:
								os.remove(tmp)
	print (r'SIZE: %d' % (size))

def DelFinishingTmp(delete = False):
	'''
	整理lighting的tmp，只保留3个版本
	'''
	size = 0
	SHOT_roma = r'\\file-cluster\GDC\Projects\ROMA\PRJ_roma\SHOT_roma'
	scenes = os.listdir(SHOT_roma)
	for scene in scenes:
		if re.compile(r'^sq_', re.IGNORECASE).search(scene) == None:
			continue
		path = os.path.join(SHOT_roma, scene)
		if not os.path.isdir(path):
			continue
		shots = os.listdir(path)
		for shot in shots:
			path = os.path.join(SHOT_roma, scene, shot, r'scenes\finishing')
			if not os.path.isdir(path):
				continue
			characters = os.listdir(path)
			for character in characters:
				path = os.path.join(SHOT_roma, scene, shot, r'scenes\finishing', character, 'tmp')
				if not os.path.isdir(path):
					continue
				tmpFilenames = os.listdir(path)
				filenames = os.listdir(os.path.join(SHOT_roma, scene, shot, r'scenes\finishing', character))
				for filename in filenames:
					old = []
					for tmpFilename in tmpFilenames:
						s = re.sub(r'^\d{4}\.\d{2}\.\d{2}-\d{2}\.\d{2}\.\d{2}@', '', tmpFilename)
						if not (s != tmpFilename and s == filename):
							continue
						old.append(tmpFilename)
					old.sort()
					for i in range(len(old)-1, -1, -1):
						tmp1 = os.path.join(SHOT_roma, scene, shot, r'scenes\finishing', character, 'tmp', old[i])
						if not os.path.isfile(tmp1):
							continue
						statinfo1 = os.stat(tmp1)
						for j in range(i-1, -1, -1):
							tmp2 = os.path.join(SHOT_roma, scene, shot, r'scenes\finishing', character, 'tmp', old[j])
							if not os.path.isfile(tmp2):
								continue
							statinfo2 = os.stat(tmp2)
							if statinfo1.st_mtime == statinfo2.st_mtime:
								size = size + statinfo2.st_size
								print tmp2
								if delete:
									os.remove(tmp2)
	print (r'SIZE: %d' % (size))

def GenLog():
	done = []
	folder = r'Z:\Scratch\TD\log'
	files = os.listdir(folder)
	fo = open(os.path.join(r'\\192.168.2.10\ftp$\ROMA', '201010-201102.txt'), "w")
	for filename in files:
		fi = open(os.path.join(folder, filename), "r")
		while True:
			line = fi.readline()
			if not line:
				break
			m = re.compile(r'^(copy|move) .*(\\\\file-cluster\\GDC\\Projects\\ROMA\\PRJ_roma\\(MC_roma|SHOT_roma)\\.*)$', re.IGNORECASE).search(line)
			if m == None:
				continue
			dest = re.compile(r'^(\\\\file-cluster\\GDC\\Projects\\ROMA\\PRJ_roma\\MC_roma\\scenes\\characters\\([^\\]+\\){3})((tmp\\)?[^\\]+)$', re.IGNORECASE).sub(r'\g<1>fixed\\\g<3>', m.group(2))
			line = fi.readline()
			if not line:
				break
			if re.compile(r'^Error:', re.IGNORECASE).search(line) != None:
				continue
			if dest in done:
				continue
			if not os.path.isfile(dest):
				continue
			done.append(dest)
			fo.write('%s\r\n' % (dest))
			m = re.compile(r'^(\\\\file-cluster\\GDC\\Projects\\ROMA\\PRJ_roma\\SHOT_roma\\sq_[0-9a-z]+\\roma_sq_[0-9a-z]+_sc_[0-9a-z]+\\).*$', re.IGNORECASE).search(dest)
			if m == None:
				continue
			dest = '%sworkspace.mel' % (m.group(1))
			if dest in done:
				continue
			done.append(dest)
			fo.write('%s\r\n' % (dest))
		fi.close()
	fo.close()

def ToggleFolTexture(selected = False, nosize = True):
	nodes = []
	if selected:
		nodes = maya.mel.eval('zwTextureNetwork')
	else:
		nodes = maya.cmds.ls(type = 'file')
	if nodes == None:
		return
	for node in nodes:
		source = maya.cmds.getAttr('%s.fileTextureName' % (node))
		dest = source
		if nosize:
			dest = re.compile(r'(/fol/)', re.IGNORECASE).sub(r'\g<1>nosize/', source)
		else:
			dest = re.compile(r'(/fol/)nosize/', re.IGNORECASE).sub(r'\g<1>', source)
		if dest == source:
			continue
		path = maya.cmds.workspace(expandName = dest)
		if not os.path.isfile(path):
			continue
		maya.OpenMaya.MGlobal.executeCommand(r'setAttr -type "string" "%s.fileTextureName" "%s"' % (node, dest), True)

def CreateVfxMotionVectorLayer():
	selection = maya.cmds.ls(selection = True)
	sceneName = maya.cmds.file(query=True, sceneName = True, shortName =True)
	m = re.compile(r'^vfx_([0-9a-z]+)_([0-9a-z]+)(_[0-9a-z]+)?', re.IGNORECASE).search(sceneName)
	if m == None:
		maya.OpenMaya.MGlobal.displayError(u'文件命名不规范')
		return
	sq = m.group(1)
	sc = m.group(2)
	char = 'vfx'
	if m.group(3) != None:
		if re.compile(r'^_(motion|Vector|mVector|RX)', re.IGNORECASE).search(m.group(3)) == None:
			char = 'vfx' + m.group(3)
	maya.mel.eval('source "zwCreatePassFile.mel"')
	maya.mel.eval('zwCreatePassFileSaveNode "%s" "%s" "%s" "motionVector"' % (sq, sc, char))
	if selection != None:
		if len(selection) > 0:
			maya.cmds.select(selection)
	autoSetForRendering()

def Connect_mmma_Material():
	selection = maya.cmds.ls(selection = True)
	if selection == None:
		maya.OpenMaya.MGlobal.displayError(u'请选择头发的Ribbox')
		return
	if len(selection) == 0:
		maya.OpenMaya.MGlobal.displayError(u'请选择头发的Ribbox')
		return
	if maya.cmds.nodeType(selection[0]) != 'transform':
		maya.OpenMaya.MGlobal.displayError(u'请选择头发的Ribbox')
		return
	selection = maya.cmds.listRelatives(selection[0], shapes = True)
	shadingEngine = maya.cmds.listConnections(selection[0], type = 'shadingEngine')
	if shadingEngine == None:
		maya.OpenMaya.MGlobal.displayError(u'头发的Ribbox没有材质')
		return
	if len(shadingEngine) == 0:
		maya.OpenMaya.MGlobal.displayError(u'头发的Ribbox没有材质')
		return

	pfxHair = maya.cmds.ls(type = 'pfxHair')
	if pfxHair == None:
		return
	if len(pfxHair) == 0:
		return
	pfxHair = maya.cmds.listRelatives(pfxHair[0], parent = True)
	if not maya.cmds.objExists('%s.MayaManAttsNode' % pfxHair[0]):
		return
	MayaManAttributes = maya.cmds.listConnections('%s.MayaManAttsNode' % pfxHair[0])
	if MayaManAttributes == None:
		return
	if len(MayaManAttributes) == 0:
		return

	if not maya.cmds.isConnected('%s.message' % (shadingEngine[0]), '%s.mmma_Material' % (MayaManAttributes[0])):
		maya.OpenMaya.MGlobal.executeCommand('connectAttr -force "%s.message" "%s.mmma_Material"' % (shadingEngine[0], MayaManAttributes[0]), True)

def List_mmma_Material():
	'''
	列出被柔化掉的mmma_Material
	'''
	find = False

	pfxHairs = maya.cmds.ls(type = 'pfxHair')
	if pfxHairs == None:
		return
	for pfxHair in pfxHairs:
		parent = maya.cmds.listRelatives(pfxHair, parent = True)
		if not maya.cmds.objExists('%s.MayaManAttsNode' % parent[0]):
			#continue
			find = True
			break
		MayaManAttributes = maya.cmds.listConnections('%s.MayaManAttsNode' % parent[0], type = 'MayaManAttributes')
		if MayaManAttributes == None:
			#continue
			find = True
			break
		if len(MayaManAttributes) == 0:
			#continue
			find = True
			break
		shadingEngines = maya.cmds.listConnections('%s.mmma_Material' % MayaManAttributes[0], type = 'shadingEngine')
		if shadingEngines == None:
			find = True
			break
		if len(shadingEngines) == 0:
			find = True
			break
		Ribbox = maya.cmds.sets(shadingEngines[0], query = True)
		if Ribbox == None:
			find = True
			break
		if len(Ribbox) == 0:
			find = True
			continue
	
	if find:
		sceneName = maya.cmds.file(query=True, sceneName = True)
		fo = open(r'\\file-cluster\GDC\Scratch\TD\mmma_Material.txt', "a")
		fo.write('%s\r\n' % (sceneName.replace('/', '\\')))
		fo.close()

def ListHRS():
	for root, dirs, files in os.walk(r'\\file-cluster\GDC\Projects\ROMA\PRJ_roma\MC_roma\scenes'):
		for HRS in files:
			if re.compile(r'_HRS\.m[ab]$', re.IGNORECASE).search(HRS) != None and re.compile(r'\\fixed$', re.IGNORECASE).search(root) != None:
				(title, ext) = os.path.splitext(HRS)
				#print r'"\\file-cluster\GDC\Resource\Support\Virtual Vertex\Muster5.54x32\Mrtool.exe" -b -s 192.168.3.185 -u skywalker -pool "Entire Farm" -e 99 -n %s -f %s\%s -proj \\file-cluster\GDC\Projects\ROMA\PRJ_roma\MC_roma -pr 100 -sf 1 -ef 1 -bf 1 -se 1 -st 1 -add "zwWinxCheckinFinishing" -info "user: huangzhongwei time: 2011/03/30 13:18:05"' % (title, root, HRS)
				print 'D:\\alias\\maya2008\\bin\\mayabatch.exe -command \"python \\\"import idmt.maya.roma\\nidmt.maya.roma.List_mmma_Material()\\\"" -file \"%s\\%s\"\r\n' % (root, HRS)

def ListHRS1():
	for root, dirs, files in os.walk(r'\\file-cluster\GDC\Projects\ROMA\PRJ_roma\MC_roma\scenes'):
		if re.compile(r'\\tmp$', re.IGNORECASE).search(root) == None and ((re.compile(r'\\scenes\\characters\\', re.IGNORECASE).search(root) != None and re.compile(r'\\fixed$', re.IGNORECASE).search(root) != None) or (re.compile(r'\\scenes\\props\\', re.IGNORECASE).search(root) != None)):
			for HRS in files:
				if re.compile(r'_(HRS|RND)\.m[ab]$', re.IGNORECASE).search(HRS) != None:
					print 'D:\\alias\\maya2008\\bin\\mayabatch.exe -command \"zwTempCheckShave\" -file \"%s\\%s\"' % (root, HRS)


def RecreateContent():
	size = 0

	fo = open(r'\\192.168.2.10\ftp$\ROMA\MC_roma_scenes_20110408.txt', "a")

	scenes = r'\\file-cluster\GDC\Projects\ROMA\PRJ_roma\MC_roma\scenes'
	genres = ('characters', 'environments', 'props', 'sets')
	for genre in genres:
		path = os.path.join(scenes, genre)
		if not os.path.isdir(path):
			continue
		groups = os.listdir(path)
		for group in groups:
			path = os.path.join(scenes, genre, group)
			if not os.path.isdir(path):
				continue
			names = os.listdir(path)
			for name in names:
				path = os.path.join(scenes, genre, group, name)
				if not os.path.isdir(path):
					continue
				types = os.listdir(path)
				for type in types:
					path = os.path.join(scenes, genre, group, name, type)
					if not os.path.isdir(path):
						continue
					types = os.listdir(path)
					path = os.path.join(scenes, genre, group, name, type)
					if not os.path.isdir(path):
						continue
					modes = os.listdir(path)
					for mode in modes:
						path = os.path.join(scenes, genre, group, name, type, mode)
						if re.compile(r'\.(mb|xml)$', re.IGNORECASE).search(mode) != None:
							if genre != 'characters':
								statinfo = os.stat(path)
								size = size + statinfo.st_size
								#print path
								fo.write('%s\r\n' % path)
								path = RecreateContentGetTmp(path)
								if path != "":
									statinfo = os.stat(path)
									size = size + statinfo.st_size
									#print path
									fo.write('%s\r\n' % path)
							continue
						if not os.path.isdir(path):
							continue
						if mode == 'setup':
							for root, dirs, files in os.walk(path):
								if re.compile(r'\\sourceimages$', re.IGNORECASE).search(root) == None:
									continue
								for rib in files:
									rib = os.path.join(root, rib)
									statinfo = os.stat(rib)
									size = size + statinfo.st_size
									#print rib
									fo.write('%s\r\n' % rib)
							continue
						if not mode in ('fixed', 'foliage', 'modeling', 'set'):
							continue
						filenames = os.listdir(path)
						for filename in filenames:
							path = os.path.join(scenes, genre, group, name, type, mode, filename)
							if mode == 'foliage' and filename == 'ribs':
								for root, dirs, files in os.walk(path):
									for rib in files:
										rib = os.path.join(root, rib)
										statinfo = os.stat(rib)
										size = size + statinfo.st_size
										#print rib
										fo.write('%s\r\n' % rib)
								continue
							if re.compile(r'\.(mb|xml)$', re.IGNORECASE).search(filename) == None:
								continue
							statinfo = os.stat(path)
							size = size + statinfo.st_size
							#print path
							fo.write('%s\r\n' % path)
							path = RecreateContentGetTmp(path)
							if path != "":
								statinfo = os.stat(path)
								size = size + statinfo.st_size
								#print path
								fo.write('%s\r\n' % path)
						
	print (r'SIZE: %d' % (size))
	fo.close()

def RecreateContentGetTmp(path):
	filename = os.path.basename(path)
	if re.compile(r'\.xml$', re.IGNORECASE).search(filename) != None:
		return ""
	tmpFolder = os.path.join(os.path.dirname(path), 'tmp')
	if not os.path.isdir(tmpFolder):
		return ""
	tmpFilenames = os.listdir(tmpFolder)
	old = []
	for tmpFilename in tmpFilenames:
		s = re.sub(r'^\d{4}\.\d{2}\.\d{2}-\d{2}\.\d{2}\.\d{2}@', '', tmpFilename)
		if not (s != tmpFilename and s == filename):
			continue
		old.append(tmpFilename)
	if len(old) > 0:
		old.sort()
		return os.path.join(tmpFolder, old[len(old)-1])
	return ""

def MayaManRenderShadowMapPath():
	path = ''

	if maya.cmds.pluginInfo('MayaMan', query = True, loaded = True):
		#path = os.path.join(maya.mel.eval('zwGetMusterProject ""'), re.sub('.*/(mayaman/.*)$', '\g<1>', maya.cmds.MayaManInfo(expandvariables = '$(RIBDIR)/shadow_maps/$(TXSUBDIR)')))
		path = os.path.join(maya.mel.eval('zwGetMusterProject ""'), maya.cmds.MayaManInfo(expandvariables = 'mayaman/$(SCENENAME)/shadow_maps/prman'))
		path = path.replace('\\', '/')

	return path

def MayaManRenderShadowMap():
	transform = maya.cmds.ls(sl = True)
	if idmt.maya.cmds.len(transform) != 1:
		maya.cmds.confirmDialog(title = 'MayaMan Render ShadowMap', message = 'This feature requires that a single light is selected')
		return
	#shapes = maya.cmds.listRelatives(transform[0], shapes = True)
	#if idmt.maya.cmds.len(shapes) == 0:
	#	maya.cmds.confirmDialog(title = 'MayaMan Render ShadowMap', message = 'This feature requires that a single light is selected')
	#	return

	#if maya.cmds.window('mayaManRenderShadowMapWindow', exists = True):
	#	maya.cmds.deleteUI('mayaManRenderShadowMapWindow')

	maya.mel.eval('MayaManRenderShadowMap')

	path = MayaManRenderShadowMapPath()
	if not os.path.isdir(path):
		os.makedirs(path)

	currentTime = maya.cmds.currentTime(query = True)

	maya.cmds.textField('mayaManRenderShadowMapWindow|mainCL|shadowMapDirectoryRL|shadowMapDirectoryTX', edit = True, text = path)
	maya.cmds.textField('mayaManRenderShadowMapWindow|mainCL|shadowMapNameRL|shadowMapNameTX', edit = True, text = transform[0])
	maya.cmds.checkBox('mayaManRenderShadowMapWindow|mainCL|checkBoxesCL|useFullPathsCB', edit = True, value = True)
	maya.cmds.intField('mayaManRenderShadowMapWindow|mainCL|frameRangeRL|start', edit = True, value = currentTime)
        maya.cmds.intField('mayaManRenderShadowMapWindow|mainCL|frameRangeRL|end', edit = True, value = currentTime)

	maya.mel.eval('MayaManOnRenderShadowMap')

def HairRiF():
	rs = maya.cmds.confirmDialog(title = u'添加RiFilters: HairRiF', message= u'只有猫头鹰和小鸟才需要点这个，你确定吗？', button = [u'确定', u'取消'])
	if rs == u'确定':
		AddRiFilter('HairRiF.dll', '-n')

def ListAssets():
	scenes = r'\\file-cluster\GDC\Projects\ROMA\PRJ_roma\MC_roma\scenes'
	genres = ('characters', 'environments', 'props', 'sets')
	for genre in genres:
		path = os.path.join(scenes, genre)
		if not os.path.isdir(path):
			continue
		groups = os.listdir(path)
		for group in groups:
			path = os.path.join(scenes, genre, group)
			if not os.path.isdir(path):
				continue
			names = os.listdir(path)
			for name in names:
				path = os.path.join(scenes, genre, group, name)
				if not os.path.isdir(path):
					continue
				types = os.listdir(path)
				for type in types:
					if genre == 'characters':
						path = os.path.join(scenes, genre, group, name, type, 'fixed')
					elif genre == 'sets':
						path = os.path.join(scenes, genre, group, name, type, 'set')
					else:
						path = os.path.join(scenes, genre, group, name, type)
					if not os.path.isdir(path):
						continue
					filenames = os.listdir(path)
					for filename in filenames:
						if re.compile(r'\.m[ab]$', re.IGNORECASE).search(filename) != None:
							print '${MC_roma}/scenes/%s/%s/%s/%s' % (genre, group, name, type)
							break

def contactOccOn():
	sceneName = maya.cmds.file(query=True, sceneName = True, shortName = True)
	if re.compile(r'_ptc_', re.IGNORECASE).search(sceneName) == None:
		maya.OpenMaya.MGlobal.displayError(u'只有 ptc 文件才能使用本按钮')
		return
	old = maya.cmds.getAttr('MayaManNugget.UserRibOptions')
	UserRibOptions = old
	if re.compile(r'Attribute \"user\" \"float contactOcc\" \[\d\]').search(old) != None:
		UserRibOptions = re.compile(r'Attribute \"user\" \"float contactOcc\" \[\d\]').sub('Attribute "user" "float contactOcc" [1]', old)
	else:
		UserRibOptions = old + '\n\nAttribute "user" "float contactOcc" [1] # CONTACT OCCLUSION ON/OFF SWITCH'
	if UserRibOptions != old:
		maya.cmds.setAttr('MayaManNugget.UserRibOptions', UserRibOptions, type = 'string')

class StereoCamSolve(object):
	def __init__(self):
		if maya.cmds.window('StereoCamSolve', exists = True):
			maya.cmds.deleteUI('StereoCamSolve')
		maya.cmds.window('StereoCamSolve', t = u'修改摄像机', resizeToFitChildren  = True)
		maya.cmds.columnLayout(adjustableColumn = True, rowSpacing = 4)
		self.textFieldGrp1 = maya.cmds.textFieldGrp(label  = 'SQ')
		self.textFieldGrp2 = maya.cmds.textFieldGrp(label  = 'SC')
		maya.cmds.scrollField(editable = False, wordWrap = True, text  = u'选择一个摄像机。将会导入左、右眼摄像机，修改它们的动画使跟选择的摄像机一致，导出修改好的摄像机的本机工程目录')
		maya.cmds.button(label = 'OK', command = partial(self.OnBnClickedButtonOK))
		maya.cmds.showWindow('StereoCamSolve')

	def OnBnClickedButtonOK(self, xxx):
		cameraLeft = 'original_camera'
		sl = maya.cmds.ls(cameraLeft)
		if len(sl) != 0:
			maya.OpenMaya.MGlobal.displayError(u'场景中不能有名为 original_camera 的摄像机')
			return
		cameraRight = 'camera_stereoRx'
		sl = maya.cmds.ls(cameraRight)
		if len(sl) != 0:
			maya.OpenMaya.MGlobal.displayError(u'场景中不能有名为 camera_stereoRx 的摄像机')
			return

		sl = maya.cmds.ls(sl = True)
		if len(sl) != 1:
			maya.OpenMaya.MGlobal.displayError(u'请选择一个摄像机')
			return
		camera = sl[0]

		lefts = []
		rights = []
		sq = maya.cmds.textFieldGrp(self.textFieldGrp1, query = True, text = True)
		sc = maya.cmds.textFieldGrp(self.textFieldGrp2, query = True, text = True)
		folder = r'\\file-cluster\GDC\Projects\ROMA\PRJ_roma\SHOT_roma\stereo_cams_approved\seq_%s\sc_%s' % (sq, sc)
		if os.path.isdir(folder):
			filenames = os.listdir(folder)
			for filename in filenames:
				if re.compile(r'_Lx[\._].*m[ab]$', re.IGNORECASE).search(filename) != None:
					lefts.append(filename)
				elif re.compile(r'_Rx[\._].*m[ab]$', re.IGNORECASE).search(filename) != None:
					rights.append(filename)
		if len(lefts) == 0:
			maya.OpenMaya.MGlobal.displayError(u'找不到左眼摄像机文件')
			return
		if len(rights) == 0:
			maya.OpenMaya.MGlobal.displayError(u'找不到右眼摄像机文件')
			return
		
		left = ''
		right = ''
		if len(lefts) == 1:
			left = lefts[0]
		else:
			left = maya.cmds.confirmDialog(t = u'修改摄像机', message = u'多于一个左眼摄像机文件，请选择：', button = lefts, dismissString = '')
			if left == '':
				return
		if len(rights) == 1:
			right = rights[0]
		else:
			right = maya.cmds.confirmDialog(t = u'修改摄像机', message = u'多于一个右眼摄像机文件，请选择：', button = rights, dismissString = '')
			if right == '':
				return

		first = maya.cmds.findKeyframe(camera, which = 'first')
		last = maya.cmds.findKeyframe(camera, which = 'last')
		maya.cmds.playbackOptions(minTime = first, maxTime = last)
		maya.cmds.currentTime(1)

		path = os.path.join(folder, left)
		maya.cmds.file(path, i = True)

		path = os.path.join(folder, right)
		maya.cmds.file(path, i = True)

		attrs = ('rotateX', 'rotateY', 'rotateZ', 'scaleX', 'scaleY', 'scaleZ', 'translateX', 'translateY', 'translateZ')

		for attr in attrs:
			maya.cmds.setAttr('%s.%s' % (cameraLeft, attr), lock = False)
		animCurves = maya.cmds.listConnections(cameraLeft, t = 'animCurve')
		for animCurve in animCurves:
			maya.cmds.delete(animCurve)

		for attr in attrs:
			maya.cmds.setAttr('%s.%s' % (cameraRight, attr), lock = False)
		animCurves = maya.cmds.listConnections(cameraRight, t = 'animCurve')
		for animCurve in animCurves:
			maya.cmds.delete(animCurve)

		maya.cmds.parent(cameraRight, cameraLeft)
		maya.cmds.parentConstraint(camera, cameraLeft)
		
		maya.cmds.select(cameraRight)
		maya.mel.eval('source zwCameraImportExport.mel; zwBakeCamera;')
		maya.cmds.delete(cameraRight)
		maya.cmds.rename(cameraRight + '_baked', cameraRight)
		path = '%s/scenes/%s' % (maya.cmds.workspace(query = True, rootDirectory = True), right)
		maya.cmds.file(path, exportSelected = True, typ ='mayaBinary')
		maya.cmds.delete(cameraRight)
		
		maya.cmds.select(cameraLeft)
		maya.mel.eval('source zwCameraImportExport.mel; zwBakeCamera;')
		maya.cmds.delete(cameraLeft)
		maya.cmds.rename(cameraLeft + '_baked', cameraLeft)
		path = '%s/scenes/%s' % (maya.cmds.workspace(query = True, rootDirectory = True), left)
		maya.cmds.file(path, exportSelected = True, typ ='mayaBinary')
		maya.cmds.delete(cameraLeft)

def MayaManTexture(muster = False, computername = None):
	if muster:
		if os.getenv('USERNAME').lower() != 'musterservice':
			return
	
	s = 0
	f = 0

	nodes = maya.cmds.ls(typ = 'file')

	if not maya.cmds.about(batch = True):
		maya.cmds.progressWindow(maxValue = len(nodes)+1, t = '设置贴图的MayaManTexture 属性', isInterruptable = True)

	for i in range(len(nodes)):
		node = nodes[i]

		if not maya.cmds.about(batch = True):
			if maya.cmds.progressWindow(query = True, isCancelled = True):
				maya.cmds.progressWindow(endProgress = True)
				break
			maya.cmds.progressWindow(edit = True, progress = i + 1, status = str(i + 1) + '/' + str(len(nodes)) + '    ' + nodes[i])

		if not maya.cmds.objExists(node + '.MayaManTexture'):
			maya.OpenMaya.MGlobal.displayWarning(u'MayaManTexture 属性不存在：%s' % node)
			f = f + 1
			continue

		texMirrow = idmt.maya.customIDMTSetup.setRenderTex(computername)
		texMirrow = texMirrow.replace('\\', '/')

		path = maya.cmds.getAttr(r'%s.fileTextureName' % (node))
		path = idmt.maya.path.GetFullPath(path)
		path = re.sub(r'^//', texMirrow + '/', path)
		path1 = re.sub(r'[^/\\]+$', r'prman/\g<0>.tif.pX.pY.mU.tex', path)
		path2 = re.sub(r'[^/\\]+$', r'prman/\g<0>.tif.mU.tex', path)
		
		if os.path.isfile(path1):
			path = path1
		elif os.path.isfile(path2):
			path = path2
		else:
			idmt.maya.cmds.setAttr(node + '.MayaManTexture', '')
			maya.OpenMaya.MGlobal.displayWarning(u'文件不存在：%s\n%s' % (node, path1))
			f = f + 1
			continue

		#lock = path + '.lock'
		#if os.path.isfile(lock):
		#	idmt.maya.cmds.setAttr(node + '.MayaManTexture', '')
		#	maya.OpenMaya.MGlobal.displayWarning(u'文件lock：%s\n%s' % (node, lock))
		#	f = f + 1
		#	continue
		
		idmt.maya.cmds.setAttr(node + '.MayaManTexture', path)
		s = s + 1
	
	if not maya.cmds.about(batch = True):
		maya.cmds.progressWindow(endProgress = True)
		if f > 0:
			maya.cmds.confirmDialog(t = u'设置贴图的MayaManTexture 属性', button = 'OK', message = u'%d 成功，%d 失败\n\n详情请查看Script Editor' %(s, f))
			maya.mel.eval('ScriptEditor')
