#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''    
__author__ = 'dell'
__mtime__ = '2017/9/28:1:02'
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
'''
import re, os, sys
import maya.cmds as mc
import maya.mel as mel
import pymel.core as pm
import tempfile
def handle_file_then_save(handle_proc):
    def _handle(self):
        fn_sht = pm.sceneName().basename()
        sys_temp_path = tempfile.gettempdir()
        fn_temp_full = os.path.join(sys_temp_path,fn_sht)
        handle_proc(self)
        pm.renameFile(fn_temp_full)
        print "now start save temporary file---------{}".format(fn_temp_full)
        try:
            pm.saveFile(force=True)
        except:
            Error("Save file 2 temporary failed!!!!!!!!!!")
        return fn_temp_full
    return _handle
class OptimizeBeforCheckin(object):
    def __init__(self):
        pass

    def remove_unk_plgs(self):
        fn_full = os.path.join(ur'{}\scenes'.format(os.path.abspath(pm.workspace.getPath())),pm.sceneName().basename())
        fn_temp_full = self.delete_fileNode()
        print "File saved 2 temporary path Succeed!!!"
        import idmt.maya.unknownPlugin as rup
        rup.RemoveUnknownPluginMb(fn_temp_full,fn_full)

    @handle_file_then_save
    def delete_fileNode(self):
        lst_fileNodes = pm.ls(type = 'file')
        if lst_fileNodes:pm.delete(lst_fileNodes)