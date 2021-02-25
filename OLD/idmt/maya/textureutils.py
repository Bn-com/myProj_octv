# -*- coding: utf-8 -*-
# Copyright (C) 2000-2010 IDMT. All rights reserved.
'''
Texture Utilities:
1)display the textures' informations: path, resolution, size
2)collect all texture to a folder, convert to iff, zoom to half
'''
__author__	= 'huangzhongwei@idmt.com.cn'
__date__	= '2010-07-28'

import maya.cmds as cmds
import maya.mel as mel
import os
import re
import tempfile

def ui(applyTo = None, findStr = None, replaceStr = None):
	'''main myuis'''
	def run(cmd):
		return lambda x : cmds.python('try:\n\treload(' + __name__ + ')\nexcept:\n\timport ' + __name__ + '\n' + __name__ + '.' + cmd)

	if cmds.window('textureutils', exists = True):
		cmds.deleteUI('textureutils')

	setOptionVars()

	if findStr == None:
		findStr = cmds.optionVar(query = 'textureutilsFind')
	if replaceStr == None:
		replaceStr = cmds.optionVar(query = 'textureutilsReplace')

	window1 = cmds.window('textureutils', menuBar = True, title = 'Texture Utilities', width = 500, height = 200)
	cmds.menu(label = 'Help')
	#cmds.menuItem(label = 'Help on Texture Utilities...', command = 'zjHelpCallback zwTextureCollector')
	formLayout1 = cmds.formLayout()
	columnLayout1 = cmds.columnLayout(adjustableColumn = True)
	radioButtonGrp1 = cmds.radioButtonGrp('radioButtonGrpApplyToAll', adjustableColumn = 2, label = 'Apply to:', label1 = 'All Textures')
	cmds.radioButtonGrp('radioButtonGrpApplyToSelected', shareCollection = radioButtonGrp1, adjustableColumn = 2, label = '', label1 = 'Selected Objects Only')
	cmds.setParent('..')
	tabLayout1 = cmds.tabLayout(tabsVisible = False, scrollable = True, childResizable = True)
	cmds.columnLayout(adjustableColumn = True)
	cmds.frameLayout(visible = False, label = 'Information', borderStyle = 'etchedIn', collapsable = True)
	cmds.columnLayout(adjustableColumn = True, rowSpacing = 2)
	radioButtonGrp1 = cmds.radioButtonGrp('radioButtonGrpBrief', adjustableColumn = 2, label = 'Informations:', label1 = 'Brief')
	cmds.radioButtonGrp('radioButtonGrpDetails', shareCollection = radioButtonGrp1, adjustableColumn = 2, label = '', label1 = 'Details')
	cmds.button(label = 'Show', command = run('OnBnClickedShow()'))
	cmds.setParent('..')
	cmds.setParent('..')
	cmds.frameLayout(visible = False, label = 'Collector', borderStyle = 'etchedIn', collapsable = True)
	cmds.columnLayout(adjustableColumn = True, rowSpacing = 2)
	cmds.checkBoxGrp(adjustableColumn = 2, label = 'Options:', label1 = 'Refer to new file')
	cmds.checkBoxGrp(adjustableColumn = 2, label = '', label1 = 'Convert to iff')
	cmds.checkBoxGrp(adjustableColumn = 2, label = '', label1 = 'Zoom 1/2')
	cmds.checkBoxGrp(adjustableColumn = 2, label = '', label1 = '4k -> 2k')
	cmds.separator()
	cmds.checkBoxGrp(adjustableColumn = 2, label = '', label1 = 'Save New Files in')
	cmds.textFieldButtonGrp(label = '', buttonLabel = 'Browse', adjustableColumn = 2)
	cmds.button(label = 'Collect')
	cmds.setParent('..')
	cmds.setParent('..')
	cmds.frameLayout(label = 'Replace', borderStyle = 'etchedIn', collapsable = True)
	cmds.columnLayout(adjustableColumn = True, rowSpacing = 2)
	cmds.textFieldGrp('textFieldGrpFind', label = 'Find:', adjustableColumn = 2, text = findStr)
	cmds.textFieldGrp('textFieldGrpReplace', label = 'Replace:', adjustableColumn = 2, text = replaceStr)
	cmds.button(label = 'Replace', command = run('OnBnClickedReplace()'))
	cmds.setParent('..')
	cmds.setParent('..')
	cmds.formLayout(formLayout1, edit = True, attachForm = ((columnLayout1, 'left', 0), (columnLayout1, 'top', 0), (columnLayout1, 'right', 0), (tabLayout1, 'left', 0), (tabLayout1, 'right', 0), (tabLayout1, 'bottom', 0)), attachControl = ((tabLayout1, 'top', 0, columnLayout1)))

	if applyTo == None:
		applyTo = cmds.optionVar(query = 'textureutilsApplyTo')
	if applyTo == 0:
		cmds.radioButtonGrp('radioButtonGrpApplyToAll', edit = True, select = 1)
	elif applyTo == 1:
		cmds.radioButtonGrp('radioButtonGrpApplyToSelected', edit = True, select = 1)

	textureutilsShow = cmds.optionVar(query = 'textureutilsShow')
	if textureutilsShow == 0:
		cmds.radioButtonGrp('radioButtonGrpBrief', edit = True, select = 1)
	elif textureutilsShow == 1:
		cmds.radioButtonGrp('radioButtonGrpDetails', edit = True, select = 1)

	cmds.showWindow(window1)

def setOptionVars(forceFactorySettings = False):
	'''Set optionVar'''
	if forceFactorySettings or not cmds.optionVar(exists = 'textureutilsApplyTo'):
		cmds.optionVar(intValue = ('textureutilsApplyTo', 0))
	if forceFactorySettings or not cmds.optionVar(exists = 'textureutilsShow'):
		cmds.optionVar(intValue = ('textureutilsShow', 0))
	if forceFactorySettings or not cmds.optionVar(exists = 'textureutilsFind'):
		cmds.optionVar(stringValue = ('textureutilsFind', ''))
	if forceFactorySettings or not cmds.optionVar(exists = 'textureutilsReplace'):
		cmds.optionVar(stringValue = ('textureutilsReplace', ''))

def callback():
	'''Update data'''
	textureutilsApplyTo = 0
	if cmds.radioButtonGrp('radioButtonGrpApplyToAll', query = True, select = True) == 1:
		textureutilsApplyTo = 0
	elif cmds.radioButtonGrp('radioButtonGrpApplyToSelected', query = True, select = True) == 1:
		textureutilsApplyTo = 1
	cmds.optionVar(intValue = ('textureutilsApplyTo', textureutilsApplyTo))

	textureutilsShow = 0
	if cmds.radioButtonGrp('radioButtonGrpBrief', query = True, select = True) == 1:
		textureutilsShow = 0
	elif cmds.radioButtonGrp('radioButtonGrpDetails', query = True, select = True) == 1:
		textureutilsShow = 1
	cmds.optionVar(intValue = ('textureutilsShow', textureutilsShow))

	textureutilsFind = cmds.textFieldGrp('textFieldGrpFind', query = True, text = True)
	cmds.optionVar(stringValue = ('textureutilsFind', textureutilsFind))
	textureutilsReplace = cmds.textFieldGrp('textFieldGrpReplace', query = True, text = True)
	cmds.optionVar(stringValue = ('textureutilsReplace', textureutilsReplace))


def OnBnClickedShow():
	'''On "Show" infomation button clicked'''
	callback()
	performInfomation()

def OnBnClickedReplace():
	'''On "Replace" button clicked'''
	callback()
	performReplace()

def performInfomation():
	'''Display the textures' informations'''
	textureutilsApplyTo = cmds.optionVar(query = 'textureutilsApplyTo')
	textureutilsShow = cmds.optionVar(query = 'textureutilsShow')
	nodes = []
	if textureutilsApplyTo == 0:
		nodes = cmds.ls(type = 'file')
	elif textureutilsApplyTo == 1:
		nodes = cmds.python('zwTextureNetwork')
	if nodes == None:
		nodes = []
	
	cmds.progressWindow(max = len(nodes)+1, title = 'Texture Infomation', isInterruptable = True)
	
	xml = cmds.file(query = True, sceneName = True, shortName = True)
	#(xml, ext) = os.path.splitext(xml)
	if xml == '':
		xml = __name__;
	xml = os.path.join(tempfile.gettempdir(), xml + '.xml')
	xmlFile = open(xml, 'w')
	xmlFile.writelines('<?xml version="1.0" ?>')
	xmlFile.writelines('<?xml-stylesheet type="text/xsl" href="http://app-server/ws/Support/Working/myuis/textureutils.xsl" ?>')
	xmlFile.writelines('<root>')
	for i in range(len(nodes)):
		if cmds.progressWindow(query = True, isCancelled = True):
			cmds.progressWindow(endProgress = True)
			break
		cmds.progressWindow(edit = True, progress = i + 1, status = str(i + 1) + '/' + str(len(nodes)) + '    ' + nodes[i])

		fileTextureName = cmds.getAttr(nodes[i] + '.fileTextureName')
		(dir, filename) = os.path.split(fileTextureName)
		path = cmds.workspace(expandName = fileTextureName)
		exists = os.path.exists(path)
		size = 0
		resolutuon = [0, 0]
		if exists:
			size = cmds.idmtFile(path, size = True)
			resolutuon = cmds.idmtImage(path, size = True)

		xmlFile.writelines('\t<node>')
		xmlFile.writelines('\t\t<name>' + nodes[i] + '</name>')
		xmlFile.writelines('\t\t<texture>' + fileTextureName + '</texture>')
		xmlFile.writelines('\t\t<filename>' + filename + '</filename>')
		xmlFile.writelines('\t\t<path>' + path + '</path>')
		xmlFile.writelines('\t\t<exists>' + str(exists) + '</exists>')
		xmlFile.writelines('\t\t<size>' + str(size) + '</size>')
		xmlFile.writelines('\t\t<resolutuon>' + str(resolutuon[0]) + ' x ' + str(resolutuon[1]) + '</resolutuon>')
		xmlFile.writelines('\t</node>')
	xmlFile.write('</root>')
	xmlFile.flush()
	xmlFile.close()

	cmds.progressWindow(endProgress = True)

	mel.eval('global int $textureutilsDlg;\r\nidmtDHtmlDlg -destroyWindow $textureutilsDlg;\r\n$textureutilsDlg = `idmtDHtmlDlg -host "%s"`' % re.sub(r'\\', r'/', xml))

def performReplace():
	'''Replace the textures' path'''
	textureutilsApplyTo = cmds.optionVar(query = 'textureutilsApplyTo')
	textureutilsFind = cmds.optionVar(query = 'textureutilsFind')
	textureutilsReplace = cmds.optionVar(query = 'textureutilsReplace')
	cmd = 'source kcModifyMapPathGUI.mel; kcModifyMapPath "%s" "%s" %d;' % (re.sub(r'\\', r'\\\\', textureutilsFind), re.sub(r'\\', r'\\\\', textureutilsReplace), textureutilsApplyTo + 1)
	mel.eval(cmd)
