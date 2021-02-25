# -*- coding: utf-8 -*-
import maya.cmds as mc
import maya.mel as mel
from pymel.core import *
import sys
import re

from idmt.maya.DOD.DODIV.Maya.do_idPassTool import *
import idmt.maya.DOD.DODIV.Maya.commonProperties as docp
import idmt.maya.DOD.DODIV.Maya.zb_createSpecRL as zcrl


def do_deleteTurtleNodes():
    turtleNodes = mc.ls('Turtle*')
    for node in turtleNodes:
        mc.lockNode(node, lock=False)
        mc.delete(node)


def fresnelShader(projShotName):
    fsl = mc.shadingNode('surfaceShader', asShader=True, name=projShotName + '_fresnel')
    sg = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=projShotName + '_fresnelSG')
    mc.connectAttr(fsl + '.outColor', sg + '.surfaceShader', f=True)

    sampler = mc.createNode('samplerInfo', name=projShotName + '_depSamplerInfo')
    ramp = mc.shadingNode('ramp', asTexture=True, name=projShotName + '_fslRamp')
    rampPlaTex = mc.shadingNode('place2dTexture', asUtility=True, name=projShotName + '_fslPlaTex')
    mc.connectAttr(rampPlaTex + '.outUV', ramp + '.uv', f=True)
    mc.setAttr(ramp + '.colorEntryList[2].color', 0, 0, 0, type='double3')
    mc.setAttr(ramp + '.colorEntryList[0].color', 1, 1, 1, type='double3')
    mc.removeMultiInstance(ramp + '.colorEntryList[1]', b=True)

    mc.connectAttr(sampler + '.facingRatio', ramp + '.uCoord', f=True)
    mc.connectAttr(sampler + '.facingRatio', ramp + '.vCoord', f=True)
    mc.connectAttr(ramp + '.outColor', fsl + '.outColor', f=True)
    mc.setAttr(ramp + ".colorEntryList[0].position", 0)
    mc.setAttr(ramp + ".colorEntryList[2].position", 1)
    return sg


def shadowShader(projShotName):
    shadow = mc.shadingNode('useBackground', asShader=True, name=projShotName + '_shadow')
    mc.setAttr(shadow + '.specularColor', 0, 0, 0, type='double3')
    mc.setAttr(shadow + '.reflectivity', 0)
    mc.setAttr(shadow + '.reflectionLimit', 0)
    mc.setAttr(shadow + '.shadowMask', 1)
    sg = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=projShotName + '_shadowSG')
    mc.connectAttr(shadow + '.outColor', sg + '.surfaceShader', f=True)
    return sg


def occShader(projShotName):
    occ = mc.shadingNode('surfaceShader', asShader=True, name=projShotName + '_occ')
    sg = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=projShotName + '_occSG')
    mc.connectAttr(occ + '.outColor', sg + '.surfaceShader', f=True)
    occlusion = mc.createNode('mib_amb_occlusion', name=projShotName + '_occlusion')
    mc.connectAttr(occlusion + '.outValue', occ + '.outColor', f=True)
    mc.setAttr(occlusion + '.samples', 128)
    mc.setAttr(occlusion + '.max_distance', 10)
    return sg


def normalShader(projShotName):
    nor = mc.shadingNode('surfaceShader', asShader=True, name=projShotName + '_normal')
    sg = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=projShotName + '_normalSG')
    mc.connectAttr(nor + '.outColor', sg + '.surfaceShader', f=True)
    norOcc = mc.createNode('mib_amb_occlusion', name=projShotName + '_norOcclusion')
    mc.connectAttr(norOcc + '.outValue', nor + '.outColor', f=True)
    mc.setAttr(norOcc + '.samples', 128)
    mc.setAttr(norOcc + '.max_distance', 0.0)
    mc.setAttr(norOcc + '.output_mode', 3)
    return sg


def do_assignLambert():
    matShd = 'idmt_IDPass_lambert'
    if mc.objExists('idmt_IDPass_lambert'):
        pass
    else:
        matShd = mc.shadingNode('lambert', asShader=True, name='idmt_IDPass_lambert')

    mesh = ls(type=['mesh', 'nurbsSurface'])
    for m in mesh:
        select(m, r=True)
        mc.hyperShade(assign=matShd)


def zdepthShader(projShotName):
    depth = mc.shadingNode('surfaceShader', asShader=True, name=projShotName + '_depth')
    near = mc.addAttr(depth, ln='nearClipPlane',  at='double',  dv=1)
    mc.setAttr(depth + '.nearClipPlane', e=True, keyable=True)

    far = mc.addAttr(depth, ln='farClipPlane',  at='double',  dv=500)
    mc.setAttr(depth + '.farClipPlane', e=True, keyable=True)

    black = mc.addAttr(depth, ln='black',  at='double',  dv=0)
    mc.setAttr(depth + '.black', e=True, keyable=True)

    white = mc.addAttr(depth, ln='white',  at='double',  dv=1)
    mc.setAttr(depth + '.white', e=True, keyable=True)

    sg = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=projShotName + '_depthSG')
    mc.connectAttr(depth + '.outColor', sg + '.surfaceShader', f=True)
    sampler = mc.createNode('samplerInfo', name=projShotName + '_depSamplerInfo')
    mulDiv = mc.createNode('multiplyDivide', name=projShotName + '_dep_MulDiv')
    mc.setAttr(mulDiv + ".input2X", -1)
    setRange = mc.createNode('setRange', name=projShotName + '_dep_setRange')
    mc.setAttr(setRange + ".oldMinX", 1)
    mc.setAttr(setRange + ".oldMaxX", 500)
    mc.setAttr(setRange + ".minX", 1)
    mc.setAttr(setRange + ".maxX", 0)
    mc.connectAttr(sampler + '.pointCameraZ', mulDiv + '.input1X', f=True)
    mc.connectAttr(mulDiv + '.outputX', setRange + '.valueX', f=True)
    mc.connectAttr(setRange + '.outValueX', depth + '.outColorR', f=True)
    mc.connectAttr(setRange + '.outValueX', depth + '.outColorG', f=True)
    mc.connectAttr(setRange + '.outValueX', depth + '.outColorB', f=True)
    mc.connectAttr(depth + '.white', setRange + '.minX', f=True)
    mc.connectAttr(depth + '.black', setRange + '.maxX', f=True)
    mc.connectAttr(depth + '.nearClipPlane', setRange + '.oldMinX', f=True)
    mc.connectAttr(depth + '.farClipPlane', setRange + '.oldMaxX', f=True)
    return sg


def do_AutoLayerSetIdPass():
    try:
        docp.do_sceneOpenScript()
    except:
        pass
    matShd = matShader('do')
    mc.select(cl=True)
    path = r'//file-cluster/gdc/Projects/DiveollyDive4/DiveollyDive4_Scratch/TD/Rendering/idpass_files/'
    allRef = mc.file(q=True, r=True)
    passName = ''
    selNodes = []
    for rr in allRef:
        fn = os.path.basename(rr).split('.')[0]
        idPassFn = path + fn + '.xml'
        if os.path.isfile(idPassFn):
            refObjNode = mc.referenceQuery(rr, rfn=True, tr=True)
            nodes = referenceQuery(refObjNode, n=True, dagPath=True)
            for node in nodes:
                bbox = xform(node, q=True, ws=True, bb=True)
                if bbox[0] or bbox[1] or bbox[2]:
                    selNodes.append(node)
                    break

    idpass_names = ['Idp01', 'Idp02', 'Idp03']
    for idp in idpass_names:
        idpassLay = idp
        if not mc.objExists(idpassLay):
            idpassLay = mc.createRenderLayer(selNodes, name=idp, number=1, noRecurse=True)
        mc.editRenderLayerGlobals(currentRenderLayer=idpassLay)
        mc.select(selNodes, r=True)
        mc.hyperShade(assign=matShd)
        mc.hyperShade(assign=matShd)
        for rr in allRef:
            fn = os.path.basename(rr).split('.')[0]
            idPassFn = path + fn + '.xml'
            ns = mc.file(rr, q=True, ns=True)
            if os.path.isfile(idPassFn):
                """
                    refObjNode =  mc.referenceQuery(rr, rfn = True, tr = True)
                    refObjTmp = mc.listConnections(refObjNode, s = False, d = True, type = 'transform')
                    refObj = ''

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
    do_eye_ipd_autoLayer()


def do_setLightsOff():
    lights = ls(type='light')
    for l in lights:
        mc.setAttr(l.getParent().root() + '.visibility', False)


def do_find_displacementNode(mat):

    se = mc.listConnections(mat + '.message', s=False, d=True, type='shadingEngine')

    if se:
        displacement = mc.listConnections(se[0] + '.displacementShader', s=True, d=False, type='displacementShader')

        if displacement:

            mc.hyperShade(objects=mat)
            objs = mc.ls(sl=True)

            objName = ''
            for obj in objs:
                objName = objName + obj + '&'

            locator = mc.spaceLocator(name='do___displacement___#')

            mc.addAttr(locator[0], ln="displacementNode", dt="string")
            mc.setAttr(locator[0] + '.displacementNode', displacement[0], type="string")

            mc.addAttr(locator[0], ln="objects", dt="string")
            mc.setAttr(locator[0] + '.objects', objName, type="string")


def do_displacement_assign(type, displacement_locator):

    for loc in displacement_locator:

        dispNode = mc.getAttr(loc + '.displacementNode')
        objsName = mc.getAttr(loc + '.objects')
        objs = objsName.split('&')
        sg = ''

        if type == 'Fsl':
            sg = fresnelShader('do')

        if type == 'Shw':
            sg = shadowShader('do')

        if type == 'Occ':
            sg = occShader('do')

        if type == 'Nor':
            sg = normalShader('do')

        if type == 'Zdp':
            sg = zdepthShader('do')

        if type == 'Cao':
            sg = occShader('do')
        if type == 'Key':
            key = mc.shadingNode('lambert', asShader=True, name='do_key_displacement')
        sg = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name='do_key_SG')
        mc.connectAttr(key + '.color', sg + '.surfaceShader', f=True)
        setAttr(key + '.color', 1, 1, 1, type='double3')

        mc.connectAttr(dispNode + '.displacement', sg + '.displacementShader', f=True)

        mat = mc.listConnections(sg + '.surfaceShader', s=True)

        for obj in objs:
            if obj != '':
                mc.select(obj, r=True)
                mc.hyperShade(assign=mat[0])


def do_setReflective(mat, val):
    try:
        select(mat, r=True)
        objs = ls(sl=True)

        if (objs):
            editRenderLayerAdjustment(objs[0] + '.reflectivity')
            attrCon = listConnections(objs[0] + '.reflectivity', d=False, s=True, p=True)
            if attrCon:
                try:
                    disconnectAttr(attrCon[0], objs[0] + '.reflectivity')
                except:
                    pass
            setAttr(objs[0] + '.reflectivity', val)
    except:
        pass


def do_batchSetReflective():
    do_setReflective('*:vicky_vicky_vicky_hair_mia_material_x2', 0.3)
    do_setReflective('*:apple_eaten_apple_SHD2', 0.0)
    do_setReflective('*:halvaOrg_eyeCover_SHD2', 0.0)
    do_setReflective('*:svenOrig_helmetB_SHD2', 0.15)
    do_setReflective('*:svenOrig_helmetA_SHD2', 0.15)
    do_setReflective('*:svenOrig_belts_SHD2', 0.15)
    do_setReflective('*:svenOrig_buckleBolts_SHD2', 0.15)
    do_setReflective('*:svenOrig_bracelette_SHD3', 0.15)


def do_fixSpec():
    layers = ls(type='renderLayer')
    FD = False
    for layer in layers:
        if re.compile('(_AMB$|_SPEC$)', re.IGNORECASE).search(layer.name()):
            editRenderLayerGlobals(currentRenderLayer=layer)
            # do_batchSetReflective()
            do_setReflective('*:svenOrig_helmetB_SHD2', 0.15)
            do_setReflective('*:svenOrig_helmetA_SHD2', 0.15)
            do_setReflective('*:svenOrig_belts_SHD2', 0.15)
            do_setReflective('*:svenOrig_buckleBolts_SHD2', 0.15)
            do_setReflective('*:svenOrig_bracelette_SHD3', 0.15)
            FD = True

    if not FD:
        confirmDialog(title='Confirm', message=u'没有找到AMB或者SPEC层', button=['Ok'], defaultButton='Ok')


def do_autoLayer(method='A'):
    try:
        docp.do_sceneOpenScript()
    except:
        pass
    sn = mc.file(sceneName=True, q=True, shortName=True)

    prefix = ''
    layList = ['Clr', 'Occ', 'Shw', 'Nor', 'Zdp', 'Fsl', 'Idp', 'Cao', 'Arn']
    layNameForSep = ''
    layerNames = sn.split('_')
    for i in layerNames:
        for ll in layList:
            if i.find(ll) > -1:
                layNameForSep = layNameForSep + ll
        if layNameForSep:
            prefix = i.split(layNameForSep)[0]
            break

    select(cl=True)
    mats = ls(materials=True)

    for mat in mats:
        do_find_displacementNode(mat)
    displacement_locator = ls('do___displacement___*', type='transform')
    if sn.find('Clr') > -1 or displacement_locator:
        pass
#===============================================================================
    else:
        if not sn.find('Char') > -1 and not sn.find('Idp') > -1 and not sn.find(u'Arn') > -1:
            mel.eval('source "zzjUtilityTools.mel";lighting_DeleteUnusedNode()')
        try:
            mc.setAttr('miDefaultOptions.finalGather', False)
        except:
            pass
    if displacement_locator:
        if sn.find('Clr') > -1:
            mel.eval('SelectAll')
            sel = mc.ls(sl=True)
            layer = mc.createRenderLayer(sel, name=prefix + 'Clr', number=1, noRecurse=True)
        if sn.find('Zdp') > -1:
            mel.eval('SelectAll')
            sel = mc.ls(sl=True)
            layer = mc.createRenderLayer(sel, name=prefix + 'Zdp', number=1, noRecurse=True)
            mc.editRenderLayerGlobals(currentRenderLayer=layer)
            sg = zdepthShader('do')

            mat = mc.listConnections(sg + '.surfaceShader', s=True)
            sels = mc.ls(type=['mesh', 'nurbsSurface'])
            for i in sels:
                mc.select(i, r=True)
                mc.hyperShade(assign=mat[0])
            do_displacement_assign('Zdp', displacement_locator)
            mc.setAttr('miDefaultOptions.rayTracing', 0)
            mc.editRenderLayerAdjustment('miDefaultOptions.rayTracing', lyr=layer)
        if sn.find('Occ') > -1:
            mel.eval('SelectAll')
            sel = mc.ls(sl=True)
            layer = mc.createRenderLayer(sel, name=prefix + 'Occ', number=1, noRecurse=True)
            mc.editRenderLayerGlobals(currentRenderLayer=layer)
            sg = occShader('do')
            mat = mc.listConnections(sg + '.surfaceShader', s=True)
            sels = mc.ls(type=['mesh', 'nurbsSurface'])
            for i in sels:
                mc.select(i, r=True)
                mc.hyperShade(assign=mat[0])
            # mel.eval('SelectAll')
            #mc.hyperShade(assign = mat[0])
            # mel.eval('SelectAll')
            #mc.hyperShade(assign = mat[0])
            do_displacement_assign('Occ', displacement_locator)
            mc.setAttr('miDefaultOptions.rayTracing', 1)
            mc.editRenderLayerAdjustment('miDefaultOptions.rayTracing', lyr=layer)

        if sn.find('Cao') > -1:
            mel.eval('SelectAll')
            sel = mc.ls(sl=True)
            layer = mc.createRenderLayer(sel, name=prefix + 'Cao', number=1, noRecurse=True)
            mc.editRenderLayerGlobals(currentRenderLayer=layer)
            sg = occShader('do')
            mat = mc.listConnections(sg + '.surfaceShader', s=True)
            sels = mc.ls(type=['mesh', 'nurbsSurface'])
            for i in sels:
                mc.select(i, r=True)
                mc.hyperShade(assign=mat[0])
            do_displacement_assign('Cao', displacement_locator)
            mc.setAttr('miDefaultOptions.rayTracing', 1)
            mc.editRenderLayerAdjustment('miDefaultOptions.rayTracing', lyr=layer)

        if sn.find('Shw') > -1:
            mel.eval('SelectAll')
            sel = mc.ls(sl=True)
            layer = mc.createRenderLayer(sel, name=prefix + 'Shadow', number=1, noRecurse=True)
            mc.editRenderLayerGlobals(currentRenderLayer=layer)
            sg = shadowShader('do')
            mat = mc.listConnections(sg + '.surfaceShader', s=True)
            sels = mc.ls(type=['mesh', 'nurbsSurface'])
            for i in sels:
                mc.select(i, r=True)
                mc.hyperShade(assign=mat[0])
            do_displacement_assign('Shw', displacement_locator)
            mc.setAttr('miDefaultOptions.rayTracing', 1)
            mc.editRenderLayerAdjustment('miDefaultOptions.rayTracing', lyr=layer)

        if sn.find('Fsl') > -1:
            mel.eval('SelectAll')
            sel = mc.ls(sl=True)
            layer = mc.createRenderLayer(sel, name=prefix + 'Fresnel', number=1, noRecurse=True)
            mc.editRenderLayerGlobals(currentRenderLayer=layer)
            sg = fresnelShader('do')
            mat = mc.listConnections(sg + '.surfaceShader', s=True)
            sels = mc.ls(type=['mesh', 'nurbsSurface'])
            for i in sels:
                mc.select(i, r=True)
                mc.hyperShade(assign=mat[0])
            do_displacement_assign('Fsl', displacement_locator)
            mc.setAttr('miDefaultOptions.rayTracing', 0)
            mc.editRenderLayerAdjustment('miDefaultOptions.rayTracing', lyr=layer)

        if sn.find('Nor') > -1:
            mel.eval('SelectAll')
            sel = mc.ls(sl=True)
            layer = mc.createRenderLayer(sel, name=prefix + 'Normal', number=1, noRecurse=True)
            mc.editRenderLayerGlobals(currentRenderLayer=layer)
            sg = normalShader('do')
            mat = mc.listConnections(sg + '.surfaceShader', s=True)
            sels = mc.ls(type=['mesh', 'nurbsSurface'])

            for i in sels:
                mc.select(i, r=True)
                mc.hyperShade(assign=mat[0])
            do_displacement_assign('Nor', displacement_locator)
            mc.setAttr('miDefaultOptions.rayTracing', 0)
            mc.editRenderLayerAdjustment('miDefaultOptions.rayTracing', lyr=layer)

        if sn.find('Idp') > -1 and prefix == 'Sc':
            mc.select(cl=True)
            mc.createRenderLayer(name=prefix + 'Idp', number=1)
            mc.setAttr('miDefaultOptions.rayTracing', 0)
            mc.editRenderLayerAdjustment('miDefaultOptions.rayTracing', lyr=layer)
        elif sn.find('Idp') > -1 and prefix != 'Sc':
            try:
                do_AutoLayerSetIdPass()
            except:
                pass
        if sn.find(u'Cau') > -1:
            create_noColor_RndLayer(u'caustic')
        if sn.find(u'Arn') > -1 and prefix == u'Sc':
            create_noColor_RndLayer(RL_name=u'Arn', imp_rfn=True, style=u'BG', cleanMat=True)
        elif sn.find(u'Arn') > -1 and prefix != u'Sc':
            create_noColor_RndLayer(RL_name=u'Arn', imp_rfn=True, style=u'CHR', cleanMat=True)
        mc.delete(displacement_locator)

    else:
        if sn.find('Clr') > -1:
            mel.eval('SelectAll')
            sel = mc.ls(sl=True)
            layer = mc.createRenderLayer(sel, name=prefix + 'Clr', number=1, noRecurse=True)
        if sn.find('Zdp') > -1:
            mel.eval('SelectAll')
            sel = mc.ls(sl=True)
            layer = mc.createRenderLayer(sel, name=prefix + 'Zdp', number=1, noRecurse=True)
            sg = zdepthShader('do')
            mc.connectAttr(sg + '.message', layer + '.shadingGroupOverride', f=True)
            mc.setAttr('miDefaultOptions.rayTracing', 0)
            mc.editRenderLayerAdjustment('miDefaultOptions.rayTracing', lyr=layer)
        if sn.find('Occ') > -1:
            mel.eval('SelectAll')
            sel = mc.ls(sl=True)
            layer = mc.createRenderLayer(sel, name=prefix + 'Occ', number=1, noRecurse=True)
            sg = occShader('do')
            mc.connectAttr(sg + '.message', layer + '.shadingGroupOverride', f=True)
            mc.setAttr('miDefaultOptions.rayTracing', 1)
            mc.editRenderLayerAdjustment('miDefaultOptions.rayTracing', lyr=layer)

        if sn.find('Cao') > -1:
            mel.eval('SelectAll')
            sel = mc.ls(sl=True)
            layer = mc.createRenderLayer(sel, name=prefix + 'Cao', number=1, noRecurse=True)
            sg = occShader('do')
            mc.connectAttr(sg + '.message', layer + '.shadingGroupOverride', f=True)
            mc.setAttr('miDefaultOptions.rayTracing', 1)
            mc.editRenderLayerAdjustment('miDefaultOptions.rayTracing', lyr=layer)

        if sn.find('Shw') > -1:
            mel.eval('SelectAll')
            sel = mc.ls(sl=True)
            layer = mc.createRenderLayer(sel, name=prefix + 'Shadow', number=1, noRecurse=True)
            sg = shadowShader('do')
            mc.connectAttr(sg + '.message', layer + '.shadingGroupOverride', f=True)
            mc.setAttr('miDefaultOptions.rayTracing', 1)
            mc.editRenderLayerAdjustment('miDefaultOptions.rayTracing', lyr=layer)

        if sn.find('Fsl') > -1:
            mel.eval('SelectAll')
            sel = mc.ls(sl=True)
            layer = mc.createRenderLayer(sel, name=prefix + 'Fresnel', number=1, noRecurse=True)
            sg = fresnelShader('do')
            mc.connectAttr(sg + '.message', layer + '.shadingGroupOverride', f=True)
            mc.setAttr('miDefaultOptions.rayTracing', 0)
            mc.editRenderLayerAdjustment('miDefaultOptions.rayTracing', lyr=layer)

        if sn.find('Nor') > -1:
            mel.eval('SelectAll')
            sel = mc.ls(sl=True)
            layer = mc.createRenderLayer(sel, name=prefix + 'Normal', number=1, noRecurse=True)
            sg = normalShader('do')
            mc.connectAttr(sg + '.message', layer + '.shadingGroupOverride', f=True)
            mc.setAttr('miDefaultOptions.rayTracing', 0)
            mc.editRenderLayerAdjustment('miDefaultOptions.rayTracing', lyr=layer)

        if sn.find('Idp') > -1 and prefix == 'Sc':
            mc.select(cl=True)
            mc.createRenderLayer(name=prefix + 'Idp', number=1)
            mc.setAttr('miDefaultOptions.rayTracing', 0)
            mc.editRenderLayerAdjustment('miDefaultOptions.rayTracing', lyr=layer)
        elif sn.find('Idp') > -1 and prefix != 'Sc':
            try:
                do_AutoLayerSetIdPass()
            except:
                pass
        if sn.find(u'Cau') > -1:
            create_noColor_RndLayer(u'caustic')
        if sn.find(u'Arn') > -1 and prefix == u'Sc':
            create_noColor_RndLayer(RL_name=u'Arn', imp_rfn=True, style=u'BG', cleanMat=True)
        elif sn.find(u'Arn') > -1 and prefix != u'Sc':
            create_noColor_RndLayer(RL_name=u'Arn', imp_rfn=True, style=u'CHR', cleanMat=True)
    mel.eval('renderLayerEditorRenderable RenderLayerTab "defaultRenderLayer" "0"')
    editRenderLayerGlobals(currentRenderLayer='defaultRenderLayer')
    select(cl=True)
    execfile(ur'\\file-cluster\GDC\Resource\Support\Python\2.6-x64\Lib\site-packages\idmt\maya\DOD\DODIV\Maya\do4_config_rnd_parameter.py')


def setAllGammaValue(value):
    gc = mc.ls(type='gammaCorrect')
    for g in gc:
        mc.setAttr(g + '.gammaX', value)
        mc.setAttr(g + '.gammaY', value)
        mc.setAttr(g + '.gammaZ', value)
    print u'------------------------------------ 所有的 gamma 值都已设置为 ' + str(value) + ' ---------------------------------------',


def setSelPrimaryVisibilityOff():
    allSelShp = mc.ls(sl=True, shapes=True, dag=True)
    if mc.editRenderLayerGlobals(query=True, currentRenderLayer=True) == 'defaultRenderLayer':
        mc.confirmDialog(title='Confirm', message=u'请不要在默认渲染层设置', defaultButton='Yes')
        return
    for ass in allSelShp:
        if mel.eval('attributeExists "primaryVisibility" ' + ass):
            mc.editRenderLayerAdjustment(ass + '.primaryVisibility')
            mc.setAttr(ass + '.primaryVisibility', 0)
    print u'------------------------------------ 所选物体的 primaryVisibility 属性已经关闭 ---------------------------------------',


def do_occWithTrans():
    sn = mc.file(sceneName=True, q=True, shortName=True)
    prefix = ''
    layList = ['Bey', 'Occ', 'Shw', 'Nor', 'Zdp', 'Fsl', 'Idp', 'Cao']
    layNameForSep = ''
    layerNames = sn.split('_')
    for i in layerNames:
        for ll in layList:
            if i.find(ll) > -1:
                layNameForSep = layNameForSep + ll
        if layNameForSep:
            prefix = i.split(layNameForSep)[0]
            break
    mel.eval('SelectAll')
    sel = mc.ls(sl=True)
    layer = mc.createRenderLayer(sel, name=prefix + 'Occ', number=1, noRecurse=True)
    mc.editRenderLayerGlobals(currentRenderLayer=layer)

    mc.editRenderLayerAdjustment('miDefaultOptions.rayTracing', lyr=layer)
    mc.setAttr('miDefaultOptions.rayTracing', 1)

    mc.editRenderLayerAdjustment('miDefaultOptions.maxReflectionRays', lyr=layer)
    mc.setAttr('miDefaultOptions.maxReflectionRays', 5)

    mc.editRenderLayerAdjustment('miDefaultOptions.maxRefractionRays', lyr=layer)
    mc.setAttr('miDefaultOptions.maxRefractionRays', 5)
    mc.editRenderLayerAdjustment('miDefaultOptions.maxRayDepth', lyr=layer)
    mc.setAttr('miDefaultOptions.maxRayDepth', 10)
    mc.editRenderLayerAdjustment('miDefaultOptions.finalGather', lyr=layer)
    mc.setAttr('miDefaultOptions.finalGather', 1)

    mc.editRenderLayerAdjustment('miDefaultOptions.finalGatherRays', lyr=layer)
    mc.editRenderLayerAdjustment('miDefaultOptions.finalGatherPresampleDensity', lyr=layer)

    mats = mc.ls(materials=True)

    allOccShades = []

    fg = ''

    for mat in mats:
        attr = mc.listAttr(mat, st='*opacity')

        if attr:
            for a in attr:
                connects = mc.listConnections(mat + '.' + a, s=True)

                if connects:
                    mc.hyperShade(objects=mat)
                    objs = mc.ls(sl=True)

                    mc.editRenderLayerAdjustment(connects[0] + '.invert', lyr=layer)
                    mc.editRenderLayerAdjustment(connects[0] + '.filterType', lyr=layer)
                    mc.setAttr(connects[0] + '.invert', 0)
                    mc.setAttr(connects[0] + '.filterType', 0)
                    projShotName = 'do'

                    occ = mc.shadingNode('lambert', asShader=True, name=projShotName + '_occ_trans')
                    sg = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=projShotName + '_occSG')
                    mc.connectAttr(occ + '.outColor', sg + '.surfaceShader', f=True)
                    mc.setAttr(sg + '.miExportShadingEngine', 0)

                    objName = ''

                    for obj in objs:
                        print obj
                        objName += obj + '|'
                    print objName
                    mc.addAttr(occ, ln="objects", dt="string")
                    mc.setAttr(occ + '.objects', e=True, keyable=True)

                    mc.setAttr(occ + '.objects', objName, type="string")

                    if not fg:
                        fg = mc.createNode('mib_fg_occlusion', name='_fg')
                    ct = mc.createNode('mib_opacity', name='_ct')

                    mc.connectAttr(fg + '.outValueA', ct + '.inputA')
                    mc.connectAttr(fg + '.outValue', ct + '.input')

                    mc.connectAttr(connects[0] + '.outAlpha', ct + '.opacityA')
                    mc.connectAttr(connects[0] + '.outColor', ct + '.opacity')

                    mc.connectAttr(ct + '.outValue', sg + '.miMaterialShader')

                    allOccShades.append(occ)

    if allOccShades:
        occLambert = mc.shadingNode('lambert', asShader=True, name=projShotName + '_occ_lambert')
        sgLambert = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=projShotName + '_occ_lambertSG')
        mc.connectAttr(occLambert + '.outColor', sgLambert + '.surfaceShader', f=True)
        mc.connectAttr(fg + '.outValue', sgLambert + '.miMaterialShader')
        mc.setAttr(sgLambert + '.miExportShadingEngine', 0)
        mel.eval('SelectAll')
        mc.hyperShade(a=occLambert)

        for sh in allOccShades:
            attrVal = mc.getAttr(sh + '.objects')
            objs = attrVal.split('|')

            for obj in objs:
                if obj != '':
                    s = mc.pickWalk(obj, direction='up')
                    if s:
                        mc.select(s[0], r=True)
                        mc.hyperShade(a=sh)

        mc.editRenderLayerGlobals(currentRenderLayer='defaultRenderLayer')


def do_AutoLayerSetIdPassWithMouth():
    matShd = matShader('do')
    mc.select(cl=True)
    path = r'//file-cluster/gdc/Projects/DiveollyDive4/DiveollyDive4_Scratch/TD/Rendering/idpass_files/'
    allRef = mc.file(q=True, r=True)
    for rr in allRef:
        fn = os.path.basename(rr).split('.')[0]
        idPassFn = path + fn + '.xml'
        if os.path.isfile(idPassFn):
            refObjNode = mc.referenceQuery(rr, rfn=True, tr=True)
            refObj = mc.listConnections(refObjNode, s=False, d=True, type='transform')[0]
            rgbs = []
            root = ET.parse(path + fn + ".xml")
            ipassNode = root.find('idPass')
            for c in ipassNode.getchildren():
                if c.tag.capitalize() == 'Mrgb':
                    idpassLay = mc.createRenderLayer(refObj, name=fn.split('-')[0] + c.tag.capitalize(), number=1, noRecurse=True)
                    mc.setAttr('miDefaultOptions.rayTracing', 0)
                    mc.editRenderLayerAdjustment('miDefaultOptions.rayTracing', lyr=idpassLay)
                    mc.editRenderLayerGlobals(currentRenderLayer=idpassLay)
                    mc.select(refObj, r=True)
                    mc.hyperShade(assign=matShd)
                    mc.hyperShade(assign=matShd)
                    ns = mc.file(rr, q=True, ns=True)
                    setIdPass(path, fn, ns, c)


def do_create_occ_nor():

    if mc.window('trans_MainWin', exists=True):
        mc.deleteUI('trans_MainWin')

    mc.window('trans_MainWin', title=u'VickyTheViking -- Create Layers With Transparency Map', width=460, height=180, sizeable=False)
    mc.columnLayout(rowSpacing=2, columnAttach=['both', 5], columnWidth=460)

    mc.checkBoxGrp('transLayer', label=u'Layers：', labelArray3=['Occ', 'Nor', 'Zdp'], valueArray3=[True, True, True], numberOfCheckBoxes=3)

    mc.separator(height=10, style='out')
    mc.button(label='          Create Layers', backgroundColor=[0.44, 0.67, .9], c='do_create_occ_nor_proc()')
    mc.text(label='         ')
    mc.showWindow('trans_MainWin')


def do_create_occ_nor_proc():

    if not mc.checkBoxGrp('transLayer', q=True, v1=True) and not mc.checkBoxGrp('transLayer', q=True, v2=True) and not mc.checkBoxGrp('transLayer', q=True, v3=True):
        mc.confirmDialog(title='Confirm', message=u'哎呀，似乎你没有选择需要创建的层！！！！', defaultButton='Yes')
        return

    do_create_locator_occ_nor()

    mel.eval('source "zzjUtilityTools.mel";lighting_DeleteUnusedNode()')
    if mc.checkBoxGrp('transLayer', q=True, v1=True):
        do_occ_nor('Occ')

    if mc.checkBoxGrp('transLayer', q=True, v2=True):
        do_occ_nor('Nor')

    if mc.checkBoxGrp('transLayer', q=True, v3=True):
        do_occ_nor('Zdp')

    #locatorNodes = mc.ls('do___occ___nor___*', type = 'transform')
    # mc.delete(locatorNodes)


def do_occ_nor(type):

    mel.eval('SelectAll')
    sel = mc.ls(sl=True)
    layer = mc.createRenderLayer(sel, name='Sc' + type, number=1, noRecurse=True)
    mc.editRenderLayerGlobals(currentRenderLayer=layer)

    mc.editRenderLayerAdjustment('miDefaultOptions.rayTracing', lyr=layer)

    mc.editRenderLayerAdjustment('miDefaultOptions.maxReflectionRays', lyr=layer)

    mc.editRenderLayerAdjustment('miDefaultOptions.maxRefractionRays', lyr=layer)

    mc.editRenderLayerAdjustment('miDefaultOptions.maxRayDepth', lyr=layer)

    mc.editRenderLayerAdjustment('miDefaultOptions.finalGather', lyr=layer)

    mc.editRenderLayerAdjustment('miDefaultOptions.finalGatherRays', lyr=layer)
    mc.editRenderLayerAdjustment('miDefaultOptions.finalGatherPresampleDensity', lyr=layer)

    mc.setAttr('miDefaultOptions.rayTracing', 1)
    mc.setAttr('miDefaultOptions.maxRayDepth', 10)
    mc.setAttr('miDefaultOptions.maxRefractionRays', 10)
    mc.setAttr('miDefaultOptions.maxReflectionRays', 0)

    projShotName = 'do'

    fg = ''

    if type == 'Occ':

        mc.setAttr('miDefaultOptions.finalGather', 1)
        mc.setAttr("miDefaultOptions.finalGatherRays", 300)

        mc.editRenderLayerAdjustment('miDefaultOptions.finalGatherFalloffStop', lyr=layer)
        mc.setAttr('miDefaultOptions.finalGatherFalloffStop', 50)

        fg = mc.createNode('mib_fg_occlusion', name='_fg')
    elif type == 'Nor':

        mc.setAttr('miDefaultOptions.finalGather', 0)
        mc.setAttr("miDefaultOptions.finalGatherRays", 100)

        fg = mc.createNode('mib_amb_occlusion', name='_norOcclusion')
        mc.setAttr(fg + '.samples', 32)
        mc.setAttr(fg + '.max_distance', 3.0)
        mc.setAttr(fg + '.output_mode', 3)
    else:

        mc.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer', lyr=layer)
        mc.setAttr('defaultRenderGlobals.currentRenderer', 'mayaSoftware', type='string')

        mc.setAttr('defaultRenderQuality.edgeAntiAliasing', 0)
        mc.setAttr('defaultRenderQuality.useMultiPixelFilter', 1)
        mc.setAttr('defaultRenderQuality.shadingSamples', 2)
        mc.setAttr('defaultRenderQuality.maxShadingSamples', 8)
        mc.setAttr('defaultRenderQuality.visibilitySamples', 1)
        mc.setAttr('defaultRenderQuality.maxVisibilitySamples', 4)
        mc.setAttr('defaultRenderQuality.redThreshold', 0.4)
        mc.setAttr('defaultRenderQuality.greenThreshold', 0.3)
        mc.setAttr('defaultRenderQuality.blueThreshold', 0.6)

        """
        mc.setAttr( 'miDefaultOptions.rayTracing', 0)
        mc.setAttr('miDefaultOptions.maxRayDepth', 2)
        mc.setAttr( 'miDefaultOptions.maxRefractionRays', 1)
        mc.setAttr( 'miDefaultOptions.maxReflectionRays', 1) 
        
        mc.setAttr('miDefaultOptions.finalGather', 0)
        """

        loc = mc.spaceLocator(name='do___zdepth___ctrl__#')
        fg = loc[0]
        mc.addAttr(fg, ln='nearClipPlane',  at='double',  dv=1)
        mc.setAttr(fg + '.nearClipPlane', e=True, keyable=True)
        mc.addAttr(fg, ln='farClipPlane',  at='double',  dv=13000)
        mc.setAttr(fg + '.farClipPlane', e=True, keyable=True)
        mc.addAttr(fg, ln='black',  at='double',  dv=0)
        mc.setAttr(fg + '.black', e=True, keyable=True)

        mc.addAttr(fg, ln='white',  at='double',  dv=1)
        mc.setAttr(fg + '.white', e=True, keyable=True)

        mc.setAttr(fg + '.v', 0)
        mc.setAttr(fg + '.tx', lock=True, keyable=False, channelBox=False)
        mc.setAttr(fg + '.ty', lock=True, keyable=False, channelBox=False)
        mc.setAttr(fg + '.tz', lock=True, keyable=False, channelBox=False)
        mc.setAttr(fg + '.rx', lock=True, keyable=False, channelBox=False)
        mc.setAttr(fg + '.ry', lock=True, keyable=False, channelBox=False)
        mc.setAttr(fg + '.rz', lock=True, keyable=False, channelBox=False)
        mc.setAttr(fg + '.sx', lock=True, keyable=False, channelBox=False)
        mc.setAttr(fg + '.sy', lock=True, keyable=False, channelBox=False)
        mc.setAttr(fg + '.sz', lock=True, keyable=False, channelBox=False)
        mc.setAttr(fg + '.v', lock=True, keyable=False, channelBox=False)

        #mc.lockNode( fg, lock = True )

    allShdae = ''

    if type == 'Zdp':
        allShdae = createDepthNetwork(projShotName, fg, layer, '')
    else:
        allShdae = mc.shadingNode('lambert', asShader=True, name=projShotName + '_' + type + '_lambert')
        sgLambert = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=projShotName + '_' + type + '_lambertSG')
        mc.connectAttr(allShdae + '.outColor', sgLambert + '.surfaceShader', f=True)
        mc.connectAttr(fg + '.outValue', sgLambert + '.miMaterialShader')
        mc.setAttr(sgLambert + '.miExportShadingEngine', 0)

    mel.eval('SelectAll')
    mc.hyperShade(a=allShdae)

    locatorNodes = mc.ls('do___occ___nor___*', type='transform')

    for loc in locatorNodes:

        filePath = mc.getAttr(loc + '.fileNode')
        objsName = mc.getAttr(loc + '.objects')
        objs = objsName.split('&')
        sgNode = ''
        if type == 'Zdp':
            sgNode = createDepthNetwork(projShotName, fg, layer, filePath)
        else:
            sgNode = createOpaOccNetwork(projShotName, fg, layer, filePath)

        for obj in objs:
            if obj != '':
                mc.select(obj, r=True)
                mc.hyperShade(a=sgNode)

    try:
        mc.setAttr("defaultRenderLayer.renderable", 0)
    except:
        print 'hello world!'


def do_china_great_wall_rgb_node(projShotName, color):
    do_create_locator_occ_nor()
    filePath = ''
    sels = mc.ls(sl=True)

    locators = mc.ls('do___occ___nor___*', type='transform')

    for sel in sels:
        for locator in locators:
            objs = mc.getAttr(locator + '.objects')
            if sel in objs:
                filePath = mc.getAttr(locator + '.fileNode')

        lamb = mc.shadingNode('lambert', asShader=True, name=projShotName + '_rgb_' + '_' + color)
        sg = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=projShotName + '_rgb_' + '_' + color + 'SG')
        mc.connectAttr(lamb + '.outColor', sg + '.surfaceShader', f=True)
        mc.setAttr(lamb + '.diffuse', 1)

        if color == 'r':
            mc.setAttr(lamb + '.color', 1, 0, 0, type='double3')
            mc.setAttr(lamb + '.ambientColor', 1, 0, 0, type='double3')

        if color == 'g':
            mc.setAttr(lamb + '.color', 0, 1, 0, type='double3')
            mc.setAttr(lamb + '.ambientColor', 0, 1, 0, type='double3')

        if color == 'b':
            mc.setAttr(lamb + '.color', 0, 0, 1, type='double3')
            mc.setAttr(lamb + '.ambientColor', 0, 0, 1, type='double3')

        mc.setAttr(lamb + '.matteOpacity', 0)

        if color == 'a':
            mc.setAttr(lamb + '.color', 0, 0, 0, type='double3')
            mc.setAttr(lamb + '.ambientColor', 0, 0, 0, type='double3')
            mc.setAttr(lamb + '.diffuse', 0)
            mc.setAttr(lamb + '.matteOpacity', 1)

        if filePath:
            fileNode = mel.eval('createRenderNodeCB -as2DTexture "" file ""')
            mc.setAttr(fileNode + '.invert', 0)
            mc.setAttr(fileNode + '.filterType', 0)
            mc.setAttr(fileNode + '.fileTextureName', filePath, type='string')

            mc.connectAttr(fileNode + '.outTransparency', lamb + '.transparency', f=True)

        mc.select(sel, r=True)
        mc.hyperShade(assign=lamb)


def do_create_locator_occ_nor():
    if not mc.objExists('do_transparency_locator_Grp'):
        mc.group(em=True, name='do_transparency_locator_Grp')
    else:
        return

    mats = mc.ls(materials=True)
    for mat in mats:
        if not do_find_fileNode(mat, 'transparency'):
            do_find_fileNode(mat, 'cutout_opacity')


def do_find_fileNode(mat, attr):

    if mc.objExists(mat + '.' + attr):
        fnode = ''
        fnodes = mc.listConnections(mat + '.' + attr, s=True, d=False)

        if fnodes and mc.objectType(fnodes[0]) == 'file':
            fnode = fnodes[0]
        """
        elif fnodes and mc.objectType(fnodes[0]) != 'file':
            fnodes = mc.listConnections(fnodes[0], s = True, d = False)
            for f in fnodes:
                if mc.objectType(f) == 'file':
                    fnode = f
                    break
        """

        if fnode:
            mc.hyperShade(objects=mat)
            objs = mc.ls(sl=True)

            objName = ''
            for obj in objs:
                objName = objName + obj + '&'

            locator = mc.spaceLocator(name='do___occ___nor___#')
            mc.parent(locator[0], 'do_transparency_locator_Grp')
            filePath = mc.getAttr(fnode + '.fileTextureName')
            print filePath

            mc.addAttr(locator[0], ln="fileNode", dt="string")
            mc.setAttr(locator[0] + '.fileNode', filePath, type="string")

            mc.addAttr(locator[0], ln="objects", dt="string")
            mc.setAttr(locator[0] + '.objects', objName, type="string")
            return True

    return False


def createOpaOccNetwork(lambName, fg, layer, filePath):
    fileNode = mel.eval('createRenderNodeCB -as2DTexture "" file ""')
    mc.editRenderLayerAdjustment(fileNode + '.invert', lyr=layer)
    mc.editRenderLayerAdjustment(fileNode + '.filterType', lyr=layer)
    mc.setAttr(fileNode + '.invert', 0)
    mc.setAttr(fileNode + '.filterType', 0)
    mc.setAttr(fileNode + '.fileTextureName', filePath, type='string')

    ct = mc.createNode('mib_opacity', name='_ct')

    mc.connectAttr(fileNode + '.outAlpha', ct + '.opacityR')
    mc.connectAttr(fileNode + '.outAlpha', ct + '.opacityG')
    mc.connectAttr(fileNode + '.outAlpha', ct + '.opacityB')

    occAll = mc.shadingNode('lambert', asShader=True, name=lambName)
    sgAll = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=lambName + 'SG')
    mc.connectAttr(occAll + '.outColor', sgAll + '.surfaceShader', f=True)
    mc.setAttr(sgAll + '.miExportShadingEngine', 0)

    mc.connectAttr(fg + '.outValueA', ct + '.inputA')
    mc.connectAttr(fg + '.outValue', ct + '.input')
    mc.connectAttr(ct + '.outValue', sgAll + '.miMaterialShader')

    return occAll


def createDepthNetwork(projShotName, locator, layer, filePath):
    depth = mc.shadingNode('lambert', asShader=True, name=projShotName + '_depth')
    mc.setAttr(depth + '.diffuse', 0)
    mc.setAttr(depth + '.ambientColor', 1, 1, 1, type='double3')

    if filePath:
        fileNode = mel.eval('createRenderNodeCB -as2DTexture "" file ""')
        mc.setAttr(fileNode + '.invert', 0)
        mc.setAttr(fileNode + '.filterType', 0)
        mc.setAttr(fileNode + '.fileTextureName', filePath, type='string')
        mc.connectAttr(fileNode + '.outTransparency', depth + '.transparency', force=True)

    sg = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=projShotName + '_depthSG')
    mc.connectAttr(depth + '.outColor', sg + '.surfaceShader', f=True)
    sampler = mc.createNode('samplerInfo', name=projShotName + '_depSamplerInfo')
    mulDiv = mc.createNode('multiplyDivide', name=projShotName + '_dep_MulDiv')
    mc.setAttr(mulDiv + ".input2X", -1)
    setRange = mc.createNode('setRange', name=projShotName + '_dep_setRange')
    mc.setAttr(setRange + ".oldMinX", 1)
    mc.setAttr(setRange + ".oldMaxX", 500)
    mc.setAttr(setRange + ".minX", 1)
    mc.setAttr(setRange + ".maxX", 0)
    mc.connectAttr(sampler + '.pointCameraZ', mulDiv + '.input1X', f=True)
    mc.connectAttr(mulDiv + '.outputX', setRange + '.valueX', f=True)
    mc.connectAttr(setRange + '.outValueX', depth + '.colorR', f=True)
    mc.connectAttr(setRange + '.outValueX', depth + '.colorG', f=True)
    mc.connectAttr(setRange + '.outValueX', depth + '.colorB', f=True)
    mc.connectAttr(locator + '.white', setRange + '.minX', f=True)
    mc.connectAttr(locator + '.black', setRange + '.maxX', f=True)
    mc.connectAttr(locator + '.nearClipPlane', setRange + '.oldMinX', f=True)
    mc.connectAttr(locator + '.farClipPlane', setRange + '.oldMaxX', f=True)
    return sg


def do_rgb_node(projShotName, type):

    selObjShape = []

    sels = ls(sl=True)

    for sel in sels:
        shape = ''
        try:
            shape = sel.getShape()
        except:
            pass

        if shape != '':
            if objectType(shape) == 'mesh' or objectType(shape) == 'nurbsSurface':
                selObjShape.append(shape)

    selObjShape = list(set(selObjShape))

    lamb = projShotName + '_rgba_' + '_' + type

    if not mc.objExists(projShotName + '_rgba_' + '_' + type):

        if type == 'matte' or type == 'lamb':
            lamb = mc.shadingNode('lambert', asShader=True, name=projShotName + '_rgba_' + '_' + type)
            sg = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=projShotName + '_rgba_' + '_' + type + 'SG')
            mc.connectAttr(lamb + '.outColor', sg + '.surfaceShader', f=True)
            if type == 'matte':
                mc.setAttr(lamb + '.color', 0, 0, 0, type='double3')
                mc.setAttr(lamb + '.matteOpacityMode', 0)

        else:
            lamb = mc.shadingNode('surfaceShader', asShader=True, name=projShotName + '_rgba_' + '_' + type)
            sg = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=projShotName + '_rgba_' + '_' + type + 'SG')
            mc.connectAttr(lamb + '.outColor', sg + '.surfaceShader', f=True)
            mc.setAttr(lamb + '.outMatteOpacity', 0, 0, 0, type='double3')

            if type == 'r':
                mc.setAttr(lamb + '.outColor', 1, 0, 0, type='double3')

            if type == 'g':
                mc.setAttr(lamb + '.outColor', 0, 1, 0, type='double3')

            if type == 'b':
                mc.setAttr(lamb + '.outColor', 0, 0, 1, type='double3')

            if type == 'a':
                mc.setAttr(lamb + '.outMatteOpacity', 1, 1, 1, type='double3')

    for m in selObjShape:
        select(m, r=True)
        mc.hyperShade(assign=lamb)
    select(cl=True)


def do_eye_ipd_autoLayer():
    faceCtrs = mc.ls(u'*:Facial_CTRL_FRAME')
    for each_FC in faceCtrs:
        if mc.listAttr(each_FC, st=u'eyeBall_TX'):
            mc.setAttr(u'%s.eyeBall_TX' % each_FC, 1)

    p_eye_4 = re.compile(u'_eye_[RL]4_')
    p_eye_3 = re.compile(u'_eye_[RL]3_')
    p_eye_2 = re.compile(u'_eye_[RL]2_')
    p_eye_1 = re.compile(u'_eye_[RL]1_')

    primaryObj_generator = (d for d in mc.ls(typ=[u'mesh', u'nurbsSurface'], ni=True, l=True) if mc.getAttr("%s.primaryVisibility" % d) and (docp.nodeIsVisible(d)) and (d.find(u'do4_c') != -1))
    bodyObjs = []
    eyesObjs = {'e1': [], 'e2': [], 'e3': [], 'e4': []}
    for ec_pri in primaryObj_generator:
    #    p_eye = re.compile(u'_eye[0-9]*_')
        if p_eye_1.search(ec_pri.split(u'|')[-1]):
            eyesObjs['e1'].append(ec_pri)
        elif p_eye_2.search(ec_pri.split(u'|')[-1]):
            eyesObjs['e2'].append(ec_pri)
        elif p_eye_3.search(ec_pri.split(u'|')[-1]):
            eyesObjs['e3'].append(ec_pri)
        elif p_eye_4.search(ec_pri.split(u'|')[-1]):
            eyesObjs['e4'].append(ec_pri)
        else:
            bodyObjs.append(ec_pri)

    RndLay_name = u'Idp04'
    asign_obj_shader_to_RndLayer(eyesObjs[u'e1'], RndLay_name)
    asign_obj_shader_to_RndLayer(eyesObjs[u'e2'], RndLay_name, rgbShader(u'do', u'b'))
    asign_obj_shader_to_RndLayer(eyesObjs[u'e3'], RndLay_name, rgbShader(u'do', u'a'))
    asign_obj_shader_to_RndLayer(bodyObjs, RndLay_name, matShader(u'do'))


def create_noColor_RndLayer(RL_name=u'caustic', imp_rfn=True, lmbMat_name="lambert_WHO", style=u'CHR', cleanMat=False):
    allRNIterator = docp.list_valid_referenceNodes()
    for eachRN in allRNIterator:
        if not mc.referenceQuery(eachRN, isLoaded=True):
            rf_file = mc.referenceQuery(eachRN, f=True)
            mc.file(rf_file, lr=eachRN)
        if imp_rfn:
            mc.file(ir=True, rfn=eachRN)
    allMeshes_all = (d for d in mc.ls(typ=u'mesh', l=True) if not mc.referenceQuery(d, inr=True))
    allMesheShapes_nrf = (d for d in mc.ls(typ=u'mesh', ni=True, l=True) if mc.getAttr(
        "%s.primaryVisibility" % d) and (docp.nodeIsVisible(d)) and check_mesh_validity(d) and not mc.referenceQuery(d, inr=True))
    allMesheShapes_rf = (d for d in mc.ls(typ='mesh', ni=True, l=True) if mc.getAttr(
        "%s.primaryVisibility" % d) and (docp.nodeIsVisible(d)) and check_mesh_validity(d) and mc.referenceQuery(d, inr=True))
    allMeshes_nrf = []
    allMeshes_rf = []
    allMesheShapes_nrf_ls = []
    allMeshes_rf_ls = []
    for each_msh in allMesheShapes_nrf:
        allMesheShapes_nrf_ls.append(each_msh)
        allMeshes_nrf.append(mc.listRelatives(each_msh, parent=True, f=True, type=u'transform')[0])
    for each_msh_rf in allMesheShapes_rf:
        allMeshes_rf_ls.append(each_msh_rf)
        allMeshes_rf.append(mc.listRelatives(each_msh_rf, parent=True, f=True, type=u'transform')[0])
    lamShd = lmbMat_name
    lamSG = u'%sSG' % lamShd
    create_spec_MAT(lamShd)
    for objShape in allMeshes_all:
        disconnect_shape_sg(objShape, lamSG)
    allMeshes_nrf.extend(allMeshes_rf)
    if RL_name == u'caustic':
        LightPath = r"\\file-cluster\GDC\Projects\DiveollyDive4\DiveollyDive4_Scratch\Render\lights\caustic\caustic_light.mb"
        mc.file(LightPath, i=True, type=u'mayaBinary', ra=True, namespace="%s_Light" % (RL_name), options="v=0", loadReferenceDepth="all")
        im_light = mc.ls("%s_Light*:*" % (RL_name), type="transform")[0]
        allMeshes_nrf.append(im_light)
        if imp_rfn:
            asign_obj_shader_to_RndLayer(allMeshes_nrf, RL_name)
        else:
            asign_obj_shader_to_RndLayer(allMeshes_nrf, RL_name, lamShd)
        mc.setAttr('defaultRenderLayer.renderable', 0)
    elif RL_name == u'fringe':
        LightPath = r"\\file-cluster\GDC\Projects\DiveollyDive4\DiveollyDive4_Scratch\Render\lights\edge light\caustic_light.mb"
        mc.file(LightPath, i=True, type=u'mayaBinary', ra=True, namespace="%s_Light" % (RL_name), options="v=0", loadReferenceDepth="all")
        im_light = mc.ls("%s_Light*:*" % (RL_name), type="transform")[0]
        allMeshes_nrf.append(im_light)
        if imp_rfn:
            asign_obj_shader_to_RndLayer(allMeshes_nrf, RL_name)
        else:
            asign_obj_shader_to_RndLayer(allMeshes_nrf, RL_name, lamShd)
        mc.setAttr('defaultRenderLayer.renderable', 0)
    elif RL_name == u'Arn':
        anord_ao_nm_autoLayer(allMeshes_nrf, style)
    if not imp_rfn:
        mel_cmd = u"source \"//file-cluster/GDC/Resource/Support/Maya/projects/Ninjago/njEnvMaterialChange.mel\""
        mel.eval(mel_cmd)
        mel.eval(u'hideNjReferenceMat()')
        # mel.eval(u'showNjReferenceMat()')
    if cleanMat:
        mel.eval("MLdeleteUnused")
        delete_allLight()
#===================指定物体到某指定渲染层(不存在则创建)，指定材质球(或保留原材质)=========================================


def asign_obj_shader_to_RndLayer(objs, RndLay_name, shader_name=u'hold'):
    RL_node = RndLay_name
    if not mc.objExists(RL_node):
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
            if mc.listRelatives(eachObj, shapes=True, ni=True, type=[u'mesh', u'nurbsSurface']) or mc.nodeType(eachObj) in [u'mesh', u'nurbsSurface']:
                mc.sets(eachObj, e=True, forceElement=shd_SG)


def delete_allShader(storeSG=None):
    allSG = [eachSG for eachSG in mc.ls(type="shadingEngine") if not mc.referenceQuery(eachSG, inr=True)]
    initialSG = ["initialParticleSE", "initialShadingGroup"]
    if storeSG:
        initialSG.extend(storeSG)
    userSG = [allSG[i] for i in range(len(allSG)) if allSG[i] not in initialSG]
    if len(userSG) != 0:
        mc.delete(userSG)
        mel.eval("MLdeleteUnused")


def delete_allLight():
    allLights = [each_l for each_l in mc.ls(type=u'light', l=True) if not mc.referenceQuery(each_l, inr=True)]
    if len(allLights):
        mc.delete(allLights)


def check_mesh_validity(meshShape):  # =========检测读取geoCache物体，enable属性未开启前，无形态==========
    #meshShape = listMeshes[3]
    if mc.polyEvaluate(meshShape, face=1):
        return True
    else:
        get_cacheFaile = [each_hist for each_hist in mc.listHistory(meshShape, ac=True) if mc.nodeType(each_hist) == u'cacheFile']
        if get_cacheFaile != []:
            getControl = mc.listConnections(u'%s.enable' % get_cacheFaile[0], p=True)
            if getControl:
                mc.setAttr(getControl[0], 1)
                mc.setAttr(getControl[0], 0)
            else:
                mc.setAttr(u'%s.enable' % get_cacheFaile[0], 1)

        if mc.polyEvaluate(meshShape, face=1):
            return True
        else:
            return False


def anord_ao_nm_autoLayer(selObjs, style=u'CHR'):
    from idmt.maya.core_common.core_arnold import idmt_renderLayerCore
    reload(idmt_renderLayerCore)
    idmt_renderLayerCore.idmtRLArnoldConfig().idmtArnoldRendererSettings()
    from idmt.maya.perform_common.renderLayers import dod_renderLayers
    reload(dod_renderLayers)
    mc.select(selObjs, r=True)
    dod_renderLayers.renderLayer_dod().dodRLNMArnoldCreate(style, 1, 1)
    mc.select(selObjs, r=True)
    dod_renderLayers.renderLayer_dod().dodRLAOArnoldCreate(style, 1, 1)


def disconnect_shape_sg(objShape, assignNewSG=False, whole=True):  # ====断开指定物体与SG节点的连接（是否连接新的sg）
    objShape_par = u'|'.join(objShape.split(u'|')[:-1])
    if not whole:  # ===========（按面赋予材质的的物体，是否整体再指定材质----否）
        if assignNewSG:  # =====按照物体原赋予材质信息重新指定材质============
            con_sg_noSort = [eachSG for eachSG in mc.listConnections(objShape, type=u'shadingEngine') if not eachSG == u'initialShadingGroup']
            con_sg = [con_sg_noSort[i] for i in range(len(con_sg_noSort)) if con_sg_noSort[i] not in con_sg_noSort[:i]]
            con_members = []
            for each_sg in con_sg:
                mc.hyperShade(o=each_sg)
                members = [each_mem for each_mem in mc.ls(sl=True, l=True, fl=True) if each_mem.find(objShape_par) > -1]
                if len(members) != 0:
                    mc.sets(members, e=True, fe=assignNewSG)
        else:  # =============只是断开物体与SG的连接========================
            con_sg_plus = mc.listConnections(objShape, type=u'shadingEngine', c=True, p=True)
            if con_sg_plus:
                for i in range(0, len(con_sg_plus), 2):
                    try:
                        mc.disconnectAttr(con_sg_plus[i], con_sg_plus[i + 1])
                        print u'====Disconect %s and %s' % (con_sg_plus[i], con_sg_plus[i + 1])
                    except:
                        mc.disconnectAttr(con_sg_plus[i + 1], con_sg_plus[i])
                        print u'====Disconect %s and %s' % (con_sg_plus[i + 1], con_sg_plus[i])
    else:  # ==============整体赋予新的材质=================
        create_MatGrp = create_spec_MAT(assignNewSG)
        con_sg_plus = mc.listConnections(objShape, type=u'shadingEngine', c=True, p=True)
        if con_sg_plus:
            for i in range(0, len(con_sg_plus), 2):
                try:
                    mc.disconnectAttr(con_sg_plus[i], con_sg_plus[i + 1])
                except:
                    mc.disconnectAttr(con_sg_plus[i + 1], con_sg_plus[i])
        try:
            mc.sets(objShape, e=True, fe=create_MatGrp[1])
        except:
            print u'%s,can not assign mat' % objShape


def create_spec_MAT(mat_name, mt_type=u'lambert'):  # =====创建指定名字的材质球或者sg====================
    if mc.objExists(mat_name):  # ===============判断物体若存在=====================
        if not mc.nodeType(mat_name) == u'shadingEngine':  # ============如果物体类型不是SG节点=================
            SG_nodeLs = mc.listConnections(u'%s.outColor' % mat_name)
            matSG = u'%sSG' % mat_name
            if SG_nodeLs:
                return [mat_name, SG_nodeLs[0]]
            else:
                if mc.objExists(matSG):
                    mc.connectAttr((mat_name + '.outColor'), (mat_name + 'SG.surfaceShader'), f=True)
                else:
                    matSG = mc.sets(name=(mat_name + "SG"), renderable=True, noSurfaceShader=True, empty=True)
                    mc.connectAttr((mat_name + '.outColor'), (mat_name + 'SG.surfaceShader'), f=True)
                return [mat_name, matSG]
        else:  # =============若物体类型为sg节点===================================
            p_unSG = re.compile(u'[^SG]+')
            mat_name_re = p_unSG.search(mat_name).group()
            mt_temp = mc.listConnections(u'%s.surfaceShader' % mat_name)
            if mt_temp:
                return [mt_temp[0], mat_name]
            else:
                if mc.objExists(mat_name_re):
                    mc.connectAttr((mat_name_re + '.outColor'), (mat_name + '.surfaceShader'), f=True)
                    return[mat_name_re, mat_name]
                else:
                    mt_temp = mc.shadingNode(mt_type, asShader=True, n=mat_name_re)
                    mc.connectAttr((mt_temp + '.outColor'), (mat_name + '.surfaceShader'), f=True)
                    return [mt_temp, mat_name]
    else:  # ===========若物体不存在，创建它和SG================
        matShd = mc.shadingNode(mt_type, asShader=True, n=mat_name)
        matSG = mc.sets(name=(matShd + "SG"), renderable=True, noSurfaceShader=True, empty=True)
        mc.connectAttr(u'%s.outColor' % matShd, u'%s.surfaceShader' % matSG, f=True)
        return [mat_name, matSG]
