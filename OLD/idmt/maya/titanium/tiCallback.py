# -*- coding: utf-8 -*-

import ctypes
import maya.cmds
import maya.mel
import maya.OpenMaya
import maya.utils
import os
import re
import shutil
import sys
import tiSceneOpenJob as  tiSceneOpenJob
reload(tiSceneOpenJob)

def BeforeImportCheck(retCode, file, clientData):
    print '*' * 50
    print 'Callback -> BeforeImportCheck'
    print '*' * 50

def BeforeOpenCheck(retCode, file, clientData):
    print '*' * 50
    print 'Callback -> BeforeOpenCheck'
    print '*' * 50

def BeforeExportCheck(retCode, file, clientData):
    print '*' * 50
    print 'Callback -> BeforeExportCheck'
    print '*' * 50

def BeforeCreateReferenceCheck(retCode, file, clientData):

    ctypes.cast(long(retCode), ctypes.POINTER(ctypes.c_ubyte)).contents.value = True
    try:
        pathOld = file.expandedFullName()    # 得到原来的路径
        pathNew = pathOld

        if re.compile(r'[/\\](XJCS)[/\\]', re.IGNORECASE).search(pathNew):
            if re.compile(r'[/\\](model)[/\\]', re.IGNORECASE).search(pathNew):
                print '=== this is model file ==='
                # pathNew = re.compile(r'model', re.IGNORECASE).sub(r'master', pathNew)
                # pathNew = re.compile(r'_mo.(ma|mb)', re.IGNORECASE).sub(r'_ms_anim.mb', pathNew)

                # if os.path.isfile(pathNew):
                    # print "%s -> %s" % (pathOld, pathNew)
                    # file.setRawFullName(pathNew)
                # elif maya.OpenMaya.MGlobal.mayaState() == maya.OpenMaya.MGlobal.kBatch:
                    # os.environ['REFERENCE_FILE_NOT_FOUND'] = "REFERENCE_FILE_NOT_FOUND"

            elif re.compile(r'_rg.(ma|mb)$', re.IGNORECASE).search(pathNew):
                print '=== this is rg file ==='
                # msAnim = re.compile(r'_rg.(ma|mb)', re.IGNORECASE).sub(r'_ms_anim.mb', pathNew)
                # msAnim = re.compile(r'rigging', re.IGNORECASE).sub(r'master', msAnim)
                
                # if os.path.isfile(msAnim):
                #     print "%s -> %s" % (pathOld, msAnim)
                #     file.setRawFullName(msAnim)
                    
                # else:
                #     rg = re.compile(r'master', re.IGNORECASE).sub(r'rigging', pathNew)
                #     if os.path.isfile(rg):
                #         print "%s -> %s" % (pathOld, rg)
                #         file.setRawFullName(rg)
    except:
        pass



def BeforeLoadReferenceCheck(retCode, file, clientData):
    print '*' * 50
    print 'Callback -> BeforeLoadReferenceCheck'
    print '*' * 50
    BeforeCreateReferenceCheck(message, function, clientData)


def AfterOpen(clientData):
    try:
        sceneName = maya.cmds.file(query=True, sceneName = True, shortName = True)
        
        if re.search(r'^xj_', sceneName, re.IGNORECASE):
            tiSceneOpenJob.xjcs()
    except:
        pass



def BeforeImport(retCode, file, clientData):
    ctypes.cast(long(retCode), ctypes.POINTER(ctypes.c_ubyte)).contents.value = True
    path = file.expandedFullName()
    print 'BeforeImport'


def BeforeSave(clientData):
    print 'BeforeSave'

def AfterSave(clientData):
    # maya.cmds.idmtService("StartTask", "%s|%s" % (maya.OpenMaya.MFileIO.currentFile(), os.getenv('USERNAME')))
    print 'AfterSave'