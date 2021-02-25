# -*- coding: utf-8 -*-
# Copyright (C) 2000-2010 IDMT. All rights reserved.

__author__    = 'huangzhongwei@idmt.com.cn'
__date__    = '2013-02-27'

import os
import re
import maya.cmds

def lighting():
    filename = maya.cmds.file(query = True, sceneName = True, shortName = True)
    if filename == "":
        return
    filename = re.sub(r'\.mb$', '.ma', filename)
    temp = os.path.join(maya.cmds.diskCache(query = True, tempDir = True), filename)
    if os.path.isfile(temp):
        os.remove(temp)
    maya.cmds.file(rename = temp)

    folder = "D:\\Info_Temp\\Calimero_render"
    if not os.path.isdir(folder):
        os.makedirs(folder)
    dest = os.path.join(folder, filename)
    if os.path.isfile(dest):
        os.remove(dest)

    referencs = maya.cmds.file(query = True, reference = True)
    for referenc in referencs:
        if re.search(r'_cam\.ma', referenc, re.IGNORECASE) != None:
            maya.cmds.file(referenc, removeReference = True)

    find = False
    referencs = maya.cmds.file(query = True, reference = True, shortName = True, withoutCopyNumber = True)
    for referenc in referencs:
        if referenc == "CAL_CAMERA_00.ma":
            find = True
            break
    if not find:
         maya.cmds.file("Z:/Projects/Calimero/Common_Sync/CAL_MAYA/scenes/CAMERA/CAL_CAMERA_00.ma", reference= True, namespace = "CAMERA")

    maya.cmds.file(force = True, prompt = False, save = True, uiConfiguration = False, type = "mayaAscii")

    f = open("\\\\file-cluster\\GDC\\Projects\\Calimero\\Common_Sync\\CAL_MAYA\\2013\\python\\teamto\\hierarchy.txt", 'r')
    hierarchy = f.readlines()
    f.close()

    fi = open(temp, "r")
    fo = open(dest, "w")
    while True:
        line = fi.readline()
        if not line:
            break
        m = re.search(r"\"([^\"]+/Calimero/Project/scenes/[^/\"]+/([^/\"]+)/[^/\"]+/([^/\"]+))\"", line, re.IGNORECASE)
        if m != None:
            pathOld = m.group(1)
            asset = m.group(2)
            sceneName = m.group(3)
            step = ""
            if re.search(r"_(mo|layout)[\._]", sceneName, re.IGNORECASE) != None:
                step = "layout"
            elif re.search(r"_(rg|anim)[\._]", sceneName, re.IGNORECASE) != None:
                step = "anim"
            elif re.search(r"_tx[\._]", sceneName, re.IGNORECASE) != None:
                step = "tx"
            elif re.search(r"_render[\._]", sceneName, re.IGNORECASE) != None:
                step = "render"
            if step != "":
                pathNew = ""
                for hi in hierarchy:
                    if re.search(r"\|" + asset + r"\|", hi, re.IGNORECASE) != None:
                        hi = re.sub(r"\s", "", hi)
                        hi = re.sub(r"^MODELS\|", "scenes/", hi)
                        hi = hi.replace("|", "/")
                        pathNew = "//tex.alphanim.lan/Calimero/CAL_RSYNC/CAL_MAYA//%spublish/%s_%s_000.ma" % (hi, asset.lower(), step)
                if pathNew != "":
                    line = line.replace(pathOld, pathNew)

        m = re.search("\"([^\"]+CAL_CAMERA_00.ma)\"", line, re.IGNORECASE)
        if m != None:
            pathOld = m.group(1)
            pathNew = "//tex.alphanim.lan/Calimero/CAL_RSYNC/CAL_MAYA//scenes/CAMERA/CAL_CAMERA_00.ma"
            line = line.replace(pathOld, pathNew)

        fo.write(line)
    fi.close()
    fo.close()

    os.remove(temp)