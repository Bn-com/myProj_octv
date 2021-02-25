# -*- coding: utf-8 -*-
# Copyright (C) 2000-2010 IDMT. All rights reserved.
'''
关于Checkin的系列函数
'''
__author__    = 'huangzhongwei@idmt.com.cn'
__date__    = '2011-03-21'

import idmt.maya.cmds
import idmt.maya.path
import maya.cmds as cmds
import maya.mel as mel
import maya.OpenMaya as OpenMaya
import os
import re
import zipfile
import hashlib
import suds
import tempfile
import json
import logging
import time

def UploadMiProxyFile(folder):
    '''
    上传miProxyFile
    '''
    done = []
    pattern = re.sub(r'/scenes/.*$', '/', folder)
    miProxyFiles = cmds.ls(shapes = True)
    for miProxyFile in miProxyFiles:
        attr = '%s.miProxyFile' % (miProxyFile)
        if not cmds.objExists(attr):
            continue
        source = cmds.getAttr(attr)
        if source == None:
            continue
        if not os.path.isfile(source):
            continue
        source = idmt.maya.path.GetFullPath(source)
        if re.compile(pattern, re.IGNORECASE).search(source) != None:
            idmt.maya.cmds.setAttr(attr, source)
            continue
        dest = '%s/%s' % (folder, os.path.basename(source))
        if not source in done:
            mel.eval('zwSysFile "copy" "%s" "%s" true' % (source, dest))
            done.append(source)
        idmt.maya.cmds.setAttr(attr, dest)

def zipScene():
    sceneName = cmds.file(query = True, sceneName = True)
    zipFileName = re.sub(r'[^\.]+$', 'zip', sceneName)
    zip = zipfile.ZipFile(zipFileName, 'w', zipfile.ZIP_DEFLATED)
    arcname = "scenes\\%s" % (cmds.file(query = True, sceneName = True, shortName = True))
    zip.write(sceneName, arcname)
    files = cmds.file(query = True, list = True)
    for file in files:
        m = re.search("/(sourceimages/.*)$", file)
        if m is None:
            continue
        arcname = m.group(1).replace('/', '\\')
        zip.write(file, arcname)
    workspace = os.path.join(cmds.workspace(query = True, fullName = True), "workspace.mel")
    if os.path.isfile(workspace):
        zip.write(workspace, "workspace.mel")
    zip.close()

def zipYodaRg(destFolder, asset_type):
    destFolder = destFolder.replace("/", "\\")
    sceneName = cmds.file(query = True, sceneName = True)
    zipFileName = re.sub(r'[^\.]+$', 'zip', sceneName)
    zip = zipfile.ZipFile(zipFileName, 'w', zipfile.ZIP_DEFLATED, True)
    filename = cmds.file(query = True, sceneName = True, shortName = True)
    if asset_type == "sets":
        filename = filename.replace("_rg.", "_ms_tex.")
    else:
        filename = filename.replace("_rg.", "_ms_anim.").replace("_tx.", "_ms_anim.")
    arcname = "scenes\\%s\\master\\%s" % (re.sub(r'.*\\scenes\\(.*)\\[^\\]+$', r'\g<1>', destFolder), filename)
    arcname = "scenes\\%s" % (filename)
    zip.write(sceneName, arcname)
    files = cmds.file(query = True, list = True)
    for file in files:
        m = re.search("/(sourceimages/.*)$", file, re.IGNORECASE)
        if m is None:
            continue
        arcname = m.group(1).replace('/', '\\')
        arcname = "sourceimages\\%s" % (os.path.basename(file))
        zip.write(file, arcname)
    zip.close()

def YODA_addVersion():
    if cmds.objExists("time1.version"):
        return
    filename = cmds.file(query = True, sceneName = True, shortName = True)
    m = re.search(r"^[^\._]+_([^\._]+)_([^\._]+)_([^\._]+)_(an|fs)[\._]", filename, re.IGNORECASE)
    if not m:
        return
    episode = m.group(1)
    scene = m.group(2)
    shot = m.group(3)
    folder = "\\\\file-cluster\\GDC\\Projects\\YODA\\Project\\scenes\\Animation\\episode_%s\\sequence_%s\\scene_%s\\anim" % (episode, scene, shot)
    if not os.path.isdir(folder):
        return
    source = cmds.file(query = True, sceneName = True)
    md51 = GetFileMd5(source)
    ans = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            if re.search("\.m(a|b)$", file, re.IGNORECASE):
                ans.append(os.path.join(root, file))
    ans.sort()
    ans.reverse()
    for an in ans:
        md52 = GetFileMd5(an)
        if md51 == md52:
            filename = os.path.basename(an)
            cmds.addAttr("time1", shortName = "ver", longName = "version", dataType = "string")
            cmds.setAttr("time1.version", filename, type = "string")
            break

def GetFileMd5(filename):
    myhash = hashlib.md5()
    f = file(filename, 'rb')
    while True:
        b = f.read(8096)
        if not b :
            break
        myhash.update(b)
    f.close()
    return myhash.hexdigest().upper()

def ShunLiuCheckinAssetLog(msg = "", failLog = ""):
    if msg != "":
        OpenMaya.MGlobal.displayError(msg)

    print "\n\n\n";
    f = open("\\\\file-cluster\\GDC\\Resource\\Support\\Maya\\2013\\gdc.txt", "r")
    while True:
        line = f.readline()
        if not line:
            break
        print line.rstrip()
    f.close()
    print "\n\n\n"
    time.sleep(5.0)

    if failLog != "":
        f = open(failLog, "w")
        f.close()

def ShunLiuCheckinAsset(folder, imgFilename):
    logging.getLogger('suds').setLevel(logging.CRITICAL)

    sh019 = "E:\\Checkin"
    projectName = "ShunLiu"
    projectNameShort = "csl"

    m = re.search(r"^([a-z0-9]+_([a-z0-9]+)(_([a-z0-9]+))?_(h|l)_(mo|rg|tx))(_c?\d{3})?\.([a-z0-9]+)$", imgFilename, re.IGNORECASE)
    task_name = m.group(1)
    asset_name = m.group(2)
    _sep = m.group(3)
    if _sep == None:
        _sep = ""
    asset_sep = m.group(4)
    if asset_sep == None:
        asset_sep = ""
    lod = m.group(5).lower()
    pp = m.group(6).lower()
    mime = m.group(8).lower()

    # log
    startLog = os.path.join(sh019, task_name, "start")
    if os.path.isfile(startLog):
        os.remove(startLog)
    f = open(startLog, "w")
    f.close()
    failLog = os.path.join(sh019, task_name, "fail")
    if os.path.isfile(failLog):
        os.remove(failLog)
    successLog = os.path.join(sh019, task_name, "success")
    if os.path.isfile(successLog):
        os.remove(successLog)

    # open maya file fail
    zipFilename = cmds.file(query = True, sceneName = True, shortName = True)
    if zipFilename == "":
        ShunLiuCheckinAssetLog(msg = u"不能获取当前文件名，可能原因：文件损坏、打开报错、maya版本不正确", failLog = failLog)
        return

    param = [folder, task_name, asset_name, asset_sep, lod, pp]
    paramJson = json.dumps(param)
    client = suds.client.Client("http://idmt-plex/plex/ws/daily.asmx?wsdl")
    reply = client.service.GetTB("DB.PLEX.%s" % projectName, "P_FtpCheckinAssetStep1", paramJson)
    if reply == "":
        ShunLiuCheckinAssetLog(msg = u"P_FtpCheckinAssetStep1错误", failLog = failLog)
        return
    try:
        dt = json.loads(reply)
    except:
        ShunLiuCheckinAssetLog(msg = u"P_FtpCheckinAssetStep1错误", failLog = failLog)
        return
    msg = dt[0]["msg"]
    asset_id = dt[0]["asset_id"]
    asset_name = dt[0]["asset_name"]
    asset_type = dt[0]["asset_type"]
    doBy = dt[0]["doBy"]
    dailyVer = dt[0]["dailyVer"]
    mayaVer = dt[0]["mayaVer"]
    vloume = dt[0]["vloume"]
    if msg != "":
        ShunLiuCheckinAssetLog(msg = msg, failLog = failLog)
        return

    # zjCheckinClean.mel
    asset_mode = pp
    if pp == "mo":
        asset_mode = "model"
    elif pp == "rg":
        asset_mode = "rigging"
    elif pp == "tx":
        asset_mode = "texture"
    ext = re.search(r"[^\.]+$", zipFilename).group().lower()
    asset_file = "%s_%s%s_%s_%s.%s" % (projectNameShort, asset_name, _sep, lod, pp, ext)
    temp = os.path.join(tempfile.gettempdir(), asset_file)
    if os.path.isfile(temp):
        os.remove(temp)
    destFolder = "//file-cluster/GDC/Projects/%s/Project/scenes/%s/%s/%s" % (projectName, asset_type, asset_name, asset_mode)
    command = "zjCheckinClean(5, {\"%s\", \"%s\", \"%s\", \"1\", \"0\", \"0\", \"1\", \"50\", \"1\", \"%s\", \"%s\", \"0\"})" % (projectName, asset_file, destFolder, asset_mode, asset_type)
    try:
        mel.eval(command)
    except:
        ShunLiuCheckinAssetLog(failLog = failLog)
        return

    # upload maya
    mayaDest = os.path.join(destFolder, asset_file)
    if mayaVer > 1 and os.path.isfile(mayaDest):
        history = os.path.join(destFolder, "history", "%s_%s%s_%s_%s_c%03d.%s" % (projectNameShort, asset_name, _sep, lod, pp, mayaVer - 1, ext))
        if not os.path.isfile(history):
            rs = mel.eval("zwSysFile \"copy\" \"%s\" \"%s\" 1" % (mayaDest.replace("\\", "\\\\"), history.replace("\\", "\\\\")))
            if rs != "":
                ShunLiuCheckinAssetLog(msg = rs, failLog = failLog)
                return
    rs = mel.eval("zwSysFile \"move\" \"%s\" \"%s\" 1" % (temp.replace("\\", "\\\\"), mayaDest.replace("\\", "\\\\")))
    if rs != "":
        ShunLiuCheckinAssetLog(msg = rs, failLog = failLog)
        return

    imgPath = os.path.join(sh019, task_name, imgFilename)
    dest = os.path.join(destFolder, "%s_%s%s_%s_%s.0001.%s" % (projectNameShort, asset_name, _sep, lod, pp, mime))
    rs = mel.eval("zwSysFile \"copy\" \"%s\" \"%s\" 1" % (imgPath.replace("\\", "\\\\"), dest.replace("\\", "\\\\")))
    if rs != "":
        ShunLiuCheckinAssetLog(msg = rs, failLog = failLog)
        return

    # usp_AssetFile_Input
    mw = False
    description = ""
    needPass = None
    progress = 50
    enable = 1
    dot = 0
    renderCnt = 1
    edition = "2014"
    statinfo = os.stat(temp)
    size = statinfo.st_size / 1024
    if statinfo.st_size % 1024:
        size = size + 1
    location = "sz"
    hasComment = False
    param = [asset_id, mw, asset_mode, asset_sep, asset_file, doby, mayaVer, description, needPass, progress, lod, mime, enable, dot, renderCnt, edition, size, location, hasComment]
    paramJson = json.dumps(param)
    reply = client.service.GetTB("DB.PLEX.%s" % projectName, "usp_AssetFile_Input", paramJson)

    # upload daily
    filename = "%s_%s%s_%s_%s_c%03d.%s" % (projectNameShort, asset_name, _sep, lod, pp, dailyVer, mime)
    dest = os.path.join("\\\\file-cluster\\GDC\\Projects", projectName, "Production\\Daily\\standby", volume, filename)
    rs = mel.eval("zwSysFile \"copy\" \"%s\" \"%s\" 1" % (imgPath.replace("\\", "\\\\"), dest.replace("\\", "\\\\")))
    if rs != "":
        ShunLiuCheckinAssetLog(msg = rs, failLog = failLog)
        return

    # usp_DailyFile_Input
    mode = asset_mode
    if asset_mode in ["model", "texture"]:
        mode = "preproduction"
    scene = ""
    hasMB = False
    MBExtension = ""
    isFile = True
    referRemark = mayaDest
    corpFile = "SZ"

    param = [filename, mode, volume, scene, asset_id, mime, hasMB, MBExtension, isFile, doBy, referRemark, corpFile]
    paramJson = json.dumps(param)
    reply = client.service.GetTB("DB.PLEX.%s" % projectName, "usp_DailyFile_Input", paramJson)

    successLog = os.path.join(sh019, task_name, "success")
    f = open(successLog, "w")
    f.close()