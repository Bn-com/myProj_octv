# -*- coding: utf-8 -*-

import maya.cmds as mc
import maya.mel as mel
import pymel.core as pm
import os
import re
import mtoa
import mtoa.cmds.registerArnoldRenderer

import xlrd
reload(xlrd)

import tiBase as tiBase
reload(tiBase)
import tiFile as tiFile
reload(tiFile)

import tiLog as tiLog
reload(tiLog)

import libs.DkbObjectsInCameraView as DkbObjectsInCameraView
reload(DkbObjectsInCameraView)


class tiEgg(tiFile.tiAnimFile):
    """docstring for ClassName"""
    def __init__(self, *args, **kw):
        super(tiEgg, self).__init__(*args)
        mtoa.core.createOptions()
        self.chrs, self.props, self.sets = self.getReferenceFiles()
        self.renderCamera = None

    def checkSmoothSet(self):
        for f in (self.chrs + self.props + self.sets):
            if mc.objExists('%s:SMOOTH_SET' % f.namespace):
                break
            else:
                print '%s no SMOOTH_SET' % f.namespace
        else:
            mc.error('=== not found SMOOTH_SE ===')

    def checkIDP(self):
        hasError = False
        for m in (self.chrs + self.sets):
            tf = tiFile.tiAssetFile(m.path)
            for i in range(1,5):
                name = 'ID1%d' % i
                fh = tf.rgbInfoFile(name)
                if os.path.exists(fh):
                    print fh
                    break
            else:
                hasError = True
                print u'=== 找不到 %s 的IDP信息,请先输出 ===' % tf.id
        
        if hasError:
            mc.error(u'=== not found any IDP files ===')

    def isolateLightGrp(self, lightGrpName, hideModel = False, override = False):
        pattern = re.compile(lightGrpName, re.I)

        # layerName = '__set_layer__'
        
        # if not mc.objExists(layerName):
        #     mc.select(cl = True)
        #     layer = mc.createDisplayLayer(name = layerName, number = 1, nr =  True)
        
        # mc.setAttr(layerName + '.visibility', False)
        modelPattern = re.compile('MODEL$', re.I)

        for s in self.sets:
            children = pm.listRelatives('%s:SET' % s.namespace)
            find = False
            for child in children:
                state = True if  pattern.search(child.name()) else False
                
                if override:
                    mc.editRenderLayerAdjustment(child.name() + '.visibility')

                if modelPattern.search(child.name()):
                    child.visibility.set(hideModel)
                else:
                    child.visibility.set(state)

                if state:
                    find = True
                # else:
                #     pm.editDisplayLayerMembers(layerName, child, noRecurse = True)
            if find:
                break
        else:
            print u'%s 组必须在SET组下' % lightGrpName
            mc.error(u'not found %s lighting group' % lightGrpName)

    def setupRGBLights(self, lightGrp):
        lightGrpChildren = pm.listRelatives(lightGrp, ad = True)
        for l in lightGrpChildren:
            lightName = l.split('|')[-1].split(':')[-1]

            objType = pm.objectType(l)

            if objType == 'transform':
                if not re.match('^key|^fill|^rim', lightName, re.I):
                    l.visibility.set(0)
                
            elif re.search('light', objType, re.I):

                if re.match('^key', lightName, re.I):
                    l.color.set(1,0,0)
                elif re.match('^fill', lightName, re.I):
                    l.color.set(0,1,0)
                elif re.match('^rim', lightName, re.I):
                    l.color.set(0,0,1)


    def keyLightOn(self, lightGrp, override = False):

        lightGrpChildren = pm.listRelatives(lightGrp, ad = True)
        for l in lightGrpChildren:
            lightName = l.split('|')[-1].split(':')[-1]

            objType = pm.objectType(l)

            if objType == 'transform':

                if override:
                    mc.editRenderLayerAdjustment(child.name() + '.visibility')


                if not re.match('^key', lightName, re.I):
                    l.visibility.set(0)
                else:
                    l.visibility.set(1)
                
    def overrideLayerAOShadingGrp(self, layer):
        sg, shd = self.avoShader('ao')

        mc.connectAttr(sg + '.message', layer + '.shadingGroupOverride', f = True)



    def overrideLayerBlackShadingGrp(self, layer):
        shaderType = 'aiUtility'
        shdName = 'SHD_%s_RenderLayerShadingGroup' % shaderType
        sgName = 'SG_%s_RenderLayerShadingGroup' % shaderType

        if not mc.objExists(sgName):
            sg, shd = self.initShadingNetwork(shaderType, sgName, shdName)
        else:
            sg = sgName
            shd = shdName
        
        shadowAttrs = {
            'shadeMode': 2,
            'color': (0,0,0)
        }
        tiBase.batchSetAttrs(shd, shadowAttrs)

        mc.connectAttr(sg + '.message', layer + '.shadingGroupOverride', f = True)



            
    def overrideLayerShadowShadingGrp(self, layer):
        shaderType = 'aiShadowMatte'
        shdName = 'SHD_%s_RenderLayerShadingGroup' % shaderType
        sgName = 'SG_%s_RenderLayerShadingGroup' % shaderType

        if not mc.objExists(sgName):
            sg, shd = self.initShadingNetwork(shaderType, sgName, shdName)
        else:
            sg = sgName
            shd = shdName
        
        shadowAttrs = {
            'background': 1,
            'backgroundColor': (0,0,0),
            'shadowColor': (1,1,1)
        }
        tiBase.batchSetAttrs(shd, shadowAttrs)

        mc.connectAttr(sg + '.message', layer + '.shadingGroupOverride', f = True)


    def overrideLayerDefaultShadingGrp(self, layer):
        shaderType = 'aiUtility'
        shdName = 'SHD_%s_RenderLayerShadingGroup' % shaderType
        sgName = 'SG_%s_RenderLayerShadingGroup' % shaderType

        if not mc.objExists(sgName):
            sg, shd = self.initShadingNetwork(shaderType, sgName, shdName)
        else:
            sg = sgName
            shd = shdName
        mc.setAttr(shd + '.shadeMode', 1)
        mc.connectAttr(sg + '.message', layer + '.shadingGroupOverride', f = True)

    # def getAllRefNodes(self, refNodes):
    #     nodes = []
    #     for n in refNodes:
    #         nodes += n.nodes()
    #     return nodes

    def getAssetRootGrp(self):
        rootGrps = []
        for ref in (self.chrs + self.props + self.sets):
            rootGrps += pm.ls(regex = ref.namespace + ':(SET|CHR|PRO)') 
        return rootGrps


    def importAllRefNodes(self, refNodes):
        for n in refNodes:
            n.importContents()

    def removeRefNodes(self, refNodes):
        for n in refNodes:
            n.remove()
        del refNodes[:]

    
    # def duplicateLightGrp(self, lightGrp):
    #     if mc.objExists('tiLightingGrp'):
    #         mc.delete('tiLightingGrp')

    #     dupGrp = pm.duplicate(lightGrp, returnRootsOnly = True, name = lightGrp)
    #     pm.group(dupGrp, world = True, name = 'tiLightingGrp')
    #     return 'tiLightingGrp'


    







    # def setDefaultShader():

    #     refFiles = pm.listReferences()

        
    #     for ref in refFiles:
    #         if not ref.isLoaded():
    #             print u'===== 参考没加载 %s, 清除 =====' % ref
    #             ref.remove()
                
    #         else:
    #             tf = tiFile.tiAssetFile(ref.path)
          
    #             for n in ref.nodes():
    #                 if pm.objectType(n) == 'mesh' and n.intermediateObject.get() == False:
    #                     if tf.assetType == 'characters':
    #                         n.primaryVisibility.set(0)
    #                     elif tf.assetType == 'sets':
    #                         n.primaryVisibility.set(0)
    #                         n.castsShadows.set(0)
                        
    #                     mc.sets(n.name(),e=1, forceElement = 'initialShadingGroup')

    def setDefaultShader(self):
        mc.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
        nodes = self.getAssetRootGrp()

        # objnames = map(lambda obj : obj.replace('|', '|' + ref.namespace + ':')[1:], val['objs'])
        # mc.sets( objnames, e=1, forceElement = sg[0])
        nodeNames = map(lambda node: node.name(), nodes)
        mc.sets(nodeNames,e=1, forceElement = 'initialShadingGroup')
        # for n in nodes:
        #     mc.sets(n.name(),e=1, forceElement = 'initialShadingGroup')

    def cleanShaderAndTexture(self):

        mel.eval('MLdeleteUnused;OptimizeScene;cleanUpScene 1;')


    def creatRenderLayer(self,layerName, objs):
        pm.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
        if pm.objExists(layerName):
            pm.delete(layerName)

        pm.select(cl = True)
        renderLayer = pm.createRenderLayer(objs, name = layerName, number = 1, noRecurse = True)
        
        pm.setAttr(renderLayer + '.renderable', True)
        pm.setAttr('defaultRenderLayer.renderable', False)
        pm.editRenderLayerGlobals(currentRenderLayer = renderLayer)
        return renderLayer.name()


    def createDriver(self, driverType):
        if driverType == 'exr':
            driverAttrs = {'aiTranslator': 'exr','mergeAOVs': True,'exrCompression': 3}

        elif driverType == 'tif':
            driverAttrs = {'aiTranslator': 'tif','tiffCompression': 1,'dither': 1, 'tiffFormat': 0}


        driverName = 'aiAov_' + driverType + '_driver'
        if not mc.objExists(driverName):
            driverName = mc.createNode('aiAOVDriver', n = driverName)
        
        tiBase.batchSetAttrs(driverName, driverAttrs)

        tiBase.batchSetAttrs('defaultArnoldDriver', driverAttrs)


        return driverName


    def aiAOVCreate(self,avoType, driver = 'exr', dataType = 5):

        aovTypeMap = mtoa.aovs.getAOVTypeMap()
        isBuiltinAovs = aovTypeMap.has_key(avoType)
        if isBuiltinAovs:
            dt = aovTypeMap[avoType]

            tps = mtoa.aovs.TYPES
            for tp in tps:
                key, val = tp
                if key == dt:
                    dataType = val
                    break

        filterType = 'gaussian'
        # filterTypeMap = mtoa.aovs.defaultFiltersByName
        
        # if filterTypeMap.has_key(avoType):
        #     filterType = filterTypeMap[avoType]
            

        
        aovNode = self.safeCreateNode('aiAOV', 'aiAOV_' + avoType)
        mc.setAttr( aovNode + '.name', avoType, type = 'string')
        mc.setAttr( aovNode + '.type', dataType)
        
        if driver == 'exr':
            if not mc.isConnected('defaultArnoldDriver.message', aovNode + '.outputs[0].driver'):
                mc.connectAttr('defaultArnoldDriver.message', aovNode + '.outputs[0].driver', f = True)
        else:
            newDriver = self.createDriver(driver)
            mc.connectAttr(newDriver + '.message', aovNode + '.outputs[0].driver', f = True)

        filterNode = 'defaultArnoldFilter' 

        if filterType != 'gaussian':
            newFilterName = 'aiAOV_Filter_' + filterType
            if mc.objExists(newFilterName):
                filterNode = newFilterName
            else:
                filterNode = mc.createNode('aiAOVFilter', name = newFilterName)
                mc.setAttr(filterNode + '.aiTranslator', filterType, type = 'string')


        if not mc.isConnected( filterNode + '.message', aovNode + '.outputs[0].filter'):
            mc.connectAttr( filterNode + '.message', aovNode + '.outputs[0].filter', f = True)

        

        aovListNum = mc.getAttr('defaultArnoldRenderOptions.aovList',  size = True)
        isConnected = False
        for n in range(aovListNum):
            if not mc.listConnections('defaultArnoldRenderOptions.aovList[%d]' % n):
                mc.connectAttr(aovNode + '.message', 'defaultArnoldRenderOptions.aovList[%d]' % n, f = True)
                isConnected = True
                break
        if not isConnected:
            mc.connectAttr(aovNode + '.message', 'defaultArnoldRenderOptions.aovList[%d]' % aovListNum, f = True)


        if avoType in ['crypto_asset', 'crypto_material', 'crypto_object']:
            sg, shd = self.avoShader('cryptomatte')
            mc.connectAttr(shd + '.outColor', aovNode + '.defaultValue', f = True)

        if not isBuiltinAovs:
            if avoType == 'ao':
                sg, shd = self.avoShader('ao')
                
            elif avoType == 'fr':
                sg, shd = self.avoShader('fr')

            mc.connectAttr(shd + '.outColor', aovNode + '.defaultValue', f = True)


    def avoShader(self, shaderType):
        shdName = 'SHD_%s_AOV' % shaderType
        sgName = 'SG_%s_AOV' % shaderType

        if shaderType == 'cryptomatte':
            if mc.objExists(shdName):
                return shdName, shdName

        else:
            if mc.objExists(shdName) and mc.objExists(sgName):
                return sgName, shdName

        if shaderType == 'ao':
            sg, shd = self.initShadingNetwork('aiAmbientOcclusion', sgName, shdName)
            attrs = {
                'samples': 4,
                'falloff': 0.05
            }
            tiBase.batchSetAttrs(shd, attrs)
        elif shaderType == 'fr':
            sg, shd = self.initShadingNetwork('aiUtility', sgName, shdName)
            
            mc.setAttr(shd + '.shadeMode', 2)

            ramp = mc.shadingNode ('ramp', asShader=True, name= 'tiFresnel_Ramp')
            mc.removeMultiInstance(ramp + '.colorEntryList[1]' , b = 1)

            rampAttrs = {
                'interpolation': 3,
                'colorEntryList[2].position': 1,
                'colorEntryList[0].position': 0,
                'colorEntryList[2].color': (0,0,0),
                'colorEntryList[0].color': (1,1,1),
            }
            tiBase.batchSetAttrs(ramp, rampAttrs)


            samplerInfo = mc.shadingNode ('samplerInfo', asShader=True, name= 'tiFresnel_SamplerInfo')

            mc.connectAttr(samplerInfo + '.facingRatio', ramp + '.vCoord', f = True)
            mc.connectAttr(ramp + '.outColor', shd + '.color', f = True)

        elif shaderType == 'cryptomatte':
            shd = mc.createNode('cryptomatte', n = shdName)
            sg = shd

        return sg, shd

    def getReferenceFiles(self):

        refChrs = []
        refProps = []
        refSets = []

        chrPattern = re.compile('%s_c.+_h_ms_render.(ma|mb)' % self.proj, re.I)
        propPattern = re.compile('%s_p.+_h_ms_render.(ma|mb)' % self.proj, re.I)
        setPattern = re.compile('%s_s.+_h_ms_render.(ma|mb)' % self.proj, re.I)

        refFiles = pm.listReferences()

        for ref in refFiles:
            if not ref.isLoaded():
                tiLog.logInfo(u'参考没加载 %s, 清除' % ref)
                ref.remove()
            else:
                basename = os.path.basename(ref.path)
                
                if chrPattern.match(basename):
                    refChrs.append(ref)
                elif propPattern.match(basename):
                    refProps.append(ref)
                elif setPattern.match(basename):
                    refSets.append(ref)
        
        return refChrs, refProps, refSets



    def getLightGrp(self, grpName, isOn = False, lightInfo = '', override = False):

        useLightGrp = None

        lightGrps = pm.ls(regex = '*:?(%s(?i))' % grpName) #mc.ls('*:' + grpName, long = True)

        if len(lightGrps) != 1:
            for g in lightGrps:
                tiLog.logInfo(i.longName())
            tiLog.error(u'场景中没有或存在多个 %s 灯光组' % grpName)

        lightGrp = lightGrps[0]

        lightGrp.visibility.set(isOn)

        if isOn:
            lightGrpChildren =pm.listRelatives(lightGrp, type = 'transform', fullPath = True)

    
            for lg in lightGrpChildren:
                if override:
                    mc.editRenderLayerAdjustment(lg.name() + '.visibility')

                if re.match('^' + lightInfo, lg.split('|')[-1].split(':')[-1], re.IGNORECASE):
                    useLightGrp = lg
                    lg.visibility.set(1)
                    break
                else:
                    lg.visibility.set(0)

            else:
                
                print u'=======场景中找不到 %s_light组 , 请检查Excel表中 %s_%s_%s 镜头场景时段中的灯光信息 %s，或联系TD及PA处理=======' % (lightInfo, self.ep, self.scene, self.shot, lightInfo)
                mc.error('=== see more infomation ===')
            
        return useLightGrp


    def getLightInfo(self):
    
        excelPath = self.lightingExcelFile

        if not os.path.lexists(excelPath):
            tiLog.error(u'灯光Excel文件不存在: %s, 请联系PA处理' % excelPath)

        sheet = xlrd.open_workbook(excelPath).sheet_by_index(0)
        
        rowMax = sheet.nrows
        
        rowID = -1

        for i in range(rowMax):
            
            exlEp = sheet.cell(i,0).value  #sheet.row_values(i)[0]
            
            exlEp = str('%d' % exlEp) if type(exlEp) == float else exlEp
            exlScene = sheet.cell(i,1).value  #sheet.row_values(i)[1]
            exlShot = sheet.cell(i,2).value  #sheet.row_values(i)[2]

            if self.ep in exlEp and self.scene in exlScene  and self.shot in exlShot:
                rowID = i
                break

        if rowID == -1:
            tiLog.error(u'灯光Excel文件中找不到该镜头: %s_%s_%s' % (self.ep, self.scene, self.shot))

        rowData = sheet.row_values(rowID)
        if len(rowData) < 9:
            tiLog.error(u'Excel表 I 列中没有数据， 数据格式不对，请联系TD及PA处理')

        return sheet.cell(rowID,8).value.strip()
    

    def initShadingNetwork(self, shaderType, sgName, shdName):

        sg = mc.sets(renderable = True, noSurfaceShader = True, em = True,n = sgName) 
        shd = mc.shadingNode(shaderType, asShader=True,n=shdName)

        mc.connectAttr(shd + '.outColor', sg + '.surfaceShader', f = True)
        return sg, shd

    def deletRenderLayers(self):
        mc.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
        layers = mc.ls(type = 'renderLayer')
        for lay in layers:
            if 'defaultRenderLayer' not in lay:
                try:
                    mc.delete(lay)
                except:
                    print u'=== 无法删除渲染层: %s ===' % lay

    def deletDisplayLayers(self):
        for dlayer in mc.ls(type = 'displayLayer'):
            if dlayer != 'defaultLayer' and dlayer != 'norender' and dlayer != '__camera_out__':
                try:
                    mc.delete(dlayer)
                except:
                    print u'=== 无法删除显示层: %s ===' % lay

    def cleanAOVs(self):
        aovs = mtoa.aovs.getAOVs()
        for aov in aovs:
            mc.delete(aov.node)
        
    def safeCreateNode(self, node, name):
        if mc.objExists(name):
            try:
                mc.delete(name)
            except:
                return node
        newNode = mc.createNode(node, name = name)
        return newNode

    def setSmoothAttrs(self):
        smoothSets = pm.ls(regex='*:smooth_[012]$', type = 'objectSet')
        for s in smoothSets:
            lastChar = int(s.name()[-1])
            if lastChar == 1 or lastChar == 2:
                if not pm.attributeQuery('aiSubdivType', node = s,  exists = True):
                    s.addAttr('aiSubdivType', at = 'short')
                if not pm.attributeQuery('aiSubdivIterations', node = s,  exists = True):
                    s.addAttr('aiSubdivIterations', at = 'short')
                    
                s.setAttr('aiSubdivType', 1)
                s.setAttr('aiSubdivIterations', lastChar)

    # def getGlassCarShaders(self):
    #     glassCarShaders = pm.ls(regex='*GlassCar$', type = 'aiStandardSurface')
    #     return glassCarShaders


    def getAllMesh(self):
        allMeshes = []
        for m in pm.ls(type = 'mesh'):
            if not m.intermediateObject.get():
                allMeshes.append(m)
        return allMeshes

    # def getCam(self):
    #     cams = pm.ls(type = 'camera')
        
    #     shot = 'cam_%s' % '_'.join([self.ep, self.scene, self.shot])

    #     canNode = None
    #     for cam in cams:
    #         camParent = cam.getParent().name()
    #         if camParent.startswith(shot):
    #             cam.renderable.set(True)
    #             canNode = camParent
    #             break
    #         else:
    #             cam.renderable.set(False)

    #     else:
    #         mc.error(u'=== not found legal camera: %s ===' % shot )
    #     return canNode


    def getRenderCamera(self):
        shot = '_'.join([self.ep, self.scene, self.shot])
        camName = 'cam_%s' % shot
        bakeCams = [ x for x in pm.ls(regex = '*:?(%s(?i))_bake' % camName, type = 'transform') if pm.nodeType(x.getShape()) == 'camera']
        
        if bakeCams:
            return bakeCams[0].name()
        cams = [ x for x in pm.ls(regex = '*:?(%s(?i))' % camName, type = 'transform') if pm.nodeType(x.getShape()) == 'camera']
        if cams:
            return cams[0].name()
        
        mc.error('=== not found legal camera ===')

    def setRenderCam(self):
        shotCamera = self.getRenderCamera()
        if shotCamera:
            map(lambda x: x.renderable.set(False), pm.ls(type = 'camera'))
            mc.setAttr(shotCamera + '.renderable', True)
            


    # def setRenderCam(self):
    #     cams = pm.ls(type = 'camera')
        
    #     shot = 'cam_%s' % '_'.join([self.ep, self.scene, self.shot])


    #     for cam in cams:
    #         camParent = cam.getParent().name()
    #         cam.renderable.set(camParent.startswith(shot))



    def getCameraOutObjs(self, startFrame, endFrame):
        displayLayerName = '__camera_out__'
        if mc.objExists(displayLayerName):
            mc.delete(displayLayerName)


        renderCamera = self.getRenderCamera()

        # startFrame, endFrame = self.getCameraAnimationTimeRange(renderCamera)
        

        setObjs = [ n.getParent().longName() for n in pm.ls(regex = '.+:SET\|.+:MODEL\|.+', type = 'mesh')]
        setObjs += [n.longName() for n in pm.ls(regex = '.+:SET\|.+:MODEL\|.+', type = 'aiStandIn')]
        
        camIn = []
        if startFrame == endFrame:
            for obj in setObjs:
                if DkbObjectsInCameraView.process(renderCamera, obj):
                    camIn.append(obj)
                    
        else:
            for i in xrange(startFrame, (endFrame + 1)):
                mc.currentTime(i)
                for obj in setObjs:
                    if DkbObjectsInCameraView.process(renderCamera, obj):
                        camIn.append(obj)


        mc.select(cl = True)
        mc.createDisplayLayer(name = displayLayerName, number = 1, empty =  True)

        camOut = list(set(setObjs) - set(camIn))

        mc.editDisplayLayerMembers(displayLayerName, camOut, noRecurse = True)
        mc.setAttr(displayLayerName + '.visibility', False)
        print '=== hide camera out objs done ==='
        
    def getCameraAnimationTimeRange(self, renderCamera):

        cameraRef = mc.group(empty = True, name = '__camera_locator__')
        mc.parentConstraint(renderCamera, cameraRef, mo = False, weight = 1)


        cameraShapeName = pm.PyNode(renderCamera).getShape().name()
        
        attrs = ['tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'focalLength']

        start = -1
        end = -1

        startFrame, endFrame, duration = tiBase.timeLine()
        for i in range(startFrame,endFrame):
            
            currentResult = []
            nextResult = []
            for attr in attrs:
                if attr != 'focalLength':
                    currentResult.append( mc.getAttr('%s.%s' % (cameraRef,attr), t = i))
                    nextResult.append( mc.getAttr('%s.%s' % (cameraRef,attr), t = i + 1))
                else:
                    currentResult.append( mc.getAttr('%s.%s' % (cameraShapeName,attr), t = i))
                    nextResult.append( mc.getAttr('%s.%s' % (cameraShapeName,attr), t = i + 1))


            if start == -1 and currentResult != nextResult:
                start = i
                
            if currentResult != nextResult:
                end = i

        mc.delete(cameraRef)
        
        if start == end:
            return startFrame, startFrame

        
        return start, end + 1

    


    # def getGlassCarObjs(self):
    #     glassCarShaders = self.getGlassCarShaders()

    #     for g in glassCarShaders:
    #         glassObjs = tiBase.getObjsByMaterial(g.name())
    #         for obj in glassObjs:
    #             self.glassCarObjs.append(pm.PyNode(obj).getShape())

    # def setMatteNotGlassCarMeshes(self):
    #     excludeGlassCarMeshes =  [item for item in self.getAllMesh() if item not in self.glassCarObjs]

    #     for i in excludeGlassCarMeshes:
    #         i.aiMatte.set(1)

    # def turnOffGlassCarPrim(self):
    #     glassCarShaders = self.getGlassCarShaders()

    #     for g in glassCarShaders:
    #         meshes = tiBase.getObjsByMaterial(g.name())
    #         for m in meshes:
    #             try:
    #                 shapeNode = pm.PyNode(m).getShape()
    #                 shapeNode.primaryVisibility.set(0)
    #                 self.glassCarObj
    #             except:
    #                 pass


    