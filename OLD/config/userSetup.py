# -*- coding: utf-8 -*-

__author__    = 'huangzhongwei@idmt.com.cn'
__date__    = '2013-08-02'

import re
import sys
import os

PYTHONPATH = r'C:\tools\LocalTools\3partPlugin\pxUsd\lib\python'
if os.path.exists(PYTHONPATH) and PYTHONPATH not in sys.path:
    sys.path.append(PYTHONPATH)

PYTHONPATH = r'\\file-cluster\GDC\Resource\Development\Maya\GDC\Plug\Python\GDC'
if not PYTHONPATH in sys.path:
    sys.path.append(PYTHONPATH)
ver = sys.winver
PYTHONPATH = r'\\file-cluster\GDC\Resource\Development\Maya\GDC\Plug\Python\%s\Lib\site-packages' % ver
if not PYTHONPATH in sys.path:
    sys.path.append(PYTHONPATH)

if re.search('32 bit', sys.version) == None:
    ver = '%s-x64' % sys.winver
PYTHONPATH = r'\\file-cluster\GDC\Resource\Support\Python\%s\DLLs' % ver
if PYTHONPATH in sys.path:
    sys.path.remove(PYTHONPATH)
PYTHONPATH = r'\\file-cluster\GDC\Resource\Support\Python\%s\Lib\site-packages' % ver
if PYTHONPATH in sys.path:
    sys.path.remove(PYTHONPATH)

import idmt.maya.customIDMTSetup as customIDMTSetup
customIDMTSetup.customIDMTSetup()