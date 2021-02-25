# -*- coding: utf-8 -*-

'''
Created on 2013-6-18

@author: shenkang
'''
import maya.cmds as mc
import maya.mel as mel


# shader import 
# file nodes ,for tga ,filter off ,for map ,filter config minmap


class cllRLConfig(object):
    def __init__(self):
        print ''

    # Auto Create
    def cllRLAutoCreate(self, render2D = 1 , PFX = 1 ):
        print ('=================================================================')
        print '====================!!!Start AutoRenderLayer!!!===================='
        
        # Back To MasterLayer
        mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')
        # clean unknown nodes
        self.checkDonotNodesClean()
        # File Node Config
        self.cllRLFileNodeConfig()
        # VisTT
        self.clRLVisConfig()
        # 约束处理
        from idmt.maya.py_common import sk_checkCommon
        sk_checkCommon.sk_checkTools().sk_checkBakeConstraints()
        # renderpass Create
        self.cllRLRenderPass()
        # common Setting
        self.cllRLCommonConfig()
        # mr Setting
        self.mentalRayProductionLevel()
        
        
        # Step 1：RGB,BW,SPEC,RIM
        
        # RGB
        self.cllRLRGBCreate()
        # BW
        self.cllRLBWCreate()
        # SPEC
        self.cllRLSPECCreate()        
        # RIM
        self.cllRLRIMLIGHTCreate()

        # smoothSet
        self.cllRLDoSmooth()
        # Back To MasterLayer
        mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')
        # Unrender MasterLayer
        mel.eval(r'renderLayerEditorRenderable RenderLayerTab "defaultRenderLayer" "0";')
        # mc.setAttr
        # common Setting
        self.cllRLCommonConfig()
        # save
        self.cllRLSave('auto_01')
        
        # Step 2：Light,ZDepth,BG_RGB
        if mc.ls('RGB'):
            mc.delete('RGB')
        if mc.ls('BW'):
            mc.delete('BW')
        if mc.ls('SPEC'):
            mc.delete('SPEC')
        if mc.ls('RIMLIGHT'):
            mc.delete('RIMLIGHT')
        
        # Light
        self.cllRLLIGHTCreate()
        # ZDepth
        self.cllRLZDEPTHCreate()
        # BG_RGB
        self.cllRLBGRGBCreate()
        
        # smoothSet
        self.cllRLDoSmooth()
        # Back To MasterLayer
        mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')
        # Unrender MasterLayer
        mel.eval(r'renderLayerEditorRenderable RenderLayerTab "defaultRenderLayer" "0";')
        # common Setting
        self.cllRLCommonConfig()
        # save
        self.cllRLSave('auto_02')
        
        # RENDER_2D
        self.cllRLSpeficCreate('RENDER_2D', '2D')
        # PFX
        self.cllRLSpeficCreate('PFX', 'PFX')
        
        print '=======================!!!All Done!!!======================='
        print ('===========================================================')
    
    # Create Single Render Layer
    def cllRLSpeficCreate(self, renderLayer , mode=''):
        print (unicode('===============!!!Start 【%s】!!!===============' % (str(renderLayer)), 'utf8'))
        print 'Working...'

        # Back To MasterLayer
        mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')
        # Clean Unknwon Nodes
        self.checkDonotNodesClean()
        # File Node Config
        self.cllRLFileNodeConfig()
        # 约束处理
        from idmt.maya.py_common import sk_checkCommon
        sk_checkCommon.sk_checkTools().sk_checkBakeConstraints()
        # renderpass Create
        self.cllRLRenderPass()
        # common Setting
        self.cllRLCommonConfig()
        # mr Setting
        self.mentalRayProductionLevel()
        # 指定层
        # RGB
        if renderLayer == 'RGB':
            try:
                mc.delete('RGB')
            except:
                pass
            self.cllRLRGBCreate()
        # BW
        if renderLayer == 'BW':
            try:
                mc.delete('BW')
            except:
                pass
            self.cllRLBWCreate()
        # SPE
        if renderLayer == 'SPEC':
            try:
                mc.delete('SPEC')
            except:
                pass
            self.cllRLSPECCreate()
        # RIM
        if renderLayer == 'RIMLIGHT':
            try:
                mc.delete('RIMLIGHT')
            except:
                pass
            self.cllRLRIMLIGHTCreate()
        # Light
        if renderLayer == 'LIGHT':
            try:
                mc.delete('LIGHT')
            except:
                pass
            self.cllRLLIGHTCreate()
        # ZDepth
        if renderLayer == 'ZDEPTH':
            try:
                mc.delete('ZDEPTH')
            except:
                pass
            self.cllRLZDEPTHCreate()

        # BG_RGB
        if renderLayer == 'BG_RGB':
            try:
                mc.delete('BG_RGB')
            except:
                pass
            self.cllRLBGRGBCreate()
        # RENDER_2D
        if renderLayer == 'RENDER_2D':
            try:
                mc.delete('RENDER_2D')
            except:
                pass
            #sk_checkCommon.sk_checkTools().checkCleanRenderLayers()
            self.cllRLBGRENDER2DCreate()
        # PFX
        if renderLayer == 'PFX':
            try:
                mc.delete('PFX')
            except:
                pass
            #sk_checkCommon.sk_checkTools().checkCleanRenderLayers()
            self.cllRLBGPFXCreate()
        # smoothSet
        self.cllRLDoSmooth()
        # Back To MasterLayer
        mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')
        # UnRender MasterLayer
        mel.eval(r'renderLayerEditorRenderable RenderLayerTab "defaultRenderLayer" "0";')
        # common Setting
        self.cllRLCommonConfig()
        
        if mode:
            self.cllRLSave(mode)
        
        print (unicode('===============!!!Done  【%s】!!!===============' % (str('renderLayer')), 'utf8'))
        print '\n'
       
    # getShotInfo
    def checkShotInfo(self):
        temp = (mc.file(query=1, exn=1)).split('/')
        info = []
        if '_' in temp[len(temp) - 1]:
            info = temp[len(temp) - 1].split('_')
        else:
            mc.warning(unicode('========================[File Name Wrong]========================', 'utf8'))
        return info    
    
    # delete unknown nodes
    def checkDonotNodesClean(self):
        # 清理未知节点
        unknownNodes = mc.ls(type='unknown')
        if unknownNodes:
            for node in unknownNodes:
                mc.lockNode(node, l=0)
                mc.delete(node)
        # 清理海龟节点
        turtleNodes = mc.ls(type='ilrBakeLayer')
        for node in turtleNodes:
            mc.lockNode(node, l=0)
            mc.delete(node)
       
    # Save File
    def cllRLSave(self, mode):
        print (unicode('===============!!!Start 【%s】!!!===============' % (str('Save')), 'utf8'))
        print 'Working...'
        shotInfo = self.checkShotInfo()
        pathLocal = ('D:/Info_Temp/renderLayerFile/' + shotInfo[0] + '/' + shotInfo[1] + '/' + shotInfo[2] + '/')
        mc.sysFile(pathLocal, makeDir=True)
        fileName = pathLocal + shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2]
        if mode == 'auto_01':
            fileType = '_l4AllLayer_c001.ma'
        if mode == 'auto_02':
            fileType = '_l3AllLayer_c001.ma'
        if mode == '2D':
            fileType = '_l1Render2D_c001.ma'
        if mode == 'PFX':
            fileType = '_l1PFX_c001.ma'
        fileName = fileName + fileType
        mc.file(rename=fileName)
        mc.file(save=1)
        print (unicode('===============!!!Done  【%s】!!!===============' % (str('Save')), 'utf8'))
        print '\n'
        
    # Import Camera
    def cllRLCamImport(self):
        camGrp = mc.ls('CAM_GRP')
        if camGrp:
            mc.delete(camGrp)
        
        
    # Create renderPass
    def cllRLRenderPass(self):
        print (unicode('===============!!!Start 【%s】!!!===============' % (str('RenderPass')), 'utf8'))
        print 'Working...'
        
        shotInfo = self.checkShotInfo()
        prefixName = shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2]
        
        # 创建idPass1
        ex_idPass1 = mc.ls((prefixName + '_idPass1'), type='renderPass')
        if ex_idPass1:
            renderPass = (prefixName + '_idPass1')
        else:
            renderPass = mc.shadingNode('renderPass', asRendering=1)
        configType = [1, 'CSTCOL', 3, 1, 0, 1, 'Illumination', 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.cllRLRenderPassConfig(renderPass, configType)
        mc.rename(renderPass, (prefixName + '_idPass1'))
        
        # 创建idPass2
        ex_idPass2 = mc.ls((prefixName + '_idPass2'), type='renderPass')
        if ex_idPass2:
            renderPass = (prefixName + '_idPass2')
        else:
            renderPass = mc.shadingNode('renderPass', asRendering=1)
        configType = [1, 'CSTCOL', 3, 1, 0, 1, 'Illumination', 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.cllRLRenderPassConfig(renderPass, configType)
        mc.rename(renderPass, (prefixName + '_idPass2'))
        
        # 创建idPass3
        ex_idPass3 = mc.ls((prefixName + '_idPass3'), type='renderPass')
        if ex_idPass3:
            renderPass = (prefixName + '_idPass3')
        else:
            renderPass = mc.shadingNode('renderPass', asRendering=1)
        configType = [1, 'CSTCOL', 3, 1, 0, 1, 'Illumination', 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.cllRLRenderPassConfig(renderPass, configType)
        mc.rename(renderPass, (prefixName + '_idPass3'))
        
        # 创建idPassChr
        ex_idPassChr = mc.ls((prefixName + '_idPassChr'), type='renderPass')
        if ex_idPassChr:
            renderPass = (prefixName + '_idPassChr')
        else:
            renderPass = mc.shadingNode('renderPass', asRendering=1)
        configType = [1, 'CSTCOL', 3, 1, 0, 1, 'Illumination', 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.cllRLRenderPassConfig(renderPass, configType)
        mc.rename(renderPass, (prefixName + '_idPassChr'))
        
        # 创建idPassChrMain
        ex_idPassChrMain = mc.ls((prefixName + '_idPassChrMain'), type='renderPass')
        if ex_idPassChrMain:
            renderPass = (prefixName + '_idPassChrMain')
        else:
            renderPass = mc.shadingNode('renderPass', asRendering=1)
        configType = [1, 'CSTCOL', 4, 1, 0, 1, 'Illumination', 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.cllRLRenderPassConfig(renderPass, configType)
        mc.rename(renderPass, (prefixName + '_idPassChrMain'))
        
        # 连接节点到renderpass
        self.renderpassConnect()
        
        print (unicode('===============!!!Done  【%s】!!!===============' % (str('RenderPass')), 'utf8'))
        print '\n'
        
    # 设置renderpass属性
    def cllRLRenderPassConfig(self, renderPass, configType):
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
        
        shotInfo = self.checkShotInfo()
        prefixName = shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2]
        
        for node in colorBufferNods:
            # 无法将通用的断开命令提前。。断开和连接操作必须连续才有效
            # 处理colorID
            if '_ColorID' in node and '_ColorID2' not in node and '_ColorID3' not in node:
                # 首先要获取当前连接的属性
                lastNode = mc.listConnections((node + '.renderPass'), s=1)
                if lastNode:
                    mc.disconnectAttr((lastNode[0] + '.message'), (node + '.renderPass'))
                mc.connectAttr((prefixName + "_idPass1.message"), (node + '.renderPass'))
            # 处理colorID2
            if '_ColorID2' in node :
                # 首先要获取当前连接的属性
                lastNode = mc.listConnections((node + '.renderPass'), s=1)
                if lastNode:
                    mc.disconnectAttr((lastNode[0] + '.message'), (node + '.renderPass'))
                mc.connectAttr((prefixName + "_idPass2.message"), (node + '.renderPass'))
            # 处理colorID3
            if '_ColorID3' in node :
                # 首先要获取当前连接的属性
                lastNode = mc.listConnections((node + '.renderPass'), s=1)
                if lastNode:
                    mc.disconnectAttr((lastNode[0] + '.message'), (node + '.renderPass'))
                mc.connectAttr((prefixName + "_idPass3.message"), (node + '.renderPass'))
            # 处理colorID_CHR
            if '_ColorID_CHR' in node:
                # 首先要获取当前连接的属性
                lastNode = mc.listConnections((node + '.renderPass'), s=1)
                if lastNode:
                    mc.disconnectAttr((lastNode[0] + '.message'), (node + '.renderPass'))
                mc.connectAttr((prefixName + "_idPassChr.message"), (node + '.renderPass'))
            if '_ColorID_ChrMain' in node:
                # 首先要获取当前连接的属性
                lastNode = mc.listConnections((node + '.renderPass'), s=1)
                if lastNode:
                    mc.disconnectAttr((lastNode[0] + '.message'), (node + '.renderPass'))
                mc.connectAttr((prefixName + "_idPassChrMain.message"), (node + '.renderPass'))
    
    # 处理texture file节点属性
    # tga filter off;map minimap and 3 modify
    def cllRLFileNodeConfig(self):
        print (unicode('===============!!!Start 【%s】!!!===============' % (str('fileNodeConfig')), 'utf8'))
        print 'Working...'
        # 处理map
        fileNodes = mc.ls(type='file')
        num = 1
        for node in fileNodes:
            path = mc.getAttr(node + '.fileTextureName')
            format = path.split('.')[-1]
            # 小写化
            format = format.lower()
            if format == 'tga':
                mc.setAttr((node + '.filterType'), 0)
            if format == 'png':
                path = path.replace('png','map')
                mc.setAttr((node + '.fileTextureName'),path,type = 'string')
            if format == 'map':
                mc.setAttr((node + '.filterType'), 1)
                mc.setAttr((node + '.miOverrideConvertToOptim'), 1)
                mc.setAttr((node + '.miUseEllipticalFilter'), 1)
                cmd = "setAttr \\\"" + node +".miConvertToOptim\\\"" + "  0";
                fullCmd = "evalDeferred -lowestPriority \"" + cmd + "\""
                mel.eval(fullCmd)
                mc.setAttr((node + '.miEllipticalMaxMinor'), 8)
                num += 1
        checkType = 'File Noeds'
        if num == len(fileNodes):  
            print (unicode('===============!!!Done  【%s】!!!===============' % (str('fileNodeConfig')), 'utf8'))
            print '\n'
        else:
            print (unicode('===============!!!Done  【%s】!!!===============' % (str('fileNodeConfig')), 'utf8'))
            print '\n'

    # 物体分类清单
    def cllRLObjectsTList(self, objType=1, objs=[]):
        # 获取root
        '''
        from idmt.maya.py_common import sk_checkCommon
        reload(sk_checkCommon)
        if objType == 1:
            rootGrps = sk_checkCommon.sk_checkTools().checkOutlinerGroup()
        else:
            rootGrps = objs
        '''
        rootGrps = []
        if mc.ls('CHR_GRP'):
            rootGrps  = rootGrps + mc.listRelatives('CHR_GRP',c=1)
        if mc.ls('PRP_GRP'):
            rootGrps  = rootGrps + mc.listRelatives('PRP_GRP',c=1)
        if mc.ls('SET_GRP'):
            rootGrps  = rootGrps + mc.listRelatives('SET_GRP',c=1)
        if mc.ls('VFX_GRP'):
            rootGrps  = rootGrps + mc.listRelatives('VFX_GRP',c=1)
        
        refCHR = []
        refPROP = []
        refSET = []
        refENV = []
        refSKY = []
        refCalimero = []
        refVisTT = []
        for grp in rootGrps:
            # 剔除非ref
            isRef = mc.referenceQuery(grp, isNodeReferenced=True)
            if isRef:
                # 获取refPath
                refPath = mc.referenceQuery(grp, filename=True)
                refPath = refPath.lower()
                # 角色
                if '/characters/' in refPath:
                    refCHR.append(grp)
                    # Calimero
                    if 'cali' in refPath :
                        refCalimero.append(grp)
                    if 'cali' in refPath or 'pris' in refPath or 'vale' in refPath or 'pier' in refPath:
                        refVisTT.append(grp)
                # 道具
                if '/props/' in refPath:
                    refPROP.append(grp)
                # 其他类，下面细化
                if  '/sets/' in refPath:
                    # Set
                    setKeys = [ '_int',  '_ext']
                    configNum = 0
                    for key in setKeys:
                        if key in refPath:
                            refSET.append(grp)
                        else:
                            configNum += 1
                    # Env
                    if configNum == 2:
                        refENV.append(grp)
        result = []
        result.append(refCHR)
        result.append(refPROP)
        result.append(refSET)
        result.append(refENV)
        result.append(refSKY)
        result.append(refCalimero)
        result.append(refVisTT)
        return result
    
    # 渲染标准设置
    def cllRLCommonConfig(self):
        print (unicode('===============!!!Start 【%s】!!!===============' % (str('标准设置')), 'utf8'))
        print 'Working...'
        
        # Camera
        #from idmt.maya.py_common import sk_hbExceptCam
        #reload(sk_hbExceptCam)
        #sk_hbExceptCam.sk_hbExceptCam().camServerReference()   
        
        shotInfo = self.checkShotInfo()
        
        # camera renderer
        cameras = mc.ls(type = 'camera')
        renderCam = 'CAM:' + shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2] + '_bkShape'
        if mc.ls(renderCam):
            for cam in cameras:
                if cam != renderCam:
                    mc.setAttr((cam + '.renderable'),0)
                else:
                    mc.setAttr((cam + '.renderable'),1)
        else:
            for cam in cameras:
                if 'shShape' not in cam:
                    mc.setAttr((cam + '.renderable'),0)
                else:
                    mc.setAttr((cam + '.renderable'),1)
                    
        # 开启窗口，创建各种UI
        mel.eval('unifiedRenderGlobalsWindow')
        
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
        
        # FPS制式设置
        mc.currentUnit(time='pal')
        # 渲染范围设置
        mc.setAttr('defaultRenderGlobals.startFrame', 1)  
        mc.setAttr('defaultRenderGlobals.endFrame', 20)  

        # 输出格式设置
        mc.setAttr('defaultRenderGlobals.imageFormat', 7) 
        # 格式命名
        mc.optionMenuGrp('extMenu', e=1, select=1)
        mel.eval('changeMayaSoftwareFileNameFormat;')
        mc.optionMenuGrp('extMenu', e=1, select=3)
        mel.eval('changeMayaSoftwareFileNameFormat;')
        
        # 关闭默认灯光
        mc.setAttr('defaultRenderGlobals.enableDefaultLight',0)

        # mel.eval("prefWndUnitsChanged \"time\";")

        print (unicode('===============!!!Done  【%s】!!!===============' % (str('标准设置')), 'utf8'))
        print '\n'
        
    # mr 产品级设置    
    def mentalRayProductionLevel(self):
        print (unicode('===============!!!Start 【%s】!!!===============' % (str('MR设置')), 'utf8'))
        print 'Working...'
        
        mc.setAttr('defaultRenderGlobals.imageFormat', 7)   
        try:
            mel.eval('loadPlugin "Mayatomr"')
        except:
            pass
        mc.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')
        # 创建UI
        mel.eval('mentalrayUI ""')
        # 读取之前创建的production_preset
        mel.eval('nodePreset -load "miDefaultOptions" "production_mi"')
            
        mc.setAttr("miDefaultOptions.minSamples",0)
        mc.setAttr("miDefaultOptions.maxSamples",2)
        mc.setAttr("miDefaultOptions.contrastR",0.1)
        mc.setAttr("miDefaultOptions.contrastG",0.1)
        mc.setAttr("miDefaultOptions.contrastB",0.1)
        mc.setAttr("miDefaultOptions.contrastA",0.1)
        mc.setAttr("miDefaultOptions.filter",2)
        mc.setAttr("miDefaultOptions.filterWidth",1)
        mc.setAttr("miDefaultOptions.filterHeight",1)
        mc.setAttr("miDefaultOptions.jitter",1)
        mc.setAttr("miDefaultOptions.rayTracing",1)
        mc.setAttr("miDefaultOptions.maxReflectionRays",0)
        mc.setAttr("miDefaultOptions.maxRefractionRays",0)
        mc.setAttr("miDefaultOptions.maxRayDepth",0)
        mc.setAttr("miDefaultOptions.maxShadowRayDepth",2)
        mc.setAttr("miDefaultOptions.maxReflectionBlur",1)
        mc.setAttr("miDefaultOptions.maxRefractionBlur",1)
        
        # 默认image format
        if mc.optionMenuGrp('imageMenuMentalRay', exists=1):
            mc.optionMenuGrp('imageMenuMentalRay', e=1, sl=13)
            mel.eval('changeMentalRayImageFormat')
        
        print (unicode('===============!!!Done  【%s】!!!===============' % (str('MR设置')), 'utf8'))
        print '\n'

    # 获取所有SG节点
    def cllRLSGNodesGet(self):
        SGNodes = mc.ls(type='shadingEngine')
        SGNodes.remove('initialParticleSE')
        SGNodes.remove('initialShadingGroup')
        # SG分类
        refSGCHR = []
        refSGPROP = []
        refSGSET = []
        refSGENV = []
        refSGSKY = []
        refSGCalimero = []
        # 判断分类
        # 根据连接的物体的参考进行判断
        for SGNode in SGNodes:
            if '_cam_' not in SGNode and '_CAM_' not in SGNode:
                listMeshTransform = mc.listConnections(SGNode, type='mesh')
                if listMeshTransform:
                    # 只选一个进行处理即可
                    # 取参考路径
                    # 获取refPath
                    refPath = mc.referenceQuery(listMeshTransform[0], filename=True)
                    # 角色
                    if '/CHARACTERS/' in refPath or '/characters/' in refPath:
                        refSGCHR.append(SGNode)
                        # Calimero
                        # if '/CHR_CALI/' in refPath or '/chr_cali/' in refPath:
                        if 'CALI' in refPath or 'cali' in refPath :
                            refSGCalimero.append(SGNode)
                    # 道具
                    if '/PROPS/' in refPath or '/props/' in refPath:
                        refSGPROP.append(SGNode)
                    # 其他类，下面细化
                    if '/SETS/' in refPath or '/sets/' in refPath:
                        # Set
                        setKeys = ['_Int', '_int', '_Ext', '_ext']
                        configNum = 0
                        for key in setKeys:
                            if key in refPath:
                                refSGSET.append(SGNode)
                            else:
                                configNum += 1
                        # Env
                        if configNum == 4:
                            refSGENV.append(SGNode)

        result = []
        result.append(refSGCHR)
        result.append(refSGPROP)
        result.append(refSGSET)
        result.append(refSGENV)
        result.append(refSGSKY)
        result.append(refSGCalimero)
        return result
    
    # smoothSet
    def cllRLDoSmooth(self, layerType=1):
        self.smoothSetDoSmooth()
        
    # 获取smoothSet的物体
    def smoothSetGetObjects(self,level):
        tempSet = mc.ls(type='objectSet')
        objsSet = []
        objsSmooth = [] 
        for temp in tempSet:
            if ('smooth_' + str(level)) in temp or ('smooth' + str(level)) in temp:
                objsSet.append(temp)
        if objsSet:
            for objSet in objsSet:
                meshes = mc.sets(objSet, q=1)
                if meshes:
                    for mesh in meshes:
                        objsSmooth.append(mc.ls((mesh), l=1)[0])
        return objsSmooth
    
    # 处理所有smoothSet的smooth级别
    def smoothSetDoSmooth(self):
        topNodes = mc.ls(assemblies=True)
        mc.displaySmoothness(topNodes, polygonObject=3)
        # 处理smooth 0
        objs = self.smoothSetGetObjects(0)
        if objs:
            for obj in objs:
                try:
                    mc.setAttr((mc.listRelatives(obj,s=1)[0]+'.displaySmoothMesh'),2)
                except:
                    pass
                mc.setAttr((mc.listRelatives(obj,s=1)[0]+'.useSmoothPreviewForRender'),0)
                mc.setAttr((mc.listRelatives(obj,s=1)[0]+'.renderSmoothLevel'),0)
        # 处理smooth 1
        objs = self.smoothSetGetObjects(1)
        if objs:
            for obj in objs:
                try:
                    mc.setAttr((mc.listRelatives(obj,s=1)[0]+'.displaySmoothMesh'),2)
                except:
                    pass
                mc.setAttr((mc.listRelatives(obj,s=1)[0]+'.useSmoothPreviewForRender'),0)
                mc.setAttr((mc.listRelatives(obj,s=1)[0]+'.renderSmoothLevel'),1)
        # 处理smooth 2
        objs = self.smoothSetGetObjects(2)
        if objs:
            for obj in objs:
                try:
                    mc.setAttr((mc.listRelatives(obj,s=1)[0]+'.displaySmoothMesh'),2)
                except:
                    pass
                mc.setAttr((mc.listRelatives(obj,s=1)[0]+'.useSmoothPreviewForRender'),0)
                mc.setAttr((mc.listRelatives(obj,s=1)[0]+'.renderSmoothLevel'),2)
    
    # vis属性
    def clRLVisConfig(self):
        objs = self.cllRLObjectsTList()
        refVisTT = objs[6]
        for asset in refVisTT:
            controlShapes = mc.listRelatives(asset , ad=1 , type = 'nurbsCurve', f= 1)
            if controlShapes:
                for ctrlShape in controlShapes:
                    ctrl = mc.listRelatives(ctrlShape,p=1,type = 'transform',f=1)[0]
                    if mc.ls(ctrl + '.twoDline_vis'):
                        mc.setAttr((ctrl + '.twoDline_vis'),1)
    # RGB层
    # No Lights
    def cllRLRGBCreate(self):
        print (unicode('===============!!!Start 【%s】!!!===============' % (str('RGB层')), 'utf8'))
        print 'Working...'
                
        shotInfo = self.checkShotInfo()
        prefixName = shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2]
                
        # 物体
        objs = self.cllRLObjectsTList()
        refCHR = objs[0]
        refPROP = objs[1]
        refSET = objs[2]
        refENV = objs[3]
        refSKY = objs[4]
        refCalimero = objs[5]

        # 灯光
        lights = mc.ls(type='light')
        if 'IDMT_2D_KeyLight' in lights:
            lights.remove('IDMT_2D_KeyLight')
        if 'IDMT_2D_SideLight' in lights:
            lights.remove('IDMT_2D_SideLight')
        
        # 物体
        rlObjs = refCHR + refPROP + refSET + refSKY
        
        
        # 创建RenderLayer
        if (refCHR + refPROP + refSET):
            layerName = 'RGB'
            mc.createRenderLayer(rlObjs , name=layerName , noRecurse=1 , makeCurrent=1)
            
            # 隐藏灯光
            for light in lights:
                lightGrp = mc.listRelatives(light, p=1)[0]
                mc.editRenderLayerAdjustment(lightGrp + '.v')
                mc.setAttr((light + '.v'), 0)
                mc.editRenderLayerAdjustment(light + '.intensity')
                mc.setAttr((light + '.intensity'), 0)
            
            # 连接renderPass
            # 赋予idpass1
            mc.connectAttr('RGB.renderPass', (prefixName+'_idPass1.owner'))
            
            # 材质不理会
            # 设置
            # self.cllRLCommonConfig()
            
            # 特殊处理
            objs = mc.ls('*pris_*:msh_iris_L_',type = 'transform') + mc.ls('*pris_*:msh_iris_R_',type = 'transform')
            if objs:
                for obj in objs:
                    cmdInfo = "editRenderLayerAdjustment \"" + obj + '.v\"' 
                    mel.eval(cmdInfo)
                    mc.setAttr((obj+'.v'),0)
            
            # 渲染设置
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')
            mel.eval("editRenderLayerAdjustment \"defaultRenderGlobals.currentRenderer\";")
    
            # exr
            # mc.setAttr('defaultRenderGlobals.imfPluginKey', 'exr', type='string')
            # mel.eval('updateMultiCameraBufferNamingMenu;')
            mel.eval("editRenderLayerAdjustment \"defaultRenderGlobals.imageFormat\";")
            if mc.optionMenuGrp('imageMenuMentalRay', exists=1):
                # mc.optionMenuGrp('imageMenuMentalRay', e=1, sl=7)
                # mel.eval('changeMentalRayImageFormat')
                mc.optionMenuGrp('imageMenuMentalRay', e=1, sl=13)
                try:
                    mel.eval('changeMentalRayImageFormat')
                except:
                    pass
    
            # 16位zip压缩
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.editRenderLayerAdjustment('miDefaultFramebuffer.datatype')
            mc.setAttr('miDefaultFramebuffer.datatype', 16)
    
            # 格式命名
            mc.optionMenuGrp('extMenu', e=1, select=3)
            
            print (unicode('===============!!!Done  【%s】!!!===============' % (str('RGB层')), 'utf8'))
            print '\n'
        else:
            print (unicode('===============!!!None  【%s】!!!===============' % (str('RGB层')), 'utf8'))        
            print '\n'
    # BW层
    # No Lights
    def cllRLBWCreate(self):
        print (unicode('===============!!!Start 【%s】!!!===============' % (str('BW层')), 'utf8'))
        print 'Working...'
        
        shotInfo = self.checkShotInfo()
        prefixName = shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2]

        # 物体
        objs = self.cllRLObjectsTList()
        refCHR = objs[0]
        refPROP = objs[1]
        refSET = objs[2]
        refENV = objs[3]
        refSKY = objs[4]
        refCalimero = objs[5]

        # 灯光
        lights = mc.ls(type='light')
        if 'IDMT_2D_KeyLight' in lights:
            lights.remove('IDMT_2D_KeyLight')
        if 'IDMT_2D_SideLight' in lights:
            lights.remove('IDMT_2D_SideLight')

        # 物体
        rlObjs = refPROP + refSET + refENV + refSKY + lights
        
        # 创建RenderLayer
        if (refPROP + refSET + refENV + refSKY):
            layerName = 'BW'
            mc.createRenderLayer(rlObjs , name=layerName , noRecurse=1 , makeCurrent=1)
    
            # 隐藏灯光
            for light in lights:
                lightGrp = mc.listRelatives(light, p=1)[0]
                mc.editRenderLayerAdjustment(lightGrp + '.v')
                mc.setAttr((light + '.v'), 0)
                mc.editRenderLayerAdjustment(light + '.intensity')
                mc.setAttr((light + '.intensity'), 0)
            
            # 连接renderPass
            # 无
    
            # 材质
            SGnodes = self.cllRLSGNodesGet()
            refSGCHR = SGnodes[0]
            refSGPROP = SGnodes[1]
            refSGSET = SGnodes[2]
            refSGENV = SGnodes[3]
            refSGSKY = SGnodes[4]
            refSGCalimero = SGnodes[5]
            
            rlSGNodes = refSGPROP + refSGSET + refSGENV + refSGSKY
    
            # 创建备用材质组
            shaderName = 'SHD_' + 'BW'
            if mc.ls(shaderName):
                mc.delete(shaderName)
            shaderNeed = mc.shadingNode ('lambert', asShader=True, name=shaderName)   
            mc.setAttr(('%s.color') % (shaderNeed), 1, 1, 1, type="double3")
            mc.setAttr(('%s.ambientColor') % (shaderNeed), 1, 1, 1, type="double3")
    
            # 连接材质
            for SGNode in rlSGNodes:
                # 查找RGB或RGBA节点
                RGBNodeGrp = mc.listConnections(SGNode + '.surfaceShader')
                if RGBNodeGrp:
                    RGBNode = RGBNodeGrp[0]
                    needTxNode = ''
                    # 寻找BW节点
                    needTxNode = RGBNode.replace('_RGB', '_BW')
                    # RGB/RGBA提供的node
                    if mc.objExists(needTxNode):
                        node = needTxNode
                    else:
                        node = shaderNeed
                    mc.editRenderLayerAdjustment((SGNode + '.surfaceShader'))
                    mc.disconnectAttr((RGBNode + '.outColor'), (SGNode + '.surfaceShader'))
                    mc.connectAttr((node + '.outColor'), (SGNode + '.surfaceShader'))
    
            # 设置
            # self.cllRLCommonConfig()
    
            # 渲染设置
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')
            mel.eval("editRenderLayerAdjustment \"defaultRenderGlobals.currentRenderer\";")
    
            # exr
            mel.eval("editRenderLayerAdjustment \"defaultRenderGlobals.imageFormat\";")
            if mc.optionMenuGrp('imageMenuMentalRay', exists=1):
                # mc.optionMenuGrp('imageMenuMentalRay', e=1, sl=7)
                # mel.eval('changeMentalRayImageFormat')
                mc.optionMenuGrp('imageMenuMentalRay', e=1, sl=13)
                try:
                    mel.eval('changeMentalRayImageFormat')
                except:
                    pass
    
            # mc.setAttr('defaultRenderGlobals.imfPluginKey','exr',type = 'string')
            # mel.eval('updateMultiCameraBufferNamingMenu;')
            # mel.eval("editRenderLayerAdjustment \"defaultRenderGlobals.imageFormat\";")
            
            # 8位zip压缩
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.editRenderLayerAdjustment('miDefaultFramebuffer.datatype')
            mc.setAttr('miDefaultFramebuffer.datatype', 2)
    
            print (unicode('===============!!!Done  【%s】!!!===============' % (str('BW层')), 'utf8'))        
            print '\n'
        else:
            print (unicode('===============!!!None  【%s】!!!===============' % (str('BW层')), 'utf8'))        
            print '\n'
            
    # SPEC层
    # 客户灯光规则错误
    def cllRLSPECCreate(self):
        print (unicode('===============!!!Start 【%s】!!!===============' % (str('SPEC层')), 'utf8'))
        print 'Working...'
        
        shotInfo = self.checkShotInfo()
        prefixName = shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2]
        
        # 物体
        objs = self.cllRLObjectsTList()
        refCHR = objs[0]
        refPROP = objs[1]
        refSET = objs[2]
        refENV = objs[3]
        refSKY = objs[4]
        refCalimero = objs[5]

        # 灯光
        lights = mc.ls(type='light')
        if 'IDMT_2D_KeyLight' in lights:
            lights.remove('IDMT_2D_KeyLight')
        if 'IDMT_2D_SideLight' in lights:
            lights.remove('IDMT_2D_SideLight')
        
        # 物体
        rlObjs = refCHR + lights
        
        # 创建RenderLayer
        if refCHR:
            layerName = 'SPEC'
            mc.createRenderLayer(rlObjs , name=layerName , noRecurse=1 , makeCurrent=1)
                   
            # 主光开启，其他光隐藏
            for light in lights:
                if 'KEY' in light:
                    mc.editRenderLayerAdjustment(light + '.color')
                    mc.setAttr((light + '.color'), 1, 1, 1, type='double3')
                else:
                    lightGrp = mc.listRelatives(light, p=1)[0]
                    mc.editRenderLayerAdjustment(lightGrp + '.v')
                    mc.setAttr((light + '.v'), 0)
                    mc.editRenderLayerAdjustment(light + '.intensity')
                    mc.setAttr((light + '.intensity'), 0)
                # 所有灯光黑色阴影
                mc.editRenderLayerAdjustment(light + '.shadowColor')
                mc.setAttr((light + '.shadowColor'), 0, 0, 0, type='double3')
                
            # 连接renderPass
            mc.connectAttr('SPEC.renderPass', (prefixName+'_idPassChr.owner'))
            mc.connectAttr('SPEC.renderPass', (prefixName+'_idPassChrMain.owner'))
            
            # 材质
            SGnodes = self.cllRLSGNodesGet()
            refSGCHR = SGnodes[0]
            refSGPROP = SGnodes[1]
            refSGSET = SGnodes[2]
            refSGENV = SGnodes[3]
            refSGSKY = SGnodes[4]
            refSGCalimero = SGnodes[5]
            
            rlSGNodes = refSGENV
            
    
            # 设置reflect属性
            # 仅仅关闭beauty开启specular
            mel.eval("renderLayerBuiltinPreset specular SPEC")
            
            
            # 设置
            # self.cllRLCommonConfig()
    
            # 渲染设置
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')
            mel.eval("editRenderLayerAdjustment \"defaultRenderGlobals.currentRenderer\";")
    
            # exr格式
            mel.eval("editRenderLayerAdjustment \"defaultRenderGlobals.imageFormat\";")
            if mc.optionMenuGrp('imageMenuMentalRay', exists=1):
                # mc.optionMenuGrp('imageMenuMentalRay', e=1, sl=7)
                # mel.eval('changeMentalRayImageFormat')
                mc.optionMenuGrp('imageMenuMentalRay', e=1, sl=13)
                try:
                    mel.eval('changeMentalRayImageFormat')
                except:
                    pass
                
            # 8位zip压缩
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.editRenderLayerAdjustment('miDefaultFramebuffer.datatype')
            mc.setAttr('miDefaultFramebuffer.datatype', 2)
            
            print (unicode('===============!!!Done  【%s】!!!===============' % (str('SPEC层')), 'utf8'))        
            print '\n'
        else:
            print (unicode('===============!!!None  【%s】!!!===============' % (str('SPEC层')), 'utf8'))        
            print '\n'
        
    # RIMLIGHT层
    def cllRLRIMLIGHTCreate(self):
        print (unicode('===============!!!Start 【%s】!!!===============' % (str('RIMLIGHT层')), 'utf8'))
        print 'Working...'
        
        shotInfo = self.checkShotInfo()
        prefixName = shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2]
        
        # 物体
        objs = self.cllRLObjectsTList()
        refCHR = objs[0]
        refPROP = objs[1]
        refSET = objs[2]
        refENV = objs[3]
        refSKY = objs[4]
        refCalimero = objs[5]

        # 灯光
        lights = mc.ls(type='light')
        if 'IDMT_2D_KeyLight' in lights:
            lights.remove('IDMT_2D_KeyLight')
        if 'IDMT_2D_SideLight' in lights:
            lights.remove('IDMT_2D_SideLight')
        
        # 物体
        rlObjs = refCHR + lights
        
        # 创建RenderLayer
        if refCHR:
            layerName = 'RIMLIGHT'
            mc.createRenderLayer(rlObjs , name=layerName , noRecurse=1 , makeCurrent=1)
            
            # 主光开启强度1颜色1 1 1，其他光隐藏
            for light in lights:
                # 判断是否ENV的灯光
                #rootGrp = '|' + mc.ls(light, l=1)[0].split('|')[1]
                if '_KEY' in light:
                    mc.editRenderLayerAdjustment(light + '.color')
                    mc.setAttr((light + '.color'), 1, 1, 1, type='double3')
                else:
                    mc.editRenderLayerAdjustment(light + '.intensity')
                    mc.setAttr((light + '.intensity'), 0)
                    mc.editRenderLayerAdjustment(light + '.v')
                    mc.setAttr((light + '.v'), 0)
                # 所有灯光黑色阴影
                mc.editRenderLayerAdjustment(light + '.shadowColor')
                mc.setAttr((light + '.shadowColor'), 0, 0, 0, type='double3')
            
            # 连接renderPass
            
            # 材质
            SGnodes = self.cllRLSGNodesGet()
            refSGCHR = SGnodes[0]
            refSGPROP = SGnodes[1]
            refSGSET = SGnodes[2]
            refSGENV = SGnodes[3]
            refSGSKY = SGnodes[4]
            refSGCalimero = SGnodes[5]
            
            rlSGNodes = refSGCHR
            
            # 创建备用材质组
            shaderName = 'SHD_' + 'BLACK'
            if mc.ls(shaderName):
                mc.delete(shaderName)
            shaderNeed = mc.shadingNode ('lambert', asShader=True, name=shaderName)   
            mc.setAttr(('%s.color') % (shaderNeed), 0, 0, 0, type="double3")
    
            # 连接材质
            for SGNode in rlSGNodes:
                # 查找RGB或RGBA节点
                RGBNodeGrp = mc.listConnections(SGNode + '.surfaceShader')
                if RGBNodeGrp:
                    RGBNode = RGBNodeGrp[0]
                    needTxNode = ''
                    '''
                    # 寻找内部节点
                    listTxNodes = mc.listConnections(RGBNode)
                    for nd in listTxNodes:
                        if "_RIM" in nd:
                            needTxNode = nd
                            break
                    '''
                    # 寻找RIMLIGHT节点
                    if '_RGBA' not in RGBNode:
                        needTxNode = RGBNode.replace('_RGB', '_RIM')
                    else:
                        needTxNode = RGBNode.replace('_RGBA', '_RIM')
                    # RGB/RGBA提供的node
                    if mc.objExists(needTxNode):
                        node = needTxNode
                    else:
                        node = shaderNeed
                    mc.editRenderLayerAdjustment((SGNode + '.surfaceShader'))
                    mc.disconnectAttr((RGBNode + '.outColor'), (SGNode + '.surfaceShader'))
                    mc.connectAttr((node + '.outColor'), (SGNode + '.surfaceShader'))
                                  
            # 设置
            # self.cllRLCommonConfig()
            
            # 渲染设置
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')
            mel.eval("editRenderLayerAdjustment \"defaultRenderGlobals.currentRenderer\";")
                    
            # exr格式
            mel.eval("editRenderLayerAdjustment \"defaultRenderGlobals.imageFormat\";")
            if mc.optionMenuGrp('imageMenuMentalRay', exists=1):
                # mc.optionMenuGrp('imageMenuMentalRay', e=1, sl=7)
                # mel.eval('changeMentalRayImageFormat')
                mc.optionMenuGrp('imageMenuMentalRay', e=1, sl=13)
                try:
                    mel.eval('changeMentalRayImageFormat')
                except:
                    pass
               
            # 8位zip压缩
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.editRenderLayerAdjustment('miDefaultFramebuffer.datatype')
            mc.setAttr('miDefaultFramebuffer.datatype', 2)
    
            print (unicode('===============!!!Done  【%s】!!!===============' % (str('RIMLIGHT层')), 'utf8'))        
            print '\n'
        else:
            print (unicode('===============!!!None  【%s】!!!===============' % (str('RIMLIGHT层')), 'utf8'))        
            print '\n'

    # LIGHT层
    # 客户灯光规则错误
    # 另外可能从SHD_LIGHT提供
    def cllRLLIGHTCreate(self):
        print (unicode('===============!!!Start 【%s】!!!===============' % (str('LIGHT层')), 'utf8'))
        print 'Working...'
        
        shotInfo = self.checkShotInfo()
        prefixName = shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2]
        
        # 物体
        objs = self.cllRLObjectsTList()
        refCHR = objs[0]
        refPROP = objs[1]
        refSET = objs[2]
        refENV = objs[3]
        refSKY = objs[4]
        refCalimero = objs[5]

        # 灯光
        lights = mc.ls(type='light')
        if 'IDMT_2D_KeyLight' in lights:
            lights.remove('IDMT_2D_KeyLight')
        if 'IDMT_2D_SideLight' in lights:
            lights.remove('IDMT_2D_SideLight')
        
        # 物体
        rlObjs = refCHR + refPROP + refSET + refSKY + lights
        
        # 创建RenderLayer
        if (refCHR + refPROP + refSET + refSKY):
            layerName = 'LIGHT'
            mc.createRenderLayer(rlObjs , name=layerName , noRecurse=1 , makeCurrent=1)
            
            # 连接renderPass
            mc.connectAttr('LIGHT.renderPass', (prefixName+'_idPass3.owner'))
            
            
            # KEY光红色，BRANCH蓝色，EXTRA绿色
            for light in lights:
                # 判断是否ENV的灯光
                #rootGrp = '|' + mc.ls(light, l=1)[0].split('|')[1]
                #if rootGrp in refENV:
                if '_KEY' in light:
                    mc.editRenderLayerAdjustment(light + '.color')
                    mc.setAttr((light + '.color'), 1, 0, 0, type='double3')
                if '_BOUNCE' in light:
                    mc.editRenderLayerAdjustment(light + '.color')
                    mc.setAttr((light + '.color'), 0, 0, 1, type='double3')
                if '_EXTRA' in light:
                    mc.editRenderLayerAdjustment(light + '.color')
                    mc.setAttr((light + '.color'), 0, 1, 0, type='double3')
                if '_ONLY' in light:
                    if '_KEY' not in light and '_BOUNCE' not in light and '_EXTRA' not in light:
                        mc.editRenderLayerAdjustment(light + '.intensity')
                        mc.setAttr((light + '.intensity'), 0)
                        mc.editRenderLayerAdjustment(light + '.v')
                        mc.setAttr((light + '.v'), 0)
                # 所有灯光黑色阴影
                mc.editRenderLayerAdjustment(light + '.shadowColor')
                mc.setAttr((light + '.shadowColor'), 0, 0, 0, type='double3')
    
            # 材质
            SGnodes = self.cllRLSGNodesGet()
            refSGCHR = SGnodes[0]
            refSGPROP = SGnodes[1]
            refSGSET = SGnodes[2]
            refSGENV = SGnodes[3]
            refSGSKY = SGnodes[4]
            refSGCalimero = SGnodes[5]
            
            rlSGNodes = refSGCHR + refSGPROP + refSGSET + refSGSKY
            
            # 创建备用材质组
            shaderName = 'SHD_' + 'LIGHT'
            if mc.ls(shaderName):
                mc.delete(shaderName)
            shaderNeed = mc.shadingNode ('lambert', asShader=True, name=shaderName)   
            mc.setAttr(('%s.color') % (shaderNeed), 1, 1, 1, type="double3")
            # 连接材质
            for SGNode in rlSGNodes:
                # 查找RGB或RGBA节点
                RGBNodeGrp = mc.listConnections(SGNode + '.surfaceShader')
                if RGBNodeGrp:
                    RGBNode = RGBNodeGrp[0]
                    needTxNode = ''
                    # 寻找LIGHT节点
                    if '_RGBA' not in RGBNode:
                        needTxNode = RGBNode.replace('_RGB', '_LIGHT')
                    else:
                        needTxNode = RGBNode.replace('_RGBA', '_LIGHT')
                    # RGB/RGBA提供的node
                    if mc.objExists(needTxNode) and 'LIGHT' in needTxNode:
                        node = needTxNode
                    else:
                        node = shaderNeed
                    mc.editRenderLayerAdjustment((SGNode + '.surfaceShader'))
                    mc.disconnectAttr((RGBNode + '.outColor'), (SGNode + '.surfaceShader'))
                    mc.connectAttr((node + '.outColor'), (SGNode + '.surfaceShader'), f=1)
            # 设置
            # self.cllRLCommonConfig()
            # 渲染设置
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')
            mel.eval("editRenderLayerAdjustment \"defaultRenderGlobals.currentRenderer\";")
            
            # exr格式
            mel.eval("editRenderLayerAdjustment \"defaultRenderGlobals.imageFormat\";")
            if mc.optionMenuGrp('imageMenuMentalRay', exists=1):
                # mc.optionMenuGrp('imageMenuMentalRay', e=1, sl=7)
                # mel.eval('changeMentalRayImageFormat')
                mc.optionMenuGrp('imageMenuMentalRay', e=1, sl=13)
                try:
                    mel.eval('changeMentalRayImageFormat')
                except:
                    pass
                
            # 16位zip压缩
            # 需要处理
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.editRenderLayerAdjustment('miDefaultFramebuffer.datatype')
            mc.setAttr('miDefaultFramebuffer.datatype', 16)
    
            print (unicode('===============!!!Done  【%s】!!!===============' % (str('LIGHT层')), 'utf8'))        
            print '\n'
        else:
            print (unicode('===============!!!None  【%s】!!!===============' % (str('LIGHT层')), 'utf8'))        
            print '\n'
            
    # ZDEPTH层
    # No Lights
    def cllRLZDEPTHCreate(self, distance=14000):
        print (unicode('===============!!!Start 【%s】!!!===============' % (str('ZDEPTH层')), 'utf8'))
        print 'Working...'
        
        
        # 物体
        objs = self.cllRLObjectsTList()
        refCHR = objs[0]
        refPROP = objs[1]
        refSET = objs[2]
        refENV = objs[3]
        refSKY = objs[4]
        refCalimero = objs[5]

        # 灯光
        lights = mc.ls(type='light')
        if 'IDMT_2D_KeyLight' in lights:
            lights.remove('IDMT_2D_KeyLight')
        if 'IDMT_2D_SideLight' in lights:
            lights.remove('IDMT_2D_SideLight')
        
        # 物体
        rlObjs = refCHR + refPROP + refSET + refENV + refSKY
        
        # 创建RenderLayer
        if (refCHR + refPROP + refSET + refENV):
            layerName = 'ZDEPTH'
            mc.createRenderLayer(rlObjs , name=layerName , noRecurse=1 , makeCurrent=1)
            
            # 隐藏灯光
            for light in lights:
                lightGrp = mc.listRelatives(light, p=1)[0]
                mc.editRenderLayerAdjustment(lightGrp + '.v')
                mc.setAttr((light + '.v'), 0)
                mc.editRenderLayerAdjustment(light + '.intensity')
                mc.setAttr((light + '.intensity'), 0)
    
            # 连接renderPass
            
            # 材质
            SGnodes = self.cllRLSGNodesGet()
            refSGCHR = SGnodes[0]
            refSGPROP = SGnodes[1]
            refSGSET = SGnodes[2]
            refSGENV = SGnodes[3]
            refSGSKY = SGnodes[4]
            refSGCalimero = SGnodes[5]
            
            rlSGNodes = refSGCHR + refSGPROP + refSGSET + refSGENV + refSGSKY
    
            # 创建备用材质组
            shaderName = 'SHD_' + 'ZDEPTH'
            if mc.ls(shaderName):
                mc.delete(shaderName)
            if mc.ls('%s_sampleInfo' % (shaderName)):
                mc.delete('%s_sampleInfo' % (shaderName))
            if mc.ls('SHD_ZDEPTH_setRangeZ'):
                mc.delete('SHD_ZDEPTH_setRangeZ')
            if mc.ls('SHD_ZDEPTH_multDivZ'):
                mc.delete('SHD_ZDEPTH_multDivZ')
            if mc.ls('SHD_ZDEPTH_sampInfoZ'):
                mc.delete('SHD_ZDEPTH_sampInfoZ')  
            if mc.ls('SHD_Depth_SG'):
                mc.delete('SHD_Depth_SG')  
            depthShader = mc.shadingNode ('lambert', asShader=True, name=shaderName)
            mc.setAttr((depthShader + '.ambientColor'),1,1,1,type = 'double3')
            setRangeNode = mc.shadingNode ('setRange', asUtility=True, name='SHD_ZDEPTH_setRangeZ')
            mc.setAttr((setRangeNode+'.minX'),1)
            multiplyDivideNode = mc.shadingNode ('multiplyDivide', asUtility=True, name='SHD_ZDEPTH_multDivZ')
            mc.setAttr((multiplyDivideNode+'.input2X'),-1)
            samplerInfoNode = mc.shadingNode ('samplerInfo', asUtility=True, name='SHD_ZDEPTH_sampInfoZ')
            mc.addAttr(samplerInfoNode, longName='NearClipCalimero',nn='Near Clip Calimero', attributeType='float', defaultValue=0.1)
            mc.addAttr(samplerInfoNode, longName='FarClipCalimero',nn='Far Clip Calimero', attributeType='float', defaultValue= distance )
            depthSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name='SHD_Depth_SG')
            mc.connectAttr(('%s.%s') % (depthShader , 'outColor') , ('%s.%s') % (depthSG , 'surfaceShader'), f=True)
            shaderNeed = depthShader
            # 连接
            mc.connectAttr(('%s.%s') % (setRangeNode , 'outValueX') , ('%s.%s') % (depthShader , 'colorR'), f=True)
            mc.connectAttr(('%s.%s') % (setRangeNode , 'outValueX') , ('%s.%s') % (depthShader , 'colorG'), f=True)
            mc.connectAttr(('%s.%s') % (setRangeNode , 'outValueX') , ('%s.%s') % (depthShader , 'colorB'), f=True)
            mc.connectAttr(('%s.%s') % (samplerInfoNode , 'NearClipCalimero') , ('%s.%s') % (setRangeNode , 'oldMinX'), f=True)
            mc.connectAttr(('%s.%s') % (samplerInfoNode , 'FarClipCalimero') , ('%s.%s') % (setRangeNode , 'oldMaxX'), f=True)
            mc.connectAttr(('%s.%s') % (samplerInfoNode , 'pointCameraZ') , ('%s.%s') % (multiplyDivideNode , 'input1X'), f=True)
            mc.connectAttr(('%s.%s') % (multiplyDivideNode , 'outputX') , ('%s.%s') % (setRangeNode , 'valueX'), f=True)
    
            # 连接材质
            for SGNode in rlSGNodes:
                # 查找RGB或RGBA节点
                RGBNodeGrp = mc.listConnections(SGNode + '.surfaceShader')
                if RGBNodeGrp:
                    RGBNode = RGBNodeGrp[0]
                    needTxNode = ''
                    # 寻找ZDEPTH节点
                    if '_RGBA' not in RGBNode:
                        needTxNode = RGBNode.replace('_RGB', '_ZDEPTH')
                    else:
                        needTxNode = RGBNode.replace('_RGBA', '_ZDEPTH')
                    # RGB/RGBA提供的node
                    if mc.objExists(needTxNode):
                        node = needTxNode
                    else:
                        node = shaderNeed
                    mc.editRenderLayerAdjustment((SGNode + '.surfaceShader'))
                    mc.disconnectAttr((RGBNode + '.outColor'), (SGNode + '.surfaceShader'))
                    mc.connectAttr((node + '.outColor'), (SGNode + '.surfaceShader'))
    
            # 设置
            # self.cllRLCommonConfig()
    
            # sampInfoZ
            sampleInfoZ = mc.ls('*_sampInfoZ',type = 'samplerInfo' ) + mc.ls('*:*_sampInfoZ',type = 'samplerInfo' )
            if sampleInfoZ:
                for sampleNode in sampleInfoZ:
                    mc.setAttr((sampleNode + '.NearClipCalimero'),0.1)
                    mc.setAttr((sampleNode + '.FarClipCalimero'),distance)
    
            # 渲染设置
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')
            mel.eval("editRenderLayerAdjustment \"defaultRenderGlobals.currentRenderer\";")
            
            # exr格式
            mel.eval("editRenderLayerAdjustment \"defaultRenderGlobals.imageFormat\";")
            if mc.optionMenuGrp('imageMenuMentalRay', exists=1):
                # mc.optionMenuGrp('imageMenuMentalRay', e=1, sl=7)
                # mel.eval('changeMentalRayImageFormat')
                mc.optionMenuGrp('imageMenuMentalRay', e=1, sl=13)
                try:
                    mel.eval('changeMentalRayImageFormat')
                except:
                    pass
                
            # 32位zip压缩
            # 需要处理
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.editRenderLayerAdjustment('miDefaultFramebuffer.datatype')
            mc.setAttr('miDefaultFramebuffer.datatype', 5)
    
            print (unicode('===============!!!Done  【%s】!!!===============' % (str('ZDEPTH层')), 'utf8'))        
            print '\n'
        else:
            print (unicode('===============!!!None  【%s】!!!===============' % (str('ZDEPTH层')), 'utf8'))        
            print '\n'

    # BG_RGB层
    def cllRLBGRGBCreate(self):
        print (unicode('===============!!!Start 【%s】!!!===============' % (str('BG_RGB')), 'utf8'))
        print 'Working...'
        
        shotInfo = self.checkShotInfo()
        prefixName = shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2]
        
        # 物体
        objs = self.cllRLObjectsTList()
        refCHR = objs[0]
        refPROP = objs[1]
        refSET = objs[2]
        refENV = objs[3]
        refSKY = objs[4]
        refCalimero = objs[5]

        # 灯光
        lights = mc.ls(type='light')
        if 'IDMT_2D_KeyLight' in lights:
            lights.remove('IDMT_2D_KeyLight')
        if 'IDMT_2D_SideLight' in lights:
            lights.remove('IDMT_2D_SideLight')
        
        # 物体
        rlObjs = refENV + lights
        
        if refENV:
            
            # 创建RenderLayer
            layerName = 'BG_RGB'
            mc.createRenderLayer(rlObjs , name=layerName , noRecurse=1 , makeCurrent=1)
            
            # 隐藏灯光
            for light in lights:
                lightGrp = mc.listRelatives(light, p=1)[0]
                mc.editRenderLayerAdjustment(light + '.intensity')
                mc.setAttr((light + '.intensity'), 0)
                mc.editRenderLayerAdjustment(lightGrp + '.v')
                mc.setAttr((light + '.v'), 0)
            
            # 连接renderPass
            mc.connectAttr('BG_RGB.renderPass', (prefixName+'_idPass2.owner'))
            
            # 设置
            # self.cllRLCommonConfig()
            
            # 渲染设置
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')
            mel.eval("editRenderLayerAdjustment \"defaultRenderGlobals.currentRenderer\";")        
    
            # exr格式
            mel.eval("editRenderLayerAdjustment \"defaultRenderGlobals.imageFormat\";")
            if mc.optionMenuGrp('imageMenuMentalRay', exists=1):
                # mc.optionMenuGrp('imageMenuMentalRay', e=1, sl=7)
                # mel.eval('changeMentalRayImageFormat')
                mc.optionMenuGrp('imageMenuMentalRay', e=1, sl=13)
                try:
                    mel.eval('changeMentalRayImageFormat')
                except:
                    pass
    
            # 16位zip压缩
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.editRenderLayerAdjustment('miDefaultFramebuffer.datatype')
            mc.setAttr('miDefaultFramebuffer.datatype', 16)
    
            print (unicode('===============!!!Done  【%s】!!!===============' % (str('BG_RGB层')), 'utf8'))        
            print '\n'
        else:
            print (unicode('===============!!!None  【%s】!!!===============' % (str('BG_RGB层')), 'utf8'))        
            print '\n'   
        
        
    # RENDER2D层
    def cllRLBGRENDER2DCreate(self):
        print (unicode('===============!!!Start 【%s】!!!===============' % (str('RENDER_2D层')), 'utf8'))
        print 'Working...'
        
        # 物体
        # 仅仅ENV，不接受阴影
        objs = self.cllRLObjectsTList()
        refCHR = objs[0]
        refPROP = objs[1]
        refSET = objs[2]
        refENV = objs[3]
        refSKY = objs[4]
        refCalimero = objs[5]

        # 灯光
        lights = mc.ls(type='light')

        # CreateLight
        # 主光
        if mc.ls('IDMT_2D_KeyLight'):
            mc.delete('IDMT_2D_KeyLight')
        if mc.ls('IDMT_2D_SideLight'):
            mc.delete('IDMT_2D_SideLight')
        keyLight = mc.directionalLight(name='IDMT_2D_KeyLight', rotation=(24, 36, 11), intensity=1)
        mc.setAttr((keyLight + '.color'), 1, 1, 1, type='double3')
        mc.setAttr((keyLight + '.useDepthMapShadows'), 0)
        mc.setAttr((keyLight + '.useRayTraceShadows'), 1)
        mc.setAttr((keyLight + '.lightAngle'), 0)
        mc.setAttr((keyLight + '.shadowRays'), 1)
        mc.setAttr((keyLight + '.rayDepthLimit'), 1)
        # 辅光
        sideLight = mc.directionalLight(name='IDMT_2D_SideLight', rotation=(90, 0, 0), intensity=0.5)
        mc.setAttr((sideLight + '.color'), 1, 1, 1, type='double3')
        mc.setAttr((sideLight + '.useDepthMapShadows'), 0)
        mc.setAttr((sideLight + '.useRayTraceShadows'), 0)
        # 重提灯光
        # lights = []
        lights.append(keyLight)
        lights.append(sideLight)

        # 物体
        rlObjs = refENV + lights
        
        if refENV:
            # 创建RenderLayer
            layerName = 'RENDER_2D'
            mc.createRenderLayer(rlObjs , name=layerName , noRecurse=1 , makeCurrent=1)
    
            # 处理ENV的mesh不接受阴影
            for grp in refENV:
                allChildren = mc.listRelatives(grp, ad=1, type='transform')
                # 只处理mesh
                if allChildren:
                    for child in allChildren:
                        shape = mc.listRelatives(child, s=1)
                        if shape:
                            if mc.nodeType(shape[0]) == 'mesh':
                                # 处理不接收阴影
                                mc.editRenderLayerAdjustment(shape[0] + '.receiveShadows')
                                mc.setAttr((shape[0] + '.receiveShadows'), 0)
            # 连接renderPass
    
    
            # 隐藏灯光
            for light in lights:
                lightGrp = mc.listRelatives(light, p=1)[0]
                mc.editRenderLayerAdjustment(light + '.intensity')
                if 'IDMT_2D_' not in light:
                    mc.setAttr((light + '.intensity'), 0)
                mc.editRenderLayerAdjustment(lightGrp + '.v')
                mc.setAttr((light + '.v'), 0)
                
            # 材质
            SGnodes = self.cllRLSGNodesGet()
            refSGCHR = SGnodes[0]
            refSGPROP = SGnodes[1]
            refSGSET = SGnodes[2]
            refSGENV = SGnodes[3]
            refSGSKY = SGnodes[4]
            refSGCalimero = SGnodes[5]
            
            rlSGNodes = refSGENV
            
            # 创建备用材质组
            shaderName = 'SHD_CALI_' + '2D'
            if mc.ls(shaderName):
                mc.delete(shaderName)
            shaderNeed = mc.shadingNode ('surfaceShader', asShader=True, name=shaderName)   
            mc.setAttr(('%s.outColor') % (shaderNeed), 0, 0, 0, type="double3")
    
            # 连接材质
            for SGNode in rlSGNodes:
                # 查找RGB或RGBA节点
                RGBNodeGrp = mc.listConnections(SGNode + '.surfaceShader')
                if RGBNodeGrp:
                    RGBNode = RGBNodeGrp[0]
                    needTxNode = ''
                    # 寻找2D节点
                    if '_RGBA' not in needTxNode:
                        needTxNode = RGBNode.replace('_RGB', '_2D')
                    else:
                        needTxNode = RGBNode.replace('_RGBA', '_2D')
                    # RGB/RGBA提供的node
                    if mc.objExists(needTxNode):
                        node = needTxNode
                    else:
                        node = shaderNeed
                    mc.editRenderLayerAdjustment((SGNode + '.surfaceShader'))
                    mc.disconnectAttr((RGBNode + '.outColor'), (SGNode + '.surfaceShader'))
                    mc.connectAttr((node + '.outColor'), (SGNode + '.surfaceShader'))
            
    
            # 设置
            # self.cllRLCommonConfig()
    
            # 渲染设置
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')
            mel.eval("editRenderLayerAdjustment \"defaultRenderGlobals.currentRenderer\";")
            
            # exr格式
            mel.eval("editRenderLayerAdjustment \"defaultRenderGlobals.imageFormat\";")
            if mc.optionMenuGrp('imageMenuMentalRay', exists=1):
                # mc.optionMenuGrp('imageMenuMentalRay', e=1, sl=7)
                # mel.eval('changeMentalRayImageFormat')
                mc.optionMenuGrp('imageMenuMentalRay', e=1, sl=13)
                try:
                    mel.eval('changeMentalRayImageFormat')
                except:
                    pass
                
            # 16位zip压缩
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.editRenderLayerAdjustment('miDefaultFramebuffer.datatype')
            mc.setAttr('miDefaultFramebuffer.datatype', 16)
    
            print (unicode('===============!!!Done  【%s】!!!===============' % (str('RENDER_2D层')), 'utf8'))        
            print '\n'
        else:
            print (unicode('===============!!!None  【%s】!!!===============' % (str('RENDER_2D层')), 'utf8'))        
            print '\n'
            
    # PFX层,仅仅CALI
    def cllRLBGPFXCreate(self):
        print (unicode('===============!!!Start 【%s】!!!===============' % (str('PFX层')), 'utf8'))
        print 'Working...'
        
        # 物体
        objs = self.cllRLObjectsTList()
        refCHR = objs[0]
        refPROP = objs[1]
        refSET = objs[2]
        refENV = objs[3]
        refSKY = objs[4]
        refCalimero = objs[5]

        # 灯光
        lights = mc.ls(type='light')
        if 'IDMT_2D_KeyLight' in lights:
            lights.remove('IDMT_2D_KeyLight')
        if 'IDMT_2D_SideLight' in lights:
            lights.remove('IDMT_2D_SideLight')

        # 物体
        rlObjs = refCalimero 
        if rlObjs:
            # 创建RenderLayer
            layerName = 'PFX'
            mc.createRenderLayer(rlObjs , name=layerName , noRecurse=1 , makeCurrent=1)
            
            # 隐藏灯光
            for light in lights:
                lightGrp = mc.listRelatives(light, p=1)[0]
                mc.editRenderLayerAdjustment(light + '.intensity')
                mc.setAttr((light + '.intensity'), 0)
                mc.editRenderLayerAdjustment(lightGrp + '.v')
                mc.setAttr((light + '.v'), 0)
                   
            # 连接renderPass
    
            # 材质
            SGnodes = self.cllRLSGNodesGet()
            refSGCHR = SGnodes[0]
            refSGPROP = SGnodes[1]
            refSGSET = SGnodes[2]
            refSGENV = SGnodes[3]
            refSGSKY = SGnodes[4]
            refSGCalimero = SGnodes[5]
            
            rlSGNodes = refSGCalimero
            
            # 创建备用材质组
            shaderName = 'SHD_' + 'BLACK'
            if mc.ls(shaderName):
                mc.delete(shaderName)
            shaderNeed = mc.shadingNode ('lambert', asShader=True, name=shaderName)   
            mc.setAttr(('%s.color') % (shaderNeed), 0, 0, 0, type="double3")
    
            # 连接材质
            for SGNode in rlSGNodes:
                # 查找RGB或RGBA节点
                RGBNodeGrp = mc.listConnections(SGNode + '.surfaceShader')
                if RGBNodeGrp:
                    RGBNode = RGBNodeGrp[0]
                    needTxNode = ''
                    '''
                    # 寻找内部节点
                    listTxNodes = mc.listConnections(RGBNode)
                    for nd in listTxNodes:
                        if "_BLACK" in nd:
                            needTxNode = nd
                            break
                    '''
                    # 寻找BLACK节点
                    if '_RGBA' not in RGBNode:
                        needTxNode = RGBNode.replace('_RGB', '_BLACK')
                    else:
                        needTxNode = RGBNode.replace('_RGBA', '_BLACK')
                    # RGB/RGBA提供的node
                    if mc.objExists(needTxNode):
                        node = needTxNode
                    else:
                        node = shaderNeed
                    mc.editRenderLayerAdjustment((SGNode + '.surfaceShader'))
                    mc.disconnectAttr((RGBNode + '.outColor'), (SGNode + '.surfaceShader'))
                    mc.connectAttr((node + '.outColor'), (SGNode + '.surfaceShader'))
            
            # 设置
            # self.cllRLCommonConfig()
    
            # 渲染器
            mc.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'mayaSoftware', type='string')
            
            mc.editRenderLayerAdjustment('defaultResolution.width')
            mc.setAttr('defaultResolution.width', 3840)
            mc.editRenderLayerAdjustment('defaultResolution.height')
            mc.setAttr('defaultResolution.height', 2160)
    
            # exr格式
            '''
            if mc.optionMenuGrp('imageMenuMentalRay', exists=1):
                mc.optionMenuGrp('imageMenuMentalRay', e=1, sl=7)
                mel.eval('changeMentalRayImageFormat')
                mc.optionMenuGrp('imageMenuMentalRay', e=1, sl=13)
                mel.eval('changeMentalRayImageFormat')
            '''
            
            # 8位zip压缩
            mc.setAttr('mentalrayGlobals.imageCompression', 4)
            mc.editRenderLayerAdjustment('miDefaultFramebuffer.datatype')
            mc.setAttr('miDefaultFramebuffer.datatype', 2)
    
            
            print (unicode('===============!!!Done  【%s】!!!===============' % (str('PFX层')), 'utf8'))        
            print '\n'
        else:
            print (unicode('===============!!!None  【%s】!!!===============' % (str('PFX层')), 'utf8'))        
            print '\n'
        
