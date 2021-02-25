#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2013-9-122013

@author: zhangben



'''
import maya.cmds as mc
import maya.mel as mel
import re
import os
from maya.app.stereo import stereoCameraCustomPanel
import math
#======commom propertie======detection specific node whether can rendered out=====
#===Notice:this procedure has a unsatisfactory part when U iteration a group of dagobjects with the same parent node,
#===the procedure will check all the parent node again and again.So,the procedure will be modified and be optimized soon or later...
#===Sory for my poor English,I hope you will understand me.


def nodeIsVisible(nodeName):
    #===if user is asking about a bogus node ,return false
    if mc.objExists(nodeName) == False:
        return False
    #===Object must a DAG node,or it's not visible.
    # There's no MEL query to identify a DAG node, but the kDagNode class adds
    # the '.visibility' attribute, so we'll use its existence as a cue.
    if mc.attributeQuery('visibility', node=nodeName, exists=True) == False:
        return False
    #===the obvious:Start with the '.visibility'attrbute on the node.
    visible = True
    if mc.keyframe(u'%s.visibility' % nodeName, q=True):
        visible = True in mc.keyframe(u'%s.visibility' % nodeName, q=True, valueChange=True)
    else:
        visible = mc.getAttr(u'%s.visibility' % nodeName)
    #===if this is a intermediate mesh,it's not visible
    if mc.attributeQuery('intermediateObject', node=nodeName, exists=True):
        #===there is a interesting syntax write function,and there are several write style
        # visible & (not mc.getAttr(u'%s.intermediateObject'%nodeName
        visible = visible and (not mc.getAttr(u'%s.intermediateObject' % nodeName))
    #===if the object is in a displayLayer,and the displayLayer is hidden,then the object is hidden
    if mc.attributeQuery('overrideEnabled', node=nodeName, exists=True) and mc.getAttr(u'%s.overrideEnabled' % nodeName):
        visible = visible and mc.getAttr(u'%s.overrideVisibility' % nodeName)
    # ascend the hierarchy and check all of the parent nodes
    if visible:
        parentNodes = mc.listRelatives(nodeName, parent=True, f=True)
        if parentNodes != None:
            visible = visible and (nodeIsVisible(parentNodes[0]))  # ==this is a classic recursive function syntax
    # print u'%s VISIBLE STATE IS : %s' % (nodeName, visible)
    return visible

#========移除目标目录中除了制定要保留的目录外的所有子目录=====================================


def remove_remain_DIR(destinationDir, remainDir):
    normRemainDir = [os.path.normpath(eachReDir) for eachReDir in remainDir]
    if not os.path.isdir(destinationDir):
        return
    for eachDir in os.listdir(destinationDir):
        fullPath = os.path.normpath(os.path.join(destinationDir, eachDir))
        if fullPath in normRemainDir:
            continue
        elif os.path.isfile(fullPath):
            os.remove(fullPath)
        elif os.path.isdir(fullPath):
            removeall(fullPath, remainDir)
            os.rmdir(fullPath)
#=============================================================================
#==================获取父节点的一组函数==============================================


def getParent(specObj, parentLevel):  # ===============层级===========================
    #specObj = mc.ls(sl=True,l=True)[0]
    #parentLevel = 3
    ind = parentLevel * -1
    return(u'|'.join(specObj.split(u'|')[:ind]))


def getParent_2(specObj, parentDescription):  # ===============描述字符===========================
    p_desc = re.compile(parentDescription)
    par_node = specObj
    while par_node != None and p_desc.search(par_node) == None:
        par_node = mc.listRelatives(par_node, p=True, f=True)[0]
    return par_node


def getParent_3(specObj, parentType):  # ===============父节点类型===========================
    par_node = specObj
    while par_node != None and mc.nodeType(par_node) != parentType:
        par_node_ls = mc.listRelatives(par_node, p=True, f=True)
        if par_node_ls:
            par_node = par_node_ls[0]
        else:
            return None
    return par_node


def getParent_root(nodeName):
    #nodeName = "pCube1"
    #nodeName ="|jellyfish_master|jellyfish_master_curveShape"
    parentNode = nodeName
    pNodes = mc.listRelatives(nodeName, p=True, f=True)

    while pNodes:
        parentNode = pNodes[0]
        pNodes = mc.listRelatives(pNodes[0], p=True, f=True)
    return parentNode


def getShotInformation():  # ===========获取镜头文件信息：项目缩写，sq_num,sc_num,环节信息，版本，格式===========
    shotFileName_ln = mc.file(q=True, sn=True)
    shotFilePath = os.path.dirname(shotFileName_ln)
    shotFileName_shn = mc.file(q=True, sn=True, shn=True)
    shotFileName_shn = os.path.splitext(shotFileName_shn)
    shotFileName_shn_split = shotFileName_shn[0].split(u'_')
    print '-------'
    print shotFileName_shn_split
    resultList = {u'path': shotFilePath, u'project_abbr': shotFileName_shn_split[0],
                  u'sq_num': shotFileName_shn_split[1], u'sc_num': shotFileName_shn_split[2],
                  u'mode': shotFileName_shn_split[3], u'verson': shotFileName_shn_split[4],
                  u'type': shotFileName_shn[-1]}

    return resultList


#=================add dod scene file open script============================================
def do_sceneOpenScript():
    turtleNodes = mc.ls(u'Turtle*')
    for eachNode in turtleNodes:
        mc.lockNode(eachNode, l=False)
        mc.delete(eachNode)
    config_shotFile_cameraParameter()
    if not mc.pluginInfo(u'Mayatomr.mll', q=True, loaded=True):
        mc.loadPlugin(u'Mayatomr.mll')

    mel.eval(u'miCreateDefaultNodes()')
    mel.eval(u'miCreateOtherOptionsNodesForURG()')

    defRndGlb = u'defaultRenderGlobals'
    mc.setAttr(u'%s.currentRenderer' % defRndGlb, u'mentalRay', type=u'string')

    mc.setAttr(u'defaultResolution.width', 2048)
    mc.setAttr(u'defaultResolution.height', 1106)

    mc.setAttr(u'defaultResolution.deviceAspectRatio', 1.852)
    mc.setAttr(u'defaultResolution.pixelAspect', 1.0)

    mc.setAttr(u'miDefaultOptions.minSamples', 0)
    mc.setAttr(u'miDefaultOptions.maxSamples', 2)
    mc.setAttr(u'miDefaultOptions.contrastR', 0.02)
    mc.setAttr(u'miDefaultOptions.contrastG', 0.02)
    mc.setAttr(u'miDefaultOptions.contrastB', 0.02)
    mc.setAttr(u'miDefaultOptions.maxReflectionRays', 1)
    mc.setAttr(u'miDefaultOptions.maxRefractionRays', 1)
    mc.setAttr(u'miDefaultOptions.maxRayDepth', 2)
    mc.setAttr(u'miDefaultOptions.maxShadowRayDepth', 3)
    mc.setAttr(u'miDefaultOptions.jitter', 1)
    mc.setAttr(u'miDefaultOptions.filter', 2)
    mc.setAttr(u'miDefaultFramebuffer.datatype', 16)

    mel.eval(u'zwSceneOpenedScriptJobStartEnd()')


#=====================配置镜头文件摄像机================================================
def config_shotFile_cameraParameter():
    try:
        file_infor = getShotInformation()
    except:
        return None
    sq_shot = u'%s_%s' % (file_infor[u'sq_num'], file_infor[u'sc_num'])
    p_cam = re.compile(u'%s_baked$' % sq_shot)

    shot_Cam_ls = [exactCam for exactCam in mc.ls(type='stereoRigTransform') if p_cam.search(exactCam) != None]
    if shot_Cam_ls == []:
        p_cam_noBaked = re.compile(u'%s$' % sq_shot)
        shot_Cam_ls = [exactCam for exactCam in mc.ls(type='stereoRigTransform') if p_cam_noBaked.search(exactCam) != None]

        if shot_Cam_ls == []:
            print u'+++++++++++File:s++++++++There Is No Render Camera,Please Check Your Scenes!!++++++++++++'
            return

    renderCams = [stereoShape for stereoShape in mc.listRelatives(shot_Cam_ls[0], c=True, ad=True, type=u'camera', f=True) if mc.nodeType(stereoShape) == u'camera']
    #============================================================
    # ===========set all camera renderable off=====关闭所有肥渲染摄像机可渲染属性，开启渲染摄像机可渲染属性==============
    allCameShape = mc.ls(type="camera", l=True)
    for eachCamShape in allCameShape:
        if eachCamShape in renderCams:
            mc.setAttr(u'%s.renderable' % eachCamShape, 1)
        else:
            mc.setAttr(u'%s.renderable' % eachCamShape, 0)
    return shot_Cam_ls[0]


def get_shot_rnd_cam():
    file_infor = getShotInformation()
    sq_shot = u'%s_%s' % (file_infor[u'sq_num'], file_infor[u'sc_num'])
    p_cam = re.compile(u'%s_baked$' % sq_shot)

    shot_Cam_ls = [exactCam for exactCam in mc.ls(type='stereoRigTransform') if p_cam.search(exactCam) != None]
    if shot_Cam_ls == []:
        p_cam_noBaked = re.compile(u'%s$' % sq_shot)
        shot_Cam_ls = [exactCam for exactCam in mc.ls(type='stereoRigTransform') if p_cam_noBaked.search(exactCam) != None]

        if shot_Cam_ls == []:
            print u'+++++++++++File:s++++++++There Is No Render Camera,Please Check Your Scenes!!++++++++++++'
            return

    renderCams = [stereoShape for stereoShape in mc.listRelatives(shot_Cam_ls[0], c=True, ad=True, type=u'camera', f=True) if mc.nodeType(stereoShape) == u'camera']
    return renderCams
#===============================删除显示层================================


def get_shot_StereoCamGrp_camSHPS():
    file_infor = getShotInformation()
    sq_shot = u'%s_%s' % (file_infor[u'sq_num'], file_infor[u'sc_num'])
    p_cam = re.compile(u'%s_baked$' % sq_shot)

    p_center = re.compile("CenterCam", re.I)
    p_left = re.compile("left", re.I)
    p_right = re.compile("right", re.I)

    shot_Cam_ls = [exactCam for exactCam in mc.ls(type='stereoRigTransform') if p_cam.search(exactCam) != None]
    if shot_Cam_ls == []:
        p_cam_noBaked = re.compile(u'%s$' % sq_shot)
        shot_Cam_ls = [exactCam for exactCam in mc.ls(type='stereoRigTransform') if p_cam_noBaked.search(exactCam) != None]

        if shot_Cam_ls == []:
            print u'+++++++++++File:s++++++++There Is No Render Camera,Please Check Your Scenes!!++++++++++++'
            return

    stereoCamGrp_cnt_SHPS = [eachCam for eachCam in mc.listRelatives(shot_Cam_ls[0], c=True, ad=True, type=u'camera', f=True) if mc.nodeType(eachCam) == u'stereoRigCamera']
    stereoCam_SHPS = [stereoShape for stereoShape in mc.listRelatives(shot_Cam_ls[0], c=True, ad=True, type=u'camera', f=True) if mc.nodeType(stereoShape) == u'camera']
    stereoCamGrp_cnt_SHPS.extend(stereoCam_SHPS)
    return stereoCamGrp_cnt_SHPS


def delete_displayLayer():
    p_nr = re.compile(u'(norender)', re.I)
    p_def = re.compile(u'defaultLayer')
    allDisLayers = [eadisLayer for eadisLayer in mc.ls(type=u'displayLayer') if not mc.referenceQuery(eadisLayer, inr=True) and eadisLayer != u'defaultLayer']
    for eachDL in allDisLayers:
        if mc.editDisplayLayerMembers(eachDL, q=True) != None:
            emptLayerCmd = u'layerEditorEmpty %s;' % eachDL
            mel.eval(emptLayerCmd)
        allCons = mc.listConnections(eachDL, p=True, s=True, d=True, c=True)
        if allCons != None:
            for i in range(0, len(allCons), 2):
                try:
                    mc.disconnectAttr(allCons[i], allCons[i + 1])
                except:
                    mc.disconnectAttr(allCons[i + 1], allCons[i])
        layerMAN = mc.listConnections(u'%s.identification' % eachDL, p=True)
        if layerMAN != None:
            mc.disconnectAttr(layerMAN[0], u'%s.identification' % eachDL)
    mc.delete(allDisLayers)


def get_currentActivViewPanel():
    allVisPanels = mc.getPanel(visiblePanels=True)
    modelPanels = [allVisPanels[j] for j in range(len(allVisPanels)) if (mc.getPanel(typeOf=allVisPanels[j])) == "modelPanel"]
    scriptPanels = [allVisPanels[j] for j in range(len(allVisPanels)) if (mc.getPanel(typeOf=allVisPanels[j])) == "scriptedPanel"]
    activeStereoPanel = [scriptPanels[k] for k in range(len(scriptPanels)) if mc.scriptedPanel(scriptPanels[k], q=True, type=True) == "Stereo"]
    # print modelPanels,activeStereoPanel

    allEditors = mc.lsUI(editors=True)
    stereoEditors = [allEditors[k] for k in range(len(allEditors)) if allEditors[k] == "StereoPanelEditor"]
    stereoPanels = mc.stereoCameraView(stereoEditors[0], query=True, panel=True)
    # print stereoPanels
    current_ac_viewPanel = ""
    activeModelPanel = []
    for eachMP in modelPanels:
        MEs = mc.modelPanel(eachMP, q=True, modelEditor=True)
        if(mc.modelEditor(MEs, q=True, activeView=True) and (mc.modelPanel(eachMP, q=True, camera=True) in mc.listCameras(perspective=True))):
            activeModelPanel.append(eachMP)
        if (activeModelPanel != []):
            current_ac_viewPanel = activeModelPanel[0]

    if current_ac_viewPanel == ""and activeStereoPanel[0] == stereoPanels:
        current_ac_viewPanel = stereoPanels

    return current_ac_viewPanel
# print ok


def lookThroughRndCame(camShape, ste_editor="StereoPanelEditor"):
    modeList = ['anaglyphLum', 'centerEye', 'leftEye', 'rightEye']
    if getParent_3(camShape, u'stereoRigTransform'):
        mel.eval('stereoCameraSwitchToCamera %s %s' % (camShape, get_currentActivViewPanel()))
        p_right = re.compile(u'right', re.I)
        p_left = re.compile(u'left', re.I)
        if p_right.search(camShape):
            stereoCameraCustomPanel.stereoCameraViewCallback(ste_editor, "{'displayMode': '%s'}" % (modeList[3]))
        elif p_left.search(camShape):
            stereoCameraCustomPanel.stereoCameraViewCallback(ste_editor, "{'displayMode': '%s'}" % (modeList[2]))
        else:
            stereoCameraCustomPanel.stereoCameraViewCallback(ste_editor, "{'displayMode': '%s'}" % (modeList[1]))
    else:
        mel.eval("lookThroughModelPanel %s %s" % (camShape, get_currentActivViewPanel()))
#============================================================================


def get_crrent_rnd_camera(disShape=True):
    renderCams = [eachCam for eachCam in mc.ls(type=u'camera', l=True) if mc.getAttr(u'%s.renderable' % eachCam) == 1]
    if disShape:
        return renderCams
    else:
        renderCams_par = []
        for each_cam in renderCams:
            cam_p = mc.listRelatives(each_cam, p=True, f=True)[0]
            renderCams_par.append(cam_p)
        return renderCams_par


def del_unknownNodes():
    #========delete all unknown nodes======================================
    unknowNodes = mc.ls(type=u'unknown')
    if unknowNodes != []:
        for ea in unknowNodes:
            try:
                mc.lockNode(ea, l=False)
                mc.delete(ea)
            except:
                continue
        #========delete all tuttle nodes======================================
    tutleNodes = mc.ls(u'Turtle*')
    if tutleNodes != []:
        for et in tutleNodes:
            try:
                mc.lockNode(et, l=False)
                mc.delete(et)
            except:
                continue


def del_unConnectRefNode():
    allRNIterator = (eachRN for eachRN in mc.ls(type=u'reference') if not mc.listConnections(u'%s.message' % eachRN, d=True))
    for eachRN in allRNIterator:
        mc.lockNode(eachRN, l=False)
        mc.delete(eachRN)


def list_valid_referenceNodes():
    allRN = mc.ls(type=u'reference')
    valid_rn = []
    for each_rn in allRN:
        try:
            if mc.referenceQuery(each_rn, filename=True):
                valid_rn.append(each_rn)
        except:
            pass
    return valid_rn


def rp_zPath2FileCluster():
    cacheNodes = mc.ls(type=u'cacheFile')
    rp_path = u''
    for each_cf in cacheNodes:
        cch_path = mc.getAttr(u'%s.cachePath' % each_cf)
        if cch_path.startswith(u'Z:'):
            rp_path = cch_path.replace(u'Z:', u'//file-cluster/GDC')
            mc.setAttr(u'%s.cachePath' % each_cf, rp_path, type=u'string')
        elif cch_path.startswith(u'z:'):
            rp_path = cch_path.replace(u'z:', u'//file-cluster/GDC')
            mc.setAttr(u'%s.cachePath' % each_cf, rp_path, type=u'string')


def clean_up_no_clr_rndFile():
    allRNIterator = list_valid_referenceNodes()
    for eachRN in allRNIterator:
        if not mc.referenceQuery(eachRN, isLoaded=True):
            rf_file = mc.referenceQuery(eachRN, f=True)
            mc.file(rf_file, lr=eachRN)
        mc.file(ir=True, rfn=eachRN)
    mc.editRenderLayerGlobals(currentRenderLayer='defaultRenderLayer')
    allMeshes_all = (d for d in mc.ls(typ=u'mesh', l=True) if not mc.referenceQuery(d, inr=True))
    for each_obj in allMeshes_all:
        get_con_RENINFO = mc.listConnections(each_obj, p=True, c=True, type=u'reference')
        if get_con_RENINFO:
            try:
                mc.disconnectAttr(get_con_RENINFO[0], get_con_RENINFO[1])
            except:
                mc.disconnectAttr(get_con_RENINFO[1], get_con_RENINFO[0])
        disconnect_shape_sg(each_obj, u'lambert_WHOSG')
    mel.eval("MLdeleteUnused")
    del_unknownNodes()


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


def get_noRnd_DL():
    p_nr = re.compile(u'norender', re.I)

    DLM = [each_dlm for each_dlm in mc.ls(type=u'displayLayerManager') if not mc.referenceQuery(each_dlm, inr=True)]
    NR_DL = [each_DL for each_DL in mc.listConnections(DLM[0], type=u'displayLayer') if p_nr.search(each_DL)]
    if NR_DL != []:
        return NR_DL[0]
    else:
        return None


def hsv2rgb(h, s, v):
    h = float(h)
    s = float(s)
    v = float(v)
    h60 = h / 60.0
    h60f = math.floor(h60)
    hi = int(h60f) % 6
    f = h60 - h60f
    p = v * (1 - s)
    q = v * (1 - f * s)
    t = v * (1 - (1 - f) * s)
    r, g, b = 0, 0, 0
    if hi == 0:
        r, g, b = v, t, p
    elif hi == 1:
        r, g, b = q, v, p
    elif hi == 2:
        r, g, b = p, v, t
    elif hi == 3:
        r, g, b = p, q, v
    elif hi == 4:
        r, g, b = t, p, v
    elif hi == 5:
        r, g, b = v, p, q
    r, g, b = int(r * 255), int(g * 255), int(b * 255)
    return r, g, b


def rgb2hsv(r, g, b):
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx - mn
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g - b) / df) + 360) % 360
    elif mx == g:
        h = (60 * ((b - r) / df) + 120) % 360
    elif mx == b:
        h = (60 * ((r - g) / df) + 240) % 360
    if mx == 0:
        s = 0
    else:
        s = df / mx
    v = mx
    return h, s, v


def set_mrTextur_writ_lightmap(writableValue=True):  # ==================设置SSS材质，lightmap的mentalrayTextrue节点，写贴图属性====
    user_tmp_dir = mc.internalVar(userTmpDir=True)

    all_lmaps = mc.ls(type=u'misss_fast_lmap_maya')
    for each in all_lmaps:
        get_mr_txt = mc.listConnections(u'%s.lightmap' % each)
        if get_mr_txt:
            char_sign = u'_'.join(get_mr_txt[0].split(u':'))
            lmap_dir = u'%s%s_mr_lmap' % (user_tmp_dir, char_sign)
            mc.setAttr(u'%s.fileTextureName' % get_mr_txt[0], lmap_dir, type=u'string')
            mc.setAttr(u'%s.miWritable' % get_mr_txt[0], writableValue)
