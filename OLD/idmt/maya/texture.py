# -*- coding: utf-8 -*-
# Copyright (C) 2000-2010 IDMT. All rights reserved.
'''
functions for texture
'''
__author__	= 'huangzhongwei@idmt.com.cn'
__date__	= '2011-05-23'

import hashlib

def md5(decodeStr):
	m = hashlib.md5()
	m.update(decodeStr)
	encodeStr = m.hexdigest()
	return encodeStr