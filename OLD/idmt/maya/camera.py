# -*- coding: utf-8 -*-
# Copyright (C) 2000-2010 IDMT. All rights reserved.
'''
Functions for Camera
'''
__author__    = 'huangzhongwei@idmt.com.cn'
__date__    = '2011-03-02'

import idmt.maya.cmds
import maya.cmds
import maya.mel
import maya.OpenMaya
import os
import re

def CheckPosition(camera = None, silent = False):
    rs = True

    if camera == None:
        maya.mel.eval('source "zwCameraImportExport.mel"')
        camera = maya.mel.eval('zwGetCameraEx ""')
    if not maya.cmds.objExists(camera):
        return rs
    cameraName = re.search(r'[^\|]+$', camera).group(0)

    project =  maya.mel.eval('zwGetProject ""')
    max = 15000
    if project == "Ninjago" or project == 'VickyTheViking':  #添加VV项目的判断
        max = 3000

    translation = maya.cmds.xform(camera, query = True, worldSpace = True, translation = True)
    if abs(translation[0]) > max or abs(translation[1]) > max or abs(translation[2]) > max:
        if silent:
            os.environ["ISSUE_CAMERA_POSITION"] = "(>%d), %s: %.3f %.3f %.3f" % (max, cameraName, translation[0], translation[1], translation[2])
            return False
        if project == "Ninjagox" or project == 'VickyTheViking' : #添加VV项目的判断
            if maya.cmds.about(batch = True):
                message = u'摄像机离原点过远（>%d），这可能会导致渲染问题，建议往原点靠拢\n%s: %.3f %.3f %.3f\n如有疑问请联系项目TD' % (max, cameraName, translation[0], translation[1], translation[2])
                maya.OpenMaya.MGlobal.displayError(message)
            else:
                message = u'摄像机离原点过远（>%d），这可能会导致渲染问题，建议往原点靠拢\n\n%s: %.3f %.3f %.3f\n\n如有疑问请联系项目TD\n' % (max, cameraName, translation[0], translation[1], translation[2])
                maya.cmds.confirmDialog(message = message, button = ["OK"])
            rs = False
        else:
            if not maya.cmds.about(batch = True):
                message = u'摄像机离原点过远（>%d），这可能会导致渲染问题，建议往原点靠拢\n\n%s: %.3f %.3f %.3f\n\n点 Cancel 返回检查处理，点 Ignore 忽略继续\n\n如有疑问请联系项目TD\n' % (max, cameraName, translation[0], translation[1], translation[2])
                result = maya.cmds.confirmDialog(message = message, button = ["Cancel", "Ignore"], defaultButton = "Cancel", cancelButton = "Cancel", dismissString = "Cancel")
                if result == "Cancel":
                    rs = False

    return rs

def DisplayGateMaskQuery():
    '''
    查询IDMT黑边的状态
    '''
    camera = ''
    modelPanel = maya.cmds.getPanel(withFocus = True)
    if maya.cmds.getPanel(typeOf = modelPanel)  == 'modelPanel':
        camera = maya.cmds.modelEditor(modelPanel, query = True, camera = True)
    elif maya.cmds.about(apiVersion = True) >= 200900:
        view = maya.mel.eval('getCustomViewEditorFromPanel "%s"' % (modelPanel))
        if maya.cmds.stereoCameraView(view, exists = True):
            camera = maya.cmds.stereoCameraView(view, query = True, camera = True)

    if camera == '':
        return False

    attrs = maya.cmds.listAttr('%s.imagePlane' % (camera), multi = True)
    if attrs != None:
        for attr in attrs:
            imagePlanes = maya.cmds.listConnections('%s.%s' % (camera, attr))
            if imagePlanes == None:
                continue
            for imagePlane in imagePlanes:
                imageName = maya.cmds.getAttr('%s.imageName' % (imagePlane))
                imageName = os.path.basename(imageName)
                if imageName == 'resolutionGate.iff' or imageName == 'Guidance_frame.iff':
                    return True

    return False

def DisplayGateMaskQuery1():
    '''
    查询IDMT黑边的状态
    '''
    #if os.getenv('USERNAME') == 'huangzhongwei':
    if maya.cmds.about(apiVersion = True) >= 200900:
        return DisplayGateMaskQuery2009()

    camera = ''
    modelPanel = maya.cmds.getPanel(withFocus = True)
    if maya.cmds.getPanel(typeOf = modelPanel)  == 'modelPanel':
        camera = maya.cmds.modelEditor(modelPanel, query = True, camera = True)
    elif maya.cmds.about(apiVersion = True) >= 200900:
        view = maya.mel.eval('getCustomViewEditorFromPanel "%s"' % (modelPanel))
        if maya.cmds.stereoCameraView(view, exists = True):
            camera = maya.cmds.stereoCameraView(view, query = True, camera = True)

    if camera == '':
        return False

    attrs = maya.cmds.listAttr('%s.imagePlane' % (camera), multi = True)
    if attrs != None:
        for attr in attrs:
            imagePlanes = maya.cmds.listConnections('%s.%s' % (camera, attr))
            if imagePlanes == None:
                continue
            for imagePlane in imagePlanes:
                imageName = maya.cmds.getAttr('%s.imageName' % (imagePlane))
                imageName = os.path.basename(imageName)
                if imageName == 'resolutionGate.iff' or imageName == 'Guidance_frame.iff':
                    return True

    return False

def DisplayGateMaskQuery2009():
    '''
    查询IDMT黑边的状态
    '''
    return False

def DisplayGateMaskRemove():
    '''
    不显示IDMT黑边
    '''
    cameras = []
    modelPanel = maya.cmds.getPanel(withFocus = True)
    if maya.cmds.getPanel(typeOf = modelPanel)  == 'modelPanel':
        cameras.append(maya.cmds.modelEditor(modelPanel, query = True, camera = True))
    elif maya.cmds.about(apiVersion = True) >= 200900:
        view = maya.mel.eval('getCustomViewEditorFromPanel "%s"' % (modelPanel))
        if maya.cmds.stereoCameraView(view, exists = True):
            stereoCamera = maya.cmds.stereoCameraView(view, query = True, camera = True)
            cameras.append(stereoCamera)
            stereoCamera = maya.mel.eval('getTransform "%s"' % (stereoCamera))
            for LR in ('leftCam', 'rightCam'):
                connections = maya.cmds.listConnections('%s.%s' % (stereoCamera, LR))
                cameras.append(connections[0])

    for camera in cameras:
        attrs = maya.cmds.listAttr('%s.imagePlane' % (camera), multi = True)
        if attrs == None:
            continue
        for attr in attrs:
            imagePlanes = maya.cmds.listConnections('%s.%s' % (camera, attr))
            if imagePlanes == None:
                continue
            for imagePlane in imagePlanes:
                if not maya.cmds.objExists(imagePlane):
                    continue
                imageName = maya.cmds.getAttr('%s.imageName' % (imagePlane))
                imageName = os.path.basename(imageName)
                if imageName == 'resolutionGate.iff' or imageName == 'Guidance_frame.iff':
                    maya.cmds.delete(imagePlane)

def DisplayGateMaskRemove1():
    '''
    不显示IDMT黑边
    '''
    if not maya.mel.eval('zwGetProject ""') in ['GummiTarzan', 'OTTO']:
        if maya.cmds.about(apiVersion = True) >= 200900:
            DisplayGateMaskRemove2009()
            return

    cameras = []
    modelPanel = maya.cmds.getPanel(withFocus = True)
    if maya.cmds.getPanel(typeOf = modelPanel)  == 'modelPanel':
        cameras.append(maya.cmds.modelEditor(modelPanel, query = True, camera = True))
    elif maya.cmds.about(apiVersion = True) >= 200900:
        view = maya.mel.eval('getCustomViewEditorFromPanel "%s"' % (modelPanel))
        if maya.cmds.stereoCameraView(view, exists = True):
            stereoCamera = maya.cmds.stereoCameraView(view, query = True, camera = True)
            cameras.append(stereoCamera)
            stereoCamera = maya.mel.eval('getTransform "%s"' % (stereoCamera))
            for LR in ('leftCam', 'rightCam'):
                connections = maya.cmds.listConnections('%s.%s' % (stereoCamera, LR))
                cameras.append(connections[0])

    for camera in cameras:
        attrs = maya.cmds.listAttr('%s.imagePlane' % (camera), multi = True)
        if attrs == None:
            continue
        for attr in attrs:
            imagePlanes = maya.cmds.listConnections('%s.%s' % (camera, attr))
            if imagePlanes == None:
                continue
            for imagePlane in imagePlanes:
                if not maya.cmds.objExists(imagePlane):
                    continue
                imageName = maya.cmds.getAttr('%s.imageName' % (imagePlane))
                imageName = os.path.basename(imageName)
                if imageName == 'resolutionGate.iff' or imageName == 'Guidance_frame.iff':
                    maya.cmds.delete(imagePlane)

def DisplayGateMaskRemove2009():
    '''
    不显示IDMT黑边
    '''
    idmtDisplayGateMask = maya.cmds.optionVar(query = 'idmtDisplayGateMask')
    if idmtDisplayGateMask == 0 or idmtDisplayGateMask == '':
        return
    maya.cmds.optionVar(stringValue = ('idmtDisplayGateMask', ''))
    maya.mel.eval(idmtDisplayGateMask)

def DisplayGateMaskSet1(imageName):
    '''
    显示IDMT黑边
    '''
    cameras = []
    modelPanel = maya.cmds.getPanel(withFocus = True)
    if maya.cmds.getPanel(typeOf = modelPanel)  == 'modelPanel':
        cameras.append(maya.cmds.modelEditor(modelPanel, query = True, camera = True))
    elif maya.cmds.about(apiVersion = True) >= 200900:
        view = maya.mel.eval('getCustomViewEditorFromPanel "%s"' % (modelPanel))
        if maya.cmds.stereoCameraView(view, exists = True):
            stereoCamera = maya.cmds.stereoCameraView(view, query = True, camera = True)
            cameras.append(stereoCamera)
            stereoCamera = maya.mel.eval('getTransform "%s"' % (stereoCamera))
            for LR in ('leftCam', 'rightCam'):
                connections = maya.cmds.listConnections('%s.%s' % (stereoCamera, LR))
                cameras.append(connections[0])

    if len(cameras) == 0:
        return
    transform = maya.mel.eval('getTransform "%s"' % (cameras[0]))

    level = 8
    if re.search(r'[/\\]OKI[/\\]', imageName) != None:
        level = 2.666667
    elif re.search(r'[/\\]WinxClubII[/\\]', imageName) != None:
        level = 2
    for camera in cameras:
        imagePlane = maya.cmds.createNode('imagePlane')
        maya.cmds.connectAttr('%s.message' % (imagePlane), '%s.imagePlane' % (camera),  nextAvailable = True)

        #如果有imagePlane，imagePlane必须最后连，否则显示不出来
        connections = maya.cmds.listConnections('%s.imagePlane[0]' % (camera), plugs = True)
        if connections != None:
            if len(connections) == 1:
                maya.cmds.disconnectAttr(connections[0], '%s.imagePlane[0]' % (camera))
                maya.cmds.connectAttr(connections[0], '%s.imagePlane[0]' % (camera))

        maya.cmds.setAttr('%s.displayOnlyIfCurrent' % (imagePlane), True)
        maya.cmds.setAttr('%s.imageName' % (imagePlane), imageName, type = 'string')
        maya.cmds.setAttr('%s.fit' % (imagePlane), 4)

        script = ''
        script += "// Created by Toggle Custom Resolution Gate Tool, HuangZhongwei R&D IDMT\n\n";
        script += imagePlane + ".depth = " + camera + ".nearClipPlane * 2.1;\n\n";
        if re.search(r'[/\\]WinxClubII[/\\]', imageName) != None:
            maya.cmds.setAttr('%s.useDepthMap' % (imagePlane), True)
            script += imagePlane + ".depthBias = " + camera + ".nearClipPlane * 2.1;\n\n";
        script += "float $rezAspect = defaultResolution.width / defaultResolution.height;\n";
        script += "$rezAspect = defaultResolution.deviceAspectRatio;\n";
        script += "float $camX = " + camera + ".horizontalFilmAperture;\n";
        script += "float $camY = " + camera + ".verticalFilmAperture;\n";
        script += "float $camAspect = $camX / $camY;\n";
        script += "float $scaleX = " + transform + ".scaleX / " + transform + ".scaleZ;\n";
        script += "float $scaleY = " + transform + ".scaleY / " + transform + ".scaleZ;\n";
        script += "float $level = " + str(level) + ";\n";
        script += "int $fitType = " + camera + ".filmFit;\n\n";
        script += "if ($fitType == 0) {\t\t\t\t// FILL\n";
        script += "\tif ($rezAspect < $camAspect) {\n";
        script += "\t\t" + imagePlane + ".sizeX = $camY * $rezAspect * $scaleX * $level;\n";
        script += "\t\t" + imagePlane + ".sizeY = $camY * $scaleY * $level;\n";
        script += "\t} else {\n";
        script += "\t\t" + imagePlane + ".sizeX = $camX * $scaleX * $level;\n";
        script += "\t\t" + imagePlane + ".sizeY = $camX / $rezAspect * $scaleY * $level;\n";
        script += "\t}\n";
        script += "} else if ($fitType == 1) {\t\t\t// HORIZONTAL\n";
        script += "\t" + imagePlane + ".sizeX = $camX * $scaleX * $level;\n";
        script += "\t" + imagePlane + ".sizeY = $camX / $rezAspect * $scaleY * $level;\n";
        script += "} else if ($fitType == 2) {\t\t\t// VERTICAL\n";
        script += "\t" + imagePlane + ".sizeX = $camY * $rezAspect * $scaleX * $level;\n";
        script += "\t" + imagePlane + ".sizeY = $camY * $scaleY * $level;\n";
        script += "} else if ($fitType == 3) {\t\t\t// OVERSCAN\n";
        script += "\tif ($rezAspect < $camAspect) {\n";
        script += "\t\t" + imagePlane + ".sizeX = $camX * $scaleX * $level;\n";
        script += "\t\t" + imagePlane + ".sizeY = $camX / $rezAspect * $scaleY * $level;\n";
        script += "\t} else {\n";
        script += "\t\t" + imagePlane + ".sizeX = $camY * $rezAspect * $scaleX * $level;\n";
        script += "\t\t" + imagePlane + ".sizeY = $camY * $scaleY * $level;\n";
        script += "\t}\n";
        script += "}\n";
        script += imagePlane + ".offsetX = " + camera + ".horizontalFilmOffset * $scaleX;\n";
        script += imagePlane + ".offsetY = " + camera + ".verticalFilmOffset * $scaleY;\n";

        maya.cmds.expression(string = script)

        #if re.search(r'[/\\]WinxClubII[/\\]', imageName) != None:
        #    maya.cmds.setAttr('%s.useDepthMap' % (imagePlane), True)
        #    maya.cmds.setAttr('%s.depthBias' % (imagePlane), maya.cmds.getAttr('%s.nearClipPlane' % (camera)))

def DisplayGateMaskSet2(imageName):
    '''
    显示IDMT黑边
    '''
    if not maya.mel.eval('zwGetProject ""') in ['GummiTarzan', 'OTTO']:
        if maya.cmds.about(apiVersion = True) >= 200900:
            DisplayGateMaskSet2009()
            return

    cameras = []
    modelPanel = maya.cmds.getPanel(withFocus = True)
    if maya.cmds.getPanel(typeOf = modelPanel)  == 'modelPanel':
        cameras.append(maya.cmds.modelEditor(modelPanel, query = True, camera = True))
    elif maya.cmds.about(apiVersion = True) >= 200900:
        view = maya.mel.eval('getCustomViewEditorFromPanel "%s"' % (modelPanel))
        if maya.cmds.stereoCameraView(view, exists = True):
            stereoCamera = maya.cmds.stereoCameraView(view, query = True, camera = True)
            cameras.append(stereoCamera)
            stereoCamera = maya.mel.eval('getTransform "%s"' % (stereoCamera))
            for LR in ('leftCam', 'rightCam'):
                connections = maya.cmds.listConnections('%s.%s' % (stereoCamera, LR))
                cameras.append(connections[0])

    if len(cameras) == 0:
        return
    transform = maya.mel.eval('getTransform "%s"' % (cameras[0]))

    level = 8
    if re.search(r'[/\\]OKI[/\\]', imageName) != None:
        level = 2.666667
    elif re.search(r'[/\\]WinxClubII[/\\]', imageName) != None:
        level = 2
    for camera in cameras:
        imagePlane = maya.cmds.createNode('imagePlane')
        maya.cmds.connectAttr('%s.message' % (imagePlane), '%s.imagePlane' % (camera),  nextAvailable = True)

        #如果有imagePlane，imagePlane必须最后连，否则显示不出来
        connections = maya.cmds.listConnections('%s.imagePlane[0]' % (camera), plugs = True)
        if connections != None:
            if len(connections) == 1:
                maya.cmds.disconnectAttr(connections[0], '%s.imagePlane[0]' % (camera))
                maya.cmds.connectAttr(connections[0], '%s.imagePlane[0]' % (camera))

        maya.cmds.setAttr('%s.displayOnlyIfCurrent' % (imagePlane), True)
        maya.cmds.setAttr('%s.imageName' % (imagePlane), imageName, type = 'string')
        maya.cmds.setAttr('%s.fit' % (imagePlane), 4)

        script = ''
        script += "// Created by Toggle Custom Resolution Gate Tool, HuangZhongwei R&D IDMT\n\n";
        script += imagePlane + ".depth = " + camera + ".nearClipPlane * 2.1;\n\n";
        if re.search(r'[/\\]WinxClubII[/\\]', imageName) != None:
            maya.cmds.setAttr('%s.useDepthMap' % (imagePlane), True)
            script += imagePlane + ".depthBias = " + camera + ".nearClipPlane * 2.1;\n\n";
        script += "float $rezAspect = defaultResolution.width / defaultResolution.height;\n";
        script += "$rezAspect = defaultResolution.deviceAspectRatio;\n";
        script += "float $camX = " + camera + ".horizontalFilmAperture;\n";
        script += "float $camY = " + camera + ".verticalFilmAperture;\n";
        script += "float $camAspect = $camX / $camY;\n";
        script += "float $scaleX = " + transform + ".scaleX / " + transform + ".scaleZ;\n";
        script += "float $scaleY = " + transform + ".scaleY / " + transform + ".scaleZ;\n";
        script += "float $level = " + str(level) + ";\n";
        script += "int $fitType = " + camera + ".filmFit;\n\n";
        script += "if ($fitType == 0) {\t\t\t\t// FILL\n";
        script += "\tif ($rezAspect < $camAspect) {\n";
        script += "\t\t" + imagePlane + ".sizeX = $camY * $rezAspect * $scaleX * $level;\n";
        script += "\t\t" + imagePlane + ".sizeY = $camY * $scaleY * $level;\n";
        script += "\t} else {\n";
        script += "\t\t" + imagePlane + ".sizeX = $camX * $scaleX * $level;\n";
        script += "\t\t" + imagePlane + ".sizeY = $camX / $rezAspect * $scaleY * $level;\n";
        script += "\t}\n";
        script += "} else if ($fitType == 1) {\t\t\t// HORIZONTAL\n";
        script += "\t" + imagePlane + ".sizeX = $camX * $scaleX * $level;\n";
        script += "\t" + imagePlane + ".sizeY = $camX / $rezAspect * $scaleY * $level;\n";
        script += "} else if ($fitType == 2) {\t\t\t// VERTICAL\n";
        script += "\t" + imagePlane + ".sizeX = $camY * $rezAspect * $scaleX * $level;\n";
        script += "\t" + imagePlane + ".sizeY = $camY * $scaleY * $level;\n";
        script += "} else if ($fitType == 3) {\t\t\t// OVERSCAN\n";
        script += "\tif ($rezAspect < $camAspect) {\n";
        script += "\t\t" + imagePlane + ".sizeX = $camX * $scaleX * $level;\n";
        script += "\t\t" + imagePlane + ".sizeY = $camX / $rezAspect * $scaleY * $level;\n";
        script += "\t} else {\n";
        script += "\t\t" + imagePlane + ".sizeX = $camY * $rezAspect * $scaleX * $level;\n";
        script += "\t\t" + imagePlane + ".sizeY = $camY * $scaleY * $level;\n";
        script += "\t}\n";
        script += "}\n";
        script += imagePlane + ".offsetX = " + camera + ".horizontalFilmOffset * $scaleX;\n";
        script += imagePlane + ".offsetY = " + camera + ".verticalFilmOffset * $scaleY;\n";

        maya.cmds.expression(string = script)

        #if re.search(r'[/\\]WinxClubII[/\\]', imageName) != None:
        #    maya.cmds.setAttr('%s.useDepthMap' % (imagePlane), True)
        #    maya.cmds.setAttr('%s.depthBias' % (imagePlane), maya.cmds.getAttr('%s.nearClipPlane' % (camera)))

def DisplayGateMaskSet2009():
    '''
    显示IDMT黑边
    '''
    project =  maya.mel.eval('zwGetProject ""')

    cameras = []
    modelPanel = maya.cmds.getPanel(withFocus = True)
    if maya.cmds.getPanel(typeOf = modelPanel)  == 'modelPanel':
        cameras.append(maya.cmds.modelEditor(modelPanel, query = True, camera = True))
    else:
        view = maya.mel.eval('getCustomViewEditorFromPanel "%s"' % (modelPanel))
        if maya.cmds.stereoCameraView(view, exists = True):
            stereoCamera = maya.cmds.stereoCameraView(view, query = True, camera = True)
            cameras.append(stereoCamera)
            stereoCamera = maya.mel.eval('getTransform "%s"' % (stereoCamera))
            for LR in ('leftCam', 'rightCam'):
                connections = maya.cmds.listConnections('%s.%s' % (stereoCamera, LR))
                cameras.append(connections[0])

    idmtDisplayGateMask = ''
    for camera in cameras:
        #idmtDisplayGateMask += 'zwSetAttrInt "%s.displayResolution" %d;\n' % (camera, maya.cmds.getAttr('%s.displayResolution' % (camera)))
        #idmt.maya.cmds.setAttr('%s.displayResolution' % (camera), 1)
        idmtDisplayGateMask += 'zwSetAttrInt "%s.displayGateMask" %d;\n' % (camera, maya.cmds.getAttr('%s.displayGateMask' % (camera)))
        idmt.maya.cmds.setAttr('%s.displayGateMask' % (camera), 1)
        if project == 'DiveollyDive3':
            idmtDisplayGateMask += 'setAttr "%s.displayGateMaskOpacity" %f;\n' % (camera, maya.cmds.getAttr('%s.displayGateMaskOpacity' % (camera)))
            maya.cmds.setAttr('%s.displayGateMaskOpacity' % (camera), 0.7)
            displayGateMaskColor = maya.cmds.getAttr('%s.displayGateMaskColor' % (camera))
            idmtDisplayGateMask += 'setAttr "%s.displayGateMaskColor" %f %f %f;\n' % (camera, displayGateMaskColor[0][0], displayGateMaskColor[0][1], displayGateMaskColor[0][2])
            maya.cmds.setAttr('%s.displayGateMaskColor' % (camera), 0, 0, 0, type = 'double3')
        else:
            idmtDisplayGateMask += 'setAttr "%s.displayGateMaskOpacity" %f;\n' % (camera, maya.cmds.getAttr('%s.displayGateMaskOpacity' % (camera)))
            maya.cmds.setAttr('%s.displayGateMaskOpacity' % (camera), 1)
            displayGateMaskColor = maya.cmds.getAttr('%s.displayGateMaskColor' % (camera))
            idmtDisplayGateMask += 'setAttr "%s.displayGateMaskColor" %f %f %f;\n' % (camera, displayGateMaskColor[0][0], displayGateMaskColor[0][1], displayGateMaskColor[0][2])
            maya.cmds.setAttr('%s.displayGateMaskColor' % (camera), 0, 0, 0, type = 'double3')
    maya.cmds.optionVar(stringValue = ('idmtDisplayGateMask', idmtDisplayGateMask))
