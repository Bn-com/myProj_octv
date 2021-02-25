#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on '2015/11/25'
@author = 'zhangben'

'''
import maya.mel as mel
import maya.cmds as mc
from pymel.core import *
import re, os, sys

def hs_im_cache():
    cache_path = ur'E:/MiniTiger/SQ_990/SC_9990/cache/nCache/mi_hiarCacheTest_anim_follicleDifrentSet'
    for each_hs in ls(exactType = 'hairSystem'):
        each_hs_cache_name = '%s.xml' % (each_hs.name())
        each_hs_cf = '%s/%s' % (cache_path,each_hs_cache_name)
        select(each_hs)
        if each_hs.listConnections(type = 'cacheFile'): mel.eval('deleteCacheFile 3 { "keep", "", "nCloth" } ;')
        if os.path.exists(each_hs_cf):
            im_cache_cmd = 'doImportCacheFile \"%s/" \"xml\" {} {} ' % (each_hs_cf)
            mel.eval(im_cache_cmd)
def mi_generate_txfile():
    mel.eval('source \"zwImgcvt\"')
    file_nodes = ls(exactType = 'file')
    for each_fn in ls(exactType = 'file'):
        sourceImagePath = each_fn.attr('fileTextureName').get()
        targetImagePath = u'%s.tx'%(os.path.splitext(sourceImagePath)[0])
        mel.eval('zwImgcvt \"' + sourceImagePath + '\" \"' + targetImagePath + '\"')
def mi_phong2aiStnd():
    all_phongs = ls(type = u'phong')
    for each_ph in ls(type=u'phong'):
        select(each_ph,r=True)
        mel.eval('hyperShade -objects \"\"')
        if selected():
            con_obj = selected()[0]
            print con_obj
            con_fileOutClr_ls = each_ph.attr(u'color').listConnections(d=True,p=True,scn=True,s=True)
            con_fileOutClr = ''
            if con_fileOutClr_ls: con_fileOutClr = con_fileOutClr_ls[0]
            new_SHD = '%sshader'%con_obj.getParent().name().upper()
            new_SG = '%sSG'%con_obj.getParent().name().upper()
            if objExists(new_SHD): delete(new_SHD)
            if objExists(new_SG): delete(new_SG)
            mc.shadingNode('aiStandard', asShader=True,n=new_SHD)
            mc.sets(renderable=1,noSurfaceShader=1,em=1,n=new_SG)
            PyNode(new_SHD).outColor >> PyNode(new_SG).surfaceShader
            sets(new_SG,e=1, forceElement = con_obj )
            con_fileOutClr >> PyNode(new_SHD).color
            PyNode(new_SHD).Ks.set(0.1)
            #delete(ls(type = u'phong'))
def mi_batch_savefile(excuteFuntion,storPath):
    fn = sceneName()
    shortName = os.path.split(fn)[-1]
    d_temp_folder = ur'd:\minitiger_tempSaveFile'
    stor_folder = os.path.join(d_temp_folder,storPath)
    if not os.path.isdir(stor_folder):os.makedirs(stor_folder)
    save_file_path_new = os.path.join(stor_folder,shortName)
    eval(excuteFuntion)
    mc.file(rn = save_file_path_new)
    saveFile()
    print u'File alembic cache node \'abc_File\' attribute modified!!!!!!'
def mi_modification_abcFilePathAttr(amendDriver = u'z:/Projects'):
    abcNode = ls(type = u'AlembicNode')
    if abcNode:
        for each_abcnode in abcNode:
            abcFile_path = each_abcnode.attr(u'abc_File').get() #\\file-cluster\GDC
            #abcFile_path = abcNode[0].attr(u'abc_File').get() #\\file-cluster\GDC
            p_pathPrefix = re.compile(u'(//file-cluster/GDC/Projects)|(L:/Projects)',re.I)
            modify_path = p_pathPrefix.sub(amendDriver,abcFile_path)
            each_abcnode.attr(u'abc_File').set(modify_path)
            print u'node: %s  abc_file attribute modified value == %s' % (each_abcnode,modify_path)
