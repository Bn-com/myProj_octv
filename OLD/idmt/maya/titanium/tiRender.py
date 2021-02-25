# -*- coding: utf-8 -*-

import maya.cmds as mc
import maya.mel as mel
import pymel.core as pm
import os
import re
import mtoa
import mtoa.cmds.registerArnoldRenderer


# mtoa.core.createOptions()
# mtoa.cmds.registerArnoldRenderer.registerArnoldRenderer()

import xlrd
reload(xlrd)

from functools import partial
import tiBase as tiBase
reload(tiBase)
import tiFile as tiFile
reload(tiFile)


def xjcsDefaultRenderSettings( format = 'exr'):
    mtoa.core.createOptions()
    if format == 'exr':
        mc.setAttr( 'defaultArnoldDriver.ai_translator', 'exr', type='string' )
        driverAttrs = {'aiTranslator': 'exr','mergeAOVs': True,'exrCompression': 3}

    elif format == 'tif':
        mc.setAttr( 'defaultArnoldDriver.ai_translator', 'tif', type='string' )
        driverAttrs = {'aiTranslator': 'tif','tiffCompression': 1,'dither': 1, 'tiffFormat': 0}

    
    tiBase.batchSetAttrs('defaultArnoldDriver',driverAttrs)

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
        # 'startFrame': 1001,
        # 'endFrame': 1100
    }


    tiBase.batchSetAttrs('defaultRenderGlobals', defaultRenderGlobalsAttrs)


    resAttrs = {
        'width': 1920,
        'height': 1080,
        'pixelAspect': 1
    }
    tiBase.batchSetAttrs('defaultResolution', resAttrs)


    arnoldRenderOptions = {
        'AASamples': 5 if format == 'exr' else 3,
        'GIDiffuseSamples': 2 if format == 'exr' else 0,
        'GISpecularSamples': 2 if format == 'exr' else 0,
        'GITransmissionSamples': 5 if format == 'exr' else 0,
        'GISssSamples': 5 if format == 'exr' else 0,
        'GIVolumeSamples': 2,

        'enableAdaptiveSampling': 1 if format == 'exr' else 0,
        'AASamplesMax': 6 ,

        'use_sample_clamp': 1,
        'AASampleClamp': 1.5,
        'indirectSampleClamp': 1.5,

        'lock_sampling_noise': 1,

        'GITotalDepth': 10,
        'GIDiffuseDepth': 1,
        'GISpecularDepth': 1,
        'GITransmissionDepth': 8 if format == 'exr' else 2,
        'GIVolumeDepth': 0,
        'autoTransparencyDepth': 10,


        'autotx': 0,
        'textureAutotile': 64,
        'textureMaxMemoryMB': 1024,
        
    }

    tiBase.batchSetAttrs('defaultArnoldRenderOptions', arnoldRenderOptions)

'''
if ($shotInfo[0] == "cl")
        {
            python("from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig");
            python("reload(sk_referenceConfig)");
            python("sk_referenceConfig.sk_referenceConfig().checkReferenceShaderReset(0)");
            python("from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools");
            python("reload(sk_sceneTools)");
            print "\n";
            print ("======================  >>[ " + $shotInfo[0] + "_" + $shotInfo[1] + "_" + $shotInfo[2] + " ]<<  START  "+ "======================" + "\n");
            // 处理非参考的namespace
            python("sk_sceneTools.sk_sceneTools().sk_sceneNoRefNamespaceClean()");
            // anim转render
            python("from idmt.maya.Calimero import sk_calimeroProjectTools");
            python("reload(sk_calimeroProjectTools)");
            python("sk_calimeroProjectTools.sk_clProjectTools().sk_clAnim2Render()");
            // 加载丢失参考
            python("sk_calimeroProjectTools.sk_clProjectTools().calimeroRefAutoLoad(\"lr\")");
            // 整理文件
            python("from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools");
            python("reload(sk_sceneTools)");
            python("sk_sceneTools.sk_sceneTools().sk_sceneReorganize(2)");
            // 后台分层
            python("from idmt.maya.Calimero import sk_renderLayer_Calimero");
            python("reload(sk_renderLayer_Calimero)");
            python("sk_renderLayer_Calimero.clRLConfig().clRLAutoCreate(1,1,1)");
            
            print "\n";
            print ("======================  >>[ " + $shotInfo[0] + "_" + $shotInfo[1] + "_" + $shotInfo[2] + " ]<<  End  "+ "======================" + "\n");
            print "\n";
        }
'''


def ArnoldToolKit():
    
    if mc.window('tiArnoldToolKitUI', exists=True):
        mc.deleteUI('tiArnoldToolKitUI')
    mc.window('tiArnoldToolKitUI', title=u'tiArnoldToolKitUI -- 星际车神',
              width=320, height=350, sizeable=True)

    form = mc.formLayout()
    tabs = mc.tabLayout('tabTiArnoldToolKit',innerMarginWidth=5, innerMarginHeight=5)
    mc.formLayout(
        form, edit=True, attachForm=((tabs, 'top', 0), (tabs, 'left', 0), (tabs, 'bottom', 0), (tabs, 'right', 0)))
    child1 = mc.columnLayout(adjustableColumn=True)
    mc.frameLayout(label=u'角色', bgc=[0, 0, 0.0], cll=0,cl=1)
    mc.rowColumnLayout(numberOfColumns=4)
    mc.button(label=u'Char Color',width=90,height=30,bgc=[0.13, 0.15, 0.25], c = 'import idmt.maya.titanium.tiEgg as tiEgg;reload(tiEgg);tiEgg.tiEgg().setupChrColorLayer()')
    mc.button(label=u'Char AOV',width=90,height=30,bgc=[0.13, 0.15, 0.25], c = 'import idmt.maya.titanium.tiEgg as tiEgg;reload(tiEgg);tiEgg.tiEgg().setupChrAovLayer()')
    mc.button(label=u'Char IDP',width=90,height=30,bgc=[0.13, 0.15, 0.25], c = 'import idmt.maya.titanium.tiEgg as tiEgg;reload(tiEgg);tiEgg.tiEgg().setupChrIdpLayer()')

    mc.setParent('..')
    mc.setParent('..')

    mc.frameLayout(label=u'场景', bgc=[0, 0, 0.0], cll=0,cl=1)
    mc.rowColumnLayout(numberOfColumns=4)
    mc.button(label=u'Set Color',width=90,height=30,bgc=[0.13, 0.15, 0.25], c = 'import idmt.maya.titanium.tiEgg as tiEgg;reload(tiEgg);tiEgg.tiEgg().setupSetColorLayer()')
    mc.button(label=u'Set AOV',width=90,height=30,bgc=[0.13, 0.15, 0.25], c = 'import idmt.maya.titanium.tiEgg as tiEgg;reload(tiEgg);tiEgg.tiEgg().setupSetAovLayer()')
    mc.button(label=u'Set IDP',width=90,height=30,bgc=[0.13, 0.15, 0.25], c = 'import idmt.maya.titanium.tiEgg as tiEgg;reload(tiEgg);tiEgg.tiEgg().setupSetIdpLayer()')
    mc.setParent('..')
    mc.setParent('..')

    mc.frameLayout(label=u'角色&场景', bgc=[0, 0, 0.0], cll=0,cl=1)
    mc.rowColumnLayout(numberOfColumns=4)
    mc.button(label=u'SetCon',width=90,height=30,bgc=[0.13, 0.15, 0.25], c = 'import idmt.maya.titanium.tiEgg as tiEgg;reload(tiEgg);tiEgg.tiEgg().setupSetConLayer()')

    mc.setParent('..')
    mc.setParent('..')

    mc.setParent('..')
    
    child2 = mc.columnLayout(adjustableColumn=True)
    mc.frameLayout(label=u'IDP输出工具', bgc=[0, 0, 0.0], cll=0,cl=1)
    mc.rowColumnLayout(numberOfColumns=4)
    mc.button(label=u'ID11',width=90,height=30,bgc=[0.13, 0.15, 0.25], c = 'import idmt.maya.titanium.tiPre as tiPre;reload(tiPre);tiPre.rgbInfoExport("ID11")')
    mc.button(label=u'ID12',width=90,height=30,bgc=[0.13, 0.15, 0.25], c = 'import idmt.maya.titanium.tiPre as tiPre;reload(tiPre);tiPre.rgbInfoExport("ID12")')
    mc.button(label=u'ID13',width=90,height=30,bgc=[0.13, 0.15, 0.25], c = 'import idmt.maya.titanium.tiPre as tiPre;reload(tiPre);tiPre.rgbInfoExport("ID13")')
    mc.button(label=u'ID14',width=90,height=30,bgc=[0.13, 0.15, 0.25], c = 'import idmt.maya.titanium.tiPre as tiPre;reload(tiPre);tiPre.rgbInfoExport("ID14")')
    mc.button(label=u'ID检测',width=90,height=30,bgc=[0, 0.5, 0], c = 'import idmt.maya.titanium.tiPre as tiPre;reload(tiPre);tiPre.readRGBInfoTest()')
    mc.setParent('..')
    mc.setParent('..')

    mc.frameLayout(label=u'IDP材质工具', bgc=[0, 0, 0.0], cll=0,cl=1)
    mc.rowColumnLayout(numberOfColumns=4)
    mc.button(label=u'R',width=90,height=30,bgc=[1, 0, 0], c = 'import idmt.maya.titanium.tiPre as tiPre;reload(tiPre);tiPre.ArnoldIDCreat("ArnoldIdpR")')
    mc.button(label=u'G',width=90,height=30,bgc=[0,1, 0], c = 'import idmt.maya.titanium.tiPre as tiPre;reload(tiPre);tiPre.ArnoldIDCreat("ArnoldIdpG")')
    mc.button(label=u'B',width=90,height=30,bgc=[0, 0, 1], c = 'import idmt.maya.titanium.tiPre as tiPre;reload(tiPre);tiPre.ArnoldIDCreat("ArnoldIdpB")')
    mc.button(label=u'M',width=90,height=30,bgc=[0, 0, 0], c = 'import idmt.maya.titanium.tiPre as tiPre;reload(tiPre);tiPre.ArnoldIDCreat("ArnoldIdpM")')
    mc.button(label=u'A',width=90,height=30,bgc=[1, 1, 1], c = 'import idmt.maya.titanium.tiPre as tiPre;reload(tiPre);tiPre.ArnoldIDCreat("ArnoldIdpA")')
    mc.setParent('..')
    mc.setParent('..')

    # mc.button(label=u'Char IDP11',width=90,height=30,bgc=[0.13, 0.15, 0.25])
    # mc.button(label=u'Char IDP12',width=90,height=30,bgc=[0.0, 0.0, 0.0])
    # mc.button(label=u'Char IDP21',width=90,height=30,bgc=[0.0, 0.0, 0.0])
    # mc.button(label=u'Char IDP22',width=90,height=30,bgc=[0.0, 0.5, 0.0])

    mc.setParent('..')


    child3 = mc.columnLayout(adjustableColumn=True)
    mc.frameLayout(label=u'角色', bgc=[0, 0, 0.0], cll=0,cl=1)
    mc.rowColumnLayout(numberOfColumns=4)
    mc.button(label=u'Char Color',width=90,height=30,bgc=[0.13, 0.3, 0.25], c = 'import idmt.maya.titanium.tiEgg as tiEgg;reload(tiEgg);tiEgg.tiEgg().testSetupLayer("chrColor")')
    mc.button(label=u'Glass Color',width=90,height=30,bgc=[0.13, 0.3, 0.25], c = 'import idmt.maya.titanium.tiEgg as tiEgg;reload(tiEgg);tiEgg.tiEgg().testSetupLayer("glassColor")')
    mc.button(label=u'Char AOV',width=90,height=30,bgc=[0.13, 0.3, 0.25], c = 'import idmt.maya.titanium.tiEgg as tiEgg;reload(tiEgg);tiEgg.tiEgg().testSetupLayer("chrAov")')
    mc.setParent('..')
    mc.setParent('..')

    mc.frameLayout(label=u'场景', bgc=[0, 0, 0.0], cll=0,cl=1)
    mc.rowColumnLayout(numberOfColumns=4)
    mc.button(label=u'Set Color',width=90,height=30,bgc=[0.13, 0.3, 0.25], c = 'import idmt.maya.titanium.tiEgg as tiEgg;reload(tiEgg);tiEgg.tiEgg().testSetupLayer("setColor")')
    mc.button(label=u'Set AOV',width=90,height=30,bgc=[0.13, 0.3, 0.25], c = 'import idmt.maya.titanium.tiEgg as tiEgg;reload(tiEgg);tiEgg.tiEgg().testSetupLayer("setAov")')
    mc.setParent('..')
    mc.setParent('..')

    mc.frameLayout(label=u'角色&场景', bgc=[0, 0, 0.0], cll=0,cl=1)
    mc.rowColumnLayout(numberOfColumns=4)
    mc.button(label=u'SetCon',width=90,height=30,bgc=[0.13, 0.3, 0.25], c = 'import idmt.maya.titanium.tiEgg as tiEgg;reload(tiEgg);tiEgg.tiEgg().testSetupLayer("setCon")')
    mc.setParent('..')
    mc.setParent('..')

    mc.setParent('..')


    child4 = mc.columnLayout(adjustableColumn=True)
    mc.button(label = 'c')
    mc.setParent('..')
    mc.tabLayout(tabs, edit=True, tabLabel=(
        (child1, u'分层'), (child2, u'工具'), (child3, u'分层测试'),(child4, u'TMP')))
    mc.showWindow('tiArnoldToolKitUI')    




def tiFindIDPUI():
    
    if mc.window('tiFindIDP', exists=True):
        mc.deleteUI('tiFindIDP')
    mc.window('tiFindIDP', title=u'tiFindIDP -- 星际车神',
              width=320, height=350, sizeable=True)

    form = mc.formLayout()
    tabs = mc.tabLayout('tabTiFindIDP',innerMarginWidth=5, innerMarginHeight=5)
    mc.formLayout(
        form, edit=True, attachForm=((tabs, 'top', 0), (tabs, 'left', 0), (tabs, 'bottom', 0), (tabs, 'right', 0)))
    child1 = mc.columnLayout(adjustableColumn=True)

    items = getIdpFiles().keys()

    mc.textScrollList( 
        numberOfRows=8, 
        allowMultiSelection=True,
        append=items,
        showIndexedItem=4,
        font = 'plainLabelFont',
        height = 50

    )
    mc.setParent('..')


    
    child2 = mc.columnLayout(adjustableColumn=True)
    

    mc.setParent('..')


    child3 = mc.columnLayout(adjustableColumn=True)
    

    mc.setParent('..')


    
    mc.tabLayout(tabs, edit=True, tabLabel=(
        (child1, u'角色'), (child2, u'道具'), (child3, u'场景')))
    mc.showWindow('tiFindIDP')   


def getIdpFiles(objType = 'characters'):

    path = os.path.join(r'\\file-cluster\gdc\Projects\XJCS\Project\data\AssetInfos', 'characters')
    objs = {}
    for root, dirs, files in os.walk(path):
        


        for f in files:
            seps = f.split('_RGB_ID')
            if len(seps) > 1:
                obj = seps[0]
                if obj not in objs:
                    objs[obj] = os.path.join(root, f)
    return objs



#t: chr glass bg
#chr = ['diffuse', 'specular', 'sss', 'transmission']
# createAov('chr', )
def createAov(layer,  aovTypes, driverType, callback = None, *args):
    deletRenderLayers()
    cleanAOVs()
    
    if layer in ['chrColor', 'glassColor', 'chrAov']:
        lightGrp = setupLights()
        if 'Aov' in layer:
            setupRGBLights(lightGrp)

        newGrp = duplicateLightGrp(lightGrp)
        objs = autoSetupRenderFiles(['characters', 'props'])
        objs.append(newGrp)

    elif layer in ['setColor', 'setAov']:
        lightGrp = setupLights('set')
        if 'Aov' in layer:
            setupRGBLights(lightGrp)
        objs = autoSetupRenderFiles(['sets'])
    elif layer in ['setCon']:
        setupLights('set')
        objs = autoSetupRenderFiles(['characters', 'props', 'sets'])

    mc.select(objs, r = True)
    newLayer = creatRenderLayer(layer)
    if callback:
        callback(newLayer)

    

    for at in aovTypes:
        aiAOVCreate(at, driver = driverType)

    # if driverType == 'exr':
    #     driverAttrs = {'aiTranslator': 'exr','mergeAOVs': True,'exrCompression': 3}

    # elif driverType == 'tif':
    #     driverAttrs = {'aiTranslator': 'tif','tiffCompression': 1,'dither': 1, 'tiffFormat': 0}
    # tiBase.batchSetAttrs('defaultArnoldDriver',driverAttrs)



    xjcsDefaultRenderSettings(driverType)
    return newLayer



def setupChrColorRenderLayer(layer):
    
    print '*' * 50
    print u'ChrColor 设置折射反射'
    print '*' * 50


def setupGlassColorRenderLayer(layer):
    
    print '*' * 50
    print u'设置物体MATTE'
    print '*' * 50

def setupAovRenderLayer(layer):
    shaderType = 'aiUtility'
    shdName = 'SHD_%s_RenderLayerShadingGroup' % shaderType
    sgName = 'SG_%s_RenderLayerShadingGroup' % shaderType

    if not mc.objExists(sgName):
        sg, shd = initShadingNetwork(shaderType, sgName, shdName)
    else:
        sg = sgName
        shd = shdName
    mc.setAttr(shd + '.shadeMode', 1)
    mc.connectAttr(sg + '.message', layer + '.shadingGroupOverride', f = True)

    print '*' * 50
    print u'导入灯光，设置灯光 RGB'
    print '*' * 50



def setupSetColorRenderLayer(layer):
    print '*' * 50
    print u'render setting设置不开反射折射，3S属性'
    print '*' * 50


def setupSetAovRenderLayer(layer):
    print '*' * 50
    print u'becuty 层不带材质，主光为红色，补光为绿，边缘光为蓝。（tiff渲染为8位素材）'
    print '*' * 50


def setupSetConRenderLayer(layer):
    shaderType = 'aiShadowMatte'
    shdName = 'SHD_%s_RenderLayerShadingGroup' % shaderType
    sgName = 'SG_%s_RenderLayerShadingGroup' % shaderType

    if not mc.objExists(sgName):
        sg, shd = initShadingNetwork(shaderType, sgName, shdName)
    else:
        sg = sgName


    shdAttrs = {
        'background': 1,
        'backgroundColor': (0,0,0),
        'shadowColor': (1,1,1)
    }
    tiBase.batchSetAttrs(shd, shdAttrs)


    mc.connectAttr(sg + '.message', layer + '.shadingGroupOverride', f = True)

    print '*' * 50
    print u'becuty为角色对场景投影'
    print '*' * 50


def deletRenderLayers():
    pm.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
    layers = mc.ls(type = 'renderLayer')
    for lay in layers:
        if lay != 'defaultRenderLayer':
            mc.delete(lay)




def cleanAOVs():
    aovs = mtoa.aovs.getAOVs()
    for aov in aovs:
        mc.delete(aov.node)
    # aovConnectedNodes = mc.listConnections('defaultArnoldRenderOptions.aovList')
    # if aovConnectedNodes:
    #     for n in aovConnectedNodes:
    #         tiBase.unlockAndDelete(n)


def creatRenderLayer(layerName):
    if pm.objExists(layerName):
        if pm.editRenderLayerGlobals(currentRenderLayer = True, q = True) == layerName:
            pm.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
        pm.delete(layerName)

    renderLayer = pm.createRenderLayer(pm.ls(sl = True), name = layerName, number = 1, noRecurse = True)
    
    pm.setAttr(renderLayer + '.renderable', True)
    pm.setAttr('defaultRenderLayer.renderable', False)
    pm.editRenderLayerGlobals(currentRenderLayer = renderLayer)
    # pm.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
    return renderLayer


def createDriver(driverType):
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

def aiAOVCreate(avoType, dataType = 5, driver = 'exr'):

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

    filterType = 'DEFAULT'
    filterTypeMap = mtoa.aovs.defaultFiltersByName
    
    if filterTypeMap.has_key(avoType):
        filterType = filterTypeMap[avoType]
        
    
    aovNode = tiBase.createNode('aiAOV', 'aiAOV_' + avoType)
    mc.setAttr( aovNode + '.name', avoType, type = 'string')
    mc.setAttr( aovNode + '.type', dataType)
    

    # if not mc.isConnected('defaultArnoldDriver.message', aovNode + '.outputs[0].driver'):
    mc.connectAttr('defaultArnoldDriver.message', aovNode + '.outputs[0].driver', f = True)

    # newDriver = createDriver(driver)
    # mc.connectAttr(newDriver + '.message', aovNode + '.outputs[0].driver', f = True)

    filterNode = 'defaultArnoldFilter' 

    if filterType != 'DEFAULT':
        newFilterName = 'aiAOV_Filter_' + filterType
        if mc.objExists(newFilterName):
            filterNode = newFilterName
        else:
            filterNode = mc.createNode('aiAOVFilter', name = newFilterName)
            mc.setAttr(filterNode + '.aiTranslator', filterType, type = 'string')


    # if not mc.isConnected( filterNode + '.message', aovNode + '.outputs[0].filter'):
    mc.connectAttr( filterNode + '.message', aovNode + '.outputs[0].filter', f = True)

    # if filterType == 'DEFAULT':

    #     if not mc.isConnected('defaultArnoldFilter.message', aovNode + '.outputs[0].filter'):
    #         mc.connectAttr('defaultArnoldFilter.message', aovNode + '.outputs[0].filter', f = True)
    # else:
    #     filterNode = tiBase.createNode('aiAOVFilter', 'aiAOV_Filter_' + filterType)


    # aovConnectedNodes = mc.listConnections(aovNode + '.message', p = True)
    # if aovConnectedNodes:
    #     for node in aovConnectedNodes:
    #         mc.disconnectAttr(aovNode + '.message', node)

    aovListNum = mc.getAttr('defaultArnoldRenderOptions.aovList',  size = True)
    isConnected = False
    for n in range(aovListNum):
        if not mc.listConnections('defaultArnoldRenderOptions.aovList[%d]' % n):
            mc.connectAttr(aovNode + '.message', 'defaultArnoldRenderOptions.aovList[%d]' % n, f = True)
            isConnected = True
            break
    if not isConnected:
        mc.connectAttr(aovNode + '.message', 'defaultArnoldRenderOptions.aovList[%d]' % aovListNum, f = True)

    if not isBuiltinAovs:
        if avoType == 'ao':
            sg, shd = avoShader('ao')
            
        elif avoType == 'fr':
            sg, shd = avoShader('fr')

        mc.connectAttr(shd + '.outColor', aovNode + '.defaultValue', f = True)

        


    return aovNode

def initShadingNetwork(shaderType, sgName, shdName, ):
   
    # for node in [sgName, shdName]:
    #     if mc.objExists(node):
    #         return sgName, shdName
    #         break
    # sg = mc.createNode('shadingEngine', name = sgName)
    # shd = mc.createNode(shaderType, n=shdName)
    sg = mc.sets(renderable = True, noSurfaceShader = True, em = True,n = sgName) 
    shd = mc.shadingNode(shaderType, asShader=True,n=shdName)

    mc.connectAttr(shd + '.outColor', sg + '.surfaceShader', f = True)
    return sg, shd


def avoShader(shaderType):
    shdName = 'SHD_%s_AOV' % shaderType
    sgName = 'SG_%s_AOV' % shaderType

    # shdName = 'aov_shader_%s' % shaderType
    # sgName = 'aov_shader_%s' % shaderType

    
    if mc.objExists(shdName) and mc.objExists(sgName):
        return sgName, shdName

    if shaderType == 'ao':
        sg, shd = initShadingNetwork('aiAmbientOcclusion', sgName, shdName)
        attrs = {
            'samples': 4,
            'falloff': 0.05
        }
        tiBase.batchSetAttrs(shd, attrs)
    elif shaderType == 'fr':
        sg, shd = initShadingNetwork('aiUtility', sgName, shdName)
        
        mc.setAttr(shd + '.shadeMode', 2)

        ramp = mc.shadingNode ('ramp', asShader=True, name= 'tiFresnel_Ramp')
        mc.removeMultiInstance(ramp + '.colorEntryList[1]' , b = 1)
        # mc.setAttr(ramp + '.interpolation', 3)
        # mc.setAttr(ramp + '.colorEntryList[2].position', 1)
        # mc.setAttr(ramp + '.colorEntryList[0].position', 0)
        # mc.setAttr(ramp + '.colorEntryList[2].color', 0,0,0,type = 'double3')
        # mc.setAttr(ramp + '.colorEntryList[0].color', 1,1,1,type = 'double3') 
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

    return sg, shd
    




def autoSetupRenderFiles(keepTypes):

    refFiles = pm.listReferences()

    chrAndProp = []
    scenes = []
    objs = []
    for ref in refFiles:
        if not ref.isLoaded():
            print u'===== 参考没加载 %s, 清除 =====' % ref
            ref.remove()
            
        else:
            tf = tiFile.tiAssetFile(ref.path)
            if tf.assetType not in keepTypes:
                print u'===== 清除不参与渲染的参考 %s,  =====' % ref
                # ref.remove()

            else:
                ref.selectAll()
                objs += mc.ls(sl = True)
    return objs


def setDefaultShader():

    refFiles = pm.listReferences()

    
    for ref in refFiles:
        if not ref.isLoaded():
            print u'===== 参考没加载 %s, 清除 =====' % ref
            ref.remove()
            
        else:
            tf = tiFile.tiAssetFile(ref.path)
      
            for n in ref.nodes():
                if pm.objectType(n) == 'mesh' and n.intermediateObject.get() == False:
                    if tf.assetType == 'characters':
                        n.primaryVisibility.set(0)
                    elif tf.assetType == 'sets':
                        n.primaryVisibility.set(0)
                        n.castsShadows.set(0)
                    
                    mc.sets(n.name(),e=1, forceElement = 'initialShadingGroup')

def setupRGBLights(lightGrp):
    lightGrpChildren = pm.listRelatives(lightGrp, ad = True)
    for l in lightGrpChildren:

        lightName = l.longName().split('|')[-1].split(':')[-1]

        objType = pm.objectType(l)

        if objType == 'transform':
            if not re.match('^key|^fill|^rim', lightName, re.I):
                l.visibility.set(0)
            # if re.match('^sky', lightName, re.IGNORECASE):
            #     l.visibility.set(0)
            
        elif re.search('light', objType, re.I):

            if re.match('^key', lightName, re.I):
                l.color.set(1,0,0)
            elif re.match('^fill', lightName, re.I):
                l.color.set(0,1,0)
            elif re.match('^rim', lightName, re.I):
                l.color.set(0,0,1)

def duplicateLightGrp(lightGrp):
    if mc.objExists('tiLightingGrp'):
        mc.delete('tiLightingGrp')

    dupGrp = mc.duplicate(lightGrp, returnRootsOnly = True, name = lightGrp)
    grp = mc.group(dupGrp, world = True, name = 'tiLightingGrp')
    return grp

def setupLights(light = 'chr'):
    
    tf = tiFile.tiAnimFile()

    ep = tf.ep
    scene = tf.scene
    shot = tf.shot


    excelPath = tf.lightingExcelFile

    if not os.path.lexists(excelPath):
        mc.error(u'=======灯光信息 Excel 文件不存在: %s, 请联系TD及PA处理=======' % excelPath)

    shotAllData = xlrd.open_workbook(excelPath).sheets()[0]
    
    rowMax = shotAllData.nrows
    
    rowID = -1

    for i in range(rowMax):
        print shotAllData.row_values(i)
        exlEp = shotAllData.row_values(i)[0]
        exlScene = shotAllData.row_values(i)[1]
        exlShot = shotAllData.row_values(i)[2]
        if exlEp == ep and exlScene == scene and exlShot == shot:
            rowID = i
            break

    if rowID == -1:
        mc.error(u'=======找不到该镜头对应的信息: %s_%s_%s=======' % (ep, scene, shot))

    rowData = shotAllData.row_values(rowID)
    if len(rowData) < 9:
        mc.error(u'=======Excel表中 I 列中没有数据， 数据格式不对，请联系TD及PA处理=======')


    lightSet =  shotAllData.row_values(rowID)[8]

    if not lightSet:
        mc.error(u'=======镜头 %s_%s_%s 场景时段中没有灯光信息，请联系TD及PA处理=======' % (ep, scene, shot))


    chrLightGrp = setupLightGrps('MSH_Chr_light', light == 'chr')

    setLightGrp = setupLightGrps('MSH_Set_light', light == 'set')

    lightGrp = chrLightGrp if light == 'chr' else setLightGrp


    
    useLightGrp = None

    for lg in lightGrp:
        fullLgName = lg.longName()
        if re.match('^' + lightSet, fullLgName.split('|')[-1].split(':')[-1], re.IGNORECASE):
            useLightGrp = fullLgName
            pm.setAttr(lg + '.visibility', 1)
        else:
            pm.setAttr(lg + '.visibility', 0)

    if not useLightGrp:
        
        mc.error(u'=======场景中找不到 %s_light 组 , 请检查Excel表中 %s_%s_%s 镜头场景时段中的灯光信息 %s，或联系TD及PA处理=======' % (lightSet, ep, scene, shot, lightSet))
    
    return useLightGrp

def setupLightGrps(grpName, isVis):
    
    lightGrp = pm.ls(regex = '*:?(%s(?i))' % grpName) #mc.ls('*:' + grpName, long = True)

    if len(lightGrp) != 1:
        print lightGrp
        print '*:' + grpName
        mc.error(u'=======场景中有多个或0个 %s 灯光组=======' % grpName)

    pm.setAttr(lightGrp[0] + '.visibility', isVis)

    lightGrpChildren =pm.listRelatives(lightGrp[0], type = 'transform', fullPath = True)

    for lg in lightGrpChildren:
        pm.setAttr(lg + '.visibility', 0)

    return lightGrpChildren

def ArnoldAOVCreat(AOVtype='Zdp',passtype=int('5')):
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

            mc.setAttr((zdpDriver+'.aiTranslator'),'exr',type='string')
            mc.setAttr ((zdpDriver+'.exrCompression'), 3)
            mc.setAttr ((zdpDriver+'.halfPrecision'), 1)
            mc.setAttr ((zdpDriver+'.autocrop'), 1)
            mc.setAttr ((AOVArnoldPass+'.type'), 4)

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
        mc.setAttr('defaultArnoldDriver.aiTranslator','tif',type='string')
        mc.setAttr('defaultArnoldDriver.tiffFormat',0)            
        mc.setAttr('defaultArnoldDriver.tiffCompression',1) 
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
        mc.setAttr((ArnoldPass + '.type'),5)   
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
        mc.setAttr ('defaultArnoldDriver.mergeAOVs', 0)
        mc.setAttr('defaultArnoldDriver.prefix','<RenderLayer>_<RenderPass>/<Scene>_<RenderLayer>_<RenderPass>',type='string')               

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
        mc.setAttr((ArnoldPass + '.type'),5)   
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
        mc.setAttr ('defaultArnoldDriver.mergeAOVs', 0)
        mc.setAttr('defaultArnoldDriver.prefix','<RenderLayer>_<RenderPass>/<Scene>_<RenderLayer>_<RenderPass>',type='string')                       
#渲染层创建



def ArnoldShaderAssign(shaderType='Shadow',transparency=0):
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
            if shaderType=='reflection':
                mc.shadingNode('aiStandard', asShader=True,n=Shade)  
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
                mc.setAttr ((Shade+'.falloff'),0.05)
                mc.setAttr ((Shade+'.samples'),4)            
    #反射材质
            if shaderType=='reflection':
                mc.setAttr ((Shade+'.Kd'),0)
                mc.setAttr ((Shade+'.Ks'),1)
                mc.setAttr ((Shade+'.Ks'),1)  
                mc.setAttr ((Shade+'.specularRoughness'),1)
                mc.setAttr ((Shade+'.specularFresnel'),1)                                
                mc.setAttr ((Shade+'.Kr'),1)    
                mc.setAttr ((Shade+'.Fresnel'),1)
                mc.setAttr ((Shade+'.Krn'),1) 
                                                                
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