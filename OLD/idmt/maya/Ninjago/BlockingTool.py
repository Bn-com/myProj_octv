# -*- coding: utf-8 -*-
# Copyright (C) 2000-2010 IDMT. All rights reserved.
'''
Ninjago Blocking Import Export
'''
__author__	= 'huangzhongwei@idmt.com.cn'
__date__	= '2011-04-14'

import idmt.maya.cmds
import maya.cmds as cmds
import maya.mel as mel
import maya.OpenMaya as OpenMaya
import os
import re

def Export():
	sceneName = cmds.file(query=True, sceneName = True, shortName =True)
	m = re.search(r'^nj_(E\d{4})_(Q\d{4})[_\.]', sceneName)
	if m == None:
		OpenMaya.MGlobal.displayError(u'文件命名不规范')
		return
	ep = m.group(1)
	sequence = m.group(2)

	cameras = cmds.ls(cameras = True, long = True)
	for camera in cameras:
		parent = cmds.listRelatives(camera, parent = True, fullPath = True)
		camera = parent[0]

		name = re.search(r'[^\|]+$', camera).group(0)
		m = re.search(r'^(Q\d{4})_(S\d{4})_Cam$', name)
		if m == None:
			continue
		seq = m.group(1)
		shot = m.group(2)
		camera = cmds.rename(camera, 'cam_%s_%s_%s' % (ep, seq, shot))
		cmds.select(camera)
		temp = os.path.join(os.getenv('TEMP'), 'nj_%s_%s_%s_cam.ma' % (ep, seq, shot))
		camera = cmds.rename(camera, name)
		cmds.file(temp, preserveReferences = True, exportSelected = True, type = 'mayaAscii')
		if not os.path.isfile(temp):
			continue
		dest = r'\\file-cluster\GDC\Projects\Ninjago\Project\data\Blocking\%s\%s\Camera_Group\%s.ma' % (ep, seq, name)
		command = r'zwSysFile "move" "%s" "%s" true' % (temp.replace('\\', '\\\\'), dest.replace('\\', '\\\\'))
		mel.eval(command)

	if not cmds.pluginInfo('animImportExport', query = True, loaded = True):
		cmds.loadPlugin('animImportExport')
	references = cmds.file(query = True, reference = True)
	references = idmt.maya.cmds.list(references)
	for reference in references:
		m = re.search(r'/Asset/([^/]+)', reference)
		if m == None:
			continue
		destFolder = r'\\file-cluster\GDC\Projects\Ninjago\Project\data\Blocking\%s\%s\Asset\%s' % (ep, sequence, re.sub(r'.*/Asset/', '', reference).replace('/', '\\'))
		command = r'zwSysFile "md" "%s" "" true' % (destFolder.replace('\\', '\\\\'))
		mel.eval(command)
		cmds.file(reference, selectAll = True, referenceNode = True)
		filename = cmds.referenceQuery(reference, filename = True, shortName = True)
		temp = os.path.join(os.getenv('TEMP'), 'anim.anim')
		try:
			cmds.file(temp, force = True, options = "precision=8;intValue=17;nodeNames=1;verboseUnits=0;whichRange=1;range=0:10;options=keys;hierarchy=none;controlPoints=0;shapes=1;helpPictures=0;useChannelBox=0;copyKeyCmd=-animation objects -option keys -hierarchy none -controlPoints 0 -shape 1 ", typ = "animExport", pr = True, es = True)
		except:
			continue
		if not os.path.isfile(temp):
			continue
		dest = os.path.join(destFolder, 'anim.anim')
		command = r'zwSysFile "move" "%s" "%s" true' % (temp.replace('\\', '\\\\'), dest.replace('\\', '\\\\'))
		mel.eval(command)

	cameras = cmds.ls(cameras = True, long = True)
	for camera in cameras:
		parent = cmds.listRelatives(camera, parent = True, fullPath = True)
		camera = parent[0]

		name = re.search(r'[^\|]+$', camera).group(0)
		m = re.search(r'^(Q\d{4})_(S\d{4})_Cam$', name)
		if m == None:
			continue
		sq = m.group(1)
		sc = m.group(2)
		Import(ep, sq, sc)

def Import(ep, sq, sc):
	cameraFile = r'//file-cluster/GDC/Projects/Ninjago/Project/data/Blocking/%s/%s/Camera_Group/%s_%s_Cam.ma' % (ep, sq, sq, sc)
	if not os.path.isfile(cameraFile):
		OpenMaya.MGlobal.displayError(u'找不到对应的摄像机文件')
		OpenMaya.MGlobal.displayError(cameraFile)
		return
	cmds.file(cameraFile, open = True, force = True)
	filename = 'nj_%s_%s_%s_ly_001.ma' % (ep, sq, sc)
	temp = os.path.join(os.getenv('TEMP'), filename)
	cmds.file(rename = temp)

	GetAssetInAnims = []
	assetTypes = ['characters', 'misc', 'props', 'sets']
	for assetType in assetTypes:
		GetAssetInAnim = cmds.idmtService('GetAssetInAnimNinjago', r'%s|%s|master' % (filename, assetType))
		if GetAssetInAnim == '':
			continue
		buf = GetAssetInAnim.split('|')
		for i in range(0, len(buf), 3):
			GetAssetInAnims.append(assetType)
			GetAssetInAnims.append(buf[i+0])
			GetAssetInAnims.append(buf[i+1])
			GetAssetInAnims.append(buf[i+2])

	referenceCount = 0

	AssetFolder = r'\\file-cluster\GDC\Projects\Ninjago\Project\data\Blocking\%s\%s\Asset' % (ep, sq)
	if not os.path.isdir(AssetFolder):
		return
	for root, dirs, files in os.walk(AssetFolder):
		for ma in dirs:
			if re.search('\.m[ab]({|$)', ma, re.IGNORECASE) != None:
				m = re.search(r'\\Asset\\([^\\]+)\\([^\\]+)\\([^\\]+)', root)
				if m == None:
					continue
				assetType = m.group(1)
				assetCode = m.group(2)
				assetName = m.group(3)
				assetType = re.sub('^Chars', 'characters', assetType, re.IGNORECASE)
				for i in range(0, len(GetAssetInAnims), 4):
					if re.search(r'^%s$' % (assetType), GetAssetInAnims[i], re.IGNORECASE) == None:
						continue
					if re.search(r'^%s$' % (assetCode), GetAssetInAnims[i+1], re.IGNORECASE) == None:
						continue
					if re.search(r'^[a-z]\d{6}%s' % (assetName), GetAssetInAnims[i+2], re.IGNORECASE) == None:
						continue
					assetPath = os.path.join(r'\\file-cluster\GDC\Projects\Ninjago\Project\scenes', GetAssetInAnims[i], GetAssetInAnims[i+1], GetAssetInAnims[i+2], 'master', GetAssetInAnims[i+3])
					fileType = 'mayaAscii'
					if re.search('\.mb$', GetAssetInAnims[i+3], re.IGNORECASE) != None:
						fileType = 'mayaBinary'
					reference = mel.eval(r'slImportRef "%s" "%s"' % (assetPath.replace('\\', '\\\\'), fileType))
					referenceCount = referenceCount + 1
					anim = os.path.join(root, ma, 'anim.anim')
					if os.path.isfile(anim):
						ImportAnim(anim, reference)
					break

	if referenceCount > 0:
		cmds.file(save = True, force = True)
		cmds.idmtProject(checkin = True, description = u'Blocking工具自动生成')
		os.remove(temp)

def ImportUI():
	def run(cmd):
		return lambda x : cmds.python('try:\n\treload(' + __name__ + ')\nexcept:\n\timport ' + __name__ + '\n' + __name__ + '.' + cmd)

	sceneName = cmds.file(query=True, sceneName = True, shortName =True)
	m = re.search(r'^nj_(E\d{4})_(Q\d{4})_(S\d{4})[_\.]', sceneName)
	if m == None:
		OpenMaya.MGlobal.displayError(u'文件命名不规范')
		return
	ep = m.group(1)
	sequence = m.group(2)
	shot = m.group(3)
	
	if cmds.window('ImportBlocking', exists = True):
		cmds.deleteUI('ImportBlocking')
	window1 = cmds.window('ImportBlocking', title = 'Import Blocking', width = 300, height = 400)
	formLayout1 = cmds.formLayout()
	tabLayout1 = cmds.tabLayout(tabsVisible = False, scrollable = True, childResizable = True)
	cmds.columnLayout(adjustableColumn = True, rowSpacing = 4)
	path = r'//file-cluster/GDC/Projects/Ninjago/Project/data/Blocking/%s/%s/Camera_Group/%s_%s_Cam.ma' % (ep, sequence, sequence, shot)
	enable = os.path.isfile(path)
	cmds.button(label = u'导入Blocking摄像机', en = enable, command = run('ImportCamera("%s")' % (path)))
	AssetFolder = r'\\file-cluster\GDC\Projects\Ninjago\Project\data\Blocking\%s\%s\Asset' % (ep, sequence)
	if os.path.isdir(AssetFolder):
		cmds.frameLayout(label = u'在Reference Editor选择参考，导入其动画', borderStyle = 'etchedIn', collapsable = True)
		cmds.columnLayout(adjustableColumn = True)
		assetTypes = os.listdir(AssetFolder)
		for assetType in assetTypes:
			assetTypeFolder = os.path.join(AssetFolder, assetType)
			if not os.path.isdir(assetTypeFolder):
				continue
			cmds.frameLayout(label = assetType, borderStyle = 'etchedIn', collapsable = True)
			cmds.columnLayout(adjustableColumn = True)
			
			for root, dirs, files in os.walk(assetTypeFolder):
				for filename in files:
					if filename == 'anim.anim':
						asset = os.path.basename(root)
						anim = os.path.join(root, 'anim.anim')
						cmds.button(label = asset, command = run('ImportAnim("%s")' % (anim.replace('\\', '/'))))
			cmds.setParent('..')
			cmds.setParent('..')
	cmds.formLayout(formLayout1, edit = True, attachForm = ((tabLayout1, 'left', 0), (tabLayout1, 'top', 0), (tabLayout1, 'right', 0), (tabLayout1, 'bottom', 0)))
	cmds.showWindow(window1)

def ImportCamera(path):
	cmds.file(path, i = True)

def ImportAnim(animFile, reference = None):
	ControlMap = {
		'SuperRoot_Ctrl' : 'Master',
		'Root_Ctrl' : 'Character',
		'Head_Ctrl' : 'head_ctrl',
		'Pelvis_Ctrl' : 'waist_Ctrl',
		'Hip_Ctrl' : 'root_waist_ikCtrl',
		'L_Thigh_Ctrl' : 'LfLeg_Leg_FK',
		'L_Knee_Ctrl' : 'LfLeg_Knee_FK',
		'L_Ankle_Ctrl' : 'LfLeg_Ankle_FK',
		'R_Thigh_Ctrl' : 'RtLeg_Leg_FK',
		'R_Knee_Ctrl' : 'RtLeg_Knee_FK',
		'R_Ankle_Ctrl' : 'RtLeg_Ankle_FK',
		'Spine1_Ctrl' : 'waist_FK1_ctrl',
		'Spine2_Ctrl' : 'waist_FK2_ctrl',
		'L_Shoulder_Ctrl' : 'LfArm_UpArm_FK',
		'L_Elbow_Ctrl' : 'LfArm_Elbow_FK',
		'L_Wrist_Ctrl' : 'LfArm_Wrist_FK',
		'L_Thumb_Ctrl' : 'Lf_finger1_ctrl',
		'L_Pinky_Ctrl' : 'Lf_finger2_ctrl',
		'R_Shoulder_Ctrl' : 'RtArm_UpArm_FK',
		'R_Elbow_Ctrl' : 'RtArm_Elbow_FK',
		'R_Wrist_Ctrl' : 'RtArm_Wrist_FK',
		'R_Thumb_Ctrl' : 'Rt_finger1_ctrl',
		'R_Pinky_Ctrl' : 'Rt_finger2_ctrl',
		'L_IkThigh_Ctrl' : 'LfLeg_tipIkCtrl',
		'L_Leg_Ctrl' : 'LfLeg_Leg_IK',
		'R_IkThigh_Ctrl' : 'RtLeg_tipIkCtrl',
		'R_Leg_Ctrl' : 'RtLeg_Leg_IK',
		'L_IkShoulder_Ctrl' : 'Lf_shoulder',
		'L_Arm_Ctrl' : 'LfArm_Wrist_IK',
		'R_IkShoulder_Ctrl' : 'Rt_shoulder',
		'R_Arm_Ctrl' : 'RtArm_Wrist_IK',
		'LightningDragon_neckRoot_Con' : 'neck_fk_ctrl1',
		'LightningDragon_neckBase_Con' : 'neck_fk_ctrl2',
		'LightningDragon_headCon' : 'neck_fk_ctrl3',
		'LightningDragon_chestCon' : 'body_fk_ctrl1',
		'LightningDragon_trunkCon' : 'body_fk_ctrl3',
		'LightningDragon_rootCon' : 'waist_Ctrl',
		'LightningDragon_tail1_Con' : 'tail_fk_ctrl1',
		'LightningDragon_tail2_Con' : 'tail_fk_ctrl2',
		'LightningDragon_tail3_Con' : 'tail_fk_ctrl3',
		'LightningDragon_heelik_LCon' : 'LfLeg_Leg_IK',
		'LightningDragonFront_heelik_LCon' : 'Lf1Leg_Leg_IK',
		'LightningDragon_heelik_RCon' : 'RtLeg_Leg_IK',
		'LightningDragonFront_heelik_RCon' : 'Rt1Leg_Leg_IK',
		'LightningDragon_armfk_LCon' : 'Lfwing_fk_ctrl1',
		'LightningDragon_thumbA_L_Con' : 'Lfwrist_fk_ctrl',
		'LightningDragon_wristfk_LCon' : 'Lfwing_fk_ctrl3',
		'LightningDragon_finger4A_L_Con' : 'Lfwing_1_1',
		'LightningDragon_finger4B_L_Con' : 'Lfwing_1_2',
		'LightningDragon_finger3A_L_Con' : 'Lfwing_2_1',
		'LightningDragon_finger3B_L_Con' : 'Lfwing_2_2',
		'LightningDragon_finger2A_L_Con' : 'Lfwing_3_1',
		'LightningDragon_finger2B_L_Con' : 'Lfwing_3_2',
		'LightningDragon_finger1A_L_Con' : 'Lfwing_4_1',
		'LightningDragon_finger1B_L_Con' : 'Lfwing_2_2',
		'LightningDragon_armfk_RCon' : 'Rtwing_fk_ctrl1',
		'LightningDragon_thumbA_R_Con' : 'Rtwrist_fk_ctrl',
		'LightningDragon_wristfk_RCon' : 'Rtwing_fk_ctrl3',
		'LightningDragon_finger4A_R_Con' : 'Rtwing_1_1',
		'LightningDragon_finger4B_R_Con' : 'Rtwing_1_2',
		'LightningDragon_finger3A_R_Con' : 'Rtwing_2_1',
		'LightningDragon_finger3B_R_Con' : 'Rtwing_2_2',
		'LightningDragon_finger2A_R_Con' : 'Rtwing_3_1',
		'LightningDragon_finger2B_R_Con' : 'Rtwing_3_2',
		'LightningDragon_finger1A_R_Con' : 'Rtwing_4_1',
		'LightningDragon_finger1B_R_Con' : 'Rtwing_2_2',
		'LightningDragon_thumb2A_L_Con' : 'Lf_Toe_thumb1',
		'LightningDragon_thumb2B_L_Con' : 'Lf_Toe_thumb2',
		'LightningDragon_thumb2C_L_Con' : 'Lf_Toe_thumb3',
		'LightningDragon_toe1A_L_Con' : 'Lf_Toe_index1',
		'LightningDragon_toe1B_L_Con' : 'Lf_Toe_index2',
		'LightningDragon_toe1C_L_Con' : 'Lf_Toe_index3',
		'LightningDragon_toe2A_L_Con' : 'Lf_Toe_mid1',
		'LightningDragon_toe2B_L_Con' : 'Lf_Toe_mid2',
		'LightningDragon_toe2C_L_Con' : 'Lf_Toe_mid3',
		'LightningDragon_toe3A_L_Con' : 'Lf_Toe_ring1',
		'LightningDragon_toe3B_L_Con' : 'Lf_Toe_ring2',
		'LightningDragon_toe3C_L_Con' : 'Lf_Toe_ring3',
		'LightningDragonFront_thumb2A_L_Con' : 'Lf1_Toe_thumb1',
		'LightningDragonFront_thumb2B_L_Con' : 'Lf1_Toe_thumb2',
		'LightningDragonFront_thumb2C_L_Con' : 'Lf1_Toe_thumb3',
		'LightningDragonFront_toe1A_L_Con' : 'Lf1_Toe_index1',
		'LightningDragonFront_toe1B_L_Con' : 'Lf1_Toe_index2',
		'LightningDragonFront_toe1C_L_Con' : 'Lf1_Toe_index3',
		'LightningDragonFront_toe2A_L_Con' : 'Lf1_Toe_mid1',
		'LightningDragonFront_toe2B_L_Con' : 'Lf1_Toe_mid2',
		'LightningDragonFront_toe2C_L_Con' : 'Lf1_Toe_mid3',
		'LightningDragonFront_toe3A_L_Con' : 'Lf1_Toe_ring1',
		'LightningDragonFront_toe3B_L_Con' : 'Lf1_Toe_ring2',
		'LightningDragonFront_toe3C_L_Con' : 'Lf1_Toe_ring3',
		'LightningDragon_thumb2A_R_Con' : 'Rt_Toe_thumb1',
		'LightningDragon_thumb2B_R_Con' : 'Rt_Toe_thumb2',
		'LightningDragon_thumb2C_R_Con' : 'Rt_Toe_thumb3',
		'LightningDragon_toe1A_R_Con' : 'Rt_Toe_index1',
		'LightningDragon_toe1B_R_Con' : 'Rt_Toe_index2',
		'LightningDragon_toe1C_R_Con' : 'Rt_Toe_index3',
		'LightningDragon_toe2A_R_Con' : 'Rt_Toe_mid1',
		'LightningDragon_toe2B_R_Con' : 'Rt_Toe_mid2',
		'LightningDragon_toe2C_R_Con' : 'Rt_Toe_mid3',
		'LightningDragon_toe3A_R_Con' : 'Rt_Toe_ring1',
		'LightningDragon_toe3B_R_Con' : 'Rt_Toe_ring2',
		'LightningDragon_toe3C_R_Con' : 'Rt_Toe_ring3',
		'LightningDragonFront_thumb2A_R_Con' : 'Rt1_Toe_thumb1',
		'LightningDragonFront_thumb2B_R_Con' : 'Rt1_Toe_thumb2',
		'LightningDragonFront_thumb2C_R_Con' : 'Rt1_Toe_thumb3',
		'LightningDragonFront_toe1A_R_Con' : 'Rt1_Toe_index1',
		'LightningDragonFront_toe1B_R_Con' : 'Rt1_Toe_index2',
		'LightningDragonFront_toe1C_R_Con' : 'Rt1_Toe_index3',
		'LightningDragonFront_toe2A_R_Con' : 'Rt1_Toe_mid1',
		'LightningDragonFront_toe2B_R_Con' : 'Rt1_Toe_mid2',
		'LightningDragonFront_toe2C_R_Con' : 'Rt1_Toe_mid3',
		'LightningDragonFront_toe3A_R_Con' : 'Rt1_Toe_ring1',
		'LightningDragonFront_toe3B_R_Con' : 'Rt1_Toe_ring2',
		'LightningDragonFront_toe3C_R_Con' : 'Rt1_Toe_ring3'}

	if reference == None:
		mel.eval('global string $gReferenceEditorPanel')
		references = None
		try:
			references = mel.eval('sceneEditor -query -selectItem $gReferenceEditorPanel')
		except:
			pass
		if idmt.maya.cmds.len(references) != 1:
			OpenMaya.MGlobal.displayError(u'请在Reference Editor选择一个参考')
			return
		reference = references[0]
	namespace = cmds.file(reference, query = True, namespace = True)
	
	head = ''
	headEnd = False
	anim = ''
	oldObj = ''
	newObj = ''
	attr = ''

	if not cmds.pluginInfo('animImportExport', query = True, loaded = True):
		cmds.loadPlugin('animImportExport')

	fi = open(animFile, "r")
	while True:
		oldLine = fi.readline()
		if not oldLine:
			break
		
		m = re.search(r'^anim (\S+) \S+ (\S+)( \d){3};', oldLine)
		if m != None:
			headEnd = True
			anim = ''

			oldObj = m.group(2)
			attr = m.group(1)
			if re.search(r'([^:]+:){2}', oldObj) != None:
				OpenMaya.MGlobal.displayWarning(u'属性无效：%s.%s' % (oldObj, attr))
				continue
			shortName = re.search(r'[^:]+$', oldObj).group(0)
			newObj = r'%s:%s' % (namespace, shortName)
			if not cmds.objExists(newObj):
				if shortName in ControlMap:
					shortName = ControlMap[shortName]
					newObj = r'%s:%s' % (namespace, shortName)
			#if not cmds.objExists(newObj):
			#	buf = cmds.ls('%s:*_%s' % (namespace, newObj))
			#	if idmt.maya.cmds.len(buf) == 1:
			#		newObj = buf[0]
			if cmds.objExists('%s.%s' % (newObj, attr)):
				anim = re.sub(r'^(anim \S+ \S+ )\S+( \d \d )\d', r'\g<1>%s\g<2>0' % (newObj), oldLine)
			else:
				OpenMaya.MGlobal.displayWarning(u'属性无效：%s.%s' % (oldObj, attr))
			continue
		
		if not headEnd:
			head = head + oldLine
			continue

		if anim != '':
			anim = anim + oldLine
			if re.search(r'^}', oldLine) != None:
				anim = head + anim
				temp = os.path.join(os.getenv('TEMP'), '%s_%s.anim' % (newObj.replace(':', '_'), attr.replace('.', '_')))
				fo = open(temp, "w")
				fo.write(anim)
				fo.close()
				anim = ''
				cmds.select(newObj)
				try:
					cmds.file(temp, i = True, type ="animImport", options = "targetTime=4;copies=1;option=replace;pictures=0;connect=0;")
					print u'成功设置：%s.%s' % (newObj, attr)
				except:
					OpenMaya.MGlobal.displayWarning(u'不能设置：%s.%s' % (newObj, attr))
				os.remove(temp)
	fi.close()