# -*- coding: utf-8 -*-
#  Author : liangyu
#  Data   : 2015_17-03

from idmt.maya.py_common import sk_infoConfig
reload(sk_infoConfig)
import maya.cmds as mc
import maya.mel as mel
import re
import os
import sys
class north_PathtoL(object):
    def __init__(self):
        pass
       
    def north_L(self,cacheFile=1,fileTex=1,ref=1):
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        variableName='L:'
        varibalePath=''  
        if ref==1:           
            refpaths=mc.file(query=True,reference=1)
            if refpaths:
                for refpath in refpaths:
                    if refpath.split('_')[-1]=='cam.ma':
                        pass     
                    else:    
                        if '//file-cluster/GDC' in refpath or 'Z:' in refpath  or 'z:' in refpath or 'L:' in refpath:
                            refRN=mc.file(refpath,q=1,rfn=1) 
                            varibalePath = re.compile('^(//file-cluster/GDC|Z:|z:)', re.IGNORECASE).sub(variableName, refpath)
                        if varibalePath <> refpath:
                            try:
                                mc.file(varibalePath,loadReference=refRN,type='mayaBinary',options='v=0')
                            except:
                                pass                    
            print(u'=====================【参考路径替换L盘完成】=====================') 
            
        if cacheFile==1 and mc.ls(type = 'AlembicNode'):
            abcNodes=mc.ls(type = 'AlembicNode',l=1)
            for node in abcNodes:
                if mc.objExists(node+'.abc_File'):
                    filePath=mc.getAttr(node+'.abc_File')               
                    varibalePath=re.compile('^(//file-cluster/GDC|Z:/Projects)', re.IGNORECASE).sub(variableName, filePath)
                    if varibalePath <> filePath:
                        try:
                            mc.setAttr(node+'.abc_File',varibalePath,type='string')
                        except:
                            pass             				    				               
            print(u'=====================【cache变量路径已经转换完成】=====================')
            
        if fileTex==1 and mc.ls(type='file'):
            for eachTxt in mc.ls(type='file'):
                if mc.objExists(eachTxt+'.fileTextureName'):
                    filePath = mc.getAttr(eachTxt+'.fileTextureName')
                    varibalePath = re.compile('^(//file-cluster/GDC|Z:|z:)', re.IGNORECASE).sub(variableName, filePath)
                    if varibalePath <> filePath:
                        try:
                            mc.setAttr(eachTxt +'.fileTextureName', varibalePath, type='string')
                        except:
                            pass	        	    
            print(u'=====================【材质贴图变量路径已经转换完成】=====================')     
            
        
    def north_hairDisHide(self): 
        from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
        reload(sk_referenceConfig)
        namesapces=[]
        RNs=sk_referenceConfig.sk_referenceConfig().checkReferenceGetInfo()
        for RN in RNs:
            name_space=sk_referenceConfig.sk_referenceConfig ().checkReferenceGetNamespaceInfo(RN)
            namesapces.append(name_space)
        
        bodyGRP=[]
        bodySHAVE=[]
        if namesapces:   
            for name in namesapces:
                bodyGRP.append(mc.ls(name+':*body_grp')[0])
                bodySHAVE.append(mc.ls(name+':*SHAVE')[0])
                
        if bodyGRP:
            for objGRP in bodyGRP:
                objlist=mc.listRelatives(objGRP, c=1, f=1, type='transform')
                if objlist:
                    for obj in objlist:
                        vis=mc.getAttr(obj+'.v')
                        if vis==1:
                            pass
                        else:
                            mc.setAttr((obj+'.v'),1)
                            
        if bodySHAVE:
            for obj in bodySHAVE:
                vis=mc.getAttr(obj+'.v')
                if vis==0:
                    pass
                else:
                    mc.setAttr((obj+'.v'),0)                      						
                   
                                           
         