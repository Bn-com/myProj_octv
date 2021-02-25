# -*- coding: utf-8 -*-
# 【顺溜】【工具】
#  Author : 韩虹
#  Data   : 2014_08
# import sys
# sys.path.append('D:\\food\pyp\common')


#常用工具
from idmt.maya.py_common import sk_infoConfig
reload(sk_infoConfig)
import maya.cmds as mc
import maya.mel as mel
import re
import os
import sys
class sk_ImagePathSwitch(object):
    def __init__(self):
        pass
       
    def sk_ImagePathSwitch(self,cacheFile=0,aiStandIn=0,fileTex=1,ref=0):
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        variableName='${IDMT_PROJECTS}'
        varibalePath=''  
        if aiStandIn==1 and mc.ls(type='aiStandIn',l=1):
            for arNode  in mc.ls(type='aiStandIn',l=1):
                if mc.objExists(arNode+'.dso') :                
                    filePath=mc.getAttr(arNode+'.dso')
                    varibalePath=re.compile('^(//file-cluster/GDC|Z:)/Projects|L:', re.IGNORECASE).sub(variableName, filePath)
                    if varibalePath <> filePath:
                        try:
                            mc.setAttr(arNode+'.dso',varibalePath,type='string')
                        except:
                            pass 
            print(u'=====================【渲染代理变量路径已经转换完成】=====================')
        if cacheFile==1 and mc.ls(type='cacheFile'):
            for arNode  in mc.ls(type='cacheFile',l=1):
                if mc.objExists(arNode+'.cachePath') :                
                    filePath=mc.getAttr(arNode+'.cachePath')
                    variableName='${IDMT_PROJECTS}/Strawberry3/Project'
                    varibalePath=re.compile('^(//file-cluster/GDC|Z:)/Projects/Strawberry/Project', re.IGNORECASE).sub(variableName, filePath)
#                    if shotInfo[0]=='do5':
#                        varibalePath=varibalePath.replace('/scenes/Animation','/data/GEO_CACHE').replace('/setdressing','')                                                
                    if varibalePath <> filePath:
                        try:
                            mc.setAttr(arNode+'.cachePath',varibalePath,type='string')
                        except:
                            pass             				    				               
            print(u'=====================【cache变量路径已经转换完成】=====================')
        if fileTex==1 and mc.ls(type='file'):
            for eachTxt in mc.ls(type='file'):
                if mc.objExists(eachTxt+'.fileTextureName'):
                    filePath = mc.getAttr(eachTxt+'.fileTextureName')
                    varibalePath = re.compile('^(//file-cluster/GDC|Z:|z:|L:)/Projects', re.IGNORECASE).sub(variableName, filePath)
                    if varibalePath <> filePath:
                        try:
                            mc.setAttr(eachTxt +'.fileTextureName', varibalePath, type='string')
                        except:
                            pass	        	    
            print(u'=====================【材质贴图变量路径已经转换完成】=====================')        

        if ref==1:
            refpaths=mc.file(query=True,reference=1)
            if refpaths:
                for refpath in refpaths:
                    if '//file-cluster/GDC' in refpath or 'Z:' in refpath  or 'z:' in refpath or 'L:' in refpath:
                        refRN=mc.file(refpath,q=1,rfn=1) 
                        varibalePath = re.compile('^(//file-cluster/GDC|Z:|z:|L:)/Projects', re.IGNORECASE).sub(variableName, refpath)
                    if varibalePath <> filePath:
                        try:
                            mc.file(varibalePath,loadReference=refRN,type='mayaBinary',options='v=0')
                        except:
                            pass	        	    
            print(u'=====================【材质贴图变量路径已经转换完成】=====================')                						
        tempath='D:/Info_Temp/Variable/'
        mc.sysFile(tempath, makeDir=True)                                                               
        return 0                     
                                           
         