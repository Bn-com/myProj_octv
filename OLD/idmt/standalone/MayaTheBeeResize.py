# -*- coding: utf-8 -*-
# Copyright (C) 2000-2010 IDMT. All rights reserved.
'''
'''
__author__	= 'huangzhongwei@idmt.com.cn'
__date__	= '2011-12-27'

import glob
import os
import re
import shutil
import sys
import win32file

import win32con
import win32gui
import win32process
def _EnumWindowsProc(hwnd, extra):
	windowText = win32gui.GetWindowText(hwnd)
	if re.search('^ImageMagick Studio library and utility programs', windowText) != None or re.search('^convert.exe - Application Error', windowText) != None:
		win32gui.SendMessage(hwnd, win32con.WM_CLOSE)

import datetime
import threading
def myCloseWindow():
	win32gui.EnumWindows(_EnumWindowsProc, None)
	t = threading.Timer(1.0, myCloseWindow)
	t.start()

def Resize(source):
	cmd = "D:\\Alias\\Maya2010x64\\bin\\imf_info.exe \"%s\"" % (source)
	rs = os.popen(cmd).read()
	if re.search('\s+1280\s+720\s+', rs) != None:
		sys.exit(0)
	if re.search('\s+1920\s+1080\s+', rs) == None:
		print u'// Error: 只能转换1920x1080的图片'
		sys.exit(-1)
	
	statinfo = os.stat(source)

	temp = source
	filename = os.path.basename(source)
	if re.search('\.tif$', filename, re.IGNORECASE) != None:
		temp = os.path.join(os.path.dirname(source), re.sub('\.', '_temp.', filename))
		os.rename(source, temp)

	cmd = "\\\\file-cluster\\GDC\\Resource\\Support\\Others\\ImageMagick-5.4.6-Q16\\convert.exe \"%s\" -resize 1280x720 \"%s\"" % (temp, source)
	print cmd
	rs = os.system(cmd)

	if rs != 0:
		if temp != source:
			cmd = "D:\\Alias\\Maya2010x64\\bin\\imf_diff.exe \"\\\\file-cluster\\GDC\\Projects\\MayaTheBee\\Project\\data\\Resize\\1080p\\MA_Ep008_Sq001B_Sc024_Rendering_Tk01_MGxtraPass.0130.tif\" \"%s\"" % (temp)
			rs1 = os.popen(cmd).read()
			if re.search(' are identical', rs1) != None:
				shutil.copy("\\\\file-cluster\\GDC\\Projects\\MayaTheBee\\Project\\data\\Resize\\720p\\MA_Ep008_Sq001B_Sc024_Rendering_Tk01_MGxtraPass.0130.tif", source)
				rs = 0

	if temp != source:
		if os.path.isfile(temp):
			if rs == 0:
				os.remove(temp)
			else:
				if os.path.isfile(source):
					os.remove(source)
				os.rename(temp, source)

	if rs == 0:
		filehandle = win32file.CreateFile(source, win32file.GENERIC_WRITE, 0, None, win32file.OPEN_EXISTING, 0, 0)
		win32file.SetFileTime(filehandle, None, None, statinfo.st_mtime)

	sys.exit(rs)

if __name__ == "__main__":
	path = sys.argv[1]
	print path
	myCloseWindow()
	Resize(path)