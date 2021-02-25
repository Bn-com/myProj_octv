#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2013-12-92013

@author: zhangben
'''
import maya.cmds as mc
import re
import os
import maya.mel as mel
import idmt.maya.DOD.DODIV.Maya.commonProperties as docp


def do_config_miarmy_cacheParameter(projectName, drive=u'L:'):
    MiarmyCachePath = ur'%s\Projects\%s\Project\data\Miarmy_CACHE' % (drive, projectName)

    arnoldPath = ur'\\file-cluster\gdc\Resource\Support\Basefount\Miarmy2.5.01\bin\mtoa024'

    mcdGl_node = mc.ls(type=u'McdGlobal')

    if not mc.pluginInfo(u'MiarmyProForMaya2012.mll', q=True, loaded=True):
        mc.loadPlugin(u'MiarmyProForMaya2012.mll')

    str(MiarmyCachePath)

    fnsplt = docp.getShotInformation()

    shotInfo = u'shot_%s_%s' % (fnsplt[u'sq_num'], fnsplt[u'sc_num'])

    agent_cache_path = ur'%s\AGN_CACHE\%s' % (MiarmyCachePath, shotInfo)
    if not os.path.isdir(agent_cache_path):
        os.mkdir(agent_cache_path)
    mc.setAttr(u'%s.cacheFolder' % mcdGl_node[0], agent_cache_path, type='string')
    mc.setAttr(u'%s.cacheName' % mcdGl_node[0], u'agentCache', type=u'string')

    arnold_cache_path = ur'%s\ARN_CACHE\%s' % (MiarmyCachePath, shotInfo)
    if not os.path.isdir(arnold_cache_path):
        os.mkdir(arnold_cache_path)
    mc.setAttr(u'%s.outARFd' % mcdGl_node[0], arnold_cache_path, type=u'string')
    mc.setAttr(u'%s.outARNm' % mcdGl_node[0], u'arnCache', type=u'string')
    mc.setAttr(u'%s.arProc' % mcdGl_node[0], arnoldPath, type=u'string')

    md_cache_path = ur'%s\MD_CACHE\%s' % (MiarmyCachePath, shotInfo)
    if not os.path.isdir(md_cache_path):
        os.mkdir(md_cache_path)
    mc.setAttr(u'%s.outMD2Folder' % mcdGl_node[0], md_cache_path, type=u'string')
    mc.setAttr(u'%s.outMD2Name' % mcdGl_node[0], u'mdCache', type=u'string')

if __name__ == "__main__":
    do_config_miarmy_cacheParameter(u'DiveollyDive4')
