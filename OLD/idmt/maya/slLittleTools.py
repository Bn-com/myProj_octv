# -*- coding: utf-8 -*-
# Copyright (C) 2000-2012 IDMT. All rights reserved.
'''
tools name:
1)�Ա������ļ��Ƿ�ͬ
2)���ȶԱ��޸�ʱ�䣬��ζԱȴ�С
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

