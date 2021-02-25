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
    def im_bookFile_btcmd(self):
        mi_bookReplaceToolsim_file_path = ur'E:\MiniTiger\book\scenes\mi_p005001Book_h_ms_render.mb'
        mi_bookReplaceTools.im_sorce_geo_grps = self.im_bookFile(im_file_path)
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
            replace_book_geoGrp = duplicate(PyNode(replace_book_geoGrpName))[0]
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




