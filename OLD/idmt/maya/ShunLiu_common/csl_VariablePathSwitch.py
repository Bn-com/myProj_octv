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
class csl_VariablePathSwitch(object):
    def __init__(self):
        pass
       
    def csl_VariableSwitch(self,cacheFile=1,mip=1,aiStandIn=1,fileTex=1,ref=0,abc=0,aiimage=0):
        dirty = False

        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        variableName='${IDMT_PROJECTS}'
        varibalePath=''
        if mc.pluginInfo('mtoa', query = True, loaded = True):
            if aiStandIn==1 and mc.ls(type='aiStandIn',l=1):
                for arNode  in mc.ls(type='aiStandIn',l=1):
                    if mc.objExists(arNode+'.dso') :
                        filePath=mc.getAttr(arNode+'.dso')
                        varibalePath=re.compile('^(//file-cluster/GDC|Z:|L:)/Projects', re.IGNORECASE).sub(variableName, filePath)
                        if varibalePath <> filePath:
                            try:
                                mc.setAttr(arNode+'.dso',varibalePath,type='string')
                                dirty = True
                            except:
                                pass
                print(u'=====================【渲染代理变量路径已经转换完成】=====================')

        if mip==1 and mc.ls(type='mesh',l=1):
            for arNode  in mc.ls(type='mesh',l=1):
                if mc.objExists(arNode+'.miProxyFile') :                
                    filePath=mc.getAttr(arNode+'.miProxyFile')
                    if filePath:
                        varibalePath=re.compile('^(//file-cluster/GDC|Z:|L:)/Projects', re.IGNORECASE).sub(variableName, filePath)
                        if varibalePath <> filePath:
                            try:
                                mc.setAttr(arNode+'.miProxyFile',varibalePath,type='string')
                                dirty = True
                            except:
                                pass 
            print(u'=====================【渲染代理变量路径已经转换完成】=====================')            
        if cacheFile==1 and mc.ls(type='cacheFile'):
            for arNode  in mc.ls(type='cacheFile',l=1):
                if mc.objExists(arNode+'.cachePath') :                
                    filePath=mc.getAttr(arNode+'.cachePath')
                    varibalePath=re.compile('^(//file-cluster/GDC|Z:|L:)/Projects', re.IGNORECASE).sub(variableName, filePath)
#                    if shotInfo[0]=='do5':
#                        varibalePath=varibalePath.replace('/scenes/Animation','/data/GEO_CACHE').replace('/setdressing','')                                                
                    if varibalePath <> filePath:
                        try:
                            mc.setAttr(arNode+'.cachePath',varibalePath,type='string')
                            dirty = True
                        except:
                            pass             				    				               
            print(u'=====================【cache变量路径已经转换完成】=====================')
        if fileTex==1 and mc.ls(type='file'):
            for eachTxt in mc.ls(type='file'):
                if mc.objExists(eachTxt+'.fileTextureName'):
                    filePath = mc.getAttr(eachTxt+'.fileTextureName')
                    varibalePath = re.compile('^(//file-cluster/GDC|Z:|L:)/Projects', re.IGNORECASE).sub(variableName, filePath)
                    if varibalePath <> filePath:
                        try:
                            mc.setAttr(eachTxt +'.fileTextureName', varibalePath, type='string')
                            dirty = True
                        except:
                            pass	        	    
            print(u'=====================【材质贴图变量路径已经转换完成】=====================')        
        if mc.pluginInfo('mtoa', query = True, loaded = True):
            if aiimage==1 and mc.ls(type='aiImage'):
                for eachTxt in mc.ls(type='aiImage'):
                    if mc.objExists(eachTxt+'.filename'):
                        filePath = mc.getAttr(eachTxt+'.filename')
                        varibalePath = re.compile('^(//file-cluster/GDC|Z:|L:)/Projects', re.IGNORECASE).sub(variableName, filePath)
                        if varibalePath <> filePath:
                            try:
                                mc.setAttr(eachTxt +'.filename', varibalePath, type='string')
                                dirty = True
                            except:
                                pass
                print(u'=====================【aiImage贴图变量路径已经转换完成】=====================')
        if mc.pluginInfo('AbcImport', query = True, loaded = True):
            if abc==1 and mc.ls(type='AlembicNode'):
                for arNode  in mc.ls(type='AlembicNode',l=1):
                    if mc.objExists(arNode+'.abc_File') :
                        filePath=mc.getAttr(arNode+'.abc_File')
                        varibalePath=re.compile('^(//file-cluster/GDC|Z:|L:)/Projects', re.IGNORECASE).sub(variableName, filePath)
                        if varibalePath <> filePath:
                            try:
                                mc.setAttr(arNode+'.abc_File',varibalePath,type='string')
                            except:
                                pass

        if ref==1:
            refpaths=mc.file(query=True,reference=1)
            if refpaths:
                for refpath in refpaths:
                    if '//file-cluster/GDC' in refpath or 'Z:' in refpath  or 'z:' in refpath or 'L:' in refpath:
                        refRN=mc.file(refpath,q=1,rfn=1) 
                        varibalePath = re.compile('^(//file-cluster/GDC|Z:|L:)/Projects', re.IGNORECASE).sub(variableName, refpath)
                    if varibalePath <> refpath:
                        try:
                            mc.file(varibalePath,loadReference=refRN,type='mayaBinary',options='v=0')
                            dirty = True
                        except:
                            pass	        	    
            print(u'=====================【参考变量路径已经转换完成】=====================')                						
        tempath='D:/Info_Temp/Variable/'
        mc.sysFile(tempath, makeDir=True)                                                               

        return dirty
    def YAK_aiStandSwitch(self,var=0):
        aiStandIns=mc.ls(type='aiStandIn',l=1)
        for ais in aiStandIns:
            if mc.objExists(ais+'.dso') :
                filePath=mc.getAttr(ais+'.dso')
                if  var==1 and filePath!='' and '${IDMT_PROJECTS}' in filePath:
                    filePath=filePath.replace('${IDMT_PROJECTS}','//file-cluster/GDC')
                if var==0 and filePath!='':
                    filePath=''
                mc.setAttr(ais+'.dso',filePath,type='string')
        return 0