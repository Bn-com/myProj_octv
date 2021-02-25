#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2013-10-292013

@author: zhangben
'''
import maya.cmds as mc
import os,re
import maya.mel as mel

def renderSceneByLambert(ma_filePath):
    #===========file imformation === contains: file shot name=workspace=rendered=images output directory= render camera====== 
    ma_filePath_shn = os.path.basename(ma_filePath)
    ma_filePath_shn_spl= os.path.splitext(os.path.basename(ma_filePath))[0].split(u'_')
    proj_abbreviation = ma_filePath_shn_spl[0]
    sq_num = ma_filePath_shn_spl[1]
    shot_num = ma_filePath_shn_spl[2]
    mode = ma_filePath_shn_spl[3]
    ves_numStr = ma_filePath_shn_spl[4]
    #=================Save As File Name=========================
    ma_filePath_shn_new = u'%s_%s_%s_%s_PrevRnd'%(proj_abbreviation,sq_num,shot_num,mode)
    #=================Images directory &&& Scenes Directory==========================
    fileWorkspace = mc.workspace(q=True,o=True)
    outImagesDir = u'%s/images'%fileWorkspace
    saveFileDir = u'%s/scenes'%fileWorkspace
    
    #===============prnd file ===========================================
    prndFile = u'%s/%s_prevRnd.prnd'%(saveFileDir,ma_filePath_shn_new)
    #=================render camera=============================
    sq_shot = u'%s_%s'%(sq_num,shot_num)
    p_cam = re.compile(u'%s_baked$'%sq_shot)
    
    shot_Cam_ls = [exactCam for exactCam in mc.ls(type = 'stereoRigTransform') if p_cam.search(exactCam) != None]
    if shot_Cam_ls == []:
        print u'+++++++++++File:%s++++++++There Is No Baked Render Camera++++++++++++++++++++' % ma_filePath_shn
        return
    
    renderCams = [stereoShape for stereoShape in mc.listRelatives(shot_Cam_ls[0],c=True,ad=True,type=u'camera',f=True) if mc.nodeType(stereoShape)==u'camera']
    
    #============================================================
    ####===========set all camera renderable off===================
        
    allCameShape = mc.ls(type="camera")
    for eachCamShape in allCameShape:
        mc.setAttr(u'%s.renderable'%eachCamShape,0)
    #============set default renderlayer can not be rendered 
    if mc.objExists(u"defaultRenderLayer"):
        mc.editRenderLayerGlobals(crl="defaultRenderLayer")
        mc.setAttr('defaultRenderLayer.renderable',0)
    else:
        mc.error("There is no defaultRenderLayer")
        
    #====delete all renderLayers except default renderLayer================
    allOtherRL = [eachLayer for eachLayer in mc.ls(type='renderLayer') if eachLayer != 'defaultRenderLayer']
    if len(allOtherRL) != 0:
        for eachRL in allOtherRL:
            mc.delete(eachRL)    
    #====firstly,get the dagObjects who will be rendered out============
    #===use generator expression just wanna save alittle time,hope so==========
        
    primaryObj_generator= (d for d in mc.ls(v=True,typ=[u'mesh',u'nurbsSurface'],ni=True,l=True) if mc.getAttr("%s.primaryVisibility" % d) and (docp.nodeIsVisible(d)))
    primaryObj = []
    eyesObjs = []
    for ec_pri in primaryObj_generator:
        p_eye = re.compile(u'_eye[0-9]*_')
    
        if p_eye.search(ec_pri.split(u'|')[-1]):
            eyesObjs.append(ec_pri)
        else:
            primaryObj.append(ec_pri)
    
    #===========set default render attributes ===================
    res_w = 2048
    res_h = 1024
    
    if proj_abbreviation == u'do4':#======DOD4  preview render resolution==================================
        res_w = 948
        res_h = 512    
    
    
    timeInfo = mel.eval("idmtProject -timeLine -echo on;")
    
    mc.setAttr(u'defaultRenderGlobals.currentRenderer',u"mayaSoftware",type=u"string")
    mc.setAttr(u'defaultRenderGlobals.imageFilePrefix',u"<Scene>/<Scene>",type=u"string")
    mc.setAttr(u'defaultResolution.width',res_w)
    mc.setAttr(u'defaultResolution.height',res_h)
    mc.setAttr(u'defaultRenderQuality.edgeAntiAliasing',2)
    
    #=======================create render layer preview ==================================================
    
    RL_nameStr = create_previewRenderLayer(primaryObj,u'prev',shot_Cam_ls[0],eyesObjs)
    
    mc.editRenderLayerAdjustment( u'defaultRenderGlobals.startFrame',u'defaultRenderGlobals.endFrame',u'%s.renderable'%renderCams[0],u'%s.renderable'%renderCams[1])
    mc.setAttr(u'defaultRenderGlobals.startFrame',timeInfo[0])
    mc.setAttr(u'defaultRenderGlobals.endFrame',timeInfo[1])
    mc.setAttr(u'%s.renderable'%renderCams[0],1)
    mc.setAttr(u'%s.renderable'%renderCams[1],1)
    #======write layer and camera information to prnd file======================
    infoStr = u'%s:%s:%s:start:%04d:end:%04d\r\n'%(RL_nameStr,renderCams[0].split(u'|')[-1],renderCams[1].split(u'|')[-1],timeInfo[0],timeInfo[1])
    fp = open(prndFile,'a')
    fp.write(infoStr)
    fp.close()
    
    
    
    #============save file as prev render file ===================================
    mc.file(rn = ma_filePath_shn_new)
    mc.file(save =True,type = "mayaAscii")

#=======================+++++++++++
#====evnironDict = os.environ.get
#++++++++++++++++++++++++++++++++++


def create_prevRndBatFile(rndFile,outputDir):
    maya_loc = os.getenv('MAYA_LOCATION')
    renderOpPathStr = u"\"%s/bin/render.exe\""%(maya_loc)
    filePathStr = u"\"%s\""%(rndFile)
    cmdStr =u"%s -rd %s %s\n"%(renderOpPathStr,outputDir,filePathStr)
    
    
    sysTemp = os.environ['TEMP']
    batFile = u'%s/PrevBatchRender.bat'%(sysTemp)
    f_bat = open(batFile,'a')
    f_bat.write(cmdStr)
    f_bat.close()

#=====create renderlayer partial content==========
def create_previewRenderLayer(renderObjs,shaderPref="custom",renderCam=None,keepMatObjs=None,shaderType=u'lambert',RL_name=u"CustRenderLayer"):
    #shaderType = u'lambert'
    #shaderPref = u'prev'
    if renderCam != None:
        camNameSplit = renderCam.split(u'_')
        RL_name = "shot_%s_%s_PRV"%(camNameSplit[1],camNameSplit[2])   
        prv_LightShape = mc.directionalLight(name = u'preViewLight_%s_%s'%(camNameSplit[1],camNameSplit[2]),rgb=[1,1,1])
        prv_light = mc.listRelatives(prv_LightShape,p=True,f=True)[0]
        mc.parentConstraint(renderCam,prv_light,mo=False,st=[u'x',u'y',u'z'],w=1)
        mc.select(cl=True)
#      renderObjs.append(renderCam)
#      renderObjs.append(prv_light)
    
    RL_node = mc.createRenderLayer(renderObjs,name=RL_name,number=1,noRecurse=True,mc=True)
    
    RL_shader_name = u"%s_%s"%(shaderPref,shaderType)
    RL_SG = u''
    if not mc.objExists(RL_shader_name):
        RL_shader = mc.shadingNode(shaderType,name=RL_shader_name,asShader=True)
       
    else:
        RL_shader = RL_shader_name
    
    sgArray = mc.listConnections(RL_shader,source=False,destination=True,type='shadingEngine')
    if sgArray == None:
        RL_SG = mc.sets(name = '%sSG'%(RL_shader),renderable=True,noSurfaceShader=True,empty=True)
       #mc.defaultNavigation(connectToExisting=True,source=RL_shader,destination=RL_SG)
        mc.connectAttr(u'%s.outColor'%RL_shader,u'%s.surfaceShader'%RL_SG,f=True)    
    else:
        RL_SG = sgArray[0]
    #   mc.connectAttr(u'%s.message'%RL_SG,u'%s.shadingGroupOverride'%RL_node,f=True)
    for eachObj in renderObjs:
        mc.sets(eachObj,e=True,forceElement=RL_SG)   
    #sets -edit -forceElement do4_c009001HippocampiDalong:SHD_eye3SG do4_c009001HippocampiDalong:MSH_l_hi_eye3_Shape;
    if keepMatObjs != []:
        mc.editRenderLayerMembers(RL_node,keepMatObjs)
    
    mc.editRenderLayerMembers(RL_node,prv_light)
    mc.editRenderLayerMembers(RL_node,renderCam)
    
    #mc.connectAttr(u'%s.outColor'%RL_shader,u'%s.surfaceShader'%RL_SG,f=True)    
    return RL_node


def checkCamNameAvailable(camName):#==============check the rationality by camera's name ===========
    #camName = u'cam_004c_009a'
    p = re.compile(u'cam(_[0-9]{3}[a-zA-Z]*)+')
    if p.match(camName):
        return True
    else:
        return False

def neatenOutImages(mayaProDir):#=======neaton output images:整理自动渲染输出的图片到左右眼路径下===============================

    projScenes = ur'%s/scenes'%mayaProDir
    projImages = ur'%s/images'%mayaProDir
    
    fileLists = os.listdir(projScenes)
    myFiles = []
    for eachFile in fileLists:
        if os.path.splitext(eachFile)[-1] == u'.ma':
            myFiles.append(os.path.splitext(eachFile)[0])
    
    fileName = myFiles[0]
    imageOutDir = u'%s/%s'%(projImages,fileName)
    
    p_r = re.compile(u'(right)',re.IGNORECASE)
    p_l = re.compile(u'(left)',re.IGNORECASE)
    
    
    allLeftOutDir = []
    allRightOutDir = []
    
    allOutImages_left = []
    allOutImages_right = []
    
    #====创建左眼，右眼输出路径文件夹===================
    new_outputDir_l = u'%s/stereo_left'%imageOutDir  
    new_outputDir_r = u'%s/stereo_right'%imageOutDir 
    
    os.mkdir(new_outputDir_r)
    os.mkdir(new_outputDir_l)
    #==================================================
        
    for root,pathes,files in os.walk(imageOutDir):#========transition   render out images to special directory===============
        for ea_file in files:
            if p_r.search(root) != None and root.replace(u'\\','/') != new_outputDir_r:
                shutil.move(os.path.join(root,ea_file),new_outputDir_r)
            if p_l.search(root) != None and root.replace(u'\\','/') != new_outputDir_l:
                shutil.move(os.path.join(root,ea_file),new_outputDir_l)
    
    #=========remove others folder except left & right folder contain the image sequence===============
    remove_remain_DIR(imageOutDir,[new_outputDir_l,new_outputDir_r])

               
def remove_remain_DIR(destinationDir,remainDir):
    normRemainDir = [os.path.normpath(eachReDir) for eachReDir in remainDir]
    if not os.path.isdir(destinationDir):
        return
    for eachDir in  os.listdir(destinationDir):
        fullPath = os.path.normpath(os.path.join(destinationDir,eachDir))
        if fullPath in normRemainDir:
            continue
        elif os.path.isfile(fullPath):
            os.remove(fullPath)
        elif os.path.isdir(fullPath):
            removeall(fullPath,remainDir)
            os.rmdir(fullPath)


if __name__ == "__main__":
    ma_filePath = mc.file(q=True,sn=True)
    renderSceneByLambert(ma_filePath)







