# -*- coding: utf-8 -*-
# 【通用】【pyc 转py】
#  Author : 韩虹
#  Data   : 2017_11
# import sys
# sys.path.append('D:\\food\pyp\common')


#渲染后台

import maya.cmds as mc
import maya.mel as mel
import pymel.core as pm

import json
import logging
import os
import re
import suds

import os
import re
class GA_pycTopy(object):
    def __init__(self):
        # namespace清理
        pass
    #----------------------------------------------------------#
    #----------------------------------------------------------------------------------------------------------#      #----------------------------------------------------------#
    def checkFileWrite(self,path , info , addtion=0):
        print u'>>>>>>[write]'
        print path
        mc.sysFile(os.path.dirname(path), makeDir=True)
        if addtion == 1:
            info = self.checkFileRead(path) + info
        txt = open(path, 'w')
        try:
            txt.writelines(str(a) + '\r\n' for a in info)
            print('Writing........')
        finally:
            txt.close()
    def checkFileRead(self,path):
        print u'>>>>>>[read]'
        print path
        mc.sysFile(os.path.dirname(path), makeDir=True)
        txt = open(path, 'r');
        try:
            fileContent = txt.readlines()
            print('Loading........')
        finally:
            txt.close()
        result = []
        for info in fileContent:
            if '\r\n' in info:
                result.append(info.split('\r\n')[0])
            else:
                result.append(info)
        return result
    def getFileList(self,path):
        p = str(path)

        if p=="":
              return [ ]
        path= p.replace( "/","\\")
        if p[ -1] != "\\":

            path= p+"\\"
        a = os.listdir(path)
        b = [ x   for x in a if os.path.isfile(path+ x ) ]
        return b
    #pycpath 为pyc路径，infopath 为写入信息.bat路径
    def GA_WritePycInfo(self,pycpath,infopath):
        filLists=self.getFileList(pycpath)
        info=[]
        for fil in filLists:
            if '.pyc' in fil:
                inf='C:/Python27/Python -u C:/Python27/uncompyle2-master/scripts/uncompyle2   '+(p+'/'+fil)+' > ' +p+'/'+fil.split('.pyc')[0]+'.py'
                info.append(inf)
        if info:
            self.checkFileWrite(infopath,info)
        return info
