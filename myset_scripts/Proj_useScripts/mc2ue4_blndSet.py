#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = mc2ue4_blndSet
__author__ = zhangben 
__mtime__ = 2019/9/23 : 9:39
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
"""
#========================================================================================================

#=

import pymel.core as pm
import re,os,sys
import maya.cmds as mc
import pymel.core as pm
import maya.OpenMaya as om

# conf_ctrller()
#
# facialCtrl_win()

from functools import partial


def facialCtrl_win():
    if pm.window('fc_win', exists=True, q=True): pm.deleteUI('fc_win')
    pm.window('fc_win')
    pm.scrollLayout('m_scr')
    pm.columnLayout('mainClm', adjustableColumn=True)
    # pm.floatSlider('fc_sld',min=0, max=1, value=0.0, step=0.001,dc=sldCmd)
    pm.checkBox("SideCBx", l="OtherSide")
    pm.showWindow('fc_win')
    addSLD()

def addSLD():
    for selCtller in pm.selected():
        if selCtller.nodeType() != 'transform':continue
        bldAttr = [eaAttr for eaAttr in selCtller.listAttr(ud=True) if re.search('^CTRL', eaAttr.attrName(), re.I)]
        ctl_nm = selCtller.nodeName()
        lab_nm = '{}_TXT'.format(ctl_nm)
        lab = pm.text(lab_nm, l=ctl_nm, p='mainClm')
        for ea_atr in bldAttr:
            atrnm = ea_atr.attrName()
            #atrnm = "CTRL_up_r_brow_r"
            print("current add attribute {}".format(atrnm))
            rel_node_nm_1 = re.sub('^CTRL_', '', atrnm)
            rel_node_nm_2 = re.sub('_(sklntrx)|_(sklntry)|_(sklntrz)*$', '', rel_node_nm_1)
            #re.sub('_(jntrx)|(jntry)|(jntrz)*$', '', rel_node_nm_1)
            #rel_node_nm_2 = re.sub(('_(jntrx)|(jntry)|(jntrz)*$', '', 'up_r_brow_r')
            sldgrp = None
            if pm.PyNode(rel_node_nm_2).nodeType() == 'blendShape':
            # pm.floatSliderGrp( 'sld_{}'.format(atrnm),label = atrnm, field=False, minValue=0.00, maxValue=1.00, value=0,p='mainClm',dc=lambda x = atrnm:sldCmd(y,x))
                sldgrp = pm.floatSliderGrp('sld_{}'.format(atrnm), label=atrnm, field=True, minValue=0.00, maxValue=1.00, value=0, p='mainClm', cc='empty')
            else:
                sldgrp = pm.floatSliderGrp('sld_{}'.format(atrnm), label=atrnm, field=True, min=-360, max=360, value=0, p='mainClm', cc='empty')
            set_sldValue(sldgrp,lab_nm)
            pm.floatSliderGrp(sldgrp, e=True, cc=partial(moveSld, sldgrp,lab_nm))

def set_sldValue(sldgrp,labelName):
    ctrller_nd = pm.PyNode(pm.text(labelName, q=True, l=True))
    blndAttr_nm = pm.floatSliderGrp(sldgrp, q=True, l=True)
    blnd_nd_nm_0 = re.sub('^CTRL_', '', blndAttr_nm)
    rel_node_nm = re.sub('_(sklntrx)|_(sklntry)|_(sklntrz)*$', '', blnd_nd_nm_0)
    blndNode = pm.PyNode(rel_node_nm)
    adjustAttr = None
    if blndNode.nodeType() == 'joint':
        jnt_attr_name = re.search('_(sklntrx)|_(sklntry)|_(sklntrz)*$', blnd_nd_nm_0).group()
        jnt_attr_name = re.sub('_sklnt', '', jnt_attr_name)
        adjustAttr = blndNode.attr(jnt_attr_name)
    else:
        adjustAttr = blndNode.attr('weight')[0]
    value = adjustAttr.get()
    pm.floatSliderGrp(sldgrp, e=True, v=value)

def moveSld(slider, *args):
    # slider = sldgrp
    ctrl_label_nam = args[0]
    ctrller_nd = pm.PyNode(pm.text(ctrl_label_nam, q=True, l=True))
    blndAttr_nm = pm.floatSliderGrp(slider, q=True, l=True)
    blnd_nd_nm_0 = re.sub('^CTRL_', '', blndAttr_nm)
    rel_node_nm = re.sub('_(sklntrx)|_(sklntry)|_(sklntrz)*$', '', blnd_nd_nm_0)
    blndNode = pm.PyNode(rel_node_nm)
    adjustAttr = None
    if blndNode.nodeType() == 'joint':
        jnt_attr_name = re.search('_(sklntrx)|_(sklntry)|_(sklntrz)*$', blnd_nd_nm_0).group()
        jnt_attr_name = re.sub('_sklnt', '', jnt_attr_name)
        adjustAttr = blndNode.attr(jnt_attr_name)
    else:
        adjustAttr = blndNode.attr('weight')[0]
    value = getSliderValue(slider)
    adjustAttr.set(value)
    if pm.checkBox('SideCBx', q=True, v=True):
        s_dic = {'R': 'L', 'L': 'R','r':'l','l':'r'}
        if blndNode.nodeType() == 'joint':
            nm_spl = rel_node_nm.split('_')
            if nm_spl[0] in s_dic:
                nm_spl[0] = s_dic[nm_spl[0]]
                opp_jnt_nm = '_'.join(nm_spl)
                opp_jnt = pm.PyNode(opp_jnt_nm)
                opp_jnt_attr = opp_jnt.attr(jnt_attr_name)
                opp_jnt_attr.set(value)
        else:
            nm_spl = rel_node_nm.split('_')
            if nm_spl[1] in s_dic:
                nm_spl[1] = s_dic[nm_spl[1]]
                opp_blnd = '_'.join(nm_spl)
                wgAttr = pm.PyNode(opp_blnd).attr('weight')
                wgAttr[0].set(value)


def getSliderValue(ctrlName):
    value = mc.floatSliderGrp(ctrlName, q=True, value=True)
    return value

# configurate facial controller
def conf_ctrller():
    sel_ctr_pairs = pm.selected()
    ctrllsers = [ss for ss in sel_ctr_pairs if ss.nodeType() == 'transform']
    blnds = [ss for ss in sel_ctr_pairs if ss.nodeType() == 'blendShape']
    bones = [ss for ss in sel_ctr_pairs if ss.nodeType() == 'joint']
    for ea_ctrl in ctrllsers:
        ctrl_nm = ea_ctrl.nodeName()
        for attr in ea_ctrl.listAttr(ud=True):
            ea_ctrl.deleteAttr(attr.attrName())
        nmSpl = ctrl_nm.split('_')
        side = nmSpl[1]
        if side not in {'R': 'L', 'L': 'R','r':'l','l':'r'}:
            if blnds:
                for e_blnd in blnds:
                    blndNm = e_blnd.nodeName()
                    add_attr_nm = 'CTRL_{}'.format(blndNm)
                    ea_ctrl.addAttr(add_attr_nm, at='float')
                # e_blnd_wht = e_blnd.attr('weight')
                # wgAttr = e_blnd_wht[0]
                # ctrller.attr(add_attr_nm) // wgAttr
            elif bones:
                for e_jnt in bones:
                    boneNm = e_jnt.name()
                    for ax in ['rx', 'ry', 'rz']:
                        addAttr_nm = 'CTRL_{}_sklnt{}'.format(boneNm, ax)
                        ea_ctrl.addAttr(addAttr_nm, at='float')
        else:
            if blnds:
                rel_blnds = []
                for ea_blnd in blnds:
                    blnd_name = ea_blnd.nodeName()
                    if re.search('{}'.format(side), blnd_name.split('_')[1],re.I): rel_blnds.append(ea_blnd.nodeName())
                rel_blnds.sort()
                for e_blnd in rel_blnds:
                    add_attr_nm = 'CTRL_{}'.format(e_blnd)
                    ea_ctrl.addAttr(add_attr_nm, at='float')
            elif bones:
                rel_bones = []
                for ea_jnt in bones:
                    boneNm = ea_jnt.name()
                    if re.search('{}'.format(side), boneNm.split('_')[0],re.I): rel_bones.append(ea_jnt.nodeName())
                rel_bones.sort()
                for e_jnt in rel_bones:
                    for ax in ['rx', 'ry', 'rz']:
                        addAttr_nm = 'CTRL_{}_sklnt{}'.format(e_jnt, ax)
                        ea_ctrl.addAttr(addAttr_nm, at='float')
def resetAllCtrl():
    # slider = sldgrp
    ctrls =[sl for sl in pm.selected() if aa.getShape().__class__.__name__ == 'NurbsCurve']
    if not ctrls:
       ctrlGrp_ls = pm.ls('Facial_Ctrl_grp')
       if not ctrlGrp_ls:ctrlGrp_ls = pm.ls('*:Facial_Ctrl_grp')
       ctrlGrp = ctrlGrp_ls[0]
       ctrls = [crv.getParent() for crv in ctrlGrp.getChildren(ad=True,type='nurbsCurve')]
    for ea_ctrl in ctrls:
        ctrlAttr = ea_ctrl.listAttr(ud=True,k=False)
        for ea_attr in ctrlAttr:
            blndAttr_nm = ea_attr.attrName()
            blnd_nd_nm_0 = re.sub('^CTRL_', '', blndAttr_nm)
            rel_node_nm = re.sub('_(sklntrx)|_(sklntry)|_(sklntrz)*$', '', blnd_nd_nm_0)
            blndNode = pm.PyNode(rel_node_nm)
            if blndNode.nodeType() == 'joint':
                jnt_attr_name = re.search('_(sklntrx)|_(sklntry)|_(sklntrz)*$', blnd_nd_nm_0).group()
                jnt_attr_name = re.sub('_sklnt', '', jnt_attr_name)
                adjustAttr = blndNode.attr(jnt_attr_name)
            else:
                adjustAttr = blndNode.attr('weight')[0]
            adjustAttr.set(0)
            s_dic = {'R': 'L', 'L': 'R','r':'l','l':'r'}
            if blndNode.nodeType() == 'joint':
                nm_spl = rel_node_nm.split('_')
                if nm_spl[0] in s_dic:
                    nm_spl[0] = s_dic[nm_spl[0]]
                    opp_jnt_nm = '_'.join(nm_spl)
                    opp_jnt = pm.PyNode(opp_jnt_nm)
                    opp_jnt_attr = opp_jnt.attr(jnt_attr_name)
                    opp_jnt_attr.set(0)
            else:
                nm_spl = rel_node_nm.split('_')
                if nm_spl[1] in s_dic:
                    nm_spl[1] = s_dic[nm_spl[1]]
                    opp_blnd = '_'.join(nm_spl)
                    wgAttr = pm.PyNode(opp_blnd).attr('weight')
                    wgAttr[0].set(0)

resetAllCtrl()








import datetime
import json

class RecDxyData2Disk(object):
    def __init__(self):
        # slider = sldgrp
        self.DaTm = datetime.datetime.now()
        #DaTm.__format__('%Y%m%d')
        #DaTm.strftime('%Y%m%d%H%M%S')
        self.proj_dir = pm.workspace.path
        self.dataStoreDir = '{}/data/dxyzRecordData'.format(self.proj_dir)
        self.scene_bsnm = pm.sceneName().basename().strip()
        self.dt_f_name=None
        if not self.scene_bsnm: self.dt_f_name = 'DxyzRecData_{}.json'.format(self.DaTm.strftime('%Y%m%d%H%M%S'))
        else:  self.dt_f_name = "DxyzRecData_{}.json".format(self.scene_bsnm)
        self.dataFile = "{}/{}".format(self.dataStoreDir,self.dt_f_name)
        self.rec_indx = 0
        self.rec_dict = {}
        self.read_dict = {}
    def obtainData(self,indxKey=0):
        if not indxKey: indxKey = self.rec_indx
        self.rec_dict[    indxKey] = {'STAT':'recorded','DATA':{}}
        #ctrls =[sl for sl in pm.selected() if aa.getShape().__class__.__name__ == 'NurbsCurve']
        #if not ctrls:
        ctrlGrp_ls = pm.ls('Facial_Ctrl_grp')
        if not ctrlGrp_ls:ctrlGrp_ls = pm.ls('*:Facial_Ctrl_grp')
        ctrlGrp = ctrlGrp_ls[0]
        ctrls = [crv.getParent() for crv in ctrlGrp.getChildren(ad=True,type='nurbsCurve')]
        s_dic = {'R': 'L', 'L': 'R','r':'l','l':'r'}
        for ea_ctrl in ctrls:
            ctrlAttr = ea_ctrl.listAttr(ud=True,k=False)
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
                    print "{} : {} ".format(adjustAttr.name(),adjustAttr.get())
                    self.rec_dict[indxKey]['DATA'].update({adjustAttr.name():adjustAttr.get()})
                    if nm_spl[0] in s_dic:
                        nm_spl[0] = s_dic[nm_spl[0]]
                        opp_jnt_nm = '_'.join(nm_spl)
                        opp_jnt = pm.PyNode(opp_jnt_nm)
                        opp_jnt_attr = opp_jnt.attr(jnt_attr_name)
                        print "{} : {} ".format(opp_jnt_attr.name(),opp_jnt_attr.get())
                        self.rec_dict[    indxKey]['DATA'].update({adjustAttr.name():adjustAttr.get()})
                else:
                    adjustAttr = blndNode.attr('weight')[0]
                    print "{} : {} ".format(adjustAttr.name(),adjustAttr.get())
                    self.rec_dict[    indxKey]['DATA'].update({adjustAttr.name():adjustAttr.get()})
                if nm_spl[1] in s_dic:
                    nm_spl[1] = s_dic[nm_spl[1]]
                    opp_blnd = '_'.join(nm_spl)
                    wgAttr = pm.PyNode(opp_blnd).attr('weight')[0]
                    self.rec_dict[indxKey]['DATA'].update({wgAttr.name():wgAttr.get()})
    def storeDate2Dict(self):
        print self.rec_indx
        self.obtainData()
        self.rec_indx +=1
    def pop(self,k=None):
        if not k:
            self.rec_dict.pop()
            self.rec_indx = max(0,self.rec_indx-1)
        else: self.rec_dict.pop(k)
    def wr2disk(self):
        if not os.path.isdir(self.dataStoreDir):os.makedirs(self.dataStoreDir)
        with open(self.dataFile,'w') as wf:
            json.dump(self.rec_dict,wf)












"""
aa = pm.selected()[0]



blnds = []
opSets = [blnds.extend(s.listConnections(type='blendShape')) for s in aa.listConnections(type='objectSet') if s.listConnections(type='blendShape') and s.listConnections(type='blendShape')[0] not in blnds for aa in pm.selected()]

pm.select(blnds)

up_blnds = [b for b in blnds if re.search('^up',b.name(),re.I)]
pm.select(up_blnds)


r_blnds = [bb for  bb in pm.selected() if bb.name().split('_')[1] in ['r','R']]
pm.select(r_blnds)

l_blnds = [bb for  bb in pm.selected() if bb.name().split('_')[1] in ['l','L']]
pm.select(l_blnds)


nose_blnds = [bb for bb in pm.selected() if re.search('_nose_',bb.name(),re.I)]
pm.select(nose_blnds)


for eb in pm.selected():
    blnd_nm_spl = eb.name().split('_')
    blnd_nm_spl[1] = 'l'
    new_blnd_nm = '_'.join(blnd_nm_spl)
    eb.rename(new_blnd_nm)






















#================================================================================================

#conf_ctrller()

#
facialCtrl_win()

from functools import partial


def facialCtrl_win():
    if pm.window('fc_win', exists=True, q=True): pm.deleteUI('fc_win')
    pm.window('fc_win')
    pm.scrollLayout('m_scr')
    pm.columnLayout('mainClm', adjustableColumn=True)
    # pm.floatSlider('fc_sld',min=0, max=1, value=0.0, step=0.001,dc=sldCmd)
    pm.checkBox("SideCBx", l="OtherSide")
    pm.showWindow('fc_win')
    addSLD()


def addSLD():
    for selCtller in pm.selected():
        if selCtller.nodeType() != 'transform':continue
        bldAttr = [eaAttr for eaAttr in selCtller.listAttr(ud=True) if re.search('^CTRL', eaAttr.attrName(), re.I)]
        ctl_nm = selCtller.nodeName()
        lab_nm = '{}_TXT'.format(ctl_nm)
        lab = pm.text(lab_nm, l=ctl_nm, p='mainClm')
        for ea_atr in bldAttr:
            atrnm = ea_atr.attrName()
            rel_node_nm_1 = re.sub('^CTRL_', '', atrnm)
            rel_node_nm_2 = re.sub('_[(rx)(ry)(rz)]*$', '', rel_node_nm_1)
            sldgrp = None
            if pm.PyNode(rel_node_nm_2).nodeType() == 'blendShape':
            # pm.floatSliderGrp( 'sld_{}'.format(atrnm),label = atrnm, field=False, minValue=0.00, maxValue=1.00, value=0,p='mainClm',dc=lambda x = atrnm:sldCmd(y,x))
                sldgrp = pm.floatSliderGrp('sld_{}'.format(atrnm), label=atrnm, field=True, minValue=0.00, maxValue=1.00, value=0, p='mainClm', cc='empty')
            else:
                sldgrp = pm.floatSliderGrp('sld_{}'.format(atrnm), label=atrnm, field=True, min=-360, max=360, value=0, p='mainClm', cc='empty')
            set_sldValue(sldgrp,lab_nm)
            pm.floatSliderGrp(sldgrp, e=True, cc=partial(moveSld, sldgrp,lab_nm))

def set_sldValue(sldgrp,labelName):
    ctrller_nd = pm.PyNode(pm.text(labelName, q=True, l=True))
    blndAttr_nm = pm.floatSliderGrp(sldgrp, q=True, l=True)
    blnd_nd_nm_0 = re.sub('^CTRL_', '', blndAttr_nm)
    rel_node_nm = re.sub('_[(rx)(ry)(rz)]*$', '', blnd_nd_nm_0)
    blndNode = pm.PyNode(rel_node_nm)
    adjustAttr = None
    if blndNode.nodeType() == 'joint':
        jnt_attr_name = re.search('[(rx)(ry)(rz)]*$', blnd_nd_nm_0).group()
        adjustAttr = blndNode.attr(jnt_attr_name)
    else:
        adjustAttr = blndNode.attr('weight')[0]
    value = adjustAttr.get()
    pm.floatSliderGrp(sldgrp, e=True, v=value)

def moveSld(slider, *args):
    # slider = sldgrp
    ctrl_label_nam = args[0]
    ctrller_nd = pm.PyNode(pm.text(ctrl_label_nam, q=True, l=True))
    blndAttr_nm = pm.floatSliderGrp(slider, q=True, l=True)
    blnd_nd_nm_0 = re.sub('^CTRL_', '', blndAttr_nm)
    rel_node_nm = re.sub('_[(rx)(ry)(rz)]*$', '', blnd_nd_nm_0)
    blndNode = pm.PyNode(rel_node_nm)
    adjustAttr = None
    if blndNode.nodeType() == 'joint':
        jnt_attr_name = re.search('[(rx)(ry)(rz)]*$', blnd_nd_nm_0).group()
        adjustAttr = blndNode.attr(jnt_attr_name)
    else:
        adjustAttr = blndNode.attr('weight')[0]
    value = getSliderValue(slider)
    adjustAttr.set(value)
    if pm.checkBox('SideCBx', q=True, v=True):
        s_dic = {'R': 'L', 'L': 'R'}
        if blndNode.nodeType() == 'joint':
            nm_spl = rel_node_nm.split('_')
            if nm_spl[0] in s_dic:
                nm_spl[0] = s_dic[nm_spl[0]]
                opp_jnt_nm = '_'.join(nm_spl)
                opp_jnt = pm.PyNode(opp_jnt_nm)
                opp_jnt_attr = opp_jnt.attr(jnt_attr_name)
                opp_jnt_attr.set(value)
        else:
            nm_spl = rel_node_nm.split('_')
            if nm_spl[1] in s_dic:
                nm_spl[1] = s_dic[nm_spl[1]]
                opp_blnd = '_'.join(nm_spl)
                wgAttr = pm.PyNode(opp_blnd).attr('weight')
                wgAttr[0].set(value)


def getSliderValue(ctrlName):
    value = mc.floatSliderGrp(ctrlName, q=True, value=True)
    return value


# configurate facial controller
def conf_ctrller():
    sel_ctr_pairs = pm.selected()
    ctrllsers = [ss for ss in sel_ctr_pairs if ss.nodeType() == 'transform']
    blnds = [ss for ss in sel_ctr_pairs if ss.nodeType() == 'blendShape']
    bones = [ss for ss in sel_ctr_pairs if ss.nodeType() == 'joint']
    for ea_ctrl in ctrllsers:
        ctrl_nm = ea_ctrl.nodeName()
        for attr in ea_ctrl.listAttr(ud=True):
            ea_ctrl.deleteAttr(attr.attrName())
        nmSpl = ctrl_nm.split('_')
        side = nmSpl[1]
        if side not in {'R': 'L', 'L': 'R'}:
            if blnds:
                for e_blnd in blnds:
                    blndNm = e_blnd.nodeName()
                    add_attr_nm = 'CTRL_{}'.format(blndNm)
                    ea_ctrl.addAttr(add_attr_nm, at='float')
                # e_blnd_wht = e_blnd.attr('weight')
                # wgAttr = e_blnd_wht[0]
                # ctrller.attr(add_attr_nm) // wgAttr
            elif bones:
                for e_jnt in bones:
                    boneNm = e_jnt.name()
                    for ax in ['rx', 'ry', 'rz']:
                        addAttr_nm = 'CTRL_{}_skelten{}'.format(boneNm, ax)
                        ea_ctrl.addAttr(add_attr_nm, at='float')
        else:
            if blnds:
                rel_blnds = []
                if len(blnds) != 1:
                    for ea_blnd in blnds:
                        blnd_name = ea_blnd.nodeName()
                        if re.search('{}'.format(side), blnd_name.split('_')[1]): rel_blnds.append(ea_blnd.nodeName())
                else:
                    rel_blnds.extend(blnds)
                rel_blnds.sort()
                for e_blnd in rel_blnds:
                    add_attr_nm = 'CTRL_{}'.format(e_blnd)
                    ea_ctrl.addAttr(add_attr_nm, at='float')
            elif bones:
                rel_bones = []
                for ea_jnt in bones:
                    boneNm = ea_jnt.name()
                    if re.search('{}'.format(side), boneNm.split('_')[0]): rel_bones.append(ea_jnt.nodeName())
                rel_bones.sort()
                for e_jnt in rel_bones:
                    for ax in ['rx', 'ry', 'rz']:
                        addAttr_nm = 'CTRL_{}_skelten{}'.format(e_jnt, ax)
                        ea_ctrl.addAttr(addAttr_nm, at='float')



# add ctroller blender attribute
# ctrller = sel_ctr_pairs[-1]
# # blnds = sel_ctr_pairs[:-1]
# for e_blnd in blnds:
#     blndNm = e_blnd.nodeName()
#     add_attr_nm = 'CTRL_{}'.format(blndNm)
#     ctrller.addAttr(add_attr_nm, at='float')
#     e_blnd_wht = e_blnd.attr('weight')
#     wgAttr = e_blnd_wht[0]


# ctrller.attr(add_attr_nm) // wgAttr


def sldCmd(*args):
    s_dic = {'R': 'L', 'L': 'R'}
    sel_blnders = pm.selected()
    if not sel_blnders: return
    for bl in sel_blnders:
        if bl.nodeType() != 'blendShape': continue
        setV = pm.floatSlider('fc_sld', q=True, v=True)
        wgAttr = bl.attr('weight')
        wgAttr[0].set(setV)
        if pm.checkBox('SideCBx', q=True, v=True):
            blNm = bl.nodeName()
            nm_spl = blNm.split('_')
            if nm_spl[1] in s_dic:
                nm_spl[1] = s_dic[nm_spl[1]]
                opp_blnd = '_'.join(nm_spl)
                if pm.PyNode(opp_blnd) not in sel_blnders:
                    wgAttr = pm.PyNode(opp_blnd).attr('weight')
                    wgAttr[0].set(setV)







#========================================================================================================

from functools import partial


def facialCtrl_win():
    if pm.window('fc_win', exists=True, q=True): pm.deleteUI('fc_win')
    pm.window('fc_win')
    pm.columnLayout('mainClm', adjustableColumn=True)
    # pm.floatSlider('fc_sld',min=0, max=1, value=0.0, step=0.001,dc=sldCmd)
    pm.checkBox("SideCBx", l="OtherSide")
    pm.showWindow('fc_win')
    addSLD()


def addSLD():
    selCtller = pm.selected()[0]
    bldAttr = [eaAttr for eaAttr in selCtller.listAttr(ud=True) if re.search('^CTRL', eaAttr.attrName(), re.I)]
    lab = pm.text('ctrl_name', l=selCtller.nodeName(), p='mainClm')
    for ea_atr in bldAttr:
        atrnm = ea_atr.attrName()
        # pm.floatSliderGrp( 'sld_{}'.format(atrnm),label = atrnm, field=False, minValue=0.00, maxValue=1.00, value=0,p='mainClm',dc=lambda x = atrnm:sldCmd(y,x))
        sldgrp = pm.floatSliderGrp('sld_{}'.format(atrnm), label=atrnm, field=False, minValue=0.00, maxValue=1.00, value=0, p='mainClm', dc='empty')
        pm.floatSliderGrp(sldgrp, e=True, dc=partial(moveSld, sldgrp))


def moveSld(slider, *args):
    ctrller_nd = pm.PyNode(pm.text('ctrl_name', q=True, l=True))
    value = getSliderValue(slider)
    blndAttr_nm = pm.floatSliderGrp(slider, q=True, l=True)
    blnd_nd_nm = re.sub('^CTRL_', '', blndAttr_nm)
    blndNode = pm.PyNode(blnd_nd_nm)
    wght_attr = blndNode.attr('weight')
    wght_attr[0].set(value)
    s_dic = {'R': 'L', 'L': 'R'}
    if pm.checkBox('SideCBx', q=True, v=True):
        nm_spl = blnd_nd_nm.split('_')
        if nm_spl[1] in s_dic:
            nm_spl[1] = s_dic[nm_spl[1]]
            opp_blnd = '_'.join(nm_spl)
            wgAttr = pm.PyNode(opp_blnd).attr('weight')
            wgAttr[0].set(value)


def getSliderValue(ctrlName):
    value = mc.floatSliderGrp(ctrlName, q=True, value=True)
    return value


# configurate facial controller
sel_ctr_pairs = pm.selected()
ctrllsers = [ss for ss in sel_ctr_pairs if ss.nodeType() == 'transform']
blnds = [ss for ss in sel_ctr_pairs if ss.nodeType() == 'blendShape']
for ea_ctrl in ctrllsers:
    ctrl_nm = ea_ctrl.nodeName()
    nmSpl = ctrl_nm.split('_')
    side = nmSpl[1]
    if side not in {'R': 'L', 'L': 'R'}:
        for e_blnd in blnds:
            blndNm = e_blnd.nodeName()
            add_attr_nm = 'CTRL_{}'.format(blndNm)
            ctrller.addAttr(add_attr_nm, at='float')
        # e_blnd_wht = e_blnd.attr('weight')
        # wgAttr = e_blnd_wht[0]
        # ctrller.attr(add_attr_nm) // wgAttr
    else:
        rel_blnds = []
        for ea_blnd in blnds:
            blnd_name = ea_blnd.nodeName()
            if re.search('{}'.format(side), blnd_name.split('_')[1]): rel_blnds.append(ea_blnd.nodeName())
        rel_blnds.sort()
        for e_blnd in rel_blnds:
            add_attr_nm = 'CTRL_{}'.format(e_blnd)
            ea_ctrl.addAttr(add_attr_nm, at='float')

# add ctroller blender attribute
ctrller = sel_ctr_pairs[-1]
blnds = sel_ctr_pairs[:-1]
for e_blnd in blnds:
    blndNm = e_blnd.nodeName()
    add_attr_nm = 'CTRL_{}'.format(blndNm)
    ctrller.addAttr(add_attr_nm, at='float')
    e_blnd_wht = e_blnd.attr('weight')
    wgAttr = e_blnd_wht[0]


# ctrller.attr(add_attr_nm) // wgAttr


def sldCmd(*args):
    s_dic = {'R': 'L', 'L': 'R'}
    sel_blnders = pm.selected()
    if not sel_blnders: return
    for bl in sel_blnders:
        if bl.nodeType() != 'blendShape': continue
        setV = pm.floatSlider('fc_sld', q=True, v=True)
        wgAttr = bl.attr('weight')
        wgAttr[0].set(setV)
        if pm.checkBox('SideCBx', q=True, v=True):
            blNm = bl.nodeName()
            nm_spl = blNm.split('_')
            if nm_spl[1] in s_dic:
                nm_spl[1] = s_dic[nm_spl[1]]
                opp_blnd = '_'.join(nm_spl)
                if pm.PyNode(opp_blnd) not in sel_blnders:
                    wgAttr = pm.PyNode(opp_blnd).attr('weight')
                    wgAttr[0].set(setV)


for nn in pm.selected():
    new_nm = re.sub('^Up_','Lower_',nn.nodeName())
    nn.rename(new_nm)
#============================================================================================================================























sels = pm.selected()
src = sels[-1]

targs = sels[:-1]

for n in targs:
    nd_nm = n.name()
    pm.blendShape(n, src, n='{}_blnd'.format(nd_nm))

for n in pm.selected():
    c_nm = n.nodeName()
    new_nm = '{}_Upper'.format(c_nm)
    shp_nd = n.getShape()
    shp_nm = shp_nd.nodeName()
    shp_nm_new = "{}Shape".format(shp_nm)
    shp_nd.rename(shp_nm_new)
    n.rename(new_nm)

for n in pm.selected():
    c_nm = n.nodeName()
    new_nm = '{}_Lower'.format(c_nm)
    shp_nd = n.getShape()
    shp_nm = shp_nd.nodeName()
    shp_nm_new = "{}Shape".format(shp_nm)
    shp_nd.rename(shp_nm_new)
    n.rename(new_nm)



# arrange blendshape target modes
AllTargs = pm.selected()

maxColumn = 11

mAxis_x = 30
mAxis_y = 40

for n in range(len(AllTargs)):
    p_x = n % maxColumn * mAxis_x
    p_y = n // maxColumn * mAxis_y
    print p_x
    t = AllTargs[n]
    t.v.set(1)
    t.tx.set(p_x)
    t.ty.set(p_y)

#  set all connect blendShape weight value to 0
mmhead = pm.selected()[0]

conBlnds = [se.listConnections(type='blendShape')[0] for se in mmhead.listConnections(d=True,type='objectSet') if re.search('_blndSet',se.name(),re.I) and se.listConnections(type='blendShape')]

for bl in conBlnds:
    wgAttr = bl.attr('weight')
    wgAttr[0].set(0)


# #=========adjust blendShape values
# if pm.window('fc_win',exists=True,q=True):pm.deleteUI('fc_win')
# pm.window('fc_win')
# pm.columnLayout( adjustableColumn=True )
# pm.floatSlider('fc_sld',min=0, max=1, value=0.0, step=0.001,dc=sldCmd)
# pm.checkBox("SideCBx",l="OtherSide')
# pm.showWindow('fc_win')


def sldCmd(*args):
    s_dic = {'R':'L','L':'R'}
    sel_blnders = pm.selected()
    if not sel_blnders:return
    for bl in sel_blnders:
        if bl.nodeType() !='blendShape': continue
        setV = pm.floatSlider('fc_sld',q=True,v=True)
        wgAttr = bl.attr('weight')
        wgAttr[0].set(setV)
        if pm.checkBox('SideCBx',q=True,v=True):
            blNm = bl.nodeName()
            nm_spl = blNm.split('_')
            if nm_spl[1] in  s_dic:
                nm_spl[1] = s_dic[nm_spl[1]]
                opp_blnd = '_'.join(nm_spl)
                if pm.PyNode(opp_blnd) not in sel_blnders:
                    wgAttr = pm.PyNode(opp_blnd).attr('weight')
                    wgAttr[0].set(setV)



#sel_ctr_pairs = pm.selected()

ctrller = sel_ctr_pairs[-1]
blnds = sel_ctr_pairs[:-1]

for e_blnd in blnds:
    blndNm = e_blnd.nodeName()
    add_attr_nm = 'CTRL_{}'.format(blndNm)
    ctrller.addAttr(add_attr_nm,at='float')
    e_blnd_wht = e_blnd.attr('weight')
    wgAttr = e_blnd_wht[0]
    ctrller.attr(add_attr_nm) >> wgAttr


allBlnds = pm.selected()

pm.select([eb for eb in allBlnds if re.search('_[RL]_',eb.nodeName(),re.I)])


sels_bones = pm.selected()
all_op_bones = sels_bones

[all_op_bones.extend(ea_bn.getChildren(ad=True)) for ea_bn in sels_bones]

pm.select(all_op_bones)

for jnt in all_op_bones:
    or_atrs = ['X','Y','Z']
    for ea_or in or_atrs:
        opAttr_nm = 'jointOrient{}'.format(ea_or)
        opAttr = jnt.attr(opAttr_nm)

if pm.window('fc_win', exists=True, q=True): pm.deleteUI('fc_win')
pm.window('fc_win')
pm.columnLayout('mainClm', adjustableColumn=True)
# pm.floatSlider('fc_sld',min=0, max=1, value=0.0, step=0.001,dc=sldCmd)
pm.checkBox("SideCBx", l="OtherSide")
pm.showWindow('fc_win')

addSLD()


def addSLD():
    selCtller = pm.selected()[0]


bldAttr = [eaAttr for eaAttr in selCtller.listAttr(ud=True) if re.search('^CTRL', eaAttr.attrName(), re.I)]
lab = pm.text('ctrl_name', l=selCtller.nodeName(), p='mainClm')
for ea_atr in bldAttr:
    atrnm = ea_atr.attrName()
# pm.floatSliderGrp( 'sld_{}'.format(atrnm),label = atrnm, field=False, minValue=0.00, maxValue=1.00, value=0,p='mainClm',dc=lambda x = atrnm:sldCmd(y,x))
sldgrp = pm.floatSliderGrp('sld_{}'.format(atrnm), label=atrnm, field=False, minValue=0.00, maxValue=1.00, value=0, p='mainClm', dc='empty')


def moveSld(slider, *args):
    ctrller_nd = pm.PyNode(pm.text('ctrl_name', q=True, l=True))
    value = getSliderValue(slider)
    blndAttr_nm = pm.floatSliderGrp(slider, q=True, name=True)
    print blndAttr_nm


def getSliderValue(ctrlName):
    value = cmds.floatSliderGrp(ctrlName, q=True, value=True)
    return value


def sldCmd(*args):
    ctrller_nd = pm.PyNode(pm.text('ctrl_name', q=True, l=True))
    for v in args:
        print v


def sldCmd(*args):
    s_dic = {'R': 'L', 'L': 'R'}
    sel_blnders = pm.selected()
    if not sel_blnders: return
    for bl in sel_blnders:
        if bl.nodeType() != 'blendShape': continue
        setV = pm.floatSlider('fc_sld', q=True, v=True)
        wgAttr = bl.attr('weight')
        wgAttr[0].set(setV)
        if pm.checkBox('SideCBx', q=True, v=True):
            blNm = bl.nodeName()
            nm_spl = blNm.split('_')
            if nm_spl[1] in s_dic:
                nm_spl[1] = s_dic[nm_spl[1]]
                opp_blnd = '_'.join(nm_spl)
                if pm.PyNode(opp_blnd) not in sel_blnders:
                    wgAttr = pm.PyNode(opp_blnd).attr('weight')
                    wgAttr[0].set(setV)


import os, re

sideDict = {'left': 'L', 'right': 'R'}
oppo_dict = {0: 1, 1: 0}
iffy_joinVws = []
joinVws = nuke.selectedNodes('JoinViews')
for jv in joinVws:
    # jv  = joinVws[0]
    if jv.inputs() != 2: continue
    inputs_attrs = jv.knob('viewassoc').getValue().split('\n')
    for n in range(len(inputs_attrs)):
        con_read = jv.input(n)
        side_kw = inputs_attrs[n]
        side_vw = sideDict[side_kw]
        con_stuff = con_read['file'].getValue()
        con_stuff_spl = con_stuff.split('/')
        get_camSide = None
        for eaSpl in con_stuff_spl:
    if re.search('cam[(era)|_]*[r|l]$', eaSpl, re.I):
        cam_name = re.search('cam[(era)|_]*[r|l]$', eaSpl, re.I).group()
        get_camSide = re.search('[R|L]$', cam_name, re.I).group()
        break
        # if get_camSide != side_vw:
        #    iffy_joinVws[jv].update({n:{inputs_attrs[n]:con_read}})
        if get_camSide != side_vw and jv not in iffy_joinVws: iffy_joinVws.append(jv)
for jv in iffy_joinVws:
    con_reads = [jv.input(0), jv.input(1)]
    jv.setInput(0, None)
    jv.setInput(1, None)
    jv.setInput(0, con_reads[1])
    jv.setInput(1, con_reads[0])
"""

import pymel.core as pm
import re


# ==========================

class TransFacialData(object):
    def __init__(self):
        self.pSels = None

    def trans_anim_data(pSels=None):
        pHead = None
        pJnts = []
        if not pSels:
            pSels = pm.selected()
            if not pSels: return
        for pSel in pSels:
            if pSel.getShape() and pSel.getShape().nodeType() == 'mesh':
                pHead = pSel.getShape()
            else:
                pJnts.append(pSel)
        # pm.select(psel.listRelatives(ad=True))
        # pSelShp = pSels[0].getShape()
        conBlnds = []
        tmp = [conBlnds.extend(s.listConnections(type='blendShape')) for s in pHead.listConnections(type='objectSet') if
               s.listConnections(type='blendShape') and s.listConnections(type='blendShape')[0] not in conBlnds]
        for eb in conBlnds:
            blndNm_strip = eb.name(stripNamespace=True)
            src_w_attr = eb.attr('weight')[0]
            dest_blnd = pm.PyNode(blndNm_strip)
            dest_blnd_w_attr = dest_blnd.attr('weight')[0]
            dest_blnd_w_attr.set(src_w_attr.get())
        for ejnt in pJnts:
            rot_attrs = ['rx', 'ry', 'rz']
            jnts_nm_strip = ejnt.name(stripNamespace=True)
            dest_jnt = pm.PyNode(jnts_nm_strip)
            for er in rot_attrs:
                dest_jnt.attr(er).set(ejnt.attr(er).get())


if __name__ == "__main__":
    pSels = pm.selected()
    trans_anim_data(pSels)

