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
	cmd = "D:\\Alias\\Maya2010x64\\bin\\imf_diff.exe \"\\\\file-cluster\\GDC\\Projects\\MayaTheBee\\Project\\data\\Resize\\1080p\\MA_Ep008_Sq001B_Sc024_Rendering_Tk01_MGxtraPass.0130.tif\" \"%s\"" % (source)
	rs = os.popen(cmd).read()
	if re.search(' are identical', rs) != None:
		print path
		rs = 0

if __name__ == "__main__":
	path = sys.argv[1]
	Resize(path)