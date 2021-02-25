__author__ = 'xuweijian'
# -*- coding: utf-8 -*-

import maya.cmds as mc
import maya.mel as mel
from functools import partial
class VrayRenderLayer():
    def UI(self):
        if mc.window('VrayRender',exists=1):
            mc.deleteUI('VrayRender')
        mc.window('VrayRender')
        mc.columnLayout('column1')
        mc.button('CHR',l='CHR',c=partial(self.VrayRenderCreat,'CHR'))
        mc.button('SET',l='SET',c=partial(self.VrayRenderCreat,'SET'))
        mc.button('IDZ',l='IDZ',c=partial(self.VrayRenderCreat,'IDZ'))
        #mc.button('deleteElment',l='deleteElment',c=partial(self.VrayRenderDel,1,0))
        mc.button('deleteLayer',l='deleteLayer',c=partial(self.VrayRenderDel,1,1))
        mc.setParent('..')
        mc.showWindow('VrayRender')

    def VrayRenderCreat(self,layerName,UI=False):
        print 'begin'
        meshArry=self.getMesh()
        meshChr=meshArry[0]
        meshPr=meshArry[1]
        meshSet=meshArry[2]
        meshAll=meshChr+meshPr+meshSet
        print meshAll
        #meshAll=meshArry[0]+meshArry[1]+meshArry[2]
        self.VrayRenderDel()
        mc.createRenderLayer(meshAll,name=layerName, noRecurse=1, makeCurrent=1)
        if layerName=='CHR':
            self.VrayElementCreat('NM')
            self.VrayElementCreat('DF')
            self.VrayElementCreat('ID')
            self.VrayElementCreat('MD')
            chrobj=meshChr+meshPr
            if chrobj:
                for one in chrobj:
                    mc.setAttr((one+'.primaryVisibility'),1)
            if meshSet:
                for one in meshSet:
                    mc.setAttr((one+'.primaryVisibility'),0)
        #elif layerName=='SET'
        elif layerName=='SET':
            self.VrayElementCreat('NM')
            self.VrayElementCreat('DF')
            self.VrayElementCreat('ID')
            self.VrayElementCreat('MD')
            chrobj=meshChr+meshPr
            if chrobj:
                for one in chrobj:
                    mc.setAttr((one+'.primaryVisibility'),0)
            if meshSet:
                for one in meshSet:
                    mc.setAttr((one+'.primaryVisibility'),1)
        elif layerName=='IDZ':
            self.VrayElementCreat('ZD')
            self.VrayElementCreat('MID')
            if meshAll:
                for one in meshAll:
                    mc.setAttr((one+'.primaryVisibility'),1)
            self.VrayShaderAssign(meshChr,'R',0,1)
            self.VrayShaderAssign(meshPr,'G',0,1)
            self.VrayShaderAssign(meshSet,'B',0,1)




    def VrayRenderDel(self,rd=1,re=1,UI=0):
        if rd==1:
            mc.editRenderLayerGlobals(currentRenderLayer='defaultRenderLayer')
            layers=mc.ls(type='renderLayer',l=1)
            layers.remove('defaultRenderLayer')
            if layers:
                for layer in layers:
                    try:
                        mc.delete(layer)
                    except:
                        print 'cant delete layer %s'%layer
        if re==1:
            vre=mc.ls(type='VRayRenderElement',l=1)
            if vre:
                try:
                    mc.delete(vre)
                except:
                    print 'cant delete element %s'%vre


    def getMesh(self):
        meshChr=[]
        meshPr=[]
        meshSet=[]
        meshArry=[]
        if mc.ls('CHR_GRP'):
            obj=mc.listRelatives('CHR_GRP', ad=1, ni=1, type='mesh', f=1)
            if obj:
                meshChr=meshChr+obj
        if mc.ls('PRP_GRP'):
            obj=mc.listRelatives('PRP_GRP', ad=1, ni=1, type='mesh', f=1)
            if obj:
                meshPr=meshPr+obj
        if mc.ls('SET_GRP'):
            obj=mc.listRelatives('SET_GRP', ad=1, ni=1, type='mesh', f=1)
            if obj:
                meshSet=meshSet+obj
        meshArry=[meshChr,meshPr,meshSet]
        return meshArry




    def VrayElementCreat(self,em='NM'):
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
                #节点r
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
                    #mc.select(Shade)
                    self.VrayIDASet(Shade,[1,0,0])
            if shaderType=='G':
                mc.setAttr(Shade+'.color',0,1,0,type='double3')
                if mtID==1:
                    #mc.select(Shade)
                    self.VrayIDASet(Shade,[0,1,0])
            if shaderType=='B':
                mc.setAttr(Shade+'.color',0,0,1,type='double3')
                if mtID==1:
                    #mc.select(Shade)
                    self.VrayIDASet(Shade,[0,0,1])
            if shaderType=='M':
                mc.setAttr(Shade+'.color',0,0,0,type='double3')
                if mtID==1:
                    #mc.select(Shade)
                    self.VrayIDASet(Shade,[0,0,0])
        return 0

    def VrayIDASet(self,obj,ID=[1,0,0]):
        if obj:
            cmd= 'vray addAttributesFromGroup ' + obj+' vray_material_id 1'
            mel.eval(cmd)
            mc.setAttr((obj+'.vrayColorId'),ID[0],ID[1],ID[2])


VrayRenderLayer().UI()