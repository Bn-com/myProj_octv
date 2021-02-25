#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = 'PPC_ReassignMaterial.py'
__author__ = zhangben
__mtime__ = 2018/11/27:17:18
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
'''
import pymel.core as pm
import os, re
import maya.cmds as mc
import pickle
from . import run_deb
# class OCT_Reassing_materials(object):
#     """对combine后的模型，重新指定材质
#             　 有一个已经修正过材质的combine的物体，
#             　 列出场景中需要修正材质的物体，根据shader，来指定传递
#     """
#
#
reload(run_deb)
run_deb.rnd_prt()

class PPC_ReassignMatUI(object):
    def __init__(self):
        self._dst_shd_dict = {}
        self._source_shd_dict = {}
        self._dst_objs_dict = {}
        self._dst_objs_filter_dict = {}
    def refreshData(self):
        self._source_shd_dict = self._source_shd_dict

    def action_data(self,actyp='r', dtyp='dst',dstsData=None):
        # dttyp = 'src'
        tmpdir = os.getenv('TMP')
        tmpf = os.path.join(tmpdir, "_reassmt_{}.trc".format(dtyp))
        dst_shd_dataFiles = []
        if dtyp =='dsts':
            for eachObj in dstsData.keys():
                tmpf = os.path.join(tmpdir,'_octReassignMatData_{}.trc'.format(eachObj))
                dst_shd_dataFiles.append(tmpf)
        if actyp == 'w':
            if dtyp == 'dsts':
                for eaf in dst_shd_dataFiles:
                    opf = open(eaf,'w')
                    pickle.dump(dstsData.values(), opf, 1)
                    opf.close()
            else:
                opf = open(tmpf, 'w')
                if dtyp == 'src':
                    pickle.dump(self._source_shd_dict, opf, 1)
                elif dtyp == 'dst':
                    pickle.dump(self._dst_shd_dict, opf, 1)
                opf.close()
        else:
            rdf = open(tmpf, 'r')
            rd = pickle.load(rdf)
            rdf.close()
            return rd
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
        listSrcSdCmdStr = 'ins_rs = PPC_ReassignMatUI()\nins_rs.lfbt_cmd()'
        mc.button('addSource', label='List From Object shaders', p=src_clm, c=listSrcSdCmdStr)
        # ======== list selected dst objectes====================
        trg_clm = mc.columnLayout('trg_CLM', columnAttach=('both', 5), rowSpacing=10, p=main_rly, adjustableColumn=True)
        mc.textScrollList('trgObjsTSL', parent=trg_clm, sc='ins_rs.sel_dst_itme_cmd()')
        mc.button('adddst', label='To objects', p=trg_clm, c='ins_rs.update_dstList()')
        mc.textFieldButtonGrp('filterTFB',label='filter key word',buttonLabel='filter/Back',p=trg_clm,bc='ins_rs.filterBTCMD()',cw3=[80,100,120])
        # mc.setParent('..')
        # ==================list dst object's shaders=====================
        trg_lst_clm = mc.columnLayout('trg_lst_CLM', columnAttach=('both', 5), rowSpacing=10, p=main_rly,adjustableColumn=True, w=350)
        mc.text('lstTX', label='old shaders list', p=trg_lst_clm, al='left')
        mc.textScrollList('trgShdTSL', parent=trg_lst_clm, w=300,sc='ins_rs.sel_item_cmd(\'dst\')')
        mc.textFieldGrp('keywordTFG',label='keyword', text='',columnAlign=[1,'left'],columnWidth2=[75,250],w=250,p=trg_lst_clm)

        bt_grps = mc.rowLayout('bt_GRPS', numberOfColumns=3, columnWidth3=[400, 300, 300], columnOffset3=[15, 120, 60],p=main_fl)
        mc.button('atbt',label='AutoReassign[Model Match 100]', p=bt_grps, w=250,c='ins_rs.auto_reassign()')
        runbt = mc.button('runButon', label='reassign', p=bt_grps, w=250,c='ins_rs.Reassing_btcmd()')
        all_cb = mc.checkBox('allcb',label='other objects do the same ', p=bt_grps, w=150,)

        # adjust layout elements
        mc.formLayout(main_fl, edit=True, attachForm=[(main_rly, 'top', 5)],attachControl=[(bt_grps, 'top', 15, main_rly)])

        mc.window(main_win, e=True, wh=(850, 300), rtf=True,sizeable=False)
        mc.showWindow(main_win)

    # ins_reasign = OCT_Reassing_materials()

    def add_element(self, express='src'):#====add element 2 instance variable and out put data to disk=============
        if express == 'src':
            self._source_shd_dict.clear()
            self._source_shd_dict = self.list_AllShaders(pm.selected()[0])
            self.action_data('w','src')
        else:
            self._dst_shd_dict.clear()
            self._dst_shd_dict = self.list_AllShaders(pm.selected()[0])
            self.action_data('w','dst')

    def reassing_materials(self, sel_src_lb, sel_dst_lb):# reassign materials by selected shaders,including source and destinatte
        # sel = list_src_shd.keys()[3]
        sel_src_sg = self.action_data('r','src')[sel_src_lb].values()[0]
        # dst = list_dst_shd.keys()[3]#
        # sel_trg = self._dst_shd_dict[sel_dst].values()[0]
        self.sel_faces(sel_dst_lb, 'dst')
        pm.sets(sel_src_sg, e=True, forceElement=True)

    def list_AllShaders(self, specObj, ignorID=False):
        """
        :param specObj: specify object is the DAG Shape node
        :param ignorID:
        :return: return a dict ,key is the shader's name, key is a dict too
        """
        # specObj = pm.selected()[0]
        print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
        if specObj.type() != u'mesh': specObj = specObj.getShape()
        print specObj.name()
        ls_sgs = specObj.listConnections(type='shadingEngine')
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

    def sel_faces(self, sel_shd_label, type='dst'):  # select faces based on selected labels.
        if type == 'dst':
            sel_sg = self.action_data('r','dst')[sel_shd_label].values()[0]
            pm.select(pm.sets(sel_sg, q=True), r=True)
        else:
            sel_sg = self.action_data('r','src')[sel_shd_label].values()[0]
            pm.select(pm.sets(sel_sg, q=True), r=True)

    # ins_reasign = OCT_Reassing_materials()

    def lfbt_cmd(self):
        mc.textScrollList('srcShdTSL', e=True, ra=True)
        self.add_element('src')
        src_shd_dct = self.action_data('r','src')
        mc.textScrollList('srcShdTSL', e=True, append=src_shd_dct.keys())

    def sel_item_cmd(self, type='src'):

        if type == 'src':
            sel_lable = mc.textScrollList('srcShdTSL', q=True, si=True)
            self.sel_faces(sel_lable[0], 'src')
        if type == 'dst':
            sel_lable = mc.textScrollList('trgShdTSL', q=True, si=True)
            self.sel_faces(sel_lable[0], 'dst')
            mc.textFieldGrp('keywordTFG',e=True,text=PPC_ReassignMatUI.autoFindKeywords(sel_lable[0]))

    def update_dstList(self):
        mc.textScrollList('trgObjsTSL', e=True, ra=True)
        dsts_sel = pm.selected()
        dsts = []
        for each in dsts_sel:
            # eachMeshes_0 = each.listRelatives(s=True,ni=True,type='mesh',ad=True)
            eachMeshes = each.listRelatives(ad=True,type='mesh',ni=True)
            # print eachMeshes
            # pm.select(eachMeshes[1])
            for eachMesh in eachMeshes:
                dsts.append(eachMesh)
        dsts = [dsts[n] for n in range(len(dsts)) if dsts[n] not in dsts[:n]]
        self._dst_objs_dict.clear()
        dsts_cont= {}
        for each in dsts:
            # if not each.getShape():
            #     each = each.listRelatives(ad=True,s=True,type='mesh',ni=True)[0]
            self._dst_objs_dict[each.name()] = each
            temp_nm = re.sub('\|','____',each.name())
            objs_nm_legal = re.sub(':', '_____', temp_nm)
            # print("========================start list shaders ===============")
            dsts_cont[objs_nm_legal] = self.list_AllShaders(each)
            print("=====================objects listed======================")
            self.action_data('w', 'dsts',dsts_cont)
            dsts_cont.clear()
        mc.textScrollList('trgObjsTSL', e=True, append=self._dst_objs_dict.keys())
    def filterBTCMD(self):
        cur_lst = self._dst_objs_dict.keys()
        mc.textScrollList('trgObjsTSL',e=True,ra=True)
        filterKw = mc.textFieldButtonGrp('filterTFB', q=True, text=True)
        if not filterKw:
            mc.textScrollList('trgObjsTSL', e=True, append = self._dst_objs_dict.keys())
            return
        for ea_nm in cur_lst:
            if re.search(filterKw,ea_nm):
                self._dst_objs_filter_dict[ea_nm] = self._dst_objs_dict[ea_nm]
                mc.textScrollList('trgObjsTSL',e=True,append =ea_nm)



    def sel_dst_itme_cmd(self):
        self._dst_shd_dict.clear()
        mc.textScrollList('trgShdTSL', e=True, ra=True)
        sel_label = mc.textScrollList('trgObjsTSL', q=True, si=True)
        pm.select(self._dst_objs_dict[sel_label[0]])
        self.add_element('dst')
        # self._dst_shd_dict = self._dst_shd_dict

        mc.textScrollList('trgShdTSL', e=True, append=self.action_data('r','dst').keys())

    def Reassing_btcmd(self):
        dst_shd = mc.textScrollList('trgShdTSL', si=True, q=True)
        source_shd = mc.textScrollList('srcShdTSL', si=True, q=True)
        source_shd_obj = self.action_data('r', 'src')[source_shd[0]]
        source_sg = source_shd_obj.values()[0]
        self.reassing_materials(source_shd[0], dst_shd[0])
        self.action_data('r','src')[source_shd[0]].values()[0]

        if mc.checkBox('allcb', q=True, value=True):
            curt_obj = mc.textScrollList('trgObjsTSL', q=True, si=True)[0]
            othObjs = [each for each in self._dst_objs_dict if each != curt_obj]
            tmpdir = os.getenv('TMP')
            for each in othObjs:
                temp_nm = re.sub('\|', '____', each)
                dt_filename = re.sub(':', '_____', temp_nm)
                dt_filename_f = os.path.join(tmpdir, '_octReassignMatData_{}.trc'.format(dt_filename))
                if os.path.isfile(dt_filename_f):
                    rdf = open(dt_filename_f, 'r')
                    dts = pickle.load(rdf)[0]
                    rdf.close()

                # kw = PPC_ReassignMatUI.autoFindKeywords(dst_shd[0])
                kw  = mc.textFieldGrp('keywordTFG',q=True,text=True)
                for eachSd in dts:
                    listSd = dts[eachSd].keys()[0]
                    nd_shnm = listSd.name(stripNamespace=True)
                    des_SG = ''
                    if re.search(kw, nd_shnm):
                        des_SG = dts[eachSd].values()[0]
                        pm.select(pm.sets(des_SG, q=True))
                        pm.sets(source_sg, e=True, forceElement=True)
            mc.confirmDialog(title='Confirm',message='Reassigned materials',button=['Okey'])

    @staticmethod
    def autoFindKeywords(namestr):
        spltNm = namestr.split('_')
        if len(spltNm) == 1:
            return re.search('[a-zA-Z]+', namestr).group()
        else:
            return re.search('[a-zA-Z]+', spltNm[-2]).group()

    @staticmethod
    def auto_reassign():
        selObjs = pm.selected()

        src_obj = selObjs[0]
        src_sds = PPC_ReassignMatUI.list_AllShaders(selObjs[0])
        des_objs = selObjs[1:]

        for eachShd in src_sds:
            SG_nd = src_sds[eachShd].values()[0]

            setsmb = pm.sets(SG_nd, q=True)
            src_faces_nm = ''
            for eachMb in setsmb:
                if eachMb.node() == src_obj.getShape():
                    src_faces = eachMb
                    src_faces_nm = src_faces.name()
            faces_ids = src_faces_nm.split('.')[-1]
            pm.select(src_faces_nm)
            for eachDes in des_objs:
                eaShp = eachDes.getShape()
                des_fac_obj = pm.PyNode("{}.{}".format(eaShp, faces_ids))
                pm.select(des_fac_obj, r=True)
                pm.sets(SG_nd, e=True, forceElement=True)
if __name__ == "__main__":
    octRM = PPC_ReassignMatUI()
    octRM.call_ui()
