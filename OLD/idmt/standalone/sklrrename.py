# -*- coding: utf-8 -*-
# Copyright (C) 2000-2010 IDMT. All rights reserved.
'''
defaultLayer1
'''
__author__	= 'huangzhongwei@idmt.com.cn'
__date__	= '2014-12-31'

import os
import sys
import re

path = sys.argv[1]
filename = os.path.basename(path)
p = re.compile(r'^(([^_]+_){3}[^_]+)((_[^_]+)+)(_lr[\._])', re.IGNORECASE)
m = p.search(filename)
if m != None:
    d = p.sub(r'\g<1>%s\g<5>' % m.group(3).replace('_', ''), filename)
    folder = os.path.dirname(path)
    d = os.path.join(folder, d)
    os.rename(path, d)