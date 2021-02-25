#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2013-9-252013

@author: zhangben
'''
import maya.cmds as mc
import maya.mel as mel
import re,os
import idmt.maya.DOD.DODIV.Maya.commonProperties as docp



def do4_batchProc_wholeLayoutFile(NewStoreDir):
    if not os.path.isdir(NewStoreDir):
        try:
            os.mkdir(NewStoreDir)
        except:
            print "please check your enter directory :%s"%NewStoreDir
        return
####=====load all reference file================================
    allRNIterator = (eachRN for eachRN in mc.ls(type=u'reference') if mc.listConnections(u'%s.message'%eachRN,d=True))
    
    for eachRN in allRNIterator:
        if not mc.referenceQuery(eachRN,isLoaded=True):
            rf_file = mc.referenceQuery(eachRN,f=True)
            mc.file(rf_file,lr=eachRN)

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
    
    mc.setAttr(u'defaultRenderGlobals.currentRenderer',u"mayaSoftware",type=u"string")
    mc.setAttr(u'defaultRenderGlobals.imageFilePrefix',u"<Scene>/<Scene>",type=u"string")
    mc.setAttr(u'defaultResolution.width',948)
    mc.setAttr(u'defaultResolution.height',512)
    mc.setAttr(u'defaultRenderQuality.edgeAntiAliasing',2)
#=======create a new simple projection folder to stor file and render out images======================
#NewStoreDir = ur'E:/NewTest'
    mc.workspace(NewStoreDir,o=True)
    pro_path = mc.workspace(q=True,rootDirectory=True)
    mc.workspace(dir=pro_path)
    
    mc.workspace(fr = [u'images',u'images'])
    mc.workspace(cr = u'images')
#mc.workspace(fileRuleEntry = "scene")
#mc.workspace(q=True,frl=True)
    mc.workspace(fr = [u'scene',u'scenes'])
    mc.workspace(cr = u'scenes')
    
#======the information of file's name=========================
    fileName = mc.file(sn=True,q=True)
    
    fileNameSplit = os.path.split(fileName)
    
    newFileNameCharList = os.path.splitext(fileNameSplit[-1])[0].split('_')
    newFileNameCharList[2] = '%sPrevRnd'%newFileNameCharList[2]
    fileNewName = '_'.join(newFileNameCharList)
    
    
    proScenePath = u"%s/scenes"%NewStoreDir
    prndFile = u'%s/%s_prevRnd.prnd'%(proScenePath,fileNewName)
    
    proImagesPath = u"%s/images/%s"%(NewStoreDir,fileNewName)
    
#====create renderLayer by each shot camera===========================
    shotLs = mc.ls(type=u'shot')
    for eachShot in shotLs:
        shotSTFrame = mc.getAttr(u'%s.startFrame'%eachShot)
        shotEDFrame = mc.getAttr(u'%s.endFrame'%eachShot)
        shotCam = mc.listConnections(u'%s.currentCamera'%eachShot)
        shotRenderCam = [stereoShape for stereoShape in mc.listRelatives(shotCam[0],c=True,ad=True,type=u'camera',f=True) if mc.nodeType(stereoShape)==u'camera']
            
        if not checkCamNameAvailable(shotCam[0]):#====check camera's rationality==============
            mc.error((u"pleas check +++[%s]+++ connections camera\'s name"%(eachShot)).upper())

#create_previewRenderLayer(renderObjs,shaderPref="custom",renderCam=None,keepMatObjs=None,shaderType=u'lambert'):
        RL_nameStr = create_previewRenderLayer(primaryObj,u'prev',shotCam[0],eyesObjs)
        mc.editRenderLayerAdjustment( u'defaultRenderGlobals.startFrame',u'defaultRenderGlobals.endFrame',u'%s.renderable'%shotRenderCam[0],u'%s.renderable'%shotRenderCam[1])
        mc.setAttr(u'defaultRenderGlobals.startFrame',shotSTFrame)
        mc.setAttr(u'defaultRenderGlobals.endFrame',shotEDFrame)
        mc.setAttr(u'%s.renderable'%shotRenderCam[0],1)
        mc.setAttr(u'%s.renderable'%shotRenderCam[1],1)
#======write layer and camera information to prnd file======================
        infoStr = u'%s:%s:%s:start:%04d:end:%04d\r\n'%(RL_nameStr,shotRenderCam[0].split(u'|')[-1],\
                        shotRenderCam[1].split(u'|')[-1],shotSTFrame,shotEDFrame)
        fp = open(prndFile,'a')
        fp.write(infoStr)
        fp.close()
#=================================================
        mc.editRenderLayerGlobals(crl="defaultRenderLayer") 
#=====save file into specify directory==================
    
    mc.file(rn=fileNewName)
    saveNewFile = mc.file(typ=u'mayaAscii')
    mc.file(s=True)
#================================================================
    create_prevRndBatFile(saveNewFile,proImagesPath)
    
    return os.path.split(saveNewFile)[0]
    
    
    
    
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
    if keepMatObjs != None:
        mc.editRenderLayerMembers(RL_node,keepMatObjs)
    
    mc.editRenderLayerMembers(RL_node,prv_light)
    mc.editRenderLayerMembers(RL_node,renderCam)
    
    #mc.connectAttr(u'%s.outColor'%RL_shader,u'%s.surfaceShader'%RL_SG,f=True)    
    return RL_node



#===============================================================================
# #=====create renderlayer partial content==========
# def create_previewRenderLayer(renderObjs,shaderPref="custom",renderCam=None,keepMatObjs=None,shaderType=u'lambert',RL_name=u"CustRenderLayer"):
#    #shaderType = u'lambert'
#    #shaderPref = u'prev'
#    if renderCam != None:
#        camNameSplit = renderCam.split(u'_')
#        RL_name = "shot_%s_%s_PRV"%(camNameSplit[1],camNameSplit[2])   
#        prv_LightShape = mc.directionalLight(name = u'preViewLight_%s_%s'%(camNameSplit[1],camNameSplit[2]),rgb=[1,1,1])
#        prv_light = mc.listRelatives(prv_LightShape,p=True,f=True)[0]
#        mc.parentConstraint(renderCam,prv_light,mo=False,st=[u'x',u'y',u'z'],w=1)
#        
#        renderObjs.append(renderCam)
#        renderObjs.append(prv_light)
#    
#    RL_node = mc.createRenderLayer(renderObjs,name=RL_name,number=1,noRecurse=True,mc=True)
#    
#    RL_shader_name = u"%s_%s"%(shaderPref,shaderType)
#    RL_SG = u''
#    if not mc.objExists(RL_shader_name):
#        RL_shader = mc.shadingNode(shaderType,name=RL_shader_name,asShader=True)
#        
#    else:
#        RL_shader = RL_shader_name
#    
#    sgArray = mc.listConnections(RL_shader,source=False,destination=True,type='shadingEngine')
#    if sgArray == None:
#        RL_SG = mc.sets(name = '%sSG'%(RL_shader),renderable=True,noSurfaceShader=True,empty=True)
#        mc.defaultNavigation(connectToExisting=True,source=RL_shader,destination=RL_SG)
#    else:
#        RL_SG = sgArray[0]
#    mc.connectAttr(u'%s.message'%RL_SG,u'%s.shadingGroupOverride'%RL_node,f=True)
#    
#    mc.connectAttr(u'%s.outColor'%RL_shader,u'%s.surfaceShader'%RL_SG,f=True)
#    #===========================================================================
#    # for eachObj in renderObjs:
#    #   mc.sets(eachObj,e=True,forceElement=RL_SG)   
#    # #sets -edit -forceElement do4_c009001HippocampiDalong:SHD_eye3SG do4_c009001HippocampiDalong:MSH_l_hi_eye3_Shape;
#    #===========================================================================
#    if keepMatObjs != None:
#        mc.editRenderLayerMembers(RL_node,keepMatObjs)
#    return RL_node
#===============================================================================




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
    removeall(imageOutDir,[new_outputDir_l,new_outputDir_r])

               
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

