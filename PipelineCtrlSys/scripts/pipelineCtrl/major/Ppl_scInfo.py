#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'Pc_obtScInfor'    
__author__ = zhangben
__mtime__ = 2018/12/6:17:26
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
"""
import maya.cmds as mc
import pymel.core as pm
import re,os


class Pc_scInfo(object):
    """
    获取镜头文件信息
    """
    def __init__(self):
        self.modeDic = {u'mo': 'mod', u'tx': 'texture', u'rg': 'rigging', u'ms': 'master', u'an':'anim',u'sm':'simulation',u'ef':'effect',u'lg':'lighting',u'rn':'rendering'}
        #self.precisionDic = {u'lo':'l'}
        self.proj = None               #项目名称
        self.shotId = None             #文件主题描述部分
        self.prjPath = None  # 项目工程目录（数据库）
        self.prjPath_loc = None  # 本地工程路径
        self.curPath = None  # 当前文件存储路径
        self.mode = None  # 环节描述
        self.destFolder = None  # checkin　目录
        self.shotType = 2  # 镜头场次分类方式 默认是2
        self.section = None
        #===asset file informations
        self.assId = None              #资产ID
        self.assType =None             #资产类型
        self.assPrec = None            #资产精度描述
        #==========read file information===================
        self.obtScInfo()
    def obtScInfo(self):#获取信息的函数 并赋值
        scnm = pm.sceneName()
        # print scnm
        scbsnm = scnm.basename()
        bsnm_spl = scbsnm.split(u'_')
        # print bsnm_spl
        self.proj = bsnm_spl[0]
        # print bsnm_spl[1][:2]
        if bsnm_spl[1][:2] in [u'ch',u'pr',u'se']:
            self.section = 'asset'
        else:
            self.section = 'shot'
        if self.section == 'asset':
            self.assId = bsnm_spl[1]
            # print assId
            self.assType = bsnm_spl[-1].split(u'.')[0]
            self.mode = self.modeDic[self.assType]
            self.assPrec = bsnm_spl[-2]
            #print bsnm_spl[-2]