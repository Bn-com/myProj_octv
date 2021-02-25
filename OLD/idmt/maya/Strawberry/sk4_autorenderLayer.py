# -*- coding: utf-8 -*-

'''
Created on 2014-10-8

@author: liangyu
'''
import maya.cmds as mc
import maya.mel as mel
import idmt.pipeline.db

from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
reload(sk_infoConfig)

class sk4_autorenderLayer(object):
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

 

        # Step 2：  [MentalRay][HAIR]
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
 
       # Step 3：  [SoftWare][BG]
        # 清理渲染层
        if shaderForece:
            mc.file(baseFileName,open = 1 , f = 1)
        else:
            sk_sceneTools.sk_sceneTools().checkCleanRenderLayers()
            self.sk4RLSYSShaderClean()
            
        #清理文件
        mel.eval('source "Z:/Resource/Support/Maya/projects/Strawberry4/DeleteMetals.mel";HbDeleteMaterials();')
        
        # Shadow
        self.sk4RLSHDCreate('CHR' , shaderForece = shaderForece)
        # Zdepth
        self.sk4RLZDEPTHCreate('BG' , shaderForece = shaderForece)

        mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')
        # Unrender MasterLayer
        mc.setAttr("defaultRenderLayer.renderable", 0)
        # common Setting
        self.sk4RLCommonConfig()
        # save
        self.sk4RLSave('SWZS',2) 
                    
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

        #清理文件
        mel.eval('source "Z:/Resource/Support/Maya/projects/Strawberry4/DeleteMetals.mel";HbDeleteMaterials();')
        
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
        # 打开文件
            
        mc.file(baseFileName,open = 1 , f = 1)
       
        # 清理掉所有灯光
        lights = mc.ls(type = 'light')
        if lights:
            mc.delete(lights)
 
        #清理材质
        mel.eval('source "Z:/Resource/Support/Maya/projects/Strawberry4/DeleteMetals.mel";HbDeleteMaterials();')
               
        # RGB
        self.sk4FBRCreate()
        # FBR
        self.sk4SBRCreate()
        
        mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')
        # Unrender MasterLayer
        mc.setAttr("defaultRenderLayer.renderable", 0)
        
        # common Setting
        self.sk4RLCommonConfig()
        
        # 清理无用材质球
        '''
        if shaderForece:
            print u'\n'
            print u'======清理无用材质球Starting======'
            print u'---working---'
            mel.eval('MLdeleteUnused')
            print u'======清理无用材质球Done!!!======'
            print u'\n'
        '''    
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
        
        mc.setAttr('defaultResolution.width', 1280)
        mc.setAttr('defaultResolution.height', 720)
        
        fileName = fileName + fileType
        print u'-------'
        print fileName
        mc.file(rename=fileName)
        mc.file(save=1,type = 'mayaBinary',f = 1)
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
       

             

            # 渲染设置
            mc.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')

            # 开启光线追踪
            mc.editRenderLayerAdjustment('miDefaultOptions.rayTracing')
            mc.setAttr('miDefaultOptions.rayTracing', 1)


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

        if rlObjs:
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
            self.sk4RLSwDoSmooth()
                
            # 经典连材质模式
            if not SGOType:
                # layerObjs 类型必然是transform
                for obj in rlObjs:
                    # 属于matter
                    if obj in MaskObjs:
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
            print u'头发系统已关闭' 
        else:
            print u'没有头发系统'       