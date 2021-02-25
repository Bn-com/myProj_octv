# -*- coding: utf-8 -*-

'''
Created on 2013-6-18

@author: shenkang
'''
import maya.cmds as mc
import maya.mel as mel
import idmt.pipeline.db

# shader import
# file nodes ,for tga ,filter off ,for map ,filter config minmap


class zmRLConfig(object):

    def __init__(self):
        pass

    # UIZMRenderLayer
    def sk_UIZoomWhiteDolphinRenderLayersLayers(self):
        # 窗口
        if mc.window("sk_sceneUIZoomWhiteDolphinRenderLayers", ex=1):
            mc.deleteUI("sk_sceneUIZoomWhiteDolphinRenderLayers", window=True)
        mc.window("sk_sceneUIZoomWhiteDolphinRenderLayers", title="ZoomWhiteDolphin RenderLayers Tools", widthHeight=(420, 520), resizeToFitChildren = True, menuBar=0)
        # 主界面
        mc.columnLayout(adjustableColumn = True)
        
        mc.image(image = "Z:/Projects/Strawberry/Strawberry_Scratch/TD/image/p4.jpg",vis=1,width=445,height=267)
        mc.setParent("..")
        mc.setParent("..")
        # 分解创建
        mc.frameLayout(label=u'[MR]RenderLayers Ganeral | 通用设置', borderStyle='etchedOut')

        mc.rowLayout(numberOfColumns=4, columnWidth4=(100, 100, 100, 100))
        mc.button(l=u'工程目录设置', bgc=[0.3, 0.3, 0.3], width=100, height=25, c='mel.eval(\'source "//file-cluster/GDC/Resource/Support/Maya/projects/VickytheViking/vvSetProject.mel"\')\nmel.eval(\"vvSetProject\")')
        mc.button(l=u'Zdepth设置', bgc=[0.3, 0.3, 0.3], width=100, height=25, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.zmRLConfig().zmRLayerZdepthDistanceConfigUI()')
        mc.button(l=u'贴图尺寸设置', bgc=[0.3, 0.3, 0.3], width=100, height=25, c='mel.eval(\'source zwToggleMaps.mel;\')\nmel.eval(\"zwToggleMaps\\"\\"\")')
        mc.button(l=u'shading network修正', bgc=[0.3, 0.3, 0.3], width=100, height=25, c='from idmt.maya.ZoomWhiteDolphin import zm_namespace_shader\nreload(zm_namespace_shader)\nzm_namespace_shader.renamespaceUI()')

        mc.setParent("..")

        # 分解创建
        mc.frameLayout(label=u'[MR]RenderLayers Manual | 手动创建RenderLayers', borderStyle='etchedOut')

        mc.rowLayout(numberOfColumns=4, columnWidth4=(100, 100, 100, 100))
        mc.button(l=u'[CHR]CAUSTICS', bgc=[0.1, 0.1, 0.1], width=100, height=25, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.zmRLConfig().zmRLSpeficCreate(\"CHR_CAUSTICS\")')
        mc.button(l=u'[BG]CAUSTICS', bgc=[0.1, 0.1, 0.1], width=100, height=25, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.zmRLConfig().zmRLSpeficCreate(\"BG_CAUSTICS\")')
        mc.button(l=u'[FG]CO', bgc=[0.1, 0.1, 0.1], width=100, height=25, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.zmRLConfig().zmRLSpeficCreate(\"FG_CO\")')
        mc.button(l=u'[BG]CO', bgc=[0.1, 0.1, 0.1], width=100, height=25, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.zmRLConfig().zmRLSpeficCreate(\"BG_CO\")')
        mc.setParent("..")

        mc.rowLayout(numberOfColumns=4, columnWidth4=(100, 100, 100, 100))
        mc.button(l=u'[ALL]Zdepth', bgc=[0.1, 0.1, 0.1], width=100, height=25, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.zmRLConfig().zmRLSpeficCreate(\"ALL_ZDEPTH\")')
        mc.button(l=u'[ALL]Mask01', bgc=[0.1, 0.1, 0.1], width=100, height=25, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.zmRLConfig().zmRLSpeficCreate(\"ALL_MASK01\")')
        mc.button(l=u'[BG]Mask', bgc=[0.1, 0.1, 0.1], width=100, height=25, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.zmRLConfig().zmRLSpeficCreate(\"BG_MASK\")')
        mc.button(l=u'[SEA]CP', bgc=[0.1, 0.1, 0.1], width=100, height=25, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.zmRLConfig().zmRLSpeficCreate(\"SEA_CP\")')
        mc.setParent("..")

        mc.rowLayout(numberOfColumns=4, columnWidth4=(100, 100, 100, 100))
        mc.button(l=u'[SEA]COa', bgc=[0.1, 0.1, 0.1], width=100, height=25, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.zmRLConfig().zmRLSpeficCreate(\"SEA_WO\")')
        mc.button(l=u'[FG]LGT', bgc=[0.1, 0.1, 0.1], width=100, height=25, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.zmRLConfig().zmRLSpeficCreate(\"FG_LGT\")')
        mc.button(l=u'[SEA]SHDW', bgc=[0.1, 0.1, 0.1], width=100, height=25, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.zmRLConfig().zmRLSpeficCreate(\"SEA_SHDW\")')
        mc.button(l=u'[SEA]COu', bgc=[0.1, 0.1, 0.1], width=100, height=25, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.zmRLConfig().zmRLSpeficCreate(\"SEA_TO\")')
        mc.setParent("..")

        mc.rowLayout(numberOfColumns=4, columnWidth4=(100, 100, 100, 100))
        mc.button(l=u'[CHR]LGTR', bgc=[0.1, 0.1, 0.1], width=100, height=25, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.zmRLConfig().zmRLSpeficCreate(\"CHR_LGTSYS\")')
        mc.button(l=u'[ALL]Mask02', bgc=[0.1, 0.1, 0.1], width=100, height=25, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.zmRLConfig().zmRLSpeficCreate(\"ALL_MASK02\")')
        mc.button(l=u'[LG]LGT', bgc=[0.1, 0.1, 0.1], width=100, height=25, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.zmRLConfig().zmRLSpeficCreate(\"ALL_SHADOW\")')
        mc.button(l=u'[CHR]IDP', bgc=[0.1, 0.1, 0.1], width=100, height=25, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.zmRLConfig().zmRLSpeficCreate(\"CHR_IDP\")')
        mc.setParent("..")

        mc.rowLayout(numberOfColumns=4, columnWidth4=(100, 100, 100, 100))
        mc.button(l=u'[ALL]PREVIEW', bgc=[0.1, 0.1, 0.1], width=100, height=25, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.zmRLConfig().zmRLSpeficCreate(\"ALL_PREVIEW\")')
        mc.button(l=u'[ALL]NM', bgc=[0.1, 0.1, 0.1], width=100, height=25, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.zmRLConfig().zmRLSpeficCreate(\"ALL_NM\")')
        mc.button(l=u'[CHR]LINE', bgc=[0.1, 0.1, 0.1], width=100, height=25, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.zmRLConfig().zmRLSpeficCreate(\"CHR_LINE\")')
        mc.button(l=u'[BG]Zdepth', bgc=[0.1, 0.1, 0.1], width=100, height=25, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.zmRLConfig().zmRLSpeficCreate(\"BG_ZDEPTH\")')
        mc.setParent("..")

        mc.setParent("..")
        
        mc.rowLayout(numberOfColumns=4, columnWidth4=(100, 100, 100, 100))
        mc.button(l=u'[BG]Mask03', bgc=[0.1, 0.1, 0.1], width=100, height=25, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.zmRLConfig().zmRLSpeficCreate(\"BG_MASK03\")')
        mc.button(l=u'[ALL]Reflect', bgc=[0.1, 0.1, 0.1], width=100, height=25,c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.zmRLConfig().zmRLSpeficCreate(\"ALL_Reflect\")')
        mc.button(l=u'[ALL]EXTRALIGHT', bgc=[0.1, 0.1, 0.1], width=100, height=25,c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.zmRLConfig().zmRLSpeficCreate(\"ALL_Volume\")')
        mc.button(l=u'[CHR]Depth', bgc=[0.1, 0.1, 0.1], width=100, height=25,c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.zmRLConfig().zmSpecialdepthtCreate(0)')
        mc.setParent("..")

        mc.setParent("..")
        
        mc.rowLayout(numberOfColumns=4, columnWidth4=(100, 100, 100, 100))
        mc.button(l=u'[FG]LGTNIGHT', bgc=[0.1, 0.1, 0.1], width=100, height=25,c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.zmRLConfig().zmRLSpeficCreate(\"FG_LGTNIGHT\")')
        mc.button(l=u'[waves]', bgc=[0.1, 0.1, 0.1], width=100, height=25,c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.zmRLConfig().zmRLSpeficCreate(\"FG_Waves\")')
        mc.button(l=u'[CHR]BABY', bgc=[0.1, 0.1, 0.1], width=100, height=25, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.zmRLConfig().zmRLSpeficCreate(\"CHR_baby\")')
        mc.button(l=u'[BG]CAUSTICSWALLS', bgc=[0.1, 0.1, 0.1], width=100, height=25,c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.zmRLConfig().zmRLSpeficCreate(\"BG_CAUSTICSWALLS\")')
        mc.setParent("..")

        mc.rowLayout(numberOfColumns=4, columnWidth4=(100, 100, 100, 100))
        mc.button(l=u'VOLUMELIGHTS', bgc=[0.1, 0.1, 0.1], width=100, height=25,c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.zmRLConfig().zmRLSpeficCreate(\"BG_VOLUMELIGHTS\")')
        mc.button(l=u'[PORP]MASK04', bgc=[0.1, 0.1, 0.1], width=100, height=25,c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.zmRLConfig().zmRLSpeficCreate(\"PROP_MASK04\")')
        mc.button(l=u'[FG]LGTFIRE', bgc=[0.1, 0.1, 0.1], width=100, height=25,c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.zmRLConfig().zmRLSpeficCreate(\"FG_FIRE\")')
        mc.button(l=u'[CHR]LGTFIRE', bgc=[0.1, 0.1, 0.1], width=100, height=25,c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.zmRLConfig().zmRLSpeficCreate(\"CHR_FIRE\")')
        
        mc.setParent("..")
        mc.setParent("..")        
        

        # Arnold
        mc.frameLayout(label=u'[Arnold]RenderLayers Manual | 手动创建RenderLayers', borderStyle='etchedOut')

        mc.rowLayout(numberOfColumns=4, columnWidth4=(100, 100, 100, 100))
        mc.button(l=u'[==wait==]', bgc=[0.1, 0.1, 0.1], width=100, height=25)
        mc.button(l=u'[==wait==]', bgc=[0.1, 0.1, 0.1], width=100, height=25)
        mc.button(l=u'[Main]双面材质层', bgc=[0.1, 0.1, 0.1], width=100, height=25, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.zmRLConfig().zmRLSelectMSKreate(\"Double_Side\")')
        mc.button(l=u'[==wait==]', bgc=[0.1, 0.1, 0.1], width=100, height=25)
        mc.setParent("..")

        mc.setParent("..")

        mc.frameLayout(label=u'[Tools]RenderLayers Other Tools ', borderStyle='etchedOut')
        mc.rowLayout(numberOfColumns=4, columnWidth4=(100, 100, 100, 100))
        mc.button(l=u'[Shader]R', bgc=[0.8, 0.1, 0.1], width=100, height=25, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.zmRLConfig().zmRGBMShaderCreate(\"R\")')
        mc.button(l=u'[Shader]G', bgc=[0.1, 0.8, 0.1], width=100, height=25, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.zmRLConfig().zmRGBMShaderCreate(\"G\")')
        mc.button(l=u'[Shader]B', bgc=[0.1, 0.6, 0.8], width=100, height=25, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.zmRLConfig().zmRGBMShaderCreate(\"B\")')
        mc.button(l=u'[Shader]M', bgc=[0.0, 0.0, 0.0], width=100, height=25, c='from idmt.maya.ZoomWhiteDolphin import sk_renderLayer_ZoomWhiteDolphin\nreload(sk_renderLayer_ZoomWhiteDolphin)\nsk_renderLayer_ZoomWhiteDolphin.zmRLConfig().zmRGBMShaderCreate(\"M\")')
        mc.setParent("..")
        mc.setParent("..")

        mc.setParent("..")
        mc.showWindow("sk_sceneUIZoomWhiteDolphinRenderLayers")
    
    # 选取模式
    def zmRLSelectMode(self):
        rlObjs = []
        needObjs=[]
        # 选取模式
        selObjs = mc.ls(sl=1, l=1)
        if not selObjs:
            mc.confirmDialog(title=u'警告', message=u'请选择物体', button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')
        checkMeshes = mc.listRelatives(selObjs, ad=1, type='mesh',f = 1)
        if not checkMeshes:
            mc.confirmDialog(title=u'警告', message=u'请选择物体', button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')
        else: 
            needObjs=  mc.listRelatives(checkMeshes, p=1, type='transform', f=1)         
            rlObjs = list(set(needObjs))
        return rlObjs
   
    # Create Single Render Layer
    def zmRLSpeficCreate(self, renderLayer, saveMode='', selectMode=0, arnoldType=0):
        print (u'===============!!!Start 【%s】!!!===============' % (renderLayer))
        print 'Working...'

        from idmt.maya.py_common import sk_checkCommon
        reload(sk_checkCommon)

        # Back To MasterLayer
        mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')

        cacheFiles = mc.ls(type='cacheFile')

        # clean Unknwon Nodes
        sk_checkCommon.sk_checkTools().checkDonotNodeCleanBase(0)


        # common Setting
        self.zmRLCommonConfig()
        self.zmRLSkydomeMoodConfig()

        # arnold Setting
        if arnoldType:
            self.arnoldRendererSettings()

        # mr Setting
        self.mentalRayProductionLevel()
        # 指定层
        BGType = renderLayer.split('_')[0]
        layerType = renderLayer.split('_')[1]
        try:
            mc.delete(renderLayer)
        except:
            pass

        # self.zmRLExrConfig()

        # 优先处理master层

        # preview
        if layerType == 'PREVIEW':
            if mc.ls(BGType + '_' + layerType):
                mc.delete(BGType + '_' + layerType)
            self.zmRLPVCreate(BGType, selectObjType=selectMode)


        # FG_CO,BG_CO
        if layerType == 'CO':
            if mc.ls(BGType + '_' + layerType):
                mc.delete(BGType + '_' + layerType)
            self.zmRLWCOCreate(BGType, selectObjType=selectMode)


        # Normal
        if layerType == 'NM':
            if mc.ls(BGType + '_' + layerType):
                mc.delete(BGType + '_' + layerType)
            if arnoldType == 0:
                self.zmRLNMCreate(BGType, selectObjType=selectMode)
            if arnoldType == 1:
                self.zmRLNMArnoldCreate(BGType, selectObjType=selectMode)

        # Light_New
        if layerType == 'LGTSYS':

            if mc.ls(BGType + '_' + layerType):
                mc.delete(BGType + '_' + layerType)
            self.zmRLLIGHTNewCreate(BGType, selectObjType=selectMode)

        if layerType == 'LTSYS':
            if mc.ls(BGType + '_' + layerType):
                mc.delete(BGType + '_' + layerType)
            self.zmRLLIGHTCHCreate(BGType, selectObjType=selectMode)
            
        #CHR_IDP
        if layerType == 'IDP':
            if mc.ls(BGType + '_' + layerType):
                mc.delete(BGType + '_' + layerType)
            self.zmIDPCHRCreate(BGType, selectObjType=selectMode)
            
        #双面材质
        if layerType == 'Side':
            if mc.ls(BGType + '_' + layerType):
                mc.delete(BGType + '_' + layerType)
            self.zmRLSelectMSKreate(BGType, selectObjType=selectMode)
        # ZDepth
        if layerType == 'ZDEPTH':
            if mc.ls(BGType + '_' + layerType):
                mc.delete(BGType + '_' + layerType)
            self.zmRLZDEPTHCreate(BGType, selectObjType=selectMode)
        # SHDW
        if layerType == 'SHDW':
            if mc.ls(BGType + '_' + layerType):
                mc.delete(BGType + '_' + layerType)
            self.zmRLSDCreate(BGType, selectObjType=selectMode)
        # LINE
        if layerType == 'LINE':
            if mc.ls(BGType + '_' + layerType):
                mc.delete(BGType + '_' + layerType)
            self.zmRLLineCreate(BGType, selectObjType=selectMode)
        # CAUSTICS
        if layerType == 'CAUSTICS':
            if mc.ls(BGType + '_' + layerType):
                mc.delete(BGType + '_' + layerType)
            self.zmRLCausticsCreate(BGType, selectObjType=selectMode)
        #SEA_COa
        if layerType == 'WO':
            if mc.ls(BGType + '_' + layerType):
                mc.delete(BGType + '_' + layerType)
            self.zmRLSEACOaCreate(BGType, selectObjType=selectMode)
            
         #SEA_COu
        if layerType == 'TO':
            if mc.ls(BGType + '_' + layerType):
                mc.delete(BGType + '_' + layerType)
            self.zmRLSEACObCreate(BGType, selectObjType=selectMode)           
                               
        # MASK_01
        if layerType == 'MASK01':
            if mc.ls(BGType + '_' + layerType):
                mc.delete(BGType + '_' + layerType)
            self.zmRLMSK01reate(BGType, selectObjType=selectMode)

        if layerType == 'MASK02':
            if mc.ls(BGType + '_' + layerType):
                mc.delete(BGType + '_' + layerType)
            self.zmRLMSK02reate(BGType, selectObjType=selectMode)
            
        if layerType == 'MASK03':
            if mc.ls(BGType + '_' + layerType):
                mc.delete(BGType + '_' + layerType)
            self.zmMskCCreate(BGType, selectObjType=selectMode)           
        # MASK_01
        if layerType == 'MSK':
            if mc.ls(BGType + '_' + layerType):
                mc.delete(BGType + '_' + layerType)
            self.zmRLSeaMSKreate()

        if layerType == 'MASK':
            if mc.ls(BGType + '_' + layerType):
                mc.delete(BGType + '_' + layerType)
            self.zmRLMskCreate(BGType, selectObjType=selectMode)

        if layerType == 'CP':
            if mc.ls(BGType + '_' + layerType):
                mc.delete(BGType + '_' + layerType)
            self.zmSEAcoCreate(BGType, selectObjType=selectMode)

        if layerType == 'SHADOW':
            if mc.ls(BGType + '_' + layerType):
                mc.delete(BGType + '_' + layerType)
            self.zmLGLGTCreate(BGType, selectObjType=selectMode)
            
        if layerType == 'Reflect':
            if mc.ls(BGType + '_' + layerType):
                mc.delete(BGType + '_' + layerType)
            self.zmReflectCreate(BGType, selectObjType=selectMode)            
            
        if layerType == 'Volume':
            if mc.ls(BGType + '_' + layerType):
                mc.delete(BGType + '_' + layerType)
            self.zmRLExtraLIGHTCreate(BGType, selectObjType=selectMode) 
            
        if layerType == 'LGTNIGHT':
            if mc.ls(BGType + '_' + layerType):
                mc.delete(BGType + '_' + layerType)
            self.zmFGLGTNIGHTCreate(BGType, selectObjType=selectMode)
        
        if layerType == 'Waves':
            if mc.ls(BGType + '_' + layerType):
                mc.delete(BGType + '_' + layerType)
            self.zmRLwavesCreate(BGType, selectObjType=selectMode)  
                       
        if layerType == 'baby':
            if mc.ls(BGType + '_' + layerType):
                mc.delete(BGType + '_' + layerType)
            self.zmRLLIGHTBabyCreate(BGType, selectObjType=selectMode)

        if layerType == 'CAUSTICSWALLS':
            if mc.ls(BGType + '_' + layerType):
                mc.delete(BGType + '_' + layerType)
            self.zmRLCAUSTICSWALLSCreate(BGType, selectObjType=selectMode)

        if layerType == 'VOLUMELIGHTS':
            if mc.ls(BGType + '_' + layerType):
                mc.delete(BGType + '_' + layerType)
            self.zmRLVOLUMELIGHTSCreate(BGType, selectObjType=selectMode)

        # LIGHT
        if layerType == 'LGT':
            if BGType in ['CHRF', 'CHRB', 'FG']:
                if BGType == 'CHRF':
                    if mc.ls('CHR_LGTF'):
                        mc.delete('CHR_LGTF')
                if BGType == 'CHRB':
                    if mc.ls('CHR_LGTB'):
                        mc.delete('CHR_LGTB')
                if BGType == 'FG':
                    if mc.ls('FG_LGT'):
                        mc.delete('FG_LGT')
                    BGType = 'LGTFG'
            else:
                if mc.ls(BGType + '_' + layerType):
                    mc.delete(BGType + '_' + layerType)
            self.zmRLLIGHTCreate(BGType, selectObjType=selectMode)

        if layerType == 'MASK04':
            if mc.ls(BGType + '_' + layerType):
                mc.delete(BGType + '_' + layerType)
            self.zmMSK04Create(BGType, selectObjType=selectMode)  
            

        if layerType == 'FIRE':
            if mc.ls(BGType + '_' + layerType):
                mc.delete(BGType + '_' + layerType)
            self.zmFIRECreate(BGType, selectObjType=selectMode)  
                        
        # smoothSet
        self.zmRLDoSmooth()
        # Back To MasterLayer
        mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')
        # UnRender MasterLayer
        mc.setAttr("defaultRenderLayer.renderable", 0)
        # camSetting
        self.zmRLCamSetting()
        # common Setting
        # self.zmRLCommonConfig()

        if cacheFiles:
            for cache in cacheFiles:
                mc.setAttr((cache + '.enable'), 1)

        print (u'===============!!!Done  【%s】!!!===============' % ('renderLayer'))
        print '\n'

    # Import Camera
    def zmCamImport(self):
        camGrp = mc.ls('CAM_GRP')
        if camGrp:
            mc.delete(camGrp)

    # camSetting
    def zmRLCamSetting(self):
        from idmt.maya.py_common import sk_infoConfig
        reload(sk_infoConfig)
        # 处理cam
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        camName = 'CAM:cam_' + str(shotInfo[1]) + '_' + str(shotInfo[2]) + '_baked'
        if mc.ls(camName, type='transform'):
            camShape = mc.listRelatives(mc.ls(camName, type='transform')[0], ni=1, c=1)[0]
            mc.setAttr((camShape + '.renderable'), 1)
            try:
                mc.setAttr(('perspShape.renderable'), 0)
            except:
                pass
        else:
            mc.error('===============未找到有效CAM【%s】===============' % camName)

    # Create renderPass
    def zmRLRenderPass(self):
        print (u'===============!!!Start 【%s】!!!===============' % ('RenderPass'))
        print 'Working...'

        # shadow
        ex_rsShadow = mc.ls('shadow', type='renderPass')
        if ex_rsShadow:
            ex_rsShadow = 'shadow'
        else:
            renderPass = mc.shadingNode('renderPass', asRendering=1)
        configType = [1, 'SHD', 3, 256, 0, 1, 'Illumination', 1, 1, 0, 0, 0, 0, 1, 0, 10, 0, 10]
        self.zmRLRenderPassConfig(renderPass, configType)
        mc.rename(renderPass, 'shadow')
        print (u'===============!!!Done  【%s】!!!===============' % ('RenderPass'))
        print '\n'

    # 设置renderpass属性
    def zmRLRenderPassConfig(self, renderPass, configType):
        # renderable
        mc.setAttr((renderPass + '.renderable'), int(configType[0]))
        # nodeType
        mc.setRenderPassType(renderPass, type=str(configType[1]))
        # channels
        mc.setAttr((renderPass + '.numChannels'), int(configType[2]))
        # frameType
        mc.setAttr((renderPass + '.frameBufferType'), int(configType[3]))
        # colorProfile
        mc.setAttr((renderPass + '.colorProfile'), int(configType[4]))
        # filtering
        mc.setAttr((renderPass + '.filtering'), int(configType[5]))
        # passGroupName
        mc.setAttr((renderPass + '.passGroupName'), str(configType[6]), type='string')
        # holdout
        mc.setAttr((renderPass + '.holdout'), int(configType[7]))
        # transparency
        mc.setAttr((renderPass + '.useTransparency'), int(configType[8]))
        # reflectHidden
        mc.setAttr((renderPass + '.reflectHidden'), int(configType[9]))
        # refractHidden
        mc.setAttr((renderPass + '.refractHidden'), int(configType[10]))
        # hiddenReflect
        mc.setAttr((renderPass + '.hiddenReflect'), int(configType[11]))
        # hiddenRefract
        mc.setAttr((renderPass + '.hiddenRefract'), int(configType[12]))
        # transparentAttenuation
        mc.setAttr((renderPass + '.transparentAttenuation'), int(configType[13]))
        # minReflectionLevel
        mc.setAttr((renderPass + '.minReflectionLevel'), int(configType[14]))
        # maxReflectionLevel
        mc.setAttr((renderPass + '.maxReflectionLevel'), int(configType[15]))
        # minRefractionLevel
        mc.setAttr((renderPass + '.minRefractionLevel'), int(configType[16]))
        # maxRefractionLevel
        mc.setAttr((renderPass + '.maxRefractionLevel'), int(configType[17]))

    # 连接所有材质节点到对应的idpass
    def renderpassConnect(self):
        colorBufferNods = mc.ls(type='writeToColorBuffer')
        for node in colorBufferNods:
            # 无法将通用的断开命令提前。。断开和连接操作必须连续才有效
            # 处理colorID
            if '_ColorID' in node and '_ColorID2' not in node and '_ColorID3' not in node:
                # 首先要获取当前连接的属性
                lastNode = mc.listConnections((node + '.renderPass'), s=1)
                if lastNode:
                    mc.disconnectAttr((lastNode[0] + '.message'), (node + '.renderPass'))
                mc.connectAttr("idPass1.message", (node + '.renderPass'))
            # 处理colorID2
            if '_ColorID2' in node:
                # 首先要获取当前连接的属性
                lastNode = mc.listConnections((node + '.renderPass'), s=1)
                if lastNode:
                    mc.disconnectAttr((lastNode[0] + '.message'), (node + '.renderPass'))
                mc.connectAttr("idPass2.message", (node + '.renderPass'))
            # 处理colorID3
            if '_ColorID3' in node:
                # 首先要获取当前连接的属性
                lastNode = mc.listConnections((node + '.renderPass'), s=1)
                if lastNode:
                    mc.disconnectAttr((lastNode[0] + '.message'), (node + '.renderPass'))
                mc.connectAttr("idPass3.message", (node + '.renderPass'))
            # 处理colorID_CHR
            if '_ColorID_CHR' in node:
                # 首先要获取当前连接的属性
                lastNode = mc.listConnections((node + '.renderPass'), s=1)
                if lastNode:
                    mc.disconnectAttr((lastNode[0] + '.message'), (node + '.renderPass'))
                mc.connectAttr("idPassChr.message", (node + '.renderPass'))
            if '_ColorID_ChrMain' in node:
                # 首先要获取当前连接的属性
                lastNode = mc.listConnections((node + '.renderPass'), s=1)
                if lastNode:
                    mc.disconnectAttr((lastNode[0] + '.message'), (node + '.renderPass'))
                mc.connectAttr("idPassChrMain.message", (node + '.renderPass'))

    # 物体分类清单
    # import后不用参考时也可以处理
    # 使用条件：sk_sceneConfig.sk_sceneConfig().sk_sceneReorganize(0)
    def zmRLObjectsTList(self, objType=1, objs=[]):
        # 获取root
        from idmt.maya.py_common import sk_checkCommon
        reload(sk_checkCommon)

        refCHR = []
        refPROP = []
        refSET = []
        refSKY = []
        refSEA = []
        needSKY = []
        needPROP = []
        needrefSEA = []

        if mc.ls('CHR_GRP'):
            if mc.listRelatives('CHR_GRP', c=1, f=1, type='transform'):
                refCHR = mc.listRelatives('CHR_GRP', c=1, f=1, type='transform')
        if mc.ls('PRP_GRP'):
            if mc.listRelatives('PRP_GRP', c=1, f=1, type='transform'):
                refPROP = mc.listRelatives('PRP_GRP', c=1, f=1, type='transform')
                for prop in refPROP:
                    if '_p00501surfing' not in prop:
                        needPROP.append(prop)
                    if '_p00501surfing' in prop:
                        needrefSEA.append(prop)

        if needrefSEA:
            needrefSEATemp = list(set(needrefSEA))
            needrefSEA = []
            for seaGrp in needrefSEATemp:
                objs = mc.listRelatives(seaGrp, ad=1, f=1, type='transform')
                if objs:
                    for obj in objs:
                        if 'MSH_c_hi_shell_ca_' in obj:
                            needrefSEA.append(obj)

        if mc.ls('SET_GRP'):
            if mc.listRelatives('SET_GRP', c=1, f=1, type='transform'):
                refSETgroup = mc.listRelatives('SET_GRP', c=1, f=1, type='transform')
                refSET=mc.listRelatives(refSETgroup, c=1, f=1, type='transform')
                for obj in refSET:
                    if 'FX' in obj:
                        refSET.remove(obj)

        if refSET:
            grpSKY = mc.ls('*:*MSH_c_hi_Cyclos', type='transform', l=1) or mc.ls('*:*:*MSH_c_hi_Cyclos', type='transform', l=1)
            if grpSKY:
                meshes = mc.listRelatives(grpSKY, ad=1, ni=1, type='mesh', f=1)
                if meshes:
                    refSKY = mc.listRelatives(meshes, p=1, type='transform', f=1)

        if refSKY:
            for obj in refSKY:
                if '_sea_' not in obj:
                    needSKY.append(obj)

        refSKY = needSKY

        refSEA = needrefSEA + mc.ls('*:*_sea_*', type='transform') + mc.ls('*_sea_', type='transform')

        refPROP = needPROP

        for i in range(4):
            needInfo = []
            if i == 0:
                refGrps = refCHR
            if i == 1:
                refGrps = refPROP
            if i == 2:
                refGrps = refSET
            if i == 3:
                refGrps = refSKY
            if i == 4:
                refGrps = refSEA
            if refGrps:
                meshes = mc.listRelatives(refGrps, ad=1, ni=1, type='mesh', f=1)
                if meshes:
                    meshGrps = mc.listRelatives(meshes, p=1, type='transform', f=1)
                    needInfo = meshGrps
            if i == 0:
                refCHR = needInfo
            if i == 1:
                refPROP = needInfo
            if i == 2:
                refSET = needInfo
            if i == 3:
                refSKY = needInfo
            if i == 4:
                refSEA = needInfo

        # 鱼群支持
        fishGrp = 'fishGeo_grp'
        if mc.objExists(fishGrp):
            meshes = mc.listRelatives(fishGrp, ad=1, ni=1, type='mesh')
            if meshes:
                refPROP = mc.listRelatives(meshes, p=1, type='transform', f=1)

        result = []
        result.append(list(set(refCHR)))
        result.append(list(set(refPROP)))
        result.append(list(set(refSET)))
        result.append(list(set(refSKY)))
        result.append(list(set(refSEA)))
        return result
    # 渲染标准设置

    def zmRLCommonConfig(self):
        print (u'===============!!!Start 【%s】!!!===============' % (u'标准设置'))
        print 'Working...'
        # Camera
        from idmt.maya.py_common import sk_hbExceptCam
        reload(sk_hbExceptCam)
        # sk_hbExceptCam.sk_hbExceptCam().camServerReference()

        # 开启窗口，创建各种UI
        # mel.eval('unifiedRenderGlobalsWindow')

        # 标准设置
        mc.setAttr('defaultRenderQuality.edgeAntiAliasing', 1)
        mc.setAttr('defaultRenderGlobals.animation', 1)
        mc.setAttr('defaultRenderGlobals.outFormatControl', 0)
        mc.setAttr('defaultRenderGlobals.extensionPadding', 4)
        mc.setAttr('defaultRenderGlobals.imageFilePrefix', '<Layer>/<Scene>_<Layer>', type='string')
        mc.setAttr('defaultResolution.width', 1920)
        mc.setAttr('defaultResolution.height', 1080)
        mc.setAttr('defaultResolution.deviceAspectRatio', 1.777)
        mc.setAttr('defaultResolution.pixelAspect', 1.00)
        mc.evalDeferred('import maya.cmds as mc\nmc.setAttr((\'defaultResolution.pixelAspect\'),1)', lowestPriority=1)
        mc.setAttr('defaultResolution.dotsPerInch', 72)
        mc.setAttr('defaultRenderQuality.edgeAntiAliasing', 1)
        # 开始处理
        from idmt.maya.py_common import sk_infoConfig
        shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
        shot = shotInfos[0] + '_' + shotInfos[1] + '_' + shotInfos[2]
        anim = idmt.pipeline.db.GetAnimByFilename(shot)
        startFrame = anim.frmStart
        endFrame = anim.frmEnd
        fpsFrame = anim.fps
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
            preStartFrame = startFrame - 10
            mc.playbackOptions(animationStartTime=preStartFrame)
            # 结束帧
            mc.playbackOptions(max=endFrame)
            # 结束预留
            posEndFrame = endFrame + 10
            mc.playbackOptions(animationEndTime=posEndFrame)
            # 渲染范围设置
            mc.setAttr('defaultRenderGlobals.startFrame', startFrame)
            mc.setAttr('defaultRenderGlobals.endFrame', endFrame)

        mel.eval('setAttr -type "string" defaultRenderGlobals.preMel "cycleCheck -e off"')

        # 格式命名
        # 原先调用菜单，现在直接改节点
        mc.setAttr('defaultRenderGlobals.animation', 1)
        mc.setAttr('defaultRenderGlobals.putFrameBeforeExt', 1)
        mc.setAttr('defaultRenderGlobals.periodInExt', 1)
        mc.setAttr('defaultRenderGlobals.extensionPadding', 4)
        if mc.getAttr('defaultRenderGlobals.outFormatControl') == 1:
            mc.setAttr('defaultRenderGlobals.outFormatControl', 0)

        # mel.eval("prefWndUnitsChanged \"time\";")

        print (u'===============!!!Done  【%s】!!!===============' % u'标准设置')
        print '\n'

    # mr 产品级设置
    def mentalRayProductionLevel(self):
        print (u'===============!!!Start 【%s】!!!===============' % (u'MR设置'))
        print 'Working...'

        mc.setAttr('defaultRenderGlobals.imageFormat', 7)
        
        if not(mc.pluginInfo("Mayatomr.mll",query=1,loaded=1)):
            mel.eval('loadPlugin "Mayatomr"')
            
        mc.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')
        # 开启窗口，创建各种UI，该死的MR，为啥不直接生成，非要延时。。
        # mel.eval('unifiedRenderGlobalsWindow')
        # 创建UI
        #mel.eval('mentalrayUI ""')

        # 创建miDefaultOptions节点
        mel.eval('miCreateDefaultNodes')
        # 读取之前创建的production_preset
        mel.eval('nodePreset -load "miDefaultOptions" "production_mi"')

        # 删除天光，关闭FG
        mc.setAttr('miDefaultOptions.finalGather', 0)
        try:
            mel.eval('miDeleteSunSky')
        except:
            pass



        # exr
        # mc.editRenderLayerAdjustment('defaultRenderGlobals.imageFormat')
        mc.setAttr('defaultRenderGlobals.imageFormat', 51)
        mc.setAttr('defaultRenderGlobals.imfkey', 'exr', type='string')
        mc.setAttr('mentalrayGlobals.imageCompression', 4)
        mc.setAttr('mentalrayGlobals.compressionQuality', 0)
        mc.setAttr('miDefaultOptions.maxSamples', 2)

        try:
            mc.setAttr('miDefaultOptions.minSamples', 0)
        except:
            pass

        mc.setAttr('miDefaultOptions.filter', 2)

        print (u'===============!!!Done  【%s】!!!===============' % (u'MR设置'))
        print '\n'



    # 获取所有SG节点
    def zmRLSGNodesGet(self):
        SGNodes = mc.ls(type='shadingEngine')
        SGNodes.remove('initialParticleSE')
        SGNodes.remove('initialShadingGroup')
        # SG分类
        refSGCHR = []
        refSGPROP = []
        refSGSET = []
        # 判断分类
        # 根据连接的物体的参考进行判断
        for SGNode in SGNodes:
            listMeshTransform = mc.listConnections(SGNode, type='mesh')
            if listMeshTransform:
                # 只选一个进行处理即可
                # 取参考路径
                # 获取refPath
                refPath = mc.referenceQuery(listMeshTransform[0], filename=True)
                refPath = refPath.lower()
                # 角色
                if '/characters/' in refPath:
                    refSGCHR.append(SGNode)
                # 道具
                if '/props/' in refPath:
                    refSGPROP.append(SGNode)
                # 其他类，下面细化
                if '/sets/' in refPath:
                    refSGSET.append(SGNode)
        result = []
        result.append(refSGCHR)
        result.append(refSGPROP)
        result.append(refSGSET)
        return result

    # smoothSet
    def zmRLDoSmooth(self, layerType=1):
        from idmt.maya.py_common import sk_smoothSet
        reload(sk_smoothSet)
        # 非PFX层用
        if layerType == 1:
            sk_smoothSet.sk_smoothSetTools().smoothSetDoSmooth()

    # 获取有透明贴图的物体
    def zmRLTransparencyObjsOld(self):
        transparencySG = []
        doNotNeedSG = ['_ao_', '_nm_', '_light_', '_rim_', '_spec_']
        # 获取file节点
        SGNodes = mc.ls(type='shadingEngine')
        for SGNode in SGNodes:
            doNot = 0
            for doNotNeed in doNotNeedSG:
                if doNotNeed in SGNode.lower():
                    doNot = doNot + 1
            # 剔除不要的分层SG节点，只保留原始SG
            if doNot == 0:
                # 获取shader
                shaderNode = mc.listConnections(SGNode + '.surfaceShader')
                if shaderNode:
                    # 获取提供透明属性的上级连接的节点
                    transpancyNode = ''
                    if mc.nodeType(shaderNode) != 'surfaceShader':
                        if mc.objExists(shaderNode[0] + '.transparency'):
                            transpancyAttr = mc.ls(shaderNode[0] + '.transparency')
                            transpancyNode = mc.listConnections(transpancyAttr[0], plugs=1, connections=1, destination=0)
                    else:
                        transpancyAttr = mc.ls(shaderNode[0] + '.outTransparency')
                        transpancyNode = mc.listConnections(transpancyAttr[0], plugs=1, connections=1, destination=0)
                    # 存在透明通道，则保存
                    if transpancyNode:
                        transpancyNode = mc.listConnections(transpancyAttr[0], plugs=1)
                        # SG节点命名判断
                        # 遵循'SHD_..._keyInfo_SG'
                        if ':' in SGNode:
                            #meshes = mc.listConnections(SGNode,type = 'mesh')
                            meshes = mc.sets(SGNode, q=1)
                            # 记录信息
                            transparencySG.append([SGNode, meshes, transpancyNode[0]])
                        else:
                            #meshes = mc.listConnections(SGNode,type = 'mesh')
                            meshes = mc.sets(SGNode, q=1)
                            # 记录信息
                            transparencySG.append([SGNode, meshes, transpancyNode[0]])

        return transparencySG

    # 获取有透明贴图的物体,通过参考获取服务器端数据
    # refNamespaceMode 0 Ref Mode | 1 Namespace Mode
    def zmRLTransparencyObjs(self, refNamespaceMode=1):
        from idmt.maya.py_common import sk_referenceConfig
        reload(sk_referenceConfig)
        from idmt.maya.py_common import sk_infoConfig
        reload(sk_infoConfig)
        import os

        allAssetInfo = []
        allAssetNsInfo = []

        transpancySGNodesAll = []
        transpancyMeshesAll = []
        transpancyNodesAll = []

        # refInfo
        if refNamespaceMode == 0:
            refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
            refNodes = refInfos[0][0]
            refPaths = refInfos[1][0]
            refns = refInfos[2][0]

            if refNodes:
                allAssetInfo = []
                for i in range(len(refNodes)):
                    # 非cam
                    if '_' in refNodes[i]:
                        assetFileName = refPaths[i].split('/')[-1]
                        assetInfo = assetFileName.split('_')
                        assetInfoNeed = assetInfo[0] + '_' + assetInfo[1] + '_' + assetInfo[2]
                        allAssetInfo.append(assetInfoNeed)
                        allAssetNsInfo.append(refns[i])

        # Namespace Mode
        if refNamespaceMode == 1:
            nsList = mc.namespaceInfo(listOnlyNamespaces=1)
            if 'UI' in nsList:
                nsList.remove('UI')
            if 'shared' in nsList:
                nsList.remove('shared')
            if nsList:
                for i in range(len(nsList)):
                    numStr = []
                    for j in range(10):
                        numStr.append(str(j))
                    ns = nsList[i]
                    # 只要一级namespace
                    if '_' in ns and ":" not in ns:
                        assetInfo = ns.split('_')
                        if len(assetInfo) == 2:
                            assetInfoNeed = assetInfo[0] + '_' + assetInfo[1] + '_h'
                        if len(assetInfo) > 2:
                            assetInfoNeed = assetInfo[0] + '_' + assetInfo[1] + '_' + assetInfo[2]
                            print assetInfoNeed
                            print assetInfo
                            # 处理非正常namespace
                            if assetInfo[-1][-1] in numStr or assetInfo[2] not in ['h', 'm', 'l']:
                                assetInfoNeed = assetInfo[0] + '_' + assetInfo[1] + '_h'
                        allAssetInfo.append(assetInfoNeed)
                        allAssetNsInfo.append(ns)


        if allAssetInfo:
            # 获得asset的trans信息
            serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
            for asset in allAssetInfo:
                # print '---'
                # print asset
                id = allAssetInfo.index(asset)
                assetInfo = asset.split('_')
                ns = allAssetNsInfo[id]
                serverTransPath = serverPath + 'data/AssetInfos/transShaderInfo/' + assetInfo[0] + '/' + str(assetInfo[1]) + '/' + str(assetInfo[2]) + '/'
                # print serverTransPath
                # asset SG 信息
                assetTransSGNodes = []
                if os.path.exists(serverTransPath + 'transSGNodes.txt'):
                    assetTransSGNodesTemp = sk_infoConfig.sk_infoConfig().checkFileRead(serverTransPath + 'transSGNodes.txt')
                    for info in assetTransSGNodesTemp:
                        assetTransSGNodes.append(ns + ':' + info)
                # asset Mesh 信息
                assetTransMeshesTemp = []
                if os.path.exists(serverTransPath + 'transMeshes.txt'):
                    assetTransMeshesTemp = sk_infoConfig.sk_infoConfig().checkFileRead(serverTransPath + 'transMeshes.txt')
                # asset Shader Node 信息
                assetTransNodes = []
                if os.path.exists(serverTransPath + 'transNodes.txt'):
                    assetTransNodesTemp = sk_infoConfig.sk_infoConfig().checkFileRead(serverTransPath + 'transNodes.txt')
                    for info in assetTransNodesTemp:
                        if info[:6] == '[food]':
                            #assetTransNodes.append( float(info[7:]) )
                            assetTransNodes.append(info)
                        else:
                            assetTransNodes.append(ns + ':' + info)
                assetTransMeshes = []
                # 处理assetTransMeshesTemp,恢复namespace
                if assetTransMeshesTemp:
                    for lineInfo in assetTransMeshesTemp:
                        needInfo = []
                        if ', ' not in lineInfo:
                            tempInfo = ns + ':' + str(lineInfo[3:-2])
                            needInfo.append(tempInfo)
                        else:
                            allInfos = lineInfo.split(', ')
                            for j in range(len(allInfos)):
                                tempInfo = ''
                                if j == 0 or j == (len(allInfos) - 1):
                                    if j == 0:
                                        tempInfo = ns + ':' + allInfos[j][3:-1]
                                    else:
                                        tempInfo = ns + ':' + allInfos[j][2:-2]
                                else:
                                    tempInfo = ns + ':' + allInfos[j][2:-1]
                                needInfo.append(tempInfo)
                        assetTransMeshes.append(needInfo)

                # 记录信息
                transpancySGNodesAll = transpancySGNodesAll + assetTransSGNodes
                transpancyMeshesAll = transpancyMeshesAll + assetTransMeshes
                transpancyNodesAll = transpancyNodesAll + assetTransNodes

        result = []
        result.append(transpancySGNodesAll)
        result.append(transpancyMeshesAll)
        result.append(transpancyNodesAll)
        return result

    # 获取有置换贴图的物体
    def zmRLDisplacementObjsOld(self):
        displacementSG = []

        # 获取file节点
        SGNodes = mc.ls(type='shadingEngine')
        for SGNode in SGNodes:
            # 判断SG节点是否有置换连接
            displacementCheck = 0
            checkDisNo1 = mc.listConnections((SGNode + '.displacementShader'), s=1)
            if checkDisNo1:
                displacementCheck = 1
            if mc.objExists(SGNode + '.miDisplacementShader'):
                checkDisNo2 = mc.listConnections((SGNode + '.miDisplacementShader'), s=1)
                if checkDisNo2:
                    displacementCheck = 2
            if displacementCheck:
                needDisplacementSG = SGNode
                needDisplacementMeshes = mc.sets(SGNode, q=1)
                if displacementCheck == 1:
                    needDisplacementShader = mc.listConnections((SGNode + '.displacementShader'), s=1)[0]
                if displacementCheck == 2:
                    needDisplacementShader = mc.listConnections((SGNode + '.miDisplacementShader'), s=1)[0]
                displacementSG.append([needDisplacementSG, needDisplacementMeshes, needDisplacementShader])

        return displacementSG

    # 获取有置换贴图的物体,通过参考获取服务器端数据
    # refNamespaceMode 0 Ref Mode | 1 Namespace Mode
    def zmRLDisplacementObjs(self, refNamespaceMode=1):
        from idmt.maya.py_common import sk_referenceConfig
        reload(sk_referenceConfig)
        from idmt.maya.py_common import sk_infoConfig
        reload(sk_infoConfig)
        import os

        allAssetInfo = []
        allAssetNsInfo = []

        displacementSGNodesAll = []
        displacementMeshesAll = []
        displacementNodesAll = []

        # refInfo
        if refNamespaceMode == 0:
            refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
            refNodes = refInfos[0][0]
            refPaths = refInfos[1][0]
            refns = refInfos[2][0]

            if refNodes:
                allAssetInfo = []
                for i in range(len(refNodes)):
                    # 非cam
                    if '_' in refNodes[i]:
                        assetFileName = refPaths[i].split('/')[-1]
                        assetInfo = assetFileName.split('_')
                        assetInfoNeed = assetInfo[0] + '_' + assetInfo[1] + '_' + assetInfo[2]
                        allAssetInfo.append(assetInfoNeed)
                        allAssetNsInfo.append(refns[i])

        # Namespace Mode
        if refNamespaceMode == 1:
            nsList = mc.namespaceInfo(listOnlyNamespaces=1)
            if 'UI' in nsList:
                nsList.remove('UI')
            if 'shared' in nsList:
                nsList.remove('shared')
            if nsList:
                for i in range(len(nsList)):
                    ns = nsList[i]
                    # 只要一级namespace
                    if '_' in ns and ":" not in ns:
                        assetInfo = ns.split('_')
                        if len(assetInfo) == 2:
                            assetInfoNeed = assetInfo[0] + '_' + assetInfo[1] + '_h'
                        if len(assetInfo) > 2:
                            assetInfoNeed = assetInfo[0] + '_' + assetInfo[1] + '_' + assetInfo[2]
                        allAssetInfo.append(assetInfoNeed)
                        allAssetNsInfo.append(ns)

        # print allAssetInfo
        # print allAssetNsInfo

        if allAssetInfo:
            # 获得asset的trans信息
            serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
            for asset in allAssetInfo:
                id = allAssetInfo.index(asset)
                assetInfo = asset.split('_')
                ns = allAssetNsInfo[id]
                serverTransPath = serverPath + 'data/AssetInfos/displacementShaderInfo/' + assetInfo[0] + '/' + str(assetInfo[1]) + '/' + str(assetInfo[2]) + '/'
                # print serverTransPath
                # asset SG 信息
                assetTransSGNodes = []
                if os.path.exists(serverTransPath + 'displacementSGNodes.txt'):
                    assetTransSGNodesTemp = sk_infoConfig.sk_infoConfig().checkFileRead(serverTransPath + 'displacementSGNodes.txt')
                    for info in assetTransSGNodesTemp:
                        assetTransSGNodes.append(ns + ':' + info)
                # asset Mesh 信息
                assetTransMeshesTemp = []
                if os.path.exists(serverTransPath + 'displacementMeshes.txt'):
                    assetTransMeshesTemp = sk_infoConfig.sk_infoConfig().checkFileRead(serverTransPath + 'displacementMeshes.txt')
                # asset Shader Node 信息
                assetTransNodes = []
                if os.path.exists(serverTransPath + 'displacementNodes.txt'):
                    assetTransNodesTemp = sk_infoConfig.sk_infoConfig().checkFileRead(serverTransPath + 'displacementNodes.txt')
                    for info in assetTransNodesTemp:
                        assetTransNodes.append(ns + ':' + info)
                assetTransMeshes = []
                # 处理assetTransMeshesTemp,恢复namespace
                if assetTransMeshesTemp:
                    for lineInfo in assetTransMeshesTemp:
                        needInfo = []
                        if ', ' not in lineInfo:
                            tempInfo = ns + ':' + str(lineInfo[3:-2])
                            needInfo.append(tempInfo)
                        else:
                            allInfos = lineInfo.split(', ')
                            for j in range(len(allInfos)):
                                tempInfo = ''
                                if j == 0 or j == (len(allInfos) - 1):
                                    if j == 0:
                                        tempInfo = ns + ':' + allInfos[j][3:-1]
                                    else:
                                        tempInfo = ns + ':' + allInfos[j][2:-2]
                                else:
                                    tempInfo = ns + ':' + allInfos[j][2:-1]
                                needInfo.append(tempInfo)
                        assetTransMeshes.append(needInfo)

                # 记录信息
                displacementSGNodesAll = displacementSGNodesAll + assetTransSGNodes
                displacementMeshesAll = displacementMeshesAll + assetTransMeshes
                displacementNodesAll = displacementNodesAll + assetTransNodes

        result = []
        result.append(displacementSGNodesAll)
        result.append(displacementMeshesAll)
        result.append(displacementNodesAll)
        return result

    # WCO和DCO分辨
    # wdType 0    dark | 1    white
    def zmRLWDColorcheck(self, objs, wdType):
        # Shader记录
        whiteColorShader = ''
        darkColorShader = ''
        # 获取mesh的SG节点
        SGNodes = []
        if objs:
            for obj in objs:
                mesh = mc.listRelatives(obj, s=1, ni=1, f=1)
                if mesh:
                    mesh = mesh[0]
                    shaderSG = mc.listConnections(mesh, d=1, type='shadingEngine')
                    if shaderSG:
                        SGNodes = SGNodes + shaderSG
        if SGNodes:
            SGNodes = list(set(SGNodes))
            # 获取WCO和DCO
            for node in SGNodes:
                # 获取colorShader
                colorShader = mc.listConnections((node + '.surfaceShader'), s=1)
                if colorShader:
                    colorShader = colorShader[0]
                    # print u'------'
                    # print colorShader
                    # 获取colorRamp
                    colorNode = mc.listConnections((colorShader + '.color'), s=1)
                    if colorNode:
                        if mc.nodeType(colorNode[0]) in ['ramp', 'condition']:
                            if mc.nodeType(colorNode[0]) == 'ramp':
                                rampShader = colorNode[0]
                                # ramp节点引入点
                                rampInputs = mc.getAttr((rampShader + '.colorEntryList'), mi=1)
                                if rampInputs:
                                    needRampInputs = rampInputs[:]
                                    if len(needRampInputs) >= 2:
                                        # print '----'
                                        # print needRampInputs
                                        self.zmWDRampConfig(rampShader, needRampInputs, colorShader, wdType)
                                    else:
                                        mc.error(u'==============[%s]do not have 2 or more inputs' % rampShader)
                            if mc.nodeType(colorNode[0]) == 'condition':
                                conditionNode = colorNode[0]
                                rampShaders = mc.listConnections(conditionNode, s=1, type='ramp')
                                if rampShaders:
                                    for rampShader in rampShaders:
                                        # ramp节点引入点
                                        rampInputs = mc.getAttr((rampShader + '.colorEntryList'), mi=1)
                                        if rampInputs:
                                            needRampInputs = rampInputs[:]
                                            if len(needRampInputs) >= 2:
                                                # 获取ramp连接的属性
                                                self.zmWDRampConfig(rampShader, needRampInputs, conditionNode, wdType)

    def zmWDRampConfig(self, rampShader, needRampInputs, colorShader, wdType):
        inputValue = []
        for rampEntryList in needRampInputs:
            inputValue.append(mc.getAttr(rampShader + '.colorEntryList[' + str(rampEntryList) + '].position'))
        # 比较大小，第一大为wco,第二大为bco
        tempNeedRampInputs = needRampInputs[:]
        tempInputValue = inputValue[:]
        # wco
        valueMax = max(tempInputValue)
        indexMax = tempInputValue.index(valueMax)
        wColorInput = rampShader + '.colorEntryList[' + str(tempNeedRampInputs[indexMax]) + ']'
        # attr
        colorShaderAttr = '.color'
        if mc.nodeType(colorShader) == 'condition':
            colorShaderAttr = '.colorIfTrue'
        if len(needRampInputs) == 3:
            # mco
            tempInputValue.remove(valueMax)
            tempNeedRampInputs.remove(tempNeedRampInputs[indexMax])
            valueMax = max(tempInputValue)
            indexMax = tempInputValue.index(valueMax)
            mColorInput = rampShader + '.colorEntryList[' + str(tempNeedRampInputs[indexMax]) + ']'
            # bco
            tempInputValue.remove(valueMax)
            tempNeedRampInputs.remove(tempNeedRampInputs[indexMax])
            valueMin = min(tempInputValue)
            indexMin = tempInputValue.index(valueMin)
            dColorInput = rampShader + '.colorEntryList[' + str(tempNeedRampInputs[indexMin]) + ']'
            # shader
            if wColorInput and mColorInput and dColorInput:
                whiteColorShader = mc.listConnections((wColorInput + '.color'), s=1, p=1)
                middleColorShader = mc.listConnections((mColorInput + '.color'), s=1, p=1)
                darkColorShader = mc.listConnections((dColorInput + '.color'), s=1, p=1)
                if whiteColorShader and middleColorShader and darkColorShader:
                    whiteColorShader = whiteColorShader[0]
                    middleColorShader = middleColorShader[0]
                    darkColorShader = darkColorShader[0]
                    # 开始处理层材质
                    mc.editRenderLayerAdjustment(colorShader + colorShaderAttr)
                    if wdType == 0:
                        mc.connectAttr(darkColorShader, (colorShader + colorShaderAttr), f=1)
                    # 只与第二条连接
                    if wdType == 1:
                        mc.connectAttr(middleColorShader, (colorShader + colorShaderAttr), f=1)

        else:
            # bco
            tempInputValue.remove(valueMax)
            tempNeedRampInputs.remove(tempNeedRampInputs[indexMax])
            valueMin = min(tempInputValue)
            indexMin = tempInputValue.index(valueMin)
            dColorInput = rampShader + '.colorEntryList[' + str(tempNeedRampInputs[indexMin]) + ']'
            # 获取
            if wColorInput and dColorInput:
                whiteColorShader = mc.listConnections((wColorInput + '.color'), s=1, p=1)
                darkColorShader = mc.listConnections((dColorInput + '.color'), s=1, p=1)
                if whiteColorShader and darkColorShader:
                    whiteColorShader = whiteColorShader[0]
                    darkColorShader = darkColorShader[0]
                    # 开始处理层材质
                    # print u'------'
                    # print colorShader
                    mc.editRenderLayerAdjustment(colorShader + colorShaderAttr)
                    if wdType == 0:
                        mc.connectAttr(darkColorShader, (colorShader + colorShaderAttr), f=1)
                    if wdType == 1:
                        mc.connectAttr(whiteColorShader, (colorShader + colorShaderAttr), f=1)

    # w,d属性export
    def zmRLWDInfoExport(self):
        from idmt.maya.py_common import sk_checkCommon
        reload(sk_checkCommon)
        # Shader记录
        wdColorRamp = []
        wdColorRampPosition = []
        wdColorRampMeshes = []
        objs = sk_checkCommon.sk_checkTools().checkCacheSetObjects()
        # 获取mesh的SG节点
        if objs:
            SGNodes = []
            for obj in objs:
                mesh = mc.listRelatives(obj, s=1, ni=1, f=1)
                if mesh:
                    mesh = mesh[0]
                    shaderSG = mc.listConnections(mesh, d=1, type='shadingEngine')
                    if shaderSG:
                        SGNodes = SGNodes + shaderSG
        # 获取mesh的SG节点
        SGNodes = mc.ls(type='shadingEngine')
        if SGNodes:
            SGNodes = list(set(SGNodes))
            # 获取WCO和DCO
            for node in SGNodes:
                if 'zm_s' in node:
                    continue
                # 获取colorShader
                colorShader = mc.listConnections((node + '.surfaceShader'), s=1)
                if colorShader:
                    colorShader = colorShader[0]
                    # 获取colorRamp
                    rampShader = ''
                    if mc.objExists((colorShader + '.color')):
                        rampShader = mc.listConnections((colorShader + '.color'), s=1)
                    if rampShader:
                        rampShader = rampShader[0]
                        # ramp节点引入点
                        rampInputs = ''
                        if mc.objExists(rampShader + '.colorEntryList'):
                            rampInputs = mc.getAttr((rampShader + '.colorEntryList'), mi=1)
                        if rampInputs:
                            needRampInputs = rampInputs[:]
                            if len(needRampInputs) >= 2:
                                # 获取输入点位置信息
                                inputValue = []
                                for rampEntryList in needRampInputs:
                                    inputValue.append(mc.getAttr(rampShader + '.colorEntryList[' + str(rampEntryList) + '].position'))
                                # 比较大小，第一大为wco,第二大为bco
                                tempNeedRampInputs = needRampInputs[:]
                                tempInputValue = inputValue[:]
                                # wco
                                valueMax = max(tempInputValue)
                                indexMax = tempInputValue.index(valueMax)
                                wColorInput = rampShader + '.colorEntryList[' + str(tempNeedRampInputs[indexMax]) + ']'
                                wPosition = mc.getAttr(wColorInput + '.position')
                                if len(needRampInputs) == 3:
                                    # mco
                                    tempInputValue.remove(valueMax)
                                    tempNeedRampInputs.remove(tempNeedRampInputs[indexMax])
                                    valueMax = max(tempInputValue)
                                    indexMax = tempInputValue.index(valueMax)
                                    mColorInput = rampShader + '.colorEntryList[' + str(tempNeedRampInputs[indexMax]) + ']'
                                    mPosition = mc.getAttr(mColorInput + '.position')
                                    # bco
                                    tempInputValue.remove(valueMax)
                                    tempNeedRampInputs.remove(tempNeedRampInputs[indexMax])
                                    valueMin = min(tempInputValue)
                                    indexMin = tempInputValue.index(valueMin)
                                    dColorInput = rampShader + '.colorEntryList[' + str(tempNeedRampInputs[indexMin]) + ']'
                                    dPosition = mc.getAttr(dColorInput + '.position')
                                else:
                                    # bco
                                    tempInputValue.remove(valueMax)
                                    tempNeedRampInputs.remove(tempNeedRampInputs[indexMax])
                                    valueMin = min(tempInputValue)
                                    indexMin = tempInputValue.index(valueMin)
                                    dColorInput = rampShader + '.colorEntryList[' + str(tempNeedRampInputs[indexMin]) + ']'
                                    dPosition = mc.getAttr(dColorInput + '.position')

                                # record
                                wdColorRamp.append((rampShader + '>_<' + node))
                                wdColorRampPosition.append([wPosition, dPosition])
                                wdColorRampMeshes.append(mc.sets(node, q=1))

        # 输出信息
        from idmt.maya.py_common import sk_infoConfig
        reload(sk_infoConfig)

        # 本地及服务器端路径
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        localPath = sk_infoConfig.sk_infoConfig().checkLocalInfoPath()
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        localTransPath = localPath + 'wdRampInfo/' + shotInfo[0] + '/' + str(shotInfo[1]) + '/' + str(shotInfo[2]) + '/'
        mc.sysFile(localTransPath, makeDir=1)
        serverTransPath = serverPath + 'data/AssetInfos/wdRampInfo/' + shotInfo[0] + '/' + str(shotInfo[1]) + '/' + str(shotInfo[2]) + '/'
        makeDirCMD = 'zwSysFile(\"MD\",\"' + serverTransPath + '\",\"\",1)'
        mel.eval(makeDirCMD)

        # 本地输出及更新
        sk_infoConfig.sk_infoConfig().checkFileWrite((localTransPath + 'wdRampNodes.txt'), wdColorRamp)
        updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localTransPath + 'wdRampNodes.txt') + '"' + ' ' + '"' + (serverTransPath + 'wdRampNodes.txt') + '"' + ' true'
        mel.eval(updateAnimCMD)
        sk_infoConfig.sk_infoConfig().checkFileWrite((localTransPath + 'wdRampPosition.txt'), wdColorRampPosition)
        updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localTransPath + 'wdRampPosition.txt') + '"' + ' ' + '"' + (serverTransPath + 'wdRampPosition.txt') + '"' + ' true'
        mel.eval(updateAnimCMD)
        sk_infoConfig.sk_infoConfig().checkFileWrite((localTransPath + 'wdRampMeshes.txt'), wdColorRampMeshes)
        updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localTransPath + 'wdRampMeshes.txt') + '"' + ' ' + '"' + (serverTransPath + 'wdRampMeshes.txt') + '"' + ' true'
        mel.eval(updateAnimCMD)

    # 获取有rampInfo的物体,通过参考获取服务器端数据
    # refNamespaceMode 0 Ref Mode | 1 Namespace Mode
    def zmRLWDInfoObjs(self, refNamespaceMode=1):
        from idmt.maya.py_common import sk_referenceConfig
        reload(sk_referenceConfig)
        from idmt.maya.py_common import sk_infoConfig
        reload(sk_infoConfig)
        import os

        allAssetInfo = []
        allAssetNsInfo = []

        assetRampNodesAll = []
        assetRampMeshesAll = []
        assetRampPositionAll = []

        # refInfo
        if refNamespaceMode == 0:
            refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
            refNodes = refInfos[0][0]
            refPaths = refInfos[1][0]
            refns = refInfos[2][0]

            if refNodes:
                allAssetInfo = []
                for i in range(len(refNodes)):
                    # 非cam
                    if '_' in refNodes[i]:
                        assetFileName = refPaths[i].split('/')[-1]
                        assetInfo = assetFileName.split('_')
                        assetInfoNeed = assetInfo[0] + '_' + assetInfo[1] + '_' + assetInfo[2]
                        allAssetInfo.append(assetInfoNeed)
                        allAssetNsInfo.append(refns[i])

        # Namespace Mode
        if refNamespaceMode == 1:
            nsList = mc.namespaceInfo(listOnlyNamespaces=1)
            if 'UI' in nsList:
                nsList.remove('UI')
            if 'shared' in nsList:
                nsList.remove('shared')
            if nsList:
                for i in range(len(nsList)):
                    ns = nsList[i]
                    # 只要一级namespace
                    if '_' in ns and ":" not in ns:
                        assetInfo = ns.split('_')
                        if len(assetInfo) == 2:
                            assetInfoNeed = assetInfo[0] + '_' + assetInfo[1] + '_h'
                        if len(assetInfo) > 2:
                            assetInfoNeed = assetInfo[0] + '_' + assetInfo[1] + '_' + assetInfo[2]
                        allAssetInfo.append(assetInfoNeed)
                        allAssetNsInfo.append(ns)

        # print allAssetInfo
        # print allAssetNsInfo

        if allAssetInfo:
            # 获得asset的trans信息
            serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
            for asset in allAssetInfo:
                id = allAssetInfo.index(asset)
                assetInfo = asset.split('_')
                ns = allAssetNsInfo[id]
                serverTransPath = serverPath + 'data/AssetInfos/wdRampInfo/' + assetInfo[0] + '/' + str(assetInfo[1]) + '/' + str(assetInfo[2]) + '/'
                # print serverTransPath
                # asset RampNode 信息
                assetRampNodes = []
                if os.path.exists(serverTransPath + 'wdRampNodes.txt'):
                    assetRampNodesTemp = sk_infoConfig.sk_infoConfig().checkFileRead(serverTransPath + 'wdRampNodes.txt')
                    for info in assetRampNodesTemp:
                        assetRampNodes.append(ns + ':' + info)
                # asset Mesh 信息
                assetRampMeshesTemp = []
                if os.path.exists(serverTransPath + 'wdRampMeshes.txt'):
                    assetRampMeshesTemp = sk_infoConfig.sk_infoConfig().checkFileRead(serverTransPath + 'wdRampMeshes.txt')
                # asset RampPosition 信息
                assetRampPositionTemp = []
                if os.path.exists(serverTransPath + 'wdRampPosition.txt'):
                    assetRampPositionTemp = sk_infoConfig.sk_infoConfig().checkFileRead(serverTransPath + 'wdRampPosition.txt')
                # 恢复为数组数据
                assetRampMeshes = []
                # 处理assetTransMeshesTemp,恢复namespace
                if assetRampMeshesTemp:
                    for lineInfo in assetRampMeshesTemp:
                        needInfo = []
                        if ', ' not in lineInfo:
                            tempInfo = ns + ':' + str(lineInfo[3:-2])
                            needInfo.append(tempInfo)
                        else:
                            allInfos = lineInfo.split(', ')
                            for j in range(len(allInfos)):
                                tempInfo = ''
                                if j == 0 or j == (len(allInfos) - 1):
                                    if j == 0:
                                        tempInfo = ns + ':' + allInfos[j][3:-1]
                                    else:
                                        tempInfo = ns + ':' + allInfos[j][2:-2]
                                else:
                                    tempInfo = ns + ':' + allInfos[j][2:-1]
                                needInfo.append(tempInfo)
                        assetRampMeshes.append(needInfo)
                # 恢复为数组数据
                assetRampPosition = []
                if assetRampPositionTemp:
                    for lineInfo in assetRampPositionTemp:
                        allInfos = lineInfo.split(', ')
                        needList = []
                        needList.append(float(allInfos[0][1:]))
                        needList.append(float(allInfos[1][:-2]))
                        assetRampPosition.append(needList)

                # 记录信息
                assetRampNodesAll = assetRampNodesAll + assetRampNodes
                assetRampMeshesAll = assetRampMeshesAll + assetRampMeshes
                assetRampPositionAll = assetRampPositionAll + assetRampPosition

        result = []
        result.append(assetRampNodesAll)
        result.append(assetRampMeshesAll)
        result.append(assetRampPositionAll)
        return result

    # 断开所有SG节点的连接
    def zmRLSGNodesDisConnections(self):

        objs = self.zmRLObjectsTList()
        refCHR = objs[0]
        refPROP = objs[1]
        refSET = objs[2]
        refSKY = objs[3]
        refSEA = objs[4]

        sgNodes = mc.ls(type='shadingEngine')

        nodeSG = []
        SGNode = ''
        SGNodes = []
        if mc.ls('*:*SEA', type='objectSet'):
            if mc.ls('*:*MSH_c_hi_temp_sea_MSK_', type='transform'):
                obj = mc.ls('*:*MSH_c_hi_temp_sea_MSK_', type='transform')
                objMESH = mc.listRelatives(obj, ad=1, ni=1, type='mesh', f=1)
                SGNodes = mc.listConnections(objMESH, type='shadingEngine', d=1)
                if SGNodes:
                    SGNode = SGNodes[0]

        objSG = ''
        objSGs = []
        if mc.ls('*:*SEA', type='objectSet'):
            if mc.ls('*:*MSH_c_hi_temp_sea_CO_', type='transform'):
                obj = mc.ls('*:*MSH_c_hi_temp_sea_CO_', type='transform')
                objMESH = mc.listRelatives(obj, ad=1, ni=1, type='mesh', f=1)
                objSGs = mc.listConnections(objMESH, type='shadingEngine', d=1)
                if objSGs:
                    objSG = objSGs[0]

        if sgNodes:
            for sg in sgNodes:
                if (SGNode not in sg)and (objSG not in sg):
                    nodeSG.append(sg)
        sgNodes = nodeSG

        if sgNodes:
            for sgNode in sgNodes:
                if sgNode == "initialShadingGroup":
                    continue
                if sgNode == "initialParticleSE":
                    continue
                # 获取dagSetMembers连接信息,返回列表必定为2的倍数
                buf = mc.listConnections((sgNode + '.dagSetMembers'), connections=1, plugs=1)
                if buf:
                    for i in range(len(buf) / 2):
                        shape = buf[i + 1].split('.')[0]
                        if mc.nodeType(shape) != 'renderLayer':
                            try:
                                mc.disconnectAttr(buf[i + 1], buf[i])
                            except:
                                pass
                # 获取memberWireframeColor连接信息,返回列表必定为2的倍数
                buf = mc.listConnections((sgNode + '.memberWireframeColor'), connections=1, plugs=1)
                if buf:
                    for i in range(len(buf) / 2):
                        shape = buf[i + 1].split('.')[0]
                        if mc.nodeType(shape) != 'renderLayer':
                            try:
                                mc.disconnectAttr(buf[i + 1], buf[i])
                            except:
                                pass

    # 透明属性连接
    def zmRLTransShaderConnectiion(self, transpancyNode, transShader, transShaderAttr):
        if transpancyNode[:6] == '[food]':
            transValue = float(transpancyNode[7:])
            try:
                transpancyConnections = mc.listConnections((transShader + '.' + transShaderAttr), s=1, plugs=1)
                mc.disconnectAttr(('%s') % (transpancyConnections[0]), ('%s.%s') % (transShader, transShaderAttr))
            except:
                pass
            mc.setAttr((transShader + '.' + transShaderAttr), transValue, transValue, transValue, type='double3')
        else:
            print transpancyNode
            if mc.nodeType(transpancyNode.split('.')[0]) in['layeredShader', 'surfaceShader', 'ramp', 'file', 'reverse']:
                if mc.nodeType(transpancyNode.split('.')[0]) in ['layeredShader', 'surfaceShader']:
                    try:
                        mc.disconnectAttr(('%s.%s') % (transpancyNode.split('.')[0], transShaderAttr), ('%s.%s') % (transShader, transShaderAttr))
                    except:
                        pass
                    mc.connectAttr(('%s.%s') % (transpancyNode.split('.')[0], transShaderAttr), ('%s.%s') % (transShader, transShaderAttr), f=True)
                if mc.nodeType(transpancyNode.split('.')[0]) in ['ramp', 'file']:
                    try:
                        mc.disconnectAttr(('%s.%s') % (transpancyNode.split('.')[0], 'outColor'), ('%s.%s') % (transShader, transShaderAttr))
                    except:
                        pass
                    mc.connectAttr(('%s.%s') % (transpancyNode.split('.')[0], 'outColor'), ('%s.%s') % (transShader, transShaderAttr), f=True)
                if mc.nodeType(transpancyNode.split('.')[0]) in ['reverse', ]:
                    try:
                        mc.disconnectAttr(('%s.%s') % (transpancyNode.split('.')[0], 'output'), ('%s.%s') % (transShader, transShaderAttr))
                    except:
                        pass
                    mc.connectAttr(('%s.%s') % (transpancyNode.split('.')[0], 'output'), ('%s.%s') % (transShader, transShaderAttr), f=True)
            else:
                try:
                    mc.disconnectAttr(('%s.%s') % (transpancyNode.split('.')[0], 'outAlpha'), ('%s.%s') % (transShader, transShaderAttr))
                except:
                    pass
                mc.connectAttr(('%s.%s') % (transpancyNode.split('.')[0], 'outAlpha'), ('%s.%s') % (transShader, transShaderAttr), f=True)

    # 非CO之类的层，主层给个临时材质球，避免材质出错
    def zmRLMasterCleanCreate(self, layerType='', selectObjType=0):
        print (u'===============!!!Start 【%s】!!!===============' % (u'MasterTemp层'))
        print 'Working...'

        # 物体
        objs = self.zmRLObjectsTList()
        refCHR = objs[0]
        refPROP = objs[1]
        refSET = objs[2]

        rlObjs = refCHR + refPROP + refSET

        needobjs = []
        if rlObjs:
            for obj in rlObjs:
                if ('MSH_c_hi_temp_sea_MSK_' not in obj) and ('MSH_c_hi_temp_sea_CO_' not in obj):
                    needobjs.append(obj)

        rlObjs = needobjs

        layerType = 'MasterTemp'

        # 灯光
        lights = mc.ls(type='light')

        # 选取模式
        if selectObjType == 1:
            rlObjs = self.zmRLSelectMode()

        if rlObjs:

            # 断开所有SG连接
            self.zmRLSGNodesDisConnections()

            # 通用材质
            shaderNode = 'SHD_' + layerType + '_Shader'
            if mc.ls(shaderNode):
                mc.delete(shaderNode)
            shaderSG = 'SHD_' + layerType + '_SG'
            if mc.ls(shaderSG):
                mc.delete(shaderSG)
            shaderNode = mc.shadingNode('lambert', asShader=True, name=shaderNode)
            shaderSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=shaderSG)
            mc.connectAttr((shaderNode + '.outColor'), (shaderSG + '.surfaceShader'))

            # 优先全局着色
            for obj in rlObjs:
                try:
                    mc.sets(obj, e=1, forceElement=shaderSG)
                except:
                    # 获取物体面数
                    faceNum = mc.polyEvaluate(obj, face=1)
                    mc.sets((obj + u'.f[:' + str(faceNum - 1) + u']'), e=1, forceElement=shaderSG)

            print (u'===============!!!Done  【%s】!!!===============' % (u'%MasterTemp层'))
            print '\n'

    # preview层
    # No Lights

    def zmRLPVCreate(self, layerType, selectObjType=0):
        print (u'===============!!!Start 【%s】!!!===============' % (u'%s_Preview层' % layerType))
        print 'Working...'

        # 物体
        objs = self.zmRLObjectsTList()
        refCHR = objs[0]
        refPROP = objs[1]
        refSET = objs[2]
        refSKY = objs[3]
        refSEA = objs[4]

        # 灯光
        lights = mc.ls(type='light', l=1)
        lightGrps = []
        needLightGrps = []
        if lights:
            lightGrps.append(mc.listRelatives(lights, p=1, type='transform', f=1)[0])
        if lightGrps:
            if layerType == 'FG' or layerType == 'CHR':
                for grp in lightGrps:
                    if 'LGT_DAY_KEY' in grp:
                        needLightGrps.append(grp)
            if layerType == 'CHRF':
                for grp in lightGrps:
                    if 'LGT_DAY_KEY_F' in grp:
                        needLightGrps.append(grp)
            if layerType == 'CHRB':
                for grp in lightGrps:
                    if 'LGT_DAY_KEY_B' in grp:
                        needLightGrps.append(grp)

        # 物体
        rlObjs = []
        if layerType == 'ALL':
            rlObjs = refCHR + refPROP + refSET + refSKY + refSEA
            layerName = 'ALL_PREVIEW'

        # 选取模式
        if selectObjType == 1:
            rlObjs = self.zmRLSelectMode()

        if rlObjs:
            # 创建RenderLayer
            if mc.ls(layerName):
                mc.delete(layerName)

            mc.createRenderLayer((rlObjs + needLightGrps), name=layerName, noRecurse=1, makeCurrent=1)

            # 渲染设置
            mc.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')

            from idmt.maya.py_common import sk_infoConfig
            reload(sk_infoConfig)
            shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
            sceneName = shotInfo[0] + '_' + str(shotInfo[1]) + '_' + str(shotInfo[2])
            mc.editRenderLayerAdjustment('defaultRenderGlobals.imageFilePrefix')
            mc.setAttr('defaultRenderGlobals.imageFilePrefix', ('<Layer>/' + sceneName + '_lr_<Layer>_c001'), type='string')

            # 关闭光线追踪
            mc.editRenderLayerAdjustment('miDefaultOptions.rayTracing')
            mc.setAttr('miDefaultOptions.rayTracing', 0)

            # 格式命名
            mc.setAttr('defaultRenderGlobals.animation', 1)
            mc.setAttr('defaultRenderGlobals.putFrameBeforeExt', 1)
            mc.setAttr('defaultRenderGlobals.periodInExt', 1)
            mc.setAttr('defaultRenderGlobals.extensionPadding', 4)
            if mc.getAttr('defaultRenderGlobals.outFormatControl') == 1:
                mc.setAttr('defaultRenderGlobals.outFormatControl', 0)

            # 设置
            mc.editRenderLayerAdjustment('defaultResolution.width')
            mc.setAttr('defaultResolution.width', 1280)
            mc.editRenderLayerAdjustment('defaultResolution.height')
            mc.setAttr('defaultResolution.height', 720)

            # exr
            mc.editRenderLayerAdjustment('defaultRenderGlobals.imageFormat')
            mc.setAttr("defaultRenderGlobals.imageFormat", 32)

            print (u'===============!!!Done  【%s】!!!===============' % (u'%s_Preview层' % layerType))
            print '\n'

        else:
            print (u'===============!!!Error  【%s】无物体!!!===============' % (u'%s_Preview层' % layerType))
            print '\n'

 
    # FG_CO,BG_CO层
    # No Lights
    def zmRLWCOCreate(self, layerType, selectObjType=0):
        print (u'===============!!!Start 【%s】!!!===============' % (u'%s_CO层' % layerType))
        print 'Working...'

        # 物体
        objs = self.zmRLObjectsTList()
        refCHR = objs[0]
        refPROP = objs[1]
        refSET = objs[2]
        refSKY = objs[3]
        refSEA = objs[4]
        
        state=0
        icegrp=[]
        # 灯光
        specallights = []

        lights = mc.ls(type='light')
        if lights:
            for light in lights:
                if "ONLY_FG_CO" in light:
                    specallights.append(light)

        # 物体
        rlObjs = []
        if layerType == 'FG':
            rlObjs = refSET
            if refSET:
                for obj in refSET:
                    if '_sea_' in obj.lower() or '_sky_' in obj.lower():
                        rlObjs.remove(obj)
            layerName = 'FG_CO'
            
        if layerType == 'BG':
            rlObjs = refSKY
            layerName = 'BG_CO'

        # 选取模式
        if selectObjType == 1:
            rlObjs = self.zmRLSelectMode()

        if rlObjs:
            # BG,sky隐藏
            if layerType == 'FG':
                
                 # 创建RenderLayer
                if mc.ls(layerName):
                    mc.delete(layerName)
                mc.createRenderLayer(rlObjs + specallights, name=layerName, noRecurse=1, makeCurrent=1)
                if refSKY:
                    for obj in refSKY:
                        mc.editRenderLayerAdjustment(obj + '.v')
                        mc.setAttr((obj + '.v'), 0)
                
                if refSET:
                    for obj in refSET:
                        if 'Icicle' in obj:
                            state = 1
                            icegrp.append(obj)
                if state==1:                                
                    # 创建passContributionMap
                    Map = mc.createNode('passContributionMap', n='passMap')
                    mc.connectAttr((layerName + '.passContributionMap'), (Map + '.owner'), na=1)


                    if icegrp:
                        for obj in icegrp:                            
                            mc.connectAttr((obj + '.message'), (Map + '.dagObjects'), na=1)

      
                    # 创建renderPass节点   
                    cusColor = mc.shadingNode('renderPass', asRendering=1, name='customColor')
                    mc.setRenderPassType(cusColor,type='CSTCOL')
                    mc.setAttr(cusColor+'.numChannels',4)
        
                   
                    # 使renderPass节点与层和passContributionMap相连
                    mc.connectAttr((layerName + '.renderPass'), (cusColor + '.owner'), nextAvailable=1)
        
                    mc.connectAttr((cusColor + '.message'), (Map + '.renderPass'), nextAvailable=1)
        
                    #获取shader节点
                    shadergrp=[]
                    shaderGP=[]
                    if icegrp:
                        for obj in icegrp:
                            mesh=mc.listRelatives(obj, s=1, ni=1, f=1)[0] 
                            SGNode=mc.listConnections(mesh, d=1, type='shadingEngine')
                            if SGNode:
                                for SG in SGNode:                                   
                                    shaderGP = mc.listConnections((SG + '.surfaceShader'),s = 1,plugs = 1)
                                    for GP in shaderGP:
                                        shadergrp.append(GP)
                    shadergrp=list(set(shadergrp))                                                        
                    # 创建writeToColorBuffer节点
                    ColorBuffergrp=[]
                    if shadergrp:
                         for obj in shadergrp:
                             ColorBuffer = mc.shadingNode('writeToColorBuffer', asShader=1, name='colorBuffer')
                             mc.setAttr((ColorBuffer + '.color'), 0, 0, 1, type='double3')
                             mc.connectAttr((cusColor + '.message'), (ColorBuffer + '.renderPass'))
                             ColorBuffergrp.append(ColorBuffer)

                    for i in range(len(shadergrp)):                                                  
                        if mc.isConnected(shadergrp[i], (ColorBuffergrp[i] + '.evaluationPassThrough'))==0:
                            mc.connectAttr(shadergrp[i], (ColorBuffergrp[i] + '.evaluationPassThrough')) 


            # FG，只有sky:1591
            if layerType == 'BG':
                 # 创建RenderLayer
                if mc.ls(layerName):
                    mc.delete(layerName)
                mc.createRenderLayer(rlObjs, name=layerName, noRecurse=1, makeCurrent=1)
                if refSET:
                    for obj in refSET:
                        try:
                            mc.editRenderLayerAdjustment(obj + '.v')
                            mc.setAttr((obj + '.v'), 0)
                        except:
                            mc.editRenderLayerAdjustment(obj + '.lodVisibility')
                            mc.setAttr((obj + '.lodVisibility'), 0)
                if refSKY:
                    for obj in refSKY:
                        mc.editRenderLayerAdjustment(obj + '.v')
                        mc.setAttr((obj + '.v'), 1)
                        
                if mc.ls('*:*Cloud_Ctrl'):
                    if mc.getAttr(mc.ls('*:*Cloud_Ctrl')[0]+'.v')==True:
                        mc.editRenderLayerAdjustment(mc.ls('*:*Cloud_Ctrl')[0] + '.v')
                        mc.setAttr(mc.ls('*:*Cloud_Ctrl')[0]+'.v',0)
                    
                if mc.ls('*:*MSH_c_hi_Sun_'):
                    if mc.getAttr(mc.ls('*:*MSH_c_hi_Sun_')[0]+'.v')==True:
                        mc.editRenderLayerAdjustment(mc.ls('*:*MSH_c_hi_Sun_')[0] + '.v')
                        mc.setAttr(mc.ls('*:*MSH_c_hi_Sun_')[0]+'.v',0)                
                    
                if mc.ls('*:*MSH_c_hi_Sky_'):
                    if mc.getAttr(mc.ls('*:*MSH_c_hi_Sky_')[0]+'.v')==True:
                        mc.editRenderLayerAdjustment(mc.ls('*:*MSH_c_hi_Sky_')[0] + '.v')
                        mc.setAttr(mc.ls('*:*MSH_c_hi_Sky_')[0]+'.v',0) 

                if mc.ls('*:*MSH_c_hi_DomeSky_'):
                    if mc.getAttr(mc.ls('*:*MSH_c_hi_DomeSky_')[0]+'.v')==True:
                        mc.editRenderLayerAdjustment(mc.ls('*:*MSH_c_hi_DomeSky_')[0] + '.v')
                        mc.setAttr(mc.ls('*:*MSH_c_hi_DomeSky_')[0]+'.v',0) 
                                               
                if mc.ls('*:*MSH_c_hi_Cyclo_CloudsBG_'):
                    if mc.getAttr(mc.ls('*:*MSH_c_hi_Cyclo_CloudsBG_')[0]+'.v')==True:
                        mc.editRenderLayerAdjustment(mc.ls('*:*MSH_c_hi_Cyclo_CloudsBG_')[0] + '.v')
                        mc.setAttr(mc.ls('*:*MSH_c_hi_Cyclo_CloudsBG_')[0]+'.v',0)
                        
                if mc.ls('*:*MSH_c_hi_Cyclo_FarBG_'):
                    if mc.getAttr(mc.ls('*:*MSH_c_hi_Cyclo_FarBG_')[0]+'.v')==True:
                        mc.editRenderLayerAdjustment(mc.ls('*:*MSH_c_hi_Cyclo_FarBG_')[0] + '.v')
                        mc.setAttr(mc.ls('*:*MSH_c_hi_Cyclo_FarBG_')[0]+'.v',0)
                        
                if mc.ls('*:*MSH_c_hi_Cyclo_MainBG_'):
                    if mc.getAttr(mc.ls('*:*MSH_c_hi_Cyclo_MainBG_')[0]+'.v')==True:
                        mc.editRenderLayerAdjustment(mc.ls('*:*MSH_c_hi_Cyclo_MainBG_')[0] + '.v')
                        mc.setAttr(mc.ls('*:*MSH_c_hi_Cyclo_MainBG_')[0]+'.v',0)
                        
                if mc.ls('*:*MSH_c_hi_Cyclo_CloudsOL_'):
                    if mc.getAttr(mc.ls('*:*MSH_c_hi_Cyclo_CloudsOL_')[0]+'.v')==True:
                        mc.editRenderLayerAdjustment(mc.ls('*:*MSH_c_hi_Cyclo_CloudsOL_')[0] + '.v')
                        mc.setAttr(mc.ls('*:*MSH_c_hi_Cyclo_CloudsOL_')[0]+'.v',0)                                                                        
                        
                if mc.ls('*:*MSH_c_hi_Cyclo_PalmTrees_'):
                    if mc.getAttr(mc.ls('*:*MSH_c_hi_Cyclo_PalmTrees_')[0]+'.v')==True:
                        mc.editRenderLayerAdjustment(mc.ls('*:*MSH_c_hi_Cyclo_PalmTrees_')[0] + '.v')
                        mc.setAttr(mc.ls('*:*MSH_c_hi_Cyclo_PalmTrees_')[0]+'.v',0) 
                        
                if mc.ls('*:*MSH_c_hi_Cyclo_CloseBG_'):
                    if mc.getAttr(mc.ls('*:*MSH_c_hi_Cyclo_CloseBG_')[0]+'.v')==True:
                        mc.editRenderLayerAdjustment(mc.ls('*:*MSH_c_hi_Cyclo_CloseBG_')[0] + '.v')
                        mc.setAttr(mc.ls('*:*MSH_c_hi_Cyclo_CloseBG_')[0]+'.v',0)    
                        
                if mc.ls('*:*MSH_c_hi_CloudsBG_'):
                    if mc.getAttr(mc.ls('*:*MSH_c_hi_CloudsBG_')[0]+'.v')==True:
                        mc.editRenderLayerAdjustment(mc.ls('*:*MSH_c_hi_CloudsBG_')[0] + '.v')
                        mc.setAttr(mc.ls('*:*MSH_c_hi_CloudsBG_')[0]+'.v',0) 
                        
                if mc.ls('*:*MSH_c_hi_FarBG_'):
                    if mc.getAttr(mc.ls('*:*MSH_c_hi_FarBG_')[0]+'.v')==True:
                        mc.editRenderLayerAdjustment(mc.ls('*:*MSH_c_hi_FarBG_')[0] + '.v')
                        mc.setAttr(mc.ls('*:*MSH_c_hi_FarBG_')[0]+'.v',0)                                                                                                                                         

                if mc.ls('*:*MSH_c_hi_MainBG_'):
                    if mc.getAttr(mc.ls('*:*MSH_c_hi_MainBG_')[0]+'.v')==True:
                        mc.editRenderLayerAdjustment(mc.ls('*:*MSH_c_hi_MainBG_')[0] + '.v')
                        mc.setAttr(mc.ls('*:*MSH_c_hi_MainBG_')[0]+'.v',0) 

                if mc.ls('*:*MSH_c_hi_CloudsOL_'):
                    if mc.getAttr(mc.ls('*:*MSH_c_hi_CloudsOL_')[0]+'.v')==True:
                        mc.editRenderLayerAdjustment(mc.ls('*:*MSH_c_hi_CloudsOL_')[0] + '.v')
                        mc.setAttr(mc.ls('*:*MSH_c_hi_CloudsOL_')[0]+'.v',0) 
                        
                if mc.ls('*:*MSH_c_hi_CloseBG_'):
                    if mc.getAttr(mc.ls('*:*MSH_c_hi_CloseBG_')[0]+'.v')==True:
                        mc.editRenderLayerAdjustment(mc.ls('*:*MSH_c_hi_CloseBG_')[0] + '.v')
                        mc.setAttr(mc.ls('*:*MSH_c_hi_CloseBG_')[0]+'.v',0) 
                        
                if mc.ls('*:*MSH_c_hi_PalmTrees_'):
                    if mc.getAttr(mc.ls('*:*MSH_c_hi_PalmTrees_')[0]+'.v')==True:
                        mc.editRenderLayerAdjustment(mc.ls('*:*MSH_c_hi_PalmTrees_')[0] + '.v')
                        mc.setAttr(mc.ls('*:*MSH_c_hi_PalmTrees_')[0]+'.v',0) 

                if mc.ls('*:*MSH_c_hi_Cyclo_Clouds1_'):
                   if mc.getAttr(mc.ls('*:*MSH_c_hi_Cyclo_Clouds1_')[0]+'.v')==True:
                       mc.editRenderLayerAdjustment(mc.ls('*:*MSH_c_hi_Cyclo_Clouds1_')[0] + '.v')
                       mc.setAttr(mc.ls('*:*MSH_c_hi_Cyclo_Clouds1_')[0]+'.v',0)                       
                        
                                                                                                                                          
                from idmt.maya.py_common import sk_infoConfig
                reload(sk_infoConfig)
                shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
                camName = 'CAM:cam_' + str(shotInfo[1]) + '_' + str(shotInfo[2]) + '_baked'
                if mc.ls(camName):
                    mc.editRenderLayerAdjustment(camName + '.farClipPlane')
                    mc.setAttr((camName + '.farClipPlane'), 1000000)


            # 渲染设置
            mc.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')

            # 关闭光线追踪
            mc.editRenderLayerAdjustment('miDefaultOptions.rayTracing')
            mc.setAttr('miDefaultOptions.rayTracing', 0)

            # 格式命名
            mc.setAttr('defaultRenderGlobals.animation', 1)
            mc.setAttr('defaultRenderGlobals.putFrameBeforeExt', 1)
            mc.setAttr('defaultRenderGlobals.periodInExt', 1)
            mc.setAttr('defaultRenderGlobals.extensionPadding', 4)
            if mc.getAttr('defaultRenderGlobals.outFormatControl') == 1:
                mc.setAttr('defaultRenderGlobals.outFormatControl', 0)

            # exr
            mc.editRenderLayerAdjustment('defaultRenderGlobals.imageFormat')
            mc.setAttr('defaultRenderGlobals.imageFormat', 51)
            mc.setAttr('defaultRenderGlobals.imfkey', 'exr', type='string')
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.setAttr('mentalrayGlobals.compressionQuality', 0)

            # 16位zip压缩
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.editRenderLayerAdjustment('miDefaultFramebuffer.datatype')
            mc.setAttr('miDefaultFramebuffer.datatype', 16)

            print (u'===============!!!Done  【%s】!!!===============' % (u'%s_CO层' % layerType))
            print '\n'

        else:
            print (u'===============!!!Error  【%s】无物体!!!===============' % (u'%s_CO层' % layerType))
            print '\n'

 
    # ALL_NM层
    # No Lights
    # 放弃与AO类似部分，直接amb_occ连shader的color，trans连shader的trans
    def zmRLNMCreate(self, layerType, selectObjType=0):
        print (u'===============!!!Start 【%s】!!!===============' % (u'%s_NM层' % layerType))
        print 'Working...'

        # 物体
        objs = self.zmRLObjectsTList()
        refCHR = objs[0]
        refPROP = objs[1]
        refSET = objs[2]
        refSEA = objs[4]


        if layerType == 'ALL':
            rlObjs = refCHR + refPROP + refSET
            layerName = 'ALL_NM'

        # 灯光
        lights = mc.ls(type='light')

        # 选取模式
        if selectObjType == 1:
            rlObjs = self.zmRLSelectMode()

        if rlObjs:

            # 特殊处理，半透明用
            # 获取信息必须在masterLayer进行
            transpancyObjs = self.zmRLTransparencyObjs()
            transpancySGNodes = transpancyObjs[0]
            transpancyMeshes = transpancyObjs[1]
            transpancyNode = transpancyObjs[2]

            # 创建RenderLayer
            if mc.ls(layerName):
                mc.delete(layerName)

            mc.createRenderLayer(rlObjs, name=layerName, noRecurse=1, makeCurrent=1)
            
            if refSEA:
                for obj in refSEA:
                    mesh = mc.listRelatives(obj, ni=1, type='mesh', s=1, f=1)[0]
                    mc.editRenderLayerAdjustment(mesh + '.v')
                    mc.setAttr((mesh + '.v'), 0)

            # 通用AO材质
            shaderNode = 'SHD_' + layerType + '_NM_Shader'
            if mc.ls(shaderNode):
                mc.delete(shaderNode)
            NMNode = 'SHD_' + layerType + '_NM_Node'
            if mc.ls(NMNode):
                mc.delete(NMNode)
            NMSG = 'SHD_' + layerType + '_NM_SG'
            if mc.ls(NMSG):
                mc.delete(NMSG)
            shaderNode = mc.shadingNode('surfaceShader', asShader=True, name=shaderNode)
            NMNode = mc.shadingNode('mib_amb_occlusion', asTexture=True, name=NMNode)
            NMSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=NMSG)
            mc.connectAttr((shaderNode + '.outColor'), (NMSG + '.surfaceShader'))
            mc.connectAttr((NMNode + '.outValue'), (shaderNode + '.outColor'))

            if(layerType == 'ALL'):
                mc.setAttr(('%s.%s') % (NMNode, 'samples'), 64)
                mc.setAttr(('%s.%s') % (NMNode, 'max_distance'), 30)
                mc.setAttr(('%s.%s') % (NMNode, 'output_mode'), 3)
                mc.setAttr(('%s.%s') % (NMNode, 'spread'), 0.2)
                mc.setAttr(('%s.%s') % (NMNode, 'id_inclexcl'), -1)
                mc.setAttr(('%s.%s') % (NMNode, 'dark'), 0.223026, 0.223026, 0.223026, type="double3")

            if(layerType == 'CHR'):
                mc.setAttr(('%s.%s') % (NMNode, 'samples'), 128)
                mc.setAttr(('%s.%s') % (NMNode, 'max_distance'), 5)
                mc.setAttr(('%s.%s') % (NMNode, 'output_mode'), 3)

            if(layerType == 'BG'):
                mc.setAttr(('%s.%s') % (NMNode, 'samples'), 64)
                mc.setAttr(('%s.%s') % (NMNode, 'max_distance'), 10)
                mc.setAttr(('%s.%s') % (NMNode, 'output_mode'), 3)

            # 优先全局着色
            for obj in rlObjs:
                # print '----------------'
                # print obj
                #mc.sets(obj, e=1, forceElement= NMSG )
                try:
                    mc.sets(obj, e=1, forceElement=NMSG)
                except:
                    # 获取物体面数
                    faceNum = mc.polyEvaluate(obj, face=1)
                    mc.sets((obj + u'.f[:' + str(faceNum - 1) + u']'), e=1, forceElement=NMSG)


            # 特殊物体着色
            if transpancySGNodes:
                for i in range(len(transpancySGNodes)):
                    if mc.ls(transpancySGNodes[i]):
                        if '_' not in transpancySGNodes[i]:
                            print u'>>>>>>[注意][%s]名字需要最少有1个_分隔符' % transpancySGNodes[i]
                        else:
                            keySGInfo = transpancySGNodes[i].split('_')[-2]
                        keySGInfo = str(i)
                        meshes = transpancyMeshes[i]
                        # 有着色物体时才进行
                        if meshes:
                            shaderTrsNode = 'SHD_' + layerType + '_' + keySGInfo + '_NM_Shader'
                            if mc.ls(shaderTrsNode):
                                mc.delete(shaderTrsNode)
                            NMTrsNode = 'SHD_' + layerType + '_' + keySGInfo + '_NM_Node'
                            if mc.ls(NMTrsNode):
                                mc.delete(NMTrsNode)
                            NMTrsSG = 'SHD_' + layerType + '_' + keySGInfo + '_NM_SG'
                            if mc.ls(NMTrsSG):
                                mc.delete(NMTrsSG)
                            # 创建
                            shaderTrsNode = mc.shadingNode('lambert', asShader=True, name=shaderTrsNode)
                            mc.setAttr((shaderTrsNode+'.ambientColor'),1,1,1,type='double3')
                            NMTrsNode = mc.shadingNode('mib_amb_occlusion', asTexture=True, name=NMTrsNode)
                            NMTrsSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=NMTrsSG)
                            # 连接
                            mc.connectAttr((shaderTrsNode + '.outColor'), (NMTrsSG + '.surfaceShader'))
                            mc.connectAttr((NMTrsNode + '.outValue'), (shaderTrsNode + '.color'))

                            # 透明连接
                            self.zmRLTransShaderConnectiion(transpancyNode[i], shaderTrsNode, 'transparency')

                            # file贴图反转
                            if '.outTransparency' in transpancyNode[i]:
                                mc.editRenderLayerAdjustment(transpancyNode[i].split('.')[0] + '.invert')
                                mc.setAttr((transpancyNode[i].split('.')[0] + ".invert"), 1)

                            # 设置NM
                            if(layerType == 'ALL'):
                                mc.setAttr(('%s.%s') % (NMTrsNode, 'samples'), 64)
                                mc.setAttr(('%s.%s') % (NMTrsNode, 'max_distance'), 30)
                                mc.setAttr(('%s.%s') % (NMTrsNode, 'output_mode'), 3)
                                mc.setAttr(('%s.%s') % (NMTrsNode, 'spread'), 0.2)
                                mc.setAttr(('%s.%s') % (NMTrsNode, 'id_inclexcl'), -1)
                                mc.setAttr(('%s.%s') % (NMTrsNode, 'dark'), 0.223026, 0.223026, 0.223026, type="double3")

                            if(layerType == 'CHR'):
                                mc.setAttr(('%s.%s') % (NMTrsNode, 'samples'), 128)
                                mc.setAttr(('%s.%s') % (NMTrsNode, 'max_distance'), 5)
                                mc.setAttr(('%s.%s') % (NMTrsNode, 'output_mode'), 3)

                            if(layerType == 'BG'):
                                mc.setAttr(('%s.%s') % (NMTrsNode, 'samples'), 64)
                                mc.setAttr(('%s.%s') % (NMTrsNode, 'max_distance'), 10)
                                mc.setAttr(('%s.%s') % (NMTrsNode, 'output_mode'), 3)

                            # 着色
                            for mesh in meshes:
                                if mc.objExists(mesh):
                                    try:
                                        mc.sets(mesh, e=1, forceElement=NMTrsSG)
                                    except:
                                        # 获取物体面数
                                        obj = mc.listRelatives(mesh, p=1, f=1)[0]
                                        faceNum = mc.polyEvaluate(obj, face=1)
                                        mc.sets((obj + u'.f[:' + str(faceNum - 1) + u']'), e=1, forceElement=NMTrsSG)

            # 隐藏灯光
            for light in lights:
                lightGrp = mc.listRelatives(light, p=1, type='transform', f=1)[0]
                mc.editRenderLayerAdjustment(lightGrp + '.v')
                mc.setAttr((light + '.v'), 0)
                mc.editRenderLayerAdjustment(light + '.intensity')
                mc.setAttr((light + '.intensity'), 0)

            # 设置
            # self.zmRLCommonConfig()

            # 渲染设置
            mc.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')

            # 关闭光线追踪
            mc.editRenderLayerAdjustment('miDefaultOptions.rayTracing')
            mc.setAttr('miDefaultOptions.rayTracing', 0)

            # 格式命名
            mc.setAttr('defaultRenderGlobals.animation', 1)
            mc.setAttr('defaultRenderGlobals.putFrameBeforeExt', 1)
            mc.setAttr('defaultRenderGlobals.periodInExt', 1)
            mc.setAttr('defaultRenderGlobals.extensionPadding', 4)
            if mc.getAttr('defaultRenderGlobals.outFormatControl') == 1:
                mc.setAttr('defaultRenderGlobals.outFormatControl', 0)

            # exr
            mc.editRenderLayerAdjustment('defaultRenderGlobals.imageFormat')
            mc.setAttr('defaultRenderGlobals.imageFormat', 51)
            mc.setAttr('defaultRenderGlobals.imfkey', 'exr', type='string')
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.setAttr('mentalrayGlobals.compressionQuality', 0)

            # 16位zip压缩
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.editRenderLayerAdjustment('miDefaultFramebuffer.datatype')
            mc.setAttr('miDefaultFramebuffer.datatype', 16)

            print (u'===============!!!Done  【%s】!!!===============' % (u'%s_NM层' % layerType))
            print '\n'
        else:
            print (u'===============!!!Error  【%s】无物体!!!===============' % (u'%s_NM层' % layerType))
            print '\n'

 

    # CHR_IDP层
    def zmIDPCHRCreate(self, layerType, selectObjType=0):
        print (u'===============!!!Start 【%s】!!!===============' % (u'%s_IDP层' % layerType))
        print 'Working...'

        # 物体
        objs = self.zmRLObjectsTList()
        refCHR = objs[0]
        refPROP = objs[1]
        refSET = objs[2]
        refSEA = objs[4]
        
        rlObjs=[]

        # 选取模式
        if selectObjType == 1:
            rlObjs = self.zmRLSelectMode()
            
        if layerType=='CHR':
            layerName='CHR_IDP'
            

            CHRGP=[]
            if refCHR:   
                for CHR in refCHR:
                    if 'c016001Biff' in CHR:
                        CHRGP.append(CHR)
            
            if CHRGP:
                rlObjs=refCHR+refPROP
            else:                                   
                mc.confirmDialog(title=u'警告', message=u'确认有“c016001Biff”壮汉这个角色，点击YES OR NO继续分层', button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')  
   

        if rlObjs:
            # 创建RenderLayer
            if mc.ls(layerName):
                mc.delete(layerName)

            mc.createRenderLayer(rlObjs, name=layerName, noRecurse=1, makeCurrent=1)
            mc.editRenderLayerGlobals(currentRenderLayer=layerName)
            
            mc.select(rlObjs)
            mel.eval('source "//file-cluster/GDC/Resource/Support/Maya/projects/Lionelville/HbRgbaMaterialTool.mel";HbMaterialM;')

            facespecail=['*:*MSH_c_hi_Pants_ca_2_.f[329:337]','*:*MSH_c_hi_Pants_ca_2_.f[339:340]','*:*MSH_c_hi_Pants_ca_2_.f[365:379]','*:*MSH_c_hi_Pants_ca_2_.f[381:385]','*:*MSH_c_hi_Pants_ca_2_.f[387:388]','*:*MSH_c_hi_Pants_ca_2_.f[920:931]','*:*MSH_c_hi_Pants_ca_2_.f[956:979]','*:*MSH_c_hi_Pants_ca_2_.f[1182:1184]','*:*MSH_c_hi_Pants_ca_2_.f[1208:1210]','*:*MSH_c_hi_Pants_ca_2_.f[1246:1248]','*:*MSH_c_hi_Pants_ca_2_.f[1258:1260]']
            for face in facespecail:
                mc.select(face)
                mel.eval('source "//file-cluster/GDC/Resource/Support/Maya/projects/Lionelville/HbRgbaMaterialTool.mel";HbMaterialR;')

            
          

            # 渲染设置
            mc.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')

            # 格式命名
            mc.setAttr('defaultRenderGlobals.animation', 1)
            mc.setAttr('defaultRenderGlobals.putFrameBeforeExt', 1)
            mc.setAttr('defaultRenderGlobals.periodInExt', 1)
            mc.setAttr('defaultRenderGlobals.extensionPadding', 4)
            if mc.getAttr('defaultRenderGlobals.outFormatControl') == 1:
                mc.setAttr('defaultRenderGlobals.outFormatControl', 0)

            # exr
            mc.editRenderLayerAdjustment('defaultRenderGlobals.imageFormat')
            mc.setAttr('defaultRenderGlobals.imageFormat', 51)
            mc.setAttr('defaultRenderGlobals.imfkey', 'exr', type='string')
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.setAttr('mentalrayGlobals.compressionQuality', 0)

            # 16位zip压缩
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.editRenderLayerAdjustment('miDefaultFramebuffer.datatype')
            mc.setAttr('miDefaultFramebuffer.datatype', 16)

            print (u'===============!!!Done  【%s】!!!===============' % (u'%s_IDP层' % layerType))
            print '\n'
        else:
            print (u'===============!!!Error  【%s】无物体!!!===============' % (u'%s_IDP层' % layerType))
            print '\n'            
            
            
            

 

    # FG_LGT层
    # 新版本
    def zmRLLIGHTCreate(self, layerType, selectObjType=0):
        print (u'===============!!!Start 【%s】!!!===============' % (u'%s_LGT层' % layerType))
        print 'Working...'

        # 物体
        objs = self.zmRLObjectsTList()
        refCHR = objs[0]
        refPROP = objs[1]
        refSET = objs[2]
        refSKY = objs[3]
        seaInfo = objs[4]
        
        
        LGTSG= self.zmRLSGNodesGet()
        SGCHR=LGTSG[0]
        SGPROP=LGTSG[1]
        SGSET=LGTSG[2]
        
        rlObjs = []
        needSG = []
        if layerType == 'LGTFG':

            rlObjs = refSET + refCHR + refPROP
            needSG = SGCHR + SGPROP + SGSET
            if needSG:
                needSG = list(set(needSG))
            layerName = 'FG_LGT'

        # 灯光
        lights = mc.ls(type='light', l=1)
        lightGrps = []
        needLightGrps = []
        lightgup = []
        if lights:
            for light in lights:
                lightGrps.append(mc.listRelatives(light, p=1, type='transform', f=1)[0])
        if lightGrps:
            if layerType == 'LGTFG':
                for grp in lightGrps:
                    if 'LGT_DAY_KEY_' in grp:
                        needLightGrps.append(grp)
                if len(needLightGrps) >= 2:
                    for light in needLightGrps:
                        if mc.getAttr(light.split('|')[4] + ".v") == True:
                            lightgup.append(light)
                if len(lightgup) >= 2:
                    mc.confirmDialog(title=u'警告', message=u'FG_LGT层可能存在多盏灯光，请自行隐藏其余灯光，点击YES OR NO继续分层', button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')


        # 选取模式
        if selectObjType == 1:
            rlObjs = self.zmRLSelectMode()

        if rlObjs:
            # 透明信息
            transpancyObjs = self.zmRLTransparencyObjs()
            transpancySGNodes = transpancyObjs[0]
            transpancyMeshes = transpancyObjs[1]
            transpancyNode = transpancyObjs[2]
            
            rampObjInfos = self.zmRLWDInfoObjs()
            rampInfos = rampObjInfos[0]
            rampNodes = []
            rampSGNodes = []
            rampMeshes = rampObjInfos[1]
            rampPositions = rampObjInfos[2]
            if rampInfos:
                for info in rampInfos:
                    needInfo = info.split('>_<')
                    rampNodes.append(needInfo[0])
                    rampSGNodes.append(needInfo[1])
            

            from idmt.maya.py_common import sk_infoConfig
            reload(sk_infoConfig)
            import os

            # 创建RenderLayer
            if mc.ls(layerName):
                mc.delete(layerName)
            # 要加灯光
            mc.createRenderLayer((rlObjs + needLightGrps), name=layerName, noRecurse=1, makeCurrent=1)


            # openSea是否在场景里
            checkAssetID = ['s019001']
            namespaces = mc.namespaceInfo(listOnlyNamespaces=1)
            checkState = 0
            for ID in checkAssetID:
                for ns in namespaces:
                    if ID in ns:
                        checkState = 1
            # FG
            if layerType == 'LGTFG':
                # BG渲染关闭
                if (refCHR + refPROP):
                    for obj in (refCHR + refPROP):
                        mesh = mc.listRelatives(obj, ni=1, type='mesh', s=1, f=1)[0]
                        mc.editRenderLayerAdjustment(mesh + '.primaryVisibility')
                        mc.setAttr((mesh + '.primaryVisibility'), 0)

                # 不需要Sky
                if refSKY:
                    for obj in refSKY:
                        mc.editRenderLayerAdjustment(obj + '.visibility')
                        mc.setAttr((obj + '.visibility'), 0)

                if seaInfo:
                    for obj in seaInfo:
                        mc.editRenderLayerAdjustment(obj + '.visibility')
                        mc.setAttr((obj + '.visibility'), 0)

                # openSea在则隐藏
                if checkState:
                    lightingGrps = mc.ls('*:*LIGHTING', type='transform') + mc.ls('*:*:*LIGHTING', type='transform')
                    for ID in checkAssetID:
                        for grp in lightingGrps:
                            if ID not in grp:
                                mc.editRenderLayerAdjustment(grp + '.visibility')
                                mc.setAttr((grp + '.visibility'), 0)
                                
                cyclosGrp = mc.ls('*:*:*MSH_c_hi_Cyclos',type = 'transform',l=1)
                if cyclosGrp:
                    meshes = mc.listRelatives(cyclosGrp,ad = 1,type = 'mesh',f = 1)
                    polyGrps = mc.listRelatives(meshes,p = 1,type = 'transform',f = 1)
                    polyGrps = list(set(polyGrps))
                    for grp in polyGrps:
                        mc.editRenderLayerAdjustment(grp + '.visibility')
                        mc.setAttr((grp + '.visibility'), 0)                         


                            

            # 通用LGT材质
            shaderNode = 'SHD_' + layerType + '_LGT_Shader'
            if mc.ls(shaderNode):
                mc.delete(shaderNode)
                
            shaderNode_ramp = 'SHD_' + layerType + '_L_Shader'
            if mc.ls(shaderNode_ramp):
                mc.delete(shaderNode_ramp)


            shaderNode_ramp = mc.shadingNode('rampShader', asShader=True, name=shaderNode_ramp)
            mc.setAttr((shaderNode_ramp + '.colorInput'), 2)
            mc.setAttr((shaderNode_ramp + '.color[0].color_Color'), 1, 1, 1, type='double3')
            mc.setAttr((shaderNode_ramp + '.color[0].color_Position'), 0)
            mc.setAttr((shaderNode_ramp + '.color[0].color_Interp'), 0)
            mc.setAttr((shaderNode_ramp + '.color[1].color_Color'), 0, 0, 0, type='double3')
            mc.setAttr((shaderNode_ramp + '.color[1].color_Position'), 0.096)
            mc.setAttr((shaderNode_ramp + '.color[1].color_Interp'), 0)
            mc.setAttr((shaderNode_ramp + '.diffuse'), 1)
            mc.setAttr((shaderNode_ramp + '.translucenceDepth'), 1000)
            mc.setAttr((shaderNode_ramp + '.specularity'), 0)
            mc.setAttr((shaderNode_ramp + '.reflectivity[0].reflectivity_Position'), 0)
            mc.setAttr((shaderNode_ramp + '.reflectivity[0].reflectivity_FloatValue'), 0)

            shaderNode = mc.shadingNode('surfaceShader', asShader=True, name=shaderNode)
            mc.connectAttr((shaderNode_ramp + '.outColor'), (shaderNode + '.outColor'))
                       
            # 优先全局着色

            if needSG:
                for SGNode in needSG:
                    shaderInfo = mc.listConnections((SGNode + '.surfaceShader'),s = 1,plugs = 1)
                    if not shaderInfo:
                        continue
                    shaderInfo = shaderInfo[0]
                    mc.editRenderLayerAdjustment(SGNode + '.surfaceShader')
                    mc.disconnectAttr(shaderInfo, (SGNode + '.surfaceShader'))
                    mc.connectAttr((shaderNode + '.outColor'), (SGNode + '.surfaceShader'), f=1) 

          
            # 特殊物体着色
            # LGT新版：每套材质球都存在，transpancySGNodes
            indexTransDone = []
            if rampNodes:
                pass

            rampNodes = []
            rampSGNodes = []
            rampMeshes = rampObjInfos[1]
            rampPositions = rampObjInfos[2]
            
            
            shaderNodeA = 'SHD_' + layerType + '_alpha_Shader'
            if mc.ls(shaderNodeA):
                mc.delete(shaderNodeA)
                
            shaderNode_rampA = 'SHD_' + layerType + '_A_Shader'
            if mc.ls(shaderNode_rampA):
                mc.delete(shaderNode_rampA)


            shaderNode_rampA = mc.shadingNode('rampShader', asShader=True, name=shaderNode_rampA)
            mc.setAttr((shaderNode_rampA + '.colorInput'), 2)
            mc.setAttr((shaderNode_rampA + '.color[0].color_Color'), 1, 1, 1, type='double3')
            mc.setAttr((shaderNode_rampA + '.color[0].color_Position'), 0)
            mc.setAttr((shaderNode_rampA + '.color[0].color_Interp'), 0)
            mc.setAttr((shaderNode_rampA + '.color[1].color_Color'), 0, 0, 0, type='double3')
            mc.setAttr((shaderNode_rampA + '.color[1].color_Position'), 0.5)
            mc.setAttr((shaderNode_rampA + '.color[1].color_Interp'), 0)
            mc.setAttr((shaderNode_rampA + '.diffuse'), 1)
            mc.setAttr((shaderNode_rampA + '.translucenceDepth'), 1000)
            mc.setAttr((shaderNode_rampA + '.specularity'), 0)
            mc.setAttr((shaderNode_rampA + '.reflectivity[0].reflectivity_Position'), 0)
            mc.setAttr((shaderNode_rampA + '.reflectivity[0].reflectivity_FloatValue'), 0)

            shaderNodeA = mc.shadingNode('surfaceShader', asShader=True, name=shaderNodeA)
            mc.connectAttr((shaderNode_rampA + '.outColor'), (shaderNodeA + '.outColor'))

            if transpancySGNodes:
                for i in range(len(transpancySGNodes)):
                    if mc.ls(transpancySGNodes[i]):
                        if '_' not in transpancySGNodes[i]:
                            print u'>>>>>>[注意][%s]名字需要最少有1个_分隔符' % transpancySGNodes[i]
                        else:
                            keySGInfo = transpancySGNodes[i].split('_')[-2]
                        keySGInfo = str(i)
                        meshes = transpancyMeshes[i]
                        # 有着色物体时才进行
                        if meshes:
                            shaderTrsNode = 'SHD_' + layerType + '_' + keySGInfo + '_LGT_Shader'
                            if mc.ls(shaderTrsNode):
                                mc.delete(shaderTrsNode)


                            # 创建
                            shaderTrsNode = mc.shadingNode('lambert', asShader=True, name=shaderTrsNode)
                            #mc.setAttr((shaderTrsNode + '.color'), 0, 0, 0, type='double3')
                            mc.setAttr((shaderTrsNode + '.ambientColor'), 1, 1, 1, type='double3')
 
                                                       
                            mc.connectAttr((shaderNodeA+ '.outColor'),(shaderTrsNode+'.color'))

                            # 透明连接
                            self.zmRLTransShaderConnectiion(transpancyNode[i], shaderTrsNode, 'transparency')

                            # file贴图反转
                            if '.outTransparency' in transpancyNode[i]:
                                mc.editRenderLayerAdjustment(transpancyNode[i].split('.')[0] + '.invert')
                                mc.setAttr((transpancyNode[i].split('.')[0] + ".invert"), 1)

                            # 着色
 
                            shaderInfo = mc.listConnections((transpancySGNodes[i] + '.surfaceShader'),s = 1,plugs = 1)
                            if shaderInfo:
                                shaderInfo = shaderInfo[0]
                                mc.editRenderLayerAdjustment(transpancySGNodes[i] + '.surfaceShader')
                                mc.disconnectAttr(shaderInfo, (transpancySGNodes[i] + '.surfaceShader'))
                                mc.connectAttr((shaderTrsNode + '.outColor'), (transpancySGNodes[i] + '.surfaceShader'), f=1)

            if layerName=='FG_LGT':
                needobj=[]
                needobj01=[]
                needobj02=[]
                if refSET:
                    for obj in refSET:
                        if 'MSH_c_hi_ShellRight_'in obj:
                            needobj01.append(obj)
                        if 'MSH_c_hi_ShellLeft_' in obj:
                            needobj02.append(obj)
                needobj=needobj01+needobj02
        
                if needobj:
                    # 转到FG_LGT层处理
                    # mc.editRenderLayerGlobals(currentRenderLayer='FG_LGT')
    
                    # s001001GalionBeach赋予另外的材质
                    shaderNode = 'SHD_GalionBeach_Shader'
                    if mc.ls(shaderNode):
                        mc.delete(shaderNode)
    
                    shaderNode_ramp = 'SHD_GalionBeach_L_Shader'
                    if mc.ls(shaderNode_ramp):
                        mc.delete(shaderNode_ramp)
    
                    shaderSG = 'SHD_GalionBeach_SG'
                    if mc.ls(shaderSG):
                        mc.delete(shaderSG)
                    else:
                        shaderSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=shaderSG)
    
                    shaderNode_ramp = mc.shadingNode('rampShader', asShader=True, name=shaderNode_ramp)
                    mc.setAttr((shaderNode_ramp + '.colorInput'), 2)
                    mc.setAttr((shaderNode_ramp + '.color[0].color_Color'), 1, 1, 1, type='double3')
                    mc.setAttr((shaderNode_ramp + '.color[0].color_Position'), 0)
                    mc.setAttr((shaderNode_ramp + '.color[0].color_Interp'), 0)
                    mc.setAttr((shaderNode_ramp + '.color[1].color_Color'), 0, 0, 0, type='double3')
                    mc.setAttr((shaderNode_ramp + '.color[1].color_Position'), 0.096)
                    mc.setAttr((shaderNode_ramp + '.color[1].color_Interp'), 0)
                    mc.setAttr((shaderNode_ramp + '.diffuse'), 1)
                    mc.setAttr((shaderNode_ramp + '.translucenceDepth'), 1000)
                    mc.setAttr((shaderNode_ramp + '.specularity'), 0)
                    mc.setAttr((shaderNode_ramp + '.reflectivity[0].reflectivity_Position'), 0)
                    mc.setAttr((shaderNode_ramp + '.reflectivity[0].reflectivity_FloatValue'), 0)
    
                    shaderNode = mc.shadingNode('surfaceShader', asShader=True, name=shaderNode)
                    mc.connectAttr((shaderNode_ramp + '.outColor'), (shaderNode + '.outColor'))
    
                    try:
                        mc.connectAttr((shaderNode + '.outColor'), (shaderSG + '.surfaceShader'))
                    except:
                        pass
    
                    # s001001GalionBeach着色
                    if needobj:
                        for obj in needobj:
                            mc.sets(obj, e=1, forceElement=shaderSG)
    
                    # 创建passContributionMap
                    Map = mc.createNode('passContributionMap', n='passMap')
                    mc.connectAttr((layerName + '.passContributionMap'), (Map + '.owner'), na=1)
                    if needobj:
                        for obj in needobj:
                            mc.connectAttr((obj + '.message'), (Map + '.dagObjects'), na=1)
                    # 创建renderPass节点
                    cusColor = mc.shadingNode('renderPass', asRendering=1, name='customColor')
    
                    cmd = 'applyAttrPreset \"' + cusColor + '\" \"D:/Alias/Maya2012x64/presets/attrPresets/renderPass/customColor.mel\" 1;'
                    mel.eval(cmd)
                    #mel.eval('applyAttrPreset "customColor" "D:/Alias/Maya2012x64/presets/attrPresets/renderPass/customColor.mel" 1;')
    
                    shaRaw = mc.shadingNode('renderPass', asRendering=1, name='shadowRaw')
                    cmr = 'applyAttrPreset \"' + shaRaw + '\" \"D:/Alias/Maya2012x64/presets/attrPresets/renderPass/rawShadow.mel\" 1;'
                    mel.eval(cmr)

    
                    # 使renderPass节点与层和passContributionMap相连
                    mc.connectAttr((layerName + '.renderPass'), (cusColor + '.owner'), nextAvailable=1)
                    mc.connectAttr((layerName + '.renderPass'), (shaRaw + '.owner'), nextAvailable=1)
    
                    mc.connectAttr((cusColor + '.message'), (Map + '.renderPass'), nextAvailable=1)
                    mc.connectAttr((shaRaw + '.message'), (Map + '.renderPass'), nextAvailable=1)
    
                    # 创建writeToColorBuffer节点
                    ColorBuffer = mc.shadingNode('writeToColorBuffer', asShader=1, name='colorBuffer')
                    mc.setAttr((ColorBuffer + '.color'), 1, 0, 0, type='double3')
                    mc.connectAttr((cusColor + '.message'), (ColorBuffer + '.renderPass'))
    
                    mc.connectAttr((shaderNode + '.outColor'), (ColorBuffer + '.evaluationPassThrough'))


            # 渲染设置
            mc.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')

            # 格式命名
            mc.setAttr('defaultRenderGlobals.animation', 1)
            mc.setAttr('defaultRenderGlobals.putFrameBeforeExt', 1)
            mc.setAttr('defaultRenderGlobals.periodInExt', 1)
            mc.setAttr('defaultRenderGlobals.extensionPadding', 4)
            if mc.getAttr('defaultRenderGlobals.outFormatControl') == 1:
                mc.setAttr('defaultRenderGlobals.outFormatControl', 0)

            # exr
            mc.editRenderLayerAdjustment('defaultRenderGlobals.imageFormat')
            mc.setAttr('defaultRenderGlobals.imageFormat', 51)
            mc.setAttr('defaultRenderGlobals.imfkey', 'exr', type='string')
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.setAttr('mentalrayGlobals.compressionQuality', 0)

            # 16位zip压缩
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.editRenderLayerAdjustment('miDefaultFramebuffer.datatype')
            mc.setAttr('miDefaultFramebuffer.datatype', 16)

            print (u'===============!!!Done  【%s】!!!===============' % (u'%s_LGT层' % layerType))
            print '\n'
        else:
            print (u'===============!!!Error  【%s】无物体!!!===============' % (u'%s_LGT层' % layerType))
            print '\n'

   # LG_LGT层
    def zmLGLGTCreate(self, layerType, selectObjType=0):
        print (u'===============!!!Start 【%s】!!!===============' % (u'%s_LGT层' % layerType))
        print 'Working...'

        # 物体
        objs = self.zmRLObjectsTList()
        refCHR = objs[0]
        refPROP = objs[1]
        refSET = objs[2]
        refSKY = objs[3]
        seaInfo = objs[4]
        rlObjs = []
        
        LGTSG= self.zmRLSGNodesGet()
        SGCHR=LGTSG[0]
        SGPROP=LGTSG[1]
        SGSET=LGTSG[2]        

        if layerType == 'ALL':

            rlObjs = refSET + refCHR + refPROP
            needSG= SGCHR + SGPROP +SGSET
            layerName = 'LG_LGT'

        # 灯光
        lights = mc.ls(type='light', l=1)
        lightGrps = []
        needLightGrps = []
        needLightGrps01 = []
        needLightGrps02 = []
        needLightGrps03 = []
        needLightGrps04 = []
        if lights:
            for light in lights:
                lightGrps.append(mc.listRelatives(light, p=1, type='transform', f=1)[0])
        if lightGrps:
            if layerType == 'ALL':
                for grp in lightGrps:
                    if 'LGT_DAY_BOUNCE' in grp:
                        needLightGrps01.append(grp)
                    if 'LGT_DAY_AMBIENT' in grp:
                        needLightGrps02.append(grp)
                    if 'LGT_DAY_KEY' in grp:
                        needLightGrps03.append(grp)
                    if 'LGT_DAY_EXTRA' in grp:
                        needLightGrps04.append(grp)

        needLightGrps = needLightGrps01 + needLightGrps02 + needLightGrps03 + needLightGrps04

        # 选取模式

        if selectObjType == 1:
            rlObjs = self.zmRLSelectMode()


        if rlObjs:
            # 透明信息
            transpancyObjs = self.zmRLTransparencyObjs()
            transpancySGNodes = transpancyObjs[0]
            transpancyMeshes = transpancyObjs[1]
            transpancyNode = transpancyObjs[2]

            # Ramp信息
            rampObjInfos = self.zmRLWDInfoObjs()
            rampInfos = rampObjInfos[0]
            rampNodes = []
            rampSGNodes = []
            rampMeshes = rampObjInfos[1]
            rampPositions = rampObjInfos[2]
            if rampInfos:
                for info in rampInfos:
                    needInfo = info.split('>_<')
                    rampNodes.append(needInfo[0])
                    rampSGNodes.append(needInfo[1])

            from idmt.maya.py_common import sk_infoConfig
            reload(sk_infoConfig)
            import os

            # 创建RenderLayer
            if mc.ls(layerName):
                mc.delete(layerName)
            # 要加灯光
            mc.createRenderLayer((rlObjs + needLightGrps), name=layerName, noRecurse=1, makeCurrent=1)

            # openSea是否在场景里
            checkAssetID = ['s019001']
            namespaces = mc.namespaceInfo(listOnlyNamespaces=1)
            checkState = 0
            for ID in checkAssetID:
                for ns in namespaces:
                    if ID in ns:
                        checkState = 1
            # FG
            if layerType == 'ALL':
                # BG渲染关闭
                if (refCHR + refPROP):
                    for obj in (refCHR + refPROP):
                        mesh = mc.listRelatives(obj, ni=1, type='mesh', s=1, f=1)[0]
                        mc.editRenderLayerAdjustment(mesh + '.primaryVisibility')
                        mc.setAttr((mesh + '.primaryVisibility'), 0)

                # 不需要Sky
                if refSKY:
                    for obj in refSKY:
                        mc.editRenderLayerAdjustment(obj + '.visibility')
                        mc.setAttr((obj + '.visibility'), 0)

                if seaInfo:
                    for obj in seaInfo:
                        if 's039001ForbiddenCave' not in obj:
                            mc.editRenderLayerAdjustment(obj + '.visibility')
                            mc.setAttr((obj + '.visibility'), 0)
                
                # openSea在则隐藏
                if checkState:
                    lightingGrps = mc.ls('*:*LIGHTING', type='transform') + mc.ls('*:*:*LIGHTING', type='transform')
                    for ID in checkAssetID:
                        for grp in lightingGrps:
                            if ID not in grp:
                                mc.editRenderLayerAdjustment(grp + '.visibility')
                                mc.setAttr((grp + '.visibility'), 0)

            # 通用LGT材质
            shaderNode = 'SHD_' + layerType + '_LGT_Shader'
            if mc.ls(shaderNode):
                mc.delete(shaderNode)


            shaderNode = mc.shadingNode('lambert', asShader=True, name=shaderNode)
            mc.setAttr((shaderNode + '.color'), 1, 1, 1, type='double3')


            # 优先全局着色
            if needSG:
                for SGNode in needSG:
                    shaderInfo = mc.listConnections((SGNode + '.surfaceShader'),s = 1,plugs = 1)
                    if not shaderInfo:
                        continue
                    shaderInfo = shaderInfo[0]
                    mc.editRenderLayerAdjustment(SGNode + '.surfaceShader')
                    mc.disconnectAttr(shaderInfo, (SGNode + '.surfaceShader'))
                    mc.connectAttr((shaderNode + '.outColor'), (SGNode + '.surfaceShader'), f=1)



            if transpancySGNodes:
                for i in range(len(transpancySGNodes)):
                    if mc.ls(transpancySGNodes[i]):
                        if '_' not in transpancySGNodes[i]:
                            print u'>>>>>>[注意][%s]名字需要最少有1个_分隔符' % transpancySGNodes[i]
                        else:
                            keySGInfo = transpancySGNodes[i].split('_')[-2]
                        keySGInfo = str(i)
                        meshes = transpancyMeshes[i]
                        # 有着色物体时才进行
                        if meshes:
                            shaderTrsNode = 'SHD_' + layerType + '_' + keySGInfo + '_LGT_Shader'
                            if mc.ls(shaderTrsNode):
                                mc.delete(shaderTrsNode)

                            # 创建
                            shaderTrsNode = mc.shadingNode('lambert', asShader=True, name=shaderTrsNode)
                            mc.setAttr((shaderTrsNode + '.color'), 1, 1, 1, type='double3')

                            # 透明连接
                            self.zmRLTransShaderConnectiion(transpancyNode[i], shaderTrsNode, 'transparency')

                            # file贴图反转
                            if '.outTransparency' in transpancyNode[i]:
                                mc.editRenderLayerAdjustment(transpancyNode[i].split('.')[0] + '.invert')
                                mc.setAttr((transpancyNode[i].split('.')[0] + ".invert"), 1)
                                
                            shaderInfo = mc.listConnections((transpancySGNodes[i] + '.surfaceShader'),s = 1,plugs = 1)
                            if shaderInfo:
                                shaderInfo = shaderInfo[0]
                                mc.editRenderLayerAdjustment(transpancySGNodes[i] + '.surfaceShader')
                                mc.disconnectAttr(shaderInfo, (transpancySGNodes[i] + '.surfaceShader'))
                                mc.connectAttr((shaderTrsNode + '.outColor'), (transpancySGNodes[i] + '.surfaceShader'), f=1)


            # 渲染设置
            mc.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')

            # 格式命名
            mc.setAttr('defaultRenderGlobals.animation', 1)
            mc.setAttr('defaultRenderGlobals.putFrameBeforeExt', 1)
            mc.setAttr('defaultRenderGlobals.periodInExt', 1)
            mc.setAttr('defaultRenderGlobals.extensionPadding', 4)
            if mc.getAttr('defaultRenderGlobals.outFormatControl') == 1:
                mc.setAttr('defaultRenderGlobals.outFormatControl', 0)

            # exr
            mc.editRenderLayerAdjustment('defaultRenderGlobals.imageFormat')
            mc.setAttr('defaultRenderGlobals.imageFormat', 51)
            mc.setAttr('defaultRenderGlobals.imfkey', 'exr', type='string')
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.setAttr('mentalrayGlobals.compressionQuality', 0)

            # 16位zip压缩
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.editRenderLayerAdjustment('miDefaultFramebuffer.datatype')
            mc.setAttr('miDefaultFramebuffer.datatype', 16)

            print (u'===============!!!Done  【%s】!!!===============' % (u'%s_LGT层' % layerType))
            print '\n'
        else:
            print (u'===============!!!Error  【%s】无物体!!!===============' % (u'%s_LGT层' % layerType))
            print '\n'


    #CHR_LGTSYS 角色灯
    def zmRLLIGHTNewCreate(self, layerType, selectObjType=0):
        print (u'===============!!!Start 【%s】!!!===============' % (u'%s_CHR层' % layerType))
        print 'Working...'
        
        from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
        reload(sk_referenceConfig)

        # 选取模式
        if selectObjType == 1:
            rlObjs = self.zmRLSelectMode()

        # 物体
        objs = self.zmRLObjectsTList()
        refCHR = objs[0]
        refPROP = objs[1]
        
        CHRSG= self.zmRLSGNodesGet()
        SGCHR=CHRSG[0]
        SGPROP=CHRSG[1]
        SGSET=CHRSG[2]

        rlObjs = refCHR + refPROP
        needSG = SGCHR + SGPROP
        
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        renamespace= refInfos[2][0]
        
        refername=''
        refernames=[]
        referencename=[]
        if renamespace:
            for refnames in renamespace:                        
               if '_' in refnames:
                   referencename.append(refnames)
        if referencename:
            for refnames in referencename:
                refername=refnames.split('_')[1]
                refernames.append(refername)
        sepnames=[]
        if refernames:
            for refer in refernames:
                if refer[0]=='s':
                    sepnames.append(refer)
        refernames=sepnames
                            
        filenames=[]
        filename=''
        lightnames=[]
        lightpath='Z:/Projects/ZoomWhiteDolphin/Reference/Sylvain/LIGHTING/'
        fileslist=mc.getFileList(folder= lightpath)
        
        if fileslist:
            for files in fileslist:
                    filename=files.split('.')[0]
                    filenames.append(filename)       
        
        for refnames in refernames:
            for filename in filenames:
                if refnames == filename:
                    lightnames.append(filename)
                    
        if len(lightnames)==1:
            for lightname in lightnames:
                lightFile = lightpath+lightname+'.mb'
                
        if len(lightnames)==0:
            mc.confirmDialog(title=u'警告', message=u'（1）请确保文件中有场景参考，可不必勾选但不能移除；（2）如若排除掉（1）的情况依然提示对话框，请和S联系，让他更新角色灯光', button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')
            
        if len(lightnames)>=2:
            mc.confirmDialog(title=u'警告', message=u'文件中可能存在两个以上场景参考，请确定文件以哪个场景为主，并移除其他场景参考保留主场景参考', button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')
            
        light_grp = mc.ls('LIGHTING', type='transform')

        if mc.ls(light_grp):
            mc.delete(light_grp)

        mc.file(lightFile, i=1)

        layerName = ''
        # 灯光

        lights = []
        lightGrps = []
        needLightGrps01 = []
        needLightGrps03 = []
        needLightGrps05 = []
        needLightGrps07 = []
        needLightGrps08 = []
        needLightGrps09 = []

        needLightGrps_A = []
        needLightGrps_B = []
        needLightGrps_C = []
        needLightGrps_ABC = []

        if layerType == 'CHR':
            lights = mc.ls(type='light', l=1)
            if lights:
                for light in lights:
                    lightGrps.append(mc.listRelatives(light, p=1, type='transform', f=1)[0])
                if lightGrps:
                    for grp in lightGrps:
                        if 'DAY_CHR_A1' in grp:
                            needLightGrps01.append(grp)

                        if 'DAY_CHR_B1' in grp:
                            needLightGrps03.append(grp)

                        if 'DAY_CHR_C1' in grp:
                            needLightGrps05.append(grp)

                        if 'DAY_CHRB_A' in grp:
                            needLightGrps07.append(grp)
                        if 'DAY_CHRB_B' in grp:
                            needLightGrps08.append(grp)
                        if 'DAY_CHRB_C' in grp:
                            needLightGrps09.append(grp)

                needLightGrps_A = needLightGrps01
                needLightGrps_B = needLightGrps03
                needLightGrps_C = needLightGrps05
                needLightGrps_ABC = needLightGrps07 + needLightGrps08 + needLightGrps09

                if needLightGrps_A:
                    layerName = 'CHR_LGTA'
                    if mc.ls(layerName):
                        mc.delete(layerName)
                    mc.createRenderLayer((rlObjs + needLightGrps_A), name=layerName, noRecurse=1, makeCurrent=1)
                    mc.setAttr('defaultRenderGlobals.imageFormat', 51)
                    mc.setAttr('defaultRenderGlobals.imfkey', 'exr', type='string')

                if needLightGrps_B:
                    layerName = 'CHR_LGTB'
                    if mc.ls(layerName):
                        mc.delete(layerName)
                    mc.createRenderLayer((rlObjs + needLightGrps_B), name=layerName, noRecurse=1, makeCurrent=1)

                if needLightGrps_C:
                    layerName = 'CHR_LGTC'
                    if mc.ls(layerName):
                        mc.delete(layerName)
                    mc.createRenderLayer((rlObjs + needLightGrps_C), name=layerName, noRecurse=1, makeCurrent=1)

                if needLightGrps_ABC:
                    layerName = 'CHR_LGTRIM'
                    if mc.ls(layerName):
                        mc.delete(layerName)
                    mc.createRenderLayer((rlObjs + needLightGrps_ABC), name=layerName, noRecurse=1, makeCurrent=1)

        if rlObjs:
            # 透明信息
            transpancyObjs = self.zmRLTransparencyObjs()
            transpancySGNodes = transpancyObjs[0]
            transpancyMeshes = transpancyObjs[1]
            transpancyNode = transpancyObjs[2]

            from idmt.maya.py_common import sk_infoConfig
            reload(sk_infoConfig)
            import os

            # openSea是否在场景里
            checkAssetID = ['s019001']
            namespaces = mc.namespaceInfo(listOnlyNamespaces=1)
            checkState = 0
            for ID in checkAssetID:
                for ns in namespaces:
                    if ID in ns:
                        checkState = 1

            # 通用LGT材质

            if layerName == 'CHR_LGTRIM':
                shaderNode = 'SHD_' + layerType + '_LGT_Shader'
                if mc.ls(shaderNode):
                    mc.delete(shaderNode)
 

                shaderNode = mc.shadingNode('lambert', asShader=True, name=shaderNode)
                mc.setAttr((shaderNode + '.color'), 1, 1, 1, type='double3')
   
                

                # 优先全局着色
                if needSG:
                    for SGNode in needSG:
                        shaderInfo = mc.listConnections((SGNode + '.surfaceShader'),s = 1,plugs = 1)
                        if not shaderInfo:
                            continue
                        shaderInfo = shaderInfo[0]
                        mc.editRenderLayerAdjustment(SGNode + '.surfaceShader')
                        mc.disconnectAttr(shaderInfo, (SGNode + '.surfaceShader'))
                        mc.connectAttr((shaderNode + '.outColor'), (SGNode + '.surfaceShader'), f=1)
  
                if transpancySGNodes:
                    for i in range(len(transpancySGNodes)):
                        if mc.ls(transpancySGNodes[i]):
                            if '_' not in transpancySGNodes[i]:
                                print u'>>>>>>[注意][%s]名字需要最少有1个_分隔符' % transpancySGNodes[i]
                            else:
                                keySGInfo = transpancySGNodes[i].split('_')[-2]
                            keySGInfo = str(i)
                            meshes = transpancyMeshes[i]
                            # 有着色物体时才进行
                            if meshes:
                                shaderTrsNode = 'SHD_' + layerType + '_' + keySGInfo + '_LGT_Shader'
                                if mc.ls(shaderTrsNode):
                                    mc.delete(shaderTrsNode)
     

                                # 创建
                                shaderTrsNode = mc.shadingNode('lambert', asShader=True, name=shaderTrsNode)
                                mc.setAttr((shaderTrsNode + '.color'), 1, 1, 1, type='double3')
     
                                # 透明连接
                                self.zmRLTransShaderConnectiion(transpancyNode[i], shaderTrsNode, 'transparency')

                                # file贴图反转
                                if '.outTransparency' in transpancyNode[i]:
                                    mc.editRenderLayerAdjustment(transpancyNode[i].split('.')[0] + '.invert')
                                    mc.setAttr((transpancyNode[i].split('.')[0] + ".invert"), 1)

                                # 连接着色
                                mc.editRenderLayerAdjustment(transpancySGNodes[i] + '.surfaceShader')
                                mc.connectAttr((shaderTrsNode + '.outColor'), (transpancySGNodes[i] + '.surfaceShader'), f=1)

                                # 着色
                                shaderInfo = mc.listConnections((transpancySGNodes[i] + '.surfaceShader'),s = 1,plugs = 1)
                                if shaderInfo:
                                    shaderInfo = shaderInfo[0]
                                    mc.editRenderLayerAdjustment(transpancySGNodes[i] + '.surfaceShader')
                                    mc.disconnectAttr(shaderInfo, (transpancySGNodes[i] + '.surfaceShader'))
                                    mc.connectAttr((shaderTrsNode + '.outColor'), (transpancySGNodes[i] + '.surfaceShader'), f=1)
 

            # 设置
            # self.zmRLCommonConfig()
            # 渲染设置
            mc.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')

            # 格式命名
            mc.setAttr('defaultRenderGlobals.animation', 1)
            mc.setAttr('defaultRenderGlobals.putFrameBeforeExt', 1)
            mc.setAttr('defaultRenderGlobals.periodInExt', 1)
            mc.setAttr('defaultRenderGlobals.extensionPadding', 4)
            if mc.getAttr('defaultRenderGlobals.outFormatControl') == 1:
                mc.setAttr('defaultRenderGlobals.outFormatControl', 0)

            # exr
            mc.editRenderLayerAdjustment('defaultRenderGlobals.imageFormat')
            mc.setAttr('defaultRenderGlobals.imageFormat', 51)
            mc.setAttr('defaultRenderGlobals.imfkey', 'exr', type='string')
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.setAttr('mentalrayGlobals.compressionQuality', 0)

            # 16位zip压缩
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.editRenderLayerAdjustment('miDefaultFramebuffer.datatype')
            mc.setAttr('miDefaultFramebuffer.datatype', 16)

            print (u'===============!!!Done  【%s】!!!===============' % (u'%s_CH层' % layerType))
            print '\n'
        else:
            print (u'===============!!!Error  【%s】无物体!!!===============' % (u'%s_CHR层' % layerType))
            print '\n'
    

    def zmRLLIGHTCHCreate(self, layerType, selectObjType=0):
        print (u'===============!!!Start 【%s】!!!===============' % (u'%s_CHR层' % layerType))
        print 'Working...'

        # 选取模式
        if selectObjType == 1:
            rlObjs = self.zmRLSelectMode()

        # 物体
        objs = self.zmRLObjectsTList()
        refCHR = objs[0]
        refPROP = objs[1]

        rlObjs = refCHR + refPROP
        lightFile = 'Z:/Projects/ZoomWhiteDolphin/Project/data/lightFiles/LIGHTING_CHR_INT.mb'
        light_grp = mc.ls('LIGHTING', type='transform')

        if mc.ls(light_grp):
            mc.delete(light_grp)

        mc.file(lightFile, i=1)

        layerName = ''
        # 灯光

        lights = []
        lightGrps = []
        needLightGrps01 = []
        needLightGrps03 = []
        needLightGrps05 = []
        needLightGrps07 = []
        needLightGrps08 = []
        needLightGrps09 = []

        needLightGrps_A = []
        needLightGrps_B = []
        needLightGrps_C = []
        needLightGrps_ABC = []

        if layerType == 'CHR':
            lights = mc.ls(type='light', l=1)
            if lights:
                for light in lights:
                    lightGrps.append(mc.listRelatives(light, p=1, type='transform', f=1)[0])
                if lightGrps:
                    for grp in lightGrps:
                        if 'DAY_CHR_A1' in grp:
                            needLightGrps01.append(grp)

                        if 'DAY_CHR_B1' in grp:
                            needLightGrps03.append(grp)

                        if 'DAY_CHR_C1' in grp:
                            needLightGrps05.append(grp)

                        if 'DAY_CHRB_A' in grp:
                            needLightGrps07.append(grp)
                        if 'DAY_CHRB_B' in grp:
                            needLightGrps08.append(grp)
                        if 'DAY_CHRB_C' in grp:
                            needLightGrps09.append(grp)

                needLightGrps_A = needLightGrps01
                needLightGrps_B = needLightGrps03
                needLightGrps_C = needLightGrps05
                needLightGrps_ABC = needLightGrps07 + needLightGrps08 + needLightGrps09

                if needLightGrps_A:
                    layerName = 'CHR_LGTA'
                    if mc.ls(layerName):
                        mc.delete(layerName)
                    mc.createRenderLayer((rlObjs + needLightGrps_A), name=layerName, noRecurse=1, makeCurrent=1)
                    mc.setAttr('defaultRenderGlobals.imageFormat', 51)
                    mc.setAttr('defaultRenderGlobals.imfkey', 'exr', type='string')

                if needLightGrps_B:
                    layerName = 'CHR_LGTB'
                    if mc.ls(layerName):
                        mc.delete(layerName)
                    mc.createRenderLayer((rlObjs + needLightGrps_B), name=layerName, noRecurse=1, makeCurrent=1)

                if needLightGrps_C:
                    layerName = 'CHR_LGTC'
                    if mc.ls(layerName):
                        mc.delete(layerName)
                    mc.createRenderLayer((rlObjs + needLightGrps_C), name=layerName, noRecurse=1, makeCurrent=1)

                if needLightGrps_ABC:
                    layerName = 'CHR_LGTRIM'
                    if mc.ls(layerName):
                        mc.delete(layerName)
                    mc.createRenderLayer((rlObjs + needLightGrps_ABC), name=layerName, noRecurse=1, makeCurrent=1)

        if rlObjs:
            # 透明信息
            transpancyObjs = self.zmRLTransparencyObjs()
            transpancySGNodes = transpancyObjs[0]
            transpancyMeshes = transpancyObjs[1]
            transpancyNode = transpancyObjs[2]

            from idmt.maya.py_common import sk_infoConfig
            reload(sk_infoConfig)
            import os

            # openSea是否在场景里
            checkAssetID = ['s019001']
            namespaces = mc.namespaceInfo(listOnlyNamespaces=1)
            checkState = 0
            for ID in checkAssetID:
                for ns in namespaces:
                    if ID in ns:
                        checkState = 1

            # 通用LGT材质

            if layerName == 'CHR_LGTRIM':
                shaderNode = 'SHD_' + layerType + '_LGT_Shader'
                if mc.ls(shaderNode):
                    mc.delete(shaderNode)

                LGTSG = 'SHD_' + layerType + '_LGT_SG'
                if mc.ls(LGTSG):
                    mc.delete(LGTSG)

                shaderNode = mc.shadingNode('lambert', asShader=True, name=shaderNode)
                mc.setAttr((shaderNode + '.color'), 1, 1, 1, type='double3')

                LGTSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=LGTSG)

                mc.connectAttr((shaderNode + '.outColor'), (LGTSG + '.surfaceShader'))

                # 优先全局着色
                for obj in rlObjs:
                    try:
                        mc.sets(obj, e=1, forceElement=LGTSG)
                    except:
                        # 获取物体面数
                        faceNum = mc.polyEvaluate(obj, face=1)
                        mc.sets((obj + u'.f[:' + str(faceNum - 1) + u']'), e=1, forceElement=LGTSG)

                if transpancySGNodes:
                    for i in range(len(transpancySGNodes)):
                        if mc.ls(transpancySGNodes[i]):
                            if '_' not in transpancySGNodes[i]:
                                print u'>>>>>>[注意][%s]名字需要最少有1个_分隔符' % transpancySGNodes[i]
                            else:
                                keySGInfo = transpancySGNodes[i].split('_')[-2]
                            keySGInfo = str(i)
                            meshes = transpancyMeshes[i]
                            # 有着色物体时才进行
                            if meshes:
                                shaderTrsNode = 'SHD_' + layerType + '_' + keySGInfo + '_LGT_Shader'
                                if mc.ls(shaderTrsNode):
                                    mc.delete(shaderTrsNode)
                                LGTTrsSG = 'SHD_' + layerType + '_' + keySGInfo + '_LGT_SG'
                                if mc.ls(LGTTrsSG):
                                    mc.delete(LGTTrsSG)

                                # 创建
                                shaderTrsNode = mc.shadingNode('lambert', asShader=True, name=shaderTrsNode)
                                mc.setAttr((shaderNode + '.color'), 1, 1, 1, type='double3')

                                LGTTrsSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=LGTTrsSG)

                                # 连接
                                mc.connectAttr((shaderTrsNode + '.outColor'), (LGTTrsSG + '.surfaceShader'))

                                # 透明连接
                                self.zmRLTransShaderConnectiion(transpancyNode[i], shaderTrsNode, 'transparency')

                                # file贴图反转
                                if '.outTransparency' in transpancyNode[i]:
                                    mc.editRenderLayerAdjustment(transpancyNode[i].split('.')[0] + '.invert')
                                    mc.setAttr((transpancyNode[i].split('.')[0] + ".invert"), 1)

                                # 连接着色
                                mc.editRenderLayerAdjustment(transpancySGNodes[i] + '.surfaceShader')
                                mc.connectAttr((shaderTrsNode + '.outColor'), (transpancySGNodes[i] + '.surfaceShader'), f=1)

                                # 着色
                                for mesh in meshes:
                                    if mc.objExists(mesh):
                                        try:
                                            mc.sets(mesh, e=1, forceElement=LGTTrsSG)
                                        except:
                                            if '.f[' not in mesh:
                                                # 获取物体面数
                                                obj = mc.listRelatives(mesh, p=1, f=1)[0]
                                                faceNum = mc.polyEvaluate(obj, face=1)
                                                try:
                                                    mc.sets((obj + u'.f[0:' + str(faceNum - 1) + u']'), e=1, forceElement=LGTTrsSG)
                                                except:
                                                    # 该死的maybug！！！再次分解
                                                    mc.sets((obj + u'.f[0:' + str(int(faceNum - 1) / 2) + u']'), e=1, forceElement=LGTTrsSG)
                                                    mc.sets((obj + u'.f[' + str(int(faceNum - 1) / 2 + 1) + ':' + str(faceNum - 1) + u']'), e=1, forceElement=LGTTrsSG)
                                            else:
                                                # print u'>-------------->'
                                                # print mesh
                                                # 获取面数
                                                faceInfo = mesh.split('.f[')[-1]
                                                if ':' in faceInfo:
                                                    faceInfoList = faceInfo.split(':')
                                                    faceNumPre = int(faceInfoList[0])
                                                    faceNumPos = int(faceInfoList[1][:-1])
                                                    # 该死的maybug！！！再次分解
                                                    if faceNumPos == faceNumPre + 1:
                                                        mc.sets((obj + u'.f[' + str(faceNumPre) + u']'), e=1, forceElement=LGTTrsSG)
                                                        mc.sets((obj + u'.f[' + str(faceNumPos) + u']'), e=1, forceElement=LGTTrsSG)
                                                    else:
                                                        mc.sets((obj + u'.f[' + str(faceNumPre) + ':' + str(int(faceNumPre + (faceNumPos - faceNumPre) / 2)) + u']'), e=1, forceElement=LGTTrsSG)
                                                        mc.sets((obj + u'.f[' + str(int(faceNumPre + 1 + (faceNumPos - faceNumPre) / 2)) + ':' + str(faceNumPos) + u']'), e=1, forceElement=LGTTrsSG)
                                                else:
                                                    mc.warning(u'--------------请检测[%s]---------------' % mesh)

            # 设置
            # self.zmRLCommonConfig()
            # 渲染设置
            mc.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')

            # 格式命名
            mc.setAttr('defaultRenderGlobals.animation', 1)
            mc.setAttr('defaultRenderGlobals.putFrameBeforeExt', 1)
            mc.setAttr('defaultRenderGlobals.periodInExt', 1)
            mc.setAttr('defaultRenderGlobals.extensionPadding', 4)
            if mc.getAttr('defaultRenderGlobals.outFormatControl') == 1:
                mc.setAttr('defaultRenderGlobals.outFormatControl', 0)

            # exr
            mc.editRenderLayerAdjustment('defaultRenderGlobals.imageFormat')
            mc.setAttr('defaultRenderGlobals.imageFormat', 51)
            mc.setAttr('defaultRenderGlobals.imfkey', 'exr', type='string')
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.setAttr('mentalrayGlobals.compressionQuality', 0)

            # 16位zip压缩
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.editRenderLayerAdjustment('miDefaultFramebuffer.datatype')
            mc.setAttr('miDefaultFramebuffer.datatype', 16)

            print (u'===============!!!Done  【%s】!!!===============' % (u'%s_CH层' % layerType))
            print '\n'
        else:
            print (u'===============!!!Error  【%s】无物体!!!===============' % (u'%s_CHR层' % layerType))
            print '\n'

    # SEA_SHADOW层
    # No Lights
    def zmRLSDCreate(self, layerType, selectObjType=0):
        print (u'===============!!!Start 【%s】!!!===============' % (u'%s_SHDW层' % layerType))
        print 'Working...'

        from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
        reload(sk_referenceConfig)
        # 物体
        objs = self.zmRLObjectsTList()
        refCHR = objs[0]
        refPROP = objs[1]
        refSET = objs[2]
        refSKY = objs[3]
        refSEA = objs[4]
        
        seaSG= self.zmRLSGNodesGet()
        SGCHR=seaSG[0]
        SGPROP=seaSG[1]
        SGSET=seaSG[2]
        #读参考
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        renamespace= refInfos[2][0]
        
        refername=''
        refernames=[]
        referencename=[]
        if renamespace:
            for refnames in renamespace:                        
               if '_' in refnames:
                   referencename.append(refnames)
        if referencename:
            for refnames in referencename:
                refername=refnames.split('_')[1]
                refernames.append(refername)
        
        specalsign=0       
        if refernames:
            for refname in refernames:
                if refname=='p00501surfing':
                    specalsign=1

        #灯光       
        lightGrps = []
        needLightGrps = []
        lightgup = []

        if specalsign==1:
            if mc.ls('LGT_DAY_KEY_01'):
                mc.delete('LGT_DAY_KEY_01')
            lightFile = 'Z:/Projects/ZoomWhiteDolphin/Reference/Sylvain/LIGHTING/p00501surfing.mb'
            mc.file(lightFile, i=1)          
            needLightGrps=['LGT_DAY_KEY_01']
        else:         
            lights = mc.ls(type='light', l=1)
            if lights:
                for light in lights:
                    lightGrps.append(mc.listRelatives(light, p=1, type='transform', f=1)[0])
            if lightGrps:
                if layerType == 'ALL' or layerType == 'SEA':
                    for grp in lightGrps:
                        if 'LGT_DAY_KEY' in grp:    
                            needLightGrps.append(grp)
                    if len(needLightGrps) >= 2:
                        for light in needLightGrps:
                            if mc.getAttr(light.split('|')[4] + ".v") == True:
                                lightgup.append(light)
                    if len(lightgup) >= 2:
                        mc.confirmDialog(title=u'警告', message=u'SEA_SHDW层可能存在多盏灯光，请自行隐藏其余灯光，点击YES OR NO继续分层', button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')

        # 物体
        rlObjs = []

        if layerType == 'SEA':
            rlObjs = refCHR + refPROP + refSET + refSEA
            needSG = SGSET + SGCHR + SGPROP
          
            layerName = 'SEA_SHDW'

        # 选取模式
        if selectObjType == 1:
            rlObjs = self.zmRLSelectMode()

        if rlObjs:

            # 特殊处理，半透明用
            # 获取信息必须在masterLayer进行
            transpancyObjs = self.zmRLTransparencyObjs()
            transpancySGNodes = transpancyObjs[0]
            transpancyMeshes = transpancyObjs[1]
            transpancyNode = transpancyObjs[2]

            # openSea是否在场景里
            checkAssetID = ['s019001']
            namespaces = mc.namespaceInfo(listOnlyNamespaces=1)
            checkState = 0
            for ID in checkAssetID:
                for ns in namespaces:
                    if ID in ns:
                        checkState = 1

            # 创建RenderLayer
            if mc.ls(layerName):
                mc.delete(layerName)

            mc.createRenderLayer((rlObjs + needLightGrps), name=layerName, noRecurse=1, makeCurrent=1)



            # 处理shadow
            mel.eval('renderLayerBuiltinPreset shadow ' + layerName)
            

            # SEA
            if layerType == 'SEA':
                # 非sea的All渲染关闭
                if refSET:
                    for obj in refSET:
                        mesh = mc.listRelatives(obj, ni=1, type='mesh', s=1, f=1)[0]
                        mc.editRenderLayerAdjustment(mesh + '.primaryVisibility')
                        mc.setAttr((mesh + '.primaryVisibility'), 0)
                        mc.editRenderLayerAdjustment(mesh + '.receiveShadows')
                        mc.setAttr((mesh + '.receiveShadows'), 0)

                if refCHR:
                    for obj in refCHR:
                        mesh = mc.listRelatives(obj, ni=1, type='mesh', s=1, f=1)[0]
                        mc.editRenderLayerAdjustment(mesh + '.primaryVisibility')
                        mc.setAttr((mesh + '.primaryVisibility'), 0)
                        mc.editRenderLayerAdjustment(mesh + '.receiveShadows')
                        mc.setAttr((mesh + '.receiveShadows'), 0)

                if refPROP:
                    for obj in refPROP:                     
                        mesh = mc.listRelatives(obj, ni=1, type='mesh', s=1, f=1)[0]
                        if specalsign==0:                                        
                            mc.editRenderLayerAdjustment(mesh + '.primaryVisibility')
                            mc.setAttr((mesh + '.primaryVisibility'), 0)
                            mc.editRenderLayerAdjustment(mesh + '.receiveShadows')
                            mc.setAttr((mesh + '.receiveShadows'), 0)

                if refSEA:
                    for obj in refSEA:
                        mesh = mc.listRelatives(obj, ni=1, type='mesh', s=1, f=1)[0]
                        if specalsign==0:
                            mc.editRenderLayerAdjustment(mesh + '.primaryVisibility')
                            mc.setAttr((mesh + '.primaryVisibility'), 1)
                            mc.editRenderLayerAdjustment(mesh + '.castsShadows')
                            mc.setAttr((mesh + '.castsShadows'), 0)
                            mc.editRenderLayerAdjustment(mesh + '.receiveShadows')
                            mc.setAttr((mesh + '.receiveShadows'), 1)

                # 不需要Sky
                if refSKY:
                    for obj in refSKY:
                        mc.editRenderLayerAdjustment(obj + '.visibility')
                        mc.setAttr((obj + '.visibility'), 0)

                # openSea在则隐藏
                if checkState:
                    lightingGrps = mc.ls('*:*LIGHTING', type='transform') + mc.ls('*:*:*LIGHTING', type='transform')
                    for ID in checkAssetID:
                        for grp in lightingGrps:
                            if ID not in grp:
                                mc.editRenderLayerAdjustment(grp + '.visibility')
                                mc.setAttr((grp + '.visibility'), 0)

                # shader
                shader_Node = 'SHD_SEA_SHDW'
                if mc.ls(shader_Node):
                    mc.delete(shader_Node)
  
                shader_Node = mc.shadingNode('lambert', asShader=True, name=shader_Node)

                # 优先全局着色
                if needSG:
                    for SGNode in needSG:
                        shaderInfo = mc.listConnections((SGNode + '.surfaceShader'),s = 1,plugs = 1)
                        if not shaderInfo:
                            continue
                        shaderInfo = shaderInfo[0]
                        mc.editRenderLayerAdjustment(SGNode + '.surfaceShader')
                        mc.disconnectAttr(shaderInfo, (SGNode + '.surfaceShader'))
                        mc.connectAttr((shader_Node + '.outColor'), (SGNode + '.surfaceShader'), f=1)
  
                if transpancySGNodes:
                    for i in range(len(transpancySGNodes)):
                        if mc.ls(transpancySGNodes[i]):
                            if '_' not in transpancySGNodes[i]:
                                print u'>>>>>>[注意][%s]名字需要最少有1个_分隔符' % transpancySGNodes[i]
                            else:
                                keySGInfo = transpancySGNodes[i].split('_')[-2]
                            keySGInfo = str(i)
                            meshes = transpancyMeshes[i]
                            # 有着色物体时才进行
                            if meshes:
                                shaderNode = 'SHD_' + layerType + '_' + keySGInfo + '_SEA_SHDW'
                                if mc.ls(shaderNode):
                                    mc.delete(shaderNode)
 
                                shaderNode = mc.shadingNode('lambert', asShader=True, name=shaderNode)
 
                                # 透明连接
                                self.zmRLTransShaderConnectiion(transpancyNode[i], shaderNode, 'transparency')

                                # 翻转
                                if '.outTransparency' in transpancyNode[i]:
                                    mc.editRenderLayerAdjustment(transpancyNode[i].split('.')[0] + '.invert')
                                    mc.setAttr((transpancyNode[i].split('.')[0] + ".invert"), 1)



                                # 着色
                                shaderInfo = mc.listConnections((transpancySGNodes[i] + '.surfaceShader'),s = 1,plugs = 1)
                                if shaderInfo:
                                    shaderInfo = shaderInfo[0]
                                    mc.editRenderLayerAdjustment(transpancySGNodes[i] + '.surfaceShader')
                                    mc.disconnectAttr(shaderInfo, (transpancySGNodes[i] + '.surfaceShader'))
                                    mc.connectAttr((shaderNode + '.outColor'), (transpancySGNodes[i] + '.surfaceShader'), f=1)
                                                                
  

            # 材质不理会
            # 设置
            # self.zmRLCommonConfig()
            # 渲染设置
            mc.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')
            # MR设置
            mc.editRenderLayerAdjustment('miDefaultOptions.rayTracing')
            mc.setAttr('miDefaultOptions.rayTracing', 1)
            mc.editRenderLayerAdjustment('miDefaultOptions.maxReflectionRays')
            mc.setAttr('miDefaultOptions.maxReflectionRays', 10)
            mc.editRenderLayerAdjustment('miDefaultOptions.maxRefractionRays')
            mc.setAttr('miDefaultOptions.maxRefractionRays', 10)
            mc.editRenderLayerAdjustment('miDefaultOptions.maxRayDepth')
            mc.setAttr('miDefaultOptions.maxRayDepth', 20)
            mc.editRenderLayerAdjustment('miDefaultOptions.maxShadowRayDepth')
            mc.setAttr('miDefaultOptions.maxShadowRayDepth', 2)
            mc.editRenderLayerAdjustment('miDefaultOptions.maxReflectionBlur')
            mc.setAttr('miDefaultOptions.maxReflectionBlur', 1)
            mc.editRenderLayerAdjustment('miDefaultOptions.maxRefractionBlur')
            mc.setAttr('miDefaultOptions.maxRefractionBlur', 1)

            # 格式命名
            mc.setAttr('defaultRenderGlobals.animation', 1)
            mc.setAttr('defaultRenderGlobals.putFrameBeforeExt', 1)
            mc.setAttr('defaultRenderGlobals.periodInExt', 1)
            mc.setAttr('defaultRenderGlobals.extensionPadding', 4)
            if mc.getAttr('defaultRenderGlobals.outFormatControl') == 1:
                mc.setAttr('defaultRenderGlobals.outFormatControl', 0)

            # exr
            mc.editRenderLayerAdjustment('defaultRenderGlobals.imageFormat')
            mc.setAttr('defaultRenderGlobals.imageFormat', 51)
            mc.setAttr('defaultRenderGlobals.imfkey', 'exr', type='string')
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.setAttr('mentalrayGlobals.compressionQuality', 0)

            # 16位zip压缩
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.editRenderLayerAdjustment('miDefaultFramebuffer.datatype')
            mc.setAttr('miDefaultFramebuffer.datatype', 16)

            print (u'===============!!!Done  【%s】!!!===============' % (u'%s_SHADOW层' % layerType))
            print '\n'

        else:
            print (u'===============!!!Error  【%s】无物体!!!===============' % (u'%s_SHADOW层' % layerType))
            print '\n'

    # BG_MASK02层
    def zmRLMskCreate(self, layerType, selectObjType=0):
        print (u'===============!!!Start 【%s】!!!===============' % (u'%s_MSK02层' % 'ALL'))
        print 'Working...'

        if layerType == 'BG':
            layerName = 'BG_MASK02'

        # 选取模式
        if selectObjType == 1:
            rlObjs = self.zmRLSelectMode()
        # 物体
        objs = self.zmRLObjectsTList()
        refCHR = objs[0]
        refPROP = objs[1]
        refSET = objs[2]
        refSKY = objs[3]
        refSEA = objs[4]
        
        
        MASKSG= self.zmRLSGNodesGet()
        SGCHR=MASKSG[0]
        SGPROP=MASKSG[1]
        SGSET=MASKSG[2]
        
        

        rlObjs = refSET + refSEA
        objgrps = []
        if rlObjs:
            for obj in rlObjs:
                if obj not in refSKY:
                    objgrps.append(obj)
            rlObjs = objgrps

        seaObjs = []
        seaOjs_meshNeed = []
        if mc.ls("*:*SEA", type='objectSet'):
            seaSet = mc.ls("*:*SEA", type='objectSet')
            if seaSet:
                seaObjs = mc.sets(seaSet, q=1)
            if seaObjs:
                seaOjs_meshNeed = mc.listRelatives(seaObjs, ad=1, type='mesh', ni=1,f=1)
        else:
            mc.confirmDialog(title=u'警告', message=u'确定场景中有SET组SEA吗，不会你优化场景给删掉了吧', button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')

        seaObjs = mc.listRelatives(seaOjs_meshNeed, p=1, type='transform', f=1)

        rockObjs = []
        rockObjs_meshNeed = []
        if mc.ls("*:*ROCK", type='objectSet'):
            rockSet = mc.ls("*:*ROCK", type='objectSet')
            if rockSet:
                rockObjs = mc.sets(rockSet, q=1)
            if rockObjs:
                rockObjs_meshNeed = mc.listRelatives(rockObjs, ad=1, type='mesh', ni=1,f=1)
        else:
            mc.confirmDialog(title=u'警告', message=u'确定场景中有SET组ROCK吗，不会你优化场景给删掉了吧', button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')

        rockObjs = mc.listRelatives(rockObjs_meshNeed, p=1, type='transform', f=1)

        vegetaObjs = []
        vegetaObjs_meshNeed = []
        if mc.ls("*:*VEGETATION", type='objectSet'):
            vegetaSet = mc.ls("*:*VEGETATION", type='objectSet')
            if vegetaSet:
                vegetaObjs = mc.sets(vegetaSet, q=1)
            if vegetaObjs:
                vegetaObjs_meshNeed = mc.listRelatives(vegetaObjs, ad=1, type='mesh', ni=1,f=1)
        else:
            mc.confirmDialog(title=u'警告', message=u'确定场景中有SET组VEGETATION吗，不会你优化场景给删掉了吧', button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')

        vegetaObjs = mc.listRelatives(vegetaObjs_meshNeed, p=1, type='transform', f=1)

        objsAll = rlObjs
        objsR = []
        objsG = vegetaObjs
        objsB = rockObjs
        
        if objsAll:

            # 特殊处理，半透明用
            # 获取信息必须在masterLayer进行
            transpancyObjs = self.zmRLTransparencyObjs()
            transpancySGNodes = transpancyObjs[0]
            transpancyMeshes = transpancyObjs[1]
            transpancyNode = transpancyObjs[2]

            # 创建RenderLayer
            if mc.ls(layerName):
                mc.delete(layerName)

            mc.createRenderLayer(objsAll, name=layerName, noRecurse=1, makeCurrent=1)
            # mc.editRenderLayerGlobals(currentRenderLayer=layerName)

            SGNode = ''
            SGNodes = []
            if mc.ls('*:*SEA', type='objectSet'):
                if mc.ls('*:*MSH_c_hi_temp_sea_MSK_', type='transform'):
                    obj = mc.ls('*:*MSH_c_hi_temp_sea_MSK_', type='transform')
                    objMESH = mc.listRelatives(obj, ad=1, type='mesh', f=1)
                    SGNodes = mc.listConnections(objMESH, type='shadingEngine', d=1)
                    if SGNodes:
                        SGNode = SGNodes[0]
                else:
                    mc.confirmDialog(title=u'警告', message=u'请确定场景中有SET组SEA中命名有其中“MSH_c_hi_temp_sea_MSK_”字符段，', button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')

            if refSKY:
                for obj in refSKY:
                    #mesh = mc.listRelatives(obj, ni=1, type='mesh', s=1, f=1)[0]
                    meshTemp = mc.listRelatives(obj, ni=1, type='mesh', s=1, f=1)
                    if meshTemp :
                        mesh = meshTemp[0]
                        mc.editRenderLayerAdjustment(mesh + '.primaryVisibility')
                        mc.setAttr((mesh + '.primaryVisibility'), 0)

            # 通用RGB材质
            shaderRNode = 'SHD_' + layerType + '_R_Shader'
            if mc.ls(shaderRNode):
                mc.delete(shaderRNode)
            shaderGNode = 'SHD_' + layerType + '_G_Shader'
            if mc.ls(shaderGNode):
                mc.delete(shaderGNode)
            shaderBNode = 'SHD_' + layerType + '_B_Shader'
            if mc.ls(shaderBNode):
                mc.delete(shaderBNode)
            shaderMNode = 'SHD_' + layerType + '_M_Shader'
            if mc.ls(shaderMNode):
                mc.delete(shaderMNode)

            shaderRSG = 'SHD_' + layerType + '_R_SG'
            if mc.ls(shaderRSG):
                mc.delete(shaderRSG)

            shaderGSG = 'SHD_' + layerType + '_G_SG'
            if mc.ls(shaderGSG):
                mc.delete(shaderGSG)
            shaderBSG = 'SHD_' + layerType + '_B_SG'
            if mc.ls(shaderBSG):
                mc.delete(shaderBSG)
            shaderMSG = 'SHD_' + layerType + '_M_SG'
            if mc.ls(shaderMSG):
                mc.delete(shaderMSG)

            shaderRNode = mc.shadingNode('lambert', asShader=True, name=shaderRNode)
            mc.setAttr((shaderRNode + '.color'), 1, 0, 0, type='double3')
            mc.setAttr((shaderRNode + '.ambientColor'), 1, 1, 1, type='double3')
            mc.setAttr((shaderRNode + '.diffuse'), 0)
            mc.setAttr((shaderRNode + '.matteOpacity'), 0)
            shaderGNode = mc.shadingNode('lambert', asShader=True, name=shaderGNode)
            mc.setAttr((shaderGNode + '.color'), 0, 1, 0, type='double3')
            mc.setAttr((shaderGNode + '.ambientColor'), 1, 1, 1, type='double3')
            mc.setAttr((shaderGNode + '.diffuse'), 0)
            mc.setAttr((shaderGNode + '.matteOpacity'), 0)
            shaderBNode = mc.shadingNode('lambert', asShader=True, name=shaderBNode)
            mc.setAttr((shaderBNode + '.color'), 0, 0, 1, type='double3')
            mc.setAttr((shaderBNode + '.ambientColor'), 1, 1, 1, type='double3')
            mc.setAttr((shaderBNode + '.diffuse'), 0)
            mc.setAttr((shaderBNode + '.matteOpacity'), 0)
            shaderMNode = mc.shadingNode('lambert', asShader=True, name=shaderMNode)
            mc.setAttr((shaderMNode + '.color'), 0, 0, 0, type='double3')
            mc.setAttr((shaderMNode + '.matteOpacityMode'), 0)

            shaderRSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=shaderRSG)
            shaderGSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=shaderGSG)
            shaderBSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=shaderBSG)
            shaderMSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=shaderMSG)

            mc.connectAttr((shaderRNode + '.color'), (shaderRSG + '.surfaceShader'))
            mc.connectAttr((shaderGNode + '.color'), (shaderGSG + '.surfaceShader'))
            mc.connectAttr((shaderBNode + '.color'), (shaderBSG + '.surfaceShader'))
            mc.connectAttr((shaderMNode + '.color'), (shaderMSG + '.surfaceShader'))

            # 优先全局着色，赋予Mask

            for obj in objsAll:
                try:
                    mc.sets(obj, e=1, forceElement=shaderMSG)
                except:
                    # 获取物体面数
                    faceNum = mc.polyEvaluate(obj, face=1)
                    mc.sets((obj + u'.f[:' + str(faceNum - 1) + u']'), e=1, forceElement=shaderMSG)
                if obj in refSEA:
                    for sea in refSEA:
                        mc.select(sea)
                        mc.sets(e=1, forceElement=SGNode)
            
            if objsG:
                for obj in objsG:
                    try:
                        mc.sets(obj, e=1, forceElement=shaderGSG)                       
                    except:
                        # 获取物体面数
                        faceNum = mc.polyEvaluate(obj, face=1)
                        mc.sets((obj + u'.f[:' + str(faceNum - 1) + u']'), e=1, forceElement=shaderGSG)
                         
            if objsB:
                for obj in objsB:

                    try:
                        mc.sets(obj, e=1, forceElement=shaderBSG)
                    except:
                        # 获取物体面数
                        faceNum = mc.polyEvaluate(obj, face=1)
                        mc.sets((obj + u'.f[:' + str(faceNum - 1) + u']'), e=1, forceElement=shaderBSG)
 

 
            if transpancySGNodes:
                for i in range(len(transpancySGNodes)):
                    if mc.ls(transpancySGNodes[i]):
                        if '_' not in transpancySGNodes[i]:
                            print u'>>>>>>[注意][%s]名字需要最少有1个_分隔符' % transpancySGNodes[i]
                        else:
                            keySGInfo = transpancySGNodes[i].split('_')[-2]
                        keySGInfo = str(i)
                        meshes = transpancyMeshes[i]
                        # 不对！！！！！
                        # 有着色物体时才进行，处理对有相同透明材质的物体使用不同的RGBM
                        if meshes:
                            meshesR = []
                            meshesG = []
                            meshesB = []
                            meshesM = []
                            needColor = [[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]]
                            needRGBInfo = ['M', 'R', 'G', 'B']
                            for mesh in meshes:
                                if not mc.objExists(mesh):
                                    continue
                                meshGrp = ''
                                if '.f[' in mesh:
                                    meshGrp = mc.ls(mesh.split('.f[')[0],l=1)[0]
                                else:
                                    meshGrp = mc.listRelatives(mesh, p=1, f=1,type = 'transform')[0]
                                RGBInfo = ''
                                if meshGrp in objsR:
                                    meshesR.append(mesh)
                                if meshGrp in objsG:
                                    # 海不要透明通道
                                    if '_sea_' not in mesh:
                                        meshesG.append(mesh)
                                if meshGrp in objsB:
                                    meshesB.append(mesh)
                                if meshGrp not in (objsR + objsG + objsB):
                                    # 海不要透明通道
                                    if '_sea_' not in mesh:
                                        meshesM.append(mesh)
                                           
                            for j in range(4):
                                if j == 0:
                                    needMeshes = meshesM
                                if j == 1:
                                    needMeshes = meshesR
                                if j == 2:
                                    needMeshes = meshesG
                                if j == 3:
                                    needMeshes = meshesB
                                RGBInfo = needRGBInfo[j]
                                color = needColor[j]

                                if not needMeshes:
                                    continue

                                shaderTrsNode = 'SHD_' + layerType + '_' + keySGInfo + '_' + RGBInfo + '_Shader'
                                if mc.ls(shaderTrsNode):
                                    pass
                                else:
                                    shaderTrsNode = mc.shadingNode('lambert', asShader=True, name=shaderTrsNode)

                                shaderTrsSG = 'SHD_' + layerType + '_' + keySGInfo + '_' + RGBInfo + '_SG'
                                if mc.ls(shaderTrsSG):
                                    pass
                                else:
                                    shaderTrsSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=shaderTrsSG)


                                if RGBInfo in ['R', 'G', 'B']:

                                    mc.setAttr((shaderTrsNode + '.color'), color[0], color[1], color[2], type='double3')
                                    mc.setAttr((shaderTrsNode + '.ambientColor'), 1, 1, 1, type='double3')
                                    mc.setAttr((shaderTrsNode + '.diffuse'), 0)
                                    mc.setAttr((shaderTrsNode + '.matteOpacity'), 0)

                                if RGBInfo == 'M':
                                    mc.setAttr((shaderTrsNode + '.color'), 0, 0, 0, type='double3')
                                    mc.setAttr((shaderTrsNode + '.matteOpacityMode'), 0)


                                try:
                                    mc.connectAttr((shaderTrsNode + '.outColor'), (shaderTrsSG + '.surfaceShader'))
                                except:
                                    pass

                                # 透明连接
                                self.zmRLTransShaderConnectiion(transpancyNode[i], shaderTrsNode, 'transparency')

                                # 翻转
                                if '.outTransparency' in transpancyNode[i]:
                                    mc.editRenderLayerAdjustment(transpancyNode[i].split('.')[0] + '.invert')
                                    mc.setAttr((transpancyNode[i].split('.')[0] + ".invert"), 1)

                                if needMeshes:
                                    for mesh in needMeshes:
                                        if mc.ls(mesh):
                                            try:
                                                mc.sets(mesh, e=1, forceElement=shaderTrsSG)
                                            except:
                                                # 获取物体面数
                                                try:
                                                    obj = mc.listRelatives(mesh, p=1, f=1)[0]
                                                    faceNum = mc.polyEvaluate(obj, face=1)
                                                    mc.sets((obj + u'.f[:' + str(faceNum - 1) + u']'), e=1, forceElement=shaderTrsSG)
                                                except:     
                                                    pass


                                    

            # 设置
            # self.zmRLCommonConfig()
            # 渲染设置
            mc.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')

            # 关闭光线追踪
            mc.editRenderLayerAdjustment('miDefaultOptions.rayTracing')
            mc.setAttr('miDefaultOptions.rayTracing', 0)

            # 格式命名
            mc.setAttr('defaultRenderGlobals.animation', 1)
            mc.setAttr('defaultRenderGlobals.putFrameBeforeExt', 1)
            mc.setAttr('defaultRenderGlobals.periodInExt', 1)
            mc.setAttr('defaultRenderGlobals.extensionPadding', 4)
            if mc.getAttr('defaultRenderGlobals.outFormatControl') == 1:
                mc.setAttr('defaultRenderGlobals.outFormatControl', 0)

            # exr
            mc.editRenderLayerAdjustment('defaultRenderGlobals.imageFormat')
            mc.setAttr('defaultRenderGlobals.imageFormat', 51)
            mc.setAttr('defaultRenderGlobals.imfkey', 'exr', type='string')
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.setAttr('mentalrayGlobals.compressionQuality', 0)

            # 16位zip压缩
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.editRenderLayerAdjustment('miDefaultFramebuffer.datatype')
            mc.setAttr('miDefaultFramebuffer.datatype', 16)

            print (u'===============!!!Done  【%s】!!!===============' % (u'%s_MSK02层' % 'ALL'))
            print '\n'
        else:
            print (u'===============!!!Error  【%s】无物体!!!===============' % (u'%s_MSK02层' % 'ALL'))
            print '\n'

    # SEA_CP层
    def zmSEAcoCreate(self, layerType, selectObjType=0):
        print (u'===============!!!Start 【%s】!!!===============' % (u'%s_CP层' % layerType))
        print 'Working...'

        # 物体
        objs = self.zmRLObjectsTList()
        refCHR = objs[0]
        refPROP = objs[1]
        refSET = objs[2]
        refSKY = objs[3]
        refSEA = objs[4]

        rlObjs = []

        # 物体
        if refSEA:
            rlObjs = refSEA
        if layerType == 'SEA':
            layerName = 'SEA_CP'

        needSEA=[]
        if refSEA:
            for obj in refSEA:
                if '_p00501surfing_' in obj:
                    needSEA.append(obj)

        # 选取模式
 

        if rlObjs:                                      
            # sea
            if layerType == 'SEA':
                # 创建RenderLayer
                if layerName == 'SEA_CP':
                    if mc.ls(layerName):
                        mc.delete(layerName)
                if needSEA==[]:             
                    objSG = ''
                    objSGs = []
    
                    if mc.ls('*:*SEA', type='objectSet'):
                        if mc.ls('*:*MSH_c_hi_temp_sea_CO_', type='transform'):
                            obj = mc.ls('*:*MSH_c_hi_temp_sea_CO_', type='transform')
                            objMESH = mc.listRelatives(obj, ad=1, type='mesh', f=1)
                            objSGs = mc.listConnections(objMESH, type='shadingEngine', d=1)
                            if objSGs:
                                objSG = objSGs[0]
                        else:
                            mc.confirmDialog(title=u'警告', message=u'请确定场景中有SET组SEA中命名有其中“MSH_c_hi_temp_sea_CO_”字符段，', button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')
                    else:
                        mc.confirmDialog(title=u'警告', message=u'请确定场景中有SET组SEA,即使创建成功渲染层材质也是不正确的', button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')
    
                    if objSG:
                        for obj in rlObjs:
                            mc.select(obj)
                            mc.sets(e=1, forceElement=objSG)

                mc.createRenderLayer(rlObjs, name=layerName, noRecurse=1, makeCurrent=1)
                mc.editRenderLayerGlobals(currentRenderLayer=layerName)

            # 格式命名
            mc.setAttr('defaultRenderGlobals.animation', 1)
            mc.setAttr('defaultRenderGlobals.putFrameBeforeExt', 1)
            mc.setAttr('defaultRenderGlobals.periodInExt', 1)
            mc.setAttr('defaultRenderGlobals.extensionPadding', 4)
            if mc.getAttr('defaultRenderGlobals.outFormatControl') == 1:
                mc.setAttr('defaultRenderGlobals.outFormatControl', 0)

            # exr
            mc.editRenderLayerAdjustment('defaultRenderGlobals.imageFormat')
            mc.setAttr('defaultRenderGlobals.imageFormat', 51)
            mc.setAttr('defaultRenderGlobals.imfkey', 'exr', type='string')
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.setAttr('mentalrayGlobals.compressionQuality', 0)

            # 16位zip压缩
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.editRenderLayerAdjustment('miDefaultFramebuffer.datatype')
            mc.setAttr('miDefaultFramebuffer.datatype', 16)
            mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')
            mc.setAttr("defaultRenderLayer.renderable", 0)

            print (u'===============!!!Done  【%s】!!!===============' % (u'%s_CP层' % layerType))
            print '\n'

        else:
            print (u'===============!!!Error  【%s】无物体!!!===============' % (u'%s_CP层' % layerType))
            print '\n'
            
    #SEA_COa        
    def zmRLSEACOaCreate(self, layerType, selectObjType=0):
        print (u'===============!!!Start 【%s】!!!===============' %
               (u'%s_COa层' % layerType))
        print 'Working...'
        
        
        rlObjs=''
        OBJFile=''
        

        if layerType=='SEA':          
            layerName = 'SEA_COa'
        if mc.ls('MSH_Sea_c_hi_Animated_TX_'):
            mc.delete('MSH_Sea_c_hi_Animated_TX_')

        
        OBJFile = 'Z:/Projects/ZoomWhiteDolphin/Reference/Sylvain/LIGHTING/zm_101_lr_SeaColor_Above_c001.mb'                   
        rlObjs = 'MSH_Sea_c_hi_Animated_TX_'


        # 创建渲染层
        if rlObjs:                              
            ns = 'FoodTemp'
            mc.file(OBJFile, i=1, namespace=ns)
            # 使得namespace成为空的namespace
            mc.namespace(force=1, moveNamespace=[(':' + ns), ':'])
            # 清理空namespace
            mc.namespace(removeNamespace=(':' + ns))

            # 创建渲染层
            if mc.ls(layerName):
                mc.delete(layerName)
            mc.createRenderLayer(rlObjs, name=layerName, noRecurse=1, makeCurrent=1)


    
            # 加载MR
            if mc.pluginInfo('Mayatomr.mll', q=1, loaded=1):
                mel.eval('loadPlugin "Mayatomr.mll"')
                mc.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')
            # MR设置
            mc.editRenderLayerAdjustment('miDefaultOptions.rayTracing')
            mc.setAttr('miDefaultOptions.rayTracing', 1)
            mc.editRenderLayerAdjustment('miDefaultOptions.maxReflectionRays')
            mc.setAttr('miDefaultOptions.maxReflectionRays', 10)
            mc.editRenderLayerAdjustment('miDefaultOptions.maxRefractionRays')
            mc.setAttr('miDefaultOptions.maxRefractionRays', 10)
            mc.editRenderLayerAdjustment('miDefaultOptions.maxRayDepth')
            mc.setAttr('miDefaultOptions.maxRayDepth', 20)
            mc.editRenderLayerAdjustment('miDefaultOptions.maxShadowRayDepth')
            mc.setAttr('miDefaultOptions.maxShadowRayDepth', 2)
            mc.editRenderLayerAdjustment('miDefaultOptions.maxReflectionBlur')
            mc.setAttr('miDefaultOptions.maxReflectionBlur', 1)
            mc.editRenderLayerAdjustment('miDefaultOptions.maxRefractionBlur')
            mc.setAttr('miDefaultOptions.maxRefractionBlur', 1)
        
            # 格式命名
            mc.setAttr('defaultRenderGlobals.animation', 1)
            mc.setAttr('defaultRenderGlobals.putFrameBeforeExt', 1)
            mc.setAttr('defaultRenderGlobals.periodInExt', 1)
            mc.setAttr('defaultRenderGlobals.extensionPadding', 4)
            if mc.getAttr('defaultRenderGlobals.outFormatControl') == 1:
                mc.setAttr('defaultRenderGlobals.outFormatControl', 0)
        
            # exr
            mc.editRenderLayerAdjustment('defaultRenderGlobals.imageFormat')
            mc.setAttr('defaultRenderGlobals.imageFormat', 51)
            mc.setAttr('defaultRenderGlobals.imfkey', 'exr', type='string')
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.setAttr('mentalrayGlobals.compressionQuality', 0)
        
            # 16位zip压缩
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.editRenderLayerAdjustment('miDefaultFramebuffer.datatype')
            mc.setAttr('miDefaultFramebuffer.datatype', 16)
            mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')
            mc.setAttr("defaultRenderLayer.renderable", 0)
        
            print (u'===============!!!Done  【%s】!!!===============' % (u'%s_COa层' % layerType))
            print '\n'
        
        else:
            print (u'===============!!!Error  【%s】无物体!!!===============' % (u'%s_COa层' % layerType))
            print '\n'
            
            
    #SEA_COu        
    def zmRLSEACObCreate(self, layerType, selectObjType=0):
        print (u'===============!!!Start 【%s】!!!===============' %
               (u'%s_COb层' % layerType))
        print 'Working...'
        
        
        from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
        reload(sk_referenceConfig) 
                       
        rlObjs=''
        
        #参考名称
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        renamespace= refInfos[2][0]
        
        refername=''
        refernames=[]
        referencename=[]
        namesrefers=[]
        if renamespace:
            for refnames in renamespace:                        
               if '_' in refnames:
                   referencename.append(refnames)
        if referencename:
            for refnames in referencename:
                refername=refnames.split('_')[1]
                refernames.append(refername)
        
        #判断是否是场景名        
        if refernames:
            for refer in refernames:
                if refer[0]=='s':
                    namesrefers.append(refer)
        refernames=namesrefers
                        
        if len(refernames)==0:
            mc.confirmDialog(title=u'警告', message=u'请确保文件中有场景参考，可不必勾选但不能移除', button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')
  
        if len(refernames)>=2:
             mc.confirmDialog(title=u'警告', message=u'文件中可能存在两个以上场景参考，请移除多余场景参考，只保留需要的一个', button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')           
             
        if mc.ls('MSH_Sea_c_hi_Animated_TX_Under_'):            
            mc.delete('MSH_Sea_c_hi_Animated_TX_Under_')
            
        if mc.ls('MSH_Sea_c_hi_Animated_TX_'):            
            mc.delete('MSH_Sea_c_hi_Animated_TX_')            
                        
        if mc.ls('Shader_place3dTexture1'):            
            mc.delete('Shader_place3dTexture1')               
        #指定文件夹下的文件
        filenames=[]
        filename=''
        oceannames=[]
        oceanpath='Z:/Projects/ZoomWhiteDolphin/Reference/Sylvain/SEA/'
        fileslist=mc.getFileList(folder= oceanpath)
        
        if fileslist:
            for files in fileslist:
                    filename=files.split('.')[0]
                    filenames.append(filename)       
 
        #文件夹下文件与场景参考名称做对比       
        for refnames in refernames:
            for filename in filenames:
                if refnames == filename:
                    oceannames.append(filename)
                        

        print  oceannames   
        OBJFile=''
        if len(refernames)==1:
            if oceannames:
                if len(oceannames)==1:
                   OBJFile = oceanpath+oceannames[0]+'.mb'
                   rlObjs = 'MSH_Sea_c_hi_Animated_TX_'
                   
                if len(oceannames)>1:
                   print "是不是文件夹下放相同的文件名的文件"
           
            else:         
                OBJFile = 'Z:/Projects/ZoomWhiteDolphin/Reference/Sylvain/LIGHTING/zm_101_lr_SeaColor_Under_c001.mb'
                rlObjs = 'MSH_Sea_c_hi_Animated_TX_Under_'  
              
        if layerType=='SEA':          
            layerName = 'SEA_COu'                            

        # 创建渲染层
        if rlObjs:                              
            ns = 'FoodTemp'
            mc.file(OBJFile, i=1, namespace=ns)
            # 使得namespace成为空的namespace
            mc.namespace(force=1, moveNamespace=[(':' + ns), ':'])
            # 清理空namespace
            mc.namespace(removeNamespace=(':' + ns))

            # 创建渲染层
            if mc.ls(layerName):
                mc.delete(layerName)
            mc.createRenderLayer(rlObjs, name=layerName, noRecurse=1, makeCurrent=1)
    
            # 加载MR
            if mc.pluginInfo('Mayatomr.mll', q=1, loaded=1):
                mel.eval('loadPlugin "Mayatomr.mll"')
                mc.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')
            # MR设置
            mc.editRenderLayerAdjustment('miDefaultOptions.rayTracing')
            mc.setAttr('miDefaultOptions.rayTracing', 1)
            mc.editRenderLayerAdjustment('miDefaultOptions.maxReflectionRays')
            mc.setAttr('miDefaultOptions.maxReflectionRays', 10)
            mc.editRenderLayerAdjustment('miDefaultOptions.maxRefractionRays')
            mc.setAttr('miDefaultOptions.maxRefractionRays', 10)
            mc.editRenderLayerAdjustment('miDefaultOptions.maxRayDepth')
            mc.setAttr('miDefaultOptions.maxRayDepth', 20)
            mc.editRenderLayerAdjustment('miDefaultOptions.maxShadowRayDepth')
            mc.setAttr('miDefaultOptions.maxShadowRayDepth', 2)
            mc.editRenderLayerAdjustment('miDefaultOptions.maxReflectionBlur')
            mc.setAttr('miDefaultOptions.maxReflectionBlur', 1)
            mc.editRenderLayerAdjustment('miDefaultOptions.maxRefractionBlur')
            mc.setAttr('miDefaultOptions.maxRefractionBlur', 1)
        
            # 格式命名
            mc.setAttr('defaultRenderGlobals.animation', 1)
            mc.setAttr('defaultRenderGlobals.putFrameBeforeExt', 1)
            mc.setAttr('defaultRenderGlobals.periodInExt', 1)
            mc.setAttr('defaultRenderGlobals.extensionPadding', 4)
            if mc.getAttr('defaultRenderGlobals.outFormatControl') == 1:
                mc.setAttr('defaultRenderGlobals.outFormatControl', 0)
        
            # exr
            mc.editRenderLayerAdjustment('defaultRenderGlobals.imageFormat')
            mc.setAttr('defaultRenderGlobals.imageFormat', 51)
            mc.setAttr('defaultRenderGlobals.imfkey', 'exr', type='string')
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.setAttr('mentalrayGlobals.compressionQuality', 0)
        
            # 16位zip压缩
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.editRenderLayerAdjustment('miDefaultFramebuffer.datatype')
            mc.setAttr('miDefaultFramebuffer.datatype', 16)
            mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')
            mc.setAttr("defaultRenderLayer.renderable", 0)
        
            print (u'===============!!!Done  【%s】!!!===============' % (u'%s_COb层' % layerType))
            print '\n'
        
        else:
            print (u'===============!!!Error  【%s】无物体!!!===============' % (u'%s_COb层' % layerType))
            print '\n'
   
            
    # CHR_CAUSTICS,BG_CAUSTICS层
    # No Lights
    def zmRLCausticsCreate(self, layerType, selectObjType=0):
        print (u'===============!!!Start 【%s】!!!===============' %
               (u'%s_CAUSTICS层' % layerType))
        print 'Working...'

        # 物体
        objs = self.zmRLObjectsTList()
        refCHR = objs[0]
        refPROP = objs[1]
        refSET = objs[2]
        refSKY = objs[3]
        refSEA = objs[4]
        
        CausticSG= self.zmRLSGNodesGet()
        SGCHR=CausticSG[0]
        SGPROP=CausticSG[1]
        SGSET=CausticSG[2]

        # SEA_,ALL_,CHR_,BG_,FG_

        # 灯光

        lightGrps = []
        causticLight = ''

        lights = mc.ls(type='light', l=1)
        lightGrps = []
        needLightGrps = []
        needLightGrps01 = []
        needLightGrps02 = []
        lightFile=''
        
        if lights:
            for light in lights:
                lightGrps.append(mc.listRelatives(light, p=1, type='transform', f=1)[0])
        if lightGrps:
            for grp in lightGrps:
                if 'BG_Caustics_LGT' in grp:
                    needLightGrps01.append(grp)
    
            for grp in lightGrps:
                if 'CHR_Caustics_LGT' in grp:
                    needLightGrps02.append(grp)
                
               
        # 物体
        rlObjs = []
        objgrps02=[]
        objgrps = []
        needSG= []
        if layerType == 'BG':
            rlObjs = refSET
            needSG = SGSET
            if rlObjs:
                for obj in rlObjs:
                    if '_sea_' not in obj:
                        objgrps.append(obj)
                    if 'zm_s039001ForbiddenCave_h:MSH_c_hi_sea_' in obj:
                        objgrps02.append(obj)
            rlObjs = objgrps+objgrps02
            layerName = 'BG_CAUSTICS'
            if needLightGrps01:
                needLightGrps = needLightGrps01
            else:
                lightFile = 'Z:/Projects/ZoomWhiteDolphin/ZoomWhiteDolphin_Scratch/TD/LIGHTING/zm_lightsCaustics.mb'
                causticLight = 'BG_Caustics_LGT'
                
       
        if layerType == 'CHR':
            rlObjs = refPROP + refCHR
            needSG = SGCHR + SGPROP
            layerName = 'CHR_CAUSTICS'
            if needLightGrps02:
                needLightGrps = needLightGrps02
            else:
                lightFile = 'Z:/Projects/ZoomWhiteDolphin/ZoomWhiteDolphin_Scratch/TD/LIGHTING/zm_lightsCaustics.mb'
                causticLight = 'CHR_Caustics_LGT'
    
        # 选取模式

        if selectObjType == 1:
            rlObjs = self.zmRLSelectMode()


        if rlObjs:
            # 特殊处理，半透明用
            # 获取信息必须在masterLayer进行
            transpancyObjs = self.zmRLTransparencyObjs()
            transpancySGNodes = transpancyObjs[0]
            transpancyMeshes = transpancyObjs[1]
            transpancyNode = transpancyObjs[2]

            # openSea是否在场景里
            checkAssetID = ['s019001']
            namespaces = mc.namespaceInfo(listOnlyNamespaces=1)
            checkState = 0
            for ID in checkAssetID:
                for ns in namespaces:
                    if ID in ns:
                        checkState = 1

            # 灯光导入
            if mc.ls(causticLight):
                mc.delete(causticLight)

            if lightFile:
                ns = 'FoodTemp'
                mc.file(lightFile, i=1, namespace=ns)
                # 使得namespace成为空的namespace
                mc.namespace(force=1, moveNamespace=[(':' + ns), ':'])
                # 清理空namespace
                mc.namespace(removeNamespace=(':' + ns))
            

            # 创建渲染层
            if mc.ls(layerName):
                mc.delete(layerName)
            if needLightGrps:
                mc.createRenderLayer((rlObjs + needLightGrps), name=layerName, noRecurse=1, makeCurrent=1)
            else:
                mc.createRenderLayer((rlObjs + [causticLight]), name=layerName, noRecurse=1, makeCurrent=1)
                

            # 非sea的All渲染关闭
            if rlObjs:
                for obj in rlObjs:
                    mesh = mc.listRelatives(obj, ni=1, type='mesh', s=1, f=1)[0]
                    mc.editRenderLayerAdjustment(mesh + '.primaryVisibility')

            # 不需要Sky
            if refSKY:
                for obj in refSKY:
                    mc.editRenderLayerAdjustment(obj + '.visibility')
                    mc.setAttr((obj + '.visibility'), 0)
            # openSea在则隐藏
            if checkState:
                lightingGrps = mc.ls('*:*LIGHTING', type='transform') + mc.ls('*:*:*LIGHTING', type='transform')
                for ID in checkAssetID:
                    for grp in lightingGrps:
                        if ID not in grp:
                            mc.editRenderLayerAdjustment(grp + '.visibility')
                            mc.setAttr((grp + '.visibility'), 0)

            # shader
            if layerType == 'BG':
                shader_Node = 'SHD_Caustics_BG'
             
               
            if layerType == 'CHR':
                shader_Node = 'SHD_Caustics_CHR'
 
                
            if mc.ls(shader_Node):
                mc.delete(shader_Node)    
            shader_Node = mc.shadingNode('lambert', asShader=True, name=shader_Node)
            mc.setAttr(shader_Node + '.color', 1, 1, 1, type='double3')  
            
            if needSG:
                for SGNode in needSG:
                    shaderInfo = mc.listConnections((SGNode + '.surfaceShader'),s = 1,plugs = 1)
                    if not shaderInfo:
                        continue
                    shaderInfo = shaderInfo[0]
                    mc.editRenderLayerAdjustment(SGNode + '.surfaceShader')
                    mc.disconnectAttr(shaderInfo, (SGNode + '.surfaceShader'))
                    mc.connectAttr((shader_Node + '.outColor'), (SGNode + '.surfaceShader'), f=1)   
          

            # 特殊物体着色
            if transpancySGNodes:
                for i in range(len(transpancySGNodes)):
                    if mc.ls(transpancySGNodes[i]):
                        if '_' not in transpancySGNodes[i]:
                            print u'>>>>>>[注意][%s]名字需要最少有1个_分隔符' % transpancySGNodes[i]
                        else:
                            keySGInfo = transpancySGNodes[i].split('_')[-2]
                        keySGInfo = str(i)
                        meshes = transpancyMeshes[i]
                        # 有着色物体时才进行
                        if meshes:
                            shaderNode = 'SHD_' + layerType + '_' + keySGInfo + '_caustics'
                            if mc.ls(shaderNode):
                                mc.delete(shaderNode)

                            shaderNode = mc.shadingNode('lambert', asShader=True, name=shaderNode)
                            mc.setAttr(shaderNode + '.color', 1, 1, 1, type='double3')

                            # 透明连接
                            self.zmRLTransShaderConnectiion(transpancyNode[i], shaderNode, 'transparency')

                            # 翻转
                            if '.outTransparency' in transpancyNode[i]:
                                mc.editRenderLayerAdjustment(transpancyNode[i].split('.')[0] + '.invert')
                                mc.setAttr((transpancyNode[i].split('.')[0] + ".invert"), 1)

                            # 连接着色

                            shaderInfo = mc.listConnections((transpancySGNodes[i] + '.surfaceShader'),s = 1,plugs = 1)
                            if shaderInfo:
                                shaderInfo = shaderInfo[0]
                                mc.editRenderLayerAdjustment(transpancySGNodes[i] + '.surfaceShader')
                                mc.disconnectAttr(shaderInfo, (transpancySGNodes[i] + '.surfaceShader'))
                                mc.connectAttr((shaderNode + '.outColor'), (transpancySGNodes[i] + '.surfaceShader'), f=1)

            # 加载MR
            if mc.pluginInfo('Mayatomr.mll', q=1, loaded=1):
                mel.eval('loadPlugin "Mayatomr.mll"')
                mc.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')
            # MR设置
            mc.editRenderLayerAdjustment('miDefaultOptions.rayTracing')
            mc.setAttr('miDefaultOptions.rayTracing', 1)
            mc.editRenderLayerAdjustment('miDefaultOptions.maxReflectionRays')
            mc.setAttr('miDefaultOptions.maxReflectionRays', 10)
            mc.editRenderLayerAdjustment('miDefaultOptions.maxRefractionRays')
            mc.setAttr('miDefaultOptions.maxRefractionRays', 10)
            mc.editRenderLayerAdjustment('miDefaultOptions.maxRayDepth')
            mc.setAttr('miDefaultOptions.maxRayDepth', 20)
            mc.editRenderLayerAdjustment('miDefaultOptions.maxShadowRayDepth')
            mc.setAttr('miDefaultOptions.maxShadowRayDepth', 2)
            mc.editRenderLayerAdjustment('miDefaultOptions.maxReflectionBlur')
            mc.setAttr('miDefaultOptions.maxReflectionBlur', 1)
            mc.editRenderLayerAdjustment('miDefaultOptions.maxRefractionBlur')
            mc.setAttr('miDefaultOptions.maxRefractionBlur', 1)

            # 格式命名
            mc.setAttr('defaultRenderGlobals.animation', 1)
            mc.setAttr('defaultRenderGlobals.putFrameBeforeExt', 1)
            mc.setAttr('defaultRenderGlobals.periodInExt', 1)
            mc.setAttr('defaultRenderGlobals.extensionPadding', 4)
            if mc.getAttr('defaultRenderGlobals.outFormatControl') == 1:
                mc.setAttr('defaultRenderGlobals.outFormatControl', 0)

            # exr
            mc.editRenderLayerAdjustment('defaultRenderGlobals.imageFormat')
            mc.setAttr('defaultRenderGlobals.imageFormat', 51)
            mc.setAttr('defaultRenderGlobals.imfkey', 'exr', type='string')
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.setAttr('mentalrayGlobals.compressionQuality', 0)

            # 16位zip压缩
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.editRenderLayerAdjustment('miDefaultFramebuffer.datatype')
            mc.setAttr('miDefaultFramebuffer.datatype', 16)
            mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')
            mc.setAttr("defaultRenderLayer.renderable", 0)

            print (u'===============!!!Done  【%s】!!!===============' % (u'%s_CAUSTICS层' % layerType))
            print '\n'

        else:
            print (u'===============!!!Error  【%s】无物体!!!===============' % (u'%s_CAUSTICS层' % layerType))
            print '\n'
    # CHR_LINE层
    # No Lights

    def zmRLLineCreate(self, layerType, selectObjType=0):
        print (u'===============!!!Start 【%s】!!!===============' % (u'%s_LINE层' % layerType))
        print 'Working...'

        # 物体
        objs = self.zmRLObjectsTList()
        refCHR = objs[0]
        refPROP = objs[1]
        refSET = objs[2]
        refSKY = objs[3]
        refSEA = objs[4]

        rlObjs = []

        if layerType == 'CHR':
            rlObjs = refCHR
            layerName = 'CHR_LINE'

        # 灯光
        lights = mc.ls(type='light')

        # 选取模式
        if selectObjType == 1:
            rlObjs = self.zmRLSelectMode()

        if rlObjs:
            # 先回到masterLayer
            # Back To MasterLayer
            mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')

            mc.createRenderLayer(rlObjs, name=layerName, noRecurse=1, makeCurrent=1)

            # 通用RGB材质
            shaderBaseNode = 'SHD_' + layerType + '_LineShader'
            if mc.ls(shaderBaseNode):
                mc.delete(shaderBaseNode)

            shaderContrast = 'SHD_' + layerType + '_LineContrast'
            if mc.ls(shaderContrast):
                try:
                    mc.disconnectAttr((shaderContrast + '.message'), ('miDefaultOptions' + '.contourContrast'))
                except:
                    pass
                mc.delete(shaderContrast)

            shaderStore = 'SHD_' + layerType + '_LineStore'
            if mc.ls(shaderStore):
                try:
                    mc.disconnectAttr((shaderStore + '.message'), ('miDefaultOptions' + '.contourStore'))
                except:
                    pass
                mc.delete(shaderStore)

            shaderBaseSG = 'SHD_' + layerType + '_LineLambert_SG'
            if mc.ls(shaderBaseSG):
                mc.delete(shaderBaseSG)

            try:
                mc.disconnectAttr(('miDefaultOptions' + '.contourContrast'), (layerName + '.adjustments[1].plug'))
            except:
                pass
            try:
                mc.disconnectAttr(('miDefaultOptions' + '.contourStore'), (layerName + '.adjustments[2].plug'))
            except:
                pass

            shaderRNode = mc.shadingNode('lambert', asShader=True, name=shaderBaseNode)
            mc.setAttr((shaderRNode + '.color'), 0, 0, 0, type='double3')
            mc.setAttr((shaderRNode + '.ambientColor'), 1, 1, 1, type='double3')
            mc.setAttr((shaderRNode + '.diffuse'), 0)
            shaderGNode = mc.shadingNode('contour_contrast_function_levels', asShader=True, name=shaderContrast)
            mc.setAttr((shaderGNode + '.zdelta'), 2)
            mc.setAttr((shaderGNode + '.ndelta'), 8)
            mc.setAttr((shaderGNode + '.diff_mat'), 0)
            mc.setAttr((shaderGNode + '.diff_label'), 1)
            mc.setAttr((shaderGNode + '.diff_index'), 0)
            mc.setAttr((shaderGNode + '.diff_mat'), 0)
            mc.setAttr((shaderGNode + '.min_level'), 0)
            mc.setAttr((shaderGNode + '.max_level'), 1)
            shaderStore = mc.shadingNode('contour_store_function', asShader=True, name=shaderStore)

            shaderBaseSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=shaderBaseSG)
            mc.setAttr((shaderBaseSG + '.miContourEnable'), 1)
            mc.setAttr((shaderBaseSG + '.miContourWidth'), 0.4)
            # 开关开启自动连接了？
            # mc.connectAttr(('miDefaultOptions' + '.contourContrast'), (layerName + '.adjustments[1].plug'))
            # mc.connectAttr(('miDefaultOptions' + '.contourStore'), (layerName + '.adjustments[2].plug'))

            mc.connectAttr((shaderBaseNode + '.color'), (shaderBaseSG + '.surfaceShader'))

            mc.editRenderLayerAdjustment('miDefaultFramebuffer.contourEnable')
            mc.setAttr(('miDefaultFramebuffer.contourEnable'), 1)
            mc.setAttr('miDefaultFramebuffer.contourClearImage', 1)
            mc.setAttr('miDefaultFramebuffer.contourClearColor', 1, 1, 1, type='double3')
            mc.setAttr('miDefaultFramebuffer.contourSamples', 30)
            mc.setAttr('miDefaultFramebuffer.contourFilter', 1)
            mc.setAttr('miDefaultFramebuffer.contourFilterSupport', 1)

            mc.editRenderLayerAdjustment('miDefaultOptions.contourContrast')
            mc.connectAttr((shaderContrast + '.message'), ('miDefaultOptions' + '.contourContrast'))
            mc.connectAttr((shaderContrast + '.message'), (layerName + '.adjustments[1].value'))

            mc.editRenderLayerAdjustment('miDefaultOptions.contourStore')
            mc.connectAttr((shaderStore + '.message'), ('miDefaultOptions' + '.contourStore'))
            mc.connectAttr((shaderStore + '.message'), (layerName + '.adjustments[2].value'))

            # 优先全局着色
            for obj in rlObjs:
                # print '----------------'
                # print obj
                try:
                    mc.sets(obj, e=1, forceElement=shaderBaseSG)
                except:
                    # 获取物体面数
                    faceNum = mc.polyEvaluate(obj, face=1)
                    mc.sets((obj + u'.f[:' + str(faceNum - 1) + u']'), e=1, forceElement=shaderBaseSG)

            # 隐藏灯光
            for light in lights:
                lightGrp = mc.listRelatives(light, p=1, type='transform', f=1)[0]
                mc.editRenderLayerAdjustment(lightGrp + '.v')
                mc.setAttr((light + '.v'), 0)
                mc.editRenderLayerAdjustment(light + '.intensity')
                mc.setAttr((light + '.intensity'), 0)

            # 设置
            # self.zmRLCommonConfig()

            # 渲染设置
            mc.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')

            mc.editRenderLayerAdjustment('miDefaultOptions.minSamples')
            mc.setAttr('miDefaultOptions.minSamples',1)
            mc.editRenderLayerAdjustment('miDefaultOptions.maxSamples')
            mc.setAttr('miDefaultOptions.maxSamples',3)
            mc.editRenderLayerAdjustment('miDefaultOptions.jitter')
            mc.setAttr('miDefaultOptions.jitter',1)
            
            mc.editRenderLayerAdjustment('miDefaultOptions.contrastR')
            mc.editRenderLayerAdjustment('miDefaultOptions.contrastG')
            mc.editRenderLayerAdjustment('miDefaultOptions.contrastB')
            mc.editRenderLayerAdjustment('miDefaultOptions.contrastA')
            
            mc.setAttr('miDefaultOptions.contrastG',0.01)
            mc.setAttr('miDefaultOptions.contrastB',0.01)
            mc.setAttr('miDefaultOptions.contrastA',0.01)

            # 格式命名
            mc.setAttr('defaultRenderGlobals.animation', 1)
            mc.setAttr('defaultRenderGlobals.putFrameBeforeExt', 1)
            mc.setAttr('defaultRenderGlobals.periodInExt', 1)
            mc.setAttr('defaultRenderGlobals.extensionPadding', 4)
            if mc.getAttr('defaultRenderGlobals.outFormatControl') == 1:
                mc.setAttr('defaultRenderGlobals.outFormatControl', 0)

            # exr
            mc.editRenderLayerAdjustment('defaultRenderGlobals.imageFormat')
            mc.setAttr('defaultRenderGlobals.imageFormat', 51)
            mc.setAttr('defaultRenderGlobals.imfkey', 'exr', type='string')
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.setAttr('mentalrayGlobals.compressionQuality', 0)

            # 16位zip压缩
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.editRenderLayerAdjustment('miDefaultFramebuffer.datatype')
            mc.setAttr('miDefaultFramebuffer.datatype', 16)

            print (u'===============!!!Done  【%s】!!!===============' % (u'%s_LINE层' % layerType))
            print '\n'
        else:
            print (u'===============!!!Error  【%s】无物体!!!===============' % (u'%s_LINE层' % layerType))
            print '\n'

    # ALL_MSK01层
    def zmRLMSK01reate(self, layerType, selectObjType=0):
        print (u'===============!!!Start 【%s】!!!===============' % (u'%s_MSK01层' % 'ALL'))
        print 'Working...'

        layerType = 'MSK_01'
        # 物体
        objs = self.zmRLObjectsTList()
        refCHR = objs[0]
        refPROP = objs[1]
        refSET = objs[2]
        refSKY = objs[3]
        refSEA = objs[4]

        objgrps = []
        if refSET:
            for obj in refSET:
                if obj not in refSKY:
                    objgrps.append(obj)
                    refSET = objgrps

        rlObjs = refCHR + refPROP + refSET + refSEA
        layerName = 'ALL_MSK01'

        # 灯光
        lights = mc.ls(type='light')


        objsAll = rlObjs
        objsR = refCHR
        # GREEN
        #objsG = mc.ls('*:*_Oillamp_*', type='transform') + mc.ls('*:*:*_Oillamp_*', type='transform') + mc.ls('*:*_sea_*', type='transform') + mc.ls('*_sea_*', type='transform')
        objsG = mc.ls('*:*_Oillamp_*', l=1, type='transform') + mc.ls('*:*:*_Oillamp_*', l=1, type='transform') + mc.ls(refSEA, l=1, type='transform')
        objsB = refPROP

        if objsAll:

            # 特殊处理，半透明用
            # 获取信息必须在masterLayer进行
            transpancyObjs = self.zmRLTransparencyObjs()
            transpancySGNodes = transpancyObjs[0]
            transpancyMeshes = transpancyObjs[1]
            transpancyNode = transpancyObjs[2]

            # 创建RenderLayer
            if mc.ls(layerName):
                mc.delete(layerName)

            mc.createRenderLayer(objsAll, name=layerName, noRecurse=1, makeCurrent=1)

            # 通用RGB材质
            shaderRNode = 'SHD_' + layerType + '_R_Shader'
            if mc.ls(shaderRNode):
                mc.delete(shaderRNode)
            shaderGNode = 'SHD_' + layerType + '_G_Shader'
            if mc.ls(shaderGNode):
                mc.delete(shaderGNode)
            shaderBNode = 'SHD_' + layerType + '_B_Shader'
            if mc.ls(shaderBNode):
                mc.delete(shaderBNode)
            shaderMNode = 'SHD_' + layerType + '_M_Shader'
            if mc.ls(shaderMNode):
                mc.delete(shaderMNode)

            shaderRSG = 'SHD_' + layerType + '_R_SG'
            if mc.ls(shaderRSG):
                mc.delete(shaderRSG)
            shaderGSG = 'SHD_' + layerType + '_G_SG'
            if mc.ls(shaderGSG):
                mc.delete(shaderGSG)
            shaderBSG = 'SHD_' + layerType + '_B_SG'
            if mc.ls(shaderBSG):
                mc.delete(shaderBSG)
            shaderMSG = 'SHD_' + layerType + '_M_SG'
            if mc.ls(shaderMSG):
                mc.delete(shaderMSG)

            shaderRNode = mc.shadingNode('lambert', asShader=True, name=shaderRNode)
            mc.setAttr((shaderRNode + '.color'), 1, 0, 0, type='double3')
            mc.setAttr((shaderRNode + '.ambientColor'), 1, 1, 1, type='double3')
            mc.setAttr((shaderRNode + '.diffuse'), 0)
            mc.setAttr((shaderRNode + '.matteOpacity'), 0)
            shaderGNode = mc.shadingNode('lambert', asShader=True, name=shaderGNode)
            mc.setAttr((shaderGNode + '.color'), 0, 1, 0, type='double3')
            mc.setAttr((shaderGNode + '.ambientColor'), 1, 1, 1, type='double3')
            mc.setAttr((shaderGNode + '.diffuse'), 0)
            mc.setAttr((shaderGNode + '.matteOpacity'), 0)
            shaderBNode = mc.shadingNode('lambert', asShader=True, name=shaderBNode)
            mc.setAttr((shaderBNode + '.color'), 0, 0, 1, type='double3')
            mc.setAttr((shaderBNode + '.ambientColor'), 1, 1, 1, type='double3')
            mc.setAttr((shaderBNode + '.diffuse'), 0)
            mc.setAttr((shaderBNode + '.matteOpacity'), 0)
            shaderMNode = mc.shadingNode('lambert', asShader=True, name=shaderMNode)
            mc.setAttr((shaderMNode + '.color'), 0, 0, 0, type='double3')
            mc.setAttr((shaderMNode + '.matteOpacityMode'), 0)

            shaderRSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=shaderRSG)
            shaderGSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=shaderGSG)
            shaderBSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=shaderBSG)
            shaderMSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=shaderMSG)

            mc.connectAttr((shaderRNode + '.color'), (shaderRSG + '.surfaceShader'))
            mc.connectAttr((shaderGNode + '.color'), (shaderGSG + '.surfaceShader'))
            mc.connectAttr((shaderBNode + '.color'), (shaderBSG + '.surfaceShader'))
            mc.connectAttr((shaderMNode + '.color'), (shaderMSG + '.surfaceShader'))

            # 优先全局着色，赋予Mask
            for obj in objsAll:

                try:
                    mc.sets(obj, e=1, forceElement=shaderMSG)
                except:
                    # 获取物体面数
                    faceNum = mc.polyEvaluate(obj, face=1)
                    mc.sets((obj + u'.f[:' + str(faceNum - 1) + u']'), e=1, forceElement=shaderMSG)

            # 然后RGB赋色
            if objsR:
                for obj in objsR:
                    # print '----------------'
                    # print obj
                    try:
                        mc.sets(obj, e=1, forceElement=shaderRSG)
                    except:
                        # 获取物体面数
                        faceNum = mc.polyEvaluate(obj, face=1)
                        mc.sets((obj + u'.f[:' + str(faceNum - 1) + u']'), e=1, forceElement=shaderRSG)
                # mc.sets(objsR, e=1, forceElement= shaderRSG )
            if objsG:
                for obj in objsG:
                    # print '----------------'
                    # print obj
                    try:
                        mc.sets(obj, e=1, forceElement=shaderGSG)
                    except:
                        # 获取物体面数
                        faceNum = mc.polyEvaluate(obj, face=1)
                        mc.sets((obj + u'.f[:' + str(faceNum - 1) + u']'), e=1, forceElement=shaderGSG)

                if refSEA:
                    mc.select(refSEA)
                    self.zmRGBMShaderCreate('G')


            if objsB:
                for obj in objsB:
                    # print '----------------'
                    # print obj
                    try:
                        mc.sets(obj, e=1, forceElement=shaderBSG)
                    except:
                        # 获取物体面数
                        faceNum = mc.polyEvaluate(obj, face=1)
                        mc.sets((obj + u'.f[:' + str(faceNum - 1) + u']'), e=1, forceElement=shaderBSG)

            if transpancySGNodes:
                for i in range(len(transpancySGNodes)):
                    if mc.ls(transpancySGNodes[i]):
                        if '_' not in transpancySGNodes[i]:
                            print u'>>>>>>[注意][%s]名字需要最少有1个_分隔符' % transpancySGNodes[i]
                        else:
                            keySGInfo = transpancySGNodes[i].split('_')[-2]
                        keySGInfo = str(i)
                        meshes = transpancyMeshes[i]
                        # 不对！！！！！
                        # 有着色物体时才进行，处理对有相同透明材质的物体使用不同的RGBM
                        if meshes:
                            meshesR = []
                            meshesG = []
                            meshesB = []
                            meshesM = []
                            needColor = [[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]]
                            needRGBInfo = ['M', 'R', 'G', 'B']
                            for mesh in meshes:
                                if not mc.objExists(mesh):
                                    continue
                                meshGrp = ''
                                if '.f[' in mesh:
                                    meshGrp = mc.ls(mesh.split('.f[')[0],l=1)[0]
                                else:
                                    meshGrp = mc.listRelatives(mesh, p=1, f=1,type = 'transform')[0]
                                RGBInfo = ''
                                if meshGrp in objsR:
                                    meshesR.append(mesh)
                                if meshGrp in objsG:
                                    # 海不要透明通道
                                    if '_sea_' not in mesh:
                                        meshesG.append(mesh)
                                if meshGrp in objsB:
                                    meshesB.append(mesh)
                                if meshGrp not in (objsR + objsG + objsB):
                                    # 海不要透明通道
                                    if '_sea_' not in mesh:
                                        meshesM.append(mesh)

                            for j in range(4):
                                if j == 0:
                                    needMeshes = meshesM
                                if j == 1:
                                    needMeshes = meshesR
                                if j == 2:
                                    needMeshes = meshesG
                                if j == 3:
                                    needMeshes = meshesB
                                RGBInfo = needRGBInfo[j]
                                color = needColor[j]

                                if not needMeshes:
                                    continue

                                shaderTrsNode = 'SHD_' + layerType + '_' + keySGInfo + '_' + RGBInfo + '_Shader'
                                if mc.ls(shaderTrsNode):
                                    # mc.delete( shaderTrsNode )
                                    pass
                                else:
                                    shaderTrsNode = mc.shadingNode('lambert', asShader=True, name=shaderTrsNode)

                                shaderTrsSG = 'SHD_' + layerType + '_' + keySGInfo + '_' + RGBInfo + '_SG'
                                if mc.ls(shaderTrsSG):
                                    # mc.delete( shaderTrsSG )
                                    pass
                                else:
                                    shaderTrsSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=shaderTrsSG)

                                # shaderNode = mc.shadingNode ('surfaceShader', asShader=True, name= shaderNode)
                                if RGBInfo in ['R', 'G', 'B']:
                                    # print (shaderTrsNode + '.color')
                                    mc.setAttr((shaderTrsNode + '.color'), color[0], color[1], color[2], type='double3')
                                    mc.setAttr((shaderTrsNode + '.ambientColor'), 1, 1, 1, type='double3')
                                    mc.setAttr((shaderTrsNode + '.diffuse'), 0)
                                    mc.setAttr((shaderTrsNode + '.matteOpacity'), 0)
                                if RGBInfo == 'M':
                                    mc.setAttr((shaderTrsNode + '.color'), 0, 0, 0, type='double3')
                                    mc.setAttr((shaderTrsNode + '.matteOpacityMode'), 0)
                                # shaderSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name= shaderSG)

                                try:
                                    mc.connectAttr((shaderTrsNode + '.outColor'), (shaderTrsSG + '.surfaceShader'))
                                except:
                                    pass

                                # 透明连接
                                self.zmRLTransShaderConnectiion(transpancyNode[i], shaderTrsNode, 'transparency')

                                # 翻转
                                if '.outTransparency' in transpancyNode[i]:
                                    mc.editRenderLayerAdjustment(transpancyNode[i].split('.')[0] + '.invert')
                                    mc.setAttr((transpancyNode[i].split('.')[0] + ".invert"), 1)

                                if needMeshes:
                                    for mesh in needMeshes:
                                        if mc.ls(mesh):
                                            try:
                                                mc.sets(mesh, e=1, forceElement=shaderTrsSG)
                                            except:
                                                # 获取物体面数
                                                pass
                                # mc.sets(mesh, e=1, forceElement= shaderSG )

            if refSEA:
                mc.select(refSEA)
                mel.eval('source "//file-cluster/GDC/Resource/Support/Maya/projects/JT/HbJtRenderTools.mel"')
                mel.eval('HbMaterialG()')

            # 隐藏灯光
            for light in lights:
                lightGrp = mc.listRelatives(light, p=1, type='transform', f=1)[0]
                mc.editRenderLayerAdjustment(lightGrp + '.v')
                mc.setAttr((light + '.v'), 0)
                mc.editRenderLayerAdjustment(light + '.intensity')
                mc.setAttr((light + '.intensity'), 0)

            # 设置
            # self.zmRLCommonConfig()

            # 渲染设置
            mc.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')

            # 关闭光线追踪
            mc.editRenderLayerAdjustment('miDefaultOptions.rayTracing')
            mc.setAttr('miDefaultOptions.rayTracing', 0)

            # 格式命名
            mc.setAttr('defaultRenderGlobals.animation', 1)
            mc.setAttr('defaultRenderGlobals.putFrameBeforeExt', 1)
            mc.setAttr('defaultRenderGlobals.periodInExt', 1)
            mc.setAttr('defaultRenderGlobals.extensionPadding', 4)
            if mc.getAttr('defaultRenderGlobals.outFormatControl') == 1:
                mc.setAttr('defaultRenderGlobals.outFormatControl', 0)

            # exr
            mc.editRenderLayerAdjustment('defaultRenderGlobals.imageFormat')
            mc.setAttr('defaultRenderGlobals.imageFormat', 51)
            mc.setAttr('defaultRenderGlobals.imfkey', 'exr', type='string')
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.setAttr('mentalrayGlobals.compressionQuality', 0)

            # 16位zip压缩
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.editRenderLayerAdjustment('miDefaultFramebuffer.datatype')
            mc.setAttr('miDefaultFramebuffer.datatype', 16)

            print (u'===============!!!Done  【%s】!!!===============' % (u'%s_MSK01层' % 'ALL'))
            print '\n'
        else:
            print (u'===============!!!Error  【%s】无物体!!!===============' % (u'%s_MSK01层' % 'ALL'))
            print '\n'

    def zmRLMSK02reate(self, layerType, selectObjType=0):
        print (u'===============!!!Start 【%s】!!!===============' % (u'%s_MSK02层' % 'ALL'))
        print 'Working...'

        layerType = 'MSK_02'
        # 物体
        objs = self.zmRLObjectsTList()
        refCHR = objs[0]
        refPROP = objs[1]
        refSET = objs[2]
        refSKY = objs[3]
        refSEA = objs[4]

        objgrps = []
        if refSET:
            for obj in refSET:
                if obj not in refSKY:
                    objgrps.append(obj)
            refSET = objgrps

        rlObjs = refCHR + refPROP + refSET

        layerName = 'ALL_MSK02'

        # 灯光
        lights = mc.ls(type='light')


        objsAll = rlObjs
        objsR = refCHR
        # GREEN
        #objsG = mc.ls('*:*_Oillamp_*', type='transform') + mc.ls('*:*:*_Oillamp_*', type='transform') + mc.ls('*:*_sea_*', type='transform') + mc.ls('*_sea_*', type='transform')
        objsG = mc.ls('*:*_Oillamp_*', l=1, type='transform') + mc.ls('*:*:*_Oillamp_*', l=1, type='transform') + mc.ls(refSEA, l=1, type='transform')
        objsB = refPROP

        if objsAll:

            # 特殊处理，半透明用
            # 获取信息必须在masterLayer进行
            transpancyObjs = self.zmRLTransparencyObjs()
            transpancySGNodes = transpancyObjs[0]
            transpancyMeshes = transpancyObjs[1]
            transpancyNode = transpancyObjs[2]

            # 创建RenderLayer
            if mc.ls(layerName):
                mc.delete(layerName)

            mc.createRenderLayer(objsAll, name=layerName, noRecurse=1, makeCurrent=1)

            # 通用RGB材质
            shaderRNode = 'SHD_' + layerType + '_R_Shader'
            if mc.ls(shaderRNode):
                mc.delete(shaderRNode)
            shaderGNode = 'SHD_' + layerType + '_G_Shader'
            if mc.ls(shaderGNode):
                mc.delete(shaderGNode)
            shaderBNode = 'SHD_' + layerType + '_B_Shader'
            if mc.ls(shaderBNode):
                mc.delete(shaderBNode)
            shaderMNode = 'SHD_' + layerType + '_M_Shader'
            if mc.ls(shaderMNode):
                mc.delete(shaderMNode)

            shaderRSG = 'SHD_' + layerType + '_R_SG'
            if mc.ls(shaderRSG):
                mc.delete(shaderRSG)
            shaderGSG = 'SHD_' + layerType + '_G_SG'
            if mc.ls(shaderGSG):
                mc.delete(shaderGSG)
            shaderBSG = 'SHD_' + layerType + '_B_SG'
            if mc.ls(shaderBSG):
                mc.delete(shaderBSG)
            shaderMSG = 'SHD_' + layerType + '_M_SG'
            if mc.ls(shaderMSG):
                mc.delete(shaderMSG)

            shaderRNode = mc.shadingNode('lambert', asShader=True, name=shaderRNode)
            mc.setAttr((shaderRNode + '.color'), 1, 0, 0, type='double3')
            mc.setAttr((shaderRNode + '.ambientColor'), 1, 1, 1, type='double3')
            mc.setAttr((shaderRNode + '.diffuse'), 0)
            mc.setAttr((shaderRNode + '.matteOpacity'), 0)
            shaderGNode = mc.shadingNode('lambert', asShader=True, name=shaderGNode)
            mc.setAttr((shaderGNode + '.color'), 0, 1, 0, type='double3')
            mc.setAttr((shaderGNode + '.ambientColor'), 1, 1, 1, type='double3')
            mc.setAttr((shaderGNode + '.diffuse'), 0)
            mc.setAttr((shaderGNode + '.matteOpacity'), 0)
            shaderBNode = mc.shadingNode('lambert', asShader=True, name=shaderBNode)
            mc.setAttr((shaderBNode + '.color'), 0, 0, 1, type='double3')
            mc.setAttr((shaderBNode + '.ambientColor'), 1, 1, 1, type='double3')
            mc.setAttr((shaderBNode + '.diffuse'), 0)
            mc.setAttr((shaderBNode + '.matteOpacity'), 0)
            shaderMNode = mc.shadingNode('lambert', asShader=True, name=shaderMNode)
            mc.setAttr((shaderMNode + '.color'), 0, 0, 0, type='double3')
            mc.setAttr((shaderMNode + '.matteOpacityMode'), 0)

            shaderRSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=shaderRSG)
            shaderGSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=shaderGSG)
            shaderBSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=shaderBSG)
            shaderMSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=shaderMSG)

            mc.connectAttr((shaderRNode + '.color'), (shaderRSG + '.surfaceShader'))
            mc.connectAttr((shaderGNode + '.color'), (shaderGSG + '.surfaceShader'))
            mc.connectAttr((shaderBNode + '.color'), (shaderBSG + '.surfaceShader'))
            mc.connectAttr((shaderMNode + '.color'), (shaderMSG + '.surfaceShader'))

            # 优先全局着色，赋予Mask
            for obj in objsAll:
                try:
                    mc.sets(obj, e=1, forceElement=shaderMSG)
                except:
                    # 获取物体面数
                    faceNum = mc.polyEvaluate(obj, face=1)
                    mc.sets((obj + u'.f[:' + str(faceNum - 1) + u']'), e=1, forceElement=shaderMSG)

            # 然后RGB赋色
            if objsR:
                for obj in objsR:
                    # print '----------------'
                    # print obj
                    try:
                        mc.sets(obj, e=1, forceElement=shaderRSG)
                    except:
                        # 获取物体面数
                        faceNum = mc.polyEvaluate(obj, face=1)
                        mc.sets((obj + u'.f[:' + str(faceNum - 1) + u']'), e=1, forceElement=shaderRSG)

            if objsG:
                for obj in objsG:

                    try:
                        mc.sets(obj, e=1, forceElement=shaderGSG)
                    except:
                        # 获取物体面数
                        faceNum = mc.polyEvaluate(obj, face=1)
                        mc.sets((obj + u'.f[:' + str(faceNum - 1) + u']'), e=1, forceElement=shaderGSG)

                if refSEA:
                    mc.select(refSEA)
                    self.zmRGBMShaderCreate('G')

            if objsB:
                for obj in objsB:
                    # print '----------------'
                    # print obj
                    try:
                        mc.sets(obj, e=1, forceElement=shaderBSG)
                    except:
                        # 获取物体面数
                        faceNum = mc.polyEvaluate(obj, face=1)
                        mc.sets((obj + u'.f[:' + str(faceNum - 1) + u']'), e=1, forceElement=shaderBSG)


            if transpancySGNodes:
                for i in range(len(transpancySGNodes)):
                    if mc.ls(transpancySGNodes[i]):
                        if '_' not in transpancySGNodes[i]:
                            print u'>>>>>>[注意][%s]名字需要最少有1个_分隔符' % transpancySGNodes[i]
                        else:
                            keySGInfo = transpancySGNodes[i].split('_')[-2]
                        keySGInfo = str(i)
                        meshes = transpancyMeshes[i]
                        # 不对！！！！！
                        # 有着色物体时才进行，处理对有相同透明材质的物体使用不同的RGBM
                        if meshes:
                            meshesR = []
                            meshesG = []
                            meshesB = []
                            meshesM = []
                            needColor = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 0]]
                            needRGBInfo = ['M', 'R', 'G', 'B']
                            for mesh in meshes:
                                if not mc.objExists(mesh):
                                    continue
                                meshGrp = ''
                                if '.f[' in mesh:
                                    meshGrp = mc.ls(mesh.split('.f[')[0],l=1)[0]
                                else:
                                    meshGrp = mc.listRelatives(mesh, p=1, f=1,type = 'transform')[0]
                                RGBInfo = ''
                                if meshGrp in objsR:
                                    meshesR.append(mesh)
                                if meshGrp in objsG:
                                    # 海不要透明通道
                                    if '_sea_' not in mesh:
                                        meshesG.append(mesh)
                                if meshGrp in objsB:
                                    meshesB.append(mesh)
                                if meshGrp not in (objsR + objsG + objsB):
                                    # 海不要透明通道
                                    if '_sea_' not in mesh:
                                        meshesM.append(mesh)

                            for j in range(4):
                                if j == 0:
                                    needMeshes = meshesM
                                if j == 1:
                                    needMeshes = meshesR
                                if j == 2:
                                    needMeshes = meshesG
                                if j == 3:
                                    needMeshes = meshesB
                                RGBInfo = needRGBInfo[j]
                                color = needColor[j]

                                if not needMeshes:
                                    continue

                                shaderTrsNode = 'SHD_' + layerType + '_' + keySGInfo + '_' + RGBInfo + '_Shader'
                                if mc.ls(shaderTrsNode):
                                    pass
                                else:
                                    shaderTrsNode = mc.shadingNode('lambert', asShader=True, name=shaderTrsNode)

                                shaderTrsSG = 'SHD_' + layerType + '_' + keySGInfo + '_' + RGBInfo + '_SG'
                                if mc.ls(shaderTrsSG):
                                    pass
                                else:
                                    shaderTrsSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=shaderTrsSG)

                                if RGBInfo in ['R', 'G', 'B']:
                                    # print (shaderTrsNode + '.color')
                                    mc.setAttr((shaderTrsNode + '.color'), color[0], color[1], color[2], type='double3')
                                    mc.setAttr((shaderTrsNode + '.ambientColor'), 1, 1, 1, type='double3')
                                    mc.setAttr((shaderTrsNode + '.diffuse'), 0)
                                    mc.setAttr((shaderTrsNode + '.matteOpacity'), 0)
                                if RGBInfo == 'M':
                                    mc.setAttr((shaderTrsNode + '.color'), 0, 0, 0, type='double3')
                                    mc.setAttr((shaderTrsNode + '.matteOpacityMode'), 0)

                                try:
                                    mc.connectAttr((shaderTrsNode + '.outColor'), (shaderTrsSG + '.surfaceShader'))
                                except:
                                    pass

                                # 透明连接
                                self.zmRLTransShaderConnectiion(transpancyNode[i], shaderTrsNode, 'transparency')

                                # 翻转
                                if '.outTransparency' in transpancyNode[i]:
                                    mc.editRenderLayerAdjustment(transpancyNode[i].split('.')[0] + '.invert')
                                    mc.setAttr((transpancyNode[i].split('.')[0] + ".invert"), 1)

                                if needMeshes:
                                    for mesh in needMeshes:
                                        if mc.ls(mesh):
                                            try:
                                                mc.sets(mesh, e=1, forceElement=shaderTrsSG)
                                            except:
                                                # 获取物体面数
                                                pass


            if refSEA:
                for obj in refSEA:
                    mc.editRenderLayerAdjustment(obj + '.v')
                    mc.setAttr((obj + '.v'), 0)

            # 隐藏灯光
            for light in lights:
                lightGrp = mc.listRelatives(light, p=1, type='transform', f=1)[0]
                mc.editRenderLayerAdjustment(lightGrp + '.v')
                mc.setAttr((light + '.v'), 0)
                mc.editRenderLayerAdjustment(light + '.intensity')
                mc.setAttr((light + '.intensity'), 0)

            # 设置
            # self.zmRLCommonConfig()
            # 渲染设置
            mc.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')

            # 关闭光线追踪
            mc.editRenderLayerAdjustment('miDefaultOptions.rayTracing')
            mc.setAttr('miDefaultOptions.rayTracing', 0)

            # 格式命名
            mc.setAttr('defaultRenderGlobals.animation', 1)
            mc.setAttr('defaultRenderGlobals.putFrameBeforeExt', 1)
            mc.setAttr('defaultRenderGlobals.periodInExt', 1)
            mc.setAttr('defaultRenderGlobals.extensionPadding', 4)
            if mc.getAttr('defaultRenderGlobals.outFormatControl') == 1:
                mc.setAttr('defaultRenderGlobals.outFormatControl', 0)

            # exr
            mc.editRenderLayerAdjustment('defaultRenderGlobals.imageFormat')
            mc.setAttr('defaultRenderGlobals.imageFormat', 51)
            mc.setAttr('defaultRenderGlobals.imfkey', 'exr', type='string')
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.setAttr('mentalrayGlobals.compressionQuality', 0)

            # 16位zip压缩
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.editRenderLayerAdjustment('miDefaultFramebuffer.datatype')
            mc.setAttr('miDefaultFramebuffer.datatype', 16)

            print (u'===============!!!Done  【%s】!!!===============' % (u'%s_MSK02层' % 'ALL'))
            print '\n'
        else:
            print (u'===============!!!Error  【%s】无物体!!!===============' % (u'%s_MSK02层' % 'ALL'))
            print '\n'
    # SEA_MSK层
    # No Lights

    def zmRLSeaMSKreate(self):
        print (u'===============!!!Start 【%s】!!!===============' % (u'%s_MSK层' % 'SEA'))
        print 'Working...'

        layerType = 'SEA_MSK'
        # 物体
        objs = self.zmRLObjectsTList()
        refCHR = objs[0]
        refPROP = objs[1]
        refSET = objs[2]
        refSKY = objs[3]
        refSEA = objs[4]
        rlObjs = mc.ls(refSEA, type='transform')
        layerName = 'SEA_MSK'

        # 灯光
        lights = mc.ls(type='light')

        if rlObjs:
            # seaMsk
            seaTempGrp = mc.ls(rlObjs, type='transform')
            seaTempMesh = mc.listRelatives(seaTempGrp[0], ni=1, s=1, type='mesh')
            seaTempSGNode = mc.listConnections(seaTempMesh[0], d=1, type='shadingEngine')
            seaTempShader = mc.listConnections((seaTempSGNode[0] + '.surfaceShader'), s=1, plugs=1)[0]

            # 创建RenderLayer
            if mc.ls(layerName):
                mc.delete(layerName)

            mc.createRenderLayer(rlObjs, name=layerName, noRecurse=1, makeCurrent=1)

            seaMesh = mc.listRelatives(rlObjs[0], ni=1, s=1, type='mesh')
            seaSGNode = mc.listConnections(seaMesh[0], d=1, type='shadingEngine')[0]

            mc.editRenderLayerAdjustment(seaSGNode + '.surfaceShader')
            try:
                mc.connectAttr((seaTempShader), (seaSGNode + '.surfaceShader'), f=1)
            except:
                pass

            # 渲染设置
            mc.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')

            # 关闭光线追踪
            mc.editRenderLayerAdjustment('miDefaultOptions.rayTracing')
            mc.setAttr('miDefaultOptions.rayTracing', 0)

            # 格式命名
            mc.setAttr('defaultRenderGlobals.animation', 1)
            mc.setAttr('defaultRenderGlobals.putFrameBeforeExt', 1)
            mc.setAttr('defaultRenderGlobals.periodInExt', 1)
            mc.setAttr('defaultRenderGlobals.extensionPadding', 4)
            if mc.getAttr('defaultRenderGlobals.outFormatControl') == 1:
                mc.setAttr('defaultRenderGlobals.outFormatControl', 0)

            # exr
            mc.editRenderLayerAdjustment('defaultRenderGlobals.imageFormat')
            mc.setAttr('defaultRenderGlobals.imageFormat', 51)
            mc.setAttr('defaultRenderGlobals.imfkey', 'exr', type='string')
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.setAttr('mentalrayGlobals.compressionQuality', 0)

            # 16位zip压缩
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.editRenderLayerAdjustment('miDefaultFramebuffer.datatype')
            mc.setAttr('miDefaultFramebuffer.datatype', 16)

            print (u'===============!!!Done  【%s】!!!===============' % (u'%s_MSK层' % 'SEA'))
            print '\n'
        else:
            print (u'===============!!!Error  【%s】无物体!!!===============' % (u'%s_MSK层' % 'SEA'))
            print '\n'

    # RGB层
    # No Lights
    def zmRLRGBCreate(self, layerType, selectObjType=0):
        print (u'===============!!!Start 【%s】!!!===============' % (u'%s_RGB层' % layerType))
        print 'Working...'

        # 物体
        objs = self.zmRLObjectsTList()
        refCHR = objs[0]
        refPROP = objs[1]
        refSET = objs[2]
        refSKY = objs[3]
        refSEA = objs[4]
        if layerType == 'CHR':
            rlObjs = refCHR + refPROP
            layerName = 'CHR_RGB'
            needFileObjs = self.zmRLayerRGBObjectsConfig(1)
        if layerType == 'BG':
            rlObjs = refSET
            layerName = 'BG_RGB'
            needFileObjs = self.zmRLayerRGBObjectsConfig(3)

        # 灯光
        lights = mc.ls(type='light')


        # 获取文件内相关物体信息
        objsAll = needFileObjs[0]
        objsR = needFileObjs[1]
        objsG = needFileObjs[2]
        objsB = needFileObjs[3]

        if objsAll:
            transpancyObjs = self.zmRLTransparencyObjs()
            transpancySGNodes = transpancyObjs[0]
            transpancyMeshes = transpancyObjs[1]
            transpancyNodes = transpancyObjs[2]

            # 创建RenderLayer
            if mc.ls(layerName):
                mc.delete(layerName)

            mc.createRenderLayer(objsAll, name=layerName, noRecurse=1, makeCurrent=1)

            # 通用RGB材质
            shaderRNode = 'SHD_' + layerType + '_R_Shader'
            if mc.ls(shaderRNode):
                mc.delete(shaderRNode)
            shaderGNode = 'SHD_' + layerType + '_G_Node'
            if mc.ls(shaderGNode):
                mc.delete(shaderGNode)
            shaderBNode = 'SHD_' + layerType + '_B_Node'
            if mc.ls(shaderBNode):
                mc.delete(shaderBNode)
            shaderMNode = 'SHD_' + layerType + '_M_Node'
            if mc.ls(shaderMNode):
                mc.delete(shaderMNode)

            shaderRSG = 'SHD_' + layerType + '_R_SG'
            if mc.ls(shaderRSG):
                mc.delete(shaderRSG)
            shaderGSG = 'SHD_' + layerType + '_G_SG'
            if mc.ls(shaderGSG):
                mc.delete(shaderGSG)
            shaderBSG = 'SHD_' + layerType + '_B_SG'
            if mc.ls(shaderBSG):
                mc.delete(shaderBSG)
            shaderMSG = 'SHD_' + layerType + '_M_SG'
            if mc.ls(shaderMSG):
                mc.delete(shaderMSG)

            shaderRNode = mc.shadingNode('lambert', asShader=True, name=shaderRNode)
            mc.setAttr((shaderRNode + '.color'), 1, 0, 0, type='double3')
            mc.setAttr((shaderRNode + '.ambientColor'), 1, 1, 1, type='double3')
            mc.setAttr((shaderRNode + '.diffuse'), 0)
            mc.setAttr((shaderRNode + '.matteOpacity'), 0)
            shaderGNode = mc.shadingNode('lambert', asShader=True, name=shaderGNode)
            mc.setAttr((shaderGNode + '.color'), 0, 1, 0, type='double3')
            mc.setAttr((shaderGNode + '.ambientColor'), 1, 1, 1, type='double3')
            mc.setAttr((shaderGNode + '.diffuse'), 0)
            mc.setAttr((shaderGNode + '.matteOpacity'), 0)
            shaderBNode = mc.shadingNode('surfaceShader', asShader=True, name=shaderBNode)
            mc.setAttr((shaderBNode + '.color'), 1, 0, 0, type='double3')
            mc.setAttr((shaderBNode + '.ambientColor'), 1, 1, 1, type='double3')
            mc.setAttr((shaderBNode + '.diffuse'), 0)
            mc.setAttr((shaderBNode + '.matteOpacity'), 0)
            shaderMNode = mc.shadingNode('lambert', asShader=True, name=shaderMNode)
            mc.setAttr((shaderMNode + '.color'), 0, 0, 0, type='double3')
            mc.setAttr((shaderMNode + '.matteOpacityMode'), 0)

            shaderRSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=shaderRSG)
            shaderGSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=shaderGSG)
            shaderBSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=shaderBSG)
            shaderMSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=shaderMSG)

            mc.connectAttr((shaderRNode + '.color'), (shaderRSG + '.surfaceShader'))
            mc.connectAttr((shaderGNode + '.color'), (shaderGSG + '.surfaceShader'))
            mc.connectAttr((shaderBNode + '.color'), (shaderBSG + '.surfaceShader'))
            mc.connectAttr((shaderMNode + '.color'), (shaderMSG + '.surfaceShader'))

            # 优先全局着色，赋予Mask
            for obj in objsAll:
                try:
                    mc.sets(obj, e=1, forceElement=shaderMSG)
                except:
                    # 获取物体面数
                    faceNum = mc.polyEvaluate(obj, face=1)
                    mc.sets((obj + u'.f[:' + str(faceNum - 1) + u']'), e=1, forceElement=shaderMSG)
            # 然后RGB赋色
            if objsR:
                for obj in objsR:
                    mc.sets(obj, e=1, forceElement=shaderRSG)
            if objsG:
                for obj in objsG:
                    mc.sets(obj, e=1, forceElement=shaderGSG)
            if objsB:
                for obj in objsB:
                    mc.sets(obj, e=1, forceElement=shaderBSG)

            if transpancySGNodes:
                for i in range(len(transpancySGNodes)):
                    if mc.ls(transpancySGNodes[i]):
                        if '_' not in transpancySGNodes[i]:
                            print u'>>>>>>[注意][%s]名字需要最少有1个_分隔符' % transpancySGNodes[i]
                        else:
                            keySGInfo = transpancySGNodes[i].split('_')[-2]
                        keySGInfo = str(i)
                        meshes = transpancyMeshes[i]
                        # 有着色物体时才进行,处理相同透明贴图的不同物体处于不同RGB种的情况
                        if meshes:
                            for mesh in meshes:
                                if mc.objExists(mesh):
                                    RGBInfo = ''
                                    if mesh in objsR:
                                        RGBInfo = 'R'
                                        color = [1, 0, 0]
                                    if mesh in objsG:
                                        RGBInfo = 'G'
                                        color = [0, 1, 0]
                                    if mesh in objsB:
                                        RGBInfo = 'B'
                                        color = [0, 0, 1]
                                    if mesh not in (objsR + objsG + objsB):
                                        RGBInfo = 'M'
                                        color = [0, 0, 0]

                                    if RGBInfo:
                                        shaderNode = 'SHD_' + layerType + '_' + keySGInfo + '_' + RGBInfo + '_Shader'
                                        if mc.ls(shaderNode):
                                            pass
                                        else:
                                            shaderNode = mc.shadingNode('surfaceShader', asShader=True, name=shaderNode)

                                        shaderSG = 'SHD_' + layerType + '_' + keySGInfo + '_' + RGBInfo + '_SG'
                                        if mc.ls(shaderSG):
                                            pass
                                        else:
                                            shaderSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=shaderSG)

                                        if RGBInfo in ['R', 'G', 'B']:
                                            mc.setAttr((shaderNode + '.color'), color[0], color[1], color[2], type='double3')
                                            mc.setAttr((shaderNode + '.ambientColor'), 1, 1, 1, type='double3')
                                            mc.setAttr((shaderNode + '.diffuse'), 0)
                                            mc.setAttr((shaderNode + '.matteOpacity'), 0)
                                        if RGBInfo == 'M':
                                            mc.setAttr((shaderNode + '.color'), color[0], color[1], color[2], type='double3')
                                            mc.setAttr((shaderNode + '.matteOpacityMode'), 0)
                                        # shaderSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name= shaderSG)

                                        try:
                                            mc.connectAttr((shaderNode + '.outColor'), (shaderSG + '.surfaceShader'))
                                        except:
                                            pass
                                        try:
                                            mc.connectAttr((transpancyNodes[i].split('.')[0] + '.outColor'), (shaderNode + '.transparency'))
                                        except:
                                            pass
                                        if '.outTransparency' in transpancyNodes[i]:
                                            mc.editRenderLayerAdjustment(transpancyNodes[i].split('.')[0] + '.invert')
                                            mc.setAttr((transpancyNodes[i].split('.')[0] + ".invert"), 1)

                                        try:
                                            mc.sets(mesh, e=1, forceElement=shaderSG)
                                        except:
                                            # 获取物体面数
                                            obj = mc.listRelatives(mesh, p=1, f=1)[0]
                                            faceNum = mc.polyEvaluate(obj, face=1)
                                            mc.sets((obj + u'.f[:' + str(faceNum - 1) + u']'), e=1, forceElement=shaderSG)
                                        # mc.sets(mesh, e=1, forceElement= shaderSG )

            # 隐藏灯光
            for light in lights:
                lightGrp = mc.listRelatives(light, p=1, type='transform', f=1)[0]
                mc.editRenderLayerAdjustment(lightGrp + '.v')
                mc.setAttr((light + '.v'), 0)
                mc.editRenderLayerAdjustment(light + '.intensity')
                mc.setAttr((light + '.intensity'), 0)

            # 设置
            # self.zmRLCommonConfig()

            # 渲染设置
            mc.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')

            # 格式命名
            mc.setAttr('defaultRenderGlobals.animation', 1)
            mc.setAttr('defaultRenderGlobals.putFrameBeforeExt', 1)
            mc.setAttr('defaultRenderGlobals.periodInExt', 1)
            mc.setAttr('defaultRenderGlobals.extensionPadding', 4)
            if mc.getAttr('defaultRenderGlobals.outFormatControl') == 1:
                mc.setAttr('defaultRenderGlobals.outFormatControl', 0)

            # exr
            mc.editRenderLayerAdjustment('defaultRenderGlobals.imageFormat')
            mc.setAttr('defaultRenderGlobals.imageFormat', 51)
            mc.setAttr('defaultRenderGlobals.imfkey', 'exr', type='string')
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.setAttr('mentalrayGlobals.compressionQuality', 0)

            # 16位zip压缩
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.editRenderLayerAdjustment('miDefaultFramebuffer.datatype')
            mc.setAttr('miDefaultFramebuffer.datatype', 16)

            print (u'===============!!!Done  【%s】!!!===============' % (u'%s_RGB层' % layerType))
            print '\n'
        else:
            print (u'===============!!!Error  【%s】无物体!!!===============' % (u'%s_RGB层'))
            print '\n'

    # ALL_ZDEPTH层
    def zmRLZDEPTHCreate(self, layerType, selectObjType=0, distance=14000):
        print (u'===============!!!Start 【%s】!!!===============' % (u'%s_ZDEPTH层' % layerType))
        print 'Working...'

        # 物体
        objs = self.zmRLObjectsTList()
        refCHR = objs[0]
        refPROP = objs[1]
        refSET = objs[2]
        refSKY = objs[3]
        refSEA = objs[4]
        
        depthSG= self.zmRLSGNodesGet()
        SGCHR=depthSG[0]
        SGPROP=depthSG[1]
        SGSET=depthSG[2]

        # 物体
        rlObjs=[]
        needSG=[]
        if layerType == 'ALL':
            rlObjs = refCHR + refPROP + refSET + refSEA
            needSG = SGCHR + SGPROP + SGSET
            layerName = 'ALL_ZDEPTH'

        if layerType == 'BG':
            rlObjs = refSET
            needSG= SGSET
            layerName = 'BG_ZDEPTH'


        # 控制zdepth距离参数
        intState = 0
        setInfo = []
        if mc.ls('SET_GRP'):
            if mc.listRelatives('SET_GRP', c=1, f=1, type='transform'):
                setInfo = mc.listRelatives('SET_GRP', c=1, f=1, type='transform')
        if setInfo:
            for info in setInfo:
                namespace = info.split(':')[0]
                if namespace[-3:] == 'Int':
                    intState = 1
                    break
        if mc.ls('*:*LIGHTING_INT'):
            intState=2
            
        if intState==1:
            distance = 14000           
        if intState==2:
            distance = 750          
        if intState==0:
            distance = 28000

        # 选取模式
        if selectObjType == 1:
            rlObjs = self.zmRLSelectMode()

        if rlObjs:

            # 特殊处理，半透明用,网络读取
            transpancyObjs = self.zmRLTransparencyObjs()
            transpancySGNodes = transpancyObjs[0]
            transpancyMeshes = transpancyObjs[1]
            transpancyNode = transpancyObjs[2]
            
            for obj in transpancySGNodes:                
                print obj+'bbbbbbbbbbbbbbbb'
            print transpancyMeshes
            print transpancyNode

            # 创建RenderLayer
            if mc.ls(layerName):
                mc.delete(layerName)

            mc.createRenderLayer(rlObjs, name=layerName, noRecurse=1, makeCurrent=1)
            # 创建备用材质组
            shader_Node = 'SHD_' + layerType + '_ZDEPTH'
            if mc.ls(shader_Node):
                mc.delete(shader_Node)
            setRange_Z = 'SHD_' + layerType + '_ZDEPTH_setRangeZ'
            if mc.ls(setRange_Z):
                mc.delete(setRange_Z)
            multDiv_Z = 'SHD_' + layerType + '_ZDEPTH_multDivZ'
            if mc.ls(multDiv_Z):
                mc.delete(multDiv_Z)
            sampleInfo_Z = 'SHD_' + layerType + '_ZDEPTH_sampInfoZ'
            if mc.ls(sampleInfo_Z):
                mc.delete(sampleInfo_Z)

            shader_Node = mc.shadingNode('lambert', asShader=True, name=shader_Node)
            mc.setAttr((shader_Node + '.ambientColor'), 1, 1, 1, type='double3')
            mc.setAttr((shader_Node + '.diffuse'), 0)
            setRange_Node = mc.shadingNode('setRange', asUtility=True, name=setRange_Z)
            mc.setAttr((setRange_Node + '.minX'), 1)
            multiplyDivide_Node = mc.shadingNode('multiplyDivide', asUtility=True, name=multDiv_Z)
            mc.setAttr((multiplyDivide_Node + '.input2X'), -1)
            samplerInfo_Node = mc.shadingNode('samplerInfo', asUtility=True, name=sampleInfo_Z)
            mc.addAttr(samplerInfo_Node, longName='NearClipCalimero', nn='Near Clip Calimero', attributeType='float', defaultValue=0.1)
            mc.addAttr(samplerInfo_Node, longName='FarClipCalimero', nn='Far Clip Calimero', attributeType='float', defaultValue=distance)

            # 连接
            mc.connectAttr(('%s.%s') % (setRange_Node, 'outValueX'), ('%s.%s') % (shader_Node, 'colorR'), f=True)
            mc.connectAttr(('%s.%s') % (setRange_Node, 'outValueX'), ('%s.%s') % (shader_Node, 'colorG'), f=True)
            mc.connectAttr(('%s.%s') % (setRange_Node, 'outValueX'), ('%s.%s') % (shader_Node, 'colorB'), f=True)
            mc.connectAttr(('%s.%s') % (samplerInfo_Node, 'NearClipCalimero'), ('%s.%s') % (setRange_Node, 'oldMinX'), f=True)
            mc.connectAttr(('%s.%s') % (samplerInfo_Node, 'FarClipCalimero'), ('%s.%s') % (setRange_Node, 'oldMaxX'), f=True)
            mc.connectAttr(('%s.%s') % (samplerInfo_Node, 'pointCameraZ'), ('%s.%s') % (multiplyDivide_Node, 'input1X'), f=True)
            mc.connectAttr(('%s.%s') % (multiplyDivide_Node, 'outputX'), ('%s.%s') % (setRange_Node, 'valueX'), f=True)
            # 优先全局着色
            if needSG:
                for SGNode in needSG:
                    shaderInfo = mc.listConnections((SGNode + '.surfaceShader'),s = 1,plugs = 1)
                    if not shaderInfo:
                        continue
                    shaderInfo = shaderInfo[0]
                    mc.editRenderLayerAdjustment(SGNode + '.surfaceShader')
                    mc.disconnectAttr(shaderInfo, (SGNode + '.surfaceShader'))
                    mc.connectAttr((shader_Node + '.outColor'), (SGNode + '.surfaceShader'), f=1)
                    


            if transpancySGNodes:
                for i in range(len(transpancySGNodes)):
                    if mc.ls(transpancySGNodes[i]):
                        if '_' not in transpancySGNodes[i]:
                            print u'>>>>>>[注意][%s]名字需要最少有1个_分隔符' % transpancySGNodes[i]
                        else:
                            keySGInfo = transpancySGNodes[i].split('_')[-2]
                        keySGInfo = str(i)
                        meshes = transpancyMeshes[i]
                        for obj in meshes:                        
                            print obj+'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
                        # 有着色物体时才进行
                        if meshes:
                            shaderNode = 'SHD_' + layerType + '_' + keySGInfo + '_ZDEPTH'
                            if mc.ls(shaderNode):
                                mc.delete(shaderNode)
                            setRangeZ = 'SHD_' + layerType + '_' + keySGInfo + '_ZDEPTH_setRangeZ'
                            if mc.ls(setRangeZ):
                                mc.delete(setRangeZ)
                            multDivZ = 'SHD_' + layerType + '_' + keySGInfo + '_ZDEPTH_multDivZ'
                            if mc.ls(multDivZ):
                                mc.delete(multDivZ)
                            sampleInfoZ = 'SHD_' + layerType + '_' + keySGInfo + '_ZDEPTH_sampInfoZ'
                            if mc.ls(sampleInfoZ):
                                mc.delete(sampleInfoZ)

                            shaderNode = mc.shadingNode('lambert', asShader=True, name=shaderNode)
                            mc.setAttr((shaderNode + '.ambientColor'), 1, 1, 1, type='double3')
                            mc.setAttr((shaderNode + '.diffuse'), 0)
                            setRangeNode = mc.shadingNode('setRange', asUtility=True, name=setRangeZ)
                            mc.setAttr((setRangeNode + '.minX'), 1)
                            multiplyDivideNode = mc.shadingNode('multiplyDivide', asUtility=True, name=multDivZ)
                            mc.setAttr((multiplyDivideNode + '.input2X'), -1)
                            samplerInfoNode = mc.shadingNode('samplerInfo', asUtility=True, name=sampleInfoZ)
                            mc.addAttr(samplerInfoNode, longName='NearClipCalimero', nn='Near Clip Calimero', attributeType='float', defaultValue=0.1)
                            mc.addAttr(samplerInfoNode, longName='FarClipCalimero', nn='Far Clip Calimero', attributeType='float', defaultValue=distance)

                            # 连接
                            mc.connectAttr(('%s.%s') % (setRangeNode, 'outValueX'), ('%s.%s') % (shaderNode, 'colorR'), f=True)
                            mc.connectAttr(('%s.%s') % (setRangeNode, 'outValueX'), ('%s.%s') % (shaderNode, 'colorG'), f=True)
                            mc.connectAttr(('%s.%s') % (setRangeNode, 'outValueX'), ('%s.%s') % (shaderNode, 'colorB'), f=True)
                            mc.connectAttr(('%s.%s') % (samplerInfoNode, 'NearClipCalimero'), ('%s.%s') % (setRangeNode, 'oldMinX'), f=True)
                            mc.connectAttr(('%s.%s') % (samplerInfoNode, 'FarClipCalimero'), ('%s.%s') % (setRangeNode, 'oldMaxX'), f=True)
                            mc.connectAttr(('%s.%s') % (samplerInfoNode, 'pointCameraZ'), ('%s.%s') % (multiplyDivideNode, 'input1X'), f=True)
                            mc.connectAttr(('%s.%s') % (multiplyDivideNode, 'outputX'), ('%s.%s') % (setRangeNode, 'valueX'), f=True)

                            # 透明连接
                            self.zmRLTransShaderConnectiion(transpancyNode[i], shaderNode, 'transparency')

                            # 翻转
                            if '.outTransparency' in transpancyNode[i]:
                                mc.editRenderLayerAdjustment(transpancyNode[i].split('.')[0] + '.invert')
                                mc.setAttr((transpancyNode[i].split('.')[0] + ".invert"), 1)


                            
                            shaderInfo = mc.listConnections((transpancySGNodes[i] + '.surfaceShader'),s = 1,plugs = 1)
                            if shaderInfo:
                                shaderInfo = shaderInfo[0]
                                mc.editRenderLayerAdjustment(transpancySGNodes[i] + '.surfaceShader')
                                mc.disconnectAttr(shaderInfo, (transpancySGNodes[i] + '.surfaceShader'))
                                mc.connectAttr((shaderNode + '.outColor'), (transpancySGNodes[i] + '.surfaceShader'), f=1)


            # 渲染设置
            mc.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')

            # 关闭光线追踪
            mc.editRenderLayerAdjustment('miDefaultOptions.rayTracing')
            mc.setAttr('miDefaultOptions.rayTracing', 0)

            # 格式命名
            mc.setAttr('defaultRenderGlobals.animation', 1)
            mc.setAttr('defaultRenderGlobals.putFrameBeforeExt', 1)
            mc.setAttr('defaultRenderGlobals.periodInExt', 1)
            mc.setAttr('defaultRenderGlobals.extensionPadding', 4)
            if mc.getAttr('defaultRenderGlobals.outFormatControl') == 1:
                mc.setAttr('defaultRenderGlobals.outFormatControl', 0)

            # exr
            mc.editRenderLayerAdjustment('defaultRenderGlobals.imageFormat')
            mc.setAttr('defaultRenderGlobals.imageFormat', 51)
            mc.setAttr('defaultRenderGlobals.imfkey', 'exr', type='string')
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.setAttr('mentalrayGlobals.compressionQuality', 0)

            # 16位zip压缩
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.editRenderLayerAdjustment('miDefaultFramebuffer.datatype')
            mc.setAttr('miDefaultFramebuffer.datatype', 16)

            print (u'===============!!!Done  【%s】!!!===============' % (u'%s_ZDEPTH层' % layerType))
            print '\n'
        else:
            print (u'===============!!!Error  【%s】无物体!!!===============' % (u'%s_ZDEPTH层' % layerType))
            print '\n'

    # shadow层
    def zmRLSHDCreate(self, layerType, selectObjType=0):
        print (u'===============!!!Start 【%s】!!!===============' % (u'%s_SHD层' % layerType))
        print 'Working...'

        # 物体
        objs = self.zmRLObjectsTList()
        refCHR = objs[0]
        refPROP = objs[1]
        refSET = objs[2]
        refSKY = objs[3]
        refSEA = objs[4]
        if layerType == 'CHR':
            rlObjs = refCHR + refPROP
            layerName = 'CHR_SHD'
        if layerType == 'BG':
            rlObjs = refSET
            layerName = 'BG_SHD'

        # 灯光
        lights = mc.ls(type='light')

        # 选取模式
        if selectObjType == 1:
            rlObjs = self.zmRLSelectMode()

        if rlObjs:
            # 特殊处理，半透明用,网络读取
            transpancyObjs = self.zmRLTransparencyObjs()
            transpancySGNodes = transpancyObjs[0]
            transpancyMeshes = transpancyObjs[1]
            transpancyNode = transpancyObjs[2]

            # 创建RenderLayer
            if mc.ls(layerName):
                mc.delete(layerName)

            mc.createRenderLayer(rlObjs, name=layerName, noRecurse=1, makeCurrent=1)

            # 通用shadow材质
            shaderNode = 'SHD_' + layerType + '_SHD_Shader'
            if mc.ls(shaderNode):
                mc.delete(shaderNode)
            SHDNode = 'SHD_' + layerType + '_SHD_Node'
            if mc.ls(SHDNode):
                mc.delete(SHDNode)
            SHDSG = 'SHD_' + layerType + '_SHD_SG'
            if mc.ls(SHDSG):
                mc.delete(SHDSG)
            shaderNode = mc.shadingNode('surfaceShader', asShader=True, name=shaderNode)
            SHDNode = mc.shadingNode('mib_amb_occlusion', asTexture=True, name=SHDNode)
            SHDSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=SHDSG)
            mc.connectAttr((shaderNode + '.outColor'), (SHDSG + '.surfaceShader'))
            mc.connectAttr((SHDNode + '.outValue'), (shaderNode + '.outColor'))

            if(layerType == 'BG'):
                mc.setAttr(('%s.%s') % (SHDNode, 'samples'), 64)
                mc.setAttr(('%s.%s') % (SHDNode, 'max_distance'), 10)
                mc.setAttr(('%s.%s') % (SHDNode, 'output_mode'), 3)
            else:
                mc.setAttr(('%s.%s') % (SHDNode, 'samples'), 128)
                mc.setAttr(('%s.%s') % (SHDNode, 'max_distance'), 5)
                mc.setAttr(('%s.%s') % (SHDNode, 'output_mode'), 3)
            # 优先全局着色
            for obj in rlObjs:
                try:
                    mc.sets(obj, e=1, forceElement=SHDSG)
                except:
                    # 获取物体面数
                    faceNum = mc.polyEvaluate(obj, face=1)
                    mc.sets((obj + u'.f[:' + str(faceNum - 1) + u']'), e=1, forceElement=SHDSG)

            # 特殊物体着色
            if transpancySGNodes:
                for i in range(len(transpancySGNodes)):
                    if mc.ls(transpancySGNodes[i]):
                        if '_' not in transpancySGNodes[i]:
                            print u'>>>>>>[注意][%s]名字需要最少有1个_分隔符' % transpancySGNodes[i]
                        else:
                            keySGInfo = transpancySGNodes[i].split('_')[-2]
                        keySGInfo = str(i)
                        meshes = transpancyMeshes[i]
                        # 有着色物体时才进行
                        if meshes:
                            shaderMain = 'SHD_' + layerType + '_' + keySGInfo + '_NM_Main_Shader'
                            if mc.ls(shaderMain):
                                mc.delete(shaderMain)
                            shaderMR = 'SHD_' + layerType + '_' + keySGInfo + '_NM_TransMR_Shader'
                            if mc.ls(shaderMR):
                                mc.delete(shaderMR)
                            SHDNode = 'SHD_' + layerType + '_' + keySGInfo + '_NM_MR_Node'
                            if mc.ls(SHDNode):
                                mc.delete(SHDNode)
                            shaderMRTrans = 'SHD_' + layerType + '_' + keySGInfo + '_NM_TransMR_Shader'
                            if mc.ls(shaderMRTrans):
                                mc.delete(shaderMRTrans)
                            shaderMianSG = 'SHD_' + layerType + '_' + keySGInfo + '_NM_Main_SG'
                            if mc.ls(shaderMianSG):
                                mc.delete(shaderMianSG)
                            shaderTransMRSG = 'SHD_' + layerType + '_' + keySGInfo + '_NM_TransMR_SG'
                            if mc.ls(shaderTransMRSG):
                                mc.delete(shaderTransMRSG)
                            # 创建
                            # SHDNode = mc.shadingNode ('mib_fg_occlusion', asTexture=True, name= SHDNode)
                            SHDNode = mc.shadingNode('mib_amb_occlusion', asTexture=True, name=SHDNode)
                            shaderMRTrans = mc.shadingNode('mib_transparency', asTexture=True, name=shaderMRTrans)
                            shaderMain = mc.shadingNode('lambert', asShader=True, name=shaderMain)
                            shaderMianSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=shaderMianSG)
                            shaderMR = mc.shadingNode('lambert', asShader=True, name=shaderMR)
                            shaderTransMRSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=shaderTransMRSG)
                            # 连接
                            mc.connectAttr((shaderMain + '.outColor'), (shaderMianSG + '.surfaceShader'))
                            mc.connectAttr((shaderMR + '.outColor'), (shaderTransMRSG + '.surfaceShader'))
                            mc.connectAttr((SHDNode + '.outValue'), (shaderTransMRSG + '.miMaterialShader'))
                            mc.connectAttr((shaderMRTrans + '.outValue'), (shaderMianSG + '.miMaterialShader'))
                            mc.connectAttr((SHDNode + '.outValueA'), (shaderMRTrans + '.inputA'))
                            mc.connectAttr((transpancyNode[i].split('.')[0] + '.outAlpha'), (shaderMRTrans + '.transpA'))
                            mc.connectAttr((SHDNode + '.outValue'), (shaderMRTrans + '.input'))

                            # 透明连接
                            self.zmRLTransShaderConnectiion(transpancyNode[i], shaderMRTrans, 'transp')

                            # file贴图反转
                            if '.outTransparency' in transpancyNode[i]:
                                mc.editRenderLayerAdjustment(transpancyNode[i].split('.')[0] + '.invert')
                                mc.setAttr((transpancyNode[i].split('.')[0] + ".invert"), 1)

                            # 设置AO
                            if(layerType == 'BG'):
                                mc.setAttr(('%s.%s') % (SHDNode, 'samples'), 64)
                                mc.setAttr(('%s.%s') % (SHDNode, 'max_distance'), 10)
                                mc.setAttr(('%s.%s') % (SHDNode, 'output_mode'), 3)
                            else:
                                mc.setAttr(('%s.%s') % (SHDNode, 'samples'), 128)
                                mc.setAttr(('%s.%s') % (SHDNode, 'max_distance'), 5)
                                mc.setAttr(('%s.%s') % (SHDNode, 'output_mode'), 3)
                            # 着色
                            for mesh in meshes:
                                if mc.objExists(mesh):
                                    try:
                                        mc.sets(mesh, e=1, forceElement=shaderMianSG)
                                    except:
                                        # 获取物体面数
                                        obj = mc.listRelatives(mesh, p=1, f=1)[0]
                                        faceNum = mc.polyEvaluate(obj, face=1)
                                        mc.sets((obj + u'.f[:' + str(faceNum - 1) + u']'), e=1, forceElement=shaderMianSG)
                            # mc.sets(meshes, e=1, forceElement= shaderMianSG )

            # 隐藏灯光
            for light in lights:
                lightGrp = mc.listRelatives(light, p=1, type='transform', f=1)[0]
                mc.editRenderLayerAdjustment(lightGrp + '.v')
                mc.setAttr((light + '.v'), 0)
                mc.editRenderLayerAdjustment(light + '.intensity')
                mc.setAttr((light + '.intensity'), 0)

            # 设置
            # self.zmRLCommonConfig()

            # 渲染设置
            mc.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')

            # 格式命名
            mc.setAttr('defaultRenderGlobals.animation', 1)
            mc.setAttr('defaultRenderGlobals.putFrameBeforeExt', 1)
            mc.setAttr('defaultRenderGlobals.periodInExt', 1)
            mc.setAttr('defaultRenderGlobals.extensionPadding', 4)
            if mc.getAttr('defaultRenderGlobals.outFormatControl') == 1:
                mc.setAttr('defaultRenderGlobals.outFormatControl', 0)

            # exr
            mc.editRenderLayerAdjustment('defaultRenderGlobals.imageFormat')
            mc.setAttr('defaultRenderGlobals.imageFormat', 51)
            mc.setAttr('defaultRenderGlobals.imfkey', 'exr', type='string')
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.setAttr('mentalrayGlobals.compressionQuality', 0)

            # 16位zip压缩
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.editRenderLayerAdjustment('miDefaultFramebuffer.datatype')
            mc.setAttr('miDefaultFramebuffer.datatype', 16)

            print (u'===============!!!Done  【%s】!!!===============' % (u'%s_NM层' % layerType))
            print '\n'
        else:
            print (u'===============!!!Error  【%s】无物体!!!===============' % (u'%s_NM层' % layerType))
            print '\n'

    # EXTRALIGHT层
    # 新版本
    def zmRLExtraLIGHTCreate(self, layerType, selectObjType=0):
        print (u'===============!!!Start 【%s】!!!===============' % (u'%s_extral层' % layerType))
        print 'Working...'

        # 物体
        objs = self.zmRLObjectsTList()
        refCHR = objs[0]
        refPROP = objs[1]
        refSET = objs[2]
        refSKY = objs[3]
        seaInfo = objs[4]
        
        
        LGTSG= self.zmRLSGNodesGet()
        SGCHR=LGTSG[0]
        SGPROP=LGTSG[1]
        SGSET=LGTSG[2]
        
        rlObjs = []
        needSG = []
        ExtalSG='' 
        EXTAL_mesh='' 
        if layerType == 'ALL':

            rlObjs = refSET + refCHR + refPROP
            needSG = SGCHR + SGPROP + SGSET
            if needSG:
                needSG = list(set(needSG))
            
            EXTAL_meshgrp=[]
            ExtalSGgrp=[]
            if mc.ls('*:*SHD_BulbLAMP'):
                for node in mc.ls('*:*SHD_BulbLAMP'):                                        
                    ExtalSG=mc.listConnections((node+'.outColor'), d=1,plugs=1)[0].split('.')[0]          
                    needSG.remove(ExtalSG)
                    ExtalSGgrp.append(ExtalSG)
                    ExtalSGgrp=list(set(ExtalSGgrp))
            
                    if mc.listConnections((ExtalSG+'.dagSetMembers[0]'), s=1,plugs=1)[0]:
                        EXTAL_mesh=mc.listConnections((ExtalSG+'.dagSetMembers[0]'), s=1,plugs=1)[0].split('.')[0]
                        EXTAL_meshgrp.append(EXTAL_mesh)
                        EXTAL_meshgrp=list(set(EXTAL_meshgrp))
                                
            
    
        #EXTRALIGHT    
        EXTRAL_LIGHT01=[]
        EXTRAL_LIGHT02=[]
        needLightGrps=[]
        if mc.ls('*:*MSH_c_hi_KEY_01'):
            EXTRAL_LIGHT01=mc.ls('*:*MSH_c_hi_KEY_01')
        if mc.ls('*:*MSH_c_hi_EXTRA_01'):
            MSH_c_hi_EXTRA02=mc.ls('*:*MSH_c_hi_EXTRA_01')
            
        needLightGrps01=EXTRAL_LIGHT01
        needLightGrps02=MSH_c_hi_EXTRA02
            

        # 选取模式
        if selectObjType == 1:
            rlObjs = self.zmRLSelectMode()

        if rlObjs:
            # 透明信息
            transpancyObjs = self.zmRLTransparencyObjs()
            transpancySGNodes = transpancyObjs[0]
            transpancyMeshes = transpancyObjs[1]
            transpancyNode = transpancyObjs[2]
                                                  
            from idmt.maya.py_common import sk_infoConfig
            reload(sk_infoConfig)
            import os

            if needLightGrps01:               
                layerName = 'EXTRALIGHT_canel'
                # 创建RenderLayer
                if mc.ls(layerName):
                    mc.delete(layerName)
                # 要加灯光
                mc.createRenderLayer((rlObjs + needLightGrps01), name=layerName, noRecurse=1, makeCurrent=1)
    
                # openSea是否在场景里
                checkAssetID = ['s019001']
                namespaces = mc.namespaceInfo(listOnlyNamespaces=1)
                checkState = 0
                for ID in checkAssetID:
                    for ns in namespaces:
                        if ID in ns:
                            checkState = 1
    
                                                            
                # 通用lambert材质
                shaderNode = 'SHD_' + layerType + '_EXTAL_Shader'
                if mc.ls(shaderNode):
                    mc.delete(shaderNode)
                    
                shaderNode = mc.shadingNode('lambert', asShader=True, name=shaderNode)
                mc.setAttr((shaderNode + '.color'),1,1,1,type='double3')
                
    
                shaderNode_light = 'SHD_' + layerType + '_EXTALight_Shader'
                if mc.ls(shaderNode_light):
                    mc.delete(shaderNode_light)
                    
                shaderNode_light = mc.shadingNode('lambert', asShader=True, name=shaderNode_light)
                mc.setAttr((shaderNode_light + '.color'),1,1,1,type='double3')
                
    
                # 优先全局着色
    
                if needSG:
                    for SGNode in needSG:
                        shaderInfo = mc.listConnections((SGNode + '.surfaceShader'),s = 1,plugs = 1)
                        if not shaderInfo:
                            continue
                        shaderInfo = shaderInfo[0]
                        mc.editRenderLayerAdjustment(SGNode + '.surfaceShader')
                        mc.disconnectAttr(shaderInfo, (SGNode + '.surfaceShader'))
                        mc.connectAttr((shaderNode + '.outColor'), (SGNode + '.surfaceShader'), f=1)
                         
                if ExtalSGgrp:
                    for ExtalSG in ExtalSGgrp:        
                        shaderInfo = mc.listConnections((ExtalSG + '.surfaceShader'),s = 1,plugs = 1)
                        if not shaderInfo:
                            pass
                        shaderInfo = shaderInfo[0]
                        mc.editRenderLayerAdjustment(ExtalSG + '.surfaceShader')
                        mc.disconnectAttr(shaderInfo, (ExtalSG + '.surfaceShader'))
                        mc.connectAttr((shaderNode_light + '.outColor'), (ExtalSG + '.surfaceShader'), f=1) 
                    
      
      
                # 创建passContributionMap
                Map = mc.createNode('passContributionMap', n='passMap')
                mc.connectAttr((layerName + '.passContributionMap'), (Map + '.owner'), na=1)
                obj=''
                if EXTAL_meshgrp:                
                    for EXTAL_mesh in EXTAL_meshgrp:
                        obj=mc.listRelatives(EXTAL_mesh, p=1, ni=1, f=1)[0]
                        mc.connectAttr((obj + '.message'), (Map + '.dagObjects'), na=1)
                    
    
    
                # 创建renderPass节点   
                cusColor = mc.shadingNode('renderPass', asRendering=1, name='customColor')
                mc.setRenderPassType(cusColor,type='CSTCOL')
                mc.setAttr(cusColor+'.numChannels',4)
    
               
                # 使renderPass节点与层和passContributionMap相连
                mc.connectAttr((layerName + '.renderPass'), (cusColor + '.owner'), nextAvailable=1)
    
                mc.connectAttr((cusColor + '.message'), (Map + '.renderPass'), nextAvailable=1)
    
                # 创建writeToColorBuffer节点
                ColorBuffer = mc.shadingNode('writeToColorBuffer', asShader=1, name='colorBuffer')
                mc.setAttr((ColorBuffer + '.color'), 1, 0, 0, type='double3')
                mc.connectAttr((cusColor + '.message'), (ColorBuffer + '.renderPass'))
    
                mc.connectAttr((shaderNode_light + '.outColor'), (ColorBuffer + '.evaluationPassThrough'))      
                              
                # 特殊物体着色
                # LGT新版：每套材质球都存在，transpancySGNodes
                if transpancySGNodes:
                    for i in range(len(transpancySGNodes)):
                        if mc.ls(transpancySGNodes[i]):
                            if '_' not in transpancySGNodes[i]:
                                print u'>>>>>>[注意][%s]名字需要最少有1个_分隔符' % transpancySGNodes[i]
                            else:
                                keySGInfo = transpancySGNodes[i].split('_')[-2]
                            keySGInfo = str(i)
                            meshes = transpancyMeshes[i]
                            # 有着色物体时才进行
                            if meshes:
                                shaderTrsNode = 'SHD_' + layerType + '_' + keySGInfo + '_EXTRALIGHT_Shader'
                                if mc.ls(shaderTrsNode):
                                    mc.delete(shaderTrsNode)
    
    
                                # 创建
                                shaderTrsNode = mc.shadingNode('lambert', asShader=True, name=shaderTrsNode)
                                mc.setAttr((shaderTrsNode + '.color'), 0, 0, 0, type='double3')
                                mc.setAttr((shaderTrsNode + '.ambientColor'), 1, 1, 1, type='double3')
    
    
                                # 透明连接
                                self.zmRLTransShaderConnectiion(transpancyNode[i], shaderTrsNode, 'transparency')
    
                                # file贴图反转
                                if '.outTransparency' in transpancyNode[i]:
                                    mc.editRenderLayerAdjustment(transpancyNode[i].split('.')[0] + '.invert')
                                    mc.setAttr((transpancyNode[i].split('.')[0] + ".invert"), 1)
    
                                # 着色
     
                                shaderInfo = mc.listConnections((transpancySGNodes[i] + '.surfaceShader'),s = 1,plugs = 1)
                                if shaderInfo:
                                    shaderInfo = shaderInfo[0]
                                    mc.editRenderLayerAdjustment(transpancySGNodes[i] + '.surfaceShader')
                                    mc.disconnectAttr(shaderInfo, (transpancySGNodes[i] + '.surfaceShader'))
                                    mc.connectAttr((shaderTrsNode + '.outColor'), (transpancySGNodes[i] + '.surfaceShader'), f=1)

            if needLightGrps02:               
                layerName = 'EXTRALIGHT_volume'
                # 创建RenderLayer
                if mc.ls(layerName):
                    mc.delete(layerName)
                # 要加灯光
                mc.createRenderLayer((rlObjs + needLightGrps02), name=layerName, noRecurse=1, makeCurrent=1)
                
                for obj in rlObjs:
                    mc.select(obj)
                    mel.eval('source "//file-cluster/GDC/Resource/Support/Maya/projects/Lionelville/HbRgbaMaterialTool.mel";HbMaterialM;')
    



            # 渲染设置
            mc.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')

            # 格式命名
            mc.setAttr('defaultRenderGlobals.animation', 1)
            mc.setAttr('defaultRenderGlobals.putFrameBeforeExt', 1)
            mc.setAttr('defaultRenderGlobals.periodInExt', 1)
            mc.setAttr('defaultRenderGlobals.extensionPadding', 4)
            if mc.getAttr('defaultRenderGlobals.outFormatControl') == 1:
                mc.setAttr('defaultRenderGlobals.outFormatControl', 0)

            # exr
            mc.editRenderLayerAdjustment('defaultRenderGlobals.imageFormat')
            mc.setAttr('defaultRenderGlobals.imageFormat', 51)
            mc.setAttr('defaultRenderGlobals.imfkey', 'exr', type='string')
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.setAttr('mentalrayGlobals.compressionQuality', 0)

            # 16位zip压缩
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.editRenderLayerAdjustment('miDefaultFramebuffer.datatype')
            mc.setAttr('miDefaultFramebuffer.datatype', 16)

            print (u'===============!!!Done  【%s】!!!===============' % (u'%s_extal层' % layerType))
            print '\n'
        else:
            print (u'===============!!!Error  【%s】无物体!!!===============' % (u'%s_extal层' % layerType))
            print '\n'

    # transMode 0 本文件读取 | 1 服务器端读取asset
    def zmRlCoAOVsArnold(self, layerName='char_fish', selectObjType=0, transMode=1):
        print (u'===============!!!Start 【Arnold】【%s】!!!===============' % (u'%s_层' % layerName))
        # 选取模式
        rlObjs = ['MDGGRPMASTER']
        if selectObjType == 1:
            rlObjs = self.zmRLSelectMode()

        if rlObjs:
            # 灯光
            lights = []
            if selectObjType == 0:
                lights = mc.ls(type='light')

            if selectObjType == 1:
                lightsNeed = []
                for obj in rlObjs:
                    if 'light' in mc.nodeType(obj):
                        lightsNeed.append(obj)
                    else:
                        shape = mc.listRelatives(obj, c=1, ni=1, f=1)
                        if shape:
                            if 'light' in mc.nodeType(shape[0]):
                                lightsNeed.append(obj)
                    lights = lightsNeed

            # 特殊处理，半透明用,网络读取
            if transMode:
                transpancyObjs = self.zmRLTransparencyObjs()
                transpancySGNodes = transpancyObjs[0]
                transpancyMeshes = transpancyObjs[1]
                transpancyNode = transpancyObjs[2]

            if transMode == 0:
                transpancyObjs = self.zmRLTransparencyObjsOld()
                transpancySGNodes = []
                transpancyMeshes = []
                transpancyNode = []
                if transpancyObjs:
                    for transGrp in transpancyObjs:
                        transpancySGNodes.append(transGrp[0])
                        transpancyMeshes.append(transGrp[1])
                        transpancyNode.append(transGrp[2])

            # skyDomeLight
            skyDomeLight = 'idmt_skyDome'
            if mc.ls(skyDomeLight):
                mc.delete(skyDomeLight)
            skyTransform = 'idmt_skyDome_transform'
            if mc.ls(skyTransform):
                mc.delete(skyTransform)
            # skyDomeLight = mc.createNode('aiSkyDomeLight' ,name = skyDomeLight)
            skyDomeLight = mc.shadingNode('aiSkyDomeLight', asUtility=1, name=skyDomeLight)
            skyTransform = mc.listRelatives(skyDomeLight, f=1, p=1)[0]
            skyTransform = mc.rename(skyTransform, 'idmt_skyDome_transform')
            # mc.connectAttr(('%s.%s') % ('transform1' , 'instObjGroups') , ('%s.%s') % ('defaultLightSet' , 'dagSetMembers'), f=True)
            mc.connectAttr("%s.instObjGroups" % skyTransform, "defaultLightSet.dagSetMembers", nextAvailable=True)
            mc.setAttr((skyDomeLight + '.intensity'), 0.6)
            mc.setAttr((skyDomeLight + '.aiSamples'), 0.6)

            # 创建RenderLayer
            if mc.ls(layerName):
                mc.delete(layerName)

            # 建立层
            mc.createRenderLayer((rlObjs + [skyDomeLight]), name=layerName, noRecurse=1, makeCurrent=1)

            # setting
            mc.editRenderLayerAdjustment('defaultArnoldDriver.halfPrecision')
            mc.setAttr('defaultArnoldDriver.halfPrecision', 1)
            mc.editRenderLayerAdjustment('defaultArnoldDriver.autocrop')
            mc.setAttr('defaultArnoldDriver.autocrop', 1)
            mc.editRenderLayerAdjustment('defaultArnoldRenderOptions.AASamples')
            mc.setAttr('defaultArnoldRenderOptions.AASamples', 4)
            mc.editRenderLayerAdjustment('defaultArnoldRenderOptions.GIDiffuseSamples')
            mc.setAttr('defaultArnoldRenderOptions.GIDiffuseSamples', 0)
            mc.editRenderLayerAdjustment('defaultArnoldRenderOptions.GIGlossySamples')
            mc.setAttr('defaultArnoldRenderOptions.GIGlossySamples', 0)
            mc.editRenderLayerAdjustment('defaultArnoldRenderOptions.GIRefractionSamples')
            mc.setAttr('defaultArnoldRenderOptions.GIRefractionSamples', 0)
            mc.editRenderLayerAdjustment('defaultArnoldRenderOptions.sssBssrdfSamples')
            mc.setAttr('defaultArnoldRenderOptions.sssBssrdfSamples', 3)
            mc.editRenderLayerAdjustment('defaultArnoldRenderOptions.lock_sampling_noise')
            mc.setAttr('defaultArnoldRenderOptions.lock_sampling_noise', 1)
            mc.editRenderLayerAdjustment('defaultArnoldRenderOptions.textureAutomip')
            mc.setAttr('defaultArnoldRenderOptions.textureAutomip', 0)
            mc.editRenderLayerAdjustment('defaultArnoldRenderOptions.textureAcceptUnmipped')
            mc.setAttr('defaultArnoldRenderOptions.textureAcceptUnmipped', 0)
            mc.editRenderLayerAdjustment('defaultArnoldRenderOptions.use_existing_tiled_textures')
            mc.setAttr('defaultArnoldRenderOptions.use_existing_tiled_textures', 1)

            # shader
            # occ
            AOShader = 'SHD_AO'
            if mc.ls(AOShader):
                mc.delete(AOShader)
            AOSG = 'SHD_AO_SG'
            if mc.ls(AOSG):
                mc.delete(AOSG)
            AOShader = mc.shadingNode('aiAmbientOcclusion', asShader=True, name=AOShader)
            AOSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=(AOSG))
            mc.connectAttr(('%s.%s') % (AOShader, 'outColor'), ('%s.%s') % (AOSG, 'surfaceShader'), f=True)
            # nomal
            NMShader = 'SHD_NM'
            if mc.ls(NMShader):
                mc.delete(NMShader)
            NMSG = 'SHD_NM_SG'
            if mc.ls(NMSG):
                mc.delete(NMSG)
            NMShader = mc.shadingNode('aiUtility', asShader=True, name=NMShader)
            NMSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=(NMSG))
            mc.setAttr((NMShader + '.shadeMode'), 2)
            mc.setAttr((NMShader + '.colorMode'), 3)
            mc.connectAttr(('%s.%s') % (NMShader, 'outColor'), ('%s.%s') % (NMSG, 'surfaceShader'), f=True)
            # fresnel
            FNShader = 'SHD_Fresnel'
            if mc.ls(FNShader):
                mc.delete(FNShader)
            FNRamp = 'SHD_Fresnel_ramp'
            if mc.ls(FNRamp):
                mc.delete(FNRamp)
            FNSample = 'SHD_Fresnel_Sample'
            if mc.ls(FNSample):
                mc.delete(FNSample)
            FNSG = 'SHD_Fresnel_SG'
            if mc.ls(FNSG):
                mc.delete(FNSG)
            FNShader = mc.shadingNode('aiUtility', asShader=True, name=FNShader)
            FNRamp = mc.shadingNode('ramp', asShader=True, name=FNRamp)
            FNSample = mc.shadingNode('samplerInfo', asShader=True, name=FNSample)
            FNSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=(FNSG))
            mc.removeMultiInstance((FNRamp + '.colorEntryList[1]'), b=1)
            mc.setAttr((FNShader + '.shadeMode'), 2)
            mc.setAttr((FNRamp + '.interpolation'), 3)
            mc.setAttr((FNRamp + '.colorEntryList[2].position'), 1)
            mc.setAttr((FNRamp + '.colorEntryList[0].position'), 0)
            mc.setAttr((FNRamp + '.colorEntryList[2].color'), 0, 0, 0, type='double3')
            mc.setAttr((FNRamp + '.colorEntryList[0].color'), 1, 1, 1, type='double3')
            mc.connectAttr(('%s.%s') % (FNShader, 'outColor'), ('%s.%s') % (FNSG, 'surfaceShader'), f=True)
            mc.connectAttr(('%s.%s') % (FNSample, 'facingRatio'), ('%s.%s') % (FNRamp, 'uCoord'), f=True)
            mc.connectAttr(('%s.%s') % (FNSample, 'facingRatio'), ('%s.%s') % (FNRamp, 'vCoord'), f=True)
            mc.connectAttr(('%s.%s') % (FNRamp, 'outColor'), ('%s.%s') % (FNShader, 'color'), f=True)

            # dirver
            mc.setAttr('defaultArnoldDriver.mergeAOVs', 1)
            # renderpass
            # Z
            ZArnoldPass = 'aiAOV_Z'
            if mc.ls(ZArnoldPass):
                if mc.nodeType(ZArnoldPass) == 'aiAOV':
                    pass
                else:
                    mc.delete(ZArnoldPass)
                    mc.createNode('aiAOV', name=ZArnoldPass)
            else:
                mc.createNode('aiAOV', name=ZArnoldPass)
            mc.setAttr((ZArnoldPass + '.name'), 'Z', type='string')
            mc.setAttr((ZArnoldPass + '.type'), 4)
            # occ
            occArnoldPass = 'aiAOV_occ'
            if mc.ls(occArnoldPass):
                if mc.nodeType(occArnoldPass) == 'aiAOV':
                    pass
                else:
                    mc.delete(occArnoldPass)
                    mc.createNode('aiAOV', name=occArnoldPass)
            else:
                mc.createNode('aiAOV', name=occArnoldPass)
            mc.setAttr((occArnoldPass + '.name'), 'occ', type='string')
            mc.setAttr((occArnoldPass + '.type'), 5)
            # normal
            nmArnoldPass = 'aiAOV_normal'
            if mc.ls(nmArnoldPass):
                if mc.nodeType(nmArnoldPass) == 'aiAOV':
                    pass
                else:
                    mc.delete(nmArnoldPass)
                    mc.createNode('aiAOV', name=nmArnoldPass)
            else:
                mc.createNode('aiAOV', name=nmArnoldPass)
            mc.setAttr((nmArnoldPass + '.name'), 'normal', type='string')
            mc.setAttr((nmArnoldPass + '.type'), 5)
            # frese1
            fresenlArnoldPass = 'aiAOV_fresnel'
            if mc.ls(fresenlArnoldPass):
                if mc.nodeType(fresenlArnoldPass) == 'aiAOV':
                    pass
                else:
                    mc.delete(fresenlArnoldPass)
                    mc.createNode('aiAOV', name=fresenlArnoldPass)
            else:
                mc.createNode('aiAOV', name=fresenlArnoldPass)
            mc.setAttr((fresenlArnoldPass + '.name'), 'fresnel', type='string')
            mc.setAttr((fresenlArnoldPass + '.type'), 5)
            # aiAOVFilter
            # closset
            aiAOVFilter_Closset = 'defaultArnoldFilter_Closset'
            if mc.ls(aiAOVFilter_Closset):
                if mc.nodeType(aiAOVFilter_Closset) == 'aiAOVFilter':
                    pass
                else:
                    mc.delete(aiAOVFilter_Closset)
                    mc.createNode('aiAOVFilter', name=aiAOVFilter_Closset)
            else:
                mc.createNode('aiAOVFilter', name=aiAOVFilter_Closset)

            # 连接
            # Z
            mc.connectAttr(('%s.%s') % ('defaultArnoldDriver', 'message'), ('%s.%s') % (ZArnoldPass, 'outputs[0].driver'), f=True)
            mc.connectAttr(('%s.%s') % (aiAOVFilter_Closset, 'message'), ('%s.%s') % (ZArnoldPass, 'outputs[0].filter'), f=True)
            mc.connectAttr(('%s.%s') % (ZArnoldPass, 'message'), ('%s.%s') % ('defaultArnoldRenderOptions', 'aovList[0]'), f=True)
            # occ
            mc.connectAttr(('%s.%s') % ('defaultArnoldDriver', 'message'), ('%s.%s') % (occArnoldPass, 'outputs[0].driver'), f=True)
            mc.connectAttr(('%s.%s') % ('defaultArnoldFilter', 'message'), ('%s.%s') % (occArnoldPass, 'outputs[0].filter'), f=True)
            mc.connectAttr(('%s.%s') % (AOShader, 'outColor'), ('%s.%s') % (occArnoldPass, 'defaultValue'), f=True)
            mc.connectAttr(('%s.%s') % (occArnoldPass, 'message'), ('%s.%s') % ('defaultArnoldRenderOptions', 'aovList[1]'), f=True)
            # normal
            mc.connectAttr(('%s.%s') % ('defaultArnoldDriver', 'message'), ('%s.%s') % (nmArnoldPass, 'outputs[0].driver'), f=True)
            mc.connectAttr(('%s.%s') % ('defaultArnoldFilter', 'message'), ('%s.%s') % (nmArnoldPass, 'outputs[0].filter'), f=True)
            mc.connectAttr(('%s.%s') % (NMShader, 'outColor'), ('%s.%s') % (nmArnoldPass, 'defaultValue'), f=True)
            mc.connectAttr(('%s.%s') % (nmArnoldPass, 'message'), ('%s.%s') % ('defaultArnoldRenderOptions', 'aovList[2]'), f=True)
            # frese
            mc.connectAttr(('%s.%s') % ('defaultArnoldDriver', 'message'), ('%s.%s') % (fresenlArnoldPass, 'outputs[0].driver'), f=True)
            mc.connectAttr(('%s.%s') % ('defaultArnoldFilter', 'message'), ('%s.%s') % (fresenlArnoldPass, 'outputs[0].filter'), f=True)
            mc.connectAttr(('%s.%s') % (FNShader, 'outColor'), ('%s.%s') % (fresenlArnoldPass, 'defaultValue'), f=True)
            mc.connectAttr(('%s.%s') % (fresenlArnoldPass, 'message'), ('%s.%s') % ('defaultArnoldRenderOptions', 'aovList[3]'), f=True)

            # Back To MasterLayer
            mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')
            # Unrender MasterLayer
            mc.setAttr("defaultRenderLayer.renderable", 0)

            print (u'===============!!!Done 【Arnold】【%s】!!!===============' % (u'%s_层' % layerName))
            print '\n'
        else:
            print (u'===============!!!Error 【Arnold】【%s】无物体!!!===============' % (u'%s_层' % layerName))
            print '\n'
            
    #【通用：RGB分层信息】
    
    # 测试用RGBM材质创建

    def zmRGBMShaderCreate(self, RGBType):
        # 选取模式
        rlObjs = self.zmRLSelectMode()
        print "................................."
        print rlObjs

        if rlObjs:
            needObjs = []
            meshes = mc.listRelatives(rlObjs, ad=1, ni=1, type='mesh', f=1)
            if meshes:
                needObjs = mc.listRelatives(meshes, p=1, type='transform', f=1)
            rlObjs = list(set(needObjs))

            # 先回到masterLayer
            # Back To MasterLayer
            # 读取当前所在的渲染层
            layerNow = mel.eval('editRenderLayerGlobals -q -currentRenderLayer')
            if layerNow != 'defaultRenderLayer':

                # 特殊处理，半透明用,网络读取
                transpancyObjs = self.zmRLTransparencyObjs()
                transpancySGNodes = transpancyObjs[0]
                transpancyMeshes = transpancyObjs[1]
                transpancyNode = transpancyObjs[2]

                mel.eval('editRenderLayerGlobals -currentRenderLayer \"' + layerNow + '\"')

                # 通用RGB材质
                shaderNode = 'SHD_' + RGBType + '_Shader'
                if mc.ls(shaderNode):
                    pass
                else:
                    shaderNode = mc.shadingNode('lambert', asShader=True, name=shaderNode)

                shaderSG = 'SHD_' + RGBType + '_SG'
                if mc.ls(shaderSG):
                    pass
                else:
                    shaderSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=shaderSG)

                if RGBType == 'R':
                    color = [1, 0, 0]
                    mc.setAttr((shaderNode + '.matteOpacity'), 0)
                if RGBType == 'G':
                    color = [0, 1, 0]
                    mc.setAttr((shaderNode + '.matteOpacity'), 0)
                if RGBType == 'B':
                    color = [0, 0, 1]
                    mc.setAttr((shaderNode + '.matteOpacity'), 0)
                if RGBType == 'M':
                    color = [0, 0, 0]
                    mc.setAttr((shaderNode + '.matteOpacityMode'), 0)
                mc.setAttr((shaderNode + '.color'), color[0], color[1], color[2], type='double3')
                mc.setAttr((shaderNode + '.ambientColor'), 1, 1, 1, type='double3')
                mc.setAttr((shaderNode + '.diffuse'), 0)

                try:
                    mc.connectAttr((shaderNode + '.outColor'), (shaderSG + '.surfaceShader'))
                except:
                    pass

                # 优先全局着色，赋予Mask
                for obj in rlObjs:
                    try:
                        mc.sets(obj, e=1, forceElement=shaderSG)
                    except:
                        # 获取物体面数
                        faceNum = mc.polyEvaluate(obj, face=1)
                        mc.sets((obj + u'.f[:' + str(faceNum - 1) + u']'), e=1, forceElement=shaderSG)
                # mc.sets(rlObjs, e=1, forceElement= shaderSG )

                # 对于mesh之间，同一类材质的不同物体使用不同的RGBM Shader特殊处理
                if transpancySGNodes:
                    for i in range(len(transpancySGNodes)):
                        if mc.ls(transpancySGNodes[i]):
                            if '_' not in transpancySGNodes[i]:
                                print u'>>>>>>[注意][%s]名字需要最少有1个_分隔符' % transpancySGNodes[i]
                            else:
                                keySGInfo = transpancySGNodes[i].split('_')[-2]
                            keySGInfo = str(i)
                            meshes = transpancyMeshes[i]
                            # 有着色物体时才进行
                            if meshes:
                                for obj in rlObjs:
                                    for mesh in meshes:
                                        if obj.split('|')[-1] in mesh:
                                        # if obj in meshes:
                                            shaderTrsNode = 'SHD_' + RGBType + '_' + keySGInfo + '_Shader'
                                            if mc.ls(shaderTrsNode):
                                                pass
                                            else:
                                                shaderTrsNode = mc.shadingNode('lambert', asShader=True, name=shaderTrsNode)
                                            shaderTrsSG = 'SHD_' + RGBType + '_' + keySGInfo + '_SG'
                                            if mc.ls(shaderTrsSG):
                                                pass
                                            else:
                                                shaderTrsSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=shaderTrsSG)
                                            # 创建
                                            # shaderTrsNode = mc.shadingNode ('surfaceShader', asShader=True, name= shaderTrsNode)
                                            # shaderTrsSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name= shaderTrsSG)
                                            if RGBType == 'R':
                                                mc.setAttr((shaderTrsNode + '.matteOpacity'), 0)
                                            if RGBType == 'G':
                                                mc.setAttr((shaderTrsNode + '.matteOpacity'), 0)
                                            if RGBType == 'B':
                                                mc.setAttr((shaderTrsNode + '.matteOpacity'), 0)
                                            if RGBType == 'M':
                                                mc.setAttr((shaderTrsNode + '.matteOpacityMode'), 0)
                                            mc.setAttr((shaderTrsNode + '.color'), color[0], color[1], color[2], type='double3')
                                            mc.setAttr((shaderTrsNode + '.ambientColor'), 1, 1, 1, type='double3')
                                            mc.setAttr((shaderTrsNode + '.diffuse'), 0)

                                            # 连接
                                            try:
                                                mc.connectAttr((shaderTrsNode + '.outColor'), (shaderTrsSG + '.surfaceShader'))
                                            except:
                                                pass

                                            # 透明连接
                                            self.zmRLTransShaderConnectiion(transpancyNode[i], shaderTrsNode, 'transparency')

                                            # 着色
                                            try:
                                                mc.sets(obj, e=1, forceElement=shaderTrsSG)
                                            except:
                                                # 获取物体面数
                                                faceNum = mc.polyEvaluate(obj, face=1)
                                                mc.sets((obj + u'.f[:' + str(faceNum - 1) + u']'), e=1, forceElement=shaderTrsSG)
                                            # mc.sets(obj, e=1, forceElement= shaderTrsSG )
                                            # 处理File

                                            if '.outTransparency' in transpancyNode[i]:
                                                mc.editRenderLayerAdjustment(transpancyNode[i].split('.')[0] + '.invert')
                                                mc.setAttr((transpancyNode[i].split('.')[0] + ".invert"), 1)

        print (u'===============!!!Shader 【%s】 Created!!!===============' % RGBType)
        print '\n'

    # 分层信息输出
    def zmRLayerInfoExport(self, layerType='RGB', LayerName='myRGB', exportType='all'):
        from idmt.maya.py_common import sk_infoConfig
        reload(sk_infoConfig)
        localPath = sk_infoConfig.sk_infoConfig().checkLayerInfoLocalPath(layerType, LayerName)

        fileName = layerType + '_' + exportType + '_geo.txt'
        filePath = localPath + fileName
        # 输出物体
        objs = mc.ls(sl=1)
        if objs:
            sk_infoConfig.sk_infoConfig().checkFileWrite(filePath, objs)

    # 分层信息读取
    def zmRLayerInfoImport(self, layerType='RGB', LayerName='myRGB', exportType='all'):
        from idmt.maya.py_common import sk_infoConfig
        reload(sk_infoConfig)
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        serverPath = sk_infoConfig.sk_infoConfig().checkLayerInfoServerPath(layerType, LayerName)

        # 读文件
        fileName = layerType + '_' + exportType + '_geo.txt'
        filePath = serverPath + fileName
        import os
        if os.path.exists(filePath):
            objs = sk_infoConfig.sk_infoConfig().checkFileRead(filePath)
            return objs
        else:
            mc.error(u'===========指定信息文件【%s】不存在===========' % fileName)

    # 获取文件内所有RGB素材信息
    def zmRLayerRGBObjectsConfig(self, checkType):
        # 获取所有服务器端素材信息
        from idmt.maya.py_common import sk_infoConfig
        reload(sk_infoConfig)
        from idmt.maya.py_common import sk_checkCommon
        reload(sk_checkCommon)
        serverPath = sk_infoConfig.sk_infoConfig().checkLayerInfoServerPath('RGB')[:-6]
        allSolution = mc.getFileList(folder=serverPath)
        if 'myRGB' in allSolution:
            allSolution.remove('allAsset')
        # 获取本文件内指定类型信息
        # 每个元素为2单位的list，其一为文件内的namespace，其二为标准asset的namespace
        assetFileInfo = sk_infoConfig.sk_infoConfig().checkAsset2FileObjsConfig(checkType)
        if allSolution and assetFileInfo:
            # 获取文件内需要的asstNamespace及对应的标准namespace
            assetFileNamespaces = []
            assetRealNames = []
            for assetFile in assetFileInfo:
                assetFileNamespaces.append(assetFile[0])
                assetRealNames.append(assetFile[1])
            # 记录
            assetFileAll = []
            assetFileR = []
            assetFileG = []
            assetFileB = []
            # 应该先从服务器端方案信息里筛选
            for solution in allSolution:
                assetAllInfo = self.zmRLayerInfoImport(layerType='RGB', LayerName=solution, exportType='all')
                if assetAllInfo:
                    solutionNamespace = assetAllInfo[0].split(':')[0]
                    # print solutionNamespace
                    # print assetRealNames
                    # 方案内asset在文件内的真实asset内时进行换算名字
                    if solutionNamespace in assetRealNames:
                        infoIndex = assetRealNames.index(solutionNamespace)
                        assetFileNamespace = assetFileNamespaces[infoIndex]
                        assetRInfo = self.zmRLayerInfoImport(layerType='RGB', LayerName=solution, exportType='R')
                        assetGInfo = self.zmRLayerInfoImport(layerType='RGB', LayerName=solution, exportType='G')
                        assetBInfo = self.zmRLayerInfoImport(layerType='RGB', LayerName=solution, exportType='B')
                        # 处理成本文件信息
                        for obj in assetAllInfo:
                            assetFileAll.append((assetFileNamespace + ':' + obj[(len(solutionNamespace) + 1):]))
                        if assetRInfo:
                            for obj in assetRInfo:
                                assetFileR.append((assetFileNamespace + ':' + obj[(len(solutionNamespace) + 1):]))
                        if assetGInfo:
                            for obj in assetGInfo:
                                assetFileG.append((assetFileNamespace + ':' + obj[(len(solutionNamespace) + 1):]))
                        if assetBInfo:
                            for obj in assetBInfo:
                                assetFileB.append((assetFileNamespace + ':' + obj[(len(solutionNamespace) + 1):]))
                    else:
                        pass
            # 统一记录
            needFileObjInfo = [assetFileAll, assetFileR, assetFileG, assetFileB]
            return needFileObjInfo

    # 删除SET reference
    def zmRLayerSetReferenceDel(self):
        from idmt.maya.py_common import sk_referenceConfig
        reload(sk_referenceConfig)
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refNodes = refInfos[0][0]
        refPaths = refInfos[1][0]
        if refNodes:
            for ref in refNodes:
                if '_' in ref:
                    if ref.split('_')[1][0] in ['s', 'S']:
                        # 删除参考
                        mc.file(rfn=ref, removeReference=1)

    # 处理exr压缩格式
    def zmRLayerExrWriteMode(self):
        # 获取文件前缀名
        fileName = mc.renderSettings(fin=1, lin=1, lut=1)
        filePreName = fileName[0].split('.')[0]
        fileNameType = fileName[0].split('.')[-1]
        if fileNameType == 'iff':
            frameCurrect = mc.currentTime(q=1)
            # 处理成四位string
            frameString = ''
            if (frameCurrect / 1000) >= 1:
                frameString = str(frameCurrect).split('.')[0]
            else:
                if (frameCurrect / 100) >= 1:
                    frameString = '0' + str(frameCurrect).split('.')[0]
                else:
                    if (frameCurrect / 10) >= 1:
                        frameString = '00' + str(frameCurrect).split('.')[0]
                    else:
                        frameString = '000' + str(frameCurrect).split('.')[0]
            fileFullName = filePreName + '.' + frameString + '.' + fileNameType

    # Zdepth distance UI
    def zmRLayerZdepthDistanceConfigUI(self):
        if mc.window('Zdepth_Distance_UI', q=True, exists=True):
            mc.deleteUI('Zdepth_Distance_UI')
        mc.window('Zdepth_Distance_UI', t=(unicode('Zdepth_Distance_UI', 'utf8')), wh=[320, 90], mb=True)

        # 主界面
        mc.columnLayout()

        # 分解创建
        mc.frameLayout(label=u'Zdepth_Distance', borderStyle='etchedOut', width=320)

        mc.rowLayout()
        mc.intFieldGrp('Zdepth_Distance_Value', l=u'距离设置: ', value1=15000)
        mc.setParent("..")

        mc.setParent("..")

        mc.rowLayout()
        mc.button(label=u'[变更设置]', width=320, c='sk_renderLayer_ZoomWhiteDolphin.zmRLConfig().zmRLayerZdepthDistanceConfig()')
        mc.setParent("..")

        mc.showWindow()

    # Zdepth distance Config
    def zmRLayerZdepthDistanceConfig(self):
        value = mc.intFieldGrp('Zdepth_Distance_Value', value=1, q=1)[0]
        samplerInfoNodes = mc.ls(type='samplerInfo')
        if samplerInfoNodes:
            for node in samplerInfoNodes:
                if mc.objExists(node + '.FarClipCalimero'):
                    mc.setAttr((node + '.FarClipCalimero'), value)

    # skydome config
    def zmRLSkydomeMoodConfig(self):
        # 获取合格的LightingGrp
        lightGrps =  mc.ls(['*:*LIGHTING','*:*LIGHTING_EXT','*:*LIGHTING_INT'])
        needAsset = ['s019001']
        needLightGrps = []
        if lightGrps:
            for grp in lightGrps:
                for asset in needAsset:
                    if asset in grp:
                        needLightGrps.append(grp)
        # 处理贴图
        moodStyleList = ['Day', 'SunRise', 'Sunset', 'Night_On', 'Night_Off']
        if needLightGrps:
            for needGrp in needLightGrps:
                ns = needGrp.split(':')[0]
                # 获取mood
                moodState = mc.getAttr(needGrp + '.Mood')
                moodStyle = moodStyleList[moodState]
                if moodStyle:
                    # 获取file节点
                    fileNodes = mc.ls((ns + ':*'), type='file')
                    if fileNodes:
                        for fileNode in fileNodes:
                            txPath = mc.getAttr(fileNode + '.fileTextureName')
                            fileNameKey = txPath.split('/')[-1].split('.')[0].split('_')[-1]
                            if fileNameKey in moodStyleList:
                                # 开始处理路径
                                newTxPath = txPath.replace(fileNameKey, moodStyle)
                                print newTxPath
                                mc.setAttr((fileNode + '.fileTextureName'), newTxPath, type='string')
        
        # hide
        '''
        cyclosGrp = mc.ls('*:*MSH_c_hi_Cyclos',type = 'transform',l=1)
        if cyclosGrp:
            meshes = mc.listRelatives(cyclosGrp,ad = 1,type = 'mesh',f = 1)
            if not meshes:
                return 0
            polyGrps = mc.listRelatives(meshes,p = 1,type = 'transform',f = 1)
            if not polyGrps:
                return 0
            polyGrps = list(set(polyGrps))
            for grp in polyGrps:
                stateValue = 0
                for mood in moodStyleList:
                    if ('|' + mood.upper() + '|') in grp:
                        stateValue = 1
                if stateValue == 0:
                    mc.setAttr((grp+'.v'),0)
                else:
                    mc.setAttr((grp+'.v'),1)
                    '''
        

    # SG节点处理
    def zmRLSGNodeCleanConfig(self, sgNode):
        sgSAttrs = ['miOpaque', 'miContourEnable', 'miContourAlpha', 'miContourRelativeWidth', 'miContourWidth', 'miExportMrMaterial', 'miExportMrMaterial', 'miExportVolumeSampler', 'caching', 'rmbCommand', 'templateName', 'templatePath', 'viewName', 'iconName', 'viewMode', 'templateVersion', 'uiTreatment', 'customTreatment', 'creator', 'creationDate', 'containerType']
        sgCAttrs = ['surfaceShader', 'volumeShader', 'displacementShader', 'miContourColor', 'miMaterialShader', 'miShadowShader', 'miVolumeShader', 'miPhotonShader', 'miPhotonVolumeShader', 'miDisplacementShader', 'miEnvironmentShader', 'miLightMapShader', 'miContourShader', ]
        # 属性连接断开
        for attr in sgCAttrs:
            if mc.objExists(sgNode + '.' + attr):
                connectAttr = mc.listConnections((sgNode + '.' + attr), s=1, plugs=1)
                if connectAttr:
                    mc.editRenderLayerAdjustment(sgNode + '.' + attr)
                    mc.disconnectAttr(connectAttr[0], (sgNode + '.' + attr))
        # 属性值还原
        SGAttr = (sgNode + '.miOpaque')
        mc.editRenderLayerAdjustment(SGAttr)
        mc.setAttr(SGAttr, 0)

        SGAttr = (sgNode + '.miCutAwayOpacity')
        mc.editRenderLayerAdjustment(SGAttr)
        mc.setAttr(SGAttr, 0)

        SGAttr = (sgNode + '.miContourEnable')
        mc.editRenderLayerAdjustment(SGAttr)
        mc.setAttr(SGAttr, 0)

        SGAttr = (sgNode + '.miContourAlpha')
        mc.editRenderLayerAdjustment(SGAttr)
        mc.setAttr(SGAttr, 0)

        SGAttr = (sgNode + '.miContourRelativeWidth')
        mc.editRenderLayerAdjustment(SGAttr)
        mc.setAttr(SGAttr, 0)

        SGAttr = (sgNode + '.miContourWidth')
        mc.editRenderLayerAdjustment(SGAttr)
        mc.setAttr(SGAttr, 1.25)

        SGAttr = (sgNode + '.miExportMrMaterial')
        mc.editRenderLayerAdjustment(SGAttr)
        mc.setAttr(SGAttr, 0)

        SGAttr = (sgNode + '.miExportShadingEngine')
        mc.editRenderLayerAdjustment(SGAttr)
        mc.setAttr(SGAttr, 1)

        SGAttr = (sgNode + '.miExportVolumeSampler')
        mc.editRenderLayerAdjustment(SGAttr)
        mc.setAttr(SGAttr, 0)

        SGAttr = (sgNode + '.caching')
        mc.editRenderLayerAdjustment(SGAttr)
        mc.setAttr(SGAttr, 0)

        SGAttr = (sgNode + '.nodeState')
        mc.editRenderLayerAdjustment(SGAttr)
        mc.setAttr(SGAttr, 0)

        SGAttr = (sgNode + '.blackBox')
        mc.editRenderLayerAdjustment(SGAttr)
        mc.setAttr(SGAttr, 0)

        SGAttr = (sgNode + '.viewMode')
        mc.editRenderLayerAdjustment(SGAttr)
        mc.setAttr(SGAttr, 2)

        SGAttr = (sgNode + '.templateVersion')
        mc.editRenderLayerAdjustment(SGAttr)
        mc.setAttr(SGAttr, 1)

        SGAttr = (sgNode + '.uiTreatment')
        mc.editRenderLayerAdjustment(SGAttr)
        mc.setAttr(SGAttr, 1000)

        SGAttr = (sgNode + '.uiTreatment')
        mc.editRenderLayerAdjustment(SGAttr)
        mc.setAttr(SGAttr, 1000)
        
        
        
        # 获取所有SG节点
    def zmRLSGNodesGet(self):
        SGNodes = mc.ls(type='shadingEngine')
        SGNodes.remove('initialParticleSE')
        SGNodes.remove('initialShadingGroup')
        # SG分类
        refSGCHR = []
        refSGPROP = []
        refSGSET = []
        # 判断分类
        # 根据连接的物体的参考进行判断
        for SGNode in SGNodes:
            listMeshTransform = mc.listConnections(SGNode, type='mesh')
            if listMeshTransform:
                for obj in listMeshTransform:
                    if ':' in obj:
                        objspe=(obj.split(':')[0]).split('_')[1]
                        if objspe:
                            if objspe[0].lower()=='c':
                                refSGCHR.append(SGNode)
                            if objspe[0].lower()=='s':
                                refSGSET.append(SGNode)
                            if objspe[0].lower()=='p':
                                refSGPROP.append(SGNode)
          
        result = []
        result.append(refSGCHR)
        result.append(refSGPROP)
        result.append(refSGSET)
        return result





    #双面材质
    def zmRLSelectMSKreate(self, layerType, selectObjType=0):
        print (u'===============!!!Start 【%s】!!!===============' % (u'%s_side层' % 'Double'))
        print 'Working...'
        
        LGTSG= self.zmRLSGNodesGet()
        SGCHR=LGTSG[0]
        SGPROP=LGTSG[1]
        SGSET=LGTSG[2]
        
        rlObjs = self.zmRLSelectMode()                    
        needSG = []
    
        # 物体
        shaderSG=[]
        SGNodes=[]
        
        needSG = SGCHR + SGPROP + SGSET
        if needSG:
            needSG = list(set(needSG))

        if rlObjs:
            layerName = 'Double_side'
            for obj in rlObjs:
                mesh = mc.listRelatives(obj, s=1, ni=1, f=1)
                if mesh:
                    mesh = mesh[0]
                    shaderSG = mc.listConnections(mesh, d=1, type='shadingEngine')
                    if shaderSG:
                        SGNodes = SGNodes + shaderSG
            if SGNodes:
                SGNodes = list(set(SGNodes))
            
            if SGNodes:
                for shadeSG in SGNodes:
                    shader=mc.listConnections((shadeSG+".surfaceShader"),s=1,d=0)
                    if shader:
                        shader = shader[0]
                        if mc.nodeType(shader)=='lambert':
                            transAttr = '.transparency'
                        if mc.nodeType(shader)=='surfaceShader':
                            transAttr = '.outTransparency' 
            
            transparencyShader = mc.listConnections((shader+transAttr),s =1 ,plugs = 1)   
            
            
            
            # 创建RenderLayer
            if mc.ls(layerName):
                mc.delete(layerName)
            mc.createRenderLayer((rlObjs), name=layerName, noRecurse=1, makeCurrent=1) 
            
            # 通用LGT材质
            shaderNode = 'SHD_' + layerType + '_RB_Shader'
            if mc.ls(shaderNode):
                mc.delete(shaderNode)
                
            shaderNode_red = 'SHD_' + layerType + '_R_Shader'
            if mc.ls(shaderNode_red):
                mc.delete(shaderNode_red)
                
            shaderNode_blue = 'SHD_' + layerType + '_B_Shader'
            if mc.ls(shaderNode_blue):
                mc.delete(shaderNode_blue)                

            shaderNode_Con = 'SHD_' + layerType + '_C_Shader'
            if mc.ls(shaderNode_Con):
                mc.delete(shaderNode_Con)
                
            shaderNode_sample = 'SHD_' + layerType + '_S_Shader'
            if mc.ls(shaderNode_sample):
                mc.delete(shaderNode_sample)  

            shadertransparency=''
            
            shaderNode_blue = mc.shadingNode('surfaceShader', asShader=True, name=shaderNode_blue)
            mc.setAttr((shaderNode_blue + '.outColor'), 0, 0, 1, type='double3')
            
            shaderNode_red = mc.shadingNode('surfaceShader', asShader=True, name=shaderNode_red)
            mc.setAttr((shaderNode_red + '.outColor'), 1, 0, 0, type='double3')
            
            shaderNode_Con = mc.shadingNode('condition', asShader=True, name=shaderNode_Con)
            shaderNode_sample = mc.shadingNode('samplerInfo', asShader=True, name=shaderNode_sample)
            
            shaderNode = mc.shadingNode('lambert', asShader=True, name=shaderNode)
            mc.setAttr((shaderNode + '.ambientColor'), 1, 1, 1, type='double3')
            mc.setAttr((shaderNode + '.diffuse'), 0)
            mc.setAttr((shaderNode + '.translucenceDepth'), 0)
            mc.setAttr((shaderNode + '.translucenceFocus'), 0)
            
            
            mc.connectAttr((shaderNode_Con + '.outColor'), (shaderNode + '.color'))
            mc.connectAttr((shaderNode_red + '.outColor'), (shaderNode_Con + '.colorIfTrue'))
            mc.connectAttr((shaderNode_blue + '.outColor'), (shaderNode_Con + '.colorIfFalse'))
            mc.connectAttr((shaderNode_sample + '.flippedNormal'), (shaderNode_Con + '.firstTerm'))               
            
            if transparencyShader:
                transparencyShader=transparencyShader[0]
                shadertransparency=transparencyShader.split('.')[0]
                mc.connectAttr((shadertransparency + '.outTransparency'), (shaderNode + '.transparency')) 
            # 优先全局着色

            if needSG:
                for SGNode in needSG:
                    shaderInfo = mc.listConnections((SGNode + '.surfaceShader'),s = 1,plugs = 1)
                    if not shaderInfo:
                        continue
                    shaderInfo = shaderInfo[0]
                    mc.editRenderLayerAdjustment(SGNode + '.surfaceShader')
                    mc.disconnectAttr(shaderInfo, (SGNode + '.surfaceShader'))
                    mc.connectAttr((shaderNode + '.outColor'), (SGNode + '.surfaceShader'), f=1) 



            # 渲染设置
            mc.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')

            # 格式命名
            mc.setAttr('defaultRenderGlobals.animation', 1)
            mc.setAttr('defaultRenderGlobals.putFrameBeforeExt', 1)
            mc.setAttr('defaultRenderGlobals.periodInExt', 1)
            mc.setAttr('defaultRenderGlobals.extensionPadding', 4)
            if mc.getAttr('defaultRenderGlobals.outFormatControl') == 1:
                mc.setAttr('defaultRenderGlobals.outFormatControl', 0)

            # exr
            mc.editRenderLayerAdjustment('defaultRenderGlobals.imageFormat')
            mc.setAttr('defaultRenderGlobals.imageFormat', 51)
            mc.setAttr('defaultRenderGlobals.imfkey', 'exr', type='string')
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.setAttr('mentalrayGlobals.compressionQuality', 0)

            # 16位zip压缩
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.editRenderLayerAdjustment('miDefaultFramebuffer.datatype')
            mc.setAttr('miDefaultFramebuffer.datatype', 16)

            print (u'===============!!!Done  【%s】!!!===============' % (u'%s_层' % layerType))
            print '\n'
        else:
            print (u'===============!!!Error  【%s】无物体!!!===============' % (u'%s_层' % layerType))
            print '\n'            




    # BG_MASK03层
    # No Lights
    def zmMskCCreate(self, layerType, selectObjType=0):
        print (u'===============!!!Start 【%s】!!!===============' % (u'%s_MSK03层' % 'ALL'))
        print 'Working...'

        if layerType == 'BG':
            layerName = 'BG_MASK03'

        # 选取模式
        if selectObjType == 1:
            rlObjs = self.zmRLSelectMode()
        # 物体
        objs = self.zmRLObjectsTList()
        refCHR = objs[0]
        refPROP = objs[1]
        refSET = objs[2]
        refSKY = objs[3]
        refSEA = objs[4]
        
        NightGreen=[]
        NightRed=[]
        NightBlue=[]
        sepporp=[]
        sepNightGreen=[]
        if refSET:
            for obj in refSET:
                if 'nightGREEN' in obj:
                    NightGreen.append(obj)                   
                if 'nightRED' in obj:
                    NightRed.append(obj)                    
                if 'nightBLUE' in obj:
                    NightBlue.append(obj)
                    
        if mc.ls('*:*Pro_p007001TaxiJack'):
            sepporp=mc.ls('*:*Pro_p007001TaxiJack')
            refGrps = mc.listRelatives(sepporp, c=1, f=1, type='transform')
            if refGrps:
                meshes = mc.listRelatives(refGrps, ad=1, ni=1, type='mesh', f=1)
                if meshes:
                    meshGrps = mc.listRelatives(meshes, p=1, type='transform', f=1)
            for obj in meshGrps:
                if 'nightGREEN' in obj:
                    sepNightGreen.append(obj)                        
            objsAll=refSET+sepporp
            NightGreen=NightGreen+sepNightGreen
        else:
            objsAll=refSET 
                  
        if objsAll:

            # 特殊处理，半透明用
            # 获取信息必须在masterLayer进行
            transpancyObjs = self.zmRLTransparencyObjs()
            transpancySGNodes = transpancyObjs[0]
            transpancyMeshes = transpancyObjs[1]
            transpancyNode = transpancyObjs[2]

            # 创建RenderLayer
            if mc.ls(layerName):
                mc.delete(layerName)

            mc.createRenderLayer(objsAll, name=layerName, noRecurse=1, makeCurrent=1)
            # mc.editRenderLayerGlobals(currentRenderLayer=layerName)


            if refSKY:
                for obj in refSKY:
                    mesh = mc.listRelatives(obj, ni=1, type='mesh', s=1, f=1)[0]
                    mc.editRenderLayerAdjustment(mesh + '.primaryVisibility')
                    mc.setAttr((mesh + '.primaryVisibility'), 0)

            # 通用RGB材质

            shaderMNode = 'SHD_' + layerType + '_M_Shader'
            if mc.ls(shaderMNode):
                mc.delete(shaderMNode)


            shaderMSG = 'SHD_' + layerType + '_M_SG'
            if mc.ls(shaderMSG):
                mc.delete(shaderMSG)


            shaderMNode = mc.shadingNode('lambert', asShader=True, name=shaderMNode)
            mc.setAttr((shaderMNode + '.color'), 0, 0, 0, type='double3')
            mc.setAttr((shaderMNode + '.matteOpacityMode'), 0)

            shaderMSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=shaderMSG)

            mc.connectAttr((shaderMNode + '.color'), (shaderMSG + '.surfaceShader'))

            # 优先全局着色，赋予Mask

            for obj in objsAll:
                try:
                    mc.sets(obj, e=1, forceElement=shaderMSG)
                except:
                    # 获取物体面数
                    faceNum = mc.polyEvaluate(obj, face=1)
                    mc.sets((obj + u'.f[:' + str(faceNum - 1) + u']'), e=1, forceElement=shaderMSG)
                if obj in refSEA:
                    for sea in refSEA:
                        mc.select(sea)
                        mc.sets(e=1, forceElement=SGNode)
            

            if transpancySGNodes:
                for i in range(len(transpancySGNodes)):
                    if mc.ls(transpancySGNodes[i]):
                        if '_' not in transpancySGNodes[i]:
                            print u'>>>>>>[注意][%s]名字需要最少有1个_分隔符' % transpancySGNodes[i]
                        else:
                            keySGInfo = transpancySGNodes[i].split('_')[-2]
                        keySGInfo = str(i)
                        meshes = transpancyMeshes[i]
                        # 不对！！！！！
                        # 有着色物体时才进行，处理对有相同透明材质的物体使用不同的RGBM
                        if meshes:
                            meshesM = []
                            needColor = [0, 0, 0]
                            needRGBInfo = 'M'
                            for mesh in meshes:
                                if not mc.objExists(mesh):
                                    continue
                                meshGrp = ''
                                if '.f[' in mesh:
                                    meshGrp = mc.ls(mesh.split('.f[')[0],l=1)[0]
                                else:
                                    meshGrp = mc.listRelatives(mesh, p=1, f=1,type = 'transform')[0]
                                RGBInfo = ''
                                # 海不要透明通道
                                if '_sea_' not in mesh:
                                    meshesM.append(mesh)
                                           
                                needMeshes = meshesM
                                
                                RGBInfo = needRGBInfo
                                color = needColor

                                if not needMeshes:
                                    continue

                                shaderTrsNode = 'SHD_' + layerType + '_' + keySGInfo + '_' + RGBInfo + '_Shader'
                                if mc.ls(shaderTrsNode):
                                    # mc.delete( shaderTrsNode )
                                    pass
                                else:
                                    shaderTrsNode = mc.shadingNode('lambert', asShader=True, name=shaderTrsNode)

                                shaderTrsSG = 'SHD_' + layerType + '_' + keySGInfo + '_' + RGBInfo + '_SG'
                                if mc.ls(shaderTrsSG):
                                    # mc.delete( shaderTrsSG )
                                    pass
                                else:
                                    shaderTrsSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=shaderTrsSG)

                                # shaderNode = mc.shadingNode ('surfaceShader', asShader=True, name= shaderNode)


                                if RGBInfo == 'M':
                                    mc.setAttr((shaderTrsNode + '.color'), 0, 0, 0, type='double3')
                                    mc.setAttr((shaderTrsNode + '.matteOpacityMode'), 0)

                                # shaderSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name= shaderSG)

                                try:
                                    mc.connectAttr((shaderTrsNode + '.outColor'), (shaderTrsSG + '.surfaceShader'))
                                except:
                                    pass

                                # 透明连接
                                self.zmRLTransShaderConnectiion(transpancyNode[i], shaderTrsNode, 'transparency')

                                # 翻转
                                if '.outTransparency' in transpancyNode[i]:
                                    mc.editRenderLayerAdjustment(transpancyNode[i].split('.')[0] + '.invert')
                                    mc.setAttr((transpancyNode[i].split('.')[0] + ".invert"), 1)

                                if needMeshes:
                                    for mesh in needMeshes:
                                        if mc.ls(mesh):
                                            try:
                                                mc.sets(mesh, e=1, forceElement=shaderTrsSG)
                                            except:
                                                # 获取物体面数
                                                try:
                                                    obj = mc.listRelatives(mesh, p=1, f=1)[0]
                                                    faceNum = mc.polyEvaluate(obj, face=1)
                                                    mc.sets((obj + u'.f[:' + str(faceNum - 1) + u']'), e=1, forceElement=shaderTrsSG)
                                                except:     
                                                    pass

            if mc.ls('*:*s001001GalionBeachInt'):
                mc.select('*:*s001001GalionBeachInt')
                mel.eval('source "//file-cluster/GDC/Resource/Support/Maya/projects/Lionelville/HbRgbaMaterialTool.mel";HbMaterialB;')
                 
                objgroup=['*:*MSH_c_hi_lampe1_.f[52:69]','*:*MSH_c_hi_lampe1_.f[81]','*:*MSH_c_hi_lampe1_.f[203]', '*:*MSH_c_hi_lampe1_.f[210:213]', '*:*MSH_c_hi_lampe1_.f[330:335]','*:*MSH_c_hi_lampe1_.f[632:637]','*:*MSH_c_hi_lampe1_.f[989:1006]','*:*MSH_c_hi_lampe1_.f[1017:1018]', '*:*MSH_c_hi_lampe1_.f[1140]', '*:*MSH_c_hi_lampe1_.f[1147:1148]', '*:*MSH_c_hi_lampe1_.f[1152]' ,'*:*MSH_c_hi_lampe1_.f[1267:1272]','*:*MSH_c_hi_lampe1_.f[1437]', '*:*MSH_c_hi_lampe1_.f[1452]', '*:*MSH_c_hi_lampe1_.f[1569:1574]', '*:*MSH_c_hi_MSH_c_hi_Candle4394_Shape','*:*MSH_c_hi_MSH_c_hi_Candle4395_Shape', '*:*MSH_c_hi_Light_Boat_01_.f[532:547]']
                sepgroup=mc.ls(objgroup)
                for obj in sepgroup:
                    if obj:
                        mc.select(obj)
                        mel.eval('source "//file-cluster/GDC/Resource/Support/Maya/projects/Lionelville/HbRgbaMaterialTool.mel";HbMaterialG;')
                         
            if NightGreen:
                for obj in NightGreen:
                    mc.select(obj)
                    mel.eval('source "//file-cluster/GDC/Resource/Support/Maya/projects/Lionelville/HbRgbaMaterialTool.mel";HbMaterialG;')
        
            if NightRed:
                for obj in NightRed:
                    mc.select(obj)
                    mel.eval('source "//file-cluster/GDC/Resource/Support/Maya/projects/Lionelville/HbRgbaMaterialTool.mel";HbMaterialR;')
            
            if NightBlue:
                for obj in NightBlue:
                    mc.select(obj)
                    mel.eval('source "//file-cluster/GDC/Resource/Support/Maya/projects/Lionelville/HbRgbaMaterialTool.mel";HbMaterialB;')       

            GreenGRP=mc.ls("zm_s040001CaveQueen_h:MSH_c_hi_Ball_ca_","zm_p839001PearlCaveQueen_h:Pro")
            RedGRP=mc.ls("zm_s040001CaveQueen_h:MSH_Crystal_A1131_","zm_s040001CaveQueen_h:MSH_Crystal_A1132_","zm_s040001CaveQueen_h:MSH_Crystal_B1060_","zm_s040001CaveQueen_h:MSH_Crystal_B1106_","zm_s040001CaveQueen_h:MSH_Crystal_B1057_","zm_s040001CaveQueen_h:MSH_Crystal_B1117_","zm_s040001CaveQueen_h:MSH_Crystal_B1074_","zm_s040001CaveQueen_h:MSH_Crystal_B1090_","zm_s040001CaveQueen_h:MSH_Crystal_B1084_","zm_s040001CaveQueen_h:MSH_Crystal_B1101_","zm_s040001CaveQueen_h:MSH_Crystal_B1080_")
            BlueGRP=mc.ls("zm_s040001CaveQueen_h:c_MoatuStatue_main","zm_s040001CaveQueen_h:MSH_c_hi_Pedestal_ca_")
            
            if GreenGRP:
                mc.select(GreenGRP)
                mel.eval('source "//file-cluster/GDC/Resource/Support/Maya/projects/Lionelville/HbRgbaMaterialTool.mel";HbMaterialG;')
                    
            if RedGRP:
                mc.select(RedGRP)
                mel.eval('source "//file-cluster/GDC/Resource/Support/Maya/projects/Lionelville/HbRgbaMaterialTool.mel";HbMaterialR;')
                    
            if BlueGRP:
                for obj in BlueGRP:        
                    mc.select(obj)
                    mel.eval('source "//file-cluster/GDC/Resource/Support/Maya/projects/Lionelville/HbRgbaMaterialTool.mel";HbMaterialB;') 
                                                                           
            # 设置
            # self.zmRLCommonConfig()
            # 渲染设置
            mc.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')

            # 关闭光线追踪
            mc.editRenderLayerAdjustment('miDefaultOptions.rayTracing')
            mc.setAttr('miDefaultOptions.rayTracing', 0)

            # 格式命名
            mc.setAttr('defaultRenderGlobals.animation', 1)
            mc.setAttr('defaultRenderGlobals.putFrameBeforeExt', 1)
            mc.setAttr('defaultRenderGlobals.periodInExt', 1)
            mc.setAttr('defaultRenderGlobals.extensionPadding', 4)
            if mc.getAttr('defaultRenderGlobals.outFormatControl') == 1:
                mc.setAttr('defaultRenderGlobals.outFormatControl', 0)

            # exr
            mc.editRenderLayerAdjustment('defaultRenderGlobals.imageFormat')
            mc.setAttr('defaultRenderGlobals.imageFormat', 51)
            mc.setAttr('defaultRenderGlobals.imfkey', 'exr', type='string')
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.setAttr('mentalrayGlobals.compressionQuality', 0)

            # 16位zip压缩
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.editRenderLayerAdjustment('miDefaultFramebuffer.datatype')
            mc.setAttr('miDefaultFramebuffer.datatype', 16)

            print (u'===============!!!Done  【%s】!!!===============' % (u'%s_MSK03层' % 'ALL'))
            print '\n'
        else:
            print (u'===============!!!Error  【%s】无物体!!!===============' % (u'%s_MSK03层' % 'ALL'))
            print '\n'
            
            
    # ALL_Reflect层
    # No Lights
    def zmReflectCreate(self, layerType, selectObjType=0):
        print (u'===============!!!Start 【%s】!!!===============' % (u'%s_Reflect层' % 'ALL'))
        print 'Working...'


        # 选取模式
        if selectObjType == 1:
            rlObjs = self.zmRLSelectMode()
        # 物体
        objs = self.zmRLObjectsTList()
        refCHR = objs[0]
        refPROP = objs[1]
        refSET = objs[2]
        refSKY = objs[3]
        refSEA = objs[4]
        
            
        lights = mc.ls(type='light', l=1)
        lightGrps = []
        
        if lights:
            for light in lights:
                lightGrps.append(mc.listRelatives(light, p=1, type='transform', f=1)[0])
        
        if layerType == 'ALL':
            objsAll = refCHR+refPROP+refSET+refSKY+refSEA
            objshide = refCHR+refPROP+refSET+refSKY
            layerName = 'ALL_Reflect'        
        
      
        if objsAll:
            # 创建RenderLayer
            if mc.ls(layerName):
                mc.delete(layerName)

            mc.createRenderLayer(objsAll, name=layerName, noRecurse=1, makeCurrent=1)

            if objshide:
                for obj in objshide:
                    mesh = mc.listRelatives(obj, ni=1, type='mesh', s=1, f=1)[0]
                    mc.editRenderLayerAdjustment(mesh + '.primaryVisibility')
                    mc.setAttr((mesh + '.primaryVisibility'), 0)
                    
            if refSEA:
                for obj in refSEA:
                    mesh = mc.listRelatives(obj, ni=1, type='mesh', s=1, f=1)[0]
                    mc.editRenderLayerAdjustment(mesh + '.primaryVisibility')
                    mc.setAttr((mesh + '.primaryVisibility'), 1)

            
            # bline材质
            shaderReflctNode = 'SHD_' + layerType + '_reflect_Shader'
            if mc.ls(shaderReflctNode):
                mc.delete(shaderReflctNode)
                
            shaderReflectSG = 'SHD_' + layerType + '_reflect_SG'
            if mc.ls(shaderReflectSG):
                mc.delete(shaderReflectSG)            


            shaderReflctNode = mc.shadingNode('blinn', asShader=True, name=shaderReflctNode)
            mc.setAttr((shaderReflctNode + '.color'), 0, 0, 0, type='double3')
            mc.setAttr((shaderReflctNode + '.reflectivity'), 1)
            mc.setAttr((shaderReflctNode + '.miReflectionBlur'), 0.15)
            mc.setAttr((shaderReflctNode + '.miReflectionRays'), 8)
            
            shaderReflectSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=shaderReflectSG)
            mc.connectAttr((shaderReflctNode + '.color'), (shaderReflectSG + '.surfaceShader'))
            
                                       
            # 优先全局着色，赋予bline
            if refSEA:               
                for sea in refSEA:
                    mc.select(sea)
                    mc.sets(e=1, forceElement=shaderReflectSG)
            
            if lightGrps:
                for light in lightGrps:
                    mc.editRenderLayerAdjustment(light + '.visibility')
                    mc.setAttr((light + '.visibility'), 0)

            # 设置
            # self.zmRLCommonConfig()
            # 渲染设置
            mc.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')

            mc.editRenderLayerAdjustment('miDefaultOptions.rayTracing')
            mc.setAttr('miDefaultOptions.rayTracing', 1)
            
            mc.editRenderLayerAdjustment ("miDefaultOptions.finalGather")
            mc.setAttr('miDefaultOptions.finalGather', 1)

            # 格式命名
            mc.setAttr('defaultRenderGlobals.animation', 1)
            mc.setAttr('defaultRenderGlobals.putFrameBeforeExt', 1)
            mc.setAttr('defaultRenderGlobals.periodInExt', 1)
            mc.setAttr('defaultRenderGlobals.extensionPadding', 4)
            if mc.getAttr('defaultRenderGlobals.outFormatControl') == 1:
                mc.setAttr('defaultRenderGlobals.outFormatControl', 0)

            # exr
            mc.editRenderLayerAdjustment('defaultRenderGlobals.imageFormat')
            mc.setAttr('defaultRenderGlobals.imageFormat', 51)
            mc.setAttr('defaultRenderGlobals.imfkey', 'exr', type='string')
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.setAttr('mentalrayGlobals.compressionQuality', 0)

            # 16位zip压缩
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.editRenderLayerAdjustment('miDefaultFramebuffer.datatype')
            mc.setAttr('miDefaultFramebuffer.datatype', 16)

            print (u'===============!!!Done  【%s】!!!===============' % (u'%s_Reflect层' % 'ALL'))
            print '\n'
        else:
            print (u'===============!!!Error  【%s】无物体!!!===============' % (u'%s_Reflect层' % 'ALL'))
            print '\n'                                        
            
    # Special_depth层
    def zmSpecialdepthtCreate(self,selectObjType=0):
        print (u'===============!!!Start 【%s】!!!===============' % (u'%s_Special_depth层' ))
        print 'Working...'


        # 选取模式
        if selectObjType == 1:
            rlObjs = self.zmRLSelectMode()
        # 物体
        objs = self.zmRLObjectsTList()
        refCHR = objs[0]
        refPROP = objs[1]
        refSET = objs[2]
        refSKY = objs[3]
        refSEA = objs[4]                    
        

        objsAll = refCHR+refPROP
        layerName = 'Special_depth'        
        
      
        if objsAll:

            # 创建RenderLayer
            if mc.ls(layerName):
                mc.delete(layerName)

            mc.createRenderLayer(objsAll, name=layerName, noRecurse=1, makeCurrent=1)
            if mc.ls('zlighting'):
                mc.delete('zlighting')
            
            mel.eval('source"Z:/Resource/Support/Maya/projects/ZoomWhiteDolphin/zwTaowaY.mel";zwTaowaY;') 
            
            Levalgrp=[]
            num=''
            SmoothSet=mc.ls("*:*SMOOTH_SET",type='objectSet')
            if SmoothSet:
                for set in SmoothSet:
                    if set.split('_')[1][0]!='s':
                        smooth_leval=mc.sets(set,q=1)
                        for i in range(len(smooth_leval)):
                            if mc.listRelatives(smooth_leval[i],ad=1,ni=1,type='mesh',f=1):
                                Levalgrp=mc.listRelatives(smooth_leval[i],ad=1,ni=1,type='mesh',f=1)
                                num=smooth_leval[i].split('_')[-1]                                
                if Levalgrp:
                    for obj in objsAll:                                   
                        mc.polySmooth(obj,dv=int(num),bnr=1,c=1,kb=1,ksb=1,khe=0,kt=1,kmb=1,suv=1,peh=0,sl=1,ps=0.1,ro=1,ch=1,mth=0) 
            
            if mc.ls('zlighting'):
                mel.eval('editRenderLayerMembers -noRecurse Special_depth zlighting;')
       
            #渲染器选择        
            mc.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'mayaSoftware', type='string')

            # 标准设置
            mc.setAttr('defaultRenderQuality.edgeAntiAliasing', 1)    
            mc.setAttr('defaultRenderGlobals.animation', 1)
            mc.setAttr('defaultRenderGlobals.outFormatControl', 0)
            mc.setAttr('defaultRenderGlobals.extensionPadding', 4)
            mc.setAttr('defaultRenderGlobals.imageFilePrefix', '<Layer>/<Scene>_<Layer>', type='string')
            mc.setAttr('defaultResolution.width', 1920)
            mc.setAttr('defaultResolution.height', 1080)
            mc.setAttr('defaultResolution.deviceAspectRatio', 1.777)
            mc.setAttr('defaultResolution.pixelAspect', 1.00)
            mc.evalDeferred('mc.setAttr((\'defaultResolution.pixelAspect\'),1)',lowestPriority=1)
            mc.setAttr('defaultResolution.dotsPerInch', 72)
            mc.setAttr('defaultRenderQuality.edgeAntiAliasing', 1) 
            
            from idmt.maya.py_common import sk_infoConfig
            shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
            shot = shotInfos[0] + '_' + shotInfos[1] + '_' + shotInfos[2]
            anim = idmt.pipeline.db.GetAnimByFilename(shot)
            startFrame = anim.frmStart
            endFrame = anim.frmEnd
            fpsFrame = anim.fps
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
                preStartFrame = startFrame - 10
                mc.playbackOptions(animationStartTime=preStartFrame)
                # 结束帧

            #相机设置
            from idmt.maya.py_common import sk_infoConfig
            shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
            camName = 'CAM:cam_' + str(shotInfos[1]) + '_' + str(shotInfos[2]) + '_baked'
            camShape = mc.listRelatives(mc.ls(camName, type='transform')[0], ni=1, s=1)[0]
            if mc.ls(camName, type='transform'):             
                mc.setAttr((camShape + '.renderable'), 1)
                try:
                    mc.setAttr(('perspShape.renderable'), 0)
                except:
                    pass
            else:
                mc.error('===============未找到有效CAM【%s】===============' % camName)

            
            # 输出格式设置
            mc.setAttr('defaultRenderGlobals.imageFormat', 7) 

                    
            # 关闭默认灯光
            mc.setAttr('defaultRenderGlobals.enableDefaultLight',0)

            mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')
            mc.setAttr("defaultRenderLayer.renderable", 0)
            
            print (u'===============!!!Done  【%s】!!!===============' % (u'%s_Special_depth层' ))
            print '\n'
        else:
            print (u'===============!!!Error  【%s】无物体!!!===============' % (u'%s_Special_depth层' ))
            print '\n'  
                          
                          
                          
    # FG_LGTNIGHT层
    # 新版本
    def zmFGLGTNIGHTCreate(self, layerType, selectObjType=0):
        print (u'===============!!!Start 【%s】!!!===============' % (u'%s_LGTNIGHT层' % layerType))
        print 'Working...'

        # 物体
        objs = self.zmRLObjectsTList()
        refCHR = objs[0]
        refPROP = objs[1]
        refSET = objs[2]
        refSKY = objs[3]
        seaInfo = objs[4]
        
        
        LGTSG= self.zmRLSGNodesGet()
        SGCHR=LGTSG[0]
        SGPROP=LGTSG[1]
        SGSET=LGTSG[2]
        
        rlObjs = []
        needSG = []
        if layerType == 'FG':

            rlObjs = refSET + refCHR + refPROP
            needSG = SGCHR + SGPROP + SGSET
            if needSG:
                needSG = list(set(needSG))
            layerName = 'FG_LGTNIGHT'

        # 灯光

        needLightGrps = []
        NIGHTGRP=[]
        
        LightGRP=mc.ls('*:*LIGHTING_EXT')
        if LightGRP:
            mc.setAttr ((LightGRP[0]+'.Mood'), 3)
            NIGHT_ON=mc.listRelatives(LightGRP[0], c=1,f=1)
            for obj in NIGHT_ON:
                if 'NIGHT_ON' in obj:
                    NIGHTGRP.append(obj)
            needLightGrps=NIGHTGRP                                
        else:
            print u'请确保有LIGHTING_EXT的灯光组'


        # 选取模式
        if selectObjType == 1:
            rlObjs = self.zmRLSelectMode()

        if rlObjs:
            # 透明信息
            transpancyObjs = self.zmRLTransparencyObjs()
            transpancySGNodes = transpancyObjs[0]
            transpancyMeshes = transpancyObjs[1]
            transpancyNode = transpancyObjs[2]
            
            rampObjInfos = self.zmRLWDInfoObjs()
            rampInfos = rampObjInfos[0]
            rampNodes = []
            rampSGNodes = []
            rampMeshes = rampObjInfos[1]
            rampPositions = rampObjInfos[2]
            if rampInfos:
                for info in rampInfos:
                    needInfo = info.split('>_<')
                    rampNodes.append(needInfo[0])
                    rampSGNodes.append(needInfo[1])
            

            from idmt.maya.py_common import sk_infoConfig
            reload(sk_infoConfig)
            import os

            # 创建RenderLayer
            if mc.ls(layerName):
                mc.delete(layerName)
            # 要加灯光
            mc.createRenderLayer((rlObjs + needLightGrps), name=layerName, noRecurse=1, makeCurrent=1)


            # openSea是否在场景里
            checkAssetID = ['s019001']
            namespaces = mc.namespaceInfo(listOnlyNamespaces=1)
            checkState = 0
            for ID in checkAssetID:
                for ns in namespaces:
                    if ID in ns:
                        checkState = 1
            # FG
            if layerType == 'FG':
                # BG渲染关闭
                if (refCHR + refPROP):
                    for obj in (refCHR + refPROP):
                        mesh = mc.listRelatives(obj, ni=1, type='mesh', s=1, f=1)[0]
                        mc.editRenderLayerAdjustment(mesh + '.primaryVisibility')
                        mc.setAttr((mesh + '.primaryVisibility'), 0)

                # 不需要Sky
                if refSKY:
                    for obj in refSKY:
                        mc.editRenderLayerAdjustment(obj + '.visibility')
                        mc.setAttr((obj + '.visibility'), 0)

                if seaInfo:
                    for obj in seaInfo:
                        mc.editRenderLayerAdjustment(obj + '.visibility')
                        mc.setAttr((obj + '.visibility'), 0)

                # openSea在则隐藏
                if checkState:
                    lightingGrps = mc.ls('*:*LIGHTING', type='transform') + mc.ls('*:*:*LIGHTING', type='transform')
                    for ID in checkAssetID:
                        for grp in lightingGrps:
                            if ID not in grp:
                                mc.editRenderLayerAdjustment(grp + '.visibility')
                                mc.setAttr((grp + '.visibility'), 0)
                                
                cyclosGrp = mc.ls('*:*:*MSH_c_hi_Cyclos',type = 'transform',l=1)
                if cyclosGrp:
                    meshes = mc.listRelatives(cyclosGrp,ad = 1,type = 'mesh',f = 1)
                    polyGrps = mc.listRelatives(meshes,p = 1,type = 'transform',f = 1)
                    polyGrps = list(set(polyGrps))
                    for grp in polyGrps:
                        mc.editRenderLayerAdjustment(grp + '.visibility')
                        mc.setAttr((grp + '.visibility'), 0)                         


                            

            # 通用LGT材质
            shaderNode = 'SHD_' + layerType + '_LGT_Shader'
            if mc.ls(shaderNode):
                mc.delete(shaderNode)
                
            shaderNode_ramp = 'SHD_' + layerType + '_L_Shader'
            if mc.ls(shaderNode_ramp):
                mc.delete(shaderNode_ramp)


            shaderNode_ramp = mc.shadingNode('rampShader', asShader=True, name=shaderNode_ramp)
            mc.setAttr((shaderNode_ramp + '.colorInput'), 2)
            mc.setAttr((shaderNode_ramp + '.color[0].color_Color'), 0, 0, 0, type='double3')
            mc.setAttr((shaderNode_ramp + '.color[0].color_Position'), 0)
            mc.setAttr((shaderNode_ramp + '.color[0].color_Interp'), 0)
            mc.setAttr((shaderNode_ramp + '.color[1].color_Color'), 1, 1, 1, type='double3')
            mc.setAttr((shaderNode_ramp + '.color[1].color_Position'), 0.096)
            mc.setAttr((shaderNode_ramp + '.color[1].color_Interp'), 0)
            mc.setAttr((shaderNode_ramp + '.diffuse'), 1)
            mc.setAttr((shaderNode_ramp + '.translucenceDepth'), 1000)
            mc.setAttr((shaderNode_ramp + '.specularity'), 0)
            mc.setAttr((shaderNode_ramp + '.reflectivity[0].reflectivity_Position'), 0)
            mc.setAttr((shaderNode_ramp + '.reflectivity[0].reflectivity_FloatValue'), 0)

            shaderNode = mc.shadingNode('surfaceShader', asShader=True, name=shaderNode)
            mc.connectAttr((shaderNode_ramp + '.outColor'), (shaderNode + '.outColor'))
            

            # 优先全局着色

            if needSG:
                for SGNode in needSG:
                    shaderInfo = mc.listConnections((SGNode + '.surfaceShader'),s = 1,plugs = 1)
                    if not shaderInfo:
                        continue
                    shaderInfo = shaderInfo[0]
                    mc.editRenderLayerAdjustment(SGNode + '.surfaceShader')
                    mc.disconnectAttr(shaderInfo, (SGNode + '.surfaceShader'))
                    mc.connectAttr((shaderNode + '.outColor'), (SGNode + '.surfaceShader'), f=1) 



            # 特殊物体着色
            # LGT新版：每套材质球都存在，transpancySGNodes
            indexTransDone = []
            if rampNodes:
                pass

            rampNodes = []
            rampSGNodes = []
            rampMeshes = rampObjInfos[1]
            rampPositions = rampObjInfos[2]

            if transpancySGNodes:
                for i in range(len(transpancySGNodes)):
                    if mc.ls(transpancySGNodes[i]):
                        if '_' not in transpancySGNodes[i]:
                            print u'>>>>>>[注意][%s]名字需要最少有1个_分隔符' % transpancySGNodes[i]
                        else:
                            keySGInfo = transpancySGNodes[i].split('_')[-2]
                        keySGInfo = str(i)
                        meshes = transpancyMeshes[i]
                        # 有着色物体时才进行
                        if meshes:
                            shaderTrsNode = 'SHD_' + layerType + '_' + keySGInfo + '_LGT_Shader'
                            if mc.ls(shaderTrsNode):
                                mc.delete(shaderTrsNode)


                            # 创建
                            shaderTrsNode = mc.shadingNode('lambert', asShader=True, name=shaderTrsNode)
                            mc.setAttr((shaderTrsNode + '.color'), 1, 1, 1, type='double3')
                            mc.setAttr((shaderTrsNode + '.ambientColor'), 0, 0, 0, type='double3')


                            # 透明连接
                            #self.zmRLTransShaderConnectiion(transpancyNode[i], shaderTrsNode, 'transparency[0].transparency_Color')
                            self.zmRLTransShaderConnectiion(transpancyNode[i], shaderTrsNode, 'transparency')

                            # file贴图反转
                            if '.outTransparency' in transpancyNode[i]:
                                mc.editRenderLayerAdjustment(transpancyNode[i].split('.')[0] + '.invert')
                                mc.setAttr((transpancyNode[i].split('.')[0] + ".invert"), 1)

                            # 着色
 
                            shaderInfo = mc.listConnections((transpancySGNodes[i] + '.surfaceShader'),s = 1,plugs = 1)
                            if shaderInfo:
                                shaderInfo = shaderInfo[0]
                                mc.editRenderLayerAdjustment(transpancySGNodes[i] + '.surfaceShader')
                                mc.disconnectAttr(shaderInfo, (transpancySGNodes[i] + '.surfaceShader'))
                                mc.connectAttr((shaderTrsNode + '.outColor'), (transpancySGNodes[i] + '.surfaceShader'), f=1)

            if layerName=='FG_LGTNIGHT':
                needobj=[]
                needobj01=[]
                needobj02=[]
                if refSET:
                    for obj in refSET:
                        if 'MSH_c_hi_ShellRight_'in obj:
                            needobj01.append(obj)
                        if 'MSH_c_hi_ShellLeft_' in obj:
                            needobj02.append(obj)
                needobj=needobj01+needobj02
        
                if needobj:
                    # 转到FG_LGT层处理
                    # mc.editRenderLayerGlobals(currentRenderLayer='FG_LGT')
    
                    # s001001GalionBeach赋予另外的材质
                    shaderNode = 'SHD_GalionBeach_Shader'
                    if mc.ls(shaderNode):
                        mc.delete(shaderNode)
    
                    shaderNode_ramp = 'SHD_GalionBeach_L_Shader'
                    if mc.ls(shaderNode_ramp):
                        mc.delete(shaderNode_ramp)
    
                    shaderSG = 'SHD_GalionBeach_SG'
                    if mc.ls(shaderSG):
                        mc.delete(shaderSG)
                    else:
                        shaderSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=shaderSG)
    
                    shaderNode_ramp = mc.shadingNode('rampShader', asShader=True, name=shaderNode_ramp)
                    mc.setAttr((shaderNode_ramp + '.colorInput'), 2)
                    mc.setAttr((shaderNode_ramp + '.color[0].color_Color'), 0, 0, 0, type='double3')
                    mc.setAttr((shaderNode_ramp + '.color[0].color_Position'), 0)
                    mc.setAttr((shaderNode_ramp + '.color[0].color_Interp'), 0)
                    mc.setAttr((shaderNode_ramp + '.color[1].color_Color'), 1, 1, 1, type='double3')
                    mc.setAttr((shaderNode_ramp + '.color[1].color_Position'), 0.096)
                    mc.setAttr((shaderNode_ramp + '.color[1].color_Interp'), 0)
                    mc.setAttr((shaderNode_ramp + '.diffuse'), 1)
                    mc.setAttr((shaderNode_ramp + '.translucenceDepth'), 1000)
                    mc.setAttr((shaderNode_ramp + '.specularity'), 0)
                    mc.setAttr((shaderNode_ramp + '.reflectivity[0].reflectivity_Position'), 0)
                    mc.setAttr((shaderNode_ramp + '.reflectivity[0].reflectivity_FloatValue'), 0)
    
                    shaderNode = mc.shadingNode('surfaceShader', asShader=True, name=shaderNode)
                    mc.connectAttr((shaderNode_ramp + '.outColor'), (shaderNode + '.outColor'))
    
                    try:
                        mc.connectAttr((shaderNode + '.outColor'), (shaderSG + '.surfaceShader'))
                    except:
                        pass
    
                    # s001001GalionBeach着色
                    if needobj:
                        for obj in needobj:
                            mc.sets(obj, e=1, forceElement=shaderSG)
    
                    # 创建passContributionMap
                    Map = mc.createNode('passContributionMap', n='passMap')
                    mc.connectAttr((layerName + '.passContributionMap'), (Map + '.owner'), na=1)
                    if needobj:
                        for obj in needobj:
                            mc.connectAttr((obj + '.message'), (Map + '.dagObjects'), na=1)
                    # 创建renderPass节点
                    cusColor = mc.shadingNode('renderPass', asRendering=1, name='customColor')
    
                    cmd = 'applyAttrPreset \"' + cusColor + '\" \"D:/Alias/Maya2012x64/presets/attrPresets/renderPass/customColor.mel\" 1;'
                    mel.eval(cmd)
                    #mel.eval('applyAttrPreset "customColor" "D:/Alias/Maya2012x64/presets/attrPresets/renderPass/customColor.mel" 1;')
    
                    shaRaw = mc.shadingNode('renderPass', asRendering=1, name='shadowRaw')
                    cmr = 'applyAttrPreset \"' + shaRaw + '\" \"D:/Alias/Maya2012x64/presets/attrPresets/renderPass/rawShadow.mel\" 1;'
                    mel.eval(cmr)

    
                    # 使renderPass节点与层和passContributionMap相连
                    mc.connectAttr((layerName + '.renderPass'), (cusColor + '.owner'), nextAvailable=1)
                    mc.connectAttr((layerName + '.renderPass'), (shaRaw + '.owner'), nextAvailable=1)
    
                    mc.connectAttr((cusColor + '.message'), (Map + '.renderPass'), nextAvailable=1)
                    mc.connectAttr((shaRaw + '.message'), (Map + '.renderPass'), nextAvailable=1)
    
                    # 创建writeToColorBuffer节点
                    ColorBuffer = mc.shadingNode('writeToColorBuffer', asShader=1, name='colorBuffer')
                    mc.setAttr((ColorBuffer + '.color'), 1, 0, 0, type='double3')
                    mc.connectAttr((cusColor + '.message'), (ColorBuffer + '.renderPass'))
    
                    mc.connectAttr((shaderNode + '.outColor'), (ColorBuffer + '.evaluationPassThrough'))


            # 渲染设置
            mc.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')

            # 格式命名
            mc.setAttr('defaultRenderGlobals.animation', 1)
            mc.setAttr('defaultRenderGlobals.putFrameBeforeExt', 1)
            mc.setAttr('defaultRenderGlobals.periodInExt', 1)
            mc.setAttr('defaultRenderGlobals.extensionPadding', 4)
            if mc.getAttr('defaultRenderGlobals.outFormatControl') == 1:
                mc.setAttr('defaultRenderGlobals.outFormatControl', 0)

            # exr
            mc.editRenderLayerAdjustment('defaultRenderGlobals.imageFormat')
            mc.setAttr('defaultRenderGlobals.imageFormat', 51)
            mc.setAttr('defaultRenderGlobals.imfkey', 'exr', type='string')
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.setAttr('mentalrayGlobals.compressionQuality', 0)

            # 16位zip压缩
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.editRenderLayerAdjustment('miDefaultFramebuffer.datatype')
            mc.setAttr('miDefaultFramebuffer.datatype', 16)

            print (u'===============!!!Done  【%s】!!!===============' % (u'%s_LGTNIGHT层' % layerType))
            print '\n'
        else:
            print (u'===============!!!Error  【%s】无物体!!!===============' % (u'%s_LGTNIGHT层' % layerType))
            print '\n'




    #waves层
    def zmRLwavesCreate(self, layerType, selectObjType=0):
        print (u'===============!!!Start 【%s】!!!===============' % (u'%s_waves层' % layerType))
        print 'Working...'

        # 物体
        objs = self.zmRLObjectsTList()
        refCHR = objs[0]
        refPROP = objs[1]
        refSET = objs[2]
        refSKY = objs[3]
        seaInfo = objs[4]
        
        #SG节点
        LGTSG= self.zmRLSGNodesGet()
        SGCHR=LGTSG[0]
        SGPROP=LGTSG[1]
        SGSET=LGTSG[2]        
     
        wavesGRP=[]
        if layerType == 'FG':
            if mc.ls('*:*MSH_c_hi_shell_ca_'):
                wavesGRP=mc.ls('*:*MSH_c_hi_shell_ca_')
                
        layerName01 = 'WAVESCO'
        layerName02 = 'WAVESMSK'
        layerName03 = 'WAVESNOISE'
        layerName04 = 'WAVESHDW'

        # 灯光
        needLightGrps = []        
        if mc.ls('*:*MSH_LGT_DAY_KEY_01'):
            LightGrps=mc.ls('*:*MSH_LGT_DAY_KEY_01')
            needLightGrps=LightGrps
                   
        # 选取模式
        if selectObjType == 1:
            rlObjs = self.zmRLSelectMode()

        
        if layerName01 =='WAVESCO':
            layerName=layerName01
            rlObjs=wavesGRP           
            # 创建RenderLayer
            if mc.ls(layerName):
                mc.delete(layerName)
            # 要加灯光
            mc.createRenderLayer(rlObjs, name=layerName, noRecurse=1, makeCurrent=1)

            if mc.ls('*:*MSH_temp_CO_', type='transform'):
                objs = mc.ls('*:*MSH_temp_CO_', type='transform')
                objMESH = mc.listRelatives(objs[0], ad=1, type='mesh', f=1)
                objSGs = mc.listConnections(objMESH[0], type='shadingEngine', d=1)
                if objSGs:
                    objSG = objSGs[0]
                else:
                    mc.confirmDialog(title=u'警告', message=u'请确定有海浪这个道具，并且道具中存在“MSH_temp_CO_”字符段，', button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')

            if objSG:
                for obj in rlObjs:
                    mc.select(obj)
                    mc.sets(e=1, forceElement=objSG)

            # 渲染设置
            mc.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')
            
            mel.eval('setAttr "defaultRenderGlobals.enableDefaultLight" 0;')
            
            # 格式命名
            mc.setAttr('defaultRenderGlobals.animation', 1)
            mc.setAttr('defaultRenderGlobals.putFrameBeforeExt', 1)
            mc.setAttr('defaultRenderGlobals.periodInExt', 1)
            mc.setAttr('defaultRenderGlobals.extensionPadding', 4)
            if mc.getAttr('defaultRenderGlobals.outFormatControl') == 1:
                mc.setAttr('defaultRenderGlobals.outFormatControl', 0)
    
            # exr
            mc.editRenderLayerAdjustment('defaultRenderGlobals.imageFormat')
            mc.setAttr('defaultRenderGlobals.imageFormat', 51)
            mc.setAttr('defaultRenderGlobals.imfkey', 'exr', type='string')
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.setAttr('mentalrayGlobals.compressionQuality', 0)
    
            # 16位zip压缩
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.editRenderLayerAdjustment('miDefaultFramebuffer.datatype')
            mc.setAttr('miDefaultFramebuffer.datatype', 16)
    
            print (u'===============!!!Done  【%s】!!!===============' % (u'%s_WAVESCO层' % layerType))
            print '\n'                    
                    
        if layerName02 == 'WAVESMSK':
            layerName=layerName02
            rlObjs=wavesGRP           
            # 创建RenderLayer
            if mc.ls(layerName):
                mc.delete(layerName)
            # 要加灯光
            mc.createRenderLayer(rlObjs, name=layerName, noRecurse=1, makeCurrent=1)

            if mc.ls('*:*MSH_temp_MSK_', type='transform'):
                objs = mc.ls('*:*MSH_temp_MSK_', type='transform')
                objMESH = mc.listRelatives(objs[0], ad=1, type='mesh', f=1)
                objSGs = mc.listConnections(objMESH[0], type='shadingEngine', d=1)
                if objSGs:
                    objSG = objSGs[0]
                else:
                    mc.confirmDialog(title=u'警告', message=u'请确定有海浪这个道具，并且道具中存在“MSH_temp_MSK_”字符段，', button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')

            if objSG:
                for obj in rlObjs:
                    mc.select(obj)
                    mc.sets(e=1, forceElement=objSG)                    

            # 渲染设置
            mc.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')
            
            mel.eval('setAttr "defaultRenderGlobals.enableDefaultLight" 0;')
            
            # 格式命名
            mc.setAttr('defaultRenderGlobals.animation', 1)
            mc.setAttr('defaultRenderGlobals.putFrameBeforeExt', 1)
            mc.setAttr('defaultRenderGlobals.periodInExt', 1)
            mc.setAttr('defaultRenderGlobals.extensionPadding', 4)
            if mc.getAttr('defaultRenderGlobals.outFormatControl') == 1:
                mc.setAttr('defaultRenderGlobals.outFormatControl', 0)
    
            # exr
            mc.editRenderLayerAdjustment('defaultRenderGlobals.imageFormat')
            mc.setAttr('defaultRenderGlobals.imageFormat', 51)
            mc.setAttr('defaultRenderGlobals.imfkey', 'exr', type='string')
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.setAttr('mentalrayGlobals.compressionQuality', 0)
    
            # 16位zip压缩
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.editRenderLayerAdjustment('miDefaultFramebuffer.datatype')
            mc.setAttr('miDefaultFramebuffer.datatype', 16)
    
            print (u'===============!!!Done  【%s】!!!===============' % (u'%s_WAVESMSK层' % layerType))
            print '\n'
            
        if layerName03 == 'WAVESNOISE':
            layerName=layerName03
            rlObjs=wavesGRP           
            # 创建RenderLayer
            if mc.ls(layerName):
                mc.delete(layerName)
            # 要加灯光
            mc.createRenderLayer(rlObjs, name=layerName, noRecurse=1, makeCurrent=1)

            if mc.ls('*:*MSH_temp_NOISE_', type='transform'):
                objs = mc.ls('*:*MSH_temp_NOISE_', type='transform')
                objMESH = mc.listRelatives(objs[0], ad=1, type='mesh', f=1)
                objSGs = mc.listConnections(objMESH[0], type='shadingEngine', d=1)
                if objSGs:
                    objSG = objSGs[0]
                else:
                    mc.confirmDialog(title=u'警告', message=u'请确定有海浪这个道具，并且道具中存在“MSH_temp_NOISE_”字符段，', button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')

            if objSG:
                for obj in rlObjs:
                    mc.select(obj)
                    mc.sets(e=1, forceElement=objSG) 

            # 渲染设置
            mc.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')
            
            mel.eval('setAttr "defaultRenderGlobals.enableDefaultLight" 0;')
            
            # 格式命名
            mc.setAttr('defaultRenderGlobals.animation', 1)
            mc.setAttr('defaultRenderGlobals.putFrameBeforeExt', 1)
            mc.setAttr('defaultRenderGlobals.periodInExt', 1)
            mc.setAttr('defaultRenderGlobals.extensionPadding', 4)
            if mc.getAttr('defaultRenderGlobals.outFormatControl') == 1:
                mc.setAttr('defaultRenderGlobals.outFormatControl', 0)
    
            # exr
            mc.editRenderLayerAdjustment('defaultRenderGlobals.imageFormat')
            mc.setAttr('defaultRenderGlobals.imageFormat', 51)
            mc.setAttr('defaultRenderGlobals.imfkey', 'exr', type='string')
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.setAttr('mentalrayGlobals.compressionQuality', 0)
    
            # 16位zip压缩
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.editRenderLayerAdjustment('miDefaultFramebuffer.datatype')
            mc.setAttr('miDefaultFramebuffer.datatype', 16)
    
            print (u'===============!!!Done  【%s】!!!===============' % (u'%s_WAVESNOISE层' % layerType))
            print '\n'                    
                    
        if layerName04 == 'WAVESHDW':
            layerName=layerName04
            rlObjs= refCHR+ refPROP+wavesGRP
            needSG=SGCHR+SGPROP+SGSET    
            # 创建RenderLayer
            if mc.ls(layerName):
                mc.delete(layerName)
            # 要加灯光
            mc.createRenderLayer((rlObjs + needLightGrps), name=layerName, noRecurse=1, makeCurrent=1)
             
            if len(needLightGrps)>=2:
                mc.confirmDialog(title=u'警告', message=u'可能存在两盏主光，请自行隐藏其中一盏', button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')  

            if rlObjs:
                for obj in rlObjs:
                    mesh = mc.listRelatives(obj, ni=1, type='mesh', s=1, f=1)[0]
                    mc.editRenderLayerAdjustment(mesh + '.primaryVisibility')
                    mc.setAttr((mesh + '.primaryVisibility'), 0)
                    mc.editRenderLayerAdjustment(mesh + '.receiveShadows')
                    mc.setAttr((mesh + '.receiveShadows'), 0)

            if wavesGRP:
                for obj in wavesGRP:                     
                    mesh = mc.listRelatives(obj, ni=1, type='mesh', s=1, f=1)[0]                                 
                    mc.editRenderLayerAdjustment(mesh + '.primaryVisibility')
                    mc.setAttr((mesh + '.primaryVisibility'), 1)
                    mc.editRenderLayerAdjustment(mesh + '.receiveShadows')
                    mc.setAttr((mesh + '.receiveShadows'), 1)

            # shader
            shader_Node = 'SHD_WAVE_SHDW'
            if mc.ls(shader_Node):
                mc.delete(shader_Node)
            
            shader_Node = mc.shadingNode('lambert', asShader=True, name=shader_Node)
            mc.setAttr((shader_Node+'.color'),1,1,1,type='double3')

            # 优先全局着色
            if needSG:
                for SGNode in needSG:
                    shaderInfo = mc.listConnections((SGNode + '.surfaceShader'),s = 1,plugs = 1)
                    if not shaderInfo:
                        continue
                    shaderInfo = shaderInfo[0]
                    mc.editRenderLayerAdjustment(SGNode + '.surfaceShader')
                    mc.disconnectAttr(shaderInfo, (SGNode + '.surfaceShader'))
                    mc.connectAttr((shader_Node + '.outColor'), (SGNode + '.surfaceShader'), f=1)

            # 渲染设置
            mc.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')
            
            mel.eval('setAttr "defaultRenderGlobals.enableDefaultLight" 0;')
            
            # 格式命名
            mc.setAttr('defaultRenderGlobals.animation', 1)
            mc.setAttr('defaultRenderGlobals.putFrameBeforeExt', 1)
            mc.setAttr('defaultRenderGlobals.periodInExt', 1)
            mc.setAttr('defaultRenderGlobals.extensionPadding', 4)
            if mc.getAttr('defaultRenderGlobals.outFormatControl') == 1:
                mc.setAttr('defaultRenderGlobals.outFormatControl', 0)
    
            # exr
            mc.editRenderLayerAdjustment('defaultRenderGlobals.imageFormat')
            mc.setAttr('defaultRenderGlobals.imageFormat', 51)
            mc.setAttr('defaultRenderGlobals.imfkey', 'exr', type='string')
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.setAttr('mentalrayGlobals.compressionQuality', 0)
    
            # 16位zip压缩
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.editRenderLayerAdjustment('miDefaultFramebuffer.datatype')
            mc.setAttr('miDefaultFramebuffer.datatype', 16)
    
            print (u'===============!!!Done  【%s】!!!===============' % (u'%s_WAVESHDW层' % layerType))
            print '\n'
        


    def zmRLLIGHTBabyCreate(self, layerType, selectObjType=0):
        print (u'===============!!!Start 【%s】!!!===============' % (u'%s_CHR层' % layerType))
        print 'Working...'
        
        from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
        reload(sk_referenceConfig)

        # 选取模式
        if selectObjType == 1:
            rlObjs = self.zmRLSelectMode()

        # 物体
        objs = self.zmRLObjectsTList()
        refCHR = objs[0]
        refPROP = objs[1]
        
        CHRSG= self.zmRLSGNodesGet()
        SGCHR=CHRSG[0]
        SGPROP=CHRSG[1]
        SGSET=CHRSG[2]

        rlObjs = refCHR + refPROP
        needSG = SGCHR + SGPROP
        
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        renamespace= refInfos[2][0]
        
        refername=''
        refernames=[]
        referencename=[]
        if renamespace:
            for refnames in renamespace:                        
               if '_' in refnames:
                   referencename.append(refnames)
        if referencename:
            for refnames in referencename:
                refername=refnames.split('_')[1]
                refernames.append(refername)
        sepnames=[]
        if refernames:
            for refer in refernames:
                if refer[0]=='s':
                    sepnames.append(refer)
        refernames=sepnames
                            
        filenames=[]
        filename=''
        lightnames=[]
        lightpath='Z:/Projects/ZoomWhiteDolphin/Reference/Sylvain/LIGHTING/'
        fileslist=mc.getFileList(folder= lightpath)
        
        if fileslist:
            for files in fileslist:
                    filename=files.split('.')[0]
                    filenames.append(filename)       
        
        for refnames in refernames:
            for filename in filenames:
                if refnames == filename:
                    lightnames.append(filename)
                    
        if len(lightnames)==1:
            for lightname in lightnames:
                lightFile = lightpath+lightname+'.mb'
                
        if len(lightnames)==0:
            mc.confirmDialog(title=u'警告', message=u'（1）请确保文件中有场景参考，可不必勾选但不能移除；（2）如若排除掉（1）的情况依然提示对话框，请和S联系，让他更新角色灯光', button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')
            
        if len(lightnames)>=2:
            mc.confirmDialog(title=u'警告', message=u'文件中可能存在两个以上场景参考，请确定文件以哪个场景为主，并移除其他场景参考保留主场景参考', button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')
            
        light_grp = mc.ls('LIGHTING', type='transform')

        if mc.ls(light_grp):
            mc.delete(light_grp)

        mc.file(lightFile, i=1)

        layerName = ''
        # 灯光

        lights = []
        lightGrps = []
        needLightGrps01 = []
        needLightGrps03 = []
        needLightGrps05 = []
        needLightGrps07 = []
        needLightGrps08 = []
        needLightGrps09 = []

        needLightGrps_A = []
        needLightGrps_B = []
        needLightGrps_C = []
        needLightGrps_ABC = []

        if layerType == 'CHR':
            lights = mc.ls(type='light', l=1)
            if lights:
                for light in lights:
                    lightGrps.append(mc.listRelatives(light, p=1, type='transform', f=1)[0])
                if lightGrps:
                    for grp in lightGrps:
                        if 'DAY_CHR_A1' in grp:
                            needLightGrps01.append(grp)

                        if 'DAY_CHR_B1' in grp:
                            needLightGrps03.append(grp)

                        if 'DAY_CHR_C1' in grp:
                            needLightGrps05.append(grp)

                        if 'DAY_CHRB_A' in grp:
                            needLightGrps07.append(grp)
                        if 'DAY_CHRB_B' in grp:
                            needLightGrps08.append(grp)
                        if 'DAY_CHRB_C' in grp:
                            needLightGrps09.append(grp)

                needLightGrps_A = needLightGrps01
                needLightGrps_B = needLightGrps03
                needLightGrps_C = needLightGrps05
                needLightGrps_ABC = needLightGrps07 + needLightGrps08 + needLightGrps09

                if needLightGrps_A:
                    layerName = 'CHR_LGTA'
                    if mc.ls(layerName):
                        mc.delete(layerName)
                    mc.createRenderLayer((rlObjs + needLightGrps_A), name=layerName, noRecurse=1, makeCurrent=1)
                    if mc.ls('CAM_GRP'):
                        if mc.listRelatives('CAM_GRP', c=1, f=1, type='transform'):
                            Cams= mc.listRelatives('CAM_GRP', c=1, f=1, type='transform')
                            
                    if len(Cams)==0 or len(Cams)>1:
                        mc.confirmDialog(title=u'警告', message=u'请确保CAM_GRP组下有且仅有一个相机', button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')             
                    if len(needLightGrps_A)==0 or len(needLightGrps_A)>1:
                        mc.confirmDialog(title=u'警告', message=u'请确保有且仅有一盏灯光命名有字段“DAY_CHR_A1”', button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')
                   
                    if len(Cams)==1 and len(needLightGrps_A)==1:
                        mc.orientConstraint(Cams[0],needLightGrps_A[0],weight=1)
                    
                                    
                    mc.setAttr('defaultRenderGlobals.imageFormat', 51)
                    mc.setAttr('defaultRenderGlobals.imfkey', 'exr', type='string')



                if needLightGrps_ABC:
                    layerName = 'CHR_LGTRIM'
                    if mc.ls(layerName):
                        mc.delete(layerName)
                    mc.createRenderLayer((rlObjs + needLightGrps_ABC), name=layerName, noRecurse=1, makeCurrent=1)

        if rlObjs:
            # 透明信息
            transpancyObjs = self.zmRLTransparencyObjs()
            transpancySGNodes = transpancyObjs[0]
            transpancyMeshes = transpancyObjs[1]
            transpancyNode = transpancyObjs[2]

            from idmt.maya.py_common import sk_infoConfig
            reload(sk_infoConfig)
            import os

            # openSea是否在场景里
            checkAssetID = ['s019001']
            namespaces = mc.namespaceInfo(listOnlyNamespaces=1)
            checkState = 0
            for ID in checkAssetID:
                for ns in namespaces:
                    if ID in ns:
                        checkState = 1

            # 通用LGT材质

            if layerName == 'CHR_LGTRIM':
                shaderNode = 'SHD_' + layerType + '_LGT_Shader'
                if mc.ls(shaderNode):
                    mc.delete(shaderNode)
 

                shaderNode = mc.shadingNode('lambert', asShader=True, name=shaderNode)
                mc.setAttr((shaderNode + '.color'), 1, 1, 1, type='double3')
   
                

                # 优先全局着色
                if needSG:
                    for SGNode in needSG:
                        shaderInfo = mc.listConnections((SGNode + '.surfaceShader'),s = 1,plugs = 1)
                        if not shaderInfo:
                            continue
                        shaderInfo = shaderInfo[0]
                        mc.editRenderLayerAdjustment(SGNode + '.surfaceShader')
                        mc.disconnectAttr(shaderInfo, (SGNode + '.surfaceShader'))
                        mc.connectAttr((shaderNode + '.outColor'), (SGNode + '.surfaceShader'), f=1)
  
                if transpancySGNodes:
                    for i in range(len(transpancySGNodes)):
                        if mc.ls(transpancySGNodes[i]):
                            if '_' not in transpancySGNodes[i]:
                                print u'>>>>>>[注意][%s]名字需要最少有1个_分隔符' % transpancySGNodes[i]
                            else:
                                keySGInfo = transpancySGNodes[i].split('_')[-2]
                            keySGInfo = str(i)
                            meshes = transpancyMeshes[i]
                            # 有着色物体时才进行
                            if meshes:
                                shaderTrsNode = 'SHD_' + layerType + '_' + keySGInfo + '_LGT_Shader'
                                if mc.ls(shaderTrsNode):
                                    mc.delete(shaderTrsNode)
     

                                # 创建
                                shaderTrsNode = mc.shadingNode('lambert', asShader=True, name=shaderTrsNode)
                                mc.setAttr((shaderTrsNode + '.color'), 1, 1, 1, type='double3')
     
                                # 透明连接
                                self.zmRLTransShaderConnectiion(transpancyNode[i], shaderTrsNode, 'transparency')

                                # file贴图反转
                                if '.outTransparency' in transpancyNode[i]:
                                    mc.editRenderLayerAdjustment(transpancyNode[i].split('.')[0] + '.invert')
                                    mc.setAttr((transpancyNode[i].split('.')[0] + ".invert"), 1)

                                # 连接着色
                                mc.editRenderLayerAdjustment(transpancySGNodes[i] + '.surfaceShader')
                                mc.connectAttr((shaderTrsNode + '.outColor'), (transpancySGNodes[i] + '.surfaceShader'), f=1)

                                # 着色
                                shaderInfo = mc.listConnections((transpancySGNodes[i] + '.surfaceShader'),s = 1,plugs = 1)
                                if shaderInfo:
                                    shaderInfo = shaderInfo[0]
                                    mc.editRenderLayerAdjustment(transpancySGNodes[i] + '.surfaceShader')
                                    mc.disconnectAttr(shaderInfo, (transpancySGNodes[i] + '.surfaceShader'))
                                    mc.connectAttr((shaderTrsNode + '.outColor'), (transpancySGNodes[i] + '.surfaceShader'), f=1)
 

            # 设置
            # self.zmRLCommonConfig()
            # 渲染设置
            mc.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')

            # 格式命名
            mc.setAttr('defaultRenderGlobals.animation', 1)
            mc.setAttr('defaultRenderGlobals.putFrameBeforeExt', 1)
            mc.setAttr('defaultRenderGlobals.periodInExt', 1)
            mc.setAttr('defaultRenderGlobals.extensionPadding', 4)
            if mc.getAttr('defaultRenderGlobals.outFormatControl') == 1:
                mc.setAttr('defaultRenderGlobals.outFormatControl', 0)

            # exr
            mc.editRenderLayerAdjustment('defaultRenderGlobals.imageFormat')
            mc.setAttr('defaultRenderGlobals.imageFormat', 51)
            mc.setAttr('defaultRenderGlobals.imfkey', 'exr', type='string')
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.setAttr('mentalrayGlobals.compressionQuality', 0)

            # 16位zip压缩
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.editRenderLayerAdjustment('miDefaultFramebuffer.datatype')
            mc.setAttr('miDefaultFramebuffer.datatype', 16)

            print (u'===============!!!Done  【%s】!!!===============' % (u'%s_CH层' % layerType))
            print '\n'
        else:
            print (u'===============!!!Error  【%s】无物体!!!===============' % (u'%s_CHR层' % layerType))
            print '\n'





    
    # CAUSTICSWALLS
    def zmRLCAUSTICSWALLSCreate(self, layerType, selectObjType=0):
        print (u'===============!!!Start 【%s】!!!===============' %
               (u'%s_CAUSTICSWALLS层' % layerType))
        print 'Working...'

        # 物体
        objs = self.zmRLObjectsTList()
        refCHR = objs[0]
        refPROP = objs[1]
        refSET = objs[2]
        refSKY = objs[3]
        refSEA = objs[4]
        
        CausticSG= self.zmRLSGNodesGet()
        SGCHR=CausticSG[0]
        SGPROP=CausticSG[1]
        SGSET=CausticSG[2]


        causticLight = ''
        lightFile=''
        needLightGrps=[]           
        rlObjs = []
        needSG= []
        layerName = 'CAUSTICSWALLS'
        if layerType == 'BG':
            rlObjs = refSET
            needSG = SGSET
            
            lightFile = 'Z:/Projects/ZoomWhiteDolphin/Reference/Sylvain/LIGHTING/LGT_Caustics_ForbiddenCave.mb'
            causticLight = 'Caustics_ForbiddenCave_LGT'
                
       

    
        # 选取模式

        if selectObjType == 1:
            rlObjs = self.zmRLSelectMode()


        if rlObjs:
            # 特殊处理，半透明用
            # 获取信息必须在masterLayer进行
            transpancyObjs = self.zmRLTransparencyObjs()
            transpancySGNodes = transpancyObjs[0]
            transpancyMeshes = transpancyObjs[1]
            transpancyNode = transpancyObjs[2]


            # 灯光导入
            if mc.ls(causticLight):
                mc.delete(causticLight)

            if lightFile:
                ns = 'FoodTemp'
                mc.file(lightFile, i=1, namespace=ns)
                # 使得namespace成为空的namespace
                mc.namespace(force=1, moveNamespace=[(':' + ns), ':'])
                # 清理空namespace
                mc.namespace(removeNamespace=(':' + ns))
            

            # 创建渲染层
            if mc.ls(layerName):
                mc.delete(layerName)
            mc.createRenderLayer((rlObjs + [causticLight]), name=layerName, noRecurse=1, makeCurrent=1)
                

            # 不需要Sky
            if refSKY:
                for obj in refSKY:
                    mc.editRenderLayerAdjustment(obj + '.visibility')
                    mc.setAttr((obj + '.visibility'), 0)

            
            # shader
            if layerType == 'BG':
                shader_Node = 'SHD_CAUSTICSWALLS_BG'
             
            if mc.ls(shader_Node):
                  mc.delete(shader_Node)    
            shader_Node = mc.shadingNode('lambert', asShader=True, name=shader_Node)
            mc.setAttr(shader_Node + '.color', 1, 1, 1, type='double3')  
            
            if needSG:
                for SGNode in needSG:
                    shaderInfo = mc.listConnections((SGNode + '.surfaceShader'),s = 1,plugs = 1)
                    if not shaderInfo:
                        continue
                    shaderInfo = shaderInfo[0]
                    mc.editRenderLayerAdjustment(SGNode + '.surfaceShader')
                    mc.disconnectAttr(shaderInfo, (SGNode + '.surfaceShader'))
                    mc.connectAttr((shader_Node + '.outColor'), (SGNode + '.surfaceShader'), f=1)   
          
            
            # 特殊物体着色
            if transpancySGNodes:
                for i in range(len(transpancySGNodes)):
                    if mc.ls(transpancySGNodes[i]):
                        if '_' not in transpancySGNodes[i]:
                            print u'>>>>>>[注意][%s]名字需要最少有1个_分隔符' % transpancySGNodes[i]
                        else:
                            keySGInfo = transpancySGNodes[i].split('_')[-2]
                        keySGInfo = str(i)
                        meshes = transpancyMeshes[i]
                        # 有着色物体时才进行
                        if meshes:
                            shaderNode = 'SHD_' + layerType + '_' + keySGInfo + '_caustics'
                            if mc.ls(shaderNode):
                                mc.delete(shaderNode)

                            shaderNode = mc.shadingNode('lambert', asShader=True, name=shaderNode)
                            mc.setAttr(shaderNode + '.color', 1, 1, 1, type='double3')

                            # 透明连接
                            self.zmRLTransShaderConnectiion(transpancyNode[i], shaderNode, 'transparency')

                            # 翻转
                            if '.outTransparency' in transpancyNode[i]:
                                mc.editRenderLayerAdjustment(transpancyNode[i].split('.')[0] + '.invert')
                                mc.setAttr((transpancyNode[i].split('.')[0] + ".invert"), 1)

                            # 连接着色

                            shaderInfo = mc.listConnections((transpancySGNodes[i] + '.surfaceShader'),s = 1,plugs = 1)
                            if shaderInfo:
                                shaderInfo = shaderInfo[0]
                                mc.editRenderLayerAdjustment(transpancySGNodes[i] + '.surfaceShader')
                                mc.disconnectAttr(shaderInfo, (transpancySGNodes[i] + '.surfaceShader'))
                                mc.connectAttr((shaderNode + '.outColor'), (transpancySGNodes[i] + '.surfaceShader'), f=1)
            
            if mc.ls('CAM_GRP'):
                if mc.listRelatives('CAM_GRP', c=1, f=1, type='transform'):
                    Cams= mc.listRelatives('CAM_GRP', c=1, f=1, type='transform')
            if mc.ls('Caustics_ForbiddenCave_LGT',l=1):
                needLightGrps=mc.ls('Caustics_ForbiddenCave_LGT',l=1)                    
            if len(Cams)==0 or len(Cams)>1:
                mc.confirmDialog(title=u'警告', message=u'请确保CAM_GRP组下有且仅有一个相机', button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')   
            if len(Cams)==1:
                print Cams[0]
                mc.orientConstraint(Cams[0],needLightGrps[0],weight=1)
                mc.pointConstraint(Cams[0],needLightGrps[0])
                
            pConstraint=mc.ls('Caustics_ForbiddenCave_LGT_pointConstraint*',type='pointConstraint')
            oConstraint=mc.ls('Caustics_ForbiddenCave_LGT_orientConstraint*',type='orientConstraint')
            if pConstraint:
                mc.disconnectAttr((pConstraint[0]+'.constraintTranslateX'),(needLightGrps[0]+'.translateX'))
                mc.disconnectAttr((pConstraint[0]+'.constraintTranslateY'),(needLightGrps[0]+'.translateY'))
                mc.disconnectAttr((pConstraint[0]+'.constraintTranslateZ'),(needLightGrps[0]+'.translateZ'))
    
            if oConstraint:
                mc.disconnectAttr((oConstraint[0]+'.constraintRotateX'),(needLightGrps[0]+'.rotateX'))
                mc.disconnectAttr((oConstraint[0]+'.constraintRotateY'),(needLightGrps[0]+'.rotateY'))
                mc.disconnectAttr((oConstraint[0]+'.constraintRotateZ'),(needLightGrps[0]+'.rotateZ'))
                
             
                             
            # 加载MR
            if mc.pluginInfo('Mayatomr.mll', q=1, loaded=1):
                mel.eval('loadPlugin "Mayatomr.mll"')
                mc.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')
            # MR设置
            mc.editRenderLayerAdjustment('miDefaultOptions.rayTracing')
            mc.setAttr('miDefaultOptions.rayTracing', 1)
            mc.editRenderLayerAdjustment('miDefaultOptions.maxReflectionRays')
            mc.setAttr('miDefaultOptions.maxReflectionRays', 10)
            mc.editRenderLayerAdjustment('miDefaultOptions.maxRefractionRays')
            mc.setAttr('miDefaultOptions.maxRefractionRays', 10)
            mc.editRenderLayerAdjustment('miDefaultOptions.maxRayDepth')
            mc.setAttr('miDefaultOptions.maxRayDepth', 20)
            mc.editRenderLayerAdjustment('miDefaultOptions.maxShadowRayDepth')
            mc.setAttr('miDefaultOptions.maxShadowRayDepth', 2)
            mc.editRenderLayerAdjustment('miDefaultOptions.maxReflectionBlur')
            mc.setAttr('miDefaultOptions.maxReflectionBlur', 1)
            mc.editRenderLayerAdjustment('miDefaultOptions.maxRefractionBlur')
            mc.setAttr('miDefaultOptions.maxRefractionBlur', 1)

            # 格式命名
            mc.setAttr('defaultRenderGlobals.animation', 1)
            mc.setAttr('defaultRenderGlobals.putFrameBeforeExt', 1)
            mc.setAttr('defaultRenderGlobals.periodInExt', 1)
            mc.setAttr('defaultRenderGlobals.extensionPadding', 4)
            if mc.getAttr('defaultRenderGlobals.outFormatControl') == 1:
                mc.setAttr('defaultRenderGlobals.outFormatControl', 0)

            # exr
            mc.editRenderLayerAdjustment('defaultRenderGlobals.imageFormat')
            mc.setAttr('defaultRenderGlobals.imageFormat', 51)
            mc.setAttr('defaultRenderGlobals.imfkey', 'exr', type='string')
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.setAttr('mentalrayGlobals.compressionQuality', 0)

            # 16位zip压缩
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.editRenderLayerAdjustment('miDefaultFramebuffer.datatype')
            mc.setAttr('miDefaultFramebuffer.datatype', 16)
            mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')
            mc.setAttr("defaultRenderLayer.renderable", 0)

            print (u'===============!!!Done  【%s】!!!===============' % (u'%s_CAUSTICSWALLS层' % layerType))
            print '\n'

        else:
            print (u'===============!!!Error  【%s】无物体!!!===============' % (u'%s_CAUSTICSWALLS层' % layerType))
            print '\n'



    def zmRLVOLUMELIGHTSCreate(self, layerType, selectObjType=0):
        print (u'===============!!!Start 【%s】!!!===============' % (u'%s_VOLUMELIGHTS层' % layerType))
        print 'Working...'

        # 物体
        objs = self.zmRLObjectsTList()
        refCHR = objs[0]
        refPROP = objs[1]
        refSET = objs[2]
        refSKY = objs[3]
        seaInfo = objs[4]
        rlObjs = []
        sepgrp=[]
        
        if layerType == 'BG':
            rlObjs = refSET
            layerName = 'VOLUMELIGHTS'
            
        if rlObjs:
            for obj in rlObjs:
                if 'MSH_c_hi_volumeLIGHT_'in obj:
                    sepgrp.append(obj)
        if sepgrp:
            for obj in sepgrp:
                rlObjs.remove(obj)


        # 选取模式
        if selectObjType == 1:
            rlObjs = self.zmRLSelectMode()


        if rlObjs:
            # 透明信息
            transpancyObjs = self.zmRLTransparencyObjs()
            transpancySGNodes = transpancyObjs[0]
            transpancyMeshes = transpancyObjs[1]
            transpancyNode = transpancyObjs[2]


            # 创建RenderLayer
            if mc.ls(layerName):
                mc.delete(layerName)
            mc.createRenderLayer(rlObjs+sepgrp, name=layerName, noRecurse=1, makeCurrent=1)

            # 通用LGT材质
            shaderNode = 'SHD_' + layerType + '_MATTE_Shader'
            if mc.ls(shaderNode):
                mc.delete(shaderNode)

            shaderMATTESG = 'SHD_' + layerType + '_MATTE_SG'
            if mc.ls(shaderMATTESG):
                mc.delete(shaderMATTESG)
                
            shaderNode = mc.shadingNode('lambert', asShader=True, name=shaderNode)
            mc.setAttr((shaderNode + '.color'), 0, 0, 0, type='double3')
            mc.setAttr((shaderNode + '.matteOpacityMode'), 0)

            shaderMATTESG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=shaderMATTESG)
            mc.connectAttr((shaderNode + '.color'), (shaderMATTESG + '.surfaceShader'))
            # 优先全局着色
            for obj in rlObjs:
                try:
                    mc.sets(obj, e=1, forceElement=shaderMATTESG)
                except:
                    # 获取物体面数
                    faceNum = mc.polyEvaluate(obj, face=1)
                    mc.sets((obj + u'.f[:' + str(faceNum - 1) + u']'), e=1, forceElement=shaderMATTESG)



            if transpancySGNodes:
                for i in range(len(transpancySGNodes)):
                    if mc.ls(transpancySGNodes[i]):
                        if '_' not in transpancySGNodes[i]:
                            print u'>>>>>>[注意][%s]名字需要最少有1个_分隔符' % transpancySGNodes[i]
                        else:
                            keySGInfo = transpancySGNodes[i].split('_')[-2]
                        keySGInfo = str(i)
                        meshes = transpancyMeshes[i]
                        # 有着色物体时才进行
                        if meshes:
                            #创建透明节点
                            shaderTrsNode = 'SHD_' + layerType + '_' + keySGInfo + '_matte_Shader'
                            if mc.ls(shaderTrsNode):
                                mc.delete(shaderTrsNode)
                            shaderTrsNode = mc.shadingNode('lambert', asShader=True, name=shaderTrsNode)
                            mc.setAttr((shaderTrsNode + '.color'), 0, 0, 0, type='double3')
                            mc.setAttr((shaderTrsNode + '.matteOpacityMode'), 0)
                            #创建透明SG节点
                            shaderTrsSG = 'SHD_' + layerType +  '_' + keySGInfo + '_matteSG'
                            shaderTrsSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=shaderTrsSG)

                            mc.connectAttr((shaderTrsNode + '.outColor'), (shaderTrsSG + '.surfaceShader'))
                            # 透明连接
                            self.zmRLTransShaderConnectiion(transpancyNode[i], shaderTrsNode, 'transparency')

                            # file贴图反转
                            if '.outTransparency' in transpancyNode[i]:
                                mc.editRenderLayerAdjustment(transpancyNode[i].split('.')[0] + '.invert')
                                mc.setAttr((transpancyNode[i].split('.')[0] + ".invert"), 1)
                            
                            for mesh in meshes:       
                                mc.sets(mesh, e=1, forceElement=shaderTrsSG)

 
            if mc.ls('*:*VOLUME_LIGHTS',l=1):
                volumeGrp = mc.ls('*:*VOLUME_LIGHTS',l=1)
                mc.editRenderLayerAdjustment(volumeGrp[0] + '.v')
                mc.setAttr((volumeGrp[0] + '.v'), 1)

                                               
            # 渲染设置
            mc.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')

            # 格式命名
            mc.setAttr('defaultRenderGlobals.animation', 1)
            mc.setAttr('defaultRenderGlobals.putFrameBeforeExt', 1)
            mc.setAttr('defaultRenderGlobals.periodInExt', 1)
            mc.setAttr('defaultRenderGlobals.extensionPadding', 4)
            if mc.getAttr('defaultRenderGlobals.outFormatControl') == 1:
                mc.setAttr('defaultRenderGlobals.outFormatControl', 0)

            # exr
            mc.editRenderLayerAdjustment('defaultRenderGlobals.imageFormat')
            mc.setAttr('defaultRenderGlobals.imageFormat', 51)
            mc.setAttr('defaultRenderGlobals.imfkey', 'exr', type='string')
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.setAttr('mentalrayGlobals.compressionQuality', 0)

            # 16位zip压缩
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.editRenderLayerAdjustment('miDefaultFramebuffer.datatype')
            mc.setAttr('miDefaultFramebuffer.datatype', 16)

            print (u'===============!!!Done  【%s】!!!===============' % (u'%s_VOLUMELIGHTS层' % layerType))
            print '\n'
        else:
            print (u'===============!!!Error  【%s】无物体!!!===============' % (u'%s_VOLUMELIGHTS层' % layerType))
            print '\n'


    def zmMSK04Create(self, layerType, selectObjType=0):
        print (u'===============!!!Start 【%s】!!!===============' % (u'%s_MSK04层' % 'ALL'))
        print 'Working...'

        if layerType == 'PROP':
            layerName = 'PROP_MASK04'

        # 选取模式
        if selectObjType == 1:
            rlObjs = self.zmRLSelectMode()
        # 物体
        objs = self.zmRLObjectsTList()
        refCHR = objs[0]
        refPROP = objs[1]
        refSET = objs[2]
        refSKY = objs[3]
        refSEA = objs[4]
               
        NightGreen=[]
        NightBlue=[]
        Pop=[]
        if mc.ls('*_p82222222CapsulePatrick_*:*'):
            if refPROP:
                for obj in refPROP:
                    if 'p82222222CapsulePatrick' in obj:
                        Pop.append(obj)
                        if 'MSH_c_hi_Capsule_ca_40_' in obj:
                            NightGreen.append(obj)
                        if 'MSH_c_hi_Capsule_ca_41_' in obj:
                            NightGreen.append(obj)
                        if 'MSH_c_hi_Capsule_ca_15_' in obj:
                            NightBlue.append(obj)
                objsAll=Pop 
        else:
            mc.confirmDialog(title=u'警告', message=u'请确定文件中有"p82222222CapsulePatrick"这个道具，', button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')
                    
               
        if objsAll:

            # 创建RenderLayer
            if mc.ls(layerName):
                mc.delete(layerName)

            mc.createRenderLayer(objsAll, name=layerName, noRecurse=1, makeCurrent=1)


            # 通用RGB材质
            shaderMNode = 'SHD_' + layerType + '_R_Shader'
            if mc.ls(shaderMNode):
                mc.delete(shaderMNode)


            shaderMSG = 'SHD_' + layerType + '_R_SG'
            if mc.ls(shaderMSG):
                mc.delete(shaderMSG)


            shaderMNode = mc.shadingNode('lambert', asShader=True, name=shaderMNode)
            mc.setAttr((shaderMNode + '.color'), 1, 0, 0, type='double3')
            mc.setAttr((shaderMNode + '.ambientColor'), 1, 1, 1, type='double3')

            shaderMSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=shaderMSG)

            mc.connectAttr((shaderMNode + '.color'), (shaderMSG + '.surfaceShader'))

            # 优先全局着色，赋予Mask

            for obj in objsAll:
                try:
                    mc.sets(obj, e=1, forceElement=shaderMSG)
                except:
                    # 获取物体面数
                    faceNum = mc.polyEvaluate(obj, face=1)
                    mc.sets((obj + u'.f[:' + str(faceNum - 1) + u']'), e=1, forceElement=shaderMSG)

                                      
            if NightGreen:
                for obj in NightGreen:
                    mc.select(obj)
                    mel.eval('source "//file-cluster/GDC/Resource/Support/Maya/projects/Lionelville/HbRgbaMaterialTool.mel";HbMaterialG;')
        
           
            if NightBlue:
                for obj in NightBlue:
                    mc.select(obj)
                    mel.eval('source "//file-cluster/GDC/Resource/Support/Maya/projects/Lionelville/HbRgbaMaterialTool.mel";HbMaterialB;')       


            # 设置
            # self.zmRLCommonConfig()
            # 渲染设置
            mc.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')

            # 关闭光线追踪
            mc.editRenderLayerAdjustment('miDefaultOptions.rayTracing')
            mc.setAttr('miDefaultOptions.rayTracing', 0)

            # 格式命名
            mc.setAttr('defaultRenderGlobals.animation', 1)
            mc.setAttr('defaultRenderGlobals.putFrameBeforeExt', 1)
            mc.setAttr('defaultRenderGlobals.periodInExt', 1)
            mc.setAttr('defaultRenderGlobals.extensionPadding', 4)
            if mc.getAttr('defaultRenderGlobals.outFormatControl') == 1:
                mc.setAttr('defaultRenderGlobals.outFormatControl', 0)

            # exr
            mc.editRenderLayerAdjustment('defaultRenderGlobals.imageFormat')
            mc.setAttr('defaultRenderGlobals.imageFormat', 51)
            mc.setAttr('defaultRenderGlobals.imfkey', 'exr', type='string')
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.setAttr('mentalrayGlobals.compressionQuality', 0)

            # 16位zip压缩
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.editRenderLayerAdjustment('miDefaultFramebuffer.datatype')
            mc.setAttr('miDefaultFramebuffer.datatype', 16)

            print (u'===============!!!Done  【%s】!!!===============' % (u'%s_MSK04层' % 'ALL'))
            print '\n'
        else:
            print (u'===============!!!Error  【%s】无物体!!!===============' % (u'%s_MSK04层' % 'ALL'))
            print '\n'     
            
            
            
    def zmFIRECreate(self, layerType, selectObjType=0):
        print (u'===============!!!Start 【%s】!!!===============' % (u'%s_FIRE层' % layerType))
        print 'Working...'

        # 物体
        objs = self.zmRLObjectsTList()
        refCHR = objs[0]
        refPROP = objs[1]
        refSET = objs[2]
        refSKY = objs[3]
        seaInfo = objs[4]
        
        
        LGTSG= self.zmRLSGNodesGet()
        SGCHR=LGTSG[0]
        SGPROP=LGTSG[1]
        SGSET=LGTSG[2]
        
        rlObjs = []
        needSG = []


        # 灯光
        LG=mc.ls('*:*LIGHTING_EXT')
        if LG:
            mc.setAttr((LG[0]+'.Mood'),4)      
        needLightGrps=mc.listRelatives('*:*NIGHT_OFF', ad=1, ni=1,type='light',f=1)
               
                     
        if layerType == 'FG':
            rlObjs = refSET + refCHR + refPROP
            needSG = SGCHR + SGPROP + SGSET
            if needSG:
                needSG = list(set(needSG))            
            layerName = 'FG_LGTFIRE'

        if layerType == 'CHR':
            rlObjs =  refCHR + refPROP
            needSG =  SGPROP + SGCHR
            if needSG:
                needSG = list(set(needSG))            
            layerName = 'CHR_LGTFIRE'

        if rlObjs:
            # 特殊处理，半透明用
            # 获取信息必须在masterLayer进行
            transpancyObjs = self.zmRLTransparencyObjs()
            transpancySGNodes = transpancyObjs[0]
            transpancyMeshes = transpancyObjs[1]
            transpancyNode = transpancyObjs[2]

            # openSea是否在场景里
            checkAssetID = ['s019001']
            namespaces = mc.namespaceInfo(listOnlyNamespaces=1)
            checkState = 0
            for ID in checkAssetID:
                for ns in namespaces:
                    if ID in ns:
                        checkState = 1

            

            # 创建渲染层
            if mc.ls(layerName):
                mc.delete(layerName)

            mc.createRenderLayer((rlObjs + needLightGrps), name=layerName, noRecurse=1, makeCurrent=1)

            # openSea是否在场景里
            checkAssetID = ['s019001']
            namespaces = mc.namespaceInfo(listOnlyNamespaces=1)
            checkState = 0
            for ID in checkAssetID:
                for ns in namespaces:
                    if ID in ns:
                        checkState = 1

            # BG渲染关闭
            if layerType == 'FG':
                if (refCHR + refPROP):
                    for obj in (refCHR + refPROP):
                        mesh = mc.listRelatives(obj, ni=1, type='mesh', s=1, f=1)[0]
                        mc.editRenderLayerAdjustment(mesh + '.primaryVisibility')
                        mc.setAttr((mesh + '.primaryVisibility'), 0)           

            # 不需要Sky
            if refSKY:
                for obj in refSKY:
                    mc.editRenderLayerAdjustment(obj + '.visibility')
                    mc.setAttr((obj + '.visibility'), 0)

            if seaInfo:
                for obj in seaInfo:
                    mc.editRenderLayerAdjustment(obj + '.visibility')
                    mc.setAttr((obj + '.visibility'), 0)

            # openSea在则隐藏
            if checkState:
                lightingGrps = mc.ls('*:*LIGHTING', type='transform') + mc.ls('*:*:*LIGHTING', type='transform')
                for ID in checkAssetID:
                    for grp in lightingGrps:
                        if ID not in grp:
                            mc.editRenderLayerAdjustment(grp + '.visibility')
                            mc.setAttr((grp + '.visibility'), 0)
                            
            cyclosGrp = mc.ls('*:*:*MSH_c_hi_Cyclos',type = 'transform',l=1)
            if cyclosGrp:
                meshes = mc.listRelatives(cyclosGrp,ad = 1,type = 'mesh',f = 1)
                polyGrps = mc.listRelatives(meshes,p = 1,type = 'transform',f = 1)
                polyGrps = list(set(polyGrps))
                for grp in polyGrps:
                    mc.editRenderLayerAdjustment(grp + '.visibility')
                    mc.setAttr((grp + '.visibility'), 0)   

            # shader
            if layerType == 'FG':
                shader_Node = 'SHD_FIRE_FG'
             
               
            if layerType == 'CHR':
                shader_Node = 'SHD_FIRE_CHR'
 
                
            if mc.ls(shader_Node):
                mc.delete(shader_Node)    
            shader_Node = mc.shadingNode('lambert', asShader=True, name=shader_Node)
            mc.setAttr(shader_Node + '.color', 1, 1, 1, type='double3')  
            
            if needSG:
                for SGNode in needSG:
                    shaderInfo = mc.listConnections((SGNode + '.surfaceShader'),s = 1,plugs = 1)
                    if not shaderInfo:
                        continue
                    shaderInfo = shaderInfo[0]
                    mc.editRenderLayerAdjustment(SGNode + '.surfaceShader')
                    mc.disconnectAttr(shaderInfo, (SGNode + '.surfaceShader'))
                    mc.connectAttr((shader_Node + '.outColor'), (SGNode + '.surfaceShader'), f=1)   
          

            # 特殊物体着色
            if transpancySGNodes:
                for i in range(len(transpancySGNodes)):
                    if mc.ls(transpancySGNodes[i]):
                        if '_' not in transpancySGNodes[i]:
                            print u'>>>>>>[注意][%s]名字需要最少有1个_分隔符' % transpancySGNodes[i]
                        else:
                            keySGInfo = transpancySGNodes[i].split('_')[-2]
                        keySGInfo = str(i)
                        meshes = transpancyMeshes[i]
                        # 有着色物体时才进行
                        if meshes:
                            shaderNode = 'SHD_' + layerType + '_' + keySGInfo + '_caustics'
                            if mc.ls(shaderNode):
                                mc.delete(shaderNode)

                            shaderNode = mc.shadingNode('lambert', asShader=True, name=shaderNode)
                            mc.setAttr(shaderNode + '.color', 1, 1, 1, type='double3')

                            # 透明连接
                            self.zmRLTransShaderConnectiion(transpancyNode[i], shaderNode, 'transparency')

                            # 翻转
                            if '.outTransparency' in transpancyNode[i]:
                                mc.editRenderLayerAdjustment(transpancyNode[i].split('.')[0] + '.invert')
                                mc.setAttr((transpancyNode[i].split('.')[0] + ".invert"), 1)

                            # 连接着色

                            shaderInfo = mc.listConnections((transpancySGNodes[i] + '.surfaceShader'),s = 1,plugs = 1)
                            if shaderInfo:
                                shaderInfo = shaderInfo[0]
                                mc.editRenderLayerAdjustment(transpancySGNodes[i] + '.surfaceShader')
                                mc.disconnectAttr(shaderInfo, (transpancySGNodes[i] + '.surfaceShader'))
                                mc.connectAttr((shaderNode + '.outColor'), (transpancySGNodes[i] + '.surfaceShader'), f=1)


            # 渲染设置
            mc.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')

            # 格式命名
            mc.setAttr('defaultRenderGlobals.animation', 1)
            mc.setAttr('defaultRenderGlobals.putFrameBeforeExt', 1)
            mc.setAttr('defaultRenderGlobals.periodInExt', 1)
            mc.setAttr('defaultRenderGlobals.extensionPadding', 4)
            if mc.getAttr('defaultRenderGlobals.outFormatControl') == 1:
                mc.setAttr('defaultRenderGlobals.outFormatControl', 0)

            # exr
            mc.editRenderLayerAdjustment('defaultRenderGlobals.imageFormat')
            mc.setAttr('defaultRenderGlobals.imageFormat', 51)
            mc.setAttr('defaultRenderGlobals.imfkey', 'exr', type='string')
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.setAttr('mentalrayGlobals.compressionQuality', 0)

            # 16位zip压缩
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.editRenderLayerAdjustment('miDefaultFramebuffer.datatype')
            mc.setAttr('miDefaultFramebuffer.datatype', 16)

            print (u'===============!!!Done  【%s】!!!===============' % (u'%s_层' % layerType))
            print '\n'
        else:
            print (u'===============!!!Error  【%s】无物体!!!===============' % (u'%s_FIRE层' % layerType))
            print '\n'
            
            
            
            
            
            