#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = 'Kits4Rnd.py'
__author__ = zhangben
__mtime__ = 2019/1/2:11:34
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
'''
import re,os
import maya.cmds as mc
import pymel.core as pm


class Kits4Rnd(object):
    def __init__(self):
        self.safeCounter = 0
    @staticmethod
    def wrt_file(lst, fileName):#把列表写到文件
        f = open(fileName, 'w')
        print("===iter===check 001============")
        for each in lst:
            f.write("{}{}".format(each, os.linesep))
        f.close()
    @staticmethod
    def get_unltxt(rdFile, baseName=True):#通过渲染日志获得没有load的贴图，返回贴图文件名字列表
        tx_name_list = []
        rdf = open(os.path.abspath(rdFile), 'r')
        rls = rdf.readlines()
        rdf.close()
        print("===iter===check 002============")
        for line in rls:
            # print line
            if re.search("unloaded.{}$".format(os.linesep), line) and re.search("\"\S+\"", line, re.I):
                # print line
                tx_file = re.search("\"\S+\"", line, re.I).group()
                if baseName:
                    tx_name_list.append(os.path.split(re.sub("\"", "", tx_file, re.I))[1])
                else:
                    tx_name_list.append(re.sub("\"", "", tx_file, re.I))
        return tx_name_list
    def get_meshes_from_tex(self,txFileList):#通过 texure 名字的列表 获得场景中对应的物体
        meshesList = []
        print("===iter===check 003============")
        for each_tx in txFileList:
            file_nodes = self.getFileNodeFrTx(each_tx)
            print("===iter===check 004============")
            for each_f in file_nodes:
                meshesList.extend(self.getDgsFrFilenode(each_f))
        print("===iter===check 005============")
        meshesList = [meshesList[n] for n in range(len(meshesList)) if meshesList[n] not in meshesList[:n]]
        return meshesList
    # @staticmethod
    def getFileNodeFrTx(self,txFile_nm):#通过贴图名字获得file节点的名字
        print("===iter===check 006============")
        file_nodes = [eaf for eaf in pm.ls(type='file') if eaf.attr('fileTextureName').get().find(txFile_nm) != -1]
        if not len(file_nodes): print("============can't find the file node connected to {}".format(txFile_nm))
        return file_nodes
    # @staticmethod
    def getDgsFrFilenode(self,file_node_nm):# 通过贴图节点获得SG节点
        # getMats = []
        # getSGs = []
        getDGs = []
        if not isinstance(file_node_nm, pm.nodetypes.File): file_node_nm = pm.PyNode(file_node_nm)
        oc_attr = file_node_nm.attr('outColor')
        getMats = oc_attr.connections()
        getSGs = self.getSG(getMats, [])
        if not getSGs: return None
        print("===iter===check 007============on file node [{}]".format(file_node_nm))
        for eaSg in getSGs:
            if eaSg.connections(type='mesh'): getDGs.extend(eaSg.connections(type='mesh'))
        return getDGs

    def getSG(self, mts, res_sgs):  # 获得某个材质球所关联的SG节点
        # new_mts = []
        # each = pm.selected()[0]
        # if self.safeCounter > 50: return None
        print("===iter===check 008============")
        for each in mts:
            print("||||||||||Check {}|||||||||||||||".format(each))
            if each.type() == 'shadingEngine':
                res_sgs.append(each)
            else:
                # if each.hasAttr('outColor'):
                print("=========now check node ========={}".format(each.name()))
                tem_mts_01 = each.listConnections(d=True, s=False, scn=True)
                if not len(tem_mts_01): return None
                # tem_mts_01[3].type()
                print("===iter===check 009============")
                tem_mts = [eaMat for eaMat in tem_mts_01 if eaMat.type() not in ['materialInfo', 'defaultShaderList', 'nodeGraphEditorInfo']]
                if not len(tem_mts):
                    print("+++++++Node have no desti nodes+++++".format(each.name()))
                    return None
                self.safeCounter += 1
                print tem_mts
                self.getSG(tem_mts, res_sgs)
        return res_sgs

    # @staticmethod
    # def getSG(self,mts, res_sgs):#获得某个材质球所关联的SG节点
    #     # new_mts = []
    #     for each in mts:
    #         if not each.hasAttr('outColor') and each.type() == 'shadingEngine':
    #             res_sgs.append(each)
    #         else:
    #             # if each.hasAttr('outColor'):
    #             print("=========now check node ========={}".format(each.name()))
    #             tem_mts = each.attr('outColor').connections()
    #             self.getSG(tem_mts, res_sgs)
    #             # elif each.hasAttr('output'):
    #             #     # tem_mts = each.attr('output').connections()
    #             #     # self.getSG(tem_mts, res_sgs)
    #             #     print("===OutPut==={}".format(each.name()))
    #             #     continue
    #             # else:
    #             #     print each
    #             #     continue
    #     return res_sgs
    # sgnds = []
    # while (a):
    #     for each in getMats:
    #         if each.hasAttr('outColor'):
    #             dstNds = each.attr('outColor').connections()
    #             for each_dest in dstNds:
    #                 if each_dest.hasAttr('outColor'):
    #                     each_dest = each.attr('outColor').connections()
    #
    #         else:
    #             a = False
    # def test(num):
    #     re_lst = []
    #     for ea in range(num):
    #         if ea == 0:
    #             re_lst.append(ea)
    #         else:
    #             temp = ea
    #             test(tem)
    #     return re_lst
#
#
# #import pymel.core as pm
# import os
#
# allfns = pm.ls(type='file')
# #cprj = pm.workspace(fn=True,q=True)
# fn = pm.sceneName()
# rec_tx_fn_f = "{}/{}_textrue_data.txt".format(fn.dirname().strip(),fn.basename().splitext()[0].strip())
# wf = open(rec_tx_fn_f,'w')
# for eaf in allfns:
#     tx_path = eaf.attr('fileTextureName').get()
#     wf.write('{}::{}{}'.format(eaf.name(),tx_path,os.linesep))
# wf.close()
#
#
# #
# #
#
#
# allFs = pm.ls(type='file')
# tx_unex = []
# for each in allFs:
#     tx_path = each.attr('fileTextureName').get()
#     tx_path_spl = os.path.split(tx_path)
#     quarter_path = "{}/1_4{}".format(tx_path_spl[0], tx_path_spl[1])
#     if os.path.isfile(quarter_path):
#         print("OK!!!!{}".format(quarter_path)
#               else:
#               tx_unex.append(each)
#         print("No Texture==={}".format(quarter_path)


#===================== for arnold stand in  render visibility =========================
#
# import pymel.core as pm
#
# #render_vis = False
#
# set_aiStd_rndVis(1) #   1 可以渲染  0  不可渲染
# def set_aiStd_rndVis(render_vis):
#     aiStdNds = pm.ls(type='aiStandIn')
#     aiAtrLst = ['aiVisibleInDiffuse','aiVisibleInGlossy','overridePrimaryVisibility','overrideCastsShadows',
#     'overrideReceiveShadows','overrideVisibleInReflections','overrideVisibleInRefractions']
#     for eaStd in aiStdNds:
#         eaStd.attr('primaryVisibility').set(render_vis)
#         eaStd.attr(aiAtrLst[2]).set(not render_vis)









              # test(3,[])
# def test(num,re_lst):
#     for ea in range(num):
#         if ea == 0:
#             re_lst.append(ea)
#         else:
#             temp = ea
#             test(temp,re_lst)
#     return re_lst