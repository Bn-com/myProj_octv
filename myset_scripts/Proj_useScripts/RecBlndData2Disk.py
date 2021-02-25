#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = RecBlndData2Disk
__author__ = zhangben
__mtime__ = 2019/10/21 : 10:47
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
"""

import datetime
import json
import pymel.core as pm
import copy,re,os,sys


class RecDxyData2Disk(object):
    def __init__(self):
        # slider = sldgrp
        self.DaTm = datetime.datetime.now()
        # DaTm.__format__('%Y%m%d')
        # DaTm.strftime('%Y%m%d%H%M%S')
        self.proj_dir = pm.workspace.path
        self.dataStoreDir = '{}/data/dxyzRecordData'.format(self.proj_dir)
        self.scene_bsnm = pm.sceneName().basename().strip()
        self.dt_f_name = None
        if not self.scene_bsnm:
            self.dt_f_name = 'DxyzRecData_{}.json'.format(DaTm.strftime('%Y%m%d%H%M%S'))
        else:
            self.dt_f_name = "DxyzRecData_{}.json".format(self.scene_bsnm)
        self.dataFile = "{}/{}".format(self.dataStoreDir, self.dt_f_name)
        self.rec_indx = 0
        self.rec_dict = {}
        self.read_dict = None
        self.read_indx = 0

    def obtainData(self, indxKey=0):
        if not indxKey: indxKey = self.rec_indx
        self.rec_dict[indxKey] = {'STATE': 'recorded', 'DATA': {}}
        # ctrls =[sl for sl in pm.selected() if aa.getShape().__class__.__name__ == 'NurbsCurve']
        # if not ctrls:
        ctrlGrp_ls = pm.ls('Facial_Ctrl_grp')
        if not ctrlGrp_ls: ctrlGrp_ls = pm.ls('*:Facial_Ctrl_grp')
        ctrlGrp = ctrlGrp_ls[0]
        ctrls = [crv.getParent() for crv in ctrlGrp.getChildren(ad=True, type='nurbsCurve')]
        s_dic = {'R': 'L', 'L': 'R', 'r': 'l', 'l': 'r'}
        for ea_ctrl in ctrls:
            ctrlAttr = ea_ctrl.listAttr(ud=True, k=False)
            for ea_attr in ctrlAttr:
                blndAttr_nm = ea_attr.attrName()
                blnd_nd_nm_0 = re.sub('^CTRL_', '', blndAttr_nm)
                rel_node_nm = re.sub('_(sklntrx)|_(sklntry)|_(sklntrz)*$', '', blnd_nd_nm_0)
                blndNode = pm.PyNode(rel_node_nm)
                nm_spl = rel_node_nm.split('_')
                if blndNode.nodeType() == 'joint':
                    jnt_attr_name = re.search('_(sklntrx)|_(sklntry)|_(sklntrz)*$', blnd_nd_nm_0).group()
                    jnt_attr_name = re.sub('_sklnt', '', jnt_attr_name)
                    adjustAttr = blndNode.attr(jnt_attr_name)
                    print "{} : {} ".format(adjustAttr.name(), adjustAttr.get())
                    self.rec_dict[indxKey]['DATA'].update({adjustAttr.name(): adjustAttr.get()})
                    if nm_spl[0] in s_dic:
                        nm_spl[0] = s_dic[nm_spl[0]]
                        opp_jnt_nm = '_'.join(nm_spl)
                        opp_jnt = pm.PyNode(opp_jnt_nm)
                        opp_jnt_attr = opp_jnt.attr(jnt_attr_name)
                        print "{} : {} ".format(opp_jnt_attr.name(), opp_jnt_attr.get())
                        self.rec_dict[indxKey]['DATA'].update({adjustAttr.name(): adjustAttr.get()})
                else:
                    adjustAttr = blndNode.attr('weight')[0]
                    print "{} : {} ".format(adjustAttr.name(), adjustAttr.get())
                    self.rec_dict[indxKey]['DATA'].update({adjustAttr.name(): adjustAttr.get()})
                    if nm_spl[1] in s_dic:
                        nm_spl[1] = s_dic[nm_spl[1]]
                        opp_blnd = '_'.join(nm_spl)
                        wgAttr = pm.PyNode(opp_blnd).attr('weight')[0]
                        self.rec_dict[indxKey]['DATA'].update({wgAttr.name(): wgAttr.get()})

    def storeDate2Dict(self):
        # print self.rec_indx
        self.obtainData()
        self.rec_indx += 1

    def pop(self, k=None):
        if not k:
            self.rec_dict.pop()
            self.rec_indx = max(0, self.rec_indx - 1)
        else:
            self.rec_dict.pop(k)

    def wr2disk(self):
        if not os.path.isdir(self.dataStoreDir): os.makedirs(self.dataStoreDir)
        with open(self.dataFile, 'w') as wf:
            json.dump(self.rec_dict, wf)
        print("Recorded and Writed {} group data to disk".format(len(self.rec_dict)))
    def readData(self):
        with open(self.dataFile, 'r') as rf:
            self.read_dict = json.load(rf)

    def setValue(self, indx=0):
        if not self.read_dict: self.readData()
        if not indx:
            indx = self.get_indx()
        # print indx.__class__
        elif indx =='repeat' or not indx: indx = self.get_indx() - 1

        k_indx = '{}'.format(indx)
        Datas = self.read_dict[k_indx]
        # print Datas
        Datas['STATE'] = 'Seted'
        print("Datas have been used on position:{}".format(indx))
        for n, v in Datas['DATA'].items():
            my_attr = pm.PyNode(n)
            my_attr.set(v)

    def resetData(self, id=0):
        if id:
            self.read_dict[str(id)]['STATE'] = 'recorded'
            print("DATA read state reset which on : {}".format(id))
            return
        for m in self.read_dict:
            self.read_dict[m]['STATE'] = 'recorded'
        print("All DATA Read State reseted")

    def get_indx(self):
        rdict = copy.deepcopy(self.read_dict)
        indxs = rdict.keys()
        indxs.sort()
        indx = 'Start'
        for i in indxs:
            if rdict[i]['STATE'] == 'recorded':
                indx = i
                return indx
                break
        if indx == 'Start':
            print("ALL Value Used")
            return indxs[-1]