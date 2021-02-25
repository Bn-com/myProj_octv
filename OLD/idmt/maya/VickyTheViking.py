# -*- coding: utf-8 -*-
# Copyright (C) 2000-2010 IDMT. All rights reserved.
'''
Tools for VickyTheViking
'''
__author__	= 'huangzhongwei@idmt.com.cn'
__date__	= '2013-06-06'

import os
import re
import shutil

def H2L(path):
	temp = os.getenv('TEMP') + "\\temp.ma"
	if os.path.isfile(temp):
		os.remove(temp)

	fi = open(path, "r")
	fo = open(temp, "w")
	while True:
		oldLine = fi.readline()
		if not oldLine:
			break
		newLine = oldLine
		m = re.compile(r'"[^\"]+(/VickyTheViking/Project/scenes/01_main_pack/[^\"]+)\.ma"', re.IGNORECASE).search(oldLine)
		if m != None:
			low = '//file-cluster/GDC/Projects%s_l.ma' % (m.group(1))
			if os.path.isfile(low):
				newLine = re.compile(r'"[^\"]+(/VickyTheViking/Project/scenes/01_main_pack/[^\"]+)\.ma"', re.IGNORECASE).sub('"${IDMT_PROJECTS}\g<1>_l.ma"', newLine)
			else:
				newLine = re.compile(r'"[^\"]+(/VickyTheViking/Project/scenes/01_main_pack/[^\"]+)\.ma"', re.IGNORECASE).sub('"${IDMT_PROJECTS}\g<1>.ma"', newLine)
		fo.write(newLine)
	fi.close()
	fo.close()

	shutil.move(temp, path)
