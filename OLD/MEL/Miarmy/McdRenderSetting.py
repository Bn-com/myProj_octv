#!/usr/bin/env python

import maya.cmds as cmds
from McdGeneral import *
from McdRenderSettingGUI import *


def McdRenderSetExt(ext):
    cmds.menuItem(l = "name.#.ext")
    cmds.menuItem(l = "name.ext.#")
    cmds.menuItem(l = "name.#")
    cmds.menuItem(l = "name#.ext")
    cmds.menuItem(l = "name_#.ext")
    
    if ext == 0:
        cmds.optionMenuGrp("rsext_om", e = True, v = "name.#.ext")
    elif ext == 1:
        cmds.optionMenuGrp("rsext_om", e = True, v = "name.ext.#")
    elif ext == 2:
        cmds.optionMenuGrp("rsext_om", e = True, v = "name.#")
    elif ext == 3:
        cmds.optionMenuGrp("rsext_om", e = True, v = "name#.ext")
    elif ext == 4:
        cmds.optionMenuGrp("rsext_om", e = True, v = "name_#.ext")
    else:
        cmds.optionMenuGrp("rsext_om", e = True, v = "name.#.ext")

def om_rs_changeExtension(control, nodeName, attrName):
    qValue = cmds.optionMenuGrp(control, q = True, v = True)
    setValue = 0
    if qValue == "name.#.ext":
        setValue = 0
    elif qValue == "name.ext.#":    
        setValue = 1
    elif qValue == "name.#":
        setValue = 2
    elif qValue == "name#.ext":
        setValue = 3
    elif qValue == "name_#.ext":
        setValue = 4
    else:
        setValue = 0
    
    cmds.setAttr(nodeName + "." + attrName, setValue)
    updateAndDisplaySummary()

def McdRenderSetFmt(fmt):
    cmds.menuItem(l = "Tif(tiff)")
    cmds.menuItem(l = "Tif16(tiff)")
    cmds.menuItem(l = "Targa(tga)")
    cmds.menuItem(l = "PNG(png)")
    
    if fmt == 0:
        cmds.optionMenuGrp("rsfmt_om", e = True, v = "Tif(tiff)")
    elif fmt == 1:
        cmds.optionMenuGrp("rsfmt_om", e = True, v = "Tif16(tiff)")
    elif fmt == 2:
        cmds.optionMenuGrp("rsfmt_om", e = True, v = "Targa(tga)")
    elif fmt == 3:
        cmds.optionMenuGrp("rsfmt_om", e = True, v = "PNG(png)")
    else:
        cmds.optionMenuGrp("rsfmt_om", e = True, v = "Tif(tiff)")
        
def om_rs_changeFormat(control, nodeName, attrName):
    qValue = cmds.optionMenuGrp(control, q = True, v = True)
    setValue = 0
    if qValue == "Tif(tiff)":
        setValue = 0
    elif qValue == "Tif16(tiff)":
        setValue = 1
    elif qValue == "Targa(tga)":
        setValue = 2
    elif qValue == "PNG(png)":
        setValue = 3
    else:
        setValue = 0
    
    cmds.setAttr(nodeName + "." + attrName, setValue)
    updateAndDisplaySummary()

def McdRenderSetFilterFunc(filterfunc):
    cmds.menuItem(l = "None")
    cmds.menuItem(l = "Box")
    cmds.menuItem(l = "Triangle")
    cmds.menuItem(l = "Catmull-Rom")
    cmds.menuItem(l = "Gaussian")
    cmds.menuItem(l = "Sinc")
    
    if filterfunc == 0:
        cmds.optionMenuGrp("rsffc_om", e = True, v = "None")
    elif filterfunc == 1:
        cmds.optionMenuGrp("rsffc_om", e = True, v = "Box")
    elif filterfunc == 2:
        cmds.optionMenuGrp("rsffc_om", e = True, v = "Triangle")
    elif filterfunc == 3:
        cmds.optionMenuGrp("rsffc_om", e = True, v = "Catmull-Rom")
    elif filterfunc == 4:
        cmds.optionMenuGrp("rsffc_om", e = True, v = "Gaussian")
    elif filterfunc == 5:
        cmds.optionMenuGrp("rsffc_om", e = True, v = "Sinc")
    else:
        cmds.optionMenuGrp("rsffc_om", e = True, v = "None")

def om_rs_changeFilterFunc(control, nodeName, attrName):
    qValue = cmds.optionMenuGrp(control, q = True, v = True)
    setValue = 0
    if qValue == "None":
        setValue = 0
    elif qValue == "Box":
        setValue = 1
    elif qValue == "Triangle":
        setValue = 2
    elif qValue == "Catmull-Rom":
        setValue = 3
    elif qValue == "Gaussian":
        setValue = 4
    elif qValue == "Sinc":
        setValue = 5
    else:
        setValue = 0
    
    cmds.setAttr(nodeName + "." + attrName, setValue)

def McdRenderSetCam(globalNode):
    allCam = cmds.ls(type = "camera")
    cmds.menuItem(l = "All Render Cams (Stereo & Multi)")
    
    renderableCam = ""
    nbRenderCam = 0
    isMulti = False
    if allCam != [] and allCam != None:
        for i in range(len(allCam)):        
            cmds.menuItem(l = allCam[i])
            if cmds.getAttr(allCam[i] + ".renderable") == 1:
                renderableCam = allCam[i]
                nbRenderCam += 1

    if renderableCam == "":
        cmds.menuItem(l = "None")
        
    if nbRenderCam > 1:
        isMulti = True
        
    renderCamUpdate(globalNode, renderableCam, isMulti)
    
def renderCamUpdate(globalNode, renderableCam, isMulti):
    if isMulti:
        cmds.optionMenuGrp("rsrdc_om", e =True, v = "All Render Cams (Stereo & Multi)")
    else:
        if renderableCam != "":
            cmds.optionMenuGrp("rsrdc_om", e =True, v = renderableCam)
        else:
            cmds.optionMenuGrp("rsrdc_om", e = True,v = "None")
            
        cmds.setAttr(globalNode + ".camera", renderableCam, type = "string" )
            
            
def om_rs_changeCam(control, nodeName):
    qValue = cmds.optionMenuGrp(control, q = True, v = True)
    if qValue == "All Render Cams (Stereo & Multi)":
        cmds.setAttr(nodeName + ".camera", qValue, type = "string")
    else: 
        if qValue != "None":
            allCam = cmds.ls(type = "camera")
            if allCam != [] and allCam != None:
                for i in range(len(allCam)):
                    try:
                        cmds.setAttr(allCam[i] + ".renderable", 0)
                    except:
                        pass
            try:
                cmds.setAttr(qValue + ".renderable",1)
            except:
                pass
            
        cmds.setAttr(nodeName + ".camera", qValue, type = "string")
        
        camMask = cmds.getAttr(qValue + ".mask")
        camDepth = cmds.getAttr(qValue + ".depth")
        camMotion = cmds.getAttr(qValue + ".motionBlur")
        cmds.checkBoxGrp("rsapa_cbg", e = True, v1 = camMask)
        cmds.checkBoxGrp("rsdpt_cbg", e = True, v1 = camDepth)
        cmds.checkBoxGrp("rsmbr_cbg", e = True, v1 = camMotion)

        
def setCameraAttribOn(attrib):
    camName = cmds.optionMenuGrp("rsrdc_om", q = True, v = True)
    cmds.setAttr(camName + "." + attrib, True)
    
def setCameraAttribOff(attrib):
    camName = cmds.optionMenuGrp("rsrdc_om", q = True, v = True)
    cmds.setAttr(camName + "." + attrib, False)

def McdRenderSetPrs(globalNode):
    cmds.menuItem(l = "Custom")
    cmds.menuItem(l = "HD 720")
    cmds.menuItem(l = "HD 1080")
    cmds.menuItem(l = "PAL")
    cmds.menuItem(l = "NTSC")
    renderPresetUpdate(globalNode)
        
def renderPresetUpdate(globalNode):
    resX = cmds.getAttr(globalNode + ".resolutionX")
    resY = cmds.getAttr(globalNode + ".resolutionY")
    if resX == 1920 and resY == 1080:
        cmds.optionMenuGrp("rsprs_om", e = True, v = "HD 1080")
    elif resX == 1280 and resY == 720:
        cmds.optionMenuGrp("rsprs_om", e = True, v = "HD 720")
    elif resX == 720 and resY == 576:
        cmds.optionMenuGrp("rsprs_om", e = True, v = "PAL")
    elif resX == 720 and resY == 486:
        cmds.optionMenuGrp("rsprs_om", e = True, v = "PAL")
    else:
        cmds.optionMenuGrp("rsprs_om", e = True, v = "Custom")

def om_rs_changePresets(control, globalNode):
    qValue = cmds.optionMenuGrp(control, q = True, v = True)
    
    if qValue == "HD 720":
        resX = cmds.intFieldGrp("rsw_ifg", e = True, v1 = 1280)
        resY = cmds.intFieldGrp("rsh_ifg", e = True, v1 = 720)
        cmds.setAttr(globalNode + ".resolutionX", 1280)
        cmds.setAttr(globalNode + ".resolutionY", 720)
    elif qValue == "HD 1080":
        resX = cmds.intFieldGrp("rsw_ifg", e = True, v1 = 1920)
        resY = cmds.intFieldGrp("rsh_ifg", e = True, v1 = 1080)
        cmds.setAttr(globalNode + ".resolutionX", 1920)
        cmds.setAttr(globalNode + ".resolutionY", 1080)
    elif qValue == "PAL":
        resX = cmds.intFieldGrp("rsw_ifg", e = True, v1 = 720)
        resY = cmds.intFieldGrp("rsh_ifg", e = True, v1 = 576)
        cmds.setAttr(globalNode + ".resolutionX", 720)
        cmds.setAttr(globalNode + ".resolutionY", 576)
    elif qValue == "NTSC":
        resX = cmds.intFieldGrp("rsw_ifg", e = True, v1 = 720)
        resY = cmds.intFieldGrp("rsh_ifg", e = True, v1 = 486)
        cmds.setAttr(globalNode + ".resolutionX", 720)
        cmds.setAttr(globalNode + ".resolutionY", 486)
    
    

def setSingleNumericAttrGrp(option, control, nodeName, attrName):    
    #option: 0: bool, 1:int, 2: float
    if option == 0:
        qValue = cmds.checkBoxGrp(control, q= True, v1 = True)
        if control == "rsmbd_cbg" or control == "rsmb_cbg":
            if qValue == 1:
                cmds.confirmDialog(t = "Note", m = "Notice: motion blur can only work on agents with cache.\n" + \
                                                    "Otherwise, the simulation will break.")
        if control == "rsp_normal":
            if qValue == 1:
                if cmds.checkBoxGrp("rsp_color", q= True, v1 = True) == 0:
                    cmds.confirmDialog(t = "Note", m = "Notice:\nPlease check on \"color\" pass.\nOtherwise, no result." )
        cmds.setAttr(nodeName + "." + attrName, qValue)
    elif option == 1:
        qValue = cmds.intFieldGrp(control, q= True, v1 = True)
        cmds.setAttr(nodeName + "." + attrName, qValue)
    elif option == 2:
        qValue = cmds.floatFieldGrp(control, q= True, v1 = True)
        cmds.setAttr(nodeName + "." + attrName, qValue)
    updateAndDisplaySummary()
    renderPresetUpdate(nodeName)
        
        
def setSingleNumericAttrSliderGrp(option, control, nodeName, attrName):
    #option: 0: bool, 1:int, 2: float
    if option == 0:
        pass
    elif option == 1:
        qValue = cmds.intSliderGrp(control, q= True, v = True)
        cmds.setAttr(nodeName + "." + attrName, qValue)
    elif option == 2:
        qValue = cmds.floatSliderGrp(control, q= True, v = True)
        cmds.setAttr(nodeName + "." + attrName, qValue) 
    updateAndDisplaySummary()
        
def setStringAttrGrp(isPath, control, nodeName, attrName):
    
    imagesDir = cmds.workspace( expandName ="images" ) + "/"
    qValue = cmds.textFieldGrp(control, q = True, tx = True)
    qValue = qValue.replace("\\", "/")
    
    if control == "rspp_ph":
        if ((not os.access(qValue + "/McdRunProgram.exe", os.R_OK)) and (not os.access(qValue + "/McdRunProgram" , os.R_OK)) and (not os.access(qValue + "/McdRManDSO.so", os.R_OK)) and (not os.access(qValue + "/McdRManDSO.dll", os.R_OK))):
            cmds.confirmDialog(t = "Error", m = "Can not find McdRunProgram in the path you filled, will cause error when render.")
    
    if isPath == 1:
        access = os.access(qValue, os.W_OK)
        if access == False:
            qValue = "<Use project folder>"
            cmds.textFieldGrp(control, e = True, tx = qValue)
            qValue = imagesDir
    
    if isPath != 1:
        if qValue != "" and qValue != "<Use project folder>":
            cmds.textFieldGrp(control, e = True, tx = qValue)
        
    cmds.setAttr(nodeName + "." + attrName, qValue, type = "string")
    updateAndDisplaySummary()
    
def updateAndDisplaySummary():
    # ready
    imagesDir = cmds.workspace( expandName ="images" ) + "/"
    fmt = cmds.optionMenuGrp("rsfmt_om", q = True, v = True)
    ext = cmds.optionMenuGrp("rsext_om", q = True, v = True)
    
    # upgrade in future:
    setFmt = "tiff"
    if fmt == "Tiff(tiff)":
        setFmt = "tiff"
    elif fmt == "Tif16(tiff)":
        setFmt = "tiff"
    elif fmt == "Targa(tga)":
        setFmt = "tga"
    elif fmt == "PNG(png)":
        setFmt = "png"
    outFdr = cmds.textFieldGrp("rsfdr_tfg", q = True, tx = True)
    spx = cmds.intSliderGrp("rssx_isg", q = True, v = True)
    spy = cmds.intSliderGrp("rssy_isg", q = True, v = True)
    padding = cmds.intSliderGrp("rsfp_ifg", q = True, v = True)
    
    pad = ""
    for i in range(padding):
        pad += "#"
    
    # modify path:
    if outFdr == "<Use project folder>":
        outFdr = imagesDir
        
    cmds.text("rsop_t", e = True, l = "Path: " + outFdr)
    outNameBase = cmds.textFieldGrp("rspic_tfg", q = True, tx = True)
    
    setName = ""
    Dot = "."
    if spx == 1 and spy == 1:
        if ext == "name.#.ext":
            setName = outNameBase + Dot + pad + Dot + setFmt
        elif ext == "name.ext.#":
            setName = outNameBase + Dot + setFmt + Dot + pad
        elif ext == "name.#":
            setName = outNameBase + Dot + pad
        elif ext == "name#.ext":
            setName = outNameBase + pad + Dot + setFmt
        elif ext == "name_#.ext":
            setName = outNameBase + "_" + pad + Dot + setFmt
        else:
            setName = outNameBase + Dot + pad + Dot + setFmt
    else:
        if ext == "name.#.ext":
            setName = outNameBase+"_<x>_<y>_" + Dot + pad + Dot + setFmt
        elif ext == "name.ext.#":
            setName = outNameBase+"_<x>_<y>_" + Dot + setFmt + Dot + pad
        elif ext == "name.#":
            setName = outNameBase+"_<x>_<y>_" + Dot + pad
        elif ext == "name#.ext":
            setName = outNameBase+"_<x>_<y>_" + pad + Dot + setFmt
        elif ext == "name_#.ext":
            setName = outNameBase+"_<x>_<y>_" + "_" + pad + Dot + setFmt
        else:
            setName = outNameBase+"_<x>_<y>_" + "." + pad + Dot + setFmt
            
    # modify name:
    cmds.text("rsfn_t", e = True, l = "FileName: " + setName)
    
def copyResFromMaya():
    xRes = cmds.getAttr("defaultResolution.width")
    yRes = cmds.getAttr("defaultResolution.height")
    
    globalNode = McdListMcdGlobal()
    
    cmds.setAttr(globalNode + ".resolutionX", xRes)
    cmds.setAttr(globalNode + ".resolutionY", yRes)
    
    cmds.intFieldGrp("rsw_ifg", e= True, v1 = xRes)
    cmds.intFieldGrp("rsh_ifg", e= True, v1 = yRes)
    
    updateAndDisplaySummary()
    renderPresetUpdate(globalNode)
    
    
    
    
    
    
    
    
    
        
        