#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on '2015/10/15'
@author = 'zhangben'

'''
import maya.mel as mel
import maya.cmds as mc
from pymel.core import *
import re, os, sys
class mi_bookReplaceTools():
    im_sorce_geo_grps = ''
    def __init__(self):
        pass
    def con2relPath_mbrt(self, uiF_Name,winName):
        scriptFolder = os.path.normpath(os.path.dirname(__file__))
        ui_path = os.path.join(scriptFolder,u'UI\\%s' % (uiF_Name))
        if mc.window(winName,exists=True): mc.deleteUI(winName)
        proc_win = mc.loadUI(uiFile = ui_path)
        mc.windowPref(proc_win,tlc = (300,180))
        mc.showWindow(proc_win)
    def im_bookFile_btcmd(self):
        mi_bookReplaceToolsim_file_path = ur'\\file-cluster\GDC\Projects\MiniTiger\Project\scenes\props\p005002BookB\master\mi_p005001Book_h_ms_render.mb'
        mi_bookReplaceTools.im_sorce_geo_grps = self.im_bookFile(mi_bookReplaceToolsim_file_path)
    def dup_btcmd(self):
        self.dup_operation(selected())
    def del_btcmd(self):
        delete(mi_bookReplaceTools.im_sorce_geo_grps)
    def im_bookFile(self,im_file_path):
        #========import hi mode file and tidy members============================
        #im_file_path = ur'E:\MiniTiger\book\scenes\mi_p005001Book_h_ms_render.mb'
        #im_file_path = ur'E:\MiniTiger\book\scenes\im_testCube.mb'
        tempNS = 'imCB'
        system.importFile(im_file_path,namespace=tempNS)
        hi_bookGRP = ls('%s:MSH_c_hi_book' % tempNS)
        #hi_bookGRP[0].getChildren()
        #dir(hi_bookGRP[0])
        set_mshGrp = [mshGrp for mshGrp in ls('MSH_all') if mshGrp.root() == 'SET']
        #==========storage hi mode geo groups lists,for del them later=========================
        record_geo_grps = [eachChild for eachChild in hi_bookGRP[0].listRelatives(c=True,ad=True) if eachChild.shortName().find('_geo') != -1]
        if not objExists(hi_bookGRP[0].nodeName().split(':')[-1]):hi_bookGRP[0].setParent(set_mshGrp[0])
        else:
            for each_book in record_geo_grps:
                im_book_parent = each_book.getParent()
                book_p_nodeName = '%s'%(im_book_parent.split(':')[-1])
                if objExists(book_p_nodeName):
                    each_book.setParent(PyNode(book_p_nodeName))
                else:
                    im_book_parent.setParent(set_mshGrp[0])
        delete('imCB:PROP')
        setsLs = ['smooth_0','smooth_1','smooth_2','CURVES','MESHES','CTRLS'] # move setMembers of imported file to source
        for eachSets in setsLs:#pass
            imSets  = '%s:%s' % (tempNS,eachSets)
            if sets(imSets,q=True):
                sets(eachSets,addElement = sets(imSets,q=True))
                sets(imSets,clear=True)
        allImSets = [eachOne for eachOne in ls(exactType='objectSet') if eachOne.name().find(tempNS) != -1]
        delete(allImSets)
        self.remove_specialNS("imCB")
        return record_geo_grps
    #================tidy members OK!!!====================================
    # duplicate operation:
    def dup_operation(self,targetBooks):
        targetBooks = selected()
        source_book_geoGrps =[]
        for eachSel in targetBooks:
           # eachSel = selected()[0]
            if eachSel.nodeName().find('_geo') == -1:
               sel_book_geoGrp_ls = [each for each in eachSel.getAllParents() if each.nodeName().find('_geo') != -1]
               if sel_book_geoGrp_ls: source_book_geoGrps.append(sel_book_geoGrp_ls[0])
               else: error("你选择了物体不是切其父层级也不是geo组")
            else:
               source_book_geoGrps.append(eachSel)
        source_book_geoGrps_opt = [source_book_geoGrps[i] for i in range(len(source_book_geoGrps)) if source_book_geoGrps[i] not in source_book_geoGrps[:i]]
        for source_book_geoGrp in source_book_geoGrps_opt:
            replace_book_geoGrpName = ''
            if source_book_geoGrp.nodeName().find('_lo_') != -1: replace_book_geoGrpName = source_book_geoGrp.nodeName().replace('_lo_','_hi_')
            elif source_book_geoGrp.nodeName().find('_hi_') != -1: replace_book_geoGrpName = source_book_geoGrp.nodeName().replace('_hi_','_lo_')
            replace_book_geoGrp = duplicate(PyNode(replace_book_geoGrpName),inputConnections=True)[0]
            replace_book_geoGrp.translate.set(tuple(source_book_geoGrp.translate.get()))
            replace_book_geoGrp.rotate.set(tuple(source_book_geoGrp.rotate.get()))
            replace_book_geoGrp.scale.set(tuple(source_book_geoGrp.scale.get()))
            delete(source_book_geoGrp)
            print '%s DELED' % source_book_geoGrp
    def remove_specialNS(self,rm_ns):
        Namespace(":").setCurrent()
        #Namespace(rm_ns).listNodes()
        Namespace(rm_ns).move(":",force=True)
        Namespace(rm_ns).remove()
    def im_file_proc(self,im_file_path):
        im_geoGrp_letter = u'MSH_geo'
        need_key_char_lst = u'icon',u'myuis'
        #source_geoGrp_letter_lst =[ u'MSH_c_l_%s_all' % eachKey for eachKey in need_key_char_lst]
        geoGrp_key = u'_all'
        source_geo_parent_grp = []
        for eachOne in need_key_char_lst:
            if ls(u'*:*%s%s'%(eachOne,geoGrp_key)): source_geo_parent_grp.extend(ls(u'*:*%s%s'%(eachOne,geoGrp_key)))
        #=======get source set group namespace =====================
        source_ns = source_geo_parent_grp[0].namespace()
        #========im port hi mode file and tidy members============================
        im_file_path = ur'\\file-cluster\GDC\Projects\MiniTiger\Project\scenes\props\p053002Trash\master\mi_p053002Trash_h_ms_render.mb'
        #im_file_path = ur'\\file-cluster\GDC\Projects\MiniTiger\Project\scenes\props\p005001Book\master\mi_p005001Book_h_ms_render.mb'
        #im_file_path = ur'E:\MiniTiger\book\scenes\im_testCube.mb'
        tempNS = 'imCB'
        system.importFile(im_file_path,namespace=tempNS)
        im_getGrp = ls('%s:%s'% (tempNS,im_geoGrp_letter))
        p_modeKeyChar = re.compile(u'|'.join([u'(%s)' % each for each in need_key_char_lst]))
        #==========storage hi mode geo groups lists,for del them later=========================
        import_geo_grps = [eachChild for eachChild in im_getGrp[0].listRelatives(c=True,ad=True) if eachChild.shortName().find('_geo') != -1 and p_modeKeyChar.search(eachChild.shortName())]
        #set_mshGrp = [mshGrp for mshGrp in ls('MSH_all') if mshGrp.root() == 'SET']
        for each_sour_geo in source_geo_parent_grp:
            for each_im_geo in import_geo_grps:
                p_key = re.compile(u'(myuis)|(icon)')
                if p_key.search(each_sour_geo.name()):
                    if p_key.search(each_im_geo.name()) and p_key.search(each_im_geo.name()).group() == p_key.search(each_sour_geo.name()).group():
                        each_im_geo.setParent(each_sour_geo)
        delete('imCB:PROP')
        selected()[0].namespace()
        setsLs = ['smooth_0','smooth_1','smooth_2','CURVES','MESHES','CTRLS'] # move setMembers of imported file to source
        for eachSets in setsLs:#pass eachSets = setsLs[-2]
            source_set = u'%s%s'%(source_ns,eachSets)
            imSets  = '%s:%s' % (tempNS,eachSets)
            if objExists(imSets) and sets(imSets,q=True):
                sets(source_set,addElement = sets(imSets,q=True))
                sets(imSets,clear=True)
        allImSets = [eachOne for eachOne in ls(exactType='objectSet') if eachOne.name().find(tempNS) != -1]
        #select(allImSets)
        delete(allImSets)
        namespace(mv=(tempNS,u'mi_s022001CastleGarbage_h'),f=True)
        return import_geo_grps
    def dup_operation(self,targetBooks):
        targetBooks = selected()
        source_book_geoGrps =[]
        for eachSel in targetBooks:
           # eachSel = selected()[0]
            if eachSel.nodeName().find('_geo') == -1:
               sel_book_geoGrp_ls = [each for each in eachSel.getAllParents() if each.nodeName().find('_geo') != -1]
               if sel_book_geoGrp_ls: source_book_geoGrps.append(sel_book_geoGrp_ls[0])
               else: error("你选择了物体不是切其父层级也不是geo组")
            else:
               source_book_geoGrps.append(eachSel)
        source_book_geoGrps_opt = [source_book_geoGrps[i] for i in range(len(source_book_geoGrps)) if source_book_geoGrps[i] not in source_book_geoGrps[:i]]
        for source_book_geoGrp in source_book_geoGrps_opt:
            replace_book_geoGrpName = ''
            p_remov_num = re.compile(u'[0-9]*$')
            if source_book_geoGrp.nodeName().find('_l_') != -1: replace_book_geoGrpName = p_remov_num.sub(u'',source_book_geoGrp.nodeName().replace('_l_','_hi_'))
            elif source_book_geoGrp.nodeName().find('_hi_') != -1: replace_book_geoGrpName = p_remov_num.sub(u'',source_book_geoGrp.nodeName().replace('_hi_','_l_'))
            source_obj_ns = source_book_geoGrp.namespace()
            dup_obj_name = u'%s%s'%(source_obj_ns,replace_book_geoGrpName)
            source_nodeNm = PyNode(replace_book_geoGrpName).stripNamespace().nodeName()
            replace_book_geoGrp = u''
            if objExists(source_nodeNm):   replace_book_geoGrp = duplicate(PyNode(replace_book_geoGrpName),inputConnections=True,n=u'%s%d'%(source_nodeNm,get_obj_idNum(source_nodeNm)+1))
            else: replace_book_geoGrp = duplicate(PyNode(replace_book_geoGrpName),inputConnections=True)
            replace_book_geoGrp.translate.set(tuple(source_book_geoGrp.translate.get()))
            replace_book_geoGrp.rotate.set(tuple(source_book_geoGrp.rotate.get()))
            replace_book_geoGrp.scale.set(tuple(source_book_geoGrp.scale.get()))
            delete(source_book_geoGrp)
            print '%s DELED' % source_book_geoGrp
            replace_book_geoGrp[0].rename(replace_book_geoGrp[0].swapNamespace(source_obj_ns).nodeName())
            for each_child in replace_book_geoGrp[0].getChildren():each_child.rename(each_child.swapNamespace(source_obj_ns).nodeName())
            print u'=======================obj duplicated : %s======================================'  %  source_book_geoGrp.name()
    def rename2specNS(self,obj,specNS):
        obj.rename(obj.swapNamespace(specNS).nodeName())

    def get_obj_idNum(self,calc_obj_nm):
        #calc_obj_nm = source_nodeNm + U'012'
        p_get_idNum = re.compile(u'[0-9]+$')
        #p_get_idNum.search(calc_obj_nm).group()
        if p_get_idNum.findall(calc_obj_nm):return int(p_get_idNum.search(calc_obj_nm).group())
        else:return int(0)

