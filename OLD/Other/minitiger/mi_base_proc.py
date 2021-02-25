#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on '2015/11/26'
@author = 'zhangben'

'''
import maya.mel as mel
import maya.cmds as mc
from pymel.core import *
import re, os, sys,time
import py_compile

# 规则
# 相机只有一个的时候，不得有near,mid,far信息
# 多余一个相机的时候，必须有near,mid,far的信息
def mi_sl_checkin_clean():
    sfn_ls = sceneName().stripext().basename().split('_')
    exact_cam_nm = 'cam_%s_%s'%(sfn_ls[1],sfn_ls[2])
    keyList = ['near','mid','far']
    #stereo_CentCam_shp = ls(exactType = 'stereoRigCamera')
    stereo_CentCam_shp = mc.ls(type = 'stereoRigCamera',l=1)
    stereo_CentCam_Grp = []
    if stereo_CentCam_shp:
        stereo_CentCam_Grp = mc.listRelatives(stereo_CentCam_shp,p=1,type = 'transform',f=1)
    if not stereo_CentCam_Grp:
        stereo_CentCam_Grp = []
    erro_info = []
    infoNoCam = u'=======================文件没有相机,请注意检查======================='
    infoErrorCam = u'=======================场景里的camera名与文件名不匹配======================='
    infoSingleCam = u'=======================单一相机不得有near,mid,far======================='
    infoMulCam = u'=======================多个相机必须仅有near,mid,far======================='
    isValueError = '=======================中间立体相机的interaxialSeparation属性值不应该是默认的6.350======================='
    zvValueError = '=======================中间立体相机的zeroParallax属性值不应该是默认的254======================='
    # 名字检测
    if not stereo_CentCam_Grp:
        erro_info.append(infoNoCam)
    else:
        if len(stereo_CentCam_Grp) == 1:
            checkGrp = stereo_CentCam_Grp[0].split('|')[-1]
            if '_' not in checkGrp:
                erro_info.append(infoErrorCam)
                erro_info.append(checkGrp)
            else:
                checkKey = stereo_CentCam_Grp[0].split('_')[-1]
                if checkKey in keyList:
                    erro_info.append(infoSingleCam)
                    erro_info.append(checkGrp)
                else:
                    if checkGrp != exact_cam_nm:
                        erro_info.append(infoErrorCam)
                        erro_info.append(checkGrp)
        else:
            for checkGrp in stereo_CentCam_Grp:
                checkGrp = checkGrp.split('|')[-1]
                if '_' not in checkGrp:
                    erro_info.append(infoErrorCam)
                    erro_info.append(checkGrp)
                else:
                    if exact_cam_nm not in checkGrp:
                        erro_info.append(infoErrorCam)
                        erro_info.append(checkGrp)
                    else:
                        checkKey = checkGrp.split(exact_cam_nm)[-1][1:]
                        if checkKey not in keyList:
                            erro_info.append(infoMulCam)
                            erro_info.append(checkGrp)
        # 属性检测
        for checkCam in stereo_CentCam_shp:
            isValue = mc.getAttr('%s.interaxialSeparation'%checkCam)
            if isValue == 6.350:
                erro_info.append(isValueError)
                erro_info.append(checkCam)
            zeroParallaxValue = mc.getAttr('%s.zeroParallax'%checkCam)
            if zeroParallaxValue == 6.350:
                erro_info.append(zvValueError)
                erro_info.append(checkCam)

        #print 'done'

    '''
    if len(stereo_CentCam_shp) != 1:erro_info.append(u'=======================场景里有多余的立体摄像机=======================')
    for each_stcc_shp in stereo_CentCam_shp:
        stereo_CenterCam_trns = each_stcc_shp.getParent()
        print '------------s'
        print stereo_CenterCam_trns.name()
        print exact_cam_nm
        if  stereo_CenterCam_trns.name()!= exact_cam_nm: erro_info.append(u'=======================场景里的摄像机%s名字与文件名字不匹配=====%s=================='%(stereo_CenterCam_trns.name(),time.ctime()))
        if each_stcc_shp.attr('interaxialSeparation').get() == 6.350: erro_info.append(u'=======================中间立体相机%s的interaxialSeparation属性值不应该是默认的6.350=========%s============='%(each_stcc_shp.name(),time.ctime()))
        if each_stcc_shp.attr('zeroParallax').get() == 254.00: erro_info.append(u'=======================中间立体相机%s的zeroParallax属性值不应该是默认的254===============%s======='%(each_stcc_shp.name(),time.ctime()))
        if stereo_CenterCam_trns.scale.get().get() != (1.0,1.0,1.0): erro_info.append(u'=======================中间相机%s有缩放==============%s========='%(stereo_CenterCam_trns.name(),time.ctime()))
    '''
    if erro_info:
        #error(u'\n'.join(erro_info))
        for info in erro_info:
            print info
        mc.error()

def generate_pycfile_proc(des_path,delSource=1):
    #des_path= r'E:\MineScript\GDC_OEM_Repository\GDC_OEM_minitiger\Plug\Python\GDC'
    #des_path= r'E:\MineScript\GDC_OEM_Repository\GDC_OEM_minitiger\Plug\Python\GDC\Other\minitiger'
    for root,dirs,files in os.walk(des_path):
        for filespath in files:
            file_path_split = os.path.splitext(filespath)
            if file_path_split[-1] == '.py' and os.path.basename(filespath) != u'__init__.py':
                desfile = os.path.join(root,filespath)
                desfile_pyc = desfile.replace('.py','.pyc')
                if os.path.exists(desfile_pyc):
                    os.remove(desfile_pyc)
                    print u'+++++++++++++%s DELETED++++++++++++++' % os.path.split(desfile_pyc)[-1]
                try:
                    py_compile.compile(desfile)
                    if delSource:os.remove(desfile)
                    print u'++++++++++ %s Deleted !!!!!!!!%s++++++++++%s Created+++++++'%(os.path.split(desfile)[-1],os.linesep,os.path.split(desfile_pyc)[-1])
                except:
                    pass
                print
def abc_info_checkin():
    all_abc_nodes =[ eachNode.node() for eachNode in ls(u'*.alembic')]
    all_cache_nodes = mc.sets('MESHES', q=1)
    error_info = []
    error_objs = []
    if not all_abc_nodes:return
    # if not all_cache_nodes:
    #         error('{0:+>15}MESHES set group is empty ,please check!!!!{0:+>15}'.format(''))
    for each_abcNode in all_abc_nodes:
        if not each_abcNode.getShape():
            error_objs.append(each_abcNode)
            error_info.append(u' ++++++++ %s +++++++++ is not a parent transform node of a mesh' % each_abcNode)
        if each_abcNode not in all_cache_nodes:
            error_objs.append(each_abcNode)
            error_info.append(u'++++++++++++++++++++%s not in CACHE_OBJS lists,Please check!!!!'% each_abcNode)
    if error_info:
        select(error_objs)
        error(u'\n'.join(error_info))
        return error_objs
