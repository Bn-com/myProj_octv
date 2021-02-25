# -*- coding: utf-8 -*-
# 【通用】【NJ2017项目优化工具】
#  Author : 韩虹
#  Data   : 2016
import maya.cmds as mc
import maya.mel as mel
import pymel.core as pm
from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
reload(sk_infoConfig)
from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
reload(sk_referenceConfig)
from idmt.maya.commonCore.core_finalLayout import sk_cacheFinalLayout
reload(sk_cacheFinalLayout)
from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools
reload(sk_sceneTools)

#from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools
#reload(sk_sceneTools)
import re
class nj17_CheckTools(object):
    def __init__(self):
        pass
        #----------------------------------------------------------#
    #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【项目】【NJ2017渲染前优化工具】
    #  Author  : 韩虹
    #  Data    : 2016_5
    #------------------------------#
    def nj_FixBeforeRender(self):
        #01 删除海节点
        from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools
        reload(sk_sceneTools)
        print u'==============!!!Start 【删除无用节点】!!!=============='
        sk_sceneTools.sk_sceneTools().checkDonotNodeCleanBase()
        #强制重启IK解算
        mc.ikSystem(e = 1,sol = 1)
        mc.renderThumbnailUpdate(False)
        sk_cacheFinalLayout.sk_cacheFinalLayout().sk_checkBakeConstraints()

        #02 删除无用节点
        unknows=mc.ls(type='unknown',l=1)
        if unknows:
            for un in unknows:
                mc.lockNode(un,l=0)
                mc.delete(un)
        print u'==============!!!End 【删除无用节点】!!!=============='
        #02 1 删除相机
        cas=mc.ls(ca=1,l=1)
        if cas:
            for ca in cas:
                if 'cam_' in ca:
                    cam=mc.listRelatives(ca,p=1,type='transform',f=1)
                    if cam:
                        try:
                            mc.delete(cam[0])
                        except:
                            pass
        #03 删除代理参考节点
        mel.eval('source "zwRemoveAllProxy.mel"')
        mel.eval('zwRemoveAllProxy()')
        #03 1 删除me特效参考
        print u'==============!!!Start 【删除me特效参考】!!!=============='
        mepath='Z:/Projects/Ninjago/Project/data/AssetInfos/meInfo.txt'
        meInfo=self.checkFileRead(mepath)

        refInfo = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refNodes = refInfo[0][0]
        refPaths = refInfo[1][0]
        refNamespace = refInfo[2][0]
        if refNodes:
            for i in range(len(refNodes)):
                if '_' in refNodes[i] and len(refNodes[i].split('_'))>1 and refNodes[i].split('_')[1][0]=='m' and refNamespace[i].split('_')[-1] not in meInfo:
                    try:
                        mc.file(refPaths[i],rr=1)
                    except:
                        pass
        print u'==============!!!End 【删除me特效参考】!!!=============='
        #04 导入渲染用摄像机
        print u'==============!!!Start 【导入渲染用摄像机】!!!=============='
        mel.eval('source zwCameraImportExport.mel')
        mel.eval('zwReferenceCameraProc()')
        #05 设置相机渲染属性
        shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
        shotName=shotInfos[1]+'_'+shotInfos[2]+'_'+shotInfos[3]
        camName='cam_'+shotName
        cas=mc.ls(ca=1,l=1)
        for cam in cas:
            mc.setAttr((cam+'.depthOfField'),0)
            if camName not in cam:
                mc.setAttr((cam+'.renderable'),0)
            else:
                mc.setAttr((cam+'.renderable'),1)
        print u'==============!!!End 【导入渲染用摄像机】!!!=============='
        #06 关闭面片的眼睛和眉毛（需要前期将此添加标
        print u'==============!!!Start 【隐藏 rig】!!!=============='
        sk_sceneTools.sk_sceneTools().sk_sceneReorganize(2)
        #self.nj_Hide()
        #07 删除QSK_panel.ma
        rfns=mc.file(q=1,r=1)
        if rfns:
            for ref in rfns:
                if '_panel.ma' in ref:
                    mc.file(ref,removeReference=1)
        print u'==============!!!End 【隐藏 rig】!!!=============='
        #08 替换参考（这个根据需要再加）
        #09 删除FX的组
        #10 load Vray渲染器
        print (u'===============!!!Start 【%s】!!!===============' % (u'Vray设置'))
        print 'Working...'
        mc.setAttr('defaultRenderGlobals.imageFormat', 7)
        try:
           mel.eval('loadPlugin "vrayformaya"')
        except:
            pass
        mc.setAttr('defaultRenderGlobals.currentRenderer', 'vray', type='string')
        mel.eval('source "vrayRegisterRenderer"')
        mel.eval('vrayCreateVRaySettingsNode()')
        # Vray基本设置
        self.nj_VraySettings()
        print (u'===============!!!End 【%s】!!!===============' % (u'Vray设置'))
        #关闭colorManage
        print u'==============!!!Start 【关闭colorManage】!!!=============='
        mc.colorManagementPrefs(e=1, popupOnError=1, cmEnabled= 0)
        #sk_sceneTools.sk_sceneTools().sk_sceneReorganize(0)
        print u'==============!!!End 【关闭colorManage】!!!=============='
        print u'==============!!!End 【文件优化】!!!=============='

    #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【通用】【NJ2017渲染前优化工具】
    #  Author  : 韩虹
    #  Data    : 2016_5
    #------------------------------#
    def nj_Hide(self):
        objs=mc.ls(tr=1,sn=1)
        Infos=[':RIG',':DEFORMERS']
        HideGrps=[]
        for obj in objs:
            for info in Infos:
                if info in obj and mc.listRelatives(obj,s=1)==None and obj not in HideGrps:
                    HideGrps.append(obj)
        if HideGrps:
            for tr in HideGrps:
                try:
                    mc.setAttr((tr+'.visibility'),0)
                except:
                    mc.warning(u'【%s】visibility属性被锁，请检查文件'%tr)
                    mc.error(u'【%s】visibility属性被锁，请检查文件'%tr)
        return 0
    #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【通用】【Vray 基本设置】
    #  Author  : 韩虹
    #  Data    : 2016_5
    #------------------------------#
    def nj_VraySettings(self):
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
        try:
            mc.setAttr('vraySettings.imageFormatStr','tif',type='string')
            mc.setAttr('vraySettings.imageFormatStr','png',type='string')
            mc.setAttr ('vraySettings.imgOpt_png_bitsPerChannel', 16)
        except:
            pass
        #nj2017渲染基本设置
        mc.setAttr('vraySettings.fileNamePrefix','<Layer>/<Scene>_<Layer>',type='string')
        #设置素材命名方式
        mc.setAttr('vraySettings.imageFormatStr','tif',type='string')
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
        mc.setAttr("vraySettings.globopt_light_doLights",1)
        mc.setAttr("vraySettings.globopt_cache_bitmaps",0)
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
        mc.setAttr ('vraySettings.ddisplac_edgeLength',10)
        mc.setAttr ('vraySettings.ddisplac_viewDependent',1)
        mc.setAttr ('vraySettings.ddisplac_maxSubdivs',2)
        mc.setAttr ('vraySettings.ddisplac_tightBounds',1)
        mc.setAttr ('vraySettings.ddisplac_amount',1)
        #素材命名
        mc.setAttr('vraySettings.fileNamePrefix' ,'<Layer>/<Scene>_<Layer>',type='string')
        mc.setAttr('vraySettings.relements_separateFolders',1)
        mc.setAttr('vraySettings.fileNameRenderElementSeparator' ,'_',type='string')
        #内存
        mc.setAttr('vraySettings.sys_rayc_dynMemLimit' ,18000)
        return 0
    def checkFileRead(self,path):
        import os
        if not os.path.exists(path):
            print path
            print u'Error:    file do not exist'
            mc.error(u'Error:    file do not exist')
        txt = open(path, 'r');
        try:
            fileContent = txt.readlines()
            print('Loading........')
        finally:
            #print path
            txt.close()
        result = []
        for info in fileContent:
            if '\r\n' in info:
                result.append(info.split('\r\n')[0])
            else:
                result.append(info)
        return result
    #批量替换 ce60630014001Karlof 参考为 ce7072020001Karlof
    def refReplaceChr(self):
        refInfo = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refNodes = refInfo[0][0]
        refPaths = refInfo[1][0]
        refNamespace = refInfo[2][0]
        fileName=mc.file(q=1,sn=1,shn=1)
        tempath='D:/TempInfo/replace/'
        mc.sysFile(tempath, makeDir=True)
        ceRefs=[]
        for i in range(len(refNodes)) :
            if 'ce60630014001Karlof' in refNodes[i]  and refPaths[i]=='//file-cluster/GDC/Projects/Ninjago/Project/Scenes/characters/E6063/ce60630014001Karlof/master/nj_ce60630014001Karlof_h_ms_anim.mb':
                   ceRefs.append(refNodes[i])
        if ceRefs:
            for refRN in ceRefs:
               mc.file('//file-cluster/GDC/Projects/Ninjago/Project/scenes/characters/E7072/ce7072020001Karlof/master/nj_ce7072020001Karlof_h_ms_anim.mb', loadReference=refRN)
               mc.select(refNodes[i])
               mel.eval('source zwNamespace.mel')
               mel.eval('zwFixNamespace()')
            mc.file(rename=tempath+fileName)
            mc.file(save=1,type ='mayaBinary',f = 1)
            print u'===========已替换【ce60630014001Karlof】参考=========='
            print u'===========[%s]===========' %(tempath+fileName)
        else:
            print u'===========文件中没有【ce60630014001Karlof】参考========================'
            mc.warning(u'===========文件中没有【ce60630014001Karlof】参考========================')
        return 0
    #批量修正 'se7066010001SnakeEggSwampEXT' 参考
    def refFix(self,rn='se7066010001SnakeEggSwampEXT'):
        fileName=mc.file(q=1,sn=1,shn=1)
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refNamespace=refInfos[2][0]
        refRN=refInfos[0][0]
        refPaths = refInfos[1][0]
        tempath='D:/TempInfo/refFix/'
        mc.sysFile(tempath, makeDir=True)
        refRS=[]
        refSN=[]
        refFile=[]
        fix=0
        refPathN=''
        GRPS=[]
        if rn=='se7066010001SnakeEggSwampEXT':
            refPathN='//file-cluster/GDC/Projects/Ninjago/Project/scenes/sets/E7066/se7066010001SnakeEggSwampEXT/master/nj_se7066010001SnakeEggSwampEXT_h_ms_tex.mb'
        for i in range(len(refRN)):
            if rn in refRN[i]:
                refSN.append(refRN[i])
                refFile.append(refNamespace[i])
                fix=1
            grp = ''
            if '_' in refNamespace[i] and refNamespace[i].split('_')>1 and  refNamespace[i].split('_')[1][0]=='c':
                grp='CHR'
            if '_' in refNamespace[i] and refNamespace[i].split('_')>1 and  refNamespace[i].split('_')[1][0]=='p':
                grp='Pro'
            if '_' in refNamespace[i] and refNamespace[i].split('_')>1 and  refNamespace[i].split('_')[1][0]=='s':
                grp='SET'
            if grp != '' and rn not in refRN[i] :
                GRPS.append(refNamespace[i]+':'+grp)
                refRS.append(refRN[i])
        if fix == 0:
            pass
        if fix == 1 and refRS:
            for refR in refRS:
                mc.file(loadReference=refR)
        if fix == 1 and GRPS:
            sk_sceneTools.sk_sceneTools().sk_sceneCameraUpdate(1,shotType = 3)
            mc.select(GRPS)
            mc.file((tempath+fileName),options='v=0',f=1,type='mayaBinary',preserveReferences=1,es=1)
            mc.file((tempath+fileName),options='v=0',type='mayaBinary',f=1,o=1)
            #创建新的'se7066010001SnakeEggSwampEXT'参考
            for j in range(len(refSN)):
                mc.file(refPathN, reference=True, namespace=refSN[j])
            #导入相机
            sk_sceneTools.sk_sceneTools().sk_sceneImportCameraF(3)
            # 处理组
            sk_sceneTools.sk_sceneTools().sk_sceneReorganize(2)
            #相机打组
            shotInfo=sk_infoConfig.sk_infoConfig().checkShotInfo()
            cam= 'cam_' + str(shotInfo[1]) + '_' + str(shotInfo[2])  + '_' + str(shotInfo[3])
            if mc.ls(cam):
                camGRP='|CAM_GRP'
                mc.parent(cam,camGRP)
            #另存
            mc.file(rename=tempath+fileName)
            mc.file(save=1,type ='mayaBinary',f = 1)
            print u'===========已修正【se7066010001SnakeEggSwampEXT】参考=========='
            print u'===========[%s]===========' %(tempath+fileName)
        else:
            print u'===========文件中没有【se7066010001SnakeEggSwampEXT】参考========================'
            mc.warning(u'===========文件中没有【se7066010001SnakeEggSwampEXT】参考========================')
        return 0

# 修复snakeEggSwamp场景材质：
    def snakeEggSwamprefFix(self):
        refInfo = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refNodes = refInfo[0][0]
        refPaths = refInfo[1][0]
        refNamespace = refInfo[2][0]
        refFixRN=[]
        refFixPath=[]
        for i in range(len(refNamespace)):
            if 'se7066010001SnakeEggSwampEXT' in refPaths[i] or 'pe7072004001CrudelyDrawnMap' in refPaths[i]:
                refFixRN.append(refNodes[i])
                refFixPath.append(refPaths[i])
        if not refFixRN:
            print u'文件中没有【se7066010001SnakeEggSwampEXT】场景'
            pass
        else:
            for j in range(len(refFixRN)):
                mc.file(refFixPath[j],unloadReference=True)
                mc.select(refFixRN[j])
                sk_referenceConfig.sk_referenceConfig().checkReferenceShaderReset(1)
                mc.file(loadReference=refFixRN[j])
                print u'【%s】场景已修复'%refFixRN[j]

        return 0
