
# -*- coding: utf-8 -*-

'''
Created on 2015-11-13

@author: liangyu
'''
import maya.cmds as mc
import maya.mel as mel
import idmt.pipeline.db
import re
from pymel.core import *

from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
reload(sk_infoConfig)
from idmt.maya.Hh_common import hh_RenderArnoldLayer
reload(hh_RenderArnoldLayer)
class Lion_renderLayer(object):
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
    

    def LionRLObjectsTList(self):
        # 获取root
        from idmt.maya.py_common import sk_checkCommon
        reload(sk_checkCommon)
        refCHR = []
        refPROP = []
        refSET = []
        needSKY = []
        needPROP = []
        needrefSEA = []
        needInfo=[]
        if mc.ls('CHR_GRP'):
            if mc.listRelatives('CHR_GRP', c=1, f=1, type='transform'):
                refCHR = mc.listRelatives('CHR_GRP', c=1, f=1, type='transform')
        if mc.ls('PRP_GRP'):
            if mc.listRelatives('PRP_GRP', c=1, f=1, type='transform'):
                refPROP = mc.listRelatives('PRP_GRP', c=1, f=1, type='transform')
        if mc.ls('SET_GRP'):
            if mc.listRelatives('SET_GRP', c=1, f=1, type='transform'):
                refSETgroup = mc.listRelatives('SET_GRP', c=1, f=1, type='transform')
                refSET=mc.listRelatives(refSETgroup, c=1, f=1, type='transform')
        for i in range(3):
            needInfo = []
            if i == 0:
                refGrps = refCHR
            if i == 1:
                refGrps = refPROP
            if i == 2:
                refGrps = refSET
            if refGrps:
                meshes = mc.listRelatives(refGrps, ad=1, ni=1, type='mesh', f=1)
                if meshes:
                    for mesh in meshes:
                        objs=mc.listRelatives(mesh,p=1,f=1)
                        if  objs and 'MODEL|' in mesh:
                          needInfo.append(objs[0])
            if i == 0:
                CHRR = needInfo
            if i == 1:
                PROPR = needInfo
            if i == 2:
                SETR = needInfo
        result = [CHRR,PROPR,SETR]
        return result
    def ARtifSetting(self):
        mc.setAttr('defaultRenderGlobals.outFormatControl', 1)
        mc.setAttr('defaultArnoldDriver.aiTranslator','tif',type='string')
        mc.setAttr('defaultArnoldDriver.tiffFormat',0)
        mc.setAttr('defaultArnoldDriver.tiffCompression',1)
        mc.setAttr ('defaultArnoldDriver.mergeAOVs', 0)
        mc.setAttr ('defaultArnoldRenderOptions.aovMode',1)
        return 0

    #anorld渲染设置
    def NorCommonSetting(self,form='exr',type='mesh'):
        print (u'===============!!!Start 【%s】!!!===============' % (u'标准设置'))
        print 'Working...'
        
        # Camera
        from idmt.maya.commonCore.core_mayaCommon import sk_hbExportCam
        reload(sk_hbExportCam)

        # 标准设置
        mc.setAttr('defaultRenderGlobals.imageFormat', 7)
        try:
           mc.loadPlugin('mtoa',qt=1)
        except:
            pass
        # 开启窗口，创建各种UI
        #mel.eval('unifiedRenderGlobalsWindow')
        renderglobal=mc.getAttr('defaultRenderGlobals.currentRenderer')
        if renderglobal!='arnold':
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'arnold', type='string')
    # 下来所需的节点提前创建
        import mtoa
        mtoa.core.createOptions()
        import mtoa.cmds.registerArnoldRenderer
        mtoa.cmds.registerArnoldRenderer.registerArnoldRenderer()
        mc.setAttr('defaultRenderQuality.edgeAntiAliasing', 1)
        #mc.setAttr('defaultRenderGlobals.animation', 1)
        mel.eval("setMayaSoftwareFrameExt(3,0)")
        mc.setAttr('defaultRenderGlobals.outFormatControl', 0)
        mc.setAttr('defaultRenderGlobals.extensionPadding', 4)
        mc.setAttr('defaultRenderGlobals.imageFilePrefix', '<RenderLayer>/<Scene>_<RenderLayer>', type='string')
        mc.setAttr('defaultResolution.width', 1920)
        mc.setAttr('defaultResolution.height', 1080)
        mc.setAttr('defaultResolution.deviceAspectRatio', 1.778)
        mc.setAttr('defaultResolution.pixelAspect', 1.00)
        mc.evalDeferred('import maya.cmds as mc\nmc.setAttr((\'defaultResolution.pixelAspect\'),1)', lowestPriority=1)
        mc.setAttr('defaultResolution.dotsPerInch', 72)
        mc.setAttr('defaultRenderQuality.edgeAntiAliasing', 1)
        mc.setAttr("defaultArnoldRenderOptions.progressive_initial_level",3)
        mc.setAttr('defaultArnoldRenderOptions.texture_gamma',2.2)
        mc.setAttr('defaultViewColorManager.displayColorProfile', 3)
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
            
        if form=='exr':
            mc.setAttr('defaultArnoldDriver.aiTranslator','exr',type='string')            
            mc.setAttr ('defaultArnoldDriver.mergeAOVs', 1) 
            mc.setAttr ('defaultArnoldRenderOptions.aovMode',1)
            mc.setAttr('defaultArnoldRenderOptions.texture_gamma', 2.2)
            mc.setAttr('defaultViewColorManager.displayColorProfile', 3)
        if form=='tif':
            mc.setAttr('defaultArnoldDriver.aiTranslator','tif',type='string')
            mc.setAttr('defaultArnoldDriver.tiffFormat',0)
            mc.setAttr('defaultArnoldDriver.tiffCompression',1)
            mc.setAttr ('defaultArnoldDriver.mergeAOVs', 0)
            mc.setAttr ('defaultArnoldRenderOptions.aovMode',1)  
        if type=='mesh':
            mc.setAttr('defaultArnoldRenderOptions.AASamples', 4)
            mc.setAttr('defaultArnoldRenderOptions.GIDiffuseSamples', 3)
            mc.setAttr('defaultArnoldRenderOptions.GIGlossySamples', 2)
            mc.setAttr('defaultArnoldRenderOptions.GIRefractionSamples', 2)
            if mc.ls('defaultArnoldRenderOptions.sssBssrdfSamples'):
                mc.setAttr('defaultArnoldRenderOptions.sssBssrdfSamples', 3)
            mc.setAttr('defaultArnoldRenderOptions.lock_sampling_noise', 1)
            mc.setAttr('defaultArnoldRenderOptions.use_sample_clamp', 1)
            mc.setAttr('defaultArnoldRenderOptions.AASampleClamp', 1.5) 
            mc.setAttr('defaultArnoldRenderOptions.GITotalDepth', 1)
            mc.setAttr('defaultArnoldRenderOptions.autoTransparencyDepth', 2)
            mc.setAttr('defaultArnoldRenderOptions.texture_gamma', 2.2)
            mc.setAttr('defaultViewColorManager.displayColorProfile', 3)
        if type=='fur':
            mc.setAttr('defaultArnoldRenderOptions.AASamples', 6)
            mc.setAttr('defaultArnoldRenderOptions.GIDiffuseSamples', 3)
            mc.setAttr('defaultArnoldRenderOptions.GIGlossySamples', 0)
            mc.setAttr('defaultArnoldRenderOptions.GIRefractionSamples', 0)
            if mc.ls('defaultArnoldRenderOptions.sssBssrdfSamples'):
                mc.setAttr('defaultArnoldRenderOptions.sssBssrdfSamples', 0)
            mc.setAttr('defaultArnoldRenderOptions.lock_sampling_noise', 1)
            mc.setAttr('defaultArnoldRenderOptions.use_sample_clamp', 1)
            mc.setAttr('defaultArnoldRenderOptions.AASampleClamp', 1.5) 
            mc.setAttr('defaultArnoldRenderOptions.GITotalDepth', 1)
            mc.setAttr('defaultArnoldRenderOptions.autoTransparencyDepth', 2)

        mel.eval('setAttr -type "string" defaultRenderGlobals.preMel "cycleCheck -e off"')
        print (u'===============!!!Done  【%s】!!!===============' % u'标准设置')
        print '\n'
        return 0
 
 
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
        # 处理cam
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        shotType = sk_infoConfig.sk_infoConfig().checkShotType()
        camName = 'CAM:cam_' + str(shotInfo[1]) + '_' + str(shotInfo[2]) + '_baked'
        if not mc.ls(camName, type='transform'):
            from idmt.maya.commonCore.core_mayaCommon import sk_hbExportCam
            reload(sk_hbExportCam)
            sk_hbExportCam.sk_hbExportCam().camServerReference(info=shotType)
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
            mc.setAttr ('defaultArnoldDriver.mergeAOVs', 0)

            mc.setAttr('defaultArnoldDriver.prefix','<RenderLayer>_<RenderPass>/<Scene>_<RenderLayer>_<RenderPass>',type='string') 

            #mc.setAttr('defaultArnoldDriver.aiTranslator','exr',type='string')
            mc.setAttr('defaultArnoldDriver.aiTranslator','tif',type='string')
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
            return 0

            
    #保存文件
    def Lion_FileSave(self,alltype='CHR',type='color'):
        print ('=================================================================')
        print '====================!!!Start file save!!!===================='

        # save
        from idmt.maya.py_common import sk_infoConfig
        reload(sk_infoConfig)
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        pathLocal = sk_infoConfig.sk_infoConfig().checkRenderLayerLocalPath()
        fileName = pathLocal + shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2]
        fileType=''
        if  alltype=='CHR' and type=='color': 
            fileType = '_CHRCO_lr_c001.mb'
        if  alltype=='CHR' and type=='rgb': 
            fileType = '_CHRrgb_lr_c001.mb'
        if  alltype=='BG' and type=='color': 
            fileType = '_BGCO_lr_c001.mb'
        if  alltype=='BG' and type=='rgb': 
            fileType = '_BGrgb_lr_c001.mb'
        if  alltype == u'INTER' and type ==u'shadow':
            fileType = u'_SH_lr_c001.mb'
        fileName = fileName + fileType
        mc.file(rename=fileName)
        mc.file(save=1)

        print '=======================!!!All Done!!!======================='
        print ('===========================================================')
        
    def camImoprt(self):
        
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()       
        camName = 'CAM:cam_' + shotInfo[1] + '_' + shotInfo[2] + '_baked'
             
        if mc.ls(camName):
            ifRef = mc.referenceQuery(camName,isNodeReferenced = 1)
            if not ifRef:
                mc.delete(camName)
                mc.namespace(set=':')
                mc.namespace(force=1, moveNamespace =['CAM:',':'])
                mc.namespace(removeNamespace = 'CAM:')
        
        # Camera
        from idmt.maya.commonCore.core_mayaCommon import sk_hbExportCam
        reload(sk_hbExportCam)
        sk_hbExportCam.sk_hbExportCam().camServerReference()   
                       
        mc.setAttr((camName + '.renderable'),1)
        mc.setAttr((camName + '.farClipPlane'),100000)
        
        try:
            mc.setAttr('perspShape.renderable',0)
        except:
            pass        
 
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
         
    
    #角色color分层       
    def Lion_CHRcolorCreate(self):
        print (u'===============!!!Start !!!===============CHR_color' )
        print 'Working...' 
        
        #self.ArnoldALLDelete('aiAOV')

        # 物体
        objs = self.LionRLObjectsTList()
        refCHR = objs[0]
        refPROP = objs[1]
        refSET = objs[2]
     
        rlObjs = []
        layerName=''

        if refCHR or refPROP:
            rlObjs = refCHR + refPROP
            layerName = 'CHR'
        
        # 灯光
        #CHR_light= '//file-cluster/gdc/Projects/LION/Lion_Scratch/TD/charlight.ma'
        CHR_light= 'Z:/Projects/LION/Lion_Scratch/render/char_light/Lion_CHRLT_new.mb'
        lightfile=CHR_light
        if mc.ls('CHR_light'):
            mc.delete('CHR_light')      
        mc.file(lightfile, i=1)
        GDList=self.gdc_Attrlist(type='mesh',attrtype='GD')
        if GDList:
            for obj in GDList:
                shapes=mc.listRelatives(obj,s=1,f=1)
                for shape in shapes:
                    mc.setAttr((shape+'.primaryVisibility'),0)
        lightGRP = []
        if mc.ls('CHR_light'):
            lightGRP=mc.ls('CHR_light')       
        self.NorCommonSetting('tif','mesh')
        mc.setAttr('defaultRenderGlobals.outFormatControl', 0)
        # 创建RenderLayer
        if mc.ls(layerName):
            mc.delete(layerName)
            # 要加灯光
        mc.createRenderLayer((rlObjs + lightGRP+GDList), name=layerName, noRecurse=1, makeCurrent=1)

        self.ArnoldAOVCreat('sss')
        self.ArnoldAOVCreat('AO')
        self.ArnoldAOVCreat('Normal')
        self.ArnoldAOVCreat('Fre')
        #self.ArnoldAOVCreat('specular')
        #self.ArnoldAOVCreat('Shadow')
        self.nor_SmoothSet()
        self.camImoprt()                          
        self.zmRLCamSetting()
        self.NorCommonSetting('tif','mesh')
        #回master层
        mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')
        mc.setAttr("defaultRenderLayer.renderable", 0)
        self.Lion_FileSave('CHR','color')
        print (u'===============!!!Done !!!===============CHR_color' )
        print '\n'
        return 0
#====================Shadow 渲染层的创建========add by zhangben 20160628==================
    def Lion_SHrl_Create(self):
        print (u'===============!!!Start !!!===============SH===' )
        print 'Working...'
        #self.ArnoldALLDelete('aiAOV')
        # 物体
        objs = self.LionRLObjectsTList()
        refCHR = objs[0]
        refPROP = objs[1]
        refSET = objs[2]
        rlObjs = []
        layerName=''
        if refCHR or refPROP:
            rlObjs = refCHR + refPROP
            layerName = 'SH'
        # 灯光
        #CHR_light= '//file-cluster/gdc/Projects/LION/Lion_Scratch/TD/charlight.ma'
        CHR_light= 'Z:/Projects/LION/Lion_Scratch/render/char_light/Lion_CHRLT_new.mb'
        lightfile=CHR_light
        if mc.ls('CHR_light'):
            mc.delete('CHR_light')
        mc.file(lightfile, i=1)
        # GDList=gdc_Attrlist(type='mesh',attrtype='GD')
        # if GDList:
        #     for obj in GDList:
        #         shapes=mc.listRelatives(obj,s=1,f=1)
        #         for shape in shapes:
        #             mc.setAttr((shape+'.primaryVisibility'),0)
        lightGRP = []
        if mc.ls('charlight_meshKey_Light'):
            lightGRP=mc.ls('charlight_meshKey_Light')
        self.NorCommonSetting('tif','mesh')
        mc.setAttr('defaultRenderGlobals.outFormatControl', 0)
        # 创建RenderLayer
        if mc.ls(layerName):
            mc.delete(layerName)
            # 要加灯光
        mc.createRenderLayer((refCHR+refPROP+refSET+lightGRP), name=layerName, noRecurse=1, makeCurrent=1)
        self.ArnoldAOVCreat('AO')
        #self.ArnoldAOVCreat('specular')
        #self.ArnoldAOVCreat('Shadow')
        self.nor_SmoothSet()
        self.camImoprt()
        self.zmRLCamSetting()
        self.NorCommonSetting('tif','mesh')
        for eachOne_chrMesh in rlObjs:
            rndShp_nd = PyNode(eachOne_chrMesh).getChildren(ni=True)
            if rndShp_nd:
                rndShp_nd[0].castsShadows.set(1)
                rndShp_nd[0].primaryVisibility.set(0)
                rndShp_nd[0].receiveShadows.set(0)
        for eachOne_set in refSET:
            rndShp_nd = PyNode(eachOne_set).getChildren(ni=True)
            if rndShp_nd:
                rndShp_nd[0].castsShadows.set(0)
                rndShp_nd[0].primaryVisibility.set(1)
                rndShp_nd[0].receiveShadows.set(1)
        mel.eval(u'hookShaderOverride(\"%s\",\"aiShadowCatcher\", \"\")'%layerName)
        for each_aiSC in ls(type ='aiShadowCatcher'):
            each_aiSC.shadowColor.set(1,1,1)
        #回master层
        mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')
        mc.setAttr("defaultRenderLayer.renderable", 0)
        self.Lion_FileSave('INTER','shadow')
        print (u'===============!!!Done !!!===============SHADOW' )
        print '\n'
        return 0

   
    #角色IDP分层                              
    def Lion_CHRidpCreate(self):
        print (u'===============!!!Start !!!===============CHR_IDP' )
        print 'Working...'
        self.NorCommonSetting('tif','mesh')

        from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
        reload(sk_referenceConfig)
        refInfos = sk_referenceConfig.sk_referenceConfig ().checkReferenceListInfo()
        refPaths = refInfos[1][0]
        
        if refPaths:
            for refPath in refPaths:
                try:
                    if refPath.split('_')[1][0]=='s' or refPath.split('_')[1][0]=='S':
                        refExist = mc.referenceQuery(refPath,rfn=1)
                        mc.file(rfn=refExist,removeReference=1)
                except:
                    pass 
                
        #self.ArnoldALLDelete('aiAOV')

        from idmt.maya.Hh_common import hh_RenderArnoldLayer
        reload(hh_RenderArnoldLayer)
        hh_RenderArnoldLayer.hh_RenderArnold().csl_IDRenderLayerCreatAll(type="chr",ref=1)
 
                

        self.camImoprt()
        self.zmRLCamSetting()             
        #回master层
        mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')
        mc.setAttr("defaultRenderLayer.renderable", 0)
                              
        self.Lion_FileSave('CHR','rgb')
        print (u'===============!!!Done !!!===============CHR_IDP' )
        print '\n'        
    
         
       
    #场景IDP分层                              
    def Lion_SETidpCreate(self):
        print (u'===============!!!Start !!!===============SET_IDP' )
        print 'Working...'
        self.NorCommonSetting('tif','mesh')

        from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
        reload(sk_referenceConfig)
        refInfos = sk_referenceConfig.sk_referenceConfig ().checkReferenceListInfo()
        refPaths = refInfos[1][0]
        
        if refPaths:
            for refPath in refPaths:
                try:
                    if refPath.split('_')[1][0]!='s' and refPath.split('_')[1][0]!='S':
                        refExist = mc.referenceQuery(refPath,rfn=1)
                        mc.file(rfn=refExist,removeReference=1)
                except:
                    pass   

        self.ArnoldALLDelete('aiAOV') 
        
        from idmt.maya.Hh_common import hh_RenderArnoldLayer
        reload(hh_RenderArnoldLayer)
        hh_RenderArnoldLayer.hh_RenderArnold().csl_IDRenderLayerCreatAll(type="set",ref=0)
               

        self.zmRLCamSetting()
        #回master层
        mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')
        mc.setAttr("defaultRenderLayer.renderable", 0)
        self.Lion_FileSave('BG','rgb')
        print (u'===============!!!Done !!!===============SET_IDP' )
        print '\n' 
            
            
    #场景color分层       
    def Lion_SETcolorCreate(self):
        print (u'===============!!!Start !!!===============SET_color' )
        print 'Working...' 
        
        #self.ArnoldALLDelete('aiAOV')
        self.NorCommonSetting('tif','mesh')
        # 物体
        objs = self.LionRLObjectsTList()
        refCHR = objs[0]
        refPROP = objs[1]
        refSET = objs[2]
        
        set=[]
        if refSET:
            for obj in refSET:
                if '_light_' not in obj:
                    set.append(obj)
     
        rlObjs = []
        layerName=''
        if set:
            rlObjs = set
            
        
        # 灯光
        lightGRP=mc.ls('*:*MSH_Set_light') + mc.ls('*:*MSH_Set_Light')
        LightKEY=[]
        LightENV=[]
        if lightGRP:
            lightdown=mc.listRelatives(lightGRP, c=1, f=1, type='transform')
            if lightdown:
                for light in lightdown:
                    if 'key' in light:
                        LightKEY.append(light)
                    else:
                        LightENV.append(light)
            else:
                mc.warning(u'==================场景灯光组下，缺少灯光，主检查文件==========')
                mc.error(u'==================场景灯光组下，缺少灯光,请检查文件==========')
        else:
            mc.warning(u'==================场景中缺少场景灯光，请检查文件==========')
            mc.error(u'==================场景中缺少场景灯光，请检查文件==========')

        if rlObjs:
            if LightKEY:
                layerName='SET'
                print LightKEY
                # 创建KEY层
                mc.createRenderLayer((rlObjs + LightKEY), name=layerName, noRecurse=1, makeCurrent=1)
            if LightENV:
                layerName='SETEnv'
                mc.createRenderLayer((rlObjs + LightENV), name=layerName, noRecurse=1, makeCurrent=1)   
                self.ArnoldAOVCreat('AO')
                self.ArnoldAOVCreat('Normal')
                self.ArnoldAOVCreat('Fre')
                self.ArnoldAOVCreat('Zdp')


        self.nor_SmoothSet()  
        self.camImoprt()                          
        self.zmRLCamSetting()             
        #回master层
        mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')
        mc.setAttr("defaultRenderLayer.renderable", 0)

        self.Lion_FileSave('BG','color')
        print (u'===============!!!Done !!!===============SET_color' )
        print '\n'

# 【lion 项目】【特殊属性列表】
#  Author : hanhong
    def gdc_Attrlist(self,type='mesh',attrtype='GD'):
        objList=[]
        objs=mc.ls(type=type,l=1)
        if objs:
            for obj in objs:
                tr=mc.listRelatives(obj,p=1,type='transform',f=1)
                if tr and mc.objExists(tr[0]+'.'+attrtype) and mc.getAttr(tr[0]+'.'+attrtype)==1 and tr[0] not in objList:
                     objList.append(tr[0])
        return objList