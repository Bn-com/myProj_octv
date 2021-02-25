#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''    
__author__ = 'zhangben'
__mtime__ = '2016/7/14:15:26'
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
'''
import re, os, sys
import maya.cmds as mc
import maya.mel as mel
from pymel.core import *
def mi_batch_check_refAsset_presence(files_path):
    variable_chars = '$WOQB_PROJECT_PATH'
    variable_direct_path = u'//file-cluster/gdc/Projects/MiniTiger/Project/External/WOQB'
    for root,dirs,files in os.walk(files_path):
        for filepath in files:
            if os.path.splitext(filepath)[-1] == u'.ma':check_ma_refAsset(os.path.join(root,filepath),variable_chars,variable_direct_path)
def check_ma_refAsset(shotFilePath,variable_chars,variable_direct_path):
    """
    this function to check the asset file of the reference in the shot file is exists or not
    """
    star_chars = 'file -rdi 1 '
    p_valid_path_inLine = re.compile(u'[$A-Za-z0-9./_:]+')
    stor_all_ref_abcPath = []
    with open(shotFilePath) as read_file:
        rl = read_file.readlines()
        for ln,lineStr in enumerate(rl):
           if lineStr.startswith(star_chars):
               asset_ref_path_line = rl[ln+1]
               #print str(asset_ref_path_line)
               #valid_path_str = p_valid_path.search(asset_ref_path).group()
               asset_ref_path = p_valid_path_inLine.search(asset_ref_path_line) .group()
               p_variable = re.compile('\{}'.format(variable_chars))
               stor_all_ref_abcPath.append(p_variable.sub(variable_direct_path,asset_ref_path))
    troubleAsset = [each_asset for each_asset in stor_all_ref_abcPath if not os.path.exists(each_asset)]
    if troubleAsset:
        print u'{0:+>20}THE SHOT : {1} has unexists reference asset file \n'.format(u'',os.path.split(shotFilePath)[-1])
        for each_asset in troubleAsset:
            print u'{0:=>20}\n{1}\n{0:=>20}PLEASE CHECK THE FILE'.format(u'',each_asset)
if __name__ == "__main__":
    files_stor_path = ur'\\file-cluster\GDC\Projects\MiniTiger\Project\External\WOQB\MiniTiger\Project\scenes\Animation\episode_185\layout'
    #p_valid_path = re.compile(u'[^\"]*\S+')
    mi_batch_check_refAsset_presence(files_stor_path)