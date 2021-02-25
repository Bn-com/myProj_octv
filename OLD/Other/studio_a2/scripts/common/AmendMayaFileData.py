#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''    
__author__ = 'zhangben'
__mtime__ = '2017/11/8:16:14'
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
"""

import re, os
import maya.cmds as mc
import pymel.core as pm
import tempfile
class AmendMayaFileData(object):
    def __init__(self):
        print ("Start AmendMayaFileData Class Program!!!!!")
        self.scene_name_sht = mc.file(q=1,sn=1)
    @staticmethod
    def disposeAndSaveAs(saveAsNewDir=None,**modePair):
        print ("---------------------start save as new file-----------------------")
        fileFullPath = new_path_full = pm.sceneName()
        file_sn = file_n_sn = fileFullPath.basename()
        file_path = new_path = fileFullPath.abspath().splitpath()[0]
        if modePair:
            p_mode = re.compile(modePair.keys()[0])
            file_n_sn = p_mode.sub(modePair.values()[0],file_sn)
        if saveAsNewDir:
            new_path = saveAsNewDir
        else:
            new_path = os.path.abspath(os.path.join(file_path,'AmendMayaFileSaved'))
        if not os.path.isdir(new_path):os.makedirs(new_path)
        new_path_full = os.path.abspath(os.path.join(new_path,file_n_sn))
        print("Process Will save file to {}".format(new_path_full))
        my_v = int(re.search('\d+',pm.about(v=True,q=True)).group())
        print("============Maya Version is {:d}".format(my_v))
        if my_v == 2014:
            sys_temp_path = tempfile.gettempdir()
            temp_path_full = os.path.abspath(os.path.join(sys_temp_path,file_n_sn))
            pm.saveAs(temp_path_full,f=True)
            import idmt.maya.unknownPlugin as rup
            rup.RemoveUnknownPluginMb(temp_path_full,new_path_full)
            print ("Prevent Unknown Plugins and saved File {}".format(new_path_full))
        elif my_v > 2014 :
            unkplgs = pm.unknownPlugin(list=True,q=True)
            availabel_plg_lst = ['mtoa','pgYetiVRayMaya','xgenMR']
            for each_plg in unkplgs:
                if each_plg not in availabel_plg_lst:pm.unknownPlugin(each_plg,r=True)
            pm.saveAs(new_path_full,f=True)
            pm.saveFile()
            print ("Prevent Unknown Plugins and saved File {}".format(new_path_full))
        print("File Saved {}".format(new_path_full))
    def amend_ref_path(self,**subPair):
        all_refs = pm.listReferences()
        for each in all_refs:
            ori_path = str(each.path)
            p_sub = re.compile(subPair.keys()[0])
            if not p_sub.search(ori_path): continue
            rep_ref_infomations = self.generate_new_ref_info(each,**subPair)
            print rep_ref_infomations
            self.MyReplaceReferenceAndFixNameSapce(ori_path,rep_ref_infomations.keys()[0],rep_ref_infomations.values()[0])
        print ("amend reference path DONE!!!!!!")
    @staticmethod
    def generate_new_ref_info(each_ref,**sub_pair):
            old_path = each_ref.path
            new_path = old_path
            for each_sub_source in sub_pair:
                p_key = re.compile(each_sub_source)
                new_path = p_key.sub(sub_pair.get(each_sub_source),new_path)
            ref_new_name = '_'.join(os.path.basename(new_path).split('_')[:2])
            return {ref_new_name:new_path}
    @staticmethod
    def MyReplaceReferenceAndFixNameSapce(r,new_name,new_reference):
    #    1.    替换参考
            rfn = mc.file( r , q=1 , rfn = 1)                                     #    求rfn节点的名字
            if os.path.exists(new_reference):                                     #    这个文件前期还没出完，所以要判断一下。也有可能这个目标文件根本不存在
                mc.file(new_reference , loadReference = rfn )
            else:
                print("!!!!!!!!!!!!!!The file DO NOT EXIST!!!!!!!!!!!!::{}".format(new_reference))
                return None
    #    2.    修正namespace
            mc.namespace(setNamespace =":")
            for i in range(100):
                ns = new_name+"_" + str(i)
                #print "test ++++++++++++++++++++++++++++new_nameSpace:{}".format(ns)
                if mc.namespace(exists=ns):    continue
                else:
                    print "+++++++++++++++new namespace is :{}".format(ns)
                    newR = mc.referenceQuery(rfn,filename = 1)
                    mc.file(newR , edit=1 , namespace = ns )

                    mc.lockNode( rfn , lock =0, )                                                       #    解锁
                    newRFN = new_name + "_" + str(i) + "RN"                                    #    新rfn名字
                    if mc.objExists(newRFN) :   newRFN+= "1"                                 #    判断如果存在这个名字，自动在后面加“1”
                    if mc.objExists(newRFN) :   newRFN+= "1"                                 #    重复上面的操作，确保万无一失
                    mc.rename( rfn , newRFN)                                                           #   重命名
                    mc.lockNode(newRFN,lock=1, )                                                  #   上锁

                    break
            mc.namespace(setNamespace =":")
            return True
    @staticmethod
    def modify_line(sourceStr,**sub_pair):
        new_path = sourceStr
        for each_sub_source in sub_pair:
            #each_sub_source = "/E0011/"
            p_key = re.compile(each_sub_source)
            new_path = p_key.sub(sub_pair.get(each_sub_source),new_path)
        return new_path




# def zb_modify_mafile_refpath(dir,out_dir,**subPair):
#     collectFiles = []
#     for root,dirs,files in os.walk(dir):
#         for each_f in files:
#             if os.path.splitext(each_f)[1] == '.ma':collectFiles.append(os.path.join(root,each_f))
#     for each in collectFiles:
#         print "ok"
#
    def re_write_file(self,sourceFile,out_dir,**subPair):
        #new_path_full = sourceFile
        file_n_sn = os.path.basename(sourceFile)
        file_path = new_path = os.path.abspath(os.path.split(sourceFile)[0])
        if out_dir:
            new_path = out_dir
        else:
            new_path = os.path.abspath(os.path.join(file_path,'AmendMayaFileSaved'))
        if not os.path.isdir(new_path):os.makedirs(new_path)
        new_path_full = os.path.abspath(os.path.join(new_path,file_n_sn))
        f_rw = open(new_path_full,'w')
        print('============Now,start re_write file=======================')
        print("read data from file {}".format(sourceFile))
        with open(sourceFile,'r') as f_r:
            for each in f_r:
                if each.startswith("file -rdi 1") or each.strip().startswith("\"//file-cluster/GDC/") or each.startswith("file -r -ns"):
                    #print each
                    #print "============"
                    #print modify_line(each,**{"Projects/Ninjago/Project":"Projects/XYJ/Project","master/nj_":"master/Xyj_"})
                    f_rw.write(self.modify_line(each,**subPair))
                else:
                    f_rw.write(each)
            f_r.close()
            f_rw.close()
        print("Saved new file ---->:{}".format(new_path_full))
    @staticmethod
    def modify_line(sourceStr,**sub_pair):
        new_path = sourceStr
        for each_sub_source in sub_pair:
            #each_sub_source = "/E0011/"
            p_key = re.compile(each_sub_source)
            new_path = p_key.sub(sub_pair.get(each_sub_source),new_path)
        return new_path
    @staticmethod
    def fixRefNameSpace(ref_keyChar):
        link_desc = {'c':'chr','p':'prp','s':'scn'}
        #ref_keyChar = "mk_cBullKingBNew_h_ms_anim"
        allRefs = pm.listReferences()
        for eachRef in allRefs:
            pm.namespace(setNamespace = ':')
            p_refKey = re.compile(ref_keyChar)
            ref_path = eachRef.path
            if p_refKey.search(ref_path.strip()):
                newNs_base = '_'.join(os.path.splitext(ref_path.basename())[0].split('_')[:3])
                for i in range(0,100):
                    newNs = i and '{}{:d}'.format(newNs_base,i) or newNs_base
                    if pm.namespace(exists=newNs):continue
                    eachRef._setNamespace(newNs)
                    refNode_name_lst = newNs_base.split('_')
                    refNode_name_lst_base = refNode_name_lst[1:-1]
                    asset_name = refNode_name_lst[1]
                    link_letter = link_desc[asset_name[0]]
                    asset_name_base = refNode_name_lst[1][1:]
                    refNode_name_lst_base[0] = asset_name_base
                    new_ref_nd  = []
                    new_ref_nd.append(refNode_name_lst[0])
                    new_ref_nd.append(link_letter)
                    new_ref_nd.extend(refNode_name_lst_base)
                    new_ref_nd_name = '_'.join(new_ref_nd)
                    new_ref_nd_name += 'RN'
                    for i in range(0,100):
                        new_ref_nd_name_fn = i and '{}{:d}'.format(new_ref_nd_name,i) or new_ref_nd_name
                        if pm.objExists(new_ref_nd_name_fn):continue
                        eachRef._refNode.unlock()
                        eachRef._refNode.rename(new_ref_nd_name_fn)
                        eachRef._refNode.lock()
                        break
                    break
