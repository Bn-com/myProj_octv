#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''    
__author__ = 'zhangben'
__mtime__ = '2016/2/23'
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
'''


import re,os,sys
import maya.cmds as mc
import maya.mel as mel
from pymel.core import *


def mi_amend_abcpath_mainProc():
    sysTemp = os.environ['TEMP']
    logfile = u'%s/BatchProcLog.txt'%sysTemp
    storeFolde = sysTemp
    fileList = mi_get_lyfs()
    newOutProjDir = storeFolde
    scriptDir = internalVar(usd=True)
    script_stor_path = u'%s/mi_amend_abcPath_batch.py'%scriptDir
    sysFile(sss_path,delete=True)
    cfc_txfd = MelGlobals.get('gLastFocusedCommandControl')
    cmdScrollFieldExecuter(cfc_txfd, e=True, storeContents = script_stor_path)
    cmd_str_list = []
    batFile = u'%s\mi_amend_abcpath.bat'%(sysTemp)
    batf_op = open(batFile,'w')
    for eachFile in fileList:
        #eachFile = os.path.normpath(fileList[0])
        maya_loc = os.getenv("MAYA_LOCATION")
        m_b_dir = ur"%s/bin\mayabatch.exe"%maya_loc
        pythonCmdStr = u"\"python(\\\"import mi_amend_abcPath_batch as maab;maab.mi_save_amendedFile(ur\\\\\\\"abc_amend\\\\\\\")\\\");\""
        cmdStr = ur"%s -file %s -command %s -log %s%s" % (m_b_dir,eachFile,pythonCmdStr,logfile,os.linesep)   
        #cmdStr_nl = u'%s\r\n'%cmdStr
        #print cmdStr
        #resulContant = os.popen(cmdStr)    
        #os.system(cmdStr)
        batf_op.write(cmdStr)
        #print cmdStr
    batf_op.close()
    return batFile
def mi_get_lyfs():
    files_folder  = fileDialog2(fm=2)[0]
    p_fn = re.compile(u'mi_[0-9a-z]+_[0-9a-z]+_[\w]*_fs_[0-9a-z]+.mb')
    ly_files_ls = []
    for root,dirs,files in os.walk(files_folder):
        for filespath in files:
            if p_fn.search(filespath):
                ly_files_ls.append(os.path.normpath(os.path.join(root,filespath)))
    return ly_files_ls
def mi_save_amendedFile(storPath):
    fn = sceneName()
    shortName = os.path.split(fn)[-1]
    d_temp_folder = ur'd:\minitiger_tempSaveFile'
    stor_folder = os.path.join(d_temp_folder,storPath)
    if not os.path.isdir(stor_folder):os.makedirs(stor_folder)
    save_file_path_new = os.path.join(stor_folder,shortName)
    mi_amend_abcPath()
    mc.file(rn = save_file_path_new)
    saveFile()
    print u'File alembic cache node \'abc_File\' attribute modified!!!!!!'
    return save_file_path_new
def mi_amend_abcPath(amendDriver = u'z:/Projects'):
    abcNode = ls(type = u'AlembicNode')
    if abcNode:
        for each_abcnode in abcNode:
            abcFile_path = each_abcnode.attr(u'abc_File').get() #\\file-cluster\GDC
            #abcFile_path = abcNode[0].attr(u'abc_File').get() #\\file-cluster\GDC
            p_pathPrefix = re.compile(u'(//file-cluster/GDC/Projects)|(L:/Projects)',re.I)
            modify_path = p_pathPrefix.sub(amendDriver,abcFile_path)
            each_abcnode.attr(u'abc_File').set(modify_path)
            print u'node: %s  abc_file attribute modified value == %s' % (each_abcnode,modify_path)
if __name__ == "__main__":
    mi_amend_abcpath_mainProc()
    os.system(batFile)
    os.system(ur'start d:\minitiger_tempSaveFile\abc_amend')