#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2012-11-192012

@author: zhangben
'''
import maya.cmds as mc
import maya.mel as mel
import re 
def do3_renderTools_creatRL(LayerName,color=[0.5,0.5,0.5],pref=False):
    prefSwitch = pref
    if LayerName == "cautic":
        LightPath = r"\\file-cluster\GDC\Projects\DiveollyDive3\DiveollyDive3_Scratch\Rendering\lighting\caustic\caustic_light.mb"
        prefSwitch = True
    elif LayerName == "fringe":
        LightPath = r"\\file-cluster\GDC\Projects\DiveollyDive3\DiveollyDive3_Scratch\Rendering\lighting\edge light\RGBlight.mb"
        prefSwitch = True
    else:
        LightPath = ""
    do3_renderTools_creatSpecial_Lighting_RL(LayerName,LightPath,"mayaBinary",color,prefSwitch)
    

def do3_renderTools_creatSpecial_Lighting_RL(layerName,lightPath="",fileFormat="mayaBinary",color =[0.5,0.5,0.5],pref=False ):
    selObj = mc.ls(sl=True,l=True)
    #layerName = "CAUSTIC"
    layerFullName = layerName
    if pref ==True:
        prefStr = do3_createRL_prefix_DialogUI()
        if  prefStr != None:
            layerFullName = "%s_%s"%(prefStr,layerName)
        else:
            return
    
    
    #============create Caustic lambert Shading group====================================
    causLam = mc.shadingNode ("lambert",asShader=True,name = "%s_Lambert" % (layerName))
    causSG = mc.sets(renderable=True,noSurfaceShader =True,empty=True,name="%s_Lambert_SG" %(layerName))
    mc.connectAttr((causLam + ".outColor"),(causSG + ".surfaceShader"),f=True)
    
    #============import caustic light ===================================================
    
    if lightPath != "":
        mc.file(lightPath,i=True,type=fileFormat,ra=True,namespace ="%s_Light" %(layerName),options="v=0",loadReferenceDepth="all")
        im_light = mc.ls("%s_Light*:*"%(layerName),type="transform")[0]
        selObj.append(im_light)
    
    
    #print causticLightPath
    #============create caustic renderLayer ==============================================
    
    mc.createRenderLayer(selObj,number = 1,name=layerFullName,noRecurse=True,mc=True)
    
    cmdStr ="hookShaderOverride(\"%s\",\"\",\"%s_Lambert\");"%(layerFullName,layerName)
    mel.eval(cmdStr)

def do3_createRL_prefix_DialogUI():
    result = mc.promptDialog(title=u'创建渲染层',
                    message=u'层名前缀:',
                    button=['OK','Cancel'],
                    defaultButton='OK',
                    cancelButton='Cancel',
                    dismissString='Cancel')
    if result == 'OK':
        return mc.promptDialog(query=True, text=True)
    else:
        return None

def do3_RT_createSpecRL(layerDiscript):#=========根据描述创建渲染层，配置层专属渲染参数==============
    selObj= mc.ls(sl=True,l=True)
    if layerDiscript == "reflect":
        shader = 'useBackground'
        layerInfor = do3_RT_createRL(selObj,layerDiscript,shader)
        rt_shader = layerInfor['RT_shaderName']
        mc.setAttr((rt_shader+'.reflectivity'),0.2)
        mc.setAttr((rt_shader + '.specularColor'),1,1,1,type ='double3')
        try:
            mel.eval("source  \"//file-cluster/gdc/Resource/Support/Maya/projects/DODIII/do3_configRenderParameters.mel\"; do3_configRenderParameters;")
        except:
            pass
        do3_RL_adjustmentParameter("miDefaultOptions.finalGather",0)
        do3_RL_adjustmentParameter("miDefaultOptions.globalIllum",0)
        do3_RL_adjustmentParameter("miDefaultOptions.maxReflectionRays",1)
        do3_RL_adjustmentParameter("miDefaultOptions.maxRefractionRays",1)
        do3_RL_adjustmentParameter("miDefaultOptions.maxRayDepth",2)
        
        do3_RL_adjustmentParameter("miDefaultOptions.maxShadowRayDepth",2)
        do3_RL_adjustmentParameter("miDefaultOptions.maxReflectionBlur",1)
        do3_RL_adjustmentParameter("miDefaultOptions.maxRefractionBlur",1)


def do3_RL_adjustmentParameter(attriName,vale):#========配置数值型属性，为当前层的专属属性值======
    mc.editRenderLayerAdjustment(attriName)
    mc.setAttr(attriName,vale)
def do3_RT_createRL(objList,layerDiscript,shaderType,prefSwith=False):
    #objList = mc.ls(sl=True,l=True)
    #layerFullName = "reflect"
    #shaderType = useBackground
    p = re.compile("iceball",re.I)
    if p.search(objList[-1]) == None:
        mc.error(u"应该最后选择冰球")
     
    
    shaderNameStr = "RT_%s_%s"%(layerDiscript,shaderType)
    SG_nameStr = "RT_%s_SG"%(layerDiscript)
    #====create shader & shadingEngine=========================
    cre_shader = mc.shadingNode(shaderType,n=shaderNameStr,asShader = True)
    cre_SG = mc.sets(n=SG_nameStr,r=True,nss=True,empty=True)
    mc.connectAttr("%s.outColor"%(cre_shader),"%s.surfaceShader"%(cre_SG),f=True)
    #====create renderLayer ===================================    
    layerFullName = layerDiscript
    if prefSwith == True:
        prefStr =  do3_createRL_prefix_DialogUI()
        if prefStr == None:
            pass
        else:
            layerFullName = '%s_%s'%(prefStr,layerDiscript)
    
    cre_RL = mc.createRenderLayer(objList,number = 1,name=layerFullName,noRecurse=True,mc=True)
    if mc.objExists("defaultRenderLayer"):
        mc.setAttr('defaultRenderLayer.renderable',0)
    #mc.editRenderLayerGlobals(crl = cre_RL)    
    mc.sets(objList[-1],e=True,fe=cre_SG)
    setRenderOBjSpecAttrbute(objList[:-1],"primaryVisibility",0)
    setRenderOBjSpecAttrbute(objList[:-1],"visibleInRefractions",1)
    setRenderOBjSpecAttrbute(objList[:-1],"visibleInReflections",1)
        
        
    
    return {"RT_layerName":cre_RL,"RT_shaderName":cre_shader}

def setRenderOBjSpecAttrbute(objectsList,attrName,value):#========
    intermediateObj = mc.ls(intermediateObjects=True,l=True)
    for each in objectsList:
        shapes = []        
        meshes = mc.listRelatives(each,ad=True,c=True,type ="mesh",f=True)
        if meshes != None:
            shapes.extend([meshes[i] for i in range(len(meshes)) if meshes[i] not in intermediateObj])
        surfaces = mc.listRelatives(each,ad=True,c=True,type="nurbsSurface")    
        if surfaces != None:
            shapes.extend(surfaces)
        if len(shapes) !=0:       
            for eachShape in shapes:
                attrNameStr = "%s.%s" %(eachShape,attrName)
                do3_RL_adjustmentParameter(attrNameStr,value)

def do3_assignSpecialMaterial(mt_discrpt,mt_type):
#    mt_discrpt = "reflect"
#    mt_type = "useBackground"
    specialObjList = mc.ls(sl=True,l=True)
    shaderNameStr = "RT_%s_%s"%(mt_discrpt,mt_type)
    SG_nameStr = "RT_%s_SG"%(mt_discrpt)
    #====create shader & shadingEngine=========================
    cre_shader = mc.shadingNode(mt_type,n=shaderNameStr,asShader = True)
    cre_SG = mc.sets(n=SG_nameStr,r=True,nss=True,empty=True)
    mc.connectAttr("%s.outColor"%(cre_shader),"%s.surfaceShader"%(cre_SG),f=True)
    #==========config materialNode parameters=================
    do3_configMaterialParameters(mt_discrpt,cre_shader)
    
    #============assign to special objects====================
    
    mc.sets(specialObjList,e=True,fe=cre_SG)

def do3_configMaterialParameters(mt_discript,mt_nede):
    if mt_discript =="reflect":
        mc.setAttr((mt_nede +'.reflectivity'),0.2)
        mc.setAttr((mt_nede + '.specularColor'),1,1,1,type ='double3')

def do3_creatRenderLayer(layerDiscript,prefSwith = True): 
#    layerDiscript = "reflect"
    objList = mc.ls(sl=True,l=True)
    layerFullName = layerDiscript
    if prefSwith == True:
        prefStr =  do3_createRL_prefix_DialogUI()
        if prefStr == None:
            pass
        else:
            layerFullName = '%s_%s'%(prefStr,layerDiscript)
    
    cre_RL = mc.createRenderLayer(objList,number = 1,name=layerFullName,noRecurse=True,mc=True)
    if mc.objExists("defaultRenderLayer"):
        mc.setAttr('defaultRenderLayer.renderable',0)
    do3_configRenderLayerParameter(layerDiscript)
        
def do3_configRenderLayerParameter(rl_discript):
    if rl_discript == 'reflect':
        try:
            mel.eval("source  \"//file-cluster/gdc/Resource/Support/Maya/projects/DODIII/do3_configRenderParameters.mel\"; do3_configRenderParameters;")
        except:
            pass
        do3_RL_adjustmentParameter("miDefaultOptions.finalGather",0)
        do3_RL_adjustmentParameter("miDefaultOptions.globalIllum",0)
        do3_RL_adjustmentParameter("miDefaultOptions.maxReflectionRays",1)
        do3_RL_adjustmentParameter("miDefaultOptions.maxRefractionRays",1)
        do3_RL_adjustmentParameter("miDefaultOptions.maxRayDepth",2)
        
        do3_RL_adjustmentParameter("miDefaultOptions.maxShadowRayDepth",2)
        do3_RL_adjustmentParameter("miDefaultOptions.maxReflectionBlur",1)
        do3_RL_adjustmentParameter("miDefaultOptions.maxRefractionBlur",1)



if __name__ =="__main__":
    do3_renderTools_creatRL("CAUSTIC")
