#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = OCT_ExchangeProxy_v1
__author__ = zhangben
__mtime__ = 2019/3/15 : 10:45
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
"""
# Python code
import maya.cmds as mc
import maya.OpenMaya as om
import pymel.core as pm
import sys, re, os
import json
import shutil
import time
import copy
from stat import ST_ATIME, ST_CTIME, ST_MTIME
import subprocess


class OCT_ExchangeProxy(object):
    """
    大的场景，很多代理在布置场景的时候用的instance 的方式，之前的代理替换工具对于关联复制的代理物体替换存在位置不能正确匹配的情况
    重写
    """

    def __init__(self):
        self.keywd2dir = {'AR': 'arnoldtex', 'VR': 'Vray_DL', '.ass': 'arnoldtex', '.vrmesh': 'Vray_DL', 'AR_MOD': 'scenes', 'VR_MOD': 'scenes',
                          'MOD': 'scenes'}  # via key words get proxy file store folder name
        self.prx_file_attr = {'aiStandIn': 'dso', 'VRayMesh': 'fileName', 'AR': 'dso', 'VR': 'fileName'}  # each type proxy node has different attribute name
        self.prx_type_abbr = {'vrmesh': 'VR', 'ass': 'AR', 'aiStandIn': 'AR', 'VRayMesh': 'VR'}  # various key words symbol as a acronym word
        self.prx_need_assign = {'VR': ['.vrmesh', 'VRayMesh', 'fileName', 'VRay', 'mesh'], 'AR': ['.ass', 'aiStandIn', 'dso', 'Arnold', 'aiStandIn'],
                                'VR_MOD': ['.jpg', 'file', 'fileName', 'Model', 'mesh'], 'AR_MOD': ['.jpg', 'file', 'fileName', 'Model', 'mesh'],
                                '_MOD': ['.jpg', 'file', 'fileName', 'Model', 'mesh']}

        self.prx_ext_dic = {'AR': '.ass', 'aiStandIn': '.ass', 'VR': '.vrmesh', 'VRayMesh': '.vrmesh', 'AR_MOD': '_AR.mb', 'VR_MOD': '_VR.mb', 'MOD': '_MOD.mb'}
        self.prx_f_ext_dic = {'AR': '.ass', 'aiStandIn': '.ass', '_VR.ma': '.vrmesh', 'VRayMesh': '.vrmesh'}
        self.prx_im_f_ext_dic = {'AR': '_AR.ass', 'aiStandIn': '_AR.ass', 'VR': '_VR.ma', 'VRayMesh': '_VR.ma', 'MOD': '_MOD.mb', 'AR_MOD': '_AR.mb',
                                 'VR_MOD': '_VR.mb'}
        self.im_f_t = {'AR': 'ASS', 'VR': 'mayaAscii', 'MOD': 'mayaBinary', 'AR_MOD': 'mayaBinary', 'VR_MOD': 'mayaBinary'}

        self.prx_serv_dir = r"\\octvision.com\CG\Resource\Material_Library\Proxy\ProxySeed"

        self.path_spl_ch = {'AR': '\\', 'VR': '/', 'aiStandIn': '\\', 'VRayMesh': '/', '.ass': '\\', '.vrmesh': '/', 'MOD': '\\', 'VR_MOD': '\\',
                            'AR_MOD': '\\'}
        self.needCopy_ext = ['', '.ass', '.vrmesh', '.jpg']
        self.nowayEx = []
        self.cur_prj = pm.workspace.name

    def getInstances(self):  # get all instance shape node list
        instances = []
        iterDag = om.MItDag(om.MItDag.kBreadthFirst)
        while not iterDag.isDone():
            instanced = om.MItDag.isInstanced(iterDag)
            if instanced:
                inst_fnm = iterDag.fullPathName()
                instances.append(pm.PyNode(inst_fnm))
            iterDag.next()
        return instances

    def uninstance(self):
        instances = self.getInstances()
        while len(instances):
            parent = mc.listRelatives(instances[0], parent=True)[0]
            mc.duplicate(parent, renameChildren=True)
            mc.delete(parent)
            instances = self.getInstances()

    def imp_all_prxs(self, need_prxs_date, trg_type):
        im_prxs_dict = {}
        for ea_prx in need_prxs_date:
            # ea_prx = need_prxs_date.
            # fileAttr = ea_prx.attr(self.prx_file_attr[ea_prx.type()]).get()

            # 当前代理 信息
            prx_f_bsnm = os.path.splitext(ea_prx)[0]
            prx_f_bsnm_nornder = re.sub('(_AR|_VR)', '', prx_f_bsnm)
            src_type = re.search('(_AR|_VR)', prx_f_bsnm).group().strip("_")
            src_file_ext = os.path.splitext(ea_prx)[-1]

            current_prx_servDir = need_prxs_date[ea_prx]
            curr_prx_servDir_split = current_prx_servDir.split(self.path_spl_ch[src_file_ext])
            folder_indx = curr_prx_servDir_split.index(self.keywd2dir[src_file_ext])

            # 代理工程路径
            prx_proj_pth = self.path_spl_ch[src_file_ext].join(curr_prx_servDir_split[:folder_indx - 1])
            # 存放当前代理的 上层路径
            above_folder = self.path_spl_ch[src_file_ext].join(curr_prx_servDir_split[:folder_indx])
            # 替换的文件 信息
            targ_above_folder = above_folder
            if re.search('MOD', trg_type):
                targ_above_folder = prx_proj_pth
            targ_prx_dir = '{}{}{}'.format(targ_above_folder, self.path_spl_ch[src_file_ext], self.keywd2dir[trg_type])
            sub_str = re.sub('_MOD', '_{}'.format(src_type), self.prx_im_f_ext_dic[trg_type])
            targ_imf_nm = re.sub(self.prx_im_f_ext_dic[src_type], sub_str, ea_prx)

            # 导入的文件 需要copy的文件
            imf_pth_full = '{}{}{}'.format(targ_prx_dir, self.path_spl_ch[src_file_ext], targ_imf_nm)
            sub_str_2 = re.sub('scenes', '{}_txt'.format(prx_f_bsnm_nornder), self.keywd2dir[trg_type])

            need_cp_src = [os.path.abspath("{}{}/sourceimages/{}".format(prx_proj_pth, self.path_spl_ch[trg_type], sub_str_2))]
            move2Dir = os.path.abspath(os.path.join(self.cur_prj, 'sourceimages'))
            move2Dir_sub = os.path.abspath(os.path.join(move2Dir, sub_str_2))
            if trg_type in ['VR']:
                need_cp_src.append(os.path.abspath("{}{}/sourceimages/{}_txt".format(prx_proj_pth, self.path_spl_ch[trg_type], prx_f_bsnm_nornder)))
            lst_needCp = self.listNeedCopy(need_cp_src)
            need_info = self.doCopy(lst_needCp, trg_type)
            im_prxs_dict[ea_prx] = self.import_Prx(imf_pth_full, prx_f_bsnm_nornder, trg_type, need_info)
        return im_prxs_dict

    # import relative proxy file
    def import_Prx(self, imf_pth_full, prx_f_bsnm_nornder, trg_type, infoDcit):
        # infoDcit = need_info
        im_ns = 'RepPrx_{}'.format(prx_f_bsnm_nornder)
        mc.file(imf_pth_full, i=True, type=self.im_f_t[trg_type], ra=True, ns=im_ns, pr=True, mergeNamespacesOnClash=False, options="v=0",
                loadReferenceDepth="all")
        im_grp = pm.ls("{}*:*".format(im_ns))
        # cleanUp_Namespace(im_ns)
        # pm.namespaceInfo(
        im_grp_dict = {}
        for ea_im in im_grp:  # ea_im = im_grp[5]
            if ea_im.type() == self.prx_need_assign[trg_type][1]:
                # print im_grp.index(ea_im)
                modify_attr = ea_im.attr(self.prx_file_attr[trg_type])
                new_attr = [ea_v[1] for ea_v in infoDcit.values() if
                            re.match(unicode(re.sub(r'\\', self.path_spl_ch[trg_type], ea_v[0])), modify_attr.get(), re.I)]
                if not len(new_attr):
                    self.nowayEx.append(prx_f_bsnm_nornder)
                    continue
                modify_attr.set(unicode(re.sub(r'\\', self.path_spl_ch[trg_type], new_attr[0])))
                print("{} proxy file imported, and the node :{} attribute has modified".format(self.prx_need_assign[trg_type][3], ea_im.name()))
            elif ea_im.type() == self.prx_need_assign[trg_type][4]:
                im_grp_dict['needRep'] = ea_im
            elif ea_im.type() == 'transform':
                im_grp_dict['trans'] = ea_im
            nnm = ea_im.stripNamespace().strip()
            self.renameIt(ea_im, "{}_".format(nnm))
            # ea_im.rename("{}_".format(nnm))
        im_grp_dict['dags'] = im_grp
        self.cleanUp_Namespace(im_ns)
        return im_grp_dict





    def list_prxys_dict(self, prxy_lst):  # 返回一个字典 key ：代理文件名字 value  代理文件路径
        resDic = {}
        for ea in prxy_lst:
            attr = ea.attr(self.prx_file_attr[ea.type()]).get()
            if not os.path.isfile(attr):
                self.nowayEx.append(ea)
                continue
            px_f_nm = os.path.split(attr)[-1]
            # px_f_nm_bs = os.path.splitext(px_f_nm)[0]
            if px_f_nm in resDic:
                resDic[px_f_nm].append(ea)
            else:
                resDic[px_f_nm] = [ea]
        return resDic

    def cleanUp_Namespace(self, match_NSChar):
        mc.namespace(set=":")
        allNamespaces = mc.namespaceInfo(listOnlyNamespaces=True)
        p = re.compile(match_NSChar)

        idleNamespace = [allNamespaces[i] for i in range(len(allNamespaces)) if len(p.findall(allNamespaces[i])) != 0]
        for eachINS in idleNamespace:
            self.remove_namespace(eachINS)
        return (mc.namespaceInfo(listOnlyNamespaces=True))

    def remove_namespace(self, removeNS):
        # removeNS = "rp_1"
        mc.namespace(set=removeNS)
        objsInNs = mc.namespaceInfo(listNamespace=True)
        mc.delete(objsInNs)
        mc.namespace(set=":")
        mc.namespace(removeNamespace=removeNS)
        # return(mc.namespaceInfo(listOnlyNamespaces=True))

    def doCopy(self, lst_needCp, trg_type):
        need_asign_msg = {}
        if len(lst_needCp['ncp']):
            for ea_itme in lst_needCp['ncp']:
                need_asign_msg[ea_itme] = lst_needCp['ncp'][ea_itme]
        if len(lst_needCp['cp']):
            for ea_ndcp in lst_needCp['cp']:
                if os.path.isdir(lst_needCp['cp'][ea_ndcp][0]) and not os.path.isdir(lst_needCp['cp'][ea_ndcp][1]): os.makedirs(lst_needCp['cp'][ea_ndcp][1])
                shutil.copy2(lst_needCp['cp'][ea_ndcp][0], lst_needCp['cp'][ea_ndcp][1])
                need_asign_msg[ea_ndcp] = lst_needCp['cp'][ea_ndcp]
            for each in need_asign_msg:
                if not re.search(self.prx_need_assign[trg_type][0], each): need_asign_msg.pop(each)
        return need_asign_msg

    def listNeedCopy(self, src_dir_s, copy_files={'cp': {}, 'ncp': {}}):
        # copy_fils = {}
        # src_dir = r"\\octvision.com\CG\Resource\Material_Library\Proxy\ProxySeed\Flowers\flower018\sourceimages\Vray_DL"
        # src_dir_s = need_cp_src
        for src_dir in src_dir_s:
            if not os.path.isdir(src_dir):
                self.nowayEx.append("++++There is no texture folder CHECK! == {}".format(src_dir))
                continue
            lst_dir = os.listdir(src_dir)
            for eaobj in lst_dir:
                # eaobj = lst_dir[-2]
                ext_str = os.path.splitext(eaobj)[-1]
                targ_folder = os.path.split(src_dir)[-1]
                move2Dir = os.path.abspath(os.path.join(self.cur_prj, 'sourceimages'))
                move2Dir_sub = os.path.abspath(os.path.join(move2Dir, targ_folder))
                if ext_str in self.needCopy_ext:
                    copy_pair = [os.path.join(src_dir, eaobj), os.path.join(move2Dir_sub, eaobj)]
                    copy_files['cp'][eaobj] = copy_pair
        cp_copy_fils = copy.deepcopy(copy_files)
        for ea_cp in cp_copy_fils['cp']:
            # targ_file_name_full = os.path.join(targ_dir, ea_cp)
            if os.path.isfile(cp_copy_fils['cp'][ea_cp][1]):
                src_tm = os.stat(cp_copy_fils['cp'][ea_cp][0]).st_mtime
                targ_tm = os.stat(cp_copy_fils['cp'][ea_cp][1]).st_mtime
                print "source file modified time is {}".format(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(src_tm)))
                print "target file modified time is {}".format(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(targ_tm)))
                if time.localtime(src_tm) == time.localtime(targ_tm):
                    copy_files['ncp'][ea_cp] = [cp_copy_fils['cp'][ea_cp][0], cp_copy_fils['cp'][ea_cp][1]]
                    copy_files['cp'].pop(ea_cp)
            elif os.path.isdir(cp_copy_fils['cp'][ea_cp][1]):
                src_dir_sub = (os.path.join(src_dir, ea_cp))
                self.listNeedCopy(src_dir_sub, cp_copy_fils['cp'][ea_cp][1], copy_files)
        return copy_files

    def get_prxs(self, proxyType='aiStandIn', selObj=None):  # get all specify proxy shape node list
        all_need_prxy = []
        if selObj != 'all':
            lst_prxy = pm.selected()
            for ea in lst_prxy:
                shpType = ea.getShape().type()
                if shpType == proxyType:
                    all_need_prxy.append(ea.getShape())
                elif shpType == 'mesh' and proxyType == 'VRayMesh':
                    im_attr = ea.getShape().attr('inMesh')
                    prx_nd = im_attr.listConnections(type=proxyType)
                    if not len(prx_nd):
                        self.nowayEx.append(ea.getShape())
                        continue
                    all_need_prxy.extend(prx_nd)
        else:
            lst_prxy = pm.ls(type=proxyType)
            list_inst = self.getInstances()
            all_need_prxy.extend([ea for ea in list_inst if ea.type() == proxyType])
            print(len(all_need_prxy))
            all_need_prxy.extend([ea for ea in lst_prxy if ea not in all_need_prxy])
            print(len(all_need_prxy))
        return all_need_prxy


    def renameIt(self,obj,newNm,cur_num=None):
        if not cur_num: cur_num = 0
        new_nm_str  = "{}{}".format(newNm,cur_num)
        new_nm_str = re.sub("_0$",'_',new_nm_str)
        if pm.objExists(new_nm_str):
            cur_num +=1
            self.renameIt(obj,newNm,cur_num)
        else:
            obj.rename(newNm)




    def nessesary_prxDcit(self,prx_dict):  # proxy name and proxy file on server path
        prxy_infor_dict = {}
        readData = None
        prxy_dict = {}
        prx_infor_js = r"{}\proxy_infor.json".format(self.prx_serv_dir)
        with open(prx_infor_js, 'r') as rf:
            prxy_infor_dict = json.load(rf)
        # print
        ea_shp_lst = []
        for ea_v in prx_dict.values():
            ea_shp_lst.extend(ea_v)
        for ea_inst in ea_shp_lst:
            prxSty = ea_inst.type()
            trxSty_acr = self.prx_type_abbr[prxSty]
            prxy_dir_used = ea_inst.attr(self.prx_file_attr[prxSty]).get()
            prx_nm = os.path.split(prxy_dir_used)[1]
            prx_dir_serv = ""
            if prx_nm in prxy_infor_dict[trxSty_acr] and prx_nm not in prxy_dict:
                prxy_dict[prx_nm] = prxy_infor_dict[trxSty_acr][prx_nm]
            elif prx_nm not in prxy_infor_dict[trxSty_acr]:
                if prx_nm not in prxy_dict:
                    for root, dir, files in os.walk(self.prx_serv_dir):
                        for eafile in files:
                            eafile_pth_f = os.path.join(root, eafile)
                            if re.search(prx_nm, eafile_pth_f):
                                prx_dir_serv = eafile_pth_f
                    prxy_dict[prx_nm] = prx_dir_serv
        return prxy_dict

    def ExchangeProxy(self, prx_type, trg_type, ifAll=None):
        sel_prxs_dict = self.list_prxys_dict(self.get_prxs(prx_type, ifAll))
        need_prxs_date = self.nessesary_prxDcit(sel_prxs_dict)
        # src_type = 'AR'
        # trg_type = 'VR'
        im_objs = self.imp_all_prxs(need_prxs_date, trg_type)
        for ea_prx_type in sel_prxs_dict:  # pass
            for eaPrxShp in sel_prxs_dict[ea_prx_type]:  # pass
                trns_nd = eaPrxShp.getParent()
                grp_nd = trns_nd.getParent()
                cp_prx_trn = ""
                if eaPrxShp.isInstanced():
                    cp_prx = pm.instance(im_objs[ea_prx_type]['needRep'])
                    cp_prx_trn = cp_prx[0]
                else:
                    cp_prx = pm.duplicate(im_objs[ea_prx_type]['needRep'], rr=True)
                    cp_prx_trn = cp_prx[0]
                if grp_nd:
                    cp_prx_trn.setParent(grp_nd)
                trns_nd.translate >> cp_prx_trn.translate
                pm.delete(trns_nd)

    # ========================= update json file ,the file record all proxy information date ===================================
    def parse_prxyDate(self, prx_serv_dir):  # find all proxy files on server
        self.prx_type_abbr = {'vrmesh': 'VR', 'ass': 'AR'}
        prx_data = {'VR': {}, 'AR': {}}
        for ea_ext in self.prx_type_abbr:
            for root, dir, files in os.walk(prx_serv_dir):
                for eafile in files:
                    re_serch = re.search(ea_ext, os.path.splitext(eafile)[-1])
                    if re_serch:
                        eafile_pth_f = os.path.join(root, eafile)
                        # print type(re_serch.group())
                        # raise Exception("td check")
                        # print eafile
                        if eafile not in prx_data[self.prx_type_abbr[re_serch.group()]]:
                            prx_data[self.prx_type_abbr[re_serch.group()]][eafile] = eafile_pth_f
        return prx_data

    def rec_prxInfo(self, dataDict, fileStorPath):  # write date to json file
        # wfpth = os.environ["TMP"]
        rec_file = os.path.join(fileStorPath, "proxy_infor.json")
        with open(rec_file, 'w') as f:
            f.write(json.dumps(dataDict, indent=4))

    def wr_prx_info_2_server(self, prx_serv_dir=r"\\octvision.com\CG\Resource\Material_Library\Proxy\ProxySeed"):  # do it
        self.rec_prxInfo(self.parse_prxyDate(prx_serv_dir), prx_serv_dir)

# if __name__ == "__main__":
# wr_prx_info_2_server()