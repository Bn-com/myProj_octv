# -*- coding: utf-8 -*-
# Copyright (C) 2000-2010 IDMT. All rights reserved.
'''
Ninjago: fix asset reference
'''
__author__	= 'huangzhongwei@idmt.com.cn'
__date__	= '2011-09-27'

import os
import re
import shutil
import socket
import sys
import win32wnet

import pyUtil3 as pyUtil

def GetUNC(path):
	try:
		path = win32wnet.WNetGetUniversalName(path)
	except:
		pass
	return path

def NinjagoFixAssetReference(path):
	if re.search(r'\.ma$', path, re.IGNORECASE) == None:
		return
	path = GetUNC(path)
	if re.search(r'^\\\\file-cluster\\GDC\\Projects\\Ninjago\\Project\\scenes\\Animation\\', path, re.IGNORECASE) != None:
		if re.search(r'\\history\\', path, re.IGNORECASE) != None:
			return

	s = pyUtil.idmtService('GetAssetNameInAnim',  path)
	if s == '':
		return

	filename = os.path.basename(path)
	temp = os.path.join(os.getenv('TEMP'), filename)
	if os.path.isfile(temp):
		os.remove(temp)

	fix = False
	requires = False
	fi = open(path, "r")
	fo = open(temp, "w")
	while True:
		line = fi.readline()
		if not line:
			break
		if not requires:
			if re.search('^requires ', line) != None:
				requires = True
			else:
				m = re.search(r'\"([^\"]+\.ma)\"', line, re.IGNORECASE)
				if m != None:
					referenceOld = GetUNC(m.group(1))
					if re.search(r'^//file-cluster/GDC/Projects/Ninjago/Project/scenes/', referenceOld, re.IGNORECASE) != None:
						filenameOld = os.path.basename(referenceOld)
						assetOld = re.search(r'[^_]+_([^_]+)_', filenameOld).group(1)
						if re.search(r'\|%s(\||$)' % assetOld, s, re.IGNORECASE) == None:
							assetParent = re.search(r'.{4}', assetOld).group(0)
							m = re.search(r'\|(%s[^\|]+)' % assetParent, s, re.IGNORECASE)
							if m != None:
								assetNew = m.group(1)
								filenameNew = filenameOld.replace(assetOld, assetNew)
								referenceNew = pyUtil.idmtService('GetAssetPath',  filenameNew)
								if os.path.isfile(referenceNew):
									print '%s\t=> %s' % (assetOld, assetNew)
									referenceNew = referenceNew.replace('\\', '/')
									line = re.sub(r'\"[^\"]+\.ma\"', '\"%s\"' % referenceNew, line)
									fix = True
		fo.write(line)
	fi.close()
	fo.close()

	if fix:
		try:
			if re.search(r'^\\\\file-cluster\\GDC\\Projects\\Ninjago\\Project\\scenes\\Animation\\', path, re.IGNORECASE) != None:
				history = os.path.join(os.path.dirname(path), history)
				if not os.path.isdir(history):
					os.mkdir(history)
				history = os.path.join(history, filename)
				if not os.path.isfile(history):
					shutil.copy(path, history)
			shutil.move(temp, path)
		except:
			#print u'文件操作失败'
			os.remove(temp)
	else:
		#print u'文件未作修改'
		os.remove(temp)

path = sys.argv[1]
print path
NinjagoFixAssetReference(path)