# -*- coding: utf-8 -*-
# Copyright (C) 2000-2010 IDMT. All rights reserved.
'''
关于文件路径的系列函数
'''
__author__    = 'huangzhongwei@idmt.com.cn'
__date__    = '2010-12-02'

import idmt.pipeline.project
import maya.cmds as cmds
import os
import re

def GetFullPath(path):
    '''
    得到完整路径，例如：
    像Z:盘符这样的map路径会转换成//file-cluster/GDC这样的UNC路径
    像${MC_roma}这样带环境变量的路径会将环境变量展开，转换成//file-cluster/GDC/Projects/ROMA/PRJ_roma/MC_roma
    注意的是，本函数返回的时候，顺便将 \ 也变成 / 了
    '''
    path = cmds.workspace(expandName = path)
    path = cmds.idmtFile(path, fullPath = True)
    path = re.sub(r'\\', r'/', path)
    path = re.compile(r"^[/\\][/\\]file-cluster[/\\]GDC([/\\]SW_S3_Pipeline[/\\])", re.IGNORECASE).sub(r"Z:\g<1>", path)
    return path;

def GetDollarPath(path):
    '''
    将路径转换成带环境变量的，用于外包
    例如 Z:\Projects\TTMS\Project -> ${IDMT_PROJECTS}/TTMS/Project
    '''
    #if re.compile(r'[\\/]DiveOllyDive5[\\/]', re.IGNORECASE).search(path) != None:
    #    url = GetFullPath(path)
    #    url = re.compile(r'^L:/Projects', re.IGNORECASE).sub('${L_PROJECTS}', url)
    #    url = re.compile(r'^//file-cluster/GDC/Projects', re.IGNORECASE).sub('${L_PROJECTS}', url)
    #    return url

    envNames = ('IDMT_PROJECTS', 'MC_roma', 'MC_winxII')
    for envName in envNames:
        envValue = os.getenv(envName, '')
        if envValue != '':
            envValue = envValue.replace('\\', '/')
            fullPath = GetFullPath(path)
            url = fullPath
            if envName == 'IDMT_PROJECTS':
                #url = re.compile(r'^%s/((ShenShou)/Project)/' % (envValue), re.IGNORECASE).sub(r'${%s}/\g<1>/' % (envName), fullPath)
                m = re.compile(r'^%s/([^/]+)/Project/' % envValue, re.IGNORECASE).search(fullPath)
                if m != None:
                    projectName = m.group(1)
                    project = idmt.pipeline.project.project().GetProjectByName(projectName)
                    if project != None:
                        if project.projectId in [5, 35] or project.projectId >= 39:
                            url = re.compile(r'^%s/' % (envValue), re.IGNORECASE).sub(r'${%s}/' % (envName), fullPath)
                elif re.search(r'^(//file-cluster/GDC|L:)/Projects$', envValue, re.IGNORECASE) != None:
                    m = re.compile(r'^(//file-cluster/GDC|L:)/Projects/([^/]+)/Project/', re.IGNORECASE).search(fullPath)
                    if m != None:
                        projectName = m.group(2)
                        projectName = 'XingJiCheShen1' if projectName == 'XJCS' else projectName
                        project = idmt.pipeline.project.project().GetProjectByName(projectName)
                        if project != None:
                            if project.projectId in [5, 35] or project.projectId >= 39:
                                url = re.compile(r'^(//file-cluster/GDC|L:)/Projects/', re.IGNORECASE).sub(r'${%s}/' % (envName), fullPath)
            else:
                url = re.compile(r'^%s/' % (envValue), re.IGNORECASE).sub(r'${%s}/' % (envName), fullPath)
            if url != fullPath:
                return url
    return path
