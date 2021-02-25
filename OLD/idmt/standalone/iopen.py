# -*- coding: utf-8 -*-
# Copyright (C) 2000-2010 IDMT. All rights reserved.
'''
'''
__author__	= 'huangzhongwei@idmt.com.cn'
__date__	= '2015-06-03'

import os
import re
import sys

if __name__ == "__main__":
    path = sys.argv[1]
    path = re.sub(r'^iopen://', '', path)
    path = re.sub(r'/$', '', path)
    os.startfile(path)