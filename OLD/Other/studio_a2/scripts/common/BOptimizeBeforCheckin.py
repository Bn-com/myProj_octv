#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''    
__author__ = 'zhangben'
__mtime__ = '2017/9/29:11:07'
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
'''

import os
import pymel.core as pm
import maya.cmds as mc
import tempfile
class BOptimizeBeforCheckin(object):
    def __init__(self):
        self.fName_full = pm.sceneName()
    @staticmethod
    def remove_unk_plgs(save=True,*availabel_plg_lst):
        all_unk_plgs = pm.unknownPlugin(list=True,q=True)
        if not all_unk_plgs == 0:return
        for each_unk_plg in all_unk_plgs:
            if each_unk_plg not in availabel_plg_lst:
                pm.unknownPlugin(each_unk_plg,r=True)
                print ("Unknown Plugin {} Removed!!!!!!".format(each_unk_plg))
        if save:pm.saveFile(force=True)
    def remove_unk_plgs_my14(self,maAlterType=False):
        proj_wksp = os.path.abspath(pm.workspace.getPath())
        sys_temp_path = tempfile.gettempdir()
        target_dir = ''
        if proj_wksp.startswith(ur'\\file-cluster\GDC') or proj_wksp == pm.internalVar(uwd=True):
            target_dir = ur'D:\temp_info\removed_plugins'
        else:
            target_dir = ur'{}\scenes\romved_plugins'.format(proj_wksp)
        if maAlterType:target_dir = sys_temp_path
        if not os.path.isdir(target_dir):os.makedirs(target_dir)
        myFile_type = mc.file(type=True,q=True)
        source_file = self.fName_full
        if  myFile_type == [u'mayaAscii']:
            fName_sht =  '{}.mb'.format(os.path.splitext(source_file.basename())[0])
            tempFile = os.path.join(sys_temp_path,fName_sht)
            pm.renameFile(tempFile)
            pm.saveFile(force=True,type='mayaBinary')
            source_file = pm.sceneName()
            fName_full_amended = os.path.join(target_dir,source_file.basename())
            import idmt.maya.unknownPlugin as rup
            rup.RemoveUnknownPluginMb(source_file,fName_full_amended)
            print("===================Removed Unknown Plugins Succeed and save file {}".format(fName_full_amended))
            if maAlterType:
                pm.openFile(fName_full_amended,loadReferenceDepth = 'none',force=True)
                fn_mb = u'{}.ma'.format(os.path.splitext(fName_full_amended)[0])
                unks = pm.ls(type='unknown')
                if unks:
                    for each_unk in pm.ls(type='unkonwn'):
                        each_unk.unlock()
                        pm.delete(each_unk)
                pm.renameFile(fn_mb)
                pm.saveFile(force=True,type = 'mayaAscii')
        else:
            pm.openFile(source_file)
    @staticmethod
    def prevent_unkPlgs_14(sourceDir,targetDir):#remove 指定目录下的2014 版本 mb文件里的unknown plugins 节点，输出到另外目录
        import idmt.maya.unknownPlugin as rup
        for eachFile in os.listdir(sourceDir):
            sourceFile_full = os.path.abspath(os.path.join(sourceDir,eachFile))
            targetFIle_full = os.path.abspath(os.path.join(targetDir,eachFile))
            rup.RemoveUnknownPluginMb(sourceFile_full,targetFIle_full)