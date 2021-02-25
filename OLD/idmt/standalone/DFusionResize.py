# -*- coding: utf-8 -*-
# Copyright (C) 2000-2010 IDMT. All rights reserved.
'''
'''
__author__	= 'huangzhongwei@idmt.com.cn'
__date__	= '2011-12-27'

import os
import re
import sys
import win32file


def Resize(source):
	statinfo = os.stat(source)
	dest = re.sub(r'[^\.]+$', 'png', source)
	cmd = "\\\\file-cluster\\GDC\\Resource\\Support\\Others\\ImageMagick-5.4.6-Q16\\convert.exe \"%s\" -resize 512x512 \"%s\"" % (source, source)
	os.system(cmd)
	filehandle = win32file.CreateFile(source, win32file.GENERIC_WRITE, 0, None, win32file.OPEN_EXISTING, 0, 0)
	win32file.SetFileTime(filehandle, None, None, statinfo.st_mtime)

if __name__ == "__main__":
	path = sys.argv[1]
	print path
	Resize(path)