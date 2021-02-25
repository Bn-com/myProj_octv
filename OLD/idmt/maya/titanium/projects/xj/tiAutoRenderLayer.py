# -*- coding: utf-8 -*-
import tempfile
import maya.cmds as mc
import maya.mel as mel
import pymel.core as pm
import os
import re
import mtoa
import mtoa.cmds.registerArnoldRenderer

import xlrd
reload(xlrd)
from ... import tiPre as tiPre
reload(tiPre)
from ... import tiBase as tiBase
reload(tiBase)
from ... import tiFile as tiFile
reload(tiFile)
from ... import tiEgg as tiEgg
reload(tiEgg)

from ... import tiLog as tiLog
reload(tiLog)

from ... import tiBatchCmd as tiBatchCmd
reload(tiBatchCmd)

class tiAutoRenderLayer(tiEgg.tiEgg):
    """docstring for tiAutoRenderLayer"""
    def __init__(self, *args, **kw):
        super(tiAutoRenderLayer, self).__init__(*args, **kw)
        
        if kw.get('preCheck', False):
            errorInfo = []
            rgMoAnimPattern = re.compile('%s_(c|p|s).+_h_(rg|mo|ms_anim).(ma|mb)' % self.proj, re.I)
            renderPattern = re.compile('%s_(c|p|s).+_h_ms_render.(ma|mb)' % self.proj, re.I)
            
            chrOrSetPatter = re.compile('%s_(c|s).+_h_ms_render.(ma|mb)' % self.proj, re.I)

            refFiles = pm.listReferences()

            msRenderFiles = []

            if not refFiles:
                errorInfo.append(u'文件中没有任何参考文件')

            for ref in refFiles:
                if ref.isLoaded():
                    refPath =  ref.path
                    baseName = os.path.basename(refPath)
                    if rgMoAnimPattern.match(baseName):
                        errorInfo.append(u'文件中不能参考非ms_render文件: %s -> %s' % (ref.namespace,refPath))
                
                    if renderPattern.match(baseName):
                        msRenderFiles.append(ref)
                        
            if msRenderFiles:
                for ms in msRenderFiles:
                    if not mc.objExists('%s:SMOOTH_SET' % ms.namespace):
                        errorInfo.append(u'%s 没有 SMOOTH_SET' % ms.namespace)

                    baseName = os.path.basename(ms.path)
                    if chrOrSetPatter.match(baseName):
                        tf = tiFile.tiAssetFile(baseName)
                        for i in range(1,5):
                            name = 'ID1%d' % i
                            fh = tf.rgbInfoFile(name)
                            if os.path.exists(fh):
                                break
                        else:
                            errorInfo.append(u'找不到 %s 的IDP信息,请先输出' % tf.id)

            else:
                errorInfo.append(u'文件中没有任何ms_render文件')

            try:
                shotCam = self.getRenderCamera()
            except:
                camName = 'cam_%s_%s_%s' % (self.ep, self.scene, self.shot)
                # errorInfo.append(u'场景中没有找到正确的相机: %s' % camName)
                errorInfo.append('not found the right camera: %s' % camName)


            ligGrp = pm.ls(regex = '*:(MSH_Set_light|MSH_Chr_light)(?i)')
            if not ligGrp:
                errorInfo.append(u'场景中没有 MSH_Set_light 或 MSH_Chr_light')

            excelPath = self.lightingExcelFile

            if os.path.exists(excelPath):
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
                else:
                    errorInfo.append(u'灯光Excel文件中找不到该镜头:  %s -> %s_%s_%s' % (excelPath, self.ep, self.scene, self.shot))
                if rowID != -1:

                    rowData = sheet.row_values(rowID)
                    if len(rowData) < 9:
                        errorInfo.append(u'Excel表数据格式不对,I 列中没有数据: %s' % excelPath)

                    if not sheet.cell(rowID,8).value.strip():
                        errorInfo.append(u'Excel表 I 列中没有填写数据: %s -> %s_%s_%s' % (excelPath, self.ep, self.scene, self.shot))
            else:
                errorInfo.append(u'灯光Excel文件不存在: %s' % excelPath)

            if errorInfo:
                tiLog.print_error(errorInfo)
            else:
                print u'=== file ok for setup render layers ==='

            tiBase.changeImageFileToDollarPath()
            
            self.cameraAnimationStart, self.cameraAnimationEnd = self.getCameraAnimationTimeRange(self.getRenderCamera())
            self.getCameraOutObjs(self.cameraAnimationStart, self.cameraAnimationEnd)



    def prepareForSetupLayer(self):
        self.chrs, self.props, self.sets = self.getReferenceFiles()
        
        self.lightInfo = self.getLightInfo()

        self.deletRenderLayers()
        self.deletDisplayLayers()
        self.cleanAOVs()
        self.setSmoothAttrs()
        self.xjcsDefaultRenderSettings()
        mc.setAttr('defaultRenderLayer.renderable', False)


    # ================================== new ====================================
    def setupIdpLayer(self):
        self.prepareForSetupLayer()
        self.xjcsArnoldRenderSettings('idp', format='tif')
        
        self.getTransmissionObjs(False)

        self.setDefaultShader()

        for aov in ['crypto_asset', 'crypto_object']:
            self.aiAOVCreate(aov)

        for aovName in ['aiAOV_crypto_asset', 'aiAOV_crypto_object']:
            if mc.objExists(aovName):
                mc.setAttr(aovName + '.enabled', False)


        hasIdpSets = []
        for se in self.sets:
            map(lambda x : x.visibility.set(0), pm.ls(regex = se.namespace + ':(MSH_Set_light|MSH_Chr_light)(?i)'))
            if self.testIdpFile(se.path):
                hasIdpSets.append(se)



        hasIpdChrs = []
        
        for char in self.chrs:
            if self.testIdpFile(char.path):
                hasIpdChrs.append(char)


        if hasIpdChrs:

            for i in range(1,5):
                name = 'ID1%d' % i
                
                for ref in hasIpdChrs:

                    tf = tiFile.tiAssetFile(ref.path)
                    fh = tf.rgbInfoFile(name)
                    if os.path.exists(fh):

                        addObjs = pm.ls(regex = '*:(CHR|PRO)(?i)')

                        layerName = 'chrIdp1%d' % i
                        if not mc.objExists(layerName):
                            pm.createRenderLayer(name = layerName, number = 1, empty =  True)
                        mc.select(cl = True)
                        pm.editRenderLayerMembers(layerName, addObjs, noRecurse = True)
                        mc.editRenderLayerGlobals(currentRenderLayer = layerName)

                        data = tiBase.jsonRead(fh)
                        for key, val in data.items():
                            mc.select(cl = True)
                            shdName = 'Arnold%s' % key
                            tiPre.ArnoldIDCreat(shdName, False)
                            sg = mc.listConnections(shdName, s = False, d = True, type = 'shadingEngine')
                            if sg:
                                objnames = map(lambda obj : obj.replace('|', '|' + ref.namespace + ':')[1:], val['objs'])
                                mc.sets( objnames, e=1, forceElement = sg[0])
                                # for obj  in val['objs']:
                                #     objname = obj.replace('|', '|' + ref.namespace + ':')
                                #     mc.sets( objname[1:], e=1, forceElement = sg[0])


                        propNs = '|'.join([p.namespace for p in self.props])
        
                        for prop in pm.ls(regex = '(%s):.*' % propNs, type='mesh'):
                            # mc.editRenderLayerAdjustment(prop + '.aiOpaque')
                            # mc.setAttr(prop + '.aiOpaque', True)
                            mc.editRenderLayerAdjustment(prop.name() + '.aiMatte')
                            mc.setAttr(prop.name() + '.aiMatte', True)
                            


        hasIdpProps = []
        for prop in self.props:
            if self.testIdpFile(prop.path):
                hasIdpProps.append(prop)
        if hasIdpProps:

            for i in range(1,5):
                name = 'ID1%d' % i
                
                for ref in hasIdpProps:

                    tf = tiFile.tiAssetFile(ref.path)
                    fh = tf.rgbInfoFile(name)
                    if os.path.exists(fh):

                        addObjs = pm.ls(regex = ref.namespace + ':PRO(?i)')

                        layerName = 'propIdp1%d' %  i
                        if not mc.objExists(layerName):
                            pm.createRenderLayer(addObjs,name = layerName, number = 1, empty =  True)
                        
                        pm.select(cl = True)
                        pm.editRenderLayerMembers(layerName, addObjs, noRecurse = True)
                        mc.editRenderLayerGlobals(currentRenderLayer = layerName)

                        data = tiBase.jsonRead(fh)
                        for key, val in data.items():
                            mc.select(cl = True)
                            shdName = 'Arnold%s' % key
                            tiPre.ArnoldIDCreat(shdName, False)
                            sg = mc.listConnections(shdName, s = False, d = True, type = 'shadingEngine')
                            if sg:
                                objnames = map(lambda obj : obj.replace('|', '|' + ref.namespace + ':')[1:], val['objs'])
                                mc.sets( objnames, e=1, forceElement = sg[0])


        

        

        if hasIdpSets:

            for i in range(1,5):
                name = 'ID1%d' % i

                for ref in hasIdpSets:

                    tf = tiFile.tiAssetFile(ref.path)
                    fh = tf.rgbInfoFile(name)
                    if os.path.exists(fh):

                        addObjs = pm.ls(regex = ref.namespace + ':SET(?i)')
                        
                        layerName = 'setIdp1%d' % i

                        
                        if not mc.objExists(layerName):
                            pm.createRenderLayer(addObjs,name = layerName, number = 1, empty =  True)
                        
                        pm.select(cl = True)
                        pm.editRenderLayerMembers(layerName, addObjs, noRecurse = True)

                        mc.editRenderLayerGlobals(currentRenderLayer = layerName)

                        data = tiBase.jsonRead(fh)
                        for key, val in data.items():
                            mc.select(cl = True)
                            shdName = 'Arnold%s' % key
                            tiPre.ArnoldIDCreat(shdName, False)
                            sg = mc.listConnections(shdName, s = False, d = True, type = 'shadingEngine')
                            if sg:
                                objnames = map(lambda obj : obj.replace('|', '|' + ref.namespace + ':')[1:], val['objs'])
                                mc.sets( objnames, e=1, forceElement = sg[0])

                        self.overrideRenderFrameRange()

        

        allObjGrp = pm.ls(regex = '*:(CHR|PRO|SET)(?i)')
        layerName = 'cryptoIdp'
        if not mc.objExists(layerName):
            pm.createRenderLayer(name = layerName, number = 1, empty =  True)

        self.overrideLayerBlackShadingGrp(layerName)
        mc.select(cl = True)
        pm.editRenderLayerMembers(layerName, allObjGrp, noRecurse = True)
        mc.editRenderLayerGlobals(currentRenderLayer = layerName)

        for aovName in ['aiAOV_crypto_asset', 'aiAOV_crypto_object']:
            if mc.objExists(aovName):
                mc.editRenderLayerAdjustment(aovName + '.enabled')
                mc.setAttr(aovName + '.enabled', True)


        mc.editRenderLayerAdjustment('defaultArnoldDriver.ai_translator')
        mc.setAttr( 'defaultArnoldDriver.ai_translator', 'exr', type='string' )
        driverAttrs = {'aiTranslator': 'exr','mergeAOVs': True,'exrCompression': 3}
        tiBase.batchSetAttrs('defaultArnoldDriver',driverAttrs, True)



        

        self.importAllRefNodes(self.chrs + self.props + self.sets)
        
        self.cleanShaderAndTexture()

        
        print u'=== IDP 分层完毕 ==='


    def setupAovLayer(self):
        self.prepareForSetupLayer()
        self.getTransmissionObjs(False)
        self.setDefaultShader()
        self.xjcsArnoldRenderSettings('aov', format='tif')

        for aov in ['fr', 'N']:
            self.aiAOVCreate(aov, driver = 'tif')


        chrAndProp = pm.ls(regex = '*:(CHR|PRO|SET)(?i)')

        if chrAndProp:
            layer = self.creatRenderLayer('chrAov', chrAndProp)
            self.overrideLayerDefaultShadingGrp(layer)



            lightGrpName = 'MSH_Chr_light'
            self.isolateLightGrp(lightGrpName, override = True)

            chrLightGrp = self.getLightGrp(lightGrpName, True, self.lightInfo, override = True)

            self.setupRGBLights(chrLightGrp)


        # SET AOV
        setGrp = pm.ls(regex = '*:SET(?i)')
        if setGrp:
            setLayer = self.creatRenderLayer('setAov', setGrp)
            self.overrideRenderFrameRange()
            self.overrideLayerDefaultShadingGrp(setLayer)
            
            
            lightGrpName = 'MSH_Set_light'
            self.isolateLightGrp(lightGrpName, True, override = True)

            setLightGrp = self.getLightGrp(lightGrpName, True, self.lightInfo, override = True)

            self.setupRGBLights(setLightGrp)


        self.importAllRefNodes((self.chrs + self.props + self.sets))
        self.cleanShaderAndTexture()

        print u'=== AOV 分层完毕 ===' 


    def setupColorLayer(self):
        self.prepareForSetupLayer()
        self.xjcsArnoldRenderSettings('color')
        # self.turnOffGlassCarPrim()

        setObjs = pm.ls(regex = '*:SET(?i)')

        objs = pm.ls(regex = '*:(CHR|PRO)(?i)')


        chrEmission = False
        setEmission = False

        allAovs = []

        if objs:
            allAovs += ['diffuse', 'specular', 'sss', 'transmission']
            mats = pm.ls(regex = '({0}_c|{0}_p).+:.+'.format(self.proj), type = 'aiStandardSurface') 
            for mat in mats:
                if mat.emission.get():
                    allAovs += ['emission']
                    chrEmission = True
                    break


        if setObjs:
            allAovs += ['diffuse', 'specular', 'P', 'Z']
            mats = pm.ls(regex = '%s_s.+:.+'% self.proj, type = 'aiStandardSurface') 
            for mat in mats:
                if mat.emission.get():
                    allAovs += ['emission']
                    setEmission = True
                    break

        allAovs = list(set(allAovs))
        for aov in allAovs:
            self.aiAOVCreate(aov, driver = 'exr')




        if objs:
            transObjs = self.getTransmissionObjs()
            # objs.append(lgtGrp)
            layer = self.creatRenderLayer('chrColor', objs + setObjs)


            lightGrpName = 'MSH_Chr_light'
            self.isolateLightGrp(lightGrpName, override = True)

            chrLightGrp = self.getLightGrp(lightGrpName, True, self.lightInfo, override = True) #lightInfo)

            for obj in transObjs:
                mc.editRenderLayerAdjustment(obj + '.visibility')
                mc.setAttr(obj + '.visibility', False)
            


            hideAovs = ['aiAOV_P','aiAOV_Z'] if chrEmission else ['aiAOV_P','aiAOV_Z','aiAOV_emission']
            for aovName in hideAovs:
                if mc.objExists(aovName):
                    mc.editRenderLayerAdjustment(aovName + '.enabled')
                    mc.setAttr(aovName + '.enabled', False)



            if transObjs:
                layer = self.creatRenderLayer('glassColor', objs)

                self.isolateLightGrp(lightGrpName, override = True)

                chrLightGrp = self.getLightGrp(lightGrpName, True, self.lightInfo, override = True) #lightInfo)


                nsns = '|'.join([p.namespace for p in (self.props + self.chrs)])
            
                           
                meshObjs = [n.getParent().name() for n in pm.ls(regex = '(%s):.*' % nsns, type='mesh')]

                excludeGlassCarMeshes =  [item for item in meshObjs if item not in transObjs]
                for i in excludeGlassCarMeshes:
                    mc.editRenderLayerAdjustment(i + '.aiMatte')
                    mc.setAttr(i + '.aiMatte', True)

                for aovName in ['aiAOV_P','aiAOV_Z', 'aiAOV_sss','aiAOV_emission']:
                    if mc.objExists(aovName):
                        mc.editRenderLayerAdjustment(aovName + '.enabled')
                        mc.setAttr(aovName + '.enabled', False)

                self.xjcsArnoldRenderSettings('glassColor', True)


        # SET COLOR
        if setObjs:
            layer = self.creatRenderLayer('setColor', setObjs)
            self.overrideRenderFrameRange()
            setlightGrpName = 'MSH_Set_light'
            self.isolateLightGrp(setlightGrpName, True, override = True)

            setLightGrp = self.getLightGrp(setlightGrpName, True, self.lightInfo, override = True)

            hideAovs = ['aiAOV_sss', 'aiAOV_transmission'] if setEmission else ['aiAOV_sss', 'aiAOV_transmission','aiAOV_emission']

            for aovName in hideAovs:
                if mc.objExists(aovName):
                    mc.editRenderLayerAdjustment(aovName + '.enabled')
                    mc.setAttr(aovName + '.enabled', False)
        

        print u'=== Color 分层完毕 ==='  



    def setupAOLayer(self):
        self.prepareForSetupLayer()
        self.xjcsArnoldRenderSettings('ao', format='tif')
        
        self.setDefaultShader()

        for ligGrp in pm.ls(regex = '*:(MSH_Set_light|MSH_Chr_light)(?i)'):
            # mc.editRenderLayerAdjustment(ligGrp.name() + '.visibility')
            mc.setAttr(ligGrp.name() + '.visibility', False)



        chrProp = pm.ls(regex = '*:(CHR|PRO)(?i)')
        setGrp =  pm.ls(regex = '*:SET(?i)')
        
        if chrProp:
            chrAoLayer = self.creatRenderLayer('chrAo', (chrProp + setGrp))
            
            self.overrideLayerAOShadingGrp(chrAoLayer)

            setNs = '|'.join([s.namespace for s in self.sets])

            setMeshObjs = [n.getParent().name() for n in pm.ls(regex = '(%s):.*' % setNs, type='mesh')]
            standIns = [n.name() for n in pm.ls(regex = '(%s):.*' % setNs, type='aiStandIn')]

            for setNode in (setMeshObjs + standIns):
                mc.editRenderLayerAdjustment(setNode + '.primaryVisibility')
                mc.setAttr(setNode + '.primaryVisibility', False)

            # for ref in self.sets:
            #     for n in ref.nodes():
            #         if (pm.objectType(n) == 'mesh' and n.intermediateObject.get() == False) or pm.objectType(n) == 'aiStandIn':
            #                 # n.primaryVisibility.set(0)
            #                 # n.castsShadows.set(0)
            #                 mc.editRenderLayerAdjustment(n.name() + '.primaryVisibility')
            #                 mc.setAttr(n.name() + '.primaryVisibility', False)
                    


        if setGrp:
            setAoLayer = self.creatRenderLayer('setAo', (chrProp + setGrp))
            self.overrideRenderFrameRange()
            self.overrideLayerAOShadingGrp(setAoLayer)


            nsns = '|'.join([p.namespace for p in (self.props + self.chrs)])
                
                               
            meshObjs = [n.getParent().name() for n in pm.ls(regex = '(%s):.*' % nsns, type='mesh')]


            for ob in meshObjs:
                    mc.editRenderLayerAdjustment(ob + '.primaryVisibility')
                    mc.setAttr(ob + '.primaryVisibility', False)

        
        self.importAllRefNodes(self.sets + self.chrs + self.props)
        
        self.cleanShaderAndTexture()

        print u'=== AO  分层完毕 ==='  



    def setupShadowLayer(self):
        self.prepareForSetupLayer()
        self.xjcsArnoldRenderSettings('shadow', format='tif')
        self.setDefaultShader()


        chrProp = pm.ls(regex = '*:(CHR|PRO)(?i)')
        setGrp =  pm.ls(regex = '*:SET(?i)')

        if chrProp and setGrp:

            setShadowlayer = self.creatRenderLayer('setShadow', chrProp + setGrp)

            self.overrideLayerShadowShadingGrp(setShadowlayer)

            lightGrpName = 'MSH_Chr_light'
            self.isolateLightGrp(lightGrpName, True, override = True)

            chrLightGrp = self.getLightGrp(lightGrpName, True, self.lightInfo, override = True)

            self.keyLightOn(chrLightGrp)
            

            setNs = '|'.join([s.namespace for s in self.sets])

            setMeshObjs = [n.getParent().name() for n in pm.ls(regex = '(%s):.*' % setNs, type='mesh')]
            standIns = [n.name() for n in pm.ls(regex = '(%s):.*' % setNs, type='aiStandIn')]

            for setNode in (setMeshObjs + standIns):
                mc.editRenderLayerAdjustment(setNode + '.castsShadows')
                mc.setAttr(setNode + '.castsShadows', False)


            # for ref in self.sets:
            #     for n in ref.nodes():
            #         if (pm.objectType(n) == 'mesh' and n.intermediateObject.get() == False) or pm.objectType(n) == 'aiStandIn':
            #                 # n.primaryVisibility.set(0)
            #                 # n.castsShadows.set(0)
            #                 mc.editRenderLayerAdjustment(n.name() + '.castsShadows')
            #                 mc.setAttr(n.name() + '.castsShadows', False)


            nsns = '|'.join([p.namespace for p in (self.props + self.chrs)])
                
                               
            meshObjs = [n.getParent().name() for n in pm.ls(regex = '(%s):.*' % nsns, type='mesh')]


            for ob in meshObjs:
                    mc.editRenderLayerAdjustment(ob + '.primaryVisibility')
                    mc.setAttr(ob + '.primaryVisibility', False)


            # for ref in (self.chrs + self.props):
            #     for n in ref.nodes():
            #         if (pm.objectType(n) == 'mesh' and n.intermediateObject.get() == False) or pm.objectType(n) == 'aiStandIn':
            #                 # n.primaryVisibility.set(0)
            #                 mc.editRenderLayerAdjustment(n.name() + '.primaryVisibility')
            #                 mc.setAttr(n.name() + '.primaryVisibility', False)
                    
        







            chrShadowLayer = self.creatRenderLayer('chrShadow', chrProp + setGrp)
            
            self.overrideLayerShadowShadingGrp(chrShadowLayer)

            setlightGrpName = 'MSH_Set_light'
            self.isolateLightGrp(setlightGrpName, True, override = True)

            setLightGrp = self.getLightGrp(setlightGrpName, True, self.lightInfo, override = True)

            self.keyLightOn(setLightGrp)


            setNs = '|'.join([s.namespace for s in self.sets])

            setMeshObjs = [n.getParent().name() for n in pm.ls(regex = '(%s):.*' % setNs, type='mesh')]
            standIns = [n.name() for n in pm.ls(regex = '(%s):.*' % setNs, type='aiStandIn')]

            for setNode in (setMeshObjs + standIns):
                mc.editRenderLayerAdjustment(setNode + '.primaryVisibility')
                mc.setAttr(setNode + '.primaryVisibility', False)



            nsns = '|'.join([p.namespace for p in (self.props + self.chrs)])
                
                               
            meshObjs = [n.getParent().name() for n in pm.ls(regex = '(%s):.*' % nsns, type='mesh')]


            for ob in meshObjs:
                    mc.editRenderLayerAdjustment(ob + '.castsShadows')
                    mc.setAttr(ob + '.castsShadows', False)



            # for ref in self.sets:
            #     for n in ref.nodes():
            #         if (pm.objectType(n) == 'mesh' and n.intermediateObject.get() == False) or pm.objectType(n) == 'aiStandIn':
            #                 # n.primaryVisibility.set(0)
            #                 # n.castsShadows.set(0)
            #                 mc.editRenderLayerAdjustment(n.name() + '.primaryVisibility')
            #                 mc.setAttr(n.name() + '.primaryVisibility', False)


            # for ref in (self.chrs + self.props):
            #     for n in ref.nodes():
            #         if (pm.objectType(n) == 'mesh' and n.intermediateObject.get() == False) or pm.objectType(n) == 'aiStandIn':
            #                 # n.primaryVisibility.set(0)
            #                 mc.editRenderLayerAdjustment(n.name() + '.castsShadows')
            #                 mc.setAttr(n.name() + '.castsShadows', False)
                    




        self.importAllRefNodes(self.sets + self.chrs + self.props)
        
        self.cleanShaderAndTexture()

        print u'=== Shadow  分层完毕 ==='

    

    def outputRenderFiles2(self):

        # self.cameraAnimationStart, self.cameraAnimationEnd = self.getCameraAnimationTimeRange(self.getRenderCamera())
        # self.getCameraOutObjs(self.cameraAnimationStart, self.cameraAnimationEnd)

        path = os.path.join(self.localTemp, 'Scenes\\Animation\\lr', self.ep, self.scene, self.shot)

        if not os.path.exists(path):
            os.makedirs(path)

        layeFiles = ['color', 'aov', 'idp', 'ao']


        if (self.chrs + self.props) and self.sets:
            layeFiles.append('shadow')

        renderFiles = []
        idx = 0
        while idx < len(layeFiles):
            newFileName = '%s_%s_%s_%s_l2%s_lr_c001.mb' % (self.proj, self.ep, self.scene,  self.shot, layeFiles[idx])

            tempRenderFile = os.path.join(tempfile.gettempdir(), os.path.basename(newFileName))

        
            renderFiles.append(tempRenderFile)
            pm.saveAs(tempRenderFile, f = True)
            idx += 1

        

        if renderFiles:
            
            x = 0
            while x < len(renderFiles):
                fileName = renderFiles[x]
                

                pm.openFile(fileName, f = True)
                
                if 'color' in fileName:
                    print '=== start color ==='
                    self.setupColorLayer()
                elif 'aov' in fileName:
                    print '=== start aov ==='
                    self.setupAovLayer()
                elif 'idp' in fileName:
                    print '=== start idp ==='
                    self.setupIdpLayer()
                elif 'ao' in fileName:
                    print '=== start ao ==='
                    self.setupAOLayer()
                elif 'shadow' in fileName:
                    print '=== start shadow ==='
                    self.setupShadowLayer()
                

                if not tiBase.isOEM():
                    tiBatchCmd.checkoutAnim(u'自动分层')
                else:
                    pm.saveAs(fileName, f = True)
                
                x += 1

            print '\n%s\n' % ('*' * 50)
            for fileName in renderFiles:
                dest = os.path.join(path, os.path.basename(fileName))
                tiBase.sysMoveFile(fileName, dest)
                print u'文件保存在: %s' % dest
            print '\n%s\n' % ('*' * 50)
        else:
            print u'=== 无任何分层文件输出 ==='


    # ================================== new ====================================



    # ================================== old ====================================
    def outputRenderFiles(self):

        path = os.path.join(self.localTemp, 'Scenes\\Animation\\lr', self.ep, self.scene, self.shot)

        if not os.path.exists(path):
            os.makedirs(path)

        chrNum = len(self.chrs + self.props)
        setNum = len(self.sets)
        renderFiles = []

        if chrNum:
            layeFiles = ['chrColor', 'chrAov', 'chrIdp']
            idx = 0
            while idx < len(layeFiles):
                newFileName = '%s_%s_%s_%s_%s_lr_c001.mb' % (self.proj, self.ep, self.scene,  self.shot, layeFiles[idx])

                fullName = os.path.join(path, newFileName)
                renderFiles.append(fullName)
                pm.saveAs(fullName, f = True)
                idx += 1

        if setNum:
            layeFiles = ['setColor', 'setAov', 'setIdp']
            idx = 0
            while idx < len(layeFiles):
                newFileName = '%s_%s_%s_%s_%s_lr_c001.mb' % (self.proj, self.ep, self.scene,  self.shot, layeFiles[idx])
                fullName = os.path.join(path, newFileName)
                renderFiles.append(fullName)
                pm.saveAs(fullName, f = True)
                idx += 1

        if chrNum and setNum:
            newFileName = '%s_%s_%s_%s_%s_lr_c001.mb' % (self.proj, self.ep, self.scene,  self.shot, 'setCon')
            fullName = os.path.join(path, newFileName)
            renderFiles.append(fullName)
            pm.saveAs(fullName, f = True)

        if renderFiles:
            
            x = 0
            while x < len(renderFiles):
                fileName = renderFiles[x]
                

                pm.openFile(fileName, f = True)
                
                if 'chrColor' in fileName:
                    print '=== start chrColor ==='
                    self.setupChrColorLayer()
                elif 'chrAov' in fileName:
                    print '=== start chrAov ==='
                    self.setupChrAovLayer()
                elif 'chrIdp' in fileName:
                    print '=== start chrIdp ==='
                    self.setupChrIdpLayer()
                elif 'setColor' in fileName:
                    print '=== start setColor ==='
                    self.setupSetColorLayer()
                elif 'setAov' in fileName:
                    print '=== start setAov ==='
                    self.setupSetAovLayer()
                elif 'setIdp' in fileName:
                    print '=== start setIdp ==='
                    self.setupSetIdpLayer()
                elif 'setCon' in fileName:
                    print '=== start setCon ==='
                    self.setupSetConLayer()

                pm.saveAs(fileName, f = True)
                
                x += 1

            print '\n%s\n' % ('*' * 50)
            for fileName in renderFiles:
                print u'文件保存在: %s' % fileName
            print '\n%s\n' % ('*' * 50)
        else:
            print u'=== 无任何分层文件输出 ==='

    def setupChrColorLayer(self):
        self.prepareForSetupLayer()
        
        lightGrpName = 'MSH_Chr_light'
        self.isolateLightGrp(lightGrpName)

        chrLightGrp = self.getLightGrp(lightGrpName, True, self.lightInfo) #lightInfo)


        # setLightGrp = self.getLightGrp('MSH_Set_light')
        # lgtGrp = self.duplicateLightGrp(chrLightGrp)

        # self.removeRefNodes(self.sets)

        transObjs = self.getTransmissionObjs()

        # self.turnOffGlassCarPrim()



        for aov in ['diffuse', 'specular', 'sss', 'transmission']:
            self.aiAOVCreate(aov, driver = 'exr')


        
        objs = self.getAssetRootGrp()
        # objs.append(lgtGrp)
        layer = self.creatRenderLayer('chrColor', objs)

        for obj in transObjs:
            mc.editRenderLayerAdjustment(obj + '.visibility')
            mc.setAttr(obj + '.visibility', False)
        self.xjcsArnoldRenderSettings('chrColor', True)

        if transObjs:
            layer = self.creatRenderLayer('glassColor', objs)

            meshObjs = [n.getParent().name() for n in self.getAllMesh()]

            excludeGlassCarMeshes =  [item for item in meshObjs if item not in transObjs]
            for i in excludeGlassCarMeshes:
                mc.editRenderLayerAdjustment(i + '.aiMatte')
                mc.setAttr(i + '.aiMatte', True)

            if mc.objExists('aiAOV_sss'):
                mc.editRenderLayerAdjustment('aiAOV_sss.enabled')
                mc.setAttr('aiAOV_sss.enabled', False)


            self.xjcsArnoldRenderSettings('glassColor', True)

        print u'=== chr color 分层完毕 ==='     
    

    def setupChrAovLayer(self):
        self.prepareForSetupLayer()
        

        lightGrpName = 'MSH_Chr_light'
        self.isolateLightGrp(lightGrpName)

        chrLightGrp = self.getLightGrp(lightGrpName, True, self.lightInfo)

        self.getTransmissionObjs(False)


        self.setupRGBLights(chrLightGrp)


        self.setDefaultShader()
        
    

        for aov in ['fr', 'N']:
            self.aiAOVCreate(aov, driver = 'tif')

        objs = self.getAssetRootGrp()

        
        layer = self.creatRenderLayer('chrAov', objs)


        self.overrideLayerDefaultShadingGrp(layer)

        self.importAllRefNodes(self.chrs + self.props + self.sets)
        
        self.cleanShaderAndTexture()

        self.xjcsArnoldRenderSettings('aov', format = 'tif')
        print u'=== chr aov 分层完毕 ===' 

    def setupChrIdpLayer(self):
        self.prepareForSetupLayer()

        self.removeRefNodes(self.sets)

        self.getTransmissionObjs(False)

        self.setDefaultShader()

        hasIpdChrs = []
        hasIdpProps = []

        for char in self.chrs:
            if self.testIdpFile(char.path):
                hasIpdChrs.append(char)

        for prop in self.props:
            if self.testIdpFile(prop.path):
                hasIdpProps.append(prop)


        if hasIpdChrs:

            for i in range(1,5):
                name = 'ID1%d' % i
                
                for ref in hasIpdChrs:

                    tf = tiFile.tiAssetFile(ref.path)
                    fh = tf.rgbInfoFile(name)
                    if os.path.exists(fh):

                        addObjs = pm.ls(regex = ref.namespace + ':(CHR|PRO)')

                        layerName = 'chrIdp1%d' % i
                        if not mc.objExists(layerName):
                            pm.select(addObjs, r = True)
                            pm.createRenderLayer(name = layerName, number = 1, nr =  True)
                        else:
                            pm.select(cl = True)
                            pm.editRenderLayerMembers(layerName, addObjs, noRecurse = True)

                        mc.editRenderLayerGlobals(currentRenderLayer = layerName)

                        data = tiBase.jsonRead(fh)
                        for key, val in data.items():
                            mc.select(cl = True)
                            shdName = 'Arnold%s' % key
                            tiPre.ArnoldIDCreat(shdName, False)
                            sg = mc.listConnections(shdName, s = False, d = True, type = 'shadingEngine')
                            if sg:
                                objnames = map(lambda obj : obj.replace('|', '|' + ref.namespace + ':')[1:], val['objs'])
                                mc.sets( objnames, e=1, forceElement = sg[0])
                                # for obj  in val['objs']:
                                #     objname = obj.replace('|', '|' + ref.namespace + ':')
                                #     mc.sets( objname[1:], e=1, forceElement = sg[0])

                        propMatteObjs = []
                        propMeshes = []
                        for prop in self.props:
                            propMatteObjs += pm.ls(regex = prop.namespace + ':(SET|CHR|PRO)')
                            propMeshes += [n.name() for n in pm.ls(regex = prop.namespace + ':.*', type='mesh')]
                            print '*' * 50
                            print prop
                            print '*' * 50

                        pm.editRenderLayerMembers(layerName, propMatteObjs, noRecurse = True)

                        for prop in propMeshes:
                            mc.editRenderLayerAdjustment(prop + '.aiMatte')
                            mc.setAttr(prop + '.aiMatte', True)
                            mc.setAttr(prop + '.aiOpaque', True)


        if hasIdpProps:

            for i in range(1,5):
                name = 'ID1%d' % i
                
                for ref in hasIdpProps:

                    tf = tiFile.tiAssetFile(ref.path)
                    fh = tf.rgbInfoFile(name)
                    if os.path.exists(fh):

                        addObjs = pm.ls(regex = ref.namespace + ':PRO')


                        # layerName = 'chrIdp1%d' % i
                        # if not mc.objExists(layerName):
                        #     pm.select(addObjs, r = True)
                        #     pm.createRenderLayer(name = layerName, number = 1, nr =  True)
                        # else:
                        #     pm.select(cl = True)
                        #     pm.editRenderLayerMembers(layerName, addObjs, noRecurse = True)

                        # mc.editRenderLayerGlobals(currentRenderLayer = layerName)


                        layerName = 'propIdp1%d' %  i
                        if not mc.objExists(layerName):
                            pm.select(addObjs, r = True)
                            pm.createRenderLayer(addObjs,name = layerName, number = 1, nr =  True)
                        else:
                            pm.select(cl = True)
                            pm.editRenderLayerMembers(layerName, addObjs, noRecurse = True)

                        mc.editRenderLayerGlobals(currentRenderLayer = layerName)

                        data = tiBase.jsonRead(fh)
                        for key, val in data.items():
                            mc.select(cl = True)
                            shdName = 'Arnold%s' % key
                            tiPre.ArnoldIDCreat(shdName, False)
                            sg = mc.listConnections(shdName, s = False, d = True, type = 'shadingEngine')
                            if sg:
                                objnames = map(lambda obj : obj.replace('|', '|' + ref.namespace + ':')[1:], val['objs'])
                                mc.sets( objnames, e=1, forceElement = sg[0])

                                # for obj  in val['objs']:
                                #     objname = obj.replace('|', '|' + ref.namespace + ':')
                                #     mc.sets( objname[1:], e=1, forceElement = sg[0])

        self.importAllRefNodes(self.chrs + self.props + self.sets)
        
        self.cleanShaderAndTexture()

        self.xjcsArnoldRenderSettings('idp', format='tif')
        print u'=== chr IDP 分层完毕 ===' 


    def setupSetColorLayer(self):
        self.prepareForSetupLayer()

        lightGrpName = 'MSH_Set_light'
        self.isolateLightGrp(lightGrpName, True)

        chrLightGrp = self.getLightGrp(lightGrpName, True, self.lightInfo)

        self.removeRefNodes(self.chrs )
        self.removeRefNodes(self.props)


        setAovs = ['diffuse', 'specular', 'P', 'Z']
        mats = pm.ls(regex = '%s_s.+:.+'% 'xj', type = 'aiStandardSurface') 
        for mat in mats:
            if mat.emission.get():

                setAovs = ['diffuse', 'specular', 'P', 'Z', 'emission']
                break

        for aov in setAovs:
            self.aiAOVCreate(aov, driver = 'exr')

        objs = self.getAssetRootGrp()
       
        layer = self.creatRenderLayer('setColor', objs)

        self.xjcsArnoldRenderSettings('setColor')
        print u'=== set color 分层完毕 ==='          
    

    def setupSetAovLayer(self):
        self.prepareForSetupLayer()
        
        lightGrpName = 'MSH_Set_light'
        self.isolateLightGrp(lightGrpName, True)

        setLightGrp = self.getLightGrp(lightGrpName, True, self.lightInfo)

        self.setupRGBLights(setLightGrp)


        self.setDefaultShader()



        self.removeRefNodes(self.chrs)
        self.removeRefNodes(self.props)
        
        for aov in ['fr', 'N']:
            self.aiAOVCreate(aov, driver = 'tif')

        objs = self.getAssetRootGrp()


        layer = self.creatRenderLayer('setAov', objs)

        self.overrideLayerDefaultShadingGrp(layer)

        self.importAllRefNodes(self.sets)
        
        self.cleanShaderAndTexture()
        self.xjcsArnoldRenderSettings('aov', format='tif')
        print u'=== set aov 分层完毕 ==='     


    def setupSetIdpLayer(self):

        self.prepareForSetupLayer()

        self.removeRefNodes(self.chrs)
        self.removeRefNodes(self.props)

        self.setDefaultShader()

        self.getTransmissionObjs(False)

        hasIdpSets = []

        for se in self.sets:
            map(lambda x : x.visibility.set(0), pm.ls(regex = se.namespace + ':(MSH_Set_light|MSH_Chr_light)'))
            if self.testIdpFile(se.path):
                hasIdpSets.append(se)

        if hasIdpSets:

            for i in range(1,5):
                name = 'ID1%d' % i

                for ref in hasIdpSets:

                    tf = tiFile.tiAssetFile(ref.path)
                    fh = tf.rgbInfoFile(name)
                    if os.path.exists(fh):

                        addObjs = pm.ls(regex = ref.namespace + ':SET')
                        
                        layerName = 'setIdp1%d' % i

                        pm.select(cl = True)
                        if not mc.objExists(layerName):
                            
                            pm.createRenderLayer(addObjs,name = layerName, number = 1, nr =  True)
                        else:
                            
                            pm.editRenderLayerMembers(layerName, addObjs, noRecurse = True)

                        mc.editRenderLayerGlobals(currentRenderLayer = layerName)

                        data = tiBase.jsonRead(fh)
                        for key, val in data.items():
                            mc.select(cl = True)
                            shdName = 'Arnold%s' % key
                            tiPre.ArnoldIDCreat(shdName, False)
                            sg = mc.listConnections(shdName, s = False, d = True, type = 'shadingEngine')
                            if sg:

                                objnames = map(lambda obj : obj.replace('|', '|' + ref.namespace + ':')[1:], val['objs'])
                                mc.sets( objnames, e=1, forceElement = sg[0])

        self.importAllRefNodes(self.chrs + self.props + self.sets)
        
        self.cleanShaderAndTexture()
        self.xjcsArnoldRenderSettings('idp', format='tif')
        print u'=== set IDP 分层完毕 ==='     
                                

    def setupSetConLayer(self):

        self.xjcsArnoldRenderSettings('aov', format='tif')
        self.prepareForSetupLayer()
        

        lightGrpName = 'MSH_Chr_light'
        self.isolateLightGrp(lightGrpName, True)

        chrLightGrp = self.getLightGrp(lightGrpName, True, self.lightInfo)

        self.keyLightOn(chrLightGrp)
        
        for aov in ['ao']:
            self.aiAOVCreate(aov, driver = 'tif')

        for aov in ['crypto_asset', 'crypto_object']:
            self.aiAOVCreate(aov)

        objs = self.getAssetRootGrp()

        self.setDefaultShader()


        layer = self.creatRenderLayer('setShadow', objs)
        self.overrideLayerShadowShadingGrp(layer)

        # self.xjcsArnoldRenderSettings('chrColor', True)

        for aovName in ['aiAOV_crypto_asset', 'aiAOV_crypto_object']:
            if mc.objExists(aovName):
                mc.editRenderLayerAdjustment(aovName + '.enabled')
                mc.setAttr(aovName + '.enabled', False)



        for ref in self.sets:
            for n in ref.nodes():
                if (pm.objectType(n) == 'mesh' and n.intermediateObject.get() == False) or pm.objectType(n) == 'aiStandIn':
                        # n.primaryVisibility.set(0)
                        # n.castsShadows.set(0)
                        mc.editRenderLayerAdjustment(n.name() + '.castsShadows')
                        mc.setAttr(n.name() + '.castsShadows', False)


        for ref in (self.chrs + self.props):
            for n in ref.nodes():
                if (pm.objectType(n) == 'mesh' and n.intermediateObject.get() == False) or pm.objectType(n) == 'aiStandIn':
                        # n.primaryVisibility.set(0)
                        mc.editRenderLayerAdjustment(n.name() + '.primaryVisibility')
                        mc.setAttr(n.name() + '.primaryVisibility', False)
                    
        

        chrAoLayer = self.creatRenderLayer('chrAo', objs)
        
        self.overrideLayerAOShadingGrp(chrAoLayer)

        for ligGrp in pm.ls(regex = '*:(MSH_Set_light|MSH_Chr_light)'):
            mc.editRenderLayerAdjustment(ligGrp.name() + '.visibility')
            mc.setAttr(ligGrp.name() + '.visibility', False)


        for aovName in ['aiAOV_ao','aiAOV_crypto_asset', 'aiAOV_crypto_object']:
            if mc.objExists(aovName):
                mc.editRenderLayerAdjustment(aovName + '.enabled')
                mc.setAttr(aovName + '.enabled', False)


        for ref in self.sets:
            for n in ref.nodes():
                if (pm.objectType(n) == 'mesh' and n.intermediateObject.get() == False) or pm.objectType(n) == 'aiStandIn':
                        # n.primaryVisibility.set(0)
                        # n.castsShadows.set(0)
                        mc.editRenderLayerAdjustment(n.name() + '.primaryVisibility')
                        mc.setAttr(n.name() + '.primaryVisibility', False)
                    



        chrConLayer = self.creatRenderLayer('chrShadow', objs)

        self.overrideLayerShadowShadingGrp(chrConLayer)


        lightGrpName = 'MSH_Set_light'
        self.isolateLightGrp(lightGrpName, True, True)

        setLightGrp = self.getLightGrp(lightGrpName, True, self.lightInfo)
        self.keyLightOn(setLightGrp)


        for aovName in ['aiAOV_ao']:
            if mc.objExists(aovName):
                mc.editRenderLayerAdjustment(aovName + '.enabled')
                mc.setAttr(aovName + '.enabled', False)

        for ref in self.sets:
            for n in ref.nodes():
                if (pm.objectType(n) == 'mesh' and n.intermediateObject.get() == False) or pm.objectType(n) == 'aiStandIn':
                        # n.primaryVisibility.set(0)
                        # n.castsShadows.set(0)
                        mc.editRenderLayerAdjustment(n.name() + '.primaryVisibility')
                        mc.setAttr(n.name() + '.primaryVisibility', False)

        for ref in (self.chrs + self.props):
            for n in ref.nodes():
                if (pm.objectType(n) == 'mesh' and n.intermediateObject.get() == False) or pm.objectType(n) == 'aiStandIn':
                        # n.primaryVisibility.set(0)
                        mc.editRenderLayerAdjustment(n.name() + '.castsShadows')
                        mc.setAttr(n.name() + '.castsShadows', False)

        mc.editRenderLayerAdjustment('defaultArnoldDriver.ai_translator')
        mc.setAttr( 'defaultArnoldDriver.ai_translator', 'exr', type='string' )
        driverAttrs = {'aiTranslator': 'exr','mergeAOVs': True,'exrCompression': 3}

    
        tiBase.batchSetAttrs('defaultArnoldDriver',driverAttrs, True)


        self.importAllRefNodes(self.sets + self.chrs + self.props)
        
        self.cleanShaderAndTexture()

        print u'=== setCon  分层完毕 ==='
    # ================================== old ====================================


        

    def testIdpFile(self, filePath):
        tf = tiFile.tiAssetFile(filePath)
        
        for i in range(1,5):
            name = 'ID1%d' % i
            fh = tf.rgbInfoFile(name)
            if os.path.exists(fh):
                return True
                break


    def testSetupLayer(self, layerType):
        objs = pm.ls(sl = True)
        
        self.deletRenderLayers()
        self.cleanAOVs()

        self.xjcsDefaultRenderSettings()

        if  layerType in ['chrAov', 'setAov', 'setShadow', 'chrShadow', 'setIdp', 'chrIdp', 'chrAo', 'setAo']:
            self.xjcsArnoldRenderSettings('aov', format='tif')
        else:
            self.xjcsArnoldRenderSettings('color')

        emissionShader = False
        for mat in pm.ls(type = 'aiStandardSurface'):
            if mat.emission.get():
                emissionShader = True
                break


        mc.select(cl = True)
        if layerType == 'chrColor':

            avos = ['diffuse', 'specular', 'sss', 'transmission'] 
            if emissionShader:
                avos.append('emission')

            for aov in avos:
                self.aiAOVCreate(aov, driver = 'exr')

        elif layerType == 'glassColor':
            for aov in ['diffuse', 'specular', 'transmission']:
                self.aiAOVCreate(aov, driver = 'exr')

        elif layerType in ['chrAov', 'setAov']:
            for aov in ['fr', 'N']:
                self.aiAOVCreate(aov, driver = 'tif')

        elif layerType == 'setColor':
            avos = ['diffuse', 'specular', 'P', 'Z', 'emission']
            if emissionShader:
                avos.append('emission')
            for aov in avos:
                self.aiAOVCreate(aov, driver = 'exr')


        layer = self.creatRenderLayer(layerType, objs)
        
        if layerType in ['chrAov', 'setAov']:
            
            self.overrideLayerDefaultShadingGrp(layer)
        elif layerType in ['chrAo', 'setAo']: 
            self.overrideLayerAOShadingGrp(layer)
        elif layerType in ['chrShadow', 'setShdow']: 
            self.overrideLayerShadowShadingGrp(layer)

        elif layerType in ['chrIdp', 'setIdp']:
            self.testSetupIdpLayer()
        else:
            self.creatRenderLayer(layerType, objs)

        mc.select(cl = True)
        print '=== setup ok ==='


    def testSetupIdpLayer(self):
        

        for aov in ['crypto_asset', 'crypto_object']:
            self.aiAOVCreate(aov)

        for aovName in ['aiAOV_crypto_asset', 'aiAOV_crypto_object']:
            if mc.objExists(aovName):
                mc.setAttr(aovName + '.enabled', False)


        chrRefs, propRefs, setRefs = self.getReferenceFiles()

        hasIdpSets = []
        for se in setRefs:
            # map(lambda x : x.visibility.set(0), pm.ls(regex = se.namespace + ':(MSH_Set_light|MSH_Chr_light)(?i)'))
            if self.testIdpFile(se.path):
                hasIdpSets.append(se)



        hasIpdChrs = []
        
        for char in chrRefs:
            if self.testIdpFile(char.path):
                hasIpdChrs.append(char)


        if hasIpdChrs:

            for i in range(1,5):
                name = 'ID1%d' % i
                
                for ref in hasIpdChrs:

                    tf = tiFile.tiAssetFile(ref.path)
                    fh = tf.rgbInfoFile(name)
                    if os.path.exists(fh):

                        addObjs = pm.ls(regex = '*:(CHR|PRO)(?i)')

                        layerName = 'chrIdp1%d' % i
                        if not mc.objExists(layerName):
                            pm.createRenderLayer(name = layerName, number = 1, empty =  True)
                        mc.select(cl = True)
                        pm.editRenderLayerMembers(layerName, addObjs, noRecurse = True)
                        mc.editRenderLayerGlobals(currentRenderLayer = layerName)

                        data = tiBase.jsonRead(fh)
                        for key, val in data.items():
                            mc.select(cl = True)
                            shdName = 'Arnold%s' % key
                            tiPre.ArnoldIDCreat(shdName, False)
                            sg = mc.listConnections(shdName, s = False, d = True, type = 'shadingEngine')
                            if sg:
                                objnames = map(lambda obj : obj.replace('|', '|' + ref.namespace + ':')[1:], val['objs'])
                                mc.sets( objnames, e=1, forceElement = sg[0])
                                # for obj  in val['objs']:
                                #     objname = obj.replace('|', '|' + ref.namespace + ':')
                                #     mc.sets( objname[1:], e=1, forceElement = sg[0])


                        propNs = '|'.join([p.namespace for p in self.props])
        
                        for prop in pm.ls(regex = '(%s):.*' % propNs, type='mesh'):
                            # mc.editRenderLayerAdjustment(prop + '.aiOpaque')
                            # mc.setAttr(prop + '.aiOpaque', True)
                            mc.editRenderLayerAdjustment(prop.name() + '.aiMatte')
                            mc.setAttr(prop.name() + '.aiMatte', True)
                            


        hasIdpProps = []
        for prop in propRefs:
            if self.testIdpFile(prop.path):
                hasIdpProps.append(prop)
        if hasIdpProps:

            for i in range(1,5):
                name = 'ID1%d' % i
                
                for ref in hasIdpProps:

                    tf = tiFile.tiAssetFile(ref.path)
                    fh = tf.rgbInfoFile(name)
                    if os.path.exists(fh):

                        addObjs = pm.ls(regex = ref.namespace + ':PRO(?i)')

                        layerName = 'propIdp1%d' %  i
                        if not mc.objExists(layerName):
                            pm.createRenderLayer(addObjs,name = layerName, number = 1, empty =  True)
                        
                        pm.select(cl = True)
                        pm.editRenderLayerMembers(layerName, addObjs, noRecurse = True)
                        mc.editRenderLayerGlobals(currentRenderLayer = layerName)

                        data = tiBase.jsonRead(fh)
                        for key, val in data.items():
                            mc.select(cl = True)
                            shdName = 'Arnold%s' % key
                            tiPre.ArnoldIDCreat(shdName, False)
                            sg = mc.listConnections(shdName, s = False, d = True, type = 'shadingEngine')
                            if sg:
                                objnames = map(lambda obj : obj.replace('|', '|' + ref.namespace + ':')[1:], val['objs'])
                                mc.sets( objnames, e=1, forceElement = sg[0])


        

        

        if hasIdpSets:

            for i in range(1,5):
                name = 'ID1%d' % i

                for ref in hasIdpSets:

                    tf = tiFile.tiAssetFile(ref.path)
                    fh = tf.rgbInfoFile(name)
                    if os.path.exists(fh):

                        addObjs = pm.ls(regex = ref.namespace + ':SET(?i)')
                        
                        layerName = 'setIdp1%d' % i

                        
                        if not mc.objExists(layerName):
                            pm.createRenderLayer(addObjs,name = layerName, number = 1, empty =  True)
                        
                        pm.select(cl = True)
                        pm.editRenderLayerMembers(layerName, addObjs, noRecurse = True)

                        mc.editRenderLayerGlobals(currentRenderLayer = layerName)

                        data = tiBase.jsonRead(fh)
                        for key, val in data.items():
                            mc.select(cl = True)
                            shdName = 'Arnold%s' % key
                            tiPre.ArnoldIDCreat(shdName, False)
                            sg = mc.listConnections(shdName, s = False, d = True, type = 'shadingEngine')
                            if sg:
                                objnames = map(lambda obj : obj.replace('|', '|' + ref.namespace + ':')[1:], val['objs'])
                                mc.sets( objnames, e=1, forceElement = sg[0])


        

        allObjGrp = pm.ls(regex = '*:(CHR|PRO|SET)(?i)')
        layerName = 'cryptoIdp'
        if not mc.objExists(layerName):
            pm.createRenderLayer(name = layerName, number = 1, empty =  True)

        self.overrideLayerBlackShadingGrp(layerName)
        mc.select(cl = True)
        pm.editRenderLayerMembers(layerName, allObjGrp, noRecurse = True)
        mc.editRenderLayerGlobals(currentRenderLayer = layerName)

        for aovName in ['aiAOV_crypto_asset', 'aiAOV_crypto_object']:
            if mc.objExists(aovName):
                mc.editRenderLayerAdjustment(aovName + '.enabled')
                mc.setAttr(aovName + '.enabled', True)


        mc.editRenderLayerAdjustment('defaultArnoldDriver.ai_translator')
        mc.setAttr( 'defaultArnoldDriver.ai_translator', 'exr', type='string' )
        driverAttrs = {'aiTranslator': 'exr','mergeAOVs': True,'exrCompression': 3}
        tiBase.batchSetAttrs('defaultArnoldDriver',driverAttrs, True)





    def overrideRenderFrameRange(self):
        start, end, duration = tiBase.timeLine()
        if self.cameraAnimationStart != start or  self.cameraAnimationEnd != end:
            defaultRenderGlobalsAttrs = {
                'startFrame': self.cameraAnimationStart,
                'endFrame': self.cameraAnimationEnd
            }

            tiBase.batchSetAttrs('defaultRenderGlobals', defaultRenderGlobalsAttrs, True)

    def xjcsDefaultRenderSettings(self):

        self.setRenderCam()
        start, end, duration = tiBase.timeLine()

        # 读取数据库帧数
        # frames = mc.idmtProject( timeLine = True, echo  = False)

        # 设置渲染相机

        defaultRenderGlobalsAttrs = {
            'imageFilePrefix': '<RenderLayer>/<Scene>_<RenderLayer>',
            'outFormatControl': 0,
            'animation': 1,
            'putFrameBeforeExt': 1,
            'periodInExt': 1,
            'extensionPadding': 4,
            'startFrame': start,
            'endFrame': end
        }


        tiBase.batchSetAttrs('defaultRenderGlobals', defaultRenderGlobalsAttrs)


        resAttrs = {
            'width': 1920,
            'height': 1080,
            # 'width': 512,
            # 'height': 289,
            'pixelAspect': 1
        }
        tiBase.batchSetAttrs('defaultResolution', resAttrs)


        arnoldCommonRenderOptions = {
            
            # 'enableAdaptiveSampling': 1,
            # 'AASamplesMax': 6,

            'use_sample_clamp': 1,
            'AASampleClamp': 1.5,
            'indirectSampleClamp': 1.5,

            'lock_sampling_noise': 1,

            'autotx': 0,
            'textureAutotile': 64,
            'textureMaxMemoryMB': 1024,    
        }

        tiBase.batchSetAttrs('defaultArnoldRenderOptions', arnoldCommonRenderOptions)




    def xjcsArnoldRenderSettings(self, renderType, override = False, format = 'exr'):
        
        if format == 'exr':
            mc.setAttr( 'defaultArnoldDriver.ai_translator', 'exr', type='string' )
            driverAttrs = {'aiTranslator': 'exr','mergeAOVs': True,'exrCompression': 3}

        elif format == 'tif':
            mc.setAttr( 'defaultArnoldDriver.ai_translator', 'tif', type='string' )
            driverAttrs = {'aiTranslator': 'tif','tiffCompression': 1,'dither': 1, 'tiffFormat': 0}

        
        tiBase.batchSetAttrs('defaultArnoldDriver',driverAttrs)


        arnoldRenderOptions = {}

        if renderType in ['chrColor', 'setColor', 'color']:
            arnoldRenderOptions = {
                'AASamples': 6,
                'GIDiffuseSamples': 3,
                'GISpecularSamples': 2,
                'GITransmissionSamples': 2,
                'GISssSamples': 5,
                'GIVolumeSamples': 0,

                'GITotalDepth': 4,
                'GIDiffuseDepth': 1,
                'GISpecularDepth': 1,
                'GITransmissionDepth': 2,
                'GIVolumeDepth': 0,
                'autoTransparencyDepth': 4,
            }
        elif renderType in ['glassColor']:
            arnoldRenderOptions = {
                'AASamples': 6,
                'GIDiffuseSamples': 3,
                'GISpecularSamples': 2,
                'GITransmissionSamples': 2,
                'GISssSamples': 0,
                'GIVolumeSamples': 0,

                'GITotalDepth': 5,
                'GIDiffuseDepth': 1,
                'GISpecularDepth': 1,
                'GITransmissionDepth': 4,
                'GIVolumeDepth': 4,
                'autoTransparencyDepth': 4,
            }

        elif renderType in ['aov', 'idp', 'ao', 'shadow']:
            arnoldRenderOptions = {
                'AASamples': 5,
                'GIDiffuseSamples': 0,
                'GISpecularSamples': 0,
                'GITransmissionSamples': 0,
                'GISssSamples': 0,
                'GIVolumeSamples': 0,

                'GITotalDepth': 5,
                'GIDiffuseDepth': 0,
                'GISpecularDepth': 0,
                'GITransmissionDepth': 0,
                'GIVolumeDepth': 0,
                'autoTransparencyDepth': 4,
            }

        tiBase.batchSetAttrs('defaultArnoldRenderOptions', arnoldRenderOptions, override)


    def getTransmissionObjs(self, layVis = True):
        mats = pm.ls(regex = '(%s_p|%s_c).*'%(self.proj,self.proj), type = 'aiStandardSurface') 
        transObjs = []
        for mat in mats:
            if mat.transmission.get() > 0.0 and ('eye' not in mat.name()):
                
                transObjs += tiBase.getObjsByMaterial(mat.name())
        
        if transObjs:
            layerName = '__trans_obj_layer__'

            if not mc.objExists(layerName):
                
                mc.createDisplayLayer(name = layerName, number = 1, empty =  True)
           
            mc.select(cl = True)
            mc.editDisplayLayerMembers(layerName, transObjs, noRecurse = True)


            mc.setAttr(layerName + '.visibility', layVis)
            mc.select(cl = True)
        return transObjs



