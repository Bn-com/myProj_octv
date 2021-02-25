# -*- coding: utf-8 -*-

'''
Created on 2016-08-29

@author: 陈嘉伟
'''
import maya.cmds as mc
import maya.mel as mel
from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
reload(sk_infoConfig)


def CJW_CheckinClean():
    # 错误检测，根据阶段不同而不同
    # 检测是否有非法MODEL组,组后是否有跟数字
    for i in range(0, 9):
        grps = mc.ls('MODEL' + str(i) + '*')
        if not grps:
            continue
        else:
            mc.warning(u'【！！！请检查MODEL组命名,后不能有数字！！！】========================')
            mc.error(u'【！！！请检查MODEL组命名！！！】========================')
    # 检测MODEL组重系列
    model = mc.ls('MODEL',l=1)
    if not model:
        mc.warning(u'【！！！MODEL不存在，请检查！！！】========================')
        mc.error(u'【！！！MODEL不存在，请检查！！！】========================')
    if len(model) > 1:
        mc.warning(u'【！！！MODEL组不止一个，请检查！！！】========================')
        mc.error(u'【！！！MODEL组不止一个，请检查！！！】========================')
    if len(model[0].split('|')) !=3:
        mc.warning(u'【！！！MODEL位置不对，请检查文件！！！】========================')
        mc.error(u'【！！！MODEL位置不对，请检查文件！！！】========================')

def CJW_renovateNCache():
    nCacheFileNames = mc.ls(type='cacheFile')
    for nCacheFileName in nCacheFileNames:
        cacheName = mc.getAttr(nCacheFileName+'.cacheName')
        if '_h_ms_anim_' in cacheName:
            new = cacheName.replace('_h_ms_anim_','_')
            try:
                mc.setAttr(nCacheFileName+'.cacheName',new,type='string')
            except:
                pass
        if '_h_ms_render_' in cacheName:
            new = cacheName.replace('_h_ms_render_','_')
            try:
                mc.setAttr(nCacheFileName+'.cacheName',new,type='string')
            except:
                pass