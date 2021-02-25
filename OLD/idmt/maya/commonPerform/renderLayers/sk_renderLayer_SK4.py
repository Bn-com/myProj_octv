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

class sk_renderLayer_SK4(object):
    def __init__(self):
        pass

    #--------------------------------------------------------------------------------------------------------#
    #----------------------------------------------------------#
    # 【核心】 自动创建函数
    #----------------------------------------------------------#
    # Auto Create
    #　createMode　　０　是第一场创建，要输出信息  | 1 是第一次之后的输出，网络读信息
    def sk4RLAutoCreate(self, createMode = 0 , shaderForece = 0 ,separate = 1):
        print ('=================================================================')
        print '====================!!!Start AutoRenderLayer!!!===================='

        # Back To MasterLayer
        mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')
        # clean renderlayer
        from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools
        reload(sk_sceneTools)
        from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
        reload(sk_referenceConfig)

        # 参考import
        sk_referenceConfig.sk_referenceConfig().checkRefAllImport()
        
        # clean unknown nodes
        sk_sceneTools.sk_sceneTools().checkDonotNodeCleanBase(0)
        

        # Step Base:[导出]
        #if shaderForece:
        # 导出
        print '\n'
        print u'========================导出清理开始========================'
        print u'===如果本阶段失败，请打开文件手动清理'
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        pathLocal = sk_infoConfig.sk_infoConfig().checkRenderLayerLocalPath()
        baseFileName = pathLocal + shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2] + '_Base' + '.mb'
        # 记录norender物体
        norenderObjs = self.sk4NorenderObjs()
        if norenderObjs:
            try:
                meshes = mc.listRelatives(norenderObjs ,ad = 1, type = 'mesh' , f = 1)
            except:
                print u'===norender层出错，请保证norender层只有polygon物体==='
                print meshes
                mc.error(u'===请手动处理norender层===')
                
            if meshes:
                for mesh in meshes:
                    mc.setAttr(mesh + '.primaryVisibility',0)
        baseGrps = ['CHR_GRP','PRP_GRP','SET_GRP','OTC_GRP']
        mc.select(baseGrps)
        quickSets = mc.ls(type = 'objectSet')
        if quickSets:
            for obj in quickSets:
                if 'smooth' in obj:
                    mc.select(obj,add = 1,ne = 1)
        mc.file(baseFileName,f = 1,es = 1,pr = 1,type = 'mayaBinary')
        print u'---50%'
        # 重打开
        mc.file(baseFileName,open = 1 , f = 1)
        print u'---100%'
        print u'========================导出清理成功========================'
        print u'===下面开始正式分层'
        print '\n'
        
        # clean unknown nodes
        sk_sceneTools.sk_sceneTools().checkDonotNodeCleanBase(0)
        
        # 角色信息
        nsList = mc.namespaceInfo(listOnlyNamespaces=1)
        needNs = []
        for ns in nsList:
            if '_' not in ns:
                continue
            if ns.split('_')[1][1] == 'c':
                needNs.append(ns)

        # common Setting
        self.sk4RLCommonConfig()
        
        # Step 0: [SoftWare] smooth
        self.sk4RLSwDoSmooth()
        mc.file(rename = baseFileName)
        mc.file(save = 1 , f = 1)
        
        # 透明信息输出
        self.sk4RLTransparencyObjsOld(0,1)
        
        # Step 1：  [SoftWare][CHR]
        # 清理渲染层
        sk_sceneTools.sk_sceneTools().checkCleanRenderLayers()
        self.sk4RLSYSShaderClean()

        # Color
        self.sk4RLCOCreate('CHR')
        # Color
        self.sk4RLCOCreate('BG')
        # RGB
        #self.sk4reate('CHR_RGB')

        # Back To MasterLayer
        mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')
        # Unrender MasterLayer
        mc.setAttr("defaultRenderLayer.renderable", 0)
        # common Setting
        self.sk4RLCommonConfig()
        # save
        self.sk4RLSave('SWCBO',2)

        # Step 2：  [SoftWare][BG]
        # 清理渲染层
        if shaderForece:
            mc.file(baseFileName,open = 1 , f = 1)
        else:
            sk_sceneTools.sk_sceneTools().checkCleanRenderLayers()
            self.sk4RLSYSShaderClean()
        
        # Shadow
        self.sk4RLSHDCreate('CHR' , shaderForece = shaderForece)
        # Zdepth
        self.sk4RLZDEPTHCreate('BG' , shaderForece = shaderForece)
        # BG_RGB
        #self.sk4RLRGBCreate('BG_RGB')

        mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')
        # Unrender MasterLayer
        mc.setAttr("defaultRenderLayer.renderable", 0)
        # common Setting
        self.sk4RLCommonConfig()
        # save
        self.sk4RLSave('SWZS',2)

        # Step 3：  [MentalRay][HAIR]
        # 清理渲染层
        if shaderForece:
            mc.file(baseFileName,open = 1 , f = 1)
            # master赋予颜色
            #self.sk4RLMasterCleanCreate()
        else:
            sk_sceneTools.sk_sceneTools().checkCleanRenderLayers()
            self.sk4RLSYSShaderClean()
            
        # mr Setting
        self.mentalRayProductionLevel()
            
        # 分割角色
        if separate and needNs:
            # 获取信息
            chrGrps = []
            for ns in needNs:
                allMeshes = mc.ls((ns+':*'),type = 'mesh',l = 1)
                needMeshes = []
                for mesh in allMeshes:
                    if ':MODEL' not in mesh:
                        continue
                    if '_hair' not in mesh.split('|')[-1]:
                        continue
                    if '_hairclip' in mesh.split('|')[-1]:
                        continue
                    needMeshes.append(mc.listRelatives(mesh,p=1,f=1)[0])
                if needMeshes:
                    needMeshes = list(set(needMeshes))
                    chrGrps.append(needMeshes)
            # 分层准备
            chrNum  = len(chrGrps)
            if chrNum:
                # 分层数
                fileNum = 0
                if chrNum%4 == 0:
                    fileNum = (chrNum/4)
                else:
                    fileNum = (chrNum/4) + 1
                # 分割分层开始
                for i in range(fileNum):
                    # Back To MasterLayer
                    mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')
                    # Unrender MasterLayer
                    mc.setAttr("defaultRenderLayer.renderable", 0)
                    
                    # 清理渲染层
                    sk_sceneTools.sk_sceneTools().checkCleanRenderLayers()
                    self.sk4RLSYSShaderClean()

                    if (4*i) <= (chrNum-1):
                        self.sk4RLHairCreate(('CHR' + str(4*i)),selectObjType = 2,extraInfo = [('CHR_HAIR' + str(4*i))  ,chrGrps[4*i]])
                    if (4*i+1) <= (chrNum-1):
                        self.sk4RLHairCreate(('CHR' + str(4*i+1)),selectObjType = 2,extraInfo = [('CHR_HAIR' + str(4*i+1)),chrGrps[4*i + 1]])
                    if (4*i+2) <= (chrNum-1):
                        self.sk4RLHairCreate(('CHR' + str(4*i+2)),selectObjType = 2,extraInfo = [('CHR_HAIR' + str(4*i+2)),chrGrps[4*i + 2]])
                    if (4*i+3) <= (chrNum-1):
                        self.sk4RLHairCreate(('CHR' + str(4*i+3)),selectObjType = 2,extraInfo = [('CHR_HAIR' + str(4*i+3)),chrGrps[4*i + 3]])
                    self.sk4RLSave(('Hair' +str(i)),2,)
                    
        # Step 4：  [MentalRay][CHR]
        # 清理渲染层
        if shaderForece:
            mc.file(baseFileName,open = 1 , f = 1)
            # master赋予颜色
            #self.sk4RLMasterCleanCreate()
        else:
            sk_sceneTools.sk_sceneTools().checkCleanRenderLayers()
            self.sk4RLSYSShaderClean()
            
        # mr Setting
        self.mentalRayProductionLevel()
        
        # AO
        self.sk4RLAOCreate('CHR' , shaderForece = shaderForece)
        # AOD
        self.sk4RLAOCreate('CHRD' , shaderForece = shaderForece)
        # NM
        self.sk4RLNMCreate('CHR' , shaderForece = shaderForece)
        # 不分割角色
        if not separate:
            # Hair
            self.sk4RLHairCreate('CHR')

        # 清理无用材质球
        if shaderForece:
            print u'\n'
            print u'======清理无用材质球Starting======'
            print u'---working---'
            mel.eval('MLdeleteUnused')
            print u'======清理无用材质球Done!!!======'
            print u'\n'
        
        mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')
        # Unrender MasterLayer
        mc.setAttr("defaultRenderLayer.renderable", 0)
        
        # save
        self.sk4RLSave('MRCHR',2)

        # Step 5：  [MentalRay][BG]
        # 清理渲染层
        if shaderForece:
            mc.file(baseFileName,open = 1 , f = 1)
            # master赋予颜色
            #self.sk4RLMasterCleanCreate()
        else:
            sk_sceneTools.sk_sceneTools().checkCleanRenderLayers()
            self.sk4RLSYSShaderClean()
        
        # mr Setting
        self.mentalRayProductionLevel()
        
        # AO
        self.sk4RLAOCreate('BG' , shaderForece = shaderForece)
        # NM
        self.sk4RLNMCreate('BG' , shaderForece = shaderForece)

        #self.sk4RLDoSmooth()
        # Back To MasterLayer
        mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')
        # Unrender MasterLayer
        mc.setAttr("defaultRenderLayer.renderable", 0)
        # mc.setAttr
        # common Setting
        self.sk4RLCommonConfig()
        # save
        self.sk4RLSave('MRBG',2)
        
        # Step 6：  [SoftWare][RGB]
        # 清理渲染层
        if shaderForece:
            mc.file(baseFileName,open = 1 , f = 1)
            # master赋予颜色
            #self.sk4RLMasterCleanCreate()
        else:
            sk_sceneTools.sk_sceneTools().checkCleanRenderLayers()
            self.sk4RLSYSShaderClean()
        
        # 清理掉所有灯光
        lights = mc.ls(type = 'light')
        if lights:
            mc.delete(lights)
        
        # RGB
        self.sk4RLRGBCreate('ALL_BSR' , shaderForece = shaderForece)
        # FBR
        self.sk4RLRGBCreate('ALL_FBR' , shaderForece = shaderForece)
        
        mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')
        # Unrender MasterLayer
        mc.setAttr("defaultRenderLayer.renderable", 0)
        
        # common Setting
        self.sk4RLCommonConfig()
        
        # 清理无用材质球
        if shaderForece:
            print u'\n'
            print u'======清理无用材质球Starting======'
            print u'---working---'
            mel.eval('MLdeleteUnused')
            print u'======清理无用材质球Done!!!======'
            print u'\n'
            
        # save
        self.sk4RLSave('SWRGB',2)
        
        # 干掉base File
        import os
        os.remove(baseFileName)
        
        # [预留] 清理smooth节点
        #smsNodes = mc.ls('foodSMS_*' ,type = 'polySmoothFace')
        #if smsNodes:
        #   mc.delete(smsNodes)

        print '=======================!!!All Done!!!======================='
        print pathLocal
        print ('===========================================================')

    # Create Single Render Layer
    def sk4RLSpeficCreate(self, renderLayer, mrType = 1 ,saveMode='', selectMode=0, arnoldType=0):
        print (u'===============!!!Start 【%s】!!!===============' % (renderLayer))
        print 'Working...'

        from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools
        reload(sk_sceneTools)
        from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
        reload(sk_referenceConfig)
        
        # Back To MasterLayer
        mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')

        # 参考import
        sk_referenceConfig.sk_referenceConfig().checkRefAllImport()

        cacheFiles = mc.ls(type='cacheFile')
        # if cacheFiles:
        #    for cache in cacheFiles:
        #        mc.setAttr((cache + '.enable'),0)

        # clean Unknwon Nodes
        sk_sceneTools.sk_sceneTools().checkDonotNodeCleanBase(0)
        # renderpass Create
        # self.sk4RLRenderPass()

        # common Setting
        self.sk4RLCommonConfig()

        # arnold Setting
        if arnoldType:
            self.arnoldRendererSettings()

        # mr Setting
        if mrType:
            self.mentalRayProductionLevel()
        
        # 指定层
        BGType = renderLayer.split('_')[0]
        layerType = renderLayer.split('_')[1]
        try:
            mc.delete(renderLayer)
        except:
            pass

        # COLOR
        if layerType == 'CO':
            if mc.ls(BGType + '_' + layerType):
                mc.delete(BGType + '_' + layerType)
            self.sk4RLCOCreate(BGType, selectObjType=selectMode)

        # Ambient Occlusion
        if layerType == 'AO':
            if mc.ls(BGType + '_' + layerType):
                mc.delete(BGType + '_' + layerType)
            if arnoldType == 0:
                self.sk4RLAOCreate(BGType, selectObjType=selectMode)
            if arnoldType == 1:
                self.sk4RLAOArnoldCreate(BGType, selectObjType=selectMode)
                
        # Normal
        if layerType == 'NM':
            if mc.ls(BGType + '_' + layerType):
                mc.delete(BGType + '_' + layerType)
            if arnoldType == 0:
                self.sk4RLNMCreate(BGType, selectObjType=selectMode)
            if arnoldType == 1:
                self.sk4RLNMArnoldCreate(BGType, selectObjType=selectMode)
                
        # Zdepth
        if layerType == 'ZDP':
            if mc.ls(BGType + '_' + layerType):
                mc.delete(BGType + '_' + layerType)
            self.sk4RLZDEPTHCreate(BGType, selectObjType=selectMode)

        # SHDW
        if layerType == 'SHDW':
            if mc.ls(BGType + '_' + layerType):
                mc.delete(BGType + '_' + layerType)
            self.sk4RLSHDCreate(BGType, selectObjType=selectMode)

        # FBR
        if layerType == 'FBR':
            if mc.ls(BGType + '_' + layerType):
                mc.delete(BGType + '_' + layerType)
            self.sk4RLRGBCreate(BGType + '_' + layerType)

        # RGB
        if layerType == 'BSR':
            if mc.ls(BGType + '_' + layerType):
                mc.delete(BGType + '_' + layerType)
            self.sk4RLRGBCreate(BGType + '_' + layerType)
            
        # HAIR
        if layerType == 'HAIR':
            if mc.ls(BGType + '_' + layerType):
                mc.delete(BGType + '_' + layerType)
            self.sk4RLHairCreate(BGType, selectObjType=selectMode)

        #删除材质版本
        if layerType == 'FBR01':         
            self.sk4FBRCreate()

        if layerType == 'BSR01':
            self.sk4SBRCreate()
        # smoothSet
        #self.sk4RLDoSmooth()
        # Back To MasterLayer
        mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')
        # UnRender MasterLayer
        mc.setAttr("defaultRenderLayer.renderable", 0)
        # camSetting
        self.sk4RLCamSetting(2)
        # common Setting
        # self.sk4RLCommonConfig()

        if cacheFiles:
            for cache in cacheFiles:
                mc.setAttr((cache + '.enable'), 1)

        if saveMode:
            self.sk4RLSave(saveMode)

        print (u'===============!!!Done  【%s】!!!===============' % ('renderLayer'))
        print '\n'


    # 记录norender信息
    def sk4NorenderObjs(self):
        displayLayers = mc.ls(type = 'displayLayer')
        norenderObjs = []
        for layer in displayLayers:
            if layer.lower() == 'norender':
                objs = mc.editDisplayLayerMembers(layer,q = 1)
                if objs:
                    norenderObjs = objs
        return norenderObjs

    #--------------------------------------------------------------------------------------------------------#
    #----------------------------------------------------------#
    # 【核心】 渲染设置
    #----------------------------------------------------------#
    # 渲染标准设置
    def sk4RLCommonConfig(self):
        print (u'===============!!!Start 【%s】!!!===============' % (u'标准设置'))
        print 'Working...'
        # Camera
        from idmt.maya.commonCore.core_mayaCommon import sk_hbExportCam
        reload(sk_hbExportCam)
        # sk_hbExportCam.sk_hbExportCam().camServerReference(3)

        # 开启窗口，创建各种UI
        # mel.eval('unifiedRenderGlobalsWindow')
        #IKR开启
        mc.setAttr('defaultRenderGlobals.preMel',"ikSystem -e -sol 1",type = 'string')

        # 标准设置
        mc.setAttr('defaultRenderQuality.edgeAntiAliasing', 1)
        mc.setAttr('defaultRenderGlobals.animation', 1)
        mc.setAttr('defaultRenderGlobals.outFormatControl', 0)
        mc.setAttr('defaultRenderGlobals.extensionPadding', 4)
        mc.setAttr('defaultRenderGlobals.imageFilePrefix', '<Layer>/<Scene>_<Layer>', type='string')
        mc.setAttr('defaultResolution.width', 1280)
        mc.setAttr('defaultResolution.height', 720)
        mc.setAttr('defaultResolution.deviceAspectRatio', 1.777)
        mc.setAttr('defaultResolution.pixelAspect', 1.00)
        mc.evalDeferred('import maya.cmds as mc\nmc.setAttr((\'defaultResolution.pixelAspect\'),1)', lowestPriority=1)
        mc.setAttr('defaultResolution.dotsPerInch', 72)
        mc.setAttr('defaultRenderQuality.edgeAntiAliasing', 1)
        # 开始处理
        shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
        shot = shotInfos[0] + '_' + shotInfos[1] + '_' + shotInfos[2] + '_' + shotInfos[3]
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
        
        # software产品级
        mc.setAttr(('defaultRenderQuality' + '.edgeAntiAliasing'),0)
        mc.setAttr(('defaultRenderQuality' + '.useMultiPixelFilter'),1)
        mc.setAttr(('defaultRenderQuality' + '.shadingSamples'),2)
        mc.setAttr(('defaultRenderQuality' + '.maxShadingSamples'),8)
        mc.setAttr(('defaultRenderQuality' + '.visibilitySamples'),1)
        mc.setAttr(('defaultRenderQuality' + '.maxVisibilitySamples'),4)
        mc.setAttr(('defaultRenderQuality' + '.redThreshold'),0.4)
        mc.setAttr(('defaultRenderQuality' + '.greenThreshold'),0.3)
        mc.setAttr(('defaultRenderQuality' + '.blueThreshold'),0.6)
        mc.setAttr(('defaultRenderQuality' + '.reflections'),10)
        mc.setAttr(('defaultRenderQuality' + '.refractions'),10)
        mc.setAttr(('defaultRenderQuality' + '.shadows'),10)

        # mel.eval("prefWndUnitsChanged \"time\";")
        # IKR强制开启
        mc.setAttr('defaultRenderGlobals.preMel',"ikSystem -e -sol 1",type = 'string')

        print (u'===============!!!Done  【%s】!!!===============' % u'标准设置')
        print '\n'

    #--------------------------------#
    # mr 产品级设置
    def mentalRayProductionLevel(self):
        print (u'===============!!!Start 【%s】!!!===============' % (u'MR设置'))
        print 'Working...'

        mc.setAttr('defaultRenderGlobals.imageFormat', 7)
        try:
            mel.eval('loadPlugin "Mayatomr"')
        except:
            pass
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
        #mc.setAttr('defaultRenderGlobals.imageFormat', 51)
        #mc.setAttr('defaultRenderGlobals.imfkey', 'exr', type='string')
        #mc.setAttr('mentalrayGlobals.imageCompression', 4)
        #mc.setAttr('mentalrayGlobals.compressionQuality', 0)
        mc.setAttr('miDefaultOptions.maxSamples', 2)
        mc.setAttr('miDefaultOptions.contrastR', 0.1)
        mc.setAttr('miDefaultOptions.contrastG', 0.1)
        mc.setAttr('miDefaultOptions.contrastB', 0.1)
        mc.setAttr('miDefaultOptions.contrastA', 0.1)

        try:
            mc.setAttr('miDefaultOptions.minSamples', 0)
        except:
            pass

        # 过滤
        mc.setAttr('miDefaultOptions.filter', 2)
        mc.setAttr('miDefaultOptions.filterWidth', 1)
        mc.setAttr('miDefaultOptions.filterHeight', 2)

        print (u'===============!!!Done  【%s】!!!===============' % (u'MR设置'))
        print '\n'

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
    def sk4RLRenderPass(self):
        print (u'===============!!!Start 【%s】!!!===============' % ('RenderPass'))
        print 'Working...'

        # shadow
        ex_rsShadow = mc.ls('shadow', type='renderPass')
        if ex_rsShadow:
            ex_rsShadow = 'shadow'
        else:
            renderPass = mc.shadingNode('renderPass', asRendering=1)
        configType = [1, 'SHD', 3, 256, 0, 1, 'Illumination', 1, 1, 0, 0, 0, 0, 1, 0, 10, 0, 10]
        self.sk4RLRenderPassConfig(renderPass, configType)
        mc.rename(renderPass, 'shadow')
        print (u'===============!!!Done  【%s】!!!===============' % ('RenderPass'))
        print '\n'

    #--------------------------------#
    # 设置renderpass属性
    def sk4RLRenderPassConfig(self, renderPass, configType):
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
    #----------------------------------------------------------#
    def sk4RLFramebuffer(self, fileType = 'exr',datatype=4):    
        mc.setAttr('defaultRenderGlobals.animation', 1)
        mc.setAttr('defaultRenderGlobals.putFrameBeforeExt', 1)
        mc.setAttr('defaultRenderGlobals.periodInExt', 1)
        mc.setAttr('defaultRenderGlobals.extensionPadding', 4)
        if mc.getAttr('defaultRenderGlobals.outFormatControl') == 1:
            mc.setAttr('defaultRenderGlobals.outFormatControl', 0)
        # iff
        if fileType == 'iff':
            mc.editRenderLayerAdjustment('defaultRenderGlobals.imageFormat')
            mc.setAttr('defaultRenderGlobals.imageFormat', 7)
        # tiff
        if fileType == 'tiff':
            mc.editRenderLayerAdjustment('defaultRenderGlobals.imageFormat')
            mc.setAttr('defaultRenderGlobals.imageFormat', 3)
        # tiff16
        if fileType == 'tiff16':
            mc.editRenderLayerAdjustment('defaultRenderGlobals.imageFormat')
            mc.setAttr('defaultRenderGlobals.imageFormat', 4)
        # exr
        if fileType == 'exr':
            mc.editRenderLayerAdjustment('defaultRenderGlobals.imageFormat')
            mc.setAttr('defaultRenderGlobals.imageFormat', 51)
            mc.setAttr('defaultRenderGlobals.imfkey', 'exr', type='string')
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.setAttr('mentalrayGlobals.compressionQuality', 0)
            # 8 zip
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
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
    def sk4RLObjectsTList(self, objs=[]  ):
        # 获取root
        from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools
        reload(sk_sceneTools)

        checkObjs = []

        refCHR = []
        refPRP = []
        refSET = []
        refSKY = []
        refGroud = []
        refHair = []
        
        nodeType = 'mesh'

        # 通过大组来判断
        if mc.ls('CHR_GRP'):
            if mc.listRelatives('CHR_GRP', c=1, f=1, type='transform'):
                refCHR = mc.listRelatives('CHR_GRP', c=1, f=1, type='transform')
        if mc.ls('PRP_GRP'):
            if mc.listRelatives('PRP_GRP', c=1, f=1, type='transform'):
                refPRP = mc.listRelatives('PRP_GRP', c=1, f=1, type='transform')
        if mc.ls('SET_GRP'):
            if mc.listRelatives('SET_GRP', c=1, f=1, type='transform'):
                refSET = mc.listRelatives('SET_GRP', c=1, f=1, type='transform')
        
        # 获取hair
        refHairShapes = mc.ls('*:*_hair*',type = 'mesh' , l = 1)
        if refHairShapes:
            tempShapes =  []
            for shape in refHairShapes:
                checkHair = 1
                if '_hairclip' in shape.split('|')[-1]:
                    checkHair = 0
                if checkHair:
                    tempShapes.append(shape)
            refHairShapes = tempShapes
        if refHairShapes:
            refHair = mc.listRelatives(refHairShapes,p = 1, type = 'transform',f = 1)
            refHair = list(set(refHair))
        
        # 地面
        refMeshGroud = mc.ls('*:*_ground_*',type = 'mesh',l = 1)
        if refMeshGroud:
            refGroud = mc.listRelatives(refMeshGroud,p = 1, type = 'transform',f = 1)
            refGroud = list(set(refGroud))
        
        checkObjs = [refCHR , refPRP , refSET , refSKY , refGroud , refHair]

        for i in range(len(checkObjs)):
            # 只取mesh
            needInfo = []
            refGrps = checkObjs[i]
            if refGrps:
                needShapes = []
                shapes = mc.listRelatives(refGrps, ad=1, ni=1, type= nodeType, f=1)
                if shapes:
                    # 只取有:MODEL标记的mesh
                    for shape in shapes:
                        if nodeType == 'mesh':
                            if ':MODEL|' in shape or '|MODEL|' in shape:
                                needShapes.append(shape)
                        else:
                            needShapes.append(shape)
                    '''
                    # 只有显示的物体才被加入渲染层
                    if needShapes:
                        for shape in needShapes:
                            shapeGrp = mc.listRelatives(shape,p = 1,type = 'transform',f = 1)[0]
                            vState = sk_sceneTools.sk_sceneTools().checkObjVState(shapeGrp)
                            if not vState:
                                needInfo.append(shapeGrp)
                    '''     
                    if needShapes:
                        needInfo = mc.listRelatives(needShapes, p=1, type='transform', f=1)
            if needInfo:
                needInfo = list(set(needInfo))
            checkObjs[i] = needInfo
            
        result = []
        result = checkObjs

        return result

    #--------------------------------------------------------------------------------------------------------#
    #----------------------------------------------------------#
    # 【核心】SG节点属性
    #----------------------------------------------------------#
    # 通过rlobjs获取SG信息
    def sk4RLObjsSGNodesGet(self, objs = []):
        if not objs:
            print '1'
            return 0
        meshes = mc.listRelatives(objs,ad = 1, ni = 1, type = 'mesh',f = 1)
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
    def sk4RLSGNodesGet(self,objType = 1 , objs = []):
        SGNodes = mc.ls(type='shadingEngine')
        SGNodes.remove('initialParticleSE')
        SGNodes.remove('initialShadingGroup')
        # SG分类
        Objs = self.sk4RLObjectsTList()
        checkObjs = [Objs[0],Objs[1],Objs[2],Objs[3],Objs[4],Objs[5]]
        
        result = []
        # 判断分类
        for i in range(len(checkObjs)):
            # 根据连接的物体的参考进行判断
            temp = self.sk4RLObjsSGNodesGet(checkObjs[i])
            if not temp:
                temp = []
            result.append(temp)

        return result

    # 断开所有SG节点的连接
    def sk4RLSGNodesDisConnections(self):

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
    #--------------------------------------------------------------------------------------------------------#
    #----------------------------------------------------------#
    # 【核心】透明信息收集
    #----------------------------------------------------------#
    # 获取有透明贴图的物体 | 文件读取
    def sk4RLTransparencyObjsOld(self, valueCheck = 0 ,update = 0):
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
            # 对CHR类不做透明处理
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
            localTransPath = localPath + 'RLayerInfo/transShaderInfo/' + shotInfo[0] + '/' + str(shotInfo[1]) + '/' + str(shotInfo[2]) + '/'
            mc.sysFile(localTransPath ,makeDir = 1)
            serverTransPath = serverPath + 'data/RLayerInfo/transShaderInfo/' + shotInfo[0] + '/' + str(shotInfo[1]) + '/' + str(shotInfo[2]) + '/'
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
    def sk4RLTransparencyObjsByType(self,rlObjs, foodValue = 0):
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        currentRenderLayer = mc.editRenderLayerGlobals(currentRenderLayer = 1 ,q = 1)
        if currentRenderLayer == 'defaultRenderLayer':
            # 获取并update
            transpancyObjs = self.sk4RLTransparencyObjsOld(foodValue,1)
        else:
            serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
            serverTransPath = serverPath + 'data/RLayerInfo/transShaderInfo/' + shotInfo[0] + '/' + str(shotInfo[1]) + '/' + str(shotInfo[2]) + '/'
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
    def sk4RLTransparencyObjs(self, refNamespaceMode=1):
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
    # 透明属性连接
    def sk4RLTransShaderConnection(self, transpancyNode, transShader, transShaderAttr):
        if transpancyNode[:6] == '[food]':
            transValue = float(transpancyNode[7:])
            try:
                transpancyConnections = mc.listConnections((transShader + '.' + transShaderAttr), s=1, plugs=1)
                mc.disconnectAttr(('%s') % (transpancyConnections[0]), ('%s.%s') % (transShader, transShaderAttr))
            except:
                pass
            mc.setAttr((transShader + '.' + transShaderAttr), transValue, transValue, transValue, type='double3')
        else:
            if mc.nodeType(transpancyNode.split('.')[0]) in['layeredShader', 'surfaceShader', 'ramp', 'file', 'reverse','checker','bulge']:
                if mc.nodeType(transpancyNode.split('.')[0]) in ['layeredShader', 'surfaceShader']:
                    try:
                        mc.disconnectAttr(('%s.%s') % (transpancyNode.split('.')[0], 'outTransparency'), ('%s.%s') % (transShader, transShaderAttr))
                    except:
                        pass
                    mc.connectAttr(('%s.%s') % (transpancyNode.split('.')[0], 'outTransparency'), ('%s.%s') % (transShader, transShaderAttr), f=True)
                if mc.nodeType(transpancyNode.split('.')[0]) in ['ramp', 'file','checker','bulge']:
                    try:
                        mc.disconnectAttr(('%s.%s') % (transpancyNode.split('.')[0], 'outColor'), ('%s.%s') % (transShader, transShaderAttr))
                    except:
                        pass
                    mc.connectAttr(('%s.%s') % (transpancyNode.split('.')[0], 'outColor'), ('%s.%s') % (transShader, transShaderAttr), f=True)
                if mc.nodeType(transpancyNode.split('.')[0]) in ['reverse' ]:
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


    #--------------------------------------------------------------------------------------------------------#
    #----------------------------------------------------------#
    # 【核心】置换信息收集
    #----------------------------------------------------------#
    # 获取有置换贴图的物体|文件获取
    def sk4RLDisplacementObjsOld(self):
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
    def sk4RLDisplacementObjs(self, refNamespaceMode=1):
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
    # 清理系统创建材质球
    def sk4RLSYSShaderClean(self):
        shaderKeys = ['_AO_','_SD_','_NM_','_FN_','_ZDP_','_BSR_','_FBR_','_SPR_','_Matte_']
        materialNodes = mc.ls(materials = 1)
        SGNodes = mc.ls(type = 'shadingEngine')
        needCheckNodes = materialNodes + SGNodes
        for node in needCheckNodes:
            for key in shaderKeys:
                if key in node and 'SHD_' in node:
                    mc.delete(node)
                    break
                
    #--------------------------------#
    # 选取模式
    def sk4RLSelectMode(self):
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
        rlObjs = list(set(checkMeshes))
        return rlObjs

    #--------------------------------#
    # 读取excel信息
    def sk4RLReadEXcle(self):
        # 处理excel信息？
        # 读文件名，获取项目及镜头号
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()  

        projFullName = 'Yoda'

        serverPath = '//file-cluster/GDC/Projects/' + projFullName + '/' + projFullName + '_scratch/TD/ExcelInfo/' + str(shotInfo[1]) + '/'
        serverExcelPath = serverPath + str(shotInfo[0]).upper() + str(shotInfo[1]) + '_TimeOfDay.xls'

        print '-----'
        print serverExcelPath
        import os
        if not os.path.exists(serverExcelPath):
            print(u'=======本集Excel文件不存在，请联系TD及PA处理=======')
            mc.error(u'=======本集Excel文件不存在，请联系TD及PA处理=======')

        import xlrd
        reload(xlrd)
        # shotAllData = xlrd.open_workbook(serverExcelPath).sheets()[0] 0是第一页表格
        shotAllData = xlrd.open_workbook(serverExcelPath).sheets()[0]  
        # 读行数，具体的是镜头号加多少，视表格内容定
        shotData = shotAllData.row_values(int(shotInfo[2]) + 1)  

    #--------------------------------#
    # Save File
    # shotType  1  cl_001_002  | 2 yd_005_009_001
    def sk4RLSave(self, mode , shotType = 2 ,keyInfo = ''):
        print (u'===============!!!Start 【%s】!!!===============' % 'Save')
        print 'Working...'
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        pathLocal = sk_infoConfig.sk_infoConfig().checkRenderLayerLocalPath(shotType)
        if shotType == 2:
            fileName = pathLocal + shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2]
            camName = 'CAM:cam_' + shotInfo[1] + '_' + shotInfo[2] + '_baked'
        if shotType == 3:
            fileName = pathLocal + shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2] + '_' +  shotInfo[3]
            camName = 'CAM:cam_' + shotInfo[1] + '_' + shotInfo[2] + '_' +  shotInfo[3] + '_baked'

        fileType = '_' + mode +  '_lr_c001.mb'
        
        # 处理非参考同名相机
        if mc.ls(camName):
            # 检测是否参考
            ifRef = mc.referenceQuery(camName,isNodeReferenced = 1)
            if not ifRef:
                mc.delete(camName)
                mc.namespace(set=':')
                mc.namespace(force=1, moveNamespace =['CAM:',':'])
                mc.namespace(removeNamespace = 'CAM:')
        
        # Camera
        from idmt.maya.commonCore.core_mayaCommon import sk_hbExportCam
        reload(sk_hbExportCam)
        if shotType == 2:
            sk_hbExportCam.sk_hbExportCam().camServerReference()   
        if shotType == 3:
            sk_hbExportCam.sk_hbExportCam().camServerReference(3)   

        
        mc.setAttr((camName + '.renderable'),1)
        mc.setAttr((camName + '.farClipPlane'),100000)

        try:
            mc.setAttr('perspShape.renderable',0)
        except:
            pass

        # skydome Setting
        #self.clSkydomeExcelLoad()
        
        mc.setAttr('defaultResolution.width', 1280)
        mc.setAttr('defaultResolution.height', 720)
        
        fileName = fileName + fileType
        print u'-------'
        print fileName
        mc.file(rename=fileName)
        mc.file(save=1,type = 'mayaBinary',f = 1)
        #mc.file(save=1,f = 1)
        return pathLocal
        print '\n'
        print (u'===============!!!Done  【%s】!!!===============' %'Save')
        print '\n'

    #--------------------------------#
    # camSetting
    # typeMode 2--do_xxx_xxx  |  3--do_xxx_xxx_xxx
    def sk4RLCamSetting(self,typeMode = 3):
        # 处理cam
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        if typeMode == 2:
            camName = 'CAM:cam_' + str(shotInfo[1]) + '_' + str(shotInfo[2]) +  '_baked'
        if typeMode == 3:
            camName = 'CAM:cam_' + str(shotInfo[1]) + '_' + str(shotInfo[2]) + '_' + str(shotInfo[3]) + '_baked'
        if mc.ls(camName, type='transform'):
            camShape = mc.listRelatives(mc.ls(camName, type='transform')[0], ni=1, c=1)[0]
            mc.setAttr((camShape + '.renderable'), 1)
            try:
                mc.setAttr(('perspShape.renderable'), 0)
            except:
                pass
        else:
            print(u'===============未找到有效CAM【%s】===============' % camName)
            mc.error(u'===============未找到有效CAM【%s】===============' % camName)

    #--------------------------------#
    # smoothSet，更新smooth信息
    def sk4RLDoSmooth(self, layerType=1):
        from idmt.maya.commonCore.core_mayaCommon import sk_smoothSet
        reload(sk_smoothSet)
        # 非PFX层用
        if layerType == 1:
            sk_smoothSet.sk_smoothSet().smoothSetDoSmooth()
            
    #--------------------------------#
    # 获取眉毛物体
    def sk4RLGBowObjs(self):
        allObjs = mc.ls(type = 'transform',l=1)
        bowObjs = []
        for obj in allObjs:
            keyWords = [':drape',':brow',':brow_r_',':brow_l_',':browr_',':browl_']
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
    def sk4RLFaceObjs(self):
        planeObjs = mc.ls('*:*_planar*',type = 'transform',l = 1)
        planeObjs = mc.ls('*:*_eyepatch_*',type = 'transform',l = 1) + planeObjs
        planeObjs = mc.ls('*:*mouth_prox*',type = 'transform',l = 1) + planeObjs
        
        if not planeObjs:
            planeObjs = []
        if planeObjs:
            need = []
            for obj in planeObjs:
                if ':MODEL|' in obj:
                    need.append(obj)
            if not need:
                need = []
            planeObjs = need
            
        return planeObjs

    #--------------------------------------------------------------------------------------------------------#
    #----------------------------------------------------------#
    # 【核心】 渲染层函数集
    #----------------------------------------------------------#
    # 非CO之类的层，主层给个临时材质球，方便精简文件
    def sk4RLMasterCleanCreate(self, layerType = '', selectObjType=0 ):
        print (u'===============!!!Start 【%s】!!!===============' % (u'MasterTemp层'))
        print 'Working...'

        # 物体信息
        objs = self.sk4RLObjectsTList()
        refCHR = objs[0]
        refPRP = objs[1]
        refSET = objs[2]
        refSKY = objs[3]
        refGroud = objs[4]
        refHair = objs[5]

        rlObjs = refCHR + refPRP + refSET

        layerType = 'BASECO'

        # 灯光
        lights = mc.ls(type='light')

        # 选取模式
        if selectObjType == 1:
            rlObjs = self.zmRLSelectMode()

        if rlObjs:
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
            meshes = mc.listRelatives(rlObjs,ni = 1,s = 1, type = 'mesh')
            #try:
            #    mc.sets(meshes,e = 1 , forceElement = shaderSG)
            #except:
            for mesh in meshes:
                try:
                    mc.sets(mesh,e = 1 , forceElement = shaderSG)
                except:
                    print u'===有物体无法赋予材质==='
                    print mesh
                    mc.error(u'===有物体无法赋予材质===')

            print (u'===============!!!Done  【%s】!!!===============' % (u'%MasterTemp层'))
            print '\n'



    #--------------------------------#
    # Color层
    def sk4RLCOCreate(self, layerType, selectObjType=0 ):
        print (u'===============!!!Start 【%s】!!!===============' % (u'%s_CO层' % layerType))
        print 'Working...'
        
        self.closeHairSysterm()

        # 物体信息
        objs = self.sk4RLObjectsTList()
        refCHR = objs[0]
        refPRP = objs[1]
        refSET = objs[2]
        refSKY = objs[3]
        refGroud = objs[4]
        refHair = objs[5]
        
        # 角色灯
        chrLTGrp = ''
        if mc.ls('LT_CHR'):
            chrLTGrp = 'LT_CHR'
        else:
            if mc.ls('*:LT_CHR'):
                chrLTGrp = mc.ls('*:LT_CHR',l = 1)[0]
            else:
                print u'===本文件没有灯光组：[%s]==='%('LT_CHR')
                mc.error(u'===本文件没有灯光组：[%s]==='%('LT_CHR'))
                
        # 分类信息
        if layerType in ['CHR']:
            rlTemps = (refCHR + refPRP)
            rlObjs = self.sk4RLObjInOutConfig(rlTemps,rlTemps,refHair)
            layerName = layerType + '_CO'
            rlLights = self.sk4RLGrpLights( chrLTGrp )
        if layerType in ['BG']:
            rlObjs = refSET
            layerName = layerType + '_CO'
            rlLights = self.sk4RLGrpLights('SET_GRP')
            
        MaskObjs = []

        # 选取模式
        if selectObjType == 1:
            rlLights = []
            rlObjs = self.sk4RLSelectMode()

        if rlObjs:
            # 创建RenderLayer
            if mc.ls(layerName):
                mc.delete(layerName)

            mc.createRenderLayer((rlObjs + rlLights), name= layerName, noRecurse=1, makeCurrent=1)

            # 隐藏灯光

            # Mask显示|隐藏
            if MaskObjs:
                meshes = mc.listRelatives(MaskObjs ,ni = 1 , ad = 1 , type = 'mesh',f = 1)
                if meshes:
                    for mesh in meshes:
                        mc.editRenderLayerAdjustment(mesh + '.primaryVisibility')
                        mc.setAttr((mesh + '.primaryVisibility'),l = 0)
                        mc.setAttr((mesh + '.primaryVisibility'), 0)

            # 辉光去除
            glowShaders = mc.ls(type = 'shaderGlow')
            if glowShaders:
                for glowNode in glowShaders:
                    mc.editRenderLayerAdjustment(glowNode + '.glowType')
                    mc.setAttr((glowNode + '.glowType'),l = 0)
                    mc.setAttr((glowNode + '.glowType'), 0)
                    mc.editRenderLayerAdjustment(glowNode + '.haloType')
                    mc.setAttr((glowNode + '.haloType'),l = 0)
                    mc.setAttr((glowNode + '.haloType'), 0)
        
            # 渲染设置
            mc.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'mayaSoftware', type='string')

            # 关闭光线追踪
            mc.editRenderLayerAdjustment('defaultRenderQuality.enableRaytracing')
            mc.setAttr('defaultRenderQuality.enableRaytracing', 0)

            # exr
            self.sk4RLFramebuffer('iff',16)

            mc.editRenderLayerAdjustment('defaultResolution.width')
            mc.setAttr('defaultResolution.width', 1280 )
            mc.editRenderLayerAdjustment('defaultResolution.height')
            mc.setAttr('defaultResolution.height', 720)

            print (u'===============!!!Done  【%s】!!!===============' % (u'%s_CO层' % layerType))
            print '\n'

        else:
            print (u'===============!!!Error  【%s】无物体!!!===============' % (u'%s_CO层' % layerType))
            print '\n'

    #--------------------------------#
    # Hair层
    def sk4RLHairCreate(self, layerType, selectObjType=0 , extraInfo = []):
        print (u'===============!!!Start 【%s】!!!===============' % (u'%s_HAIR层' % layerType))
        print 'Working...'

        self.closeHairSysterm()
        # 物体信息
        objs = self.sk4RLObjectsTList()
        refCHR = objs[0]
        refPRP = objs[1]
        refSET = objs[2]
        refSKY = objs[3]
        refGroud = objs[4]
        refHair = objs[5]
        
        MaskObjs = []
        
        # hairLight
        hairLTGrp = ''
        if mc.ls('LT_HAIR'):
            hairLTGrp = 'LT_HAIR'
        else:
            if mc.ls('*:LT_HAIR'):
                hairLTGrp = mc.ls('*:LT_HAIR',l = 1)[0]
            else:
                print u'===本文件没有灯光组：[%s]==='%('LT_HAIR')
                mc.error(u'===本文件没有灯光组：[%s]==='%('LT_HAIR'))
                
        if layerType in ['CHR']:
            rlObjs = refCHR + refPRP
            layerName = layerType + '_HAIR'
            MaskObjs = refPRP + self.sk4RLObjInOutConfig(refCHR,refCHR,refHair)
            rlLights = self.sk4RLGrpLights(hairLTGrp)

        # 选取模式
        if selectObjType == 1:
            rlLights = self.sk4RLGrpLights(hairLTGrp)
            rlObjs = self.sk4RLSelectMode()
            layerName = extraInfo[0]
            
        # 定制模式
        if selectObjType == 2:
            rlLights  = self.sk4RLGrpLights(hairLTGrp)
            rlObjs    = refCHR + refPRP
            layerName = extraInfo[0]
            refHair   = extraInfo[1]
            MaskObjs = refPRP + self.sk4RLObjInOutConfig(rlObjs,rlObjs,refHair)

        if rlObjs:
            # 创建RenderLayer
            if mc.ls(layerName):
                mc.delete(layerName)

            mc.createRenderLayer((rlObjs + rlLights), name= layerName, noRecurse=1, makeCurrent=1)

            # 隐藏灯光

            # Mask显示|隐藏

            if MaskObjs:
                # blackHole 材质
                shader_Node = 'SHD_' + layerType + '_Matte_Shader'
                if mc.ls(shader_Node):
                    mc.delete(shader_Node)
                shader_SG = 'SHD_' + layerType + '_Matte_SG'
                if mc.ls(shader_SG):
                    mc.delete(shader_SG)
                shader_Node = mc.shadingNode('lambert', asShader=True, name=shader_Node)
                mc.setAttr( (shader_Node + '.color') ,0,0,0, type = 'double3')
                mc.setAttr( (shader_Node + '.matteOpacityMode') , 0)
                shader_SG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name = shader_SG)
                mc.connectAttr((shader_Node + '.outColor'), (shader_SG + '.surfaceShader'))
                # 着色
                meshes = mc.listRelatives(MaskObjs ,ni = 1 , ad = 1 , type = 'mesh',f = 1)
                if meshes:
                    try:
                        mc.sets(meshes,e = 1 , forceElement = shader_SG)
                    except:
                        for mesh in meshes:
                            try:
                                mc.sets(mesh,e = 1 , forceElement = shader_SG)
                            except:
                                print u'===有物体无法赋予材质==='
                                print mesh
                                mc.error(u'===有物体无法赋予材质===')
                        
            # 渲染设置
            mc.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')

            # 关闭光线追踪
            mc.editRenderLayerAdjustment('miDefaultOptions.rayTracing')
            mc.setAttr('miDefaultOptions.rayTracing', 1)
            
            # 设置
            mc.editRenderLayerAdjustment('miDefaultOptions.maxSamples')
            mc.setAttr('miDefaultOptions.maxSamples', 3)
            mc.editRenderLayerAdjustment('miDefaultOptions.contrastR')
            mc.setAttr('miDefaultOptions.contrastR', 0.01)
            mc.editRenderLayerAdjustment('miDefaultOptions.contrastG')
            mc.setAttr('miDefaultOptions.contrastG', 0.01)
            mc.editRenderLayerAdjustment('miDefaultOptions.contrastB')
            mc.setAttr('miDefaultOptions.contrastB', 0.01)
            mc.editRenderLayerAdjustment('miDefaultOptions.contrastA')
            mc.setAttr('miDefaultOptions.contrastA', 0.01)
            mc.editRenderLayerAdjustment('miDefaultOptions.jitter')
            mc.setAttr('miDefaultOptions.jitter', 1)

            # exr
            self.sk4RLFramebuffer('iff',16)

            mc.editRenderLayerAdjustment('defaultResolution.width')
            mc.setAttr('defaultResolution.width', 1280 )
            mc.editRenderLayerAdjustment('defaultResolution.height')
            mc.setAttr('defaultResolution.height', 720)

            print (u'===============!!!Done  【%s】!!!===============' % (u'%s_HAIR层' % layerType))
            print '\n'

        else:
            print (u'===============!!!Error  【%s】无物体!!!===============' % (u'%s_HAIR层' % layerType))
            print '\n'

    # Occlusion层
    # 需要开启FG渲染
    # No Lights
    def sk4RLAOCreate(self, layerType, selectObjType=0 ,SGOType= 0 , shaderForece = 0 ):
        print (u'===============!!!Start 【%s】!!!===============' % (u'%s_AO层' % layerType))
        print 'Working...'

        self.closeHairSysterm()
        # 物体信息
        objs = self.sk4RLObjectsTList()
        refCHR = objs[0]
        refPRP = objs[1]
        refSET = objs[2]
        refSKY = objs[3]
        refGroud = objs[4]
        refHair = objs[5]
        
        SGNodes = self.sk4RLSGNodesGet()
        SGCHR = SGNodes[0]
        SGPRP = SGNodes[1]
        SGSET = SGNodes[2]
        SGSKY = SGNodes[3]
        SGGROUND = SGNodes[4]

        MaskObjs = []
        rlSGNodes = []
        
        if layerType in ['CHR']:
            rlTemps = refCHR + refPRP + refGroud
            rlObjs = self.sk4RLObjInOutConfig(rlTemps,rlTemps,refHair)
            MaskObjs = refGroud
            rlSGNodes = SGCHR + SGPRP + SGGROUND
            layerName = layerType + '_AO'
        if layerType in ['CHRD']:
            rlObjs = refCHR + refPRP + refSET
            MaskObjs = refCHR + refPRP
            rlSGNodes = SGCHR + SGPRP + SGSET
            layerName = layerType + '_OSD'
        if layerType in ['BG']:
            rlObjs = refSET
            rlSGNodes = SGSET
            layerName = layerType + '_AO'

        # 选取模式
        if selectObjType == 1:
            rlObjs = self.sk4RLSelectMode()
            
        rlLights = []

        if rlObjs:
            # 特殊处理，半透明用
            # 获取信息必须在masterLayer进行
            transpancyObjs    = self.sk4RLTransparencyObjsByType(rlObjs , 0)
            transpancySGNodes = transpancyObjs[0]
            transpancyMeshes  = transpancyObjs[1]
            transpancyNode    = transpancyObjs[2]
            transpancyGrps    = transpancyObjs[3]

            # 创建RenderLayer
            if mc.ls(layerName):
                mc.delete(layerName)

            mc.createRenderLayer((rlObjs + rlLights), name = layerName, noRecurse=1, makeCurrent=1)

            # Mask显示|隐藏
            if MaskObjs:
                meshes = mc.listRelatives(MaskObjs ,ni = 1 , ad = 1 , type = 'mesh',f = 1)
                if meshes:
                    for mesh in meshes:
                        mc.editRenderLayerAdjustment(mesh + '.primaryVisibility')
                        try:
                            mc.setAttr((mesh + '.primaryVisibility'), 0)
                        except:
                            mc.setAttr((mesh + '.primaryVisibility'),l = 0)
                            mc.setAttr((mesh + '.primaryVisibility'), 0)
                            
            # 处理场景属性
            if layerType in ['CHRD']:
                if refSET:
                    for obj in refSET:
                        if not mc.ls(obj + '.miLabel'):
                            mc.addAttr(obj,ln = 'miLabel', at = 'double')
                        mc.setAttr((obj + '.miLabel'),1)

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
                    
            shader_Node = mc.shadingNode('lambert', asShader=True, name=shader_Node)
            AONode = mc.shadingNode('mib_amb_occlusion', asTexture=True, name=AO_Node)
            mc.setAttr((shader_Node + '.color'),1,1,1,type = 'double3')
            mc.setAttr((shader_Node + '.diffuse'),0)
            mc.connectAttr((AO_Node + '.outValue'), (shader_Node + '.ambientColor'))
            if layerType in ['CHRD']:
                mc.setAttr((AO_Node + '.id_nonself'),1)
            
            # 经典连材质模式
            if not SGOType:
                AO_SG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name = AO_SG)
                mc.connectAttr((shader_Node + '.outColor'), (AO_SG + '.surfaceShader'))
                
            if(layerType in ['CHR']):
                mc.setAttr(('%s.%s') % (AONode, 'samples'), 128)
                mc.setAttr(('%s.%s') % (AONode, 'max_distance'), 5)
                mc.setAttr(('%s.%s') % (AONode, 'output_mode'), 0)

            if(layerType in ['CHRD']):
                mc.setAttr(('%s.%s') % (AONode, 'samples'), 64)
                mc.setAttr(('%s.%s') % (AONode, 'max_distance'), 10)
                mc.setAttr(('%s.%s') % (AONode, 'output_mode'), 0)


            if(layerType in ['SET','BG']):
                mc.setAttr(('%s.%s') % (AONode, 'samples'), 64)
                mc.setAttr(('%s.%s') % (AONode, 'max_distance'), 10)
                mc.setAttr(('%s.%s') % (AONode, 'output_mode'), 0)

            # 优先全局着色
            # 经典连材质模式
            if not SGOType:
                # layerObjs 类型必然是transform
                for obj in rlObjs:
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
                    mc.setAttr((shaderTrans_Node + '.diffuse'),0)
                    mc.connectAttr((AOTrans_Node + '.outValue'), (shaderTrans_Node + '.ambientColor'))
                    mc.connectAttr((luminanceNode + '.outValue'), (shaderTrans_Node + '.transparencyR'))
                    mc.connectAttr((luminanceNode + '.outValue'), (shaderTrans_Node + '.transparencyG'))
                    mc.connectAttr((luminanceNode + '.outValue'), (shaderTrans_Node + '.transparencyB'))
                    if layerType in ['CHRD']:
                        mc.setAttr((AOTrans_Node + '.id_nonself'),1)
                    # 经典连材质模式
                    if not SGOType:
                        AOTrans_SG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name = AOTrans_SG)
                        mc.connectAttr((shaderTrans_Node + '.outColor'), (AOTrans_SG + '.surfaceShader'))

                    # 透明连接
                    self.sk4RLTransShaderConnection(transpancyNode[i], luminanceNode,'value')
                    
                    # file贴图反转
                    if '.outTransparency' in transpancyNode[i]:
                        mc.editRenderLayerAdjustment(transpancyNode[i].split('.')[0] + '.invert')
                        mc.setAttr((transpancyNode[i].split('.')[0] + ".invert"), 1)

                    # 设置AO
                    if(layerType in ['CHR']):
                        mc.setAttr(('%s.%s') % (AOTrans_Node, 'samples'), 128)
                        mc.setAttr(('%s.%s') % (AOTrans_Node, 'max_distance'), 5)
                        mc.setAttr(('%s.%s') % (AOTrans_Node, 'output_mode'), 0)

                    if(layerType in ['CHRD']):
                        mc.setAttr(('%s.%s') % (AOTrans_Node, 'samples'), 64)
                        mc.setAttr(('%s.%s') % (AOTrans_Node, 'max_distance'), 10)
                        mc.setAttr(('%s.%s') % (AOTrans_Node, 'output_mode'), 0)


                    if(layerType in ['SET','BG']):
                        mc.setAttr(('%s.%s') % (AOTrans_Node, 'samples'), 64)
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
                            meshesReserve = self.sk4RLFaceObjReverse(meshes)
                            try:
                                if meshesReserve:
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
                            mc.sets(meshes,e = 1 , forceElement = AOTrans_SG)
                        except:
                            for mesh in meshes:
                                try:
                                    mc.sets(mesh,e = 1 , forceElement = AOTrans_SG)
                                except:
                                    print u'===有物体无法赋予材质==='
                                    print mesh
                                    mc.error(u'===有物体无法赋予材质===')
            # 设置
            # self.sk4RLCommonConfig()                  

            # 渲染设置
            mc.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')

            # 开启光线追踪
            mc.editRenderLayerAdjustment('miDefaultOptions.rayTracing')
            mc.setAttr('miDefaultOptions.rayTracing', 1)

            # FG开启
            mc.editRenderLayerAdjustment('miDefaultOptions.finalGather')
            mc.setAttr('miDefaultOptions.finalGather', 0)

            # exr
            self.sk4RLFramebuffer('iff',16)

            mc.editRenderLayerAdjustment('defaultResolution.width')
            mc.setAttr('defaultResolution.width', 1280 )
            mc.editRenderLayerAdjustment('defaultResolution.height')
            mc.setAttr('defaultResolution.height', 720)

            print (u'===============!!!Done  【%s】!!!===============' % (u'%s_AO层' % layerType))
            print '\n'

        else:
            print (u'===============!!!Error  【%s】无物体!!!===============' % (u'%s_AO层' % layerType))
            print '\n'

    # Normal层
    # No Lights
    # 放弃与AO类似部分，直接amb_occ连shader的color，trans连shader的trans
    def sk4RLNMCreate(self, layerType, selectObjType=0 , SGOType = 0 , shaderForece = 0):
        print (u'===============!!!Start 【%s】!!!===============' % (u'%s_NM层' % layerType))
        print 'Working...'

        self.closeHairSysterm()
        # 物体信息
        objs = self.sk4RLObjectsTList()
        refCHR = objs[0]
        refPRP = objs[1]
        refSET = objs[2]
        refSKY = objs[3]
        refGroud = objs[4]
        refHair = objs[5]
        
        SGNodes = self.sk4RLSGNodesGet()
        SGCHR = SGNodes[0]
        SGPRP = SGNodes[1]
        SGSET = SGNodes[2]
        SGSKY = SGNodes[3]
        SGGROUND = SGNodes[4]

        MaskObjs = []
        rlSGNodes = []
        
        if layerType in ['CHR']:
            rlTemps = refCHR + refPRP
            rlObjs = self.sk4RLObjInOutConfig(rlTemps,rlTemps,refHair)
            rlSGNodes = SGCHR + SGPRP
            layerName = layerType + '_NM'
        if layerType in ['BG']:
            rlObjs = refSET
            rlSGNodes = SGSET
            layerName = layerType + '_NM'

        # 选取模式
        if selectObjType == 1:
            rlObjs = self.sk4RLSelectMode()
            
        rlLights = []

        if rlObjs:
            # 特殊处理，半透明用
            # 获取信息必须在masterLayer进行
            transpancyObjs    = self.sk4RLTransparencyObjsByType(rlObjs,0)
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

            mc.createRenderLayer((rlObjs + rlLights), name=layerName, noRecurse=1, makeCurrent=1)

            # Mask显示|隐藏
            if MaskObjs:
                meshes = mc.listRelatives(MaskObjs ,ni = 1 , ad = 1 , type = 'mesh',f = 1)
                if meshes:
                    for mesh in meshes:
                        mc.editRenderLayerAdjustment(mesh + '.primaryVisibility')
                        mc.setAttr((mesh + '.primaryVisibility'),l = 0)
                        mc.setAttr((mesh + '.primaryVisibility'), 0)

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
            mc.setAttr((shader_Node + '.color'),1,1,1,type = 'double3')
            mc.connectAttr((NM_Node + '.outValue'), (shader_Node + '.ambientColor'))
            # 经典连材质模式
            if not SGOType:
                NM_SG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name = NM_SG)
                mc.connectAttr((shader_Node + '.outColor'), (NM_SG + '.surfaceShader'))

            if(layerType in ['CHR']):
                mc.setAttr(('%s.%s') % (NM_Node, 'samples'), 128)
                mc.setAttr(('%s.%s') % (NM_Node, 'max_distance'), 5)
                mc.setAttr(('%s.%s') % (NM_Node, 'output_mode'), 3)

            if(layerType in ['SET','BG']):
                mc.setAttr(('%s.%s') % (NM_Node, 'samples'), 64)
                mc.setAttr(('%s.%s') % (NM_Node, 'max_distance'), 10)
                mc.setAttr(('%s.%s') % (NM_Node, 'output_mode'), 3)

            #print u'-----'
            #print transpancyObjs

            # 优先全局着色
            # 经典连材质模式
            if not SGOType:
                # layerObjs 类型必然是transform
                for obj in rlObjs:
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
                    shaderTrsNode = mc.shadingNode('lambert', asShader=True, name = shaderTrsNode)
                    NMTrsNode = mc.shadingNode('mib_amb_occlusion', asTexture=True, name = NMTrsNode)
                    luminanceNode = mc.shadingNode('luminance', asUtility = True, name = luminanceNode)

                    # 连接
                    mc.setAttr((shaderTrsNode + '.color'),1,1,1,type = 'double3')
                    mc.connectAttr((NMTrsNode + '.outValue'), (shaderTrsNode + '.ambientColor'))
                    mc.connectAttr((luminanceNode + '.outValue'), (shaderTrsNode + '.transparencyR'))
                    mc.connectAttr((luminanceNode + '.outValue'), (shaderTrsNode + '.transparencyG'))
                    mc.connectAttr((luminanceNode + '.outValue'), (shaderTrsNode + '.transparencyB'))
                    # 经典连材质模式
                    if not SGOType:
                        NMTrans_SG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name = NMTrans_SG)
                        mc.connectAttr((shaderTrsNode + '.outColor'), (NMTrans_SG + '.surfaceShader'))

                    # 透明连接
                    self.sk4RLTransShaderConnection(transpancyNode[i],  luminanceNode, 'value')

                    # file贴图反转
                    if '.outTransparency' in transpancyNode[i]:
                        mc.editRenderLayerAdjustment(transpancyNode[i].split('.')[0] + '.invert')
                        mc.setAttr((transpancyNode[i].split('.')[0] + ".invert"), 1)

                    if(layerType in ['CHR']):
                        mc.setAttr(('%s.%s') % (NMTrsNode, 'samples'), 128)
                        mc.setAttr(('%s.%s') % (NMTrsNode, 'max_distance'), 5)
                        mc.setAttr(('%s.%s') % (NMTrsNode, 'output_mode'), 3)

                    if(layerType in ['SET','BG']):
                        mc.setAttr(('%s.%s') % (NMTrsNode, 'samples'), 64)
                        mc.setAttr(('%s.%s') % (NMTrsNode, 'max_distance'), 10)
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
                            meshesReserve = self.sk4RLFaceObjReverse(meshes)
                            try:
                                if meshesReserve:
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
            # self.sk4RLCommonConfig()

            # 渲染设置
            mc.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')

            # 关闭光线追踪
            mc.editRenderLayerAdjustment('miDefaultOptions.rayTracing')
            mc.setAttr('miDefaultOptions.rayTracing', 1)

            # exr
            self.sk4RLFramebuffer('iff',16)

            mc.editRenderLayerAdjustment('defaultResolution.width')
            mc.setAttr('defaultResolution.width', 1280 )
            mc.editRenderLayerAdjustment('defaultResolution.height')
            mc.setAttr('defaultResolution.height', 720)

            print (u'===============!!!Done  【%s】!!!===============' % (u'%s_NM层' % layerType))
            print '\n'
        else:
            print (u'===============!!!Error  【%s】无物体!!!===============' % (u'%s_NM层' % layerType))
            print '\n'

    # ZDEPTH层
    # No Lights
    def sk4RLZDEPTHCreate(self, layerType, selectObjType=0, distance=14000 ,SGOType = 0 , shaderForece = 0):
        print (u'===============!!!Start 【%s】!!!===============' % (u'%s_ZDEPTH层' % layerType))
        print 'Working...'
        
        self.closeHairSysterm()

        # 物体信息
        objs = self.sk4RLObjectsTList()
        refCHR = objs[0]
        refPRP = objs[1]
        refSET = objs[2]
        refSKY = objs[3]
        refGroud = objs[4]
        refHair = objs[5]
        
        SGNodes = self.sk4RLSGNodesGet()
        SGCHR = SGNodes[0]
        SGPRP = SGNodes[1]
        SGSET = SGNodes[2]
        SGSKY = SGNodes[3]
        SGGROUND = SGNodes[4]

        MaskObjs = []
        rlSGNodes = []

        if layerType in ['CHR']:
            rlObjs = []
            rlSGNodes = []
            layerName = layerType + '_ZDEPTH'

        if layerType in ['BG']:
            rlObjs = refSET
            rlSGNodes = SGSET
            layerName = layerType + '_ZDEPTH'

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
            distance = 1500
        else:
            distance = 1500

        # 选取模式
        if selectObjType == 1:
            rlObjs = self.sk4RLSelectMode()
            
        rlLights = []

        if rlObjs:
            # 特殊处理，半透明用
            # 获取信息必须在masterLayer进行
            transpancyObjs    = self.sk4RLTransparencyObjsByType(rlObjs,0)
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

            mc.createRenderLayer((rlObjs+rlLights), name=layerName, noRecurse=1, makeCurrent=1)
            
            # Mask显示|隐藏
            if MaskObjs:
                meshes = mc.listRelatives(MaskObjs ,ni = 1 , ad = 1 , type = 'mesh',f = 1)
                if meshes:
                    for mesh in meshes:
                        mc.editRenderLayerAdjustment(mesh + '.primaryVisibility')
                        mc.setAttr((mesh + '.primaryVisibility'),l = 0)
                        mc.setAttr((mesh + '.primaryVisibility'), 0)
            
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
                for obj in rlObjs:
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
                    
                    shaderTrsNode = 'SHD_' + layerType + '_' + keySGInfo + '_ZDEPTH'
                    if mc.ls(shaderTrsNode):
                        mc.delete(shaderTrsNode)
                    setRangeZ = 'SHD_' + layerType + '_' + keySGInfo + '_ZDEPTH_setRangeZ'
                    if mc.ls(setRangeZ):
                        mc.delete(setRangeZ)
                    multDivZ = 'SHD_' + layerType + '_' + keySGInfo + '_ZDEPTH_multDivZ'
                    if mc.ls(multDivZ):
                        mc.delete(multDivZ)
                    sampleInfoZ = 'SHD_' + layerType + '_' + keySGInfo + '_ZDEPTH_sampInfoZ'
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
                    # 经典连材质模式
                    if not SGOType:
                        ZDPTransSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name = ZDPTransSG)
                        mc.connectAttr((shaderTrsNode + '.outColor'), (ZDPTransSG + '.surfaceShader'))               
                    
                    # 透明连接
                    self.sk4RLTransShaderConnection(transpancyNode[i], luminanceNode, 'value')

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
                            meshesReserve = self.sk4RLFaceObjReverse(meshes)
                            try:
                                if meshesReserve:
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
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'mayaSoftware', type='string')

            # 关闭光线追踪
            mc.editRenderLayerAdjustment('defaultRenderQuality.enableRaytracing')
            mc.setAttr('defaultRenderQuality.enableRaytracing', 0)

            # exr
            self.sk4RLFramebuffer('iff',16)

            mc.editRenderLayerAdjustment('defaultResolution.width')
            mc.setAttr('defaultResolution.width', 1280 )
            mc.editRenderLayerAdjustment('defaultResolution.height')
            mc.setAttr('defaultResolution.height', 720)

            print (u'===============!!!Done  【%s】!!!===============' % (u'%s_ZDEPTH层' % layerType))
            print '\n'
        else:
            print (u'===============!!!Error  【%s】无物体!!!===============' % (u'%s_ZDEPTH层' % layerType))
            print '\n'
            
    # shadow层
    def sk4RLSHDCreate( self, layerType, selectObjType = 0 ,SGOType = 0 , shaderForece = 0):
        print (u'===============!!!Start 【%s】!!!===============' % (u'%s_SHD层' % layerType))
        print 'Working...'
        
        self.closeHairSysterm()

        # 物体
        objs = self.sk4RLObjectsTList()
        refCHR = objs[0]
        refPRP = objs[1]
        refSET = objs[2]
        refSKY = objs[3]
        refGroud = objs[4]
        refHair = objs[5]

        SGNodes = self.sk4RLSGNodesGet()
        SGCHR = SGNodes[0]
        SGPRP = SGNodes[1]
        SGSET = SGNodes[2]
        SGSKY = SGNodes[3]
        SGGROUND = SGNodes[4]
        SGHAIR = SGNodes[5]

        MaskObjs = []
        rlSGNodes = []
        
        rlLights = []
        
        # 阴影灯
        sdLTGrp = ''
        if mc.ls('LT_CHD'):
            sdLTGrp = 'LT_CHD'
        else:
            if mc.ls('*:LT_CHD'):
                sdLTGrp = mc.ls('*:LT_CHD',l = 1)[0]
            else:
                print u'===本文件没有灯光组：[%s]==='%('LT_CHD')
                mc.error(u'===本文件没有灯光组：[%s]==='%('LT_CHD'))
        
        if layerType in ['CHR']:
            rlObjs = refCHR + refPRP + refSET
            layerName = layerType + '_SHD'
            MaskObjs = refCHR + refPRP
            rlSGNodes = SGCHR + SGPRP + SGSET
            rlLights = self.sk4RLGrpLights(sdLTGrp)

        # 灯光
        lights = mc.ls(type='light')

        # 选取模式
        if selectObjType == 1:
            rlObjs = self.sk4RLSelectMode()

        if rlObjs:
            # 特殊处理，半透明用
            # 获取信息必须在masterLayer进行
            transpancyObjs    = self.sk4RLTransparencyObjsByType(rlObjs,0)
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

            mc.createRenderLayer((rlObjs+rlLights), name=layerName, noRecurse=1, makeCurrent=1)
            
            # [提速] 清理smooth节点
            smsNodes = mc.ls('foodSMS_*' ,type = 'polySmoothFace')
            if smsNodes:
                mc.delete(smsNodes)

            # 通用shadow材质
            shader_Node = 'SHD_' + layerType + '_SD_Shader'
            if mc.ls(shader_Node):
                mc.delete(shader_Node)
            # 经典连材质模式
            if not SGOType:
                SD_SG = 'SHD_' + layerType + '_SD_SG'
                if mc.ls(SD_SG):
                    mc.delete(SD_SG)
            shader_Node = mc.shadingNode('lambert', asShader=True, name = shader_Node)
            mc.setAttr((shader_Node + '.color') ,1,1,1, type = 'double3')
            mc.setAttr((shader_Node + '.ambientColor') ,0,0,0, type = 'double3')
            mc.setAttr((shader_Node + '.diffuse') ,1)
            # 经典着色
            if not SGOType:
                SD_SG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name = SD_SG)
                mc.connectAttr((shader_Node + '.outColor'), (SD_SG + '.surfaceShader'))
            
            print u'\n'
            print u'======[%s]Starting======'%(u'角色道具接收阴影关闭')
            # 投射阴影
            if MaskObjs:
                meshes = mc.listRelatives(MaskObjs ,ni = 1 , ad = 1 , type = 'mesh',f = 1)
                if meshes:
                    for mesh in meshes:
                        mc.editRenderLayerAdjustment(mesh + '.primaryVisibility')
                        try:
                            mc.setAttr((mesh + '.primaryVisibility'), 0)
                        except:
                            mc.setAttr((mesh + '.primaryVisibility'),l = 0)
                            mc.setAttr((mesh + '.primaryVisibility'), 0)
                        mc.editRenderLayerAdjustment(mesh + '.receiveShadows')
                        try:
                            mc.setAttr((mesh + '.receiveShadows'), 0)
                        except:
                            mc.setAttr((mesh + '.receiveShadows'),l = 0)
                            mc.setAttr((mesh + '.receiveShadows'), 0)
                        mc.editRenderLayerAdjustment(mesh + '.castsShadows')
                        try:
                            mc.setAttr((mesh + '.castsShadows'), 1)
                        except:
                            mc.setAttr((mesh + '.castsShadows'),l = 0)
                            mc.setAttr((mesh + '.castsShadows'), 1)
            print u'======[%s]Done！！！======'%(u'角色道具接收阴影关闭')
            print u'\n'      
            print u'======[%s]Starting======'%(u'场景类别投射阴影关闭')
            # 接收阴影阴影
            if refSET:
                meshes = mc.listRelatives(refSET ,ni = 1 , ad = 1 , type = 'mesh',f = 1)
                if meshes:
                    print len(meshes)
                    for i in range(len(meshes)):
                        mesh = meshes[i]
                        if i % 1000 == 0:
                            print '-'
                            print i
                        #mc.editRenderLayerAdjustment(mesh + '.primaryVisibility')
                        try:
                            mc.setAttr((mesh + '.primaryVisibility'), 1)
                        except:
                            mc.setAttr((mesh + '.primaryVisibility'),l = 0)
                            mc.setAttr((mesh + '.primaryVisibility'), 1)
                        #mc.editRenderLayerAdjustment(mesh + '.receiveShadows')
                        try:
                            mc.setAttr((mesh + '.receiveShadows'), 1)
                        except:
                            mc.setAttr((mesh + '.receiveShadows'),l = 0)
                            mc.setAttr((mesh + '.receiveShadows'), 1)
                        #mc.editRenderLayerAdjustment(mesh + '.castsShadows')
                        try:
                            mc.setAttr((mesh + '.castsShadows'), 0)
                        except:
                            mc.setAttr((mesh + '.castsShadows'),l = 0)
                            mc.setAttr((mesh + '.castsShadows'), 0)
            print u'======[%s]Done！！！======'%(u'场景类别投射阴影关闭')
            print u'\n'
            
            # lights
            for light in rlLights:
                lightShape = mc.listRelatives(light ,s = 1)[0]
                mc.setAttr((lightShape + '.color'),0,0,0,type = 'double3')
                mc.setAttr((lightShape + '.shadowColor'),1,1,1,type = 'double3')
                
            # 还原smooth
            #self.sk4RLSwDoSmooth()
                
            # 经典连材质模式
            if not SGOType:
                # layerObjs 类型必然是transform
                for obj in rlObjs:
                    # 属于matter
                    if obj in MaskObjs:
                        continue
                    if obj in transpancyGrps:
                        continue
                    mesh = mc.listRelatives(obj,s = 1 ,ni  = 1, type = 'mesh',f=1)
                    if not mesh:
                        continue
                    mesh = mesh[0]
                    shaderSG = SD_SG
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
                    
                    shaderTrsNode = 'SHD_' + layerType + '_' + keySGInfo + '_SD_Shader'
                    if mc.ls(shaderTrsNode):
                        mc.delete(shaderTrsNode)
                    luminanceNode = 'SHD_' + layerType + '_' + keySGInfo + '_SD_LUM_Shader'
                    if mc.ls(luminanceNode):
                        mc.delete(luminanceNode)
                    # 经典连材质模式
                    if not SGOType:
                        SDTrsSG = 'SHD_' + layerType + '_' + keySGInfo + '_SD_SG'
                        if mc.ls(SDTrsSG):
                            mc.delete(SDTrsSG)
                            
                    shaderTrsNode = mc.shadingNode('lambert', asShader=True, name = shaderTrsNode)
                    luminanceNode = mc.shadingNode('luminance', asUtility = True, name = luminanceNode)
                    mc.setAttr((shaderTrsNode + '.color') ,1,1,1, type = 'double3')
                    mc.setAttr((shaderTrsNode + '.ambientColor') ,0,0,0, type = 'double3')
                    mc.setAttr((shaderTrsNode + '.diffuse') ,1)
                    mc.connectAttr((luminanceNode + '.outValue'), (shaderTrsNode + '.transparencyR'))
                    mc.connectAttr((luminanceNode + '.outValue'), (shaderTrsNode + '.transparencyG'))
                    mc.connectAttr((luminanceNode + '.outValue'), (shaderTrsNode + '.transparencyB'))
                    # 经典连材质模式
                    if not SGOType:
                        SDTrsSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name = SDTrsSG)
                        mc.connectAttr((shaderTrsNode + '.outColor'), (SDTrsSG + '.surfaceShader'))
                    
                    
                    # 透明连接
                    self.sk4RLTransShaderConnection(transpancyNode[i], luminanceNode, 'value')

                    # file贴图反转
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
                                    mc.sets(faceGrps,e = 1 , forceElement = SD_SG)
                                except:
                                    for grp in faceGrps:
                                        try:
                                            mc.sets(grp,e = 1 , forceElement = SD_SG)
                                        except:
                                            print u'===有物体无法赋予材质==='
                                            print grp
                                            mc.error(u'===有物体无法赋予材质===')
                        if shaderForece == 1:
                            meshesReserve = self.sk4RLFaceObjReverse(meshes)
                            try:
                                if meshesReserve:
                                    mc.sets(meshesReserve,e = 1 , forceElement = SD_SG)
                            except:
                                for mesh in meshesReserve:
                                    if not mesh:
                                        continue
                                    try:
                                        mc.sets(mesh,e = 1 , forceElement = SD_SG)
                                    except:
                                        print u'===有物体无法赋予材质==='
                                        print mesh
                                        mc.error(u'===有物体无法赋予材质===')

                        # 选面
                        try:
                            mc.sets(meshes,e = 1 , forceElement = SDTrsSG)
                        except:
                            for mesh in meshes:
                                try:
                                    mc.sets(mesh,e = 1 , forceElement = SDTrsSG)
                                except:
                                    print u'===有物体无法赋予材质==='
                                    print mesh
                                    mc.error(u'===有物体无法赋予材质===')

                    # SG连接连接着色
                    if SGOType:
                        shaderInfo = mc.listConnections((transpancySGNodes[i] + '.surfaceShader'),s = 1,plugs = 1)
                        if shaderInfo:
                            shaderInfo = shaderInfo[0]
                            mc.editRenderLayerAdjustment(transpancySGNodes[i] + '.surfaceShader')
                            mc.disconnectAttr(shaderInfo, (transpancySGNodes[i] + '.surfaceShader'))
                            mc.connectAttr((shaderTrsNode + '.outColor'), (transpancySGNodes[i] + '.surfaceShader'), f=1)

            # 设置
            # self.sk4RLCommonConfig()

            # 渲染器
            mc.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'mayaSoftware', type='string')

            # raytrace
            mc.editRenderLayerAdjustment('defaultRenderQuality.enableRaytracing')
            mc.setAttr("defaultRenderQuality.enableRaytracing",0)

            # 格式
            self.sk4RLFramebuffer('iff',16)

            mc.editRenderLayerAdjustment('defaultResolution.width')
            mc.setAttr('defaultResolution.width', 1280 )
            mc.editRenderLayerAdjustment('defaultResolution.height')
            mc.setAttr('defaultResolution.height', 720)

            print (u'===============!!!Done  【%s】!!!===============' % (u'%s_SHD层' % layerType))
            print '\n'
        else:
            print (u'===============!!!Error  【%s】无物体!!!===============' % (u'%s_SHD层' % layerType))
            print '\n'
 
    #----------------------------------------------------------------------------------------#
    # 【通用：RGB分层】
    # Author : 沈  康
    # Data   : 2013_11_18/2014_05_10
    # Data   : 2014_07_19/2014_07_19
    #-------------------------------------------------#
        
    #-------------------------------------------------#
    # 核心创建层函数
    def sk4RLRGBCreate(self, layerType , shaderForece = 0):
        print (u'===============!!!Start 【%s】!!!===============' % (u'%s_%s层' % (layerType.split('_')[0],layerType.split('_')[1])))
        print 'Working...'

        self.closeHairSysterm()
        
        checkInfo = layerType.split('_')

        # 物体信息
        objs = self.sk4RLObjectsTList()
        refCHR = objs[0]
        refPRP = objs[1]
        refSET = objs[2]
        refSKY = objs[3]
        refGroud = objs[4]
        refHair = objs[5]
        
        layerName = ''
        layerObjs = []
        RObjs = []
        GObjs = []
        BObjs = []
        MObjs = []

        if checkInfo[1] == 'BSR':
            RObjs = refCHR
            GObjs = refPRP
            BObjs = refSET
            MObjs = []
            layerObjs = refCHR + refPRP + refSET
        else:
            # 读取RGB
            RGBInfos = []
            RGBKey = ''
            if checkInfo[1] == 'FBR':
                RGBKey = 'FullBody'
            if checkInfo[1] == 'SPR':
                RGBKey = 'ShortParts'
            from idmt.maya.commonCore.core_renderLayer import sk_renderLayerCore
            reload(sk_renderLayerCore)
            RGBInfos = sk_renderLayerCore.sk_renderLayerCore().ydRLayerRGBObjectsConfig(RGBKey,1,1)

            #if checkInfo[1] == 'FBR':
            #    print '---'
            #    print RGBInfos
            # 处理RGB
            if RGBInfos[0]:
                for id in range(len(RGBInfos[0])):
                    if RGBInfos[0][id][0] == 1:
                        RObjs = RObjs + RGBInfos[1][id]
                    if RGBInfos[0][id][1] == 1:
                        GObjs = GObjs + RGBInfos[1][id]
                    if RGBInfos[0][id][2] == 1:
                        BObjs = BObjs + RGBInfos[1][id]
                    if RGBInfos[0][id][0] == RGBInfos[0][id][1] == RGBInfos[0][id][2] == 0:
                        MObjs = MObjs + RGBInfos[1][id]
                layerObjs = refCHR + refPRP + refSET
            else:
                layerObjs = []

        layerName = checkInfo[0] + '_' + checkInfo[-1]

        if (layerObjs):

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
                    noRGBFaces[obj] = self.sk4RLFaceObjReverse(noRGBFaces[obj])
            
            # maskObjs，仅限于 非选面的
            matteObjs = []
            for obj in layerObjs:
                if checkInfo[-1] in ['BSR']:
                    if obj not in (RObjs + GObjs + BObjs + MObjs):
                        matteObjs.append(obj)
                else:
                    if obj not in (RGrps + GGrps + BGrps + MGrps):
                        mesh = mc.listRelatives(obj,ni = 1, s = 1,type = 'mesh',f = 1)
                        if not mesh:
                            continue
                        mesh = mesh[0]
                        matteObjs.append(mesh)

            # 特殊处理，半透明用
            # 获取信息必须在masterLayer进行
            transpancyObjs    = self.sk4RLTransparencyObjsByType(layerObjs , 0)
            transpancySGNodes = transpancyObjs[0]
            transpancyMeshes  = transpancyObjs[1]
            transpancyNode    = transpancyObjs[2]
            transpancyGrps    = transpancyObjs[3]
            
            #print '------'
            #print transpancyObjs
            
            # allTransMeshes
            allTransGrps = []
            for info in transpancyGrps:
                allTransGrps = allTransGrps + info
            if allTransGrps:
                allTransGrps = list(set(allTransGrps))

            # 创建RenderLayer
            if mc.ls(layerName):
                mc.delete(layerName)

            mc.createRenderLayer(layerObjs, name=layerName, noRecurse=1, makeCurrent=1)

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
            from idmt.maya.commonCore.core_mayaCommon import sk_pyCommon
            reload(sk_pyCommon)
            
            # layerObjs 类型必然是transform
            doNotMatterObjs = []
            for obj in layerObjs:
                checkObj = ''
                if checkInfo[-1] in ['BSR']:
                    checkObj = obj
                else:
                    checkObj = mc.listRelatives(obj,s = 1 , ni = 1 ,type = 'mesh',f = 1)
                    if not checkObj:
                        continue
                    checkObj = checkObj[0]
                # 属于matter
                if checkObj in matteObjs:
                    if mc.nodeType(obj) == 'mesh':
                        mesh = mc.ls(checkObj,l = 1)[0]
                    else:
                        mesh = mc.listRelatives(obj,s = 1 ,ni  = 1, type = 'mesh',f=1)
                        if not mesh:
                            continue
                        mesh = mesh[0]
                    shaderSG = MatteSG
                    mc.select(mesh)
                    try:
                        mc.sets(mesh,e = 1 , forceElement = shaderSG)
                    except:
                        print u'===有物体无法赋予材质==='
                        print mesh
                        mc.error(u'===有物体无法赋予材质===')            

                # 不属于matter
                else:
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
                                #meshesReserve = self.sk4RLFaceObjReverse(noRGBMeshes)
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
                                    mesh = mc.listRelatives(obj,s = 1,ni =1,type = 'mesh')
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
                        if obj in RGrps:
                            grpIds = sk_pyCommon.sk_pyCommon().checkListSameAllIndex(RGrps,obj)
                            RGBMeshes = []
                            for idNum in grpIds:
                                RGBMeshes.append(RObjs[idNum])
                            shaderSG = RSG
                            #if checkInfo[1] == 'FBR':
                                #print '---'
                                #print grpIds
                                #print RGBMeshes
                                #print shaderSG
                            # 物体着色
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
                        if obj in BGrps:
                            grpIds = sk_pyCommon.sk_pyCommon().checkListSameAllIndex(BGrps,obj)
                            RGBMeshes = []
                            for idNum in grpIds:
                                RGBMeshes.append(BObjs[idNum])
                            shaderSG = BSG
                            # 物体着色
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
                        if obj in MGrps:
                            grpIds = sk_pyCommon.sk_pyCommon().checkListSameAllIndex(MGrps,obj)
                            RGBMeshes = []
                            for idNum in grpIds:
                                RGBMeshes.append(MObjs[idNum])
                            shaderSG = MSG
                            # 物体着色
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
                        self.sk4RLTransShaderConnection(transpancyNode[i], luminanceR_Node, 'value')

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
                        self.sk4RLTransShaderConnection(transpancyNode[i], luminanceG_Node, 'value')

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
                        shader_B_Trs_Node = mc.shadingNode('lambert', asShader=True, name = shader_B_Trs_Node)
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
                        self.sk4RLTransShaderConnection(transpancyNode[i], luminanceB_Node, 'value')

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
                        self.sk4RLTransShaderConnection(transpancyNode[i], luminanceM_Node, 'value')

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
                            meshesReserve = self.sk4RLFaceObjReverse(meshes)
                            try:
                                if meshesReserve:
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
                                
            # FBR,SPR Hair隐藏
            if checkInfo[1] in ['FBR','SPR']:
                if refHair:
                    for obj in refHair:
                        mc.editRenderLayerAdjustment(obj + '.v')
                        mc.setAttr((obj + '.v'),l = 0)
                        mc.setAttr((obj + '.v'), 0)

                            
            # 渲染设置
            mc.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'mayaSoftware', type='string')

            # 关闭光线追踪
            mc.editRenderLayerAdjustment('defaultRenderQuality.enableRaytracing')
            mc.setAttr('defaultRenderQuality.enableRaytracing', 0)

            # exr
            self.sk4RLFramebuffer('iff',16)

            mc.editRenderLayerAdjustment('defaultResolution.width')
            mc.setAttr('defaultResolution.width', 1280 )
            mc.editRenderLayerAdjustment('defaultResolution.height')
            mc.setAttr('defaultResolution.height', 720)

            print (u'===============!!!Done 【%s】!!!===============' % (u'%s_%s层' % (layerType.split('_')[0],layerType.split('_')[1])))
            print '\n'
        else:
            print (u'===============!!!Error 【%s】 无物体!!!===============' % (u'%s_%s层' % (layerType.split('_')[0],layerType.split('_')[1])))
            print '\n'

    # 删除SET reference
    def sk4RLayerSetReferenceDel(self):
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
    def sk4RLayerExrWriteMode(self):
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
    def sk4RLayerZdepthDistanceConfigUI(self):
        if mc.window('Zdepth_Distance_UI', q=True, exists=True):
            mc.deleteUI('Zdepth_Distance_UI')
        mc.window('Zdepth_Distance_UI', t=(unicode('Zdepth_Distance_UI', 'utf8')), wh=[320, 90], mb=True)

        # 主界面
        mc.columnLayout()

        # 分解创建
        mc.frameLayout(label=u'Zdepth_Distance', borderStyle='etchedOut', width=320)

        mc.rowLayout()
        mc.intFieldGrp('Zdepth_Distance_Value', l=u'距离设置: ', value1=1500)
        mc.setParent("..")

        mc.setParent("..")

        mc.rowLayout()
        mc.button(label=u'[变更设置]', width=320, c='sk_renderLayer_SK4.sk_renderLayer_SK4().sk4RLayerZdepthDistanceConfig()')
        mc.setParent("..")

        mc.showWindow()

    # Zdepth distance Config
    def sk4RLayerZdepthDistanceConfig(self):
        value = mc.intFieldGrp('Zdepth_Distance_Value', value=1, q=1)[0]
        samplerInfoNodes = mc.ls(type='samplerInfo')
        if samplerInfoNodes:
            for node in samplerInfoNodes:
                if mc.objExists(node + '.FarClipCalimero'):
                    mc.setAttr((node + '.FarClipCalimero'), value)

    # 排除obj函数
    def sk4RLObjInOutConfig(self,checkObjs,inObjs,outObjs):
        result = []
        if not checkObjs:
            return result
        for checkObj in checkObjs:
            if checkObj in inObjs and checkObj not in outObjs:
                result.append(checkObj)
        return result
    
    # 大组下灯光
    def sk4RLGrpLights(self,rootGrp):
        if not mc.ls(rootGrp):
            print u'===本文件没有灯光组：[%s]==='%(rootGrp)
            mc.error(u'===本文件没有灯光组：[%s]==='%(rootGrp))
        lights = mc.listRelatives(rootGrp,ad = 1 , type = 'light',f = 1)
        if not lights:
            return []
        lightGrps = mc.listRelatives(lights , ap = 1 ,type = 'transform',f= 1)
        if not lightGrps:
            return []
        return lightGrps

    # skydome config
    def sk4RLSkydomeMoodConfig(self):
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
    def sk4RLShaderAdd(self, mesh , addSG ):
        # 获取mesh连接的SG属性
        checkMesh = mesh
        if '.f[' in checkMesh:
            checkMesh = checkMesh.split('.f[')[0]
        checkMesh = mc.ls(mesh , l = 1)[0]
        allInfos = mc.listConnections(checkMesh,d = 1 , type = 'shadingEngine',plugs = 1 , connections = 1)
        if allInfos:
            needInfo = []
            for i in range(len(allInfos)/2):
                if '.memberWireframeColor' in allInfos[2*i + 1]:
                    needInfo.append([allInfos[2*i + 1],allInfos[2*i]])
                else:
                    needInfo.append([allInfos[2*i],allInfos[2*i + 1]])
            # 断开
            for info in needInfo:
                mc.editRenderLayerAdjustment(info[0])
                mc.editRenderLayerAdjustment(info[1])
                mc.disconnectAttr( info[0] , info[1] )
        # 赋予材质
        mc.sets(mesh,e = 1 , forceElement = addSG)
        
        
    # software Do Smooth
    def sk4RLSwDoSmooth(self):
        from idmt.maya.commonCore.core_mayaCommon import sk_smoothSet
        #import  sk_smoothSet
        reload(sk_smoothSet)
        # smooth 1    polySmoothFace
        objs = sk_smoothSet.sk_smoothSet().smoothSetGetObjects(1)
        print '---'
        print u'[Sms1]:%s'%(str(len(objs)))
        for i in range(len(objs)):
            obj = objs[i]
            if (i%1000 == 0):
                print i
            if not mc.getAttr(obj+'.v'):
                continue
            if 'deformers|' in mc.ls(obj,l=1)[0].lower() or 'rig|' in mc.ls(obj,l=1)[0].lower():
                continue
            shape = mc.listRelatives(obj,s=1,type = 'mesh')
            if not shape:
                continue
            # 物体
            mc.select(obj)
            try:
                polyNode = mc.polySmooth(obj,  mth=0, dv=1, bnr=1, c=1, kb=0, ksb=1, khe=0, kt=1, kmb=1, suv=1, peh=0, sl=1, dpe=1, ps=0.1, ro=1, ch=1)
            except:
                print u'===有物体无法smooth==='
                print obj
                mc.error(u'===有物体无法smooth===')  
            mc.rename(polyNode[0],('foodSMS_' + polyNode[0]))
            # 草莓酱
            newObjs = mc.ls((obj.split('|')[-1] + 'Base*'),type = 'transform',l=1)
            if not newObjs:
                continue
            for newObj in newObjs:
                mc.select(newObj)
                polyNewNode = mc.polySmooth(newObj,  mth=0, dv=1, bnr=1, c=1, kb=0, ksb=1, khe=0, kt=1, kmb=1, suv=1, peh=0, sl=1, dpe=1, ps=0.1, ro=1, ch=1)
                mc.rename(polyNewNode[0],('foodSMS_' + polyNewNode[0]))
        # smooth 2    polySmoothFace
        objs = sk_smoothSet.sk_smoothSet().smoothSetGetObjects(2)
        print '---'
        print u'[Sms2]:%s'%(str(len(objs))) 
        for i in range(len(objs)):
            obj = objs[i]
            if (i%1000 == 0):
                print i
            if not mc.getAttr(obj+'.v'):
                continue
            if 'deformers|' in mc.ls(obj,l=1)[0].lower() or 'rig|' in mc.ls(obj,l=1)[0].lower():
                continue
            shape = mc.listRelatives(obj,s=1,type = 'mesh')
            if not shape:
                continue
            mc.select(obj)
            try:
                polyNode = mc.polySmooth(obj,  mth=0, dv=2, bnr=1, c=1, kb=0, ksb=1, khe=0, kt=1, kmb=1, suv=1, peh=0, sl=1, dpe=1, ps=0.1, ro=1, ch=1)
            except:
                print u'===有物体无法smooth==='
                print obj
                mc.error(u'===有物体无法smooth===')  

            
            mc.rename(polyNode[0],('foodSMS_' + polyNode[0]))
            # 草莓酱
            newObjs = mc.ls((obj.split('|')[-1] + 'Base*'),type = 'transform',l=1)
            if not newObjs:
                continue
            for newObj in newObjs:
                mc.select(newObj)
                polyNewNode = mc.polySmooth(newObj,  mth=0, dv=2, bnr=1, c=1, kb=0, ksb=1, khe=0, kt=1, kmb=1, suv=1, peh=0, sl=1, dpe=1, ps=0.1, ro=1, ch=1)
                mc.rename(polyNewNode[0],('foodSMS_' + polyNewNode[0]))
        mc.select(cl = 1)
                            
    # 根据选面物体信息获取物体剩余面信息
    # 处理maya bug
    def sk4RLFaceObjReverse( self, checkMeshes):
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

    # SG节点处理
    def sk4RLSGNodeCleanConfig(self, sgNode):
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




    def sk4FBRCreate(self):
        print (u'===============!!!Start 【%s】!!!===============ALL_FBR' )
        print 'Working...'
        
        self.closeHairSysterm()
                
        layerType='ALL_FBR'
        checkInfo = layerType.split('_')

        # 物体信息
        objs = self.sk4RLObjectsTList()
        refCHR = objs[0]
        refPRP = objs[1]
        refSET = objs[2]
        refSKY = objs[3]
        refGroud = objs[4]
        refHair = objs[5]
        
        layerName = ''
        layerObjs = []
        RObjs = []
        GObjs = []
        BObjs = []
        MObjs = []

        # 读取RGB
        RGBInfos = []
        RGBKey = ''
        if checkInfo[1] == 'FBR':
            RGBKey = 'FullBody'
        if checkInfo[1] == 'SPR':
            RGBKey = 'ShortParts'
        from idmt.maya.commonCore.core_renderLayer import sk_renderLayerCore
        reload(sk_renderLayerCore)
        RGBInfos = sk_renderLayerCore.sk_renderLayerCore().ydRLayerRGBObjectsConfig(RGBKey,1,1)

        #if checkInfo[1] == 'FBR':
        #    print '---'
        #    print RGBInfos
        # 处理RGB
        if RGBInfos[0]:
            for id in range(len(RGBInfos[0])):
                if RGBInfos[0][id][0] == 1:
                    RObjs = RObjs + RGBInfos[1][id]
                if RGBInfos[0][id][1] == 1:
                    GObjs = GObjs + RGBInfos[1][id]
                if RGBInfos[0][id][2] == 1:
                    BObjs = BObjs + RGBInfos[1][id]
                if RGBInfos[0][id][0] == RGBInfos[0][id][1] == RGBInfos[0][id][2] == 0:
                    MObjs = MObjs + RGBInfos[1][id]
            layerObjs = refCHR + refPRP
        else:
            layerObjs = []

        layerName = checkInfo[0] + '_' + checkInfo[-1]
        
        mel.eval('source "Z:/Resource/Support/Maya/projects/Strawberry4/DeleteMetals.mel";HbDeleteMaterials();')
        
        if (layerObjs):
           
            # 创建RenderLayer
            if mc.ls(layerName):
                mc.delete(layerName)

            mc.createRenderLayer(layerObjs, name=layerName, noRecurse=1, makeCurrent=1)

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
            from idmt.maya.commonCore.core_mayaCommon import sk_pyCommon
            reload(sk_pyCommon)

            # layerObjs 类型必然是transform
            for obj in layerObjs:
                if mc.nodeType(obj) == 'mesh':
                       mesh = mc.ls(obj,l = 1)[0]
                else:
                    mesh = mc.listRelatives(obj,s = 1 ,ni  = 1, type = 'mesh',f=1)
                    if not mesh:
                        continue
                    mesh = mesh[0]
                shaderSG = MatteSG
                try:
                    mc.sets(mesh,e = 1 , forceElement = shaderSG)
                except:
                    print u'===有物体无法赋予材质==='
                    print mesh
                    mc.error(u'===有物体无法赋予材质===')            


            if RObjs:
                RGBMeshes = []
                for obj in RObjs:
                    if mc.nodeType(obj) == 'mesh':
                       mesh = mc.ls(obj,l = 1)[0]
                    else:
                        mesh = mc.listRelatives(obj,s = 1 ,ni  = 1, type = 'mesh',f=1)
                        if not mesh:
                            continue
                        mesh = mesh[0]
                    RGBMeshes.append(obj)                                                
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

            
            if BObjs:
                RGBMeshes = []
                for obj in BObjs:
                    if mc.nodeType(obj) == 'mesh':
                       mesh = mc.ls(obj,l = 1)[0]
                    else:
                        mesh = mc.listRelatives(obj,s = 1 ,ni  = 1, type = 'mesh',f=1)
                        if not mesh:
                            continue
                        mesh = mesh[0]
                    RGBMeshes.append(obj)                                                
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

            if GObjs:
                RGBMeshes = []
                for obj in GObjs:
                    if mc.nodeType(obj) == 'mesh':
                       mesh = mc.ls(obj,l = 1)[0]
                    else:
                        mesh = mc.listRelatives(obj,s = 1 ,ni  = 1, type = 'mesh',f=1)
                        if not mesh:
                            continue
                        mesh = mesh[0]
                    RGBMeshes.append(obj)                                                
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
            if MObjs:
                RGBMeshes = []
                for obj in MObjs:
                    if mc.nodeType(obj) == 'mesh':
                       mesh = mc.ls(obj,l = 1)[0]
                    else:
                        mesh = mc.listRelatives(obj,s = 1 ,ni  = 1, type = 'mesh',f=1)
                        if not mesh:
                            continue
                        mesh = mesh[0]
                    RGBMeshes.append(obj)                                                
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


            # FBR,SPR Hair隐藏
            if checkInfo[1] in ['FBR','SPR']:
                if refHair:
                    for obj in refHair:
                        mc.editRenderLayerAdjustment(obj + '.v')
                        mc.setAttr((obj + '.v'),l = 0)
                        mc.setAttr((obj + '.v'), 0)

                            
            # 渲染设置
            mc.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'mayaSoftware', type='string')

            # 关闭光线追踪
            mc.editRenderLayerAdjustment('defaultRenderQuality.enableRaytracing')
            mc.setAttr('defaultRenderQuality.enableRaytracing', 0)

            # exr
            self.sk4RLFramebuffer('iff',16)

            mc.editRenderLayerAdjustment('defaultResolution.width')
            mc.setAttr('defaultResolution.width', 1280 )
            mc.editRenderLayerAdjustment('defaultResolution.height')
            mc.setAttr('defaultResolution.height', 720)

            print (u'===============!!!Done 【%s】!!!===============ALL_FBR')
            print '\n'
        else:
            print (u'===============!!!Error 【%s】 无物体!!!===============ALL_FBR' )
            print '\n'


    def sk4SBRCreate(self):
        print (u'===============!!!Start 【%s】!!!===============ALL_BSR' )
        print 'Working...'
        
        self.closeHairSysterm()        
        
        layerType='ALL_BSR'
        checkInfo = layerType.split('_')

        # 物体信息
        objs = self.sk4RLObjectsTList()
        refCHR = objs[0]
        refPRP = objs[1]
        refSET = objs[2]
        refSKY = objs[3]
        refGroud = objs[4]
        refHair = objs[5]
        
        layerName = ''
        layerObjs = []
        RObjs = []
        GObjs = []
        BObjs = []
        MObjs = []

        if checkInfo[1] == 'BSR':
            RObjs = refCHR
            GObjs = refPRP
            BObjs = refSET
            MObjs = []
            layerObjs = refCHR + refPRP + refSET

            layerName = checkInfo[0] + '_' + checkInfo[-1]     
            mel.eval('source "Z:/Resource/Support/Maya/projects/Strawberry4/DeleteMetals.mel";HbDeleteMaterials();')
        
        if (layerObjs):
           
            # 创建RenderLayer
            if mc.ls(layerName):
                mc.delete(layerName)

            mc.createRenderLayer(layerObjs, name=layerName, noRecurse=1, makeCurrent=1)

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
            from idmt.maya.commonCore.core_mayaCommon import sk_pyCommon
            reload(sk_pyCommon)

            # layerObjs 类型必然是transform
            '''
            for obj in layerObjs:
                if mc.nodeType(obj) == 'mesh':
                       mesh = mc.ls(obj,l = 1)[0]
                else:
                    mesh = mc.listRelatives(obj,s = 1 ,ni  = 1, type = 'mesh',f=1)
                    if not mesh:
                        continue
                    mesh = mesh[0]
                shaderSG = MatteSG
                try:
                    mc.sets(mesh,e = 1 , forceElement = shaderSG)
                except:
                    print u'===有物体无法赋予材质==='
                    print mesh
                    mc.error(u'===有物体无法赋予材质===')  
            '''          

            if RObjs:
                RGBMeshes = []
                for obj in RObjs:
                    if mc.nodeType(obj) == 'mesh':
                       mesh = mc.ls(obj,l = 1)[0]
                    else:
                        mesh = mc.listRelatives(obj,s = 1 ,ni  = 1, type = 'mesh',f=1)
                        if not mesh:
                            continue
                        mesh = mesh[0]
                    RGBMeshes.append(obj)                                                
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

            
            if BObjs:
                RGBMeshes = []
                for obj in BObjs:
                    if mc.nodeType(obj) == 'mesh':
                       mesh = mc.ls(obj,l = 1)[0]
                    else:
                        mesh = mc.listRelatives(obj,s = 1 ,ni  = 1, type = 'mesh',f=1)
                        if not mesh:
                            continue
                        mesh = mesh[0]
                    RGBMeshes.append(obj)                                                
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

            if GObjs:
                RGBMeshes = []
                for obj in GObjs:
                    if mc.nodeType(obj) == 'mesh':
                       mesh = mc.ls(obj,l = 1)[0]
                    else:
                        mesh = mc.listRelatives(obj,s = 1 ,ni  = 1, type = 'mesh',f=1)
                        if not mesh:
                            continue
                        mesh = mesh[0]
                    RGBMeshes.append(obj)                                                
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
            if MObjs:
                RGBMeshes = []
                for obj in MObjs:
                    if mc.nodeType(obj) == 'mesh':
                       mesh = mc.ls(obj,l = 1)[0]
                    else:
                        mesh = mc.listRelatives(obj,s = 1 ,ni  = 1, type = 'mesh',f=1)
                        if not mesh:
                            continue
                        mesh = mesh[0]
                    RGBMeshes.append(obj)                                                
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


            # FBR,SPR Hair隐藏
            if checkInfo[1] in ['FBR','SPR']:
                if refHair:
                    for obj in refHair:
                        mc.editRenderLayerAdjustment(obj + '.v')
                        mc.setAttr((obj + '.v'),l = 0)
                        mc.setAttr((obj + '.v'), 0)

                            
            # 渲染设置
            mc.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'mayaSoftware', type='string')

            # 关闭光线追踪
            mc.editRenderLayerAdjustment('defaultRenderQuality.enableRaytracing')
            mc.setAttr('defaultRenderQuality.enableRaytracing', 0)

            # exr
            self.sk4RLFramebuffer('iff',16)

            mc.editRenderLayerAdjustment('defaultResolution.width')
            mc.setAttr('defaultResolution.width', 1280 )
            mc.editRenderLayerAdjustment('defaultResolution.height')
            mc.setAttr('defaultResolution.height', 720)

            print (u'===============!!!Done 【%s】!!!===============ALL_BSR')
            print '\n'
        else:
            print (u'===============!!!Error 【%s】 无物体!!!===============ALL_BSR' )
            print '\n'


    def closeHairSysterm(self):
        HairSysterm=mc.ls(type='hairSystem')
        if HairSysterm:
            for shape in HairSysterm:
                mc.delete(shape)


    #------------------------------------------------------------#
    def shotSetExportAnim(self):
        from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
        reload(sk_infoConfig)
        shotLoaclPath = sk_infoConfig.sk_infoConfig().checkShotDataInfoPath(server =0,infoMode = 6)
        shotSetAnimFile = shotLoaclPath + 'shotSetAnim.sla'
        ctrlShapes = mc.listRelatives('SET_GRP',ad = 1, type = 'nurbsCurve',f=1)
        ctrlGrps = []
        if ctrlShapes:
            ctrlGrps = mc.listRelatives(ctrlShapes,p=1,f=1,type = 'transform')
        startFrame = mc.playbackOptions(min=1,q=1)
        endFrame = mc.playbackOptions(max=1,q=1)
        from idmt.maya.commonCore.core_finalLayout import sk_animCurveCore
        reload(sk_animCurveCore)
        sk_animCurveCore.sk_animCurveCore().checkAnimCurveInfoExport( ctrlGrps, serverFile = 0, infoFile='anim' , targetPath = shotSetAnimFile , shotType = 3,frameRange = [startFrame,endFrame])