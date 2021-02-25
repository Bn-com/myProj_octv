# -*- coding: utf-8 -*-

'''
Created on 2017-8

@author:韩虹

Redshift渲染工具
'''

import maya.cmds as mc
import maya.mel as mel
import pymel.core as pm
import os

from idmt.maya.commonCore.core_renderLayer import sk_renderLayerCore
reload(sk_renderLayerCore)



from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
reload(sk_referenceConfig)

from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
reload(sk_infoConfig)

from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools
reload(sk_sceneTools)


import re
class GA_RedShiftRender(object):
    def __init__(self):
        pass
    #----------------------------------------------------------#
    #----------------------------------------------------------------------------------------------------------#      #----------------------------------------------------------#
        #------------------------------#
    # 【渲染】【核心】【Redshift创建AOV通道】
    #  Author  : 韩虹
    #  Data    : 2017_08
    #------------------------------#
    def GA_RSAOVCreat(self,AOVAttr='AO',line='creat'):
        AOVtypeLists=['Ambient Occlusion','Background','Bump Normals','Caustics','Caustics Raw','Depth','Diffuse Filter','Diffuse Lighting','Diffuse Lighting Raw','Emission',
        'Global Illumination','Global Illumination Raw','Matte','Motion Vectors','Normals','ObjectID','Object-Space Bump Normals','Object-Space Positions',
        'Reflections','Reflections Filter','Reflections Raw','Refractions','Refractions Filter','Refractions Raw','Shadows','Specular Lighting','Sub Surface Scatter','Sub Surface Scatter Raw',
        'Total Diffuse Lighting Raw','Total Translucency Lighting Raw','Translucency Filter','Translucency GI Raw','Translucency Lighting Raw',
        'Volume Fog Emission','Volume Fog Tint','Volume Lighting','World Position']
        AOVNameLists=['rsAov_AmbientOcclusion','rsAov_Background','rsAov_BumpNormals','rsAov_Caustics','rsAov_CausticsRaw','rsAov_Depth','rsAov_DiffuseFilter','rsAov_DiffuseLighting',
        'rsAov_DiffuseLightingRaw','rsAov_Emission','rsAov_GlobalIllumination','rsAov_GlobalIlluminationRaw','rsAov_Matte','rsAov_MotionVectors','rsAov_Normals','rsAov_ObjectID',
        'rsAov_Object_SpaceBumpNormals','rsAov_Object_SpacePositions','rsAov_Reflections','rsAov_ReflectionsFilter','rsAov_ReflectionsRaw','rsAov_Refractions',
        'rsAov_RefractionsFilter','rsAov_RefractionsRaw','rsAov_Shadows','rsAov_SpecularLighting','rsAov_SubSurfaceScatter','rsAov_SubSurfaceScatterRaw','rsAov_TotalDiffuseLightingRaw',
        'rsAov_TotalTranslucencyLightingRaw','rsAov_TranslucencyFilter','rsAov_TranslucencyGIRaw','rsAov_TranslucencyLightingRaw','rsAov_VolumeFogEmission','rsAov_VolumeFogTint',
        'rsAov_VolumeLighting','rsAov_WorldPosition']
        AOVAttrLists=['AO','Background','BumpNormals','Caustics','CausticsRaw','Z','DiffuseFilter','DiffuseLighting','DiffuseLightingRaw','Emission','GI','GIRaw','Matte','MotionVectors',
        'N','ID','ObjectBumpNormal','ObjectPosition','Reflections','ReflectionsFilter','ReflectionsRaw','Refractions','RefractionsFilter','RefractionsRaw','Shadows','SpecularLighting',
        'SSS','SSSRaw','TotalDiffuseLightingRaw','TotalTransLightingRaw','TransTint','TransGIRaw','TransLightingRaw','VolumeFogEmission','VolumeFogTint','VolumeLighting','P']
        AOVName=''
        AOVtype=''
        for i in range(len(AOVAttrLists)):
            if AOVAttrLists[i]==AOVAttr:
                AOVName=AOVNameLists[i]
                AOVtype=AOVtypeLists[i]
            if AOVAttrLists[i]==AOVAttr and mc.objExists(AOVName):
                mc.delete(AOVName)
            if AOVAttrLists[i]==AOVAttr and line=='creat':
                mel.eval('source "redshiftCreateAovTab.mel"')
                cmd="redshiftCreateAov(" + '"'+AOVtype+'"'+")"
                mel.eval(cmd)
                mel.eval('redshiftUpdateActiveAovList()')
        return [AOVAttr,AOVName,AOVtype]
    #----------------------------------------------------------------------------------------------------------#      #----------------------------------------------------------#
        #------------------------------#
    # 【渲染】【核心】PuzzleMatte AOV创建及设置】
    #  Author  : 韩虹
    #  Data    : 2017_09
    #------------------------------#
    def GA_RSAOVCreatSP(self,AOVAttr='PuzzleMatte',line='creat',types='chrID'):
        mel.eval('source "redshiftCreateAovTab.mel"')
        if AOVAttr=='PuzzleMatte':
            AOVLists=self.GA_RedshitIDAOV()
            chrID=AOVLists[0]
            setID=AOVLists[1]
            if types=='chrID':
                IDs=chrID
            else:
                IDs=setID
            if IDs and line=='creat' and AOVAttr=='PuzzleMatte':
                for id in IDs:
                    AOVOld=mc.ls(type='RedshiftAOV')
                    cmd='redshiftCreateAov("Puzzle Matte")'
                    mel.eval(cmd)
                    mel.eval('redshiftUpdateActiveAovList()')
                    AOVNew=mc.ls(type='RedshiftAOV')
                    AOVName=''
                    for aov in AOVNew:
                        if aov not in AOVOld:
                            AOVName=aov
                    if AOVName!='':
                        idn=id+'Aov_PuzzleMatte'
                        mc.rename(AOVName,idn)
                        mc.setAttr((idn+'.name'),id,type="string")
                        #设置文件输出命名
                        #mc.setAttr((idn+'.filePrefix'),'<BeautyPath>/<BeautyFile>_<RenderPass>',type='string')
                        #设置objID模式
                        mc.setAttr((idn+'.mode'),1)
                        RGB=['R','G','B']
                        pAGB=['.redId','.greenId','.blueId']
                        for i in range(len(RGB)):
                            num=self.GA_RedshitIDInfo('objectID',id,RGB[i])
                            mc.setAttr((idn+pAGB[i]),num)
            if line=='delete' and AOVAttr=='PuzzleMatte':
                AOVS=mc.ls(type='RedshiftAOV')
                for Aov in AOVS:
                    if types in Aov:
                        mc.delete(Aov)
        print u'已设置PuzzleMatteAOV'
        return 0




    #----------------------------------------------------------#
    #----------------------------------------------------------------------------------------------------------#      #----------------------------------------------------------#
        #------------------------------#
    # 【渲染】【辅助】【Redshift删除所有渲染层和AOV通道】
    #  Author  : 韩虹
    #  Data    : 2017_08
    #------------------------------#
    def RedShiftALLDelete(self,nodetype='RedshiftAOV'):
        Info = mc.ls(type=nodetype)
        if nodetype=='renderLayer':
            Info.remove('defaultRenderLayer')
            mc.editRenderLayerGlobals(currentRenderLayer='defaultRenderLayer')
        if mc.ls(Info) :
            mc.delete(Info)
        return 0
    #----------------------------------------------------------#
    #----------------------------------------------------------------------------------------------------------#      #----------------------------------------------------------#
        #------------------------------#
    # 【渲染】【辅助】【创建渲染层】
    #  Author  : 韩虹
    #  Data    : 2017_08
    #------------------------------#
    #渲染层创建
    def GA_RedshiftRendererLayerCreat(self):
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        aovsetList=['AO','N','P','Z','SSS','DiffuseFilter','DiffuseLighting','Emission','GI','GIRaw','Matte','MotionVectors','chrID','setID','Reflections','Refractions','Shadows','SpecularLighting','VolumeLighting']
        for i in range(len(aovsetList)):
            check=mc.checkBox(('GAcheck'+aovsetList[i]),q=1,v=1)
            if  check==True and aovsetList[i] not in ['chrID','setID']:
                self.GA_RSAOVCreat(aovsetList[i],'creat')
            if check==True and aovsetList[i] in ['chrID','setID']:
                self.GA_RSAOVCreatSP('PuzzleMatte','creat',aovsetList[i])

      #创建渲染层
        mel.eval('source "//file-cluster/GDC/Resource/Support/Maya/projects/ShunLiu/CSL_RenderToolsMR.mel";CSL_RenderTools_Arnold();')
        print u'=========已创建渲染层========='
    #----------------------------------------------------------#
        #------------------------------#
    # 【渲染】【渲染帧数及渲染尺寸设置】
    #  Author  : 韩虹
    #  Data    : 2017_04_18
    #------------------------------#
    def GA_FileSet(self,shotType=2):
        import idmt.pipeline.db
        shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
        shot=''
        if shotType == 2:
            shot = shotInfos[0] + '_' + shotInfos[1] + '_' + shotInfos[2]
        if shotType == 3:
            shot = shotInfos[0] + '_' + shotInfos[1] + '_' + shotInfos[2] + '_' + shotInfos[3]

        anim = idmt.pipeline.db.GetAnimByFilename(shot)
        startFrame = anim.frmStart
        endFrame = anim.frmEnd
        fpsFrame = anim.fps
        resW = anim.resolutionW
        resH = anim.resolutionH
        # 分辨率
        mc.setAttr(('defaultResolution.width'), resW)
        mc.setAttr(('defaultResolution.height'), resH)
        # FPS
        if fpsFrame == 25:
            mc.currentUnit(time='pal')
        if fpsFrame == 24:
            mc.currentUnit(time='film')
        if fpsFrame == 30:
            mc.currentUnit(time='ntsc')
        # frame
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
        # 设置帧播放模式每帧
        mc.playbackOptions(playbackSpeed=0)

        # 允许undo
        mc.undoInfo(state=True, infinity=True)
        # 设置当前帧数
        mc.currentTime(startFrame)
        # 设置
        mel.eval('setMayaSoftwareFrameExt(3, 0)')
        # 设置渲染帧数
        mc.setAttr('defaultRenderGlobals.animation',1)
        mc.setAttr('defaultRenderGlobals.startFrame',startFrame)
        mc.setAttr('defaultRenderGlobals.endFrame',endFrame)
        return shot

    #----------------------------------------------------------------------------------------------------------#      #----------------------------------------------------------#
        #------------------------------#
    # 【渲染】【辅助】【通常渲染设置】
    #  Author  : 韩虹
    #  Data    : 2017_08
    #------------------------------#
    #渲染层创建
    def GA_rsRendererSettings(self,renderlayer='co',layertype='',shotType=2,cam=1):
        mc.loadPlugin('redshift4maya',qt=1)
        #import rsmaya.xgen
        #import sys
        #sys.path.append('C:/tools/LocalTools/3partPlugin/2016/Redshift/Plugins/Maya/Common/2013/rsmay')
        try:
            import rsmaya.xgen
            rsmaya.xgen.registerXgenCallbacks()
        except:
            pass
        #from rsmaya import xgen
        #rsmaya.xgen.registerXgenCallbacks()
        #加戴redshift插件
        renderglobal=mc.getAttr('defaultRenderGlobals.currentRenderer')
        '''
        if renderglobal!='redshift':
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'redshift', type='string')
        '''
        try:
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'mayaSoftware', type='string')
        except:
            pass
        try:
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'redshift', type='string')
        except:
            pass
        #设置当前渲染器为redshfit
        mc.setAttr('defaultRenderGlobals.animation',1)
        if cam==1:
            self.GA_FileSet(shotType)
        #设置渲染帧数及渲染尺寸
        if cam==1:
            self.GA_camSet(2)
        #渲染相机设置
        mc.setAttr('defaultRenderGlobals.imageFilePrefix','<RenderLayer>/<Scene>_<RenderLayer>',type="string")
        mel.eval('loadPreferredRenderGlobalsPreset("redshift")')
        mc.setAttr('redshiftOptions.imageFormat',1)
        mc.setAttr('redshiftOptions.exrBits',16)
        mc.setAttr('redshiftOptions.exrCompression',0)
        mc.setAttr('redshiftOptions.exrIsTiled',0)

        #设置为exr格式
        mc.setAttr('redshiftOptions.autocrop',0)
        mc.setAttr('redshiftOptions.exrForceMultilayer',1)
        #将aov设置为在一个exr
        #非color 文件，设置为png格式
        if renderlayer not in ['co']:
            mc.setAttr('redshiftOptions.autocrop',0)
            mc.setAttr('redshiftOptions.imageFormat',2)
            mc.setAttr('redshiftOptions.pngBits',16)
        setLists=['unifiedMinSamples','unifiedMaxSamples','unifiedAdaptiveErrorThreshold','unifiedFilterType','unifiedFilterSize','unifiedMaxOverbright','glossyRayMaxOverbright']
        numLists=[2,256,0.001,2,3,2,2]
        #设置渲染精度
        GILists=['primaryGIEngine','secondaryGIEngine','numGIBounces','conserveGIReflectionEnergy','bruteForceGINumRays','irradiancePointCloudMode']
        gnumLists=[3,2,1,1,16,3]
        if renderlayer=='co' and layertype=='chr':
            gnumLists=[3,0,1,1,16,3]
        elif renderlayer not in ['co']:
            gnumLists=[0,0,1,1,16,3]
        Lists=setLists+GILists
        nuLists=numLists+gnumLists
        for i in range(len(Lists)):
            Attr='redshiftOptions.'+Lists[i]
            if mc.objExists(Attr):
                try:
                    mc.setAttr(Attr,nuLists[i])
                except:
                    pass
        return 0
    #----------------------------------------------------------#
    #----------------------------------------------------------------------------------------------------------#      #----------------------------------------------------------#
        #------------------------------#
    # 【渲染】【渲染相机设置】
    #  Author  : 韩虹
    #  Data    : 2017_04_18
    #------------------------------#
    def GA_camSet(self,shotType=2):
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        shot=''
        if shotType==2:
            shot=shotInfo[1]+'_'+shotInfo[2]
        if shotType==3:
            shot=shotInfo[1]+'_'+shotInfo[2]+'_'+shotInfo[3]
        cam='CAM:cam_'+shot+'_baked'
        if mc.objExists(cam)!=True:
            mc.error(u'文件中缺少正确命名的相机【%s】' %cam)
        shap=mc.listRelatives(cam,s=1,f=1)
        ca=mc.ls(ca=1,l=1)
        if not ca:
            mc.warning(u'文件中没有相机，请检查')
        for camm in ca:
            if camm!=shap[0]:
                mc.setAttr(camm+'.renderable',0)
            else:
                mc.setAttr(camm+'.renderable',1)
        return cam
    #----------------------------------------------------------#

    #----------------------------------------------------------#
    #----------------------------------------------------------------------------------------------------------#      #----------------------------------------------------------#
        #------------------------------#
    # 【渲染】【添加ID属性】
    #  Author  : 韩虹
    #  Data    : 2017_08_29
    #------------------------------#
    def GA_RedshitIDSet(self,id='objectID',idinfo='chrID1',idtype='G'):
        rgbnum=self.GA_RedshitIDInfo(id,idinfo,idtype)
        meshList=[]
        objs=mc.ls(sl=1,l=1,tr=1)
        if not objs:
            mc.error(u'============please select============')
        if id=='objectID':
            for obj in objs:
                meshs=mc.listRelatives(obj,s=1,f=1,type='mesh')
                if meshs:
                    for mesh in meshs:
                        if mc.objExists(mesh+'.rsObjectId'):
                            meshList.append(mesh)
        if not meshList:
            mc.error(u'=========没有切换redshift渲染器，或所选物体中没有polygon物体========')
        for mesh in meshList:
            mc.setAttr((mesh+'.rsObjectId'),rgbnum)
        print (u'=========已添加【%s】【%s】属性=========' %(idinfo,idtype))
        return 0

    #----------------------------------------------------------#
    #----------------------------------------------------------------------------------------------------------#      #----------------------------------------------------------#
        #------------------------------#
    # 【渲染】【ID号】【辅助】
    #  Author  : 韩虹
    #  Data    : 2017_08_29
    #------------------------------#
    def GA_RedshitIDInfo(self,id='objectID',idinfo='setID01',idtype='G'):
        num=0
        rgbnum=0
        rgbList=['R','G','B']
        if 'chrID' not in idinfo and 'setID' not in idinfo:
            mc.error(u'没有该【%s】ID号，请检查' %idinfo)
        if idtype=='M':
            rgbnum=0
        if 'chrID' in idinfo:
            num=int(idinfo.split('chrID')[-1])
            rgbnum=1
        if 'setID' in idinfo:
            num=int(idinfo.split('setID')[-1])
            rgbnum=31
        for i in range(len(rgbList)):
            if rgbList[i]==idtype:
                rgbnum=rgbnum+(num-1)*len(rgbList)+i
        return rgbnum

    #----------------------------------------------------------#
    #----------------------------------------------------------------------------------------------------------#      #----------------------------------------------------------#
        #------------------------------#
    # 【渲染】【ID号】【辅助】
    #  Author  : 韩虹
    #  Data    : 2017_08_29
    #------------------------------#
    def GA_RedshitIDAOV(self):
        meshs=mc.ls(type='mesh',l=1)
        meshsModel=[]
        if not meshs:
            mc.error(u'文件中缺少polygon物体，请检查')
        for mesh in meshs:
            if 'MODEL|' in mesh and mc.objExists(mesh+'.rsObjectId') and mesh not in meshsModel:
                meshsModel.append(mesh)
        chrInfos=[]
        setInfos=[]
        if meshsModel:
            for mes in meshsModel:
                num=mc.getAttr(mes+'.rsObjectId')
                if 0<num<=30 :
                    print mes
                    i=int((num-1)/3+1)
                    if i<10:
                        id='chrID'+'0'+str(i)
                    else:
                        id='chrID'+str(i)
                    if id not in chrInfos:
                        chrInfos.append(id)
                if num>30:
                    i=int((num-30)/3)+1
                    if i<10:
                        id='setID'+'0'+str(i)
                    else:
                        id='setID'+str(i)
                    if id not in setInfos:
                        setInfos.append(id)
        result=[chrInfos,setInfos]
        return result
    #----------------------------------------------------------------------------------------------------------#      #----------------------------------------------------------#
        #------------------------------#
    # 【渲染】【创建渲染层】【可以根据项目需求添加参数】
    #  Author  : 韩虹
    #  Data    : 2017_09_19
    #------------------------------#
    #根据不同渲染层类型设置
    #sl 是指创建时，按选择还是MODLE组中
    #dele 是否删除AOV及渲染层
    #sm 是否smooth
    #save 是否另存

    def GA_RSRenderLayerCreat(self,renderLayer='co',layertype='chr',sl=1,dele=1,sm=1,save=1,shotType=2,cam=1,server=0):
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        #渲染设置
        try:
            self.GA_rsRendererSettings(renderLayer,layertype,shotType,cam)
        except:
            self.GA_rsRendererSettings(renderLayer,layertype,shotType,cam)
        objs=[]
        if sl==1:
            objs=mc.ls(sl=1,l=1,type='transform')
        elif sl==0 and layertype in ['chr','chrlights']:
            objList=self.GA_MeshInfo('transform')
            objs=objList[0]+objList[1]
        elif sl==0 and layertype in ['set','chrset']:
            objList=self.GA_MeshInfo('transform')
            objs=objList[0]+objList[1]+objList[2]
        else:
            meshs=mc.ls(type='mesh',l=1)
            meshList=[]
            if not meshs:
                mc.error(u'文件中没有polygon物体，请检查')
            for mesh in meshs:
                if 'MODEL' in mesh and mesh not in meshList:
                    meshList.append(mesh)
            if not meshList:
                mc.error(u'文件中没有有效MODEL组，或MODEL组下没有polygon物体，请检查')
            objs=self.GA_TRMeshInfo(meshList)
        #删除灯光雾

        ###if layertype!='set':
            ###mel.eval('redshiftRemoveGlobalShader true "atmosphere"')

        #删除渲染层及AOV
        if dele==1:
            self.RedShiftALLDelete("RedshiftAOV")
            self.RedShiftALLDelete("renderLayer")
        #smooth
        if sm==1:
            self.GA_RSmoothSet()
        if renderLayer!='co':
            mel.eval('source redshiftCreateOutputTab.mel')
            try:
                mel.eval('redshiftRemoveGlobalShader true "atmosphere"')
            except:
                pass
        #关闭灯光雾alpha替代
        self.GA_RSEnvironmentAlphaR(0)
        mc.editRenderLayerGlobals(currentRenderLayer='defaultRenderLayer')
        if renderLayer=='co':
            self.GA_AttrTransfer(objs,'rsObjectId')
        if renderLayer=='co' and layertype == 'set':
            self.GA_MeshSet('set')
            self.GA_FogReset()
        elif renderLayer=='co' and layertype == 'chr':
            self.GA_MeshSet('chr')
        elif renderLayer=='shadow':
            self.GA_RefIm()
            self.GA_MeshSet('shadow')
            print u'=====shadow属性已经设置 #Arnold 设置====='
            self.GA_RSShaderAssign(objs,'shadow',0)
            print u'=====已赋shadow材质球====='
        elif renderLayer=='light' and layertype == 'chr':
            self.GA_RefIm()
            self.GA_MeshSet('chalight')
            self.GA_RSShaderAssign(objs,'Lambert',0)
            print u'=====已赋lambert材质球====='

        elif renderLayer=='id31':
            self.GA_RefIm()
            self.GA_MeshSet('id31')
            meshInfo=self.GA_MeshInfoID('mesh')
            if meshInfo==[[],[],[]]:
                mc.error(u'=====文件中缺少可渲染物体，请检查=====')
            idcolor=['RSIdpR','RSIdpG','RSIdpB']
            for i in range(len(idcolor)):
                if meshInfo[i]:
                    mc.select(meshInfo[i])
                    self.GA_RSIDCreat(idcolor[i])
        elif renderLayer=='co' and layertype == 'ao':
            self.GA_RefIm()
            self.GA_MeshSet('ao')
            meshInfo=self.GA_MeshInfoID('mesh')
            if meshInfo==[[],[],[]]:
                mc.error(u'=====文件中缺少可渲染物体，请检查=====')
            self.GA_RSShaderAssign(objs,'AO',0)
            print u'=====已赋AO材质球====='
        #chr、set合在一起
        elif renderLayer=='co' and layertype == 'chrset':
            self.GA_MeshSet('chrset')
            #meshInfo=self.GA_MeshInfoID('mesh')
            #if meshInfo==[[],[],[]]:
            #    mc.error(u'=====文件中缺少可渲染物体，请检查=====')
            self.GA_FogReset()


        #创建AOV
        AOVs=[]
        if shotInfo[0] in ['ddz'] and layertype == 'chr' and renderLayer in ['co']:
            AOVs=['AO','DiffuseFilter','DiffuseLightingRaw','Emission','GIRaw','N','chrID','Reflections','Refractions','SpecularLighting','SSSRaw','P']
        if shotInfo[0] in ['ddz'] and layertype == 'set' and renderLayer in ['co']:
            AOVs=['AO','Z','DiffuseFilter','DiffuseLightingRaw','Emission','GIRaw','N','setID','Reflections','Refractions','SpecularLighting','P']
        if shotInfo[0] in ['ddz'] and renderLayer == 'shadow':
            AOVs=['AO']
        if shotInfo[0] in ['ddz'] and renderLayer in ['id31']:
            AOVs=['chrID','setID']
        if shotInfo[0] in ['ddz'] and layertype == 'ao' and renderLayer in ['co']:
            AOVs=['AO','N']
        if shotInfo[0] in ['ddz'] and layertype == 'chrset' and renderLayer in ['co']:
            AOVs=['AO','DiffuseFilter','DiffuseLightingRaw','Emission','GIRaw','N','chrID','Reflections','Refractions','SpecularLighting','SSSRaw','P']
        if AOVs:
            for aov in AOVs:
                if aov in ['chrID','setID']:
                    self.GA_RSAOVCreatSP("PuzzleMatte","creat",aov)
                else:
                    self.GA_RSAOVCreat(aov ,"creat")
        renderName=''
        if layertype=='chr' and renderLayer=='co':
            renderName='chr'
        elif layertype=='chr' and renderLayer=='light':
            renderName='chrlights'
        elif layertype=='set' and renderLayer=='co':
            renderName='set'
        elif layertype=='chrset' and renderLayer=='co':
            renderName='chrset'
        elif layertype=='ao' and renderLayer=='co':
            renderName='ao'
        else:
            renderName=renderLayer
        #创建渲染层
        objAll=objs
        #灯光加入渲染层
        if layertype=='chr' and renderLayer=='co':
            lightGrp=self.GA_RSlightInfoList('chr','group')
            objAll=objs+lightGrp
        elif layertype=='set' and renderLayer=='co':
            lightGrp=self.GA_RSlightInfoList('set','group')
            objAll=objs+lightGrp
        elif layertype=='chr' and renderLayer=='light':
            keylight=self.GA_RSlightInfoList('chr','key')
            fillight=self.GA_RSlightInfoList('chr','fill')
            rimlight=self.GA_RSlightInfoList('chr','rim')
            objAll=objs+keylight+fillight+fillight
            lights=[keylight,fillight,rimlight]
            lightcolor=[[1,0,0],[0,1,0],[0,0,1]]
            for i in range(len(lightcolor)):
                if lights[i]:
                    for lig in lights[i]:
                        if mc.nodeType(lig) in ['RedshiftPhysicalLight','RedshiftIESLight']:
                            mc.setAttr((lig+'.color'),lightcolor[i][0],lightcolor[i][1],lightcolor[i][2],type='double3')
                        elif mc.nodeType(lig) in ['RedshiftPortalLight']:
                            mc.setAttr((lig+'.tint_color'),lightcolor[i][0],lightcolor[i][1],lightcolor[i][2],type='double3')
                        else:
                            mc.setAttr((lig+'.color'),lightcolor[i][0],lightcolor[i][1],lightcolor[i][2],type='double3')
        elif layertype=='chrset' and renderLayer=='co':
            lightGrp=self.GA_RSlightInfoList('chrset','group')
            objAll=objs+lightGrp        
        mc.createRenderLayer(objAll,name=renderName, noRecurse=1, makeCurrent=1)
        #返回defaultRenderLayer
        mc.editRenderLayerGlobals(currentRenderLayer='defaultRenderLayer')
        mc.setAttr("defaultRenderLayer.renderable", 0)
        print u'========================【%s】渲染层已创建========================' %(renderName)
        if save==1:
            tempath=''
            if os.path.exists('E:'):
                tempath='E:/Info_Temp/render/'
            else:
                tempath='D:/Info_Temp/render/'
            shotName=''
            if shotType==2:
                tempath=tempath+shotInfo[0]+'/'+shotInfo[1]+'/'+shotInfo[2]+'/'
            if shotType==3:
                tempath=tempath+shotInfo[0]+'/'+shotInfo[1]+'/'+shotInfo[2]+'/'+shotInfo[3]+'/'
            mc.sysFile(tempath, makeDir=True)
            shotName=shotInfo[0]+'_'+shotInfo[1]+'_'+shotInfo[2]
            if shotType==3:
                shotName=shotInfo[0]+'_'+shotInfo[1]+'_'+shotInfo[2]+'_'+shotInfo[3]
            shotName=shotName+'_'+renderName+'_lr_c001'
            mc.file(rename=(tempath+shotName))
            fileTypeAll='mayaBinary'
            fileForm='.mb'
            if shotInfo[0] in ['ddz']:
                mc.file(rename=(tempath+shotName+fileForm))
                mc.file(save=1,type = fileTypeAll,f = 1)
            print u'========================【%s】========================' %(tempath+shotName+fileForm)
        if server==1:
            # 用户名
            userName = os.environ['USERNAME']
            newInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
            projectInfo = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(newInfo[0])
            fileInfo=''
            if shotType==3:
                fileInfo = '1|' + projectInfo + '|' + newInfo[0] + '_' + newInfo[1] + '_' + newInfo[2] + '_' + newInfo[3] + '_' + newInfo[4] + '|' + userName
            if shotType==2:
                fileInfo = '1|' + projectInfo + '|' + newInfo[0] + '_' + newInfo[1] + '_' + newInfo[2] + '_' + newInfo[3]  + '|' + userName
            checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
            #print checkOutCmd
            mel.eval(checkOutCmd)
            # checkIn
            description = '%s' %renderName
            mel.eval('idmtProject -checkin -description \" ' + description + '\"')
        result=tempath+shotName+fileForm
        return result

    #----------------------------------------------------------------------------------------------------------#      #----------------------------------------------------------#
        #------------------------------#
    # 【渲染】【开启关闭灯光雾alpha替代】
    #  Author  : 韩虹
    #  Data    : 2017_09_19
    #------------------------------#

    def GA_RSEnvironmentAlphaR(self,key=0):
        objs=mc.ls(type='RedshiftVolumeScattering',l=1)
        Envir=[]
        if objs:
            for obj in objs:
                if mc.objExists(obj+'.replaceAlphaOnEnvironment'):
                    mc.setAttr((obj+'.replaceAlphaOnEnvironment'),key)
                    Envir.append(obj)
        return Envir


    #----------------------------------------------------------------------------------------------------------#      #----------------------------------------------------------#
        #------------------------------#
    # 【渲染】【mesh tr 互】
    #  Author  : 韩虹
    #  Data    : 2017_09_19
    #------------------------------#
    def GA_TRMeshInfo(self,objs):
        meshList=[]
        for obj in objs:
            if mc.nodeType(obj)=='mesh' and mc.listRelatives(obj,p=1,f=1) and mc.listRelatives(obj,p=1,f=1)[0] not in meshList :
                meshs=mc.listRelatives(obj,p=1,type='transform',f=1)
                meshList.append(meshs[0])
            if mc.nodeType(obj)=='transform' and mc.listRelatives(obj,s=1,type='mesh'):
                meshs=mc.listRelatives(obj,s=1,type='mesh',f=1)
                for mesh in meshs:
                    if mesh not in meshList:
                        meshList.append(mesh)
        return meshList
    #----------------------------------------------------------------------------------------------------------#      #----------------------------------------------------------#
        #------------------------------#
    # 【渲染】【传递shape属性】
    #  Author  : 韩虹
    #  Data    : 2017_09_19
    #------------------------------#
    def GA_AttrTransfer(self,objs,att='rsObjectId'):
        objList=[]
        if not objs:
            mc.error(u'物体为空，请检查')
        if mc.nodeType(objs[0])=='mesh':
            objList=self.GA_TRMeshInfo(objs)
        else:
            objList=objs
        if not objList:
            mc.error(u'物体为空，请检查')
        for obj in objList:
            meshs=mc.listRelatives(obj,s=1,type='mesh',f=1)
            if meshs and 'Deformed' not in meshs[0] and mc.objExists(meshs[0]+'.'+att):
                num=mc.getAttr(meshs[0]+'.'+att)
                for mesh in meshs:
                    mc.setAttr((mesh+'.'+att),num)
        return 0
    #------------------------------#
    # 【通用】【smooth级别设置】
    #  Author  : 韩虹
    #  Data    : 2017_09_20
    #------------------------------#

    def GA_RSmoothSet(self):
        Sets=mc.ls(set=1)
        for set in Sets:
            if 'smooth_1' in set or 'smooth_2' in set and mc.sets(set,q=1):
                objs=mc.sets(set,q=1)
                if objs:
                    meshs=self.GA_TRMeshInfo(objs)
                    if meshs:
                        for mesh in meshs:
                            mc.setAttr(mesh+'.rsEnableSubdivision',1)
            if 'smooth_0' in set in set and mc.sets(set,q=1):
                objs=mc.sets(set,q=1)
                meshs=self.GA_TRMeshInfo(objs)
                if meshs:
                    for mesh in meshs:
                        mc.setAttr(mesh+'.rsEnableSubdivision',0)
        return 0
    #------------------------------#
    # 【通用】【RS赋材质】
    #  Author  : 韩虹
    #  Data    : 2017_09_21
    #------------------------------#

    def GA_RSShaderAssign(self,objs,shaderType='AO',transparency=0):
        if transparency==0:
            Shade='SHD_'+shaderType+'_rs'
            SG=Shade+'SG'
            #删除已有材质球和SG节点
            if mc.objExists(Shade):
                mc.delete(Shade)
            if mc.objExists(SG):
                mc.delete(SG)
            ##创建新材质球和SG节点
            if shaderType=='AO':
                mc.shadingNode('RedshiftArchitectural', asShader=True,n=Shade)
            elif shaderType=='shadow':
                mc.shadingNode('RedshiftMatteShadowCatcher', asShader=True,n=Shade)
            else:
                mc.shadingNode('RedshiftArchitectural', asShader=True,n=Shade)
            mc.sets(renderable=1,noSurfaceShader=1,em=1,n=SG)
            mc.connectAttr(('%s.outColor' % Shade),('%s.surfaceShader' % SG))
            if objs:
                for obj in objs:
                    try:
                        mc.sets(obj,e=1, forceElement = SG)
                    except:
                        shapes=self.GA_TRMeshInfo([obj])
                        for shape in shapes:
                            cons=mc.listConnections(shape,type='shadingEngine')
                            if cons:
                                mc.delete(cons)
                        mc.sets(obj,e=1, forceElement = SG)
    #AO材质
            if shaderType=='AO':
                mc.setAttr ((Shade+'.ao_on'),1)
                mc.setAttr ((Shade+'.ao_samples'),1024)
                mc.setAttr ((Shade+'.ao_distance'),0.5)
                mc.setAttr ((Shade+'.ao_spread'),0.7)
                mc.setAttr ((Shade+'.ao_falloff'),0.3)                
                mc.setAttr((Shade + '.ao_dark'),0.5,0.5,0.5,type = 'double3')
                
    #Shadow材质
            if shaderType=='shadow':
                mc.setAttr((Shade + '.shadows'),1,1,1,type = 'double3')
            if shaderType=='Lambert':
                mc.setAttr((Shade + '.diffuse'),1,1,1,type = 'double3')
                mc.setAttr((Shade + '.reflectivity'),0)
        return Shade
    #------------------------------#
    # 【通用】【RSID材质】
    #  Author  : 韩虹
    #  Data    : 2017_09_21
    #------------------------------#

    def GA_RSIDCreat(self,idpShader):
        objs=mc.ls(sl=1,l=1)
        if not objs:
            mc.error(u'未选择，请选择物体')
        if mc.objExists(idpShader)==0:
            mc.shadingNode('RedshiftMatteShadowCatcher', asShader=True,n=idpShader)
        idpSG=idpShader+'SG'
        if mc.objExists(idpSG)==0:
            mc.sets(renderable=1,noSurfaceShader=1,em=1,n=idpSG)
        cons=mc.listConnections('%s.outColor' % idpShader)
        if cons!=None:
            #print 'sss'
            if(cons[0]!=idpSG):
                mc.disconnectAttr(('%s.outColor' % idpShader), ('%s.surfaceShader' % cons[0]))
                mc.connectAttr(('%s.outColor' % idpShader),('%s.surfaceShader' % idpSG))
        else:
            mc.connectAttr(('%s.outColor' % idpShader),('%s.surfaceShader' % idpSG))

        mc.setAttr((idpShader+".catch_shadows"),0 )
        mc.setAttr((idpShader+".backgroundIsEnv"),1 )
        mc.setAttr((idpShader+".background_alpha"),0 )
        if(idpShader=='RSIdpR'):
            mc.setAttr((idpShader+'.emissive_color'),1,0,0)
            mc.setAttr((idpShader+'.diffuse'),1,0,0)
        elif(idpShader=='RSIdpG'):
            mc.setAttr((idpShader+'.emissive_color'),0,1,0)
            mc.setAttr((idpShader+'.diffuse'),0,1,0)
        elif(idpShader=='RSIdpB'):
            mc.setAttr((idpShader+'.emissive_color'),0,0,1)
            mc.setAttr((idpShader+'.diffuse'),0,0,1)
            #mc.setAttr((idpShader+'.hardwareColor'),0,0,1)
        elif(idpShader=='RSIdpM'):
            mc.setAttr((idpShader+'.emissive_color'),0,0,0)
            mc.setAttr((idpShader+'.diffuse'),0,0,0)
        elif(idpShader=='RSIdpA'):
            mc.setAttr((idpShader+'.emissive_color'),0,0,0)
            mc.setAttr((idpShader+'.diffuse'),1,1,1)
            mc.setAttr((idpShader+".background_alpha"),1 )
        else:
            print u'请正确输入IDP类型'
        if objs:
            for obj in objs:
                try:
                    mc.sets(obj,e=1, forceElement=idpSG)
                except:
                    print u'===有物体无法赋予材质==='
                    print obj
                    mc.warning(u'===有物体无法赋予材质===')
        return idpShader
    #------------------------------#
    # 【辅】【判断角色，场景，道具polygon物体】
    #  Author  : 韩虹
    #  Data    : 2017_07
        #------------------------------#
    def GA_MeshInfo(self,ty='mesh'):
        if ty=='mesh':
            meshs=mc.ls(type='mesh',l=1)
        else:
            meshs=mc.ls(tr=1,l=1)
        if not meshs:
            mc.error(u'文件中没有polygon物体，请检查')
        meshchr=[]
        meshpro=[]
        meshset=[]
        for mesh in meshs:
            if ty =='mesh' and 'SET_GRP' in mesh and mesh not in meshset and 'MODEL' in mesh:
                meshset.append(mesh)
            elif ty =='mesh' and 'CHR_GRP' in mesh and mesh not in meshchr and 'MODEL' in mesh:
                meshchr.append(mesh)
            elif ty =='mesh' and 'PRP_GRP' in mesh and mesh not in meshpro and 'MODEL' in mesh and 'p000007sky' not in mesh and 'p028001cloud' not in mesh:
                meshpro.append(mesh)
            elif ty=='mesh' and 'PRP_GRP' in mesh and mesh not in meshset and 'MODEL' in mesh and 'p000007sky' in mesh or 'p028001cloud' in mesh:
                meshset.append(mesh)
            elif ty!='mesh' and 'SET_GRP' in mesh and mesh not in meshset and 'MODEL' in mesh and mc.listRelatives(mesh,s=1,type='mesh'):
                meshset.append(mesh)
            elif ty!='mesh' and 'CHR_GRP' in mesh and mesh not in meshchr and 'MODEL' in mesh and mc.listRelatives(mesh,s=1,type='mesh'):
                meshchr.append(mesh)
            elif ty!='mesh' and 'PRP_GRP' in mesh and mesh not in meshpro and 'MODEL' in mesh and mc.listRelatives(mesh,s=1,type='mesh') and 'p000007sky' not in mesh and 'p028001cloud' not in mesh:
                meshpro.append(mesh)
            elif ty!='mesh' and 'PRP_GRP' in mesh and mesh not in meshset and 'MODEL' in mesh and 'p000007sky' in mesh or 'p028001cloud' in mesh:
                meshset.append(mesh)
        result=[meshchr,meshpro,meshset]
        return result

    #------------------------------#
    # 【辅】【判断角色，场景，道具polygon物体】
    #  Author  : 韩虹
    #  Data    : 2017_07
        #------------------------------#
    def GA_MeshInfoID(self,ty='mesh'):
        if ty=='mesh':
            meshs=mc.ls(type='mesh',l=1)
        else:
            meshs=mc.ls(tr=1,l=1)
        if not meshs:
            mc.error(u'文件中没有polygon物体，请检查')
        meshchr=[]
        meshpro=[]
        meshset=[]
        for mesh in meshs:
            if ty =='mesh' and 'SET_GRP' in mesh and mesh not in meshset and 'MODEL' in mesh:
                meshset.append(mesh)
            elif ty =='mesh' and 'CHR_GRP' in mesh and mesh not in meshchr and 'MODEL' in mesh:
                meshchr.append(mesh)
            elif ty =='mesh' and 'PRP_GRP' in mesh and mesh not in meshpro and 'MODEL' in mesh:
                meshpro.append(mesh)
            elif ty!='mesh' and 'SET_GRP' in mesh and mesh not in meshset and 'MODEL' in mesh and mc.listRelatives(mesh,s=1,type='mesh'):
                meshset.append(mesh)
            elif ty!='mesh' and 'CHR_GRP' in mesh and mesh not in meshchr and 'MODEL' in mesh and mc.listRelatives(mesh,s=1,type='mesh'):
                meshchr.append(mesh)
            elif ty!='mesh' and 'PRP_GRP' in mesh and mesh not in meshset and 'MODEL' in mesh and mc.listRelatives(mesh,s=1,type='mesh'):
                meshset.append(mesh)
        result=[meshchr,meshpro,meshset]
        return result
    #------------------------------#
    # 【辅】【设置参数】【用于shadow】
    #  Author  : 韩虹
    #  Data    : 2017_09
        #------------------------------#
    def GA_MeshSet(self,renderLayer='shadow'):
        meshInfo=self.GA_MeshInfo('mesh')
        if not meshInfo:
            mc.error(u'文件中没有可渲染模型，请检查')
        chr=meshInfo[0]+meshInfo[1]
        set=meshInfo[2]
        if chr:
            for ch in chr:
                if renderLayer in ['set','shadow']:
                    mc.setAttr((ch+'.primaryVisibility'),0)
                if renderLayer in ['id31','chalight','chr','ao','chrset']:
                    mc.setAttr((ch+'.primaryVisibility'),1)
        if set:
            for se in set :
                if renderLayer in ['shadow']:
                    mc.setAttr((se+'.castsShadows'),0)
                    mc.setAttr((se+'.receiveShadows'),1)
                if renderLayer in ['chr']:
                    mc.setAttr((se+'.primaryVisibility'),0)
                if renderLayer in ['id31','set','ao','chrset']:
                    mc.setAttr((se+'.primaryVisibility'),1)
        return 0
 #导入参考
    def GA_RefIm(self):
        while mc.file(q=1,r=1):
          refPath=mc.file(q=1,r=1)
          if len(refPath)!=0:
              for r in refPath:
                  refRN=mc.file(r,q=1,rfn=1)
                  if(mc.file(r,q=1,dr=1)):
                      mc.file(refRN,loadReference=1)
                  mc.file(r,ir=1)
    #------------------------------#
    # 【辅】【RS材质勾选AO属性】
    #  Author  : 韩虹
    #  Data    : 2017_09
    #------------------------------#
    def GA_RSAOSet(self,set=1):
        mats=mc.ls(mat=1)
        matList=[]
        if mats:
            for mat in mats:
                if mc.objExists(mat+'.ao_on') and mat not in matList:
                    matList.append(mat)
        if matList:
            for mat in matList:
                mc.setAttr((mat+'.ao_on'),set)
                if set == 1:
                    mc.setAttr ((mat+'.ao_samples'),1024)
                    mc.setAttr ((mat+'.ao_distance'),0.5)
                    mc.setAttr ((mat+'.ao_spread'),0.7)
                    mc.setAttr ((mat+'.ao_falloff'),0.3)
                    mc.setAttr((mat+'.ao_dark'),0.5,0.5,0.5,type='double3')

        return 0
    #------------------------------#
    # 【辅】【灯光信息】
    #  Author  : 韩虹
    #  Data    : 2017_09
    #------------------------------#
    def GA_RSlightInfoList(self,Type='chr',lightType='group'):
        lights=mc.ls(lt=1,l=1)
        RSlighttypeList=['RedshiftPhysicalLight','RedshiftIESLight','RedshiftPortalLight','RedshiftDomeLight']
        RsLights=[]
        for rstype in RSlighttypeList:
            rslight=mc.ls(type=rstype,l=1)
            if rslight:
                for light in rslight:
                    if light not in RsLights:
                        RsLights.append(light)
        lights += RsLights
        lightInfoList=[]
        if lights:
            for light in lights:
                lightP=light.split('|')
                for lig in lightP:
                    if Type=='chr' and lightType=='group' and 'chr_light' in lig.lower() and lig not in lightInfoList:
                        lightInfoList.append(lig)
                    if Type=='set' and lightType=='group' and 'set_light' in lig.lower() and lig not in lightInfoList:
                        lightInfoList.append(lig)
                    if Type=='chrset' and lightType=='group' and 'set_light' in lig.lower() and lig not in lightInfoList:
                        lightInfoList.append(lig)
                if Type=='chr' and lightType=='key' and 'chr_light' in light.lower() and 'keylight' in light.lower() and light[0] not in lightInfoList:
                    ligt=mc.listRelatives(light,p=1,f=1)
                    lightInfoList.append(ligt[0])
                if Type=='chr' and lightType=='fill' and 'chr_light' in light.lower() and  'fillight' in light.lower() and light[0] not in lightInfoList:
                    ligt=mc.listRelatives(light,p=1,f=1)
                    lightInfoList.append(ligt[0])
                if Type=='chr' and lightType=='rim' and 'chr_light' in light.lower() and  'rimlight' in light.lower() and light[0] not in lightInfoList:
                    ligt=mc.listRelatives(light,p=1,f=1)
                    lightInfoList.append(ligt[0])
                if Type=='set' and lightType=='key' and 'set_light' in light.lower() and 'keylight' in light.lower() and light[0] not in lightInfoList:
                    ligt=mc.listRelatives(light,p=1,f=1)
                    lightInfoList.append(ligt[0])
                if Type=='set' and lightType=='fill' and 'set_light' in light.lower() and  'fillight' in light.lower() and light[0] not in lightInfoList:
                    ligt=mc.listRelatives(light,p=1,f=1)
                    lightInfoList.append(ligt[0])
                if Type=='set' and lightType=='rim' and 'set_light' in light.lower() and  'rimlight' in light.lower() and light[0] not in lightInfoList:
                    ligt=mc.listRelatives(light,p=1,f=1)
                if Type=='set' and lightType=='all' and 'set_light' in light.lower() and ligt[0] not in lightInfoList:
                    ligt=mc.listRelatives(light,p=1,f=1)
                    lightInfoList.append(ligt[0])
                if Type=='chrset' and lightType=='key' and 'set_light' in light.lower() and 'keylight' in light.lower() and light[0] not in lightInfoList:
                    ligt=mc.listRelatives(light,p=1,f=1)
                    lightInfoList.append(ligt[0])
                if Type=='chrset' and lightType=='fill' and 'set_light' in light.lower() and  'fillight' in light.lower() and light[0] not in lightInfoList:
                    ligt=mc.listRelatives(light,p=1,f=1)
                    lightInfoList.append(ligt[0])
                if Type=='chrset' and lightType=='rim' and 'set_light' in light.lower() and  'rimlight' in light.lower() and light[0] not in lightInfoList:
                    ligt=mc.listRelatives(light,p=1,f=1)
                if Type=='chrset' and lightType=='all' and 'set_light' in light.lower() and ligt[0] not in lightInfoList:
                    ligt=mc.listRelatives(light,p=1,f=1)
                    lightInfoList.append(ligt[0])
        return  lightInfoList
#'s006001street' 场景恢复灯光雾链接
    #------------------------------#
    # 【辅】【场景恢复灯光雾链接】
    #  Author  : 韩虹
    #  Data    : 2017_10
    #------------------------------#
    def GA_FogReset(self):
        fogId=['s006001street']
        namespaces=mc.namespaceInfo(listOnlyNamespaces=1)
        fogIDList=[]
        for ns in namespaces:
            for fd in fogId:
                if fd in ns:
                    fogIDList.append(ns)
        if fogIDList:
            for ns in fogIDList:
                if mc.ls(ns+':rsVolumeScattering*') and mc.nodeType(mc.ls(ns+':rsVolumeScattering*')[0])=='RedshiftVolumeScattering' :
                    fog=mc.ls(ns+':rsVolumeScattering*')[0]
                    cmd='redshiftChangeGlobalShader ' +fog+' "atmosphere"'
                    try:
                        mel.eval(cmd)
                    except:
                        pass
        return fogIDList

