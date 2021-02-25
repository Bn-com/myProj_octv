#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2013-10-29

@author: zhangben

后台批量渲染layout镜头，需要注意的是：要 指定 projName 变量的值，要在项目_scratch 路径里，
放置一个ly_light 的灯光文件，文件里最上面的灯光组命名为：ly_light  。避免程序337行，筛选
导入的灯光组时的错误冲突。

'''
import maya.cmds as mc
import os
import re
import maya.mel as mel
import idmt.maya.DOD.DODIV.Maya.commonProperties as docp
import maya.OpenMaya as om
import idmt.pipeline.db
from pymel.core import *

def renderSceneByLambert(ma_filePath=u'fileName', saveAs=True, rndSwitch=True, projName=u'DiveollyDive5'):
    # =====load all reference file================================
    if ma_filePath == u'fileName':
        ma_filePath = mc.file(q=True, sn=True)
    allRNIterator = docp.list_valid_referenceNodes()
    for eachRN in allRNIterator:
        if not mc.referenceQuery(eachRN, isLoaded=True):
            rf_file = mc.referenceQuery(eachRN, f=True)
            mc.file(rf_file, lr=eachRN)

    print "==================================All Reference files are loaded==================================="
    docp.del_unknownNodes()
    print "=========================================Unkown nodes is deleted=================================="
    #===========file imformation === contains: file shot name=workspace=rendered=images output directory= render camera======
    #===========文件信息，包括：文件短名字，工程目录，渲染器，渲染输出路径，渲染摄像机
    ma_filePath_shn = os.path.basename(ma_filePath)
    ma_filePath_shn_spl = os.path.splitext(os.path.basename(ma_filePath))[0].split(u'_')
    proj_abbreviation = ma_filePath_shn_spl[0]
    sq_num = ma_filePath_shn_spl[1]
    shot_num = ma_filePath_shn_spl[2]
    mode = ma_filePath_shn_spl[3]
    ves_numStr = ma_filePath_shn_spl[4]
    #=================Save As File Name==另存后文件的名字=======================
    ma_filePath_shn_new = u'prv_%s_%s_%s_%s_%s' % (proj_abbreviation, sq_num, shot_num, mode, ves_numStr)
    #=================Images directory &&& Scenes Directory渲染输出路径和文件存储路径==========================
    saveFileDir = os.path.dirname(ma_filePath)
    fileWorkspace = "/".join(saveFileDir.split("/")[:-1])
    outImagesDir = u'%s/images' % fileWorkspace
    if not os.path.isdir(outImagesDir):
        os.mkdir(outImagesDir)
    print "=================================ALL FOLDERS ARE  RENDY============================================"
    #===============prnd file =====记录信息文件======================================
    prndFile = u'%s/%s_prevRnd.prnd' % (saveFileDir, ma_filePath_shn_new)
    #=================render camera=======渲染摄像机======================
    sq_shot = u'%s_%s' % (sq_num, shot_num)
    p_cam = re.compile(u'%s_baked$' % sq_shot)

    shot_Cam_ls = [exactCam for exactCam in mc.ls(type='stereoRigTransform') if p_cam.search(exactCam) != None]
    if shot_Cam_ls == []:
        p_cam_noBaked = re.compile(u'%s$' % sq_shot)
        shot_Cam_ls = [exactCam for exactCam in mc.ls(type='stereoRigTransform') if p_cam_noBaked.search(exactCam) != None]

        if shot_Cam_ls == []:
            print u'+++++++++++File:%s++++++++There Is No Render Camera,Please Check Your Scenes!!++++++++++++' % ma_filePath_shn
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
    #====================2013.11.19添加，将摄像机bake后到处到项目scratch路径供长精细化====================
    timeInfo = mel.eval("idmtProject -timeLine -echo on;")
    #====================================================================================
    p_mode_ly = re.compile(u'ly', re.I)
    if p_mode_ly.search(mode):
        # print "this is LAYOUT FILE"
        ly_camExportPath = u"//file-cluster/GDC/Projects/%s/%s_Scratch/Layout/cam_export/episode_%s" % (projName, projName, sq_num)
        if not os.path.isdir(ly_camExportPath):
            os.makedirs(ly_camExportPath)

        camFileSN = u'%s_%s_%s_cam.mb' % (proj_abbreviation, sq_num, shot_num)
        camFileFN = u'%s/%s' % (ly_camExportPath, camFileSN)

        p_cam_noBaked = re.compile(u'%s$' % sq_shot)
        shot_Cam_ls = [exactCam for exactCam in mc.ls(type='stereoRigTransform') if p_cam_noBaked.search(exactCam) != None]

        mc.playbackOptions(min=timeInfo[0])
        mc.playbackOptions(max=timeInfo[1])

        mc.currentTime(timeInfo[0], e=True)

        mc.select(shot_Cam_ls[0])
        mel.eval(u'source\"zwCameraImportExport.mel\";')
        mel.eval(u'zwBakeCamera;;')
        bakedCam = mc.ls(sl=True, l=True)
        mc.file(camFileFN, f=True, options=u'v=0', typ=u'mayaBinary', pr=True, es=True)
        mc.delete(bakedCam)
        print "===============Layout File Shot Camera Is Baked and Exported To Project Scratch Directory================="

    print "===============Camera is OK!!!!!================================="
    #============set default renderlayer can not be rendered ========设置默认渲染层不可渲染
    edo_renameDefualtRenderLayerName()
    if mc.objExists(u"defaultRenderLayer"):
        mc.editRenderLayerGlobals(crl="defaultRenderLayer")
        mc.setAttr('defaultRenderLayer.renderable', 0)
    else:
        mc.error("There is no defaultRenderLayer")

    #====delete all renderLayers except default renderLayer=============删除默认渲染层外其他所有渲染层===
    allOtherRL = [eachLayer for eachLayer in mc.ls(type='renderLayer') if eachLayer != 'defaultRenderLayer']
    if len(allOtherRL) != 0:
        for eachRL in allOtherRL:
            mc.delete(eachRL)
    print "====================RENDERLAYER IS CLEANUP======================"
    #====firstly,get the dagObjects who will be rendered out====首先，获取场景中参与渲染的的几何体========
    #===use generator expression just wanna save alittle time,hope so======用生成器表达式，仅仅是为了节省点儿时间====

    facialCtrs = mc.ls(u"*:Facial_CTRL_FRAME", type="transform", l=True)  # =====开启角色面部表情次级控制器，解决某些角色模型无法被渲染的问题=====================
    userAttrStr = u"facialSecondaryCtrl"

    exactFacialCtr = (each_FCF for each_FCF in facialCtrs if mc.listAttr(each_FCF, string=userAttrStr) == [userAttrStr])
    for eachFC in exactFacialCtr:
        mc.setAttr((eachFC + "." + userAttrStr), 1)
    #=================================================================
    #===========================================================================
    # #======把用arnlod 渲染代理的植物，替换为中模============================================
    # import idmt.maya.DOD.2013.do3_vegetabel_HML_transform as dvht
    # ai_proxy = ls(type = u'aiStandIn',l=True)
    # ai_proxy_parent_GEOGrp = []
    # p_aiStIn = re.compile(u'_geo[ABC]+',re.I)
    # for eachNode in ai_proxy:
    #     if p_aiStIn.search(eachNode.name()):
    #         ai_proxy_parent_GEOGrp.append(eachNode.getParent().getParent().name())
    # if ai_proxy_parent_GEOGrp:
    #     mc.select(ai_proxy_parent_GEOGrp)        
    #     dvht.do3_vegetable_HML_transform(u'm')    
    #=======打开代理显示的低模primary visibility 属性=====================================================
    ai_proxy = ls(type = u'aiStandIn',l=True)
    for each_node in ai_proxy:
        each_node.getParent().getParent().getShape(ni=True).primaryVisibility.set(1)
    #=========================================================================================
    primaryObj_generator = (d for d in mc.ls(typ=[u'mesh', u'nurbsSurface'], ni=True, l=True) if mc.getAttr("%s.primaryVisibility" % d) and (docp.nodeIsVisible(d)))
    primaryObj = []
    eyesObjs = []
    for ec_pri in primaryObj_generator:
        p_eye = re.compile(u'_eye[0-9]*_')

        if p_eye.search(ec_pri.split(u'|')[-1]):
            eyesObjs.append(ec_pri)
        else:
            primaryObj.append(ec_pri)

    allRndMeshes = primaryObj + eyesObjs
    print "========================================OBJECT OK!!!=================================="
    #===========set default render attributes ===================
    anim = idmt.pipeline.db.GetAnimByFilename(ma_filePath)
    res_w = anim.resolutionW
    res_h = anim.resolutionH

    p_ly_sd = re.compile(u'(ly)|(sd)', re.I)

    if anim.shortName == u'do4' and p_ly_sd.search(mode):  # ======DOD4  preview render resolution==================================
        res_w = 948
        res_h = 512

    mc.setAttr(u'defaultRenderGlobals.currentRenderer', u"mentalRay", type=u"string")
    mc.setAttr(u'defaultRenderGlobals.preMel', u"cycleCheck -e off", type=u"string")
    print "===================================set renderer MentalRay======================================="
    mc.setAttr(u'defaultRenderGlobals.imageFilePrefix', u"<Scene>/<Scene>", type=u"string")

   #============================================================================
   # mc.setAttr(u'defaultRenderQuality.edgeAntiAliasing',2)
   #
   # mc.setAttr(u'defaultRenderGlobals.numCpusToUse',8)
   #============================================================================
   #======================config mentalRay Options================================
    mc.setAttr(u'miDefaultOptions.maxReflectionRays', 1)
    mc.setAttr(u'miDefaultOptions.maxRefractionRays', 1)
    mc.setAttr(u'miDefaultOptions.maxRayDepth', 2)
    mc.setAttr(u'miDefaultOptions.maxShadowRayDepth', 2)

    mc.setAttr(u'miDefaultOptions.minSamples', -2)
    mc.setAttr(u'miDefaultOptions.maxSamples', 0)
    mc.setAttr(u'miDefaultOptions.filter', 0)
    mc.setAttr(u'miDefaultOptions.rayTracing', 0)
    mc.setAttr(u'miDefaultOptions.filterWidth', 1)
    mc.setAttr(u'miDefaultOptions.filterHeight', 1)

    mc.setAttr(u'mentalrayGlobals.exportVerbosity', 0)
    mc.setAttr(u"mentalrayGlobals.renderVerbosity", 0)
    mc.setAttr(u'mentalrayGlobals.exportMessages', 0)

    #=======================create render layer preview ==================================================

    RL_nameStr = create_previewRenderLayer(allRndMeshes, u'prev', shot_Cam_ls[0])
    print "==============================RenderLayer OK!============================================"
    mc.editRenderLayerAdjustment(u'defaultRenderGlobals.startFrame', u'defaultRenderGlobals.endFrame', u'%s.renderable' % renderCams[
                                 0], u'%s.renderable' % renderCams[1], u'defaultResolution.width', u'defaultResolution.height', u'defaultRenderGlobals.imageFilePrefix')
    mc.setAttr(u'defaultRenderGlobals.startFrame', timeInfo[0])
    mc.setAttr(u'defaultRenderGlobals.endFrame', timeInfo[1])
    mc.setAttr(u'%s.renderable' % renderCams[0], 1)
    mc.setAttr(u'%s.renderable' % renderCams[1], 1)
    mc.setAttr(u'defaultResolution.width', res_w)
    mc.setAttr(u'defaultResolution.height', res_h)

    mc.setAttr(u'defaultRenderGlobals.imageFilePrefix', ma_filePath_shn.split(u'.')[0], type=u'string')

    print "===========================RENDER PARAMETER OK!!!!!!!!!!!!!!===================================="

    #======write layer and camera information to prnd file======================
    infoStr = u'%s:%s:%s:start:%04d:end:%04d\r\n' % (RL_nameStr, renderCams[0].split(u'|')[-1], renderCams[1].split(u'|')[-1], timeInfo[0], timeInfo[1])
    fp = open(prndFile, 'a')
    fp.write(infoStr)
    fp.close()
#============save file as prev render file ===================================
 #=================================add  IKSolver=================================
    mel.eval(u'setState \"iksolver\" off;setState \"iksolver\" on;')
    print "==========================iksolver Refreshed!!!!!==============================================-"
#=====================add DYNAMIC SYSTEM　SET==============================================================
    mc.dynPref(sr=False)
    mc.dynPref(rf=2)

    hairSys = mc.ls(type=u'hairSystem')

    ptcl = mc.ls(type=u'particle', l=True)
    if ptcl:
        for each_ptcl in ptcl:
            mc.setAttr(u'%s.isDynamic' % each_ptcl, 0)

        print u'==============================PATICLE IS OFF======================================'

#=========================DELETE WRITECOLORINBUFFER+++++++++++++++++++++++++++++++++++++++++++++++++++
    wtcb = mc.ls(type=u'writeToColorBuffer')
    if wtcb:
        mc.delete(wtcb)
        print u'+++++++++++++++++++++++++++WriteToColorBuffer Node Deleted!!+++++++++++++++++++++++++++++++++++++++++++++++++++++++'
    print u'============================writeToColorBuffer nodes deleted========================================'
    if saveAs:
        mc.file(rn=ma_filePath_shn_new)
        saveNewFile = mc.file(save=True, type="mayaAscii")

#    batFile = create_prevRndBatFile(saveNewFile,outImagesDir)
#    os.system(batFile)
        print"========================File Saved======================================="
    cfn = mc.file(q=True, sn=True)
    if rndSwitch:
        cmdStr = generate_renderCMDStr(cfn, outImagesDir)
        print "render command :%s" % cmdStr
    #=======================+++++++++++
    #====evnironDict = os.environ.get
    #++++++++++++++++++++++++++++++++++
        # os.system(cmdStr)
        f = os.popen(cmdStr.replace('/', '\\'))
        while True:
            line = f.readline()
            if not line:
                break
            print line
        f.close()
        print "=================RENDER COMPLETED====================================="
    else:

        cmdStr = generate_renderCMDStr(cfn, outImagesDir)
        print cmdStr

#==============================================================================


def create_prevRndBatFile(rndFile, outputDir):
    maya_loc = os.getenv('MAYA_LOCATION')
    renderOpPathStr = u"\"%s/bin/render.exe\"" % (maya_loc)
    filePathStr = u"\"%s\"" % (rndFile)
    cmdStr = u"%s -sw:mm 128 -rd %s %s\n" % (renderOpPathStr, outputDir, filePathStr)

    sysTemp = os.environ['TEMP']
    batFile = u'%s/PrevBatchRender.bat' % (sysTemp)
    if os.path.exists(batFile):
        os.remove(batFile)
    f_bat = open(batFile, 'a')
    f_bat.write(cmdStr)
    f_bat.close()
    return batFile

#===============generate render cmd================================================================


def generate_renderCMDStr(rndFile, outputDir):
    maya_loc = os.getenv('MAYA_LOCATION')
    renderOpPathStr = u"%s/bin/render.exe" % (maya_loc)
    filePathStr = u"%s" % (rndFile)
    cmdStr = u"%s -r file -mr:rt 8 -rd %s %s" % (renderOpPathStr, outputDir, filePathStr)
    return cmdStr

#=====create renderlayer partial content==========


def create_previewRenderLayer(renderObjs, shaderPref="custom", renderCam=None, keepMatObjs=None, shaderType=u'lambert', RL_name=u"CustRenderLayer", projName="DiveollyDive5"):
    #shaderType = u'lambert'
    #shaderPref = u'prev'
    if renderCam != None:
        camNameSplit = renderCam.split(u'_')
        RL_name = "shot_%s_%s_PRV" % (camNameSplit[1], camNameSplit[2])
        prv_LightShape = mc.directionalLight(name=u'preViewLight_%s_%s' % (camNameSplit[1], camNameSplit[2]), rgb=[1, 1, 1])
        prv_light = mc.listRelatives(prv_LightShape, p=True, f=True)[0]
        mc.parentConstraint(renderCam, prv_light, mo=False, st=[u'x', u'y', u'z'], w=1)
        mc.select(cl=True)
#      renderObjs.append(renderCam)
#      renderObjs.append(prv_light)

    RL_node = mc.createRenderLayer(renderObjs, name=RL_name, number=1, noRecurse=True, mc=True)
    try:
        mel.eval("hookShaderOverride(\"%s\",\"lambert\",\"\" )" % RL_node)
        if keepMatObjs != []:
            mc.editRenderLayerMembers(RL_node, keepMatObjs)
    except:

        RL_shader_name = u"%s_%s" % (shaderPref, shaderType)
        RL_SG = u''
        if not mc.objExists(RL_shader_name):
            RL_shader = mc.shadingNode(shaderType, name=RL_shader_name, asShader=True)

        else:
            RL_shader = RL_shader_name

        sgArray = mc.listConnections(RL_shader, source=False, destination=True, type='shadingEngine')
        if sgArray == None:
            RL_SG = mc.sets(name='%sSG' % (RL_shader), renderable=True, noSurfaceShader=True, empty=True)
           # mc.defaultNavigation(connectToExisting=True,source=RL_shader,destination=RL_SG)
            mc.connectAttr(u'%s.outColor' % RL_shader, u'%s.surfaceShader' % RL_SG, f=True)
        else:
            RL_SG = sgArray[0]
        #   mc.connectAttr(u'%s.message'%RL_SG,u'%s.shadingGroupOverride'%RL_node,f=True)
        for eachObj in renderObjs:
            mc.sets(eachObj, e=True, forceElement=RL_SG)
        # sets -edit -forceElement do4_c009001HippocampiDalong:SHD_eye3SG do4_c009001HippocampiDalong:MSH_l_hi_eye3_Shape;
        if keepMatObjs != []:
            mc.editRenderLayerMembers(RL_node, keepMatObjs)

    mc.editRenderLayerMembers(RL_node, prv_light)
    mc.editRenderLayerMembers(RL_node, renderCam)
    #=================add layout light group===========================20131111=============
    ly_light = u'//file-cluster/GDC/Projects/%s/%s_Scratch/lighting/previewRender_light/ly_light.mb' % (projName, projName)
    ly_lightFile = mc.file(ly_light, i=True, type=u'mayaBinary', ra=False, options=u'v=0', pr=False, namespace='ly_light')
    im_light = mc.ls('*:ly_light')[0]
    mc.editRenderLayerMembers(RL_node, im_light)
#==================================================================
    # mc.connectAttr(u'%s.outColor'%RL_shader,u'%s.surfaceShader'%RL_SG,f=True)
    return RL_node


def checkCamNameAvailable(camName):  # ==============check the rationality by camera's name ===========
    #camName = u'cam_004c_009a'
    p = re.compile(u'cam(_[0-9]{3}[a-zA-Z]*)+')
    if p.match(camName):
        return True
    else:
        return False


def neatenOutImages(mayaProDir):  # =======neaton output images:整理自动渲染输出的图片到左右眼路径下===============================

    projScenes = ur'%s/scenes' % mayaProDir
    projImages = ur'%s/images' % mayaProDir

    fileLists = os.listdir(projScenes)
    myFiles = []
    for eachFile in fileLists:
        if os.path.splitext(eachFile)[-1] == u'.ma':
            myFiles.append(os.path.splitext(eachFile)[0])

    fileName = myFiles[0]
    imageOutDir = u'%s/%s' % (projImages, fileName)

    p_r = re.compile(u'(right)', re.IGNORECASE)
    p_l = re.compile(u'(left)', re.IGNORECASE)

    allLeftOutDir = []
    allRightOutDir = []

    allOutImages_left = []
    allOutImages_right = []

    #====创建左眼，右眼输出路径文件夹===================
    new_outputDir_l = u'%s/stereo_left' % imageOutDir
    new_outputDir_r = u'%s/stereo_right' % imageOutDir

    os.mkdir(new_outputDir_r)
    os.mkdir(new_outputDir_l)
    #==================================================

    for root, pathes, files in os.walk(imageOutDir):  # ========transition   render out images to special directory===============
        for ea_file in files:
            if p_r.search(root) != None and root.replace(u'\\', '/') != new_outputDir_r:
                shutil.move(os.path.join(root, ea_file), new_outputDir_r)
            if p_l.search(root) != None and root.replace(u'\\', '/') != new_outputDir_l:
                shutil.move(os.path.join(root, ea_file), new_outputDir_l)

    #=========remove others folder except left & right folder contain the image sequence===============
    remove_remain_DIR(imageOutDir, [new_outputDir_l, new_outputDir_r])


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


def edo_renameDefualtRenderLayerName(newname='defaultRenderLayer'):
    drl = mc.listConnections('renderLayerManager.rlmi[0]', s=0, d=1)[0]
    if not drl == 'defaultRenderLayer':
        try:
            mc.delete('defaultRenderLayer')
        except:
            print 'defaultRenderLayer is not found!'
    mc.select(drl, r=1)
    msl = om.MSelectionList()
    mg = om.MGlobal()
    mg.getActiveSelectionList(msl)
    msl.length()
    mobj = om.MObject()
    msl.getDependNode(0, mobj)
    mfndn = om.MFnDependencyNode(mobj)
    mfndn.setName(newname)

# if __name__ == "__main__":
#  ma_filePath = mc.file(q=True,sn=True)
#    renderSceneByLambert(ma_filePath)
