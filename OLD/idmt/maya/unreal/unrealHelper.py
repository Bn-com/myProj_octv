# -*- coding: utf-8 -*-
# Copyright (C) 2000-2017 IDMT. All rights reserved.
'''
'''
__author__    = 'zhongming@idmt.com.cn'
__date__    = '2017-02-09'

import os
import re
import subprocess
import pymel.core as pm
import maya.cmds as mc
import maya.mel as mel
import maya.OpenMaya as om

if not mc.pluginInfo('AbcImport',loaded = 1,q = 1):
    mc.loadPlugin('AbcImport')
if not mc.pluginInfo('AbcExport',loaded = 1,q = 1):
    mc.loadPlugin('AbcExport')

def arMatToMaya(dep = 'ASSET'):
    importReferenceFiles()
    assets = []

    localPath = 'E:/Maya_UE4/Assets/'
    proxyDataPath = localPath + getNameFromFilePath(pm.system.sceneName())+ '_PROXY/'
    if dep == 'ASSET':
        cvtIff2PngAndSet()
        outputProxyAssetTransformInfo(proxyDataPath)
        assets = importProxyModelInAssetFile()
    else:
        outputProxyAssetTransformInfo(getShotPath())
    removeNamespace()
    convertArMatToMaya()
    renameAllShadersAndShadingEngines(dep)


    if assets:
        for asset in assets:
            pm.select(asset, r = True)
            exportSelectedFBX(proxyDataPath + asset.name())
        pm.delete(assets)

def convertArMatToMaya():
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
                
                pm.delete(mat)
                pm.rename(newShader, mat.name())

def createShader(name):
    nshader = pm.shadingNode('blinn', asShader = True, n = 'UNREAL_' + name)
    return nshader

def assignMatToFace():
    SEs = pm.ls(type = 'shadingEngine')
    for se in SEs:
        mat = pm.listConnections(se + '.surfaceShader', s = True, d = False)
        print '-' * 30
        print '|' * 30
        if mat:
            pm.hyperShade(o = mat[0])
            
            sels = pm.ls(sl = True)
            for sel in sels:
                if '.f[' not in sel.name():
                    pm.select(sel, r = True)
                    pm.hyperShade(assign = 'lambert1')
                    pm.select(sel, r = True)
                    faceNum = pm.polyEvaluate( f = True)
                    selStr = sel.getParent() + '.f[0:' + str(faceNum - 1) + ']'
                    pm.select(selStr, r = True)
                    pm.hyperShade(assign=mat[0])

            print '|' * 30
            print '-' * 30
        


def renameAllShadersAndShadingEngines(dep):
    mats = pm.ls(materials = True)
    pattern = re.compile('^MUE_')
    for mat in mats:
        sg = pm.listConnections(mat, d = True, s = False, t = 'shadingEngine')
        if sg:
            if not pattern.match(mat.name()):
                newName = 'MUE_' + mat.name()
                newSEName = newName + '_SG'
                try:
                    
                    if dep == 'ASSET':
                        pm.rename(mat, newName)
                        pm.rename(sg[0], newSEName)
                    else:
                        pm.rename(mat, newSEName)
                        pm.rename(sg[0], newName)

                except:
                    pass
            

def importReferenceFiles():
    refFiles = pm.system.listReferences()
    for refFile in refFiles:
        if refFile.isLoaded():
            refFile.importContents()
        else:
            refFile.remove()
    

    
def removeNamespace():
    objs = pm.ls(long = True)
    pattern = re.compile('([0-9a-zA-Z_]*:)+')

    for obj in objs:
        m = pattern.sub('', obj.name())
        try:
            pm.rename(obj, m)
        except:
            pass


def loopVisible(n):
    if pm.getAttr(n + '.visibility'):
        pa = n.getParent()
        if pa:
            return loopVisible(pa)
        else:
            return True
    else:
        return False

def filterAllRenderAndVisableMeshes(meshes):
     
    displayLayers = pm.ls(type = 'displayLayer')
    for layer in displayLayers:
        if 'defaultLayer' not in layer.name():
            if not pm.getAttr(layer + '.visibility'):
                hideObjs = layer.listMembers()
                hideGeos = pm.ls(hideObjs, g = True , dag = True)
                for ho in hideGeos:
                    pm.setAttr(ho + '.primaryVisibility', 0)
                            
    objs = []
    for mesh in meshes:
        if pm.getAttr(mesh + '.primaryVisibility'):
            transfObj = mesh.getParent()
            if loopVisible(transfObj):
                if transfObj not in objs:
                    objs.append(transfObj)

    return objs

def exportSelectedFBX(file):

    path = os.path.split(file)[0]

    if not os.path.lexists(path):
        os.makedirs(path)
    
    mel.eval('FBXExport -f "' + file + '.fbx" -s FBXExportSmoothingGroups -v true FBXExportSmoothMesh -v true')


def exportAssetToUnreal():
    arMatToMaya('ASSET')
    meshs = pm.ls(type='mesh')

    objs = filterAllRenderAndVisableMeshes(meshs)

    for obj in objs:
        convertNSidedFace2Quad(obj)

    pm.runtime.DeleteHistory()

    localPath = 'E:/Maya_UE4/Assets/'

    fileName = getNameFromFilePath(pm.system.sceneName())

    pm.select(objs, r = True)

    exportSelectedFBX(localPath + fileName)


def getNameFromFilePath(path):
    return os.path.basename(os.path.splitext(path)[0])

def getShotString():
    fileName = getNameFromFilePath(pm.system.sceneName())
    shotSegs = fileName.split('_')
    return '_'.join([shotSegs[0], shotSegs[1], shotSegs[2], shotSegs[3]])

def getShotPath():
    fileName = getNameFromFilePath(pm.system.sceneName())
    shotSegs = fileName.split('_')
    path = 'E:/Maya_UE4/Anim/' + getShotString() + '/'

    if not os.path.lexists(path):
        os.makedirs(path)

    return path


def offsetAlembicNodesTo0():
    offsetFrame = mc.idmtProject( timeLine = True, echo  = False)[0]
    als = pm.ls(type = 'AlembicNode')
    for al in als:
        pm.setAttr(al + '.offset', -offsetFrame)


def exportSelectedCameraToUE():
    sels = pm.ls(sl = True)
    if sels:
        if pm.nodeType(sels[0].getShape()) == 'camera':
            exportCameraToUE(sels[0])

def exportCameraToUE(cam):

    camName = cam.name()
    pm.rename(cam, 'bake_came')
    nodeRoot = pm.group(cam.root(), a = True, absolute = True)
    pm.xform(nodeRoot, a = True, ws = True, pivots  = (0,0,0))


    # pm.setAttr(nodeRoot + '.ry', -90)
    # nodeRoot.rotateX.set(90)
    nodeRoot.scaleX.set(10)
    nodeRoot.scaleY.set(10)
    nodeRoot.scaleZ.set(10)

    # offsetTransform = pm.xform(cam, q = True, ws = True, a = True, t = True)

    # nodeRoot.translateX.set(-1 * offsetTransform[0])
    # nodeRoot.translateY.set(-1 * offsetTransform[1])
    # nodeRoot.translateZ.set(-1 * offsetTransform[2])


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

    frames = mc.idmtProject( timeLine = True, echo  = False)

    start = frames[0]
    end = frames[1]
    print '=' * 30
    print str(start) + '   ' + str(end)
    print '=' * 30
    pm.bakeResults( dupCam + '.tx', dupCam + '.ty', dupCam + '.tz', dupCam + '.rx', dupCam + '.ry', dupCam + '.rz', dupCam.getShape() + '.fl', t=(start,end))

    pm.delete(pconstrain)

    animCurves = []

    animCurves =  pm.listConnections(dupCam, s = True, d = False)
    animCurves = animCurves + pm.listConnections(dupCam.getShape(), s = True, d = False)
    for c in animCurves:
        if 'animCurve' in pm.nodeType(c):
            pm.keyframe(c, option = 'over', relative = True, timeChange = -start , time=(start,end))
    pm.rename(dupCam, camName)
    pm.select(dupCam, r = True)


    localPath = getShotPath() + camName
    exportSelectedFBX(localPath)

    # return offsetTransform




def smoothObjsBySet():
    objSets = pm.ls(type = 'objectSet')

    for s in objSets:
        if s.name().find('smooth_1') > -1:
            for m in s.members():
                try:
                    pm.polySmooth(m, dv = 1)
                except:
                    print '=' * 50
                    print m + ' can not smooth'
                    print '=' * 50
        if s.name().find('smooth_2') > -1:
            for m in s.members():
                try:
                    pm.polySmooth(m, dv = 1)
                except:
                    print '=' * 50
                    print m + ' can not smooth'
                    print '=' * 50


def convertNSidedFace2Quad(obj):
    pm.select(obj, r = True)
    mel.eval('ConvertSelectionToFaces')
    pm.polySelectConstraint(m = 2, t = 8, sz = 3)
    selFaces = pm.ls(sl = True)
    if selFaces:
        pm.polyTriangulate(ch = 1)
        pm.polyQuad(a = 30, kgb = 1, ktb = 1, khe = 1, ws = 1, ch = 1)
    pm.select(clear = True)

def exportFSToUnreal():
    
    refFiles = pm.system.listReferences()

    rndPattern = re.compile('_render$')
    camPattern = re.compile('_cam', re.I)
    scenePattern = re.compile('^[a-zA-Z]+_s', re.I)

    exportMeshes = []
    exportCamera = None
    for lrf in refFiles:
        if not lrf.isLoaded():
            try:
                lrf.load()
            except:
                pass

    smoothObjsBySet()
          
    for rf in refFiles:
        refFileName = getNameFromFilePath(rf.path)
        
        if rndPattern.search(refFileName):

            rf.selectAll()

            meshes = pm.ls(sl = True, visible = True, type = 'mesh')
            filtedObjs = filterAllRenderAndVisableMeshes(meshes)
            

            pm.select(filtedObjs, r = True)
            if len(filtedObjs) > 1:
                pm.runtime.CombinePolygons()  
                combPol = pm.ls(sl = True)[0]
                try:
                    pm.rename(combPol, refFileName)
                except:
                    pass
                
                exportMeshes.append(combPol)

            elif len(filtedObjs) == 1:
                try:
                    pm.rename(filtedObjs[0], refFileName)
                except:
                    print 'just one object'
                    print rf
                exportMeshes.append(filtedObjs[0])

        elif camPattern.search(refFileName):
            rf.selectAll()
            exportCamera = pm.ls(sl = True, type = 'camera')[0]
            
    
    

    arMatToMaya('FS')
    # offsetAlembicNodesTo0()

    # offsetTransform = pm.xform(exportCamera.getParent(), q = True, ws = True, a = True, t = True)

    exportCameraToUE(exportCamera.getParent())

    frames = mc.idmtProject( timeLine = True, echo  = False)

    start = frames[0]
    end = frames[1]
    # pm.playbackOptions(ast = 0, aet = end - start, min = 0, max = end - start)

    # fEnd = str(end - start)

    abcExpCommand = ''
    for exp in exportMeshes:
        convertNSidedFace2Quad(exp)
        exp.rotateX.set(90)
        exp.scaleX.set(10)
        exp.scaleY.set(10)
        exp.scaleZ.set(10)

        # exp.translateX.set(-1 * offsetTransform[0])
        # exp.translateY.set(-1 * offsetTransform[1])
        # exp.translateZ.set(-1 * offsetTransform[2])

        
        # if re.match(scenePattern,exp.name()):
        #     fEnd = '0'
        jstr = '-frameRange ' + str(start) + ' ' + str(end) + ' -ro -uvWrite -writeFaceSets -writeVisibility -dataFormat ogawa -root ' + exp.fullPath()
        jstr += ' -file ' + getShotPath() + getShotString() + '_' + exp.name() + '.abc'
        abcExpCommand += ' -j "' + jstr + '"'

    mel.eval( 'AbcExport ' + abcExpCommand)


def importProxyModelInAssetFile():
    proxyAssets, proxyCtrls = getProxyData()
    assets = importProxyModel(proxyAssets)

    if proxyCtrls:
        pm.delete(proxyCtrls)

    return assets




def importProxyModel(proxyAssets):
    assets = []
    for asset in proxyAssets:
        importedAsset = importAsset(asset)
        assets.append(importedAsset)
    return assets

def getProxyData():
           
    proxyCtrls = []
    proxyAssets = []
    for c in pm.ls(type = 'nurbsCurve', long = True):
        pCtrl = c.getParent()
        if pCtrl.name().find('_p_ctrl') > -1 :
            proxyCtrls.append(pCtrl)
            assetName = pCtrl.name()
            if assetName.find('|') > -1:
                assetName = assetName.split('|')[-1]

            if assetName.find(':') > -1:
                assetName = assetName.split(':')[-1]

            assetName = assetName.split('_p_ctrl')[0]

            proxyAssets.append(assetName)
              
    proxyCtrls = list(set(proxyCtrls))

    proxyAssets = list(set(proxyAssets))

    return proxyAssets, proxyCtrls


def outputProxyAssetTransformInfo(path):

    proxyAssets, proxyCtrls = getProxyData()
    if proxyAssets:
        if not os.path.lexists(path):
            os.makedirs(path)

    for asset in proxyAssets:
        fh = open(path + asset + '.txt', 'w')

        for ctrl in proxyCtrls:
            
            if ctrl.name().find(asset) > -1:
                
                t = ctrl.translate.get()
                r = ctrl.rotate.get()
                s = ctrl.scale.get()
                newLine = '%f %f %f %f %f %f %f %f %f\n' % (t[0], t[1], t[2], r[0], r[1], r[2], s[0], s[1], s[2],)
                fh.write(newLine)
        fh.close()



def importProxyModelInFsFile():
 
    proxyAssets, proxyCtrls = getProxyData()
    assets = importProxyModel(proxyAssets)
    
    realModels = []   
       
    for asset in assets:
        for ctrl in proxyCtrls:
            n = asset.name().split('_')[0]
            if ctrl.name().find(n) > -1:
                newCtrl = pm.duplicate(asset)[0]
                p = ctrl.getParent()
                pm.parent(newCtrl, p)
                newCtrl.translate.set(ctrl.translate.get())
                newCtrl.rotate.set(ctrl.rotate.get())
                newCtrl.scale.set(ctrl.scale.get())

                realModels.append(newCtrl)

    pm.delete(assets)
    try:
        pm.delete(proxyCtrls)
    except:
        for ctrl in proxyCtrls:
            ctrl.visibility.set(0)
        pass

    return realModels




def importAsset( name ):
    assetFile = ('\\\\file-cluster\GDC\Projects\ShunLiu\Project\scenes\props\%s\master\csl_%s_h_ms_anim.mb') % (name, name)
    print assetFile
    if os.path.isfile(assetFile):
        newObject = pm.importFile(assetFile,returnNewNodes = True)
        for n in newObject:
            if n.nodeType() == 'transform':
                return n.root()
    else:
        return None
        
        
def getProxyController(n):
    try:
        ctrlShape = n.getShape()
        if ctrlShape:
            if n.name().find('_ctrl') > -1 and pm.objectType(ctrlShape) == 'nurbsCurve':   
                return n
            else:
                pa = n.getParent()
                if pa:
                    return getProxyController(pa)
                else:
                    return None
        else:
            pa = n.getParent()
            if pa:
                return getProxyController(pa)
            else:
                return None
    except:
        print n
        pa = n.getParent()
        if pa:
            return getProxyController(pa)
        else:
            return None

def cvtIff2PngAndSet():
    imgcvt = mel.eval('getenv("MAYA_LOCATION")') + '/bin/imgcvt.exe'
    tmpDir = os.environ["TMP"]

    fileNodes = pm.ls(type = 'file')
    for node in fileNodes:
        filePath = os.path.expandvars(node.fileTextureName.get())
        splitext = os.path.splitext(filePath)
        if splitext[1] == '.iff':
            cvtPath = tmpDir + '/' + os.path.basename(splitext[0]) + '.png'
            cmd = imgcvt + ' -f maya -t png ' + filePath + ' ' + cvtPath
            subprocess.call(cmd, shell = True)
            node.fileTextureName.set(cvtPath)


def makeFaceSets(obj):
    try:
        shp = obj.getShape().name()
        
        selList = om.MSelectionList()
        selList.add(shp)
        
        path = om.MDagPath()
        selList.getDagPath(0, path)
        
        fnMesh = om.MFnMesh(path)
        shaders = om.MObjectArray()
        faces = om.MIntArray()
        
        fnMesh.getConnectedShaders(0, shaders, faces)
        if shaders.length() > 0:
            faceIDs = [[] for x in xrange(shaders.length())]
            for i in range(faces.length()):
                faceIDs[faces[i]].append(i)
            
            for i in range(shaders.length()):
                dpn = om.MFnDependencyNode(shaders[i])
                toSelectFaces = []
                for fid in faceIDs[i]:
                    toSelectFaces.append(obj.name() + '.f[' + str(fid) + ']')
                pm.select(toSelectFaces, r = True)
                mc.sets(e = True, fe = 'initialShadingGroup')
                mc.sets(e = True, fe = dpn.name())
    except:
        print '-' * 100
        print obj.name() + ' can not process'
        print '-' * 100
    
    
