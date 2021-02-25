# -*- coding: utf-8 -*-
from maya.cmds import *
import maya.mel as mel
import os
try:
    import win32clipboard as w 
    import win32con
except:
    pass
mel.eval('source "zzjDelAllExtraChanls.mel";')
mel.eval('source "MayaManHelpers.mel";')


#delete all save node
#l to r rename



#first execute
try:
    a = ls(type = "MayaManNugget")[0]
    setAttr(a + ".NumCpus", 1)
    setAttr(a + ".BucketSizeX", 16)
    setAttr(a + ".BucketSizeY", 16)
    setAttr(a + ".GridSizeVal", 256)
except:
    pass


def deleteSNAll():
    #stat = confirmDialog(t = "Delete Save Node.", m = u"你确认删除所有的Save Node吗？")
    sn = ls(type = "saveNode")
    if sn != [] and sn != None:
        for i in range(len(sn)):
            try:
                delete(sn[i])
            except:
                pass
    else:
        confirmDialog(t = u"提示", m = u"没有检测到 Save Node.")
        

def Winx2L2RCamWrapper():
    try:
        allCam = ls(type = "camera")
        for i in range(len(allCam)):
            allConns = listConnections(allCam[i] + ".renderable")
            if allConns != None and allConns != []:
                for j in range(len(allConns)):
                    delete(allConns[j])
    except:
        pass
    ##//Serverone\CONTENT_4_GLOBAL\PRJ_winxII\SHOT_winxII\SQ_040\winxII_sq_040_sc_031\scenes\finishing
    
    #import cam and switch:
    #Rendercam
    #//serverone/CONTENT_4_GLOBAL/PRJ_winxII/SHOT_winxII/SQ_003/winxII_sq_003_sc_003/scenes/finishing
    ##//file-cluster/GDC/Projects/WinxClubII/Reference/FTP Download/09-12-18/Stereo_12_18_09/SQ_003/winxII_sq_003_sc_003/scenes/finishing
    #-------------------------------------------------------
    #
    sceneName = file(q=True, sn = True, shn =True)
    sections = sceneName.split("_")
    if len(sections) <3:
        confirmDialog(t = u"提示", m = u"文件名是错的，请正确命名文件")
        raise Exception("Invaild file name.")
     
    sq = sections[1]
    sc = sections[2]
    camDir = "//file-cluster/GDC/Projects/ROMA/PRJ_roma/SHOT_roma/sq_" + sq + "/roma_sq_" + sq + "_sc_" + sc + "/scenes/finishing"
    
    allCamBefore = ls(type = "camera")
    
    if os.access(camDir, os.R_OK) == True:
        stereoCam = ls("camera_stereoRx")
        
        if stereoCam == None or stereoCam == []:
            importCam = None
            allFiles = os.listdir(camDir)
            for i in range(len(allFiles)):
                if allFiles[i].find("_Rx.mb")>=0:
                    importCam = allFiles[i]
                    break
            if importCam != None:
                camPath = camDir + "/" + importCam
                file(camPath, i = True)
            else:
                confirmDialog(t = u"提示", m = u"没有找到“右眼”相机，请查看你的文件名，或者咨询TD")
                #raise Exception("found no camera to import.")
    else:
        confirmDialog(t = u"提示", m = u"没有找到相机存放的目录，请查看你的文件名，或者咨询TD")
        raise Exception("found no camera to import.")
    ##setCamera
    allCamAfter = ls(type = "camera")
    newCam = ""
    for i in range(len(allCamAfter)):
        if allCamAfter[i] not in allCamBefore:
            newCam = allCamAfter[i]
    if newCam != "":
        rightCamName = ls("camera_stereoRx")
        if rightCamName == None or rightCamName == []:
            newCamTrans = listRelatives(newCam, p = True)[0]
            rename(newCamTrans, "camera_stereoRx")
    
    #-----------------------------------------
    #import cam
    #set cam properties, renderable, off/on
    
    #change layer name
    #list all layer
    allRL = listConnections("renderLayerManager.renderLayerId")
    if len(allRL) == 1:
        confirmDialog(t = u"提示", m = u"请先建好层，再点此按钮")
        raise Exception("No render layer found.")
    
    #check is done:
    RDone = 0
    for i in range(len(allRL)):
        if allRL[i].find("_right")>0:
            RDone +=1
            break
    if RDone != 0:
        stat = confirmDialog(t = u"提示", m = u"发现你已经运用过转右眼相机，", b = [u"继续转右眼", u"转回左眼", u"取消"])
        changeLayer = 0
        if stat == u"转回左眼":
            Winx2L2RCamGoLeft()
        elif stat == u"继续转右眼":
            Winx2L2RCamGoRight()
        else:
            raise Exception("Break by user.")
    else:
        Winx2L2RCamGoRight()
        
   

        
def Winx2L2RCamGoLeft():
    #change the layer name
    layerList = listConnections("renderLayerManager.renderLayerId")
    for i in range(len(layerList)):
        try:
            newName = layerList[i].replace("_right", "_left")
	    if newName == layerList[i]:
		continue;
            rename(layerList[i], newName)
        except:
            confirmDialog(t = u"提示", m = layerList[i] + u" 无法改名，可能是非法层.")
    
    sceneName = file(q=True, sn = True, shn =True)
    if sceneName.find(".mb") > 0:
        try:
            mmn = ls(type = "MayaManNugget")[0]
            sR = getAttr(mmn + ".ShadingRate")
            pSX = getAttr(mmn + ".PixelSamplesX")
            pSY = getAttr(mmn + ".PixelSamplesY")
            pF = getAttr(mmn + ".PixelFilter")
            pFX = getAttr(mmn + ".PixelFilterX")
            pFY = getAttr(mmn + ".PixelFilterY")
            bsX = getAttr(mmn + ".BucketSizeX")
            bsY = getAttr(mmn + ".BucketSizeY")
            gSV = getAttr(mmn + ".GridSizeVal")
            uro = getAttr(mmn + ".UserRibOptions")
        except:
            raise Exception("nugget error 1")
        
        mel.eval("source \"rnd_wxII_FixBeforeRender.mel\";wxII_FixBeforeRender(\"project\");")
        
        try:
            setAttr(mmn + ".ShadingRate", sR)
            setAttr(mmn + ".PixelSamplesX", pSX)
            setAttr(mmn + ".PixelSamplesY", pSY)
            setAttr(mmn + ".PixelFilter", pF)
            setAttr(mmn + ".PixelFilterX", pFX)
            setAttr(mmn + ".PixelFilterY", pFY)
            setAttr(mmn + ".BucketSizeX", bsX)
            setAttr(mmn + ".BucketSizeY", bsY)
            setAttr(mmn + ".GridSizeVal", gSV)
            setAttr(mmn + ".UserRibOptions", uro, type = "string")
            
        except:
            raise Exception("nugget error 2")

        confirmDialog(t = u"提示", m = u"1，已经更改为“左”眼相机，\n2，文件已重命名，新名字在剪切板，请确认Check in")
    else:
        confirmDialog(t = u"提示", m = u"1，已经更改为“左”眼相机，系统为你自动运行了“网渲补”，\n2，文件已重命名，新名字在剪切板，请确认Check in")
    
    postSwitchSetup()
    postCopyCamAttr2Left()
    setClipboardFileName2Left()
    
    spaceLocator(name = "Gold999924k")
    delete("Gold999924k")
    

def Winx2L2RCamGoRight():
    #change the layer name
    layerList = listConnections("renderLayerManager.renderLayerId")
    for i in range(len(layerList)):
        try:
            newName = layerList[i].replace("_left", "_right")
	    if newName == layerList[i]:
		continue;
            rename(layerList[i], newName)
        except:
            confirmDialog(t = u"提示", m = layerList[i] + u" 无法改名，可能是非法层.")

    sceneName = file(q=True, sn = True, shn =True)
    if sceneName.find(".mb") > 0:
        try:
            mmn = ls(type = "MayaManNugget")[0]
            sR = getAttr(mmn + ".ShadingRate")
            pSX = getAttr(mmn + ".PixelSamplesX")
            pSY = getAttr(mmn + ".PixelSamplesY")
            pF = getAttr(mmn + ".PixelFilter")
            pFX = getAttr(mmn + ".PixelFilterX")
            pFY = getAttr(mmn + ".PixelFilterY")
            bsX = getAttr(mmn + ".BucketSizeX")
            bsY = getAttr(mmn + ".BucketSizeY")
            gSV = getAttr(mmn + ".GridSizeVal")
            uro = getAttr(mmn + ".UserRibOptions")
            
            
        except:
            raise Exception("nugget error 1")
        
        mel.eval("source \"rnd_wxII_FixBeforeRender.mel\";wxII_FixBeforeRender(\"project\");")
        
        try:
            setAttr(mmn + ".ShadingRate", sR)
            setAttr(mmn + ".PixelSamplesX", pSX)
            setAttr(mmn + ".PixelSamplesY", pSY)
            setAttr(mmn + ".PixelFilter", pF)
            setAttr(mmn + ".PixelFilterX", pFX)
            setAttr(mmn + ".PixelFilterY", pFY)
            setAttr(mmn + ".BucketSizeX", bsX)
            setAttr(mmn + ".BucketSizeY", bsY)
            setAttr(mmn + ".GridSizeVal", gSV)
            setAttr(mmn + ".UserRibOptions", uro, type = "string")
            
        except:
            raise Exception("nugget error 2")

        confirmDialog(t = u"提示", m = u"1，已经更改为“右”眼相机，\n2，文件已重命名，新名字在剪切板，请确认Check in")
    else:
        confirmDialog(t = u"提示", m = u"1，已经更改为“右”眼相机，系统为你自动运行了“网渲补”，\n2，文件已重命名，新名字在剪切板，请确认Check in")
    
    postSwitchSetup()
    postCopyCamAttr2Right()
    setClipboardFileName2Right()
    
    sceneName = file(q=True, sn = True, shn =True)
    if sceneName.find("_occlusionNormal")>0:
        yyResetExtraOutputChannelOnline()
        
    try:
        setAttr("camera_stereoRxShape.renderable", 1)
    except:
        pass
    spaceLocator(name = "Gold999924k")
    delete("Gold999924k")
    
def localFix2():
    try:
        mmn = ls(type = "MayaManNugget")[0]
        sR = getAttr(mmn + ".ShadingRate")
        pSX = getAttr(mmn + ".PixelSamplesX")
        pSY = getAttr(mmn + ".PixelSamplesY")
        pF = getAttr(mmn + ".PixelFilter")
        pFX = getAttr(mmn + ".PixelFilterX")
        pFY = getAttr(mmn + ".PixelFilterY")
        bsX = getAttr(mmn + ".BucketSizeX")
        bsY = getAttr(mmn + ".BucketSizeY")
        gSV = getAttr(mmn + ".GridSizeVal")
        uro = getAttr(mmn + ".UserRibOptions")
    except:
        raise Exception("nugget error 1")
    
    mel.eval("source \"rnd_wxII_FixBeforeRender.mel\";wxII_FixBeforeRender(\"project\");")
    
    try:
        setAttr(mmn + ".ShadingRate", sR)
        setAttr(mmn + ".PixelSamplesX", pSX)
        setAttr(mmn + ".PixelSamplesY", pSY)
        setAttr(mmn + ".PixelFilter", pF)
        setAttr(mmn + ".PixelFilterX", pFX)
        setAttr(mmn + ".PixelFilterY", pFY)
        setAttr(mmn + ".BucketSizeX", bsX)
        setAttr(mmn + ".BucketSizeY", bsY)
        setAttr(mmn + ".GridSizeVal", gSV)
        setAttr(mmn + ".UserRibOptions", uro, type = "string")
        
    except:
        raise Exception("nugget error 2")
    
    sceneName = file(q=True, sn = True, shn =True)
    if sceneName.find("_occlusionNormal")>0:
        stat = confirmDialog(t = u"提示", m = u"你想执行左眼还是右眼的“补”??", b = [u"右眼", u"左眼", u"取消"])
        if stat == u"右眼":
            yyResetExtraOutputChannelLocal()
    
def netFix2():

    try:
        mmn = ls(type = "MayaManNugget")[0]
        sR = getAttr(mmn + ".ShadingRate")
        pSX = getAttr(mmn + ".PixelSamplesX")
        pSY = getAttr(mmn + ".PixelSamplesY")
        pF = getAttr(mmn + ".PixelFilter")
        pFX = getAttr(mmn + ".PixelFilterX")
        pFY = getAttr(mmn + ".PixelFilterY")
        bsX = getAttr(mmn + ".BucketSizeX")
        bsY = getAttr(mmn + ".BucketSizeY")
        gSV = getAttr(mmn + ".GridSizeVal")
        uro = getAttr(mmn + ".UserRibOptions")
    except:
        raise Exception("nugget error 1")
    
    mel.eval("source \"rnd_wxII_FixBeforeRender.mel\";wxII_FixBeforeRender(\"project\");")
    
    try:
        setAttr(mmn + ".ShadingRate", sR)
        setAttr(mmn + ".PixelSamplesX", pSX)
        setAttr(mmn + ".PixelSamplesY", pSY)
        setAttr(mmn + ".PixelFilter", pF)
        setAttr(mmn + ".PixelFilterX", pFX)
        setAttr(mmn + ".PixelFilterY", pFY)
        setAttr(mmn + ".BucketSizeX", bsX)
        setAttr(mmn + ".BucketSizeY", bsY)
        setAttr(mmn + ".GridSizeVal", gSV)
        setAttr(mmn + ".UserRibOptions", uro, type = "string")
    except:
        raise Exception("nugget error 2")
    
    sceneName = file(q=True, sn = True, shn =True)
    if sceneName.find("_occlusionNormal")>0:
        stat = confirmDialog(t = u"提示", m = u"你想执行左眼还是右眼的“补”??", b = [u"右眼", u"左眼", u"取消"])
        if stat == u"右眼":
            yyResetExtraOutputChannelOnline()
    
def postSwitchSetup():
    #setup idpass rendermask
    allCams = ls(type = "camera")
    sceneName = file(q=True, sn = True, shn =True)
    if sceneName.find("_idpass")>0:
        for i in range(len(allCams)):
            setAttr(allCams[i] + ".mask", 0)
            
    allCams = ls(type = "camera")
    sceneName = file(q=True, sn = True, shn =True)
    if sceneName.find("_occlusionNormal")>0:
        for i in range(len(allCams)):
            setAttr(allCams[i] + ".backgroundColor", 1,1,1, type = "double3")
    
    
def postCopyCamAttr2Right():
    sss = 1
    ttt = 1
    source = ls("RendercamShape", "original_camera_shp", type = "camera")
    if source == [] or source == None:
        confirmDialog(t = u"警告", m = u"没有找到正确命名的左眼相机；")
        sss = 0
        
    target = ls("camera_stereoRxShape", "camera_stereoRx_shp", type = "camera")
    if target == [] or target == None:
        confirmDialog(t = u"警告", m = u"没有找到正确命名的右眼相机；")
        ttt = 0
        
    if sss == 1 and ttt == 1:
        sourceCam = source[0]
        targetCam = target[0]
        
        a = getAttr(sourceCam + ".nearClipPlane")
        setAttr(targetCam + ".nearClipPlane", a)
        
        a = getAttr(sourceCam + ".farClipPlane")
        setAttr(targetCam + ".farClipPlane", a)
    
        a = getAttr(sourceCam + ".renderable")
        setAttr(targetCam + ".renderable", a)
        
        a = getAttr(sourceCam + ".bestFitClippingPlanes")
        setAttr(targetCam + ".bestFitClippingPlanes", a)
        
        a = getAttr(sourceCam + ".image")
        setAttr(targetCam + ".image", a)
        
        a = getAttr(sourceCam + ".mask")
        setAttr(targetCam + ".mask", a)
        
        a = getAttr(sourceCam + ".depth")
        setAttr(targetCam + ".depth", a)
        
        a = getAttr(sourceCam + ".overscan")
        setAttr(targetCam + ".overscan", a)
        
        #------turn off the renderable for current source
        setAttr(sourceCam + ".renderable", 0)
        
    else:
        confirmDialog(t = u"提示", m = u"没有完成左->右眼相机属性映像；")

def postCopyCamAttr2Left():
    sss = 1
    ttt = 1
    source = ls("camera_stereoRxShape", "camera_stereoRx_shp", type = "camera")
    if source == [] or source == None:
        confirmDialog(t = u"警告", m = u"没有找到正确命名的左眼相机；")
        sss = 0
        
    target = ls("RendercamShape", "original_camera_shp", type = "camera")
    if target == [] or target == None:
        confirmDialog(t = u"警告", m = u"没有找到正确命名的右眼相机；")
        ttt = 0
        
    if sss == 1 and ttt == 1:
        sourceCam = source[0]
        targetCam = target[0]
        
        a = getAttr(sourceCam + ".nearClipPlane")
        setAttr(targetCam + ".nearClipPlane", a)
        
        a = getAttr(sourceCam + ".farClipPlane")
        setAttr(targetCam + ".farClipPlane", a)
    
        a = getAttr(sourceCam + ".renderable")
        setAttr(targetCam + ".renderable", a)
        
        a = getAttr(sourceCam + ".bestFitClippingPlanes")
        setAttr(targetCam + ".bestFitClippingPlanes", a)
        
        a = getAttr(sourceCam + ".image")
        setAttr(targetCam + ".image", a)
        
        a = getAttr(sourceCam + ".mask")
        setAttr(targetCam + ".mask", a)
        
        a = getAttr(sourceCam + ".depth")
        setAttr(targetCam + ".depth", a)
        
        a = getAttr(sourceCam + ".overscan")
        setAttr(targetCam + ".overscan", a)
        
        #turn off the renderabliliy for the right cam
        setAttr(sourceCam + ".renderable", 0)
        
    else:
        confirmDialog(t = u"提示", m = u"没有完成右->左眼相机属性映像；")

def setClipboardFileName2Right():
    try:
        sceneName = file(q=True, sn = True, shn =True)
        sections = sceneName.split("_")
        if sections[5].find("RX") < 0:
            target = sections[5] + "RX"
            newSceneName = sceneName.replace(sections[5], target)
            newScene = str(newSceneName)
            file(rename = newScene)
        else:
            newScene = sceneName
    except:
        pass
    
    try:
        yySetText(win32con.CF_TEXT, str(newScene))
    except:
        pass

def yySetText(aType,aString):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(aType,aString) 
    w.CloseClipboard()
    
def setClipboardFileName2Left():
    try:
        sceneName = file(q=True, sn = True, shn =True)
        sections = sceneName.split("_")
        if sections[5].find("RX") > 0:
            target = sections[5].split("RX")[0]
            newSceneName = sceneName.replace(sections[5], target)
            newScene = str(newSceneName)
            file(rename = newScene)
        else:
            newScene = sceneName
    except:
        pass
    
    try:
        yySetText(win32con.CF_TEXT, str(newScene))
    except:
        pass
    
def yyResetExtraOutputChannelOnline():

    sceneName = file(q=True, sn = True, shn =True)
    if sceneName.find("_occlusionNormal_")>0:
        channels = ["N"]
        paths = mel.eval('rnd_wxII_getMayamanExtraPath "occ_project";')
        #delete all channels:
        mel.eval("zzjDelAllExtraChanls;")
        for i in range(len(paths)):
            oldPath = paths[i].replace("\\", "/")
            oldName = oldPath.split("/")[-1]
            oldSeg = oldName.split("_")[4]
            newSeg = oldSeg + "RX"
            newName = oldName.replace(oldSeg, newSeg)
            newPath = oldPath.replace(oldName, newName)
            mel.eval('MayaManAddExtraOutputChannel("' + channels[i] + '", 3, true,0,0,1,0,65535,0,65535,"", 0, 0,"", "","", "");')
            mel.eval('MayaManSetData -setstring "EOPath" "' + newPath + '" ' + str(i) + ';')
            
    elif sceneName.find("_hairs")>0:
        channels = ["__key","__fill","__rim","__specular","__amb"]
        paths = mel.eval('rnd_wxII_getMayamanExtraPath "hairs_project";')
        
        #delete all channels:
        mel.eval("zzjDelAllExtraChanls;")
        for i in range(len(paths)):
            oldPath = paths[i].replace("\\", "/")
            oldName = oldPath.split("/")[-1]
            oldSeg = oldName.split("_")[4]
            newSeg = oldSeg + "RX"
            newName = oldName.replace(oldSeg, newSeg)
            newPath = oldPath.replace(oldName, newName)
            mel.eval('MayaManAddExtraOutputChannel("' + channels[i] + '", 3, true,0,0,1,0,65535,0,65535,"", 0, 0,"", "","", "");')
            mel.eval('MayaManSetData -setstring "EOPath" "' + newPath + '" ' + str(i) + ';')
    else:
        path = []
        
    mel.eval("mayaManExtraChannelsRefreshList;")
    
def yyResetExtraOutputChannelLocal():

    sceneName = file(q=True, sn = True, shn =True)
    if sceneName.find("_occlusionNormal")>0:
        channels = ["N"]
        paths = mel.eval('rnd_wxII_getMayamanExtraPath "occ_project";')
        #delete all channels:
        mel.eval("zzjDelAllExtraChanls;")
        for i in range(len(paths)):
            oldPath = paths[i].replace("\\", "/")
            oldName = oldPath.split("/")[-1]
            oldSeg = oldName.split("_")[4]
            newSeg = oldSeg + "RX"
            newName = oldName.replace(oldSeg, newSeg)
            newPath = oldPath.replace(oldName, newName)
            mel.eval('MayaManAddExtraOutputChannel("' + channels[i] + '", 3, true,0,0,1,0,65535,0,65535,"", 0, 0,"", "","", "");')
            mel.eval('MayaManSetData -setstring "EOPath" "' + newPath + '" ' + str(i) + ';')
            
    elif sceneName.find("_hairs")>0:
        channels = ["__key","__fill","__rim","__specular","__amb"]
        paths = mel.eval('rnd_wxII_getMayamanExtraPath "hairs_project";')
        
        #delete all channels:
        mel.eval("zzjDelAllExtraChanls;")
        for i in range(len(paths)):
            oldPath = paths[i].replace("\\", "/")
            oldName = oldPath.split("/")[-1]
            oldSeg = oldName.split("_")[4]
            newSeg = oldSeg + "RX"
            newName = oldName.replace(oldSeg, newSeg)
            newPath = oldPath.replace(oldName, newName)
            mel.eval('MayaManAddExtraOutputChannel("' + channels[i] + '", 3, true,0,0,1,0,65535,0,65535,"", 0, 0,"", "","", "");')
            mel.eval('MayaManSetData -setstring "EOPath" "' + newPath + '" ' + str(i) + ';')
            
    else:
        path = []
        
    mel.eval("mayaManExtraChannelsRefreshList;")

def yyResetExtraOutputChannelLocal_withHairMotionBlur():
    localFix2()
    sceneName = file(q=True, sn = True, shn =True)
    if sceneName.find("_hairs")>0:
        channels = ["__key","__fill","__rim","__specular","__amb", "__mblur"]
        paths = mel.eval('rnd_wxII_getMayamanExtraPath_WithMblur "hairs_project";')
        
        #delete all channels:
        mel.eval("zzjDelAllExtraChanls;")
        for i in range(len(paths)):
            print channels[i]
            oldPath = paths[i].replace("\\", "/")
            mel.eval('MayaManAddExtraOutputChannel("' + channels[i] + '", 3, true,0,0,1,0,65535,0,65535,"", 0, 0,"", "","", "");')
            mel.eval('MayaManSetData -setstring "EOPath" "' + oldPath + '" ' + str(i) + ';')
            
    else:
        path = []
        
    mel.eval("mayaManExtraChannelsRefreshList;")