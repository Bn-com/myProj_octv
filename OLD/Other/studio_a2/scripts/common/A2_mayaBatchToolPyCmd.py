#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''    
__author__ = 'zhangben'
__mtime__ = '2017/11/9:11:42'
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
"""
import Other.studio_a2.scripts.common.AmendMayaFileData as amfd
reload( amfd)
import sys

class A2_mayaBatchToolsPyCmd(object):
    def __init__(self):
        print("Start -----------StudioA2 MayaBatch Tools Cammand Set")
    @staticmethod
    def proj_mk_amend_ref():
        subPair = {u'cBullKingB/master/mk_cBullKingB_h_ms_anim.mb':u'cBullKingBNew/master/mk_cBullKingBNew_h_ms_anim.mb'}
        batch_svae_dir = ur'D:/temp_info/AmendMayaFileSaved'
        modePair = {'_an_':'_sa_'}
        ins_main = amfd.AmendMayaFileData()
        ins_main.amend_ref_path(**subPair)
        ins_main.disposeAndSaveAs(saveAsNewDir = batch_svae_dir,**modePair)
    @staticmethod
    def proj_mk_amend_ma_ref(sourcePath=None):
        if not sourcePath:sourcePath = sys.argv[1]
        subPair = {u'cBullKingB/master/mk_cBullKingB_h_ms_anim.mb':u'cBullKingBNew/master/mk_cBullKingBNew_h_ms_anim.mb'}
        out_dir = ur'D:/temp_info/AmendMayaFileSaved'
        ins_main = amfd.AmendMayaFileData()
        ins_main.re_write_file(sourcePath,out_dir,**subPair)

