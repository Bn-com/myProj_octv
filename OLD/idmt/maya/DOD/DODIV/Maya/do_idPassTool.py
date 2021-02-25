# -*- coding: utf-8 -*-
import maya.cmds as mc
import maya.mel as mel
from xml.dom import minidom
import traceback
from xml.etree import ElementTree as ET
from pymel.core import *
import os
import re


def topParent(obj):

    varA = mc.listRelatives(obj, p=True)
    if varA:
        while(len(varA) > 0):
            varB = varA[0]
            varA = mc.listRelatives(varA[0], p=True)
            if not varA:
                return varB
    else:
        return obj


def do_writeIdPassFile(proj_name):
    path = r'//file-cluster/gdc/Projects/%s/%s_Scratch/TD/Rendering/idpass_files/' % (
        proj_name, proj_name)
    allRef = mc.file(q=True, r=True, shn=True)
    if len(allRef) != 1:
        mc.confirmDialog(
            title='Confirm', message=u'请确认场景中有且只有一个参考物体！！！', defaultButton='Yes')
        return u'没有输出任何idpass的信息！！！'

    idPassFn = allRef[0].split('.')[0]
    refLongName = mc.file(q=True, r=True, shn=False)
    ns = mc.file(refLongName[0], q=True, ns=True)
    if os.path.isfile(path + idPassFn + '.xml'):
        msg = idPassFn + u' 的 idpass 文件已存在，覆盖？'
        confirm = mc.confirmDialog(title='Confirm', message=msg, button=[
                                   'Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')
        if confirm == 'No':
            return u'没有输出任何idpass的信息！！！'
    writeIdPassFile(path, idPassFn, ns)


def vv_setIdPass(proj_name):
    path = r'//file-cluster/gdc/Projects/%s/%s_Scratch/TD/Rendering/idpass_files/' % s(
        proj_name, proj_name)
    matShd = matShader('do')
    mc.select(cl=True)

    allRef = mc.file(q=True, r=True)
    passName = ''
    for rr in allRef:
        fn = os.path.basename(rr).split('.')[0]
        idPassFn = path + fn + '.xml'
        if os.path.isfile(idPassFn):
            refObjNode = mc.referenceQuery(rr, rfn=True, tr=True)
            refObjTmp = mc.listConnections(
                refObjNode, s=False, d=True, type='transform')
            refObj = ''
            ns = mc.file(rr, q=True, ns=True)
            if refObjTmp:
                refObj = topParent(refObjTmp[0])
            else:
                refQs = mc.referenceQuery(rr, n=True)
                for rs in refQs:
                    if rs.find('confirmMessage') == -1:
                        refObj = topParent(rs)
                        break
            rgbs = []
            root = ET.parse(path + fn + ".xml")
            ipassNode = root.find('idPass')
            for c in ipassNode.getchildren():
                idpassLay = mc.createRenderLayer(refObj, name=fn.split(
                    '-')[0] + c.tag.capitalize(), number=1, noRecurse=True)
                mc.editRenderLayerGlobals(currentRenderLayer=idpassLay)
                mc.select(refObj, r=True)
                mc.hyperShade(assign=matShd)
                mc.hyperShade(assign=matShd)
                print ns
                print fn
                print refObj
                setIdPass(path, fn, ns, c)
            passName += ns + '\n'

    mel.eval(
        'renderLayerEditorRenderable RenderLayerTab "defaultRenderLayer" "0"')

    if not passName:
        mc.confirmDialog(
            title='Confirm', message=u'没有找到任何物体的 idpass 信息！！！', defaultButton='Yes')
    else:
        msg = u'成功为\n\n' + passName + u'\n添加了idpass信息'
        mc.confirmDialog(title='Confirm', message=msg, defaultButton='Yes')


"""
def vv_autoSetIdPass():
    path = r'//file-cluster/gdc/Projects/VickytheViking/VickytheViking_Scratch/TD/Rendering/idpass_files/'
    allRef = mc.file( q = True, r = True )
    passName = ''
    idpassLayerObj = []
    for rr in allRef:
        fn = os.path.basename( rr ).split('.')[0]
        idPassFn = path + fn + '.xml'
        if os.path.isfile( idPassFn ):
            refObjNode =  mc.referenceQuery(rr, rfn = True, tr = True) 
            refObj = mc.listConnections(refObjNode, s = False, d = True, type = 'transform')[0]
            idpassLayerObj.append (refObj )
    if len(idpassLayerObj) > 0:        
        idpassLay = mc.createRenderLayer (idpassLayerObj, name = 'idpass', number = 1, noRecurse = True)
        mc.editRenderLayerGlobals(currentRenderLayer = idpassLay)
    mel.eval('renderLayerEditorRenderable RenderLayerTab "defaultRenderLayer" "0"')
    for ref in allRef:
        fn =  os.path.basename( ref ).split('.')[0]
        idPassFn = path + fn + '.xml'
        if os.path.isfile( idPassFn ):
            ns = mc.file(ref, q = True, ns = True)
            setIdPass ( path, fn, ns )
            passName += ns +'\n'
            
    if not passName:
        mc.confirmDialog( title='Confirm', message=u'没有找到任何物体的 idpass 信息！！！', defaultButton='Yes')
    else:
        msg = u'成功为\n\n'+passName+u'\n添加了idpass信息'
        mc.confirmDialog( title='Confirm', message=msg, defaultButton='Yes')
"""


def setIdPass(path, fileName, fileNamespace, node):

    rShd = rgbShader('do', 'r')
    gShd = rgbShader('do', 'g')
    bShd = rgbShader('do', 'b')
    aShd = rgbShader('do', 'a')

    root = ET.parse(path + fileName + ".xml")
    mc.select(cl=True)

    rObjs = []
    gObjs = []
    bObjs = []
    aObjs = []

    for child in node.getchildren():
        if child.tag == 'rPass':
            rpassObj = child.text.replace('namespaceHolder', fileNamespace)
            if mc.objExists(rpassObj):
                rObjs.append(rpassObj)

        if child.tag == 'gPass':
            gpassObj = child.text.replace('namespaceHolder', fileNamespace)
            if mc.objExists(gpassObj):
                gObjs.append(gpassObj)

        if child.tag == 'bPass':
            bpassObj = child.text.replace('namespaceHolder', fileNamespace)
            if mc.objExists(bpassObj):
                bObjs.append(bpassObj)

        if child.tag == 'aPass':
            apassObj = child.text.replace('namespaceHolder', fileNamespace)
            if mc.objExists(apassObj):
                aObjs.append(apassObj)

    if len(rObjs):
        mc.select(rObjs, r=True)
        mc.hyperShade(assign=rShd)

    if len(gObjs):
        mc.select(gObjs, r=True)
        mc.hyperShade(assign=gShd)

    if len(bObjs):
        mc.select(bObjs, r=True)
        mc.hyperShade(assign=bShd)

    if len(aObjs):
        mc.select(aObjs, r=True)
        mc.hyperShade(assign=aShd)

    mc.select(cl=True)


def writePassPerLayer(rgb, fileNamespace, layerNode, doc):

    for s in rgb:
        r = mc.getAttr(s + '.outColor')[0][0]
        g = mc.getAttr(s + '.outColor')[0][1]
        b = mc.getAttr(s + '.outColor')[0][2]

        mr = mc.getAttr(s + '.outMatteOpacity')[0][0]
        mg = mc.getAttr(s + '.outMatteOpacity')[0][1]
        mb = mc.getAttr(s + '.outMatteOpacity')[0][2]

        if r == 1.0 and g == 0.0 and b == 0.0 and mr == 0.0 and mg == 0.0 and mb == 0.0:
            mc.select(cl=True)
            mc.hyperShade(objects=s)
            rObjs = mc.ls(sl=True, long=True)

            for i in rObjs:
                objNode = doc.createElement('rPass')
                layerNode.appendChild(objNode)
                i = i.replace(fileNamespace, 'namespaceHolder')
                i = i.replace('|namespaceHolderRNgroup', '*')
                objTextNode = doc.createTextNode(i)
                objNode.appendChild(objTextNode)

        elif r == 0.0 and g == 1.0 and b == 0.0 and mr == 0.0 and mg == 0.0 and mb == 0.0:
            mc.select(cl=True)
            mc.hyperShade(objects=s)
            gObjs = mc.ls(sl=True, long=True)

            for i in gObjs:
                objNode = doc.createElement('gPass')
                layerNode.appendChild(objNode)
                i = i.replace(fileNamespace, 'namespaceHolder')
                i = i.replace('|namespaceHolderRNgroup', '*')
                objTextNode = doc.createTextNode(i)
                objNode.appendChild(objTextNode)

        elif r == 0.0 and g == 0.0 and b == 1.0 and mr == 0.0 and mg == 0.0 and mb == 0.0:
            mc.select(cl=True)
            mc.hyperShade(objects=s)
            bObjs = mc.ls(sl=True, long=True)

            for i in bObjs:
                objNode = doc.createElement('bPass')
                layerNode.appendChild(objNode)
                i = i.replace(fileNamespace, 'namespaceHolder')
                i = i.replace('|namespaceHolderRNgroup', '*')
                objTextNode = doc.createTextNode(i)
                objNode.appendChild(objTextNode)

        elif r == 0.0 and g == 0.0 and b == 0.0 and mr == 1.0 and mg == 1.0 and mb == 1.0:
            mc.select(cl=True)
            mc.hyperShade(objects=s)
            aObjs = mc.ls(sl=True, long=True)

            for i in aObjs:
                objNode = doc.createElement('aPass')
                layerNode.appendChild(objNode)
                i = i.replace(fileNamespace, 'namespaceHolder')
                i = i.replace('|namespaceHolderRNgroup', '*')
                objTextNode = doc.createTextNode(i)
                objNode.appendChild(objTextNode)


def writeIdPassFile(path, fileName, fileNamespace):

    mc.select(cl=True)
    rgb = mc.ls(type='surfaceShader')
    if not rgb:
        mc.confirmDialog(title='Confirm', message=u'没有找到任何RGB信息！！！', defaultButton='Yes')

    allLayers = mc.listConnections(
        'renderLayerManager.renderLayerId', d=True, s=False)

    fh = open(path + fileName + '.xml', 'w')
    doc = minidom.Document()
    rootNode = doc.createElement('root')
    doc.appendChild(rootNode)
    ipNode = doc.createElement('idPass')
    rootNode.appendChild(ipNode)

    for layer in allLayers:
        if re.search(u'(Idp01|Idp02|Idp03|Idp04)', layer, re.IGNORECASE):
            mc.editRenderLayerGlobals(currentRenderLayer=layer)
            layerNodeName = u'Idp01'
            if re.search(u'Idp02', layer):
                layerNodeName = u'Idp02'
            elif re.search(u'Idp03', layer):
                layerNodeName = u'Idp03'
            elif re.search(u'Idp04', layer):
                layerNodeName = u'Idp04'
            layerNode = doc.createElement(layerNodeName.lower())
            ipNode.appendChild(layerNode)
            writePassPerLayer(rgb, fileNamespace, layerNode, doc)

    doc.writexml(fh, "", "", "", "utf-8")
    fh.close()
    mc.select(cl=True)
    msg = fileName + u' 的 idpass 信息已经输出！！！'
    mc.confirmDialog(title='Confirm', message=msg, defaultButton='Yes')


def rgbShader(projShotName, col):
    shdName = projShotName + '_color' + col.upper()
    if mc.objExists(shdName):
        return shdName
    shd = mc.shadingNode('surfaceShader', asShader=True, name=shdName)
    sg = mc.sets(renderable=True, noSurfaceShader=True,
                 empty=True, name=projShotName + '_color' + col + 'SG')
    mc.connectAttr(shd + '.outColor', sg + '.surfaceShader', f=True)
    mc.setAttr(shd + '.outMatteOpacity', 0, 0, 0, type='double3')
    if col == 'r':
        mc.setAttr(shd + '.outColor', 1.0, 0, 0, type='double3')
    elif col == 'g':
        mc.setAttr(shd + '.outColor', 0, 1.0, 0, type='double3')
    elif col == 'b':
        mc.setAttr(shd + '.outColor', 0, 0, 1.0, type='double3')
    else:
        mc.setAttr(shd + '.outMatteOpacity', 1.0, 1.0, 1.0, type='double3')
    return shd


def matShader(projShotName):
    shdName = projShotName + '_idpass_matte'
    if mc.objExists(shdName):
        return shdName
    shd = mc.shadingNode('lambert', asShader=True, name=shdName)
    sg = mc.sets(renderable=True, noSurfaceShader=True,
                 empty=True, name=projShotName + 'matShaderSG')
    mc.setAttr(shd + '.color', 0, 0, 0, type='double3')
    mc.setAttr(shd + ".matteOpacityMode", 0)
    return shd
#===========================================================================================
#================指定物体，渲染层，材质球（是否保存原材质）======================


def asign_obj_shader_to_RndLayer(objs, RndLay_name, shader_name=u'hold'):
    RL_node = RndLay_name
    if not mc.objExists(RndLay_name):
        RL_node = mc.createRenderLayer(e=True, name=RndLay_name, number=1, noRecurse=True, mc=True)

    mc.editRenderLayerGlobals(crl=RndLay_name)
    mc.editRenderLayerMembers(RL_node, objs)
    if shader_name != u'hold':
        SG_array = mc.listConnections(shader_name, source=False, destination=True, type='shadingEngine')
        shd_SG = u''

        if SG_array == None:
            shd_SG = mc.sets(name='%sSG' % (shader_name), renderable=True, noSurfaceShader=True, empty=True)
            mc.connectAttr(u'%s.outColor' % shader_name, u'%s.surfaceShader' % shd_SG, f=True)
        else:
            shd_SG = SG_array[0]
        for eachObj in objs:
            mc.sets(eachObj, e=True, forceElement=shd_SG)


def do_setIdPass(proj_name=u'DiveollyDive4', proj_abb=u'do'):
    matShd = matShader(proj_abb)
    mc.select(cl=True)
    path = r'//file-cluster/gdc/Projects/%s/%s_Scratch/TD/Rendering/idpass_files/' % (proj_name, proj_name)
    allRef = mc.file(q=True, r=True)
    passName = ''

    if not allRef:
        mc.confirmDialog(title='Confirm', message=u'没有找到参考文件！！！', defaultButton='Yes')
        return

    selNodes = []

    for rr in allRef:

        fn = os.path.basename(rr).split('.')[0]
        idPassFn = path + fn + '.xml'
        if os.path.isfile(idPassFn):

            refObjNode = referenceQuery(rr, rfn=True, tr=True)

            nodes = referenceQuery(refObjNode, n=True, dagPath=True)
            for node in nodes:

                bbox = xform(node, q=True, ws=True, bb=True)
                if bbox[0] or bbox[1] or bbox[2]:

                    nodeParent = PyNode(node).getParent()
                    if nodeParent:
                        if nodeParent.name().find('RNgroup') > -1:
                            selNodes.append(nodeParent)
                        else:
                            selNodes.append(node)
                    else:
                        selNodes.append(node)
                    break

    idpass_names = ['Idp01', 'Idp02', 'Idp03', 'Idp04']

    for idp in idpass_names:

        idpassLay = idp
        if not objExists(idpassLay):
            idpassLay = createRenderLayer(selNodes, name=idp, number=1, noRecurse=True)
        editRenderLayerGlobals(currentRenderLayer=idpassLay)

        select(selNodes, r=True)
        hyperShade(assign=matShd)
        hyperShade(assign=matShd)

        for rr in allRef:
            fn = os.path.basename(rr).split('.')[0]
            idPassFn = path + fn + '.xml'
            ns = mc.file(rr, q=True, ns=True)
            if os.path.isfile(idPassFn):
                """
                refObjNode =  mc.referenceQuery(rr, rfn = True, tr = True)
                refObjTmp = mc.listConnections(refObjNode, s = False, d = True, type = 'transform')
                refObj = ''
                ns = mc.file(rr, q = True, ns = True)
                if refObjTmp:
                        refObj = topParent(refObjTmp[0])
                else:
                        refQs = mc.referenceQuery(rr, n = True)
                        for rs in refQs:
                                if rs.find('confirmMessage') == -1:
                                        refObj = topParent( rs )
                                        break
                """
                rgbs = []
                root = ET.parse(path + fn + ".xml")
                ipassNode = root.find('idPass')

                for c in ipassNode.getchildren():
                    if c.tag == idp.lower():

                        setIdPass(path, fn, ns, c)

                passName += ns + '\n'

    mel.eval('renderLayerEditorRenderable RenderLayerTab "defaultRenderLayer" "0"')

    if not passName:
        mc.confirmDialog(title='Confirm', message=u'没有找到任何物体的 idpass 信息！！！', defaultButton='Yes')
    else:
        msg = u'成功为\n\n' + passName + u'\n添加了idpass信息'
        mc.confirmDialog(title='Confirm', message=msg, defaultButton='Yes')
