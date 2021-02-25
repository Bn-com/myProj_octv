# -*- coding: utf-8 -*-
# Copyright (C) 2000-2011 IDMT. All rights reserved.
__author__    = 'huangzhongwei@idmt.com.cn'
__date__    = '2012-01-11'

import ctypes
import datetime
import maya.cmds
import maya.OpenMaya
import os
import re
import threading

from PyQt4.QtCore import *
from PyQt4.QtGui import *

beforeOpenCheckId = None
debugObj = None

def checkMessageBox():
    global debugObj
    if debugObj == None:
        return
    messageBox =  qApp.activeModalWidget()
    if messageBox != None:
        debugObj.end = datetime.datetime.now()
        return
    t = threading.Timer(1.0, checkMessageBox)
    t.start()

def kBeforeOpenCheck(retCode, file, clientData):
    ctypes.cast(long(retCode), ctypes.POINTER(ctypes.c_ubyte)).contents.value = True

    if re.search('^(mk)_', file.rawName()) == None:
        return

    global debugObj
    debugObj = debugLoadFile()

    debugObj.beforeLoadReferenceCheckId = maya.OpenMaya.MSceneMessage.addCheckFileCallback(maya.OpenMaya.MSceneMessage.kBeforeLoadReferenceCheck, kBeforeLoadReferenceCheck)
    debugObj.afterOpenId = maya.OpenMaya.MSceneMessage.addCallback(maya.OpenMaya.MSceneMessage.kAfterOpen, kAfterOpen2)

    debugObj.rawFullName = file.rawFullName()
    debugObj.start = datetime.datetime.now()

    if maya.cmds.about(apiVersion = True) >= 201100:
        checkMessageBox()

def kAfterOpen(clientData):
    global debugObj
    maya.OpenMaya.MSceneMessage.removeCallback(debugObj.beforeLoadReferenceCheckId)
    maya.OpenMaya.MSceneMessage.removeCallback(debugObj.afterOpenId)

    if debugObj.end == datetime.datetime.min:
        debugObj.end = datetime.datetime.now()
    debugObj.span = debugObj.end - debugObj.start

    size = 0

    s = ''

    for reference in debugObj.files:
        statinfo = os.stat(reference.resolvedFullName)
        speed = 0
        if reference.span.microseconds != 0:
            speed = statinfo.st_size / 1024.0 / 1024.0 / (reference.span.seconds + reference.span.microseconds / 1000000.0)
        size = size + statinfo.st_size

        s = '%s*%d|%.3f|%.3f|%s' % (s, reference.span.seconds, speed, statinfo.st_size / 1024.0 / 1024.0, reference.rawFullName.replace('/', '\\'))

    statinfo = os.stat(debugObj.rawFullName)
    size = size + statinfo.st_size
    speed = 0
    if debugObj.span.microseconds != 0:
        speed = size / 1024.0 / 1024.0 / (debugObj.span.seconds + debugObj.span.microseconds / 1000000.0)
    s = '%s|%s|%d|%.3f|%d|%.3f|%s%s' % (os.getenv('COMPUTERNAME'), debugObj.start.strftime('%Y/%m/%d %H:%M:%S'), debugObj.span.seconds, speed, len(debugObj.files), size / 1024.0 / 1024.0, debugObj.rawFullName.replace('/', '\\'), s)
    logId = maya.cmds.idmtService('OpenFileLog', s)

    debugObj = None

def kAfterOpen2(clientData):
    batch = False
    if maya.cmds.about(batch = True):
        batch = True

    global debugObj
    maya.OpenMaya.MSceneMessage.removeCallback(debugObj.beforeLoadReferenceCheckId)
    maya.OpenMaya.MSceneMessage.removeCallback(debugObj.afterOpenId)

    if debugObj.end == datetime.datetime.min:
        debugObj.end = datetime.datetime.now()
    debugObj.span = debugObj.end - debugObj.start

    size = 0

    s = ''

    for reference in debugObj.files:
        statinfo = os.stat(reference.resolvedFullName)
        span = reference.span.seconds * 1000 + reference.span.microseconds / 1000
        speed = int(statinfo.st_size / 1024.0 / (span / 1000.0))
        size = size + statinfo.st_size

        s = '%s*%s|%d|%d|%d|%s' % (s, reference.start.strftime('%Y/%m/%d %H:%M:%S'), span, speed, statinfo.st_size / 1024, reference.rawFullName.replace('/', '\\'))

    statinfo = os.stat(debugObj.rawFullName)
    size = size + statinfo.st_size
    span = debugObj.span.seconds * 1000 + debugObj.span.microseconds / 1000
    speed = int(size / 1024.0 / (span / 1000.0))
    s = '%s|%s|%s|%s|%d|%d|%d|%d|%s%s' % (os.getenv('COMPUTERNAME'), os.getenv('USERNAME'), batch, debugObj.start.strftime('%Y/%m/%d %H:%M:%S'), span, speed, len(debugObj.files), size / 1024, debugObj.rawFullName.replace('/', '\\'), s)
    if os.getenv('USERNAME') == 'huangzhongwei':
        print s
    else:
        logId = maya.cmds.idmtService('OpenFileLog2', s)

    debugObj = None

def kBeforeLoadReferenceCheck(retCode, file, clientData):
    ctypes.cast(long(retCode), ctypes.POINTER(ctypes.c_ubyte)).contents.value = True

    reference = debugLoadFile()
    reference.rawFullName = file.rawFullName()
    reference.resolvedFullName = file.resolvedFullName()
    reference.afterLoadReferenceId = maya.OpenMaya.MSceneMessage.addCallback(maya.OpenMaya.MSceneMessage.kAfterLoadReference, kAfterLoadReference)
    reference.start = datetime.datetime.now()

    global debugObj
    debugObj.references.append(reference)

def kAfterLoadReference(clientData):
    global debugObj
    reference = debugObj.references.pop()
    maya.OpenMaya.MSceneMessage.removeCallback(reference.afterLoadReferenceId)
    
    reference.end = datetime.datetime.now()
    reference.span = reference.end - reference.start
    debugObj.files.append(reference)

class debugLoadFile(object):
    def __init__(self):
        self.beforeLoadReferenceCheckId = 0
        self.afterLoadReferenceId = 0
        self.afterOpenId = 0

        self.rawFullName = ''
        self.resolvedFullName = ''
        self.size = 0
        
        self.start = datetime.datetime.min
        self.end = datetime.datetime.min
        self.span = self.end - self.start
        
        self.references = []
        self.files = []

def addCallback():
    global beforeOpenCheckId
    if beforeOpenCheckId == None:
        beforeOpenCheckId = maya.OpenMaya.MSceneMessage.addCheckFileCallback(maya.OpenMaya.MSceneMessage.kBeforeOpenCheck, kBeforeOpenCheck)

def removeCallback():
    global beforeOpenCheckId
    if beforeOpenCheckId != None:
        maya.OpenMaya.MSceneMessage.removeCallback(beforeOpenCheckId)
        beforeOpenCheckId = None