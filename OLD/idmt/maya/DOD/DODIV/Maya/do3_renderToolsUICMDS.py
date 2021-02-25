# -*- coding: utf-8 -*-
'''
Created on 2012-12-292012

@author: zhangben
渲染工具面板对应的函数模块文件

'''
import sys
sys.path.append("//File-cluster/GDC/Resource/Support/Maya/Python/IDMT/yfsScripts")
sys.path.append(ur"\\file-cluster\gdc\Resource\Support\Maya\projects\DODIII")

import maya.cmds as mc
import maya.mel as mel
import os
import sys
import re
import time
import getpass
import do3_modelAssignLambert as dmal
reload(dmal)
import do3_configPlaybackOptionsToCamAni as dcplo
reload(dcplo)
import do3_camToolUICMDS as dctc

import yuRepairRenderFrameTool as yrrt
#reload (yrrt)
import zb_createSpecRL as zcsr
import idmt.maya.DOD.DODIV.Maya.commonProperties as docp

winTitle = u"快乐的DOD同学们，大家好！辛苦啦！"  # 补帧工具，承恩试用，勿论成败，望用后赐教一二。不胜感激   "


def advertisingLinkerCmds():  # ===========广告牌连接地址======================
    os.system(r"explorer \"file://file-cluster/gdc/Resource/Support/Maya/docs/repatchingRenderToolsForMaya(local).mht\"")


def refreshPanelParameter():  # =========配置渲染面板==========================
    try:
        refresh_oneSentenceOneDayLable()
        refreshWinTitle()
        mc.window("DOD3RenderTools", e=True, mnb=True)
        slogan = counterProcedure()
        configAdertisingContral(slogan)
    except:
        pass


def configAdertisingContral(slogan=u"【广告位招租】"):
    if mc.control("adv_vis", q=True, ex=True):
        mc.control("adv_vis", e=True, vis=True)
        mc.button("rep_RendBT", e=True, vis=False)
        mc.text("advertisingLab", e=True, l=slogan)
        mc.button("advertisingButton", e=True, ann=u"有不明请询问RTX 1745")


def do3_RTC_pv_bt_cmds(toggle):
    do3_RTC_toggleAttr("primaryVisibility", toggle)
    if toggle == True:
        mc.button("pv_onb", e=True, bgc=[0.68, 0.68, 0.8])
        mc.button("pv_ofb", e=True, bgc=[0.45, 0.45, 0.45])
    else:
        mc.button("pv_onb", e=True, bgc=[0.45, 0.45, 0.45])
        mc.button("pv_ofb", e=True, bgc=[0.68, 0.68, 0.8])


def closeVisInTrans():  # ========物体与摄像机之间有透明物体，解决mr渲染会有“渲染了不可渲物体“的情况。
    selObj = mc.ls(sl=True, l=True)
    intermediateObj = mc.ls(intermediateObjects=True, l=True)
    for each in selObj:
        shapes = []
        meshes = mc.listRelatives(each, ad=True, c=True, type="mesh", f=True)
        if meshes != None:
            shapes.extend([meshes[i] for i in range(len(meshes)) if meshes[i] not in intermediateObj])
        surfaces = mc.listRelatives(each, ad=True, c=True, type="nurbsSurface")
        if surfaces != None:
            shapes.extend(surfaces)
        if len(shapes) != 0:
            for eachShape in shapes:
                mc.setAttr(eachShape + ".miTransparencyCast", 0)


def do3_deleteAllRenderlayer():  # ==========删除所有已建渲染层===============================================
#    RG_list = mc.ls(type="renderGlobals")
#    rendererRLs = []
#    for eachRG in RG_list:
#        rendererRL_temp = mc.listConnections(eachRG +".imageFilePrefix",type = "renderLayer")
#        if  rendererRL_temp != None:
#                rendererRLs.extend(rendererRL_temp)
#    if mc.objExists("defaultRenderLayer"):
#        rendererRLs.remove("defaultRenderLayer")
#    else:
#        mc.error("Thear has no defaultRenderLayer")
#
#    mc.editRenderLayerGlobals(currentRenderLayer = "defaultRenderLayer")
#    mc.delete(rendererRLs)
    if mc.objExists("defaultRenderLayer"):
        mc.editRenderLayerGlobals(currentRenderLayer="defaultRenderLayer")
    else:
        mc.error("Thear has no defaultRenderLayer")
    listAllRL = mc.ls(type="renderLayer")
    listAllRL.remove("defaultRenderLayer")
    mc.delete(listAllRL)


def do3_lookThrouRendCam(eyes):  # =======look through render camerae specify disMode=========
    renderCam = get_renderCam()
    sceneCam = docp.get_shot_StereoCamGrp_camSHPS()
    if eyes == 0:
        dcplo.do3_lookThrougToSpecialCam(renderCam, 0, eyes)
    else:
        dcplo.do3_lookThrougToSpecialCam(sceneCam[eyes - 1], False)


def get_sceneCam():
    allCamShapes = mc.ls(cameras=True, l=True)
    ref_cams = range(3)
    sceneCam = []
    p_center = re.compile("CenterCam", re.I)
    p_left = re.compile("left", re.I)
    p_right = re.compile("right", re.I)

    for eachCamShape in allCamShapes:
        if mc.referenceQuery(eachCamShape, isNodeReferenced=True) and p_left.search(eachCamShape) != None:
            sceneCam.append(eachCamShape)
        elif mc.referenceQuery(eachCamShape, isNodeReferenced=True) and p_center.search(eachCamShape) != None:
            sceneCam.append(eachCamShape)
        elif mc.referenceQuery(eachCamShape, isNodeReferenced=True) and p_right.search(eachCamShape) != None:
            sceneCam.append(eachCamShape)
    if len(sceneCam) == 3:
        return sceneCam
    else:
        mc.error("there has no exactely camera in the scene")


def get_renderCam():
    allCamShapes = mc.ls(cameras=True, l=True)
    fn = mc.file(q=True, sn=True, shn=True)
    ep = fn.split("_")[1]
    sc = fn.split("_")[2]
    camMatchStr = "CAM*:cam_" + ep + "_" + sc + "_baked*"
    if mc.ls(camMatchStr, l=True) == []:
        mc.error("wrong camera referenced")
    renderCam_root = ""
    for eachOne in mc.ls(camMatchStr, l=True):
        if mc.nodeType(eachOne) == "stereoRigTransform":
            renderCam_root = eachOne
    return renderCam_root


def refresh_oneSentenceOneDayLable():  # ==============每日一句===================
    timeData = time.localtime()
    dayOfWeek = int(time.strftime('%w', timeData))
    weekNum = int(time.strftime('%W', timeData))
    dayNum = int(time.strftime('%j', timeData))

    currentDate = str(dayNum)
    currentYear = time.strftime('%Y', timeData)

    dayStr = u"\t【%s的第%s天】" % (currentYear, currentDate)

    osod_txPath = r"\\file-cluster\gdc\Resource\Support\Maya\projects\DODIV\icons\oneSentenceOneDay_whole.txt"
    f_open = open(osod_txPath, 'r')
    sentenceList = f_open.readlines()
    f_open.close()
    try:
        todayCentence = sentenceList[dayNum]
    except:
        todayCentence = 'today\'s mood ,not beutifule'
    unicodecTodayCentence = todayCentence.decode('utf8')[:-2] + dayStr

    p = re.compile(ur"[\u4e00-\u9fa5]")

    firstChinesCharacter = p.search(unicodecTodayCentence).group()
    CHNIndex = unicodecTodayCentence.index(firstChinesCharacter)

    new_strLine_top = ""
    new_stLine_bottom = ""
    new_wholeStr = ""
    if CHNIndex > 160:
        new_wholeStr = aotuWordWrap(160, unicodecTodayCentence)
    else:

        new_stLine_top = unicodecTodayCentence[:CHNIndex]
        new_stLine_bottom = aotuWordWrap(160, unicodecTodayCentence[CHNIndex:])
        new_wholeStr = new_stLine_top + "\n" + new_stLine_bottom

    disSentencStr = u"每日一句:" + new_wholeStr

    mc.text("odos_lab", e=True, l=disSentencStr)


def refreshWinTitle():  # ==========窗口标题内容的刷新，根据全局变量winTitle===========
    global winTitle
    timeData = time.localtime()
    dateStr = time.strftime("%Y-%m-%d", timeData)
    titleStr = u"DOD3 Render Tools  【%s%s】" % (winTitle, dateStr.decode('utf-8'))
    mc.window("DOD3RenderTools", e=True, title=titleStr)


def aotuWordWrap(maxIndex, sentence):  # ===========自动换行，避免一日一句出现字数超过行宽的情况===
    new_sentence_LS = []
    while len(sentence) > maxIndex:
        strLine_top = sentence[:maxIndex]
        p_space = re.compile("\s")
        lineWordCount = len(p_space.findall(strLine_top))
        sen_split = sentence.split(" ")
        topSplit = strLine_top.split(" ")
        new_strLine_top = " ".join(topSplit[:lineWordCount])

        strLine_bottom = " ".join(sen_split[lineWordCount:])
        new_sentence_LS.append(new_strLine_top)
        sentence = strLine_bottom

    new_sentence = "\n".join(new_sentence_LS) + "\n" + sentence
    return new_sentence


def delete_allShaderBTCMD():  # ===========删除所有材质的button执行的命令，指向引入的dmal模块
    # dmal.delete_allShader()
    dmal.do3_modelAssignLambert(True)


def repairRendBTCMD():
    yrrt.repairRenderFrameUI()


def renderAttrSpreadSheetWin(attrList):  # 渲染属性调节对照表
    if mc.window('ren_attr_SSEWin', exists=True):
        mc.deleteUI('ren_attr_SSEWin')

    mainWin = mc.window('ren_attr_SSEWin', widthHeight=(830, 550), t="DOD3 Render Attribute SpreadSheet")
    mc.paneLayout("mainPL")
    activeList = mc.selectionConnection(activeList=True)
    mc.spreadSheetEditor(mainListConnection=activeList, showShapes=True, niceNames=True, fal=attrList, ko=False)
    mc.window('ren_attr_SSEWin', e=True, wh=(830, 560), s=True)
    mc.showWindow(mainWin)


def show_rassw():
#    selectObject = mc.ls(sl=True,l=True)
#    if len(selectObject) != 0:
#        shape_nodes = do3_returnShapeNodes(selectObject)
#        mc.select(shape_nodes,r=True)

    attrList = ["primaryVisibility", "castsShadows", "receiveShadows", "visibleInReflections", "visibleInRefractions"]
    renderAttrSpreadSheetWin(attrList)


def do3_returnShapeNodes(objects):  # 返回物体形节点
    shape_nodes = []
    for each in objects:
        if mc.nodeType(each) == "mesh" or mc.nodeType(each) == "nurbsSurface":
            shape_nodes.append(each)
        elif mc.nodeType(each) == "transform":
            shapeNode = mc.listRelatives(each, s=True, ni=True, f=True)
            shape_nodes.extend(shapeNode)
    return shape_nodes


def do3_RTC_toggleAttr(attr, value):
    selObjs = mc.ls(sl=True, l=True)
    if len(selObjs) == 0:
        mc.error("木有选择物体啊")
    shapeNodes = do3_returnShapeNodes(selObjs)
    for eachShape in shapeNodes:
        attrName = "%s.%s" % (eachShape, attr)
        zcsr.do3_RL_adjustmentParameter(attrName, value)


def do3_RTC_getAttrValue(attr):  # 返回物体某属性值
    selObjs = mc.ls(sl=True, l=True)
    if len(selObjs) == 0:
        mc.error("木有选择物体啊")
    shapeNodes = do3_returnShapeNodes(selObjs)
    attrName = "%s.%s" % (shapeNodes[0], attr)
    value = mc.getAttr(attrName)
    return value


def recardCount():  # 将用户信息写入文本
    counterFile = "//file-cluster/gdc/Projects/DiveollyDive3/DiveollyDive3_Scratch/TD/temp/counterUserNum.text"
    user = getpass.getuser()
    time.localtime(time.time())
    timeInfo = time.strftime('%Y-%m-%d  %H:%M:%S', time.localtime(time.time()))
    markStr = "%s by %s clicked\r\n" % (timeInfo, user)

    fp = open(counterFile, 'a')
    fp.write(markStr)
    fp.close()
    slogan = counterProcedure()
    configAdertisingContral(slogan)


def counterProcedure():  # 统计数字返回信息
    counterFile = "//file-cluster/gdc/Projects/DiveollyDive3/DiveollyDive3_Scratch/TD/temp/counterUserNum.text"
    userList = []
    rf = open(counterFile, 'r')
    allLines = rf.readlines()
    count = len(allLines)
    for e_l in allLines:
        userList.append(e_l.split(" ")[4])
    rf.close()
    userList = [userList[i] for i in range(len(userList)) if userList[i] not in userList[:i]]
    userCount = len(userList)
    resultStr = u"工具被%d位同学  \n 使用了       %d 次" % (userCount, count - 1)
    return resultStr


def crowd_bt_cmd():
    from idmt.maya.core_common.core_arnold import idmt_renderLayerCore
    reload(idmt_renderLayerCore)
    idmt_renderLayerCore.idmtRLArnoldConfig().idmtArnoldRendererSettings()
    from idmt.maya.perform_common.renderLayers import dod_renderLayers
    reload(dod_renderLayers)
    dod_renderLayers.renderLayer_dod().dodRlCoAOVsArnold('char_fish', 0, 1)
if __name__ == "__main__":
    pass
