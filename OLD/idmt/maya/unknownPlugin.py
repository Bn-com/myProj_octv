# -*- coding: utf-8 -*-

import maya.cmds as cmds
import maya.mel as mel
import os
import re
import struct

def GetLong(s):
    l = (struct.unpack('B', s[0])[0] << 56) + (struct.unpack('B', s[1])[0] << 48) + (struct.unpack('B', s[2])[0] << 40) + (struct.unpack('B', s[3])[0] << 32) + (struct.unpack('B', s[4])[0] << 24) + (struct.unpack('B', s[5])[0] << 16) + (struct.unpack('B', s[6])[0] << 8) + (struct.unpack('B', s[7])[0] << 0)
    return l

def RemoveUnknownPluginMb(mbIn, mbOut):
    if mbIn == mbOut:
        return
    unknownPlugins = []
    allPlugins = []
    #pathEnvVar = os.getenv("MAYA_PLUG_IN_PATH")
    pathEnvVar = mel.eval('getenv "MAYA_PLUG_IN_PATH"')
    pathArray = pathEnvVar.split(";")
    for path in pathArray:
        #if path == "//file-cluster/GDC/Resource/Development/Maya/GDC/3partPlugin/2014/unknown/plug-ins":
        if re.search(r"[/\\]unknown[/\\]", path, re.IGNORECASE) != None:
            continue
        if not os.path.isdir(path):
            continue
        plugins = os.listdir(path)
        for plugin in plugins:
            if not re.search(r'\.(py|mll|nll\.dll|pyc)$', plugin, re.IGNORECASE):
                continue
            if not os.path.isfile(os.path.join(path, plugin)):
                continue
            allPlugins.append(plugin)

    fo = open(mbOut, "wb")
    fi = open(mbIn, "rb")
    s = fi.read(8)
    fo.write(s)
    s = fi.read(8)
    fo.write(s)
    fileSizeOld = GetLong(s)
    s = fi.read(12)
    fo.write(s)
    s = fi.read(8)
    fo.write(s)
    headerSizeOld = GetLong(s)
    fileSizeNew = fileSizeOld
    headerSizeNew = headerSizeOld
    while True:
        i = fi.tell()
        if i > 28 + headerSizeOld:
            break
        s1 = fi.read(4)
        if s1 != 'PLUG':
            fo.write(s1)
            continue
        s2 = fi.read(4)
        s3 = fi.read(8)
        plugSize = GetLong(s3)
        remainder = plugSize % 8
        if remainder != 0:
            remainder = 8
        plugSize = plugSize / 8 * 8 + remainder
        s4 = fi.read(plugSize)

        ss = s4.split('\0')
        pluginName = ss[0]
        unknown = True
        if len(ss) > 3:
            if ss[2] != "":
                unknown = False
        if unknown:
            for plugin in allPlugins:
                if re.search(r'^%s(\.(py|mll|nll\.dll|pyc))?$' % re.escape(pluginName), plugin, re.IGNORECASE) != None:
                    unknown = False
                    break
        if not unknown:
            if re.search(r'^Miarmy(Express|Pro)ForMaya', pluginName, re.IGNORECASE) != None:
                if re.search(r'^Miarmy(Express|Pro)ForMaya2012', pluginName, re.IGNORECASE) != None:
                    unknown = True
        
        if unknown:
            headerSizeNew = headerSizeNew - plugSize - 16
            fileSizeNew = fileSizeNew - plugSize - 16
            unknownPlugins.append(pluginName)
        else:
            fo.write(s1)
            fo.write(s2)
            fo.write(s3)
            fo.write(s4)
    while True:
        s = fi.read(1024)
        if not s:
            break
        fo.write(s)
    fi.close()
    fo.seek(8)
    s = struct.pack('Q', fileSizeNew)
    for i in range(len(s)-1, -1, -1):
        fo.write(s[i])
    fo.seek(28)
    s = struct.pack('Q', headerSizeNew)
    for i in range(len(s)-1, -1, -1):
        fo.write(s[i])
    fo.close()
    print "Remove %d Unknown Plugin: " % (len(unknownPlugins))
    print unknownPlugins
    return unknownPlugins

def RemoveUnknownPluginMa(maIn, maOut):
    if maIn == maOut:
        return
    unknownPlugins = []
    allPlugins = []
    #pathEnvVar = os.getenv("MAYA_PLUG_IN_PATH")
    pathEnvVar = mel.eval('getenv "MAYA_PLUG_IN_PATH"')
    pathArray = pathEnvVar.split(";")
    for path in pathArray:
        #if path == "//file-cluster/GDC/Resource/Development/Maya/GDC/3partPlugin/2014/unknown/plug-ins":#
        if re.search(r"[/\\]unknown[/\\]", path, re.IGNORECASE) != None:
            continue
        if not os.path.isdir(path):
            continue
        plugins = os.listdir(path)
        for plugin in plugins:
            if not re.search(r'\.(py|mll|nll\.dll|pyc)$', plugin, re.IGNORECASE):
                continue
            if not os.path.isfile(os.path.join(path, plugin)):
                continue
            allPlugins.append(plugin)

    fo = open(maOut, "w")
    fi = open(maIn, "r")
    while True:
        line = fi.readline()
        if not line:
            break
        unknown = True
        m = re.search(r'^requires \"([^\"]+)\" \"[^\"]+\";$', line, re.IGNORECASE)
        if m:
            pluginName = m.group(1)
            #if cmds.pluginInfo(pluginName, query = True, loaded = True):2032
            #    unknown = False
            #else:
            for plugin in allPlugins:
                if re.search(r'^%s(\.(py|mll|nll\.dll|pyc))?$' % re.escape(pluginName), plugin, re.IGNORECASE) != None:
                    unknown = False
                    break
            if not unknown:
                if re.search(r'^Miarmy(Express|Pro)ForMaya', pluginName, re.IGNORECASE) != None:
                    if re.search(r'^Miarmy(Express|Pro)ForMaya2012', pluginName, re.IGNORECASE) != None:
                        unknown = True
        else:
            unknown = False
        if unknown:
            unknownPlugins.append(pluginName)
        else:
            fo.write(line)
    fi.close()
    fo.close()
    print "Remove %d Unknown Plugin: " % (len(unknownPlugins))
    print unknownPlugins
    return unknownPlugins