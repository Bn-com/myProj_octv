# -*- coding: utf-8 -*-
# Copyright (C) 2000-2010 IDMT. All rights reserved.
'''
Functions for Image
'''
__author__    = 'huangzhongwei@idmt.com.cn'
__date__    = '2014-08-12'

import maya.cmds
import maya.mel
import os
import re

def getSize(img):
    return maya.mel.eval('zwImageSize \"' + img.replace('\\', '/') + '\"')

def resize(source, dest, width, height):
    if re.search(r'\.iff$', source, re.IGNORECASE) == None and re.search(r'\.iff$', dest, re.IGNORECASE) == None:
        cmd = "\\\\file-cluster\\GDC\\Resource\\Support\\ImageMagick-6.6.7-0\\convert.exe \"%s\" -resize %dx%d \"%s\"" % (source.replace('/', '\\'), width, height, dest.replace('/', '\\'))
        print os.popen(cmd).read()
        maya.cmds.idmtFile(source, dest, copyModified = True)
    else:
        temp = source
        if re.search(' ', source) != None:
            temp = os.path.join(maya.cmds.diskCache(tempDir = True), os.path.basename(source))
            maya.cmds.sysFile(temp, delete = True)
            maya.cmds.sysFile(source, copy = temp)
            temp = maya.cmds.idmtFile(temp, shortPath = True)
        maya.cmds.idmtImage(temp, dest, resize = [width, height])
        if temp != source:
            maya.cmds.sysFile(temp, delete = True)