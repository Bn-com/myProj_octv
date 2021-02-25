# -*- coding: utf-8 -*-
'''
Created on 2012-11-262012

@author: zhangben
'''
import maya.cmds as mc
import re
import os
import random
import maya.mel as mel
import random as rd

dyn_v_m = []
dyn_control_outShot = []
dyn_control_inShot = []
coralVegs = []
aquatic_grpA = []
aquatic_grpB = []

loseCacheVegs = []


def do3_vdp_delWrapedBTCmd():
    mel.eval("source \"//file-cluster/gdc/Resource/Support/Maya/projects/DODIII/do3_skGrassCheck.mel\"; do3_skGrassCheck()")


def do3_vdp_selDynBTCmd():
    global dyn_control_inShot
    mc.select(dyn_control_inShot)


def do3_vdp_openAllBTCmd():
    mc.control("veg_dyn_parameter", e=True, enable=True)
    mc.button("selDynBT", e=True, en=True)
    mc.scriptJob(ka=True)
    do3_openAllVegDyn()


def do3_vdp_IsoDVBTCmd():

    mc.button("selectVegButton", e=True, en=True)
    mc.control("selectVegButton", e=True, en=True)
    mc.button("selDynBT", e=True, en=True)
    sel_cam_STARTHere()


def sel_cam_STARTHere():  # ========选择一个摄像机，从这里开始============================
    selCams = mc.ls(sl=True, l=True)
    if len(selCams) != 0:
        do3_ISO_control(selCams)
    else:
        do3_ISO_control()
#==========================================================================


def do3_openAllVegDyn():  # ===不做选择，配置所有有动态的植物控制器到全局变量dyn_v_m中===========
    global dyn_v_m
    allNurbsCruves = mc.ls(type="nurbsCurve")
    for j in range(len(allNurbsCruves)):
        if mc.listAttr(mc.listRelatives(allNurbsCruves[j], p=True, f=True)[0], string="shake_speed") != None:
            dyn_v_m.append(mc.listRelatives(allNurbsCruves[j], p=True, f=True)[0])

    dyn_v_m = [dyn_v_m[j] for j in range(len(dyn_v_m)) if dyn_v_m[j] not in dyn_v_m[:j]]
    dyn_v_m = [dyn_v_m[k] for k in range(len(dyn_v_m)) if mc.listRelatives(dyn_v_m[k], ad=True, c=True, type="mesh") != None]
    # print dyn_v_m
    do3_evaluateVariable(1)
#=================程序判定镜头中全部的动态水草的控制器，并ISO显示==为dyn_v_m赋值===============


def do3_ISO_control(selCams=["persp"]):
#selCams = mc.ls(sl=True)
    global dyn_v_m
    camShape = mc.listRelatives(selCams[0], shapes=True)
    if mc.nodeType(camShape[0]) != "stereoRigCamera" and mc.nodeType(camShape[0]) != "camera":
        mc.error("你选择了一个不是摄像机的物体")
        return
    allNurbsCruves = mc.ls(type="nurbsCurve")
    for j in range(len(allNurbsCruves)):
        if mc.listAttr(mc.listRelatives(allNurbsCruves[j], p=True, f=True)[0], string="shake_speed") != None:
            dyn_v_m.append(mc.listRelatives(allNurbsCruves[j], p=True, f=True)[0])

    dyn_v_m = [dyn_v_m[j] for j in range(len(dyn_v_m)) if dyn_v_m[j] not in dyn_v_m[:j]]
    dyn_v_m = [dyn_v_m[k] for k in range(len(dyn_v_m)) if mc.listRelatives(dyn_v_m[k], ad=True, c=True, type="mesh") != None]
    allEditors = mc.lsUI(editors=True)
    stereoEditors = [allEditors[k] for k in range(len(allEditors)) if allEditors[k] == "StereoPanelEditor"]
    mc.select(dyn_v_m, r=True)

    if(mc.nodeType(selCams[0]) == "stereoRigTransform"):
        mel.eval('stereoCameraSwitchToCamera %s %s' % (selCams[0], get_currentActivViewPanel()))
        mc.modelEditor(stereoEditors[0], e=True, allObjects=False)
        mc.modelEditor(stereoEditors[0], e=True, nurbsCurves=True)
        mc.modelEditor(stereoEditors[0], e=True, polymeshes=True)
        mc.isolateSelect(stereoEditors[0], state=1)
        mc.isolateSelect(stereoEditors[0], addSelected=1)
        mc.select(cl=True)
    else:
        mel.eval("lookThroughModelPanel %s %s" % (selCams[0], get_currentActivViewPanel()))

        mc.isolateSelect(get_currentActivViewPanel(), state=1)
        mc.isolateSelect(get_currentActivViewPanel(), addSelected=True)
        mc.modelEditor(get_currentActivViewPanel(), e=True, allObjects=False)
        mc.modelEditor(get_currentActivViewPanel(), e=True, nurbsCurves=True)
        mc.modelEditor(get_currentActivViewPanel(), e=True, polymeshes=True)
        # mc.isolateSelect(get_currentActivViewPanel(),state=0)
        # mc.isolateSelect(get_currentActivViewPanel(),state=1)
    mc.select(cl=True)
    return dyn_v_m


#====================选择镜头内的动态水草，确定各变量组成员 即：全部动态水草，镜头内，镜头外，镜头内水草A组，镜头内B组，镜头内珊瑚========================================
def do3_evaluateVariable(all=0):  # ==========选择镜头内的动态水草，确定各变量组成员 ===========
    global dyn_v_m
    global dyn_control_outShot
    global dyn_control_inShot
    global coralVegs
    global aquatic_grpA
    global aquatic_grpB
    # print dyn_v_m
    if all == 1:
        dyn_control_inShot = get_parentsGrp_By_levelNum(dyn_v_m, "mesh", 3)
        dyn_control_outShot = [dyn_v_m[k] for k in range(len(dyn_v_m)) if dyn_v_m[k] not in dyn_control_inShot]

        # print '\n'.join(dyn_control_inShot)
        coralVegs = do3_return_speceialVeg(dyn_control_inShot, "coral")
        aquaticVegs = do3_return_speceialVeg(dyn_control_inShot, "aquatic")

        aquatic_grpB = do3_get_specAquatic(aquaticVegs, "(geoC)*(aquatic)*")
        aquatic_grpA = [aquaticVegs[m] for m in range(len(aquaticVegs)) if aquaticVegs[m] not in aquatic_grpB]
    else:
        # mc.select(dyn_v_m)
        dyn_control_inShot = get_parentsGrp_By_levelNum(mc.ls(sl=True, l=True), "mesh", 3)
        dyn_control_outShot = [dyn_v_m[k] for k in range(len(dyn_v_m)) if dyn_v_m[k] not in dyn_control_inShot]

        coralVegs = do3_return_speceialVeg(dyn_control_inShot, "coral")
        aquaticVegs = do3_return_speceialVeg(dyn_control_inShot, "aquatic")

        aquatic_grpB = do3_get_specAquatic(aquaticVegs, "(geoC)*(aquatic)*")
        aquatic_grpA = [aquaticVegs[m] for m in range(len(aquaticVegs)) if aquaticVegs[m] not in aquatic_grpB]

#==============================================================


def do3_sel_control():
    veg_objs = mc.ls(sl=True, l=True)
    mc.select(get_parentsGrp_By_levelNum(veg_objs, "mesh", 3), r=True)


def Null():  # =========market line====下面的程序设定对应组别的水草的速度参数====================
    pass
#==================================================


def do3_amendExpCode(needDynVeg=dyn_v_m):  # ============修改cachefile 连接参数的表达式内容================
    global loseCacheVegs

    for eachCon in needDynVeg:
        con_expNodes = mc.listConnections(eachCon, type="expression")
        if con_expNodes != None:
            con_expNodes = [con_expNodes[k] for k in range(len(con_expNodes)) if con_expNodes[k] not in con_expNodes[:k]]
            for con_expNode in con_expNodes:
                expCode = mc.getAttr(con_expNode + ".expression")
                codeSplit = expCode.split("\n")
                codeSplit[1] = "        float $shot_sf_of = $shot_startFrame - 20;"
                new_expCode = "\n".join(codeSplit)

                mc.expression(con_expNode, e=True, ae=True, uc=all, s=new_expCode)

        else:
            loseCacheVegs.append(eachCon)
    return loseCacheVegs

#==============根据变量成员，配置不同的速度参数===================================


def do3_aotuSet_veg_shakeSpeed(speedLevel=1):  # ==============根据变量成员，配置不同的速度参数===
    global dyn_v_m
    global dyn_control_outShot
    global dyn_control_inShot
    global coralVegs
    global aquatic_grpA
    global aquatic_grpB
    do3_set_veg_shakeSpeed(dyn_control_inShot, coralVegs, aquatic_grpA, aquatic_grpB, speedLevel)

#===================以下为自动完成配置参数部分：自动设定水草摆动的速度参数以及打开水草摆动开关==============================================


def do3_set_veg_shakeSpeed(allGrp, coralGrp, aq_SPA, aq_SPB, speedLevel=1):  # ==========打开水草摆动开关，设定速度

    do3_amendExpCode(allGrp)
    if speedLevel == 0:
        for eachOne in allGrp:
            mc.setAttr(eachOne + ".shake_toggle", 0)
    if speedLevel == 1:
        if len(aq_SPA) != 0:
            for each_A in aq_SPA:
                mc.setAttr(each_A + ".shake_speed", 20)
                mc.setAttr(each_A + ".shake_bias", rd.randint(0, 19))
            #mc.setAttr(each_A + ".shake_toggle",1)
        if len(aq_SPB) != 0:
            for each_B in aq_SPB:
                #mc.setAttr(each_B + ".shake_toggle",1)
                mc.setAttr(each_B + ".shake_speed", 15)
                mc.setAttr(each_B + ".shake_bias", rd.randint(0, 19))
        if len(coralGrp) != 0:
            for each_coral in coralGrp:
                #mc.setAttr(each_coral + ".shake_toggle",1)
                mc.setAttr(each_coral + ".shake_speed", 25)
                mc.setAttr(each_coral + ".shake_bias", rd.randint(0, 19))
        for eachOne in allGrp:
            mc.setAttr(eachOne + ".shake_toggle", 1)
    if speedLevel == 2:
        if len(aq_SPA) != 0:
            for each_A in aq_SPA:
                #mc.setAttr(each_A + ".shake_toggle",1)
                mc.setAttr(each_A + ".shake_speed", 28)
                mc.setAttr(each_A + ".shake_bias", rd.randint(0, 19))
        if len(aq_SPB) != 0:
            for each_B in aq_SPB:
                #mc.setAttr(each_B + ".shake_toggle",1)
                mc.setAttr(each_B + ".shake_speed", 22)
                mc.setAttr(each_B + ".shake_bias", rd.randint(0, 19))
        if len(coralGrp) != 0:
            for each_coral in coralGrp:
                #mc.setAttr(each_coral + ".shake_toggle",1)
                mc.setAttr(each_coral + ".shake_speed", 38)
                mc.setAttr(each_coral + ".shake_bias", rd.randint(0, 19))
        for eachOne in allGrp:
            mc.setAttr(eachOne + ".shake_toggle", 1)
    if speedLevel == 3:
        if len(aq_SPA) != 0:
            for each_A in aq_SPA:
                #mc.setAttr(each_A + ".shake_toggle",1)
                mc.setAttr(each_A + ".shake_speed", 40)
                mc.setAttr(each_A + ".shake_bias", rd.randint(0, 19))
        if len(aq_SPB) != 0:
            for each_B in aq_SPB:
                #mc.setAttr(each_B + ".shake_toggle",1)
                mc.setAttr(each_B + ".shake_speed", 35)
                mc.setAttr(each_B + ".shake_bias", rd.randint(0, 19))
        if len(coralGrp) != 0:
            for each_coral in coralGrp:
                #mc.setAttr(each_coral + ".shake_toggle",1)
                mc.setAttr(each_coral + ".shake_speed", 55)
                mc.setAttr(each_coral + ".shake_bias", rd.randint(0, 19))
        for eachOne in allGrp:
            mc.setAttr(eachOne + ".shake_toggle", 1)


def do3_set_selVeg_shakeSpeed(speedLevel):  # ========设定选择的水草的速度参数====================
    # speedLevel=0
    select_veg_control_sqA = []
    select_veg_control_sqB = []
    select_veg_control_coral = []

    sel_objs = mc.ls(sl=True, l=True)
    sel_vegs_control_ALL = do3_select_moveControl(sel_objs)

    select_veg_control_coral = do3_return_speceialVeg(sel_vegs_control_ALL, "coral")
    select_aquatic = do3_return_speceialVeg(sel_vegs_control_ALL, "aquatic")
    select_veg_control_sqB = do3_get_specAquatic(select_aquatic, "(geoC)*(aquatic)*")
    select_veg_control_sqA = [select_aquatic[j] for j in range(len(select_aquatic)) if select_aquatic[j] not in select_veg_control_sqB]

    do3_set_veg_shakeSpeed(sel_vegs_control_ALL, select_veg_control_coral, select_veg_control_sqA, select_veg_control_sqB, speedLevel)


#==============针对水草：由控制曲线，判断水草GEO组的编号，分配到的指定的组======================
def do3_get_specAquatic(aquatics, keyCharactor):  # ==============把水草分配的指定的组
#keyCharactor = "(geoC)*(aquatic)*"
#aquatics = aquaticVegs
    specAquatic = []
    for each in aquatics:
        aquaticName = mc.listRelatives(each, c=True, type="transform")[0].split("_")[-1]
        s = re.search(keyCharactor, aquaticName)
        if str(s.group()) != "":
            specAquatic.append(each)
    return specAquatic


#===================在提供的植物中，找出指定类型的植物=====================
def do3_return_speceialVeg(allVeg, vegType):  # ===========在提供的植物中，找出指定类型的植物=====================
    #allVeg = dyn_control_inShot
    #vegType ="aquatic"
    p = re.compile(vegType)
    sepc_veg = []
    for each in allVeg:
        #each = allVeg[2]
        vegName = mc.listRelatives(each, c=True, ad=True, type="mesh")[0].split(":")[-1].split("_")[3]
        if p.search(vegName) != None:
            sepc_veg.append(each)
    return sepc_veg


#=====================hide outShot vegetables ============================================================
def do3_outShotVeg_setVis(hideToggle):  # =================hide outShot vegetables ========================
    global dyn_control_outShot
    for j in range(len(dyn_control_outShot)):
        mc.setAttr(dyn_control_outShot[j] + ".visibility", hideToggle)
#=======================create diplayLaer stor outShot vegetables and show or un show layer========================


def do3_creatNoRender_vegetableDL():
    global dyn_v_m
    global dyn_control_outShot
    global dyn_control_inShot

    if (mc.objExists("noRenderVagetable")):
        visState = mc.getAttr("noRenderVagetable.visibility")
        if visState:
            mc.setAttr("noRenderVagetable.visibility", 0)
        else:
            mc.setAttr("noRenderVagetable.visibility", 1)
    else:
        mc.createDisplayLayer(name="noRenderVagetable", empty=True)
        mc.editDisplayLayerMembers("noRenderVagetable", dyn_control_outShot)
        mc.setAttr("noRenderVagetable.visibility", 0)
#=====================得到指定类型物体的指定层级的父节点===注意物体需要FullName==========================================


def get_parentNode_By_levelNum(selectObj, objType, levelNum=1):  # =====返回物体的子物体中指定类型的物体的指定层级的父节点=================================
    controlCurve = get_curveParent(selectObj)
    return controlCurve
#====================由物体类型判定得到控制曲线节点=================================


def get_curveParent(eachNode):  # ====================由物体类型判定得到控制曲线节点=================================
    parentNode = eachNode
    while mc.listRelatives(parentNode, s=True, type="nurbsCurve") == None:
        parentNode = mc.listRelatives(parentNode, p=True, f=True)[0]
    return parentNode

#==============根据物体长名字字符串截取指定层级的父节点名字=========================================


def get_parentNode_By_LONGNAMElevelNum(selectObj, objType, levelNum=1):  # =====返回物体的子物体中指定类型的物体的指定层级的父节点=================================
    # selectObj = mc.ls(sl=True,l=True)[0]  objType = "mesh" levelNum=2
    index = levelNum * -1
    childrens = mc.listRelatives(selectObj, f=True, ad=True, c=True, type=objType)
    parentNode = ""
    if childrens != None:
        parentNode = "|".join(childrens[0].split("|")[:index])
    return parentNode


def get_parentsGrp_By_levelNum(selectObjs, objType, GrplevelNum=1):  # =====得到指定类型物体们的指定层级的父节点们
    # selectObjs = dyn_v_m  GrplevelNum=3 objType="mesh"
    # print '\n'.join(selectObjs)
    controlMoves = []
    for eachSel in selectObjs:
       # print selectObjs.index(eachSel),"     ",get_parentNode_By_levelNum(eachSel,objType,GrplevelNum)
        #eachSel = selectObjs[0]
        # print get_parentNode_By_levelNum(eachSel,objType,GrplevelNum)
        # mc.select(selectObjs[220])
        controlMoves.append(get_parentNode_By_levelNum(eachSel, objType, GrplevelNum))
    controlMoves = [controlMoves[i] for i in range(len(controlMoves)) if controlMoves[i] not in controlMoves[:i]]
    return controlMoves

#=================================================================================================
#=================================================================================================
#===================以上为自动完成配置参数部分==============================================


def do3_select_moveControl(sel_vegs):  # ========返回选择物体们的曲线控制器====================
    allCon = []
    for veg in sel_vegs:
        sel_type = mc.nodeType(mc.listRelatives(veg, shapes=True, f=True, ni=True)[0])
        if sel_type == "mesh":
            allCon.append(get_parentNode_By_levelNum(veg, "mesh", 2))
        if sel_type == "nurbsCurve":
            allCon.append(veg)
    allCon = [allCon[i] for i in range(len(allCon)) if allCon[i] not in allCon[:i]]
    return allCon
#==================================================================


def do3_select_loseCacheVegs():  # =========选择那些丢失了动态缓存的植物们======================
    global loseCacheVegs
    if len(loseCacheVegs) != 0:
        mc.select(loseCacheVegs, r=True)


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
#=======================================================================================


def Null_2():
    pass
#=================以下 重新替换丢失cache的植物===================================================


def do3_dyn_veg_index(dynVeg_con, veg_style):  # ==========获得植物的编号“ABCD"===========================

    #dynVeg_con = no_dyn_vegs[0]
    veg_index = ""
    meshShape = mc.listRelatives(dynVeg_con, c=True, ad=True, type="mesh", f=True)
    if len(meshShape) == 0:
        mc.error("%s has no meshShape child" % (dynVeg_con))
    if veg_style == "coral":
        veg_index = meshShape[0].split(":")[-1].split("_")[3][-1]
    if veg_style == "aquatic":
        mesh_trans = mc.listRelatives(meshShape, p=True, f=True)[0]
        veg_index = mc.listRelatives(mesh_trans, p=True, f=True)[0].split(":")[-1].split("_")[-1][3]
    p = re.compile("[A-Z]+")
    if p.match(veg_index) == None:
        mc.error("%s children has wrong construction" % (dynVeg_con))
    return veg_index
