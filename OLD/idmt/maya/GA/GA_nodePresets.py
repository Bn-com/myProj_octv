# -*- coding: utf-8 -*-

'''
Created on 2017-8-8

@author:韩虹

改自CG365
'''

_version = 'Beta v1.0'
_autor = ''
_date = '10/12/2014'
import os, re, sys, ConfigParser, gettext, shutil
from idmt.maya.GA import GA_template as tp
import maya.OpenMayaUI as omui
import maya.OpenMaya as om
import maya.cmds as mc
import maya.mel as mel
from functools import partial
import webbrowser
from xml.etree import ElementTree
from xml.dom import minidom
from xml.etree.ElementTree import Element, SubElement

version = mc.about(version=True)
try:
    import sip
    from PyQt4 import QtCore, QtGui
except:
    from shiboken import wrapInstance
    from PySide import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

xmlTree = {}
btnTree = {}
mayaNodeNames = ['defaultRenderUtilityList1',
 'defaultLightSet',
 'defaultTextureList1',
 'defaultObjectSet',
 'defaultShaderList1',
 'defaultLayer',
 'defaultRenderLayer',
 'defaultViewColorManager',
 'initialShadingGroup',
 'hyperLayout1',
 'initialParticleSE',
 'renderPartition',
 'persp',
 'perspShape',
 'top',
 'topShape',
 'front',
 'frontShape',
 'side',
 'sideShape',
 'layerManager',
 'sequenceManager1',
 'dof1',
 'dynController1',
 'globalCacheControl',
 'hardwareRenderGlobals',
 'hardwareRenderingGlobals',
 'defaultHardwareRenderGlobals',
 'ikSystem',
 'hikSolver',
 'ikRPsolver',
 'ikSCsolver',
 'ikSplineSolver',
 'lambert1',
 'lightLinker1',
 'particleCloud1',
 'characterPartition',
 'renderPartition',
 'shaderGlow1',
 'strokeGlobals',
 'time1']
customNodeTypes = ['mesh', 'nurbsSurface']
minorNodeTypes = mc.optionVar(query='minorNodeTypes')
mayaNodeTypes = []
for nodeTag in minorNodeTypes:
    nodeType = mc.objectType(tpt=nodeTag)
    if nodeType != 'materialInfo':
        mayaNodeTypes.append(nodeType)

mayaNodeTypes.sort()
mayaNodeNames.sort()

def getMayaWindow():
    ptr = omui.MQtUtil.mainWindow()
    try:
        return wrapInstance(long(ptr), QtGui.QWidget)
    except:
        return sip.wrapinstance(long(ptr), QtCore.QObject)


def getPresetFolder():
    mayaAppDirTemp = os.getenv('MAYA_APP_DIR')
    nodePresets = 'Presets/Material/'
    filePath = mayaAppDirTemp + '/' + nodePresets
    if not os.path.exists(mayaAppDirTemp + '/' + nodePresets):
        os.path.join(mayaAppDirTemp, nodePresets)
        os.makedirs(filePath)
    return filePath


def processString(inputStr):
    attr = inputStr
    attr = attr.replace('\n', '\\n')
    attr = attr.replace('\r', '\\r')
    attr = attr.replace('"', '\\"')
    attr = attr.replace("'", "\\'")
    return attr


def getAttrsToPublish(nodeName, listAttrString):
    atrs = mel.eval(listAttrString + ' ' + nodeName)
    if mc.container(nodeName, isContainer=True, q=True):
        pubAttrs = mc.container(nodeName, ba=True, q=True)
        pubCount = len(pubAttrs)
        for pp in range(1, pubCount, 2):
            cmd = listAttrString + ' ' + nodeName + '.' + pubAttrs[pp]
            testAttr = mel.eval(cmd)
            if len(testAttr) == 1 and testAttr[0] == pubAttrs[pp]:
                atrs[len(atrs)] = pubAttrs[pp]

    return atrs


def prettify(elem):
    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent='  ')


def createAttrPreset(nodeName, presetName):
    if not mc.objExists(nodeName):
        return ''
    nType = mc.nodeType(nodeName)
    attrPreset = Element('attrPreset')
    attrPreset.set('type', nType)
    attrPreset.set('presetName', presetName)
    listAttrString = 'listAttr -read -write -visible -hasData'
    atrs = getAttrsToPublish(nodeName=nodeName, listAttrString=listAttrString)
    for atr in atrs:
        objAt = nodeName + '.' + atr
        if mc.objExists(objAt):
            atype = mc.getAttr(objAt, sl=True, type=True)
            if 'string' == atype:
                if not mc.listAttr(objAt, hasNullData=True):
                    value = mc.getAttr(objAt)
                    value = processString(value)
                    attribute = SubElement(attrPreset, 'attribute')
                    attribute.set('name', atr)
                    attribute.set('type', 'string')
                    attribute.set('value', value)

    listAttrString = 'listAttr -multi -write -scalar -visible -hasData'
    atrs = getAttrsToPublish(nodeName=nodeName, listAttrString=listAttrString)
    for atr in atrs:
        if not mel.eval('validNodeTypeAttrForCurrentPreset("%s","%s")' % (nType, atr)):
            continue
        value = mc.getAttr(nodeName + '.' + atr)
        attribute = SubElement(attrPreset, 'attribute')
        attribute.set('name', atr)
        attribute.set('value', str(float(value)))

    return prettify(attrPreset)


def saveAttrPreset(node, ppath, presetName, postName, autoRename):
    if mc.about(evalVersion=True):
        om.MGlobal.displayWarning('saveAttrPreset is not supported in Maya PLE.')
        return ''
    if not mc.objExists(node):
        return ''
    psetCommand = createAttrPreset(nodeName=node, presetName=presetName)
    tempNode = node
    if node.split(':') != -1:
        tempNode = node.split(':')[-1]
    outPath = ppath + '/' + presetName + '_' + tempNode + '.' + postName
    xFile = open(outPath, 'w')
    xFile.write(psetCommand)
    xFile.close()


def applyPresetToNode(createNodeProc, deleteNodeProc, presetName, blend, *args):
    nodes = mc.ls(sl=1)
    if nodes:
        for node in nodes:
            if os.path.exists(presetName):
                tree = ElementTree.parse(presetName)
                root = tree.getroot()
                attributes = root.getiterator('attribute')
                for atr in attributes:
                    attribute = atr.get('name')
                    objAttr = node + '.' + attribute
                    value = atr.get('value')
                    if attribute == 'notes':
                        if not mel.eval('attributeExists %s %s' % (attribute, node)):
                            mc.addAttr(node, ln=attribute, dt=atr.get('type'))
                            mc.setAttr(objAttr, keyable=True, e=True)
                    try:
                        if mc.objExists(objAttr) and mc.getAttr(objAttr, settable=True):
                            currentValue = mc.getAttr(objAttr)
                            if atr.get('type') == 'string':
                                try:
                                    mc.setAttr(objAttr, value, type='string')
                                    print 'setAttr "%s" %s;' % (objAttr, value)
                                except:
                                    print 'have not setAttr "%s" %s;' % (objAttr, value)

                            elif blend == 1:
                                try:
                                    mc.setAttr(objAttr, float(value))
                                    print 'setAttr "%s" %s;' % (objAttr, float(value))
                                except:
                                    print 'have not setAttr "%s" %s;' % (objAttr, value)

                            elif float(currentValue) > float(value):
                                try:
                                    mc.setAttr(objAttr, float(currentValue) - (float(currentValue) - float(value)) * float(blend))
                                    print 'setAttr "%s" %s;' % (objAttr, float(currentValue) - (float(currentValue) - float(value)) * float(blend))
                                except:
                                    print 'have not setAttr "%s" %s;' % (objAttr, float(currentValue))

                            elif float(currentValue) < float(value):
                                try:
                                    mc.setAttr(objAttr, float(currentValue) + (float(value) - float(currentValue)) * float(blend))
                                    print 'setAttr "%s" %s;' % (objAttr, float(currentValue) + (float(value) - float(currentValue)) * float(blend))
                                except:
                                    print 'have not setAttr "%s" %s;' % (objAttr, float(currentValue) + (float(value) - float(currentValue)) * float(blend))

                    except:
                        print 'Have not the "%s"' % objAttr

                om.MGlobal.displayInfo('Succeed apply preset to %s node.' % node)
            else:
                om.MGlobal.displayWarning('No preset named %s for nodeType %s' % (presetName, nType))


def createNodeList(node, list, *args):
    nodes = mc.listConnections(node, connections=False, plugs=False, shapes=True, source=True, destination=True, skipConversionNodes=False)
    if nodes:
        for node in nodes:
            if node not in list:
                if mc.nodeType(node) not in mayaNodeTypes:
                    if node not in mayaNodeNames:
                        if mc.nodeType(node) not in customNodeTypes:
                            list.append(node)
                            createNodeList(node=node, list=list)


def createConnectMapPreset(node, ppath, presetName, autoRename):
    nType = mc.nodeType(node)
    nodeList = []
    createNodeList(node=node, list=nodeList)
    connectMapElement = Element('connectMap')
    tempNode = node
    if node.split(':') != -1:
        tempNode = node.split(':')[-1]
    connectMapElement.set('rootNodeName', tempNode)
    connectMapElement.set('rootNodeType', nType)
    connectMapElement.set('presetName', presetName)
    nodesElement = SubElement(connectMapElement, 'nodes')
    connectionsElement = SubElement(connectMapElement, 'connections')
    toDefaultConnectionsElement = SubElement(connectMapElement, 'toDefaultConnections')
    for newNode in nodeList:
        saveAttrPreset(node=newNode, ppath=ppath, presetName=presetName, postName='xml', autoRename=None)
        nodeElement = SubElement(nodesElement, 'node')
        tempNewNode = newNode
        if newNode.split(':') != -1:
            tempNewNode = newNode.split(':')[-1]
        nodeElement.set('name', tempNewNode)
        nodeElement.set('type', mc.nodeType(newNode))
        sourceAttrs = mc.listConnections(newNode, connections=True, plugs=True, source=True, destination=False, skipConversionNodes=True)
        if sourceAttrs:
            for i in range(0, len(sourceAttrs)):
                if i % 2:
                    fromBuffer = sourceAttrs[i].split('.')
                    fromNode = fromBuffer[0]
                    fromAttr = ''
                    if len(fromBuffer) == 2:
                        fromAttr = fromBuffer[1]
                    else:
                        for intex in range(1, len(fromBuffer)):
                            fromAttr += fromBuffer[intex] + '.'

                        fromAttr = fromAttr[:-1]
                    toBuffer = sourceAttrs[i - 1].split('.')
                    toNode = toBuffer[0]
                    toAttr = ''
                    if len(toBuffer) == 2:
                        toAttr = toBuffer[1]
                    else:
                        for intex in range(1, len(toBuffer)):
                            toAttr += toBuffer[intex] + '.'

                        toAttr = toAttr[:-1]
                    if mc.nodeType(fromNode) not in mayaNodeTypes and mc.nodeType(toNode) not in mayaNodeTypes:
                        if mc.nodeType(fromNode) not in customNodeTypes and mc.nodeType(toNode) not in customNodeTypes:
                            if fromNode not in mayaNodeNames and toNode not in mayaNodeNames:
                                connectInfos = connectionsElement.getiterator('connect')
                                state = True
                                for connectInfo in connectInfos:
                                    if connectInfo.get('fromNode') == fromNode and connectInfo.get('fromAttr') == fromAttr and connectInfo.get('toNode') == toNode and connectInfo.get('toAttr') == toAttr:
                                        state = False

                                if state:
                                    connectElement = SubElement(connectionsElement, 'connect')
                                    tempFromNode = fromNode
                                    if fromNode.split(':') != -1:
                                        tempFromNode = fromNode.split(':')[-1]
                                    tempToNode = toNode
                                    if toNode.split(':') != -1:
                                        tempToNode = toNode.split(':')[-1]
                                    connectElement.set('fromNode', tempFromNode)
                                    connectElement.set('fromAttr', fromAttr)
                                    connectElement.set('toNode', tempToNode)
                                    connectElement.set('toAttr', toAttr)
                    if fromNode not in nodeList or toNode not in nodeList:
                        if mc.nodeType(fromNode) not in customNodeTypes and mc.nodeType(toNode) not in customNodeTypes:
                            toDefaultConnectElement = SubElement(toDefaultConnectionsElement, 'toDefaultConnect')
                            tempFromNode = fromNode
                            if fromNode.split(':') != -1:
                                tempFromNode = fromNode.split(':')[-1]
                            tempToNode = toNode
                            if toNode.split(':') != -1:
                                tempToNode = toNode.split(':')[-1]
                            toDefaultConnectElement.set('fromNode', tempFromNode)
                            toDefaultConnectElement.set('fromAttr', fromAttr)
                            toDefaultConnectElement.set('toNode', tempToNode)
                            toDefaultConnectElement.set('toAttr', toAttr)

        destinationAttrs = mc.listConnections(newNode, connections=True, plugs=True, source=False, destination=True, skipConversionNodes=True)
        if destinationAttrs:
            for i in range(0, len(destinationAttrs)):
                if i % 2:
                    fromBuffer = destinationAttrs[i - 1].split('.')
                    fromNode = fromBuffer[0]
                    fromAttr = ''
                    if len(fromBuffer) == 2:
                        fromAttr = fromBuffer[1]
                    else:
                        for intex in range(1, len(fromBuffer)):
                            fromAttr += fromBuffer[intex] + '.'

                        fromAttr = fromAttr[:-1]
                    toBuffer = destinationAttrs[i].split('.')
                    toNode = toBuffer[0]
                    toAttr = ''
                    if len(toBuffer) == 2:
                        toAttr = toBuffer[1]
                    else:
                        for intex in range(1, len(toBuffer)):
                            toAttr += toBuffer[intex] + '.'

                        toAttr = toAttr[:-1]
                    if mc.nodeType(fromNode) not in mayaNodeTypes and mc.nodeType(toNode) not in mayaNodeTypes:
                        if mc.nodeType(fromNode) not in customNodeTypes and mc.nodeType(toNode) not in customNodeTypes:
                            if fromNode not in mayaNodeNames and toNode not in mayaNodeNames:
                                connectInfos = connectionsElement.getiterator('connect')
                                state = True
                                for connectInfo in connectInfos:
                                    if connectInfo.get('fromNode') == fromNode and connectInfo.get('fromAttr') == fromAttr and connectInfo.get('toNode') == toNode and connectInfo.get('toAttr') == toAttr:
                                        state = False

                                if state:
                                    connectElement = SubElement(connectionsElement, 'connect')
                                    tempFromNode = fromNode
                                    if fromNode.split(':') != -1:
                                        tempFromNode = fromNode.split(':')[-1]
                                    tempToNode = toNode
                                    if toNode.split(':') != -1:
                                        tempToNode = toNode.split(':')[-1]
                                    connectElement.set('fromNode', tempFromNode)
                                    connectElement.set('fromAttr', fromAttr)
                                    connectElement.set('toNode', tempToNode)
                                    connectElement.set('toAttr', toAttr)
                    if fromNode not in nodeList or toNode not in nodeList:
                        if mc.nodeType(fromNode) not in customNodeTypes and mc.nodeType(toNode) not in customNodeTypes:
                            toDefaultConnectElement = SubElement(toDefaultConnectionsElement, 'toDefaultConnect')
                            tempFromNode = fromNode
                            if fromNode.split(':') != -1:
                                tempFromNode = fromNode.split(':')[-1]
                            tempToNode = toNode
                            if toNode.split(':') != -1:
                                tempToNode = toNode.split(':')[-1]
                            toDefaultConnectElement.set('fromNode', tempFromNode)
                            toDefaultConnectElement.set('fromAttr', fromAttr)
                            toDefaultConnectElement.set('toNode', tempToNode)
                            toDefaultConnectElement.set('toAttr', toAttr)

    return prettify(connectMapElement)


def saveConnectMapPreset(node, ppath, presetName, postName = 'connectMap', autoRename = None, mode = None, *args):
    if mc.about(evalVersion=True):
        om.MGlobal.displayWarning('saveAttrPreset is not supported in Maya PLE.')
        return ''
    if not mc.objExists(node):
        return ''
    ntype = mc.nodeType(node)
    postPath = '/'
    tempPath = ppath + postPath
    if not mc.file(tempPath, ex=True, q=True):
        os.mkdir(tempPath)
    outPath = tempPath + '/' + presetName + '.' + postName
    postPath += '/' + presetName + '.' + postName
    i = 0
    state = True
    if mode != 'modify':
        if os.path.exists(outPath):
            doReplace = 'Auto Rename'
            no = 'No'
            if not autoRename:
                doReplace = mc.confirmDialog(title='Confirm', message='File Exists. Overwrite?', button=['Yes', no, doReplace], defaultButton=doReplace)
            if doReplace == no:
                return (False,
                 '%s%s' % (presetName, ''),
                 postPath,
                 ntype)
            if doReplace == 'Auto Rename':
                overwrite = 1
                presetName = presetName.replace('[0-9]', '')
                presetName = presetName.replace('[0-9]', '')
                for i in range(1, 100):
                    outPath = ppath + '/' + presetName + str(i) + '.' + postName
                    presetName = presetName + str(i)
                    if not os.path.exists(outPath):
                        overwrite = 0
                        break

                if overwrite:
                    om.MGlobal.displayWarning('Overwriting existing preset %s' % presetName)
                else:
                    om.MGlobal.displayInfo('Renaming preset to %s%s' % (presetName, i))
            if doReplace == 'Yes':
                i = ''
                state = True
        else:
            i = ''
    else:
        om.MGlobal.displayInfo('Modifed the current preset %s' % presetName)
    presetCommand = createConnectMapPreset(node=node, ppath=tempPath, presetName=presetName, autoRename=autoRename)
    xFile = open(outPath, 'w')
    xFile.write(presetCommand)
    xFile.close()
    return (state,
     '%s%s' % (presetName, i),
     postPath,
     ntype)


def applyConnectMapToNode(node, presetDirPath, presetName, blend, *args):
    global returnStr
    ppath = presetDirPath + '/' + presetName + '.connectMap'
    nType = mc.nodeType(node)
    oldName = node
    nodeList = []
    newNodes = []
    tree = ElementTree.parse(ppath)
    root = tree.getroot()
    oldRootName = root.get('rootNodeName')
    oldRootType = root.get('rootNodeType')
    newRootName = presetName + '_' + oldRootName
    if nType == oldRootType:
        if os.path.exists(ppath):
            createNodeList(node=node, list=nodeList)
            SGNodes = mc.listConnections(node, type='shadingEngine')
            sourceAttrs = []
            if SGNodes:
                SGNode = SGNodes[0]
                sourceAttrs = mc.listConnections(SGNode, plugs=True, source=True, destination=False, connections=True, shapes=True)
            for delNode in nodeList:
                if delNode != node:
                    if mc.objExists(delNode):
                        connectNodes = mc.listConnections(delNode, plugs=False, shapes=True, connections=False, type='groupId')
                        if connectNodes:
                            for connectNode in connectNodes:
                                mc.lockNode(connectNode, lock=True)

                        try:
                            mc.delete(delNode)
                        except:
                            pass

                        if connectNodes:
                            for connectNode in connectNodes:
                                mc.lockNode(connectNode, lock=False)

            node = mc.rename(node, newRootName)
            nodes = root.getiterator('node')
            connectInfos = root.getiterator('connect')
            toDefaultConnectInfos = root.getiterator('toDefaultConnect')
            nodeNumber = len(nodes)
            connectNumber = len(connectInfos)
            toDefaultConnectNumber = len(toDefaultConnectInfos)
            size = 2 * nodeNumber + connectNumber + toDefaultConnectNumber
            if size:
                step = float(100 / size)
            else:
                step = 1
            amount = 0
            mc.progressWindow(title='Progress', progress=amount, status='completed:', isInterruptable=True)
            autoNameDic = {}
            for index in range(0, nodeNumber):
                nodeName = presetName + '_' + nodes[index].get('name')
                if nodeName != node:
                    if mc.objExists(nodeName):
                        newPresetName = presetName.replace('[0-9]', '')
                        newPresetName = newPresetName.replace('[0-9]', '')
                        for i in range(1, 100):
                            newNodeName = newPresetName + str(i) + '_' + nodes[index].get('name')
                            if not mc.objExists(newNodeName):
                                autoNameDic[nodeName] = newNodeName
                                break

                nodeType = nodes[index].get('type')
                if nodeName != node:
                    shaderNodeTypes = ['useBackground',
                     'layeredShader',
                     'hairTubeShader',
                     'shadingMap',
                     'anisotropic',
                     'blinn',
                     'lambert',
                     'phong',
                     'phongE',
                     'rampShader',
                     'surfaceShader',
                     'aiAmbientOcclusion',
                     'aiHair',
                     'aiRaySwitch',
                     'aiShadowCatcher',
                     'aiSkin',
                     'aiStandard',
                     'aiUtility',
                     'aiWireframe',
                     'RedshiftArchitectural',
                     'RedshiftCarPaint',
                     'RedshiftSubSurfaceScatter',
                     'RedshiftSprite',
                     'RedshiftMatteShadowCatcher',
                     'RedshiftMaterialBlender',
                     'RedshiftIncandescent',
                     'RedshiftHair',
                     'oceanShader',
                     'builtin_bsdf_architectural',
                     'builtin_bsdf_architectural_comp',
                     'builtin_bsdf_ashikhmin',
                     'builtin_bsdf_carpaint',
                     'builtin_bsdf_lambert',
                     'builtin_bsdf_mirror',
                     'builtin_bsdf_phong',
                     'mi_metallic_paint',
                     'mib_illum_ward',
                     'mib_glossy_refraction',
                     'mib_illum_ward_deriv',
                     'misss_skin_specular',
                     'misss_fast_shader2',
                     'mib_illum_phong',
                     'misss_call_shader',
                     'mi_car_paint_phen',
                     'mib_illum_hair',
                     'mib_illum_lambert',
                     'path_material',
                     'mib_illum_cooktorr',
                     'mib_illum_blinn',
                     'misss_fast_simple_maya',
                     'misss_fast_shadermib_glossy_reflection',
                     'misss_set_normal',
                     'misss_mia_skin2_surface_phen',
                     'mi_metallic_paint_x_passes',
                     'misss_fast_shader2_x',
                     'mi_metallic_paint_x',
                     'mi_car_paint_phen_x_passes',
                     'mi_car_paint_phen_x',
                     'misss_fast_shader2_x',
                     'misss_fast_shader_xmisss_fast_shader_x_passes',
                     'misss_fast_shader_x',
                     'misss_fast_shader_x',
                     'mia_material1',
                     'mia_material_x',
                     'mia_material_x_passes',
                     'dgs_material',
                     'dielectric_material',
                     'misss_physical',
                     'transmat']
                    if nodeType in shaderNodeTypes:
                        mc.shadingNode(nodeType, name=autoNameDic.get(nodeName, nodeName), asShader=True)
                    elif nodeType == 'shadingEngine':
                        mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=autoNameDic.get(nodeName, nodeName))
                    else:
                        mc.createNode(nodeType, name=autoNameDic.get(nodeName, nodeName))
                    if nodeType == 'RedshiftPhysicalSky':
                        mc.addAttr(autoNameDic.get(nodeName, nodeName), shortName='rsSkyExposure', longName='rsSkyExposure', hidden=True, at='message')
                if mc.progressWindow(query=True, isCancelled=True):
                    break
                if mc.progressWindow(query=True, progress=True) >= 100:
                    break
                amount += step
                mc.progressWindow(edit=True, progress=amount)

            for newNode in nodes:
                nodeName = newNode.get('name')
                nodePresetFilePath = ppath.split('.')[0] + '_' + nodeName + '.xml'
                if os.path.exists(nodePresetFilePath):
                    newName = presetName + '_' + nodeName
                    newName = autoNameDic.get(newName, newName)
                    mc.select(newName, r=True)
                    applyPresetToNode(createNodeProc='', deleteNodeProc='', presetName=nodePresetFilePath, blend=blend)
                if mc.progressWindow(query=True, isCancelled=True):
                    break
                if mc.progressWindow(query=True, progress=True) >= 100:
                    break
                amount += step
                mc.progressWindow(edit=True, progress=amount)

            for connectInfo in connectInfos:
                if connectInfo.get('fromNode') in mayaNodeNames:
                    fromNodeName = connectInfo.get('fromNode')
                else:
                    fromNodeName = presetName + '_' + connectInfo.get('fromNode')
                    fromNodeName = autoNameDic.get(fromNodeName, fromNodeName)
                if connectInfo.get('toNode') in mayaNodeNames:
                    toNodeName = connectInfo.get('toNode')
                else:
                    toNodeName = presetName + '_' + connectInfo.get('toNode')
                    toNodeName = autoNameDic.get(toNodeName, toNodeName)
                fromNodeAndAttr = fromNodeName + '.' + connectInfo.get('fromAttr')
                toNodeAndAttr = toNodeName + '.' + connectInfo.get('toAttr')
                try:
                    if mc.attributeQuery(connectInfo.get('fromAttr'), node=fromNodeName, exists=True):
                        if mc.attributeQuery(connectInfo.get('toAttr'), node=toNodeName, exists=True):
                            if not mc.isConnected(fromNodeAndAttr, toNodeAndAttr):
                                mc.connectAttr(fromNodeAndAttr, toNodeAndAttr, force=True)
                except:
                    print '%s have not connect %s' % (fromNodeAndAttr, toNodeAndAttr)

                if mc.progressWindow(query=True, isCancelled=True):
                    break
                if mc.progressWindow(query=True, progress=True) >= 100:
                    break
                amount += step
                mc.progressWindow(edit=True, progress=amount)

            for toDefaultConnectInfo in toDefaultConnectInfos:
                if toDefaultConnectInfo.get('fromNode') in mayaNodeNames:
                    fromNodeName = toDefaultConnectInfo.get('fromNode')
                else:
                    fromNodeName = presetName + '_' + toDefaultConnectInfo.get('fromNode')
                    fromNodeName = autoNameDic.get(fromNodeName, fromNodeName)
                if toDefaultConnectInfo.get('toNode') in mayaNodeNames:
                    toNodeName = toDefaultConnectInfo.get('toNode')
                else:
                    toNodeName = presetName + '_' + toDefaultConnectInfo.get('toNode')
                    toNodeName = autoNameDic.get(toNodeName, toNodeName)
                fromNodeAndAttr = fromNodeName + '.' + toDefaultConnectInfo.get('fromAttr')
                toNodeAndAttr = toNodeName + '.' + toDefaultConnectInfo.get('toAttr')
                tempDestinationAttr = toNodeAndAttr
                letterPat = '[a-zA-Z0-9_]+'
                buf = re.findall(letterPat, tempDestinationAttr)
                numIndex = 0
                returnStr = ''
                for index in range(0, len(buf)):
                    if buf[index].isdigit():
                        numIndex = index

                attrNum = int(buf[numIndex])
                numState(objAttr=tempDestinationAttr, attrNum=attrNum)
                try:
                    mc.connectAttr(fromNodeAndAttr, returnStr)
                except:
                    print '%s have not connect %s' % (fromNodeAndAttr, toNodeAndAttr)

                if mc.progressWindow(query=True, isCancelled=True):
                    break
                if mc.progressWindow(query=True, progress=True) >= 100:
                    break
                amount += step
                mc.progressWindow(edit=True, progress=amount)

            mc.progressWindow(endProgress=1)
            newNodes.append(mc.rename(node, oldName))
            if newNodes:
                for obj in newNodes:
                    if mc.objExists(obj):
                        SGNodes = mc.listConnections(obj, type='shadingEngine')
                        if SGNodes:
                            SGNode = mc.rename(SGNodes[0], obj + 'SG')
                            if sourceAttrs:
                                for indexA in range(0, len(sourceAttrs)):
                                    if indexA % 2:
                                        attrBuf = sourceAttrs[indexA - 1].split('.')
                                        attr = attrBuf[1]
                                        try:
                                            mc.connectAttr(sourceAttrs[indexA], '%s.%s' % (SGNode, attr))
                                        except:
                                            om.MGlobal.displayInfo('The "%s" have not connect the "%s.%s"' % (sourceAttrs[indexA], SGNode, attr))

            om.MGlobal.displayInfo('Succeed apply preset to %s node.' % node)
        else:
            om.MGlobal.displayWarning('No preset named %s for nodeType %s' % (presetName, nType))
    else:
        om.MGlobal.displayWarning('Please select the "%s" type node' % oldRootType)


def numState(objAttr, attrNum):
    global returnStr
    newToNodeAndAttr = ''
    letterPat = '[a-zA-Z0-9_]+'
    buf = re.findall(letterPat, objAttr)
    numIndex = 0
    for index in range(0, len(buf)):
        if buf[index].isdigit():
            numIndex = index

    for index in range(0, len(buf)):
        if index == numIndex:
            newToNodeAndAttr += '[' + str(attrNum) + '].'
        elif index == numIndex - 1 or index == len(buf) - 1:
            newToNodeAndAttr += buf[index]
        else:
            newToNodeAndAttr += buf[index] + '.'

    if mc.connectionInfo(newToNodeAndAttr, isDestination=True):
        attrNum = attrNum + 1
        numState(objAttr=newToNodeAndAttr, attrNum=attrNum)
    else:
        returnStr = newToNodeAndAttr


def xmlParse(file):
    tree = ElementTree.parse(file)
    root = tree.getroot()
    modulesIter = root.getchildren()
    modules = {}
    for module in modulesIter:
        if not modules.has_key(module.tag):
            modules[module.tag] = {}
        for nodeType in module.getchildren():
            if not modules[module.tag].has_key(nodeType.tag):
                modules[module.tag][nodeType.tag] = []
            for preset in nodeType.getchildren():
                modules[module.tag][nodeType.tag].append(preset.get('path'))

    return modules


class iniFile():

    def __init__(self, fileDir, fileName, *args):
        self.iniFile = fileDir + '/' + fileName
        self.config = ConfigParser.ConfigParser()
        if not os.path.exists(self.iniFile):
            self.config.add_section('setting')
            self.config.set('setting', 'language', '')
            self.config.set('setting', 'presets_dir', '')
            self.config.set('setting', 'auto_refresh', '')
            self.config.set('setting', 'preset_mode', '')
            self.config.write(open(self.iniFile, 'w'))

    def getValue(self, item, *args):
        self.config.readfp(open(self.iniFile))
        return self.config.get('setting', item)

    def setValue(self, item, value, *args):
        self.config.read(self.iniFile)
        self.config.set('setting', item, value)
        #self.config.write(open(self.iniFile, 'w'))
class win(tp.templateWindow):
    def __init__(self):
        tp.templateWindow.__init__(self)
        self.cutSize = 65
        self.fileDic = []
        self.treeDic = {}
        self.manualItem = ''
        self.gridLayoutNumberOfChildren = 5
        self.configFilePath = 'Z:/Resource/Library/Public/Final/Library/Preset'
        self.userAppDir = mc.internalVar(userAppDir=True)
        self.rootDir ='Z:/Resource/Library/Public/Final/Library'
        self.iniFile = iniFile(fileDir=self.configFilePath, fileName='jn_nodePresets.config')
        self.initPresetFilePath()
        self.language = self.iniFile.getValue('language')
        self.presetsDir = self.iniFile.getValue('presets_dir')
        self.autoRefresh = self.iniFile.getValue('auto_refresh')
        self.presetMode = self.iniFile.getValue('preset_mode')
        if self.language == '':
            self.iniFile.setValue('language', 'en_US')
            self.language = self.iniFile.getValue('language')
        if self.presetsDir == '' or not os.path.exists(self.presetsDir):
            self.iniFile.setValue('presets_dir', self.initPresetFilePath())
            self.presetsDir = self.iniFile.getValue('presets_dir')
        if self.autoRefresh == '':
            self.iniFile.setValue('auto_refresh', 'Auto')
            self.autoRefresh = self.iniFile.getValue('auto_refresh')
        if self.presetMode == '':
            self.iniFile.setValue('preset_mode', 'overwrite')
            self.presetMode = self.iniFile.getValue('preset_mode')
        self.localePath = self.rootDir + '/locale'
        gettext.install('nodePresets_lang', self.localePath, unicode=True)
        gettext.translation('nodePresets_lang', self.localePath, languages=[self.language]).install(True)
        self.uiContent['window'] = 'jn_nodePresetsWindow'
        self.uiContent['size'] = (800, 600)
        self.uiContent['title'] = _('Node Preset Library')

    def commonMenu(self):
        """Create common menu items for all option boxes"""
        self.uiContent['editMenu'] = mc.menu(label=_('Edit'))
        self.uiContent['editMenuPreferences'] = mc.menuItem(label=_('Preferences'), subMenu=True)
        self.uiContent['editMenuSwitchLanguage'] = mc.menuItem(label=_('Language'), subMenu=True)
        self.uiContent['editMenuSwitchLanguageUS'] = mc.menuItem(label=_('English'), command=partial(self.switchLanguage, 'en_US'))
        self.uiContent['editMenuSwitchLanguageCN'] = mc.menuItem(label=_('Simplified Chinese'), command=partial(self.switchLanguage, 'zh_CN'))
        self.uiContent['toolsMenu'] = mc.menu(label=_('Tool'))
        if self.autoRefresh == 'Auto':
            self.uiContent['autoRefreshMenu'] = mc.menuItem(label=_('Auto Refresh'), checkBox=True, command=self.autoRefreshJobCmd)
        elif self.autoRefresh == 'Manual':
            self.uiContent['autoRefreshMenu'] = mc.menuItem(label=_('Auto Refresh'), checkBox=False, command=self.autoRefreshJobCmd)
        mc.menuItem(subMenu=True, label=_('Mode'))
        mc.radioMenuItemCollection()
        self.uiContent['overwriteMenuItem'] = mc.menuItem(label=_('Overwrite'), radioButton=True, command=self.presetModeOverwriteCmd)
        self.uiContent['modifyMenuItem'] = mc.menuItem(label=_('Modify'), radioButton=False, command=self.presetModeModifyCmd)
        self.presetModeCmd()
        self.uiContent['hypershadeMenu'] = mc.menuItem(parent=self.uiContent['toolsMenu'], label=_('Hypershade'), command=self.hypershadeCmd)
        self.uiContent['renderMenu'] = mc.menu(label=_('Render'))
        self.uiContent['renderMenuMayaSoftware'] = mc.menuItem(label=_('Maya Software'), command=self.selectMayaSoftwareNode)
        self.uiContent['renderMenuMayaHardware'] = mc.menuItem(label=_('Maya Hardware'), command=self.selectMayaHardwareNode)
        self.uiContent['renderMenuMayaHardware2_0'] = mc.menuItem(label=_('Maya Hardware 2.0'), command=self.selectMayaHardware2Node)
        self.uiContent['renderMenuRedshift'] = mc.menuItem(label=_('Redshift'), command=self.selectRedshiftNode)
        self.uiContent['renderMenuArnoldRenderer'] = mc.menuItem(label=_('Arnold Renderer'), command=self.selectArnoldRendererNode)
        self.uiContent['renderMenuMentalray'] = mc.menuItem(label=_('Mental ray'), command=self.selectMentalrayNode)
        self.uiContent['helpMenu'] = mc.menu(label=_('Help'))
        self.uiContent['helpMenuItem'] = mc.menuItem(label='Help on %s' % self.uiContent['title'], command=self.helpMenuCmd)
        if self.language == 'zh_CN':
            mc.menuItem(self.uiContent['editMenuSwitchLanguageCN'], edit=True, enable=False)
        if self.language == 'en_US':
            mc.menuItem(self.uiContent['editMenuSwitchLanguageUS'], edit=True, enable=False)

    def switchLanguage(self, language, *args):
        self.iniFile.setValue('language', language)

    def outputNukeToolCmd(self, *args):
        jn_ns.main()

    def proxyMeshSettingCmd(self, *args):
        jn_rpms.main()

    def shaderTransferCmd(self, *args):
        mel.eval('GShaderTransfer')

    def nodePresetCmd(self, *args):
        jn_np.main()

    def hypershadeCmd(self, *args):
        mel.eval('HypershadeWindow;')

    def selectMayaSoftwareNode(self, *args):
        mc.select('defaultRenderQuality', r=True)

    def selectMayaHardwareNode(self, *args):
        mc.select('hardwareRenderGlobals', r=True)

    def selectMayaHardware2Node(self, *args):
        mc.select('hardwareRenderingGlobals', r=True)

    def selectRedshiftNode(self, *args):
        mc.select('redshiftOptions', r=True)

    def selectArnoldRendererNode(self, *args):
        mc.select('defaultArnoldRenderOptions', r=True)

    def selectMentalrayNode(self, *args):
        mc.select('miDefaultOptions', r=True)

    def displayOptions(self, *args):
        self.uiContent['mainFormLayout'] = mc.formLayout(nd=100)
        self.uiContent['mainFrameLayout'] = mc.frameLayout(labelVisible=0, collapse=0, collapsable=0, borderStyle='in')
        self.uiContent['mainColumnLayout'] = mc.columnLayout(adj=1)
        mc.rowLayout(numberOfColumns=3, adjustableColumn3=2)
        mc.text(label=_(' Dir: '))
        self.uiContent['presetsDirTF'] = mc.textField(text=self.presetsDir, changeCommand=self.presetsDirTFChangeCmd)
        mc.button(label=_('Set'), command=self.presetsDirSetCmd)
        mc.setParent('..')
        mc.rowLayout(numberOfColumns=2, adjustableColumn2=2)
        mc.textField(text='')
        self.uiContent['leftIntSlider'] = mc.intSlider(min=50, max=200, value=60, step=1, dragCommand=self.updateGridLayout)
        mc.setParent('..')
        mc.setParent(self.uiContent['mainFrameLayout'])
        mc.frameLayout(labelVisible=0, borderStyle='in')
        self.uiContent['mainPaneLayout'] = mc.paneLayout(configuration='vertical2', paneSize=[1, 25, 75], staticWidthPane=1, width=400)
        self.uiContent['leftTSLFormLayout'] = mc.formLayout(nd=100)
        self.uiContent['leftTSLTabLayout'] = mc.tabLayout(innerMarginWidth=5, innerMarginHeight=5, tabsVisible=0, childResizable=1)
        self.uiContent['leftPaneLayout'] = mc.paneLayout(configuration='horizontal2')
        self.uiContent['leftUpTSLFormLayout'] = mc.formLayout(nd=100)
        self.uiContent['leftUpTSLTabLayout'] = mc.tabLayout(innerMarginWidth=5, innerMarginHeight=5, tabsVisible=0, childResizable=1)
        mc.frameLayout(labelVisible=True, label=_('Favorites'), collapse=False, collapsable=False)
        self.uiContent['leftTextScrollList'] = mc.textScrollList(append=[ i for i in range(0, 20) ], doubleClickCommand=self.textScrollListDoubleClickCommand, selectCommand=self.updateTextAndGridLayout)
        mc.popupMenu()
        mc.menuItem(label=_('Add Folder'), command=self.addFolderCmd)
        mc.menuItem(label=_('Deselect'), command=self.deselectAllCmd)
        mc.menuItem(label=_('Delete'), command=self.deleteFolderCmd)
        mc.setParent(self.uiContent['leftPaneLayout'])
        self.uiContent['leftDownTSLFormLayout'] = mc.formLayout(nd=100)
        self.uiContent['leftDownTSLTabLayout'] = mc.tabLayout(innerMarginWidth=5, innerMarginHeight=5, tabsVisible=0, childResizable=1)
        mc.frameLayout(labelVisible=True, label=_('Node Types'), collapse=False, collapsable=False)
        self.uiContent['leftDownTextScrollList'] = mc.textScrollList(selectCommand=self.updateGridLayout)
        mc.popupMenu()
        mc.menuItem(label=_('New Node'), command=self.newNode)
        mc.menuItem(label=_('New Shading Node'), command=self.newShadingNode)
        mc.setParent(self.uiContent['mainPaneLayout'])
        self.uiContent['rightGridTabLayout'] = mc.tabLayout(scrollable=1, innerMarginWidth=5, innerMarginHeight=5, tabsVisible=0, childResizable=1)
        mc.popupMenu(parent=self.uiContent['rightGridTabLayout'])
        mc.menuItem(label=_('New..'), command=self.createRenderPresetCmd)
        mc.menuItem(label=_('Delete'), command=self.deletePresetFileCmd)
        mc.setParent(self.uiContent['rightGridTabLayout'])
        self.uiContent['rightGridLayout'] = mc.gridLayout(columnsResizable=1, width=200)
        self.updatePresetLayout()
        mc.formLayout(self.uiContent['leftUpTSLFormLayout'], edit=True, attachForm=([self.uiContent['leftUpTSLTabLayout'], 'top', 0],
         [self.uiContent['leftUpTSLTabLayout'], 'left', 2],
         [self.uiContent['leftUpTSLTabLayout'], 'right', 2],
         [self.uiContent['leftUpTSLTabLayout'], 'bottom', 0]))
        mc.formLayout(self.uiContent['leftDownTSLFormLayout'], edit=True, attachForm=([self.uiContent['leftDownTSLTabLayout'], 'top', 0],
         [self.uiContent['leftDownTSLTabLayout'], 'left', 2],
         [self.uiContent['leftDownTSLTabLayout'], 'right', 2],
         [self.uiContent['leftDownTSLTabLayout'], 'bottom', 0]))
        mc.formLayout(self.uiContent['leftTSLFormLayout'], edit=True, attachForm=([self.uiContent['leftTSLTabLayout'], 'top', 0],
         [self.uiContent['leftTSLTabLayout'], 'left', 2],
         [self.uiContent['leftTSLTabLayout'], 'right', 2],
         [self.uiContent['leftTSLTabLayout'], 'bottom', 0]))
        mc.formLayout(self.uiContent['mainFormLayout'], edit=True, attachForm=([self.uiContent['mainFrameLayout'], 'top', 0],
         [self.uiContent['mainFrameLayout'], 'left', 2],
         [self.uiContent['mainFrameLayout'], 'right', 2],
         [self.uiContent['mainFrameLayout'], 'bottom', 0]))
        mc.formLayout(self.uiContent['optionsForm'], e=True, attachForm=([self.uiContent['mainFormLayout'], 'top', 0],
         [self.uiContent['mainFormLayout'], 'left', 2],
         [self.uiContent['mainFormLayout'], 'right', 2],
         [self.uiContent['mainFormLayout'], 'bottom', 0]))
        self.autoRefreshJobCmd()
        mc.window(self.uiContent['window'], widthHeight=self.uiContent['size'], resizeToFitChildren=1, sizeable=1, edit=True)

    def updatePresetLayout(self, *args):
        self.updateTextScrollList()
        self.updateGridLayout()

    def updateTextAndGridLayout(self, *args):
        self.updateDownTextScrollList()
        if self.iniFile.getValue('auto_refresh') == 'Auto':
            self.autoSelectDownTextScrollText()
        self.updateGridLayout()

    def getDirList(self, url, *args):
        files = os.listdir(url)
        if len(files) > 0:
            for file in files:
                myfile = url + '/' + file
                if os.path.isdir(myfile):
                    subDirs = os.listdir(myfile)
                    state = False
                    if subDirs:
                        for subDir in subDirs:
                            if os.path.isdir(myfile + '/' + subDir):
                                state = True

                    if state:
                        appendItemText = str(self.SPACE) + '-' + '   ' + file
                    else:
                        appendItemText = str(self.SPACE) + '   ' + file
                    mc.textScrollList(self.uiContent['leftTextScrollList'], append=appendItemText, e=1)
                    self.SPACE = self.SPACE + '    '
                    self.getDirList(myfile)
                    self.SPACE = self.SPACE[:-4]

    def updateTextScrollList(self, *args):
        mc.textScrollList(self.uiContent['leftTextScrollList'], removeAll=1, e=1)
        self.list = []
        self.SPACE = ''
        self.getDirList(self.presetsDir)

    def getTextScrollListRelativePath(self, *args):
        letterPat = '[a-zA-Z0-9_]+'
        subPat = '[-]'
        if mc.textScrollList(self.uiContent['leftTextScrollList'], selectIndexedItem=1, q=1):
            selectIndexedItem = mc.textScrollList(self.uiContent['leftTextScrollList'], selectIndexedItem=1, q=1)[0]
            selectItemOld = mc.textScrollList(self.uiContent['leftTextScrollList'], selectItem=1, q=1)[0]
            selectItemLetterOld = re.findall(letterPat, selectItemOld)[0]
            plusSubSpaceLetterNumOld = len(selectItemOld) - len(selectItemLetterOld)
            topDirIndex = {}
            parentDirIndexList = []
            topIndex = 0
            for i in range(1, selectIndexedItem + 1):
                mc.textScrollList(self.uiContent['leftTextScrollList'], selectIndexedItem=i, e=1)
                tempSelectItem = mc.textScrollList(self.uiContent['leftTextScrollList'], selectItem=1, q=1)[0]
                if re.findall(subPat, tempSelectItem):
                    plusSubSpaceLetterNum = len(tempSelectItem) - len(re.findall(letterPat, tempSelectItem)[0])
                    if plusSubSpaceLetterNum < plusSubSpaceLetterNumOld:
                        topDirIndex[i] = plusSubSpaceLetterNum
                        parentDirIndexList.append(i)

            if topDirIndex:
                items = topDirIndex.items()
                items.sort()
                temp = [ {key: value} for key, value in items ]
                tempvalue = [ value for key, value in temp[0].items() ][0]
                topIndex = [ key for key, value in items if value == tempvalue ][-1]
            dirPath = ''
            parentDirIndexList = [ i for i in parentDirIndexList if topIndex <= i ]
            if topIndex:
                for i in parentDirIndexList:
                    mc.textScrollList(self.uiContent['leftTextScrollList'], selectIndexedItem=i, e=1)
                    tempSelectItem = mc.textScrollList(self.uiContent['leftTextScrollList'], selectItem=1, q=1)[0]
                    dirPath = dirPath + '/' + re.findall(letterPat, tempSelectItem)[0]

            dirPath = dirPath + '/' + selectItemLetterOld
            mc.textScrollList(self.uiContent['leftTextScrollList'], selectIndexedItem=selectIndexedItem, e=1)
            return dirPath
        else:
            return ''

    def textScrollListDoubleClickCommand(self, *args):
        letterPat = '[a-zA-Z0-9_]+'
        plusPat = '[+]'
        subPat = '[-]'
        selectIndexedItem = mc.textScrollList(self.uiContent['leftTextScrollList'], selectIndexedItem=1, q=1)[0]
        selectItemOld = mc.textScrollList(self.uiContent['leftTextScrollList'], selectItem=1, q=1)[0]
        numberOfItems = mc.textScrollList(self.uiContent['leftTextScrollList'], numberOfItems=1, q=1)
        plusState = re.findall(plusPat, selectItemOld)
        subState = re.findall(subPat, selectItemOld)
        selectItemLetterOld = re.findall(letterPat, selectItemOld)[0]
        plusSubSpaceLetterNumOld = len(selectItemOld) - len(selectItemLetterOld)
        dirPath = self.getTextScrollListRelativePath()
        if plusState:
            selectItemNew = selectItemOld.replace('+', '-')
            mc.textScrollList(self.uiContent['leftTextScrollList'], removeIndexedItem=selectIndexedItem, e=1)
            mc.textScrollList(self.uiContent['leftTextScrollList'], appendPosition=[selectIndexedItem, selectItemNew], selectIndexedItem=selectIndexedItem, e=1)
            if self.treeDic.has_key(dirPath):
                for i in range(0, len(self.treeDic[dirPath])):
                    mc.textScrollList(self.uiContent['leftTextScrollList'], appendPosition=[selectIndexedItem + i + 1, self.treeDic[dirPath][i]], e=1)

            mc.textScrollList(self.uiContent['leftTextScrollList'], selectIndexedItem=selectIndexedItem, e=1)
        if subState:
            selectItemNew = selectItemOld.replace('-', '+')
            mc.textScrollList(self.uiContent['leftTextScrollList'], removeIndexedItem=selectIndexedItem, e=1)
            mc.textScrollList(self.uiContent['leftTextScrollList'], appendPosition=[selectIndexedItem, selectItemNew], selectIndexedItem=selectIndexedItem, e=1)
            deleteNum = 0
            state = False
            for i in range(selectIndexedItem + 1, numberOfItems + 1):
                mc.textScrollList(self.uiContent['leftTextScrollList'], selectIndexedItem=i, e=1)
                tempSelectItem = mc.textScrollList(self.uiContent['leftTextScrollList'], selectItem=1, q=1)[0]
                plusSubSpaceLetterNum = len(tempSelectItem) - len(re.findall(letterPat, tempSelectItem)[0])
                if plusSubSpaceLetterNum > plusSubSpaceLetterNumOld:
                    deleteNum = deleteNum + 1
                    state = False
                else:
                    state = True
                if state:
                    break

            self.treeDic[dirPath] = []
            for i in range(0, deleteNum):
                mc.textScrollList(self.uiContent['leftTextScrollList'], selectIndexedItem=selectIndexedItem + 1, e=1)
                tempSelectItem = mc.textScrollList(self.uiContent['leftTextScrollList'], selectItem=1, q=1)[0]
                self.treeDic[dirPath].append(tempSelectItem)
                mc.textScrollList(self.uiContent['leftTextScrollList'], removeIndexedItem=selectIndexedItem + 1, e=1)

            mc.textScrollList(self.uiContent['leftTextScrollList'], selectIndexedItem=selectIndexedItem, e=1)

    def updateDownTextScrollList(self, *args):
        mc.textScrollList(self.uiContent['leftDownTextScrollList'], removeAll=1, e=1)
        dirPath = self.presetsDir + self.getTextScrollListRelativePath()
        xmlFiels = []
        nodeTypes = []
        if os.path.isdir(dirPath):
            files = os.listdir(dirPath)
            if files:
                for f in files:
                    if True in map(f.endswith, ['.connectMap']):
                        xmlFiels.append(dirPath + '/' + f)

        for f in xmlFiels:
            tree = ElementTree.parse(f)
            root = tree.getroot()
            nodeType = root.get('rootNodeType')
            if nodeType not in nodeTypes:
                mc.textScrollList(self.uiContent['leftDownTextScrollList'], append=nodeType, e=1)
                nodeTypes.append(nodeType)

        mc.textScrollList(self.uiContent['leftDownTextScrollList'], deselectAll=True, e=True)

    def updateGridLayout(self, *args):
        libraryItems = mc.gridLayout(self.uiContent['rightGridLayout'], ca=1, q=1)
        if libraryItems:
            if len(libraryItems):
                mc.deleteUI(libraryItems)
        dirPath = self.presetsDir + self.getTextScrollListRelativePath()
        xmlFiels = []
        btnState = False
        if os.path.isdir(dirPath):
            files = os.listdir(dirPath)
            if files:
                for f in files:
                    if True in map(f.endswith, ['.connectMap']):
                        fPath = dirPath + '/' + f
                        tree = ElementTree.parse(fPath)
                        root = tree.getroot()
                        nodeType = root.get('rootNodeType')
                        selectNodeType = mc.textScrollList(self.uiContent['leftDownTextScrollList'], selectItem=True, q=True)
                        if selectNodeType:
                            if nodeType == selectNodeType[0]:
                                xmlFiels.append(dirPath + '/' + f)
                                btnState = True
                        else:
                            xmlFiels.append(dirPath + '/' + f)
                            btnState = False

        if xmlFiels:
            intSliderValue = mc.intSlider(self.uiContent['leftIntSlider'], value=1, q=1)
            gridLayoutWidth = mc.gridLayout(self.uiContent['rightGridLayout'], width=1, q=1)
            numberOfColumns = gridLayoutWidth / intSliderValue
            cellWidthHeight = gridLayoutWidth / numberOfColumns
            for xmlFile in xmlFiels:
                mc.setParent(self.uiContent['rightGridLayout'])
                picPath = xmlFile.replace('.connectMap', '.png')
                mc.frameLayout(labelVisible=0, collapse=0, collapsable=0, borderStyle='out')
                if os.path.exists(picPath):
                    btn = mc.symbolButton(image=picPath, enable=btnState, width=cellWidthHeight - 5, height=cellWidthHeight - 5)
                else:
                    btn = mc.symbolButton(image='defaultCustomLayout.png', enable=btnState, width=cellWidthHeight, height=cellWidthHeight)
                if self.presetMode == 'overwrite':
                    mc.symbolButton(btn, command=partial(self.presetBtnClickCmd, xmlFile, 1), edit=True)
                elif self.presetMode == 'modify':
                    mc.symbolButton(btn, command=partial(self.presetBtnBlendCmd, xmlFile, 1), edit=True)
                itcb1 = mc.iconTextCheckBox(style='textOnly', height=cellWidthHeight / 5.0, label=os.path.basename(xmlFile).split('.')[0], align='center', backgroundColor=[82 / 255.0, 82 / 255.0, 82 / 255.0], enableBackground=1)
                mc.iconTextCheckBox(itcb1, edit=1, onCommand=partial(self.iconTextCheckBoxOnCmd, itcb1), offCommand=partial(self.iconTextCheckBoxOffCmd, itcb1))
                mc.popupMenu(parent=btn, markingMenu=True)
                mc.menuItem(label=_('Assign Material To Selection'), radialPosition='N', command=partial(self.assignPresetToSelection, xmlFile, 1))
                mc.menuItem(label=_('Rename'), command=partial(self.renameCurrentPresetCmd, itcb1, xmlFile))
                mc.menuItem(label=_('Update..'), command=partial(self.updateCurrentPresetCmd, btn, itcb1, xmlFile))
                mc.menuItem(label=_('Screen Shot'), command=partial(self.presetBtnScreenShotCmd, btn, picPath))
                mc.menuItem(label=_('View Picture'), command=partial(self.viewSamplePictureCmd, picPath))
                mc.menuItem(divider=True)
                mc.menuItem(label=_('Blend') + ' %90', command=partial(self.presetBtnBlendCmd, xmlFile, 0.9))
                mc.menuItem(label=_('Blend') + ' %75', command=partial(self.presetBtnBlendCmd, xmlFile, 0.75))
                mc.menuItem(label=_('Blend') + ' %50', command=partial(self.presetBtnBlendCmd, xmlFile, 0.5))
                mc.menuItem(label=_('Blend') + ' %25', command=partial(self.presetBtnBlendCmd, xmlFile, 0.25))
                mc.menuItem(label=_('Blend') + ' %10', command=partial(self.presetBtnBlendCmd, xmlFile, 0.1))

            mc.gridLayout(self.uiContent['rightGridLayout'], edit=1, cellWidthHeight=[cellWidthHeight, cellWidthHeight + 12], numberOfColumns=numberOfColumns, position=['left', 50])

    def autoRefreshJobCmd(self, *args):
        if not mc.menuItem(self.uiContent['autoRefreshMenu'], checkBox=True, q=True):
            try:
                mc.scriptJob(kill=self.autoRefreshJob, force=True)
            except:
                pass

            mc.setToolTo('selectSuperContext')
            self.iniFile.setValue('auto_refresh', 'Manual')
        else:
            self.autoRefreshJob = mc.scriptJob(p=self.uiContent['autoRefreshMenu'], e=['SelectionChanged', self.autoSelectDownTextScrollText])
            self.autoSelectDownTextScrollText()
            self.iniFile.setValue('auto_refresh', 'Auto')

    def presetModeOverwriteCmd(self, *args):
        self.iniFile.setValue('preset_mode', 'overwrite')
        self.presetMode = self.iniFile.getValue('preset_mode')
        self.presetModeCmd()
        self.updateGridLayout()

    def presetModeModifyCmd(self, *args):
        self.iniFile.setValue('preset_mode', 'modify')
        self.presetMode = self.iniFile.getValue('preset_mode')
        self.presetModeCmd()
        self.updateGridLayout()

    def presetModeCmd(self, *args):
        if self.presetMode == 'overwrite':
            mc.menuItem(self.uiContent['overwriteMenuItem'], radioButton=True, edit=True)
            mc.menuItem(self.uiContent['modifyMenuItem'], radioButton=False, edit=True)
        if self.presetMode == 'modify':
            mc.menuItem(self.uiContent['overwriteMenuItem'], radioButton=False, edit=True)
            mc.menuItem(self.uiContent['modifyMenuItem'], radioButton=True, edit=True)

    def autoSelectDownTextScrollText(self, *args):
        sels = mc.ls(sl=True)
        if sels:
            nType = mc.objectType(sels[0])
            allItems = mc.textScrollList(self.uiContent['leftDownTextScrollList'], allItems=True, q=True)
            state = True
            for index in range(1, len(sels)):
                if mc.objectType(sels[index]) != nType:
                    state = False
                    break

            if allItems:
                if nType in allItems:
                    if state:
                        mc.textScrollList(self.uiContent['leftDownTextScrollList'], selectItem=nType, e=True)
                    else:
                        mc.textScrollList(self.uiContent['leftDownTextScrollList'], deselectAll=True, e=True)
                else:
                    mc.textScrollList(self.uiContent['leftDownTextScrollList'], deselectAll=True, e=True)
        else:
            mc.textScrollList(self.uiContent['leftDownTextScrollList'], deselectAll=True, e=True)
        self.updateGridLayout()

    def iconTextCheckBoxOnCmd(self, object, *args):
        mc.iconTextCheckBox(object, edit=1, backgroundColor=[104 / 255.0, 140 / 255.0, 182 / 255.0], enableBackground=1)

    def iconTextCheckBoxOffCmd(self, object, *args):
        mc.iconTextCheckBox(object, edit=1, backgroundColor=[82 / 255.0, 82 / 255.0, 82 / 255.0], enableBackground=1)

    def initPresetFilePath(self):
        filePath = 'Z:/Resource/Library/Public/Final/Library/' + 'Preset/Material/'
        if not os.path.exists(filePath):
            os.makedirs(filePath)
        return filePath

    def presetsDirSetCmd(self, *args):
        presetsDirTFText = mc.textField(self.uiContent['presetsDirTF'], text=True, query=True)
        tempBrowse = mc.fileDialog2(fm=2, cap=_('Setting Presets Dir'), dir=presetsDirTFText, okCaption=_('Set'))
        if tempBrowse:
            self.presetsDir = tempBrowse[0]
            mc.textField(self.uiContent['presetsDirTF'], edit=True, text=tempBrowse[0])
            self.iniFile.setValue('presets_dir', '%s' % self.presetsDir)
            self.updatePresetLayout()

    def presetsDirTFChangeCmd(self, *args):
        presetsDirTFText = mc.textField(self.uiContent['presetsDirTF'], text=True, query=True)
        if os.path.exists(presetsDirTFText):
            self.presetsDir = presetsDirTFText
            self.iniFile.setValue('presets_dir', '%s' % self.presetsDir)
            self.updatePresetLayout()
        else:
            mc.textField(self.uiContent['presetsDirTF'], text=self.presetsDir, edit=True)

    def textScrollListPopupMenuCmd(self, parent, *args):
        mc.popupMenu(parent=parent)
        mc.menuItem(label=_('Add Folder'), command=self.addFolderCmd)
        mc.menuItem(label=_('Deselect'), command=self.deselectAllCmd)
        mc.menuItem(label=_('Delete'), command=self.deleteFolderCmd)

    def newNode(self, *args):
        selectItems = mc.textScrollList(self.uiContent['leftDownTextScrollList'], selectItem=1, q=1)
        if selectItems:
            nodeType = selectItems[0]
            mc.createNode(nodeType)
        else:
            om.MGlobal.displayWarning('Please select item!')

    def newShadingNode(self, *args):
        selectItems = mc.textScrollList(self.uiContent['leftDownTextScrollList'], selectItem=1, q=1)
        if selectItems:
            newShader = selectItems[0]
            newShaderNode = mc.shadingNode(newShader, asShader=True)
            newSGNode = mc.sets(name=newShaderNode + 'SG', renderable=1, noSurfaceShader=1, empty=1)
            mayaArnoldRedshiftShaders = ['useBackground',
             'layeredShader',
             'hairTubeShader',
             'shadingMap',
             'anisotropic',
             'blinn',
             'lambert',
             'phong',
             'phongE',
             'rampShader',
             'surfaceShader',
             'aiAmbientOcclusion',
             'aiHair',
             'aiRaySwitch',
             'aiShadowCatcher',
             'aiSkin',
             'aiStandard',
             'aiUtility',
             'aiWireframe',
             'RedshiftArchitectural',
             'RedshiftCarPaint',
             'RedshiftSubSurfaceScatter',
             'RedshiftSprite',
             'RedshiftMatteShadowCatcher',
             'RedshiftMaterialBlender',
             'RedshiftIncandescent',
             'RedshiftHair']
            if newShader in mayaArnoldRedshiftShaders:
                try:
                    mc.connectAttr(newShaderNode + '.outColor', newSGNode + '.surfaceShader', f=True)
                except:
                    pass

            mayaShaders = ['oceanShader']
            if newShader in mayaShaders:
                try:
                    mc.connectAttr(newShaderNode + '.outColor', newSGNode + '.surfaceShader', f=True)
                    mc.connectAttr(newShaderNode + '.displacement', newSGNode + '.displacementShader', f=True)
                except:
                    pass

            mentalRayShaders = ['builtin_bsdf_architectural',
             'builtin_bsdf_architectural_comp',
             'builtin_bsdf_ashikhmin',
             'builtin_bsdf_carpaint',
             'builtin_bsdf_lambert',
             'builtin_bsdf_mirror',
             'builtin_bsdf_phong',
             'mi_metallic_paint',
             'mib_illum_ward',
             'mib_glossy_refraction',
             'mib_illum_ward_deriv',
             'misss_skin_specular',
             'misss_fast_shader2',
             'mib_illum_phong',
             'misss_call_shader',
             'mi_car_paint_phen',
             'mib_illum_hair',
             'mib_illum_lambert',
             'path_material',
             'mib_illum_cooktorr',
             'mib_illum_blinn',
             'misss_fast_simple_maya',
             'misss_fast_shadermib_glossy_reflection',
             'misss_set_normal',
             'misss_mia_skin2_surface_phen']
            if newShader in mentalRayShaders:
                try:
                    mc.connectAttr(newShaderNode + '.outValue', newSGNode + '.miMaterialShader', f=True)
                except:
                    pass

            mentalRayShadersA = ['mi_metallic_paint_x_passes',
             'misss_fast_shader2_x',
             'mi_metallic_paint_x',
             'mi_car_paint_phen_x_passes',
             'mi_car_paint_phen_x',
             'misss_fast_shader2_x',
             'misss_fast_shader_xmisss_fast_shader_x_passes',
             'misss_fast_shader_x',
             'misss_fast_shader_x']
            if newShader in mentalRayShadersA:
                try:
                    mc.connectAttr(newShaderNode + '.message', newSGNode + '.miMaterialShader', f=True)
                except:
                    pass

            mentalRayShadersB = ['mia_material', 'mia_material_x', 'mia_material_x_passes']
            if newShader in mentalRayShadersB:
                try:
                    mc.connectAttr(newShaderNode + '.message', newSGNode + '.miShadowShader', f=True)
                    mc.connectAttr(newShaderNode + '.message', newSGNode + '.miPhotonShader', f=True)
                    mc.connectAttr(newShaderNode + '.message', newSGNode + '.miMaterialShader', f=True)
                except:
                    pass

            mentalRayShadersC = ['dgs_material',
             'dielectric_material',
             'misss_physical',
             'transmat']
            if newShader in mentalRayShadersC:
                try:
                    mc.connectAttr(newShaderNode + '.outValue', newSGNode + '.miMaterialShader', f=True)
                    mc.connectAttr(newShaderNode + '.outValue', newSGNode + '.miPhotonShader', f=True)
                except:
                    pass

            return newShaderNode
        om.MGlobal.displayWarning('Please select item!')

    def presetBtnClickCmd(self, presetFilePath, blend, *args):
        sels = mc.ls(sl=True)
        if sels:
            presetDirPath = os.path.dirname(presetFilePath)
            presetName = os.path.basename(presetFilePath).split('.')[0]
            for node in sels:
                applyConnectMapToNode(node=node, presetDirPath=presetDirPath, presetName=presetName, blend=blend)

        try:
            mc.select(sels)
        except:
            pass

    def presetBtnBlendCmd(self, presetFilePath, blend, *args):
        sels = mc.ls(sl=True)
        selectItems = mc.textScrollList(self.uiContent['leftDownTextScrollList'], selectItem=1, q=1)
        if sels:
            if selectItems:
                presetNodeType = selectItems[0]
                selectNodeType = mc.nodeType(sels[0])
                if presetNodeType == selectNodeType:
                    if os.path.exists(presetFilePath):
                        tree = ElementTree.parse(presetFilePath)
                        root = tree.getroot()
                        rootNodeName = root.get('rootNodeName')
                        presetName = root.get('presetName')
                        presetDirPath = os.path.dirname(presetFilePath)
                        nodePresetFilePath = presetDirPath + '/' + presetName + '_' + rootNodeName + '.xml'
                        if os.path.exists(nodePresetFilePath):
                            for node in sels:
                                applyPresetToNode(createNodeProc='', deleteNodeProc='', presetName=nodePresetFilePath, blend=blend)

                else:
                    om.MGlobal.displayWarning('Please select the "%s" type node' % selectItems[0])
        try:
            mc.select(sels)
        except:
            pass

    def assignPresetToSelection(self, presetFilePath, blend, *args):
        sels = mc.ls(selection=True)
        if sels:
            shaderNode = self.newShadingNode()
            if shaderNode:
                presetDirPath = os.path.dirname(presetFilePath)
                presetName = os.path.basename(presetFilePath).split('.')[0]
                applyConnectMapToNode(node=shaderNode, presetDirPath=presetDirPath, presetName=presetName, blend=blend)
                mc.select(sels, r=True)
                mel.eval('hyperShade -assign %s;' % shaderNode)

    def buildFileList(self, dir, *args):
        if os.path.isdir(dir):
            subDirs = os.listdir(dir)
            if subDirs:
                for subDir in subDirs:
                    if os.path.isdir(dir + '/' + subDir):
                        if os.listdir(dir + '/' + subDir):
                            self.buildFileList(dir=dir + '/' + subDir)
                    if os.path.isfile(dir + '/' + subDir):
                        if os.path.splitext(dir + '/' + subDir)[1] == '.xml':
                            self.fileDic.append(dir + '/' + subDir)

    def renameCurrentPresetCmd(self, button, presetFilePath, *args):
        dirPath = self.presetsDir + self.getTextScrollListRelativePath()
        iconTextCheckBoxLabel = mc.iconTextCheckBox(button, label=1, q=1)
        result = mc.promptDialog(title=_('Rename Preset'), message=_('Enter Name:'), text=iconTextCheckBoxLabel, button=[_('OK'), _('Cancel')], defaultButton=_('OK'), cancelButton=_('Cancel'), dismissString=_('Cancel'))
        if result == _('OK'):
            newName = mc.promptDialog(query=True, text=True)
            mc.iconTextCheckBox(button, label=newName, e=1)
            for f in os.listdir(dirPath):
                oldNameLen = len(iconTextCheckBoxLabel)
                newXmlName = newName + f[oldNameLen:]
                if f[:oldNameLen] == iconTextCheckBoxLabel:
                    os.rename(dirPath + '/' + f, dirPath + '/' + newXmlName)

    def updateCurrentPresetCmd(self, btn, itcb, presetFilePath, *args):
        itcbLabel = mc.iconTextCheckBox(itcb, label=True, query=True)
        selectItems = mc.textScrollList(self.uiContent['leftDownTextScrollList'], selectItem=1, q=1)
        sels = mc.ls(sl=True)
        if sels and selectItems:
            if mc.nodeType(sels[0]) == selectItems[0]:
                dirName = os.path.dirname(presetFilePath)
                for f in os.listdir(dirName):
                    if f[:len(itcbLabel)] == itcbLabel:
                        os.remove(dirName + '/' + f)

                node = sels[0]
                saveConnectMapPreset(node=node, ppath=dirName, presetName=itcbLabel, autoRename=None, mode='modify')
                mc.symbolButton(btn, image='defaultCustomLayout.png', edit=True)
            else:
                om.MGlobal.displayWarning('Please select the "%s" type node' % selectItems[0])

    def addFolderCmd(self, *args):
        if mc.textScrollList(self.uiContent['leftTextScrollList'], selectIndexedItem=1, q=1):
            presetFilePath = self.presetsDir + self.getTextScrollListRelativePath()
        else:
            presetFilePath = self.presetsDir
        result = mc.promptDialog(title=_('Add Folder'), message=_('Enter Name:'), button=[_('OK'), _('Cancel')], defaultButton=_('OK'), cancelButton=_('Cancel'), dismissString=_('Cancel'))
        if result == _('OK'):
            folderName = mc.promptDialog(query=True, text=True)
            folderPath = presetFilePath + '/' + folderName
            try:
                os.makedirs(folderPath)
            except:
                om.MGlobal.displayWarning('The "%s" has been created!')

            self.updateTextScrollList()

    def deselectAllCmd(self, *args):
        mc.textScrollList(self.uiContent['leftTextScrollList'], deselectAll=1, e=1)
        self.updateGridLayout()

    def deleteFolderCmd(self, *args):
        dirPath = self.presetsDir + self.getTextScrollListRelativePath()
        if os.path.exists(dirPath):
            state = False
            if os.listdir(dirPath):
                result = mc.confirmDialog(title=_('Confirm'), message=_('Are you sure?'), button=[_('Yes'), _('No')], defaultButton=_('Yes'), cancelButton=_('No'), dismissString=_('No'))
                if result == _('Yes'):
                    state = True
            else:
                state = True
            if state:
                try:
                    shutil.rmtree(dirPath)
                    om.MGlobal.displayInfo('The "%s" have been deleted!' % dirPath)
                    self.updatePresetLayout()
                except:
                    mc.confirmDialog(title=_('Error'), message='Access is denied: "%s"!\nPlease contact administrator!' % dirPath)

    def createRenderPresetCmd(self, *args):
        presetFilePath = ''
        selectIndexedItem = mc.textScrollList(self.uiContent['leftTextScrollList'], selectIndexedItem=1, q=1)
        if selectIndexedItem:
            if selectIndexedItem:
                presetFilePath = self.presetsDir + self.getTextScrollListRelativePath()
            else:
                presetFilePath = self.presetsDir
            result = mc.promptDialog(title=_('Create Preset'), message=_('Enter Name:'), text='temp', button=[_('OK'), _('Cancel')], defaultButton=_('OK'), cancelButton=_('Cancel'), dismissString=_('Cancel'))
            if result == _('OK'):
                presetName = mc.promptDialog(query=True, text=True)
                if presetName:
                    sels = mc.ls(sl=True)
                    if sels:
                        node = sels[0]
                        stateAndName = saveConnectMapPreset(node=node, ppath=presetFilePath, presetName=presetName, autoRename=None, mode=None)
                        if stateAndName[0]:
                            self.updateTextAndGridLayout()
                else:
                    self.createRenderPresetCmd()
        else:
            result = mc.confirmDialog(title=_('Warning:'), message=_('Please Add Folder!'), button=[_('Yes'), _('No')], defaultButton=_('Yes'), cancelButton=_('No'), dismissString=_('No'))
            if result == _('Yes'):
                self.addFolderCmd()

    def viewSamplePictureCmd(self, presetPicPath, *args):
        if os.path.exists(presetPicPath):
            webbrowser.open(presetPicPath)

    def presetBtnScreenShotCmd(self, button, presetPicPath, *args):
        self.shotPixmap(filePath=presetPicPath, button=button)

    def deletePresetFileCmd(self, *args):
        dirPath = self.presetsDir + self.getTextScrollListRelativePath()
        libraryItems = mc.gridLayout(self.uiContent['rightGridLayout'], ca=1, q=1)
        if libraryItems:
            for i in libraryItems:
                iconTextCheckBox = mc.frameLayout(i, childArray=1, q=1)[1]
                if mc.iconTextCheckBox(iconTextCheckBox, value=1, q=1):
                    iconTextCheckBoxLabel = mc.iconTextCheckBox(iconTextCheckBox, label=1, q=1)
                    for f in os.listdir(dirPath):
                        fBuf = f.split('.')
                        ppath = dirPath + '/' + f
                        delState = False
                        if len(fBuf) == 2:
                            if fBuf[1] == 'connectMap' or fBuf[1] == 'xml':
                                tree = ElementTree.parse(ppath)
                                root = tree.getroot()
                                presetName = root.get('presetName')
                                if presetName == iconTextCheckBoxLabel:
                                    delState = True
                            elif fBuf[1] == 'png':
                                if fBuf[0] == iconTextCheckBoxLabel:
                                    delState = True
                            if delState:
                                os.remove(ppath)

            self.updateTextAndGridLayout()

    def shotPixmap(self, button, filePath, *args):
        widget = fullScreenLabel(parent=getMayaWindow(), button=button, parentClass=self, picPath=filePath)
        widget.setMouseTracking(True)
        widget.show()


class fullScreenLabel(QtGui.QLabel):

    def __init__(self, parent = None, button = None, parentClass = None, picPath = None, *args):
        QtGui.QLabel.__init__(self, parent)
        print parent, button, parentClass, picPath
        self.setWindowFlags(QtCore.Qt.Tool)
        self.fullScreenPixMap = QtGui.QPixmap.grabWindow(QtGui.QApplication.desktop().winId())
        self.resize(self.fullScreenPixMap.width(), self.fullScreenPixMap.height())
        self.setPixmap(self.fullScreenPixMap)
        self.showFullScreen()
        self.x1 = -1
        self.y1 = -1
        self.setCursor(QtCore.Qt.CrossCursor)
        self.startPoint = QtCore.QPoint()
        self.endPoint = QtCore.QPoint()
        self.picPath = picPath
        self.button = button
        self.parentClass = parentClass
        self.rubberBand = QtGui.QRubberBand(QtGui.QRubberBand.Rectangle, self)

    def mousePressEvent(self, event):
        self.startPoint = event.pos()
        if not self.rubberBand:
            self.rubberBand = QtGui.QRubberBand(QtGui.QRubberBand.Rectangle, self)
        self.rubberBand.setGeometry(QtCore.QRect(self.startPoint, QtCore.QSize()))
        self.rubberBand.show()
        self.update

    def mouseMoveEvent(self, event):
        self.x1 = event.x()
        self.y1 = event.y()
        self.rubberBand.setGeometry(QtCore.QRect(self.startPoint, event.pos()).normalized())
        self.update()

    def mouseReleaseEvent(self, event):
        self.endPoint = event.pos()
        x = self.startPoint.x() + 1
        y = self.startPoint.y() + 1
        w = self.endPoint.x() - x
        h = self.endPoint.y() - y
        tempixmap = QtGui.QPixmap.grabWidget(self, x, y, w, h)
        tempixmap.save(self.picPath, 'PNG')
        self.rubberBand.hide()
        self.hide()
        self.update()
        self.parentClass.updateGridLayout()


def main():
    win.showUI()


if __name__ == '__main__':
    main()
