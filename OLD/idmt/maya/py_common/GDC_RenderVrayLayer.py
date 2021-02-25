# -*- coding: utf-8 -*-

'''
Created on 2016-6-02

@author: hanhong
'''

import maya.cmds as mc
import maya.mel as mel
import pymel.core as pm
import os
import sys


sys.path.append('Z:/Netrender/Maya_Odd/cloud/DeadlineRepository7/submission/Maya/Main')
sys.path.append('Z:/Netrender/Maya_Odd/cloud/DeadlineRepository7/2013/Submission')
sys.path.append('Z:/Netrender/Maya_Odd/cloud/DeadlineRepository7/submission/MayaVRayDBR/Main')

from idmt.maya.commonCore.core_renderLayer import sk_renderLayerCore
reload(sk_renderLayerCore)



from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
reload(sk_referenceConfig)

from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
reload(sk_infoConfig)

from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools
reload(sk_sceneTools)

from idmt.maya.ShunLiu_common import csl_toolCommons
reload(csl_toolCommons)

import re
class GDC_RenderVrayLayer(object):
    def __init__(self):
        pass
    #----------------------------------------------------------------------------------------------------------#      #----------------------------------------------------------#
    def RenderVrayUI(self):
        mel.eval('source "Z:/Netrender/Maya_Odd/cloud/DeadlineRepository7/submission/Maya/Client/DeadlineMayaClient.mel"')
        #mel.eval('source "Z:/Netrender/Maya_Odd/cloud/DeadlineRepository7/submission/Maya/Main/SubmitMayaToDeadline.mel"')

    # 窗口
        if mc.window('hh_RenderVray', exists=True):
            mc.deleteUI('hh_RenderVray')
        mc.window('hh_RenderVray', title=u'Vray 渲染面板',
                  width=320, height=350, sizeable=0)
         # 面板
        form = mc.formLayout()
         # 切换面板
        tabs = mc.tabLayout('tabVray',innerMarginWidth=5, innerMarginHeight=5)
        mc.formLayout(
            form, edit=True, attachForm=((tabs, 'top', 0), (tabs, 'left', 0), (tabs, 'bottom', 0), (tabs, 'right', 0)))
         # tab_渲染工具
        child1 = mc.columnLayout(adjustableColumn=True)
        mc.image(image='//file-cluster/GDC/Resource/Support/Maya/icons/HH/NJ.png',width=320)
        mc.button(label=u'创建Project', bgc=[0, 0, 0.0], height=50, command='mel.eval(\'zwSetProject\')')
        #mc.button(label=u'另存文件', bgc=[0, 0, 0.0], height=50, command='mel.eval(\'source \"//file-cluster/GDC/Resource/Support/Maya/projects/ShunLiu/CSL_RenderToolsMR.mel\";CSL_HHSavefile();\')')
        mc.button(label=u'优化文件', bgc=[0, 0, 0.0], height=50, command='from idmt.maya.py_common import nj17_CheckTools\nreload(nj17_CheckTools)\nnj17_CheckTools.nj17_CheckTools().nj_FixBeforeRender()')
        mc.button(label=u'渲染工具', bgc=[0, 0, 0.0], height=50, command='mc.tabLayout("tabVray", edit=True, selectTabIndex=2)')
        mc.button(label=u'提交网渲(muster)', bgc=[0, 0, 0.0], height=50, command='mel.eval(\'source \"//file-cluster/GDC/Resource/Support/Maya/2013/MusterCheckin.mel\";MusterCheckin();\')')
        mc.button(label=u'提交网渲(deadline)', bgc=[0, 0, 0.0], height=50, command='mel.eval("SubmitJobToDeadline()")')
        mc.setParent('..')
         # 渲染面板面板
        child2 = mc.columnLayout(adjustableColumn=True)
        # 一键式创建AOV层
        mc.frameLayout(label=u'渲染建层工具', bgc=[0, 0, 0.0], borderStyle='in',cll=0,cl=0)
        mc.rowColumnLayout(numberOfColumns=3)
        mc.button(label=u'CHR', width=130, height=30,
                  bgc=[0.13, 0.15, 0.25], command='reload(GDC_RenderVrayLayer)\nGDC_RenderVrayLayer.GDC_RenderVrayLayer().nj_VrayRenderCreat("CHR",1)')
        mc.button(label=u'SET', width=130, height=30,
                  bgc=[0.13, 0.15, 0.25], command='reload(GDC_RenderVrayLayer)\nGDC_RenderVrayLayer.GDC_RenderVrayLayer().nj_VrayRenderCreat("SET",1)')
        mc.button(label=u'CRS', width=130, height=30,
                  bgc=[0.13, 0.15, 0.25], command='reload(GDC_RenderVrayLayer)\nGDC_RenderVrayLayer.GDC_RenderVrayLayer().nj_VrayRenderCreat("CRS",1)')
        mc.button(label=u'IDZ', width=130, height=30,
                  bgc=[0.13, 0.15, 0.25], command='reload(GDC_RenderVrayLayer)\nGDC_RenderVrayLayer.GDC_RenderVrayLayer().nj_VrayRenderCreat("IDZ",1)')
        mc.button(label=u'MOB', width=130, height=30,
                  bgc=[0.13, 0.15, 0.25], command='reload(GDC_RenderVrayLayer)\nGDC_RenderVrayLayer.GDC_RenderVrayLayer().nj_VrayRenderCreat("MBL",1)')
        #mc.button(label=u'GD', width=130, height=30,
                  #bgc=[0.13, 0.15, 0.25], command='reload(GDC_RenderVrayLayer)\nGDC_RenderVrayLayer.GDC_RenderVrayLayer().nj_VrayRenderCreat("GD",1)')
        mc.button(label=u'SKY', width=130, height=30,
                  bgc=[0.13, 0.15, 0.25], command='reload(GDC_RenderVrayLayer)\nGDC_RenderVrayLayer.GDC_RenderVrayLayer().nj_VrayRenderCreat("SKY",1)')
        mc.button(label=u'WIRE', width=130, height=30,
                  bgc=[0.13, 0.15, 0.25], command='reload(GDC_RenderVrayLayer)\nGDC_RenderVrayLayer.GDC_RenderVrayLayer().nj_VrayRenderCreat("WIRE",1)')

        mc.button(label=u'删除所有Elements', width=110,
                  height=30, bgc=[0, 0, 0.0], command='reload(GDC_RenderVrayLayer)\nGDC_RenderVrayLayer.GDC_RenderVrayLayer().gdc_VrayRenderDel(1,0)')
        mc.button(label=u'删除所有渲染层', width=110,
                  height=30, bgc=[0, 0, 0.0], command='reload(GDC_RenderVrayLayer)\nGDC_RenderVrayLayer.GDC_RenderVrayLayer().gdc_VrayRenderDel(0,1)')
                                  
        mc.setParent('..')
        mc.setParent('..')
        mc.frameLayout(label=u'IDP材质工具', bgc=[0, 0, 0.0], borderStyle='in',cll=0,cl=0)
        mc.rowColumnLayout(numberOfColumns=6)
        mc.button(label=u'R', width=80, height=30,
                  bgc=[1, 0, 0], command='reload(GDC_RenderVrayLayer)\nGDC_RenderVrayLayer.GDC_RenderVrayLayer().VrayIDAssign("R",1)')
        mc.button(label=u'G', width=80, height=30,
                  bgc=[0, 1, 0], command='reload(GDC_RenderVrayLayer)\nGDC_RenderVrayLayer.GDC_RenderVrayLayer().VrayIDAssign("G",1)')
        mc.button(label=u'B', width=80, height=30,
                  bgc=[0, 0, 1], command='reload(GDC_RenderVrayLayer)\nGDC_RenderVrayLayer.GDC_RenderVrayLayer().VrayIDAssign("B",1)')
        mc.button(label=u'M', width=80, height=30,
                  bgc=[0, 0, 0], command='reload(GDC_RenderVrayLayer)\nGDC_RenderVrayLayer.GDC_RenderVrayLayer().VrayIDAssign("M",1)')
        mc.setParent('..')
        mc.setParent('..')
        mc.frameLayout(label=u'常用工具', bgc=[0, 0, 0.0], borderStyle='in',cll=1,cl=1)
        mc.rowColumnLayout(numberOfColumns=2)

        mc.button(label=u'检测前期是否上传贴图信息', width=200, height=30,
                  bgc=[0.13, 0.6, 0.25], command='from idmt.maya.ShunLiu_common import csl_checkin\nreload(csl_checkin)\ncsl_checkin.csl_checkin().csl_ImageRecordCheck(type="quarter",server=1)\ncsl_checkin.csl_checkin().csl_ImageRecordCheck(type="half",server=1)\ncsl_checkin.csl_checkin().csl_ImageRecordCheck(type="full",server=1)')         
        mc.button(label=u'全尺寸贴图', width=200, height=30,
                  bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_checkin\nreload(csl_checkin)\ncsl_checkin.csl_checkin().csl_ImageSizeReadF(sizetype="full")')         
        mc.button(label=u'半尺寸贴图（1/4)', width=200, height=30,
                  bgc=[0.13, 0.15, 0.25], command='from idmt.maya.ShunLiu_common import csl_checkin\nreload(csl_checkin)\ncsl_checkin.csl_checkin().csl_ImageSizeReadF(sizetype="half")')  
        mc.button(label=u'1/4尺寸贴图（1/16)', width=200, height=30,
                  bgc=[0, 0, 0.0], command='from idmt.maya.ShunLiu_common import csl_checkin\nreload(csl_checkin)\ncsl_checkin.csl_checkin().csl_ImageSizeReadF(sizetype="quarter")')
##        mc.button(label=u'贴图尺寸转换并上传贴图信息', width=180, height=30,
##                  bgc=[0.6, 0.15, 0.25], command='from idmt.maya.ShunLiu_common import csl_checkin\nreload(csl_checkin)\ncsl_checkin.csl_checkin().csl_ImageSizeCover(type="quarter",server=1)\ncsl_checkin.csl_checkin().csl_ImageSizeCover(type="half",server=1)')                                     
        mc.setParent('..')
        mc.setParent('..')        
        mc.setParent('..')                
        # 渲染常用工具组
        mc.tabLayout(tabs, edit=True, tabLabel=(
            (child1, u'渲染流程'), (child2, u'Vray 渲染工具')))
        mc.showWindow('hh_RenderVray')
    #删除文件中RenderElements
    def VrayALLDelete(self,nodetype='aiAOV'):
        Info = mc.ls(type=nodetype)  
        if nodetype=='renderLayer':
            Info.remove('defaultRenderLayer')
            mc.editRenderLayerGlobals(currentRenderLayer='defaultRenderLayer')
        if mc.ls(Info) :
                mc.delete(Info)

 #导入参考       
    def csl_RefIm(self):
        while mc.file(q=1,r=1): 
          refPath=mc.file(q=1,r=1)
          if len(refPath)!=0:
              for r in refPath:
                  refRN=mc.file(r,q=1,rfn=1)
                  if(mc.file(r,q=1,dr=1)):
                      mc.file(refRN,loadReference=1)
                  mc.file(r,ir=1) 

    def csl_VraymeshInfo(self,meshtype='s'):
        meshs=mc.ls(type='mesh',l=1)
        meshList=[]
        namespaces=mc.namespaceInfo(listOnlyNamespaces=1)
        for i in range(len(meshs)):
            for j in range(len(namespaces)) :
                if namespaces[j] in meshs[i] and namespaces[j].split('_')[1][0].lower()==meshtype:
                    meshP=mc.listRelatives(meshs[i],p=1,f=1)
                    if meshP:
                        meshList.append(meshP[0])
        return meshList

    #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【NJ2017】【创建渲染层】
    #  Author  : 韩虹
    #  Data    : 2016_05
    #ip=0,不显示D，ip=1，显示弹出
    #------------------------------#
    def nj_VrayRenderCreat(self,renderName='CHR',ip=0):
        print '====star,please wait........====='
        self.gdc_RendertimeRecord()
        self.gdc_VrayRenderDel(rd=1,re=1)
        objs=[]

        if renderName in ['IDZ','MBL','WIRE']:
            objs=self.gdc_objsInfo(0,'mesh',0)
        elif renderName in ['SKY']:
            objs=mc.ls(sl=1,tr=1,l=1)
            if objs==[]:
                mc.error('=============No select,please select===========')
        else:
            objSelect=mc.ls(sl=1,tr=1,l=1)
            if objSelect:
                objs=self.gdc_objsInfo(1,'mesh',0)
            else:
                objs=self.gdc_objsInfo(0,'mesh',0)
        if mc.objExists(renderName):
            mc.delete(renderName)
        mc.select(objs)

        print '===========reacord==========='
        self.gdc_RendertimeRecord()
        meshall=self.gdc_meshInfo()
        objchr=meshall[0]
        objpr=meshall[1]
        objset=meshall[2]
        self.gdc_RendertimeRecord()
        global RenderLayerName
        RenderLayerName=''
        if renderName=='CHR' and ip==1:
            mc.layoutDialog(ui='reload(GDC_RenderVrayLayer)\nGDC_RenderVrayLayer.GDC_RenderVrayLayer().RenderLayerCreat_UI("CHR")',t=u'创建渲染文件')
        elif renderName=='SET' and ip==1:
            mc.layoutDialog(ui='reload(GDC_RenderVrayLayer)\nGDC_RenderVrayLayer.GDC_RenderVrayLayer().RenderLayerCreat_UI("SET")',t=u'创建渲染文件')
        elif renderName=='IDZ' and ip==1:
            mc.layoutDialog(ui='reload(GDC_RenderVrayLayer)\nGDC_RenderVrayLayer.GDC_RenderVrayLayer().RenderLayerCreat_UI("IDZ")',t=u'创建渲染文件')
        elif renderName=='MBL' and ip==1:
            mc.layoutDialog(ui='reload(GDC_RenderVrayLayer)\nGDC_RenderVrayLayer.GDC_RenderVrayLayer().RenderLayerCreat_UI("MBL")',t=u'创建渲染文件')
        elif renderName=='SKY' and ip==1:
            mc.layoutDialog(ui='reload(GDC_RenderVrayLayer)\nGDC_RenderVrayLayer.GDC_RenderVrayLayer().RenderLayerCreat_UI("SKY")',t=u'创建渲染文件')
        elif renderName=='CRS' and ip==1:
            mc.layoutDialog(ui='reload(GDC_RenderVrayLayer)\nGDC_RenderVrayLayer.GDC_RenderVrayLayer().RenderLayerCreat_UI("CRS")',t=u'创建渲染文件')
        elif renderName=='WIRE' and ip==1:
            mc.layoutDialog(ui='reload(GDC_RenderVrayLayer)\nGDC_RenderVrayLayer.GDC_RenderVrayLayer().RenderLayerCreat_UI("WIRE")',t=u'创建渲染文件')
        if RenderLayerName=='' and ip==1:
            mc.error(u'=======请输入层名==========')
        if ip==1 and RenderLayerName!='':
            renderName=RenderLayerName
        #设置可渲染物体
        print '=======primaryVisibility======'
        self.gdc_RendertimeRecord()
        if 'CHR' in  renderName:
            chrobj= objchr+objpr
            if chrobj:
                for obj in chrobj:
                    mesh=mc.listRelatives(obj,s=1,type='mesh',f=1)
                    if mesh:
                        for me in mesh:
                            mc.setAttr((me+'.primaryVisibility'),1)
            if objset:
                for obj in objset:
                    mesh=mc.listRelatives(obj,s=1,type='mesh',f=1)
                    if mesh:
                        for me in mesh:
                            mc.setAttr((me+'.primaryVisibility'),0)
        elif 'SET' in renderName :
            chrobj= objchr+objpr
            if chrobj:
                for obj in chrobj:
                    mesh=mc.listRelatives(obj,s=1,type='mesh',f=1)
                    if mesh:
                        for me in mesh:
                            mc.setAttr((me+'.primaryVisibility'),0)
            if objset:
                for obj in objset:
                    mesh=mc.listRelatives(obj,s=1,type='mesh',f=1)
                    if mesh:
                        for me in mesh:
                            mc.setAttr((me+'.primaryVisibility'),1)
        else:
            chrobj= objchr+objpr+objset
            if chrobj:
                for obj in chrobj:
                    mesh=mc.listRelatives(obj,s=1,type='mesh',f=1)
                    if mesh:
                        for me in mesh:
                            mc.setAttr((me+'.primaryVisibility'),1)
        #非灯光层，删导入参考，删除材质
        print '=======RefIm======'
        self.gdc_RendertimeRecord()

        if  renderName in ['IDZ','MBL','WIRE']:
            self.gdc_RefIm()
            #mel.eval('source "zzjUtilityTools.mel";lighting_DeleteUnusedNode()')
        if renderName=='IDZ':
            if objchr:
                self.VrayShaderAssign(objchr,'R',0,1)
            if  objpr:
                self.VrayShaderAssign(objpr,'G',0,1)
            if  objset:
                self.VrayShaderAssign(objset,'B',0,1)
        if renderName=='WIRE':
            objs=objset+objchr+objpr
            self.VrayShaderAssign(objs,'wf',0,1)
        #创建渲染层
        print '=======creatRenderLayer star======'
        self.gdc_RendertimeRecord()
        mc.createRenderLayer(objs,name=renderName, noRecurse=1, makeCurrent=1)
        sName=['CHR','SET','CRS']
        for i in range(len(sName)):
            if sName[i] in renderName:
                self.nj_VraySettings('co')
                mc.setAttr('vraySettings.globopt_light_doLights' ,1)
                self.nj_VrayRenderElementsCreat('NM')
                self.nj_VrayRenderElementsCreat('DF')
                self.nj_VrayRenderElementsCreat('ID')
                self.nj_VrayRenderElementsCreat('MD')

        if renderName =='GD':
            self.nj_VraySettings('co')
            csl_toolCommons.csl_toolComnnons().csl_AttrAction(line="select",attrtype="GD")
            GDS=mc.ls(sl=1,l=1)
            if GDS:
                for GD in GDS:
                    objs.remove(GD)
            else:
                mc.error(u'===========文件中没有GD属性物体，请检查===========')
            meshs=[]
            if objs:
                for obj in objs:
                    shapes=mc.listRelatives(obj,s=1,f=1,type='mesh')
                    if shapes:
                        meshs.append(obj)
            if meshs:
                for mesh in meshs:
                    try:
                        mc.setAttr((mesh+'.primaryVisibility'),0)
                    except:
                        pass
        if renderName=='IDZ':
            self.nj_VrayRenderElementsCreat('MID')
            self.nj_VrayRenderElementsCreat('ZD')
        if renderName=='MBL':
            self.nj_VraySettings('mv')
            self.nj_VrayRenderElementsCreat('MOB')
        if renderName=='SKY':
            self.nj_VraySettings('sky')
        if renderName=='WIRE':
            self.nj_VraySettings('co')
        mc.editRenderLayerGlobals(currentRenderLayer='defaultRenderLayer')
        mc.setAttr("defaultRenderLayer.renderable", 0)
        print '=======save======'
        self.gdc_RendertimeRecord()
        self.nj_RenderFileSave(renderName)
        return 0

    #------------------------------#
    # 【NJ2017】【创建渲染层】【适用于自动分层】
    #  Author  : 韩虹
    #  Data    : 2016_05
    #
    #------------------------------#
    def nj_VrayRenderCreatAuto(self,renderName='CHR'):
        self.gdc_VrayRenderDel(rd=1,re=1)
        objs=mc.ls(sl=1,l=1)
        if mc.objExists(renderName):
            mc.delete(renderName)
        mc.select(objs)
        meshall=self.gdc_meshInfo()
        objchr=meshall[0]
        objpr=meshall[1]
        objset=meshall[2]
        meshAttr=self.csl_meshAttr()
        chrr=meshAttr[0]
        setr=meshAttr[1]
        #设置可渲染物体
        if renderName in ['CHR']:
            chrobj= chrr
            if chrobj:
                for obj in chrobj:
                    mesh=mc.listRelatives(obj,s=1,type='mesh',f=1)
                    if mesh:
                        for me in mesh:
                            mc.setAttr((me+'.primaryVisibility'),1)
            if setr:
                for obj in setr:
                    mesh=mc.listRelatives(obj,s=1,type='mesh',f=1)
                    if mesh:
                        for me in mesh:
                            mc.setAttr((me+'.primaryVisibility'),0)
        elif renderName in ['SET']:
            chrobj= chrr
            if chrobj:
                for obj in chrobj:
                    mesh=mc.listRelatives(obj,s=1,type='mesh',f=1)
                    if mesh:
                        for me in mesh:
                            mc.setAttr((me+'.primaryVisibility'),0)
            if setr:
                for obj in setr:
                    mesh=mc.listRelatives(obj,s=1,type='mesh',f=1)
                    if mesh:
                        for me in mesh:
                            mc.setAttr((me+'.primaryVisibility'),1)
        else:
            chrobj= chrr+setr
            if chrobj:
                for obj in chrobj:
                    mesh=mc.listRelatives(obj,s=1,type='mesh',f=1)
                    if mesh:
                        for me in mesh:
                            mc.setAttr((me+'.primaryVisibility'),1)
        #非灯光层，删导入参考，删除材质
        if  renderName in ['IDZ','MBL','WIRE']:
            self.gdc_RefIm()
            #mel.eval('source "zzjUtilityTools.mel";lighting_DeleteUnusedNode()')
        if renderName=='IDZ':
            if objchr:
                self.VrayShaderAssign(objchr,'R',0,1)
            if  objpr:
                self.VrayShaderAssign(objpr,'G',0,1)
            if  objset:
                self.VrayShaderAssign(objset,'B',0,1)
        #创建渲染层
        mc.createRenderLayer(objs,name=renderName, noRecurse=1, makeCurrent=1)
        if renderName in ['CHR','SET','CRS']:
            self.nj_VraySettings('co')
            mc.setAttr('vraySettings.globopt_light_doLights' ,1)
            self.nj_VrayRenderElementsCreat('NM')
            self.nj_VrayRenderElementsCreat('DF')
            self.nj_VrayRenderElementsCreat('ID')
            self.nj_VrayRenderElementsCreat('MD')

        if renderName =='GD':
            self.nj_VraySettings('co')
            csl_toolCommons.csl_toolComnnons().csl_AttrAction(line="select",attrtype="GD")
            GDS=mc.ls(sl=1,l=1)
            if GDS:
                for GD in GDS:
                    objs.remove(GD)
            else:
                mc.error(u'===========文件中没有GD属性物体，请检查===========')
            meshs=[]
            if objs:
                for obj in objs:
                    shapes=mc.listRelatives(obj,s=1,f=1,type='mesh')
                    if shapes:
                        meshs.append(obj)
            if meshs:
                for mesh in meshs:
                    try:
                        mc.setAttr((mesh+'.primaryVisibility'),0)
                    except:
                        pass
        if renderName=='IDZ':
            self.nj_VraySettings('id')
            self.nj_VrayRenderElementsCreat('MID')
            self.nj_VrayRenderElementsCreat('ZD')
        if renderName=='MBL':
            self.nj_VraySettings('mv')
            self.nj_VrayRenderElementsCreat('MOB')
        if renderName in ['SKY']:
            self.nj_VraySettings('sky')
        mc.editRenderLayerGlobals(currentRenderLayer='defaultRenderLayer')
        mc.setAttr("defaultRenderLayer.renderable", 0)
        self.nj_RenderFileSave(renderName)
        return 0
    #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【NJ2017】【Vray Element 创建】
    #  Author  : 韩虹
    #  Data    : 2016_05
    #------------------------------#

    def nj_VrayRenderElementsCreat(self,em='NM'):
        if mc.objExists(em) and mc.nodeType(em)=='VRayRenderElement':
            mc.delete(em)
        if em=='NM':
            nor=mel.eval('vrayAddRenderElement normalsChannel')
            mc.rename(nor,em)
            mc.setAttr((em+'.vray_name_normals'),em,type='string')
        if em=='DF':
            nor=mel.eval('vrayAddRenderElement diffuseChannel')
            mc.rename(nor,em)
            mc.setAttr((em+'.vray_name_rawdiffuse'),em,type='string')
        if em=='ID':
            nor=mel.eval('vrayAddRenderElement MultiMatteElement')
            mc.rename(nor,em)
            mc.setAttr((em+'.vray_name_multimatte'),em,type='string')
            mc.setAttr((em+'.vray_redon_multimatte'),1)
            mc.setAttr((em+'.vray_redid_multimatte'),1)

            mc.setAttr((em+'.vray_greenon_multimatte'),1)
            mc.setAttr((em+'.vray_greenid_multimatte'),2)

            mc.setAttr((em+'.vray_blueon_multimatte'),1)
            mc.setAttr((em+'.vray_blueid_multimatte'),3)

            mc.setAttr((em+'.vray_usematid_multimatte'),0)
            mc.setAttr((em+'.vray_usematid_multimatte'),0)

        if em=='MD':
            nor=mel.eval('vrayAddRenderElement materialIDChannel')
            mc.rename(nor,em)
            mc.setAttr((em+'.vray_filename_mtlid'),em,type='string')
            mc.setAttr((em+'.vray_considerforaa_mtlid'),0)
            mc.setAttr((em+'.vray_filtering_mtlid'),1)

        if em=='MID':
            nor=mel.eval('vrayAddRenderElement materialIDChannel')
            mc.rename(nor,em)
            mc.setAttr((em+'.vray_filename_mtlid'),em,type='string')
            mc.setAttr((em+'.vray_considerforaa_mtlid'),0)
            mc.setAttr((em+'.vray_filtering_mtlid'),1)

        if em=='ZD':
            nor=mel.eval('vrayAddRenderElement zdepthChannel')
            mc.rename(nor,em)
            mc.setAttr((em+'.vray_name_zdepth'),em,type='string')
            mc.setAttr((em+'.vray_depthFromCamera_zdepth'),0)
            mc.setAttr((em+'.vray_filtering_zdepth'),1)
            mc.setAttr((em+'.vray_depthBlack'),1)
            mc.setAttr((em+'.vray_depthWhite'),100)
        if em=='MOB':
            nor=mel.eval('vrayAddRenderElement velocityChannel')
            mc.rename(nor,em)
            mc.setAttr((em+'.vray_filename_velocity'),em,type='string')
            mc.setAttr((em+'.vray_max_velocity'),25)
            mc.setAttr((em+'.vray_max_velocity_last_frame'),24)


        return 0
                                                                                                                                                                        
    #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【通用】【】
    #  Author  : 韩虹
    #  Data    : 2016_05
    #sl 1,选择；2，全部
    #sp,s，场景，p,道具，c，角色，0，全部
    #------------------------------#
    def gdc_objsInfo(self,sl=1,infotype='mesh',sp='s'):
        meshs=[]
        if sl==0:
            objs=mc.ls(type=infotype,l=1)
            if objs:
                for obj in objs:
                    objn=mc.listRelatives(obj,p=1, type='transform', f=1)
                    if objn and objn[0] not in meshs and ':MODEL' in objn[0]:
                        meshs.append(objn[0])
            else:
                mc.error(u'=======文件中没有【%s】物体============'%infotype)
        else:
            objs=mc.ls(sl=1,tr=1,l=1)
            if objs:
                for obj in objs:
                    objn=mc.listRelatives(obj, ad=1, ni=1, type=infotype, f=1)
                    if objn:
                        for ob in objn:
                            mesh=mc.listRelatives(ob,p=1,type='transform',f=1)
                            if mesh and mesh[0] not in meshs and ':MODEL' in mesh[0]:
                                meshs.append(mesh[0])
            else:
                mc.error(u'======未选择物体，请选择==========')
        if meshs and sp in ['c','p','s']:
            ss=[]
            for mesh in meshs:
                space=mc.ls(mesh,sns=1)
                if space and '_' in space[-1] and len(space[-1].split('_'))>2 and space[-1].split('_')[1][0]!=sp:
                    ss.append(mesh)
                if ss:
                    for mes in ss:
                        if mes in meshs:
                            meshs.remove(mes)
        if meshs ==[]:
            meshs=0
            mc.select(cl=1)
        else:
            mc.select(meshs)
        return meshs
    #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【通用】【】
    #  Author  : 韩虹
    #  Data    : 2016_05
    #sl
    #------------------------------#
    def gdc_meshInfo(self):
        # 获取root
        refCHR = []
        refPROP = []
        refSET = []
        needSKY = []
        needPROP = []
        needrefSEA = []
        needInfo=[]
        light=''
        if mc.ls('CHR_GRP'):
            if mc.listRelatives('CHR_GRP', c=1, f=1, type='transform'):
                refCHR = mc.listRelatives('CHR_GRP', c=1, f=1, type='transform')
        if mc.ls('PRP_GRP'):
            if mc.listRelatives('PRP_GRP', c=1, f=1, type='transform'):
                refPROP = mc.listRelatives('PRP_GRP', c=1, f=1, type='transform')
        if mc.ls('SET_GRP'):
            if mc.listRelatives('SET_GRP', c=1, f=1, type='transform'):
                refSETgroup = mc.listRelatives('SET_GRP', c=1, f=1, type='transform')
                refSET=mc.listRelatives(refSETgroup, c=1, f=1, type='transform')
        for i in range(3):
            needInfo = []
            if i == 0:
                refGrps = refCHR
            if i == 1:
                refGrps = refPROP
            if i == 2:
                refGrps = refSET
            if refGrps:
                meshes = mc.listRelatives(refGrps, ad=1, ni=1, type='mesh', f=1)
                if meshes:
                    for mesh in meshes:
                        objs=mc.listRelatives(mesh,p=1,f=1)
                        if  objs and ':RIG|' not in mesh and ':FX|' not in mesh and 'DEFORMERS' not in mesh :
                          needInfo.append(objs[0])
            if i == 0:
                CHRR = needInfo
            if i == 1:
                PROPR = needInfo
            if i == 2:
                SETR = needInfo
        result = [CHRR,PROPR,SETR]
        return result
    #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【通用】【Vray 基本设置】
    #  Author  : 韩虹
    #  Data    : 2016_5
    #infotype,co，普通灯光+color层设置
    #------------------------------#
    def nj_VraySettings(self,infotype='co'):
        mc.setAttr('defaultRenderGlobals.currentRenderer', 'vray', type='string')
        mel.eval('source "vrayRegisterRenderer"')
        mel.eval('vrayCreateVRaySettingsNode()')
        import idmt.pipeline.db
        shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
        shot=shotInfos[0]+'_'+shotInfos[1]+'_'+shotInfos[2]+'_'+shotInfos[3]
        anim = idmt.pipeline.db.GetAnimByFilename(shot)
        fpsFrame = anim.fps
        startFrame = anim.frmStart
        endFrame = anim.frmEnd
        startFrame = anim.frmStart
        resW = anim.resolutionW
        resH = anim.resolutionH
        if fpsFrame == 25:
            mc.currentUnit(time='pal')
        if fpsFrame == 24:
            mc.currentUnit(time='film')
        if fpsFrame == 30:
            mc.currentUnit(time='ntsc')
        if startFrame and fpsFrame:
            # 起始帧
            mc.playbackOptions(min=startFrame)
            # 起始预留
            preStartFrame = startFrame - 12
            mc.playbackOptions(animationStartTime=preStartFrame)
            # 结束帧
            mc.playbackOptions(max=endFrame)
            # 结束预留
            posEndFrame = endFrame + 12
            mc.playbackOptions(animationEndTime=posEndFrame)

        mc.setAttr('defaultRenderGlobals.startFrame',startFrame)
        mc.setAttr('defaultRenderGlobals.endFrame',endFrame)
        #设置当前渲染器为vray渲染器
        mc.setAttr('vraySettings.aspectLock', 0)
        mc.setAttr('vraySettings.width', resW)
        mc.setAttr('vraySettings.height', resH)
        mc.setAttr('vraySettings.pixelAspect', 1)
        mc.setAttr('vraySettings.imageFormatStr','tif',type='string')
        try:
            mc.setAttr('vraySettings.imageFormatStr','png',type='string')
            mc.setAttr ('vraySettings.imgOpt_png_bitsPerChannel', 16)
        except:
            pass
        #nj2017渲染基本设置
        mc.setAttr('vraySettings.fileNamePrefix','<Layer>/<Scene>_<Layer>',type='string')
        #设置素材命名方式
        mc.setAttr('vraySettings.imageFormatStr','png',type='string')
        mc.setAttr ('vraySettings.imgOpt_png_bitsPerChannel', 16)
        #渲染格式
        mc.setAttr("vraySettings.sRGBOn",1)
        #勾选保证MAYA默认渲染窗口的图片效果颜色显示正确
        mc.setAttr ('vraySettings.animType', 1)
        mc.setAttr ('vraySettings.animBatchOnly', 1)
        mc.setAttr ('vraySettings.fileNamePadding', 4)
        #渲染设置

        #VRAY
        #Global options
        mc.setAttr("vraySettings.globopt_geom_displacement",1)
        mc.setAttr("vraySettings.globopt_render_viewport_subdivision",0)
        mc.setAttr("vraySettings.globopt_cache_geom_plugins",0)
        mc.setAttr("vraySettings.globopt_cache_bitmaps",0)
        mc.setAttr("vraySettings.globopt_light_doLights",1)
        mc.setAttr("vraySettings.globopt_light_doDefaultLights",1)

        mc.setAttr ('vraySettings.samplerType', 1)
        mc.setAttr ('vraySettings.minShadeRate', 2)
        mc.setAttr ('vraySettings.divShadeSubdivs', 1)
        mc.setAttr ('vraySettings.renderMaskMode', 0)
        mc.setAttr ('vraySettings.aaFilterOn', 1)
        mc.setAttr ('vraySettings.aaFilterType',1)
        mc.setAttr ('vraySettings.aaFilterSize',2)
        #Adptive
        mc.setAttr ('vraySettings.dmcMinSubdivs',1)
        mc.setAttr ('vraySettings.dmcMaxSubdivs',16)
        mc.setAttr ('vraySettings.dmcThreshold',0.006)
        mc.setAttr ('vraySettings.dmcs_timeDependent',1)
        mc.setAttr ('vraySettings.dmcs_subdivsMult',1)

        mc.setAttr("vraySettings.sRGBOn",1)
        mc.setAttr("vraySettings.globopt_ray_maxIntens_on",1)
        mc.setAttr("vraySettings.globopt_ray_maxIntens",0.8)
        #color mapping
        mc.setAttr("vraySettings.cmap_type",1)
        #mc.setAttr("vraySettings.cmap_darkMule",1)
       # mc.setAttr("vraySettings.cmap_brightMult",1)
        #mc.setAttr("vraySettings.cmap_gamma",2.2)
        #mc.setAttr("vraySettings.cmap_affectBackground",1)
        #mc.setAttr("vraySettings.cmap_adaptationOnly",2)
        #线性
        mc.setAttr("vraySettings.cmap_subpixelMapping",0)
        mc.setAttr("vraySettings.cmap_linearworkflow",1)
        mc.setAttr("vraySettings.cmap_affectSwatches",1)
        mc.setAttr("vraySettings.sRGBOn",1)
        #color mapping
        mc.setAttr("vraySettings.cmap_type",1)
        #mc.setAttr("vraySettings.cmap_darkMule",1)
        #mc.setAttr("vraySettings.cmap_brightMult",1)
        #mc.setAttr("vraySettings.cmap_gamma",2.2)
        #mc.setAttr("vraySettings.cmap_affectBackground",1)
        #mc.setAttr("vraySettings.cmap_adaptationOnly",2)
        #线性
        mc.setAttr("vraySettings.cmap_subpixelMapping",0)
        mc.setAttr("vraySettings.cmap_linearworkflow",1)
        mc.setAttr("vraySettings.cmap_affectSwatches",1)

        mc.setAttr("vraySettings.dmcs_adaptiveAmount",0.85)
        mc.setAttr("vraySettings.dmcs_adaptiveThreshold",0.01)
        mc.setAttr("vraySettings.dmcs_adaptiveMinSamples",16)

        #settings
        mc.setAttr ('vraySettings.ddisplac_edgeLength',4)
        mc.setAttr ('vraySettings.ddisplac_viewDependent',1)
        mc.setAttr ('vraySettings.ddisplac_maxSubdivs',5)
        mc.setAttr ('vraySettings.ddisplac_tightBounds',1)
        mc.setAttr ('vraySettings.ddisplac_amount',1)
        #素材命名
        mc.setAttr('vraySettings.fileNamePrefix' ,'<Layer>/<Scene>_<Layer>',type='string')
        mc.setAttr('vraySettings.relements_separateFolders',1)
        mc.setAttr('vraySettings.fileNameRenderElementSeparator' ,'_',type='string')
        #内存
        mc.setAttr('vraySettings.sys_rayc_dynMemLimit' ,18000)
        if infotype=='co':
            mc.setAttr('vraySettings.globopt_light_doDefaultLights' ,1)
            mc.setAttr('vraySettings.globopt_light_doShadows' ,1)
            mc.setAttr('vraySettings.globopt_light_onlyGI' ,0)
            mc.setAttr('vraySettings.globopt_light_ignoreLightLinking' ,0)

            mc.setAttr('vraySettings.globopt_light_disableSelfIllumination' ,0)

            mc.setAttr('vraySettings.globopt_mtl_reflectionRefraction' ,1)
            mc.setAttr('vraySettings.globopt_mtl_glossy' ,1)
            mc.setAttr('vraySettings.globopt_mtl_doMaps' ,1)
            mc.setAttr('vraySettings.globopt_mtl_filterMaps' ,1)
            mc.setAttr('vraySettings.globopt_mtl_SSSEnabled' ,0)
            #灯光作用
            mc.setAttr('vraySettings.globopt_light_doLights' ,1)
            #Image sampler
            mc.setAttr('vraySettings.minShadeRate' ,2)
            mc.setAttr('vraySettings.dmcMaxSubdivs' ,32)
            mc.setAttr('vraySettings.dontSaveRgbChannel' ,1)
            #渲默认colr
            mc.setAttr('vraySettings.dontSaveRgbChannel' ,0)
        if infotype=='id':
            #灯光作用
            mc.setAttr('vraySettings.globopt_light_doLights' ,0)
            #advanced
            mc.setAttr('vraySettings.globopt_light_doDefaultLights' ,1)
            mc.setAttr('vraySettings.globopt_light_doShadows' ,0)
            mc.setAttr('vraySettings.globopt_light_onlyGI' ,0)
            mc.setAttr('vraySettings.globopt_light_ignoreLightLinking' ,0)
            mc.setAttr('vraySettings.globopt_light_disableSelfIllumination' ,0)
            mc.setAttr('vraySettings.globopt_mtl_reflectionRefraction' ,0)
            mc.setAttr('vraySettings.globopt_mtl_glossy' ,0)
            mc.setAttr('vraySettings.globopt_mtl_doMaps' ,0)
            mc.setAttr('vraySettings.globopt_mtl_filterMaps' ,0)
            mc.setAttr('vraySettings.globopt_mtl_SSSEnabled' ,0)
            #Image sampler
            #Adaptive subdivision
            mc.setAttr('vraySettings.samplerType' ,1)
            mc.setAttr('vraySettings.minShadeRate' ,2)
            mc.setAttr('vraySettings.dontSaveRgbChannel' ,1)
            #不渲默认colr
            mc.setAttr('vraySettings.dontSaveRgbChannel' ,1)
        #motionblur
        if infotype=='mv':
            #灯光作用
            mc.setAttr('vraySettings.globopt_light_doLights' ,0)
            #advanced
            mc.setAttr('vraySettings.globopt_light_doDefaultLights' ,1)
            mc.setAttr('vraySettings.globopt_light_doShadows' ,0)
            mc.setAttr('vraySettings.globopt_light_onlyGI' ,0)
            mc.setAttr('vraySettings.globopt_light_ignoreLightLinking' ,0)
            mc.setAttr('vraySettings.globopt_light_disableSelfIllumination' ,0)
            mc.setAttr('vraySettings.globopt_mtl_reflectionRefraction' ,0)
            mc.setAttr('vraySettings.globopt_mtl_glossy' ,0)
            mc.setAttr('vraySettings.globopt_mtl_doMaps' ,0)
            mc.setAttr('vraySettings.globopt_mtl_filterMaps' ,0)
            mc.setAttr('vraySettings.globopt_mtl_SSSEnabled' ,0)
            #Adaptive subdivision
            mc.setAttr('vraySettings.samplerType' ,2)
            mc.setAttr('vraySettings.subdivMinRate' ,-1)
            mc.setAttr('vraySettings.subdivMaxRate' ,1)
            #exr
            mc.setAttr('vraySettings.imageFormatStr','exr',type='string')
            #不渲默认colr
            mc.setAttr('vraySettings.dontSaveRgbChannel' ,1)
        if infotype=='sky':

            #灯光作用
            mc.setAttr('vraySettings.globopt_light_doLights' ,1)
            #advanced
            mc.setAttr('vraySettings.globopt_light_doDefaultLights' ,1)
            mc.setAttr('vraySettings.globopt_light_doShadows' ,0)
            mc.setAttr('vraySettings.globopt_light_onlyGI' ,0)
            mc.setAttr('vraySettings.globopt_light_ignoreLightLinking' ,0)
            mc.setAttr('vraySettings.globopt_light_disableSelfIllumination' ,0)
            mc.setAttr('vraySettings.globopt_mtl_reflectionRefraction' ,1)
            mc.setAttr('vraySettings.globopt_mtl_glossy' ,1)
            mc.setAttr('vraySettings.globopt_mtl_doMaps' ,1)
            mc.setAttr('vraySettings.globopt_mtl_filterMaps' ,1)
            mc.setAttr('vraySettings.globopt_mtl_SSSEnabled' ,0)
            #Adaptive
            mc.setAttr('vraySettings.samplerType' ,1)
            mc.setAttr('vraySettings.dmcMinSubdivs' ,1)
            mc.setAttr('vraySettings.dmcMaxSubdivs' ,32)
            #渲默认colr
            mc.setAttr('vraySettings.dontSaveRgbChannel' ,0)
        return 0

    #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【通用】【删除所有渲染层及RenderElement】
    #  Author  : 韩虹
    #  Data    : 2016_06_07
    #------------------------------#
    def gdc_VrayRenderDel(self,rd=1,re=1):
        if rd==1:
            mc.editRenderLayerGlobals(currentRenderLayer='defaultRenderLayer')
            layers=mc.ls(type='renderLayer',l=1)
            layers.remove('defaultRenderLayer')
            if layers:
                for layer in layers:
                    try:
                        mc.delete(layer)
                    except:
                        pass
        if re==1:
            vre=mc.ls(type='VRayRenderElement',l=1)
            if vre:
                try:
                    mc.delete(vre)
                except:
                    mc.warning(u'========无法删除VRayRenderElement,请检查文件=======')
        return 0
    #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【通用】【渲染文件存】
    #  Author  : 韩虹
    #  Data    : 2016_06_07
    #------------------------------#
    def nj_RenderFileSave(self,rendType='CHR'):
        locaPath='D:/TempInfo/renderLayerFile/'
        fileName=mc.file(q=1,sn=1,shn=1)
        if '_' in fileName and fileName.split('_')[0]=='nj' and len(fileName.split('_'))>4:
            shotInfo=fileName.split('_')
            fileSaveFile=shotInfo[0]+'_'+shotInfo[1]+'_'+shotInfo[2]+'_'+shotInfo[3]+'_'+rendType+'_lr_c001.mb'
            filepath=locaPath+shotInfo[0]+'/'+shotInfo[1]+'_'+shotInfo[2]+'_'+shotInfo[3]+'/'
            mc.sysFile(filepath, makeDir=True)
            mc.file(type='mayaBinary')
            mc.file(rename=filepath+fileSaveFile)
            mc.file(save=1,type ='mayaBinary',f = 1)
            print (u'==============【%s】已创建============='%(filepath+fileSaveFile) )
        else:
            mc.warning(u'==========文件命名不正确，请检查文件命名=========')
            mc.error(u'==========文件命名不正确，请检查文件命名=========')
        return 0
#导入参考
    def gdc_RefIm(self):
        while mc.file(q=1,r=1):
          refPath=mc.file(q=1,r=1)
          if len(refPath)!=0:
              for r in refPath:
                  refRN=mc.file(r,q=1,rfn=1)
                  if(mc.file(r,q=1,dr=1)):
                      mc.file(refRN,loadReference=1)
                  mc.file(r,ir=1)
        return 0

    def VrayIDAssign(self,shaderType='R',mtID=0):
        objs=mc.ls(sl=1,tr=1,l=1)
        meshs=[]
        if objs:
            for obj in objs:
                mesh=mc.listRelatives(obj, ad=1, ni=1, type='mesh', f=1)
                if mesh:
                    for me in mesh:
                        ob=mc.listRelatives(me,p=1,type='transform',f=1)
                        if ob:
                            meshs.append(ob[0])
        else:
            mc.error(u'========请选择===========')
        if meshs:
            RE='MID'
            self.VrayShaderAssign(meshs,shaderType,0,mtID)
            if not mc.objExists(RE):
                self.nj_VrayRenderElementsCreat('MID')
            mc.setAttr(('vraySettings.dontSaveRgbChannel'),1)

        return u'=======================选择物体已赋【%s】材质==========='%shaderType


    #------------------------------#
    # 【通用】【Vray材质球创建】
    #  Author  : 韩虹
    #  Data    : 2016_02_16
    # modify:2016_06
    #------------------------------#
    def VrayShaderAssign(self,meshs,shaderType='wf',transparency=0,mtID=0):
        #self.VrayLoading()
        if transparency==0:
            Shade='SHD_'+shaderType+'_vray'
            SG=Shade+'SG'
            #删除已有材质球和SG节点
            if mc.objExists(Shade)==0 and shaderType not in ['R','G','B']:
                mc.shadingNode('VRayMtl', asShader=True,n=Shade)
            if mc.objExists(Shade)==0 and shaderType in ['R','G','B']:
                mc.shadingNode('VRayLightMtl', asShader=True,n=Shade)
            if mc.objExists(SG)==0:
                mc.sets(renderable=1,noSurfaceShader=1,em=1,n=SG)
            try:
                mc.connectAttr(('%s.outColor' % Shade),('%s.surfaceShader' % SG))
            except:
                pass
            if meshs:
                mc.sets(meshs,e=1, forceElement = SG)
            else:
                pass
            if shaderType=='wf':
                #节点
                VRayEdge='VRayEdges'
                #创建节点
                if mc.objExists(VRayEdge):
                    mc.delete(VRayEdge)
                #创建节点
                #mc.shadingNode('aiUtility', asShader=True,n=Shade)
                mc.shadingNode('VRayEdges',asUtility=True,n=VRayEdge)
                #shade参数设置
                #VRayEdge设置
                mc.setAttr((VRayEdge+".edgesColor"), 1,1,1,type='double3')
                mc.setAttr((VRayEdge+".backgroundColor"), 0,0,0,type='double3')
                mc.setAttr((VRayEdge+".pixelWidth"),0.1)

                #连接节点
                #VRayEdge 与Shade连接
                mc.connectAttr((VRayEdge+'.outColor'),(Shade+'.diffuseColor'),f=1)
            if shaderType=='uv':
                image='//file-cluster/gdc/Projects/Ninjago/Ninjago_scratch/Modeling/prop/pe0012006001RonanMech/daily/UV_tex.TGA'
                fil='uvFile'
                if mc.objExists(fil):
                    mc.delete(fil)
                fi=mel.eval('createRenderNodeCB -as2DTexture "" file ""')
                mc.rename(fi,fil)
                mc.setAttr((fil+'.fileTextureName'), image, type='string')
                #连接节点
                mc.connectAttr((fil+'.outColor'),(Shade+'.diffuseColor'),f=1)
            if shaderType=='R':
                mc.setAttr(Shade+'.color',1,0,0,type='double3')
                if mtID==1:
                    mc.select(Shade)
                    self.VrayIDASet('set','vray_material_id',[1,0,0])
            if shaderType=='G':
                mc.setAttr(Shade+'.color',0,1,0,type='double3')
                if mtID==1:
                    mc.select(Shade)
                    self.VrayIDASet('set','vray_material_id',[0,1,0])
            if shaderType=='B':
                mc.setAttr(Shade+'.color',0,0,1,type='double3')
                if mtID==1:
                    mc.select(Shade)
                    self.VrayIDASet('set','vray_material_id',[0,0,1])
            if shaderType=='M':
                mc.setAttr(Shade+'.color',0,0,0,type='double3')
                if mtID==1:
                    mc.select(Shade)
                    self.VrayIDASet('set','vray_material_id',[0,0,0])
        return 0
    #------------------------------#
    # 【通用】【SET ,CHR 属性组】
    #  Author  : 韩虹
    #  Data    : 2016_06_27
    #
    #------------------------------#

    def csl_SETInfoRead(self):
        check=0
        chrInfo=[]
        setInfo=[]
        objs=mc.ls(tr=1,l=1)
        if objs:
            for obj in objs:
                if not mc.listRelatives(obj,s=1,f=1) and mc.objExists(obj+'.CHR'):
                    chrInfo.append(obj)
                if not mc.listRelatives(obj,s=1,f=1) and mc.objExists(obj+'.SET'):
                    setInfo.append(obj)
        if chrInfo or setInfo:
            check=1
        result=[check,chrInfo,setInfo]
        return result
    #------------------------------#
    # 【通用】【SET ,CHR 组MESH】
    #  Author  : 韩虹
    #  Data    : 2016_06_27
    #
    #------------------------------#
    def csl_meshAttr(self):
        CHRR = []
        SETR = []
        SETinfo=self.csl_SETInfoRead()
        check=SETinfo[0]
        chrInfo=SETinfo[1]
        setInfo=SETinfo[2]
        if check==1 and chrInfo:
            for chrGrp in chrInfo:
                meshs=mc.listRelatives(chrGrp, ad=1, ni=1, f=1, type='mesh')
                if meshs:
                    for mesh in meshs:
                        obj=mc.listRelatives(mesh,p=1,f=1,type='transform')
                        if obj and ':MODEL|' in obj[0] and 'DEFORMERS' not in obj[0] and obj[0] not in CHRR:
                            CHRR.append(obj[0])
        if check==1 and setInfo:
            for setGrp in setInfo:
                meshs=mc.listRelatives(setGrp, ad=1, ni=1, f=1, type='mesh')
                if meshs:
                    for mesh in meshs:
                        obj=mc.listRelatives(mesh,p=1,f=1,type='transform')
                        if obj and 'MODEL|' in obj[0] and 'DEFORMERS' not in obj[0] and obj[0] not in CHRR:
                            SETR.append(obj[0])
        if CHRR and not SETR:
            meshs=self.gdc_meshInfo()
            meshsAll=meshs[0]+meshs[1]+meshs[2]
            for CHR in CHRR:
                meshsAll.remove(CHR)
            SETR=meshsAll
        if SETR and not CHRR:
            meshs=self.gdc_meshInfo()
            meshsAll=meshs[0]+meshs[1]+meshs[2]
            for SET in SETR:
                meshsAll.remove(SET)
            CHRR=meshsAll
        if check==0:
            meshs=self.gdc_meshInfo()
            CHRR=meshs[0]+meshs[1]
            SETR=meshs[2]
        result=[CHRR,SETR]
        return result

    #------------------------------#
    # 【核】【设定ID参数】
    #  Author  : 韩虹
    #  Data    : 2016_03
        #------------------------------#
    def VrayIDASet(self,line='select',attrtype='vray_material_id',ID=[1,0,0]):
        attr=self.VrayAttrInfo(attrtype)[0]
        if attr and line=='select':
            objs=mc.ls(type='transform',l=1)+mc.ls(type='VRayMtl')+mc.ls(type='VRaySkinMtl')+mc.ls(type='VRaySwitchMtl')+mc.ls(type='VRayMtlHair3')+mc.ls(type='VRayMtl2Sided')+mc.ls(type='VRayLightMtl')
            objList=[]
            if objs :
                objList=[]
                for obj in objs:
                    if attrtype in ['vray_objectID','vray_material_id'] and mc.objExists(obj+'.'+attr) and mc.getAttr(obj+'.'+attr)==ID:
                        objList.append(obj)
                if objList:
                    mc.select(objList)
                    print u'\n'
                    print u'==========================已选择【%s】的物体==========================' %(attr+' '+str(ID))
                    print '=========================================='
                    for ob in objList:
                        print u'==============【%s】============='%ob
                    print '=========================================='
                    print u'\n'
                else:
                    print u'\n'
                    mc.warning(u'==========================文件中没有【%s】的物体==========================' % (attrtype+' '+str(ID)))
                    mc.error(u'==========================文件中没有【%s】的物体==========================' % (attrtype+' '+str(ID)))
                    print u'\n'
        if attr and line=='set':
            objs=mc.ls(sl=1,l=1)
            if objs:
                for obj in objs:
                    cmd= 'vray addAttributesFromGroup ' + obj+' '+attrtype+' 1'
                    try:
                        mel.eval(cmd)
                        if attr in ['vrayMaterialId']:
                            mc.setAttr((obj+'.vrayColorId'),ID[0],ID[1],ID[2])
                        else:
                            mc.setAttr((obj+'.'+attr),ID)
                        print obj
                    except:
                        pass
            else:
                print u'\n'
                mc.warning(u'没有选择物体，或者所选择的物体没有该vray属性选择，请选择有效物体')
                print u'\n'
        return 0
    #------------------------------#
    # 【辅】【Vray属性】
    #  Author  : 韩虹
    #  Data    : 2016_03
    #------------------------------#
    def VrayAttrInfo(self,attrtype='vray_objectID'):
        attr=''
        if  attrtype=='vray_objectID':
            attr='vrayObjectID'
            objtype=['mesh']
        if attrtype=='vray_subdivision':
            attr='vraySubdivEnable'
            objtype=['mesh']
        if attrtype=='vray_material_id':
            attr='vrayMaterialId'
            objtype=['VRayMtl','VRaySkinMtl','VRaySwitchMtl','VRayMtlHair3','VRayMtl2Sided','VRayLightMtl']
        return [attr,objtype]

    def RenderTools_Create_Layer_Button(self):
        global RenderLayerName
        RenderLayerName=mc.textField("RenderToolsLayerName",q=1, tx=1)
        return RenderLayerName

    def RenderLayerCreat_UI(self,rem='chr_co'):
        import maya.cmds as mc
        form = mc.setParent(q=True)
        mc.formLayout(form, e=True, width=20)
        t=mc.text(label=u'层名')
        mc.textField('RenderToolsLayerName',w=30,tx=rem)
        mc.setFocus('RenderToolsLayerName')
        b1=mc.button(l=u'创建文件',c='reload(GDC_RenderVrayLayer)\nGDC_RenderVrayLayer.GDC_RenderVrayLayer().RenderTools_Create_Layer_Button()\nmc.layoutDialog(dismiss="Abort")')
        mc.formLayout(form, edit=True,attachForm=[(t, 'top', 5), (t, 'left', 5), (t, 'right', 5),('RenderToolsLayerName','left',5),('RenderToolsLayerName','right',5),(b1,'left',25),(b1,'right',25)],
                                        attachNone=[(t, 'bottom'), ('RenderToolsLayerName', 'bottom'), (b1, 'bottom')],
                                        attachControl=[('RenderToolsLayerName', 'top', 5, t), (b1, 'top', 5, 'RenderToolsLayerName')])
        form

    #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【通用】【记录时间】
    #  Author  : 韩虹
    #  Data    :
    #------------------------------#
    def gdc_RendertimeRecord(self):
        import time
        print time.strftime('%Y-%m-%d-%H:%M:%S',time.localtime(time.time()))
