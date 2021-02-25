# -*- coding: utf-8 -*-
# Copyright (C) 2000-2010 IDMT. All rights reserved.
'''
defaultLayer1
'''
__author__	= 'huangzhongwei@idmt.com.cn'
__date__	= '2011-08-26'

import os
import re
import shutil
import sys

path = sys.argv[1]
if re.search(r'\.ma$', path, re.IGNORECASE) != None:
	temp = os.getenv('TEMP') + "\\temp.ma"
	if os.path.isfile(temp):
		os.remove(temp)

	find = False
	fi = open(path, "r")
	fo = open(temp, "w")
	while True:
		oldLine = fi.readline()
		if not oldLine:
			break
		newLine = oldLine
		newLine = re.compile(r'Z:/Projects/|//file-cluster/GDC/Projects/', re.IGNORECASE).sub('${IDMT_PROJECTS}/', newLine)
		if oldLine != newLine:
			find = True
		fo.write(newLine)
	fi.close()
	fo.close()
	if find:
		shutil.move(temp, path)
	else:
		os.remove(temp)