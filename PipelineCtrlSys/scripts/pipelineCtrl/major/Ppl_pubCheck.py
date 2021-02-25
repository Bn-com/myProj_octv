#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = 'pc_checkinCommon'    
__author__ = zhangben
__mtime__ = 2018/12/7:12:00
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
'''
import maya.cmds as mc
import pymel.core as pm
import maya.mel as mel
import tempfile,re,os

class Pc_pubCheck(object):
    def __init__(self):
        self.scene_nm = pm.sceneName()
        # 全流程用
    def checkDonotNodeCleanBase(self, unuse=1, turtle=1):#清理场景中的未知节点
        # 清理unusedNodes
        if unuse == 1:
            mel.eval('MLdeleteUnused')
        # 清理未知节点
        unknownNodes = mc.ls(type='unknown')
        if unknownNodes:
            for node in unknownNodes:
                if mc.ls(node):
                    mc.lockNode(node, l=0)
                    mc.delete(node)
        # 清理海龟节点
        turtleNodes = mc.ls(type='ilrBakeLayer') + mc.ls(type='ilrUIOptionsNode') + mc.ls(
            type='ilrOptionsNode') + mc.ls(type='ilrBakeLayerManager')
        if turtle and turtleNodes:
            for node in turtleNodes:
                # 非参考才执行删除
                if mc.referenceQuery(node, inr=1):
                    pass
                else:
                    if mc.ls(node):
                        mc.lockNode(node, l=0)
                        mc.delete(node)
    @staticmethod
    def check_texPath(addSet=False, wr=False, refDet=False):#check all file nodes texture path ======================
        all_f_nds = pm.ls(type='file')
        re_crtPth = re.compile(u"(Z:/Themes/)|(//octvision.com/CG/Themes)|(${OCTV_PROJECTS})")
        inproperDic = {"Nodes": [], "References": {}}
        for eaf in all_f_nds:
            ftn = eaf.attr('fileTextureName')
            if re_crtPth.search(ftn.get()): continue
            #print("|||||||PC Check Echo 002 === Texture path issue ----fileNode::{} ---{}".format(eaf.name(), ftn.get()))
            if eaf.isReferenced():
                ref_f = eaf.referenceFile()
                if ref_f.refNode in inproperDic['References']:
                    inproperDic['References'][ref_f.refNode].append("{}::{}".format(eaf.name(), ftn.get()))
                else:
                    inproperDic['References'][ref_f.refNode] = ["{}::{}".format(eaf.name(), ftn.get())]
            else:
                inproperDic['Nodes'].append("{}::{}".format(eaf.name(), ftn.get()))
        if addSet:
            if pm.PyNode(u'PC_InproperTexturePath').exists(): pm.delete(pm.PyNode(u'PC_InproperTexturePath'))
            inprpPathSet = pm.sets(name='PC_InproperTexturePath', em=True)
            addRef_List = [pm.PyNode(ea_elment.split("::")[0]) for ea_elment in inproperDic['References'][ea] for ea in inproperDic['References']]
            addRef_List = [addRef_List[n] for n in range(len(addRef_List)) if addRef_List[n] not in addRef_List[:n]]
            addNodes_lst = [ea.split("::")[0] for ea in inproperDic['Nodes']]
            addNodes_lst = [addNodes_lst[n] for n in range(len(addNodes_lst)) if addNodes_lst[n] not in addNodes_lst[:n]]
            inprpPathSet.addMembers(addRef_List)
            inprpPathSet.addMembers(addNodes_lst)
        if wr:
            curProjPath = pm.workspace.path
            rf_dir = os.path.abspath(os.path.join(curProjPath, 'scenes'))
            scene_nm = pm.sceneName().basename()
            wr_str = ""
            stro_refPath = []
            for ea in ['References','Nodes']:
                wr_str += u"NEED TO CHECK【{}】 INCLUDE: {}".format(ea.upper(), os.linesep)
                if ea == 'References':
                    for each in inproperDic[ea]:
                        if not refDet:
                            ref_f_path = each.referenceFile().path
                            if ref_f_path.strip() not in stro_refPath:
                                wr_str += "\t{} :: {}{}".format(ref_f_path.basename().strip(), ref_f_path, os.linesep)
                                stro_refPath.append(ref_f_path.strip())
                        else:
                            wr_str += "\t{} ::: {}{}".format(each.name(), each.referenceFile(), os.linesep)
                            for ea_itme in inproperDic[ea][each]:
                                wr_str += "\t\t{0}{2}\t\t[texture path]:{2}\t\t{1}{2}".format(
                                    ea_itme.split("::")[0], ea_itme.split("::")[1], os.linesep)
                else:
                    for ea_itme in inproperDic[ea]:
                        wr_str += "\t{0}{2}\t[texture path]:{2}\t{1}{2}".format(ea_itme.split("::")[0],ea_itme.split("::")[1],os.linesep)
            wf_path = u"{}\\{}_improperTextrePathNodes.txt".format(rf_dir, scene_nm.split('.')[0])
            wf = open(wf_path, 'w')
            wf.write(wr_str)
            wf.close()
            os.startfile(wf_path)

    @staticmethod
    def opminizeRef(ref_lst):
        # ref_lst = pm.listReferences()
        refFils = []
        storPath = []
        for each_ref in ref_lst:
            # each_ref = pm.listReferences()
            if each_ref.path.strip() not in storPath:
                refFils.append(each_ref)
                storPath.append(each_ref.path.strip())
        return refFils




