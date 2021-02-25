# -*- coding: utf-8 -*-

import maya.cmds as mc
import maya.mel as mel
import pymel.core as pm
import os
import re
import time
import json

import xlrd
import tempfile

import shutil
import tiProjectConfig as tiProjectConfig
reload(tiProjectConfig)

import tiFile as tiFile
reload(tiFile)

import tiPath as tiPath
reload(tiPath)

def IDMTProjects():
    return os.environ.get('IDMT_PROJECTS') if os.environ.get('IDMT_PROJECTS') else mc.error(u'========================【！！！请设置 IDMT_PROJECTS ！！！】========================')


def fileInfos():
    temp = os.path.splitext(os.path.basename(mc.file(query=1, exn=1)))[0]
    info = []
    if '_' in temp:
        info = temp.split('_')
    else:
        mc.error(u'========================【！！！文件名不规范！！！】========================')
    return info


def getObjsByMaterial(mat):
    SE =  mc.listConnections(mat, type = 'shadingEngine')
    if SE:
        objs = mc.listConnections(SE[0], type = 'mesh')
        return objs if objs else []

    return []


def autoRenameMaterials():
    
    sgs = mc.ls(type = 'shadingEngine')

    tf = tiFile.tiAssetFile()
    for sg in sgs:
        objs = mc.listConnections(sg, type = 'mesh')
        mat = mc.listConnections(sg + '.surfaceShader')
        nodeType = mc.nodeType(mat)
        
        objName = objs[0] if objs else 'NOASSIGN'

        objName = objName.split('|')[-1] if '|' in objName else objName
        objName = objName[0:-1] if objName[-1] == '_' else  objName


        newMatName = 'SHD_%s_%s_%s' % (tf.id, objName, nodeType)
        if objName[-1] == '_':
            newMatName = 'SHD_%s_%s%s' % (tf.id, objName, nodeType)

        try:
            if mat != newMatName:
                step = 666
                while True:
                    if mc.objExists(newMatName):
                        objNameAdd = (objName + str(step))
                        newMatName = 'SHD_%s_%s_%s' % (tf.id, objNameAdd, nodeType) 
                        step = step + 1
                        
                    else:
                        break

                mc.rename(mat, newMatName)

                mc.rename(sg, newMatName.replace('SHD_', 'SG_'))
                try: # view shader
                    viewMat = mc.listConnections(newMatName + '.kitty')
                    if viewMat:
                        mc.rename(viewMat, newMatName + '_VW')
                except:
                    pass
        except:
            pass
    

def propName():
    fileInfo = fileInfos()
    if len(fileInfo) > 1 and re.match('^p|^c|^s', fileInfo[1], re.IGNORECASE):
        return fileInfo[1]
    else:
        mc.error(u'========================【！！！Prop文件名不规范！！！】========================')

def currentProjectPrefix():
    fileInfo = fileInfos()
    allProjectInfo = allProjectInfos()
    if allProjectInfo.has_key(fileInfo[0]):
        return fileInfo[0]
    else:
        mc.error(u'========================【！！！项目不存在或检查文件名是否正确！！！】========================')

def allProjectInfos():
    return tiProjectConfig.PROJECTS

def currentProjectInfo():
    return tiProjectConfig.PROJECTS[currentProjectPrefix()]

def projectRoot():
    return os.path.normpath(os.path.join(IDMTProjects(), currentProjectInfo()['fullName']))

def sgAndMeshsInfo():
    SG = mc.ls(type='shadingEngine')
    shaderSGList = dict({})
    for node in SG:
        connectObjsSG = mc.sets(node, q=1)
        if connectObjsSG:
            shaderSGList[node] = connectObjsSG
    return shaderSGList


def nameRulesArray():
    rules = readShaderNameRules()
    endNames = []
    for key in rules:
        items = rules[key]
        for item in items['items']:
            endNames.append(item['eng'].strip())
    return endNames

def readShaderNameRules():
    
    legalNames = {}
    currentType = ''
    rulesFile = os.path.normpath(projectRoot() + '/project/data/shaderRules/Shader_name.xls')
    if os.path.exists(rulesFile):
        xlrd.Book.encoding = "gbk"
        rules = xlrd.open_workbook(rulesFile, encoding_override = 'gbk').sheets()[0] 
        for i in range(rules.nrows):
            name = rules.row_values(i)[0]
            if re.match('^#', name, re.IGNORECASE):
                currentType = name
                legalNames[currentType] = {'chn': rules.row_values(i)[1], 'items': []}
            else:
                if name:
                    legalNames[currentType]['items'].append({'eng': name.strip(), 'chn': rules.row_values(i)[1].strip()})
        return legalNames
    else:
        mc.error(u'file not exists：%s' % rulesFile)




def exportMaterials(file):
    sgs = mc.ls(type = 'shadingEngine')
    expMats = []
    for sg in sgs:
        if sg.find('initial') == -1:
            expMats.append(sg)
    mc.select(expMats, noExpand = True)
    try:
        mc.file(file, type = 'mayaBinary', exportSelected = True, force = True)
    except:
        pass
    print 'Materials exported at: %s' % file





def jsonRead(file):
    if os.path.exists(file):
        fo = open(file)
        data = json.load(fo)
        fo.close()
        return data
    else:
        mc.error('file: %s not exists!!!' % file)



def objDetails(obj):
    mc.currentUnit(linear = 'cm')
    m = pm.xform(obj, q = True, a = True, ws = True, matrix = True)
    t = pm.xform(obj, q = True, a = True, ws = True, translation = True)
    r = pm.xform(obj, q = True, a = True, ws = True, rotation = True)
    s = pm.xform(obj, q = True, a = True, ws = True, scale = True)

    piv = pm.xform(obj, q = True, a = True, ws = True, pivots = True)

    polyInfo = pm.polyEvaluate(obj, edge = True, face = True, vertex = True)

    edge = polyInfo['edge']
    vertex = polyInfo['vertex']
    face = polyInfo['face']

    return [t,r,s,piv,m,edge,vertex,face]

def assignAssetUvs(file):
    mc.select(cl = True)
    logInfo = ''

    data = jsonRead(file)
    objsInfo = data['ObjsInfo']

    objs = objsInfo.keys()
    for mobj in getObjsUnderModel():
        if mobj not in objs:
            logInfo = logInfo + u'物体不存于原文件: %s \n' % mobj

    for key in objsInfo:
        
        if mc.objExists(key):

            objData = objsInfo[key]

            curObj = pm.PyNode(key)

            curObjUVS = curObj.getShape().getUVs()

            # 对比UV，如相同则跳过，不处理
            if curObjUVS[0] == objData['a'][0] and curObjUVS[1] == objData['a'][1]:
                continue
            # mc.select(key, r = True)
            # mel.eval('doBakeNonDefHistory( 1, {"prePost" })')

            xtxNum = pm.polyEvaluate(curObj, vertex = True)

            if xtxNum == objData['detail'][-2]:
                shapes = pm.listRelatives(curObj, shapes = True)
                hasIntermediateObject = False
                for shape in shapes:
                    if shape.intermediateObject.get():
                        hasIntermediateObject = True
                        break
                for i in shapes:
                    if hasIntermediateObject:
                        isIntermediateObject = i.intermediateObject.get()
                        if isIntermediateObject:
                            i.intermediateObject.set(False)

                            i.clearUVs()
                            i.setUVs(objData['a'][0], objData['a'][1])
                            i.assignUVs(objData['b'][0], objData['b'][1])
                            i.reuseTriangles.set(1)
                            i.reuseTriangles.set(0)

                            i.intermediateObject.set(True)
                    else:
                        i.clearUVs()
                        i.setUVs(objData['a'][0], objData['a'][1])
                        i.assignUVs(objData['b'][0], objData['b'][1])
                        i.reuseTriangles.set(1)
                        i.reuseTriangles.set(0)
                    

                        
            else:
                logInfo = logInfo + u'%s : vertex 数量不一致 -> %d(原物体) %d(当前物体) \n' % (i, objData['detail'][-2], xtxNum,)
        else:
            logInfo = logInfo + u'物体不存在: %s \n' % key
    if logInfo:
        print '\n' * 3
        print logInfo
        mc.warning(u'有错误，请打开Script Editor查看错误信息')
    else:
        mc.select(cl = True)
        print(u'===== UV Assign Success =====')

def isOEM():
    
    if os.environ['OFFICE_LOCATION'] == 'GDC_OEM':
        return True
    return False

def timeLine():
    getIsOem = isOEM()

    if getIsOem:
        start = mc.playbackOptions(q = True, min = True)
        end = mc.playbackOptions(q = True, max = True)
        duration = (end - start) + 1
    else:
        start, end, duration = mc.idmtProject( timeLine = True, echo  = False)
    return start, end, duration

def writeFile(content, writeOutFile):
    getIsOEM = isOEM()

    tempJson = writeOutFile if getIsOEM  else os.path.join(tempfile.gettempdir(), os.path.basename(writeOutFile))

    dirPath = os.path.dirname(tempJson)
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)
    fo = open(tempJson, 'w')
    fo.write(content)
    fo.close()

    if not getIsOEM:
        mel.eval("zwSysFile \"move\" \"%s\" \"%s\" 1" % (tempJson.replace("\\", "/"), writeOutFile.replace("\\", "/")))


def sysMoveFile(src, dst, progress = ''):

    print u'=== 文件复制中%s: %s ===' % (progress, os.path.basename(src))

    getIsOEM = isOEM()
    if getIsOEM:
        dirPath = os.path.dirname(dst)
        if not os.path.exists(dirPath):
            os.makedirs(dirPath)

        shutil.move(src, dst)
    else:
        mel.eval("zwSysFile \"move\" \"%s\" \"%s\" 1" % (src.replace("\\", "/"), dst.replace("\\", "/")))

def writeVertexInfo(outFile):
    mc.currentUnit(linear = 'cm')
    infos = {}
    objs = getObjsUnderModel()
    for obj in objs:
        vtxs = pm.polyEvaluate(obj, vertex = True)
        vtxPos = []
        for vtx in range(vtxs):
            pos = pm.xform('%s.vtx[%d]' % (obj, vtx), q = True, a = True, ws = True, translation = True )
            vtxPos.append(pos)
        infos[obj.longName()] = vtxPos
    x = json.dumps(infos)
    writeFile(x,outFile)
    

def getObjsUnderModel():
    allMeshes = pm.ls(type = 'mesh')
    meshes = []
    for i in allMeshes:
        ln = i.longName()
        lnSplit = ln.split('|')
        if len(lnSplit) > 2:
            if '|MODEL|' in i.longName() and  lnSplit[2] == 'MODEL' and (not i.intermediateObject.get()):
                meshes.append(i.getParent())
    return meshes


def distance(vector1,vector2):  
    d=0;  
    for a,b in zip(vector1,vector2):  
        d+=(a-b)**2;  
    return d**0.5;

def compareUv(rgJson, txJson):

    rgData = jsonRead(rgJson)
    rgObjsInfo = rgData['ObjsInfo']

    txData = jsonRead(txJson)
    txObjsInfo = txData['ObjsInfo']


    rgObjs = rgObjsInfo.keys()
    txObjs = txObjsInfo.keys()


    # if curObjUVS[0] == objData['a'][0] and curObjUVS[1] == objData['a'][1]:

    if len(rgObjs) != len(txObjs):
        return False

    for txObj in txObjs:
        if txObjsInfo[txObj]['a'][0] != rgObjsInfo[txObj]['a'][0]:
            return False

        if txObjsInfo[txObj]['a'][1] != rgObjsInfo[txObj]['a'][1]:
            return False

    return True


def compareFile(jsonFile, compareFile):
    isDiffer = False

    data = jsonRead(jsonFile)
    objsInfo = data['ObjsInfo']

    txObjs = objsInfo.keys()
    rgObjs = getObjsUnderModel()
    objInfoA = ''
    shapeDiffer = ''
    for rgObj in rgObjs:
        lname = rgObj.longName()
        if lname not in txObjs:
            objInfoA = objInfoA + u'%s\n' % lname
        else:
            origShape = objsInfo[lname]['shape']
            curShape = rgObj.getShape().name()
            if origShape != curShape:
                shapeDiffer += u'%s -> %s\n' % (curShape, origShape)


    objInfoB = ''
    for txObj in txObjs:
        if txObj not in rgObjs:
            objInfoB = objInfoB + u'%s\n' % txObj

    if objInfoA:
        isDiffer = True
        print (u'以下物体不存在于%s文件中:\n' % compareFile) + objInfoA

    if objInfoB:
        isDiffer = True
        print (u'当前文件对比%s文件,缺少以下物体:\n' % compareFile) + objInfoB

    if shapeDiffer:
        isDiffer = True
        print u'shape名字不一致: cur -> compare\n' + shapeDiffer

    differTypes = ['translation', 'rotation', 'scale', 'pivs', 'matrix', 'edge', 'vertex', 'face']
    detailInfo = ''
    for rgObj in rgObjs:
        rgObjDetail = objDetails(rgObj)
        if objsInfo.has_key(rgObj.longName()):
            txObjDetail = objsInfo[rgObj.longName()]['detail']

            for i, item in enumerate(differTypes):
                if item != 'pivs' and item != 'matrix': #忽略piv轴心的检测
                    if rgObjDetail[i] != txObjDetail[i]:
                        detailInfo = detailInfo + u'%s: %s 数值不一致 -> %s | %s\n' % (rgObj, item, rgObjDetail[i], txObjDetail[i])
                    
    if detailInfo:
       isDiffer = True
       print (u'物体数值不一致( 当前文件 | %s ):\n' % compareFile) + detailInfo


    print (u'=== 文件对比结束 ===\n')


    return isDiffer

def writeAssetInfo(outFile):

    objs = getObjsUnderModel()
    if objs:
        assetInfo = {}
        assetInfo['SGAndMeshsInfo'] = sgAndMeshsInfo()
        assetInfo['ObjsInfo'] = {}

        for i in objs:
            mesh = i.getShape()
            mc.select(cl = True)

            storeData = {}

            storeData['detail'] = objDetails(i)
            
            uvs = mesh.getUVs()
            storeData['a'] = uvs

            auvs = mesh.getAssignedUVs()
            storeData['b'] = auvs

            storeData['shape'] = mesh.name()

            assetInfo['ObjsInfo'][i.longName()] = storeData

        x = json.dumps(assetInfo)

        writeFile(x,outFile)
        print 'asset info file output: %s' % outFile

    else:
        mc.error(u'=== not found any legal output objects, please check the file')


def deleteTurtleNodes():
    turtleNodess = mc.ls('Turtle*')
    for node in turtleNodess:
        unlockAndDelete(node)

def deleteNodesByType(nodeType):
    nodes = mc.ls(type=nodeType)
    for node in nodes:
        unlockAndDelete(node)


def unlockAndDelete(node):
    try:
        mc.lockNode( node, lock=False )
        mc.delete( node )
        print 'delete %s' % node
    except:
        print 'can not delete %s' % node


def batchSetAttrs(node, attrs, override = False):

    for key, val in attrs.items():
        if override:
            mc.editRenderLayerAdjustment(node + '.' + key)

        if type(val) == str:
            mc.setAttr(node + '.' + key, val, type = 'string')
        elif type(val) == tuple:
            r,g,b = val
            mc.setAttr(node + '.' + key, r, g, b, type = 'double3')
        else:
            mc.setAttr(node + '.' + key, val)



def createNode(node, name):
    if mc.objExists(name):
        try:
            mc.delete(name)
        except:
            return node
    newNode = mc.createNode(node, name = name)
    return newNode

def getSeqFiles(filePath):
    from string import digits
    baseDir, filename = os.path.split(filePath)
    name, ext = os.path.splitext(filename)
    filenameNoDigits = name.rstrip(digits)
    if len(filenameNoDigits) == len(name):
        return []

    digitLength = len(name[len(filenameNoDigits):])


    seqFiles = []
    for root, dirs, files in os.walk(baseDir, topdown=False):
      
        for f in files:
            if f.startswith(filenameNoDigits) and f.endswith(ext) and f[len(filenameNoDigits) : -len(ext) if ext else -1].isdigit() and len(f[len(filenameNoDigits): -len(ext)]) ==digitLength:
                
                seqFiles.append(os.path.join(root, f))
    return seqFiles

def changeImageFileToDollarPath():
    changeImageFilePathTo('D')
    # files = mc.ls(type = 'file')
    
    # for f in files:
    #     path = mc.getAttr(f + '.ftn')
    #     dollarPath = tiPath.getDollarPath(path)
        
    #     if path != dollarPath:
    #         mc.setAttr(f + '.ftn', dollarPath, type = 'string')

    # aiImages = mc.ls(type = 'aiImage')
    # for f in aiImages:
    #     path = mc.getAttr(f + '.filename')

    #     dollarPath = tiPath.getDollarPath(path)

    #     if path != dollarPath:
    #         mc.setAttr(f + '.filename', dollarPath, type = 'string')

def changeImageFilePathTo(ty):
    files = mc.ls(type = 'file')
    
    for f in files:
        path = mc.getAttr(f + '.ftn')
        dollarPath = tiPath.changePathType(ty,path)
        
        if path != dollarPath:
            mc.setAttr(f + '.ftn', dollarPath, type = 'string')

    aiImages = mc.ls(type = 'aiImage')
    for f in aiImages:
        path = mc.getAttr(f + '.filename')

        dollarPath = tiPath.changePathType(ty,path)

        if path != dollarPath:
            mc.setAttr(f + '.filename', dollarPath, type = 'string')

'''
import pymel.core as pm
import os

m = pm.ls(sl = True)[0]

uvs = m.getUVs()
auvs = m.getAssignedUVs()

n =pm.ls(sl = True)[0]
n.setUVs(uvs[0],uvs[1])
n.assignUVs(auvs[0], auvs[1])



 def setUvs(data, key, obj):
    
    if data[key]['uvData']:
        vtxFaces = []
        for da in data[key]['uvData']:
            # print da
            # return
            # mc.polyUVSet(key, uvSet = uvset, currentUVSet = True)

            # uvData = obj[uvset]['data']
            # print uvData
            # return
            # if uvData:
            for d in da['v']:

                vtxFaces.append( '%s.vtxFace%s' % (obj.name(), d))


        faceList = mc.polyListComponentConversion( vtxFaces, fvf=True, tf=True )
        # curObj.clearUSVs()

        mc.polyProjection(faceList, type = 'Planar', ch = False, ibd = True, md = 'y')
        pm.polyMapCut(obj, ch = False)

        if obj.name().find('Orig') > -1:
            pm.select(obj, r = True)
            mel.eval('DeleteHistory')

        assignedUVs = obj.getAssignedUVs()

        numUv = pm.polyEvaluate(obj, uv = True)
        uCoords = [None] * numUv
        vCoords = [None] * numUv
        


        for d in data[key]['uvData']:
            for v in d['v']:

                toUv = mc.polyListComponentConversion( '%s.vtxFace%s' % (obj.name(), v), fvf=True, tuv=True )[0]
                splitMap = re.split(r'\[|\]', toUv)
                
                uCoords[int(splitMap[1])] = d['c'][0]
                vCoords[int(splitMap[1])] = d['c'][1]
        
        
        obj.setUVs(uCoords, vCoords)
        obj.assignUVs(assignedUVs[0], assignedUVs[1])



        # for d in data[key]['uvData']:
        #     for v in d['v']:
        #         uvList = mc.polyListComponentConversion( '%s.vtxFace%s' % (obj.name(), v), fvf=True, tuv=True ) # mc.polyListComponentConversion( dd['v'], fvf=True, tuv=True )
        #         if uvList:
        #             mc.polyEditUV(uvList, relative = False, u = d['c'][0], v = d['c'][1])


        pm.polyMergeUV(obj, d = 0.01, ch = False)
        
        # mc.polyUVSet(key, uvSet = currentUvSet, currentUVSet = True)
        if obj.name().find('Orig') > -1:
            pm.select(obj, r = True)
            mel.eval('DeleteHistory')

        # pm.select(obj, r = True)
        # mel.eval('doBakeNonDefHistory( 1, {"prePost" })')

        mc.flushUndo()
        mc.clearCache( all=True )

def readUVData():
    before =  time.time()
    tf = tiFile.tiFile()

    data = jsonRead('d:/%s.json' % tf.id)
    logInfo = ''
    for key in data:
        # try:
        mc.select(cl = True)
        
        origObjs = []

        curObj = pm.PyNode(key)

        for i in pm.listRelatives(curObj.getParent(), shapes = True):
            if i.intermediateObject.get():
                i.intermediateObject.set(False)
                origObjs.append(i)

        if origObjs:

            for origObj in origObjs:
                try:
                    setUvs(data, key, origObj)
                except:
                    pass

            for origObj in origObjs:
                origObj.intermediateObject.set(True)

        else:
            try:
                setUvs(data, key, curObj)
            except:
                pass
                
        
        # except:
        #     logInfo = logInfo + 'obj: %s not exists \n' % key
    if logInfo:
        print logInfo

    print time.time() - before



def aboutUV():
    before =  time.time()
    allMeshes = pm.ls(type = 'mesh')
    meshes = []
    for i in allMeshes:
        ln = i.longName()
        lnSplit = ln.split('|')
        if len(lnSplit) > 2:
            if '|MODEL|' in i.longName() and  lnSplit[2] == 'MODEL' and (not i.intermediateObject.get()):
                meshes.append(i)
    uvDict = {}
    
    for i in meshes:
        mc.select(cl = True)

        storeData = {}

        storeData['detail'] = objDetails(i)
        
        

        coords = i.getUVs()
        data = []
        if coords:
            for uvIndx in range(len(coords[0])):
                tmpDic = {}
                vfList = mc.polyListComponentConversion( '%s.map[%d]' % (i, uvIndx) , fuv=True, tvf=True )
                newVtfList = []
                for vl in mc.ls(vfList, fl  = True):
                    newVtfList.append(vl.split('.vtxFace')[1])
                if vfList:
                    tmpDic['v'] = newVtfList# mc.ls(vfList, fl  = True)
                    tmpDic['c'] = [coords[0][uvIndx],coords[1][uvIndx]]
                data.append(tmpDic)
        
        storeData['uvData'] = data


        uvDict[i.longName()] = storeData


    x = json.dumps(uvDict)
    tf = tiFile.tiFile()
    fo = open('d:/%s.json' % tf.id, 'w')
    fo.write(x)
    fo.close()
    print 'spend time: %d' % (time.time() - before)

'''


