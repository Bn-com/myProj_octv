# -*- coding: utf-8 -*-
# Copyright (C) 2000-2018 IDMT. All rights reserved.
'''
'''
__author__    = 'zhongming@idmt.com.cn'
__date__    = '2018-01-01'

import os
import re
import subprocess
import pymel.core as pm
import maya.cmds as mc
import maya.mel as mel
import maya.OpenMaya as om
import json

OUTPUT_ASSETS = 'Z:/Projects/ShunLiu/ShunLiu_Scratch/TD/UrealProject/maya2unreal/assets/'
OUTPUT_ANIMS = 'Z:/Projects/ShunLiu/ShunLiu_Scratch/TD/UrealProject/maya2unreal/anims/'
OUTPUT_JSONS = 'Z:/Projects/ShunLiu/ShunLiu_Scratch/TD/UrealProject/maya2unreal/jsons/'

def exportProp():
    joints = pm.ls(type = 'joint')
    rootM = None
    for jt in joints:
        if jt.getParent() == 'Joint_GRP':
           rootM = jt
        jt.drawStyle.set(0)
         
    pm.select(rootM, hi = True, r = True)
    joints = pm.ls(sl = True, type = 'joint')
    pm.select(joints, r = True)


    pm.bakeResults(pm.ls(sl = True),simulation = True, t = (1,2), sampleBy = 1, disableImplicitControl = True, preserveOutsideKeys = True, sparseAnimCurveBake = False, minimizeRotation = True, controlPoints = False, shape =  True)


    disconnectJointsScaleAttr(joints)

    pm.delete(all = True, channels = True)

    pm.select(cl = True)
    rootJoin = pm.joint(p=(0,0,0), name = 'root')
    pm.parent(rootM, rootJoin)
    try:
        pm.delete('RIG')
    except:
        pm.delete('Master_GRP')

    convertArMatToMaya()
    pm.select('PRO', r = True)
    pm.select(rootJoin, add = True)

    fbxCommonOptions()

    mel.eval("FBXExportSmoothingGroups -v true")
    mel.eval("FBXExportSmoothMesh -v true")
    mel.eval("FBXExportHardEdges -v true")
    mel.eval("FBXExportTangents -v false")
    mel.eval("FBXExportInstances -v false")
    mel.eval('FBXExportTriangulate -v false')

    mel.eval("FBXExportShapes -v true")
    mel.eval("FBXExportSkins -v true")
    mel.eval("FBXExportSkeletonDefinitions -v true")

    mel.eval("FBXExportCameras -v false")

    if not os.path.lexists(OUTPUT_ASSETS):
        os.makedirs(OUTPUT_ASSETS)

    # Export!
    mel.eval('FBXExport -f "' + OUTPUT_ASSETS + getCharName(getSceneName()) + '.fbx" -s')

def exportCameraToUE():

    sels = pm.ls(sl = True)
    cam = None
    if sels and pm.nodeType(sels[0].getShape()) == 'camera':
        cam = sels[0]
    else:
        cams = pm.ls(type = 'camera')

        for cam in ['frontShape', 'perspShape', 'sideShape', 'topShape']:
            cams.remove(cam)
        if len(cams) != 1:
            pm.error('场景中有多个相机，请删除无用的相机，或选择需要导出的相机')
        else:
            cam = cams[0].getParent()
    if cam:
        start = pm.playbackOptions(q = True, min = True)
        end = pm.playbackOptions(q = True, max = True)
        
        pm.bakeResults(cam,simulation = True, t = (str(start) , str(end)), sampleBy = 1, disableImplicitControl = True, preserveOutsideKeys = True, sparseAnimCurveBake = False, minimizeRotation = True, controlPoints = False, shape =  True)

        nodeRoot = pm.group(cam.root(), a = True, absolute = True)
        pm.xform(nodeRoot, a = True, ws = True, pivots  = (0,0,0))

        nodeRoot.scaleX.set(10)
        nodeRoot.scaleY.set(10)
        nodeRoot.scaleZ.set(10)

        dupCam = pm.duplicate(cam)[0]
        pm.parent(dupCam, world = True)
        pm.setAttr(dupCam.getShape() + '.focalLength', lock = False)
        pm.connectAttr(cam.getShape() + '.focalLength', dupCam.getShape() + '.focalLength')

        attrs = ['.tx', '.ty', '.tz', '.rx', '.ry', '.rz']
        for attr in attrs:
           lockedAttr = pm.connectionInfo(dupCam + attr, gla = True)
           if lockedAttr:
               pm.setAttr(lockedAttr, lock = False)

        pconstrain = pm.parentConstraint(cam, dupCam)

        pm.bakeResults( dupCam + '.tx', dupCam + '.ty', dupCam + '.tz', dupCam + '.rx', dupCam + '.ry', dupCam + '.rz', dupCam.getShape() + '.fl', t=(start,end))

        pm.delete(pconstrain)

        animCurves = []

        animCurves =  pm.listConnections(dupCam, s = True, d = False)
        animCurves = animCurves + pm.listConnections(dupCam.getShape(), s = True, d = False)
        for c in animCurves:
            if 'animCurve' in pm.nodeType(c):
                pm.keyframe(c, option = 'over', relative = True, timeChange = -start , time=(start,end))
        pm.rename(dupCam, getSceneName() + '_UE_CAM')
        pm.select(dupCam, r = True)


        path = OUTPUT_ANIMS + getSceneName() + '/'
        if not os.path.lexists(path):
            os.makedirs(path)

        
        fbxCommonOptions()

        mel.eval("FBXExportShapes -v false")
        mel.eval("FBXExportSkins -v false")
        mel.eval("FBXExportSkeletonDefinitions -v false")
        mel.eval("FBXExportCameras -v true")

        mel.eval('FBXExport -f "' + path + getSceneName() + '_CAM.fbx" -s')
        

def expAnimation():
    refFiles = pm.system.listReferences()
    charPattern = re.compile('^csl_c[0-9]', re.I)
    propPattern = re.compile('^csl_p[0-9]', re.I)

    pm.select(cl = True)
    animObjs = []
    rootJoins = []
    parentConstraints = []
    for rf in refFiles:
        if rf.isLoaded():

            refFileName = getBaseName(rf.path)
            
            if charPattern.search(refFileName):
                ns = rf.namespace
                objDic = {}
                objDic['ns'] = ns
                objDic['type'] = 'CHAR'
                objDic['name'] = refFileName

                rootM = pm.PyNode(ns + ':Root_M')
                objDic['root'] = rootM
                pm.select(cl = True)

                rootJoin = pm.joint(p=(0,0,0), name = refFileName + '_root')
                rootJoins.append(rootJoin)
                objDic['root_tmp'] = rootJoin

                animObjs.append(objDic)


                pc = pm.parentConstraint(rootM.getParent(), rootJoin, weight = 1)
                parentConstraints.append(pc)
                rf.importContents()

            elif propPattern.search(refFileName):

                ns = rf.namespace
                objDic = {}
                objDic['ns'] = ns
                objDic['name'] = refFileName

                objDic['type'] = 'PROP'
                
                


                joints = pm.ls(ns + ':*', type = 'joint')
                rootM = None
                for jt in joints:
                    if jt.getParent().find('Joint_GRP') > -1:
                       rootM = jt
                    jt.drawStyle.set(0)


                objDic['root'] = rootM
                pm.select(cl = True)

                rootJoin = pm.joint(p=(0,0,0), name = refFileName + '_root')
                rootJoins.append(rootJoin)
                objDic['root_tmp'] = rootJoin
                animObjs.append(objDic)

                pc = pm.parentConstraint(rootM.getParent(), rootJoin, weight = 1)
                parentConstraints.append(pc)
                rf.importContents()




    minFrame = pm.playbackOptions(q = True, min = True)
    maxFrame = pm.playbackOptions(q = True, max = True)

    pm.select(cl = True)

    for obj in animObjs:

        rootM = obj['root'] 

        pm.select(obj['root'], add = True)

    pm.select(pm.ls(sl = True), hi = True, r = True)

    joints = pm.ls(sl = True, type = 'joint')

    blendShapes = pm.ls(type = 'blendShape')
    pm.select(cl = True)
    pm.select(joints, add = True)
    pm.select(blendShapes, add = True)
    pm.select(rootJoins, add = True)

    sels = pm.ls(sl = True)

    if sels:
        pm.bakeResults(pm.ls(sl = True),simulation = True, t = (minFrame , maxFrame), sampleBy = 1, disableImplicitControl = True, preserveOutsideKeys = True, sparseAnimCurveBake = False, minimizeRotation = True, controlPoints = False, shape =  True)

        
        disconnectJointsScaleAttr(joints)

        pm.delete(parentConstraints)

        pm.delete(all = True, staticChannels = True)

        convertArMatToMaya()

        print '*' * 50
        print animObjs
        print '*' * 50
        
        for obj in animObjs:

            rootM = obj['root'] 
            # pos = pm.xform(rootM, q = True, a = True, ws = True , piv =True)
            # tAttrs = ['.tx', '.ty', '.tz']

            # for index, val in enumerate(tAttrs):
                
            #     r = pm.listConnections(rootM + val, s = True, d = False)
            #     if len(r) > 0:
            #         offsetVal = pm.getAttr(rootM + val)
            #         pm.keyframe(r[0], e = True, iub = True,option = 'over', relative = True, valueChange = (pos[index] - offsetVal))
            #     else:
            #         pm.setAttr(rootM + val, pos[index])

            
            pm.select(cl = True)


            rootJoin = pm.rename(obj['root_tmp'], 'root') # pm.joint(p=(0,0,0), name = 'root')


            # pc = pm.parentConstraint(rootM.getParent(), rootJoin, weight = 1)
            # pm.delete(pc)

            pm.parent(rootM, rootJoin)


            try:
                pm.delete(obj['ns'] + ':RIG')
            except:
                pm.delete(obj['ns'] + ':Master_GRP')
            
            if obj['type'] == 'CHAR':
                pm.parent(obj['ns'] + ':CHR', w = True)
                pm.select(obj['ns'] + ':CHR', r = True)
                pm.select(rootJoin, add = True)

            elif obj['type'] == 'PROP':
                pm.parent(obj['ns'] + ':PRO', w = True)
                pm.select(obj['ns'] + ':PRO', r = True)
                pm.select(rootJoin, add = True)

            fbxCommonOptions()

            mel.eval("FBXExportShapes -v true")
            mel.eval("FBXExportSkins -v true")
            mel.eval("FBXExportSkeletonDefinitions -v true")

            # Cameras
            mel.eval("FBXExportCameras -v false")


            path = OUTPUT_ANIMS + getSceneName() + '/'
            if not os.path.lexists(path):
                os.makedirs(path)

            # Export!
            mel.eval('FBXExport -f "' + path + getSceneName() + '_' + getCharName(obj['name']) + '.fbx" -s')
            print '*' * 50
            print 'export:' + obj['name']
            print '*' * 50
            if obj['type'] == 'CHAR':
                pm.group(obj['ns'] + ':CHR', rootJoin, n = obj['name'])
            elif obj['type'] == 'PROP':
                pm.group(obj['ns'] + ':PRO', rootJoin, n = obj['name'])


def exportChar():
    pm.select('Root_M', hi = True, r = True)
    joints = pm.ls(sl = True, type = 'joint')
    rootM = pm.ls(sl = True)[0]
    blendShapes = pm.ls(type = 'blendShape')
    pm.select(blendShapes, add = True)
    pm.bakeResults(pm.ls(sl = True),simulation = True, t = (1,2), sampleBy = 1, disableImplicitControl = True, preserveOutsideKeys = True, sparseAnimCurveBake = False, minimizeRotation = True, controlPoints = False, shape =  True)

    # mainChildren = pm.PyNode('Main').getChildren(type = 'transform')
    # for child in mainChildren:
    #     if child.name() != 'DeformationSystem':
    #         pm.delete(child)

    disconnectJointsScaleAttr(joints)

    pm.delete(all = True, channels = True)
    
    pm.select(cl = True)
    rootJoin = pm.joint(p=(0,0,0), name = 'root')
    pm.parent(rootM, rootJoin)
    try:
        pm.delete('RIG')
    except:
        pm.delete('Master_GRP')

    convertArMatToMaya()
    pm.select('CHR', r = True)
    pm.select(rootJoin, add = True)

    # pm.group('CHR', rootJoin, n = getSceneName())

    fbxCommonOptions()

    mel.eval("FBXExportSmoothingGroups -v true")
    mel.eval("FBXExportSmoothMesh -v true")
    mel.eval("FBXExportHardEdges -v true")
    mel.eval("FBXExportTangents -v false")
    mel.eval("FBXExportInstances -v false")
    mel.eval('FBXExportTriangulate -v false')

    mel.eval("FBXExportShapes -v true")
    mel.eval("FBXExportSkins -v true")
    mel.eval("FBXExportSkeletonDefinitions -v true")

    mel.eval("FBXExportCameras -v false")
    

    if not os.path.lexists(OUTPUT_ASSETS):
        os.makedirs(OUTPUT_ASSETS)

    # Export!
    mel.eval('FBXExport -f "' + OUTPUT_ASSETS + getCharName(getSceneName()) + '.fbx" -s')



def getCharName(fullName):
    splites = fullName.split('_')
    if len(splites) > 2:
        return splites[1]
    return fullName

def disconnectJointsScaleAttr(joints):
    for jo in joints:
        for attr in ['.sx', '.sy', '.sz', '.scale']:
            cons = pm.listConnections(jo + attr, s = True, d = False)
            if cons:
                if pm.nodeType(cons[0]).find('animCurve') == -1:
                    consAttr = pm.listConnections(jo + attr, s = True, d = False, p = True)
                    try:
                        pm.disconnectAttr(consAttr[0], jo + attr)
                    except:
                        pass

def fbxCommonOptions():
    mel.eval("FBXExportBakeComplexAnimation -v false")
    mel.eval('FBXExportAnimationOnly -v false')
    mel.eval('FBXExportApplyConstantKeyReducer -v false')
    mel.eval('FBXExportCacheFile -v false')

    # mel.eval('FBXExportFileVersion -v FBX201600')
    mel.eval('FBXExportInAscii -v false')
    # mel.eval('FBXExportAxisConversionMethod convertAnimation')
    # mel.eval('FBXExportScaleFactor 10')

    # mel.eval('FBXExportConvertUnitString cm')
    mel.eval("FBXExportUseSceneName -v false")
    mel.eval("FBXExportQuaternion -v euler")

    # Constraints
    mel.eval("FBXExportConstraints -v false")
    # Cameras
    
    # Lights
    mel.eval("FBXExportLights -v false")
    # Embed Media
    mel.eval("FBXExportEmbeddedTextures -v false")
    # Connections
    mel.eval("FBXExportInputConnections -v false")
    # Axis Conversion
    mel.eval("FBXExportUpAxis y")

def getSceneName():
    return os.path.basename(os.path.splitext(pm.system.sceneName())[0])


def getBaseName(path):
    return os.path.basename(os.path.splitext(path)[0])

def getAssetPath():
    path = 'E:/Maya_UE4/Assets'
    if not os.path.lexists(path):
        os.makedirs(path)
    return path

def convertArMatToMaya():
    pattern = re.compile('^MUE_')
    fs = pm.ls(type = 'file')
    for f in fs:
        path = pm.getAttr(f + '.fileTextureName')
        newPath = os.path.expandvars(f.fileTextureName.get()) #path.replace('${IDMT_PROJECTS}/', 'Z:/Projects/')
        pm.setAttr(f + '.fileTextureName', newPath)             
    
    allShadingEngines = pm.ls(type = 'shadingEngine')

    for shadingEngine in allShadingEngines:
        material = pm.listConnections(shadingEngine + '.surfaceShader',s = True, d = False)
        if material:
            mat = material[0]
            if pm.nodeType(mat) == 'aiStandard':
                connections = pm.listConnections(mat,s = True, d = False, c = True, p = True)
                newShader = createShader(shadingEngine.name())
        
                for con in connections:
                    if '.kitty' in con[0].name():
                        continue
                    elif '.KsColor' in con[0].name():
                       if con[1].find('outColorR')>1 or con[1].find('outColorB')>1 or con[1].find('outColorG')>1:
                           pm.connectAttr(con[1],newShader + '.specularColorR', f = True )
                           pm.connectAttr(con[1],newShader + '.specularColorG', f = True )
                           pm.connectAttr(con[1],newShader + '.specularColorB', f = True )
                       else:
                           pm.connectAttr(con[1],newShader + '.specularColor', f = True )
                    elif '.color' in con[0].name():
                        pm.connectAttr(con[1],newShader + '.color', f = True )
                    elif '.normalCamera' in con[0].name():
                        pm.connectAttr(con[1],newShader + '.normalCamera', f = True )

                opa = pm.getAttr(mat + '.opacity')
                
                pm.setAttr(newShader + '.transparency', 1 - opa[0], 1 - opa[1], 1 - opa[2], type = 'double3',)
                
                #sg = pm.listConnections(shadingEngine,s = False, d = True, c = True, p = True, type = 'shadingEngine')
                pm.connectAttr(newShader + '.outColor', shadingEngine + '.surfaceShader', f = True )
                newName = 'MUE_' + mat.name()
                pm.delete(mat)
                if not pattern.match(newShader.name()):
                    pm.rename(newShader, newName)
            else:
                if not pattern.match(mat.name()):
                    try:
                        pm.rename(mat, 'MUE_' + mat.name())
                    except:
                        pass

def createShader(name):
    nshader = pm.shadingNode('blinn', asShader = True, n = 'UNREAL_' + name)
    return nshader


def writeMatJsonFile():
    data = {}
    SEs = pm.ls(type = 'shadingEngine')
    for se in SEs:
        mat = pm.listConnections(se + '.surfaceShader', s = True, d = False)
        print '-' * 30
        print '|' * 30
        if mat:
            pm.hyperShade(o = mat[0])
            
            sels = pm.ls(sl = True)
            for sel in sels:
                w = True
                for key in data:
                    if data[key] == mat[0].name():
                        w = False
                if w:
                    data[sel.getParent().name()] = mat[0].name()
      
    jsonData = json.dumps(data)

    txtName =  os.path.basename(os.path.splitext(pm.system.sceneName())[0]).split('_')[1]

    if not os.path.lexists(OUTPUT_JSONS):
        os.makedirs(OUTPUT_JSONS)


    txtFile = open(OUTPUT_JSONS + txtName + '.json', 'w')
    txtFile.write(jsonData)
    txtFile.close()
    mc.confirmDialog( title='Confirm', message = r'Write Json File Done', button=['OK'])

def selectJson():
    jsonFilePath = mc.fileDialog2(fm = 1, fileFilter = '*.json', dir = 'Z:\Projects\ShunLiu\ShunLiu_Scratch\TD\UrealProject\maya2unreal\jsons')
    if jsonFilePath:
        mc.textFieldButtonGrp('jsonFileName', e = True, text = jsonFilePath[0])

def readMatJsonFileWin():
    if mc.window('readMatJsonFileWin', exists =  True):
        mc.deleteUI('readMatJsonFileWin')
    
    mc.window('readMatJsonFileWin', title = 'Read Materials Json File', width = 380, height = 180, sizeable = False)
    mc.columnLayout(rowSpacing=2, columnAttach = ['both',5],columnWidth = 600)
    mc.textFieldButtonGrp('jsonFileName', label='Json File:', text='', bc = 'import idmt.maya.unreal.maya2unreal as m2u;reload(m2u);m2u.selectJson()', buttonLabel = 'Select a Json File' )
    mc.button( label='GO', command='import idmt.maya.unreal.maya2unreal as m2u;reload(m2u);m2u.readMatJsonFile()')
    mc.showWindow( 'readMatJsonFileWin' )

def readMatJsonFile():
    fileName = mc.textFieldButtonGrp('jsonFileName', q = True, text = True)
    with open(fileName) as json_data:
        d = json.load(json_data)
      
        SEs = pm.ls(type = 'shadingEngine')
        
        for se in SEs:
            mat = pm.listConnections(se + '.surfaceShader', s = True, d = False)
            print '-' * 30
            print '|' * 30
            if mat:
                pm.hyperShade(o = mat[0])
                
                sels = pm.ls(sl = True)
                for sel in sels:
                    keyName = sel.getParent().name()
                    key = d.get(keyName, '')
                    if key:
                        pm.rename(mat[0], d[keyName])

        mc.confirmDialog( title='Confirm', message= r'Read Json File Done', button=['OK'])

def renameMatsToTempName():
    for tmpMat in pm.ls(materials = True):
        try:
            pm.rename(tmpMat, 'm_tmp_#')
        except:
            pass




def getColorByAverageTexture(obj, fileNode):
    pm.select(obj, r = True)
    uvMap = pm.polyListComponentConversion(fv = True, tuv = True)
    uv = pm.polyEditUV(uvMap, q = True)
    u = []
    v = []
    for i in range(0,len(uv),2):
        u.append(uv[i])
        v.append(uv[i + 1])
    colors = pm.colorAtPoint( fileNode, o='RGB', u=tuple(u), v=tuple(v) )
    r = 0
    g = 0
    b = 0
    count = 0
    for n in range(0, len(colors), 3):
        count += 1
        r += colors[n]
        g += colors[n + 1]
        b += colors[n + 2]
    r /= count
    g /= count
    b /= count

    r = r * 1.3 if r * 1.0 < 1 else r
    g = g * 1.3 if g * 1.0 < 1 else g
    b = b * 1.3 if b * 1.0 < 1 else b

    return (r, g, b)



def makeColorForAnFile():
    SEs = pm.ls(type = 'shadingEngine')
    for se in SEs:
        try:
            mat = pm.listConnections(se + '.surfaceShader', s = True, d = False)
            print '-' * 30
            print '|' * 30
            isEye = False
            if mat and mat[0].name() not in ['lambert1', 'particleCloud1', 'shaderGlow1']:
                mSetupColor = mat[0]
                if pm.nodeType(mSetupColor) == 'aiRaySwitch':
                    tmpMat = pm.listConnections(mSetupColor + '.camera', s = True, d = False)
                    if tmpMat:
                        mSetupColor = tmpMat[0]
                        pm.connectAttr(mSetupColor + '.outColor', se + '.surfaceShader', f = True )
                averColor = mSetupColor.color.get()
                try:
                    opa = mSetupColor.opacity.get()
                    opa = (1 - opa[0], 1- opa[1], 1-opa[2])
                except:
                    opa = mSetupColor.transparency.get()

                colorConnection = pm.listConnections(mSetupColor + '.color', s = True, d = False, type = 'file')
                
                if colorConnection:
                    pm.hyperShade(o = mSetupColor)
                
                    sels = pm.ls(sl = True)
                    for sel in sels:
                        if '_eye_' in sel.name():
                            isEye = True
                    if sels:
                        averColor = getColorByAverageTexture(sels[0],colorConnection[0])

                newShader = createShader(se.name())
                
                if not isEye:
                    pm.setAttr(newShader + '.color', averColor, type = 'double3')
                else:
                    pm.connectAttr(colorConnection[0] + '.outColor', newShader + '.color',  f = True )

                pm.setAttr(newShader + '.specularColor', (0,0,0), type = 'double3')
                pm.setAttr(newShader + '.transparency', opa, type = 'double3')
                pm.connectAttr(newShader + '.outColor', se + '.surfaceShader', f = True )

                newName = mSetupColor.name()
                pm.delete(mSetupColor)
                pm.rename(newShader, newName)
        except:
            print '*' * 50
            print se.name() + ' not setup'
            print '*' * 50
    mel.eval('MLdeleteUnused;')