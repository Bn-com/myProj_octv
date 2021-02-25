__author__ = 'hanhong'

# -*- coding: utf-8 -*-

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

from idmt.maya.py_common import GA_RenderArnoldLayer
reload(GA_RenderArnoldLayer)



import re
class GA_DO6RenderCmd(object):
    def __init__(self):
        pass
    #----------------------------------------------------------------------------------------------------------#      #----------------------------------------------------------#
    #------------------------------#
    # ����Ⱦ����Arnold��Ⱦ���ߡ�
    #  Author  : ����
    #  Data    : 2017_07_06
    #------------------------------#
    def DO6RenderLayerCreat(self,renderLayer='co',layertype='chr',dele=1,sm=1):
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        objs=mc.ls(sl=1,l=1,tr=1)

        if not objs:
            mc.warning(u'��ѡ��')
            mc.error(u'======��ѡ��=====')
        #ɾ����Ⱦ�㼰AOV
        if dele==1:
            GA_RenderArnoldLayer.GA_RenderArnold().ArnoldALLDelete(nodetype="aiAOV")
            GA_RenderArnoldLayer.GA_RenderArnold().ArnoldALLDelete(nodetype="renderLayer")
        #smooth
        if sm==1:
            GA_RenderArnoldLayer.GA_RenderArnold().csl_SmoothSet()
        mc.editRenderLayerGlobals(currentRenderLayer='defaultRenderLayer')
        #��Ⱦ����
        self.GA_ArnoldRendererSettings(renderLayer)
        #������
        if renderLayer not in ['co']:
            GA_RenderArnoldLayer.GA_RenderArnold().GA_ArnoldShaderAssign('Lambert',0)
        #����AOV
        AOV=[]
        if shotInfo[0] in ['do6'] and layertype=='chr':
            AOV=['AO','Fre','N','P','Shadow','Z','Zdp','direct_diffuse','indirect_specular',]
            GA_RenderArnoldLayer.GA_RenderArnold().GA_ArnoldAOVCreat("AO")
            GA_RenderArnoldLayer.GA_RenderArnold().GA_ArnoldAOVCreat("Fre")
            GA_RenderArnoldLayer.GA_RenderArnold().GA_ArnoldAOVCreat("N")
            GA_RenderArnoldLayer.GA_RenderArnold().GA_ArnoldAOVCreat("P")
            GA_RenderArnoldLayer.GA_RenderArnold().GA_ArnoldAOVCreat("Shadow")
            GA_RenderArnoldLayer.GA_RenderArnold().GA_ArnoldAOVCreat("Z")
            GA_RenderArnoldLayer.GA_RenderArnold().GA_ArnoldAOVCreat("Zdp")
            GA_RenderArnoldLayer.GA_RenderArnold().GA_ArnoldAOVCreat("direct_diffuse")
            GA_RenderArnoldLayer.GA_RenderArnold().GA_ArnoldAOVCreat("indirect_specular")
            GA_RenderArnoldLayer.GA_RenderArnold().GA_ArnoldAOVCreat("indirect_specular")
            GA_RenderArnoldLayer.GA_RenderArnold().GA_ArnoldAOVCreat("sss")
        #������Ⱦ��
        mc.createRenderLayer(objs,name=layertype+renderLayer, noRecurse=1, makeCurrent=1)
        #����defaultRenderLayer
        mc.editRenderLayerGlobals(currentRenderLayer='defaultRenderLayer')
        mc.setAttr("defaultRenderLayer.renderable", 0)
        result=u'========================��%s����Ⱦ���Ѵ���========================' %(layertype+renderLayer)

        return result

    #----------------------------------------------------------------------------------------------------------#      #----------------------------------------------------------#
        #------------------------------#
    # ����Ⱦ����Arnold��Ⱦ���á������Ը�����Ŀ������Ӳ�����
    #  Author  : ����
    #  Data    : 2017_07_07
    #------------------------------#
    #���ݲ�ͬ��Ⱦ����������
    def GA_ArnoldRendererSettings(self,renderLayer='co'):
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        print (u'===============!!!Start ��%s��!!!===============' % (u'Arnold����'))
        print 'Working...'
        #����arnold
        mc.setAttr('defaultRenderGlobals.imageFormat', 7)
        try:
           mc.loadPlugin('mtoa',qt=1)

        except:
            pass
        # �������ڣ���������UI


        #mel.eval('unifiedRenderGlobalsWindow')
        renderglobal=mc.getAttr('defaultRenderGlobals.currentRenderer')
        if renderglobal!='arnold':
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'arnold', type='string')
        # ��������Ľڵ���ǰ����
        import mtoa
        mtoa.core.createOptions()
        import mtoa.cmds.registerArnoldRenderer
        mtoa.cmds.registerArnoldRenderer.registerArnoldRenderer()
        samplingInfo=['defaultArnoldRenderOptions.AASamples','defaultArnoldRenderOptions.GIDiffuseSamples','defaultArnoldRenderOptions.GIGlossySamples','defaultArnoldRenderOptions.GIRefractionSamples','defaultArnoldRenderOptions.GISssSamples','defaultArnoldRenderOptions.GIVolumeSamples','defaultArnoldRenderOptions.lock_sampling_noise','defaultArnoldRenderOptions.sssUseAutobump']
        sampYak=[5,2,2,2,2,0,1,1]
        if shotInfo[0] in ['do6'] and renderLayer=='co':
            sampYak=[4,6,3,1,2,2,0,0]
        imageFormat=['defaultArnoldDriver.aiTranslator']
        imageYak=['exr']
        clamping=['defaultArnoldRenderOptions.use_sample_clamp','defaultArnoldRenderOptions.use_sample_clamp_AOVs','defaultArnoldRenderOptions.AASampleClamp']
        clamYak=[1,0,1.5]
        if shotInfo[0] in ['do6'] and renderLayer=='co':
            sampYak=[0,0,10]
        filter=['defaultArnoldFilter.width']
        filtYak=[2]
        rayDepth=['defaultArnoldRenderOptions.GITotalDepth','defaultArnoldRenderOptions.GIDiffuseDepth','defaultArnoldRenderOptions.GIGlossyDepth','defaultArnoldRenderOptions.GIReflectionDepth','defaultArnoldRenderOptions.GIRefractionDepth','defaultArnoldRenderOptions.GIVolumeDepth','defaultArnoldRenderOptions.autoTransparencyDepth','defaultArnoldRenderOptions.autoTransparencyThreshold']
        rayYak=[3,1,1,2,2,0,2,0.990]
        motionblur=['defaultArnoldRenderOptions.motion_blur_enable']
        motionYak=[0]
        tex=['defaultArnoldRenderOptions.use_existing_tiled_textures']
        texYak=[1]
        AOV=['defaultArnoldDriver.mergeAOVs','defaultArnoldRenderOptions.aovMode','defaultArnoldDriver.prefix']
        AOVYak=[1,1,'']
        strInfo=['defaultArnoldDriver.aiTranslator','defaultArnoldDriver.prefix']
        infos=[samplingInfo,imageFormat,clamping,filter,rayDepth,motionblur,tex,AOV]
        infoYak=[]
        if shotInfo[0] in ['do6']:
            infoYak=[sampYak,imageYak,clamYak,filtYak,rayYak,motionYak,texYak,AOVYak]
        if shotInfo[0] in ['do6']:
            for i in range(len(infos)):
                for j in range(len(infos[i])):
                    typeinfo=infos[i][j]
                    typNum=infoYak[i][j]
                    if typeinfo not in strInfo:
                        mc.setAttr(typeinfo,typNum)
                    else:
                        mc.setAttr(typeinfo,typNum,type='string')
            mc.setAttr('defaultArnoldDriver.halfPrecision',1)
            mc.setAttr('defaultArnoldDriver.autocrop',1)



