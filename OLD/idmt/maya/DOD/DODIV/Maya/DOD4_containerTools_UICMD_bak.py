#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2013-9-122013

@author: zhangben



'''
import maya.cmds as mc
import maya.mel as mel
import os,re

def dctcmd_BTCMD(containerType):
    modePrecision = u'l'
    opraterType = unicode(mc.optionMenu('op_cmb',q=True,v=True))
    if mc.radioButton(u'h_rb',q=True,sl=True):
        modePrecision = u'h'
    if opraterType == u'Duplicate':
        selContainer = mc.ls(sl=True)
        modePrecision = unicode(selContainer[0].split(u'_')[-2])
    do4_trans_container(containerType,modePrecision,opraterType)

def configUI():
    if mc.optionMenu('op_cmb',q=True,v=True) == u'Duplicate':
        mc.control(u'sl_grp',e=True,en=False)
    else:
        mc.control(u'sl_grp',e=True,en=True)



def do4_trans_container(containerType,level,operate=u'Substitute'):
    if operate == u'Import':
        mc.select(cl=True)
        trans_container = do4_import_specify_containerImport(containerType,level)
    elif operate == u'Substitute':
        U_selectProxy = mc.ls(sl=True,l=True)
        #p = re.compile(u"_geo[0-9]*$")
        if U_selectProxy == []:
            mc.error(u'please select container object\'s geo group')
            return
        if mc.getAttr(u'%s.translateX'%U_selectProxy[0],l=True):
            mc.error(u"the translation attribute is locked of the DAG objecte you seleceted!!")
            return
        trans_info = mc.xform(U_selectProxy[0],q=True,ws=True,t=True)
        rot_info = mc.xform(U_selectProxy[0],q=True,ws=True,ro=True)
        
        colorID = 1001
        if containerType in [u'ContainerI',u'ContainerJ']:
            colorID = mc.getAttr(u'%s.textureID'%U_selectProxy[0])
        mc.delete(U_selectProxy[0])
        trans_container = do4_import_specify_containerImport(containerType,level)
        mc.setAttr(u'%s.translateX'%trans_container,trans_info[0])
        mc.setAttr(u'%s.translateY'%trans_container,trans_info[1])
        mc.setAttr(u'%s.translateZ'%trans_container,trans_info[2])
        
        mc.setAttr(u'%s.rotateX'%trans_container,rot_info[0])
        mc.setAttr(u'%s.rotateY'%trans_container,rot_info[1])
        mc.setAttr(u'%s.rotateZ'%trans_container,rot_info[2])
        
        if containerType in [u'ContainerI',u'ContainerJ']:
            mc.setAttr(u'%s.textureID'%trans_container,colorID)
        
    elif operate == u'Duplicate':
        U_selectProxy = mc.ls(sl=True,l=True)
        #p = re.compile(u"_geo[0-9]*$")
        if U_selectProxy == []:
            mc.error(u'please select container object\'s geo group')
        if mc.getAttr(u'%s.translateX'%U_selectProxy[0],l=True):
            mc.error(u"the translation attribute is locked of the DAG objecte you seleceted!!")
        if containerType in [u'ContainerI',u'ContainerJ']:
            trans_info = mc.xform(U_selectProxy[0],q=True,ws=True,t=True)
            rot_info = mc.xform(U_selectProxy[0],q=True,ws=True,ro=True)
            colorID = mc.getAttr(u'%s.textureID'%U_selectProxy[0])
            trans_container = do4_import_specify_containerImport(containerType,level)
            mc.setAttr(u'%s.translateX'%trans_container,trans_info[0])
            mc.setAttr(u'%s.translateY'%trans_container,trans_info[1])
            mc.setAttr(u'%s.translateZ'%trans_container,trans_info[2])
            mc.setAttr(u'%s.rotateX'%trans_container,rot_info[0])
            mc.setAttr(u'%s.rotateY'%trans_container,rot_info[1])
            mc.setAttr(u'%s.rotateZ'%trans_container,rot_info[2])
            mc.setAttr(u'%s.textureID'%trans_container,colorID)
        else:
            mc.namespace(set=containerType) 
            dupGrp = mc.duplicate(rc=True)
            mc.namespace(set=u':') 
def do4_import_specify_containerImport(containerType,modelPrecision=u'l'):
    containerDir = {u"ContainerA":ur"\\file-cluster\GDC\Projects\DiveollyDive4\Project\scenes\props\p406001ContainerA\master\do4_p406001ContainerA",
                    u"ContainerB":ur"\\file-cluster\GDC\Projects\DiveollyDive4\Project\scenes\props\p406002ContainerB\master\do4_p406002ContainerB",
                    u"ContainerC":ur"\\file-cluster\GDC\Projects\DiveollyDive4\Project\scenes\props\p406003ContainerC\master\do4_p406003ContainerC",
                    u"ContainerD":ur"\\file-cluster\GDC\Projects\DiveollyDive4\Project\scenes\props\p406004ContainerD\master\do4_p406004ContainerD",
                    u"ContainerE":ur"\\file-cluster\GDC\Projects\DiveollyDive4\Project\scenes\props\p406005ContainerE\master\do4_p406005ContainerE",
                    u"ContainerF":ur"\\file-cluster\GDC\Projects\DiveollyDive4\Project\scenes\props\p406006ContainerF\master\do4_p406006ContainerF",
                    u"ContainerG":ur"\\file-cluster\GDC\Projects\DiveollyDive4\Project\scenes\props\p406006ContainerG\master\do4_p406006ContainerG",
                    u"ContainerH":ur"\\file-cluster\GDC\Projects\DiveollyDive4\Project\scenes\props\p406006ContainerH\master\do4_p406006ContainerH",
                    u"ContainerI":ur"\\file-cluster\GDC\Projects\DiveollyDive4\Project\scenes\props\p406006ContainerI\master\do4_p406006ContainerI",
                    u"ContainerJ":ur"\\file-cluster\GDC\Projects\DiveollyDive4\Project\scenes\props\p406006ContainerJ\master\do4_p406006ContainerJ"}
    
    containerFile = u"%s_%sms_anim.mb"%(containerDir[containerType],modelPrecision)
    
    #MSHGroupName_elm = containerDir[containerType].split(u'_')[-1]
    #MSHGroupName = u'%s:MSH_%s_all'%(containerType,MSHGroupName_elm)
    
    tempNS = u'%sTemp'%containerType
    
    
    MSHGroupName_elm = containerDir[containerType].split(u'_')[-1]
    MSHGroupName = u'%s:MSH_%s_all'%(containerType,MSHGroupName_elm)
    
    MSHGroupName_temp = u'%s:MSH_%s_all'%(tempNS,MSHGroupName_elm)
    MSH_Geo_Grp_Name_temp = ur'|%s|%s:MSH_%s_%s_geo'%(MSHGroupName_temp,tempNS,MSHGroupName_elm,modelPrecision)
    
    newGeoGroup = u'|%s|%s:MSH_%s_%s_geo'%(MSHGroupName,containerType,MSHGroupName_elm,modelPrecision)
    
    if not mc.namespace(exists=containerType):
        mc.namespace(add=containerType)
        mc.namespace(set=u':')
         
        importFileNode = mc.file(containerFile,i=True,type=u'mayaBinary',ra=False,options=u'v=0',pr=False,namespace = tempNS)
        mc.namespace(mv =(':%s'%tempNS,':%s'%containerType),f=True)
        mc.namespace(rm =tempNS)
    
    else:
        importFileNode = mc.file(containerFile,i=True,type=u'mayaBinary',ra=False,options=u'v=0',pr=False,namespace = tempNS)
        if mc.objExists(MSHGroupName):
            mc.parent(MSH_Geo_Grp_Name_temp,MSHGroupName)
            mc.delete(MSHGroupName_temp)
            mc.namespace(mv =(':%s'%tempNS,':%s'%containerType),f=True)
            mc.namespace(rm =tempNS)
            newGeoGroup = mc.ls(sl=True,l=True)[0]
        else:
            mc.namespace(mv =(':%s'%tempNS,':%s'%containerType),f=True)
            mc.namespace(rm =tempNS)
                             
    return newGeoGroup




        
