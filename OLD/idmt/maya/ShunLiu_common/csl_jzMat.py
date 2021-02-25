# -*- coding: utf-8 -*-
import pymel.core as pm
import maya.cmds as mc
import os
import re

def csl_JzMatte():
    layers = pm.ls(type = 'renderLayer')
    for layer in layers:
        if layer.name().find('chr') < 0:
            layer.renderable.set(0)
        else:
            pm.editRenderLayerGlobals(currentRenderLayer = layer)
            pm.rename(layer, 'chr_jz_blur')



    set_tex_path_IDMT()

    
    chars = ['c024001Caizhili','c003020GaoChaoDesert','c002017ShangYuDesert','c001019ShunLiuDesert','c022001Chenmo','c021001Huahouzhi','c001008ShunLiuDesertCamo','c002008ShangYuDesertCamo','c003008GaoChaoDesertCamo','c001017ShunLiuSnow','c002015ShangYuSnow','c003019GaoChaoSnow','c009015BaoDaTingSnow','c001001ShunLiuFin','c001013ShunLiuS','c002001ShangYuFin','c002012ShangYuS','c003001GaoChaoFin','c003013GaoChaoS','c009006BaoDaTing','c009011BaoDaTingS']

    jzs = ['*:MSH_c_hi_logo_ca_1_ca_','*:MSH_c_hi_logo_ca_']


    jzObjs = []

    for c in chars:
        for jz in jzs:
            jzObjs.append('*' + c + jz)


    listJzObjs = pm.ls(jzObjs)

    listJzObjsName = []

    for jzo in listJzObjs:
        jzo.visibility.set(1)
        listJzObjsName.append(jzo.name())


    mesh = pm.ls(type = 'mesh')
    nurb = pm.ls(type = 'nurbsSurface')

    geo = []
    for g in (mesh + nurb):
        p = g.getParent()
        if p.name() not in listJzObjsName:
            geo.append(p)

    sg = pm.sets(renderable=True, noSurfaceShader=True,empty=True, name= 'jzMatte_SG')
                     
    mat = pm.shadingNode('useBackground', asShader = True, name = 'jzMatte')
    mat.specularColor.set([0, 0, 0])
    mat.reflectivity.set(0)
    mat.reflectionLimit.set(0)
    mat.shadowMask.set(0)
    mat.outColor >> sg.surfaceShader




    pm.select(geo, r = True)
    if len(pm.ls(sl = True)) > 0:
        pm.sets(sg, e = True, forceElement = True )
        pm.sets(sg, e = True, forceElement = True )


    aovs = pm.ls(type = 'aiAOV')

    for aov in aovs:
        pm.setAttr(aov + '.enabled',0)


    sname = mc.file(q = True, sn = True, shn = True)
    snames = sname.split('_')
    try:
        snames[4] = 'l1jzcolor'
    except:
        pass

    dirName = 'D:/Info_Temp/JZ_Matte/'
    mc.sysFile(dirName, makeDir = True)
    newName = dirName +  '_'.join(snames)

    mc.file(rename = newName)
    mc.file(f = True, save = True)



def set_tex_path_IDMT():

    serverPath = 'IDMT'
    serverPathMap = {'L': '${L_PROJECTS}', 'IDMT' : '${IDMT_PROJECTS}'}
    texFiles = pm.ls(type = 'file')
    for map in texFiles:
        mapPath = pm.getAttr(map +'.fileTextureName')

        realPath = os.path.realpath(os.path.expandvars(mapPath))

        if os.path.isfile(realPath):
            pat = re.compile(r'\\\\file-cluster\\GDC\\Projects',re.IGNORECASE)
            finalPath = pat.sub(serverPathMap[serverPath],realPath)
            
            pat = re.compile(r'Z:\\Projects',re.IGNORECASE)
            finalPath = pat.sub(serverPathMap[serverPath],finalPath)
            
            pat = re.compile(r'L:\\Projects',re.IGNORECASE)
            finalPath = pat.sub(serverPathMap[serverPath],finalPath)


            pm.setAttr(map +'.fileTextureName', finalPath, type = 'string' )




                