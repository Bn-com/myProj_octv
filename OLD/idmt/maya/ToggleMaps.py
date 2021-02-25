# -*- coding: utf-8 -*-
# Copyright (C) 2000-2010 IDMT. All rights reserved.
'''
Toggle Maps
'''
__author__	= 'huangzhongwei@idmt.com.cn'
__date__	= '2011-10-09'

from functools import partial
import maya.cmds
import maya.OpenMaya
import os
import re

class ToggleMaps(object):
	def __init__(self):
		self.resize = True
		apiVersion = maya.cmds.about(apiVersion = True)
		if apiVersion / 100 == 2011 and maya.cmds.about(is64 = True):
			self.resize = False
			#message = u'Toggle Maps: Maya 2011 x64运行本程序具有崩溃的风险。建议在32位版本Maya运行'
			message = u'Toggle Maps: Maya 2011 x64只能切换到已有的低分辨率贴图，如需生成低分辨率贴图，请在32位版本Maya运行'
			if maya.cmds.about(batch = True):
				maya.OpenMaya.MGlobal.displayWarning(message)
			else:
				maya.cmds.confirmDialog(button = 'OK', icon = 'warning', message = message)

	def showWindow(self):
		if maya.cmds.window('ToggleMaps', exists = True):
			maya.cmds.deleteUI('ToggleMaps')
		maya.cmds.window('ToggleMaps', t = u'Toggle Maps', resizeToFitChildren  = True)
		maya.cmds.columnLayout(adjustableColumn = True, rowSpacing = 2)
		maya.cmds.button(width = 160, height = 24, label = u'原始尺寸', command = partial(self.ToggleMaps, 0, ''))
		maya.cmds.button(width = 160, height = 24, label = '2048', command = partial(self.ToggleMaps, 2048, '2k'))
		maya.cmds.button(width = 160, height = 24, label = '1024', command = partial(self.ToggleMaps, 1024, '1k'))
		maya.cmds.button(width = 160, height = 24, label = '512', command = partial(self.ToggleMaps, 512, 'hk'))
		maya.cmds.button(width = 160, height = 24, label = '256', command = partial(self.ToggleMaps, 256, 'qk'))
		maya.cmds.showWindow('ToggleMaps')

	def ToggleMaps(self, wh, postfix, xxx):
		files = maya.cmds.ls(typ = 'file')
		if files == None:
			return

		if not maya.cmds.about(batch = True) and len(files) > 0:
			maya.cmds.progressWindow(maxValue = len(files), t = 'Toggle Maps', isInterruptable = True)

		for i in range(len(files)):
			if not maya.cmds.about(batch = True):
				if maya.cmds.progressWindow(query = True, isCancelled = True):
					break
				maya.cmds.progressWindow(edit = True, progress = i + 1, status = '%d/%d    %s' % (i + 1, len(files), files[i]))

			if not maya.cmds.objExists(files[i]):
				continue
			source = maya.cmds.getAttr(files[i] + '.fileTextureName')
			if source == '':
				continue
			pathS = maya.cmds.workspace(expandName = source)
			folder =  re.sub('/[^/]+$', '', pathS)
			if not maya.cmds.objExists(files[i] + '.originalTexture'):
				continue
			filenameO = maya.cmds.getAttr(files[i] + '.originalTexture')
			original = re.sub('[^/]+$', filenameO, source)
			pathO = maya.cmds.workspace(expandName = original)
			if not os.path.isfile(pathO):
				continue

			dest = ''
			if wh == 0:
				dest = original
			else:
				whO = maya.cmds.idmtImage(pathO, size = True)
				if whO[0] <= wh or whO[1] <= wh:
					dest = original
				else:
					useFrameExtension = maya.cmds.getAttr(files[i] + '.useFrameExtension')
					if useFrameExtension:
						pattern1 = ''
						pattern2 = ''
						if re.search(r'^([^\.]+)\.\d+\.([^.]+)$', filenameO) != None:
							pattern1 = re.sub(r'^([^\.]+)\.\d+\.([^.]+)$', r'^\g<1>\.\d+\.\g<2>$', filenameO)
							pattern2 = r'(_[1-8hq]k)?(\..*)'
						elif re.search(r'^([^\.]+)_\d+\.([^.]+)$', filenameO) != None:
							pattern1 = re.sub(r'^([^\.]+)_\d+\.([^.]+)$', r'^\g<1>_\d+\.\g<2>$', filenameO)
							pattern2 = r'(_[1-8hq]k)?(_\d+\..*)'
						else:
							continue
						filenameD = re.sub(pattern2, r'_%s\g<2>' % postfix, filenameO)
						dest = re.sub('[^/]+$', filenameD, source)
						if dest != original:
							filenameEs = os.listdir(folder)
							for filenameE in filenameEs:
								if not maya.cmds.about(batch = True):
									if maya.cmds.progressWindow(query = True, isCancelled = True):
										break

								if re.search(pattern1, filenameE) == None:
									continue
								pathEO = folder + '/' + filenameE
								filenameE = re.sub(pattern2, r'_%s\g<2>' % postfix, filenameE)
								pathED = folder + '/' + filenameE
								if not self.Exists(pathEO, pathED):
									if self.resize:
										maya.cmds.idmtImage(pathEO, pathED, resize = [wh, wh])
							if not maya.cmds.about(batch = True):
								if maya.cmds.progressWindow(query = True, isCancelled = True):
									break
					else:
						filenameD = re.sub(r'(_[1-8hq]k)?(\..*|$)', r'_%s\g<2>' % postfix, filenameO)
						dest = re.sub('[^/]+$', filenameD, source)
						if dest != original:
							pathD = maya.cmds.workspace(expandName = dest)
							if not self.Exists(pathO, pathD):
								if self.resize:
									maya.cmds.idmtImage(pathO, pathD, resize = [wh, wh])

			if source != dest:
				pathD = maya.cmds.workspace(expandName = dest)
				if self.Exists(pathO, pathD):
					maya.OpenMaya.MGlobal.executeCommand('setAttr \"%s.fileTextureName\" -type \"string\" \"%s\"' % (files[i], dest), True)

		if not maya.cmds.about(batch = True) and len(files) > 0:
			maya.cmds.progressWindow(endProgress = True)
	
	def Exists(self, source, dest):
		rs = False

		if os.path.isfile(source) and os.path.isfile(dest):
			rs = maya.cmds.idmtFile(source, dest, compareModified = True)

		return rs