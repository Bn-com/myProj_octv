#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''    
__author__ = 'zhangben'
__mtime__ = '2017/8/7:16:08'
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
'''

import sys
import os
import re
import maya.cmds as mc
import maya.mel as mel
import pymel.core as pm

def zb_modify_mafile_refpath(dir,out_dir,**subPair):
    collectFiles = []
    for root,dirs,files in os.walk(dir):
        for each_f in files:
            if os.path.splitext(each_f)[1] == '.ma':collectFiles.append(os.path.join(root,each_f))
    for each in collectFiles:
        print "ok"
        
def re_write_file(sourceFile,out_dir,**subPair):
    # sourceFile = collectFiles [1]
    #fn = os.path.split(sourceFile)[1].replace('nj_','Xyj_')
    sourceFile = "e:/nj_E0003_Q0020_S0010_an_001.ma"
    if not os.path.isdir(out_dir):os.makedirs(out_dir)
    fn = os.path.split(sourceFile)[1]
    fn_full = os.path.join(os.path.abspath(out_dir),fn)
    f_rw = open(fn_full,'w')
    print('============Now,start re_write file=======================')
    with open(sourceFile,'r') as f_r:
        for each in f_r:
            if each.startswith("file -rdi 1") or each.strip().startswith("\"//file-cluster/GDC/") or each.startswith("file -r -ns"): 
                #print each
                #print "============"
                #print modify_line(each,**{"Projects/Ninjago/Project":"Projects/XYJ/Project","master/nj_":"master/Xyj_"})
                f_rw.write(modify_line(each,**{"Projects/Ninjago/Project":"Projects/XYJ/Project","master/nj_":"master/Xyj_","\.ma":".mb"}))
            else:
                f_rw.write(each)
        f_r.close()
        f_rw.close()    
    

def modify_line(sourceStr,**sub_pair):
    new_path = sourceStr
    for each_sub_source in sub_pair:
        #each_sub_source = "/E0011/"
        p_key = re.compile(each_sub_source)
        new_path = p_key.sub(sub_pair.get(each_sub_source),new_path)
    return new_path

if __name__ == "__main__":
    dir = ur"Z:\Resource\Groups\Studio_FantasyImage\Scratch\Teapot\Animation_T1"
    out_dir = ur'D:/temp_info/a2_rnmRef_nj2xy'
    zb_modify_mafile_refpath(dir,out_dir)