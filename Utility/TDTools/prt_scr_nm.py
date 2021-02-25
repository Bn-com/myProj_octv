#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = prt_scr_nm
__author__ = zhangben 
__mtime__ = 2019/4/29 : 9:06
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
"""
print __file__
from sys import version_info
# adict = dict(a=1,b=2)
# try:
#     v = adict['c']
# except Exception as e:
#     # ex = Exception("密码长度不够".decode('utf-8'))
#     ex = "密码长度不够"
#     if version_info.major == 2:
#         raise ValueError(ex.encode('utf-8'))
#     elif version_info.major == 3:
#         raise ValueError(ex)

ex = u"密码长度不够"
if version_info.major == 2:
    raise ValueError(ex.encode('utf-8'))
elif version_info.major == 3:
    raise ValueError(ex)


#
# else:
#     raise YourException("not supported Python version")
#
# if isinstance(msg, str):
#    raise ValueError(msg)
# else:
#    raise ValueError(msg.encode('utf-8'))