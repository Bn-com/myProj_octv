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
        trans_container = do4_import_specify_containerImport(containerType,"",level)
    elif operate == u'Substitute':
        U_selectProxy = mc.ls(sl=True,l=True)
        #p = re.compile(u"_geo[0-9]*$")
        if U_selectProxy == []:
            mc.error(u'please select container object\'s geo group')
            return
        geo_desc = u'geo[0-9]*$'
        p_geo = re.compile(geo_desc)
        
        if p_geo.search(U_selectProxy[0]) == None:
            temp = getParent_2(U_selectProxy[0],geo_desc)
            U_selectProxy[0] = temp    
        
        trans_info = mc.xform(U_selectProxy[0],q=True,ws=True,t=True)
        rot_info = mc.xform(U_selectProxy[0],q=True,ws=True,ro=True)
        
        getParGrp = getParent(U_selectProxy[0],2)
        
        colorID = 1001
        if containerType in [u'ContainerI',u'ContainerJ']:
            colorID = mc.getAttr(u'%s.textureID'%U_selectProxy[0])
        
        trans_container = do4_import_specify_containerImport(containerType,getParGrp,level)
        if mc.copyKey(U_selectProxy[0]) != 0:
            mc.pasteKey(trans_container)
        mc.delete(U_selectProxy[0])
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
        
        getParGrp = getParent(U_selectProxy[0],2)    
            
        if containerType in [u'ContainerI',u'ContainerJ']:
            trans_info = mc.xform(U_selectProxy[0],q=True,ws=True,t=True)
            rot_info = mc.xform(U_selectProxy[0],q=True,ws=True,ro=True)
            colorID = mc.getAttr(u'%s.textureID'%U_selectProxy[0])
            trans_container = do4_import_specify_containerImport(containerType,getParGrp,level)
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
    return trans_container
            
def do4_import_specify_containerImport(containerType,grpParent,modelPrecision=u'l'):
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
    
    tempNS = u'%sTemp'%containerType
   
    MSHGroupName_elm = containerDir[containerType].split(u'_')[-1]
    MSHGroupName = u'%s:MSH_%s_all'%(containerType,MSHGroupName_elm)
    
    MSHGroupName_temp = u'%s:MSH_%s_all'%(tempNS,MSHGroupName_elm)
    MSH_Geo_Grp_Name_temp = ur'|%s|%s:MSH_%s_%s_geo'%(MSHGroupName_temp,tempNS,MSHGroupName_elm,modelPrecision)
    
    newGeoGroup = u'%s|%s|%s:MSH_%s_%s_geo'%(grpParent,MSHGroupName,containerType,MSHGroupName_elm,modelPrecision)
    
    if not mc.namespace(exists=containerType):
        mc.namespace(add=containerType)
        mc.namespace(set=u':')
         
        importFileNode = mc.file(containerFile,i=True,type=u'mayaBinary',ra=False,options=u'v=0',pr=False,namespace = tempNS)
        
        mc.namespace(mv =(':%s'%tempNS,':%s'%containerType),f=True)
        mc.namespace(rm =tempNS)
        if not grpParent == "":
                mc.parent(MSHGroupName,grpParent)
        
    
    else:
        importFileNode = mc.file(containerFile,i=True,type=u'mayaBinary',ra=False,options=u'v=0',pr=False,namespace = tempNS)
        if mc.objExists(MSHGroupName):
            MSHGroupName_LN = u'%s|%s'%(grpParent,MSHGroupName)
            if not mc.objExists(MSHGroupName_LN):
                mc.parent(MSHGroupName,grpParent)
            mc.parent(MSH_Geo_Grp_Name_temp,MSHGroupName_LN)
            mc.delete(MSHGroupName_temp)
            mc.namespace(mv =(':%s'%tempNS,':%s'%containerType),f=True)
            mc.namespace(rm =tempNS)
            newGeoGroup = mc.ls(sl=True,l=True)[0]
        else:
            mc.namespace(mv =(':%s'%tempNS,':%s'%containerType),f=True)
            mc.namespace(rm =tempNS)
            if not grpParent == "":
                mc.parent(MSHGroupName,grpParent)
    mc.select(cl=True)
    return newGeoGroup

def getParent(specObj,parentLevel):
    #specObj = mc.ls(sl=True,l=True)[0]
    #parentLevel = 3
    ind = parentLevel*-1
    return(u'|'.join(specObj.split(u'|')[:ind]))


def getParent_2(specObj,parentDescription):
    p_desc = re.compile(parentDescription)
    par_node = specObj
    while  par_node != None and  p_desc.search(par_node) == None:
        par_node = mc.listRelatives(par_node,p=True,f=True)[0]
    return par_node

def container_render_proxy(toggleParameter =True):
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
    U_selectProxy = mc.ls(sl=True,l=True)
    for i in range(len(U_selectProxy)):
        p_containerType = re.compile(u'Container[A-Z]+')
        containerType = p_containerType.search(U_selectProxy[i]).group()
        p_l = re.compile(u'_l_')
        if p_l.search(U_selectProxy[i]) == None:
            subLowGeo = do4_trans_container(containerType,u'l',operate=u'Substitute')
            U_selectProxy[i] = subLowGeo
        mr_proxy_file = ""    
        if containerType in [u'ContainerI',u'ContainerJ']:
            geoGrp = getParent_2(U_selectProxy[i],u'_geo[0-9]*$')
            colorID = mc.getAttr(u'%s.textureID'%geoGrp)          
            mr_proxy_file = u'%s_hms_anim.%d.mi'%(containerDir[containerType],colorID)
        else:
            mr_proxy_file = u'%s_hms_anim.mi'%(containerDir[containerType])
        modeShape = mc.listRelatives(U_selectProxy[i],c=True,ad=True,type=u'mesh',ni=True,f=True)
        attrName_mip = u'%s.miProxyFile'%modeShape[0]
        attrName_overrideToggle = u'%s.overrideEnabled'%modeShape[0]
        attrName_overrideColor = u'%s.overrideColor'%modeShape[0]
        if toggleParameter:
            try:
                mc.setAttr(attrName_overrideToggle,1)
                mc.setAttr(attrName_overrideColor,13)
                mc.setAttr(attrName_mip,mr_proxy_file,type=u'string')
                
            except:
                print "MR Render Proxy OK!!!!"
        else:
            try:
                mc.setAttr(attrName_overrideToggle,0)
                mc.setAttr(attrName_mip,"",type=u'string')
            except:
                print "MR Render Proxy Off!!!"
                
def container_render_proxy_AO(AOtoggleParameter =True):
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
    allMeshes = mc.ls(type = u'mesh',l=True)
    filtercharacter = u'p[0-9]{6,}Container[A-Z]{1,}_'
    attrName = u'miProxyFile'
    
    proxyOpenObjs = (cont_mesh for cont_mesh in allMeshes if filterSpecifyObj(cont_mesh,attrName,filtercharacter)==True)
    
    U_selectProxy = []
    for each in proxyOpenObjs:
        transNode = mc.listRelatives(each,p=True,f=True)
        U_selectProxy.append(transNode[0])
        
    for i in range(len(U_selectProxy)):
        p_containerType = re.compile(u'Container[A-Z]+')
        containerType = p_containerType.search(U_selectProxy[i]).group()
        p_l = re.compile(u'_l_')
        if p_l.search(U_selectProxy[i]) == None:
            mc.error("您没有选择一个低模")
        
        mr_proxy_file = ""    
        if containerType in [u'ContainerI',u'ContainerJ']:
            geoGrp = getParent_2(U_selectProxy[i],u'_geo[0-9]*$')
            colorID = mc.getAttr(u'%s.textureID'%geoGrp)           
            mr_proxy_file = u'%s_hms_anim.%d.mi'%(containerDir[containerType],colorID)
        else:
            mr_proxy_file = u'%s_hms_anim.mi'%(containerDir[containerType])
        
        modeShape = mc.listRelatives(U_selectProxy[i],c=True,ad=True,type=u'mesh',ni=True,f=True)
        attrName_mip = u'%s.miProxyFile'%modeShape[0]
        attrName_overrideToggle = u'%s.overrideEnabled'%modeShape[0]
        attrName_overrideColor = u'%s.overrideColor'%modeShape[0]
        
        AO_mr_proxy_file = u'%s_hms_anim_AO.mi'%(containerDir[containerType])
        
        
        if AOtoggleParameter:
            mip_name = u'%s_mip_binaryProxy'%containerType
            mip_pro_node = mc.createNode(u'mip_binaryproxy',n=mip_name)
            mc.setAttr(u'%s.object_filename'%mip_pro_node,AO_mr_proxy_file,type=u'string')
            mc.setAttr(u'%s.miExportGeoShader'%U_selectProxy[i],1)
            con_shader = mc.listConnections(u'%s.miGeoShader'%U_selectProxy[i],p=True,connections=True)
            if con_shader != None:
                mc.disconnectAttr(con_shader[1],con_shader[0])
            mc.connectAttr(u'%s.outValue'%(mip_pro_node),u'%s.miGeoShader'%(U_selectProxy[i]),f=True)
            try:
                mc.setAttr(attrName_overrideToggle,1)
                mc.setAttr(attrName_overrideColor,15)
                mc.setAttr(attrName_mip,"",type=u'string')
            except:
                print "MR Render Proxy OK!!!!"
            
        else:
            
            con_shader = mc.listConnections(u'%s.miGeoShader'%U_selectProxy[i],p=True,connections=True)
            if con_shader != None:
                mc.delete(con_shader[1].split(u'.')[0])
                mc.setAttr(u'%s.miExportGeoShader'%U_selectProxy[i],0)
            
            try:           
                mc.setAttr(attrName_overrideToggle,1)
                mc.setAttr(attrName_overrideColor,13)
                mc.setAttr(attrName_mip,mr_proxy_file,type=u'string')
            except:
                print "MR AO RenderProxy Off,and Normal proxy OK!!!"
                
def filterSpecifyObj(specObject,attrName,filtercharacter):
    p_container = re.compile(filtercharacter)
    atri = '%s.%s'%(specObject,attrName)
    
    if mc.getAttr(atri) != None and p_container.search(specObject) != None:
        return True
    else:
        return False