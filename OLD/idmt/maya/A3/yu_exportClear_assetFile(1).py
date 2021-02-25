# -*- coding: utf-8 -*-
# 【通用】【前期文件导出成干净版本】
#  Author : 虞丰盛
#  Data   : 2018_03
from maya.cmds import *
import maya.mel as mel
import sys
import os


def desFileNameCmd():
    fileName=file(q=1,sn=1,shn=1)
    scenesPath=workspace(q=1,fn=1)+'/scenes'
    tmpPath=scenesPath+'/tmp'
    if os.path.exists(tmpPath)==False:
        os.makedirs(tmpPath)

    desFileName=tmpPath+'/'+fileName
    fileType=fileName.split('.')[1]
    return desFileName,fileType

#导出前期文件
def exportAssetFile():
    fileNameTypeList=desFileNameCmd()
    desFileName=fileNameTypeList[0]
    fileType=fileNameTypeList[1]
    if fileType=='mb':
        fileType='mayaBinary'
    if fileType=='ma':
        fileType='mayaAscii'

    if objExists('CHR') and objExists('SMOOTH_SET'):
        select('CHR')
        select( 'SMOOTH_SET',add=1,ne=1)
    elif objExists('SET') and objExists('SMOOTH_SET'):
        select('SET')
        select( 'SMOOTH_SET',add=1,ne=1)
    elif objExists('PRO') and objExists('SMOOTH_SET'):
        select('PRO')
        select( 'SMOOTH_SET',add=1,ne=1)
    else:
        error(u'文件中没有CHR、SMOOTH SET组！')
    file(desFileName,force=1,es=1,options='v=0',pr=1,type=fileType)
    file(desFileName,o=1,force=1)
    print desFileName.replace('/','\\'),

#导出动力学设置文件
def exportDynRgFile():
    fileNameTypeList=desFileNameCmd()
    desFileName=fileNameTypeList[0]
    fileType=fileNameTypeList[1]
    if fileType=='mb':
        fileType='mayaBinary'
    if fileType=='ma':
        fileType='mayaAscii'

    if objExists('CHR') and objExists('SMOOTH_SET') and objExists('bodySet') and objExists('CACHE_OBJS') and objExists('cloth_CACHE_OBJS') and objExists('cloth_SMOOTH_SET') and objExists('CtrlSet') and objExists('Influence_Joint') :
        select('CHR')
        select( 'SMOOTH_SET',add=1,ne=1)
        select( 'bodySet',add=1,ne=1)
        select( 'CACHE_OBJS',add=1,ne=1)
        select( 'cloth_CACHE_OBJS',add=1,ne=1)
        select( 'cloth_SMOOTH_SET',add=1,ne=1)
        select( 'CtrlSet',add=1,ne=1)
        select( 'Influence_Joint',add=1,ne=1)
    else:
        error(u'文件中没有CHR、SMOOTH SET组、bodySet组、CACHE_OBJS组、cloth_CACHE_OBJS组、cloth_SMOOTH_SET组、CtrlSet、Influence_Joint组！')
    file(desFileName,force=1,es=1,options='v=0',pr=1,type=fileType)
    file(desFileName,o=1,force=1)
    print desFileName.replace('/','\\'),


