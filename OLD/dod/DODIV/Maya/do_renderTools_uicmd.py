# -*- coding: utf-8 -*-
'''
Created on 2013-12-72013

@author: zhangben
'''
import maya.cmds as mc
import re
import os
import sys
import time
import maya.mel as mel
import idmt.maya.DOD.DODIV.Maya.commonProperties as docp
import idmt.maya.DOD.DODIV.Maya.do3_renderToolsUICMDS as drcm
reload(docp)
import getpass


def ltc_btcmd():
    import idmt.maya.DOD.DODIV.Maya.do3_renderToolsUICMDS as drcm
    mc.confirmDialog(m=u'请选择物体设置smooth级别', b=u'知道啦')
    if mc.window(u'ltc_win', exists=True):
        mc.deleteUI(u'ltc_win')
    uiPath = ur'\\file-cluster\gdc\Resource\Support\Maya\projects\DODIV\lookThroughCamUI.myuis'
    ltc_ui = mc.loadUI(uiFile=uiPath)
    mc.windowPref(ltc_ui, topLeftCorner=[200, 630])
    mc.showWindow(ltc_ui)


def saveAsFile_btcmd():
    turtleNodes = mc.ls(u"Turtle*")
    if turtleNodes:
        for eachNode in turtleNodes:
            mc.lockNode(eachNode, l=False)
            mc.delete(eachNode)
        print u'The Nodes of Turtle Renderer Deleted'
    if mc.pluginInfo('mtoa', l=True, q=True):
        mc.unloadPlugin(u'mtoa', f=True)
        print u'Arnold Renderer unload'
    file_savePath = u'%s/scenes' % mc.workspace(q=True, fn=True)
    f_inf = docp.getShotInformation()

    new_fileName = "%s/%s_%s_%s_lr_%03d%s" % (file_savePath, f_inf[u'project_abbr'], f_inf[u'sq_num'], f_inf[u'sc_num'], 001, f_inf[u'type'])

    mc.file(rn=new_fileName)
    mc.file(save=True, force=True, type=u'mayaAscii')


def sep_btcmd():
    execfile('//file-cluster/gdc/Resource/Support/Python/2.6-x64/Lib/site-packages/idmt/maya/DOD/DODIV/Maya/do_seperateFile.py')


def shutOff_lightEmitSpec():
    selLightes = mc.ls(sl=True, l=True)
    for each_l in selLightes:
        getShape = mc.listRelatives(each_l, c=True, s=True)
        if getShape:
            if mc.listAttr(getShape[0], st=u'emitSpecular'):
                mc.setAttr(u'%s.emitSpecular' % getShape[0], 0)


def crowd_bt_cmd():
    from idmt.maya.commonCore.core_renderLayer import sk_renderLayerCore
    reload(sk_renderLayerCore)
    # 加载arnold
    sk_renderLayerCore.sk_renderLayerCore().idmtArnoldRendererSettings()
    from idmt.maya.commonPerform.renderLayers import dod_renderLayers
    reload(dod_renderLayers)
    dod_renderLayers.dod_renderLayers().dodRlCoAOVsArnold('char_fish', 0, 1, 0)


def rp_cachePath_bt_cmd():
    docp.rp_zPath2FileCluster()


def refresh_oneSentenceOneDayLable(chrNum=40):  # ==============每日一句===================
    timeData = time.localtime()
    dayOfWeek = int(time.strftime('%w', timeData))
    weekNum = int(time.strftime('%W', timeData))
    dayNum = int(time.strftime('%j', timeData))

    currentDate = str(dayNum)
    currentYear = time.strftime('%Y', timeData)

    dayStr = u"  【%s的第%s天】" % (currentYear, currentDate)

    osod_txPath = r"\\file-cluster\gdc\Resource\Support\Maya\projects\DODV\oneSentenceOneDay_whole.txt"
    f_open = open(osod_txPath, 'r')
    sentenceList = f_open.readlines()
    f_open.close()
    try:
        todayCentence = sentenceList[dayNum-300]
    except:
        todayCentence = 'today\'s mood ,not beutifule'
    unicodecTodayCentence = todayCentence.decode('utf8')[:-2] + dayStr

    p = re.compile(ur"[\u4e00-\u9fa5]")

    firstChinesCharacter = p.search(unicodecTodayCentence).group()
    CHNIndex = unicodecTodayCentence.index(firstChinesCharacter)

    new_strLine_top = ""
    new_stLine_bottom = ""
    new_wholeStr = ""
    if CHNIndex > chrNum:
        new_wholeStr = aotuWordWrap(chrNum, unicodecTodayCentence)
    else:

        new_stLine_top = unicodecTodayCentence[:CHNIndex]
        new_stLine_bottom = aotuWordWrap(chrNum, unicodecTodayCentence[CHNIndex:])
        new_wholeStr = new_stLine_top + "\n" + new_stLine_bottom

    disSentencStr = u"每日一句:" + new_wholeStr
    #disSentencStr = aotuWordWrap(chrNum, disSentencStr)
    mc.text("odos_lab", e=True, l=disSentencStr)


def aotuWordWrap(maxIndex, sentence):  # ===========自动换行，避免一日一句出现字数超过行宽的情况===
    new_sentence_LS = []
    while len(sentence.encode('utf-8')) > maxIndex:
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


def refreshPanelParameter():  # =========配置渲染面板==========================
    try:
        refresh_oneSentenceOneDayLable()
    except:
        pass


def off_dyn_cycleCheck():
    mc.cycleCheck(e=False)
    mc.setAttr(u'defaultRenderGlobals.preMel', "cycleCheck -e off", type="string")
    all_pt = mc.ls(type=u'particle', l=True)
    if len(all_pt) > 0:
        for e_p in all_pt:
            mc.setAttr(u'%s.isDynamic' % e_p, 0)

    mel.eval("OptimizeScene")


def del_wr_t_clr_bf():
    all_wtcb = mc.ls(type=u'writeToColorBuffer')
    if len(all_wtcb) > 0:
        mc.delete(all_wtcb)
        print u'writeToCOlorBuffer Nodes Deleted'
    mc.setAttr(u'mentalrayGlobals.exportVerbosity', 0)
    mc.setAttr(u'mentalrayGlobals.renderVerbosity', 0)
    mc.setAttr(u'mentalrayGlobals.exportMessages', 0)


def cleanUp_noClr_file():
    docp.clean_up_no_clr_rndFile()


def imporove_crowdFishMat():
    sel_fishBody = mc.ls(sl=True, l=True)[0]
    get_bodyShape = [sh_nd for sh_nd in mc.listRelatives(sel_fishBody, c=True, s=True, ni=True) if sh_nd.find(u'_body_') > -1][0]

    get_con_sg = mc.listConnections(get_bodyShape, type=u'shadingEngine')[0]
    get_mat = mc.listConnections(u'%s.surfaceShader' % get_con_sg)[0]
    mc.select(get_mat)
    mat_con_ksClr = mc.listConnections(u'%s.KsColor' % get_mat, p=True, c=True)
    if mat_con_ksClr:
        mc.disconnectAttr(mat_con_ksClr[1], mat_con_ksClr[0])
    mc.setAttr(u'%s.KsColor' % get_mat, 0.25, .25, .25, type=u'double3')


def export_sel_objs_with_rndly():
    if mc.pluginInfo('mtoa', l=True, q=True):
        mc.unloadPlugin(u'mtoa', f=True)
    rls = [rl for rl in mc.ls(type=u'renderLayer') if not rl.find(u'defaultRenderLayer') > -1]
    mc.select(cl=True)
    if rls != []:
        for each_rl in rls:
            # ly_mmb_root = [docp.getParent_root(each_mmb) for each_mmb in mc.editRenderLayerMembers(each_rl, q=True, fn=True)]
            # ly_mmb_root = [ly_mmb_root[i] for i in range(len(ly_mmb_root)) if ly_mmb_root[i] not in ly_mmb_root[:i]]
            # mc.select(ly_mmb_root, add=True)
            mc.select(mc.editRenderLayerMembers(each_rl, q=True, fn=True), add=True)
        mc.select(rls, add=True)
        nr_dl = docp.get_noRnd_DL()
        if nr_dl:
            mc.select(nr_dl, add=True)
        rnd_cam = docp.config_shotFile_cameraParameter()
        if rnd_cam:
            mc.select(rnd_cam, add=True)
    else:
        mc.select(all=True)
    file_filter = u'Maya ASCII (*.ma);;Maya Binary (*.mb);;'
    file_svas_name = mc.fileDialog2(cap=u'ExportSelect', fileFilter=file_filter)
    if file_svas_name:
        mc.file(file_svas_name, f=True, options=u'v=0', typ=u'mayaAscii', pr=True, es=True)


def del_nonDeformHistory_forAllSet():
    allSetMeshShapes_nrf = [d for d in mc.ls(typ=u'mesh', ni=True, l=True) if d.find(u'do4_s') > -1 and not mc.referenceQuery(d, inr=True)]
    all_nonCache_meshes_nrf = []
    for each_mesh in allSetMeshShapes_nrf:
        if not check_cache_GEO(each_mesh) and docp.nodeIsVisible(d):
            all_nonCache_meshes_nrf.append(each_mesh)
    mc.select(all_nonCache_meshes_nrf, r=True)
    mel.eval('BakeNonDefHistory')
    #     print u'+++++++++++++++++++++DELETE Non-Deform History Of SetObjectGroup++++++++++++++++++++++++++++++++++++++++++++'


def check_cache_GEO(meshShape):
    cache_History = (each_hist for each_hist in mc.listHistory(meshShape))
    is_CACHE_Drive = False
    for each_hist in cache_History:
        if mc.nodeType(each_hist) == u'cacheFile':
            is_CACHE_Drive = True
            break
    return is_CACHE_Drive


def check_polyTransHis_GEO(meshShape):
    all_his = (each_hist for each_hist in mc.listHistory(meshShape))
    with_polyTransHis = False
    for each_his in all_his:
        if mc.nodeType(each_his) == u'polyTransfer':
            with_polyTransHis = True
    return with_polyTransHis


def list_cache_Meshes():
    allMesh = cmds.ls(type='mesh', l=True)
    allCachedMesh = []
    for m in allMesh:
        for h in cmds.listHistory(m):
            if cmds.nodeType(h) == "cacheFile":
                allCachedMesh.append(m)
                break
    return allCachedMesh

if __name__ == "__main__":
    pass
