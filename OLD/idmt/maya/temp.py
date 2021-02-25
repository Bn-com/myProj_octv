# -*- coding: utf-8 -*-
# Copyright (C) 2000-2010 IDMT. All rights reserved.
'''
temp batch functions
'''
__author__	= 'huangzhongwei@idmt.com.cn'
__date__	= '2011-03-08'

import datetime
import idmt.maya.cmds
import idmt.maya.path
import maya.cmds as cmds
import maya.mel as mel
import maya.OpenMaya as OpenMaya
import maya.OpenMayaAnim as oma
import os
import shutil
import re

def lr_OPTtest20110308():
	'''
20110308 by huangzhongwei
zhaozhijie(赵志杰Tazz) 13:30:34
Z:\Projects\ROMA\PRJ_roma\SHOT_roma\stereo_cams_approved
idmt/check tools/optimize lightlinker nodes
	'''
	count = mel.eval('lr_OPTtest')
	if count > 0:
		cmds.file(save = True, force = True)

def ShenShou20110309(folder):
	folder = folder.replace('/', '\\')
	for root, dirs, files in os.walk(folder):
		for old in files:
			filename = re.compile(r'_l\d[^_]+_lr_c\d{3}_', re.IGNORECASE).sub('_', old)
			if filename != old:
				source = os.path.join(root, old)
				dest = os.path.join(root, filename)
				print '%s\t%s' % (old, filename)
				os.rename(source, dest)

def TestFixedReference(sceneName):
	cmds.file(sceneName, open = True, loadReferenceDepth = 'none')
	references = cmds.file(query = True, reference = True)
	for reference in references:
		unresolvedName = cmds.referenceQuery(reference, filename = True, unresolvedName = True, withoutCopyNumber = True)
		if re.compile(r'/scenes/characters/([^/]+/){3}[^/]+$', re.IGNORECASE).search(unresolvedName) != None:
			fo = open(r'E:\finishing.txt', "a")
			#fo.write('%s\r\n' % (sceneName.replace('/', '\\')))
			fo.write('D:\\alias\\maya2008\\bin\\mayabatch.exe -command \"python \\\"import idmt.maya.temp\\nidmt.maya.temp.FixedReference()\\\"" -file \"%s\"\r\n' % (sceneName.replace('/', '\\')))
			fo.close()
			return

def ListAnimation():
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
			path = os.path.join(SHOT_roma, scene, shot, r'scenes\animation')
			if not os.path.isdir(path):
				continue
			filenames = os.listdir(path)
			for filename in filenames:
				if re.compile(r'\.m(a|b)$', re.IGNORECASE).search(filename) != None:
					print 'D:\\alias\\maya2008\\bin\\mayabatch.exe -command \"python \\\"import idmt.maya.temp\\nidmt.maya.temp.TestFixedReference(\'%s\')\\\""' % (os.path.join(path, filename).replace('\\', '/'))

def ListFinishing():
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
				path = os.path.join(SHOT_roma, scene, shot, r'scenes\finishing', character)
				if not os.path.isdir(path):
					continue
				filenames = os.listdir(path)
				for filename in filenames:
					if re.compile(r'\.m(a|b)$', re.IGNORECASE).search(filename) != None:
						#print 'D:\\alias\\maya2008\\bin\\mayabatch.exe -command \"python \\\"import idmt.maya.temp\\nidmt.maya.temp.FixedReference()\\\"" -file \"%s\"' % (os.path.join(path, filename))
						print 'D:\\alias\\maya2008\\bin\\mayabatch.exe -command \"python \\\"import idmt.maya.temp\\nidmt.maya.temp.TestFixedReference(\'%s\')\\\""' % (os.path.join(path, filename).replace('\\', '/'))

def FixedReference(envName = 'MC_roma'):
	'''
	environment, fixed
	'''
	rs = False

	envValue = os.getenv(envName, '')
	references = cmds.file(query = True, reference = True)
	for reference in references:
		unresolvedName = cmds.referenceQuery(reference, filename = True, unresolvedName = True, withoutCopyNumber = True)
		if re.compile(r'^\${' + envName + '}', re.IGNORECASE).search(unresolvedName) != None and re.compile(r'/scenes/characters/([^/]+/){3}[^/]+$', re.IGNORECASE).search(unresolvedName) == None:
			continue
		if re.compile(r'/scenes/characters/([^/]+/){3}[^/]+$', re.IGNORECASE).search(unresolvedName) != None:
			unresolvedName = re.sub('([^/]+)$', 'fixed/\g<1>', unresolvedName)
		dollarPath = idmt.maya.path.GetDollarPath(unresolvedName)
		if re.compile(r'^\${' + envName + '}', re.IGNORECASE).search(dollarPath) == None:
			if envValue == '':
				OpenMaya.MGlobal.displayError(u'没有设置 %s 环境变量' % (envName))
				break
			OpenMaya.MGlobal.displayError(u'所有reference必须指向%s\n%s' % (envValue, reference))
			continue
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
					continue
				if unloaded == True:
					cmds.file(unloadReference = node)
				
				rs = True
			else:
				OpenMaya.MGlobal.displayError(u'所有reference必须指向%s\n%s' % (envValue, reference))
				continue

	if rs:
		cmds.file(save = True)
		#sceneName = cmds.file(query=True, sceneName = True)
		#fo = open(r'E:\finishing.txt', "a")
		#fo.write('%s\r\n' % (sceneName.replace('/', '\\')))
		#fo.close()
	
	return rs

def fol2128():
	Vegetation = r'\\file-cluster\GDC\Projects\ROMA\PRJ_roma\MC_roma\sourceimages\props\Vegetation'
	characters = os.listdir(Vegetation)
	for character in characters:
		path = os.path.join(Vegetation, character)
		if not os.path.isdir(path):
			continue
		types = os.listdir(path)
		for type in types:
			path = os.path.join(Vegetation, character, type, 'fol')
			if not os.path.isdir(path):
				continue
			filenames = os.listdir(path)
			for filename in filenames:
				source = os.path.join(path, filename)
				if not os.path.isfile(source):
					continue
				dest = os.path.join(path, 'nosize', filename)
				size = cmds.idmtImage(source, size = True)
				level = 1.0
				if size[0] > 128:
					level = 128.0 / float(size[0])
				cmds.idmtImage(source, dest, scale = level)
				#if os.path.isfile(dest):
				#	continue
				#destFolder = os.path.dirname(dest)
				#if not os.path.isdir(destFolder):
				#	os.mkdir(destFolder)
				#command = "\\\\file-cluster\\GDC\\Resource\\Support\\ImageMagick-6.6.7-0\\convert.exe \"%s\" -resize \"128x>\" \"%s\"" % (source, dest)
				#print command;
				#os.popen(command).read()
				#if not os.path.isfile(dest):
				#	continue
				#statinfo = os.stat(source)
				#os.utime(dest, (statinfo.st_mtime, statinfo.st_mtime))

def ListDefero(sceneName):
	cmds.file(sceneName, open = True, loadReferenceDepth = 'none')
	references = cmds.file(query = True, reference = True)
	for reference in references:
		if re.compile(r'/setup_Gladiators_Defero_Armour_HIG\.mb$', re.IGNORECASE).search(reference) != None:
			fo = open(r'\\file-cluster\GDC\Scratch\TD\setup_Gladiators_Defero_Armour_HIG.txt', "a")
			fo.write('%s\r\n' % (sceneName.replace('/', '\\')))
			fo.close()
			return

def DelWoodliesLightingHistory():
	size = 0
	Animation = r'Z:\Projects\Woodlies\Project\scenes\Animation'
	episodes = os.listdir(Animation)
	for episode in episodes:
		path = os.path.join(Animation, episode)
		if not os.path.isdir(path):
			continue
		sequences = os.listdir(path)
		for sequence in sequences:
			path = os.path.join(Animation, episode, sequence)
			if not os.path.isdir(path):
				continue
			scenes = os.listdir(path)
			for scene in scenes:
				path = os.path.join(Animation, episode, sequence, scene, 'lighting\\history')
				if not os.path.isdir(path):
					continue
				filenames = os.listdir(path)
				for filename in filenames:
					path = os.path.join(Animation, episode, sequence, scene, 'lighting\\history', filename)
					if not os.path.isfile(path):
						continue
					print path
					statinfo = os.stat(path)
					size = size + statinfo.st_size
					os.remove(path)
				path = os.path.join(Animation, episode, sequence, scene, 'lighting\\history')
				os.rmdir(path)
	print size

def ToogleMaps20111220():
	ress = ['', '8', '7', '6', '5', '4', '3', '2', '1', 'h', 'q']

	sourceimages = r'\\file-cluster\GDC\Projects\Ninjago\Project\sourceimages'
	assetTypes = os.listdir(sourceimages)
	for assetType in assetTypes:
		folder = os.path.join(sourceimages, assetType)
		if not os.path.isdir(folder):
			continue
		assetGroups = os.listdir(folder)
		for assetGroup in assetGroups:
			folder = os.path.join(sourceimages, assetType, assetGroup)
			if not os.path.isdir(folder):
				continue
			assets = os.listdir(folder)
			for asset in assets:
				folder = os.path.join(sourceimages, assetType, assetGroup, asset)
				if not os.path.isdir(folder):
					continue
				print folder
				done = []
				filenames = os.listdir(folder)
				for filename in filenames:
					#print filename
					if filename.lower() in done:
						continue
					path = os.path.join(folder, filename)
					if not os.path.isfile(path):
						continue
					if re.search(r'\.iff$', filename, re.IGNORECASE) == None:
						continue
					if re.search(r'_[hlms]\.iff$', filename, re.IGNORECASE) != None:
						continue

					filename0 = filename
					n = 0
					m = re.search(r'_([1-8hq])k(([_\.]\d+)?\.iff)$', filename, re.IGNORECASE)
					if m != None:
						for i in range(len(ress)):
							f = ''
							if i == 0:
								f = re.compile(r'_([1-8hq])k(([_\.]\d+)?\.iff)$', re.IGNORECASE).sub(r'\g<2>', filename)
							else:
								f = re.compile(r'_([1-8hq])k(([_\.]\d+)?\.iff)$', re.IGNORECASE).sub('_%sk%s' % (ress[i], r'\g<2>'), filename)
							path = os.path.join(folder, f)
							if os.path.isfile(path):
								filename0 = f
								n = i
								break
					if n < 7:
						n = 7

					source = os.path.join(folder, filename0)
					wh = cmds.idmtImage(source, size = True)
					for i in range(n, 11):
						f = re.compile(r'(_[1-8hq]k)?(([_\.]\d+)?\.iff)$', re.IGNORECASE).sub('_%sk%s' % (ress[i], r'\g<2>'), filename0)
						done.append(f.lower())
						if f.lower() == filename0.lower():
							continue
						w = 1024.0 * pow(2, 8-i)
						if wh[0] <= w or wh[1] <= w:
							continue
						dest = os.path.join(folder, f)
						if os.path.isfile(dest):
							continue
						cmds.idmtImage(source, dest, resize = [w, w])

def edo_reconnectAllDoD4Feet(bake=1):
    #bake=0
    ma=oma.MAnimControl()
    startTime=ma.minTime().value()
    endTime=ma.maxTime().value()
    sins=[]
    s0=cmds.ls('*FEET_OFFSET')
    s1=cmds.ls('*:FEET_OFFSET')
    s2=cmds.ls('*:*:FEET_OFFSET')
    s3=cmds.ls('*:*:*:FEET_OFFSET')
    sins=s0+s1+s2+s3
    allsins=[]
    if sins:
        for sin in sins:
            #sin=sins[0]
            ss=cmds.sets(sin,q=1)
            for s in ss:
                #s=ss[0]
                allsins.append(s)
    print allsins
    if bake==1:
        cmds.bakeSimulation(allsins,t=(startTime,endTime),at=['offset'])
    if bake==0:
        for s in allsins:
            #s=allsins[0]
            if cmds.objExists(s+'.offset') and cmds.objExists(s+'.offset_ex'):
                cmds.connectAttr(s+'.offset_ex',s+'.offset',f=1)
    if len(allsins) > 0:
        sceneName = cmds.file(query=True, sceneName = True)
        if sceneName == "":
            return
        avi = re.compile(r'\.m[ab]$', re.IGNORECASE).sub('.0001.avi', sceneName)
        if not os.path.isfile(avi):
            avi = re.compile(r'\.m[ab]$', re.IGNORECASE).sub('.0001.mov', sceneName)
        sceneName = cmds.file(query=True, sceneName = True, shortName = True)
        tempDir = cmds.diskCache(query = True, tempDir = True)
        temp = tempDir + '/' + sceneName
        cmds.file(rename = temp)
        cmds.file(save = True)
        cmds.idmtService("Checkout", "0|DiveollyDive4|%s|huangzhongwei" % (sceneName))
        if os.path.isfile(avi):
            cmds.idmtProject(checkin = True, description = u"批量修改章鱼触角设置", attachment = avi)
        else:
            cmds.idmtProject(checkin = True, description = u"批量修改章鱼触角设置")
        os.remove(temp)