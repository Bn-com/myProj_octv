# -*- coding: utf-8 -*-
# Copyright (C) 2000-2012 IDMT. All rights reserved.
'''
tools name:
1)对比两个文件是否不同
2)首先对比修改时间，其次对比大小
'''
__author__ = 'wanshoulong'
__date__    = ''

import os

def slFileContrast(source,dest):
	same=1

	SMTime = os.path.getmtime(source)
	DMTime = os.path.getmtime(dest)
	if SMTime != DMTime:
		same=0
	else:
		SSize = os.path.getsize(source)
		DSize = os.path.getsize(dest)
		if SSize != DSize:
			same=0
	
	return same	

