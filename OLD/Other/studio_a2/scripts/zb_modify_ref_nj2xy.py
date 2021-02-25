#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'zhangben'
__mtime__ = '2017/8/1:15:56'
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
'''
import re, os, sys
import maya.cmds as mc
import maya.mel as mel
import pymel.core as pm
def modify_ref_dir(stor_path = os.path.abspath(ur'D:/temp_info/a2_rnmRef_nj2xy'),saveToggle=True,**sub_pair):
    """
    修改参考路径  由nj 2  yxj
    """
    sub_pair = {"/nj_":"/Xyj_","/Ninjago/":"/XYJ/","\.ma":".mb"}
    if not os.path.isdir(stor_path):os.makedirs(stor_path)
    ref_list = pm.listReferences()
    for each_frf in ref_list:
        modify_refNode_dir(each_frf,**sub_pair)
    fn_read = mc.file(shn=True,q=True,sn=True)
    p_prf_key = re.compile("^nj_")
    fn_new = p_prf_key.sub('xyj_',fn_read)
    fn_new_full = os.path.join(stor_path,fn_new)
    if saveToggle:
        mc.file(rn=fn_new_full)
        pm.saveFile()
def modify_refNode_dir(each_frf,**sub_pair):
    #sub_pair = {"/nj_":"/Xyj_","/Ninjago/":"/XYJ/","\.ma":".mb"}
    #==============modify reference path================
    #each_frf = ref_list[0]
    old_path = each_frf.path
    new_path = old_path
    for each_sub_source in sub_pair:
        p_key = re.compile(each_sub_source)
        new_path = p_key.sub(sub_pair.get(each_sub_source),new_path)
    if os.path.isfile(new_path) and new_path != old_path:
        try:
            print("======================Start modify reference file {} path:".format(os.path.split(new_path)[1]))
            each_frf.replaceWith(new_path)
            print("Replace reference 2 new path success!!!!!\n{:>=150}".format(new_path))
        except:
            print("!!!!!There occured some issue,maybe THE ASSET FILE USED DIFFRENT VERSION MAYA!!!!!")
    else:
        print("{0:+>150} asset file didn't checkin\n {1}:::{1}:::{1}:::{1}".format(new_path,'PLEASE CHECK'))
        raise
        #continue
    #==============rename namespace======================
    #pm.PyNode(each_frf)
    each_frf._setNamespace(each_frf.namespace.replace("nj_","Xyj_"))
    #===========rename referencNode====================
    refnd = each_frf.refNode
    refnd.unlock()
    refnd_nm = refnd.name()
    each_frf.refNode.rename(refnd_nm.replace("nj_","Xyj_"))
    refnd.lock()
def generate_new_ref_info(each_ref,**sub_pair):
    old_path = each_ref.path
    new_path = old_path
    for each_sub_source in sub_pair:
        p_key = re.compile(each_sub_source)
        new_path = p_key.sub(sub_pair.get(each_sub_source),new_path)
#modify_ref_dir(**{"/nj_":"/Xyj_","/Ninjago/":"/XYJ/"})