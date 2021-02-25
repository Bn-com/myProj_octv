# -*- coding: utf-8 -*-
# Copyright (C) 2000-2010 IDMT. All rights reserved.
'''
'''
__author__	= 'huangzhongwei@idmt.com.cn'
__date__	= '2011-12-27'

import glob
import os
import re
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

def mySysFile(action, source, dest):
	print '%s \"%s\" \"%s\"' % (action, source, dest)

	source = GetUNC(source)
	source = re.compile(r'^([a-z]):', re.IGNORECASE).sub(r'//%s/\g<1>$' % os.getenv('COMPUTERNAME'), source)

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   
	sock.connect(('192.168.2.10', 2345))
	ss = '%s%%%%%s%%%%%s%%%%%s' % (os.getenv('USERNAME'), action, source, dest)
	sock.send(ss)
	sr = sock.recv(1024)
	sock.close()
	if sr == ss:
		return True
	else:
		sr = re.sub(r'^#\d+', '', sr)
		sr = re.sub(r' at \w:.*$', '', sr)
		print sr
		return False

def Checkin(source):
	filename = os.path.basename(source)
	(root, ext) = os.path.splitext(filename)
	root = re.sub(r'_[a-zA-Z]\d+\.', '', root)
	asset = re.search(r'^[^_]+', root).group(0)
	folder = '\\\\file-cluster\\GDC\\Projects\\Zorro\\Project\\relight\\assets\\' + asset
	s = pyUtil.idmtService('GetAssetPath', 'zr_%s_h_tx.ma' % asset)
	#if not os.path.isdir(folder):
	if re.search(r'\\\\file-cluster\\GDC\\Projects\\Zorro\\Project\\scenes\\', s, re.IGNORECASE) == None:
		print u'// Error: Asset 不存在：%s' % asset
		sys.exit(-1)
	dest = os.path.join(folder, root + ext)
	if os.path.isfile(dest):
		files = glob.glob(os.path.join(folder, 'history', root + "_c???" + ext))
		history = os.path.join(folder, 'history', '%s_c%03d%s' % (root, len(files)+1, ext))
		if not mySysFile('copy', dest, history):
			sys.exit(-1)
	if not mySysFile('copy', source, dest):
		sys.exit(-1)

if __name__ == "__main__":
	path = sys.argv[1]
	print path
	Checkin(path)