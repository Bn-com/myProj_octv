# -*- coding: gbk -*-
import re, shutil, os, sys
import maya.cmds as cmd
import maya.mel as mel


def offDefaultRenderLayer():
    # Set default render off
    defRnLayers = cmd.ls(type='renderLayer')
    for item in defRnLayers:
        if re.search('defaultRenderLayer', item):
            cmd.setAttr(item+'.renderable', 0)
    
    # Set only both left and right camera renderable
    cameras = cmd.ls(type='camera')
    for item in cameras:      
        if re.search('Left', item) or re.search('Right', item):
            cmd.setAttr(item+'.renderable', 1)
        else:
            cmd.setAttr(item+'.renderable', 0)
    
    cmd.setAttr("defaultRenderGlobals.enableDefaultLight", 0)
            
    return cameras

def ysGetPrefixName(command):    
    if cmd.window('BD_getInfo_Window', ex=1):
        cmd.deleteUI('BD_getInfo_Window')

    getInfoWindow = cmd.window('BD_getInfo_Window', title='getInfo', menuBar=1, mxb=1,\
                             sizeable=0, resizeToFitChildren=1, mnb=1, wh=[200,120])
    cmd.columnLayout( columnAttach=('both', 5), rowSpacing=5, columnWidth=180 )
    cmd.text(label='input Characters name for Prefix')
    prefixQuery = cmd.textField(text='')
      
    cmd.button(label='OK', w=90, h=35, c='import maya.cmds as cmd\nlayerPrefix=cmd.textField("'+prefixQuery+'", query=True, text=1)+"_"\
    \n'+command+'\ncmd.deleteUI("BD_getInfo_Window")')
    print command
    if command != 'TSR.ysRfM_charHairs(layerPrefix)' and command != 'bdr.createChar_SSS(layerPrefix)':
        cmd.button(label='env', w=90, h=35, c='import maya.cmds as cmd\nlayerPrefix="env_"\
        \n'+command+'\ncmd.deleteUI("BD_getInfo_Window")')
    cmd.setParent('..')       
    
    cmd.showWindow(getInfoWindow)

def setMentalRayRenderSetting():
    if cmd.pluginInfo('Mayatomr',query=True, loaded=True) == 0:
        cmd.loadPlugin('Mayatomr', quiet=True)
        cmd.pluginInfo('Mayatomr', edit=True, autoload=True)
        
    if cmd.objExists('mentalrayItemsList') == 0 and cmd.objExists('miDefaultOptions') == 0:
        cmd.createNode('mentalrayItemsList', name='mentalrayItemsList')  
        cmd.createNode('mentalrayGlobals', name='mentalrayGlobals')  
        cmd.createNode('mentalrayFramebuffer', name='miDefaultFramebuffer') 
        
        cmd.createNode('mentalrayOptions', name='miDefaultOptions') 
        cmd.createNode('mentalrayOptions', name='miContourPreset')
        cmd.createNode('mentalrayOptions', name='Draft')
        cmd.createNode('mentalrayOptions', name='DraftMotionBlur')
        cmd.createNode('mentalrayOptions', name='DraftRapidMotion')
        cmd.createNode('mentalrayOptions', name='Preview')
        cmd.createNode('mentalrayOptions', name='PreviewMotionblur')
        cmd.createNode('mentalrayOptions', name='PreviewRapidMotion')
        cmd.createNode('mentalrayOptions', name='PreviewCaustics')
        cmd.createNode('mentalrayOptions', name='PreviewGlobalIllum')
        cmd.createNode('mentalrayOptions', name='PreviewFinalGather')
        cmd.createNode('mentalrayOptions', name='Production')
        cmd.createNode('mentalrayOptions', name='ProductionMotionblur')
        cmd.createNode('mentalrayOptions', name='ProductionRapidMotion')
        cmd.createNode('mentalrayOptions', name='ProductionFineTrace')
        cmd.createNode('mentalrayOptions', name='ProductionRapidFur')
        cmd.createNode('mentalrayOptions', name='ProductionRapidHair')
        
        cmd.connectAttr('mentalrayGlobals.message', 'mentalrayItemsList.globals', force=True)
        cmd.connectAttr('miDefaultFramebuffer.message', 'mentalrayItemsList.framebuffers', force=True)
        cmd.connectAttr('miDefaultFramebuffer.message', 'mentalrayGlobals.framebuffer', force=True)
        cmd.connectAttr('miDefaultOptions.message', 'mentalrayGlobals.options', force=True)
        
        cmd.connectAttr('miDefaultOptions.message', 'mentalrayItemsList.options', force=True)
        cmd.connectAttr('miContourPreset.message', 'mentalrayItemsList.options', nextAvailable=True, force=True)
        cmd.connectAttr('Draft.message', 'mentalrayItemsList.options', nextAvailable=True, force=True)
        cmd.connectAttr('DraftMotionBlur.message', 'mentalrayItemsList.options', nextAvailable=True, force=True)
        cmd.connectAttr('DraftRapidMotion.message', 'mentalrayItemsList.options', nextAvailable=True, force=True)
        cmd.connectAttr('Preview.message', 'mentalrayItemsList.options', nextAvailable=True, force=True)
        cmd.connectAttr('PreviewMotionblur.message', 'mentalrayItemsList.options', nextAvailable=True, force=True)
        cmd.connectAttr('PreviewRapidMotion.message', 'mentalrayItemsList.options', nextAvailable=True, force=True)
        cmd.connectAttr('PreviewCaustics.message', 'mentalrayItemsList.options', nextAvailable=True, force=True)
        cmd.connectAttr('PreviewGlobalIllum.message', 'mentalrayItemsList.options', nextAvailable=True, force=True)
        cmd.connectAttr('PreviewFinalGather.message', 'mentalrayItemsList.options', nextAvailable=True, force=True)
        cmd.connectAttr('Production.message', 'mentalrayItemsList.options', nextAvailable=True, force=True)
        cmd.connectAttr('ProductionMotionblur.message', 'mentalrayItemsList.options', nextAvailable=True, force=True)
        cmd.connectAttr('ProductionRapidMotion.message', 'mentalrayItemsList.options', nextAvailable=True, force=True)
        cmd.connectAttr('ProductionFineTrace.message', 'mentalrayItemsList.options', nextAvailable=True, force=True)
        cmd.connectAttr('ProductionRapidFur.message', 'mentalrayItemsList.options', nextAvailable=True, force=True)
        cmd.connectAttr('ProductionRapidHair.message', 'mentalrayItemsList.options', nextAvailable=True, force=True)

    cmd.setAttr('miDefaultOptions.minSamples', 0)
    cmd.setAttr('miDefaultOptions.maxSamples', 2)
    cmd.setAttr('miDefaultOptions.contrastR', 0.1)
    cmd.setAttr('miDefaultOptions.contrastG', 0.1)
    cmd.setAttr('miDefaultOptions.contrastB', 0.1)
    cmd.setAttr('miDefaultOptions.contrastA', 0.1)
    cmd.setAttr('miDefaultOptions.filter', 2)
    cmd.setAttr('miDefaultFramebuffer.datatype', 3)
    
def createAmbPass(layerPrefix):
    setMentalRayRenderSetting()
    '''Create ambient render layer and ambient light'''             
    ambLight = cmd.ambientLight(name='ts_ambLight', ambientShade=0, intensity=0)
    ambLight = [item for item in cmd.ls(lights=1) if re.search('ts_ambLight', item)][0]
    
    geo = [item for item in cmd.ls(geometry=1) if cmd.nodeType(item) != 'renderBox']
    cmd.createRenderLayer(geo, ambLight, name=layerPrefix+'ambient', makeCurrent=1)
    cmd.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
    cmd.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')
    cmd.editRenderLayerAdjustment('defaultRenderGlobals.composite')
    cmd.setAttr('defaultRenderGlobals.composite', 1)
    cmd.editRenderLayerAdjustment(ambLight+'.intensity')
    cmd.setAttr(ambLight+'.intensity', 1)
    
def ysFresnelPass(layerPrefix):
    if cmd.objExists('tsFresnelShrSG') == 0:
        rmp = cmd.shadingNode('ramp', asTexture=1, name='tsFresnelContrl')
        rmp2d = cmd.shadingNode('place2dTexture', asUtility=1, name=rmp+'_place2d')
        spInf = cmd.shadingNode('samplerInfo', asUtility=1, name='tsFresnelRatio')
        fresSur = cmd.shadingNode('surfaceShader', asShader=1, name='tsFresnelShr')
        cmd.setAttr(fresSur+'.outMatteOpacity', 0,0,0, type='double3')
        fresSurSG = cmd.sets(renderable=1, noSurfaceShader=1, empty=1, name=fresSur+'SG')
        cmd.connectAttr(spInf+'.facingRatio', rmp+'.uvCoord.uCoord')
        cmd.connectAttr(spInf+'.facingRatio', rmp+'.uvCoord.vCoord')
        cmd.connectAttr(rmp2d+'.outUV', rmp+'.uv', force=True)
        cmd.connectAttr(rmp+'.outColor', fresSur+'.outColor', force=True)
        cmd.connectAttr(fresSur+'.outColor', fresSurSG+'.surfaceShader', force=True)
        mel.eval('showEditor "'+rmp+'"')
        mel.eval('removeMultiInstance -break true "'+rmp+'.colorEntryList[1]"')
        cmd.setAttr(rmp+'.colorEntryList[2].color', 0,0,0, type='double3')
        cmd.setAttr(rmp+'.colorEntryList[0].color', 1,1,1, type='double3')
    if cmd.objExists('tsFresnelShrSG'):
        fresSur = 'tsFresnelShrSG'    
#        modify by ZZJ 2014.3.17
#        geo = [item for item in cmd.ls(geometry=1) if cmd.nodeType(item) != 'renderBox']
#        geo = cmd.ls( sl=1 , dag =1, leaf = 1, type= ['mesh','nurbsSurface']) 
        geo = cmd.ls( sl=1 ) 
        if len(geo) != 0:
            fresLayer = cmd.createRenderLayer(geo, name=layerPrefix+'fresnel', makeCurrent=1)
            cmd.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
            cmd.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')
            cmd.connectAttr(fresSur+'.message', fresLayer+'.shadingGroupOverride', force=True)    

def createAOPass(layerPrefix):
    '''Create ambient occlusion render layer '''
    setMentalRayRenderSetting()
    
    # filter out no-rendered objects for "Ninjago"  line 151 to 172
    unexpectObjs = []
    hidDf = []
    hidRg = []
    hidBr = []
    hidDr = []
    hideDefomers = re.compile('[\w:]DEFORMERS$')
    hideRigs = re.compile('[\w:]RIG$')
    hideBrows = re.compile('[\w:]brow_$') 
    hideDrape = re.compile('[\w:]drape[\w]')  
    
    for unexpectObj in cmd.ls(type='transform'):
        if hideDefomers.search(unexpectObj):
            hidDf = cmd.listRelatives(unexpectObj, allDescendents=1)
            unexpectObjs.extend(hidDf)
    
    for unexpectObj in cmd.ls(type='transform'):
        if hideRigs.search(unexpectObj):
            hidRg = cmd.listRelatives(unexpectObj, allDescendents=1)
            unexpectObjs.extend(hidRg)
            
    for unexpectObj in cmd.ls(type='transform'):
        if hideBrows.search(unexpectObj):
            hidBr = cmd.listRelatives(unexpectObj, allDescendents=1)
            unexpectObjs.extend(unexpectObj)
            
    for unexpectObj in cmd.ls(type='transform'):
        if hideDrape.search(unexpectObj):
            hidDr = cmd.listRelatives(unexpectObj, allDescendents=1)
            unexpectObjs.extend(unexpectObj)
        
    geo = cmd.ls(type=('mesh','nurbsSurface'))
    
    for item in geo:
        if item in unexpectObjs:
            geo.remove(item)
        
    aoLayer = cmd.createRenderLayer(geo, noRecurse=1, name=layerPrefix+'AO', makeCurrent=1)
    cmd.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
    cmd.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')    
    cmd.editRenderLayerAdjustment('miDefaultFramebuffer.datatype')
    cmd.setAttr('miDefaultFramebuffer.datatype', 0)
    cmd.editRenderLayerAdjustment('miDefaultFramebuffer.premultiply')
    cmd.setAttr('miDefaultFramebuffer.premultiply', 1)
    
    # Hide RIG group and brow objects for Ninjago
    for item in cmd.ls(type=('transform','mesh')):
        if hideDefomers.search(item) or hideRigs.search(item) or hideBrows.search(item) or hideDrape.search(item):
            source = cmd.connectionInfo(item+'.visibility', sfd=1)
            if len(source) != 0:
                cmd.editRenderLayerAdjustment(item+'.visibility')
                cmd.disconnectAttr(source, item+'.visibility')
                cmd.setAttr(item+'.visibility', 0)
            else:
                cmd.setAttr(item+'.visibility', 0)
                
            
    # Setup camera background color
    for item in cmd.ls(cameras=True):
        cmd.editRenderLayerAdjustment(item+'.backgroundColor')
        cmd.setAttr(item+'.backgroundColor', 1,1,1, type='double3')
    
    # normal AO shader
    aoTex = cmd.shadingNode('mib_amb_occlusion', asTexture=1, name='aoTex')
    cmd.setAttr(aoTex+'.samples', 128)
    cmd.setAttr(aoTex+'.spread', 1)
    cmd.setAttr(aoTex+'.max_distance', 3)
    aoShr = cmd.shadingNode('surfaceShader', asShader=1, name='aoShader')
    aoShrSG = cmd.sets(name=aoShr+'SG', renderable=1, noSurfaceShader=1, empty=1)
    cmd.connectAttr(aoTex+'.outValue', aoShr+'.outColor', force=True)
    cmd.connectAttr(aoShr+'.outColor', aoShrSG+'.surfaceShader', force=True)             
    cmd.connectAttr(aoShrSG+'.message', aoLayer+'.shadingGroupOverride')
    
    

def createAOPassWithBump(layerPrefix):
    '''Create ambient occlusion render layer '''
    setMentalRayRenderSetting()
    geo = [item for item in cmd.ls(geometry=1) if cmd.nodeType(item) != 'renderBox']
    aoLayer = cmd.createRenderLayer(geo, noRecurse=1, name=layerPrefix+'AO', makeCurrent=1)
    cmd.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
    cmd.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')    
    cmd.editRenderLayerAdjustment('miDefaultFramebuffer.datatype')
    cmd.setAttr('miDefaultFramebuffer.datatype', 1)
    cmd.editRenderLayerAdjustment('miDefaultFramebuffer.premultiply')
    cmd.setAttr('miDefaultFramebuffer.premultiply', 0)
    
    # normal AO shader
    aoTex = cmd.shadingNode('mib_amb_occlusion', asTexture=1, name='aoTex')
    cmd.setAttr(aoTex+'.samples', 128)
    cmd.setAttr(aoTex+'.spread', 1)
    cmd.setAttr(aoTex+'.max_distance', 200)
    aoShr = cmd.shadingNode('surfaceShader', asShader=1, name='aoShader')
    aoShrSG = cmd.sets(name=aoShr+'SG', renderable=1, noSurfaceShader=1, empty=1)
    cmd.connectAttr(aoTex+'.outValue', aoShr+'.outColor', force=True)
    cmd.connectAttr(aoShr+'.outColor', aoShrSG+'.surfaceShader', force=True)
    
    # Filtering material
    shrInLayer = []
    layeredChildren = []
    layeredShr = cmd.ls(type='layeredShader')
    if layeredShr != None:
        for item in layeredShr:
            tmp = cmd.listConnections(item+'.inputs')
            shrInLayer.extend(tmp)
            
        for item in shrInLayer:
            if shrInLayer.count(item) >= 2 and layeredChildren.count(item) == 0:
                layeredChildren.append(item)
            elif shrInLayer.count(item) == 1:
                layeredChildren.append(item)
    
    allMats = [item for item in cmd.ls(materials=True) if cmd.nodeType(item) != 'layeredShader']
    if layeredChildren != None:
        for item in layeredChildren:
            if item in allMats:
                allMats.remove(item)
    try:
        allMats.remove(aoShr)
        allMats.remove('lambert1')
        allMats.remove('particleCloud1')
        allMats.remove('shaderGlow1')
    except:
        pass
    
    ysAOwithTransAndBump(aoShrSG, allMats, aoTex)
    ysAOwithTransAndBump4LayeredShader(layeredChildren, aoTex)
    
    return aoLayer
    
    # Set max distance value
    for item in cmd.ls(type='mib_amb_occlusion'):
        cmd.setAttr(item+'.max_distance', 6)
    
    # Fix some unknown problem caused by layeredShader and transparency map    
    for item in layeredShr:
        if re.search('accessory', item) or item.count('fingernail'):
            cmd.hyperShade(objects=item)            
            cmd.sets(edit=True, forceElement=aoShrSG)
            cmd.select(cl=1)
    
    for item in cmd.ls(geometry=1):
        if re.search('hand', item):
            cmd.select(item)
            cmd.sets(edit=True, forceElement=aoShrSG)
            cmd.select(cl=1)       
        
def ysAOwithTransAndBump(aoShrSG, shaderList, aoTex):    
    for item in cmd.ls(cameras=True):
        cmd.editRenderLayerAdjustment(item+'.backgroundColor')
        cmd.setAttr(item+'.backgroundColor', 1,1,1, type='double3')
    
    for item in shaderList:
        if cmd.objExists(item+'.normalCamera') and cmd.objExists(item+'.transparency'):
            bumpMap = cmd.listConnections(item+'.normalCamera', plugs=1)
            transMap = cmd.listConnections(item+'.transparency', source=1, destination=0)
                  
            # set up AO with bump map
            if bumpMap != None and transMap == None:
                aoShaderBump = cmd.shadingNode('lambert', name='aoShaderBump', asShader=1)
                aoShaderBumpSG = cmd.sets(name=aoShaderBump+'SG', renderable=1, noSurfaceShader=1, empty=1)
                cmd.setAttr(aoShaderBump+'.diffuse', 0)
                cmd.setAttr(aoShaderBump+'.color', 0,0,0, type='double3')
                cmd.connectAttr(aoTex+'.outValue', aoShaderBump+'.incandescence', force=True)
                cmd.connectAttr(aoShaderBump+'.outColor', aoShaderBumpSG+'.surfaceShader', force=True)
                cmd.connectAttr(bumpMap[0], aoShaderBump+'.normalCamera', force=True)
                objs = cmd.hyperShade(objects=item)
                cmd.sets(edit=True, forceElement=aoShaderBumpSG)
                cmd.select(cl=1)
            
            # set up AO with transparency
            if transMap != None and bumpMap == None:
                multiplyDivide = cmd.shadingNode('multiplyDivide', asUtility=1, name='aoMulDv')
                reverse = cmd.shadingNode('reverse', asUtility=1, name='aoReverse')
                cmd.connectAttr(transMap[0]+'.outAlpha', multiplyDivide+'.input1X')
                cmd.connectAttr(transMap[0]+'.outAlpha', multiplyDivide+'.input1Y')
                cmd.connectAttr(transMap[0]+'.outAlpha', multiplyDivide+'.input1Z')
                cmd.connectAttr(transMap[0]+'.outAlpha', reverse+'.inputX')
                cmd.connectAttr(transMap[0]+'.outAlpha', reverse+'.inputY')
                cmd.connectAttr(transMap[0]+'.outAlpha', reverse+'.inputZ')
                
                aoShaderTrans = cmd.shadingNode('surfaceShader', name='aoShaderTrans', asShader=1)
                aoShaderTransSG = cmd.sets(name=aoShaderTrans+'SG', renderable=1, noSurfaceShader=1, empty=1)
                cmd.connectAttr(aoShaderTrans+'.outColor', aoShaderTransSG+'.surfaceShader', force=True)
                cmd.connectAttr(aoTex+'.outValue', multiplyDivide+'.input2', force=True)
                cmd.connectAttr(multiplyDivide+'.output', aoShaderTrans+'.outColor', force=True)
                cmd.connectAttr(reverse+'.output', aoShaderTrans+'.outTransparency',  force=True)
                objs = cmd.hyperShade(objects=item)
                cmd.sets(edit=True, forceElement=aoShaderTransSG)
                cmd.select(cl=1)
                
            # set up AO with transparency and bump
            if transMap != None and bumpMap != None:
                multiplyDivide = cmd.shadingNode('multiplyDivide', asUtility=1, name='aoMulDvTB')
                reverse = cmd.shadingNode('reverse', asUtility=1, name='aoReverseTB')
                cmd.connectAttr(transMap[0]+'.outAlpha', multiplyDivide+'.input1X')
                cmd.connectAttr(transMap[0]+'.outAlpha', multiplyDivide+'.input1Y')
                cmd.connectAttr(transMap[0]+'.outAlpha', multiplyDivide+'.input1Z')
                cmd.connectAttr(transMap[0]+'.outAlpha', reverse+'.inputX')
                cmd.connectAttr(transMap[0]+'.outAlpha', reverse+'.inputY')
                cmd.connectAttr(transMap[0]+'.outAlpha', reverse+'.inputZ')
                
                aoTransBumpShader = cmd.shadingNode('lambert', name='aoTransBumpShader', asShader=1)
                aoTransBumpShaderSG = cmd.sets(name=aoTransBumpShader+'SG', renderable=1, noSurfaceShader=1, empty=1)
                cmd.setAttr(aoTransBumpShader+'.diffuse', 0)
                cmd.setAttr(aoTransBumpShader+'.color', 0,0,0, type='double3')
                cmd.connectAttr(aoTex+'.outValue', multiplyDivide+'.input2', force=True)
                cmd.connectAttr(multiplyDivide+'.output', aoTransBumpShader+'.incandescence', force=True)
                cmd.connectAttr(reverse+'.output', aoTransBumpShader+'.transparency', force=True)
                cmd.connectAttr(aoTransBumpShader+'.outColor', aoTransBumpShaderSG+'.surfaceShader', force=True)
                cmd.connectAttr(bumpMap[0], aoTransBumpShader+'.normalCamera', force=True)
                objs = cmd.hyperShade(objects=item)
                cmd.sets(edit=True, forceElement=aoTransBumpShaderSG)
                cmd.select(cl=1)            
        
        # AO for others
        objs = cmd.hyperShade(objects=item)
        cmd.sets(edit=True, forceElement=aoShrSG)
        cmd.select(cl=1)
       
def ysAOwithTransAndBump4LayeredShader(shaderList, aoTex):    
    for item in shaderList:
        if cmd.objExists(item+'.normalCamera') and cmd.objExists(item+'.transparency'):
            bumpMap = cmd.listConnections(item+'.normalCamera', plugs=1)
            transMap = cmd.listConnections(item+'.transparency', source=1, destination=0)
           
            # set up AO with bump map
            if bumpMap != None and transMap == None:
                aoShaderBump = cmd.shadingNode('lambert', name='aoShaderBump', asShader=1)
                cmd.setAttr(aoShaderBump+'.diffuse', 0)
                cmd.setAttr(aoShaderBump+'.color', 0,0,0, type='double3')
                cmd.connectAttr(aoTex+'.outValue', aoShaderBump+'.incandescence', force=True)
                cmd.connectAttr(bumpMap[0], aoShaderBump+'.normalCamera', force=True)
                destination = cmd.listConnections(item+'.outColor', source=0, destination=1, plugs=1)
                cmd.connectAttr(aoShaderBump+'.outColor', destination[0], force=True)

            
            # set up AO with transparency
            if transMap != None and bumpMap == None:
                multiplyDivide = cmd.shadingNode('multiplyDivide', asUtility=1, name='aoMulDv')
                reverse = cmd.shadingNode('reverse', asUtility=1, name='aoReverse')
                cmd.connectAttr(transMap[0]+'.outAlpha', multiplyDivide+'.input1X')
                cmd.connectAttr(transMap[0]+'.outAlpha', multiplyDivide+'.input1Y')
                cmd.connectAttr(transMap[0]+'.outAlpha', multiplyDivide+'.input1Z')
                cmd.connectAttr(transMap[0]+'.outAlpha', reverse+'.inputX')
                cmd.connectAttr(transMap[0]+'.outAlpha', reverse+'.inputY')
                cmd.connectAttr(transMap[0]+'.outAlpha', reverse+'.inputZ')
                
                aoShaderTrans = cmd.shadingNode('surfaceShader', name='aoShaderTrans', asShader=1)
                cmd.connectAttr(aoTex+'.outValue', multiplyDivide+'.input2', force=True)
                cmd.connectAttr(multiplyDivide+'.output', aoShaderTrans+'.outColor', force=True)
                cmd.connectAttr(reverse+'.output', aoShaderTrans+'.outTransparency',  force=True)
                destination = cmd.listConnections(item+'.outColor', source=0, destination=1, plugs=1)
                cmd.connectAttr(aoShaderTrans+'.outColor', destination[0], force=True)          
                                
            # set up AO with transparency and bump
            if transMap != None and bumpMap != None:
                multiplyDivide = cmd.shadingNode('multiplyDivide', asUtility=1, name='aoMulDvTB')
                reverse = cmd.shadingNode('reverse', asUtility=1, name='aoReverseTB')
                cmd.connectAttr(transMap[0]+'.outAlpha', multiplyDivide+'.input1X')
                cmd.connectAttr(transMap[0]+'.outAlpha', multiplyDivide+'.input1Y')
                cmd.connectAttr(transMap[0]+'.outAlpha', multiplyDivide+'.input1Z')
                cmd.connectAttr(transMap[0]+'.outAlpha', reverse+'.inputX')
                cmd.connectAttr(transMap[0]+'.outAlpha', reverse+'.inputY')
                cmd.connectAttr(transMap[0]+'.outAlpha', reverse+'.inputZ')
                
                aoTransBumpShader = cmd.shadingNode('lambert', name='aoTransBumpShader', asShader=1)
                cmd.setAttr(aoTransBumpShader+'.diffuse', 0)
                cmd.setAttr(aoTransBumpShader+'.color', 0,0,0, type='double3')
                cmd.connectAttr(aoTex+'.outValue', multiplyDivide+'.input2', force=True)
                cmd.connectAttr(multiplyDivide+'.output', aoTransBumpShader+'.incandescence', force=True)
                cmd.connectAttr(reverse+'.output', aoTransBumpShader+'.transparency', force=True)
                cmd.connectAttr(bumpMap[0], aoTransBumpShader+'.normalCamera', force=True)
                destination = cmd.listConnections(item+'.outColor', source=0, destination=1, plugs=1)
                cmd.connectAttr(aoTransBumpShader+'.outColor', destination[0], force=True)
                
def SetColorBlackOrWhite(color):
    '''set materials on current layer being black ro white'''
    
    
    mats = [item for item in cmd.ls(materials=1) if cmd.nodeType(item) != 'layeredShader'\
            and cmd.nodeType(item) != 'surfaceShader' and cmd.nodeType(item) != 'volumeFog']
    try:
        mats.remove('lambert1')
        mats.remove('particleCloud1')
        mats.remove('shaderGlow1')
    except:
        pass

    for item in mats:
        try:
            cmd.editRenderLayerAdjustment(item+'.color')
            cmd.editRenderLayerAdjustment(item+'.ambientColor')
            cmd.editRenderLayerAdjustment(item+'.incandescence')
        except:
            print 'some shader blocks this script'
            return
        
        # turn ambient color and incandescence color
        ambient = cmd.listConnections(item+'.ambientColor', plugs=1, s=1, d=0)
        if ambient != None:
            try:
                cmd.disconnectAttr(ambient[0], item+'.ambientColor')
                cmd.setAttr(item+'.ambientColor', 0,0,0, type='double3')
            except:
                pass
        if ambient == None:
            cmd.setAttr(item+'.ambientColor', 0,0,0, type='double3')
        
        incandescence = cmd.listConnections(item+'.incandescence', plugs=1, s=1, d=0)
        if incandescence != None:
            try:
                cmd.disconnectAttr(incandescence[0], item+'.incandescence')
                cmd.setAttr(item+'.incandescence', 0,0,0, type='double3')
            except:
                pass
        if ambient == None:
            cmd.setAttr(item+'.incandescence', 0,0,0, type='double3')
            
        
        # set specular color 
        map = cmd.listConnections(item+'.color', plugs=1, s=1, d=0)
        if map != None:
            cmd.disconnectAttr(map[0], item+'.color')
            if color == 'white':
                cmd.setAttr(item+'.color', 1,1,1, type='double3')
            if color == 'black':
                cmd.setAttr(item+'.color', 0,0,0, type='double3')
        if map == None:
            if color == 'white':
                cmd.setAttr(item+'.color', 1,1,1, type='double3')
            if color == 'black':
                cmd.setAttr(item+'.color', 0,0,0, type='double3')
        
        # turn off reflection color
        if cmd.objExists(item+'.reflectedColor'):
            cmd.editRenderLayerAdjustment(item+'.reflectedColor')
            reflection = cmd.listConnections(item+'.reflectedColor', plugs=1, s=1, d=0)
            if reflection != None:
                try:
                    cmd.disconnectAttr(reflection[0], item+'.reflectedColor')
                    cmd.setAttr(item+'.reflectedColor', 0,0,0, type='double3')
                except:
                    pass
            if reflection == None:
                cmd.setAttr(item+'.reflectedColor', 0,0,0, type='double3')
            
    
    return mats

def creatSpecPass(layerPrefix):
    '''Specular pass for adjustment specular intensity'''
    geo = [item for item in cmd.ls(geometry=1) if cmd.nodeType(item) != 'renderBox']
    lights = [item for item in cmd.ls(lights=1) if cmd.nodeType(item) != 'ambientLight']
    setMentalRayRenderSetting()
    if len(lights) != 0:
        cmd.createRenderLayer(geo, lights, name=layerPrefix+'specular', makeCurrent=1)
        cmd.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
        cmd.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')    
        cmd.editRenderLayerAdjustment('miDefaultFramebuffer.datatype')
        cmd.setAttr('miDefaultFramebuffer.datatype', 1)
        cmd.editRenderLayerAdjustment('miDefaultFramebuffer.premultiply')
        cmd.setAttr('miDefaultFramebuffer.premultiply', 0)
        for light in lights:
            cmd.editRenderLayerAdjustment(light+'.emitDiffuse')
            cmd.setAttr(light+'.emitDiffuse', 0)
            
        SetColorBlackOrWhite('black')

def LgtPass(lgtName, layerPreFix):
#    '''LGT pass for RGB lighting. The following code as Winx's neutral function'''
#    geo = [item for item in cmd.ls(geometry=1) if cmd.nodeType(item) != 'renderBox']
#    lights = [item for item in cmd.ls(lights=1) if cmd.nodeType(item) != 'ambientLight']
#    if len(lights) != 0:
#        cmd.createRenderLayer(geo, lights, name=layerPreFix+lgtName, makeCurrent=1)
#        for light in lights:
#            cmd.editRenderLayerAdjustment(light+'.emitSpecular')
#            cmd.setAttr(light+'.emitSpecular', 0)
#            mats = SetColorBlackOrWhite('white')
#    if len(lights) == 0:
#        print 'current scene has no valid light !'        

    '''The following is code are using material override of render layer'''
    lgtLayer = ''
    geo = [item for item in cmd.ls(geometry=1) if cmd.nodeType(item) != 'renderBox']
    lights = [item for item in cmd.ls(lights=1) if cmd.nodeType(item) != 'ambientLight']
    if len(lights)!=0 and len(geo)!=0:
        lgtLayer = cmd.createRenderLayer(geo, lights, name=layerPreFix+lgtName, makeCurrent=1)
        for light in lights:
            cmd.editRenderLayerAdjustment(light+'.emitSpecular')
            cmd.setAttr(light+'.emitSpecular', 0)
    if len(lights) == 0:
        print 'current scene has no valid light !'  
    
    whiteLambert = cmd.shadingNode('lambert', n='whiteLambert', asShader=1)
    whiteLambertSG = cmd.sets(name=whiteLambert+'SG', renderable=1, noSurfaceShader=1, empty=1)
    cmd.connectAttr(whiteLambert+'.outColor', whiteLambertSG+'.surfaceShader', force=True)
    cmd.setAttr(whiteLambert+'.color', 1,1,1, type='double3')
    
    cmd.connectAttr(whiteLambertSG+'.message', lgtLayer+'.shadingGroupOverride', force=1)
    
     
    # set specular color to black
    #    for mat in mats:
    #        if cmd.objExists(mat+'.specularColor'):
    #            cmd.editRenderLayerAdjustment(mat+'.specularColor')
    #            specColor = cmd.listConnections(mat+'.specularColor', plugs=1, s=1, d=0)
    #            if specColor != None:
    #                cmd.disconnectAttr(specColor[0], mat+'.specularColor')
    #                cmd.setAttr(mat+'.specularColor', 0,0,0, type='double3')
    #            if specColor == None:
    #                cmd.setAttr(mat+'.specularColor', 0,0,0, type='double3')
   
def setLightsColor(lightColor):
    '''adjust selected lights color in render Layers'''    
    
    if cmd.editRenderLayerGlobals(query=True, currentRenderLayer=True) == 'defaultRenderLayer':
        return
    lights = cmd.ls(lights=True)
    if lights != None:
        for item in lights:
            cmd.editRenderLayerAdjustment(item+'.color')   
            cmd.editRenderLayerAdjustment(item+'.shadowColor')               
            if lightColor == 'red':
                cmd.setAttr(item+'.color', 1,0,0, type='double3')
            if lightColor == 'green':
                cmd.setAttr(item+'.color', 0,1,0, type='double3')
            if lightColor == 'blue':
                cmd.setAttr(item+'.color', 0,0,1, type='double3')
            if lightColor == 'redShd':
                cmd.setAttr(item+'.shadowColor', 1,0,0, type='double3')
                cmd.setAttr(item+'.color', 0,0,0, type='double3')
            if lightColor == 'greenShd':
                cmd.setAttr(item+'.shadowColor', 0,1,0, type='double3')
                cmd.setAttr(item+'.color', 0,0,0, type='double3')
            if lightColor == 'blueShd':
                cmd.setAttr(item+'.shadowColor', 0,0,1, type='double3')
                cmd.setAttr(item+'.color', 0,0,0, type='double3')

def normalPass(layerPrefix):
# Use smooth surface without bump information
    setMentalRayRenderSetting()   
    
    hideDefomers = re.compile('[\w:]DEFORMERS$')
    hideRigs = re.compile('[\w:]RIG$')
    brows = re.compile('[\w:]brow_$') 
    
    geo = [item for item in cmd.ls(geometry=1) if cmd.nodeType(item) != 'renderBox']
    if len(geo) == 0:
        return
    normal = cmd.createRenderLayer(geo, name=layerPrefix+'nomal', makeCurrent=1)
    cmd.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
    cmd.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')
    cmd.editRenderLayerAdjustment('miDefaultFramebuffer.datatype')
    cmd.setAttr('miDefaultFramebuffer.datatype', 1)
    cmd.editRenderLayerAdjustment('miDefaultFramebuffer.premultiply')
    cmd.setAttr('miDefaultFramebuffer.premultiply', 1)
    
    # Hide RIG group and brow objects for Ninjago
    for item in cmd.ls(type='transform'):
        if hideRigs.search(item) or brows.search(item) or hideDefomers.search(item):
            try:
                cmd.setAttr(item+'.visibility', 0)
            except:
                cmd.editRenderLayerAdjustment(item+'.visibility')
                mel.eval('source "D:/Alias/MAYA2011x64/2013/startup/channelBoxCommand.mel"')
                mel.eval('CBdeleteConnection ("'+item+'" + ".v")')
                cmd.setAttr(item+'.visibility', 0)   
                
    
    if cmd.objExists('norShaderSG'):
        cmd.connectAttr('norShaderSG.message', normal+'.shadingGroupOverride', force=True)
        
    if cmd.objExists('norShaderSG') == 0:
        norTex = cmd.shadingNode('mib_amb_occlusion', asTexture=1, name='norTex')
        cmd.setAttr(norTex+'.samples', 128)
        cmd.setAttr(norTex+'.max_distance', 3)
        cmd.setAttr(norTex+'.output_mode', 3)
        norShr = cmd.shadingNode('surfaceShader', asShader=1, name='norShader')
        norShrSG = cmd.sets(name=norShr+'SG', renderable=1, noSurfaceShader=1, empty=1)
        cmd.connectAttr(norTex+'.outValue', norShr+'.outColor', force=True)
        cmd.connectAttr(norShr+'.outColor', norShrSG+'.surfaceShader', force=True)
        cmd.connectAttr(norShrSG+'.message', normal+'.shadingGroupOverride', force=True)

# Use information of bump node        
#    renderLayers = [item for item in cmd.ls(type='renderLayer') if re.search('defaultRenderLayer', item) == None]
#    aoLayer = []
#    count = 0
#    if len(renderLayers) == 0:
#        currentAO = createAOPass(layerPrefix)
#        normalLayer = cmd.rename(currentAO, layerPrefix+'normal')
#        cmd.editRenderLayerGlobals(currentRenderLayer=normalLayer)
#        for item in cmd.ls(type='mib_amb_occlusion'):
#            cmd.editRenderLayerAdjustment(item+'.output_mode')
#            cmd.setAttr(item+'.output_mode', 3)
#    
#    if len(renderLayers) != 0:
#        for ao in renderLayers:
#            if re.search('AO', ao):
#                count = 1
#                cmd.editRenderLayerGlobals(currentRenderLayer=ao)
#                ambOcc = cmd.ls(type='mib_amb_occlusion')
#                if ambOcc != None:                
#                    normalLayer = cmd.duplicate(ao, inputConnections=True)
#                    normalLayer = cmd.rename(normalLayer, layerPrefix+'normal')
#                    cmd.editRenderLayerGlobals(currentRenderLayer=normalLayer)
#                    for item in ambOcc:
#                        cmd.editRenderLayerAdjustment(item+'.output_mode')
#                        cmd.setAttr(item+'.output_mode', 3)
#                else: 
#                    print 'There is no mib_amb_occlusion node at all !'
#
#    del(aoLayer)

def castShaow(layerPrefix):
    allShapes = cmd.ls(geometry=1)
    geo = cmd.ls(geometry=1)
    selected = cmd.ls(sl=True, dag=True)
    allLights = cmd.ls(lights=1)
    light = []
    for item in allLights:
        if item in selected:
            light.append(item)
    
    # Check light and selected objects
    if len(selected) == 0:
        cmd.confirmDialog(title='Confirm', message='Nothing selected!', button='Please drag you mouse on something')
        return
    if len(light) == 0:
        cmd.confirmDialog(title='Confirm', message='Nothing selected!', button='Please select a light object')
        return
    for item in selected:
        if item in allShapes:
            allShapes.remove(item)
    others = allShapes
    
    # Create render layer and userbackground shader
    castShadow = cmd.createRenderLayer(geo, light, name=layerPrefix+'castShadow', makeCurrent=1)
    cShadow = cmd.shadingNode('useBackground', asShader=1, name='cShadow')
    cShadowSG = cmd.sets(name=cShadow+'SG', renderable=1, noSurfaceShader=1, empty=1)
    cmd.setAttr(cShadow+'.reflectivity', 0)
    cmd.setAttr(cShadow+'.reflectionLimit', 0)
    cmd.connectAttr(cShadow+'.outColor', cShadowSG+'.surfaceShader', force=True)
    cmd.connectAttr(cShadowSG+'.message', castShadow+'.shadingGroupOverride', force=True)
    
    # set up visibility for all geometry object
    for item in selected:
        if cmd.objExists(item+'.primaryVisibility'):
            cmd.editRenderLayerAdjustment(item+'.primaryVisibility')
            cmd.setAttr(item+'.primaryVisibility', 0)
            cmd.setAttr(item+'.receiveShadows', 0)
    for item in others:
        if cmd.objExists(item+'.castsShadows'):
            cmd.editRenderLayerAdjustment(item+'.castsShadows')
            cmd.setAttr(item+'.castsShadows', 0)    
    
def castAO(layerPrefix):
    geo = cmd.ls(geometry=1)
    selected = cmd.ls(sl=True, dag=True)
   
    # Check selected objects
    if len(selected) == 0 and len(geo) != 0:
        cmd.confirmDialog(title='Confirm', message='Nothing selected!', button='Please drag you mouse on something')
        return
    
    for item in selected:
        if item in geo:
            geo.remove(item)
    others = geo
    
    # Create render layer and AO shader
    castAO = cmd.createRenderLayer(cmd.ls(geometry=1), name=layerPrefix+'castAO', makeCurrent=1)
    setMentalRayRenderSetting()
    cmd.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
    cmd.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')
    
    # set cameras backgroundColor 
    for cam in cmd.listCameras(p=1):
        cmd.editRenderLayerAdjustment(cam+'.backgroundColor')
        cmd.setAttr(cam+'.backgroundColor', 1,1,1, type='double3')
    
    aoTex = cmd.shadingNode('mib_amb_occlusion', name='aoTexture', asTexture=1)
    cmd.setAttr(aoTex+'.samples', 128)
    cmd.setAttr(aoTex+'.max_distance', 6)
    aoShader = cmd.shadingNode('surfaceShader', asShader=1, name='aoShader')
    aoShaderSG = cmd.sets(name=aoShader+'SG', renderable=1, noSurfaceShader=1, empty=1)
    cmd.connectAttr(aoTex+'.outValue', aoShader+'.outColor', force=True)
    cmd.connectAttr(aoShader+'.outColor', aoShaderSG+'.surfaceShader', force=True)
    cmd.connectAttr(aoShaderSG+'.message', castAO+'.shadingGroupOverride', force=True)
    
    # set up visibility for all geometry object
    for item in selected:
        if cmd.objExists(item+'.primaryVisibility'):
            cmd.editRenderLayerAdjustment(item+'.primaryVisibility')
            cmd.setAttr(item+'.primaryVisibility', 0)

def creatColorPass(layerPrefix):
    '''Create beauty render layer'''         
    setMentalRayRenderSetting()        
    geo = [item for item in cmd.ls(geometry=1) if cmd.nodeType(item) != 'renderBox']
    lights = cmd.ls(lights=1)    
    if len(lights) == 0:
        print u"������û���κεƹ⣡"
        return
    cmd.createRenderLayer(geo, lights, name=layerPrefix+'Color', makeCurrent=1)
    cmd.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
    cmd.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')
    
def createDepthPass(layerPrefix):    
#    modify by ZZJ 2014.3.17
#    geo = cmd.ls(geometry=1)
    
    geo = cmd.ls(sl=1)            
    if geo != None or geo != []: 
        # create depth layer
        depthLayer = cmd.createRenderLayer(geo, noRecurse=1, name=layerPrefix+'depth', makeCurrent=1)
        setMentalRayRenderSetting()
        cmd.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
        cmd.setAttr('defaultRenderGlobals.currentRenderer', 'mayaSoftware', type='string')
        cmd.editRenderLayerAdjustment('defaultRenderGlobals.imageFormat')
        cmd.setAttr('defaultRenderGlobals.imageFormat', 10)
        cmd.setAttr("defaultRenderGlobals.currentRenderer","mentalRay" ,type ="string" )
        # create depth shader
        ifo = cmd.shadingNode('samplerInfo', asUtility=1, name='depInfo')
        mul = cmd.shadingNode('multiplyDivide', asUtility=1, name='depMul')
        rng = cmd.shadingNode('setRange', asUtility=1, name='depRng')
        depshr = cmd.shadingNode('surfaceShader', name='ts_Depth', asShader=1)
        depshrSG = cmd.sets(name=depshr+'SG', renderable=1, noSurfaceShader=1, empty=1)
        
        cmd.addAttr(depshr, longName='nearClipPlane', attributeType='float', dv=1)
        cmd.addAttr(depshr, longName='farClipPlane', attributeType='float',dv=500)
        cmd.connectAttr(ifo+'.pointCameraZ', mul+'.input1X')
        cmd.setAttr(mul+'.input2X', -1.0)
        cmd.connectAttr(mul+'.outputX', rng+'.valueX')
        cmd.expression(o=rng, s='oldMin.oldMinX='+depshr+'.nearClipPlane;\
        \noldMax.oldMaxX='+depshr+'.farClipPlane;')
        
        cmd.connectAttr(rng+'.outValueX', depshr+'.outColorR', force=True)
        cmd.connectAttr(rng+'.outValueX', depshr+'.outColorG', force=True)
        cmd.connectAttr(rng+'.outValueX', depshr+'.outColorB', force=True)    
        cmd.connectAttr(depshr+'.outColor', depshrSG+'.surfaceShader')
        
        # Adjust parameters
        cmd.addAttr(depshr, longName='black', attributeType='float')
        cmd.addAttr(depshr, longName='white', attributeType='float')
        cmd.connectAttr(depshr+'.black', rng+'.minX')
        cmd.connectAttr(depshr+'.white', rng+'.maxX')
        cmd.setAttr(depshr+'.black', 0)
        cmd.setAttr(depshr+'.white', 1)
        cmd.connectAttr(depshrSG+'.message', depthLayer+'.shadingGroupOverride', force=True)
        cmd.select(cl=True)
        
        cams = cmd.listCameras()
        attrs = ['nearClipPlane', 'farClipPlane']
        for cam in cams:
            for attr in attrs:
                connects = cmd.listConnections(cam+'.'+attr, s=1, d=0, c=1, p=1)
                if connects != None:
                    for i in range(0, len(connects), 2):
                        cmd.disconnectAttr(connects[i+1], connects[i]) 

def createReflectionPass(layerPrefix):
    allShapes = cmd.ls(geometry=1)
    geo = cmd.ls(geometry=1)
    selected = cmd.ls(sl=True, dag=True)
    allLights = cmd.ls(lights=1)
    
    # Check light and selected objects
    if len(selected) == 0:
        cmd.confirmDialog(title='Confirm', message='Nothing selected!', button='Please drag you mouse on something')
        return
    if len(allLights) == 0:
        cmd.confirmDialog(title='Confirm', message=u'������û�еƹ�', button='OK')
        return
    if len(geo) == 0:
        cmd.confirmDialog(title='Confirm', message=u'����һ���ճ���', button='OK')
        return
    
    setMentalRayRenderSetting()
    
    for item in selected:
        if item in allShapes:
            allShapes.remove(item)
        if item in allLights:
            allShapes.remove(item)
    others = allShapes
    
    # Create render layer and userbackground shader
    if len(allLights) != 0:
        refLayer = cmd.createRenderLayer(geo, allLights, name=layerPrefix+'Refl', makeCurrent=1)
    if len(allLights) == 0:
        refLayer = cmd.createRenderLayer(geo, name=layerPrefix+'Refl', makeCurrent=1)
    cmd.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
    cmd.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')    
    cmd.editRenderLayerAdjustment('miDefaultFramebuffer.datatype')
    cmd.setAttr('miDefaultFramebuffer.datatype', 1)
    cmd.editRenderLayerAdjustment('miDefaultFramebuffer.premultiply')
    cmd.setAttr('miDefaultFramebuffer.premultiply', 0)
    
    refShr = cmd.shadingNode('useBackground', asShader=1, name='Refl')
    refShrSG = cmd.sets(name=refShr+'SG', renderable=1, noSurfaceShader=1, empty=1)
    cmd.setAttr(refShr+'.reflectivity', 1)
    cmd.setAttr(refShr+'.reflectionLimit', 1)
    cmd.setAttr(refShr+'.shadowMask', 0)
    cmd.connectAttr(refShr+'.outColor', refShrSG+'.surfaceShader', force=True)
    cmd.select(selected)
    cmd.sets(edit=True, forceElement=refShrSG)
    
    
    # set up visibility for all geometry object
    for item in selected:
        if cmd.objExists(item+'.primaryVisibility'):
            cmd.editRenderLayerAdjustment(item+'.primaryVisibility')
            cmd.setAttr(item+'.primaryVisibility', 1)
    for item in others:
        if cmd.objExists(item+'.castsShadows'):
            cmd.editRenderLayerAdjustment(item+'.primaryVisibility')
            cmd.setAttr(item+'.primaryVisibility', 0)    

def createIndirectPass(layerPrefix):
    # fix irradianceColor 
    for Irra in cmd.ls(materials=1):
        if cmd.objExists(Irra+'.miIrradianceColor'):
            cmd.setAttr(Irra+'.miIrradianceColor', 1,1,1, type='double3')            
    geo = cmd.ls(geometry=1)
    if len(geo) == 0:
        cmd.confirmDialog(title='Confirm', message='Empty scene', button='OK')
        return
    
    setMentalRayRenderSetting()
    
    if cmd.objExists('indrIBL') == 0:
        cmd.editRenderLayerGlobals(currentRenderLayer='defaultRenderLayer')
        indrIBL = cmd.createNode('mentalrayIblShape', name='indrIBL')  
        cmd.setAttr(indrIBL+'.mapping', 1)
        cmd.setAttr(indrIBL+'.visibleInFinalGather', 0)
        cmd.setAttr(indrIBL+'.primaryVisibility', 0)
        cmd.setAttr(indrIBL+'.texture', '//File-cluster/GDC/Resource/Support/Maya/Python/IDMT/TTMS/IBL/DH206LX.hdr', type='string')
        try:
            cmd.connectAttr(indrIBL+'.message', 'mentalrayGlobals.imageBasedLighting', force=True)
        except:
            pass
        
    if cmd.objExists('indrIBL'):
        cmd.editRenderLayerGlobals(currentRenderLayer='defaultRenderLayer')
        cmd.setAttr(indrIBL+'.visibleInFinalGather', 0)
        cmd.setAttr(indrIBL+'.primaryVisibility', 0)
        try:
            cmd.connectAttr('indrIBL.message', 'mentalrayGlobals.imageBasedLighting', force=True)
        except:
            pass
        
    cmd.setAttr('miDefaultOptions.finalGather', 0)
    indirectLayer = cmd.createRenderLayer(geo, name=layerPrefix+'indirect', makeCurrent=1)   
    cmd.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
    cmd.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')
    cmd.editRenderLayerAdjustment('miDefaultFramebuffer.datatype')
    cmd.setAttr('miDefaultFramebuffer.datatype', 1)
    cmd.editRenderLayerAdjustment('miDefaultFramebuffer.premultiply')
    cmd.setAttr('miDefaultFramebuffer.premultiply', 0)
    cmd.editRenderLayerAdjustment('miDefaultOptions.finalGather')
    cmd.editRenderLayerAdjustment(indrIBL+'.visibleInFinalGather')
    cmd.setAttr(indrIBL+'.visibleInFinalGather', 1)
    cmd.setAttr('miDefaultOptions.finalGather', 1)
    cmd.setAttr('miDefaultOptions.finalGatherRays', 200)
    cmd.setAttr('miDefaultOptions.maxReflectionRays', 0)
    cmd.setAttr('miDefaultOptions.maxRefractionRays', 0)
    SetColorBlackOrWhite('white')  

    
    # Change shader's attributes
    for item in cmd.ls(materials=True):
        if cmd.objExists(item+'.specularColor'):
            cmd.editRenderLayerAdjustment(item+'.specularColor')
            connects = cmd.listConnections(item+'.specularColor', s=1, d=0, p=1)
            if connects == None:
                cmd.setAttr(item+'.specularColor', 0,0,0, type='double3')
            if connects != None:
                cmd.disconnectAttr(connects[0], item+'.specularColor')
                cmd.setAttr(item+'.specularColor', 0,0,0, type='double3')
        
        if cmd.objExists(item+'.diffuse'):
            cmd.editRenderLayerAdjustment(item+'.diffuse')
            connects = cmd.listConnections(item+'.diffuse', s=1, d=0, p=1)
            if connects == None:
                cmd.setAttr(item+'.diffuse', 1)
            if connects != None:
                cmd.disconnectAttr(connects[0], item+'.diffuse')
                cmd.setAttr(item+'.diffuse', 1)
            
                      
def createChar_SSS(layerPrefix):
    '''create sss shader for selected objects and create a renderLayer for that'''
    geo = cmd.ls(geometry=1)
    selected = cmd.ls(sl=True, dag=True)
   
    # Check selected objects
    if len(selected) == 0 and len(geo) != 0:
        cmd.confirmDialog(title='Confirm', message='Nothing selected!', button='Please drag you mouse on something')
        return

    for item in selected:
        if item in geo:
            geo.remove(item)
    others = geo
    
    # get texName
    fileName = cmd.file(query=1, sn=1, shn=1)
    path = cmd.workspace(query=1, rd=1)+'sourceimages/'
    if len(fileName) == 0:
        print 'current scene needs a name !'
        return
    if len(fileName) > 0:
        pathName = path+fileName[0:-3]+'.lmap'  
    
    setMentalRayRenderSetting()
    
    if cmd.objExists('light_CharSSS_Grp') == 0:
        mel.eval("file -import -type \"mayaBinary\" (\"//File-cluster/GDC/Resource/Support/Maya/Python/IDMT/TTMS/IBL/ssslight.mb\")")
        
    sssLight = cmd.ls('light_CharSSS_Grp', dag=True)
    sssLayer = cmd.createRenderLayer(cmd.ls(geometry=1), sssLight, name=layerPrefix+'SSS', makeCurrent=1)
    cmd.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
    cmd.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')
    cmd.editRenderLayerAdjustment('miDefaultFramebuffer.datatype')
    cmd.setAttr('miDefaultFramebuffer.datatype', 1)
    cmd.editRenderLayerAdjustment('miDefaultFramebuffer.premultiply')
    cmd.setAttr('miDefaultFramebuffer.premultiply', 0)
    cmd.setAttr('miDefaultOptions.maxReflectionRays', 0)
    cmd.setAttr('miDefaultOptions.maxRefractionRays', 0)
    
    # sss Parameter's define
    charName = 'Jac1_'
    front_sss_weight = 0.0
    front_sss_radius = 0.0
    mid_sss_weight = 0.0
    mid_sss_radius = 0.0
    back_sss_weight = 0.0
    back_sss_depth = 0.0
    scaleConversion =  0.0
    fallOff = 0.0

    if charName == 'Jac1_':
        front_sss_weight = 0.15
        front_sss_radius = 0.005
        mid_sss_weight = 0.25
        mid_sss_radius = 0.006
        back_sss_weight = 6
        back_sss_radius = 0.12
        back_sss_depth = 0.4
        scaleConversion = 3
    
    sssSaveTex = cmd.shadingNode('mentalrayTexture', name=layerPrefix+'SSSsaveTex', asTexture=1)           
    cmd.setAttr(sssSaveTex+'.miWritable', 1)
    cmd.setAttr(sssSaveTex+'.miDepth', 4)
    cmd.expression(o=sssSaveTex, s='miWidth = defaultResolution.width * 2;\nmiHeight = defaultResolution.height;')
    cmd.setAttr(sssSaveTex+'.fileTextureName', '', type='string')  
    cmd.setAttr(sssSaveTex+'.fileTextureName', '', type='string')                
    sssLmap = cmd.createNode('misss_fast_lmap_maya', name=layerPrefix+'SSSlmap') 
    sssShr = cmd.shadingNode('misss_fast_skin_maya', name=layerPrefix+'sss', asShader=1)
    sssShrSG = cmd.sets(name=sssShr+'SG', renderable=1, noSurfaceShader=1, empty=1)
    cmd.setAttr(sssShr+'.samples', 1024)
    cmd.setAttr(sssShr+'.diffuse_weight', 0)
    cmd.setAttr(sssShr+'.overall_weight', 0)
    cmd.setAttr(sssShr+'.front_sss_weight', front_sss_weight)
    cmd.setAttr(sssShr+'.front_sss_radius', front_sss_radius)
    cmd.setAttr(sssShr+'.mid_sss_weight', mid_sss_weight)
    cmd.setAttr(sssShr+'.mid_sss_radius', mid_sss_radius)
    cmd.setAttr(sssShr+'.back_sss_weight', back_sss_weight)
    cmd.setAttr(sssShr+'.back_sss_radius', back_sss_radius)
    cmd.setAttr(sssShr+'.back_sss_depth', back_sss_depth)
    cmd.setAttr(sssShr+'.scale_conversion', scaleConversion)
#    cmd.setAttr(sssSaveTex+'.fileTextureName', pathName, type='string')
    cmd.connectAttr(sssSaveTex+'.message', sssLmap+'.lightmap', force=True) 
    cmd.connectAttr(sssSaveTex+'.message', sssShr+'.lightmap', force=True)
    cmd.connectAttr(sssLmap+'.message', sssShrSG+'.miLightMapShader', force=True)
    cmd.connectAttr(sssShr+'.outValue', sssShrSG+'.miMaterialShader', force=True)
    
    cmd.select(selected)
    cmd.sets(edit=True, forceElement=sssShrSG)
    cmd.select(cl=1)
    
    if others != None or other != 0:
        matte = cmd.shadingNode('lambert', asShader=1, name='ts_matte')
        matteSG = cmd.sets(name=matte+'SG', renderable=1, noSurfaceShader=1, empty=1)
        cmd.setAttr(matte+'.matteOpacityMode', 0)
        cmd.setAttr(matte+'.diffuse', 0)
        cmd.connectAttr(matte+'.outColor', matteSG+'.surfaceShader', force=True)
        cmd.select(others)                       
        cmd.sets(edit=True, forceElement=matteSG)
        cmd.select(cl=1)
        
def ts_SSS_light():
    if cmd.objExists('light_CharSSS_Grp') == 0:
        mel.eval("file -import -type \"mayaBinary\" (\"//File-cluster/GDC/Resource/Support/Maya/Python/IDMT/TTMS/IBL/ssslight.mb\")")
        
def delEyelashes():
    '''Delete original eyelash of all characters'''
    mel.eval("source \"//file-cluster/GDC/Resource/Support/Maya/2013/zjRemoveNamespace.mel\"")
    mel.eval("zjRemoveNamespace()")
        
    if cmd.objExists('jac_r_lo_head'):
        try:
            cmd.select('jac_r_lo_head.f[928:969]', 'jac_r_lo_head.f[1898:1939]')
            cmd.delete()
        except:
            pass

def ts_IBL():
    setMentalRayRenderSetting()
    cmd.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')
    cmd.setAttr('miDefaultOptions.finalGather', 1)
    cmd.setAttr('miDefaultOptions.finalGatherRays', 200)
    cmd.setAttr('miDefaultOptions.maxReflectionRays', 0)
    cmd.setAttr('miDefaultOptions.maxRefractionRays', 0)
    
    if cmd.objExists('indrIBL') == 0:
        cmd.editRenderLayerGlobals(currentRenderLayer='defaultRenderLayer')
        indrIBL = cmd.createNode('mentalrayIblShape', name='indrIBL')  
        cmd.setAttr(indrIBL+'.mapping', 1)
        cmd.setAttr(indrIBL+'.visibleInFinalGather', 1)
        cmd.setAttr(indrIBL+'.primaryVisibility', 0)
        cmd.setAttr(indrIBL+'.texture', '//File-cluster/GDC/Resource/Support/Maya/Python/IDMT/TTMS/IBL/DH206LX.hdr', type='string')
        try:
            cmd.connectAttr(indrIBL+'.message', 'mentalrayGlobals.imageBasedLighting', force=True)
        except:
            pass
        
    if cmd.objExists('indrIBL'):
        cmd.editRenderLayerGlobals(currentRenderLayer='defaultRenderLayer')
        cmd.setAttr(indrIBL+'.visibleInFinalGather', 1)
        cmd.setAttr(indrIBL+'.primaryVisibility', 0)
        try:
            cmd.connectAttr('indrIBL.message', 'mentalrayGlobals.imageBasedLighting', force=True)
        except:
            pass
        
def ysAdjustBumpDepAndAOdist(name):
    if name == 'bump2d':
        bumpDep = cmd.ls(type='bump2d')
        if bumpDep != None:
            para = cmd.floatSliderGrp('BumpDep', query=True, v=1)
            for item in bumpDep:
#                originalPara = cmd.getAttr(item+'.bumpDepth')
#                cmd.setAttr(item+'.bumpDepth', para+originalPara)
                cmd.setAttr(item+'.bumpDepth', para)

    if name == 'occlusion':
        aoTex = cmd.ls(type='mib_amb_occlusion')
        if aoTex != None:
            para = cmd.floatSliderGrp('AO_Dist', query=True, v=1)
            for item in aoTex:
                cmd.setAttr(item+'.max_distance', para)
                                  
def ysCreateNoneLightingPasses():
    # create none lighting renderlayer for character or enviornment
    commandChar = 'import BD_ysRenderlayerSetup as bdr\nreload(bdr)\nbdr.createAOPass(layerPrefix)\nbdr.createAmbPass(layerPrefix)\nbdr.normalPass(layerPrefix)\nbdr.ysFresnelPass(layerPrefix)'
    
    commandEnv = 'import BD_ysRenderlayerSetup as bdr\nreload(bdr)\nbdr.createAOPass(layerPrefix)\nbdr.createAmbPass(layerPrefix)\nbdr.createDepthPass(layerPrefix)\nbdr.normalPass(layerPrefix)\nbdr.ysFresnelPass(layerPrefix)'
    if cmd.window('BD_NoneLighting_Window', ex=1):
        cmd.deleteUI('BD_NoneLighting_Window')

    getInfoWindow = cmd.window('BD_NoneLighting_Window', title='NoneLighting', menuBar=1, mxb=1,\
                             sizeable=0, resizeToFitChildren=1, mnb=1, wh=[200,120])
    cmd.columnLayout( columnAttach=('both', 5), rowSpacing=5, columnWidth=180 )
    cmd.text(label='input Characters name for Prefix')
    prefixQuery = cmd.textField(text='')
      
    cmd.button(label='OK', w=90, h=35, c='import maya.cmds as cmd\nlayerPrefix=cmd.textField("'+prefixQuery+'", query=True, text=1)+"_"\
    \n'+commandChar+'\ncmd.deleteUI("BD_NoneLighting_Window")')
    cmd.button(label='env', w=90, h=35, c='layerPrefix="env_"\
    \n'+commandEnv+'\ncmd.deleteUI("BD_NoneLighting_Window")')
    cmd.setParent('..')   
    cmd.showWindow(getInfoWindow)

def ysCreateMVPass(layerPrefix):
    '''Create render layer for motion blur using MR Passes feature'''
    setMentalRayRenderSetting()
    mel.eval('unifiedRenderGlobalsWindow')
    geo = [item for item in cmd.ls(geometry=1) if cmd.nodeType(item) != 'renderBox']
    MVLayer = cmd.createRenderLayer(geo, noRecurse=1, name=layerPrefix+'MV', makeCurrent=1)
    cmd.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
    cmd.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')    
    cmd.editRenderLayerAdjustment('miDefaultFramebuffer.datatype')
    cmd.setAttr('miDefaultFramebuffer.datatype', 5)
    cmd.editRenderLayerAdjustment('miDefaultOptions.motionBlur')
    cmd.setAttr('miDefaultOptions.motionBlur', 2)
    cmd.editRenderLayerAdjustment('miDefaultOptions.shutterDelay')
    cmd.setAttr('miDefaultOptions.shutterDelay', 1)
    cmd.editRenderLayerAdjustment('miDefaultOptions.shutter')
    cmd.setAttr('miDefaultOptions.shutter', 1)
    cmd.editRenderLayerAdjustment('defaultRenderGlobals.imageFormat')
    cmd.setAttr('defaultRenderGlobals.imageFormat', 51)
    cmd.setAttr('defaultRenderGlobals.imfkey', 'exr', type="string" )
    
    # Set up render passses 
    MV_2D = cmd.createNode('renderPass', name='MV_2DToxik')
    mel.eval('applyAttrPreset "'+MV_2D+'" "D:/Alias/MAYA2011x64/presets/attrPresets/renderPass/2DMotionVector.mel" 1;')
    mel.eval('renderLayerEditorOnSelectionChanged RenderLayerTab')
    mel.eval('layerEditorRenderLayerManagerChange RenderLayerTab')
    mel.eval('renderPassesAdjustLayerConnection 1 "scene";')
    cmd.connectAttr(MVLayer+'.renderPass', MV_2D+'.owner', nextAvailable=1)
        
def ysCreateRenderLayer(layer):
    import BD_ysRenderlayerSetup as bdr
    reload(bdr)
    if layer == 'ambient':  
        ysGetPrefixName('bdr.createAmbPass(layerPrefix)')    
        
    if layer == 'Fresnel':  
        ysGetPrefixName('bdr.ysFresnelPass(layerPrefix)')    
   
    if layer == 'color':
        ysGetPrefixName('bdr.creatColorPass(layerPrefix)')
        
    if layer == 'specular':
        ysGetPrefixName('bdr.creatSpecPass(layerPrefix)')
    
    if layer == 'occlusion':
        ysGetPrefixName('bdr.createAOPassWithBump(layerPrefix)')
        
    if layer == 'castAO':
        ysGetPrefixName('bdr.castAO(layerPrefix)')
    
    if layer == 'castShadow':
        ysGetPrefixName('bdr.castShaow(layerPrefix)')
    
    if layer == 'lgt':
        ysGetPrefixName('bdr.LgtPass("lgt", layerPrefix)')
        
    if layer == 'extraLgt':
        ysGetPrefixName('bdr.LgtPass("extraLgt", layerPrefix)')
    
    if layer == 'Depth':
        ysGetPrefixName('bdr.createDepthPass(layerPrefix)')    
        
    if layer == 'reflection':
        ysGetPrefixName('bdr.createReflectionPass(layerPrefix)')
        
    if layer == 'normal':
        ysGetPrefixName('bdr.normalPass(layerPrefix)') 
    
    if layer == 'Char_SSS':
        ysGetPrefixName('bdr.createChar_SSS(layerPrefix)') 
        
    if layer == 'indirect':
        ysGetPrefixName('bdr.createIndirectPass(layerPrefix)') 
    
    if layer == 'CharHairs':
        ysGetPrefixName('bdr.ysRfM_charHairs(layerPrefix)') 
        
    if layer == 'motionblur':
        ysGetPrefixName('bdr.ysCreateMVPass(layerPrefix)') 