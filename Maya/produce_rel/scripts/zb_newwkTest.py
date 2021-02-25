#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = 'OCT_ReassignMaterial.py'
__author__ = zhangben
__mtime__ = 2018/11/27:17:18
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
'''
import pymel.core as pm
import os, re
import maya.cmds as mc


# class OCT_Reassing_materials(object):
#     """对combine后的模型，重新指定材质
#             　 有一个已经修正过材质的combine的物体，
#             　 列出场景中需要修正材质的物体，根据shader，来指定传递
#     """
# 
#    

class OCT_ReaasingMatUI(object):
    def __init__(self):
        self._target_shd_dict = {}
        self._source_shd_dict = {}
        self.targ_obj_dic = {}

    def refreshData(self):
        self._source_shd_dict = self._source_shd_dict

    @staticmethod
    def call_ui():
        # def reassignMat_MainWindow():
        if mc.window("reassignMatWin", exists=True):
            mc.deleteUI("reassignMatWin")

        main_win = mc.window('reassignMatWin', title="Reassing materials")
        main_fl = mc.formLayout('mainFL')
        # main_clm = mc.columnLayout('main_CLM',w=600,adjustableColumn=True)

        main_rly = mc.rowLayout('mainRL', numberOfColumns=3, w=880, p=main_fl, rowAttach=[(3, 'top', 0)])
        # ======= list corect objes shaders==========
        src_clm = mc.columnLayout('src_CLM', columnAttach=('both', 5), rowSpacing=10, p=main_rly, adjustableColumn=True)
        mc.textScrollList('srcShdTSL', parent=src_clm, sc='ins_rs.sel_item_cmd()')
        listSrcSdCmdStr = 'ins_rs = OCT_ReaasingMatUI()\nins_rs.lfbt_cmd()'
        mc.button('addSource', label='List From Object shaders', p=src_clm, c=listSrcSdCmdStr)
        # ======== list selected target objectes====================
        trg_clm = mc.columnLayout('trg_CLM', columnAttach=('both', 5), rowSpacing=10, p=main_rly, adjustableColumn=True)
        mc.textScrollList('trgObjsTSL', parent=trg_clm, sc='ins_rs.sel_targ_itme_cmd()')
        mc.button('addTarget', label='To objects', p=trg_clm, c='ins_rs.update_targetList()')
        # mc.setParent('..')
        # ==================list target object's shaders=====================
        trg_lst_clm = mc.columnLayout('trg_lst_CLM', columnAttach=('both', 5), rowSpacing=10, p=main_rly,
                                      adjustableColumn=True, w=350)
        mc.text('lstTX', label='old shaders list', p=trg_lst_clm, al='left')
        mc.textScrollList('trgShdTSL', parent=trg_lst_clm, w=300,sc='ins_rs.sel_item_cmd(\'targ\')')

        bt_grps = mc.rowLayout('bt_GRPS', numberOfColumns=3, columnWidth3=[150, 400, 300], columnOffset3=[15, 20, 60],
                               p=main_fl)
        niceName = mc.checkBox(label='ignore Prefix', p=bt_grps, w=150)
        runbt = mc.button('runButon', label='reassign', p=bt_grps, w=300,c='ins_rs.Reassing_btcmd()')
        all_cb = mc.checkBox(label='other objects do the same ', p=bt_grps, w=150)

        # adjust layout elements
        mc.formLayout(main_fl, edit=True, attachForm=[(main_rly, 'top', 5)],
                      attachControl=[(bt_grps, 'top', 15, main_rly)])

        mc.window(main_win, e=True, wh=(850, 300), rtf=True)
        mc.showWindow(main_win)

    # ins_reasign = OCT_Reassing_materials()

    def add_element(self, express='src'):
        if express == 'src':
            self._source_shd_dict.clear()
            self._source_shd_dict = self.list_AllShaders(pm.selected()[0])
        else:
            self._target_shd_dict.clear()
            self._target_shd_dict = self.list_AllShaders(pm.selected()[0])

    def reassing_materials(self, sel_src_lb, sel_targ_lb):
        # sel = list_src_shd.keys()[3]
        sel_src_sg = self._source_shd_dict[sel_src_lb].values()[0]
        # targ = list_target_shd.keys()[3]#
        # sel_trg = self._target_shd_dict[sel_targ].values()[0]
        self.sel_faces(sel_targ_lb, 'target')
        pm.sets(sel_src_sg, e=True, forceElement=True)

    def list_AllShaders(self, specObj, ignorID=False):
        # specObj = pm.selected()[0]
        shpnd = specObj.getShape()
        ls_sgs = shpnd.listConnections(type='shadingEngine')
        sgs_opmt = [ls_sgs[i] for i in range(len(ls_sgs)) if ls_sgs[i] not in ls_sgs[:i]]
        shder_dict = {}

        for eachSG in sgs_opmt:
            try:
                get_shd = eachSG.attr('surfaceShader').listConnections()[0]
            except:
                pm.error("The SG node doesn't be connected in surfaceShader Attribute!!!please Check!!")
            sd_nm_label = get_shd.name(stripNamespace=True)
            sg_shd_pair = {}
            if ignorID:
                sd_nm_label_spl = sd_nm_label.split('_')
                if len(sd_nm_label_spl) == 1:
                    sd_nm_label = sd_nm_label_spl[0]
                else:
                    sd_nm_label = '_'.join(sd_nm_label_spl[1:])
            sg_shd_pair[get_shd] = eachSG
            shd_nm_label = self.re_nm(sd_nm_label, shder_dict)
            shder_dict[shd_nm_label] = sg_shd_pair
        return shder_dict

    def re_nm(self, old, tagetList):
        n = 0
        while old in tagetList:
            base_char = re.search('[^_0-9]*', old).group()
            old = '{}_{:03d}'.format(base_char, n)
            n += 1
        return old

    def sel_faces(self, sel_shd_label, type='target'):  # select faces based on selected labels.
        if type == 'target':
            sel_sg = self._target_shd_dict[sel_shd_label].values()[0]
            pm.select(pm.sets(sel_sg, q=True), r=True)
        else:
            sel_sg = self._source_shd_dict[sel_shd_label].values()[0]
            pm.select(pm.sets(sel_sg, q=True), r=True)

    # ins_reasign = OCT_Reassing_materials()

    def lfbt_cmd(self):
        mc.textScrollList('srcShdTSL', e=True, ra=True)
        self.add_element('src')
        src_shd_dct = self._source_shd_dict
        mc.textScrollList('srcShdTSL', e=True, append=src_shd_dct.keys())

    def sel_item_cmd(self, type='src'):

        if type == 'src':
            sel_lable = mc.textScrollList('srcShdTSL', q=True, si=True)
            self.sel_faces(sel_lable[0], 'src')
        if type == 'targ':
            sel_lable = mc.textScrollList('trgShdTSL', q=True, si=True)
            self.sel_faces(sel_lable[0], 'target')

    def update_targetList(self):
        mc.textScrollList('trgObjsTSL', e=True, ra=True)
        targs = pm.selected()
        self.targ_obj_dic.clear()
        for each in targs:
            self.targ_obj_dic[each.name()] = each
        mc.textScrollList('trgObjsTSL', e=True, append=self.targ_obj_dic.keys())

    def sel_targ_itme_cmd(self):
        self._target_shd_dict.clear()
        mc.textScrollList('trgShdTSL', e=True, ra=True)
        sel_label = mc.textScrollList('trgObjsTSL', q=True, si=True)
        pm.select(self.targ_obj_dic[sel_label[0]])
        self.add_element('targ')
        self._target_shd_dict = self._target_shd_dict

        mc.textScrollList('trgShdTSL', e=True, append=self._target_shd_dict.keys())

    def Reassing_btcmd(self):
        targ_shd = mc.textScrollList('trgShdTSL', si=True, q=True)
        source_shd = mc.textScrollList('srcShdTSL', si=True, q=True)
        self.reassing_materials(source_shd[0], targ_shd[0])
        self._source_shd_dict[source_shd[0]].values()[0]

    # def reassing_materials(self, sel_src_lb, sel_targ_lb):
    #     # sel = list_src_shd.keys()[3]
    #     sel_src_sg = self._target_shd_dict[sel_src_lb].values()[0]
    #     # targ = list_target_shd.keys()[3]#
    #     # sel_trg = self._target_shd_dict[sel_targ].values()[0]
    #     self.sel_faces(sel_targ_lb, 'target')
    #     pm.sets(sel_src_sg, e=True, forceElement=True)
# ins_rs = OCT_ReaasingMatUI()
# ins_rs.update_targetList()

if __name__ == "__main__":
    octRM = OCT_ReaasingMatUI()
    octRM.call_ui()
