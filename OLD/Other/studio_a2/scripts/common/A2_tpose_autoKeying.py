#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''    
__author__ = 'dell'
__mtime__ = '2017/9/19:0:39'
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
'''

import pymel.core as pm
import os,re

class A2_tpose_autoKeying(object):# aotu keying t-pose at 51 frames befor start time on time line
    def __init__(self,proj_name = u'MonkeyKing'):
        self.proj_name = proj_name
        self.Tpose_char_list_path = ur'\\file-cluster\gdc\Projects\{0}\{0}_Scratch\TD\TPose_char_list'.format(self.proj_name)
    def WriteChrCtrls2File(self):#record character rigging controls to server
        #proj_name = u'MonkeyKing'
        #Tpose_char_list_path = u'E:\Shunliu\ohter\Tpose_chars_list'
        if not os.path.isdir(self.Tpose_char_list_path):os.makedirs(self.Tpose_char_list_path)
        sel_ctrls = pm.selected()
        chr_ctrls_dic = {}
        for each_ctr in sel_ctrls:
            char_name_str = ''
            if each_ctr.isReferenced(): char_name_str = '_'.join(each_ctr.referenceFile().path.splitpath()[1].split('_')[:2])
            elif each_ctr.namespace():
                chr_nsp = each_ctr.namespace()
                p_valid_name = re.compile('[\D]+')
                char_name_str = p_valid_name.search(chr_nsp).group()
            else: char_name_str = '_'.join(pm.sceneName().namebase.split('_')[:2])
            if  char_name_str in chr_ctrls_dic:chr_ctrls_dic[char_name_str].append(each_ctr.stripNamespace().nodeName())
            else:chr_ctrls_dic[char_name_str] = [each_ctr.stripNamespace().nodeName()]
            print char_name_str
        for each_chr in chr_ctrls_dic:
            record_file = os.path.join('{}'.format(self.Tpose_char_list_path),'{}.txt'.format(each_chr))
            print record_file
            f = open(record_file,'w')
            for each_ctrl in chr_ctrls_dic[each_chr]:
                f.write(u'{}{}'.format(each_ctrl,os.linesep))
            f.close()
        print "export tpose relatives controls to server!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    def via_ref_aotuKeying_tpose(self,stfrm='file'):# auto keying tpose via refecrence list
        chr_name_lst = os.listdir(self.Tpose_char_list_path)
        chr_name_lst_pack = ['({})'.format(n.split('.')[0]) for n in chr_name_lst]
        chr_name_lst2Str = '|'.join(chr_name_lst_pack)
        p_chrNm = re.compile(chr_name_lst2Str)
        get_all_refs = pm.listReferences()
        for each_ref in get_all_refs:
            if p_chrNm.search(each_ref.path):
                rd_file_name = os.path.join(self.Tpose_char_list_path,'{}.txt'.format(p_chrNm.search(each_ref.path).group()))
                get_ctrls_list = []
                with open(rd_file_name) as f:
                    get_ctrls_list.extend(['{}:{}'.format(each_ref.namespace,m.strip(os.linesep)) for m in f.readlines()])
                self.aotu_tpose_keying(get_ctrls_list,stfrm)
    @staticmethod
    def aotu_tpose_keying(ctrls_list,stfrm = 'file'):#  keying controls at special frame
        if stfrm == 'file':
            stfrm = pm.playbackOptions(min=True,q=True)
        hold_frm = stfrm - 21
        tpose_frm = stfrm - 51
        for each_ctrl in ctrls_list :
            if not pm.PyNode(each_ctrl).exists():  continue
            key_attrs = ['tx','ty','tz','rx','ry','rz']
            special_attrs = ['Twist','FootRoll','BallRoll','ToeRoll']
            key_attrs.extend(special_attrs)
            each_ctrl_ls = pm.ls(each_ctrl,r=True)
            answer = ''
            if len(each_ctrl_ls) !=1:
                answer = pm.confirmDialog(button=['Go On','CheckAgain'],message='More Than One Object matches name: {}'.format(each_ctrl))
            if answer == 'CheckAgain':return None
            for each_ctrl_2 in each_ctrl_ls:
                cons_collection = ['parentConstraint','orientConstraint','pointConstraint']
                con_obj_ls = each_ctrl_2.listConnections(s=True,d=False)
                con_obj_ls_simplify = [con_obj_ls[n] for n in range(len(con_obj_ls)) if con_obj_ls[n] not in con_obj_ls[:n] and con_obj_ls[n].nodeType() in cons_collection]
                for each_attr in key_attrs:
                    if not each_ctrl_2.hasAttr(each_attr):continue
                    elif each_attr in special_attrs:
                        print("==========={} Attribute {} Will be set Tpose keyframe===============".format(each_ctrl_2,each_attr))
                    attr_full = each_ctrl_2.attr(each_attr)
                    if attr_full.isKeyable():
                        get_stfrm_v = attr_full.get(time=stfrm)
                        if not pm.keyframe(attr_full,time =(stfrm,stfrm),q=True):
                            attr_full.setKey(v = get_stfrm_v,time = stfrm,itt='flat',ott='flat')
                        if not pm.keyframe(attr_full,time =(hold_frm,hold_frm),q=True):
                            attr_full.setKey(v=get_stfrm_v,time = hold_frm,itt='flat',ott='flat')
                        if not pm.keyframe(attr_full,time =(tpose_frm,tpose_frm),q=True):
                            attr_full.setKey(v=0,time=tpose_frm,itt='flat',ott='flat')
                if con_obj_ls_simplify:
                    new_input_node = each_ctrl_2.listConnections(s=True,d=False)
                    new_input_node_simplity = [new_input_node[n] for n in range(len(new_input_node)) if new_input_node[n] not in new_input_node[:n] and new_input_node[n].nodeType()=='pairBlend']
                    for each_blend in new_input_node_simplity:
                        blendWeight_ctrl_attr = each_blend.weight.listConnections(d=True,p=True)[0]
                        if not pm.keyframe(blendWeight_ctrl_attr,time =(stfrm,stfrm),q=True):
                            blendWeight_ctrl_attr.setKey(v = 1,time = stfrm,itt='flat',ott='flat')
                        if not pm.keyframe(blendWeight_ctrl_attr,time =(hold_frm,hold_frm),q=True):
                            blendWeight_ctrl_attr.setKey(v=1,time = hold_frm,itt = 'flat',ott='flat')
                        if not pm.keyframe(blendWeight_ctrl_attr,time =(tpose_frm,tpose_frm),q=True):
                            blendWeight_ctrl_attr.setKey(v=0,time = tpose_frm,itt='auto',ott='auto')