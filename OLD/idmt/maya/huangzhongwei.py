# -*- coding: utf-8 -*-
# Copyright (C) 2000-2011 IDMT. All rights reserved.
__author__	= 'huangzhongwei@idmt.com.cn'
__date__	= '2011-11-02'

import maya.cmds
import maya.mel
import maya.OpenMaya
import os
import re

import pyUtil3 as pyUtil

def bkCreateExportObject():
	'''
	Zorro -> Bakery属性
	'''
	sceneName = maya.cmds.file(query = True, sceneName = True, shortName = True)

	sceneName = re.sub('\.mb$', '.ma', sceneName)
	path = maya.cmds.idmtService('GetAssetPath', sceneName)
	m = re.search(r'\\scenes\\(.*)(\\[^\\]+){2}$', path)
	BkAsset = ''
	if m != None:
		BkAsset = m.group(1)
		BkAsset = BkAsset.replace('\\', '/')
	else:
		maya.OpenMaya.MGlobal.displayError(u'不能根据文件名判断路径')
		return
	
	#m = re.search(r'^[^_]{2}_([^_]+)(_[^_]+)?_[^_]_([^_]{2}|final)[_\.]', sceneName)
	#BkAsset = ''
	#if m != None:
	#	BkAsset = m.group(1)
	#else:
	#	maya.OpenMaya.MGlobal.displayError(u'不能根据文件名判断路径')
	#	return

	version = maya.cmds.about(version = True)
	#plugin1 = re.sub(r'.*(\d{4}).*', r'maya_mud_export_\g<1>', version)
	#plugin = 'maya_mud_export'
	#if not (maya.cmds.pluginInfo(plugin1, query = True, loaded = True) or maya.cmds.pluginInfo(plugin, query = True, loaded = True)):
	#	maya.cmds.loadPlugin(plugin)

	plugin = re.sub(r'.*(\d{4}).*', r'maya_mud_export_\g<1>', version)
	if not maya.cmds.pluginInfo(plugin, query = True, loaded = True):
		maya.cmds.loadPlugin(plugin)

	minTime = maya.cmds.playbackOptions(query = True, minTime = True)
	if minTime != 1.0:
		maya.cmds.playbackOptions(min = 1.0)
	maxTime = maya.cmds.playbackOptions(query = True, maxTime = True)
	if maxTime != 24.0:
		maya.cmds.playbackOptions(max = 24.0)

	#maya.cmds.select('CHR')
	buf = maya.cmds.ls(sl = True)
	CHR = buf[0]
	maya.mel.eval('bkAddBkAssetAttribute')
	maya.cmds.setAttr(CHR + '.BkAsset', BkAsset, typ = 'string')
	maya.mel.eval('bkCreateExportObject')
	buf = maya.cmds.ls(sl = True)
	Bakery_export = buf[0]
	maya.cmds.setAttr(Bakery_export + '.All_Shot_Asset', 1)
	#maya.cmds.setAttr(Bakery_export + '.Asset_Name_List', 'master', typ = 'string')
	#path = maya.cmds.file(query = True, sceneName = True)
	#path = re.sub('/[^/]+/[^/]+$', '', path)
	path = "//file-cluster/GDC/Projects/Zorro/Project/relight"
	#maya.cmds.setAttr(Bakery_export + '.Assets_Export_Directory', path, typ = 'string')
	#maya.cmds.setAttr(Bakery_export + '.Shot_Export_Directory', path, typ = 'string')
	maya.cmds.setAttr(Bakery_export + '.use_config_file', 1)
	maya.cmds.setAttr(Bakery_export + '.config_file', '//file-cluster/GDC/Projects/Zorro/Project/relight/tools/exports/mode1/assets_export_config.var', typ = 'string')

def bkCreateExportObjectAnim():
	'''
	Zorro
	Bakery -> Create Bakery Export Object
	'''
	sceneName = maya.cmds.file(query = True, sceneName = True, shortName = True)
	m = re.search('^zr_([^_\.]+)_([^_\.]+)_([^_\.]+)[_\.]', sceneName)
	if m == None:
		maya.OpenMaya.MGlobal.displayError(u'文件命名不规范')
		return
	ep = m.group(1)
	sq = m.group(2)
	sc = m.group(3)
	s = pyUtil.idmtService('GetTimeLine', sceneName)
	m = re.search('^(\d+)\|(\d+)\|\d+$', s)
	if m == None:
		maya.OpenMaya.MGlobal.displayError(u'不能从数据库读取帧数信息')
		return
	Start_Time = int(m.group(1))
	End_Time = int(m.group(2))
	if Start_Time == 1001:
		Start_Time = Start_Time - 1000
		End_Time = End_Time - 1000
	config_file = '//file-cluster/GDC/Projects/Zorro/Project/scenes/Animation/episode_%s/sequence_%s/scene_%s/scene_%s_export_config.var' % (ep, sq, sc, sc)
	#if not os.path.isfile(config_file):
	fi = open(r'\\file-cluster\GDC\Projects\Zorro\Project\relight\tools\exports\mode3\shots_export_config.var', 'r')
	temp = os.path.join(os.getenv('TEMP'), 'scene_%s_export_config.var' % sc)
	if os.path.isfile(temp):
		os.remove(temp)
	fo = open(temp, "w")
	while True:
		s = fi.readline()
		if not s:
			break
		s = re.sub(r'(v_export_first_frame = )\d+', r'\g<1>' + str(Start_Time), s)
		s = re.sub(r'(v_export_last_frame = )\d+', r'\g<1>' + str(End_Time), s)
		s = re.sub(r'(v_season_name = ).*', r'\g<1>"episode_' + ep + "\";", s)
		s = re.sub(r'(v_episode_name = ).*', r'\g<1>"sequence_' + sq + "\";", s)
		s = re.sub(r'(v_export_shot_name = ).*', r'\g<1>"scene_' + sc + "\";", s)
		fo.write(s)
	fi.close()
	fo.close()
	maya.mel.eval(r'zwSysFile "move" "%s" "%s" true' % (temp.replace('\\', '/'), config_file.replace('\\', '/')))
	#if not os.path.isfile(config_file):
	#	maya.OpenMaya.MGlobal.displayError(u'Config File不存在：%s' % config_file)
	#	return
	maya.mel.eval('bkCreateExportObject')
	Bakery_export = maya.cmds.ls(sl = True)[0]
	maya.cmds.setAttr(Bakery_export + '.All_Shot_Asset', 3)
	maya.cmds.setAttr(Bakery_export + '.animation_mode', 0)
	maya.cmds.setAttr(Bakery_export + '.use_config_file', 1)
	maya.cmds.setAttr(Bakery_export + '.config_file', config_file, typ = 'string')
	maya.cmds.setAttr(Bakery_export + '.Start_Time', Start_Time)
	maya.cmds.setAttr(Bakery_export + '.End_Time', End_Time)
	#maya.cmds.setAttr(Bakery_export + '.Motion_vectors', 1)
