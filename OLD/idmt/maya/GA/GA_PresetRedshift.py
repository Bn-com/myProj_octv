# -*- coding: utf-8 -*-

'''
Created on 2017-8-8

@author:韩虹

改自CG365
'''

import maya.cmds as mc
import maya.mel as mel
import maya.OpenMayaUI as omui
import maya.OpenMaya as om
import os, sys, inspect, re, webbrowser, glob, ConfigParser, string, gettext, subprocess, shutil
from functools import partial
from xml.etree import ElementTree
from xml.dom import minidom
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
from idmt.maya.GA import GA_template as tp
from idmt.maya.GA import GA_redshiftProxyMeshSetting as jn_rpms
version = mc.about(version=True)
try:
    import sip
    from PyQt4 import QtCore, QtGui
except:
    from shiboken import wrapInstance
    from PySide import QtCore, QtGui

configFilePath = 'Z:/Resource/Library/Public/Final/Library/Preset'
mayaNodeNames = ['defaultRenderUtilityList1',
 'defaultLightSet',
 'defaultTextureList1',
 'defaultObjectSet',
 'defaultShaderList1',
 'defaultLayer',
 'defaultRenderLayer',
 'defaultViewColorManager',
 'materialInfo1',
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
    mayaNodeTypes.append(mc.objectType(tpt=nodeTag))

mayaNodeTypes.sort()
mayaNodeNames.sort()

def currentFileDirectory():
    path = os.path.realpath(sys.path[0])
    if os.path.isfile(path):
        path = os.path.dirname(path)
        return os.path.abspath(path)
    else:
        caller_file = inspect.stack()[1][1]
        return os.path.abspath(os.path.dirname(caller_file))


def setCurrentRenderer(renderer):
    if mel.eval('assertIsValidRenderer("%s")' % renderer):
        mc.setAttr('defaultRenderGlobals.currentRenderer', renderer, type='string')
        return 1
    return 0


def getMayaWindow():
    ptr = omui.MQtUtil.mainWindow()
    try:
        return wrapInstance(long(ptr), QtGui.QWidget)
    except:
        return sip.wrapinstance(long(ptr), QtCore.QObject)


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
    return reparsed.toprettyxml(indent=' ')


def createAttrPreset(nodeName):
    if not mc.objExists(nodeName):
        return ''
    nType = mc.nodeType(nodeName)
    attrPreset = Element('attrPreset')
    attrPreset.set('type', nType)
    listAttrString = 'listAttr -read -write -visible -hasData'
    atrs = getAttrsToPublish(nodeName=nodeName, listAttrString=listAttrString)
    if atrs:
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
    if atrs:
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
    psetCommand = createAttrPreset(node)
    outPath = ppath + '/' + presetName + '.' + postName
    xFile = open(outPath, 'w')
    xFile.write(psetCommand)
    xFile.close()


def applyPresetToNode(node, presetFilePath, blend, *args):
    if node:
        nType = mc.nodeType(node)
        if os.path.exists(presetFilePath):
            tree = ElementTree.parse(presetFilePath)
            root = tree.getroot()
            attributes = root.getchildren()
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


def createAOVPreset(dirPath, presetName):
    activeAovs = mc.ls(type='RedshiftAOV')
    attrPreset = Element('attrPreset')
    attrPreset.set('type', 'RedshiftAOV')
    for aov in activeAovs:
        saveAttrPreset(node=aov, ppath=dirPath, presetName=presetName + '_' + aov, postName='xml', autoRename=None)
        buf = aov.split('_')
        bufSize = len(buf)
        aovType = mc.getAttr(aov + '.aovType')
        attribute = SubElement(attrPreset, 'attribute')
        attribute.set('name', aov)
        attribute.set('value', aovType)

    psetCommand = prettify(attrPreset)
    outPath = dirPath + '/' + presetName + '.aov'
    xFile = open(outPath, 'w')
    xFile.write(psetCommand)
    xFile.close()


def applyAOVPresetToSetting(presetFilePath, *args):
    selectObject = mc.ls(selection=True)
    [ mc.delete(aov) for aov in mc.ls(type='RedshiftAOV') ]
    if os.path.exists(presetFilePath):
        tree = ElementTree.parse(presetFilePath)
        root = tree.getroot()
        attributes = root.getchildren()
        mel.eval('redshiftUpdateActiveAovList();')
        for atr in attributes:
            nodeName = atr.get('name')
            nodeType = atr.get('value')
            mel.eval('redshiftCreateAov("%s");' % nodeType)
            aovNodePresetFilePath = os.path.dirname(presetFilePath) + '/' + os.path.basename(presetFilePath).split('.')[0] + '_' + nodeName + '.xml'
            if os.path.exists(aovNodePresetFilePath):
                applyPresetToNode(node=nodeName, presetFilePath=aovNodePresetFilePath, blend=1)

        mel.eval('redshiftUpdateActiveAovList();')
    mc.select(cl=True)
    if selectObject:
        for obj in selectObject:
            if mc.objExists(obj):
                mc.select(obj, add=True)


def createNodeList(node, nodelist, *args):
    nodes = mc.listConnections(node, connections=False, plugs=False, shapes=True, source=True, destination=True, skipConversionNodes=False)
    if nodes:
        for node in nodes:
            if node not in nodelist:
                if mc.nodeType(node) not in mayaNodeTypes:
                    if mc.nodeType(node) not in customNodeTypes:
                        if node not in mayaNodeNames:
                            nodelist.append(node)
                            createNodeList(node=node, nodelist=nodelist)


def createConnectMapPreset(node, ppath, presetName, autoRename):
    nodeList = []
    connectInfos = {}
    createNodeList(node=node, nodelist=nodeList)
    if not nodeList:
        nodeList.append(node)
    connectMapElement = Element('connectMap')
    nodesElement = SubElement(connectMapElement, 'nodes')
    connectionsElement = SubElement(connectMapElement, 'connections')
    for newNode in nodeList:
        saveAttrPreset(node=newNode, ppath=ppath, presetName=presetName + '_' + newNode, postName='xml', autoRename=None)
        nodeElement = SubElement(nodesElement, 'node')
        nodeElement.set('name', newNode)
        nodeElement.set('type', mc.nodeType(newNode))
        sourceAttrs = mc.listConnections(newNode, connections=True, plugs=True, source=True, destination=False, skipConversionNodes=True)
        if sourceAttrs:
            for i in range(0, len(sourceAttrs)):
                if i % 2:
                    connectElement = SubElement(connectionsElement, 'connect')
                    connectElement.set('fromNode', sourceAttrs[i].split('.')[0])
                    connectElement.set('fromAttr', sourceAttrs[i].split('.')[1])
                    connectElement.set('toNode', sourceAttrs[i - 1].split('.')[0])
                    connectElement.set('toAttr', sourceAttrs[i - 1].split('.')[1])

        destinationAttrs = mc.listConnections(node, connections=True, plugs=True, source=False, destination=True, skipConversionNodes=True)
        if destinationAttrs:
            for i in range(0, len(destinationAttrs)):
                if i % 2:
                    connectElement = SubElement(connectionsElement, 'connect')
                    connectElement.set('fromNode', destinationAttrs[i - 1].split('.')[0])
                    connectElement.set('fromAttr', destinationAttrs[i - 1].split('.')[1])
                    connectElement.set('toNode', destinationAttrs[i].split('.')[0])
                    connectElement.set('toAttr', destinationAttrs[i].split('.')[1])

    return prettify(connectMapElement)


def saveConnectMapPreset(node, ppath, presetName, postName = 'connectMap', autoRename = None, mode = None, *args):
    if mc.about(evalVersion=True):
        om.MGlobal.displayWarning('saveAttrPreset is not supported in Maya PLE.')
        return ''
    if not mc.objExists(node):
        return ''
    psetCommand = createConnectMapPreset(node=node, ppath=ppath, presetName=presetName, autoRename=autoRename)
    ntype = mc.nodeType(node)
    outPath = ppath + '/' + presetName + '.' + postName
    oldPath = outPath
    i = 0
    state = True
    if mode != 'modify':
        if os.path.exists(outPath):
            doReplace = _('Auto Rename')
            yes = _('Yes')
            no = _('No')
            if not autoRename:
                result = mc.confirmDialog(title=_('Confirm'), message=_('File already exists. Overwrite?'), button=[yes, no, doReplace], defaultButton=doReplace)
            if result == no:
                return (False,
                 '%s%s' % (presetName, ''),
                 outPath,
                 ntype)
            if result == doReplace:
                overwrite = 1
                presetName = presetName.replace('[0-9]', '')
                presetName = presetName.replace('[0-9]', '')
                for i in range(1, 100):
                    outPath = ppath + '/' + presetName + str(i) + '.' + postName
                    if not os.path.exists(outPath):
                        overwrite = 0
                        break

                if overwrite:
                    om.MGlobal.displayWarning('Overwriting existing preset %s' % presetName)
                else:
                    om.MGlobal.displayInfo('Renaming preset to %s%s' % (presetName, i))
            if result == yes:
                i = ''
                state = True
        else:
            i = ''
    else:
        om.MGlobal.displayInfo('Modifed the current preset %s' % presetName)
    xFile = open(outPath, 'w')
    xFile.write(psetCommand)
    xFile.close()
    return (state,
     '%s%s' % (presetName, i),
     outPath,
     ntype)


def applyConnectMapToNode(node, presetFilePath, blend, *args):
    if node:
        nodeList = []
        selectObject = mc.ls(selection=True)
        createNodeList(node=node, nodelist=nodeList)
        for delNode in nodeList:
            if delNode != node:
                if mc.objExists(delNode):
                    if delNode in ('lightList1',):
                        continue
                    else:
                        mc.delete(delNode)

        if os.path.exists(presetFilePath):
            tree = ElementTree.parse(presetFilePath)
            root = tree.getroot()
            for newNode in root.getiterator('node'):
                nodeName = newNode.get('name')
                nodeType = newNode.get('type')
                if nodeName != node:
                    if nodeType[:8] == 'Redshift':
                        if nodeType == 'RedshiftPhysicalSun':
                            continue
                        else:
                            mc.shadingNode(nodeType, name=nodeName, asUtility=True)
                    else:
                        mc.createNode(nodeType, name=nodeName)
                    if nodeType == 'RedshiftPhysicalSky':
                        mc.addAttr(nodeName, shortName='rsSkyExposure', longName='rsSkyExposure', hidden=True, at='message')

            for newNode in root.getiterator('node'):
                nodeName = newNode.get('name')
                nodeType = newNode.get('type')
                if nodeType == 'RedshiftPhysicalSun':
                    if mc.objExists('sunDirection'):
                        mc.shadingNode(nodeType, name=nodeName, parent='sunDirection', asLight=True)

            for newNode in root.getiterator('node'):
                nodeName = newNode.get('name')
                nodePresetFilePath = presetFilePath.split('.')[0] + '_' + nodeName + '.xml'
                if os.path.exists(nodePresetFilePath):
                    applyPresetToNode(node=nodeName, presetFilePath=nodePresetFilePath, blend=1)

            for connectInfo in root.getiterator('connect'):
                fromNodeAndAttr = connectInfo.get('fromNode') + '.' + connectInfo.get('fromAttr')
                toNodeAndAttr = connectInfo.get('toNode') + '.' + connectInfo.get('toAttr')
                if mc.attributeQuery(connectInfo.get('fromAttr'), node=connectInfo.get('fromNode'), exists=True):
                    if mc.attributeQuery(connectInfo.get('toAttr'), node=connectInfo.get('toNode'), exists=True):
                        mc.connectAttr(fromNodeAndAttr, toNodeAndAttr, force=True)

            mc.select(cl=True)
            if selectObject:
                for obj in selectObject:
                    if mc.objExists(obj):
                        mc.select(obj, add=True)

            om.MGlobal.displayInfo('Succeed apply preset to %s node.' % node)
        else:
            om.MGlobal.displayWarning('No preset named %s for nodeType %s' % (presetName, nType))


class iniFile():

    def __init__(self, fileDir, fileName, *args):
        self.iniFile = fileDir + '/' + fileName
        self.config = ConfigParser.ConfigParser()
        if not os.path.exists(self.iniFile):
            self.config.add_section('setting')
            self.config.set('setting', 'language', '')
            self.config.set('setting', 'presets_dir', '')
            self.config.write(open(self.iniFile, 'w'))

    def getValue(self, item, *args):
        self.config.readfp(open(self.iniFile))
        return self.config.get('setting', item)

    def setValue(self, item, value, *args):
        self.config.read(self.iniFile)
        self.config.set('setting', item, value)
        self.config.write(open(self.iniFile, 'w'))


class win(tp.templateWindow):

    def __init__(self):
        tp.templateWindow.__init__(self)
        self.cutSize = 65
        self.fileDic = []
        self.treeDic = {}
        mel.eval('setCurrentRenderer("redshift")')
        redshiftOptionsTemp = mc.ls('redshiftOptions', type='RedshiftOptions')
        if redshiftOptionsTemp:
            self.redshiftOptionsNode = redshiftOptionsTemp[0]
        self.gridLayoutNumberOfChildren = 5
        self.configFilePath ='Z:/Resource/Library/Public/Final/Library/Preset'
        self.userAppDir = mc.internalVar(userAppDir=True)
        self.rootDir = 'Z:/Resource/Library/Public/Final/Library'
        self.iniFile = iniFile(fileDir=self.configFilePath, fileName='jn_redshiftManager.config')
        self.initPresetFilePath()
        self.language = self.iniFile.getValue('language')
        self.presetsDir = self.iniFile.getValue('presets_dir')
        if self.language == '':
            self.iniFile.setValue('language', 'en_US')
            self.language = self.iniFile.getValue('language')
        if self.presetsDir == '' or not os.path.exists(self.presetsDir):
            self.iniFile.setValue('presets_dir', self.initPresetFilePath())
            self.presetsDir = self.iniFile.getValue('presets_dir')
        self.localePath = self.rootDir + '/locale'
        gettext.install('redshiftManager_lang', self.localePath, unicode=True)
        gettext.translation('redshiftManager_lang', self.localePath, languages=[self.language]).install(True)
        self.uiContent['tabNames'] = [_('Common'),
         _('Output'),
         _('AOV'),
         _('Opt'),
         _('GI'),
         _('Photon'),
         _('SSS'),
         _('System'),
         _('Memory')]
        self.uiContent['tabDict'] = {self.uiContent['tabNames'][0]: 'Common',
         self.uiContent['tabNames'][1]: 'Output',
         self.uiContent['tabNames'][2]: 'Aov',
         self.uiContent['tabNames'][3]: 'Optimizations',
         self.uiContent['tabNames'][4]: 'GlobalIllumination',
         self.uiContent['tabNames'][5]: 'PhotonMapping',
         self.uiContent['tabNames'][6]: 'SubsurfaceScattering',
         self.uiContent['tabNames'][7]: 'System',
         self.uiContent['tabNames'][8]: 'Memory'}
        self.uiContent['window'] = 'jn_redshiftManagerWindow'
        self.uiContent['size'] = (650, 700)
        self.uiContent['title'] = _('Render Preset Manager')

    def commonMenu(self):
        """Create common menu items for all option boxes"""
        self.uiContent['editMenu'] = mc.menu(label=_('Edit'))
        self.uiContent['editMenuCPID'] = mc.menuItem(label=_('Change Project Image Directory...'), command=self.projectWindowCmd)
        self.uiContent['editMenuPreferences'] = mc.menuItem(label=_('Preferences'), subMenu=True)
        self.uiContent['editMenuSwitchLanguage'] = mc.menuItem(label=_('Lanuage'), subMenu=True)
        self.uiContent['editMenuSwitchLanguageUS'] = mc.menuItem(label=_('English'), command=partial(self.switchLanguage, 'en_US'))
        self.uiContent['editMenuSwitchLanguageCN'] = mc.menuItem(label=_('Simplified Chinese'), command=partial(self.switchLanguage, 'zh_CN'))
        self.uiContent['toolsMenu'] = mc.menu(label=_('Tools'))
        self.uiContent['toolsMenuProxyMeshSetting'] = mc.menuItem(label=_('Proxy Mesh Setting'), command=self.proxyMeshSettingCmd)
        self.uiContent['shaderTransfer'] = mc.menuItem(label=_('Shader Transfer'), command=self.shaderTransferCmd)
        self.uiContent['nodePreset'] = mc.menuItem(label=_('Node Preset Library'), command=self.nodePresetCmd)
        self.uiContent['helpMenu'] = mc.menu(label=_('Help'))
        self.uiContent['helpMenuItem'] = mc.menuItem(label='Help on %s' % self.uiContent['title'], command=self.helpMenuCmd)
        if self.language == 'zh_CN':
            mc.menuItem(self.uiContent['editMenuSwitchLanguageCN'], edit=True, enable=False)
        if self.language == 'en_US':
            mc.menuItem(self.uiContent['editMenuSwitchLanguageUS'], edit=True, enable=False)

    def displayOptions(self, *args):
        self.uiContent['mainPaneLayout'] = mc.paneLayout(paneSize=[1, 8, 8], staticHeightPane=1, configuration='horizontal2')
        mc.frameLayout(labelVisible=False)
        mc.rowLayout(numberOfColumns=20)
        sh1b2 = mc.shelfButton(image1='proxySetting_small.png', label=_('Proxy Mesh Setting'), annotation=_('Redhsift Proxy Setting Tool'), command=self.proxyMeshSettingCmd, imageOverlayLabel='Proxy')
        sh1b3 = mc.shelfButton(image1='shaderTransfer_small.png', label=_('Shader Transfer'), annotation=_('Shader Transfer Tool'), command=self.shaderTransferCmd, imageOverlayLabel='Trans')
        sh1b4 = mc.shelfButton(image1='nodePreset_small.png', label=_('Node Preset Library'), annotation=_('Node Preset Tool'), command=self.nodePresetCmd, imageOverlayLabel='NPreset')
        openBar1 = mc.shelfButton(image1='openBar.png', enable=True)
        sh1b4 = mc.shelfButton(image1='rvOpenWindow.png', label=_('Render View'), annotation=_('Open Render View'), command=mc.RenderViewWindow)
        sh1b5 = mc.shelfButton(image1='rvRender.png', label=_('Render the current frame(Redshift)'), annotation=_('Render the current frame(Redshift)'), command=mc.RenderIntoNewWindow)
        sh1b6 = mc.shelfButton(image1='rvIprRender.png', label=_('IPR render the current frame(Redshift)'), annotation=_('IPR render the current frame(Redshift)'), command=mc.IPRRenderIntoNewWindow)
        sh1b7 = mc.shelfButton(image1='rvRenderGlobals.png', label=_('Display Render Settings Window(Redshift)'), annotation=_('Display Render Settings Window(Redshift)'), command=partial(mel.eval, 'unifiedRenderGlobalsWindow'))
        mc.setParent('..')
        mc.setParent('..')
        self.uiContent['paneLayout'] = mc.paneLayout(paneSize=[1, 40, 60], staticWidthPane=1, configuration='vertical2')
        self.leftContent(parent=self.uiContent['paneLayout'])
        self.rightContent(parent=self.uiContent['paneLayout'])
        self.uiContent['helpLineFrameLayout'] = mc.frameLayout(labelVisible=False, parent=self.uiContent['optionsForm'])
        self.uiContent['helpLine'] = mc.helpLine()
        mc.formLayout(self.uiContent['optionsForm'], e=True, attachForm=([self.uiContent['mainPaneLayout'], 'top', 0],
         [self.uiContent['mainPaneLayout'], 'left', 2],
         [self.uiContent['mainPaneLayout'], 'right', 2],
         [self.uiContent['helpLineFrameLayout'], 'left', 2],
         [self.uiContent['helpLineFrameLayout'], 'right', 2],
         [self.uiContent['helpLineFrameLayout'], 'bottom', 0]), attachControl=([self.uiContent['mainPaneLayout'],
          'bottom',
          5,
          self.uiContent['helpLineFrameLayout']],))
        mc.window(self.uiContent['window'], widthHeight=self.uiContent['size'], resizeToFitChildren=1, sizeable=1, edit=True)

    def leftContent(self, parent):
        self.uiContent['leftMainFormLayout'] = mc.formLayout(nd=100)
        self.uiContent['leftMainTabLayout'] = mc.tabLayout(innerMarginWidth=5, innerMarginHeight=5, tabsVisible=0, childResizable=1, width=400)
        self.uiContent['leftOptionsForm'] = mc.formLayout(nd=100)
        self.uiContent['leftFrameLayout'] = mc.frameLayout(labelVisible=0, borderStyle='in')
        mc.rowLayout(numberOfColumns=2)
        mc.text(label=_(' Render Layer'))
        self.uiContent['leftRenderLayerOptionMenu'] = mc.optionMenu(annotation=_('Select layer to adjust render settings for'), cc=self.updateCurrentRenderLayerSel)
        mc.setParent(self.uiContent['leftFrameLayout'])
        self.uiContent['leftPresetsFrameLayout'] = mc.frameLayout(label=_('Presets'), labelVisible=1, collapse=0, collapsable=0, borderStyle='in')
        mc.columnLayout(adj=1)
        mc.rowLayout(numberOfColumns=3, adjustableColumn3=2)
        mc.text(label=_(' Dir: '))
        self.uiContent['presetsDirTF'] = mc.textField(text=self.presetsDir, changeCommand=self.presetsDirTFChangeCmd)
        mc.button(label=_('Set'), command=self.presetsDirSetCmd)
        mc.setParent('..')
        mc.rowLayout(numberOfColumns=2, adjustableColumn2=2)
        mc.textField(text='')
        self.uiContent['leftIntSlider'] = mc.intSlider(min=50, max=200, value=60, step=1, dragCommand=self.updateGridLayout)
        mc.setParent('..')
        mc.setParent(self.uiContent['leftPresetsFrameLayout'])
        mc.frameLayout(labelVisible=0, borderStyle='in')
        self.uiContent['leftPaneLayout'] = mc.paneLayout(configuration='vertical2', paneSize=[1, 15, 85], staticWidthPane=1, width=320)
        self.uiContent['leftTSLFormLayout'] = mc.formLayout(nd=100)
        self.uiContent['leftTSLTabLayout'] = mc.tabLayout(innerMarginWidth=5, innerMarginHeight=5, tabsVisible=0, childResizable=1)
        self.uiContent['leftTextScrollList'] = mc.textScrollList(append=[ i for i in range(0, 20) ], doubleClickCommand=self.textScrollListDoubleClickCommand, selectCommand=self.updateGridLayout)
        self.textScrollListPopupMenuCmd(parent=self.uiContent['leftTextScrollList'])
        mc.setParent(self.uiContent['leftPaneLayout'])
        self.uiContent['leftGridTabLayout'] = mc.tabLayout(scrollable=1, innerMarginWidth=5, innerMarginHeight=5, tabsVisible=0, childResizable=1)
        mc.popupMenu(parent=self.uiContent['leftGridTabLayout'])
        mc.menuItem(label=_('New..'), command=self.createRenderPresetCmd)
        mc.menuItem(label=_('Delete'), command=self.deletePresetFileCmd)
        mc.setParent(self.uiContent['leftGridTabLayout'])
        self.uiContent['leftGridLayout'] = mc.gridLayout(columnsResizable=1, width=200)
        mc.setParent(parent)
        self.updateRenderLayerOptionMenu()
        self.updatePresetLayout()
        mc.formLayout(self.uiContent['leftTSLFormLayout'], edit=True, attachForm=([self.uiContent['leftTSLTabLayout'], 'top', 0],
         [self.uiContent['leftTSLTabLayout'], 'left', 2],
         [self.uiContent['leftTSLTabLayout'], 'right', 2],
         [self.uiContent['leftTSLTabLayout'], 'bottom', 0]))
        mc.formLayout(self.uiContent['leftOptionsForm'], edit=True, attachForm=([self.uiContent['leftFrameLayout'], 'top', 0],
         [self.uiContent['leftFrameLayout'], 'left', 2],
         [self.uiContent['leftFrameLayout'], 'right', 2],
         [self.uiContent['leftFrameLayout'], 'bottom', 0]))
        mc.formLayout(self.uiContent['leftMainFormLayout'], e=True, attachForm=([self.uiContent['leftMainTabLayout'], 'top', 0],
         [self.uiContent['leftMainTabLayout'], 'left', 2],
         [self.uiContent['leftMainTabLayout'], 'right', 2],
         [self.uiContent['leftMainTabLayout'], 'bottom', 0]))
        mc.setParent(parent)

    def rightContent(self, parent, *args):
        tabs = mc.tabLayout(innerMarginWidth=5, innerMarginHeight=5, tabsVisible=1, childResizable=1, visible=0)
        for tab in self.uiContent['tabNames']:
            self.addTab(label=tab, parent=tabs)

    def updatePresetLayout(self, *args):
        self.updateTextScrollList()
        self.updateGridLayout()

    def existSetFile(self, dirPaht, *args):
        if os.path.exists(dirPaht):
            subFiles = os.listfile(dirPath)

    def getDirList(self, url, *args):
        files = os.listdir(url)
        if len(files) > 0:
            for file in files:
                myfile = url + '/' + file
                if os.path.isdir(myfile):
                    subDirs = os.listdir(myfile)
                    appendItemText = ''
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

    def projectWindowCmd(self, *args):
        mel.eval('projectWindow')

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

    def updateGridLayout(self, *args):
        libraryItems = mc.gridLayout(self.uiContent['leftGridLayout'], ca=1, q=1)
        if libraryItems:
            if len(libraryItems):
                mc.deleteUI(libraryItems)
        dirPath = self.presetsDir + self.getTextScrollListRelativePath()
        xmlFiels = []
        if os.path.isdir(dirPath):
            files = os.listdir(dirPath)
            if files:
                for f in files:
                    if True in map(f.endswith, ['.connectMap']):
                        xmlFiels.append(dirPath + '/' + f)

        if xmlFiels:
            intSliderValue = mc.intSlider(self.uiContent['leftIntSlider'], value=1, q=1)
            gridLayoutWidth = mc.gridLayout(self.uiContent['leftGridLayout'], width=1, q=1)
            numberOfColumns = gridLayoutWidth / intSliderValue
            cellWidthHeight = gridLayoutWidth / numberOfColumns
            for xmlFile in xmlFiels:
                mc.setParent(self.uiContent['leftGridLayout'])
                picPath = xmlFile.replace('.connectMap', '.png')
                cl1 = mc.frameLayout(labelVisible=0, collapse=0, collapsable=0, borderStyle='out')
                if os.path.exists(picPath):
                    btn = mc.symbolButton(image=picPath, command=partial(self.presetBtnClickCmd, xmlFile), width=cellWidthHeight - 5, height=cellWidthHeight - 5)
                else:
                    btn = mc.symbolButton(image='defaultCustomLayout.png', command=partial(self.presetBtnClickCmd, xmlFile), width=cellWidthHeight, height=cellWidthHeight)
                itcb1 = mc.iconTextCheckBox(style='textOnly', height=cellWidthHeight / 5.0, label=os.path.basename(xmlFile).split('.')[0], align='center', backgroundColor=[82 / 255.0, 82 / 255.0, 82 / 255.0], enableBackground=1)
                itcb1 = mc.iconTextCheckBox(itcb1, edit=1, onCommand=partial(self.iconTextCheckBoxOnCmd, itcb1), offCommand=partial(self.iconTextCheckBoxOffCmd, itcb1))
                mc.popupMenu(parent=cl1)
                mc.menuItem(label=_('Rename'), command=partial(self.renameCurrentPresetCmd, itcb1, xmlFile))
                mc.menuItem(label=_('Update..'), command=partial(self.updateCurrentPresetCmd, btn, itcb1, xmlFile))
                mc.menuItem(label=_('Screen Shot'), command=partial(self.presetBtnScreenShotCmd, btn, picPath))
                mc.menuItem(label=_('View Picture'), command=partial(self.viewSamplePictureCmd, picPath))

            mc.gridLayout(self.uiContent['leftGridLayout'], edit=1, cellWidthHeight=[cellWidthHeight, cellWidthHeight + 12], numberOfColumns=numberOfColumns, position=['left', 50])

    def iconTextCheckBoxOnCmd(self, object, *args):
        mc.iconTextCheckBox(object, edit=1, backgroundColor=[104 / 255.0, 140 / 255.0, 182 / 255.0], enableBackground=1)

    def iconTextCheckBoxOffCmd(self, object, *args):
        mc.iconTextCheckBox(object, edit=1, backgroundColor=[82 / 255.0, 82 / 255.0, 82 / 255.0], enableBackground=1)

    def initPresetFilePath(self):
        filePath = 'Z:/Resource/Library/Public/Final/Library/' + 'Preset/Render'
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

    def updateRenderLayerOptionMenu(self, *args):
        mc.setParent(self.uiContent['window'])
        if not mc.objExists('renderLayerManager'):
            return
        mel.eval('string $layers[] = `listConnections renderLayerManager.renderLayerId`;')
        if mel.eval('$tempVar = size($layers)') > 0:
            currLayer = mc.editRenderLayerGlobals(query=True, currentRenderLayer=True)
            mel.eval('string $currLayer = `editRenderLayerGlobals -q -currentRenderLayer`;')
            layers = mel.eval('$temVar = sortLayers($layers)')
            numLayers = len(layers)
            menuItemNames = mc.optionMenu(self.uiContent['leftRenderLayerOptionMenu'], itemListLong=True, query=True)
            numItems = 0
            if menuItemNames:
                numItems = len(menuItemNames)
            i = 0
            j = 0
            currItem = ''
            for i in range(0, numLayers):
                layer = layers[numLayers - i - 1]
                label = layer
                if layer == 'defaultRenderLayer':
                    label = 'masterLayer'
                if layer == currLayer:
                    currItem = label
                if i >= numItems:
                    mc.menuItem(label=label, parent=self.uiContent['leftRenderLayerOptionMenu'])
                else:
                    mc.menuItem(menuItemNames[i], edit=True, label=label)
                j = i

            if numItems > j:
                for i in range(j, numItems):
                    print numItems[i]
                    mc.deleteUI(menuItemNames[i])

            if currItem != '':
                mc.optionMenu(self.uiContent['leftRenderLayerOptionMenu'], edit=True, value=currItem)

    def updateCurrentRenderLayerSel(self, *args):
        mc.setParent(self.uiContent['window'])
        currLayer = mc.editRenderLayerGlobals(query=True, currentRenderLayer=True)
        newLayer = mc.optionMenu(self.uiContent['leftRenderLayerOptionMenu'], query=True, value=True)
        if newLayer == 'masterLayer':
            newLayer = 'defaultRenderLayer'
        if currLayer != newLayer and mc.objExists(newLayer) and mc.nodeType(newLayer) == 'renderLayer':
            if mel.eval('catch(`editRenderLayerGlobals -currentRenderLayer "%s"`)' % newLayer):
                mc.optionMenu(self.uiContent['leftRenderLayerOptionMenu'], edit=True, value=currLayer)

    def addTab(self, label, parent):
        mc.setParent(parent)
        form = mc.formLayout()
        tabName = self.uiContent['tabDict'][label]
        mel.eval('source "redshiftCreate%sTab.mel"' % tabName)
        mel.eval('redshiftCreate%sTab' % tabName)
        mc.tabLayout(parent, edit=True, tabLabel=(form, label))

    def switchLanguage(self, language, *args):
        self.iniFile.setValue('language', language)

    def outputNukeToolCmd(self, *args):
        jn_ns.main()

    def proxyMeshSettingCmd(self, *args):
        jn_rpms.main()

    def shaderTransferCmd(self, *args):
        mel.eval('python("from idmt.maya.GA import GA_shaderTransfer")')
        mel.eval('python("GA_shaderTransfer.main()")')

    def nodePresetCmd(self, *args):
        mel.eval('python("from idmt.maya.GA import GA_nodePresets")')
        mel.eval('python("GA_nodePresets.main()")')

    def presetBtnClickCmd(self, presetFilePath, *args):
        applyAOVPresetToSetting(presetFilePath=presetFilePath.split('.')[0] + '.aov')
        applyConnectMapToNode(node=self.redshiftOptionsNode, presetFilePath=presetFilePath, blend=1)

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
        result = mc.promptDialog(title=_('Rename Preset'), message=_('Enter Name:'), button=[_('OK'), _('Cancel')], defaultButton=_('OK'), cancelButton=_('Cancel'), dismissString=_('Cancel'))
        if result == _('OK'):
            newName = mc.promptDialog(query=True, text=True)
            mc.iconTextCheckBox(button, label=newName, e=1)
            for f in os.listdir(dirPath):
                oldNameLen = len(iconTextCheckBoxLabel)
                newXmlName = newName + f[oldNameLen:]
                if f[:oldNameLen] == iconTextCheckBoxLabel:
                    os.rename(dirPath + '/' + f, dirPath + '/' + newXmlName)

    def copyCurrentPresetCmd(self, presetFilePath, *args):
        pass

    def updateCurrentPresetCmd(self, btn, itcb, presetFilePath, *args):
        itcbLabel = mc.iconTextCheckBox(itcb, label=True, query=True)
        dirName = os.path.dirname(presetFilePath)
        for f in os.listdir(dirName):
            if f[:len(itcbLabel)] == itcbLabel:
                os.remove(dirName + '/' + f)

        stateAndName = saveConnectMapPreset(node=self.redshiftOptionsNode, ppath=dirName, presetName=itcbLabel, autoRename=None, mode='modify')
        createAOVPreset(dirPath=os.path.dirname(stateAndName[2]), presetName=os.path.basename(stateAndName[2]).split('.')[0])
        mc.symbolButton(btn, image='defaultCustomLayout.png', edit=True)

    def addFolderCmd(self, *args):
        presetFilePath = ''
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
        selectIndexedItem = mc.textScrollList(self.uiContent['leftTextScrollList'], selectIndexedItem=1, q=1)
        if selectIndexedItem:
            if selectIndexedItem:
                presetFilePath = self.presetsDir + self.getTextScrollListRelativePath()
            else:
                presetFilePath = self.presetsDir
            result = mc.promptDialog(title=_('Create Render Preset'), message=_('Enter Name:'), text='temp', button=[_('OK'), _('Cancel')], defaultButton=_('OK'), cancelButton=_('Cancel'), dismissString=_('Cancel'))
            if result == _('OK'):
                presetName = mc.promptDialog(query=True, text=True)
                if presetName:
                    stateAndName = saveConnectMapPreset(node=self.redshiftOptionsNode, ppath=presetFilePath, presetName=presetName, autoRename=None, mode=None)
                    createAOVPreset(dirPath=os.path.dirname(stateAndName[2]), presetName=os.path.basename(stateAndName[2]).split('.')[0])
                    if stateAndName[0]:
                        self.updateGridLayout()
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
        libraryItems = mc.gridLayout(self.uiContent['leftGridLayout'], ca=1, q=1)
        if libraryItems:
            for i in libraryItems:
                iconTextCheckBox = mc.frameLayout(i, childArray=1, q=1)[1]
                if mc.iconTextCheckBox(iconTextCheckBox, value=1, q=1):
                    iconTextCheckBoxLabel = mc.iconTextCheckBox(iconTextCheckBox, label=1, q=1)
                    for f in os.listdir(dirPath):
                        if f[:len(iconTextCheckBoxLabel)] == iconTextCheckBoxLabel:
                            os.remove(dirPath + '/' + f)

            self.updateGridLayout()

    def shotPixmap(self, button, filePath, *args):
        widget = fullScreenLabel(parent=getMayaWindow(), button=button, parentClass=self, picPath=filePath)
        widget.setMouseTracking(True)
        widget.show()


class fullScreenLabel(QtGui.QLabel):

    def __init__(self, parent = None, button = None, parentClass = None, picPath = None, *args):
        QtGui.QLabel.__init__(self, parent)
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
        self.update()

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

