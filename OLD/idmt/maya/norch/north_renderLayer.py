
# -*- coding: utf-8 -*-

'''
Created on 2015-4-27

@author: liangyu
'''
import maya.cmds as mc
import maya.mel as mel
import idmt.pipeline.db
import re

from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
reload(sk_infoConfig)

class north_renderLayer(object):
    def __init__(self):
        pass
    #选择物体 
    def objsCreate(self):
        needObjs = []
        # 选取模式
        selObjs = mc.ls(sl=1, l=1)
        if not selObjs:
            mc.confirmDialog(title=u'警告', message=u'请选择物体', button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No') 
            mc.error(u'请选择物体')        
        return selObjs
    #anorld渲染设置
    def NorCommonSetting(self,form='exr',type='mesh'):
        print (u'===============!!!Start 【%s】!!!===============' % (u'标准设置'))
        print 'Working...'
        
        # Camera
        from idmt.maya.commonCore.core_mayaCommon import sk_hbExportCam
        reload(sk_hbExportCam)

        # 标准设置
        mc.setAttr('defaultRenderGlobals.currentRenderer', 'arnold', type='string')
        mc.setAttr('defaultRenderQuality.edgeAntiAliasing', 1)
        mc.setAttr('defaultRenderGlobals.animation', 1)
        mc.setAttr('defaultRenderGlobals.outFormatControl', 0)
        mc.setAttr('defaultRenderGlobals.extensionPadding', 4)
        mc.setAttr('defaultRenderGlobals.imageFilePrefix', '<RenderLayer>/<Scene>_<RenderLayer>', type='string')
        mc.setAttr('defaultResolution.width', 1998)
        mc.setAttr('defaultResolution.height', 1080)
        mc.setAttr('defaultResolution.deviceAspectRatio', 1.85)
        mc.setAttr('defaultResolution.pixelAspect', 1.00)
        mc.evalDeferred('import maya.cmds as mc\nmc.setAttr((\'defaultResolution.pixelAspect\'),1)', lowestPriority=1)
        mc.setAttr('defaultResolution.dotsPerInch', 72)
        mc.setAttr('defaultRenderQuality.edgeAntiAliasing', 1)
        mc.setAttr("defaultArnoldRenderOptions.progressive_initial_level",3)
        mc.setAttr('defaultArnoldRenderOptions.texture_gamma',1)
        mc.setAttr("defaultViewColorManager.displayColorProfile",2)
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
            
        if(form=='exr'):
            mc.setAttr('defaultArnoldDriver.aiTranslator','exr',type='string')            
            mc.setAttr ('defaultArnoldDriver.mergeAOVs', 1) 
            mc.setAttr ('defaultArnoldRenderOptions.aovMode',1)
        if(form=='tif'):            
            mc.setAttr('defaultArnoldDriver.aiTranslator','tif',type='string')
            mc.setAttr('defaultArnoldDriver.tiffFormat',0)
            mc.setAttr('defaultArnoldDriver.tiffCompression',1) 
            mc.setAttr ('defaultArnoldDriver.mergeAOVs', 0)
            mc.setAttr ('defaultArnoldRenderOptions.aovMode',1)  
        if(type=='mesh'):   
            mc.setAttr('defaultArnoldRenderOptions.AASamples', 4)
            mc.setAttr('defaultArnoldRenderOptions.GIDiffuseSamples', 3)
            mc.setAttr('defaultArnoldRenderOptions.GIGlossySamples', 2)
            mc.setAttr('defaultArnoldRenderOptions.GIRefractionSamples', 2)
            mc.setAttr('defaultArnoldRenderOptions.sssBssrdfSamples', 3)
            mc.setAttr('defaultArnoldRenderOptions.lock_sampling_noise', 1)
            mc.setAttr('defaultArnoldRenderOptions.use_sample_clamp', 1)
            mc.setAttr('defaultArnoldRenderOptions.AASampleClamp', 1.5) 
            mc.setAttr('defaultArnoldRenderOptions.GITotalDepth', 1)
            mc.setAttr('defaultArnoldRenderOptions.autoTransparencyDepth', 2) 
        if(type=='fur'):   
            mc.setAttr('defaultArnoldRenderOptions.AASamples', 6)
            mc.setAttr('defaultArnoldRenderOptions.GIDiffuseSamples', 3)
            mc.setAttr('defaultArnoldRenderOptions.GIGlossySamples', 0)
            mc.setAttr('defaultArnoldRenderOptions.GIRefractionSamples', 0)
            mc.setAttr('defaultArnoldRenderOptions.sssBssrdfSamples', 0)
            mc.setAttr('defaultArnoldRenderOptions.lock_sampling_noise', 1)
            mc.setAttr('defaultArnoldRenderOptions.use_sample_clamp', 1)
            mc.setAttr('defaultArnoldRenderOptions.AASampleClamp', 1.5) 
            mc.setAttr('defaultArnoldRenderOptions.GITotalDepth', 1)
            mc.setAttr('defaultArnoldRenderOptions.autoTransparencyDepth', 2)                   
                 

        mel.eval('setAttr -type "string" defaultRenderGlobals.preMel "cycleCheck -e off"')
               
        print (u'===============!!!Done  【%s】!!!===============' % u'标准设置')
        print '\n'
 
 
    # mr 产品级设置
    def mentalRayProductionLevel(self):
        print (u'===============!!!Start 【%s】!!!===============' % (u'MR设置'))
        print 'Working...'

       
        try:
            mel.eval('loadPlugin "Mayatomr"')
        except:
            pass

        mc.editRenderLayerAdjustment("defaultRenderGlobals.currentRenderer")
        mc.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')

      # tif
        mc.editRenderLayerAdjustment('defaultRenderGlobals.imageFormat')
        mc.setAttr('defaultRenderGlobals.imageFormat', 3)
        
        mc.setAttr("miDefaultOptions.miRenderUsing",2)
        mc.setAttr('miDefaultOptions.maxSamples', 2)
        mc.setAttr('miDefaultOptions.contrastR', 0.1)
        mc.setAttr('miDefaultOptions.contrastG', 0.1)
        mc.setAttr('miDefaultOptions.contrastB', 0.1)
        mc.setAttr('miDefaultOptions.contrastA', 0.1)
        mc.setAttr("miDefaultOptions.jitter",1)
        
        mc.setAttr("miDefaultOptions.miRenderUsing",2)
        try:
            mc.setAttr('miDefaultOptions.minSamples', 0)
        except:
            pass

        # 过滤
        mc.setAttr('miDefaultOptions.filter', 2)
        mc.setAttr('miDefaultOptions.filterWidth', 1)
        mc.setAttr('miDefaultOptions.filterHeight', 2)
        
        
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

        
        print (u'===============!!!Done  【%s】!!!===============' % (u'MR设置'))
        print '\n'
        
        
                
    # 摄像机设置
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
            mc.error(u'===============未找到有效CAM【%s】===============' % camName)
   
    #anorld_smooth设置
    def nor_FinalSmoothSet(self,smoothInfo='smooth_2',renderusing='arnold',tangents=1):
        Sets=mc.ls(set=1)
        smoothNum=int(smoothInfo.split('_')[-1])
        for set in Sets:
            if re.search(smoothInfo,set)!=None:
                objs=mc.sets(set,q=1)
                if objs:
                    for obj in objs:
                        objfull=mc.ls(obj,l=1)
                        meshs=mc.listRelatives(objfull,s=1,f=1,type='mesh')
                        if meshs:
                            for mesh in meshs:
                                if smoothNum==0:
                                    try:
                                        mc.setAttr((mesh+'.aiSubdivType'),0)
                                    except:
                                        print(u'===============!!!物体中没有这个属性 【%s】!!!===============' % mesh+'.aiSubdivType')
                                else:                             
                                    mc.setAttr((mesh+'.aiSubdivType'),1)
                                    mc.setAttr((mesh+'.aiSubdivIterations'),smoothNum)
                                    if tangents==1:
                                        mc.setAttr((mesh+'.aiSubdivSmoothDerivs'),1)
                                    if tangents==0:
                                        mc.setAttr((mesh+'.aiSubdivSmoothDerivs'),0)                                                                                  
                                    
        print (u'===============!!!已经设置 【%s】!!!===============' % smoothInfo)
        return 0 
    
    #anorld_smooth调用 
    def nor_SmoothSet(self):
        self.nor_FinalSmoothSet(smoothInfo='smooth_0',renderusing='arnold',tangents=0)
        self.nor_FinalSmoothSet(smoothInfo='smooth_1',renderusing='arnold',tangents=0) 
        self.nor_FinalSmoothSet(smoothInfo='smooth_2',renderusing='arnold',tangents=0)
        return 0    


    # 删除所有AOV
    def ArnoldALLDelete(self,nodetype='aiAOV'):
        Info = mc.ls(type=nodetype)  
        if nodetype=='renderLayer':
            Info.remove('defaultRenderLayer')
            mc.editRenderLayerGlobals(currentRenderLayer='defaultRenderLayer')
        if mc.ls(Info) :
                mc.delete(Info)
                
    # 导入灯光
    def norlightingImp(self,type='CHR'):                
        CHR_light=''
        AN_light=''
        lightfile=''
        if(type=='CHR'):
            CHR_light= 'Z:/Projects/North/North_Scratch/render/light/humanLight.ma'
            lightfile=CHR_light
        if(type=='AN'):        
            AN_light = 'Z:/Projects/North/North_Scratch/render/light/AnimalLight.ma'
            lightfile=AN_light
        if mc.ls('human_light_GRP'):
            mc.delete('human_light_GRP')
        if mc.ls('animal_light_GRP'):
            mc.delete('animal_light_GRP')
        
        mc.file(lightfile, i=1)   
    #MR_smooth调用
    def zmRLDoSmooth(self):
        from idmt.maya.py_common import sk_smoothSet
        reload(sk_smoothSet)
        sk_smoothSet.sk_smoothSetTools().smoothSetDoSmooth()

    #材质球创建
    def ArnoldShaderAssign(self,shaderType='Shadow',transparency=0):
        meshs=mc.ls(sl=1,l=1)
        if transparency==0:
            Shade='SHD_'+shaderType+'_arnold'
            SG=Shade+'SG'
            #删除已有材质球和SG节点
            if mc.objExists(Shade):
                mc.delete(Shade)
            if mc.objExists(SG):
                mc.delete(SG) 
            #创建新材质球和SG节点
            if shaderType=='AO':
                mc.shadingNode('aiAmbientOcclusion', asShader=True,n=Shade)
            if shaderType=='Shadow':
                mc.shadingNode('aiShadowCatcher', asShader=True,n=Shade)    
            else:
                mc.shadingNode('aiUtility', asShader=True,n=Shade)
            mc.sets(renderable=1,noSurfaceShader=1,em=1,n=SG)
            mc.connectAttr(('%s.outColor' % Shade),('%s.surfaceShader' % SG))
            if meshs:
                mc.sets(meshs,e=1, forceElement = SG)
            else:
                pass            
            if shaderType=='Zdp': 
                #节点
                setRange='csl_setRange_arnold'
                express='csl_expression_arnold'
                multiply='csl_multiplyDivide_arnold'
                samplerInfo='csl_samplerInfo_arnold'
                #创建节点
                if mc.objExists(setRange):
                    mc.delete(setRange)
                if mc.objExists(multiply):
                    mc.delete(multiply) 
                if mc.objExists(samplerInfo):
                    mc.delete(samplerInfo) 
                if mc.objExists(express):
                    mc.delete(express)     
                #创建节点
                #mc.shadingNode('aiUtility', asShader=True,n=Shade)
                mc.shadingNode('setRange',asUtility=True,n=setRange)
                mc.shadingNode('multiplyDivide',asUtility=True,n=multiply)
                mc.shadingNode('samplerInfo',asUtility=True,n=samplerInfo)  
                #添加shade节点
                mc.setAttr((Shade+'.shadeMode'),2)
                mc.addAttr(Shade,sn='black',longName='black',nn='Black',attributeType='double')
                mc.addAttr(Shade,sn='write',longName='write',nn='Write',attributeType='double')
                mc.addAttr(Shade,sn='farClipPlane',longName='farClipPlane',nn='Far Clip Plane',attributeType='double')
                mc.addAttr(Shade,sn='nearClipPlane',longName='nearClipPlane',nn='Near Clip Plane',attributeType='double')
                #shade参数设置
                mc.setAttr((Shade+'.shade_mode'),2)
                mc.setAttr((Shade+'.black'),1)
                mc.setAttr((Shade+'.write'),-1)
                mc.setAttr((Shade+'.farClipPlane'),800)
                mc.setAttr((Shade+'.nearClipPlane'),1)
                #range设置
                mc.setAttr((setRange+".ai_max"), 1,0,0)
                #multiply设置
                mc.setAttr((multiply+".i2"), -1,1,1)
                mc.setAttr((multiply+'.input2X'),-1)
                #express创建
                expCommon=setRange+'.oldMinX='+Shade+'.nearClipPlane;\n'+setRange+'.oldMaxX='+Shade+'.farClipPlane;'
                mc.expression (n=express,s=expCommon)
                #连接节点
                #setRange 与Shade连接
                mc.connectAttr((setRange+'.outValueX'),(Shade+'.colorR'),f=1)
                mc.connectAttr((setRange+'.outValueX'),(Shade+'.colorG'),f=1)
                mc.connectAttr((setRange+'.outValueX'),(Shade+'.colorB'),f=1)
                mc.connectAttr((Shade+'.write'),(setRange+'.maxX'),f=1)
                mc.connectAttr((Shade+'.black'),(setRange+'.minX'),f=1)
                #multiplyDivide 与multiply连接
                mc.connectAttr((multiply+'.outputX'),(setRange+'.valueX'),f=1)
                #samplerInfo与multiplyDivide连接
                mc.connectAttr((samplerInfo+'.pointCameraZ'),(multiply+'.input1X'),f=1)
    #AO材质
            if shaderType=='AO':
                mc.setAttr ((Shade+'.samples'),12)
                mc.setAttr ((Shade+'.spread'),0.8)
    #Normal 材质
            if shaderType=='Normal':
                mc.setAttr ((Shade+'.shadeMode'),2)
                mc.setAttr ((Shade+'.colorMode'),3)
            if shaderType=='Fre':
                FNRamp = 'SHD_Fresnel_ramp_arnold'
                FNSample = 'SHD_Fresnel_Sample_arnold'
                if mc.ls( FNRamp ):
                    mc.delete(FNRamp)
                if mc.ls( FNSample ):
                    mc.delete(FNSample)                
                mc.shadingNode ('ramp', asShader=True, name= FNRamp)  
                mc.shadingNode ('samplerInfo', asShader=True, name= FNSample)
                mc.removeMultiInstance((FNRamp + '.colorEntryList[1]') , b = 1)
                mc.setAttr((Shade + '.shadeMode'),2)
                mc.setAttr((FNRamp + '.interpolation'),3)
                mc.setAttr((FNRamp + '.colorEntryList[2].position'),1)
                mc.setAttr((FNRamp + '.colorEntryList[0].position'),0)
                mc.setAttr((FNRamp + '.colorEntryList[2].color'),0,0,0,type = 'double3')
                mc.setAttr((FNRamp + '.colorEntryList[0].color'),1,1,1,type = 'double3') 
                mc.connectAttr(('%s.%s') % (FNSample , 'facingRatio') , ('%s.%s') % (FNRamp , 'uCoord'), f=True)
                mc.connectAttr(('%s.%s') % (FNSample , 'facingRatio') , ('%s.%s') % (FNRamp , 'vCoord'), f=True)
                mc.connectAttr(('%s.%s') % (FNRamp , 'outColor') , ('%s.%s') % (Shade , 'color'), f=True)                       
    #Shadow材质
            if shaderType=='Shadow':
                mc.setAttr((Shade + '.backgroundColor'),0,0,0,type = 'double3') 
                mc.setAttr((Shade + '.shadowColor'),1,1,1,type = 'double3')
                mc.setAttr((Shade + '.hardwareColor'),0,1,0,type = 'double3')                
            if shaderType=='Lambert':
                mc.setAttr((Shade + '.shadeMode'),1) 
                mc.setAttr((Shade + '.color'),1,1,1,type = 'double3')  
 
 
    #AVO创建
    def ArnoldAOVCreat(self,AOVtype='Zdp',passtype=int('5')):
        #Arnold 外部AOV 创建        
        if  AOVtype in ['Zdp','AO','Normal','Shadow','Fre']:
            self.ArnoldShaderAssign(AOVtype,transparency=0)
            AOVShader = 'SHD_'+AOVtype+'_arnold'
            # AOV Pass Creat
            AOVArnoldPass = 'ZDAOV_'+AOVtype
            if mc.ls(AOVArnoldPass) :
                if mc.nodeType(AOVArnoldPass) =='aiAOV':
                    pass
                else:
                    mc.delete(AOVArnoldPass)
                    mc.createNode('aiAOV',name = AOVArnoldPass)
            else:
                mc.createNode('aiAOV',name = AOVArnoldPass )
            mc.setAttr((AOVArnoldPass + '.name'),AOVtype,type = 'string')
            mc.setAttr((AOVArnoldPass + '.type'),passtype) 
            # connect
            try:
                mc.disconnectAttr(('%s.%s') % ('defaultArnoldDriver' , 'message') , ('%s.%s') % (AOVArnoldPass , 'outputs[0].driver'))
            except:
                pass
            mc.connectAttr(('%s.%s') % ('defaultArnoldDriver' , 'message') , ('%s.%s') % (AOVArnoldPass , 'outputs[0].driver'), f=True)
            try:
                mc.disconnectAttr(('%s.%s') % ( 'defaultArnoldFilter' , 'message') , ('%s.%s') % (AOVArnoldPass , 'outputs[0].filter'))
            except:
                pass
            mc.connectAttr(('%s.%s') % ( 'defaultArnoldFilter' , 'message') , ('%s.%s') % (AOVArnoldPass , 'outputs[0].filter'), f=True)
            try:
                mc.disconnectAttr(('%s.%s') % ( AOVShader , 'outColor') , ('%s.%s') % (AOVArnoldPass, 'defaultValue'))
            except:
                pass
            mc.connectAttr(('%s.%s') % ( AOVShader , 'outColor') , ('%s.%s') % (AOVArnoldPass, 'defaultValue'), f=True)
            if  AOVtype=='Zdp':
                zdpDriver='zdpAovDirver'
                if mc.ls(zdpDriver):
                    mc.delete(zdpDriver)
                mc.shadingNode('aiAOVDriver',asUtility=1,n=zdpDriver)                                 
                try:
                    mc.disconnectAttr(('%s.%s') % ('defaultArnoldDriver' , 'message') , ('%s.%s') % (AOVArnoldPass , 'outputs[0].driver'))
                except:
                    pass
                mc.connectAttr(('%s.%s') % (zdpDriver , 'message') , ('%s.%s') % (AOVArnoldPass , 'outputs[0].driver'), f=True) 
 
 
                try:
                    mc.disconnectAttr(('%s.%s') % ( AOVArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[0]'))
                except:
                    pass
                mc.connectAttr(('%s.%s') % ( AOVArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[0]'), f=True)  
                '''
                mc.setAttr((zdpDriver+'.prefix'),'<RenderLayer>_<RenderPass>/<Scene>_<RenderLayer>_<RenderPass>',type='string') 
                '''
                mc.setAttr((zdpDriver+'.aiTranslator'),'exr',type='string')
                mc.setAttr ((zdpDriver+'.exrCompression'), 3)
                mc.setAttr ((zdpDriver+'.halfPrecision'), 1)
                mc.setAttr ((zdpDriver+'.autocrop'), 1)
                mc.setAttr ((zdpDriver+'.mergeAOVs'), 1)
                mc.setAttr ((AOVArnoldPass+'.type'), 6)

            if  AOVtype=='AO':
                try:
                    mc.disconnectAttr(('%s.%s') % ( AOVArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[1]'))
                except:
                    pass
                mc.connectAttr(('%s.%s') % ( AOVArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[1]'), f=True)                 
            if  AOVtype=='Normal':
                try:
                    mc.disconnectAttr(('%s.%s') % ( AOVArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[2]'))
                except:
                    pass
                mc.connectAttr(('%s.%s') % ( AOVArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[2]'), f=True)
            if  AOVtype=='Shadow':
                try:
                    mc.disconnectAttr(('%s.%s') % ( AOVArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[3]'))
                except:
                    pass
                mc.connectAttr(('%s.%s') % ( AOVArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[3]'), f=True)
            if  AOVtype=='Fre':
                try:
                    mc.disconnectAttr(('%s.%s') % ( AOVArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[4]'))
                except:
                    pass
                mc.connectAttr(('%s.%s') % ( AOVArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[4]'), f=True)
            mc.setAttr ('defaultArnoldDriver.mergeAOVs', 1)
            '''
            mc.setAttr('defaultArnoldDriver.prefix','<RenderLayer>_<RenderPass>/<Scene>_<RenderLayer>_<RenderPass>',type='string') 
            '''
            mc.setAttr('defaultArnoldDriver.aiTranslator','exr',type='string')
            mc.setAttr ((AOVArnoldPass+'.type'), 6)
            mc.setAttr((AOVArnoldPass+'.enabled'),0)
            mc.editRenderLayerAdjustment(AOVArnoldPass+'.enabled') 
            mc.setAttr((AOVArnoldPass+'.enabled'),1)      

        #Arnold 内部AOV创建
        if  AOVtype in ['sss','Z','motionvector','opacity']:
            ArnoldPass = 'aiAOV_'+AOVtype
            if mc.ls(ArnoldPass) :
                if mc.nodeType(ArnoldPass) =='aiAOV':
                    pass
                else:
                    mc.delete(ArnoldPass)
                    mc.createNode('aiAOV',name = ArnoldPass)
            else:
                mc.createNode('aiAOV',name = ArnoldPass )
            mc.setAttr((ArnoldPass + '.name'),AOVtype,type = 'string')
            mc.setAttr((ArnoldPass + '.type'),6)   
             # aiAOVFilter
            # closset
            aiAOVFilter_Closset =  'defaultArnoldFilter_Closset'
            if mc.ls(aiAOVFilter_Closset) :
                if mc.nodeType(aiAOVFilter_Closset) =='aiAOVFilter':
                    pass
                else:
                    mc.delete(aiAOVFilter_Closset)
                    mc.createNode('aiAOVFilter',name = aiAOVFilter_Closset)
            else:
                mc.createNode('aiAOVFilter',name = aiAOVFilter_Closset )       
#
            #connect
            try:
                mc.disconnectAttr(('%s.%s') % ('defaultArnoldDriver' , 'message') , ('%s.%s') % (ArnoldPass , 'outputs[0].driver'))
            except:
                pass
            mc.connectAttr(('%s.%s') % ('defaultArnoldDriver' , 'message') , ('%s.%s') % (ArnoldPass , 'outputs[0].driver'), f=True)
            try:
                mc.disconnectAttr(('%s.%s') % ( aiAOVFilter_Closset , 'message') , ('%s.%s') % (ArnoldPass, 'outputs[0].filter'))
            except:
                pass
            mc.connectAttr(('%s.%s') % ( aiAOVFilter_Closset , 'message') , ('%s.%s') % (ArnoldPass, 'outputs[0].filter'), f=True)
            if AOVtype=='sss':
                try:
                    mc.disconnectAttr(('%s.%s') % ( ArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[21]'))
                except:
                    pass
                mc.connectAttr(('%s.%s') % ( ArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[21]'), f=True)       
            if AOVtype=='motionvector':
                try:
                    mc.disconnectAttr(('%s.%s') % ( ArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[22]'))
                except:
                    pass
                mc.connectAttr(('%s.%s') % ( ArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[22]'), f=True)  
                mc.setAttr('defaultArnoldRenderOptions.ignoreMotionBlur',1)
                mc.setAttr('defaultArnoldRenderOptions.motion_blur_enable',1)
                mc.setAttr('defaultArnoldRenderOptions.range_type',0)
            mc.setAttr ('defaultArnoldDriver.mergeAOVs', 1)
            '''
            mc.setAttr('defaultArnoldDriver.prefix','<RenderLayer>_<RenderPass>/<Scene>_<RenderLayer>_<RenderPass>',type='string') 
            ''' 
            mc.setAttr((ArnoldPass+'.enabled'),0)             
            mc.editRenderLayerAdjustment(ArnoldPass+'.enabled') 
            mc.setAttr((ArnoldPass+'.enabled'),1) 
            
            if AOVtype=='opacity':
                try:
                    mc.disconnectAttr(('%s.%s') % ( ArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[23]'))
                except:
                    pass
                mc.connectAttr(('%s.%s') % ( ArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[23]'), f=True)                               

            if AOVtype=='Z':
                try:
                    mc.disconnectAttr(('%s.%s') % ( ArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[24]'))
                except:
                    pass
                mc.connectAttr(('%s.%s') % ( ArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[24]'), f=True)          
        intPass=['direct_diffuse','direct_specular','emission','indirect_diffuse','indirect_specular','reflection','refraction','specular','N','P']
        if  AOVtype in intPass:
            for i in range(len(intPass)):
                if intPass[i]==AOVtype:
                    num=30+i
            ArnoldPass = 'aiAOV_'+AOVtype
            if mc.ls(ArnoldPass) :
                if mc.nodeType(ArnoldPass) =='aiAOV':
                    pass
                else:
                    mc.delete(ArnoldPass)
                    mc.createNode('aiAOV',name = ArnoldPass)
            else:
                mc.createNode('aiAOV',name = ArnoldPass )
            mc.setAttr((ArnoldPass + '.name'),AOVtype,type = 'string')
            mc.setAttr((ArnoldPass + '.type'),6)   
             # aiAOVFilter
            # closset
            aiAOVFilter_Closset =  'defaultArnoldFilter_Closset'
            if mc.ls(aiAOVFilter_Closset) :
                if mc.nodeType(aiAOVFilter_Closset) =='aiAOVFilter':
                    pass
                else:
                    mc.delete(aiAOVFilter_Closset)
                    mc.createNode('aiAOVFilter',name = aiAOVFilter_Closset)
            else:
                mc.createNode('aiAOVFilter',name = aiAOVFilter_Closset )       
#
            #connect
            try:
                mc.disconnectAttr(('%s.%s') % ('defaultArnoldDriver' , 'message') , ('%s.%s') % (ArnoldPass , 'outputs[0].driver'))
            except:
                pass
            mc.connectAttr(('%s.%s') % ('defaultArnoldDriver' , 'message') , ('%s.%s') % (ArnoldPass , 'outputs[0].driver'), f=True)
            try:
                mc.disconnectAttr(('%s.%s') % ( aiAOVFilter_Closset , 'message') , ('%s.%s') % (ArnoldPass, 'outputs[0].filter'))
            except:
                pass
            mc.connectAttr(('%s.%s') % ( aiAOVFilter_Closset , 'message') , ('%s.%s') % (ArnoldPass, 'outputs[0].filter'), f=True)

            if AOVtype==intPass[0]:
                try:
                    mc.disconnectAttr(('%s.%s') % ( ArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[40]'))
                except:
                    pass
                mc.connectAttr(('%s.%s') % ( ArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[40]'), f=True)       
            if AOVtype==intPass[1]:
                try:
                    mc.disconnectAttr(('%s.%s') % ( ArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[41]'))
                except:
                    pass
                mc.connectAttr(('%s.%s') % ( ArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[41]'), f=True)  

            if AOVtype==intPass[2]:
                try:
                    mc.disconnectAttr(('%s.%s') % ( ArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[42]'))
                except:
                    pass
                mc.connectAttr(('%s.%s') % ( ArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[42]'), f=True) 

            if AOVtype==intPass[3]:
                try:
                    mc.disconnectAttr(('%s.%s') % ( ArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[43]'))
                except:
                    pass
                mc.connectAttr(('%s.%s') % ( ArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[43]'), f=True) 

            if AOVtype==intPass[4]:
                try:
                    mc.disconnectAttr(('%s.%s') % ( ArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[44]'))
                except:
                    pass
                mc.connectAttr(('%s.%s') % ( ArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[44]'), f=True) 

            if AOVtype==intPass[5]:
                try:
                    mc.disconnectAttr(('%s.%s') % ( ArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[45]'))
                except:
                    pass
                mc.connectAttr(('%s.%s') % ( ArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[45]'), f=True) 

            if AOVtype==intPass[6]:
                try:
                    mc.disconnectAttr(('%s.%s') % ( ArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[46]'))
                except:
                    pass
                mc.connectAttr(('%s.%s') % ( ArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[46]'), f=True) 

            if AOVtype==intPass[7]:
                try:
                    mc.disconnectAttr(('%s.%s') % ( ArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[47]'))
                except:
                    pass
                mc.connectAttr(('%s.%s') % ( ArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[47]'), f=True) 
            if AOVtype==intPass[8]:
                zdpDriver=AOVtype+'AovDirver'
                if mc.ls(zdpDriver):
                    mc.delete(zdpDriver)
                mc.shadingNode('aiAOVDriver',asUtility=1,n=zdpDriver)                                 
                try:
                    mc.disconnectAttr(('%s.%s') % ('defaultArnoldDriver' , 'message') , ('%s.%s') % (AOVArnoldPass , 'outputs[0].driver'))
                except:
                    pass
                mc.connectAttr(('%s.%s') % (zdpDriver , 'message') , ('%s.%s') % (AOVArnoldPass , 'outputs[0].driver'), f=True) 
 
 
                try:
                    mc.disconnectAttr(('%s.%s') % ( AOVArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[48]'))
                except:
                    pass
                mc.connectAttr(('%s.%s') % ( AOVArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[48]'), f=True)  

                mc.setAttr((zdpDriver+'.aiTranslator'),'exr',type='string')
                mc.setAttr ((zdpDriver+'.exrCompression'), 3)
                mc.setAttr ((zdpDriver+'.halfPrecision'), 1)
                mc.setAttr ((zdpDriver+'.autocrop'), 1)
                mc.setAttr ((AOVArnoldPass+'.type'), 7)


            if AOVtype==intPass[9]:
                zdpDriver=AOVtype+'AovDirver'
                if mc.ls(zdpDriver):
                    mc.delete(zdpDriver)
                mc.shadingNode('aiAOVDriver',asUtility=1,n=zdpDriver)                                 
                try:
                    mc.disconnectAttr(('%s.%s') % ('defaultArnoldDriver' , 'message') , ('%s.%s') % (AOVArnoldPass , 'outputs[0].driver'))
                except:
                    pass
                mc.connectAttr(('%s.%s') % (zdpDriver , 'message') , ('%s.%s') % (AOVArnoldPass , 'outputs[0].driver'), f=True) 
 
 
                try:
                    mc.disconnectAttr(('%s.%s') % ( AOVArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[48]'))
                except:
                    pass
                mc.connectAttr(('%s.%s') % ( AOVArnoldPass , 'message') , ('%s.%s') % ('defaultArnoldRenderOptions' , 'aovList[48]'), f=True)  

                mc.setAttr((zdpDriver+'.aiTranslator'),'exr',type='string')
                mc.setAttr ((zdpDriver+'.exrCompression'), 3)
                mc.setAttr ((zdpDriver+'.halfPrecision'), 1)
                mc.setAttr ((zdpDriver+'.autocrop'), 1)
                mc.setAttr ((AOVArnoldPass+'.type'), 8)
            mc.setAttr ('defaultArnoldDriver.mergeAOVs', 1)
            '''
            mc.setAttr('defaultArnoldDriver.prefix','<RenderLayer>_<RenderPass>/<Scene>_<RenderLayer>_<RenderPass>',type='string')  
            '''
            mc.setAttr((ArnoldPass+'.enabled'),0)                          
            mc.editRenderLayerAdjustment(ArnoldPass+'.enabled') 
            mc.setAttr((ArnoldPass+'.enabled'),1)    


            
    #保存文件
    def Nor_fileSave(self,alltype='Animal',type='mesh',format='exr'):
        print ('=================================================================')
        print '====================!!!Start file save!!!===================='

        # save
        from idmt.maya.py_common import sk_infoConfig
        reload(sk_infoConfig)
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        pathLocal = sk_infoConfig.sk_infoConfig().checkRenderLayerLocalPath()
        fileName = pathLocal + shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2]
        fileType=''
        if  alltype=='Animal' and type=='mesh'and format=='exr': 
            fileType = '_AmeshEXR_lr_c001.mb'
        if  alltype=='Human' and type=='mesh'and format=='exr': 
            fileType = '_HmeshEXR_lr_c001.mb'
        if  alltype=='Animal' and type=='fur'and format=='exr': 
            fileType = '_AfurEXR_lr_c001.mb'
        if  alltype=='Human' and type=='fur'and format=='exr': 
            fileType = '_HfurEXR_lr_c001.mb'
        if  alltype=='Animal' and type=='mesh'and format=='tif': 
            fileType = '_AmeshTif_lr_c001.mb'
        if  alltype=='Human' and type=='mesh'and format=='tif': 
            fileType = '_HmeshTif_lr_c001.mb'
        if  alltype=='Animal' and type=='fur'and format=='tif': 
            fileType = '_AfurTif_lr_c001.mb'
        if  alltype=='Human' and type=='fur'and format=='tif': 
            fileType = '_HfurTif_lr_c001.mb'             
        if  alltype=='ALL' and type=='rgb'and format=='tif': 
            fileType = '_ALLRGB_lr_c001.mb'   
                                
        fileName = fileName + fileType
        mc.file(rename=fileName)
        mc.file(save=1)

        print '=======================!!!All Done!!!======================='
        print ('===========================================================')
        
            
    
    #动物mesh分层       
    def NorA_MeshCreate(self):
        print (u'===============!!!Start !!!===============AN_mesh' )
        print 'Working...' 
        
        self.ArnoldALLDelete('aiAOV') 
        
        objs=self.objsCreate() 
        rlObjs=[]
        needObjs=[]
        checkMeshes = mc.listRelatives(objs, ad=1, type='mesh',f = 1)
        if not checkMeshes:
            mc.confirmDialog(title=u'警告', message=u'请选择物体', button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')
            mc.error(u'请选择物体')
        else: 
            needObjs=  mc.listRelatives(checkMeshes, p=1, type='transform', f=1)         
            rlObjs = list(set(needObjs))
                    
        
        lights = mc.ls('animal_light_GRP')       
        if not lights:
            mc.confirmDialog(title=u'警告', message=u'请先导入动物灯光', button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')                      
            mc.error(u'请先导入动物灯光') 
        #眼睛
        eyes=[]  
        if rlObjs:
            for obj in rlObjs:
                if '_eye_' in obj:
                    eyes.append(obj)
        eyemeshes=[]
        if eyes:
            eyemeshes= mc.listRelatives(eyes, ad=1, ni=1, type='mesh', f=1)
                    
        layerobjs=rlObjs 
        layerName=''       
        if layerobjs:
            #动物mesh amb 
            if lights: 
                layerName='ANmeshAmb'
                lightGRP=[]
                if mc.ls('mesh_AMB'):
                    lightGRP=mc.ls('mesh_AMB')
                else:
                    mc.confirmDialog(title=u'警告', message=u'请联系朱瑞仪确保文件夹有灯光', button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')         
                                                      
                if mc.ls(layerName):
                    mc.delete(layerName)   
                mc.createRenderLayer((layerobjs+lightGRP), name=layerName, noRecurse=1, makeCurrent=1)
    
            #动物mesh diff                                              
            if lights:
                layerName='ANmeshDIFF' 
                lightGRP=[]
                if mc.ls('meshDiff_light'):
                    lightGRP=mc.ls('meshDiff_light')
                else:
                    mc.confirmDialog(title=u'警告', message=u'请联系朱瑞仪确保文件夹有灯光', button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')         
                                                      
                if mc.ls(layerName):
                    mc.delete(layerName)   
                mc.createRenderLayer((layerobjs+lightGRP), name=layerName, noRecurse=1, makeCurrent=1)
                self.ArnoldAOVCreat('direct_diffuse') 
                self.ArnoldAOVCreat('direct_specular') 
                self.ArnoldAOVCreat('AO')
 
            #眼睛                              
            if lights:                                              
                lightGRP=[]
                if mc.ls('meshDiff_light') and mc.ls('mesh_AMB'):
                    lightGRP=mc.ls('meshDiff_light')+ mc.ls('mesh_AMB')
                else:
                    mc.confirmDialog(title=u'警告', message=u'请联系朱瑞仪确保文件夹有灯光', button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')         
                layerName='ANeye'                                       
                if mc.ls(layerName):
                    mc.delete(layerName)   
                mc.createRenderLayer((layerobjs+lightGRP), name=layerName, noRecurse=1, makeCurrent=1)
                
                if rlObjs:
                    if eyes:
                        for obj in eyes:
                            for jbo in rlObjs:
                                if jbo==obj:
                                    print obj
                                    rlObjs.remove(jbo)
                                                                         
                SGNodes=mc.ls('SHD_Matte_ai_SG')                  
                if SGNodes:
                    for obj in rlObjs:
                        mc.sets(obj, e=1, forceElement=SGNodes[0])
                else:
                    self.Nor_Mshader()
                    SGNodes=mc.ls('SHD_Matte_ai_SG')   
                    if rlObjs:
                        for obj in rlObjs:
                            try:
                                mc.sets(obj, e=1, forceElement=SGNodes[0])
                            except:
                                print(u'请删除层后再试一次分层') 

                if eyemeshes:
                    for mesh in eyemeshes:
                        SGNode=mc.listConnections(mesh, d=1, type='shadingEngine')
                        if SGNode:
                            SGNode=SGNode[0] 
                        try:                           
                            shader = mc.listConnections((SGNode + '.surfaceShader'),s = 1,plugs = 1)[0].split('.')[-2] 
                        except:
                            pass
                        if mc.nodeType(shader)=='aiStandard':
                            mc.editRenderLayerAdjustment(shader+'.Kd')
                            mc.setAttr((shader+'.Kd'),1) 
                                                                                                             
        self.NorCommonSetting('exr','mesh')
        self.nor_SmoothSet()                            
        self.zmRLCamSetting()             
        #回master层
        mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')
        mc.setAttr("defaultRenderLayer.renderable", 0)
                              
        self.Nor_fileSave('Animal','mesh','exr')      
        print (u'===============!!!Done !!!===============AN_mesh' )
        print '\n'  
    
    #角色IDP分层                              
    def Nor_IDPCreate(self,type='CHR'):
        print (u'===============!!!Start !!!===============IDP' )
        print 'Working...'

        objs=self.objsCreate() 
        rlObjs=[]
        needObjs=[]
        checkMeshes = mc.listRelatives(objs, ad=1, type='mesh',f = 1)
        if not checkMeshes:
            mc.confirmDialog(title=u'警告', message=u'请选择物体', button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')
            mc.error(u'请选择物体')
        else: 
            needObjs=  mc.listRelatives(checkMeshes, p=1, type='transform', f=1)         
            rlObjs = list(set(needObjs))
            
                    
        objs = rlObjs
        layerName=''
        checkInfo='idp'
        if type=='CHR':
            layerName= 'chrIDP'
        if type=='AN':
            layerName= 'animalIDP'        

        RGBKey = 'FullBody'
        from idmt.maya.commonCore.core_renderLayer import sk_renderLayerCore
        reload(sk_renderLayerCore)
        RGBInfos = sk_renderLayerCore.sk_renderLayerCore().ydRLayerRGBObjectsConfig(RGBKey,0,1)

        layerObjs = []
        RObjs = []
        GObjs = []
        BObjs = []
        MObjs = []

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
            layerObjs=objs
        else:
            layerObjs = []
            mc.error(u'你选择的物体没有输出IDP信息，请找朱瑞仪输出')
        
        
        if (layerObjs):
            print '============================================='
           
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
                            
        self.mentalRayProductionLevel()
        self.zmRLDoSmooth()                            
        self.zmRLCamSetting()
        
        #回master层
        mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')
        mc.setAttr("defaultRenderLayer.renderable", 0)
        if type=='AN':
            self.Nor_fileSave('Animal','mesh','tif')
        else:
            self.Nor_fileSave('Human','mesh','tif')
            
        print (u'===============!!!Done !!!===============IDP' )
        print '\n'        
    
         
       
    #创建anorld_matte材质
    def Nor_Mshader(self):            
        SHDNode = 'SHD_Matte_ai'
        if mc.ls(SHDNode):
            mc.delete(SHDNode)
        SHDSG = 'SHD_Matte_ai_SG'
        if mc.ls(SHDSG):
            mc.delete(SHDSG)
        SHDNode = mc.shadingNode('aiStandard', asShader=True, name=SHDNode)
        SHDSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=SHDSG)
        mc.connectAttr((SHDNode + '.outColor'), (SHDSG + '.surfaceShader'))
        
        mc.setAttr((SHDNode+'.aiEnableMatte'),1)
            
            
    #动物fur分层       
    def NorA_FurCreate(self):
        print (u'===============!!!Start !!!===============animal FUR' )
        print 'Working...'

        self.ArnoldALLDelete('aiAOV')
        
        objs=self.objsCreate() 
        rlObjs=[]
        needObjs=[]
        checkMeshes = mc.listRelatives(objs, ad=1, type='mesh',f = 1)
        if not checkMeshes:
            mc.confirmDialog(title=u'警告', message=u'请选择物体', button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')
            mc.error(u'请选择物体')
        else: 
            needObjs=  mc.listRelatives(checkMeshes, p=1, type='transform', f=1)         
            rlObjs = list(set(needObjs))
                    
        layerobjs=objs
        layerName=''

        lights = mc.ls('animal_light_GRP')       
        if not lights:
            mc.confirmDialog(title=u'警告', message=u'请先导入动物灯光', button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')                      
            mc.error(u'请先导入动物灯光') 
                                
        if layerobjs: 
            '''
            self.norlightingImp('AN')
            '''  
            #AN_furAMB层                              
            if lights: 
                lightGRP=[]
                if mc.ls('furAmb_light'):
                    lightGRP=mc.ls('furAmb_light')
                else:
                    mc.confirmDialog(title=u'警告', message=u'请联系朱瑞仪确保文件夹有灯光', button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')         
                layerName='ANfurAMB'                                       
                if mc.ls(layerName):
                    mc.delete(layerName)   
                mc.createRenderLayer((layerobjs+lightGRP), name=layerName, noRecurse=1, makeCurrent=1)
                                
                SGNodes=mc.ls('SHD_Matte_ai_SG')                  
                if SGNodes:
                    for obj in rlObjs:
                        mc.sets(obj, e=1, forceElement=SGNodes[0])
                else:
                    self.Nor_Mshader()
                    SGNodes=mc.ls('SHD_Matte_ai_SG')   
                    if rlObjs:
                        for obj in rlObjs:
                            try:
                                mc.sets(obj, e=1, forceElement=SGNodes[0])
                            except:
                                print(u'请删除层后再试一次分层')       
                                
            #AN_furKEY层                              
            if lights: 
                lightGRP=[]
                if mc.ls('furKey_light'):
                    lightGRP=mc.ls('furKey_light')
                else:
                    mc.confirmDialog(title=u'警告', message=u'请联系朱瑞仪确保文件夹有灯光', button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')         
                layerName='ANfurKEY'                                       
                if mc.ls(layerName):
                    mc.delete(layerName)   
                mc.createRenderLayer((layerobjs+lightGRP), name=layerName, noRecurse=1, makeCurrent=1)
                                              
                SGNodes=mc.ls('SHD_Matte_ai_SG')                  
                if SGNodes:
                    for obj in rlObjs:
                        mc.sets(obj, e=1, forceElement=SGNodes[0])
                else:
                    self.Nor_Mshader()
                    SGNodes=mc.ls('SHD_Matte_ai_SG')   
                    if rlObjs:
                        for obj in rlObjs:
                            try:
                                mc.sets(obj, e=1, forceElement=SGNodes[0])
                            except:
                                print(u'请删除层后再试一次分层')
                        
            #AN_furRim层                              
            if lights: 
                lightGRP=[]
                if mc.ls('furRim_light'):
                    lightGRP=mc.ls('furRim_light')
                else:
                    mc.confirmDialog(title=u'警告', message=u'请联系朱瑞仪确保文件夹有灯光', button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')         
                layerName='ANfurRim'                                       
                if mc.ls(layerName):
                    mc.delete(layerName)   
                mc.createRenderLayer((layerobjs+lightGRP), name=layerName, noRecurse=1, makeCurrent=1)
                                              
                SGNodes=mc.ls('SHD_Matte_ai_SG')                  
                if SGNodes:
                    for obj in rlObjs:
                        mc.sets(obj, e=1, forceElement=SGNodes[0])
                else:
                    self.Nor_Mshader()
                    SGNodes=mc.ls('SHD_Matte_ai_SG')   
                    if rlObjs:
                        for obj in rlObjs:
                            try:
                                mc.sets(obj, e=1, forceElement=SGNodes[0])
                            except:
                                print(u'请删除层后再试一次分层')
                               
            #AN_furRGB层                              
            if lights: 
                lightGRP=[]
                if mc.ls('furRgb_light'):
                    lightGRP=mc.ls('furRgb_light')
                else:
                    mc.confirmDialog(title=u'警告', message=u'请联系朱瑞仪确保文件夹有灯光', button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')         
                layerName='ANfurRGB'                                       
                if mc.ls(layerName):
                    mc.delete(layerName)   
                mc.createRenderLayer((layerobjs+lightGRP), name=layerName, noRecurse=1, makeCurrent=1)
                                              
                SGNodes=mc.ls('SHD_Matte_ai_SG')                  
                if SGNodes:
                    for obj in rlObjs:
                        mc.sets(obj, e=1, forceElement=SGNodes[0])
                else:
                    self.Nor_Mshader()
                    SGNodes=mc.ls('SHD_Matte_ai_SG')   
                    if rlObjs:
                        for obj in rlObjs:
                            try:
                                mc.sets(obj, e=1, forceElement=SGNodes[0])
                            except:
                                print(u'请删除层后再试一次分层')
                               

            #AN_furDIFF层                              
            if lights: 
                lightGRP=[]
                if mc.ls('furDiff_light'):
                    lightGRP=mc.ls('furDiff_light')
                else:
                    mc.confirmDialog(title=u'警告', message=u'请联系朱瑞仪确保文件夹有灯光', button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')         
                layerName='ANfurDIFF'                                       
                if mc.ls(layerName):
                    mc.delete(layerName)   
                mc.createRenderLayer((layerobjs+lightGRP), name=layerName, noRecurse=1, makeCurrent=1) 
                
                SGNodes=mc.ls('SHD_Matte_ai_SG')                  
                if SGNodes:
                    for obj in rlObjs:
                        mc.sets(obj, e=1, forceElement=SGNodes[0])
                else:
                    self.Nor_Mshader()
                    SGNodes=mc.ls('SHD_Matte_ai_SG')   
                    if rlObjs:
                        for obj in rlObjs:
                            try:
                                mc.sets(obj, e=1, forceElement=SGNodes[0])
                            except:
                                print(u'请删除层后再试一次分层')
                       
                                                                                                                                         
        self.NorCommonSetting('tif','fur')
        self.nor_SmoothSet()                            
        self.zmRLCamSetting() 
                
        #回master层
        mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')
        mc.setAttr("defaultRenderLayer.renderable", 0)    
        
        self.Nor_fileSave('Animal','fur','tif')               
        print (u'===============!!!Done !!!===============Aniaml FUR' )
        print '\n'  



    #动物furDiff分层       
    def NorA_FurDiffCreate(self):
        print (u'===============!!!Start !!!===============animal FURDiff' )
        print 'Working...'

        self.ArnoldALLDelete('aiAOV')
        
        objs=self.objsCreate() 
        rlObjs=[]
        needObjs=[]
        checkMeshes = mc.listRelatives(objs, ad=1, type='mesh',f = 1)
        if not checkMeshes:
            mc.confirmDialog(title=u'警告', message=u'请选择物体', button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')
            mc.error(u'请选择物体')
        else: 
            needObjs=  mc.listRelatives(checkMeshes, p=1, type='transform', f=1)         
            rlObjs = list(set(needObjs))
                    
        layerobjs=objs
        layerName=''           
        if layerobjs:
            ''' 
            self.norlightingImp('AN')
            '''  
            #AN_furAMB层                              
            if mc.ls('animal_light_GRP'): 
                lightGRP=[]
                if mc.ls('furDiff_light'):
                    lightGRP=mc.ls('furDiff_light')
                else:
                    mc.confirmDialog(title=u'警告', message=u'请联系朱瑞仪确保文件夹有灯光', button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')         
                layerName='ANfurDIFF'                                       
                if mc.ls(layerName):
                    mc.delete(layerName)   
                mc.createRenderLayer((layerobjs+lightGRP), name=layerName, noRecurse=1, makeCurrent=1) 
                
                SGNodes=mc.ls('SHD_Matte_ai_SG')                  
                if SGNodes:
                    for obj in rlObjs:
                        mc.sets(obj, e=1, forceElement=SGNodes[0])
                else:
                    self.Nor_Mshader()
                    if rlObjs:
                        for obj in rlObjs:
                            try:
                                mc.sets(obj, e=1, forceElement=SGNodes[0])
                            except:
                                print(u'请删除层后再试一次分层')
                
                self.ArnoldAOVCreat('direct_diffuse')
            else:
                mc.confirmDialog(title=u'警告', message=u'请先导入动物灯光', button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')                                                                                     
                        

        self.NorCommonSetting('exr','fur')
        self.nor_SmoothSet()                            
        self.zmRLCamSetting() 
                
        #回master层
        mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')
        mc.setAttr("defaultRenderLayer.renderable", 0)    
        
        self.Nor_fileSave('Animal','fur','exr')               
        print (u'===============!!!Done !!!===============Aniaml FURDiff' )
        print '\n'  



    #人类fur分层       
    def NorH_FurCreate(self):
        print (u'===============!!!Start !!!===============Human FUR' )
        print 'Working...'

        self.ArnoldALLDelete('aiAOV')
        
        objs=self.objsCreate() 
        rlObjs=[]
        needObjs=[]
        checkMeshes = mc.listRelatives(objs, ad=1, type='mesh',f = 1)
        if not checkMeshes:
            mc.confirmDialog(title=u'警告', message=u'请选择物体', button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')
            mc.error(u'请选择物体')
        else: 
            needObjs=  mc.listRelatives(checkMeshes, p=1, type='transform', f=1)         
            rlObjs = list(set(needObjs))
                    
        layerobjs=objs
        layerName=''
        #眼睫毛        #眼镜
        eyelash=[] 
        specs=[] 
        if rlObjs:
            for obj in rlObjs:
                if '_eyelash_' in obj:
                    eyelash.append(obj)
                if 'ice_c007001olympia:MSH_olympa_specs_geo_' in obj:
                    specs.append(obj)                      
       
        lights = mc.ls('human_light_GRP')       
        if not lights:
            mc.confirmDialog(title=u'警告', message=u'请先导入人类灯光', button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')              
            mc.error(u'请先导入人类灯光')                        
        if layerobjs:
            #Human_furkey层                              
            if lights: 
                lightGRP=[]
                if mc.ls('furKey_Light'):
                    lightGRP=mc.ls('furKey_Light')
                else:
                    mc.confirmDialog(title=u'警告', message=u'请联系朱瑞仪确保文件夹有灯光', button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')         
                layerName='HumanfurKey'                                       
                if mc.ls(layerName):
                    mc.delete(layerName)   
                mc.createRenderLayer((layerobjs+lightGRP), name=layerName, noRecurse=1, makeCurrent=1)
                
                if eyelash:
                    for obj in eyelash:
                        mc.editRenderLayerAdjustment(obj+'.primaryVisibility')
                        mc.setAttr(obj+'.primaryVisibility', 0)
                                                
                SGNodes=mc.ls('SHD_Matte_ai_SG')                  
                if SGNodes:
                    for obj in rlObjs:
                        mc.sets(obj, e=1, forceElement=SGNodes[0])
                else:
                    self.Nor_Mshader()
                    SGNodes=mc.ls('SHD_Matte_ai_SG')   
                    if rlObjs:
                        for obj in rlObjs:
                            try:
                                mc.sets(obj, e=1, forceElement=SGNodes[0])
                            except:
                                print(u'请删除层后再试一次分层')

                if specs:
                    for obj in specs:
                        mc.editRenderLayerAdjustment(obj+'.visibility')
                        mc.setAttr(obj+'.visibility', 0)                         
                self.ArnoldAOVCreat('direct_specular')  

                self.NorCommonSetting('exr','fur')                  
                mc.editRenderLayerAdjustment('defaultArnoldRenderOptions.AASamples')
                mc.setAttr ("defaultArnoldRenderOptions.AASamples",8)
                mc.editRenderLayerAdjustment('defaultArnoldRenderOptions.GITotalDepth')
                mc.setAttr ("defaultArnoldRenderOptions.GITotalDepth",10)
                mc.editRenderLayerAdjustment('defaultArnoldRenderOptions.autoTransparencyDepth')
                mc.setAttr ("defaultArnoldRenderOptions.autoTransparencyDepth",10)  
                                              
            #Human_furAMB层                              
            if lights: 
                lightGRP=[]
                if mc.ls('furAmb'):
                    lightGRP=mc.ls('furAmb')
                else:
                    mc.confirmDialog(title=u'警告', message=u'请联系朱瑞仪确保文件夹有灯光', button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')         
                layerName='HumanfurAMB'                                       
                if mc.ls(layerName):
                    mc.delete(layerName)   
                mc.createRenderLayer((layerobjs+lightGRP), name=layerName, noRecurse=1, makeCurrent=1)

               
                if eyelash:
                    for obj in eyelash:
                        mc.editRenderLayerAdjustment(obj+'.primaryVisibility')
                        mc.setAttr(obj+'.primaryVisibility', 0)                


                                                                                  
                SGNodes=mc.ls('SHD_Matte_ai_SG')                  
                if SGNodes:
                    for obj in rlObjs:
                        mc.sets(obj, e=1, forceElement=SGNodes[0])
                else:
                    self.Nor_Mshader()
                    SGNodes=mc.ls('SHD_Matte_ai_SG')   
                    if rlObjs:
                        for obj in rlObjs:
                            try:
                                mc.sets(obj, e=1, forceElement=SGNodes[0])
                            except:
                                print(u'请删除层后再试一次分层')

                if specs:
                    for obj in specs:
                        mc.editRenderLayerAdjustment(obj+'.visibility')
                        mc.setAttr(obj+'.visibility', 0)  

                self.NorCommonSetting('exr','fur')               
                mc.editRenderLayerAdjustment('defaultArnoldRenderOptions.AASamples')
                mc.setAttr('defaultArnoldRenderOptions.AASamples', 5)
                mc.editRenderLayerAdjustment('defaultArnoldRenderOptions.GIDiffuseSamples')
                mc.setAttr('defaultArnoldRenderOptions.GIDiffuseSamples', 3)
                mc.editRenderLayerAdjustment('defaultArnoldRenderOptions.GIGlossySamples')
                mc.setAttr('defaultArnoldRenderOptions.GIGlossySamples', 0)
                mc.editRenderLayerAdjustment('defaultArnoldRenderOptions.GIRefractionSamples')
                mc.setAttr('defaultArnoldRenderOptions.GIRefractionSamples', 0)
                mc.editRenderLayerAdjustment('defaultArnoldRenderOptions.sssBssrdfSamples')
                mc.setAttr('defaultArnoldRenderOptions.sssBssrdfSamples', 0)
                mc.editRenderLayerAdjustment('defaultArnoldRenderOptions.lock_sampling_noise')
                mc.setAttr('defaultArnoldRenderOptions.lock_sampling_noise', 1)
                mc.editRenderLayerAdjustment('defaultArnoldRenderOptions.use_sample_clamp')
                mc.setAttr('defaultArnoldRenderOptions.use_sample_clamp', 1)
                mc.editRenderLayerAdjustment('defaultArnoldRenderOptions.AASampleClamp')
                mc.setAttr('defaultArnoldRenderOptions.AASampleClamp', 1.5) 
                mc.editRenderLayerAdjustment('defaultArnoldRenderOptions.GITotalDepth')
                mc.setAttr('defaultArnoldRenderOptions.GITotalDepth', 2)
                mc.editRenderLayerAdjustment('defaultArnoldRenderOptions.GIDiffuseDepth')
                mc.setAttr('defaultArnoldRenderOptions.GIDiffuseDepth', 2)
                mc.editRenderLayerAdjustment('defaultArnoldRenderOptions.GIGlossyDepth')
                mc.setAttr('defaultArnoldRenderOptions.GIGlossyDepth', 2)
                mc.editRenderLayerAdjustment('defaultArnoldRenderOptions.GIReflectionDepth')
                mc.setAttr('defaultArnoldRenderOptions.GIReflectionDepth', 0)
                mc.editRenderLayerAdjustment('defaultArnoldRenderOptions.GIRefractionDepth')
                mc.setAttr('defaultArnoldRenderOptions.GIRefractionDepth', 0)
                mc.editRenderLayerAdjustment('defaultArnoldRenderOptions.autoTransparencyDepth')
                mc.setAttr('defaultArnoldRenderOptions.autoTransparencyDepth', 5)  
                
                if mc.ls('furAmbShapeDeformed'):
                    mc.editRenderLayerAdjustment("furAmbShapeDeformed.aiSamples")
                    mc.setAttr ("furAmbShapeDeformed.aiSamples",4)       
             
                                   
            #睫毛层                              
            if lights:                                              
                lightGRP=[]
                if mc.ls('meshAmb_Light'):
                    lightGRP=mc.ls('meshAmb_Light')
                else:
                    mc.confirmDialog(title=u'警告', message=u'请联系朱瑞仪确保文件夹有灯光', button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')         
                layerName='eyelash'                                       
                if mc.ls(layerName):
                    mc.delete(layerName)   
                mc.createRenderLayer((rlObjs+lightGRP), name=layerName, noRecurse=1, makeCurrent=1)
                
                if rlObjs:
                    if eyelash:
                        for obj in eyelash:
                            for jbo in rlObjs:
                                if jbo==obj:
                                    print obj
                                    rlObjs.remove(jbo)
                                                                         
                SGNodes=mc.ls('SHD_Matte_ai_SG')                  
                if SGNodes:
                    for obj in rlObjs:
                        mc.sets(obj, e=1, forceElement=SGNodes[0])
                else:
                    self.Nor_Mshader()
                    SGNodes=mc.ls('SHD_Matte_ai_SG')   
                    if rlObjs:
                        for obj in rlObjs:
                            try:
                                mc.sets(obj, e=1, forceElement=SGNodes[0])
                            except:
                                print(u'请删除层后再试一次分层') 

                if specs:
                    for obj in specs:
                        mc.editRenderLayerAdjustment(obj+'.visibility')
                        mc.setAttr(obj+'.visibility', 0) 

                self.NorCommonSetting('exr','fur')


        self.nor_SmoothSet()                            
        self.zmRLCamSetting() 
                
        #回master层
        mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')
        mc.setAttr("defaultRenderLayer.renderable", 0)    
        
        self.Nor_fileSave('Human','fur','exr')               
        print (u'===============!!!Done !!!===============Human FUR' )
        print '\n' 
        
        
    #人类mesh分层       
    def NorH_meshCreate(self):
        print (u'===============!!!Start !!!===============Human meshEXR' )
        print 'Working...'

        self.ArnoldALLDelete('aiAOV')
        
        objs=self.objsCreate() 
        rlObjs=[]
        needObjs=[]
        checkMeshes = mc.listRelatives(objs, ad=1, type='mesh',f = 1)
        if not checkMeshes:
            mc.confirmDialog(title=u'警告', message=u'请选择物体', button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')
            mc.error(u'请选择物体')
        else: 
            needObjs=  mc.listRelatives(checkMeshes, p=1, type='transform', f=1)         
            rlObjs = list(set(needObjs))
        #眼睛       
        eyes=[]  
        if rlObjs:
            for obj in rlObjs:
                if '_eye_' in obj:
                    eyes.append(obj)
        eyemeshes=[]
        if eyes:
            eyemeshes= mc.listRelatives(eyes, ad=1, ni=1, type='mesh',f=1)
                                
        layerobjs=rlObjs
        layerName=''     
        #眼睫毛
        eyelash=[]  
        if rlObjs:
            for obj in rlObjs:
                if '_eyelash_' in obj:
                    eyelash.append(obj)
        #眼镜
        specs=mc.ls('ice_c007001olympia:MSH_olympa_specs_geo_',type='transform',sl=1,l=1)
         
        lights = mc.ls('human_light_GRP')       
        if not lights:
            mc.confirmDialog(title=u'警告', message=u'请先导入人类灯光', button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')  
            mc.error(u'请先导入人类灯光')     
            
        hairs=mc.ls(type='shaveHair')               
              
        if layerobjs: 
            '''
            self.norlightingImp('CHR')
            '''  
            #Human_meshkey层                              
            if lights: 
                lightGRP=[]
                if mc.ls('meshKey_Light'):
                    lightGRP=mc.ls('meshKey_Light')
                else:
                    mc.confirmDialog(title=u'警告', message=u'请联系朱瑞仪确保文件夹有灯光', button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')         
                layerName='HumanmeshKey'                                       
                if mc.ls(layerName):
                    mc.delete(layerName)   
                mc.createRenderLayer((layerobjs+hairs+lightGRP), name=layerName, noRecurse=1, makeCurrent=1)
                
                if hairs:
                    for obj in hairs:
                        mc.editRenderLayerAdjustment(obj+'.primaryVisibility')
                        mc.setAttr(obj+'.primaryVisibility', 0)
                        
                if eyelash:
                    for obj in eyelash:
                        mc.editRenderLayerAdjustment(obj+'.primaryVisibility')
                        mc.setAttr(obj+'.primaryVisibility', 0)                        

                if specs:
                    for obj in specs:
                        mc.editRenderLayerAdjustment(obj+'.visibility')
                        mc.setAttr(obj+'.visibility', 0) 
                
                sampleShader = mc.ls(type='samplerInfo')
                tex=''
                rampColors=''
                if sampleShader:
                    for obj in sampleShader:
                        texs= mc.listConnections((obj+'.facingRatio'),source = 1 , plugs = 1)
                        if texs:
                            tex=texs[0].split('.')[0]
                            if mc.listConnections((tex+'.colorEntryList[0].color'),source = 1 , plugs = 1):
                                rampColors=mc.listConnections((tex+'.colorEntryList[0].color'),source = 1 , plugs = 1)
                                if rampColors:
                                    rampColors=rampColors[0]
                            if mc.listConnections((tex+'.colorEntryList[1].color'),source = 1 , plugs = 1):
                                rampColors=mc.listConnections((tex+'.colorEntryList[1].color'),source = 1 , plugs = 1)
                                if rampColors:
                                    rampColors=rampColors[0]
                                                                              
                        if rampColors:
                            if rampColors.split('.')[-1]=='outColor':                          
                                rampColor=rampColors.split('.')[0]                
                                if mc.objExists(rampColor+'.colorGain'):
                                    mc.editRenderLayerAdjustment(rampColor+'.colorGain')
                                    mc.setAttr((rampColor+'.colorGain'),0,0,0,type='double3')
                
                self.ArnoldAOVCreat('direct_diffuse') 
                self.ArnoldAOVCreat('direct_specular')
                self.ArnoldAOVCreat('reflection') 
                self.ArnoldAOVCreat('sss')                                                
                self.ArnoldAOVCreat('AO') 
                                                                                                   
            #Human_meshAMB层                              
            if lights: 
                lightGRP=[]
                if mc.ls('meshAmb_Light'):
                    lightGRP=mc.ls('meshAmb_Light')
                else:
                    mc.confirmDialog(title=u'警告', message=u'请联系朱瑞仪确保文件夹有灯光', button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')         
                layerName='HumanmeshAMB'                                       
                if mc.ls(layerName):
                    mc.delete(layerName)   
                mc.createRenderLayer((layerobjs+lightGRP), name=layerName, noRecurse=1, makeCurrent=1)
                
                if eyelash:
                    for obj in eyelash:
                        mc.editRenderLayerAdjustment(obj+'.primaryVisibility')
                        mc.setAttr(obj+'.primaryVisibility', 0)                

                if specs:
                    for obj in specs:
                        mc.editRenderLayerAdjustment(obj+'.visibility')
                        mc.setAttr(obj+'.visibility', 0) 
                
                self.ArnoldAOVCreat('direct_diffuse') 
                self.ArnoldAOVCreat('direct_specular')
                self.ArnoldAOVCreat('sss')                                              
                self.ArnoldAOVCreat('reflection')                         

            #Human_meshRIM层                              
            if lights: 
                lightGRP=[]
                if mc.ls('meshRim_Light'):
                    lightGRP=mc.ls('meshRim_Light')
                else:
                    mc.confirmDialog(title=u'警告', message=u'请联系朱瑞仪确保文件夹有灯光', button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')         
                layerName='HumanmeshRIM'                                       
                if mc.ls(layerName):
                    mc.delete(layerName)   
                mc.createRenderLayer((layerobjs+lightGRP), name=layerName, noRecurse=1, makeCurrent=1)
                
                if eyelash:
                    for obj in eyelash:
                        mc.editRenderLayerAdjustment(obj+'.primaryVisibility')
                        mc.setAttr(obj+'.primaryVisibility', 0)                

                if specs:
                    for obj in specs:
                        mc.editRenderLayerAdjustment(obj+'.visibility')
                        mc.setAttr(obj+'.visibility', 0)                 
                
                self.ArnoldAOVCreat('sss')                                              
                self.ArnoldAOVCreat('Fre')  
                
            #眼睛                              
            if lights:                                              
                lightGRP=[]
                if mc.ls('meshAmb_Light_GRP') and mc.ls('meshKey_Light_GRP'):
                    lightGRP=mc.ls('meshAmb_Light_GRP')+ mc.ls('meshKey_Light_GRP')
                else:
                    mc.confirmDialog(title=u'警告', message=u'请联系朱瑞仪确保文件夹有灯光', button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')         
                layerName='Humaneye'                                       
                if mc.ls(layerName):
                    mc.delete(layerName)   
                mc.createRenderLayer((layerobjs+lightGRP), name=layerName, noRecurse=1, makeCurrent=1)
                
                if rlObjs:
                    if eyes:
                        for obj in eyes:
                            for jbo in rlObjs:
                                if jbo==obj:
                                    print obj
                                    rlObjs.remove(jbo)
                                                                         
                SGNodes=mc.ls('SHD_Matte_ai_SG')                  
                if SGNodes:
                    for obj in rlObjs:
                        mc.sets(obj, e=1, forceElement=SGNodes[0])
                else:
                    self.Nor_Mshader()
                    SGNodes=mc.ls('SHD_Matte_ai_SG')   
                    if rlObjs:
                        for obj in rlObjs:
                            try:
                                mc.sets(obj, e=1, forceElement=SGNodes[0])
                            except:
                                print(u'请删除层后再试一次分层') 

                if eyemeshes:
                    for mesh in eyemeshes:
                        SGNode=mc.listConnections(mesh, d=1, type='shadingEngine')
                        if SGNode:
                            SGNode=SGNode[0]
                        try: 
                            shader = mc.listConnections((SGNode + '.surfaceShader'),s = 1,plugs = 1)[0].split('.')[-2] 
                        except:
                            pass
                        if mc.nodeType(shader)=='aiStandard':
                            mc.editRenderLayerAdjustment(shader+'.Kd')
                            mc.setAttr((shader+'.Kd'),1)                 
                                                                                                                                                       
            self.NorCommonSetting('exr','mesh')
            self.nor_SmoothSet()                            
            self.zmRLCamSetting() 
                
        #回master层
        mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')
        mc.setAttr("defaultRenderLayer.renderable", 0)    
        
        self.Nor_fileSave('Human','mesh','exr')               
        print (u'===============!!!Done !!!===============Human meshEXR' )
        print '\n'    
        
        
        
        
        
    #保存lighting文件
    def Nor_filelightingSave(self):
        print ('=================================================================')
        print '====================!!!Start fileling save!!!===================='

        # save
        from idmt.maya.py_common import sk_infoConfig
        reload(sk_infoConfig)
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        pathLocal = sk_infoConfig.sk_infoConfig().checkRenderLayerLocalPath()
        fileName = pathLocal + shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2]
        fileType = '_lighting_lr_c001.mb'             
                                
        fileName = fileName + fileType
        mc.file(rename=fileName)
        mc.file(save=1)

        print '=======================!!! Done fileing saved!!!======================='
        print ('===========================================================')           
        
    #拆分文件
    def Nor_SeprateFileSave(self,type='CHR'):        
        from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
        reload(sk_infoConfig)
        
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        pathLocal = sk_infoConfig.sk_infoConfig().checkRenderLayerLocalPath()
        baseFileName=''
        if type=='CHR':
            baseFileName = pathLocal + shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2] + '_Human'+ '.mb'
        if type=='AN':
            baseFileName = pathLocal + shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2] + '_Animal' + '.mb'
        baseGrps=self.objsCreate()
        mc.select(baseGrps)
        mc.file(baseFileName,f = 1,es = 1,pr = 1,type = 'mayaBinary')        
        


    #所有RGB分层       
    def ALLRGBCreate(self):
        print (u'===============!!!Start !!!===============ALL RGB' )
        print 'Working...'
        
        from idmt.maya.Hh_common import hh_RenderArnoldLayer
        reload(hh_RenderArnoldLayer)
        
        if mc.ls('human_light_GRP'):
            mc.delete('human_light_GRP')
        if mc.ls('animal_light_GRP'):
            mc.delete('animal_light_GRP')        
        #物体
        meshes=mc.ls(type='mesh',l=1)
        objs=mc.listRelatives(meshes, p=1, type='transform', f=1)       
        Chrs=[]
        Props=[]
        Sets=[]
        if objs:
            for obj in objs:
                if (((obj.split('|')[-1]).split(':')[0]).split('_')[1][0])=='C' or (((obj.split('|')[-1]).split(':')[0]).split('_')[1][0])== 'c':
                    Chrs.append(obj)
                if (((obj.split('|')[-1]).split(':')[0]).split('_')[1][0])=='P' or (((obj.split('|')[-1]).split(':')[0]).split('_')[1][0])== 'p':
                    Props.append(obj)
                if (((obj.split('|')[-1]).split(':')[0]).split('_')[1][0])=='S' or (((obj.split('|')[-1]).split(':')[0]).split('_')[1][0])in ['s', 'S'] or (((obj.split('|')[-1]).split(':')[0]).split('_')[1][0])=='b':
                    Sets.append(obj)  
        #毛发
        hairs=mc.ls(type='shaveHair')
                          
        layerobjs=objs+hairs
        layerName=''  
                 
        if layerobjs: 
            layerName='ALLIDP'                                    
            if mc.ls(layerName):
                mc.delete(layerName)   
            mc.createRenderLayer(layerobjs, name=layerName, noRecurse=1, makeCurrent=1)

            if Chrs:
                for obj in Chrs:             
                    mc.select(obj)
                    hh_RenderArnoldLayer.hh_RenderArnold().ArnoldIDCreat("ArnoldIdpR")
            
            if hairs:
                if mc.ls('ArnoldIdpR'):
                    speshader=mc.ls('ArnoldIdpR')[0]
                    for shape in hairs:
                        mc.editRenderLayerAdjustment(shape+'.aiOverrideHair')
                        mc.setAttr((shape+'.aiOverrideHair'),1)
                        
                        mc.editRenderLayerAdjustment(shape+'.aiHairShader') 
                        
                        if mc.connectionInfo((shape+'.aiHairShader'), isSource=True) :    
                            ConnectShader=mc.listConnections((shape+'.aiHairShader'),source = 1 , plugs = 1)
                            for shader in ConnectShader:
                                if shader.split('.')[-1]=='outColor':
                                    mc.disconnectAttr(shader,(shape+'.aiHairShader'))
                            mc.connectAttr((speshader+'.outColor'),(shape+'.aiHairShader'))
                        else:
                            mc.connectAttr((speshader+'.outColor'),(shape+'.aiHairShader'))
                        
                                     
            if Props:
                for obj in Props:          
                    mc.select(obj)
                    hh_RenderArnoldLayer.hh_RenderArnold().ArnoldIDCreat("ArnoldIdpG") 
            

            if Sets:
                for obj in Sets:          
                    mc.select(obj)
                    hh_RenderArnoldLayer.hh_RenderArnold().ArnoldIDCreat("ArnoldIdpB")                
            
            self.NorCommonSetting('tif','fur')
            self.nor_SmoothSet()                            
            self.zmRLCamSetting() 
                                                                                                                                                                     
        #回master层
        mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')
        mc.setAttr("defaultRenderLayer.renderable", 0)    
        
        self.Nor_fileSave('ALL','rgb','tif')               
        print (u'===============!!!Done !!!===============ALL RGB' )
        print '\n'     
        
        
        
    def Nor_eyeshaderchange(self,sign=0):
        ai=sign
        eyeshader=mc.ls(type='blendColors')
        if eyeshader:
            for shader in eyeshader:
                if ai==0:
                    mc.setAttr((shader+'.blender'),0)
                if ai==1:
                    mc.setAttr((shader+'.blender'),1)        
        
                 