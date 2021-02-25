# -*- coding: utf-8 -*-

'''
Created on 2013-6-18

@author: shenkang
'''
import maya.cmds as mc
import maya.mel as mel
import idmt.pipeline.db

from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
reload(sk_infoConfig)

class sk_renderLayer_Yoda(object):
    def __init__(self):
        pass

    #--------------------------------------------------------------------------------------------------------#
    #----------------------------------------------------------#
    # 【核心】 自动创建函数
    #----------------------------------------------------------#
    # Auto Create
    #　createMode　        　０　是第一场创建，要输出信息  | 1 是第一次之后的输出，网络读信息
    # refClean        参考清理
    # RGB             允许创建RGB
    # RGBCreatType    
    def ydRLAutoCreate(self, createMode = 0 ,refClean = 1 , RGB = 0 , RGBCreatType = 0 , shaderForece = 0):
        print ('=================================================================')
        print '====================!!!Start AutoRenderLayer!!!===================='

        # Back To MasterLayer
        mc.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
        # clean renderlayer
        from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools
        reload(sk_sceneTools)
        from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
        reload(sk_referenceConfig)
        if refClean == 1:
            # 处理非参考的namespace
            sk_sceneTools.sk_sceneTools().sk_sceneNoRefNamespaceClean()
        # clean unknown nodes
        sk_sceneTools.sk_sceneTools().checkDonotNodeCleanBase(0)
        #清理渲染层
        sk_sceneTools.sk_sceneTools().checkCleanRenderLayers()
        
        # Step Base:[导出]
        # 导出
        print '\n'
        print u'========================导出清理开始========================'
        print u'===如果本阶段失败，请打开文件手动清理'
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        pathLocal = sk_infoConfig.sk_infoConfig().checkRenderLayerLocalPath(3)
        baseFileName = pathLocal + shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2] + '_' + shotInfo[3] + '_Base' + '.mb'
        baseFileName = baseFileName.replace('D:','E:')

        baseGrps = mc.ls(assemblies=True)
        mc.select(baseGrps)
        mrNodes = mc.ls(type='mentalrayGlobals')+ mc.ls(type='mentalrayItemsList') +mc.ls(type='mentalrayOptions')
        if mrNodes:
            mc.select(mrNodes,add = 1)
#修改日期2014/11/5 （韩虹）
        mc.file(baseFileName,options='v=0',f=1,type='mayaBinary',preserveReferences=1,es=1)    
#        mc.file(baseFileName,f = 1,es = 1,pr = 1,type = 'mayaBinary')
        print u'---50%'
        # 重打开
        #mc.file(f=1, new=1)
        #mc.file(rename = baseFileName)
        ##mc.file(baseFileName,open = 1 , f = 1)
        #mc.file( baseFileName , i = 1 , mergeNamespacesOnClash = 0 , pr = 1)
        mc.file(baseFileName,options='v=0',type='mayaBinary',f=1,o=1)        
        print u'---100%'
        print u'========================导出清理成功========================'
        print u'===下面开始正式分层'
        print '\n'

        # common Setting
        self.ydRLCommonConfig()
        
        # mr Setting
        self.mentalRayProductionLevel()
        
        # 格式
        self.ydRLFramebuffer('iff',3,0)

        # 断开连接,在master层处理,避免分层时处理崩溃
        objsNeedHide = self.ydRLGBowObjs() 
        objsNeedHide = self.ydRLFaceObjs() + objsNeedHide
        if objsNeedHide:
            for obj in objsNeedHide:
                mc.lockNode((obj + '.v'), l = 0)
                self.ydRLDeleteConnection((obj + '.v'))

        # 备份
        #mc.file(rename= baseFileName)
        #mc.file(s = 1 , f = 1)

        idPass = ['BSR','FBR','SPR']

        # Step Base:参考import
        #sk_referenceConfig.sk_referenceConfig().checkRefAllImport()
        # Back To MasterLayer
        #print '=====================================hello======================================'
        mc.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
        # 输出透明信息
        self.ydRLTransparencyObjsOld(0,1)
        #print '=====================================hdone======================================'

        # Step 0：输出信息
        if createMode == 0:
            self.ydRLObjectsTList(2,1,'mesh')
            self.ydRLObjectsTList(2,1,'light')

        # Step 1：CHR
        #self.ydRLSave('BASE',3)
        
        keyInfos = ['CHRF','CHRM','CHRB']

        for key in keyInfos:
            # 清理渲染层
            sk_sceneTools.sk_sceneTools().checkCleanRenderLayers()
            self.ydRLSYSShaderClean()
            # Color
            self.ydRLCOCreate(key)
            # Ambient Occlusion
            self.ydRLAOCreate(key , shaderForece = shaderForece)
            # Back To MasterLayer
            mc.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
            # Normal
            self.ydRLNMCreate(key , shaderForece = shaderForece)
            # Back To MasterLayer
            mc.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
            # Light
            self.ydRLFNCreate(key , shaderForece = shaderForece)
            
            if mc.ls(key + '_CO'):
                # smoothSet
                #self.ydRLDoSmooth()
                # Back To MasterLayer
                mc.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
                # Unrender MasterLayer
                mc.setAttr("defaultRenderLayer.renderable", 0)
                # mc.setAttr
                # common Setting
                self.ydRLCommonConfig()
                # save
                self.ydRLSave(key,3)
                
            # IDP创建模式
            if RGB:
                for idp in idPass:
                    # 清理渲染层
                    sk_sceneTools.sk_sceneTools().checkCleanRenderLayers()
                    self.ydRLSYSShaderClean()
                    # 单层 
                    self.ydRLRGBCreate((key + '_' + idp) , shaderForece = shaderForece)
                    # Back To MasterLayer
                    mc.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
                    if RGBCreatType:
                        if mc.ls(key + '_' + idp):
                            # Back To MasterLayer
                            mc.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
                            # Unrender MasterLayer
                            mc.setAttr("defaultRenderLayer.renderable", 0)
                            # common Setting
                            self.ydRLCommonConfig()
                            # save
                            self.ydRLSave(key,3,idp)
                if not RGBCreatType:
                    # 多层创建
                    if mc.ls(key + '_BSR'):
                        # Back To MasterLayer
                        mc.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
                        # Unrender MasterLayer
                        mc.setAttr("defaultRenderLayer.renderable", 0)
                        # mc.setAttr
                        # common Setting
                        self.ydRLCommonConfig()
                        # save
                        self.ydRLSave(key,3,'RGB')

        # Step 2：PRP
        keyInfos = ['PRPF','PRPM','PRPB']
        
        for key in keyInfos:
            # 清理渲染层
            sk_sceneTools.sk_sceneTools().checkCleanRenderLayers()
            self.ydRLSYSShaderClean()
            # Color
            self.ydRLCOCreate(key)
            # Ambient Occlusion
            self.ydRLAOCreate(key, shaderForece = shaderForece)
            # Back To MasterLayer
            mc.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
            # Normal
            self.ydRLNMCreate(key, shaderForece = shaderForece)
            # Back To MasterLayer
            mc.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
            # Light
            self.ydRLFNCreate(key, shaderForece = shaderForece)
            
            if mc.ls(key + '_CO'):
                # smoothSet
                #self.ydRLDoSmooth()
                # Back To MasterLayer
                mc.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
                # Unrender MasterLayer
                mc.setAttr("defaultRenderLayer.renderable", 0)
                # mc.setAttr
                # common Setting
                self.ydRLCommonConfig()
                # save
                self.ydRLSave(key,3)

            # IDP创建模式
            if RGB:
                # 道具只要BSR
                for idp in ['BSR']:
                    # 清理渲染层
                    sk_sceneTools.sk_sceneTools().checkCleanRenderLayers()
                    self.ydRLSYSShaderClean()
                    # 单层 
                    self.ydRLRGBCreate((key + '_' + idp), shaderForece = shaderForece)
                    if RGBCreatType:
                        if mc.ls(key + '_' + idp):
                            # Back To MasterLayer
                            mc.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
                            # Unrender MasterLayer
                            mc.setAttr("defaultRenderLayer.renderable", 0)
                            # common Setting
                            self.ydRLCommonConfig()
                            # save
                            self.ydRLSave(key,3,idp)
                if not RGBCreatType:
                    # 多层创建
                    if mc.ls(key + '_BSR'):
                        # Back To MasterLayer
                        mc.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
                        # Unrender MasterLayer
                        mc.setAttr("defaultRenderLayer.renderable", 0)
                        # mc.setAttr
                        # common Setting
                        self.ydRLCommonConfig()
                        # save
                        self.ydRLSave(key,3,'RGB')


        # Step 3：SET
        keyInfos = ['SETF','SETM','SETB']
        
        for key in keyInfos:
            # 清理渲染层
            sk_sceneTools.sk_sceneTools().checkCleanRenderLayers()
            self.ydRLSYSShaderClean()
            # Color
            self.ydRLCOCreate(key)
            # ZDepth
            self.ydRLZDEPTHCreate(key, shaderForece = shaderForece)
            # Back To MasterLayer
            mc.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
            # Normal
            self.ydRLNMCreate(key, shaderForece = shaderForece)
            # Back To MasterLayer
            mc.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
            # Light
            self.ydRLFNCreate(key, shaderForece = shaderForece)

            if mc.ls(key + '_CO'):
                # smoothSet
                #self.ydRLDoSmooth()
                # Back To MasterLayer
                mc.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
                # Unrender MasterLayer
                mc.setAttr("defaultRenderLayer.renderable", 0)
                # mc.setAttr
                # common Setting
                self.ydRLCommonConfig()
                # save
                self.ydRLSave( key ,3)

            if RGB:
                # 场景不要BSR
                for idp in ['FBR','SPR']:
                    # 清理渲染层
                    sk_sceneTools.sk_sceneTools().checkCleanRenderLayers()
                    self.ydRLSYSShaderClean()
                    # 单层 
                    self.ydRLRGBCreate((key + '_' + idp), shaderForece = shaderForece)
                    if RGBCreatType:
                        if mc.ls(key + '_' + idp):
                            # Back To MasterLayer
                            mc.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
                            # Unrender MasterLayer
                            mc.setAttr("defaultRenderLayer.renderable", 0)
                            # common Setting
                            self.ydRLCommonConfig()
                            # save
                            self.ydRLSave(key,3,idp)

        # Step 4：SPC
        keyInfos = ['SPCF','SPCM','SPCB']
        
        for key in keyInfos:
            # 清理渲染层
            sk_sceneTools.sk_sceneTools().checkCleanRenderLayers()
            self.ydRLSYSShaderClean()
            # Color
            self.ydRLCOCreate(key)
            # Ambient Occlusion
            self.ydRLAOCreate(key, shaderForece = shaderForece)
            # Back To MasterLayer
            mc.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
            # Normal
            self.ydRLNMCreate(key, shaderForece = shaderForece)
            # Back To MasterLayer
            mc.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
            # Light
            self.ydRLFNCreate(key, shaderForece = shaderForece)
            if mc.ls(key + '_CO'):
                # smoothSet
                #self.ydRLDoSmooth()
                # Back To MasterLayer
                mc.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
                # Unrender MasterLayer
                mc.setAttr("defaultRenderLayer.renderable", 0)
                # mc.setAttr
                # common Setting
                self.ydRLCommonConfig()
                # save
                self.ydRLSave(key,3)

            # IDP创建模式
            if RGB:
                for idp in idPass:
                    # 清理渲染层
                    sk_sceneTools.sk_sceneTools().checkCleanRenderLayers()
                    self.ydRLSYSShaderClean()
                    # 单层 
                    self.ydRLRGBCreate((key + '_' + idp), shaderForece = shaderForece)
                    # Back To MasterLayer
                    mc.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
                    if RGBCreatType:
                        if mc.ls(key + '_' + idp):
                            # Back To MasterLayer
                            mc.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
                            # Unrender MasterLayer
                            mc.setAttr("defaultRenderLayer.renderable", 0)
                            # common Setting
                            self.ydRLCommonConfig()
                            # save
                            self.ydRLSave(key,3,idp)
                if not RGBCreatType:
                    # 多层创建
                    if mc.ls(key + '_BSR'):
                        # Back To MasterLayer
                        mc.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
                        # Unrender MasterLayer
                        mc.setAttr("defaultRenderLayer.renderable", 0)
                        # mc.setAttr
                        # common Setting
                        self.ydRLCommonConfig()
                        # save
                        self.ydRLSave(key,3,'RGB')
        
        # Setp 5:SET_AO
        sk_sceneTools.sk_sceneTools().checkCleanRenderLayers()
        self.ydRLSYSShaderClean()
        
        keyInfos = ['SETF','SETM','SETB']
        
        for key in keyInfos:
            # Ambient Occlusion
            self.ydRLAOCreate(key, shaderForece = shaderForece)
            # Back To MasterLayer
            mc.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
            
        if (mc.ls('SETF_AO') + mc.ls('SETM_AO') + mc.ls('SETB_AO')):
            # smoothSet
            #self.ydRLDoSmooth()
            # Back To MasterLayer
            mc.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
            # Unrender MasterLayer
            mc.setAttr("defaultRenderLayer.renderable", 0)
            # mc.setAttr
            # common Setting
            self.ydRLCommonConfig()
            # save
            self.ydRLSave('SETAO',3,'')
            
            
        # Step 6：ENV
        # 清理渲染层
        sk_sceneTools.sk_sceneTools().checkCleanRenderLayers()
        self.ydRLSYSShaderClean()
        
        keyInfos = ['HILL','CLOUD','SKY']
        
        for key in keyInfos:
            # Color
            self.ydRLCOCreate(key)
            
        if (mc.ls('HILL_CO') + mc.ls('CLOUD_CO') + mc.ls('SKY_CO')):
            # smoothSet
            #self.ydRLDoSmooth()
            # Back To MasterLayer
            mc.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
            # Unrender MasterLayer
            mc.setAttr("defaultRenderLayer.renderable", 0)
            # mc.setAttr
            # common Setting
            self.ydRLCommonConfig()
            # 清理文件
            if mc.ls('HILL_CO'):
                rlHillObjs = mc.editRenderLayerMembers('HILL_CO',fullNames = 1 ,q = 1)
            else:
                rlHillObjs = []
            if not rlHillObjs:
                rlHillObjs = []
            if mc.ls('CLOUD_CO'):
                rlCloudObjs = mc.editRenderLayerMembers('CLOUD_CO',fullNames = 1 ,q = 1)
            else:
                rlCloudObjs = []
            if not rlCloudObjs:
                rlCloudObjs = []
            if mc.ls('SKY_CO'):
                rlSkyObjs = mc.editRenderLayerMembers('SKY_CO',fullNames = 1 ,q = 1)
            else:
                rlSkyObjs = []
            if not rlSkyObjs:
                rlSkyObjs = []
            rlENVGrps = rlHillObjs + rlCloudObjs + rlSkyObjs
            rlENVObjs = []
            if rlENVGrps:
                envMeshes = mc.listRelatives(rlENVGrps , ad =  1 , type = 'mesh' , f =  1)
                rlENVObjs = mc.listRelatives(envMeshes , p = 1 , type = 'transform' , f = 1)
                rlENVObjs = list(set(rlENVObjs))
            allMeshes = mc.ls(type = 'mesh',l = 1)
            if allMeshes:
                allObjs = mc.listRelatives(allMeshes , p = 1 , type = 'transform' , f = 1)
                allObjs = list(set(allObjs))
                for obj in allObjs:
                    if obj not in rlENVObjs:
                        if mc.ls(obj):
                            mc.delete(obj)
            # save
            self.ydRLSave('ENV',3)
            
        # 干掉base File
        import os
        os.remove(baseFileName)

        print '=======================!!!All Done!!!======================='
        print pathLocal.replace('D:','E:')
        print ('===========================================================')

    # Create Single Render Layer
    def ydRLSpeficCreate(self, renderLayer, saveMode='', selectMode=0, arnoldType=0 ,createMode = 1 , ui = 0):
        print (u'===============!!!Start 【%s】!!!===============' % (renderLayer))
        print 'Working...'

        from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools
        reload(sk_sceneTools)
        
        createName = ''
        
        if ui==1:
            result = mc.promptDialog(
                title=u'创建渲染层',
                message= renderLayer,
                button=['OK', 'Cancel'],
                defaultButton='OK',
                cancelButton='Cancel',
                dismissString='Cancel')
            if result == 'OK':
                createName = mc.promptDialog(query=True, text=True)            

        # Back To MasterLayer
        mc.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
        
        # 处理非参考的namespace
        #sk_sceneTools.sk_sceneTools().sk_sceneNoRefNamespaceClean()
        
        cacheFiles = mc.ls(type='cacheFile')
        # if cacheFiles:
        #    for cache in cacheFiles:
        #        mc.setAttr((cache + '.enable'),0)

        # clean Unknwon Nodes
        sk_sceneTools.sk_sceneTools().checkDonotNodeCleanBase(0)
        # renderpass Create
        # self.ydRLRenderPass()

        # common Setting
        self.ydRLCommonConfig()

        # arnold Setting
        if arnoldType:
            self.arnoldRendererSettings()

        # mr Setting
        self.mentalRayProductionLevel(createMode=createMode)
        # 指定层
        BGType = renderLayer.split('_')[0]
        layerType = renderLayer.split('_')[1]
        try:
            mc.delete(renderLayer)
        except:
            pass

        # 格式
        self.ydRLFramebuffer('iff',3,0)

        # COLOR
        if layerType == 'CO':
            if mc.ls(BGType + '_' + layerType):
                mc.delete(BGType + '_' + layerType)
            self.ydRLCOCreate(BGType, selectObjType=selectMode ,createMode=createMode , createName = createName)

        # Ambient Occlusion
        if layerType == 'AO':
            if mc.ls(BGType + '_' + layerType):
                mc.delete(BGType + '_' + layerType)
            if arnoldType == 0:
                self.ydRLAOCreate(BGType, selectObjType=selectMode,createMode=createMode, createName = createName)
            if arnoldType == 1:
                self.ydRLAOArnoldCreate(BGType, selectObjType=selectMode,createMode=createMode, createName = createName)
        # Normal
        if layerType == 'NM':
            if mc.ls(BGType + '_' + layerType):
                mc.delete(BGType + '_' + layerType)
            if arnoldType == 0:
                self.ydRLNMCreate(BGType, selectObjType=selectMode ,createMode=createMode, createName = createName)
            if arnoldType == 1:
                self.ydRLNMArnoldCreate(BGType, selectObjType=selectMode ,createMode=createMode, createName = createName)
        # Frenel
        if layerType == 'FN':
            if mc.ls(BGType + '_' + layerType):
                mc.delete(BGType + '_' + layerType)
            self.ydRLFNCreate(BGType, selectObjType=selectMode,createMode=createMode, createName = createName)
        # Zdepth
        if layerType == 'ZDP':
            if mc.ls(BGType + '_' + layerType):
                mc.delete(BGType + '_' + layerType)
            self.ydRLZDEPTHCreate(BGType, selectObjType=selectMode,createMode=createMode, createName = createName)
        # RGB
        if layerType in ['BSR','FBR','SPR']:
            if mc.ls(BGType + '_' + layerType):
                mc.delete(BGType + '_' + layerType)
            self.ydRLRGBCreate((BGType + '_' + layerType), selectObjType=selectMode)

        # smoothSet
        #self.ydRLDoSmooth()
        # Back To MasterLayer
        #mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')
        mc.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
        # UnRender MasterLayer
        mc.setAttr("defaultRenderLayer.renderable", 0)
        # camSetting
        if createMode:
            self.ydRLCamSetting(3)
        # common Setting
        # self.ydRLCommonConfig()

        if cacheFiles:
            for cache in cacheFiles:
                mc.setAttr((cache + '.enable'), 1)

        if saveMode:
            self.ydRLSave(saveMode)

        print (u'===============!!!Done  【%s】!!!===============' % ('renderLayer'))
        print '\n'


    # 处理export
    def ydExportTest(self):
        renderLayers = mc.ls(type = 'renderLayer')
        renderLayers.remove('defaultRenderLayer')
        
        mc.select(cl = 1)
        
        allNodes = []
        for renderLayer in renderLayers:
            mc.select(renderLayer,add = 1, ne = 1)
            layerNodes = mc.listConnections(renderLayer,d = 1)
            needNodes = []
            for node in layerNodes:
                needNodes.append(node)
            if not needNodes:
                continue
            layerNodes = list(set(needNodes))
            allNodes = allNodes + layerNodes
        if allNodes:
            mc.select(allNodes,add = 1 , ne = 1)
            
        needOther = mc.ls(materials = 1)
        if needOther:
            mc.select(needOther,ne = 1,add = 1)

    # 清理系统创建材质球
    def ydRLSYSShaderClean(self):
        shaderKeys = ['_AO_','_ASD_','_NM_','_FN_','_ZDP_','_BSR_','_FBR_','_SPR_','_Matte_']
        materialNodes = mc.ls(materials = 1)
        SGNodes = mc.ls(type = 'shadingEngine')
        needCheckNodes = materialNodes + SGNodes
        for node in needCheckNodes:
            for key in shaderKeys:
                if key in node and 'SHD_' in node:
                    mc.delete(node)
                    break

    #--------------------------------------------------------------------------------------------------------#
    #----------------------------------------------------------#
    # 【核心】 渲染设置
    #----------------------------------------------------------#
    # 渲染标准设置
    def ydRLCommonConfig(self , layerName = '' ,shotType = 3):
        print (u'===============!!!Start 【%s】!!!===============' % (u'标准设置'))
        print 'Working...'
        
        shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
        shot = ''
        if shotType == 2:
            shot = shotInfos[0] + '_' + shotInfos[1] + '_' + shotInfos[2]
        if shotType == 3:
            shot = shotInfos[0] + '_' + shotInfos[1] + '_' + shotInfos[2] + '_' + shotInfos[3] 
        
        # Camera
        from idmt.maya.commonCore.core_mayaCommon import sk_hbExportCam
        reload(sk_hbExportCam)
        # sk_hbExportCam.sk_hbExportCam().camServerReference(3)

        # 开启窗口，创建各种UI
        # mel.eval('unifiedRenderGlobalsWindow')

        # 标准设置
        mc.setAttr('defaultRenderQuality.edgeAntiAliasing', 1)
        mc.setAttr('defaultRenderGlobals.animation', 1)
        mc.setAttr('defaultRenderGlobals.outFormatControl', 0)
        mc.setAttr('defaultRenderGlobals.extensionPadding', 4)
        mc.setAttr('defaultResolution.width', 1280 )
        mc.setAttr('defaultResolution.height', 720)
        mc.setAttr('defaultResolution.deviceAspectRatio', 1.777)
        mc.setAttr('defaultResolution.pixelAspect', 1.00)
        mc.evalDeferred('import maya.cmds as mc\nmc.setAttr((\'defaultResolution.pixelAspect\'),1)', lowestPriority=1)
        mc.setAttr('defaultResolution.dotsPerInch', 72)
        mc.setAttr('defaultRenderQuality.edgeAntiAliasing', 1)
        
        if layerName == '':
            mc.setAttr('defaultRenderGlobals.imageFilePrefix', '<Layer>/<Scene>_<Layer>', type='string')
        else:
            mc.setAttr('defaultRenderGlobals.imageFilePrefix', (layerName + '/' + shot + '_' + layerName), type='string')
        
        # 开始处理
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
            mc.currentTime(startFrame)
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

        # 格式命名
        # 原先调用菜单，现在直接改节点
        '''
        mc.setAttr('defaultRenderGlobals.animation', 1)
        mc.setAttr('defaultRenderGlobals.putFrameBeforeExt', 1)
        mc.setAttr('defaultRenderGlobals.periodInExt', 1)
        mc.setAttr('defaultRenderGlobals.extensionPadding', 4)
        if mc.getAttr('defaultRenderGlobals.outFormatControl') == 1:
            mc.setAttr('defaultRenderGlobals.outFormatControl', 0)
        '''
        #self.ydRLFramebuffer('iff',16,0)

        # mel.eval("prefWndUnitsChanged \"time\";")
        # IKR强制开启
        mc.setAttr('defaultRenderGlobals.enableDefaultLight',1)
        mc.setAttr('defaultRenderGlobals.preMel',"cycleCheck -e off;ikSystem -e -sol 1;",type = 'string')
        print (u'===============!!!Done  【%s】!!!===============' % u'标准设置')
        print '\n'

    #--------------------------------#
    # mr 产品级设置
    def mentalRayProductionLevel(self,createMode = 1):
        print (u'===============!!!Start 【%s】!!!===============' % (u'MR设置'))
        print 'Working...'

        mc.setAttr('defaultRenderGlobals.imageFormat', 7)
        try:
            mel.eval('loadPlugin "Mayatomr"')
        except:
            pass
    #删除多余mr节点：        
#        mentalnodes=mc.ls(type='mentalrayItemsList')+mc.ls(type='mentalrayGlobals')+mc.ls(type='mentalrayOptions')
#        Delmen=[]
#        if mentalnodes:         
#            for node in mentalnodes:
#                if  mc.referenceQuery(node,inr=1)==0:
#                    Delmen.append(node)
#        if Delmen:            
#            try:
#                mc.delete(Delmen) 
#            except:
#                pass                                   
        # 开启窗口，创建各种UI，该死的MR，为啥不直接生成，非要延时。。
        # mel.eval('unifiedRenderGlobalsWindow')
        # 创建UI
        #mel.eval('mentalrayUI ""')
        
        # 创建miDefaultOptions节点
        mel.eval('miCreateDefaultNodes')

        mc.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')
        
        mc.setAttr('miDefaultOptions.miRenderUsing', 2)
        
        #mel.eval('zzjSetMentalrayQuality(\"production\"); ')

        # 读取之前创建的production_preset
        #mel.eval('nodePreset -load "miDefaultOptions" "production_mi"')

        # 删除天光，关闭FG
        mc.setAttr('miDefaultOptions.finalGather', 0)
        try:
            mel.eval('miDeleteSunSky')
        except:
            pass

        # exr
        # mc.editRenderLayerAdjustment('defaultRenderGlobals.imageFormat')
        
        mc.setAttr('miDefaultOptions.maxSamples', 2)
        mc.setAttr('miDefaultOptions.contrastR', 0.1)
        mc.setAttr('miDefaultOptions.contrastG', 0.1)
        mc.setAttr('miDefaultOptions.contrastB', 0.1)
        mc.setAttr('miDefaultOptions.contrastA', 0.1)
        
        if createMode:
            self.ydRLFramebuffer('iff',3,0)
        
        try:
            mc.setAttr('miDefaultOptions.minSamples', 0)
        except:
            pass
        
        # 过滤
        mc.setAttr('miDefaultOptions.filter', 2)
        mc.setAttr('miDefaultOptions.filterWidth', 1)
        mc.setAttr('miDefaultOptions.filterHeight', 1)
        
        mc.setAttr('miDefaultOptions.jitter', 1)
        mc.setAttr('miDefaultOptions.scanline', 1)
        mc.setAttr('miDefaultOptions.sampleLock', 0)
        
        mc.setAttr('miDefaultOptions.maxRefractionRays', 1)
        mc.setAttr('miDefaultOptions.maxReflectionRays', 1)
        mc.setAttr('miDefaultOptions.maxRayDepth', 2)
        mc.setAttr('miDefaultOptions.maxShadowRayDepth', 2)
        
        mc.setAttr('miDefaultOptions.rebuildShadowMaps', 0)

        # excel
        if createMode:
            shotData    = self.ydRLReadServerData()
            if shotData[5]:
                maxSamples  = int(shotData[5])
                if maxSamples:
                    print '---'
                    print maxSamples
                    mc.setAttr('miDefaultOptions.maxSamples', maxSamples)
            if shotData[6]:
                contrastData= float(shotData[6])
                if contrastData:
                    mc.setAttr('miDefaultOptions.contrastR', contrastData)
                    mc.setAttr('miDefaultOptions.contrastG', contrastData)
                    mc.setAttr('miDefaultOptions.contrastB', contrastData)
                    mc.setAttr('miDefaultOptions.contrastA', contrastData)

        print (u'===============!!!Done  【%s】!!!===============' % (u'MR设置'))
        print '\n'

        mc.setAttr('miDefaultOptions.miRenderUsing', 0)
        mc.setAttr('miDefaultOptions.miRenderUsing', 2) 
    #--------------------------------#
    # arnold 设置
    def arnoldRendererSettings(self):
        print (u'===============!!!Start 【%s】!!!===============' % (u'Arnold设置'))
        print 'Working...'

        mc.setAttr('defaultRenderGlobals.imageFormat', 7)
        try:
            mel.eval('loadPlugin "mtoa"')
        except:
            pass
        # 开启窗口，创建各种UI
        # mel.eval('unifiedRenderGlobalsWindow')
        mc.setAttr('defaultRenderGlobals.currentRenderer', 'arnold', type='string')
        # 下来所需的节点提前创建
        import mtoa
        mtoa.core.createOptions()
        import mtoa.cmds.registerArnoldRenderer
        mtoa.cmds.registerArnoldRenderer.registerArnoldRenderer()

        mc.setAttr('defaultArnoldDriver.halfPrecision', 1)
        mc.setAttr('defaultArnoldDriver.tiled', 0)
        mc.setAttr('defaultArnoldDriver.autocrop', 1)
        mc.setAttr('defaultArnoldRenderOptions.AASamples', 4)

        print (u'===============!!!Done  【%s】!!!===============' % (u'Arnold设置'))
        print '\n'

    #--------------------------------------------------------------------------------------------------------#
    #----------------------------------------------------------#
    # 【核心】renderpass系列
    #----------------------------------------------------------#

    #--------------------------------#
    # Create renderPass
    def ydRLRenderPass(self):
        print (u'===============!!!Start 【%s】!!!===============' % ('RenderPass'))
        print 'Working...'

        # shadow
        ex_rsShadow = mc.ls('shadow', type='renderPass')
        if ex_rsShadow:
            ex_rsShadow = 'shadow'
        else:
            renderPass = mc.shadingNode('renderPass', asRendering=1)
        configType = [1, 'SHD', 3, 256, 0, 1, 'Illumination', 1, 1, 0, 0, 0, 0, 1, 0, 10, 0, 10]
        self.ydRLRenderPassConfig(renderPass, configType)
        mc.rename(renderPass, 'shadow')
        print (u'===============!!!Done  【%s】!!!===============' % ('RenderPass'))
        print '\n'

    #--------------------------------#
    # 设置renderpass属性
    def ydRLRenderPassConfig(self, renderPass, configType):
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

    #--------------------------------#
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

    #--------------------------------------------------------------------------------------------------------#
    #----------------------------------------------------------#
    # 【核心】 物体分类|不通过ref方式判断
    # ZIP code
    #----------------------------------------------------------#
    def ydRLFramebuffer(self, fileType = 'iff',datatype=16 ,notmaster = 1):    
        mc.setAttr('defaultRenderGlobals.animation', 1)
        mc.setAttr('defaultRenderGlobals.putFrameBeforeExt', 1)
        mc.setAttr('defaultRenderGlobals.periodInExt', 1)
        mc.setAttr('defaultRenderGlobals.extensionPadding', 4)
        if mc.getAttr('defaultRenderGlobals.outFormatControl') == 1:
            mc.setAttr('defaultRenderGlobals.outFormatControl', 0)
        # tiff
        if fileType == 'tiff':
            if not notmaster:
                mc.editRenderLayerAdjustment('defaultRenderGlobals.imageFormat')
            mc.setAttr('defaultRenderGlobals.imageFormat', 3)
        # tiff16
        if fileType == 'tiff16':
            if not notmaster:
                mc.editRenderLayerAdjustment('defaultRenderGlobals.imageFormat')
            mc.setAttr('defaultRenderGlobals.imageFormat', 4)
        # exr
        if fileType == 'exr':
            if not notmaster:
                mc.editRenderLayerAdjustment('defaultRenderGlobals.imageFormat')
            mc.setAttr('defaultRenderGlobals.imageFormat', 51)
            mc.setAttr('defaultRenderGlobals.imfkey', 'exr', type='string')
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.setAttr('mentalrayGlobals.compressionQuality', 0)
            # 8 zip
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            if not notmaster:
                mc.editRenderLayerAdjustment('miDefaultFramebuffer.datatype')
            mc.setAttr('miDefaultFramebuffer.datatype', datatype)
        # iff
        if fileType == 'iff':
            if notmaster:
                mc.editRenderLayerAdjustment('defaultRenderGlobals.imageFormat')
            mc.setAttr('defaultRenderGlobals.imageFormat', 0)
            # 8 zip
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            if notmaster:
                mc.editRenderLayerAdjustment('miDefaultFramebuffer.datatype')
            mc.setAttr('miDefaultFramebuffer.datatype', datatype)

    #--------------------------------------------------------------------------------------------------------#
    #----------------------------------------------------------#
    # 【核心】 物体分类|不通过ref方式判断
    #----------------------------------------------------------#
    # 物体分类清单
    # import后不用参考时也可以处理
    # 使用条件：sk_sceneConfig.sk_sceneConfig().sk_sceneReorganize(0)
    # objType   1 根据大组判断  | 2 根据渲染层判断
    # nodeType  mesh 返回polygon的transform节点 | light 返回 light的transform节点
    # returnType 1 直接返回显示层所有包括子级有效物体 | 0 直接返回单独一级大组
    def ydRLObjectsTList(self, objType=1,  returnType = 1 ,nodeType = 'mesh',objs=[] ,update = 1 ):
        # 获取root
        from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools
        reload(sk_sceneTools)

        checkObjs = []

        refCHR = []
        refPRP = []
        refSET = []
        refSKY = []

        # 通过大组来判断
        if objType == 1:
            if mc.ls('CHR_GRP'):
                if mc.listRelatives('CHR_GRP', c=1, f=1, type='transform'):
                    refCHR = mc.listRelatives('CHR_GRP', c=1, f=1, type='transform')
            if mc.ls('PRP_GRP'):
                if mc.listRelatives('PRP_GRP', c=1, f=1, type='transform'):
                    refPRP = mc.listRelatives('PRP_GRP', c=1, f=1, type='transform')
            if mc.ls('SET_GRP'):
                if mc.listRelatives('SET_GRP', c=1, f=1, type='transform'):
                    refSET = mc.listRelatives('SET_GRP', c=1, f=1, type='transform')
            checkObjs = [refCHR , refPRP , refSET , refSKY]
                   
        # 通过显示层来判断 
        if objType == 2:
            refCHR_F = []
            if mc.ls('IDMTRL_F_CHR',type = 'renderLayer'):
                refCHR_F = mc.editRenderLayerMembers('IDMTRL_F_CHR',fullNames = 1 ,q = 1)
                if not refCHR_F:
                    refCHR_F = []
            refCHR_M = []
            if mc.ls('IDMTRL_M_CHR',type = 'renderLayer'):
                refCHR_M = mc.editRenderLayerMembers('IDMTRL_M_CHR',fullNames = 1 ,q = 1)
                if not refCHR_M:
                    refCHR_M = []
            refCHR_B = []
            if mc.ls('IDMTRL_B_CHR',type = 'renderLayer'):
                refCHR_B = mc.editRenderLayerMembers('IDMTRL_B_CHR',fullNames = 1 ,q = 1)
                if not refCHR_B:
                    refCHR_B = []
            refPRP_F = []
            if mc.ls('IDMTRL_F_PRP',type = 'renderLayer'):
                refPRP_F = mc.editRenderLayerMembers('IDMTRL_F_PRP',fullNames = 1 ,q = 1)
                if not refPRP_F:
                    refPRP_F = []
            refPRP_M = []
            if mc.ls('IDMTRL_M_PRP',type = 'renderLayer'):
                refPRP_M = mc.editRenderLayerMembers('IDMTRL_M_PRP',fullNames = 1 ,q = 1)
                if not refPRP_M:
                    refPRP_M = []
            refPRP_B = []
            if mc.ls('IDMTRL_B_PRP',type = 'renderLayer'):
                refPRP_B = mc.editRenderLayerMembers('IDMTRL_B_PRP',fullNames = 1 ,q = 1)
                if not refPRP_B:
                    refPRP_B = []
            refSET_F = []
            if mc.ls('IDMTRL_F_SET',type = 'renderLayer'):
                refSET_F = mc.editRenderLayerMembers('IDMTRL_F_SET',fullNames = 1 ,q = 1)
                if not refSET_F:
                    refSET_F = []
            refSET_M = []
            if mc.ls('IDMTRL_M_SET',type = 'renderLayer'):
                refSET_M = mc.editRenderLayerMembers('IDMTRL_M_SET',fullNames = 1 ,q = 1)
                if not refSET_M:
                    refSET_M = []
            refSET_B = []
            if mc.ls('IDMTRL_B_SET',type = 'renderLayer'):
                refSET_B = mc.editRenderLayerMembers('IDMTRL_B_SET',fullNames = 1 ,q = 1)
                if not refSET_B:
                    refSET_B = []
            refSPC_F = []
            if mc.ls('IDMTRL_F_SPC',type = 'renderLayer'):
                refSPC_F = mc.editRenderLayerMembers('IDMTRL_F_SPC',fullNames = 1 ,q = 1)
                if not refSPC_F:
                    refSPC_F = []
            refSPC_F_MSK = []
            if mc.ls('IDMTRL_F_SPC_MSK',type = 'renderLayer'):
                refSPC_F_MSK = mc.editRenderLayerMembers('IDMTRL_F_SPC_MSK',fullNames = 1 ,q = 1)
                if not refSPC_F_MSK:
                    refSPC_F_MSK = []
            refSPC_M = []
            if mc.ls('IDMTRL_M_SPC',type = 'renderLayer'):
                refSPC_M = mc.editRenderLayerMembers('IDMTRL_M_SPC',fullNames = 1 ,q = 1)
                if not refSPC_M:
                    refSPC_M = []
            refSPC_M_MSK = []
            if mc.ls('IDMTRL_M_SPC_MSK',type = 'renderLayer'):
                refSPC_M_MSK = mc.editRenderLayerMembers('IDMTRL_M_SPC_MSK',fullNames = 1 ,q = 1)
                if not refSPC_M_MSK:
                    refSPC_M_MSK = []
            refSPC_B = []
            if mc.ls('IDMTRL_B_SPC',type = 'renderLayer'):
                refSPC_B = mc.editRenderLayerMembers('IDMTRL_B_SPC',fullNames = 1 ,q = 1)
                if not refSPC_B:
                    refSPC_B = []
            refSPC_B_MSK = []
            if mc.ls('IDMTRL_B_SPC_MSK',type = 'renderLayer'):
                refSPC_B_MSK = mc.editRenderLayerMembers('IDMTRL_B_SPC_MSK',fullNames = 1 ,q = 1)
                if not refSPC_B_MSK:
                    refSPC_B_MSK = []
            refHILL = []
            if mc.ls('IDMTRL_HILL',type = 'renderLayer'):
                refHILL = mc.editRenderLayerMembers('IDMTRL_HILL',fullNames = 1 ,q = 1)
                if not refHILL:
                    refHILL = []
            refCLOUD = []
            if mc.ls('IDMTRL_CLOUD',type = 'renderLayer'):
                refCLOUD = mc.editRenderLayerMembers('IDMTRL_CLOUD',fullNames = 1 ,q = 1)
                if not refCLOUD:
                    refCLOUD = []
            refSKY = []
            if mc.ls('IDMTRL_SKY',type = 'renderLayer'):
                refSKY = mc.editRenderLayerMembers('IDMTRL_SKY',fullNames = 1 ,q = 1)
                if not refSKY:
                    refSKY = []

            checkObjs = [refCHR_F,refCHR_M,refCHR_B]
            checkObjs = checkObjs + [refPRP_F,refPRP_M,refPRP_B]
            checkObjs = checkObjs + [refSET_F,refSET_M,refSET_B]
            checkObjs = checkObjs + [refSPC_F,refSPC_M,refSPC_B]
            checkObjs = checkObjs + [refSPC_F_MSK,refSPC_M_MSK,refSPC_B_MSK]
            checkObjs = checkObjs + [refHILL,refCLOUD,refSKY]
        
        if returnType == 0:
            return checkObjs
        
        allRenderLayers = ['IDMTRL_F_CHR','IDMTRL_M_CHR','IDMTRL_B_CHR']
        allRenderLayers = allRenderLayers + ['IDMTRL_F_PRP','IDMTRL_M_PRP','IDMTRL_B_PRP']
        allRenderLayers = allRenderLayers + ['IDMTRL_F_SET','IDMTRL_M_SET','IDMTRL_B_SET']
        allRenderLayers = allRenderLayers + ['IDMTRL_F_SPC','IDMTRL_M_SPC','IDMTRL_B_SPC']
        allRenderLayers = allRenderLayers + ['IDMTRL_F_SPC_MSK','IDMTRL_M_SPC_MSK','IDMTRL_B_SPC_MSK']
        allRenderLayers = allRenderLayers + ['IDMTRL_HILL','IDMTRL_CLOUD','IDMTRL_SKY']

        for i in range(len(checkObjs)):
            # 只取mesh
            needInfo = []
            refGrps = checkObjs[i]
            if refGrps:
                needShapes = []
                shapes = mc.listRelatives(refGrps, ad=1, ni=1, type= nodeType, f=1)
                if not shapes:
                    continue
                # 只取有:MODEL标记的mesh
                for shape in shapes:
                    if nodeType == 'mesh':
                        # 非RIG组生效
                        if ':RIG|' not in shape or '|RIG|' in shape:
                            needShapes.append(shape)
                    else:
                        needShapes.append(shape)
                if needShapes:
                    if not mc.ls(allRenderLayers[i],type = 'renderLayer'):
                        continue
                    # 进入渲染层
                    mc.editRenderLayerGlobals(currentRenderLayer = allRenderLayers[i])
                    # 只有显示的物体才被加入渲染层
                    for shape in needShapes:
                        shapeGrp = mc.listRelatives(shape,ap = 1,type = 'transform',f = 1)
                        if len(shapeGrp) > 1:
                            for grp in shapeGrp:
                                vState = sk_sceneTools.sk_sceneTools().checkObjVState(grp)
                                if vState:
                                    needInfo.append(grp)
                        else:
                            shapeGrp = shapeGrp[0]
                            vState = sk_sceneTools.sk_sceneTools().checkObjVState(shapeGrp)
                            if vState:
                                needInfo.append(shapeGrp)
                        
            if needInfo:
                needInfo = list(set(needInfo))
            checkObjs[i] = needInfo
            
        # Back To MasterLayer
        mc.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
        
        result = []
        
        if objType == 1:
            result = checkObjs

        if objType == 2:
            result = checkObjs
            if update:
                # 本地及服务器端路径
                shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
                localPath = sk_infoConfig.sk_infoConfig().checkLocalInfoPath()
                serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
                localTransPath = localPath + 'renderLayerInfos/' + shotInfo[0] + '/' + str(shotInfo[1]) + '/' + str(shotInfo[2]) + '/' + str(shotInfo[3]) + '/'
                mc.sysFile(localTransPath ,makeDir = 1)
                serverTransPath = serverPath + 'data/renderLayerInfos/' + shotInfo[0] + '/' + str(shotInfo[1]) + '/' + str(shotInfo[2]) + '/' + str(shotInfo[3]) + '/'
                makeDirCMD = 'zwSysFile(\"MD\",\"' + serverTransPath + '\",\"\",1)'
                mel.eval(makeDirCMD)
                
                # 本地输出及更新
                keyInfos = ['CHRF','CHRM','CHRB','PRPF','PRPM','PRPB','SETF','SETM','SETB','SPCF','SPCM','SPCB','SPCMSKF','SPCMSKM','SPCMSKB','HILL','CLOUD','SKY']
                
                for i in range(len(keyInfos)):
                    print u'---[%s] start---'%(keyInfos[i])
                    sk_infoConfig.sk_infoConfig().checkFileWrite((localTransPath + nodeType +'_' +  keyInfos[i] + '.txt'), checkObjs[i])
                    updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localTransPath + nodeType +'_' +  keyInfos[i] + '.txt') + '"' + ' ' + '"' + (serverTransPath + nodeType +'_' +  keyInfos[i] + '.txt') + '"' + ' true'
                    mel.eval(updateAnimCMD)
                    print u'---[%s] done ---'%(keyInfos[i])
                
                print u'------------[分类信息] [%s] Done------------'%(nodeType)

            '''
            # CHR
            result.append([checkObjs[0],checkObjs[1],checkObjs[2]])
            # PRP
            result.append([checkObjs[3],checkObjs[4],checkObjs[5]])
            # SET
            result.append([checkObjs[6],checkObjs[7],checkObjs[8]])
            # SPC
            result.append([checkObjs[9],checkObjs[10],checkObjs[11]])
            # SPCMSK
            result.append([checkObjs[12],checkObjs[13],checkObjs[14]])
            # OTHER
            result.append([checkObjs[15],checkObjs[16],checkObjs[17]])
            '''
        return result

    #----------------------------------------------------------#
    # 【核心】渲染层物体信息处理，对层数特别多的情况处理
    #　layerType　　CHRF之类
    # renderLayer FBR,FN之类
    # FBR | SPR 的类型，都是mesh
    def ydRLObjsInfo(self,layerType,renderLayer):
        # 物体
        #objs = self.ydRLObjectsTList(2,1,'mesh',[])
        #objs = []
        # 读取
        # 本地及服务器端路径
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        serverTransPath = serverPath + 'data/renderLayerInfos/' + shotInfo[0] + '/' + str(shotInfo[1]) + '/' + str(shotInfo[2]) + '/' + str(shotInfo[3]) + '/'
        
        try:
            refCHR_F = sk_infoConfig.sk_infoConfig().checkFileRead(serverTransPath + 'mesh' +'_' +  'CHRF' + '.txt')
            refCHR_M = sk_infoConfig.sk_infoConfig().checkFileRead(serverTransPath + 'mesh' +'_' +  'CHRM' + '.txt')
            refCHR_B = sk_infoConfig.sk_infoConfig().checkFileRead(serverTransPath + 'mesh' +'_' +  'CHRB' + '.txt')
            refPRP_F = sk_infoConfig.sk_infoConfig().checkFileRead(serverTransPath + 'mesh' +'_' +  'PRPF' + '.txt')
            refPRP_M = sk_infoConfig.sk_infoConfig().checkFileRead(serverTransPath + 'mesh' +'_' +  'PRPM' + '.txt')
            refPRP_B = sk_infoConfig.sk_infoConfig().checkFileRead(serverTransPath + 'mesh' +'_' +  'PRPB' + '.txt')
            refSET_F = sk_infoConfig.sk_infoConfig().checkFileRead(serverTransPath + 'mesh' +'_' +  'SETF' + '.txt')
            refSET_M = sk_infoConfig.sk_infoConfig().checkFileRead(serverTransPath + 'mesh' +'_' +  'SETM' + '.txt')
            refSET_B = sk_infoConfig.sk_infoConfig().checkFileRead(serverTransPath + 'mesh' +'_' +  'SETB' + '.txt')
            refSPC_F = sk_infoConfig.sk_infoConfig().checkFileRead(serverTransPath + 'mesh' +'_' +  'SPCF' + '.txt')
            refSPC_M = sk_infoConfig.sk_infoConfig().checkFileRead(serverTransPath + 'mesh' +'_' +  'SPCM' + '.txt')
            refSPC_B = sk_infoConfig.sk_infoConfig().checkFileRead(serverTransPath + 'mesh' +'_' +  'SPCB' + '.txt')
            refSPC_F_MSK = sk_infoConfig.sk_infoConfig().checkFileRead(serverTransPath + 'mesh' +'_' +  'SPCMSKF' + '.txt')
            refSPC_M_MSK = sk_infoConfig.sk_infoConfig().checkFileRead(serverTransPath + 'mesh' +'_' +  'SPCMSKM' + '.txt')
            refSPC_B_MSK = sk_infoConfig.sk_infoConfig().checkFileRead(serverTransPath + 'mesh' +'_' +  'SPCMSKB' + '.txt')
            refHILL  = sk_infoConfig.sk_infoConfig().checkFileRead(serverTransPath + 'mesh' +'_' +  'HILL' + '.txt')
            refCLOUD = sk_infoConfig.sk_infoConfig().checkFileRead(serverTransPath + 'mesh' +'_' +  'CLOUD' + '.txt')
            refSKY   = sk_infoConfig.sk_infoConfig().checkFileRead(serverTransPath + 'mesh' +'_' +  'SKY' + '.txt')
            
            refCHR_F_lt = sk_infoConfig.sk_infoConfig().checkFileRead(serverTransPath + 'light' +'_' +  'CHRF' + '.txt')
            refCHR_M_lt = sk_infoConfig.sk_infoConfig().checkFileRead(serverTransPath + 'light' +'_' +  'CHRM' + '.txt')
            refCHR_B_lt = sk_infoConfig.sk_infoConfig().checkFileRead(serverTransPath + 'light' +'_' +  'CHRB' + '.txt')
            refPRP_F_lt = sk_infoConfig.sk_infoConfig().checkFileRead(serverTransPath + 'light' +'_' +  'PRPF' + '.txt')
            refPRP_M_lt = sk_infoConfig.sk_infoConfig().checkFileRead(serverTransPath + 'light' +'_' +  'PRPM' + '.txt')
            refPRP_B_lt = sk_infoConfig.sk_infoConfig().checkFileRead(serverTransPath + 'light' +'_' +  'PRPB' + '.txt')
            refSET_F_lt = sk_infoConfig.sk_infoConfig().checkFileRead(serverTransPath + 'light' +'_' +  'SETF' + '.txt')
            refSET_M_lt = sk_infoConfig.sk_infoConfig().checkFileRead(serverTransPath + 'light' +'_' +  'SETM' + '.txt')
            refSET_B_lt = sk_infoConfig.sk_infoConfig().checkFileRead(serverTransPath + 'light' +'_' +  'SETB' + '.txt')
            refSPC_F_lt = sk_infoConfig.sk_infoConfig().checkFileRead(serverTransPath + 'light' +'_' +  'SPCF' + '.txt')
            refSPC_M_lt = sk_infoConfig.sk_infoConfig().checkFileRead(serverTransPath + 'light' +'_' +  'SPCM' + '.txt')
            refSPC_B_lt = sk_infoConfig.sk_infoConfig().checkFileRead(serverTransPath + 'light' +'_' +  'SPCB' + '.txt')
            refHILL_lt  = sk_infoConfig.sk_infoConfig().checkFileRead(serverTransPath + 'light' +'_' +  'HILL' + '.txt')
            refCLOUD_lt = sk_infoConfig.sk_infoConfig().checkFileRead(serverTransPath + 'light' +'_' +  'CLOUD' + '.txt')
            refSKY_lt   = sk_infoConfig.sk_infoConfig().checkFileRead(serverTransPath + 'light' +'_' +  'SKY' + '.txt')
        except:
            print u'===本镜头没有导出分层信息，请重新输出==='
            mc.error(u'===本镜头没有导出分层信息，请重新输出===')
        
        refCHR   = refCHR_F + refCHR_M + refCHR_B
        refPRP   = refPRP_F + refPRP_M + refPRP_B
        refSET   = refSET_F + refSET_M + refSET_B
        refSPC   = refSPC_F + refSPC_M + refSPC_B
        refEnv   = refHILL  + refCLOUD + refSKY
        
        # RGB提前支取
        FBRKey = 'FullBody'
        FBRInfos = self.ydRLayerRGBObjectsConfig(FBRKey)
        SPRKey = 'ShortParts'
        SPRInfos = self.ydRLayerRGBObjectsConfig(SPRKey)
        
        # 物体
        rlObjs = []
        MaskObjs = []
        rlLights = []
        layerObjs = []
        layerName =''
        if layerType == 'CHRF':
            tempObjs    = refCHR + refPRP + refSET 
            if renderLayer in ['NM','FN','BSR']:
                tempObjs = refCHR_F
            if tempObjs:
                for obj in tempObjs:
                    if obj not in refSPC:
                        rlObjs.append(obj)
        
            MaskObjs  = refPRP + refSET + refCHR_M + refCHR_B
            layerObjs = refCHR_F
            # CHR的BSR剔除PRP,2014.8.6
            if renderLayer in ['BSR']:
                #MaskObjs = [ ( refPRP + refSET + refCHR_M + refCHR_B) , [] , [] ]
                MaskObjs = [ ( refSET + refCHR_M + refCHR_B) , [] , [] ]
                if layerObjs:
                    # layerObjs=  refCHR_F + refPRP + refSET + refCHR_M + refCHR_B
                    layerObjs=  refCHR_F + refSET + refCHR_M + refCHR_B
            if renderLayer in ['FBR']:
                RGBMObjs = self.ydRLRGBObjsInfoConfig(FBRInfos , refCHR_F , refSPC )
                rlObjs   = RGBMObjs[0]
                MaskObjs = RGBMObjs[1:]
            if renderLayer in ['SPR']:
                RGBMObjs = self.ydRLRGBObjsInfoConfig(SPRInfos , refCHR_F , refSPC )
                rlObjs   = RGBMObjs[0]
                MaskObjs = RGBMObjs[1:]

            rlLights  = refCHR_F_lt
            layerName = 'CHRF_' + renderLayer
            
        if layerType == 'CHRM':
            tempObjs    = refCHR + refPRP + refSET 
            if renderLayer in ['NM','FN','BSR']:
                tempObjs = refCHR_M
            if tempObjs:
                for obj in tempObjs:
                    if obj not in refSPC:
                        rlObjs.append(obj)

            MaskObjs  = refPRP + refSET + refCHR_F + refCHR_B
            layerObjs = refCHR_M
            # CHR的BSR剔除PRP,2014.8.6
            # CHRB剔除CHRF和CHRM,2014.8.6
            if renderLayer in ['BSR']:
                #MaskObjs = [(refPRP + refSET + refCHR_B + refCHR_F ),[],[]]
                MaskObjs = [(refSET + refCHR_B),[],[]]
                if layerObjs:
                    #layerObjs= refCHR_M  + refPRP + refSET  + refCHR_B + refCHR_F
                    layerObjs= refCHR_M + refSET  + refCHR_B
            if renderLayer in ['FBR']:
                RGBMObjs = self.ydRLRGBObjsInfoConfig(FBRInfos , refCHR_M , refSPC )
                #return [refCHR_M,RGBMObjs]
                rlObjs   = RGBMObjs[0]
                MaskObjs = RGBMObjs[1:]
            if renderLayer in ['SPR']:
                RGBMObjs = self.ydRLRGBObjsInfoConfig(SPRInfos , refCHR_M , refSPC )
                rlObjs   = RGBMObjs[0]
                MaskObjs = RGBMObjs[1:]
                
            rlLights  = refCHR_M_lt
            layerName = 'CHRM_' + renderLayer
            
        if layerType == 'CHRB':
            tempObjs    = refCHR + refPRP + refSET
            if renderLayer in ['NM','FN','BSR']:
                tempObjs = refCHR_B
            if tempObjs:
                for obj in tempObjs:
                    if obj not in refSPC:
                        rlObjs.append(obj)
                
            MaskObjs  = refPRP + refSET + refCHR_F + refCHR_M
            layerObjs = refCHR_B
            # CHR的BSR剔除PRP,2014.8.6
            # CHRB剔除CHRF和CHRM,2014.8.6
            if renderLayer in ['BSR']:
                #MaskObjs = [(refPRP + refSET + refCHR_F + refCHR_M),[],[]]
                MaskObjs = [(refSET),[],[]]
                if layerObjs:
                    #layerObjs = refCHR_B + refPRP + refSET + refCHR_F + refCHR_M
                    layerObjs = refCHR_B + refSET
            if renderLayer in ['FBR']:
                RGBMObjs = self.ydRLRGBObjsInfoConfig(FBRInfos , refCHR_B , refSPC )
                rlObjs   = RGBMObjs[0]
                MaskObjs = RGBMObjs[1:]
            if renderLayer in ['SPR']:
                RGBMObjs = self.ydRLRGBObjsInfoConfig(SPRInfos , refCHR_B , refSPC )
                rlObjs   = RGBMObjs[0]
                MaskObjs = RGBMObjs[1:]

            rlLights  = refCHR_B_lt
            layerName = 'CHRB_' + renderLayer
            
        if layerType == 'PRPF':
            tempObjs    = refPRP + refCHR + refSET
            if renderLayer in ['NM','FN','BSR']:
                tempObjs = refPRP_F
            if tempObjs:
                for obj in tempObjs:
                    if obj not in refSPC:
                        rlObjs.append(obj)

            MaskObjs  = refCHR + refSET + refPRP_M + refPRP_B
            layerObjs = refPRP_F
            # PRP的BSR剔除CHR,2014.8.6
            if renderLayer in ['BSR']:
                #MaskObjs = [(refCHR + refSET + refPRP_M + refPRP_B),[],[]]
                MaskObjs = [(refSET + refPRP_M + refPRP_B),[],[]]
                if layerObjs:
                    #layerObjs = refPRP_F + refCHR + refSET + refPRP_M + refPRP_B
                    layerObjs = refPRP_F + refSET + refPRP_M + refPRP_B
            if renderLayer in ['FBR']:
                RGBMObjs = self.ydRLRGBObjsInfoConfig(FBRInfos , refPRP_F , refSPC )
                rlObjs   = RGBMObjs[0]
                MaskObjs = RGBMObjs[1:]
            if renderLayer in ['SPR']:
                RGBMObjs = self.ydRLRGBObjsInfoConfig(SPRInfos , refPRP_F , refSPC )
                rlObjs   = RGBMObjs[0]
                MaskObjs = RGBMObjs[1:]
                
            rlLights  = refPRP_F_lt
            layerName = 'PRPF_' + renderLayer
            
        if layerType == 'PRPM':
            tempObjs    = refPRP + refCHR + refSET
            if renderLayer in ['NM','FN','BSR']:
                tempObjs = refPRP_M
            if tempObjs:
                for obj in tempObjs:
                    if obj not in refSPC:
                        rlObjs.append(obj)

            MaskObjs  = refCHR + refSET + refPRP_F + refPRP_B
            layerObjs = refPRP_M
            # PRP的BSR剔除CHR,2014.8.6
            if renderLayer in ['BSR']:
                #MaskObjs = [(refCHR + refSET + refPRP_F + refPRP_B),[],[]]
                MaskObjs = [(refSET + refPRP_F + refPRP_B),[],[]]
                if layerObjs:
                    #layerObjs = refPRP_M + refCHR + refSET + refPRP_F + refPRP_B
                    layerObjs = refPRP_M + refSET + refPRP_F + refPRP_B
            if renderLayer in ['FBR']:
                RGBMObjs = self.ydRLRGBObjsInfoConfig(FBRInfos , refPRP_M , refSPC )
                rlObjs   = RGBMObjs[0]
                MaskObjs = RGBMObjs[1:]
            if renderLayer in ['SPR']:
                RGBMObjs = self.ydRLRGBObjsInfoConfig(SPRInfos , refPRP_M , refSPC )
                rlObjs   = RGBMObjs[0]
                MaskObjs = RGBMObjs[1:]
                
            rlLights  = refPRP_M_lt
            layerName = 'PRPM_' + renderLayer
            
        if layerType == 'PRPB':
            tempObjs    = refPRP + refCHR + refSET
            if renderLayer in ['NM','FN','BSR']:
                tempObjs = refPRP_B
            if tempObjs:
                for obj in tempObjs:
                    if obj not in refSPC:
                        rlObjs.append(obj)

            MaskObjs  = refCHR + refSET + refPRP_F + refPRP_M
            layerObjs = refPRP_B
            # PRP的BSR剔除CHR,2014.8.6
            if renderLayer in ['BSR']:
                #MaskObjs = [(refCHR + refSET + refPRP_F + refPRP_M),[],[]]
                MaskObjs = [(refSET + refPRP_F + refPRP_M),[],[]]
                if layerObjs:
                    #layerObjs = refPRP_B + refCHR + refSET + refPRP_F + refPRP_M
                    layerObjs = refPRP_B + refSET + refPRP_F + refPRP_M
            if renderLayer in ['FBR']:
                RGBMObjs = self.ydRLRGBObjsInfoConfig(FBRInfos , refPRP_B , refSPC )
                rlObjs   = RGBMObjs[0]
                MaskObjs = RGBMObjs[1:]
            if renderLayer in ['SPR']:
                RGBMObjs = self.ydRLRGBObjsInfoConfig(SPRInfos , refPRP_B , refSPC )
                rlObjs   = RGBMObjs[0]
                MaskObjs = RGBMObjs[1:]
                        
            rlLights  = refPRP_B_lt
            layerName = 'PRPB_' + renderLayer
            
        if layerType == 'SETF':
            rlObjs    = refSET + refCHR + refPRP + refSPC
            if renderLayer in ['NM','FN','ZDEPTH','BSR']:
                rlObjs = []
                tempObjs = refSET_F
                if tempObjs:
                    for obj in tempObjs:
                        if obj not in refSPC:
                            rlObjs.append(obj)

            tempObjs  = refCHR + refPRP + refSPC + refSET_M + refSET_B
            if tempObjs:
                for obj in tempObjs:
                    if obj not in refSET_F:
                        MaskObjs.append(obj)
            layerObjs = refSET_F
            if renderLayer in ['BSR']:
                MaskObjs = [MaskObjs,[],[]]
                if layerObjs:
                    layerObjs = refSET_F + refCHR + refPRP + refSPC + refSET_M + refSET_B
            if renderLayer in ['FBR']:
                RGBMObjs = self.ydRLRGBObjsInfoConfig(FBRInfos , refSET_F , [] )
                rlObjs   = RGBMObjs[0]
                MaskObjs = RGBMObjs[1:]
            if renderLayer in ['SPR']:
                RGBMObjs = self.ydRLRGBObjsInfoConfig(SPRInfos , refSET_F , [] )
                rlObjs   = RGBMObjs[0]
                MaskObjs = RGBMObjs[1:]
            
            rlLights  = refSET_F_lt
            layerName = 'SETF_' + renderLayer  
            
        if layerType == 'SETM':
            rlObjs    = refSET + refCHR + refPRP + refSPC
            if renderLayer in ['NM','FN','ZDEPTH','BSR']:
                rlObjs = []
                tempObjs = refSET_M
                if tempObjs:
                    for obj in tempObjs:
                        if obj not in refSPC:
                            rlObjs.append(obj)
                
            tempObjs  = refCHR + refPRP + refSPC + refSET_F + refSET_B
            if tempObjs:
                for obj in tempObjs:
                    if obj not in refSET_M:
                        MaskObjs.append(obj)
            layerObjs = refSET_M
            if renderLayer in ['BSR']:
                MaskObjs = [MaskObjs,[],[]]
                if layerObjs:
                    layerObjs = refSET_F + refCHR + refPRP + refSPC  + refSET_F + refSET_M
            if renderLayer in ['FBR']:
                RGBMObjs = self.ydRLRGBObjsInfoConfig(FBRInfos , refSET_M , [] )
                rlObjs   = RGBMObjs[0]
                MaskObjs = RGBMObjs[1:]
            if renderLayer in ['SPR']:
                RGBMObjs = self.ydRLRGBObjsInfoConfig(SPRInfos , refSET_M , [] )
                rlObjs   = RGBMObjs[0]
                MaskObjs = RGBMObjs[1:]
            
            rlLights  = refSET_M_lt

            layerName = 'SETM_' + renderLayer 
            
        if layerType == 'SETB':
            rlObjs    = refSET + refCHR + refPRP + refSPC
            if renderLayer in ['NM','FN','ZDEPTH','BSR']:
                rlObjs = []
                tempObjs = refSET_B
                if tempObjs:
                    for obj in tempObjs:
                        if obj not in refSPC:
                            rlObjs.append(obj)

            tempObjs  = refCHR + refPRP + refSPC  + refSET_F + refSET_M
            if tempObjs:
                for obj in tempObjs:
                    if obj not in refSET_B:
                        MaskObjs.append(obj)
            layerObjs = refSET_B
            if renderLayer in ['BSR']:
                MaskObjs = [MaskObjs,[],[]]
                if layerObjs:
                    layerObjs = refSET_B + refCHR + refPRP + refSPC  + refSET_F + refSET_M
            if renderLayer in ['FBR']:
                RGBMObjs = self.ydRLRGBObjsInfoConfig(FBRInfos , refSET_B , [] )
                rlObjs   = RGBMObjs[0]
                MaskObjs = RGBMObjs[1:]
            if renderLayer in ['SPR']:
                RGBMObjs = self.ydRLRGBObjsInfoConfig(SPRInfos , refSET_B , [] )
                rlObjs   = RGBMObjs[0]
                MaskObjs = RGBMObjs[1:]
            
            rlLights  = refSET_B_lt
            layerName = 'SETB_' + renderLayer

        if layerType == 'SPCF':
            rlObjs    = refSPC_F + refSPC_F_MSK
            MaskObjs  = refSPC_F_MSK
            layerObjs = refSPC_F
            if renderLayer in ['NM','FN','BSR']:
                rlObjs = refSPC_F
                MaskObjs = []
            if renderLayer in ['BSR']:
                MaskObjs = [MaskObjs,[],[]]
                if layerObjs:
                    layerObjs = refSPC_F + refSPC_F_MSK
            # SPC只需要BSR
            if renderLayer in ['FBR']:
                #RGBMObjs = self.ydRLRGBObjsInfoConfig(FBRInfos , refSPC_F , [] )
                rlObjs   = []
                MaskObjs = [[],[],[]]
            if renderLayer in ['SPR']:
                #RGBMObjs = self.ydRLRGBObjsInfoConfig(SPRInfos , refSPC_F , [] )
                rlObjs   = []
                MaskObjs = [[],[],[]]

            rlLights  = refSPC_F_lt
            layerName = 'SPCF_' + renderLayer
            
        if layerType == 'SPCM':
            rlObjs    = refSPC_M + refSPC_M_MSK
            MaskObjs  = refSPC_M_MSK
            layerObjs = refSPC_M
            if renderLayer in ['NM','FN','BSR']:
                rlObjs = refSPC_M
                MaskObjs = []
            if renderLayer in ['BSR']:
                MaskObjs = [MaskObjs,[],[]]
                if layerObjs:
                    layerObjs = refSPC_M + refSPC_M_MSK
            # SPC只需要BSR
            if renderLayer in ['FBR']:
                #RGBMObjs = self.ydRLRGBObjsInfoConfig(FBRInfos , refSPC_M , [] )
                rlObjs   = []
                MaskObjs = [[],[],[]]
            if renderLayer in ['SPR']:
                #RGBMObjs = self.ydRLRGBObjsInfoConfig(SPRInfos , refSPC_M , [] )
                rlObjs   = []
                MaskObjs = [[],[],[]]
            rlLights  = refSPC_M_lt
            layerName = 'SPCM_' + renderLayer
            
        if layerType == 'SPCB':
            rlObjs    = refSPC_B + refSPC_B_MSK
            MaskObjs  = refSPC_B_MSK
            layerObjs = refSPC_B
            if renderLayer in ['NM','FN','BSR']:
                rlObjs = refSPC_B
                MaskObjs = []
            if renderLayer in ['BSR']:
                MaskObjs = [MaskObjs,[],[]]
                if layerObjs:
                    layerObjs = refSPC_B + refSPC_B_MSK
            # SPC只需要BSR
            if renderLayer in ['FBR']:
                #RGBMObjs = self.ydRLRGBObjsInfoConfig(FBRInfos , refSPC_b , [] )
                rlObjs   = []
                MaskObjs = [[],[],[]]
            if renderLayer in ['SPR']:
                #RGBMObjs = self.ydRLRGBObjsInfoConfig(SPRInfos , refSPC_b , [] )
                rlObjs   = []
                MaskObjs = [[],[],[]]
            rlLights  = refSPC_B_lt
            layerName = 'SPCB_' + renderLayer

        if layerType == 'HILL':
            rlObjs    = refHILL
            MaskObjs  = []
            rlLights  = self.ydRLEnvLightCreate()
            layerObjs = refHILL
            layerName = 'HILL_' + renderLayer
            
        if layerType == 'CLOUD':
            rlObjs    = refCLOUD 
            MaskObjs  = []
            rlLights  = self.ydRLEnvLightCreate()
            layerObjs = refCLOUD
            layerName = 'CLOUD_' + renderLayer
            
        if layerType == 'SKY':
            rlObjs    = refSKY 
            MaskObjs  = []
            rlLights  = self.ydRLEnvLightCreate()
            layerObjs = refSKY
            layerName = 'SKY_' + renderLayer
            
        SGConfig  = self.ydRLObjsSGNodesGet(rlObjs)   
        if not SGConfig:
            SGConfig = [] 
        
        if rlObjs:
            rlObjs = list(set(rlObjs))
        
        if MaskObjs:
            if renderLayer in ['BSR','FBR','SPR']:
                temp = []
                for info in MaskObjs:
                    if info:
                        info = list(set(info))
                        temp.append(info)
                    else:
                        temp.append([])
                MaskObjs = temp
            else:       
                MaskObjs = list(set(MaskObjs))
                
        if layerObjs:
            layerObjs = list(set(layerObjs))
            
        result = []
        result.append(rlObjs)
        result.append(MaskObjs)
        result.append(layerName)
        result.append(SGConfig)
        result.append(rlLights)
        result.append(layerObjs)
        print u'===Obj Info Done==='
        return result

    #----------------------------------------------------------#
    # 【核心】补充：处理RGB信息甄别
    def ydRLRGBObjsInfoConfig(self, allInfos , inObjs =  [] , outObjs = [] ):
        colorInfos = allInfos[0]
        meshInfos = allInfos[1]

        if not allInfos or not inObjs:
            return [[],[],[],[]]

        RObjs = []
        GObjs = []
        BObjs = []
        MObjs = []
        
        #　甄别类别
        for i in range(len(colorInfos)):
            if colorInfos[i][0] or colorInfos[i][1] or colorInfos[i][2]:
                # R
                if colorInfos[i][0] == 1:
                    RObjs = RObjs + self.ydRLCheckInfoObjs(meshInfos[i] , inObjs ,outObjs )
                # G
                if colorInfos[i][1] == 1:
                    GObjs = GObjs + self.ydRLCheckInfoObjs(meshInfos[i] , inObjs ,outObjs )
                # B
                if colorInfos[i][2] == 1:
                    BObjs = BObjs + self.ydRLCheckInfoObjs(meshInfos[i] , inObjs ,outObjs )
            # M
            else:
                MObjs = MObjs + self.ydRLCheckInfoObjs(meshInfos[i] , inObjs ,outObjs )

        return [RObjs,GObjs,BObjs,MObjs]
    
    #----------------------------------------------------------#
    # 【核心】补充：处理RGB信息甄别II
    def ydRLCheckInfoObjs(self,checkMeshes , inObjs , outObjs):
        tempMeshes = checkMeshes
        needMeshes = []
        if tempMeshes:
            for mesh in tempMeshes:
                if not mc.ls(mesh):
                    continue
                checkMesh = ''
                if '.f[' not in mesh:
                    obj = mc.listRelatives(mesh,p = 1 ,type = 'transform' , f = 1)
                    if not obj:
                        continue
                    obj = obj[0]
                else:
                    mes = mesh.split('.f[')[0]
                    obj = mc.listRelatives(mes,p = 1 ,type = 'transform' , f = 1)
                    if not obj:
                        continue
                    obj = obj[0]
                if outObjs:
                    if mc.objExists(obj) and obj not in outObjs:
                        checkMesh = mesh
                else:
                    if mc.objExists(obj) :
                        checkMesh = mesh
                        
                # 处理mesh
                if checkMesh:
                    if '.f[' in checkMesh:
                        faceNum = mc.polyEvaluate(checkMesh.split('.f[')[0], face=1)
                        print (checkMesh.split('.f[')[0] + '.f[0:' + str(faceNum - 1) + ']')
                        if checkMesh == (checkMesh.split('.f[')[0] + '.f[0:' + str(faceNum - 1) + ']'):
                            shape = mc.listRelatives(checkMesh.split('.f[')[0],s = 1,ni = 1, type = 'mesh',f = 1)[0]
                            needMeshes.append(shape)
                        else:
                            needMeshes.append(checkMesh)
                    else:
                        needMeshes.append(checkMesh)
        return needMeshes

    #----------------------------------------------------------#
    # 【核心】补充：所有显示层创建
    def ydRLObjsTypesCreate(self):
        typeLayers = ['IDMTRL_F_CHR','IDMTRL_M_CHR','IDMTRL_B_CHR']
        typeLayers = typeLayers + ['IDMTRL_F_PRP','IDMTRL_M_PRP','IDMTRL_B_PRP']
        typeLayers = typeLayers + ['IDMTRL_F_SET','IDMTRL_M_SET','IDMTRL_B_SET']
        typeLayers = typeLayers + ['IDMTRL_F_SPC','IDMTRL_F_SPC_MSK','IDMTRL_M_SPC','IDMTRL_M_SPC_MSK','IDMTRL_B_SPC','IDMTRL_B_SPC_MSK']
        typeLayers = typeLayers + ['IDMTRL_HILL','IDMTRL_CLOUD','IDMTRL_SKY']
        
        for layer in typeLayers:
            if not mc.ls(layer):
                #mc.createDisplayLayer(name = layer,nr = 1,empty = 1)
                mc.createRenderLayer(name = layer, noRecurse=1, makeCurrent=1, empty = 1)
                
    #----------------------------------------------------------#
    # 【核心】显示各个显示层加了物体
    def ydRLObjsTypesInfos(self):
        #objs = self.ydRLObjectsTList(2,0)
        objs = []
        objLights = []
        typeLayers = ['IDMTRL_F_CHR','IDMTRL_M_CHR','IDMTRL_B_CHR']
        typeLayers = typeLayers + ['IDMTRL_F_PRP','IDMTRL_M_PRP','IDMTRL_B_PRP']
        typeLayers = typeLayers + ['IDMTRL_F_SET','IDMTRL_M_SET','IDMTRL_B_SET']
        typeLayers = typeLayers + ['IDMTRL_F_SPC','IDMTRL_M_SPC','IDMTRL_B_SPC']
        typeLayers = typeLayers + ['IDMTRL_F_SPC_MSK','IDMTRL_M_SPC_MSK','IDMTRL_B_SPC_MSK']
        typeLayers = typeLayers + ['IDMTRL_HILL','IDMTRL_CLOUD','IDMTRL_SKY']
        
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        serverTransPath = serverPath + 'data/renderLayerInfos/' + shotInfo[0] + '/' + str(shotInfo[1]) + '/' + str(shotInfo[2]) + '/' + str(shotInfo[3]) + '/'

        # 输出信息
        self.ydRLObjectsTList(2,1,'mesh')
        self.ydRLObjectsTList(2,1,'light')

        keyInfos = ['CHRF','CHRM','CHRB','PRPF','PRPM','PRPB','SETF','SETM','SETB','SPCF','SPCM','SPCB','SPCMSKF','SPCMSKM','SPCMSKB','HILL','CLOUD','SKY']
        
        for key in keyInfos:
            info = sk_infoConfig.sk_infoConfig().checkFileRead(serverTransPath + 'mesh' +'_' +  key + '.txt')
            print u'===[%s][%s] Read Done==='%(key,'mesh')
            objs.append(info)

            if info not in ['SPCMSKF','SPCMSKM','SPCMSKB']:
                info = sk_infoConfig.sk_infoConfig().checkFileRead(serverTransPath + 'light' +'_' +  key + '.txt')
                print u'===[%s][%s] Read Done==='%(key,'light')
                objLights.append(info)
            else:
                objLights.append([])

        infos = []
        infos.append(u'\n----------------------------------------')
        for i in range(len(objs)):
            infos.append(typeLayers[i] + ' ' + 'mesh ' + ':\t\t' + str(len(objs[i])))
            infos.append(typeLayers[i] + ' ' + 'light' + ':\t\t' + str(len(objLights[i])))
            infos.append(u'-----')
        infos.append(u'----------------------------------------\n')
        
        for line in infos:
            print line
            
    #----------------------------------------------------------#
    # 根据选面物体信息获取物体剩余面信息
    # 处理maya bug
    def ydRLFaceObjReverse( self, checkMeshes):
        if not checkMeshes:
            return []
        meshesReverse = []
        # 核心算法：基于原理
        '''
        meshGrpInfos  = {}
        for mesh in checkMeshes:
            if '.f[' not in mesh:
                continue
            keys = meshGrpInfos.keys()
            if mesh.split('.f[')[0] not in keys:
                meshGrpInfos[mesh.split('.f[')[0]] = []
            meshGrpInfos[mesh.split('.f[')[0]].append(mesh)
        if meshGrpInfos:
            grpKeys = meshGrpInfos.keys()
            for grp in grpKeys:
                faceNum = mc.polyEvaluate(grp, face=1)
                usedNum = []
                # 记录物体
                for mesh in meshGrpInfos[grp]:
                    for i in range(faceNum):
                        if ':' in mesh.split('.f[')[-1]:
                            checkMin = int(mesh.split('.f[')[-1].split(':')[0])
                            checkMax = int(mesh.split('.f[')[-1].split(':')[-1].split(']')[0])
                            if (i >= checkMin and i <= checkMax):
                                if i not in usedNum:
                                    usedNum.append(i)
                        else:
                            if i == int(mesh.split('.f[')[-1].split(']')[0]):
                                if i not in usedNum:
                                    usedNum.append(i)
                # 处理反转数据
                for j in range(faceNum):
                    if j not in usedNum:
                        meshesReverse.append(grp + '.f[' + str(j) + ']')
        # 精简长度
        if meshesReverse:
            mc.select(meshesReverse)
            meshesReverse = mc.ls(sl = 1,l = 1)
        '''
        # 新算法：基于maya操作
        checkGrps = []
        for mesh in checkMeshes:
            if '.f[' in mesh:
                checkGrps.append(mesh.split('.f[')[0])
            else:
                if mc.nodeType(mesh) == 'transform':
                    grp = mesh
                else:
                    grp = mc.listRelatives(mesh,p=1,type = 'transform',f = 1)[0]
                checkGrps.append(grp)
        checkGrps = list(set(checkGrps))
        checkAllFaces = []
        for grp in checkGrps:
            faceNum = mc.polyEvaluate(grp, face=1)
            checkAllFaces.append(grp + '.f[0:' + str(faceNum-1) + ']')
        mc.select(checkMeshes)
        mc.select(checkAllFaces,tgl = 1)
        meshesReverse = mc.ls(sl = 1,l = 1)
        mc.select(cl = 1)
        return meshesReverse
    
    #--------------------------------------------------------------------------------------------------------#
    #----------------------------------------------------------#
    # 【核心】SG节点属性
    #----------------------------------------------------------#
    # 通过rlobjs获取SG信息
    def ydRLObjsSGNodesGet(self, objs = []):
        if not objs:
            print '1'
            return 0
        meshes = mc.listRelatives(objs,ad = 1, type = 'mesh',f = 1)
        if not meshes:
            print '2'
            return 0
        SGNodes = mc.listConnections(meshes,d = 1 ,type = 'shadingEngine')
        if not SGNodes:
            print '3'
            return 0
        result = list(set(SGNodes))
        return result
    
    # 获取所有SG节点
    def ydRLSGNodesGet(self,objType = 1 , objs = []):
        SGNodes = mc.ls(type='shadingEngine')
        SGNodes.remove('initialParticleSE')
        SGNodes.remove('initialShadingGroup')
        # SG分类
        refSGCHR = []
        refSGPROPC = []
        refSGPROPS = []
        refSGSET = []
        refSGSKY = []
        
        # 判断分类
        if objType == 1:
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
                        refSGPROPC.append(SGNode)
                    # 其他类，下面细化
                    if '/sets/' in refPath:
                        refSGSET.append(SGNode)
        
        result = []
        result.append(refSGCHR)
        result.append(refSGPROPC)
        result.append(refSGPROPS)
        result.append(refSGSET)
        result.append(refSGSKY)
        return result



    # 断开所有SG节点的连接
    def ydRLSGNodesDisConnections(self):

        SGNodes = mc.ls(type='shadingEngine')

        if SGNodes:
            for SGNode in SGNodes:
                if SGNode == "initialShadingGroup":
                    continue
                if SGNode == "initialParticleSE":
                    continue
                # 获取dagSetMembers连接信息,返回列表必定为2的倍数
                buf = mc.listConnections((SGNode + '.dagSetMembers'), connections=1, plugs=1)
                if buf:
                    for i in range(len(buf) / 2):
                        shape = buf[i + 1].split('.')[0]
                        if mc.nodeType(shape) != 'renderLayer':
                            try:
                                mc.disconnectAttr(buf[i + 1], buf[i])
                            except:
                                pass
                # 获取memberWireframeColor连接信息,返回列表必定为2的倍数
                buf = mc.listConnections((SGNode + '.memberWireframeColor'), connections=1, plugs=1)
                if buf:
                    for i in range(len(buf) / 2):
                        shape = buf[i + 1].split('.')[0]
                        if mc.nodeType(shape) != 'renderLayer':
                            try:
                                mc.disconnectAttr(buf[i + 1], buf[i])
                            except:
                                pass

    #--------------------------------------------------------------------------------------------------------#
    #----------------------------------------------------------#
    # 【核心】透明信息收集
    #----------------------------------------------------------#
    # 获取有透明贴图的物体 | 文件读取
    def ydRLTransparencyObjsOld(self, valueCheck = 0 ,update = 0):
        transparencySG = []
        # 获取file节点
        SGNodes = mc.ls(type = 'shadingEngine')
        doNotNeedSG = ['_ao_', '_nm_', '_light_', '_rim_', '_spec_','_fn_','_zdepth_','_rgb_']
        # 获取file节点
        SGNodes = mc.ls(type='shadingEngine')
        for SGNode in SGNodes:
            doNot = 0
            for doNotNeed in doNotNeedSG:
                if doNotNeed in SGNode.lower():
                    doNot = doNot + 1
            # 剔除不要的分层SG节点，只保留原始SG
            if doNot != 0:
                continue
            transLayerShaderCheckState = 0
            transRampShaderCheckState = 0
            # 判断是否有透明值
            transValueState = 0
            # 获取shader
            shaderNode = mc.listConnections( SGNode + '.surfaceShader')
            if not shaderNode:
                continue
            # 获取提供透明属性的上级连接的节点
            transpancyNode = ''
            needTranparencyAttr = ''
            if mc.nodeType(shaderNode[0]) != 'surfaceShader':
                # 判断是否层纹理
                # 对于层纹理，一旦发现有透明贴图，立即将本节点的outTransparency输出给新layer shader
                if mc.nodeType(shaderNode[0]) in ['layeredShader','layeredTexture']:
                    transpancyNode = ''
                    '''
                    # 获取层纹理的input
                    layerInputs = mc.getAttr((shaderNode[0] + '.inputs'),mi = 1)
                    if not layerInputs:
                        continue
                    for inputNum in layerInputs:
                        transpancyNode = ''
                        transpancyAttr = mc.ls(shaderNode[0] + '.inputs[' + str(inputNum) + ']' + '.transparency')
                        transpancyNode = mc.listConnections(transpancyAttr[0], plugs = 1 , connections = 1 ,destination = 0 )
                        if transpancyNode:
                            transLayerShaderCheckState = 1
                    if transLayerShaderCheckState:
                        transpancyNode = [shaderNode[0]]
                    else:
                        # 判断有没有值
                        needTranparencyAttr = shaderNode[0] + '.outTransparency'
                        transValue = mc.getAttr(needTranparencyAttr)
                        if transValue[0][0] != 0:
                            transpancyNode = [shaderNode[0]]
                        else:
                            transpancyNode = ''
                    '''
                    pass
                else:
                    # 判断是否 rampShader
                    # 对于判断是否rampShader，一旦发现有透明贴图，立即将本节点的outTransparency输出给新layer shader 
                    if mc.nodeType(shaderNode[0]) == 'rampShader':
                        transList = mc.getAttr((shaderNode[0] + '.transparency'),mi = 1)
                        for inputNum in transList:
                            transpancyNode = ''
                            transpancyAttr = mc.ls(shaderNode[0] + '.transparency[' + str(inputNum) + ']' + '.transparency_Color')
                            transpancyNode = mc.listConnections(transpancyAttr[0], plugs = 1 , connections = 1 ,destination = 0 )
                            if transpancyNode:
                                transRampShaderCheckState = 1
                        if transRampShaderCheckState:
                            transpancyNode = [shaderNode[0]]
                        else:
                            # 判断有没有值
                            needTranparencyAttr = shaderNode[0] + '.outTransparency'
                            transValue = mc.getAttr(needTranparencyAttr)
                            if transValue[0][0] != 0:
                                transpancyNode = [shaderNode[0]]
                            else:
                                transpancyNode = ''
                    else:
                        if mc.objExists(shaderNode[0] + '.transparency'):
                            transpancyAttr = mc.ls(shaderNode[0] + '.transparency')
                            transpancyNode = mc.listConnections(transpancyAttr[0], plugs = 1 , connections = 1 ,destination = 0 )
                            # 获取值
                            if not transpancyNode:
                                transValue = mc.getAttr(transpancyAttr[0])
                                if transValue[0][0] != 0:
                                    transValueState = 1
                                    transpancyNode = '[food]' + str(transValue[0][0])
            else:
                transpancyAttr = mc.ls(shaderNode[0] + '.outTransparency')
                transpancyNode = mc.listConnections(transpancyAttr[0], plugs = 1 , connections = 1 ,destination = 0 )
                # 获取值
                if not transpancyNode:
                    transValue = mc.getAttr(transpancyAttr[0])
                    if transValue[0][0] != 0:
                        transValueState = 1
                        transpancyNode = '[food]' + str(transValue[0][0])
            #print transpancyNode
            # 存在透明通道，则保存
            if transpancyNode:
                if transpancyAttr[0] in transpancyNode:
                    transpancyNode.remove(transpancyAttr[0])
            if transpancyNode:
                needTransNode = ''
                if transpancyNode[0] == '[':
                    needTransNode = transpancyNode
                else:
                    needTransNode = transpancyNode[0]
                # SG节点命名判断
                if ':' in SGNode:
                    meshes = mc.sets(SGNode,q=1)
                    if not meshes:
                        continue
                    meshes = mc.ls(meshes,l = 1)
                    
                    objs = []
                    for mesh in meshes:
                        # 地面不需要透明材质
                        if '_ground' in mesh.split('|')[-1]:
                            meshes.remove(mesh)
                            continue
                        if '.f[' in mesh:
                            objs.append(mesh.split('.f[')[0])
                        else:
                            objs.append(mc.listRelatives(mesh,p = 1, type = 'transform',f = 1)[0])
                            
                    #记录信息
                    if '[' in needTransNode:
                        transparencySG.append([SGNode,meshes,needTransNode,objs])
                    else:
                        if mc.nodeType(needTransNode.split('.')[0]) not in ['layeredShader','layeredTexture']:
                            transparencySG.append([SGNode,meshes,needTransNode,objs])
                else:
                    meshes = mc.sets(SGNode,q=1)
                    if not meshes:
                        continue
                    meshes = mc.ls(meshes,l = 1)
                    
                    objs = []
                    for mesh in meshes:
                        # 地面不需要透明材质
                        if '_ground' in mesh.split('|')[-1]:
                            meshes.remove(mesh)
                            continue
                        if '.f[' in mesh:
                            objs.append(mesh.split('.f[')[0])
                        else:
                            objs.append(mc.listRelatives(mesh,p = 1, type = 'transform',f = 1)[0])
                            
                    #记录信息
                    if '[' in needTransNode:
                        transparencySG.append([SGNode,meshes,needTransNode,objs])
                    else:
                        if mc.nodeType(needTransNode.split('.')[0]) not in ['layeredShader','layeredTexture']:
                            transparencySG.append([SGNode,meshes,needTransNode,objs])

        # 输出信息
        # 必须全部输出，避免由有内容到无内容的不更新bug更新
        # 整理信息
        #if not transparencySG:
        #    return [[],[],[]]
            
        # 处理数据结构
        needSGNodes    = []
        needSGMeshes   = []
        needTransNodes = []
        needSGObjs = []
        for j in range(len(transparencySG)):
            recordState = 1
            if not transparencySG[j][1]:
                continue
            if transparencySG[j][1]:
                if not transparencySG[j][1][0]:
                    continue
            if valueCheck:
                if '[food]' in transparencySG[j][2]:
                    recordState = 0
            if recordState:
                needSGNodes.append(transparencySG[j][0])
                needSGMeshes.append(transparencySG[j][1])
                needTransNodes.append(transparencySG[j][2])
                needSGObjs.append(transparencySG[j][3])
        transparencySG = [needSGNodes,needSGMeshes,needTransNodes,needSGObjs]
        # 上传
        if update:
            # 本地及服务器端路径
            shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
            localPath = sk_infoConfig.sk_infoConfig().checkLocalInfoPath()
            serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
            localTransPath = localPath + 'RLayerInfo/transShaderInfo/' + shotInfo[0] + '/' + str(shotInfo[1]) + '/' + str(shotInfo[2]) + '/' + str(shotInfo[3]) + '/'
            mc.sysFile(localTransPath ,makeDir = 1)
            serverTransPath = serverPath + 'data/RLayerInfo/transShaderInfo/' + shotInfo[0] + '/' + str(shotInfo[1]) + '/' + str(shotInfo[2]) + '/' + str(shotInfo[3]) + '/'
            makeDirCMD = 'zwSysFile(\"MD\",\"' + serverTransPath + '\",\"\",1)'
            mel.eval(makeDirCMD)
            # 本地输出及更新
            sk_infoConfig.sk_infoConfig().checkFileWrite((localTransPath +  'transSGNodes.txt'), transparencySG[0])
            updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localTransPath + 'transSGNodes.txt') + '"' + ' ' + '"' + (serverTransPath + 'transSGNodes.txt') + '"' + ' true'
            mel.eval(updateAnimCMD)
            sk_infoConfig.sk_infoConfig().checkFileWrite((localTransPath +  'transMeshes.txt'), transparencySG[1])
            updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localTransPath + 'transMeshes.txt') + '"' + ' ' + '"' + (serverTransPath + 'transMeshes.txt') + '"' + ' true'
            mel.eval(updateAnimCMD)
            sk_infoConfig.sk_infoConfig().checkFileWrite((localTransPath +  'transNodes.txt'), transparencySG[2])
            updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localTransPath + 'transNodes.txt') + '"' + ' ' + '"' + (serverTransPath + 'transNodes.txt') + '"' + ' true'
            mel.eval(updateAnimCMD)
            sk_infoConfig.sk_infoConfig().checkFileWrite((localTransPath +  'transObjs.txt'), transparencySG[3])
            updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localTransPath + 'transObjs.txt') + '"' + ' ' + '"' + (serverTransPath + 'transObjs.txt') + '"' + ' true'
            mel.eval(updateAnimCMD)
        return transparencySG
    
    #----------------------------------------------------------#
    # 按类别获取该层有的透明信息
    def ydRLTransparencyObjsByType(self,rlObjs,layerType):
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        currentRenderLayer = mc.editRenderLayerGlobals(currentRenderLayer = 1 ,q = 1)
        if currentRenderLayer == 'defaultRenderLayer':
            # 获取并update
            transpancyObjs = self.ydRLTransparencyObjsOld(1,1)
        else:
            serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
            serverTransPath = serverPath + 'data/RLayerInfo/transShaderInfo/' + shotInfo[0] + '/' + str(shotInfo[1]) + '/' + str(shotInfo[2]) + '/' + str(shotInfo[3]) + '/'
            needSGNodes     = sk_infoConfig.sk_infoConfig().checkFileRead(serverTransPath +  'transSGNodes.txt')
            needTransNodes  = sk_infoConfig.sk_infoConfig().checkFileRead(serverTransPath +  'transNodes.txt')
            # 处理数据
            tempSGMeshes    = sk_infoConfig.sk_infoConfig().checkFileRead(serverTransPath +  'transMeshes.txt')
            tempSGObjs      = sk_infoConfig.sk_infoConfig().checkFileRead(serverTransPath +  'transObjs.txt')
            needSGMeshes    = []
            needSGObjs      = []
            if tempSGMeshes:
                # meshesh
                for i in range(len(tempSGMeshes)):
                    resultInfo = []
                    allInfo    = tempSGMeshes[i]
                    splitInfo = allInfo.split(', ')
                    for j in range(len(splitInfo)):
                        needInfo = splitInfo[j][2:-1]
                        if j == 0:
                            needInfo = splitInfo[j][3:-1]
                        if j == (len(splitInfo) - 1):
                            needInfo = splitInfo[j][2:-2]
                        resultInfo.append(needInfo)
                    needSGMeshes.append(resultInfo)
                # objs
                for i in range(len(tempSGObjs)):
                    resultInfo = []
                    allInfo    = tempSGObjs[i]
                    splitInfo = allInfo.split(', ')
                    for j in range(len(splitInfo)):
                        needInfo = splitInfo[j][2:-1]
                        if j == 0:
                            needInfo = splitInfo[j][3:-1]
                        if j == (len(splitInfo) - 1):
                            needInfo = splitInfo[j][2:-2]
                        resultInfo.append(needInfo)
                    needSGObjs.append(resultInfo)
            transpancyObjs  = [needSGNodes,needSGMeshes,needTransNodes,needSGObjs]

        transpancySGNodes = []
        transpancyMeshes = []
        transpancyNode = []
        transpancyGrps = []
        meshes = transpancyObjs[1]
        needID = []
        if meshes:
            for k in range(len(meshes)):
                if not mc.ls(meshes[k][0]):
                    continue
                if '.f[' in meshes[k][0]:
                    obj = meshes[k][0].split('.f[')[0]
                else:
                    obj = mc.listRelatives(meshes[k][0],p = 1, type = 'transform', f = 1)[0]
                if obj in rlObjs:
                    needID.append(k)
        else:
            transpancySGNodes = transpancyObjs[0]
            transpancyMeshes = transpancyObjs[1]
            transpancyNode = transpancyObjs[2]
            transpancyGrps = transpancyObjs[3]
            
        if needID:
            needID = list(set(needID))
            for num in needID:
                transpancySGNodes.append(transpancyObjs[0][num])
                transpancyMeshes.append(transpancyObjs[1][num])
                transpancyNode.append(transpancyObjs[2][num])
                transpancyGrps.append(transpancyObjs[3][num])
        return [transpancySGNodes,transpancyMeshes,transpancyNode,transpancyGrps]
    
    
    #----------------------------------------------------------#
    # 获取有透明贴图的物体,通过参考获取服务器端数据
    # refNamespaceMode 0 Ref Mode | 1 Namespace Mode
    def ydRLTransparencyObjs(self, refNamespaceMode=1):
        from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
        reload(sk_referenceConfig)
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
                            # 处理非正常namespace
                            if assetInfo[-1][-1] in numStr or assetInfo[2] not in ['h', 'm', 'l']:
                                assetInfoNeed = assetInfo[0] + '_' + assetInfo[1] + '_h'
                        allAssetInfo.append(assetInfoNeed)
                        allAssetNsInfo.append(ns)
        # print '-----'
        # print allAssetInfo
        # print '-----'
        # print allAssetNsInfo
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

    #--------------------------------------------------------------------------------------------------------#
    #----------------------------------------------------------#
    # 【核心】透明属性连接
    #----------------------------------------------------------#
    # 透明属性连接
    def ydRLTransShaderConnection(self, transpancyNode, transShader, transShaderAttr):
        if transpancyNode[:6] == '[food]':
            transValue = float(transpancyNode[7:])
            try:
                transpancyConnections = mc.listConnections((transShader + '.' + transShaderAttr), s=1, plugs=1)
                mc.disconnectAttr(('%s') % (transpancyConnections[0]), ('%s.%s') % (transShader, transShaderAttr))
            except:
                pass
            mc.setAttr((transShader + '.' + transShaderAttr), transValue, transValue, transValue, type='double3')
        else:
            if mc.nodeType(transpancyNode.split('.')[0]) in['layeredShader','layeredTexture', 'surfaceShader', 'ramp', 'file', 'reverse','checker','bulge','fractal']:
                if mc.nodeType(transpancyNode.split('.')[0]) in ['layeredShader','layeredTexture', 'surfaceShader']:
                    try:
                        mc.disconnectAttr(('%s.%s') % (transpancyNode.split('.')[0], 'outTransparency'), ('%s.%s') % (transShader, transShaderAttr))
                    except:
                        pass
                    mc.connectAttr(('%s.%s') % (transpancyNode.split('.')[0], 'outTransparency'), ('%s.%s') % (transShader, transShaderAttr), f=True)
                if mc.nodeType(transpancyNode.split('.')[0]) in ['ramp', 'file' ,'bulge','checker','fractal']:
                    try:
                        mc.disconnectAttr(('%s.%s') % (transpancyNode.split('.')[0], 'outColor'), ('%s.%s') % (transShader, transShaderAttr))
                    except:
                        pass
                    mc.connectAttr(('%s.%s') % (transpancyNode.split('.')[0], 'outColor'), ('%s.%s') % (transShader, transShaderAttr), f=True)
                if mc.nodeType(transpancyNode.split('.')[0]) in ['reverse']:
                    try:
                        mc.disconnectAttr(('%s.%s') % (transpancyNode.split('.')[0], 'output'), ('%s.%s') % (transShader, transShaderAttr))
                    except:
                        pass
                    mc.connectAttr(('%s.%s') % (transpancyNode.split('.')[0], 'output'), ('%s.%s') % (transShader, transShaderAttr), f=True)
            else:
                if mc.objExists(transShader+'.'+transShaderAttr):
                    try:
                        mc.disconnectAttr(('%s.%s') % (transpancyNode.split('.')[0], 'outAlpha'), ('%s.%s') % (transShader, transShaderAttr))
                    except:
                        pass
                    mc.connectAttr(('%s.%s') % (transpancyNode.split('.')[0], 'outAlpha'), ('%s.%s') % (transShader, transShaderAttr), f=True)


    #--------------------------------------------------------------------------------------------------------#
    #----------------------------------------------------------#
    # 【核心】置换信息收集
    #----------------------------------------------------------#
    # 获取有置换贴图的物体|文件获取
    def ydRLDisplacementObjsOld(self):
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
    #----------------------------------------------------------#
    # 获取有置换贴图的物体,通过参考获取服务器端数据
    # refNamespaceMode 0 Ref Mode | 1 Namespace Mode
    def ydRLDisplacementObjs(self, refNamespaceMode=1):
        from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
        reload(sk_referenceConfig)
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

    #--------------------------------------------------------------------------------------------------------#
    #----------------------------------------------------------#
    # 【辅助】 各种基础功能建设
    #----------------------------------------------------------#
    
    #--------------------------------#
    # 选取模式
    def ydRLSelectMode(self):
        # 选取模式
        rlObjs = []
        # 选取模式
        selObjs = mc.ls(sl=1, l=1)
        if not selObjs:
            print('======请选取物体======')
            mc.error('======请选取物体======')
        checkMeshes = mc.listRelatives(selObjs, ad=1, type='mesh',f = 1)
        if not checkMeshes:
            print('======请选取有效物体======')
            mc.error('======请选取有效物体======')
        rlObjs = list(set(selObjs))
        return rlObjs

    #--------------------------------#
    # 读取数据库信息
    def ydRLReadServerData(self):
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()  
        #project = 'Ninjago'
        project = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(shotInfo[0])
        
        import pyodbc
        cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=192.168.168.16;DATABASE=idmtPlex_%s;UID=EWAUser;PWD=hk#$G#324f'%(project))
        cursor = cnxn.cursor()
        cmd_tk = 'exec idmtPlex_%s.dbo.usp_TD0001 \'%s\',\'%s\',\'%s\''%(project,shotInfo[1],shotInfo[2],shotInfo[3])
        data = cursor.execute(cmd_tk).fetchone()
        # 关闭连接
        pyodbc.connect('DRIVER={SQL Server};SERVER=192.168.168.16;DATABASE=idmtPlex_%s;UID=EWAUser;PWD=hk#$G#324f'%(project)).close()

        return data

    #--------------------------------#
    # 读取excel信息
    def ydRLReadEXcle(self):
        # 处理excel信息？
        # 读文件名，获取项目及镜头号
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()  

        projFullName = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(shotInfo[0])

        #serverPath = '//file-cluster/GDC/Projects/' + projFullName + '/' + projFullName +  '_scratch/TD/ExcelInfo/' + str(shotInfo[1]) + '/' 
        serverPath = '//file-cluster/GDC/Projects/' + projFullName + '/Reference/Product manager/Render/ExcelInfo/' + str(shotInfo[1]) + '/' 
        serverExcelPath = serverPath + shotInfo[0].upper() + str(shotInfo[1]) + '_TimeOfDay.xls'
        
        print '-----'
        print serverExcelPath
        
        import os
        if not os.path.exists(serverExcelPath):
            print(u'=======本集Excel文件不存在，请联系环节负责人处理=====')
            mc.error(u'=======本集Excel文件不存在，请联系环节负责人处理=====')

        import xlrd
        reload(xlrd)
        # shotAllData = xlrd.open_workbook(serverExcelPath).sheets()[0] 0是第一页表格
        shotAllData = xlrd.open_workbook(serverExcelPath).sheets()[0]  
        
        # 定位行数
        # 先找场名
        rowMax = shotAllData.nrows
        rowID = []
        for i in range(rowMax):
            shotID = self.ydRLExcelInfoConfig(shotAllData.row_values(i)[0])
            # 场
            checkInfo = shotInfo[2]
            if shotID == checkInfo:
                rowID.append(i)
        
        if not rowID:
            print u'=====本镜头信息不在指定表格内，请联系环节负责人处理====='
            mc.error(u'=====本镜头信息不在指定表格内，请联系环节负责人处理=====')
        
        # 找镜头号
        needID = 0
        for line in rowID:
            shotID = self.ydRLExcelInfoConfig(shotAllData.row_values(line)[1])
            # 镜头号
            checkInfo = shotInfo[3]
            if shotID == checkInfo:
                needID = line
                break
        
        if not needID:
            print u'=====本镜头信息不在指定表格内，请联系环节负责人处理====='
            mc.error(u'=====本镜头信息不在指定表格内，请联系环节负责人处理=====')

        # 读行数，具体的是镜头号加多少，视表格内容定
        shotData = shotAllData.row_values(needID)  
        
        return shotData


    # 处理表格信息
    def ydRLExcelInfoConfig(self,info):
        info = str(info)
        while info[-1] in [';',' ']:
            info = info[:-1]
        while '.' in info:
            info = info.split('.')[0]
        return info

    #--------------------------------#
    # Save File
    # shotType  1  cl_001_002  | 2 yd_005_009_001
    def ydRLSave(self, mode , shotType = 3 , RGB = ''):
        print (u'===============!!!Start 【%s】!!!===============' % 'Save')
        print 'Working...'
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        pathLocal = sk_infoConfig.sk_infoConfig().checkRenderLayerLocalPath(shotType).replace('D:','E:')
        mc.sysFile(pathLocal, makeDir=True)
        fileType=''
        if shotType == 2:
            fileName = pathLocal + shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2]
            camName = '*:*am_' + shotInfo[1] + '_' + shotInfo[2] + '_baked'
        if shotType == 3:
            fileName = pathLocal + shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2] + '_' +  shotInfo[3]
            camName = '*:*am_'  + shotInfo[1] + '_' + shotInfo[2] + '_' +  shotInfo[3] + '_baked'
        if mode == 'CHRF' and RGB!='CO' and RGB!='NCO':
            fileType = '_l4CHRF' + RGB + '_lr_c001.mb'
        if mode == 'CHRM' and RGB!='CO' and RGB!='NCO':
            fileType = '_l4CHRM' + RGB + '_lr_c001.mb'
        if mode == 'CHRB' and RGB!='CO' and RGB!='NCO':
            fileType = '_l4CHRB' + RGB + '_lr_c001.mb'
 
        if mode == 'CHRB' and RGB=='CO':
            fileType = '_l1CHRB' + RGB + '_lr_c001.mb' 
        if mode == 'CHRF' and RGB=='CO':
            fileType = '_l1CHRF' + RGB + '_lr_c001.mb'
        if mode == 'CHRM'and RGB=='CO':
            fileType = '_l1CHRM' + RGB + '_lr_c001.mb'

        if mode == 'CHRB' and RGB=='NCO':
            fileType = '_l3CHRB' + RGB + '_lr_c001.mb'
        if mode == 'CHRF' and RGB=='NCO':
            fileType = '_l3CHRF' + RGB + '_lr_c001.mb'
        if mode == 'CHRM' and RGB=='NCO':
            fileType = '_l3CHRM' + RGB + '_lr_c001.mb'
  
    
        if mode == 'PRPF':
            fileType = '_l4PRPF' + RGB + '_lr_c001.mb'
        if mode == 'PRPM':
            fileType = '_l4PRPM' + RGB + '_lr_c001.mb'
        if mode == 'PRPB':
            fileType = '_l4PRPB' + RGB + '_lr_c001.mb'
    
        if mode == 'SETF' and RGB!='CO' and RGB!='NCO':
            fileType = '_l4SETF' + RGB + '_lr_c001.mb'
        if mode == 'SETM'and RGB!='CO' and RGB!='NCO':
            fileType = '_l4SETM' + RGB + '_lr_c001.mb'
        if mode == 'SETB' and RGB!='CO' and RGB!='NCO':
            fileType = '_l4SETB' + RGB + '_lr_c001.mb'

        if mode == 'SETB' and RGB=='NCO':
            fileType = '_l3SETB' + RGB + '_lr_c001.mb'
        if mode == 'SETF' and RGB=='NCO':
            fileType = '_l3SETF' + RGB + '_lr_c001.mb'
        if mode == 'SETM' and RGB=='NCO':
            fileType = '_l3SETM' + RGB + '_lr_c001.mb'

        if mode == 'SETB' and RGB=='CO':
            fileType = '_l1SETB' + RGB + '_lr_c001.mb'            
        if mode == 'SETF' and RGB=='CO':
            fileType = '_l1SETF' + RGB + '_lr_c001.mb'
        if mode == 'SETM' and RGB=='CO' :
            fileType = '_l1SETM' + RGB + '_lr_c001.mb'

 
        if mode == 'SPCF' :
            fileType = '_l4SPCF' + RGB + '_lr_c001.mb'
        if mode == 'SPCM':
            fileType = '_l4SPCM' + RGB + '_lr_c001.mb'
        if mode == 'SPCB':
            fileType = '_l4SPCB' + RGB + '_lr_c001.mb'
        if mode == 'SPCF':
            fileType = '_l4SPCF' + RGB + '_lr_c001.mb'
        if mode == 'SPCM':
            fileType = '_l4SPCM' + RGB + '_lr_c001.mb'
        if mode == 'SPCB':
            fileType = '_l4SPCB' + RGB + '_lr_c001.mb'
        if mode == 'ENV':
            fileType = '_l3ENV' + RGB + '_lr_c001.mb'
        if mode == 'SETAO':
            fileType = '_l3SETAO' + RGB + '_lr_c001.mb'
    
        if mode == 'BASE':
            fileType = '_BASE' + RGB + '_lr_c001.mb'
        
        # 处理非参考同名相机
        if mc.ls(camName):
            # 检测是否参考
            ifRef = mc.referenceQuery(camName,isNodeReferenced = 1)
            if not ifRef:
                mc.delete(camName)
                mc.namespace(set=':')
                mc.namespace(force=1, moveNamespace =['CAM:',':'])
                mc.namespace(removeNamespace = 'CAM:')
        
        # camera定位
        camName = mc.ls(camName)
        if camName:
            camName = camName[0]
        else:
            print u'\n'
            print u'=====本文件cam异常，请检查文件====='
            mc.error(u'=====本文件cam异常，请检查文件=====')
        print '---'
        print camName
        
        # Camera
        from idmt.maya.commonCore.core_mayaCommon import sk_hbExportCam
        reload(sk_hbExportCam)
        if shotType == 1:
            sk_hbExportCam.sk_hbExportCam().camServerReference()   
        if shotType == 2:
            sk_hbExportCam.sk_hbExportCam().camServerReference(3)   
    
        mel.eval("source \"zwCameraImportExport.mel\"")
        #camName = mel.eval("zwGetCameraEx \"\"")
        mc.setAttr((camName + '.renderable'),1)
        mc.setAttr((camName + '.farClipPlane'),100000)
    
        # skydome Setting
        #self.clSkydomeExcelLoad()
    
        try:
            mc.setAttr('perspShape.renderable',0)
        except:
            pass
    
        fileName = fileName + fileType
        print u'-------'
        print fileName
        print '\n'
    
        mc.file(rename = fileName)
    
        mc.file(save=1,type = 'mayaBinary',f = 1)
    
        #mc.file(save=1,f = 1)
        return pathLocal
        print (u'===============!!!Done  【%s】!!!===============' %'Save')
        print '\n'

#--------------------------------#
# camSetting
# typeMode 2--do_xxx_xxx  |  3--do_xxx_xxx_xxx
    def ydRLCamSetting(self,typeMode = 3):
        # 处理cam
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        if typeMode == 2:
            camName = 'CAM:*_' + str(shotInfo[1]) + '_' + str(shotInfo[2]) +  '_baked'
        if typeMode == 3:
            camName = 'CAM:*_' + str(shotInfo[1]) + '_' + str(shotInfo[2]) + '_' + str(shotInfo[3]) + '_baked'
        if mc.ls(camName, type='transform'):
            camName = mc.ls(camName,type = 'transform')[0]
            camShape = mc.listRelatives(mc.ls(camName, type='transform')[0], ni=1, c=1)[0]
            mc.setAttr((camShape + '.renderable'), 1)
            try:
                mc.setAttr(('perspShape.renderable'), 0)
            except:
                pass
        else:
            print('===============未找到有效CAM【%s】===============' % camName)
            mc.error('===============未找到有效CAM【%s】===============' % camName)
    
    #--------------------------------#
    # smoothSet，更新smooth信息
    def ydRLDoSmooth(self, layerType=1):
        from idmt.maya.commonCore.core_mayaCommon import sk_smoothSet
        reload(sk_smoothSet)
        # 非PFX层用
        if layerType == 1:
            sk_smoothSet.sk_smoothSet().smoothSetDoSmooth()
            
    #--------------------------------#
    # 获取眉毛物体
    def ydRLGBowObjs(self):
        allObjs = mc.ls(type = 'transform',l=1)
        bowObjs = []
        for obj in allObjs:
            keyWords = ['drape','brow','brow_r_','brow_l_','browr_','browl_','eyepatch_']
            for key in keyWords:
                if key in obj.split('|')[-1].lower():
                    mesh = mc.listRelatives(obj,s= 1,ni= 1,type ='mesh')
                    if mesh:
                        bowObjs.append(obj)
    
        if not bowObjs:
            bowObjs = []
        if bowObjs:
            need = []
            for obj in bowObjs:
                if ':MODEL|' in obj:
                    need.append(obj)
            if not need:
                need = []
            bowObjs = need
            
        return bowObjs
    
    #--------------------------------#
    # 获取五官物体
    def ydRLFaceObjs(self):
        planeObjs = mc.ls('*:*_planar*',type = 'transform',l = 1)
        planeObjs = mc.ls('*:*_eyepatch_*',type = 'transform',l = 1) + planeObjs
        planeObjs = mc.ls('*:*mask*',type = 'transform',l = 1) + planeObjs
        planeObjs = mc.ls('*:*mouth_prox*',type = 'transform',l = 1) + planeObjs
        planeObjs = mc.ls('*:*Rimple_*',type = 'transform',l = 1) + planeObjs
        planeObjs = mc.ls('*:MSH_glasses_*',type = 'transform',l = 1) + planeObjs
        planeObjs = mc.ls('*:*glass*',type = 'transform',l = 1) + planeObjs
        planeObjs = mc.ls('*:*cheaters_*',type = 'transform',l = 1) + planeObjs
        planeObjs = mc.ls('*:*_defor',type = 'transform',l = 1) + planeObjs
        planeObjs = mc.ls('*:*crinkle*',type = 'transform',l = 1) + planeObjs

        reObjs=mc.ls('*:MSH_Diamonts*',type = 'transform',l = 1)
        reObjs=mc.ls('*:*_frame*',type = 'transform',l = 1)+reObjs
        reObjs=mc.ls('*ce60570075001Dogshank*:*',type = 'transform',l=1)+reObjs
        if mc.ls(reObjs):
            for robj in reObjs  :
                if robj in planeObjs:
                    planeObjs.remove(robj)
        
        if not planeObjs:
            planeObjs = []
        if planeObjs:
            need = []
            for obj in planeObjs:
              
                if ':RIG|' not in obj :
                    shape=mc.listRelatives(obj,s=1,f=1)
                    if shape and mc.nodeType(shape[0])=='mesh':
                        need.append(obj)
            if not need:
                need = []
            planeObjs = need
            
        return planeObjs

    #--------------------------------------------------------------------------------------------------------#
    #----------------------------------------------------------#
    # 【核心】 渲染层函数集
    #----------------------------------------------------------#

    #--------------------------------#
    # Color层
    def ydRLCOCreate(self, layerType, selectObjType=0 ,createMode = 1,createName = ''):
        print (u'===============!!!Start 【%s】!!!===============' % (u'%s_CO层' % layerType))
        print 'Working...'

        # 物体信息
        rlObjs      = []
        MaskObjs    = []
        layerName   = ''
        rlSGNodes   = []
        rlLights    = []
        layerObjs   = []
        if selectObjType == 0:
            needInfo = self.ydRLObjsInfo(layerType,'CO')
            rlObjs    = needInfo[0]
            MaskObjs  = needInfo[1]
            layerName = needInfo[2]
            rlSGNodes = needInfo[3]
            rlLights  = needInfo[4]
            layerObjs = needInfo[5]

        # 选取模式
        if selectObjType == 1:
            rlObjs    = self.ydRLSelectMode()
            layerObjs = rlObjs
            layerName = createName + '_CO'

        if layerObjs:
            # 创建RenderLayer
            if mc.ls(layerName):
                mc.delete(layerName)

            mc.createRenderLayer((rlObjs + rlLights), name=layerName, noRecurse=1, makeCurrent=1)

            # 隐藏灯光

            # Mask显示|隐藏
            if MaskObjs:
                meshes = mc.listRelatives(MaskObjs ,ni = 1 , ad = 1 , type = 'mesh',f = 1)
                if meshes:
                    for mesh in meshes:
                        #mc.editRenderLayerAdjustment(mesh + '.primaryVisibility')
                        #mc.setAttr((mesh + '.primaryVisibility'),l = 0)
                        mc.setAttr((mesh + '.primaryVisibility'), 0)
                        #mc.editRenderLayerAdjustment(mesh + '.receiveShadows')
                        #mc.setAttr((mesh + '.receiveShadows'), l = 0)
                        mc.setAttr((mesh + '.receiveShadows'), 0)
                        
            # CHR层，眉毛保留，其他五官隐藏
            '''
            if layerType[:3] in ['CHR']:
                objsNeedHide = self.ydRLFaceObjs()
                if objsNeedHide:
                    for obj in objsNeedHide:
                        mc.editRenderLayerAdjustment(obj + '.v')
                        mc.setAttr((obj + '.v'), 0)
            '''

            # 渲染设置
            mc.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')

            # 开启光线追踪
            mc.editRenderLayerAdjustment('miDefaultOptions.rayTracing')
            mc.setAttr('miDefaultOptions.rayTracing', 1)

            # exr
            if createMode:
                self.ydRLFramebuffer('iff',3)

            print (u'===============!!!Done  【%s】!!!===============' % (u'%s_CO层' % layerType))
            print '\n'

        else:
            print (u'===============!!!Error  【%s】无物体!!!===============' % (u'%s_CO层' % layerType))
            print '\n'


    # Occlusion层
    # 需要开启FG渲染
    # No Lights
    def ydRLAOCreate(self, layerType, selectObjType=0 , SGOType = 0 , shaderForece = 0 ,createMode = 1,createName = ''):
        print (u'===============!!!Start 【%s】!!!===============' % (u'%s_AO层' % layerType))
        print 'Working...'

        # 物体信息
        rlObjs      = []
        MaskObjs    = []
        layerName   = ''
        rlSGNodes   = []
        rlLights    = []
        layerObjs   = []
        if selectObjType == 0:
            needInfo = self.ydRLObjsInfo(layerType,'AO')
            rlObjs    = needInfo[0]
            MaskObjs  = needInfo[1]
            layerName = needInfo[2]
            rlSGNodes = needInfo[3]
            rlLights  = needInfo[4]
            layerObjs = needInfo[5]

        # 选取模式
        if selectObjType == 1:
            rlObjs    = self.ydRLSelectMode()
            layerObjs = rlObjs
            layerName = createName + '_AO'

        if layerObjs:
            transpancyObjs = [[],[],[],[]]

            if createMode:
            # 特殊处理，半透明用
                # 获取信息必须在masterLayer进行
                transpancyObjs    = self.ydRLTransparencyObjsByType(layerObjs,layerType)
                
            transpancySGNodes = transpancyObjs[0]
            transpancyMeshes  = transpancyObjs[1]
            transpancyNode    = transpancyObjs[2]
            transpancyGrps    = transpancyObjs[3]

            # allTransMeshes
            allTransGrps = []
            for info in transpancyGrps:
                allTransGrps = allTransGrps + info
            if allTransGrps:
                allTransGrps = list(set(allTransGrps))
                
            # 创建RenderLayer
            if mc.ls(layerName):
                mc.delete(layerName)
            
            mc.createRenderLayer((rlObjs), name=layerName, noRecurse=1, makeCurrent=1)
            
            # Mask显示|隐藏
            if MaskObjs:
                meshes = mc.listRelatives(MaskObjs ,ni = 1 , ad = 1 , type = 'mesh',f = 1)
                if meshes:
                    for mesh in meshes:
                        #mc.editRenderLayerAdjustment(mesh + '.primaryVisibility')
                        #mc.setAttr((mesh + '.primaryVisibility'),l = 0)
                        mc.setAttr((mesh + '.primaryVisibility'), 0)
                        #mc.editRenderLayerAdjustment(mesh + '.receiveShadows')
                        #mc.setAttr((mesh + '.receiveShadows'), l = 0)
                        mc.setAttr((mesh + '.receiveShadows'), 0)

            # AO层，眉毛隐藏，其他五官隐藏，眉毛不投射阴影
            if layerType[:3] in ['CHR']:
                objsNeedHide = self.ydRLGBowObjs() 
                objsNeedHide = self.ydRLFaceObjs() + objsNeedHide
                if objsNeedHide:
                    for obj in objsNeedHide:
                        #mc.editRenderLayerAdjustment(obj + '.v')
                        mc.setAttr((obj + '.v'), 0)

            # 通用AO材质
            shader_Node = 'SHD_' + layerType + '_AO_Shader'
            if mc.ls(shader_Node):
                mc.delete(shader_Node)
            AO_Node = 'SHD_' + layerType + '_AO_Node'
            if mc.ls(AO_Node):
                mc.delete(AO_Node)
            # 经典连材质模式
            if not SGOType:
                AO_SG = 'SHD_' + layerType + '_AO_SG'
                if mc.ls(AO_SG):
                    mc.delete(AO_SG)

            shader_Node = mc.shadingNode('surfaceShader', asShader=True, name=shader_Node)
            AO_Node = mc.shadingNode('mib_amb_occlusion', asTexture=True, name=AO_Node)
            mc.connectAttr((AO_Node + '.outValue'), (shader_Node + '.outColor'))
            # 经典连材质模式
            if not SGOType:
                AO_SG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name = AO_SG)
                mc.connectAttr((shader_Node + '.outColor'), (AO_SG + '.surfaceShader'))
            
            if(layerType[:3] in ['CHR','PRP']):
                mc.setAttr(('%s.%s') % (AO_Node, 'samples'), 136)
                mc.setAttr(('%s.%s') % (AO_Node, 'max_distance'), 2)
                mc.setAttr(('%s.%s') % (AO_Node, 'output_mode'), 0)

            if(layerType[:3] in ['SET','SPC']):
                mc.setAttr(('%s.%s') % (AO_Node, 'samples'), 136)
                mc.setAttr(('%s.%s') % (AO_Node, 'max_distance'), 10)
                mc.setAttr(('%s.%s') % (AO_Node, 'output_mode'), 0)

            # 优先全局着色
            # 经典连材质模式
            if not SGOType:
                # layerObjs 类型必然是transform
                for obj in layerObjs:
                    # 属于matter
                    if obj in MaskObjs:
                        continue
                    if obj in transpancyGrps:
                        continue
                    mesh = mc.listRelatives(obj,s = 1 ,ni  = 1, type = 'mesh',f=1)
                    if not mesh:
                        continue
                    mesh = mesh[0]
                    shaderSG = AO_SG
                    mc.select(mesh)
                    try:
                        mc.sets(mesh,e = 1 , forceElement = shaderSG)
                        print '---006'
                        print AO_SG
                    except:
                        print u'===有物体无法赋予材质==='
                        print mesh
                        mc.error(u'===有物体无法赋予材质===')

            # SG连接模式
            if SGOType:
                if rlSGNodes:
                    for SGNode in rlSGNodes:
                        shaderInfo = mc.listConnections((SGNode + '.surfaceShader'),s = 1,plugs = 1)
                        if not shaderInfo:
                            continue
                        shaderInfo = shaderInfo[0]
                        mc.editRenderLayerAdjustment(SGNode + '.surfaceShader')
                        mc.disconnectAttr(shaderInfo, (SGNode + '.surfaceShader'))
                        mc.connectAttr((shader_Node + '.outColor'), (SGNode + '.surfaceShader'), f=1)

            '''
            # 特殊物体着色
            if transpancySGNodes:
                for i in range(len(transpancySGNodes)):
                    if not mc.ls(transpancySGNodes[i]):
                        continue
                    if transpancySGNodes[i] not in rlSGNodes:
                        continue
                    keySGInfo = str(i)
                    meshes = transpancyMeshes[i]
                    
                    # 有着色物体时才进行
                    if not meshes:
                        continue
                    
                    shaderMain = 'SHD_' + layerType + '_' + keySGInfo + '_AO_Main_Shader'
                    if mc.ls(shaderMain):
                        mc.delete(shaderMain)
                    shaderMR = 'SHD_' + layerType + '_' + keySGInfo + '_AO_TransMR_Shader'
                    if mc.ls(shaderMR):
                        mc.delete(shaderMR)
                    AONode = 'SHD_' + layerType + '_' + keySGInfo + '_AO_MR_Node'
                    if mc.ls(AONode):
                        mc.delete(AONode)
                    shaderMRTrans = 'SHD_' + layerType + '_' + keySGInfo + '_AO_TransMR_Shader'
                    if mc.ls(shaderMRTrans):
                        mc.delete(shaderMRTrans)
                    luminanceNode = 'SHD_' + layerType + '_' + keySGInfo + '_AO_LUM_Shader'
                    if mc.ls(luminanceNode):
                        mc.delete(luminanceNode)
                    # 创建
                    AONode = mc.shadingNode('mib_amb_occlusion', asTexture= True, name = AONode)
                    shaderMRTrans = mc.shadingNode('mib_transparency', asTexture = True, name = shaderMRTrans)
                    shaderMain = mc.shadingNode('lambert', asShader = True, name = shaderMain)
                    shaderMR = mc.shadingNode('lambert', asShader = True, name = shaderMR)
                    luminanceNode = mc.shadingNode('luminance', asUtility = True, name = luminanceNode)
                    # 连接
                    try:
                        transpancyConnections = mc.listConnections((transpancySGNodes[i] + '.' + 'surfaceShader'), s=1, plugs=1)
                        mc.disconnectAttr(('%s') % (transpancyConnections[0]), ('%s.%s') % (transpancySGNodes[i], 'surfaceShader'))
                    except:
                        pass
                    mc.connectAttr((shaderMain + '.outColor'), (transpancySGNodes[i] + '.surfaceShader'))
                    miMaterialShader = mc.listConnections((transpancySGNodes[i] + '.miMaterialShader'),s = 1,plugs = 1)
                    if miMaterialShader:
                        mc.disconnectAttr(('%s') % (miMaterialShader[0]), ('%s.%s') % (transpancySGNodes[i], 'miMaterialShader'))
                    mc.connectAttr((shaderMRTrans + '.outValue'), (transpancySGNodes[i] + '.miMaterialShader'))
                    mc.connectAttr((AONode + '.outValueA'), (shaderMRTrans + '.inputA'))
                    mc.connectAttr((luminanceNode + '.outValue'), (shaderMRTrans + '.transpR'))
                    mc.connectAttr((luminanceNode + '.outValue'), (shaderMRTrans + '.transpG'))
                    mc.connectAttr((luminanceNode + '.outValue'), (shaderMRTrans + '.transpB'))
                    # 透明连接
                    self.ydRLTransShaderConnection(transpancyNode[i], luminanceNode,'value')
                    # file贴图反转
                    if '.outTransparency' in transpancyNode[i]:
                        mc.editRenderLayerAdjustment(transpancyNode[i].split('.')[0] + '.invert')
                        mc.setAttr((transpancyNode[i].split('.')[0] + ".invert"), 1)

                    # 设置AO
                    if(layerType[:3] in ['CHR','PRP']):
                        mc.setAttr(('%s.%s') % (AONode, 'samples'), 136)
                        mc.setAttr(('%s.%s') % (AONode, 'max_distance'), 2)
                        mc.setAttr(('%s.%s') % (AONode, 'output_mode'), 0)

                    if(layerType[:3] in ['SET','SPC']):
                        mc.setAttr(('%s.%s') % (AONode, 'samples'), 136)
                        mc.setAttr(('%s.%s') % (AONode, 'max_distance'), 10)
                        mc.setAttr(('%s.%s') % (AONode, 'output_mode'), 0)
                    # 着色
                    # 连接着色
                    shaderInfo = mc.listConnections((transpancySGNodes[i] + '.surfaceShader'),s = 1,plugs = 1)
                    if shaderInfo:
                        shaderInfo = shaderInfo[0]
                        mc.editRenderLayerAdjustment(transpancySGNodes[i] + '.surfaceShader')
                        mc.disconnectAttr(shaderInfo, (transpancySGNodes[i] + '.surfaceShader'))
                        mc.connectAttr((shaderMain + '.outColor'), (transpancySGNodes[i] + '.surfaceShader'), f=1)
            '''
            # 特殊物体着色
            if transpancySGNodes:
                for i in range(len(transpancySGNodes)):
                    if not mc.ls(transpancySGNodes[i]):
                        continue
                    #if transpancySGNodes[i] not in rlSGNodes:
                    #    continue
                    keySGInfo = str(i)
                    meshes = transpancyMeshes[i]
                    
                    # 有着色物体时才进行
                    if not meshes:
                        continue
                    # 创建
                    shaderTrans_Node = 'SHD_' + layerType + '_' + keySGInfo + '_AO_Shader'
                    if mc.ls(shaderTrans_Node):
                        mc.delete(shaderTrans_Node)
                    AOTrans_Node = 'SHD_'  + layerType + '_' + keySGInfo +  '_AO_Node'
                    if mc.ls(AOTrans_Node):
                        mc.delete(AOTrans_Node)
                    luminanceNode = 'SHD_' + layerType + '_' + keySGInfo + '_AO_LUM_Shader'
                    if mc.ls(luminanceNode):
                        mc.delete(luminanceNode)
                    # 经典连材质模式
                    if not SGOType:
                        AOTrans_SG = 'SHD_' + layerType + '_' + keySGInfo + '_AO_SG'
                        if mc.ls(AOTrans_SG):
                            mc.delete(AOTrans_SG)
                            
                    # 连接
                    shaderTrans_Node = mc.shadingNode('lambert', asShader=True, name = shaderTrans_Node)
                    AOTrans_Node = mc.shadingNode('mib_amb_occlusion', asTexture=True, name = AOTrans_Node)
                    luminanceNode = mc.shadingNode('luminance', asUtility = True, name = luminanceNode)
                    mc.setAttr((shaderTrans_Node + '.color'),1,1,1,type = 'double3')
                    mc.connectAttr((AOTrans_Node + '.outValue'), (shaderTrans_Node + '.ambientColor'))
                    mc.connectAttr((luminanceNode + '.outValue'), (shaderTrans_Node + '.transparencyR'))
                    mc.connectAttr((luminanceNode + '.outValue'), (shaderTrans_Node + '.transparencyG'))
                    mc.connectAttr((luminanceNode + '.outValue'), (shaderTrans_Node + '.transparencyB'))
                    # 经典连材质模式
                    if not SGOType:
                        AOTrans_SG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name = AOTrans_SG)
                        mc.connectAttr((shaderTrans_Node + '.outColor'), (AOTrans_SG + '.surfaceShader'))

                    # 透明连接
                    self.ydRLTransShaderConnection(transpancyNode[i], luminanceNode,'value')
                    
                    # file贴图反转
                    if '.outTransparency' in transpancyNode[i]:
                        mc.editRenderLayerAdjustment(transpancyNode[i].split('.')[0] + '.invert')
                        mc.setAttr((transpancyNode[i].split('.')[0] + ".invert"), 1)

                    # 设置AO
                    if(layerType[:3] in ['CHR','PRP']):
                        mc.setAttr(('%s.%s') % (AOTrans_Node, 'samples'), 136)
                        mc.setAttr(('%s.%s') % (AOTrans_Node, 'max_distance'), 2)
                        mc.setAttr(('%s.%s') % (AOTrans_Node, 'output_mode'), 0)

                    if(layerType[:3] in ['SET','SPC']):
                        mc.setAttr(('%s.%s') % (AOTrans_Node, 'samples'), 136)
                        mc.setAttr(('%s.%s') % (AOTrans_Node, 'max_distance'), 10)
                        mc.setAttr(('%s.%s') % (AOTrans_Node, 'output_mode'), 0)
                        
                    # 着色
                    # SG连接着色
                    if SGOType:
                        shaderInfo = mc.listConnections((transpancySGNodes[i] + '.surfaceShader'),s = 1,plugs = 1)
                        print shaderInfo
                        if shaderInfo:
                            shaderInfo = shaderInfo[0]
                            mc.editRenderLayerAdjustment(transpancySGNodes[i] + '.surfaceShader')
                            mc.disconnectAttr(shaderInfo, (transpancySGNodes[i] + '.surfaceShader'))
                            mc.connectAttr((shaderTrans_Node + '.outColor'), (transpancySGNodes[i] + '.surfaceShader'), f=1)
                            #mc.connectAttr((shaderMain + '.outColor'), (transpancySGNodes[i] + '.surfaceShader'), f=1)

                    # 经典着色
                    if not SGOType:
                        # 物体赋予
                        if shaderForece == 0:
                            faceGrps = []
                            for mesh in meshes:
                                if '.f[' in mesh:
                                    faceGrps.append(mesh.split('.f[')[0])
                            if faceGrps:
                                faceGrps = list(set(faceGrps))
                                try:
                                    mc.sets(faceGrps,e = 1 , forceElement = AO_SG)
                                except:
                                    for grp in faceGrps:
                                        try:
                                            mc.sets(grp,e = 1 , forceElement = AO_SG)
                                        except:
                                            print u'===有物体无法赋予材质==='
                                            print grp
                                            mc.error(u'===有物体无法赋予材质===')
                        if shaderForece == 1:
                            meshesReserve = self.ydRLFaceObjReverse(meshes)
                            try:
                                mc.sets(meshesReserve,e = 1 , forceElement = AO_SG)
                            except:
                                for mesh in meshesReserve:
                                    if not mesh:
                                        continue
                                    try:
                                        mc.sets(mesh,e = 1 , forceElement = AO_SG)
                                    except:
                                        print u'===有物体无法赋予材质==='
                                        print mesh
                                        mc.error(u'===有物体无法赋予材质===')

                        # 选面
                        try:
                            mc.sets(meshes,e = 1 , forceElement = AO_SG)
                        except:
                            for mesh in meshes:
                                try:
                                    mc.sets(mesh,e = 1 , forceElement = AOTrans_SG)
                                except:
                                    print u'===有物体无法赋予材质==='
                                    print mesh
                                    mc.error(u'===有物体无法赋予材质===')

            # 设置
            # self.ydRLCommonConfig()

            # 渲染设置
            mc.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')

            # 开启光线追踪
            mc.editRenderLayerAdjustment('miDefaultOptions.rayTracing')
            mc.setAttr('miDefaultOptions.rayTracing', 1)

            # FG开启
            mc.editRenderLayerAdjustment('miDefaultOptions.finalGather')
            mc.setAttr('miDefaultOptions.finalGather', 0)

            # cam背景色
            if createMode:
                shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
                camName = 'CAM:*_'  + shotInfo[1] + '_' + shotInfo[2] + '_' +  shotInfo[3] + '_baked'
                if not mc.ls(camName):
                    from idmt.maya.commonCore.core_mayaCommon import sk_hbExportCam
                    reload(sk_hbExportCam)
                    sk_hbExportCam.sk_hbExportCam().camServerReference(3)
                    if not mc.ls(camName):
                        print u'===没发现最终CAM==='
                        mc.error(u'===没发现最终CAM===')
                camName = mc.ls(camName,type = 'transform')[0]
                camShape = mc.listRelatives(camName, s = 1, ni = 1)[0]
                print '---'
                print camShape
                try:
                    mc.editRenderLayerAdjustment( camShape + '.backgroundColor')
                    mc.setAttr(( camShape + '.backgroundColor'), 1, 1, 1, type='double3')
                except:
                    pass
            
            # exr
            if createMode:
                self.ydRLFramebuffer('iff',3)

            print (u'===============!!!Done  【%s】!!!===============' % (u'%s_AO层' % layerType))
            print '\n'

        else:
            print (u'===============!!!Error  【%s】无物体!!!===============' % (u'%s_AO层' % layerType))
            print '\n'

    # Normal层
    # No Lights
    # 放弃与AO类似部分，直接amb_occ连shader的color，trans连shader的trans
    def ydRLNMCreate(self, layerType, selectObjType=0 , SGOType = 0 , shaderForece = 0 ,createMode = 1,createName = ''):
        print (u'===============!!!Start 【%s】!!!===============' % (u'%s_NM层' % layerType))
        print 'Working...'

        # 物体信息
        rlObjs      = []
        MaskObjs    = []
        layerName   = ''
        rlSGNodes   = []
        rlLights    = []
        layerObjs   = []
        if selectObjType == 0:
            needInfo = self.ydRLObjsInfo(layerType,'NM')
            rlObjs    = needInfo[0]
            MaskObjs  = needInfo[1]
            layerName = needInfo[2]
            rlSGNodes = needInfo[3]
            rlLights  = needInfo[4]
            layerObjs = needInfo[5]

        # 选取模式
        if selectObjType == 1:
            rlObjs    = self.ydRLSelectMode()
            layerObjs = rlObjs
            layerName = createName + '_NM'

        if layerObjs:
            transpancyObjs = [[],[],[],[]]

            # 特殊处理，半透明用
            # 获取信息必须在masterLayer进行
            if createMode:
                transpancyObjs    = self.ydRLTransparencyObjsByType(layerObjs,layerType)
                
            transpancySGNodes = transpancyObjs[0]
            transpancyMeshes  = transpancyObjs[1]
            transpancyNode    = transpancyObjs[2]
            transpancyGrps    = transpancyObjs[3]

            # allTransMeshes
            allTransGrps = []
            for info in transpancyGrps:
                allTransGrps = allTransGrps + info
            if allTransGrps:
                allTransGrps = list(set(allTransGrps))
                
            # 创建RenderLayer
            if mc.ls(layerName):
                mc.delete(layerName)

            mc.createRenderLayer((rlObjs), name=layerName, noRecurse=1, makeCurrent=1)

            # Mask显示|隐藏
            if MaskObjs:
                meshes = mc.listRelatives(MaskObjs ,ni = 1 , ad = 1 , type = 'mesh',f = 1)
                if meshes:
                    for mesh in meshes:
                        #mc.editRenderLayerAdjustment(mesh + '.primaryVisibility')
                        #mc.setAttr((mesh + '.primaryVisibility'),l = 0)
                        mc.setAttr((mesh + '.primaryVisibility'), 0)
                        #mc.editRenderLayerAdjustment(mesh + '.receiveShadows')
                        #mc.setAttr((mesh + '.receiveShadows'), l = 0)
                        mc.setAttr((mesh + '.receiveShadows'), 0)
                        
            # NM层，眉毛隐藏，其他五官隐藏
            if layerType[:3] in ['CHR']:
                objsNeedHide = self.ydRLGBowObjs() 
                objsNeedHide = self.ydRLFaceObjs() + objsNeedHide
                if objsNeedHide:
                    for obj in objsNeedHide:
                        #mc.lockNode((obj + '.v'), l = 0)
                        #self.ydRLDeleteConnection((obj + '.v'))
                        #mc.editRenderLayerAdjustment(obj + '.v')
                        mc.setAttr((obj + '.v'), 0)  

            # 通用NM材质
            shader_Node = 'SHD_' + layerType + '_NM_Shader'
            if mc.ls(shader_Node):
                mc.delete(shader_Node)
            NM_Node = 'SHD_' + layerType + '_NM_Node'
            if mc.ls(NM_Node):
                mc.delete(NM_Node)
            # 经典连材质模式
            if not SGOType:
                NM_SG = 'SHD_' + layerType + '_NM_SG'
                if mc.ls(NM_SG):
                    mc.delete(NM_SG)
                
            shader_Node = mc.shadingNode('lambert', asShader=True, name=shader_Node)
            NM_Node = mc.shadingNode('mib_amb_occlusion', asTexture=True, name=NM_Node)
            mc.setAttr(('%s.%s') % (shader_Node, 'ambientColor'), 1,1,1,type = 'double3')
            mc.connectAttr((NM_Node + '.outValue'), (shader_Node + '.color'))
            # 经典连材质模式
            if not SGOType:
                NM_SG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name = NM_SG)
                mc.connectAttr((shader_Node + '.outColor'), (NM_SG + '.surfaceShader'))

            if(layerType[:3] in ['CHR','PRP']):
                mc.setAttr(('%s.%s') % (NM_Node, 'samples'), 136)
                mc.setAttr(('%s.%s') % (NM_Node, 'max_distance'), 0)
                mc.setAttr(('%s.%s') % (NM_Node, 'output_mode'), 3)

            if(layerType[:3] in ['SET','SPC']):
                mc.setAttr(('%s.%s') % (NM_Node, 'samples'), 136)
                mc.setAttr(('%s.%s') % (NM_Node, 'max_distance'), 0)
                mc.setAttr(('%s.%s') % (NM_Node, 'output_mode'), 3)

            # 优先全局着色
            # 经典连材质模式
            if not SGOType:
                # layerObjs 类型必然是transform
                for obj in layerObjs:
                    # 属于matter
                    if obj in MaskObjs:
                        continue
                    if obj in transpancyGrps:
                        continue
                    mesh = mc.listRelatives(obj,s = 1 ,ni  = 1, type = 'mesh',f=1)
                    if not mesh:
                        continue
                    mesh = mesh[0]
                    shaderSG = NM_SG
                    mc.select(mesh)
                    try:
                        mc.sets(mesh,e = 1 , forceElement = shaderSG)
                    except:
                        print u'===有物体无法赋予材质==='
                        print mesh
                        mc.error(u'===有物体无法赋予材质===')
            
            # SG连接模式
            if SGOType:
                if rlSGNodes:
                    for SGNode in rlSGNodes:
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
                    if not mc.ls(transpancySGNodes[i]):
                        continue
                    #if transpancySGNodes[i] not in rlSGNodes:
                    #    continue
                    keySGInfo = str(i)
                    meshes = transpancyMeshes[i]
                    
                    # 有着色物体时才进行
                    if not meshes:
                        continue
                    
                    shaderTrsNode = 'SHD_' + layerType + '_' + keySGInfo + '_NM_Shader'
                    if mc.ls(shaderTrsNode):
                        mc.delete(shaderTrsNode)
                    NMTrsNode = 'SHD_' + layerType + '_' + keySGInfo + '_NM_Node'
                    if mc.ls(NMTrsNode):
                        mc.delete(NMTrsNode)
                    luminanceNode = 'SHD_' + layerType + '_' + keySGInfo + '_NM_LUM_Shader'
                    if mc.ls(luminanceNode):
                        mc.delete(luminanceNode)
                    # 经典连材质模式
                    if not SGOType:
                        NMTrans_SG = 'SHD_' + layerType + '_' + keySGInfo + '_NM_SG'
                        if mc.ls(NMTrans_SG):
                            mc.delete(NMTrans_SG)
                            
                    # 创建
                    shaderTrsNode = mc.shadingNode('lambert', asShader=True, name=shaderTrsNode)
                    NMTrsNode = mc.shadingNode('mib_amb_occlusion', asTexture=True, name=NMTrsNode)
                    luminanceNode = mc.shadingNode('luminance', asUtility = True, name = luminanceNode)
                    # 连接
                    mc.setAttr(('%s.%s') % (shaderTrsNode, 'ambientColor'), 1,1,1,type = 'double3')
                    mc.connectAttr((NMTrsNode + '.outValue'), (shaderTrsNode + '.color'))
                    mc.connectAttr((luminanceNode + '.outValue'), (shaderTrsNode + '.transparencyR'))
                    mc.connectAttr((luminanceNode + '.outValue'), (shaderTrsNode + '.transparencyG'))
                    mc.connectAttr((luminanceNode + '.outValue'), (shaderTrsNode + '.transparencyB'))
                    # 经典连材质模式
                    if not SGOType:
                        NMTrans_SG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name = NMTrans_SG)
                        mc.connectAttr((shaderTrsNode + '.outColor'), (NMTrans_SG + '.surfaceShader'))

                    # 透明连接
                    self.ydRLTransShaderConnection(transpancyNode[i], luminanceNode, 'value')

                    # file贴图反转
                    if '.outTransparency' in transpancyNode[i]:
                        mc.editRenderLayerAdjustment(transpancyNode[i].split('.')[0] + '.invert')
                        mc.setAttr((transpancyNode[i].split('.')[0] + ".invert"), 1)

                    if(layerType[:3] in ['CHR','PRP']):
                        mc.setAttr(('%s.%s') % (NMTrsNode, 'samples'), 136)
                        mc.setAttr(('%s.%s') % (NMTrsNode, 'max_distance'), 0)
                        mc.setAttr(('%s.%s') % (NMTrsNode, 'output_mode'), 3)

                    if(layerType[:3] in ['SET','SPEC']):
                        mc.setAttr(('%s.%s') % (NMTrsNode, 'samples'), 136)
                        mc.setAttr(('%s.%s') % (NMTrsNode, 'max_distance'), 0)
                        mc.setAttr(('%s.%s') % (NMTrsNode, 'output_mode'), 3)

                    # 经典着色
                    if not SGOType:
                        # 物体赋予
                        if shaderForece == 0:
                            faceGrps = []
                            for mesh in meshes:
                                if '.f[' in mesh:
                                    faceGrps.append(mesh.split('.f[')[0])
                            if faceGrps:
                                faceGrps = list(set(faceGrps))
                                try:
                                    mc.sets(faceGrps,e = 1 , forceElement = NM_SG)
                                except:
                                    for grp in faceGrps:
                                        try:
                                            mc.sets(grp,e = 1 , forceElement = NM_SG)
                                        except:
                                            print u'===有物体无法赋予材质==='
                                            print grp
                                            mc.error(u'===有物体无法赋予材质===')
                        if shaderForece == 1:
                            meshesReserve = self.ydRLFaceObjReverse(meshes)
                            try:
                                mc.sets(meshesReserve,e = 1 , forceElement = NM_SG)
                            except:
                                for mesh in meshesReserve:
                                    if not mesh:
                                        continue
                                    try:
                                        mc.sets(mesh,e = 1 , forceElement = NM_SG)
                                    except:
                                        print u'===有物体无法赋予材质==='
                                        print mesh
                                        mc.error(u'===有物体无法赋予材质===')

                        # 选面
                        try:
                            mc.sets(meshes,e = 1 , forceElement = NMTrans_SG)
                        except:
                            for mesh in meshes:
                                try:
                                    mc.sets(mesh,e = 1 , forceElement = NMTrans_SG)
                                except:
                                    print u'===有物体无法赋予材质==='
                                    print mesh
                                    mc.error(u'===有物体无法赋予材质===')
                                
                    # SG连接着色
                    if SGOType:
                        shaderInfo = mc.listConnections((transpancySGNodes[i] + '.surfaceShader'),s = 1,plugs = 1)
                        if shaderInfo:
                            shaderInfo = shaderInfo[0]
                            mc.editRenderLayerAdjustment(transpancySGNodes[i] + '.surfaceShader')
                            mc.disconnectAttr(shaderInfo, (transpancySGNodes[i] + '.surfaceShader'))
                            mc.connectAttr((shaderTrsNode + '.outColor'), (transpancySGNodes[i] + '.surfaceShader'), f=1)



            # 设置
            # self.ydRLCommonConfig()
            
            # 渲染设置
            mc.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')

            # 关闭光线追踪
            mc.editRenderLayerAdjustment('miDefaultOptions.rayTracing')
            mc.setAttr('miDefaultOptions.rayTracing', 0)

            # exr
            if createMode:
                self.ydRLFramebuffer('iff',3)

            print (u'===============!!!Done  【%s】!!!===============' % (u'%s_NM层' % layerType))
            print '\n'
        else:
            print (u'===============!!!Error  【%s】无物体!!!===============' % (u'%s_NM层' % layerType))
            print '\n'

    # ZDEPTH层
    # No Lights
    def ydRLZDEPTHCreate(self, layerType, selectObjType=0, distance=500 , SGOType = 0 , shaderForece = 0 , createMode = 1,createName = ''):
        print (u'===============!!!Start 【%s】!!!===============' % (u'%s_ZDEPTH层' % layerType))
        print 'Working...'

        # 物体信息
        rlObjs      = []
        MaskObjs    = []
        layerName   = ''
        rlSGNodes   = []
        rlLights    = []
        layerObjs   = []
        if selectObjType == 0:
            needInfo = self.ydRLObjsInfo(layerType,'ZDP')
            rlObjs    = needInfo[0]
            MaskObjs  = needInfo[1]
            layerName = needInfo[2]
            rlSGNodes = needInfo[3]
            rlLights  = needInfo[4]
            layerObjs = needInfo[5]

        # 选取模式
        if selectObjType == 1:
            rlObjs    = self.ydRLSelectMode()
            layerObjs = rlObjs
            layerName = createName + '_ZDP'

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
        if intState:
            distance = 500
        else:
            distance = 500
 
        # excel
        if createMode:
            shotData = self.ydRLReadServerData()
            try:
                if shotData[3]:
                    zdepthCreate = shotData[3]
                    tempLayerObjs = []
                    if 'F' in zdepthCreate and layerType[-1] == 'F':
                        tempLayerObjs = layerObjs
                    if 'M' in zdepthCreate and layerType[-1] == 'M':
                        tempLayerObjs = layerObjs
                    if 'B' in zdepthCreate and layerType[-1] == 'B':
                        tempLayerObjs = layerObjs
                    layerObjs = tempLayerObjs
                if shotData[4]:
                    zdepthValue = float(shotData[4])
                    if zdepthValue:
                        distance = zdepthValue
            except:
                print u'===请注意，本镜头zpdeth数据不是有效数值==='
                mc.error(u'===请注意，本镜头zpdeth数据不是有效数值===')

        if layerObjs:
            transpancyObjs = [[],[],[],[]]
            
            # 特殊处理，半透明用
            # 获取信息必须在masterLayer进行
            if createMode:
                transpancyObjs    = self.ydRLTransparencyObjsByType(layerObjs,layerType)
            transpancySGNodes = transpancyObjs[0]
            transpancyMeshes  = transpancyObjs[1]
            transpancyNode    = transpancyObjs[2]
            transpancyGrps    = transpancyObjs[3]

            # allTransMeshes
            allTransGrps = []
            for info in transpancyGrps:
                allTransGrps = allTransGrps + info
            if allTransGrps:
                allTransGrps = list(set(allTransGrps))
                
            # 创建RenderLayer
            if mc.ls(layerName):
                mc.delete(layerName)

            mc.createRenderLayer((rlObjs), name=layerName, noRecurse=1, makeCurrent=1)
            
            # Mask显示|隐藏
            if MaskObjs:
                meshes = mc.listRelatives(MaskObjs ,ni = 1 , ad = 1 , type = 'mesh',f = 1)
                if meshes:
                    for mesh in meshes:
                        #mc.editRenderLayerAdjustment(mesh + '.primaryVisibility')
                        #mc.setAttr((mesh + '.primaryVisibility'),l = 0)
                        mc.setAttr((mesh + '.primaryVisibility'), 0)
                        #mc.editRenderLayerAdjustment(mesh + '.receiveShadows')
                        #mc.setAttr((mesh + '.receiveShadows'), l = 0)
                        mc.setAttr((mesh + '.receiveShadows'), 0)
                        
            # ZPDEPTH层，眉毛隐藏，其他五官隐藏
            if layerType[:3] in ['CHR']:
                objsNeedHide = self.ydRLGBowObjs() 
                objsNeedHide = self.ydRLFaceObjs() + objsNeedHide
                if objsNeedHide:
                    for obj in objsNeedHide:
                        #mc.lockNode((obj + '.v'), l = 0)
                        #self.ydRLDeleteConnection((obj + '.v'))
                        #mc.editRenderLayerAdjustment(obj + '.v')
                        mc.setAttr((obj + '.v'), 0)
            
            # 创建备用材质组
            shader_Node = 'SHD_' + layerType + '_ZDP_Shader'
            if mc.ls(shader_Node):
                mc.delete(shader_Node)
            setRange_Z = 'SHD_' + layerType + '_ZDP_setRangeZ'
            if mc.ls(setRange_Z):
                mc.delete(setRange_Z)
            multDiv_Z = 'SHD_' + layerType + '_ZDP_multDivZ'
            if mc.ls(multDiv_Z):
                mc.delete(multDiv_Z)
            sampleInfo_Z = 'SHD_' + layerType + '_ZDP_sampInfoZ'
            if mc.ls(sampleInfo_Z):
                mc.delete(sampleInfo_Z)
            # 经典连材质模式
            if not SGOType:
                ZDP_SG = 'SHD_' + layerType + '_ZDP_SG'
                if mc.ls(ZDP_SG):
                    mc.delete(ZDP_SG)

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
            # 经典连材质模式
            if not SGOType:
                ZDP_SG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name = ZDP_SG)
                mc.connectAttr((shader_Node + '.outColor'), (ZDP_SG + '.surfaceShader'))

            # 连接
            mc.connectAttr(('%s.%s') % (setRange_Node, 'outValueX'), ('%s.%s') % (shader_Node, 'colorR'), f=True)
            mc.connectAttr(('%s.%s') % (setRange_Node, 'outValueX'), ('%s.%s') % (shader_Node, 'colorG'), f=True)
            mc.connectAttr(('%s.%s') % (setRange_Node, 'outValueX'), ('%s.%s') % (shader_Node, 'colorB'), f=True)
            mc.connectAttr(('%s.%s') % (samplerInfo_Node, 'NearClipCalimero'), ('%s.%s') % (setRange_Node, 'oldMinX'), f=True)
            mc.connectAttr(('%s.%s') % (samplerInfo_Node, 'FarClipCalimero'), ('%s.%s') % (setRange_Node, 'oldMaxX'), f=True)
            mc.connectAttr(('%s.%s') % (samplerInfo_Node, 'pointCameraZ'), ('%s.%s') % (multiplyDivide_Node, 'input1X'), f=True)
            mc.connectAttr(('%s.%s') % (multiplyDivide_Node, 'outputX'), ('%s.%s') % (setRange_Node, 'valueX'), f=True)
            
            # 优先全局着色
            # 经典连材质模式
            if not SGOType:
                # layerObjs 类型必然是transform
                for obj in layerObjs:
                    # 属于matter
                    if obj in MaskObjs:
                        continue
                    if obj in transpancyGrps:
                        continue
                    mesh = mc.listRelatives(obj,s = 1 ,ni  = 1, type = 'mesh',f=1)
                    if not mesh:
                        continue
                    mesh = mesh[0]
                    shaderSG = ZDP_SG
                    mc.select(mesh)
                    try:
                        mc.sets(mesh,e = 1 , forceElement = shaderSG)
                    except:
                        print u'===有物体无法赋予材质==='
                        print mesh
                        mc.error(u'===有物体无法赋予材质===')
                        
            # SG连接着色
            if SGOType:
                if rlSGNodes:
                    for SGNode in rlSGNodes:
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
                    if not mc.ls(transpancySGNodes[i]):
                        continue
                    #if transpancySGNodes[i] not in rlSGNodes:
                    #    continue
                    keySGInfo = str(i)
                    meshes = transpancyMeshes[i]
                    
                    # 有着色物体时才进行
                    if not meshes:
                        continue
            
                    shaderTrsNode = 'SHD_' + layerType + '_' + keySGInfo + '_ZDP_Shader'
                    if mc.ls(shaderTrsNode):
                        mc.delete(shaderTrsNode)
                    setRangeZ = 'SHD_' + layerType + '_' + keySGInfo + '_ZDP_setRangeZ'
                    if mc.ls(setRangeZ):
                        mc.delete(setRangeZ)
                    multDivZ = 'SHD_' + layerType + '_' + keySGInfo + '_ZDP_multDivZ'
                    if mc.ls(multDivZ):
                        mc.delete(multDivZ)
                    sampleInfoZ = 'SHD_' + layerType + '_' + keySGInfo + '_ZDP_sampInfoZ'
                    if mc.ls(sampleInfoZ):
                        mc.delete(sampleInfoZ)
                    luminanceNode = 'SHD_' + layerType + '_' + keySGInfo + '_ZDP_LUM_Shader'
                    if mc.ls(luminanceNode):
                        mc.delete(luminanceNode)
                    # 经典连材质模式
                    if not SGOType:
                        ZDPTransSG = 'SHD_' + layerType + '_' + keySGInfo + '_ZDP_SG'
                        if mc.ls(ZDPTransSG):
                            mc.delete(ZDPTransSG)

                    shaderTrsNode = mc.shadingNode('lambert', asShader=True, name=shaderTrsNode)
                    mc.setAttr((shaderTrsNode + '.ambientColor'), 1, 1, 1, type='double3')
                    mc.setAttr((shaderTrsNode + '.diffuse'), 0)
                    setRangeNode = mc.shadingNode('setRange', asUtility=True, name=setRangeZ)
                    mc.setAttr((setRangeNode + '.minX'), 1)
                    multiplyDivideNode = mc.shadingNode('multiplyDivide', asUtility=True, name=multDivZ)
                    mc.setAttr((multiplyDivideNode + '.input2X'), -1)
                    samplerInfoNode = mc.shadingNode('samplerInfo', asUtility=True, name=sampleInfoZ)
                    mc.addAttr(samplerInfoNode, longName='NearClipCalimero', nn='Near Clip Calimero', attributeType='float', defaultValue=0.1)
                    mc.addAttr(samplerInfoNode, longName='FarClipCalimero', nn='Far Clip Calimero', attributeType='float', defaultValue=distance)
                    luminanceNode = mc.shadingNode('luminance', asUtility = True, name = luminanceNode)
                    # 经典连材质模式
                    if not SGOType:
                        ZDPTransSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name = ZDPTransSG)
                        mc.connectAttr((shaderTrsNode + '.outColor'), (ZDPTransSG + '.surfaceShader'))               
                    
                    # 连接
                    mc.connectAttr(('%s.%s') % (setRangeNode, 'outValueX'), ('%s.%s') % (shaderTrsNode, 'colorR'), f=True)
                    mc.connectAttr(('%s.%s') % (setRangeNode, 'outValueX'), ('%s.%s') % (shaderTrsNode, 'colorG'), f=True)
                    mc.connectAttr(('%s.%s') % (setRangeNode, 'outValueX'), ('%s.%s') % (shaderTrsNode, 'colorB'), f=True)
                    mc.connectAttr(('%s.%s') % (samplerInfoNode, 'NearClipCalimero'), ('%s.%s') % (setRangeNode, 'oldMinX'), f=True)
                    mc.connectAttr(('%s.%s') % (samplerInfoNode, 'FarClipCalimero'), ('%s.%s') % (setRangeNode, 'oldMaxX'), f=True)
                    mc.connectAttr(('%s.%s') % (samplerInfoNode, 'pointCameraZ'), ('%s.%s') % (multiplyDivideNode, 'input1X'), f=True)
                    mc.connectAttr(('%s.%s') % (multiplyDivideNode, 'outputX'), ('%s.%s') % (setRangeNode, 'valueX'), f=True)
                    mc.connectAttr((luminanceNode + '.outValue'), (shaderTrsNode + '.transparencyR'))
                    mc.connectAttr((luminanceNode + '.outValue'), (shaderTrsNode + '.transparencyG'))
                    mc.connectAttr((luminanceNode + '.outValue'), (shaderTrsNode + '.transparencyB'))
                    
                    # 透明连接
                    self.ydRLTransShaderConnection(transpancyNode[i], luminanceNode, 'value')

                    # 翻转
                    if '.outTransparency' in transpancyNode[i]:
                        mc.editRenderLayerAdjustment(transpancyNode[i].split('.')[0] + '.invert')
                        mc.setAttr((transpancyNode[i].split('.')[0] + ".invert"), 1)

                    # 经典着色
                    if not SGOType:
                        # 物体赋予
                        if shaderForece == 0:
                            faceGrps = []
                            for mesh in meshes:
                                if '.f[' in mesh:
                                    faceGrps.append(mesh.split('.f[')[0])
                            if faceGrps:
                                faceGrps = list(set(faceGrps))
                                try:
                                    mc.sets(faceGrps,e = 1 , forceElement = ZDP_SG)
                                except:
                                    for grp in faceGrps:
                                        try:
                                            mc.sets(grp,e = 1 , forceElement = ZDP_SG)
                                        except:
                                            print u'===有物体无法赋予材质==='
                                            print grp
                                            mc.error(u'===有物体无法赋予材质===')
                        if shaderForece == 1:
                            meshesReserve = self.ydRLFaceObjReverse(meshes)
                            try:
                                mc.sets(meshesReserve,e = 1 , forceElement = ZDP_SG)
                            except:
                                for mesh in meshesReserve:
                                    if not mesh:
                                        continue
                                    try:
                                        mc.sets(mesh,e = 1 , forceElement = ZDP_SG)
                                    except:
                                        print u'===有物体无法赋予材质==='
                                        print mesh
                                        mc.error(u'===有物体无法赋予材质===')
                        # 选面
                        try:
                            mc.sets(meshes,e = 1 , forceElement = ZDPTransSG)
                        except:
                            for mesh in meshes:
                                try:
                                    mc.sets(mesh,e = 1 , forceElement = ZDPTransSG)
                                except:
                                    print u'===有物体无法赋予材质==='
                                    print mesh
                                    mc.error(u'===有物体无法赋予材质===')
                                

                    # 连接着色
                    if SGOType:
                        shaderInfo = mc.listConnections((transpancySGNodes[i] + '.surfaceShader'),s = 1,plugs = 1)
                        if shaderInfo:
                            shaderInfo = shaderInfo[0]
                            mc.editRenderLayerAdjustment(transpancySGNodes[i] + '.surfaceShader')
                            mc.disconnectAttr(shaderInfo, (transpancySGNodes[i] + '.surfaceShader'))
                            mc.connectAttr((shaderTrsNode + '.outColor'), (transpancySGNodes[i] + '.surfaceShader'), f=1)

            # 渲染设置
            mc.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')

            # 关闭光线追踪
            mc.editRenderLayerAdjustment('miDefaultOptions.rayTracing')
            mc.setAttr('miDefaultOptions.rayTracing', 0)

            # exr
            if createMode:
                self.ydRLFramebuffer('iff',3)

            print (u'===============!!!Done  【%s】!!!===============' % (u'%s_ZDEPTH层' % layerType))
            print '\n'
        else:
            print (u'===============!!!Error  【%s】无物体!!!===============' % (u'%s_ZDEPTH层' % layerType))
            print '\n'

    
    # Fresnel层
    # No Lights
    def ydRLFNCreate(self, layerType, selectObjType=0 , SGOType = 0 , shaderForece = 0 , createMode = 1,createName = ''):
        print (u'===============!!!Start 【%s】!!!===============' % (u'%s_Fresnel层' % layerType))
        print 'Working...'

        # 物体信息
        rlObjs      = []
        MaskObjs    = []
        layerName   = ''
        rlSGNodes   = []
        rlLights    = []
        layerObjs   = []
        if selectObjType == 0:
            needInfo = self.ydRLObjsInfo(layerType,'FN')
            rlObjs    = needInfo[0]
            MaskObjs  = needInfo[1]
            layerName = needInfo[2]
            rlSGNodes = needInfo[3]
            rlLights  = needInfo[4]
            layerObjs = needInfo[5]

        # 选取模式
        if selectObjType == 1:
            rlObjs    = self.ydRLSelectMode()
            layerObjs = rlObjs
            layerName = createName + '_FN'

        if layerObjs:
            transpancyObjs = [[],[],[],[]]
            # 特殊处理，半透明用
            # 获取信息必须在masterLayer进行
            if createMode:
                transpancyObjs    = self.ydRLTransparencyObjsByType(layerObjs,layerType)
            transpancySGNodes = transpancyObjs[0]
            transpancyMeshes  = transpancyObjs[1]
            transpancyNode    = transpancyObjs[2]
            transpancyGrps    = transpancyObjs[3]

            # allTransMeshes
            allTransGrps = []
            for info in transpancyGrps:
                allTransGrps = allTransGrps + info
            if allTransGrps:
                allTransGrps = list(set(allTransGrps))
                
            # 创建RenderLayer
            if mc.ls(layerName):
                mc.delete(layerName)

            mc.createRenderLayer((rlObjs), name=layerName, noRecurse=1, makeCurrent=1)
            
            # Mask显示|隐藏
            if MaskObjs:
                meshes = mc.listRelatives(MaskObjs ,ni = 1 , ad = 1 , type = 'mesh',f = 1)
                if meshes:
                    for mesh in meshes:
                        #mc.editRenderLayerAdjustment(mesh + '.primaryVisibility')
                        #mc.setAttr((mesh + '.primaryVisibility'),l = 0)
                        mc.setAttr((mesh + '.primaryVisibility'), 0)
                        #mc.editRenderLayerAdjustment(mesh + '.receiveShadows')
                        #mc.setAttr((mesh + '.receiveShadows'), l = 0)
                        mc.setAttr((mesh + '.receiveShadows'), 0)
                        
            # Fresnel层，眉毛隐藏，其他五官隐藏
            if layerType[:3] in ['CHR']:
                objsNeedHide = self.ydRLGBowObjs() 
                objsNeedHide = self.ydRLFaceObjs()  + objsNeedHide
                if objsNeedHide:
                    for obj in objsNeedHide:
                        #mc.lockNode((obj + '.v'), l = 0)
                        #self.ydRLDeleteConnection((obj + '.v'))
                        #mc.editRenderLayerAdjustment(obj + '.v')
                        mc.setAttr((obj + '.v'), 0)
            
            # 创建备用材质组
            shader_Node = 'SHD_' + layerType + '_FN_Shader'
            if mc.ls(shader_Node):
                mc.delete(shader_Node)
            rampShader_FN = 'SHD_' + layerType + '_FN_Ramp'
            if mc.ls(rampShader_FN):
                mc.delete(rampShader_FN)
            sampleInfo_FN = 'SHD_' + layerType + '_FN_sampInfo'
            if mc.ls(sampleInfo_FN):
                mc.delete(sampleInfo_FN)
            place2d_FN = 'SHD_' + layerType + '_FN_place2d'
            if mc.ls(place2d_FN):
                mc.delete(place2d_FN)
            # 经典连材质模式
            if not SGOType:
                FN_SG = 'SHD_' + layerType + '_FN_SG'
                if mc.ls(FN_SG):
                    mc.delete(FN_SG)
                    
            #shader_Node = mc.shadingNode('surfaceShader', asShader=True, name=shader_Node)
            #mc.setAttr((shader_Node + '.outMatteOpacity'), 0, 0, 0, type='double3')
            shader_Node = mc.shadingNode('lambert', asShader=True, name= shader_Node)
            mc.setAttr((shader_Node + '.ambientColor'), 1, 1, 1, type='double3')
            mc.setAttr((shader_Node + '.diffuse'), 0)
            
            rampShader_FN = mc.shadingNode('ramp', asTexture=True, name=rampShader_FN)
            mc.removeMultiInstance((rampShader_FN + '.colorEntryList[1]'),b = 1)
            mc.setAttr((rampShader_FN + '.colorEntryList[0].color'),1,1,1,type = 'double3')
            mc.setAttr((rampShader_FN + '.colorEntryList[1].color'),0,0,0,type = 'double3')
            mc.setAttr((rampShader_FN + '.colorEntryList[1].position'),1)
            
            sampleInfo_FN = mc.shadingNode('samplerInfo', asUtility=True, name=sampleInfo_FN)
            
            place2d_FN = mc.shadingNode('place2dTexture', asUtility=True, name=place2d_FN)

            # 连接
            mc.connectAttr(('%s.%s') % (place2d_FN, 'outUV'), ('%s.%s') % (rampShader_FN, 'uvCoord'), f=True)
            mc.connectAttr(('%s.%s') % (sampleInfo_FN, 'facingRatio'), ('%s.%s') % (rampShader_FN, 'uCoord'), f=True)
            mc.connectAttr(('%s.%s') % (sampleInfo_FN, 'facingRatio'), ('%s.%s') % (rampShader_FN, 'vCoord'), f=True)
            mc.connectAttr(('%s.%s') % (rampShader_FN, 'outColor'), ('%s.%s') % (shader_Node, 'color'), f=True)
            # 经典着色
            if not SGOType:
                FN_SG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name = FN_SG)
                mc.connectAttr((shader_Node + '.outColor'), (FN_SG + '.surfaceShader'))
                
            # 优先全局着色
            # 经典连材质模式
            if not SGOType:
                # layerObjs 类型必然是transform
                for obj in layerObjs:
                    # 属于matter
                    if obj in MaskObjs:
                        continue
                    if obj in transpancyGrps:
                        continue
                    mesh = mc.listRelatives(obj,s = 1 ,ni  = 1, type = 'mesh',f=1)
                    if not mesh:
                        continue
                    mesh = mesh[0]
                    shaderSG = FN_SG
                    mc.select(mesh)
                    try:
                        mc.sets(mesh,e = 1 , forceElement = shaderSG)
                    except:
                        print u'===有物体无法赋予材质==='
                        print mesh
                        mc.error(u'===有物体无法赋予材质===')

            # SG连接模式
            if SGOType:
                if rlSGNodes:
                    for SGNode in rlSGNodes:
                        shaderInfo = mc.listConnections((SGNode + '.surfaceShader'),s = 1,plugs = 1)
                        if not shaderInfo:
                            continue
                        shaderInfo = shaderInfo[0]
                        mc.editRenderLayerAdjustment(SGNode + '.surfaceShader')
                        mc.disconnectAttr(shaderInfo, (SGNode + '.surfaceShader'))
                        mc.connectAttr((shader_Node + '.outColor'), (SGNode + '.surfaceShader'), f=1)

            # 特殊物体着色
#            if transpancySGNodes:
#                for i in range(len(transpancySGNodes)):
#                    if not mc.ls(transpancySGNodes[i]):
#                        continue
#                    #if transpancySGNodes[i] not in rlSGNodes:
#                    #    continue
#                    keySGInfo = str(i)
#                    meshes = transpancyMeshes[i]
#                    
#                    # 有着色物体时才进行
#                    if not meshes:
#                        continue
#                    
#                    shaderTrsNode = 'SHD_' + layerType  + '_' + keySGInfo + '_FN_Shader'
#                    if mc.ls(shaderTrsNode):
#                        mc.delete(shaderTrsNode)
#                    rampShaderFN = 'SHD_' + layerType + '_' + keySGInfo + '_FN_Ramp'
#                    if mc.ls(rampShaderFN):
#                        mc.delete(rampShaderFN)
#                    sampleInfoFN = 'SHD_' + layerType + '_' + keySGInfo + '_FN_sampInfo'
#                    if mc.ls(sampleInfoFN):
#                        mc.delete(sampleInfoFN)
#                    place2dFN = 'SHD_' + layerType + '_' + keySGInfo + '_FN_place2d'
#                    if mc.ls(place2dFN):
#                        mc.delete(place2dFN)
#                    luminanceNode = 'SHD_' + layerType + '_' + keySGInfo + '_FN_LUM_Shader'
#                    if mc.ls(luminanceNode):
#                        mc.delete(luminanceNode)
#                    # 经典连材质模式
#                    if not SGOType:
#                        FNTrsSG = 'SHD_' + layerType + '_' + keySGInfo + '_FN_SG'
#                        if mc.ls(FNTrsSG):
#                            mc.delete(FNTrsSG)
#                            
#                    #shaderTrsNode = mc.shadingNode('surfaceShader', asShader=True, name=shaderTrsNode)
#                    #mc.setAttr((shaderTrsNode + '.outMatteOpacity'), 0, 0, 0, type='double3')
#                    shaderTrsNode = mc.shadingNode('lambert', asShader=True, name=shaderTrsNode)
#                    mc.setAttr((shaderTrsNode + '.ambientColor'), 1, 1, 1, type='double3')
#                    mc.setAttr((shaderTrsNode + '.diffuse'), 0)
#                    
#                    rampShaderFN = mc.shadingNode('ramp', asTexture=True, name=rampShaderFN)
#                    mc.removeMultiInstance((rampShaderFN + '.colorEntryList[1]'),b = 1)
#                    mc.setAttr((rampShaderFN + '.colorEntryList[0].color'),1,1,1,type = 'double3')
#                    mc.setAttr((rampShaderFN + '.colorEntryList[1].color'),0,0,0,type = 'double3')
#                    mc.setAttr((rampShaderFN + '.colorEntryList[1].position'),1)
#                    
#                    luminanceNode = mc.shadingNode('luminance', asUtility = True, name = luminanceNode)
#                    sampleInfoFN = mc.shadingNode('samplerInfo', asUtility=True, name=sampleInfoFN)
#                    place2dFN = mc.shadingNode('place2dTexture', asUtility=True, name=place2dFN)
#                    # 经典连材质模式
#                    if not SGOType:
#                        FNTrsSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name = FNTrsSG)
#                        mc.connectAttr((shaderTrsNode + '.outColor'), (FNTrsSG + '.surfaceShader'))
#                    
#                    # 连接
#                    mc.connectAttr(('%s.%s') % (place2dFN, 'outUV'), ('%s.%s') % (rampShaderFN, 'uvCoord'), f=True)
#                    mc.connectAttr(('%s.%s') % (sampleInfoFN, 'facingRatio'), ('%s.%s') % (rampShaderFN, 'uCoord'), f=True)
#                    mc.connectAttr(('%s.%s') % (sampleInfoFN, 'facingRatio'), ('%s.%s') % (rampShaderFN, 'vCoord'), f=True)
#                    mc.connectAttr(('%s.%s') % (rampShaderFN, 'outColor'), ('%s.%s') % (shaderTrsNode, 'color'), f=True)
#                    mc.connectAttr((luminanceNode + '.outValue'), (shaderTrsNode + '.transparencyR'))
#                    mc.connectAttr((luminanceNode + '.outValue'), (shaderTrsNode + '.transparencyG'))
#                    mc.connectAttr((luminanceNode + '.outValue'), (shaderTrsNode + '.transparencyB'))
#                    
#                    # 透明连接
#                    self.ydRLTransShaderConnection(transpancyNode[i], luminanceNode, 'value')
#
#                    # 翻转
#                    if '.outTransparency' in transpancyNode[i]:
#                        mc.editRenderLayerAdjustment(transpancyNode[i].split('.')[0] + '.invert')
#                        mc.setAttr((transpancyNode[i].split('.')[0] + ".invert"), 1)
#
#                    # 经典着色
#                    if not SGOType:
#                        # 物体赋予
#                        if shaderForece == 0:
#                            faceGrps = []
#                            for mesh in meshes:
#                                if '.f[' in mesh:
#                                    faceGrps.append(mesh.split('.f[')[0])
#                            if faceGrps:
#                                faceGrps = list(set(faceGrps))
#                                try:
#                                    mc.sets(faceGrps,e = 1 , forceElement = FN_SG)
#                                except:
#                                    for grp in faceGrps:
#                                        try:
#                                            mc.sets(grp,e = 1 , forceElement = FN_SG)
#                                        except:
#                                            print u'===有物体无法赋予材质==='
#                                            print grp
#                                            mc.error(u'===有物体无法赋予材质===')
#                        if shaderForece == 1:
#                            meshesReserve = self.ydRLFaceObjReverse(meshes)
#                            try:
#                                mc.sets(mesh,e = 1 , forceElement = FN_SG)
#                            except:
#                                for mesh in meshesReserve:
#                                    if not mesh:
#                                        continue
#                                    try:
#                                        mc.sets(mesh,e = 1 , forceElement = FN_SG)
#                                    except:
#                                        print u'===有物体无法赋予材质==='
#                                        print mesh
#                                        mc.error(u'===有物体无法赋予材质===')
#
#                        # 选面
#                        try:
#                            mc.sets(meshes,e = 1 , forceElement = FNTrsSG)
#                        except:
#                            for mesh in meshes:
#                                try:
#                                    mc.sets(mesh,e = 1 , forceElement = FNTrsSG)
#                                except:
#                                    print u'===有物体无法赋予材质==='
#                                    print mesh
#                                    mc.error(u'===有物体无法赋予材质===')
#
#                    # SG连接连接着色
#                    if SGOType:
#                        shaderInfo = mc.listConnections((transpancySGNodes[i] + '.surfaceShader'),s = 1,plugs = 1)
#                        if shaderInfo:
#                            shaderInfo = shaderInfo[0]
#                            mc.editRenderLayerAdjustment(transpancySGNodes[i] + '.surfaceShader')
#                            mc.disconnectAttr(shaderInfo, (transpancySGNodes[i] + '.surfaceShader'))
#                            mc.connectAttr((shaderTrsNode + '.outColor'), (transpancySGNodes[i] + '.surfaceShader'), f=1)

            # 渲染设置
            mc.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')

            # 关闭光线追踪
            mc.editRenderLayerAdjustment('miDefaultOptions.rayTracing')
            mc.setAttr('miDefaultOptions.rayTracing', 0)

            # exr
            if createMode:
                self.ydRLFramebuffer('iff',3)

            print (u'===============!!!Done  【%s】!!!===============' % (u'%s_Fresnel层' % layerType))
            print '\n'
        else:
            print (u'===============!!!Error  【%s】无物体!!!===============' % (u'%s_Fresnel层' % layerType))
            print '\n'
    
            
    #----------------------------------------------------------------------------------------#
    # 【通用：RGB分层】
    # Author : 沈  康
    # Data   : 2013_11_18/2014_05_10
    # Data   : 2014_05_28/2014_06_08
    #-------------------------------------------------#

    #-------------------------------------------------#
    # RGB自动创建函数
    def ydRLRGBAutoCreate(self,layerType , shaderForece = 0):     
        # BSR
        self.ydRLRGBCreate((layerType + '_' + 'BSR') , shaderForece )
        # Back To MasterLayer
        mc.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
        # FBR
        self.ydRLRGBCreate((layerType + '_' + 'FBR') , shaderForece )
        # Back To MasterLayer
        mc.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
        # SPR
        self.ydRLRGBCreate((layerType + '_' + 'SPR') , shaderForece )
        # Back To MasterLayer
        mc.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
        

    #-------------------------------------------------#
    # 核心创建层函数,韩虹 2014 11 04 修改自沈康（同名函数）主要修改了面材质计算方法
    def ydRLRGBCreate(self,layerType , selectObjType=0, shaderForece = 0):
        print (u'===============!!!Start 【%s】!!!===============' % (u'%s_%s层' % (layerType.split('_')[0],layerType.split('_')[1])))
        print 'Working...'
    
        checkInfo = layerType.split('_')
        # 缺少物体
        # 物体信息
        needInfo = self.ydRLObjsInfo(checkInfo[0],checkInfo[1])
        rlObjs    = needInfo[0]
        MaskObjs  = needInfo[1]
        layerName = needInfo[2]
        rlSGNodes = needInfo[3]
        rlLights  = needInfo[4]
        layerObjs = needInfo[5]
        
        RObjs = rlObjs
        GObjs = MaskObjs[0]
        BObjs = MaskObjs[1]
        MObjs = MaskObjs[2]
    
        if layerObjs:
            # 处理RGBM
            needGrps  = [[],[],[],[]]
            needFaces = [[],[],[],[]]
            if checkInfo[-1] in ['BSR']:
                needGrps = [RObjs,GObjs,BObjs,MObjs]
            else:
                for i in range(4):
                    checkMeshes = []
                    checkGrps   = []
                    checkFaces  = []
                    if i == 0:
                        checkMeshes = RObjs
                    if i == 1:
                        checkMeshes = GObjs
                    if i == 2:
                        checkMeshes = BObjs
                    if i == 3:
                        checkMeshes = MObjs
                    for info in checkMeshes:
                        if '.f[' in info:
                            checkGrps.append(info.split('.f[')[0])
                            checkFaces.append(info.split('.f[')[0])
                        else:
                            checkGrps.append(mc.listRelatives(info,p=1,type='transform',f= 1)[0])
                    needGrps[i]  = checkGrps
                    needFaces[i] = checkFaces
            # 所有RGB物体
            RGrps =needGrps[0]
            GGrps =needGrps[1]
            BGrps =needGrps[2]
            MGrps =needGrps[3]
            # 选面给的物体
            RFaces = needFaces[0]
            GFaces = needFaces[1]
            BFaces = needFaces[2]
            MFaces = needFaces[3]
            
            # 有RGB信息的物体，非RGB的记录
            noRGBFaces = {}
            for i in range(4):
                grpInfos  = list(set(needGrps[i]))
                faceInfos = []
                if i == 0:
                    faceInfos = RObjs
                if i == 1:
                    faceInfos = GObjs
                if i == 2:
                    faceInfos = BObjs
                if i == 3:
                    faceInfos = MObjs
                if not grpInfos:
                    continue
                objKeys = noRGBFaces.keys()
                # 处理grp信息
                for j in range(len(grpInfos)):
                    # 标准创建
                    if grpInfos[j] not in objKeys:
                        noRGBFaces[grpInfos[j]] = []
                    # 处理face信息
                    for k in range(len(faceInfos)):
                        if grpInfos[j] in faceInfos[k]:
                            if '.f[' in faceInfos[k]:
                                noRGBFaces[grpInfos[j]].append(faceInfos[k])
            if noRGBFaces:
                objs = noRGBFaces.keys()
                for obj in objs:
                    noRGBFaces[obj] = self.ydRLFaceObjReverse(noRGBFaces[obj])
            matteObjs = []
            for obj in layerObjs:
                if checkInfo[-1] in ['BSR']:
                    if obj not in (RGrps + GGrps + BGrps + MGrps) :
                        matteObjs.append(obj)
                else:
                    mesh = mc.listRelatives(obj,ni = 1, s = 1,type = 'mesh',f = 1)
                    if not mesh:
                        continue
                    mesh = mesh[0]
                    if obj not in (RGrps + GGrps + BGrps + MGrps) :
                        matteObjs.append(mesh)          
            # 特殊处理，半透明用
            # 获取信息必须在masterLayer进行
            transpancyObjs    = self.ydRLTransparencyObjsByType((RObjs + GObjs + BObjs + MObjs),layerType)
            transpancySGNodes = transpancyObjs[0]
            transpancyMeshes  = transpancyObjs[1]
            transpancyNode    = transpancyObjs[2]
            transpancyGrps    = transpancyObjs[3]
    
            # allTransMeshes
            allTransGrps = []
            for info in transpancyGrps:
                allTransGrps = allTransGrps + info
            if allTransGrps:
                allTransGrps = list(set(allTransGrps))
                
            # 创建RenderLayer
            if mc.ls(layerName):
                mc.delete(layerName)
    
            mc.createRenderLayer((layerObjs), name=layerName, noRecurse=1, makeCurrent=1)
            
            # 材质球准备工作
            
            # matter
            shader_Matte = 'SHD_' + checkInfo[0] + '_' + checkInfo[1] + '_Matte' + '_Shader'
            if mc.ls(shader_Matte):
                mc.delete(shader_Matte)
            MatteSG = 'SHD_' + checkInfo[0] + '_' + checkInfo[1] + '_Matte_SG'
            if mc.ls(MatteSG):
                mc.delete(MatteSG)
            shader_Matte = mc.shadingNode('lambert', asShader=True, name = shader_Matte)
            MatteSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name = MatteSG)
            # 连接
            mc.setAttr((shader_Matte + '.color'), 0, 0, 0, type='double3')
            mc.setAttr((shader_Matte + '.ambientColor'), 1, 1, 1, type='double3')
            mc.setAttr((shader_Matte + '.diffuse'), 0)
            mc.setAttr((shader_Matte + '.matteOpacityMode'), 0)
            mc.connectAttr((shader_Matte + '.outColor'), (MatteSG + '.surfaceShader'))
            
            # 材质球组 R
            shader_R_Node = 'SHD_' + checkInfo[0] + '_R_' + checkInfo[1] + '_Shader'
            if mc.ls(shader_R_Node):
                mc.delete(shader_R_Node)
            RSG = 'SHD_' + checkInfo[0] + '_R_' + checkInfo[1] + '_SG'
            if mc.ls(RSG):
                mc.delete(RSG)
            shader_R_Node = mc.shadingNode('lambert', asShader=True, name = shader_R_Node)
            RSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name = RSG)
            # 连接
            mc.setAttr((shader_R_Node + '.color'), 1, 0, 0, type='double3')
            mc.setAttr((shader_R_Node + '.ambientColor'), 1, 1, 1, type='double3')
            mc.setAttr((shader_R_Node + '.diffuse'), 1)
            mc.setAttr((shader_R_Node + '.matteOpacityMode'), 2)
            mc.setAttr((shader_R_Node + '.matteOpacity'), 0)
            mc.connectAttr((shader_R_Node + '.outColor'), (RSG + '.surfaceShader'))
            
            # 材质球组 G
            shader_G_Node = 'SHD_' + checkInfo[0] + '_G_' + checkInfo[1] + '_Shader'
            if mc.ls(shader_G_Node):
                mc.delete(shader_G_Node)
            GSG = 'SHD_' + checkInfo[0] + '_G_' + checkInfo[1] + '_SG'
            if mc.ls(GSG):
                mc.delete(GSG)
            shader_G_Node = mc.shadingNode('lambert', asShader=True, name = shader_G_Node)
            GSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name = GSG)
            # 连接
            mc.setAttr((shader_G_Node + '.color'), 0, 1, 0, type='double3')
            mc.setAttr((shader_G_Node + '.ambientColor'), 1, 1, 1, type='double3')
            mc.setAttr((shader_G_Node + '.diffuse'), 1)
            mc.setAttr((shader_G_Node + '.matteOpacityMode'), 2)
            mc.setAttr((shader_G_Node + '.matteOpacity'), 0)
            mc.connectAttr((shader_G_Node + '.outColor'), (GSG + '.surfaceShader'))
            
            # 材质球组 B
            shader_B_Node = 'SHD_' + checkInfo[0] + '_B_' + checkInfo[1] + '_Shader'
            if mc.ls(shader_B_Node):
                mc.delete(shader_B_Node)
            BSG = 'SHD_' + checkInfo[0] + '_B_' + checkInfo[1] + '_SG'
            if mc.ls(BSG):
                mc.delete(BSG)
            shader_B_Node = mc.shadingNode('lambert', asShader=True, name = shader_B_Node)
            BSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name = BSG)
            # 连接
            mc.setAttr((shader_B_Node + '.color'), 0, 0, 1, type='double3')
            mc.setAttr((shader_B_Node + '.ambientColor'), 1, 1, 1, type='double3')
            mc.setAttr((shader_B_Node + '.diffuse'), 1)
            mc.setAttr((shader_B_Node + '.matteOpacityMode'), 2)
            mc.setAttr((shader_B_Node + '.matteOpacity'), 0)
            mc.connectAttr((shader_B_Node + '.outColor'), (BSG + '.surfaceShader'))
            
            # 材质球组 M
            shader_M_Node = 'SHD_' + checkInfo[0] + '_M_' + checkInfo[1] + '_Shader'
            if mc.ls(shader_M_Node):
                mc.delete(shader_M_Node)
            MSG = 'SHD_' + checkInfo[0] + '_M_' + checkInfo[1] + '_SG'
            if mc.ls(MSG):
                mc.delete(MSG)
            shader_M_Node = mc.shadingNode('lambert', asShader=True, name = shader_M_Node)
            MSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name = MSG)
            # 连接
            mc.setAttr((shader_M_Node + '.color'), 0, 0, 0, type='double3')
            mc.setAttr((shader_M_Node + '.ambientColor'), 1, 1, 1, type='double3')
            mc.setAttr((shader_M_Node + '.diffuse'), 0)
            mc.setAttr((shader_M_Node + '.matteOpacityMode'), 2)
            mc.setAttr((shader_M_Node + '.matteOpacity'), 1)
            mc.connectAttr((shader_M_Node + '.outColor'), (MSG + '.surfaceShader'))
                
            # 分类
            shaderSG = ''
            # layerObjs 类型必然是transform
            from idmt.maya.commonCore.core_mayaCommon import sk_pyCommon
            reload(sk_pyCommon)
            doNotMatterObjs = []
            for obj in layerObjs:
                checkObj = ''
                if checkInfo[-1] in ['BSR']:
                    checkObj = obj
                else:
                    checkObj = mc.listRelatives(obj,s = 1 , ni = 1 ,type = 'mesh',f = 1)
                    if not checkObj:
                        continue
                    else:
                        checkObj = checkObj[0]
                        
                # 属于matter
                if checkObj in matteObjs:
                    if mc.nodeType(obj) == 'mesh':
                        mesh = mc.ls(obj,l = 1)[0]
                    else:
                        mesh = mc.listRelatives(obj,s = 1 ,ni  = 1, type = 'mesh',f=1)
                        if not mesh:
                            continue
                        mesh = mesh[0]
                    shaderSG = MatteSG
                    if not mc.ls(mesh):
                        continue
                    mc.select(mesh)
                    try:
                        mc.sets(mesh,e = 1 , forceElement = shaderSG)
                    except:
                        print u'===有物体无法赋予材质==='
                        print mesh
                        mc.error(u'===有物体无法赋予材质===')
                    
                # 不属于matter

                # 确定不属于透明物体
                if obj not in allTransGrps:
                    RGBMeshes = []
                    shaderSG = ''
                    # 精确处理：先处理非选面的物体
                    if shaderForece:
                        faceObjKeys = noRGBFaces.keys()
                        if obj in faceObjKeys and obj not in doNotMatterObjs:
                            noRGBMeshes = noRGBFaces[obj]
                            shaderSG = MatteSG
                            #meshesReserve = self.ydRLFaceObjReverse(noRGBMeshes)
                            # matter只上一次
                            doNotMatterObjs.append(obj)
                            try:
                                mc.sets(noRGBMeshes,e = 1 , forceElement = shaderSG)
                            except:
                                for mesh in noRGBMeshes:
                                    if not mesh:
                                        continue
                                    try:
                                        mc.sets(mesh,e = 1 , forceElement = shaderSG)
                                    except:
                                        print u'===有物体无法赋予材质==='
                                        print mesh
                                        mc.error(u'===有物体无法赋予材质===')
                    # 先整体着色
                    if not shaderForece:
                        # [选面者]整体着色
                        if obj in (RFaces + GFaces + BFaces + MFaces):
                            # matter只上一次
                            if obj not in doNotMatterObjs:
                                mesh = mc.listRelatives(obj,s = 1,ni =1,type = 'mesh',f=1)
                                if not mesh:
                                    continue
                                mesh = mesh[0]
                                shaderSG = MatteSG
                                # matter只上一次
                                doNotMatterObjs.append(obj)
                                try:
                                    mc.sets(mesh,e = 1 , forceElement = shaderSG)
                                except:
                                    print u'===有物体无法赋予材质==='
                                    print mesh
                                    mc.error(u'===有物体无法赋予材质===')
                    # 判断是RGBM中哪一类
                    if obj in MGrps:
                        grpIds = sk_pyCommon.sk_pyCommon().checkListSameAllIndex(MGrps,obj)
                        RGBMeshes = []
                        for idNum in grpIds:
                            RGBMeshes.append(MObjs[idNum])
                        shaderSG = MSG
                        try:
                            mc.sets(RGBMeshes,e = 1 , forceElement = shaderSG)
                        except:
                            for mesh in RGBMeshes:
                                try:
                                    mc.sets(mesh,e = 1 , forceElement = shaderSG)
                                except:
                                    print u'===有物体无法赋予材质==='
                                    print mesh
                                    mc.error(u'===有物体无法赋予材质===')     
                    if mc.ls(mc.listRelatives(obj,s=1,f=1)) and mc.listRelatives(obj,s=1,f=1)[0] in MGrps:
                        grpIds = sk_pyCommon.sk_pyCommon().checkListSameAllIndex(MGrps,mc.listRelatives(obj,s=1,f=1)[0])
                        RGBMeshes = []
                        for idNum in grpIds:
                            RGBMeshes.append(MObjs[idNum])
                        shaderSG = MSG
                        try:
                            mc.sets(RGBMeshes,e = 1 , forceElement = shaderSG)
                        except:
                            for mesh in RGBMeshes:
                                try:
                                    mc.sets(mesh,e = 1 , forceElement = shaderSG)
                                except:
                                    print u'===有物体无法赋予材质==='
                                    print mesh
                                    mc.error(u'===有物体无法赋予材质===')                                          
                    
                    if obj in RGrps :
                        grpIds = sk_pyCommon.sk_pyCommon().checkListSameAllIndex(RGrps,obj)
                        RGBMeshes = []
                        for idNum in grpIds:
                            RGBMeshes.append(RObjs[idNum])
                        shaderSG = RSG
                        try:
                            mc.sets(RGBMeshes,e = 1 , forceElement = shaderSG)
                        except:
                            for mesh in RGBMeshes:
                                try:
                                    mc.sets(mesh,e = 1 , forceElement = shaderSG)
                                except:
                                    print u'===有物体无法赋予材质==='
                                    print mesh
                                    mc.error(u'===有物体无法赋予材质===')
                    if mc.ls(mc.listRelatives(obj,s=1,f=1)) and mc.listRelatives(obj,s=1,f=1)[0] in RGrps:
                        grpIds = sk_pyCommon.sk_pyCommon().checkListSameAllIndex(RGrps,mc.listRelatives(obj,s=1,f=1)[0])
                        RGBMeshes = []
                        for idNum in grpIds:
                            RGBMeshes.append(RObjs[idNum])
                        shaderSG = RSG
                        try:
                            mc.sets(RGBMeshes,e = 1 , forceElement = shaderSG)
                        except:
                            for mesh in RGBMeshes:
                                try:
                                    mc.sets(mesh,e = 1 , forceElement = shaderSG)
                                except:
                                    print u'===有物体无法赋予材质==='
                                    print mesh
                                    mc.error(u'===有物体无法赋予材质===')
                                    
                    if obj in GGrps:
                        grpIds = sk_pyCommon.sk_pyCommon().checkListSameAllIndex(GGrps,obj)
                        RGBMeshes = []
                        for idNum in grpIds:
                            RGBMeshes.append(GObjs[idNum])
                        shaderSG = GSG
                        try:
                            mc.sets(RGBMeshes,e = 1 , forceElement = shaderSG)
                        except:
                            for mesh in RGBMeshes:
                                try:
                                    mc.sets(mesh,e = 1 , forceElement = shaderSG)
                                except:
                                    print u'===有物体无法赋予材质==='
                                    print mesh
                                    mc.error(u'===有物体无法赋予材质===')
                    if mc.ls(mc.listRelatives(obj,s=1,f=1)) and mc.listRelatives(obj,s=1,f=1)[0] in GGrps:
                        grpIds = sk_pyCommon.sk_pyCommon().checkListSameAllIndex(GGrps,mc.listRelatives(obj,s=1,f=1)[0])
                        RGBMeshes = []
                        for idNum in grpIds:
                            RGBMeshes.append(GObjs[idNum])
                        shaderSG = GSG
                        try:
                            mc.sets(RGBMeshes,e = 1 , forceElement = shaderSG)
                        except:
                            for mesh in RGBMeshes:
                                try:
                                    mc.sets(mesh,e = 1 , forceElement = shaderSG)
                                except:
                                    print u'===有物体无法赋予材质==='
                                    print mesh
                                    mc.error(u'===有物体无法赋予材质===')                                        


                    if obj in BGrps:
                        grpIds = sk_pyCommon.sk_pyCommon().checkListSameAllIndex(BGrps,obj)
                        RGBMeshes = []
                        for idNum in grpIds:
                            RGBMeshes.append(BObjs[idNum])
                        shaderSG = BSG
                        try:
                            mc.sets(RGBMeshes,e = 1 , forceElement = shaderSG)
                        except:
                            for mesh in RGBMeshes:
                                try:
                                    mc.sets(mesh,e = 1 , forceElement = shaderSG)
                                except:
                                    print u'===有物体无法赋予材质==='
                                    print mesh
                                    mc.error(u'===有物体无法赋予材质===')                                        
                               
                    if mc.ls(mc.listRelatives(obj,s=1,f=1)) and mc.listRelatives(obj,s=1,f=1)[0] in BGrps:
                        grpIds = sk_pyCommon.sk_pyCommon().checkListSameAllIndex(BGrps,mc.listRelatives(obj,s=1,f=1)[0])
                        RGBMeshes = []
                        for idNum in grpIds:
                            RGBMeshes.append(BObjs[idNum])
                        shaderSG = BSG
                        try:
                            mc.sets(RGBMeshes,e = 1 , forceElement = shaderSG)
                        except:
                            for mesh in RGBMeshes:
                                try:
                                    mc.sets(mesh,e = 1 , forceElement = shaderSG)
                                except:
                                    print u'===有物体无法赋予材质==='
                                    print mesh
                                    mc.error(u'===有物体无法赋予材质===')   
    
            # [优先]_特殊物体着色
            if transpancySGNodes:
                for i in range(len(transpancySGNodes)):
                    if not mc.ls(transpancySGNodes[i]):
                        continue
                    keySGInfo = str(i)
                    meshes = transpancyMeshes[i]
                    # 有着色物体时才进行
                    if not meshes:
                        continue
                    # 透明物体处理
                    RMeshes = []
                    GMeshes = []
                    BMeshes = []
                    MMeshes = []
                    
                    for mesh in meshes:
                        if '.f[' in mesh:
                            grp = mesh.split('.f[')[0]
                        else:
                            grp = mc.listRelatives(mesh , p = 1 , type = 'transform' , f= 1)[0]
                        if grp in RGrps:
                            RMeshes.append(mesh)
                        if grp in GGrps:
                            GMeshes.append(mesh)
                        if grp in BGrps:
                            BMeshes.append(mesh)
                        if grp in MGrps:
                            MMeshes.append(mesh)
                    
                    keyInfo  = ''
                    keyColor = []
                    
                    if RMeshes:
                        keyInfo  = 'R'
                        keyColor = [1,0,0]
                        # 材质球组
                        shader_R_Trs_Node = 'SHD_' + layerType + '_' + keySGInfo +  '_Trs_' + keyInfo + '_' + checkInfo[1] + '_Shader'
                        if mc.ls(shader_R_Trs_Node):
                            mc.delete(shader_R_Trs_Node)
                        R_TrsSG = 'SHD_' + layerType + '_' + keySGInfo + '_Trs_' + keyInfo + '_' + checkInfo[1] + '_SG'
                        if mc.ls(R_TrsSG):
                            mc.delete(R_TrsSG)
                        luminanceR_Node = 'SHD_' + layerType + '_' + keySGInfo + '_' + keyInfo + '_LUM_Shader'
                        if mc.ls(luminanceR_Node):
                            mc.delete(luminanceR_Node)
                        # 连接
                        shader_R_Trs_Node = mc.shadingNode('lambert', asShader=True, name = shader_R_Trs_Node)
                        R_TrsSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name = R_TrsSG)
                        luminanceR_Node = mc.shadingNode('luminance', asUtility = True, name = luminanceR_Node)
                        mc.setAttr((shader_R_Trs_Node + '.color'), keyColor[0], keyColor[1], keyColor[2], type='double3')
                        mc.setAttr((shader_R_Trs_Node + '.ambientColor'), 1, 1, 1, type='double3')
                        mc.setAttr((shader_R_Trs_Node + '.diffuse'), 0)
                        mc.setAttr((shader_R_Trs_Node + '.matteOpacityMode'), 2)
                        mc.setAttr((shader_R_Trs_Node + '.matteOpacity'), 0)
                        mc.connectAttr((shader_R_Trs_Node + '.outColor'), (R_TrsSG + '.surfaceShader'))
                        mc.connectAttr((luminanceR_Node + '.outValue'), (shader_R_Trs_Node + '.transparencyR'))
                        mc.connectAttr((luminanceR_Node + '.outValue'), (shader_R_Trs_Node + '.transparencyG'))
                        mc.connectAttr((luminanceR_Node + '.outValue'), (shader_R_Trs_Node + '.transparencyB'))
                        # 透明连接
                        self.ydRLTransShaderConnection(transpancyNode[i], luminanceR_Node, 'value')
    
                    if GMeshes:
                        keyInfo  = 'G'
                        keyColor = [0,1,0]
                        # 材质球组
                        shader_G_Trs_Node = 'SHD_' + layerType + '_' + keySGInfo +  '_Trs_' + keyInfo + '_' + checkInfo[1] + '_Shader'
                        if mc.ls(shader_G_Trs_Node):
                            mc.delete(shader_G_Trs_Node)
                        G_TrsSG = 'SHD_' + layerType + '_' + keySGInfo + '_Trs_' + keyInfo + '_' + checkInfo[1] + '_SG'
                        if mc.ls(G_TrsSG):
                            mc.delete(G_TrsSG)
                        luminanceG_Node = 'SHD_' + layerType + '_' + keySGInfo + '_' + keyInfo + '_LUM_Shader'
                        if mc.ls(luminanceG_Node):
                            mc.delete(luminanceG_Node)
                        # 连接
                        shader_G_Trs_Node = mc.shadingNode('lambert', asShader=True, name = shader_G_Trs_Node)
                        G_TrsSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name = G_TrsSG)
                        luminanceG_Node = mc.shadingNode('luminance', asUtility = True, name = luminanceG_Node)
                        mc.setAttr((shader_G_Trs_Node + '.color'), keyColor[0], keyColor[1], keyColor[2], type='double3')
                        mc.setAttr((shader_G_Trs_Node + '.ambientColor'), 1, 1, 1, type='double3')
                        mc.setAttr((shader_G_Trs_Node + '.diffuse'), 0)
                        mc.setAttr((shader_G_Trs_Node + '.matteOpacityMode'), 2)
                        mc.setAttr((shader_G_Trs_Node + '.matteOpacity'), 0)
                        mc.connectAttr((shader_G_Trs_Node + '.outColor'), (G_TrsSG + '.surfaceShader'))
                        mc.connectAttr((luminanceG_Node + '.outValue'), (shader_G_Trs_Node + '.transparencyR'))
                        mc.connectAttr((luminanceG_Node + '.outValue'), (shader_G_Trs_Node + '.transparencyG'))
                        mc.connectAttr((luminanceG_Node + '.outValue'), (shader_G_Trs_Node + '.transparencyB'))
                        # 透明连接
                        self.ydRLTransShaderConnection(transpancyNode[i], luminanceG_Node, 'value')
                        
                    if BMeshes:
                        keyInfo  = 'B'
                        keyColor = [0,0,1]
                        # 材质球组
                        shader_B_Trs_Node = 'SHD_' + layerType + '_' + keySGInfo +  '_Trs_' + keyInfo + '_' + checkInfo[1] + '_Shader'
                        if mc.ls(shader_B_Trs_Node):
                            mc.delete(shader_B_Trs_Node)
                        B_TrsSG = 'SHD_' + layerType + '_' + keySGInfo + '_Trs_' + keyInfo + '_' + checkInfo[1] + '_SG'
                        if mc.ls(B_TrsSG):
                            mc.delete(B_TrsSG)
                        luminanceB_Node = 'SHD_' + layerType + '_' + keySGInfo + '_' + keyInfo + '_LUM_Shader'
                        if mc.ls(luminanceB_Node):
                            mc.delete(luminanceB_Node)
                        # 连接
                        shader_B_Trs_Node = mc.shadingNode('lambert', asShader=True, name = shader_R_Trs_Node)
                        B_TrsSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name = B_TrsSG)
                        luminanceB_Node = mc.shadingNode('luminance', asUtility = True, name = luminanceB_Node)
                        mc.setAttr((shader_B_Trs_Node + '.color'), keyColor[0], keyColor[1], keyColor[2], type='double3')
                        mc.setAttr((shader_B_Trs_Node + '.ambientColor'), 1, 1, 1, type='double3')
                        mc.setAttr((shader_B_Trs_Node + '.diffuse'), 0)
                        mc.setAttr((shader_B_Trs_Node + '.matteOpacityMode'), 2)
                        mc.setAttr((shader_B_Trs_Node + '.matteOpacity'), 0)
                        mc.connectAttr((shader_B_Trs_Node + '.outColor'), (B_TrsSG + '.surfaceShader'))
                        mc.connectAttr((luminanceR_Node + '.outValue'), (shader_B_Trs_Node + '.transparencyR'))
                        mc.connectAttr((luminanceB_Node + '.outValue'), (shader_B_Trs_Node + '.transparencyG'))
                        mc.connectAttr((luminanceB_Node + '.outValue'), (shader_B_Trs_Node + '.transparencyB'))
                        # 透明连接
                        self.ydRLTransShaderConnection(transpancyNode[i], luminanceB_Node, 'value')
                        
                    if MMeshes:
                        keyInfo  = 'B'
                        keyColor = [0,0,0]
                        # 材质球组
                        shader_M_Trs_Node = 'SHD_' + layerType + '_' + keySGInfo +  '_Trs_' + keyInfo + '_' + checkInfo[1] + '_Shader'
                        if mc.ls(shader_M_Trs_Node):
                            mc.delete(shader_M_Trs_Node)
                        M_TrsSG = 'SHD_' + layerType + '_' + keySGInfo + '_Trs_' + keyInfo + '_' + checkInfo[1] + '_SG'
                        if mc.ls(M_TrsSG):
                            mc.delete(M_TrsSG)
                        luminanceM_Node = 'SHD_' + layerType + '_' + keySGInfo + '_' + keyInfo + '_LUM_Shader'
                        if mc.ls(luminanceM_Node):
                            mc.delete(luminanceM_Node)
                        # 连接
                        shader_M_Trs_Node = mc.shadingNode('lambert', asShader=True, name = shader_M_Trs_Node)
                        M_TrsSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name = M_TrsSG)
                        luminanceM_Node = mc.shadingNode('luminance', asUtility = True, name = luminanceM_Node)
                        mc.setAttr((shader_M_Trs_Node + '.color'), keyColor[0], keyColor[1], keyColor[2], type='double3')
                        mc.setAttr((shader_M_Trs_Node + '.ambientColor'), 1, 1, 1, type='double3')
                        mc.setAttr((shader_M_Trs_Node + '.diffuse'), 0)
                        mc.setAttr((shader_M_Trs_Node + '.matteOpacityMode'), 2)
                        mc.setAttr((shader_M_Trs_Node + '.matteOpacity'), 0)
                        mc.connectAttr((shader_M_Trs_Node + '.outColor'), (M_TrsSG + '.surfaceShader'))
                        mc.connectAttr((luminanceM_Node + '.outValue'), (shader_M_Trs_Node + '.transparencyR'))
                        mc.connectAttr((luminanceM_Node + '.outValue'), (shader_M_Trs_Node + '.transparencyG'))
                        mc.connectAttr((luminanceM_Node + '.outValue'), (shader_M_Trs_Node + '.transparencyB'))
                        # 透明连接
                        self.ydRLTransShaderConnection(transpancyNode[i], luminanceM_Node, 'value')
                        
                    # 非默认四大类者，不赋予材质
                    if not keyColor:
                        continue
    
                    # 翻转
                    if '.outTransparency' in transpancyNode[i]:
                        mc.editRenderLayerAdjustment(transpancyNode[i].split('.')[0] + '.invert')
                        mc.setAttr((transpancyNode[i].split('.')[0] + ".invert"), 1)
    
                    # 透明作色
                    for i in range(4):
                        if i == 0:
                            meshes = RMeshes
                            if meshes:
                                keyInfo = 'R'
                                baseSG = 'SHD_' + checkInfo[0] + '_' + keyInfo + '_' +  checkInfo[1] + '_SG'
                                shaderSG = 'SHD_'  + layerType + '_' + keySGInfo + '_Trs_' + keyInfo + '_' + checkInfo[1] + '_SG'
                        if i == 1:
                            meshes = GMeshes
                            if meshes:
                                keyInfo = 'G'
                                baseSG = 'SHD_' + checkInfo[0] + '_' + keyInfo + '_' +  checkInfo[1] + '_SG'
                                shaderSG = 'SHD_'  + layerType + '_' + keySGInfo + '_Trs_' + keyInfo + '_' + checkInfo[1] + '_SG'
                        if i == 3:
                            meshes = BMeshes
                            if meshes:
                                keyInfo = 'B'
                                baseSG = 'SHD_' + checkInfo[0] + '_' + keyInfo + '_' +  checkInfo[1] + '_SG'
                                shaderSG = 'SHD_'  + layerType + '_' + keySGInfo + '_Trs_' + keyInfo + '_' + checkInfo[1] + '_SG'
                        if i == 4:
                            meshes = MMeshes
                            if meshes:
                                keyInfo = 'M'
                                baseSG = 'SHD_' + checkInfo[0] + '_' + keyInfo + '_' +  checkInfo[1] + '_SG'
                                shaderSG = 'SHD_'  + layerType + '_' + keySGInfo + '_Trs_' + keyInfo + '_' + checkInfo[1] + '_SG'
                        if not meshes:
                            continue
                        
                        # 物体赋予
                        # 物体赋予
                        if shaderForece == 0:
                            faceGrps = []
                            for mesh in meshes:
                                if '.f[' in mesh:
                                    faceGrps.append(mesh.split('.f[')[0])
                            if faceGrps:
                                faceGrps = list(set(faceGrps))
                                try:
                                    mc.sets(faceGrps,e = 1 , forceElement = baseSG)
                                except:
                                    for grp in faceGrps:
                                        try:
                                            mc.sets(grp,e = 1 , forceElement = baseSG)
                                        except:
                                            print u'===有物体无法赋予材质==='
                                            print grp
                                            mc.error(u'===有物体无法赋予材质===')
                        if shaderForece == 1:
                            meshesReserve = self.ydRLFaceObjReverse(meshes)
                            try:
                                mc.sets(meshesReserve,e = 1 , forceElement = baseSG)
                            except:
                                for mesh in meshesReserve:
                                    if not mesh:
                                        continue
                                    try:
                                        mc.sets(mesh,e = 1 , forceElement = baseSG)
                                    except:
                                        print u'===有物体无法赋予材质==='
                                        print mesh
                                        mc.error(u'===有物体无法赋予材质===')
                        
                        # 选面
                        try:
                            mc.sets(meshes,e = 1 , forceElement = shaderSG)
                        except:
                            for mesh in meshes:
                                try:
                                    mc.sets(mesh,e = 1 , forceElement = shaderSG)
                                except:
                                    print u'===有物体无法赋予材质==='
                                    print mesh
                                    mc.error(u'===有物体无法赋予材质===')
                                #self.ydRLShaderAdd(mesh,MatteSG)
            # 渲染设置
            mc.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')
    
            # 关闭光线追踪
            mc.editRenderLayerAdjustment('miDefaultOptions.rayTracing')
            mc.setAttr('miDefaultOptions.rayTracing', 0)
    
            # exr
            self.ydRLFramebuffer('iff',3)
    
            print (u'===============!!!Done 【%s】!!!===============' % (u'%s_%s层' % (layerType.split('_')[0],layerType.split('_')[1])))
            print '\n'
        else:
            print (u'===============!!!Error 【%s】 无物体!!!===============' % (u'%s_%s层' % (layerType.split('_')[0],layerType.split('_')[1])))
            print '\n'    
    
#    def ydRLRGBCreate(self, layerType , selectObjType=0, shaderForece = 0):
#        print (u'===============!!!Start 【%s】!!!===============' % (u'%s_%s层' % (layerType.split('_')[0],layerType.split('_')[1])))
#        print 'Working...'
#
#        checkInfo = layerType.split('_')
#        # 缺少物体
#        # 物体信息
#        needInfo = self.ydRLObjsInfo(checkInfo[0],checkInfo[1])
#        rlObjs    = needInfo[0]
#        MaskObjs  = needInfo[1]
#        layerName = needInfo[2]
#        rlSGNodes = needInfo[3]
#        rlLights  = needInfo[4]
#        layerObjs = needInfo[5]
#        
#        RObjs = rlObjs
#        GObjs = MaskObjs[0]
#        BObjs = MaskObjs[1]
#        MObjs = MaskObjs[2]
#
#        matteObjs = []
#        for obj in layerObjs:
#            if checkInfo[-1] in ['BSR']:
#                if obj not in (RObjs + GObjs + BObjs + MObjs):
#                    matteObjs.append(obj)
#            else:
#                mesh = mc.listRelatives(obj,ni = 1, s = 1,type = 'mesh',f = 1)
#                if not mesh:
#                    continue
#                mesh = mesh[0]
#                if mesh not in (RObjs + GObjs + BObjs + MObjs):
#                    matteObjs.append(mesh)
#
#        if layerObjs:
#            # 处理RGBM
#            needGrps  = [[],[],[],[]]
#            needFaces = [[],[],[],[]]
#            if checkInfo[-1] in ['BSR']:
#                needGrps = [RObjs,GObjs,BObjs,MObjs]
#            else:
#                for i in range(4):
#                    checkMeshes = []
#                    checkGrps   = []
#                    checkFaces  = []
#                    if i == 0:
#                        checkMeshes = RObjs
#                    if i == 1:
#                        checkMeshes = GObjs
#                    if i == 2:
#                        checkMeshes = BObjs
#                    if i == 3:
#                        checkMeshes = MObjs
#                    for info in checkMeshes:
#                        if '.f[' in info:
#                            checkGrps.append(info.split('.f[')[0])
#                            checkFaces.append(info)
#                        else:
#                            checkGrps.append(mc.listRelatives(info,p=1,type='transform',f= 1)[0])
#                    needGrps[i]  = checkGrps
#                    needFaces[i] = checkFaces
#            # 所有RGB物体
#            RGrps =needGrps[0]
#            GGrps =needGrps[1]
#            BGrps =needGrps[2]
#            MGrps =needGrps[3]
#            # 选面给的物体
#            RFaces = needFaces[0]
#            GFaces = needFaces[1]
#            BFaces = needFaces[2]
#            MFaces = needFaces[3]
#            
#            # 有RGB信息的物体，非RGB的记录
#            noRGBFaces = {}
#            for i in range(4):
#                grpInfos  = list(set(needGrps[i]))
#                faceInfos = []
#                if i == 0:
#                    faceInfos = RObjs
#                if i == 1:
#                    faceInfos = GObjs
#                if i == 2:
#                    faceInfos = BObjs
#                if i == 3:
#                    faceInfos = MObjs
#                if not grpInfos:
#                    continue
#                objKeys = noRGBFaces.keys()
#                # 处理grp信息
#                for j in range(len(grpInfos)):
#                    # 标准创建
#                    if grpInfos[j] not in objKeys:
#                        noRGBFaces[grpInfos[j]] = []
#                    # 处理face信息
#                    for k in range(len(faceInfos)):
#                        if grpInfos[j] in faceInfos[k]:
#                            if '.f[' in faceInfos[k]:
#                                noRGBFaces[grpInfos[j]].append(faceInfos[k])
#            if noRGBFaces:
#                objs = noRGBFaces.keys()
#                for obj in objs:
#                    noRGBFaces[obj] = self.ydRLFaceObjReverse(noRGBFaces[obj])
#
#            # 特殊处理，半透明用
#            # 获取信息必须在masterLayer进行
#            transpancyObjs    = self.ydRLTransparencyObjsByType((RObjs + GObjs + BObjs + MObjs),layerType)
#            transpancySGNodes = transpancyObjs[0]
#            transpancyMeshes  = transpancyObjs[1]
#            transpancyNode    = transpancyObjs[2]
#            transpancyGrps    = transpancyObjs[3]
#
#            # allTransMeshes
#            allTransGrps = []
#            for info in transpancyGrps:
#                allTransGrps = allTransGrps + info
#            if allTransGrps:
#                allTransGrps = list(set(allTransGrps))
#                
#            # 创建RenderLayer
#            if mc.ls(layerName):
#                mc.delete(layerName)
#
#            mc.createRenderLayer((layerObjs), name=layerName, noRecurse=1, makeCurrent=1)
#            
#            # 材质球准备工作
#            
#            # matter
#            shader_Matte = 'SHD_' + checkInfo[0] + '_' + checkInfo[1] + '_Matte' + '_Shader'
#            if mc.ls(shader_Matte):
#                mc.delete(shader_Matte)
#            MatteSG = 'SHD_' + checkInfo[0] + '_' + checkInfo[1] + '_Matte_SG'
#            if mc.ls(MatteSG):
#                mc.delete(MatteSG)
#            shader_Matte = mc.shadingNode('lambert', asShader=True, name = shader_Matte)
#            MatteSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name = MatteSG)
#            # 连接
#            mc.setAttr((shader_Matte + '.color'), 0, 0, 0, type='double3')
#            mc.setAttr((shader_Matte + '.ambientColor'), 1, 1, 1, type='double3')
#            mc.setAttr((shader_Matte + '.diffuse'), 0)
#            mc.setAttr((shader_Matte + '.matteOpacityMode'), 0)
#            mc.connectAttr((shader_Matte + '.outColor'), (MatteSG + '.surfaceShader'))
#            
#            # 材质球组 R
#            shader_R_Node = 'SHD_' + checkInfo[0] + '_R_' + checkInfo[1] + '_Shader'
#            if mc.ls(shader_R_Node):
#                mc.delete(shader_R_Node)
#            RSG = 'SHD_' + checkInfo[0] + '_R_' + checkInfo[1] + '_SG'
#            if mc.ls(RSG):
#                mc.delete(RSG)
#            shader_R_Node = mc.shadingNode('lambert', asShader=True, name = shader_R_Node)
#            RSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name = RSG)
#            # 连接
#            mc.setAttr((shader_R_Node + '.color'), 1, 0, 0, type='double3')
#            mc.setAttr((shader_R_Node + '.ambientColor'), 1, 1, 1, type='double3')
#            mc.setAttr((shader_R_Node + '.diffuse'), 1)
#            mc.setAttr((shader_R_Node + '.matteOpacityMode'), 2)
#            mc.setAttr((shader_R_Node + '.matteOpacity'), 0)
#            mc.connectAttr((shader_R_Node + '.outColor'), (RSG + '.surfaceShader'))
#            
#            # 材质球组 G
#            shader_G_Node = 'SHD_' + checkInfo[0] + '_G_' + checkInfo[1] + '_Shader'
#            if mc.ls(shader_G_Node):
#                mc.delete(shader_G_Node)
#            GSG = 'SHD_' + checkInfo[0] + '_G_' + checkInfo[1] + '_SG'
#            if mc.ls(GSG):
#                mc.delete(GSG)
#            shader_G_Node = mc.shadingNode('lambert', asShader=True, name = shader_G_Node)
#            GSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name = GSG)
#            # 连接
#            mc.setAttr((shader_G_Node + '.color'), 0, 1, 0, type='double3')
#            mc.setAttr((shader_G_Node + '.ambientColor'), 1, 1, 1, type='double3')
#            mc.setAttr((shader_G_Node + '.diffuse'), 1)
#            mc.setAttr((shader_G_Node + '.matteOpacityMode'), 2)
#            mc.setAttr((shader_G_Node + '.matteOpacity'), 0)
#            mc.connectAttr((shader_G_Node + '.outColor'), (GSG + '.surfaceShader'))
#            
#            # 材质球组 B
#            shader_B_Node = 'SHD_' + checkInfo[0] + '_B_' + checkInfo[1] + '_Shader'
#            if mc.ls(shader_B_Node):
#                mc.delete(shader_B_Node)
#            BSG = 'SHD_' + checkInfo[0] + '_B_' + checkInfo[1] + '_SG'
#            if mc.ls(BSG):
#                mc.delete(BSG)
#            shader_B_Node = mc.shadingNode('lambert', asShader=True, name = shader_B_Node)
#            BSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name = BSG)
#            # 连接
#            mc.setAttr((shader_B_Node + '.color'), 0, 0, 1, type='double3')
#            mc.setAttr((shader_B_Node + '.ambientColor'), 1, 1, 1, type='double3')
#            mc.setAttr((shader_B_Node + '.diffuse'), 1)
#            mc.setAttr((shader_B_Node + '.matteOpacityMode'), 2)
#            mc.setAttr((shader_B_Node + '.matteOpacity'), 0)
#            mc.connectAttr((shader_B_Node + '.outColor'), (BSG + '.surfaceShader'))
#            
#            # 材质球组 M
#            shader_M_Node = 'SHD_' + checkInfo[0] + '_M_' + checkInfo[1] + '_Shader'
#            if mc.ls(shader_M_Node):
#                mc.delete(shader_M_Node)
#            MSG = 'SHD_' + checkInfo[0] + '_M_' + checkInfo[1] + '_SG'
#            if mc.ls(MSG):
#                mc.delete(MSG)
#            shader_M_Node = mc.shadingNode('lambert', asShader=True, name = shader_M_Node)
#            MSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name = MSG)
#            # 连接
#            mc.setAttr((shader_M_Node + '.color'), 0, 0, 0, type='double3')
#            mc.setAttr((shader_M_Node + '.ambientColor'), 1, 1, 1, type='double3')
#            mc.setAttr((shader_M_Node + '.diffuse'), 0)
#            mc.setAttr((shader_M_Node + '.matteOpacityMode'), 2)
#            mc.setAttr((shader_M_Node + '.matteOpacity'), 1)
#            mc.connectAttr((shader_M_Node + '.outColor'), (MSG + '.surfaceShader'))
#                
#            # 分类
#            shaderSG = ''
#            # layerObjs 类型必然是transform
#            from idmt.maya.commonCore.core_mayaCommon import sk_pyCommon
#            reload(sk_pyCommon)
#            doNotMatterObjs = []
#            for obj in layerObjs:
#                checkObj = ''
#                if checkInfo[-1] in ['BSR']:
#                    checkObj = obj
#                else:
#                    checkObj = mc.listRelatives(obj,s = 1 , ni = 1 ,type = 'mesh',f = 1)
#                    if not checkObj:
#                        continue
#                    else:
#                        checkObj = checkObj[0]
#                        
#                # 属于matter
#                if checkObj in matteObjs:
#                    if mc.nodeType(obj) == 'mesh':
#                        mesh = mc.ls(obj,l = 1)[0]
#                    else:
#                        mesh = mc.listRelatives(obj,s = 1 ,ni  = 1, type = 'mesh',f=1)
#                        if not mesh:
#                            continue
#                        mesh = mesh[0]
#                    shaderSG = MatteSG
#                    if not mc.ls(mesh):
#                        continue
#                    mc.select(mesh)
#                    try:
#                        mc.sets(mesh,e = 1 , forceElement = shaderSG)
#                    except:
#                        print u'===有物体无法赋予材质==='
#                        print mesh
#                        mc.error(u'===有物体无法赋予材质===')
#                    
#                # 不属于matter
#                else:
#                    # 确定不属于透明物体
#                    if obj not in allTransGrps:
#                        RGBMeshes = []
#                        shaderSG = ''
#                        # 精确处理：先处理非选面的物体
#                        if shaderForece:
#                            faceObjKeys = noRGBFaces.keys()
#                            if obj in faceObjKeys and obj not in doNotMatterObjs:
#                                noRGBMeshes = noRGBFaces[obj]
#                                shaderSG = MatteSG
#                                #meshesReserve = self.ydRLFaceObjReverse(noRGBMeshes)
#                                # matter只上一次
#                                doNotMatterObjs.append(obj)
#                                try:
#                                    mc.sets(noRGBMeshes,e = 1 , forceElement = shaderSG)
#                                except:
#                                    for mesh in noRGBMeshes:
#                                        if not mesh:
#                                            continue
#                                        try:
#                                            mc.sets(mesh,e = 1 , forceElement = shaderSG)
#                                        except:
#                                            print u'===有物体无法赋予材质==='
#                                            print mesh
#                                            mc.error(u'===有物体无法赋予材质===')
#                        # 先整体着色
#                        if not shaderForece:
#                            # [选面者]整体着色
#                            if obj in (RFaces + GFaces + BFaces + MFaces):
#                                # matter只上一次
#                                if obj not in doNotMatterObjs:
#                                    mesh = mc.listRelatives(obj,s = 1,ni =1,type = 'mesh',f=1)
#                                    if not mesh:
#                                        continue
#                                    mesh = mesh[0]
#                                    shaderSG = MatteSG
#                                    # matter只上一次
#                                    doNotMatterObjs.append(obj)
#                                    try:
#                                        mc.sets(mesh,e = 1 , forceElement = shaderSG)
#                                    except:
#                                        print u'===有物体无法赋予材质==='
#                                        print mesh
#                                        mc.error(u'===有物体无法赋予材质===')
#                        # 判断是RGBM中哪一类
#
#                        if obj in RGrps:
#                            grpIds = sk_pyCommon.sk_pyCommon().checkListSameAllIndex(RGrps,obj)
#                            RGBMeshes = []
#                            for idNum in grpIds:
#                                RGBMeshes.append(RObjs[idNum])
#                            shaderSG = RSG
#                            try:
#                                mc.sets(RGBMeshes,e = 1 , forceElement = shaderSG)
#                            except:
#                                for mesh in RGBMeshes:
#                                    try:
#                                        mc.sets(mesh,e = 1 , forceElement = shaderSG)
#                                    except:
#                                        print u'===有物体无法赋予材质==='
#                                        print mesh
#                                        mc.error(u'===有物体无法赋予材质===')
#                        if obj in GGrps:
#                            grpIds = sk_pyCommon.sk_pyCommon().checkListSameAllIndex(GGrps,obj)
#                            RGBMeshes = []
#                            for idNum in grpIds:
#                                RGBMeshes.append(GObjs[idNum])
#                            shaderSG = GSG
#                            try:
#                                mc.sets(RGBMeshes,e = 1 , forceElement = shaderSG)
#                            except:
#                                for mesh in RGBMeshes:
#                                    try:
#                                        mc.sets(mesh,e = 1 , forceElement = shaderSG)
#                                    except:
#                                        print u'===有物体无法赋予材质==='
#                                        print mesh
#                                        mc.error(u'===有物体无法赋予材质===')
#                        if obj in BGrps:
#                            grpIds = sk_pyCommon.sk_pyCommon().checkListSameAllIndex(BGrps,obj)
#                            RGBMeshes = []
#                            for idNum in grpIds:
#                                RGBMeshes.append(BObjs[idNum])
#                            shaderSG = BSG
#                            try:
#                                mc.sets(RGBMeshes,e = 1 , forceElement = shaderSG)
#                            except:
#                                for mesh in RGBMeshes:
#                                    try:
#                                        mc.sets(mesh,e = 1 , forceElement = shaderSG)
#                                    except:
#                                        print u'===有物体无法赋予材质==='
#                                        print mesh
#                                        mc.error(u'===有物体无法赋予材质===')
#
#
#            # [优先]_特殊物体着色
#            if transpancySGNodes:
#                for i in range(len(transpancySGNodes)):
#                    if not mc.ls(transpancySGNodes[i]):
#                        continue
#                    keySGInfo = str(i)
#                    meshes = transpancyMeshes[i]
#                    # 有着色物体时才进行
#                    if not meshes:
#                        continue
#                    # 透明物体处理
#                    RMeshes = []
#                    GMeshes = []
#                    BMeshes = []
#                    MMeshes = []
#                    
#                    for mesh in meshes:
#                        if '.f[' in mesh:
#                            grp = mesh.split('.f[')[0]
#                        else:
#                            grp = mc.listRelatives(mesh , p = 1 , type = 'transform' , f= 1)[0]
#                        if grp in RGrps:
#                            RMeshes.append(mesh)
#                        if grp in GGrps:
#                            GMeshes.append(mesh)
#                        if grp in BGrps:
#                            BMeshes.append(mesh)
#                        if grp in MGrps:
#                            MMeshes.append(mesh)
#                    
#                    keyInfo  = ''
#                    keyColor = []
#                    
#                    if RMeshes:
#                        keyInfo  = 'R'
#                        keyColor = [1,0,0]
#                        # 材质球组
#                        shader_R_Trs_Node = 'SHD_' + layerType + '_' + keySGInfo +  '_Trs_' + keyInfo + '_' + checkInfo[1] + '_Shader'
#                        if mc.ls(shader_R_Trs_Node):
#                            mc.delete(shader_R_Trs_Node)
#                        R_TrsSG = 'SHD_' + layerType + '_' + keySGInfo + '_Trs_' + keyInfo + '_' + checkInfo[1] + '_SG'
#                        if mc.ls(R_TrsSG):
#                            mc.delete(R_TrsSG)
#                        luminanceR_Node = 'SHD_' + layerType + '_' + keySGInfo + '_' + keyInfo + '_LUM_Shader'
#                        if mc.ls(luminanceR_Node):
#                            mc.delete(luminanceR_Node)
#                        # 连接
#                        shader_R_Trs_Node = mc.shadingNode('lambert', asShader=True, name = shader_R_Trs_Node)
#                        R_TrsSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name = R_TrsSG)
#                        luminanceR_Node = mc.shadingNode('luminance', asUtility = True, name = luminanceR_Node)
#                        mc.setAttr((shader_R_Trs_Node + '.color'), keyColor[0], keyColor[1], keyColor[2], type='double3')
#                        mc.setAttr((shader_R_Trs_Node + '.ambientColor'), 1, 1, 1, type='double3')
#                        mc.setAttr((shader_R_Trs_Node + '.diffuse'), 0)
#                        mc.setAttr((shader_R_Trs_Node + '.matteOpacityMode'), 2)
#                        mc.setAttr((shader_R_Trs_Node + '.matteOpacity'), 0)
#                        mc.connectAttr((shader_R_Trs_Node + '.outColor'), (R_TrsSG + '.surfaceShader'))
#                        mc.connectAttr((luminanceR_Node + '.outValue'), (shader_R_Trs_Node + '.transparencyR'))
#                        mc.connectAttr((luminanceR_Node + '.outValue'), (shader_R_Trs_Node + '.transparencyG'))
#                        mc.connectAttr((luminanceR_Node + '.outValue'), (shader_R_Trs_Node + '.transparencyB'))
#                        # 透明连接
#                        self.ydRLTransShaderConnection(transpancyNode[i], luminanceR_Node, 'value')
#
#                    if GMeshes:
#                        keyInfo  = 'G'
#                        keyColor = [0,1,0]
#                        # 材质球组
#                        shader_G_Trs_Node = 'SHD_' + layerType + '_' + keySGInfo +  '_Trs_' + keyInfo + '_' + checkInfo[1] + '_Shader'
#                        if mc.ls(shader_G_Trs_Node):
#                            mc.delete(shader_G_Trs_Node)
#                        G_TrsSG = 'SHD_' + layerType + '_' + keySGInfo + '_Trs_' + keyInfo + '_' + checkInfo[1] + '_SG'
#                        if mc.ls(G_TrsSG):
#                            mc.delete(G_TrsSG)
#                        luminanceG_Node = 'SHD_' + layerType + '_' + keySGInfo + '_' + keyInfo + '_LUM_Shader'
#                        if mc.ls(luminanceG_Node):
#                            mc.delete(luminanceG_Node)
#                        # 连接
#                        shader_G_Trs_Node = mc.shadingNode('lambert', asShader=True, name = shader_G_Trs_Node)
#                        G_TrsSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name = G_TrsSG)
#                        luminanceG_Node = mc.shadingNode('luminance', asUtility = True, name = luminanceG_Node)
#                        mc.setAttr((shader_G_Trs_Node + '.color'), keyColor[0], keyColor[1], keyColor[2], type='double3')
#                        mc.setAttr((shader_G_Trs_Node + '.ambientColor'), 1, 1, 1, type='double3')
#                        mc.setAttr((shader_G_Trs_Node + '.diffuse'), 0)
#                        mc.setAttr((shader_G_Trs_Node + '.matteOpacityMode'), 2)
#                        mc.setAttr((shader_G_Trs_Node + '.matteOpacity'), 0)
#                        mc.connectAttr((shader_G_Trs_Node + '.outColor'), (G_TrsSG + '.surfaceShader'))
#                        mc.connectAttr((luminanceG_Node + '.outValue'), (shader_G_Trs_Node + '.transparencyR'))
#                        mc.connectAttr((luminanceG_Node + '.outValue'), (shader_G_Trs_Node + '.transparencyG'))
#                        mc.connectAttr((luminanceG_Node + '.outValue'), (shader_G_Trs_Node + '.transparencyB'))
#                        # 透明连接
#                        self.ydRLTransShaderConnection(transpancyNode[i], luminanceG_Node, 'value')
#                        
#                    if BMeshes:
#                        keyInfo  = 'B'
#                        keyColor = [0,0,1]
#                        # 材质球组
#                        shader_B_Trs_Node = 'SHD_' + layerType + '_' + keySGInfo +  '_Trs_' + keyInfo + '_' + checkInfo[1] + '_Shader'
#                        if mc.ls(shader_B_Trs_Node):
#                            mc.delete(shader_B_Trs_Node)
#                        B_TrsSG = 'SHD_' + layerType + '_' + keySGInfo + '_Trs_' + keyInfo + '_' + checkInfo[1] + '_SG'
#                        if mc.ls(B_TrsSG):
#                            mc.delete(B_TrsSG)
#                        luminanceB_Node = 'SHD_' + layerType + '_' + keySGInfo + '_' + keyInfo + '_LUM_Shader'
#                        if mc.ls(luminanceB_Node):
#                            mc.delete(luminanceB_Node)
#                        # 连接
#                        shader_B_Trs_Node = mc.shadingNode('lambert', asShader=True, name = shader_R_Trs_Node)
#                        B_TrsSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name = B_TrsSG)
#                        luminanceB_Node = mc.shadingNode('luminance', asUtility = True, name = luminanceB_Node)
#                        mc.setAttr((shader_B_Trs_Node + '.color'), keyColor[0], keyColor[1], keyColor[2], type='double3')
#                        mc.setAttr((shader_B_Trs_Node + '.ambientColor'), 1, 1, 1, type='double3')
#                        mc.setAttr((shader_B_Trs_Node + '.diffuse'), 0)
#                        mc.setAttr((shader_B_Trs_Node + '.matteOpacityMode'), 2)
#                        mc.setAttr((shader_B_Trs_Node + '.matteOpacity'), 0)
#                        mc.connectAttr((shader_B_Trs_Node + '.outColor'), (B_TrsSG + '.surfaceShader'))
#                        mc.connectAttr((luminanceR_Node + '.outValue'), (shader_B_Trs_Node + '.transparencyR'))
#                        mc.connectAttr((luminanceB_Node + '.outValue'), (shader_B_Trs_Node + '.transparencyG'))
#                        mc.connectAttr((luminanceB_Node + '.outValue'), (shader_B_Trs_Node + '.transparencyB'))
#                        # 透明连接
#                        self.ydRLTransShaderConnection(transpancyNode[i], luminanceB_Node, 'value')
#                        
#                    if MMeshes:
#                        keyInfo  = 'B'
#                        keyColor = [0,0,0]
#                        # 材质球组
#                        shader_M_Trs_Node = 'SHD_' + layerType + '_' + keySGInfo +  '_Trs_' + keyInfo + '_' + checkInfo[1] + '_Shader'
#                        if mc.ls(shader_M_Trs_Node):
#                            mc.delete(shader_M_Trs_Node)
#                        M_TrsSG = 'SHD_' + layerType + '_' + keySGInfo + '_Trs_' + keyInfo + '_' + checkInfo[1] + '_SG'
#                        if mc.ls(M_TrsSG):
#                            mc.delete(M_TrsSG)
#                        luminanceM_Node = 'SHD_' + layerType + '_' + keySGInfo + '_' + keyInfo + '_LUM_Shader'
#                        if mc.ls(luminanceM_Node):
#                            mc.delete(luminanceM_Node)
#                        # 连接
#                        shader_M_Trs_Node = mc.shadingNode('lambert', asShader=True, name = shader_M_Trs_Node)
#                        M_TrsSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name = M_TrsSG)
#                        luminanceM_Node = mc.shadingNode('luminance', asUtility = True, name = luminanceM_Node)
#                        mc.setAttr((shader_M_Trs_Node + '.color'), keyColor[0], keyColor[1], keyColor[2], type='double3')
#                        mc.setAttr((shader_M_Trs_Node + '.ambientColor'), 1, 1, 1, type='double3')
#                        mc.setAttr((shader_M_Trs_Node + '.diffuse'), 0)
#                        mc.setAttr((shader_M_Trs_Node + '.matteOpacityMode'), 2)
#                        mc.setAttr((shader_M_Trs_Node + '.matteOpacity'), 0)
#                        mc.connectAttr((shader_M_Trs_Node + '.outColor'), (M_TrsSG + '.surfaceShader'))
#                        mc.connectAttr((luminanceM_Node + '.outValue'), (shader_M_Trs_Node + '.transparencyR'))
#                        mc.connectAttr((luminanceM_Node + '.outValue'), (shader_M_Trs_Node + '.transparencyG'))
#                        mc.connectAttr((luminanceM_Node + '.outValue'), (shader_M_Trs_Node + '.transparencyB'))
#                        # 透明连接
#                        self.ydRLTransShaderConnection(transpancyNode[i], luminanceM_Node, 'value')
#                        
#                    # 非默认四大类者，不赋予材质
#                    if not keyColor:
#                        continue
#
#                    # 翻转
#                    if '.outTransparency' in transpancyNode[i]:
#                        mc.editRenderLayerAdjustment(transpancyNode[i].split('.')[0] + '.invert')
#                        mc.setAttr((transpancyNode[i].split('.')[0] + ".invert"), 1)
#
#                    # 透明作色
#                    for i in range(4):
#                        if i == 0:
#                            meshes = RMeshes
#                            if meshes:
#                                keyInfo = 'R'
#                                baseSG = 'SHD_' + checkInfo[0] + '_' + keyInfo + '_' +  checkInfo[1] + '_SG'
#                                shaderSG = 'SHD_'  + layerType + '_' + keySGInfo + '_Trs_' + keyInfo + '_' + checkInfo[1] + '_SG'
#                        if i == 1:
#                            meshes = GMeshes
#                            if meshes:
#                                keyInfo = 'G'
#                                baseSG = 'SHD_' + checkInfo[0] + '_' + keyInfo + '_' +  checkInfo[1] + '_SG'
#                                shaderSG = 'SHD_'  + layerType + '_' + keySGInfo + '_Trs_' + keyInfo + '_' + checkInfo[1] + '_SG'
#                        if i == 3:
#                            meshes = BMeshes
#                            if meshes:
#                                keyInfo = 'B'
#                                baseSG = 'SHD_' + checkInfo[0] + '_' + keyInfo + '_' +  checkInfo[1] + '_SG'
#                                shaderSG = 'SHD_'  + layerType + '_' + keySGInfo + '_Trs_' + keyInfo + '_' + checkInfo[1] + '_SG'
#                        if i == 4:
#                            meshes = MMeshes
#                            if meshes:
#                                keyInfo = 'M'
#                                baseSG = 'SHD_' + checkInfo[0] + '_' + keyInfo + '_' +  checkInfo[1] + '_SG'
#                                shaderSG = 'SHD_'  + layerType + '_' + keySGInfo + '_Trs_' + keyInfo + '_' + checkInfo[1] + '_SG'
#                        if not meshes:
#                            continue
#                        
#                        # 物体赋予
#                        # 物体赋予
#                        if shaderForece == 0:
#                            faceGrps = []
#                            for mesh in meshes:
#                                if '.f[' in mesh:
#                                    faceGrps.append(mesh.split('.f[')[0])
#                            if faceGrps:
#                                faceGrps = list(set(faceGrps))
#                                try:
#                                    mc.sets(faceGrps,e = 1 , forceElement = baseSG)
#                                except:
#                                    for grp in faceGrps:
#                                        try:
#                                            mc.sets(grp,e = 1 , forceElement = baseSG)
#                                        except:
#                                            print u'===有物体无法赋予材质==='
#                                            print grp
#                                            mc.error(u'===有物体无法赋予材质===')
#                        if shaderForece == 1:
#                            meshesReserve = self.ydRLFaceObjReverse(meshes)
#                            try:
#                                mc.sets(meshesReserve,e = 1 , forceElement = baseSG)
#                            except:
#                                for mesh in meshesReserve:
#                                    if not mesh:
#                                        continue
#                                    try:
#                                        mc.sets(mesh,e = 1 , forceElement = baseSG)
#                                    except:
#                                        print u'===有物体无法赋予材质==='
#                                        print mesh
#                                        mc.error(u'===有物体无法赋予材质===')
#                        
#                        # 选面
#                        try:
#                            mc.sets(meshes,e = 1 , forceElement = shaderSG)
#                        except:
#                            for mesh in meshes:
#                                try:
#                                    mc.sets(mesh,e = 1 , forceElement = shaderSG)
#                                except:
#                                    print u'===有物体无法赋予材质==='
#                                    print mesh
#                                    mc.error(u'===有物体无法赋予材质===')
#                                #self.ydRLShaderAdd(mesh,MatteSG)
#
#            '''
#            # 创建备用材质组
#            if RObjs:
#                # 材质球组
#                shader_R_Node = 'SHD_' + chekInfo[0] + '_R_' + chekInfo[1] + '_Shader'
#                if mc.ls(shader_R_Node):
#                    mc.delete(shader_R_Node)
#                RSG = 'SHD_' + chekInfo[0] + '_R_' + chekInfo[1] + '_SG'
#                if mc.ls(RSG):
#                    mc.delete(RSG)
#                shader_R_Node = mc.shadingNode('lambert', asShader=True, name = shader_R_Node)
#                RSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name = RSG)
#                # 连接
#                mc.setAttr((shader_R_Node + '.color'), 1, 0, 0, type='double3')
#                mc.setAttr((shader_R_Node + '.ambientColor'), 1, 1, 1, type='double3')
#                mc.setAttr((shader_R_Node + '.diffuse'), 1)
#                mc.setAttr((shader_R_Node + '.matteOpacityMode'), 2)
#                mc.setAttr((shader_R_Node + '.matteOpacity'), 0)
#                mc.connectAttr((shader_R_Node + '.outColor'), (RSG + '.surfaceShader'))
#              
#            if GObjs:  
#                # 材质球组
#                shader_G_Node = 'SHD_' + chekInfo[0] + '_G_' + chekInfo[1] + '_Shader'
#                if mc.ls(shader_G_Node):
#                    mc.delete(shader_G_Node)
#                GSG = 'SHD_' + chekInfo[0] + '_G_' + chekInfo[1] + '_SG'
#                if mc.ls(GSG):
#                    mc.delete(GSG)
#                shader_G_Node = mc.shadingNode('lambert', asShader=True, name = shader_G_Node)
#                GSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name = GSG)
#                # 连接
#                mc.setAttr((shader_G_Node + '.color'), 0, 1, 0, type='double3')
#                mc.setAttr((shader_G_Node + '.ambientColor'), 1, 1, 1, type='double3')
#                mc.setAttr((shader_G_Node + '.diffuse'), 1)
#                mc.setAttr((shader_G_Node + '.matteOpacityMode'), 2)
#                mc.setAttr((shader_G_Node + '.matteOpacity'), 0)
#                mc.connectAttr((shader_G_Node + '.outColor'), (GSG + '.surfaceShader'))
#            
#            if BObjs:
#                # 材质球组
#                shader_B_Node = 'SHD_' + chekInfo[0] + '_B_' + chekInfo[1] + '_Shader'
#                if mc.ls(shader_B_Node):
#                    mc.delete(shader_B_Node)
#                BSG = 'SHD_' + chekInfo[0] + '_B_' + chekInfo[1] + '_SG'
#                if mc.ls(BSG):
#                    mc.delete(BSG)
#                shader_B_Node = mc.shadingNode('lambert', asShader=True, name = shader_B_Node)
#                BSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name = BSG)
#                # 连接
#                mc.setAttr((shader_B_Node + '.color'), 0, 0, 1, type='double3')
#                mc.setAttr((shader_B_Node + '.ambientColor'), 1, 1, 1, type='double3')
#                mc.setAttr((shader_B_Node + '.diffuse'), 1)
#                mc.setAttr((shader_B_Node + '.matteOpacityMode'), 2)
#                mc.setAttr((shader_B_Node + '.matteOpacity'), 0)
#                mc.connectAttr((shader_B_Node + '.outColor'), (BSG + '.surfaceShader'))
#                
#            if MObjs:
#                # 材质球组
#                shader_M_Node = 'SHD_' + chekInfo[0] + '_M_' + chekInfo[1] + '_Shader'
#                if mc.ls(shader_M_Node):
#                    mc.delete(shader_M_Node)
#                MSG = 'SHD_' + chekInfo[0] + '_M_' + chekInfo[1] + '_SG'
#                if mc.ls(MSG):
#                    mc.delete(MSG)
#                shader_M_Node = mc.shadingNode('lambert', asShader=True, name = shader_M_Node)
#                MSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name = MSG)
#                # 连接
#                mc.setAttr((shader_M_Node + '.color'), 0, 0, 0, type='double3')
#                mc.setAttr((shader_M_Node + '.ambientColor'), 1, 1, 1, type='double3')
#                mc.setAttr((shader_M_Node + '.diffuse'), 0)
#                mc.setAttr((shader_M_Node + '.matteOpacityMode'), 2)
#                mc.setAttr((shader_M_Node + '.matteOpacity'), 1)
#                mc.connectAttr((shader_M_Node + '.outColor'), (MSG + '.surfaceShader'))
#
#            # matter
#            shader_Matte = 'SHD_' + chekInfo[0] + '_' + chekInfo[1] + '_Matte' + '_Shader'
#            if mc.ls(shader_Matte):
#                mc.delete(shader_Matte)
#            MatteSG = 'SHD_' + chekInfo[0] + '_' + chekInfo[1] + '_Matte_SG'
#            if mc.ls(MatteSG):
#                mc.delete(MatteSG)
#            shader_Matte = mc.shadingNode('lambert', asShader=True, name = shader_Matte)
#            MatteSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name = MatteSG)
#            # 连接
#            mc.setAttr((shader_Matte + '.color'), 0, 0, 0, type='double3')
#            mc.setAttr((shader_Matte + '.ambientColor'), 1, 1, 1, type='double3')
#            mc.setAttr((shader_Matte + '.diffuse'), 0)
#            mc.setAttr((shader_Matte + '.matteOpacityMode'), 0)
#            mc.connectAttr((shader_Matte + '.outColor'), (MatteSG + '.surfaceShader'))
#            # 着色
#            if matteObjs:
#                for obj in matteObjs:
#                    if mc.nodeType(obj) == 'mesh':
#                        mesh = mc.ls(obj,l = 1)[0]
#                    else:
#                        mesh = mc.listRelatives(obj,s = 1 ,ni  = 1, type = 'mesh',f=1)
#                        if not mesh:
#                            continue
#                        mesh = mesh[0]
#                    self.ydRLShaderAdd(mesh,MatteSG)
#
#            # 处理两个物体集
#            RMeshes = []
#            GMeshes = []
#            BMeshes = []
#            MMeshes = []
#            
#            # RGBA着色
#            for i in range(4):
#                objs = []
#                shaderSG = ''
#                if i == 0:
#                    objs = RObjs
#                    if objs:
#                        shaderSG = RSG
#                if i == 1:
#                    objs = GObjs
#                    if objs:
#                        shaderSG = GSG
#                if i == 2:
#                    objs = BObjs
#                    if objs:
#                        shaderSG = BSG
#                if i == 3:
#                    objs = MObjs
#                    if objs:
#                        shaderSG = MSG
#                if not objs:
#                    continue
#                for obj in objs:
#                    if mc.nodeType(obj) == 'mesh':
#                        mesh = obj
#                    else:
#                        mesh = mc.listRelatives(obj,s= 1,type = 'mesh',f = 1)
#                        if not mesh:
#                            continue
#                        mesh = mesh[0]
#                    self.ydRLShaderAdd(mesh,shaderSG)
#                    #mc.sets(mesh, e=1, forceElement = shaderSG)
#
#            # [优先]_特殊物体着色
#            if transpancySGNodes:
#                for i in range(len(transpancySGNodes)):
#                    if mc.ls(transpancySGNodes[i]):
#                        keySGInfo = str(i)
#                        meshes = transpancyMeshes[i]
#                        # 有着色物体时才进行
#                        if meshes:
#                            for mesh in meshes:
#                                if '.f[' in mesh:
#                                    grp = mesh.split('.f[')[0]
#                                else:
#                                    grp = mc.listRelatives(mesh , p = 1 , type = 'transform' , f= 1)[0]
#                                if grp in rlObjs:
#                                    RMeshes.append(mesh)
#                                if grp in MaskObjs[0]:
#                                    GMeshes.append(mesh)
#                                if grp in MaskObjs[1]:
#                                    BMeshes.append(mesh)
#                                if grp in MaskObjs[2]:
#                                    MMeshes.append(mesh)
#                            
#                            keyInfo  = ''
#                            keyColor = []
#                            
#                            if RMeshes:
#                                keyInfo  = 'R'
#                                keyColor = [1,0,0]
#                    
#                            if GMeshes:
#                                keyInfo  = 'G'
#                                keyColor = [0,1,0]
#                              
#                            if BMeshes:
#                                keyInfo  = 'B'
#                                keyColor = [0,0,1]
#
#                            if MMeshes:
#                                keyInfo  = 'B'
#                                keyColor = [0,0,0]
#
#                            # 材质球组
#                            shader_RGB_Trs_Node = 'SHD_' + layerType + '_' + keySGInfo +  '_Trs_' + keyInfo + '_' + chekInfo[1] + '_Shader'
#                            if mc.ls(shader_RGB_Trs_Node):
#                                mc.delete(shader_RGB_Trs_Node)
#                            RGB_TrsSG = 'SHD_' + layerType + '_' + keyInfo + '_Trs_' + chekInfo[1] + '_SG'
#                            if mc.ls(RGB_TrsSG):
#                                mc.delete(RGB_TrsSG)
#                            luminanceNode = 'SHD_' + layerType + '_' + keySGInfo + '_' + keyInfo + '_LUM_Shader'
#                            if mc.ls(luminanceNode):
#                                mc.delete(luminanceNode)
#                            # 连接
#                            shader_RGB_Trs_Node = mc.shadingNode('lambert', asShader=True, name = shader_RGB_Trs_Node)
#                            RGB_TrsSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name = RGB_TrsSG)
#                            luminanceNode = mc.shadingNode('luminance', asUtility = True, name = luminanceNode)
#                            mc.setAttr((shader_RGB_Trs_Node + '.color'), keyColor[0], keyColor[1], keyColor[2], type='double3')
#                            mc.setAttr((shader_RGB_Trs_Node + '.ambientColor'), 1, 1, 1, type='double3')
#                            mc.setAttr((shader_RGB_Trs_Node + '.diffuse'), 0)
#                            mc.setAttr((shader_RGB_Trs_Node + '.matteOpacityMode'), 2)
#                            mc.setAttr((shader_RGB_Trs_Node + '.matteOpacity'), 0)
#                            mc.connectAttr((shader_RGB_Trs_Node + '.outColor'), (RGB_TrsSG + '.surfaceShader'))
#                            # 透明连接
#                            self.ydRLTransShaderConnection(transpancyNode[i], shader_RGB_Trs_Node, 'transparency')
#                            
#                            # 翻转
#                            if '.outTransparency' in transpancyNode[i]:
#                                mc.editRenderLayerAdjustment(transpancyNode[i].split('.')[0] + '.invert')
#                                mc.setAttr((transpancyNode[i].split('.')[0] + ".invert"), 1)
#
#                            # 透明作色
#                            for i in range(4):
#                                if i == 0:
#                                    meshes = RMeshes
#                                    if meshes:
#                                        keyInfo = 'R'
#                                        shaderSG = 'SHD_' + layerType + '_' + keyInfo + '_Trs_' + chekInfo[1] + '_SG'
#                                if i == 1:
#                                    meshes = GMeshes
#                                    if meshes:
#                                        keyInfo = 'G'
#                                        shaderSG = 'SHD_' + layerType + '_' + keyInfo + '_Trs_' + chekInfo[1] + '_SG'
#                                if i == 3:
#                                    meshes = BMeshes
#                                    if meshes:
#                                        keyInfo = 'B'
#                                        shaderSG = 'SHD_' + layerType + '_' + keyInfo + '_Trs_' + chekInfo[1] + '_SG'
#                                if i == 4:
#                                    meshes = MMeshes
#                                    if meshes:
#                                        keyInfo = 'M'
#                                        shaderSG = 'SHD_' + layerType + '_' + keyInfo + '_Trs_' + chekInfo[1] + '_SG'
#                                if not meshes:
#                                    continue
#                                for mesh in meshes:
#                                    self.ydRLShaderAdd(mesh,MatteSG)
#            '''
#            # 渲染设置
#            mc.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
#            mc.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')
#
#            # 关闭光线追踪
#            mc.editRenderLayerAdjustment('miDefaultOptions.rayTracing')
#            mc.setAttr('miDefaultOptions.rayTracing', 0)
#
#            # exr
#            self.ydRLFramebuffer('iff',16)
#
#            print (u'===============!!!Done 【%s】!!!===============' % (u'%s_%s层' % (layerType.split('_')[0],layerType.split('_')[1])))
#            print '\n'
#        else:
#            print (u'===============!!!Error 【%s】 无物体!!!===============' % (u'%s_%s层' % (layerType.split('_')[0],layerType.split('_')[1])))
#            print '\n'

    # 补充：修正渲染层需求必须是transform节点
    def ydRLayerMeshToObjs(self,meshes):
        if not meshes:
            return []
        needObjs = []
        for mesh in meshes:
            if mc.nodeType(mesh) == 'transform':
                needObjs.append(mesh)
            if mc.nodeType(mesh) == 'mesh':
                if '.f[' in mesh:
                    grp = mesh.split('.f[')
                    if mc.ls(grp):
                        grp = mc.ls(grp[0],l= 1)
                    else:
                        grp = []
                else:
                    grp = mc.listRelatives(mesh,p=1,type = 'transform',f=1)
                if not grp:
                    continue
                needObjs.append(grp[0])
        return needObjs

    #----------------------------------------------------------------------------------------#
    # 【通用：RGB分层输出系统】
    # Author : 沈  康
    # Data   : 2013_11_18/2014_05_10
    # Data   : 2014_5_28/2014_06_10
    #-------------------------------------------------#
    def ydRLayerRGBOutPutUI(self):
        # 窗口
        if mc.window ("sk_ydRGBOutPutTools",ex=1):
            mc.deleteUI( "sk_ydRGBOutPutTools", window=True )
        mc.window("sk_ydRGBOutPutTools",title="ydRGBOutputTools", widthHeight=(180, 300),menuBar=0)

        # 面板
        form = mc.formLayout()
        # 切换面板
        tabs = mc.tabLayout(innerMarginWidth=5, innerMarginHeight=5)
        mc.formLayout( form, edit=True, attachForm=((tabs, 'top', 0), (tabs, 'left', 0), (tabs, 'bottom', 0), (tabs, 'right', 0)) )
        
        # FullBody类
        child1 = mc.rowColumnLayout()
        
        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0,0,0],label = (unicode('【FBR】【Asset】测试', 'utf8')),c = 'from idmt.maya.commonPerform.renderLayers import sk_renderLayer_Yoda\nreload(sk_renderLayer_Yoda)\nsk_renderLayer_Yoda.sk_renderLayer_Yoda().ydRLayerRGBInfoAssetTest(\"FullBody\",1,1)')
        mc.setParent("..")   

        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0,0,0.0],label = (unicode('===【RGBM】创建===', 'utf8')),c = 'from idmt.maya.commonPerform.renderLayers import sk_renderLayer_Yoda\nreload(sk_renderLayer_Yoda)\nsk_renderLayer_Yoda.sk_renderLayer_Yoda().ydRLRGBBaseShaderCreate(1)')
        mc.setParent("..")  

        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [.8,0,0],label = (unicode('【R】【选材质球】输出', 'utf8')),c = 'from idmt.maya.commonPerform.renderLayers import sk_renderLayer_Yoda\nreload(sk_renderLayer_Yoda)\nsk_renderLayer_Yoda.sk_renderLayer_Yoda().ydRLayerRGBInfoExport(\"FullBody\",\"R\",1)')
        mc.setParent("..")  

        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0,0.8,0],label = (unicode('【G】【选材质球】输出', 'utf8')),c = 'from idmt.maya.commonPerform.renderLayers import sk_renderLayer_Yoda\nreload(sk_renderLayer_Yoda)\nsk_renderLayer_Yoda.sk_renderLayer_Yoda().ydRLayerRGBInfoExport(\"FullBody\",\"G\",1)')
        mc.setParent("..")   

        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0,0.3,0.8],label = (unicode('【B】【选材质球】输出', 'utf8')),c = 'from idmt.maya.commonPerform.renderLayers import sk_renderLayer_Yoda\nreload(sk_renderLayer_Yoda)\nsk_renderLayer_Yoda.sk_renderLayer_Yoda().ydRLayerRGBInfoExport(\"FullBody\",\"B\",1)')
        mc.setParent("..")   

        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0.65,0.65,0.65],label = (unicode('【M】【选材质球】输出', 'utf8')),c = 'from idmt.maya.commonPerform.renderLayers import sk_renderLayer_Yoda\nreload(sk_renderLayer_Yoda)\nsk_renderLayer_Yoda.sk_renderLayer_Yoda().ydRLayerRGBInfoExport(\"FullBody\",\"M\",1)')
        mc.setParent("..")   
        
        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0,0,0.0],label = (unicode('===FullBody===', 'utf8')))
        mc.setParent("..")  
        '''
        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0,0,0],label = (unicode('【FBR】【信息】【清理】', 'utf8')),c = 'from idmt.maya.commonPerform.renderLayers import sk_renderLayer_Yoda\nreload(sk_renderLayer_Yoda)\nsk_renderLayer_Yoda.sk_renderLayer_Yoda().ydRLayerRGBInfoClean(\"FullBody\",1)')
        mc.setParent("..")  
        '''
        mc.setParent("..") 
        
        # ShortParts类
        child2 = mc.rowColumnLayout()
        
        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0,0,0],label = (unicode('【SPR】【Asset】测试', 'utf8')),c = 'from idmt.maya.commonPerform.renderLayers import sk_renderLayer_Yoda\nreload(sk_renderLayer_Yoda)\nsk_renderLayer_Yoda.sk_renderLayer_Yoda().ydRLayerRGBInfoAssetTest(\"ShortParts\",1,1)')
        mc.setParent("..")   
    
        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0,0,0.0],label = (unicode('===【RGBM】创建===', 'utf8')),c = 'from idmt.maya.commonPerform.renderLayers import sk_renderLayer_Yoda\nreload(sk_renderLayer_Yoda)\nsk_renderLayer_Yoda.sk_renderLayer_Yoda().ydRLRGBBaseShaderCreate(1)')
        mc.setParent("..")   
        
        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [.8,0,0],label = (unicode('【R】【选材质球】输出', 'utf8')),c = 'from idmt.maya.commonPerform.renderLayers import sk_renderLayer_Yoda\nreload(sk_renderLayer_Yoda)\nsk_renderLayer_Yoda.sk_renderLayer_Yoda().ydRLayerRGBInfoExport(\"ShortParts\",\"R\",1)')
        mc.setParent("..")  

        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0,0.8,0],label = (unicode('【G】【选材质球】输出', 'utf8')),c = 'from idmt.maya.commonPerform.renderLayers import sk_renderLayer_Yoda\nreload(sk_renderLayer_Yoda)\nsk_renderLayer_Yoda.sk_renderLayer_Yoda().ydRLayerRGBInfoExport(\"ShortParts\",\"G\",1)')
        mc.setParent("..")   

        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0,0.3,0.8],label = (unicode('【B】【选材质球】输出', 'utf8')),c = 'from idmt.maya.commonPerform.renderLayers import sk_renderLayer_Yoda\nreload(sk_renderLayer_Yoda)\nsk_renderLayer_Yoda.sk_renderLayer_Yoda().ydRLayerRGBInfoExport(\"ShortParts\",\"B\",1)')
        mc.setParent("..")   

        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0.7,0.7,0.7],label = (unicode('【M】【选材质球】输出', 'utf8')),c = 'from idmt.maya.commonPerform.renderLayers import sk_renderLayer_Yoda\nreload(sk_renderLayer_Yoda)\nsk_renderLayer_Yoda.sk_renderLayer_Yoda().ydRLayerRGBInfoExport(\"ShortParts\",\"M\",1)')
        mc.setParent("..")   
        
        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0,0,0.0],label = (unicode('===ShortParts===', 'utf8')))
        mc.setParent("..")   
        '''
        mc.rowLayout()
        mc.button(w = 150 , h = 30 ,bgc = [0,0,0],label = (unicode('【SPR】【信息】【清理】', 'utf8')),c = 'from idmt.maya.commonPerform.renderLayers import sk_renderLayer_Yoda\nreload(sk_renderLayer_Yoda)\nsk_renderLayer_Yoda.sk_renderLayer_Yoda().ydRLayerRGBInfoClean(\"ShortParts\",1)')
        mc.setParent("..")   
        '''
        mc.setParent("..") 
        
        mc.tabLayout( tabs, edit=True, tabLabel=((child1, unicode('===FullBody===', 'utf8')), (child2, unicode('===ShortParts===', 'utf8'))) )
        
        mc.showWindow( "sk_ydRGBOutPutTools" )

    #--------------------------#
    # 标准材质球创建
    def ydRLRGBBaseShaderCreate(self,RGBMode = 0):
        for i in range(4):
            # color
            if i == 0:
                key = 'R'
                colors = [1.0 , 0.0 , 0.0]
            if i == 1:
                key = 'G'
                colors = [0.0 , 1.0 , 0.0]
            if i == 2:
                key = 'M'
                colors = [0.0 , 0.0 , 1.0]
            if i == 3:
                key = 'B'
                colors = [0.0 , 0.0 , 0.0]
            # 创建材质球
            shaderTest = 'SHD_testIDP_' + key + '_Shader'
            if mc.ls(shaderTest):
                mc.delete(shaderTest)
            SGTest = 'SHD_testIDP_' + key + '_SG'
            if mc.ls(SGTest):
                mc.delete(SGTest)
            shaderTest = mc.shadingNode('lambert', asShader=True, name = shaderTest)
            SGTest = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name = SGTest)
            # 连接
            mc.setAttr((shaderTest + '.matteOpacityMode'), 2)
            if RGBMode:
                if colors[0] or colors[1] or colors[2]:
                    mc.setAttr((shaderTest + '.matteOpacity'), 0)
            mc.setAttr((shaderTest + '.color'), colors[0], colors[1], colors[2], type='double3')
            mc.setAttr((shaderTest + '.ambientColor'), 1, 1, 1, type='double3')
            mc.setAttr((shaderTest + '.diffuse'), 1)
            mc.connectAttr((shaderTest + '.outColor'), (SGTest + '.surfaceShader'))

    #--------------------------#
    # 分层信息输出
    # 数据结构：第一行，字符串，|分割三个通道信息；从第二行开始，每行一个mesh
    def ydRLayerRGBInfoExport(self, LayerName='FullBody', exportType='all', update = 0):
        localPath = sk_infoConfig.sk_infoConfig().checkLayerInfoLocalPath('RGB', LayerName)
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()

        fileName = 'RGB' + '_'+ shotInfo[1] + '_' + exportType + '_geo.txt'
        filePath = localPath + shotInfo[1] + '\\'+ fileName
        mc.sysFile((localPath + shotInfo[1] + '\\'),makeDir = 1)
        # 输出物体
        shader = mc.ls(sl=1)
        if not shader:
            print(u'===请选中有效材质球===')
            mc.error(u'===请选中有效材质球===')
        if mc.nodeType(shader[0]) not in ['lambert','surfaceShader','aiUtility']:
            print(u'===请选中有效材质球===')
            mc.error(u'===请选中有效材质球===')
        if mc.nodeType(shader[0]) in ['lambert','aiUtility']:
            colorInfo = mc.getAttr(shader[0] + '.color')
        if mc.nodeType(shader[0]) == 'surfaceShader':
            colorInfo = mc.getAttr(shader[0] + '.outColor')
        shaderColor = str(colorInfo[0][0]) + '|' + str(colorInfo[0][1]) + '|' + str(colorInfo[0][2])
        SGNodes = mc.listConnections(shader,d=1,type = 'shadingEngine')
        if not SGNodes:
            print(u'===请选中有效材质球===')
            mc.error(u'===请选中有效材质球===')
        meshes = mc.sets(SGNodes,q=1)
        meshes = mc.ls(meshes, l = 1)
        if not meshes:
            print(u'===请选中有效材质球===')
            mc.error(u'===请选中有效材质球===')
        # outputInfo
        outPutInfo = [shaderColor]
        for mesh in meshes:
            outPutInfo = outPutInfo + [mesh]
        sk_infoConfig.sk_infoConfig().checkFileWrite(filePath, outPutInfo)
        # update
        if update:
        # 本地及服务器端路径
            # 此处路径问题
            serverPath = sk_infoConfig.sk_infoConfig().checkLayerInfoServerPath('RGB', LayerName)
            serverFilePath = serverPath + shotInfo[1] + '\\' + fileName
            updateCMD = 'zwSysFile "copy" ' + '"' + (filePath.replace('\\', '/')) + '"' + ' ' + '"' + (serverFilePath.replace('\\', '/')) + '"' + ' true'
            mel.eval(updateCMD)
            # 注册数据库
            projName = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(shotInfo[0])
            userName = mel.eval('getenv \"USERNAME\"')
            info = projName + '|' + shotInfo[1] + '|' + userName
            mc.idmtService('RgbInput', info)
        
        print u'========[%s]_[%s]_[输出]完毕！！！========'%(LayerName,exportType)

    #--------------------------#
    # 分层信息类别清空
    def ydRLayerRGBInfoClean(self,LayerName='FullBody' ,server  = 0 ):
        # 路径
        if server:
            filePath = sk_infoConfig.sk_infoConfig().checkLayerInfoServerPath('RGB', LayerName)

        else:
            filePath = sk_infoConfig.sk_infoConfig().checkLayerInfoLocalPath('RGB', LayerName)
        
        print filePath.replace('\\','/')[:-1]
        delCmd = 'zwSysFile(\"rd\",\"' + filePath.replace('\\','/')[:-1] + '\",\"\",1)'
        mel.eval(delCmd)
        
        print u'========[%s]_[清理]完毕！！！========'%(LayerName)
        
    #--------------------------#
    # 分层信息验证
    # 创建材质球,不支持透明贴图
    def ydRLayerRGBInfoAssetTest(self,LayerName='FullBody' ,server  = 0 , RGBMode = 0):
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        
        allInfos = self.ydRLayerRGBInfoImport(LayerName , shotInfo[1] , server)
        
        if not allInfos:
            print u'=========本Asset没有有效IDP信息========='
            mc.error(u'=========本Asset没有有效IDP信息=========')
            
        # 分层
        meshes = mc.ls(type = 'mesh',l=1)
        needMeshes = []
        for mesh in meshes:
            if '|RIG|' not in mesh:
                obj = mc.listRelatives(mesh,ap = 1 ,type = 'transform',f = 1)
                if obj:
                    needMeshes.append(mesh)
        meshes = needMeshes
        objs = mc.listRelatives(meshes,ap = 1, type = 'transform' ,f = 1)
        objs = list(set(objs))
        
        if mc.ls(LayerName):
            mc.delete(LayerName)
        
        mc.createRenderLayer(objs, name = LayerName, noRecurse=1, makeCurrent=1)
        
        # 给与基本matte
        shaderMatte = 'SHD_testIDP_' + LayerName + '_Matte_Shader'
        if mc.ls(shaderMatte):
            mc.delete(shaderMatte)
        MatteSG = 'SHD_testIDP_' + LayerName + '_Matte_SG'
        if mc.ls(MatteSG):
            mc.delete(MatteSG)
        shaderMatte = mc.shadingNode('lambert', asShader=True, name = shaderMatte)
        MatteSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name = MatteSG)
        
        mc.setAttr((shaderMatte + '.color'), 0, 0, 0, type='double3')
        mc.setAttr((shaderMatte + '.ambientColor'), 1, 1, 1, type='double3')
        mc.setAttr((shaderMatte + '.diffuse'), 1)
        mc.setAttr((shaderMatte + '.matteOpacityMode'), 0)
        mc.connectAttr((shaderMatte + '.outColor'), (MatteSG + '.surfaceShader'))
        
        try:
            mc.sets(objs,e = 1 , forceElement = MatteSG)
        except:
            for mesh in meshes:
                try:
                    mc.sets(mesh,e = 1 , forceElement = MatteSG)
                except:
                    print mesh
                    print(u'===请检查本行上方，其无法正常着色===')
                    mc.error(u'===请检查本行上方，其无法正常着色===')
                    print '\n'
                
        # RGBA
        for i in range(len(allInfos)):
            info = allInfos[i]
            # color
            colors = info[0].split('|')
            colors = [float(colors[0]),float(colors[1]),float(colors[2])]
            # mesh
            meshes = info[1:]
            # 创建材质球
            shaderTest = 'SHD_testIDP_' + str(i) + '_' +  LayerName + '_Shader'
            if mc.ls(shaderTest):
                mc.delete(shaderTest)
            SGTest = 'SHD_testIDP_' + str(i) + '_' +  LayerName + '_SG'
            if mc.ls(SGTest):
                mc.delete(SGTest)
            shaderTest = mc.shadingNode('lambert', asShader=True, name = shaderTest)
            SGTest = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name = SGTest)
            # 连接
            mc.setAttr((shaderTest + '.matteOpacityMode'), 2)
            if RGBMode:
                if colors[0] or colors[1] or colors[2]:
                    mc.setAttr((shaderTest + '.matteOpacity'), 0)
            mc.setAttr((shaderTest + '.color'), colors[0], colors[1], colors[2], type='double3')
            mc.setAttr((shaderTest + '.ambientColor'), 1, 1, 1, type='double3')
            mc.setAttr((shaderTest + '.diffuse'), 1)
            mc.connectAttr((shaderTest + '.outColor'), (SGTest + '.surfaceShader'))
            # 赋予材质
            mc.sets(meshes, e=1, forceElement = SGTest)
            
        print u'----------[RGB_%s]    Done!!!----------'%(LayerName)

    #----------------------------------------------------------------------------------------#
    # 【通用：RGB分层读取系统】
    # Author : 沈  康
    # Data   : 2013_11_18/2014_05_10
    # Data   : 2014_5_28/2014_06_10
    #----------------------------------------------------------------------------------------#
    #--------------------------#
    # 分层信息读取
    def ydRLayerRGBInfoImport(self,LayerName = 'FullBody', assetName = '' ,server = 0):
        # 路径
        if server:
            serverPath = sk_infoConfig.sk_infoConfig().checkLayerInfoServerPath('RGB', LayerName)
            filePath = serverPath + assetName + '\\' 
        else:
            localPath = sk_infoConfig.sk_infoConfig().checkLayerInfoLocalPath('RGB', LayerName)
            filePath = localPath + assetName + '\\' 
            
        #print filePath
        alllFiles = mc.getFileList(folder = filePath)

        if not alllFiles:
            return []
        
        # 读文件
        result = []
        for fileName in alllFiles:
            if fileName[-4:] != '.txt':
                continue
            result.append(sk_infoConfig.sk_infoConfig().checkFileRead(filePath + fileName))
        return result

    #--------------------------#
    # 获取文件内所有asset的RGB素材信息
    # specialType 为SK之类的特殊asset编号提供，偏移到第二位判断asset类别
    # 数据结构：两个list
    # 第一个list，多个颜色信息的组合，每个颜色信息也是个list记录RGB通道信息
    # 第二个list，与第一个list对应，每个元素是对应颜色信息的meshlist(有根据namespace调整信息)
    # namespace使用条件：文件整理过，namespace通过reference路径变更过结构
    # 改版：无视参考模式
    def ydRLayerRGBObjectsConfig(self, LayerName = 'FullBody', specialType = 0 , server = 1 ):
        from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
        reload(sk_referenceConfig)
        shaderColor = []
        shaderMeshes = []
        #refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        #refNamespace = refInfos[2][0]
        needNamespaces = mc.namespaceInfo(listOnlyNamespaces=1)
        for ns in needNamespaces:
            if '_' not in ns:
                continue
            if ns.split('_')[1][specialType] in ['c','p','s']:
                assetName = ns.split('_')[1]
                allInfos = self.ydRLayerRGBInfoImport(LayerName,assetName,server)
                for info in allInfos:
                    # color
                    shaderColor.append([float(info[0].split('|')[0]),float(info[0].split('|')[1]),float(info[0].split('|')[2])])
                    # 处理meshes
                    needMeshes = []
                    for k in range(len(info)):
                        checkMesh = ''
                        if k == 0:
                            continue
                        if '|' not in info[k]:
                            if mc.objExists(ns + ':' + info[k]):
                                needMeshFull = mc.ls(( ns + ':' + info[k]),l = 1)[0]
                                checkMesh = needMeshFull

                        else:
                            # 全面启动长名
                            needMesh = info[k].replace('|',('|' + ns + ':'))
                            if not mc.ls('*' + needMesh):
                                continue
                            needMeshFull = mc.ls(('*' + needMesh),l = 1)[0]
                            checkMesh = needMeshFull
                        if checkMesh:
                            if '.f[' in checkMesh:
                                faceNum = mc.polyEvaluate(checkMesh.split('.f[')[0], face=1)
                                # 整点归shape
                                if checkMesh == (checkMesh.split('.f[')[0] + '.f[0:' + str(faceNum - 1) + ']'):
                                    shape = mc.listRelatives(checkMesh.split('.f[')[0],s = 1,ni = 1, type = 'mesh',f = 1)
                                    # 对场景而言，应该有删物体，所以要判断在不在
                                    if shape:
                                        needMeshes.append(shape[0])
                                else:
                                    # 对场景而言，应该有删物体，所以要判断在不在
                                    if mc.ls(checkMesh):
                                        needMeshes.append(checkMesh)
                            else:
                                # 对场景而言，应该有删物体，所以要判断在不在
                                if mc.ls(checkMesh):
                                    needMeshes.append(checkMesh)
                    #needMeshes = mc.ls(needMeshes , l = 1)
                    shaderMeshes.append(needMeshes)
        result = [shaderColor,shaderMeshes]
        return result
    
    #----------------------------------------------------------------------------------------#
    # 杂项整理工具集
    #----------------------------------------------------------------------------------------#
    # 删除SET reference
    def ydRLayerSetReferenceDel(self):
        from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
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
    def ydRLayerExrWriteMode(self):
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
    def ydRLayerZdepthDistanceConfigUI(self):
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
        mc.button(label=u'[变更设置]', width=320, c='sk_renderLayer_Yoda.sk_renderLayer_Yoda().ydRLayerZdepthDistanceConfig()')
        mc.setParent("..")

        mc.showWindow()

    # Zdepth distance Config
    def ydRLayerZdepthDistanceConfig(self):
        value = mc.intFieldGrp('Zdepth_Distance_Value', value=1, q=1)[0]
        samplerInfoNodes = mc.ls(type='samplerInfo')
        if samplerInfoNodes:
            for node in samplerInfoNodes:
                if mc.objExists(node + '.FarClipCalimero'):
                    mc.setAttr((node + '.FarClipCalimero'), value)

    # skydome config
    def ydRLSkydomeMoodConfig(self):
        # 获取合格的LightingGrp
        lightGrps = mc.ls('*:LIGHTING', type='transform')
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

    # 断开mesh的SG重新赋予材质
    def ydRLShaderAdd(self, mesh , addSG ):
        # 获取mesh连接的SG属性
        checkMesh = mesh
        if '.f[' in checkMesh:
            checkMesh = checkMesh.split('.f[')[0]
        checkMesh = mc.ls(mesh , l = 1)[0]
        allInfos = mc.listConnections(checkMesh,d = 1 , type = 'shadingEngine',plugs = 1 , connections = 1)
        layerName = 'CHRF_BSR'
        if allInfos:
            needInfo = []
            for i in range(len(allInfos)/2):
                if '.memberWireframeColor' in allInfos[2*i + 1]:
                    needInfo.append([allInfos[2*i + 1],allInfos[2*i]])
                else:
                    needInfo.append([allInfos[2*i],allInfos[2*i + 1]])
            # 断开
            for info in needInfo:
                if '.memberWireframeColor' not in info[1]:
                    # mesh -> layer
                    connectNumInfos = mc.getAttr((layerName + '.outAdjustments'), mi=1)
                    newID = 0
                    if connectNumInfos:
                        newID = len(connectNumInfos)
                        while newID in connectNumInfos:
                            newID = newID + 1
                    else:
                        newID = 0
                    mc.connectAttr( info[0] , (layerName + '.outAdjustments[' +str(newID) + '].outPlug'))
                    # layer -> SG
                    # masterLayer
                    connectIINumInfos = mc.getAttr((info[1].split('[')[0]), mi=1)
                    newIDII = 0
                    if connectIINumInfos:
                        newIDII = len(connectIINumInfos)
                        while newIDII in connectIINumInfos:
                            newIDII = newIDII + 1
                    else:
                        newIDII = 0
                    #mc.connectAttr( ('defaultRenderLayer' + '.outAdjustments[' +str(newID) + '].outValue') , ( info[1].split('[')[0] + '[' +str(newID) + ']'))
                    # newLayer
                    mc.connectAttr( (layerName + '.outAdjustments[' +str(newID) + '].outValue') , ( info[1].split('[')[0] + '[' +str(newIDII) + ']'))
                    #mc.editRenderLayerAdjustment(info[0])
                    #mc.editRenderLayerAdjustment(info[1])
                mc.disconnectAttr( info[0] , info[1] )
        # 赋予材质
        mc.sets(mesh,e = 1 , forceElement = addSG)
    
    # 断开所有SG连接
    def ydRLSGDisConnect(self):
        # 获取
        sgNodes = mc.ls(type = 'shadingEngine')
        sgNodes.remove('initialParticleSE')
        sgNodes.remove('initialShadingGroup')
        connectInfos = []
        for sgNode in sgNodes:
            meshes = mc.listConnections(sgNode,s = 1,type = 'mesh',plugs = 1)
            if not meshes:
                continue
            for mesh in meshes:
                sgNodeAttr = mc.listConnections(mesh,d = 1 , type = 'shadingEngine',plugs = 1)
                if not sgNodeAttr:
                    continue
                connectInfos.append([mesh,sgNodeAttr[0]])
        # 断开
        #layerName = 'CHRF_FBR'
        if connectInfos:
            for info in connectInfos:
                if '.instObjGroups.' in info[0]:
                    continue
                #mc.connectAttr( info[0] , (layerName + '.outAdjustments[0].outPlug'))
                #mc.editRenderLayerAdjustment(info[0])
                #mc.editRenderLayerAdjustment(info[1])
                #print '---'
                #print info[0]
                #print info[1]
                mc.disconnectAttr(info[0],info[1])
    
    # SG节点处理
    def ydRLSGNodeCleanConfig(self, sgNode):
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

    # 完全断开指定属性
    def ydRLDeleteConnection(self , attr ):
        # 被输入方
        if mc.connectionInfo(attr , isDestination = 1):
            destination = mc.connectionInfo(attr , getExactDestination = 1)
            srcConn = mc.listConnections(destination, s = 1, d = 0 , type = 'character')
            if srcConn:
                # 断开
                mc.character(destination , e = 1 ,rm = srcConn[0])
            sArr = mc.ls(destination , ro = 1)
            if sArr:
                src = mc.connectionInfo(destination , sourceFromDestination = 1)
                if src:
                    mc.disconnectAttr(src , destination)
            else:
                mc.delete(destination , icn = 1)

    # env 灯光，yoda专用
    def ydRLEnvLightCreate(self):
        envLight = 'IDMT_P2_ENV_LT'
        if not mc.ls(envLight):
            mc.shadingNode('ambientLight',asLight = 1,name = envLight )
        mc.setAttr((envLight + '.ambientShade'),0)
        return [envLight]