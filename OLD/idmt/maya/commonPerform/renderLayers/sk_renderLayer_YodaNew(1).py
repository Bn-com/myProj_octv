# -*- coding: utf-8 -*-

'''
Created on 2013-6-18

@author: shenkang

amend:hanhong
'''
import maya.cmds as mc
import maya.mel as mel
import idmt.pipeline.db

from idmt.maya.commonCore.core_finalLayout import sk_cacheFinalLayout
reload(sk_cacheFinalLayout)

from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
reload(sk_infoConfig)

from idmt.maya.py_common import nj_doMotionVector
reload(nj_doMotionVector)

from idmt.maya.commonPerform.renderLayers import sk_renderLayer_Yo
reload(sk_renderLayer_Yo)

class sk_renderLayer_YodaNew(object):
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
    def ydRLAutoCreateNew(self,createMode = 0 ,refClean = 1 , RGB = 0 , RGBCreatType = 0 , shaderForece = 0,exr=1):
        print('=================================================================')
        print('====================!!!Start AutoRenderLayer!!!====================')
    
        # Back To MasterLayer
        mc.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
        # clean renderlayer
        from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools
        reload(sk_sceneTools)
        from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
        reload(sk_referenceConfig)
#        if refClean == 1:
            # 处理非参考的namespace
#            sk_sceneTools.sk_sceneTools().sk_sceneNoRefNamespaceClean()
        # clean unknown nodes
        sk_sceneTools.sk_sceneTools().checkDonotNodeCleanBase(0)
        #清理渲染层
        sk_sceneTools.sk_sceneTools().checkCleanRenderLayers()    
        # 强制启动IK解算
        mc.ikSystem(e = 1,sol = 1)
        print('\n')
        print(u'=========================IK解算器强制更新========================')
        print('\n')
        #预处理，约束清理
        
        sk_cacheFinalLayout.sk_cacheFinalLayout().sk_checkBakeConstraints()
        print(u'========================【约束】【烘焙】【成功】========================')            
        # Step Base:[导出]
        # 导出
        #角色文件
        print('\n')
        print(u'========================导出清理开始========================')
        print(u'===如果本阶段失败，请打开文件手动清理')
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()   
        pathLocal = sk_infoConfig.sk_infoConfig().checkRenderLayerLocalPath(3)
        mc.sysFile((pathLocal+'render'), makeDir=True)        
        baseFileName = pathLocal +'render/'+ shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2] + '_' + shotInfo[3] + '_Base' + '.mb'
        baseFileName = baseFileName
    
        baseGrps = mc.ls(assemblies=True)
        mc.select(baseGrps)
        mrNodes = mc.ls(type='mentalrayGlobals')+ mc.ls(type='mentalrayItemsList') +mc.ls(type='mentalrayOptions')
        if mrNodes:
            mc.select(mrNodes,add = 1)
#    #修改日期2014/11/5 （韩虹）
        #mc.file(baseFileName,options='v=0',f=1,type='mayaBinary',preserveReferences=1,es=1)    
        mc.file(baseFileName,f = 1,es = 1,pr = 1,type = 'mayaBinary')
#        mc.file(rename=baseFileName)
#        mc.file(save=1,type = 'mayaBinary',f = 1)
        print(u'---50%')
        # 重打开
        #mc.file(f=1, new=1)
        #mc.file(rename = baseFileName)
        ##mc.file(baseFileName,open = 1 , f = 1)
        #mc.file( baseFileName , i = 1 , mergeNamespacesOnClash = 0 , pr = 1)
        mc.file(baseFileName,options='v=0',type='mayaBinary',f=1,o=1)        
        print(u'---100%')
        print(u'========================导出清理成功========================')
        print(u'===下面开始正式分层')
        print('\n')
        
    
        # common Setting
        sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLCommonConfig()
        
        # mr Setting
        sk_renderLayer_Yo.sk_renderLayer_Yo().mentalRayProductionLevel()
        
        # 格式
        sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLFramebuffer('iff',3,0)
    
        # 断开连接,在master层处理,避免分层时处理崩溃
        objsNeedHide = sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLGBowObjs() 
        objsNeedHide = sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLFaceObjs() + objsNeedHide        
        if objsNeedHide:
            for obj in objsNeedHide:
                mc.lockNode((obj + '.v'), l = 0)
                sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLDeleteConnection((obj + '.v'))
    
        #备份
        mc.file(rename= baseFileName)
        mc.file(s = 1 , f = 1)
    
        idPass = ['BSR','FBR','SPR']
    
        # Step Base:参考import
        #sk_referenceConfig.sk_referenceConfig().checkRefAllImport()
        # Back To MasterLayer
        #print('=====================================hello======================================')
        mc.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
        # 输出透明信息
        sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLTransparencyObjsOld(0,1)
        #print('=====================================hdone======================================')
    
        # Step 0：输出信息
        if createMode == 0:
            sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLObjectsTList(2,1,'mesh')
            sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLObjectsTList(2,1,'light')
        # step 01:导出文件
        if exr==1:
            baseRGBName = pathLocal +'render/'+ shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2] + '_' + shotInfo[3] + '_BaseRgb' + '.mb'
            baseRGBName = baseRGBName
            keyInfos = ['CHRF','CHRM','CHRB','PRPF','PRPM','PRPB','SETF','SETM','SETB','SPCF','SPCM','SPCB','SPCMSKF','SPCMSKM','SPCMSKB','HILL','CLOUD','SKY']
            for key in keyInfos:
                self.ydfileExr(key,selectObjType=0,infotype='AO')
            mel.eval("source \"//file-cluster/GDC/Resource/Support/Maya/2013/zzjUtilityTools.mel\";lighting_DeleteUnusedNode()")
            print(u'赋予lambet1材质')
            if mc.ls(type='mesh'):
                meshes=mc.ls(type='mesh')
            for mesh in meshes:
                try:
                    mc.select(mesh)
                    mc.sets(mesh,e=1,forceElement='initialShadingGroup')
                except:
                    pass 
            
            mel.eval('source "Z:/Resource/Support/Maya/projects/Strawberry4/DeleteMetals.mel";HbDeleteMaterials();')        
            for key in keyInfos:
                self.ydfileExr(key,selectObjType=0,infotype='RGB')
            mc.select(baseGrps)
            mrNodes = mc.ls(type='mentalrayGlobals')+ mc.ls(type='mentalrayItemsList') +mc.ls(type='mentalrayOptions')
            if mrNodes:
                mc.select(mrNodes,add = 1) 
            mc.file(baseRGBName,options='v=0',f=1,type='mayaBinary',preserveReferences=1,es=1)                                                   
        # Step 1：CHR
        #sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLSave('BASE',3)
        
        keyInfos = ['CHRF','CHRM','CHRB']
    
        for key in keyInfos:
            if exr==1:
                self.ydfileOpen(layerType=key, selectObjType=0,infotype='AO')   
            # 清理渲染层
            sk_sceneTools.sk_sceneTools().checkCleanRenderLayers()
            sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLSYSShaderClean()
            # Color
            sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLCOCreate(key)
                
            if mc.ls(key + '_CO'):
                # smoothSet
                #sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLDoSmooth()
                # Back To MasterLayer
                mc.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
                # Unrender MasterLayer
                mc.setAttr("defaultRenderLayer.renderable", 0)
                # mc.setAttr
                # common Setting
                sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLCommonConfig()

                # mr Setting
                sk_renderLayer_Yo.sk_renderLayer_Yo().mentalRayProductionLevel()
                
                # 格式
                sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLFramebuffer('iff',3,0) 
                #
                mc.setAttr('miDefaultOptions.miRenderUsing', 0)
                mc.setAttr('miDefaultOptions.miRenderUsing', 2)    
                # save
                planeObjs = mc.ls('*:*glasses_*',type = 'transform',l = 1) 
                if planeObjs:
                    mc.setAttr('miDefaultOptions.rayTracing',1)
                    mc.setAttr('miDefaultOptions.maxReflectionRays',4)
                    mc.setAttr('miDefaultOptions.maxRefractionRays',4)
                    mc.setAttr('miDefaultOptions.maxRayDepth',6) 
                sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLSave(key,3,'CO')
#非color层
            if exr==1:
                self.ydfileOpen(layerType=key, selectObjType=0,infotype='RGB')   
            # Ambient Occlusion
            sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLAOCreate(key , shaderForece = shaderForece)
            # Back To MasterLayer
            mc.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
            # Normal
            sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLNMCreate(key , shaderForece = shaderForece)
            # Back To MasterLayer
            mc.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
            # Light
            sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLFNCreate(key , shaderForece = shaderForece)

            if mc.ls(key + '_FN'):
                # smoothSet
                #sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLDoSmooth()
                # Back To MasterLayer
                mc.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
                # Unrender MasterLayer
                mc.setAttr("defaultRenderLayer.renderable", 0)
                # mc.setAttr
                # common Setting
                sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLCommonConfig()
                # mr Setting
                sk_renderLayer_Yo.sk_renderLayer_Yo().mentalRayProductionLevel()
                
                # 格式
                sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLFramebuffer('iff',3,0) 
                # save
                sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLSave(key,3,'NCO')                                
            # IDP创建模式
            if RGB:
                for idp in idPass:
                    if exr==1:
                        self.ydfileOpen(layerType=key, selectObjType=0,infotype='RGB')  
                    # 清理渲染层
                    sk_sceneTools.sk_sceneTools().checkCleanRenderLayers()
                    sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLSYSShaderClean()
                    # 单层 
                    sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLRGBCreate((key + '_' + idp) , shaderForece = shaderForece)
                    # Back To MasterLayer
                    mc.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
                    if RGBCreatType:
                        if mc.ls(key + '_' + idp):
                            # Back To MasterLayer
                            mc.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
                            # Unrender MasterLayer
                            mc.setAttr("defaultRenderLayer.renderable", 0)
                            # common Setting
                            sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLCommonConfig()
                            sk_renderLayer_Yo.sk_renderLayer_Yo().mentalRayProductionLevel()
                            mc.setAttr('miDefaultOptions.miRenderUsing', 0)
                            mc.setAttr('miDefaultOptions.miRenderUsing', 2)  
                            # save
                            sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLSave(key,3,idp)
                if not RGBCreatType:
                    # 多层创建
                    if mc.ls(key + '_BSR'):
                        # Back To MasterLayer
                        mc.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
                        # Unrender MasterLayer
                        mc.setAttr("defaultRenderLayer.renderable", 0)
                        # mc.setAttr
                        # common Setting
                        sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLCommonConfig()
                        # mr Setting
                        sk_renderLayer_Yo.sk_renderLayer_Yo().mentalRayProductionLevel()

                        mc.setAttr('miDefaultOptions.miRenderUsing', 0)
                        mc.setAttr('miDefaultOptions.miRenderUsing', 2)                        
                        # 格式
                        sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLFramebuffer('iff',3,0) 
                        # save
                        sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLSave(key,3,'RGB')
    
        # Step 2：PRP
        keyInfos = ['PRPF','PRPM','PRPB']
        
        for key in keyInfos:
            if exr==1:
                self.ydfileOpen(layerType=key, selectObjType=0,infotype='AO')          
            # 清理渲染层
            sk_sceneTools.sk_sceneTools().checkCleanRenderLayers()
            sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLSYSShaderClean()
            # Color
            sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLCOCreate(key)
            if mc.ls(key + '_CO'):
                # smoothSet
                #sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLDoSmooth()
                # Back To MasterLayer
                mc.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
                # Unrender MasterLayer
                mc.setAttr("defaultRenderLayer.renderable", 0)
                # mc.setAttr
                # common Setting
                sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLCommonConfig()
                # mr Setting
                sk_renderLayer_Yo.sk_renderLayer_Yo().mentalRayProductionLevel()

                mc.setAttr('miDefaultOptions.miRenderUsing', 0)
                mc.setAttr('miDefaultOptions.miRenderUsing', 2)                
                # 格式
                sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLFramebuffer('iff',3,0) 
                # save
                sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLSave(key,3,'CO')
#非color层
            if exr==1:
                self.ydfileOpen(layerType=key, selectObjType=0,infotype='RGB')  
            # Ambient Occlusion
            sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLAOCreate(key , shaderForece = shaderForece)
            # Back To MasterLayer
            mc.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
            # Normal
            sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLNMCreate(key , shaderForece = shaderForece)
            # Back To MasterLayer
            mc.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
            # Light
            sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLFNCreate(key , shaderForece = shaderForece)

            if mc.ls(key + '_FN'):
                # smoothSet
                #sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLDoSmooth()
                # Back To MasterLayer
                mc.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
                # Unrender MasterLayer
                mc.setAttr("defaultRenderLayer.renderable", 0)
                # mc.setAttr
                # common Setting
                sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLCommonConfig()
                # mr Setting
                sk_renderLayer_Yo.sk_renderLayer_Yo().mentalRayProductionLevel()
                
                # 格式
                sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLFramebuffer('iff',3,0) 
                # save
                sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLSave(key,3,'NCO')                 
    
            # IDP创建模式
            if RGB:
                # 道具只要BSR
                for idp in ['BSR']:
                    if exr==1:
                        self.ydfileOpen(layerType=key, selectObjType=0,infotype='RGB')                  
                    # 清理渲染层
                    sk_sceneTools.sk_sceneTools().checkCleanRenderLayers()
                    sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLSYSShaderClean()
                    
                    # 单层 
                    sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLRGBCreate((key + '_' + idp), shaderForece = shaderForece)
                    if RGBCreatType:
                        if mc.ls(key + '_' + idp):
                            # Back To MasterLayer
                            mc.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
                            # Unrender MasterLayer
                            mc.setAttr("defaultRenderLayer.renderable", 0)
                            # common Setting
                            sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLCommonConfig()
                            # mr Setting
                            sk_renderLayer_Yo.sk_renderLayer_Yo().mentalRayProductionLevel()
                            mc.setAttr('miDefaultOptions.miRenderUsing', 0)
                            mc.setAttr('miDefaultOptions.miRenderUsing', 2)                            
                            # 格式
                            sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLFramebuffer('iff',3,0) 
                            # save
                            sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLSave(key,3,idp)
                if not RGBCreatType:
                    # 多层创建
                    if mc.ls(key + '_BSR'):
                        # Back To MasterLayer
                        mc.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
                        # Unrender MasterLayer
                        mc.setAttr("defaultRenderLayer.renderable", 0)
                        # mc.setAttr
                        # common Setting
                        sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLCommonConfig()
                        # mr Setting
                        sk_renderLayer_Yo.sk_renderLayer_Yo().mentalRayProductionLevel()

                        mc.setAttr('miDefaultOptions.miRenderUsing', 0)
                        mc.setAttr('miDefaultOptions.miRenderUsing', 2)                           
                        # 格式
                        sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLFramebuffer('iff',3,0) 
                        # save
                        sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLSave(key,3,'RGB')
    
    
        # Step 3：SET
        keyInfos = ['SETF','SETM','SETB']
 #修改场景分层方案，将color 与非color层分开文件       
        for key in keyInfos:
            if exr==1:
                self.ydfileOpen(layerType=key, selectObjType=0,infotype='AO')          
            # 清理渲染层
            sk_sceneTools.sk_sceneTools().checkCleanRenderLayers()
            sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLSYSShaderClean()
            # Color
            sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLCOCreate(key)

            if mc.ls(key + '_CO'):
                # smoothSet
                #sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLDoSmooth()
                # Back To MasterLayer
                mc.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
                # Unrender MasterLayer
                mc.setAttr("defaultRenderLayer.renderable", 0)
                # mc.setAttr
                # common Setting
                sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLCommonConfig()
                # mr Setting
                sk_renderLayer_Yo.sk_renderLayer_Yo().mentalRayProductionLevel()
                mc.setAttr('miDefaultOptions.miRenderUsing', 0)
                mc.setAttr('miDefaultOptions.miRenderUsing', 2)   
                # 格式
                sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLFramebuffer('iff',3,0) 
                # save
                sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLSave(key,3,'CO')

            if exr==1:
                self.ydfileOpen(layerType=key, selectObjType=0,infotype='RGB') 
            # ZDepth
            sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLZDEPTHCreate(key, shaderForece = shaderForece)
            # Back To MasterLayer
            mc.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
            # Normal
            sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLNMCreate(key, shaderForece = shaderForece)
            # Back To MasterLayer
            mc.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
            # Light
            sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLFNCreate(key, shaderForece = shaderForece)

            if mc.ls(key + '_FN'):
                # smoothSet
                #sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLDoSmooth()
                # Back To MasterLayer
                mc.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
                # Unrender MasterLayer
                mc.setAttr("defaultRenderLayer.renderable", 0)
                # mc.setAttr
                # common Setting
                sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLCommonConfig()
                # mr Setting
                sk_renderLayer_Yo.sk_renderLayer_Yo().mentalRayProductionLevel()
                mc.setAttr('miDefaultOptions.miRenderUsing', 0)
                mc.setAttr('miDefaultOptions.miRenderUsing', 2)                   
                # 格式
                sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLFramebuffer('iff',3,0) 
                # save
                sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLSave(key,3,'NCO')
                         
            if RGB:
                # 场景不要BSR
                for idp in ['FBR','SPR']:
                    if exr==1:
                        self.ydfileOpen(layerType=key, selectObjType=0,infotype='RGB')                                
                    # 清理渲染层
                    sk_sceneTools.sk_sceneTools().checkCleanRenderLayers()
                    sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLSYSShaderClean()
                    # 单层 
                    sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLRGBCreate((key + '_' + idp), shaderForece = shaderForece)
                    if RGBCreatType:
                        if mc.ls(key + '_' + idp):
                            # Back To MasterLayer
                            mc.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
                            # Unrender MasterLayer
                            mc.setAttr("defaultRenderLayer.renderable", 0)
                            # common Setting
                            sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLCommonConfig()
                            # mr Setting
                            sk_renderLayer_Yo.sk_renderLayer_Yo().mentalRayProductionLevel()
                            mc.setAttr('miDefaultOptions.miRenderUsing', 0)
                            mc.setAttr('miDefaultOptions.miRenderUsing', 2)   
                            
                            # 格式
                            sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLFramebuffer('iff',3,0) 
                            # save
                            sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLSave(key,3,idp)
    
        # Step 4：SPC
        keyInfos = ['SPCF','SPCM','SPCB']
        
        for key in keyInfos:
            if exr==1:
                self.ydfileOpen(layerType=key, selectObjType=0,infotype='AO')          
            # 清理渲染层
            sk_sceneTools.sk_sceneTools().checkCleanRenderLayers()
            sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLSYSShaderClean()
            # Color
            sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLCOCreate(key)
            if mc.ls(key + '_CO'):
                # smoothSet
                #sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLDoSmooth()
                # Back To MasterLayer
                mc.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
                # Unrender MasterLayer
                mc.setAttr("defaultRenderLayer.renderable", 0)
                # mc.setAttr
                # common Setting
                sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLCommonConfig()
                # mr Setting
                sk_renderLayer_Yo.sk_renderLayer_Yo().mentalRayProductionLevel()
            
                mc.setAttr('miDefaultOptions.miRenderUsing', 0)
                mc.setAttr('miDefaultOptions.miRenderUsing', 2)                
                # 格式
                sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLFramebuffer('iff',3,0) 
                # save
                sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLSave(key,3,'CO')
#非color层
            if exr==1:
                self.ydfileOpen(layerType=key, selectObjType=0,infotype='RGB') 
                
            # Ambient Occlusion
            sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLAOCreate(key , shaderForece = shaderForece)
            # Back To MasterLayer
            mc.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
            # Normal
            sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLNMCreate(key , shaderForece = shaderForece)
            # Back To MasterLayer
            mc.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
            # Light
            sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLFNCreate(key , shaderForece = shaderForece)
            
            if mc.ls(key + '_FN'):
                # smoothSet
                #sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLDoSmooth()
                # Back To MasterLayer
                mc.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
                # Unrender MasterLayer
                mc.setAttr("defaultRenderLayer.renderable", 0)
                # mc.setAttr
                # common Setting
                sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLCommonConfig()
                # mr Setting
                sk_renderLayer_Yo.sk_renderLayer_Yo().mentalRayProductionLevel()
                
                # 格式
                sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLFramebuffer('iff',3,0) 
                # save
                sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLSave(key,3,'NCO')            
    
            # IDP创建模式
            if RGB:
                for idp in idPass:
                    if exr==1:
                        self.ydfileOpen(layerType=key, selectObjType=0,infotype='RGB')                    
                    # 清理渲染层
                    sk_sceneTools.sk_sceneTools().checkCleanRenderLayers()
                    sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLSYSShaderClean()
                    # 单层 
                    sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLRGBCreate((key + '_' + idp), shaderForece = shaderForece)
                    # Back To MasterLayer
                    mc.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
                    if RGBCreatType:
                        if mc.ls(key + '_' + idp):
                            # Back To MasterLayer
                            mc.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
                            # Unrender MasterLayer
                            mc.setAttr("defaultRenderLayer.renderable", 0)
                            # common Setting
                            sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLCommonConfig()
                            # mr Setting
                            sk_renderLayer_Yo.sk_renderLayer_Yo().mentalRayProductionLevel()
                            
                            # 格式
                            sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLFramebuffer('iff',3,0) 
                            # save
                            mc.setAttr('miDefaultOptions.miRenderUsing', 0)
                            mc.setAttr('miDefaultOptions.miRenderUsing', 2)   
                            sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLSave(key,3,idp)
                if not RGBCreatType:
                    # 多层创建
                    if mc.ls(key + '_BSR'):
                        # Back To MasterLayer
                        mc.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
                        # Unrender MasterLayer
                        mc.setAttr("defaultRenderLayer.renderable", 0)
                        # mc.setAttr
                        # common Setting
                        sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLCommonConfig()
                        # mr Setting
                        sk_renderLayer_Yo.sk_renderLayer_Yo().mentalRayProductionLevel()
                        
                        # 格式
                        sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLFramebuffer('iff',3,0) 
                        # save
                        mc.setAttr('miDefaultOptions.miRenderUsing', 0)
                        mc.setAttr('miDefaultOptions.miRenderUsing', 2)   
                        sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLSave(key,3,'RGB')
        
        # Setp 5:SET_AO
        sk_sceneTools.sk_sceneTools().checkCleanRenderLayers()
        sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLSYSShaderClean()
        
        keyInfos = ['SETF','SETM','SETB']
        if exr==1:
            mc.file(baseRGBName,options='v=0',type='mayaBinary',f=1,o=1)        
        for key in keyInfos:           
            # Ambient Occlusion
            sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLAOCreate(key, shaderForece = shaderForece)
            # Back To MasterLayer
            mc.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
            
        if (mc.ls('SETF_AO') + mc.ls('SETM_AO') + mc.ls('SETB_AO')):
            # smoothSet
            #sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLDoSmooth()
            # Back To MasterLayer
            mc.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
            # Unrender MasterLayer
            mc.setAttr("defaultRenderLayer.renderable", 0)
            # mc.setAttr
            # common Setting
            sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLCommonConfig()
            # mr Setting
            sk_renderLayer_Yo.sk_renderLayer_Yo().mentalRayProductionLevel()
            
            # 格式
            sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLFramebuffer('iff',3,0) 
            # save
            mc.setAttr('miDefaultOptions.miRenderUsing', 0)
            mc.setAttr('miDefaultOptions.miRenderUsing', 2)   
            sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLSave('SETAO',3,'')
            
        # Setp 5+:MotionVector
        sk_sceneTools.sk_sceneTools().checkCleanRenderLayers()
        sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLSYSShaderClean()
        
        
        if exr==1:
            mc.file(baseRGBName,options='v=0',type='mayaBinary',f=1,o=1)  
        meshs=mc.ls(type='mesh',l=1)
        env=mc.ls('HILL_CO') + mc.ls('CLOUD_CO') + mc.ls('SKY_CO')
        objs=[]
        objF=[]
        if meshs:
            for mesh in meshs:
                obj=mc.listRelatives(mesh,p=1,f=1)                    
                if obj:
                    objs.append(obj[0])
        if objs:
            for obj in objs:
                if obj not in env:
                    objF.append(obj)
        if objF:
            # Unrender MasterLayer
            mc.setAttr("defaultRenderLayer.renderable", 0)            

            # mr Setting
            sk_renderLayer_Yo.sk_renderLayer_Yo().mentalRayProductionLevel()
            
            # 格式
            sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLFramebuffer('iff',3,0) 
            # save
            mc.setAttr('miDefaultOptions.miRenderUsing', 0)
            mc.setAttr('miDefaultOptions.miRenderUsing', 2)             
            mc.select(objF)  
            nj_doMotionVector.nj_doMotionVector().nj_doMotionVectorPassProc()
            mc.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')  
            sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLSave('MV',3,'')
            
        # Step 6：ENV
        # 清理渲染层
        sk_sceneTools.sk_sceneTools().checkCleanRenderLayers()
        sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLSYSShaderClean()
        
        keyInfos = ['HILL','CLOUD','SKY']
        if exr==1:
            mc.file(baseFileName,options='v=0',type='mayaBinary',f=1,o=1)         
        for key in keyInfos:           
            # Color
            sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLCOCreate(key)
            
        if (mc.ls('HILL_CO') + mc.ls('CLOUD_CO') + mc.ls('SKY_CO')):
            # smoothSet
            #sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLDoSmooth()
            # Back To MasterLayer
            mc.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
            # Unrender MasterLayer
            mc.setAttr("defaultRenderLayer.renderable", 0)
            # mc.setAttr
            # common Setting
            sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLCommonConfig()
            # mr Setting
            sk_renderLayer_Yo.sk_renderLayer_Yo().mentalRayProductionLevel()
 
            
            # 格式
            sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLFramebuffer('iff',3,0) 
            mc.setAttr('miDefaultOptions.miRenderUsing', 0)
            mc.setAttr('miDefaultOptions.miRenderUsing', 2)   
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
            sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLSave('ENV',3)
            
        # 干掉base File
#        import os
#        os.remove(baseFileName)
        #删除render文件夹
        renderFold = sk_infoConfig.sk_infoConfig().checkRenderLayerLocalPath(3)+'render/'
        files=mc.getFileList(folder=renderFold)
        if files:
            for fil in files:
                mc.sysFile((renderFold+fil),delete=1)

#        import os
#        os.remove(renderFold)
    
        print('=======================!!!All Done!!!=======================')
        print(pathLocal)
        print('===========================================================')


#读取层信息
    def ydlayerinfo(self, layerType='CHRM', selectObjType=0,infotype='CO'):
        # 物体信息
        rlObjs      = []
        MaskObjs    = []
        layerName   = ''
        rlSGNodes   = []
        rlLights    = []
        layerObjs   = []
        if selectObjType == 0:
            needInfo = sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLObjsInfo(layerType,infotype)
            rlObjs    = needInfo[0]
            MaskObjs  = needInfo[1]
            layerName = needInfo[2]
            #rlSGNodes = needInfo[3]
            rlLights  = needInfo[4]
            layerObjs = needInfo[5]
        # 选取模式
        if selectObjType == 1:
            rlObjs    = sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLSelectMode()
            layerObjs = rlObjs
            layerName = createName + infotype
    
        return   [rlObjs, MaskObjs, layerName,rlSGNodes,rlLights, layerObjs]  

#导出相应文件    
    def ydfileExr(self,layerType='CHRM', selectObjType=0,infotype='CO'):
        # 物体信息
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        pathLocal = sk_infoConfig.sk_infoConfig().checkRenderLayerLocalPath(3)+'render/'
        
        mc.sysFile(pathLocal, makeDir=True)
        layernum=''
        if layerType=='SET' and layerName=='AO':
            layernum='l3'
        else:
            layernum='l4'        
        shortName=''
        if infotype=='RGB':
            shortName=shotInfo[0]+'_'+shotInfo[1]+'_'+shotInfo[2]+'_'+shotInfo[3]+'_'+layernum+layerType+infotype+'_lr_c001.mb'
        else:            
            shortName=shotInfo[0]+'_'+shotInfo[1]+'_'+shotInfo[2]+'_'+shotInfo[3]+'_'+layernum+layerType+'_lr_c001.mb'
        needInfo = self.ydlayerinfo(layerType, selectObjType,infotype)
        rlObjs    = needInfo[0]
        MaskObjs  = needInfo[1]
        layerName = needInfo[2]
        #rlSGNodes = needInfo[3]
        rlLights  = needInfo[4]
        layerObjs = needInfo[5]
        camn='*:*am_'+shotInfo[1]+'_'+shotInfo[2]+'_'+shotInfo[3]+'_baked'
        cams=mc.ls(camn,l=1)
        cam=''
        if cams:
            cam=cams[0]
        if rlObjs:
            objs=rlObjs+rlLights+[cam]
            for obj in objs:
                if not obj:
                    continue
                try:
                    mc.select(obj,add=1)
                except:
                    pass
            mrNodes = mc.ls(type='mentalrayGlobals')+ mc.ls(type='mentalrayItemsList') +mc.ls(type='mentalrayOptions')
            if mrNodes:
                mc.select(mrNodes,add = 1)            
            mc.file((pathLocal+shortName),options='v=0',f=1,type='mayaBinary',preserveReferences=1,es=1)            
        return 0 

    def ydfileOpen(self,layerType='CHRM', selectObjType=0,infotype='CO'):
        # 物体信息
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        pathLocal = sk_infoConfig.sk_infoConfig().checkRenderLayerLocalPath(3)+'render/'
        
        layernum=''
        if layerType=='SET' and layerName=='AO':
            layernum='l3'
        else:
            layernum='l4'        
        
        shortName=''
        if infotype=='RGB':
            shortName=shotInfo[0]+'_'+shotInfo[1]+'_'+shotInfo[2]+'_'+shotInfo[3]+'_'+layernum+layerType+infotype+'_lr_c001.mb'
        else:            
            shortName=shotInfo[0]+'_'+shotInfo[1]+'_'+shotInfo[2]+'_'+shotInfo[3]+'_'+layernum+layerType+'_lr_c001.mb'
        needInfo = self.ydlayerinfo(layerType, selectObjType,infotype)
        rlObjs    = needInfo[0]
        MaskObjs  = needInfo[1]
        layerName = needInfo[2]
        #rlSGNodes = needInfo[3]
        rlLights  = needInfo[4]
        layerObjs = needInfo[5]
        if rlObjs:
             mc.file((pathLocal+shortName),options='v=0',type='mayaBinary',f=1,o=1)
        # common Setting
        sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLCommonConfig()
        
        # mr Setting
        sk_renderLayer_Yo.sk_renderLayer_Yo().mentalRayProductionLevel()
        
        # 格式
        sk_renderLayer_Yo.sk_renderLayer_Yo().ydRLFramebuffer('iff',3,0)              
        # 设置  

        shot = shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2] + '_' + shotInfo[3] 
               
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
        return 0 

               