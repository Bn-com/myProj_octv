# -*- coding: utf-8 -*-
import maya.cmds as mc
import maya.mel as mel

def shaderCheck():
    UIName = 'sy_ShaderCheck_mi'
    # 窗口
    if mc.window(UIName, ex=1):
        mc.deleteUI(UIName, window=True)
    mc.window(UIName, title="Sylvain's Shader Check", widthHeight=(150, 210), menuBar=0)
    # 主界面
    mc.columnLayout()

    # 行按钮
    mc.rowLayout()
    # Title
    mc.button(w=150, h=20, bgc=[0.1, 0.1, 0.1], label="Shader Check")
    mc.setParent("..")

    # 行按钮
    mc.rowLayout()
    # CHR
    mc.button(w=150, h=30, bgc=[0.1, 0.7, 0.1], label='Reflect',c='meshReflect()')
    mc.setParent("..")

    # 行按钮
    mc.rowLayout()
    # CHR
    mc.button(w=150, h=30, bgc=[0.1, 0.6, 0.1], label='Refract',c='meshRefract()')
    mc.setParent("..")

    # 行按钮
    mc.rowLayout()
    # CHR
    mc.button(w=150, h=30, bgc=[0.1, 0.5, 0.1], label='Specular',c='meshSpec()')
    mc.setParent("..")

    # 行按钮
    mc.rowLayout()
    # CHR
    mc.button(w=150, h=30, bgc=[0.1, 0.6, 0.1], label='SSS',c='meshSSS()')
    mc.setParent("..")

    # 行按钮
    mc.rowLayout()
    # CHR
    mc.button(w=150, h=30, bgc=[0.1, 0.7, 0.1], label='Emission',c='meshEmis()')
    mc.setParent("..")

    mc.showWindow(UIName)

#SELECT MESH WITH SHADERS WITH EMISSIOn ON SELECT GROUPS
def meshEmis():
    meshs=mc.ls(sl=1,l=1,tr=1)
    meshEmis=[]
    if meshs:
        for  mesh in meshs:
            shapes = mc.listRelatives(mesh, ad=1, ni=1, type='mesh', f=1)
            if not shapes:
                continue
            for shape in shapes:
                msg=mc.listConnections(shape,s=0,type = 'shadingEngine')
                obj=mc.listRelatives(shape,p=1,f=1)[0]
                if not msg:
                    continue
                shader=mc.listConnections('%s.surfaceShader' % msg[0])
                shader = shader[0]
                needShaders = mc.hyperShade(listUpstreamNodes = shader)
                if not needShaders:
                    continue
                if shader not in needShaders:
                    needShaders.append(shader)
                for checkShader in needShaders:
                    checkAttr = checkShader+'.emission'
                    if (mc.ls(checkAttr) and mc.getAttr(checkAttr)>0) and obj not in meshEmis:
                        meshEmis.append(obj)

    #else:
    #    mc.error('======= Please select=======')       
    if meshEmis:
        mc.select(meshEmis)
    else:
        mc.select(cl=1)
        print 'all aistandard shader has Refract <0,the meshs you select'

#SELECT MESH WITH SHADERS WITH REFRACTION ON SELECT GROUPS
def meshRefract():
    meshs=mc.ls(sl=1,l=1,tr=1)
    meshRefract=[]
    if meshs:
        for  mesh in meshs:
            shapes = mc.listRelatives(mesh, ad=1, ni=1, type='mesh', f=1)
            if not shapes:
                continue
            for shape in shapes:
                msg=mc.listConnections(shape,s=0,type = 'shadingEngine')
                obj=mc.listRelatives(shape,p=1,f=1)[0]
                if not msg:
                    continue
                shader=mc.listConnections('%s.surfaceShader' % msg[0])
                shader = shader[0]
                needShaders = mc.hyperShade(listUpstreamNodes = shader)
                if not needShaders:
                    continue
                if shader not in needShaders:
                    needShaders.append(shader)
                for checkShader in needShaders:
                    checkAttr = checkShader+'.Kt'
                    if (mc.ls(checkAttr) and mc.getAttr(checkAttr)>0) and obj not in meshRefract:
                        meshRefract.append(obj)

    #else:
    #    mc.error('======= Please select=======')       
    if meshRefract:
        mc.select(meshRefract)
    else:
        mc.select(cl=1)
        print 'all aistandard shader has Refract <0,the meshs you select'

#SELECT MESH WITH SHADERS WITH SSS ON SELECT GROUPS
def meshSSS():
    meshs=mc.ls(sl=1,l=1,tr=1)
    meshSSS=[]
    if meshs:
        for  mesh in meshs:
            shapes = mc.listRelatives(mesh, ad=1, ni=1, type='mesh', f=1)
            if not shapes:
                continue
            for shape in shapes:
                msg=mc.listConnections(shape,s=0,type = 'shadingEngine')
                obj=mc.listRelatives(shape,p=1,f=1)[0]
                if not msg:
                    continue
                shader=mc.listConnections('%s.surfaceShader' % msg[0])
                shader = shader[0]
                needShaders = mc.hyperShade(listUpstreamNodes = shader)
                if not needShaders:
                    continue
                if shader not in needShaders:
                    needShaders.append(shader)
                for checkShader in needShaders:
                    checkAttr = checkShader+'.Ksss'
                    if (mc.ls(checkAttr) and mc.getAttr(checkAttr)>0) and obj not in meshSSS:
                        meshSSS.append(obj)

    #else:
    #    mc.error('======= Please select=======')       
    if meshSSS:
        mc.select(meshSSS)
    else:
        mc.select(cl=1)
        print 'all aistandard shader has Refract <0,the meshs you select'

#SELECT MESH WITH SHADERS WITH REFLECTION ON SELECT GROUPS
def meshReflect():
    meshs=mc.ls(sl=1,l=1,tr=1)
    meshReflect=[]
    if meshs:
        for  mesh in meshs:
            shapes = mc.listRelatives(mesh, ad=1, ni=1, type='mesh', f=1)
            if not shapes:
                continue
            for shape in shapes:
                msg=mc.listConnections(shape,s=0,type = 'shadingEngine')
                obj=mc.listRelatives(shape,p=1,f=1)[0]
                if not msg:
                    continue
                shader=mc.listConnections('%s.surfaceShader' % msg[0])
                shader = shader[0]
                needShaders = mc.hyperShade(listUpstreamNodes = shader)
                if not needShaders:
                    continue
                if shader not in needShaders:
                    needShaders.append(shader)
                for checkShader in needShaders:
                    checkAttr = checkShader+'.Kr'
                    if (mc.ls(checkAttr) and mc.getAttr(checkAttr)>0) and obj not in meshReflect:
                        meshReflect.append(obj)

    #else:
    #    mc.error('======= Please select=======')       
    if meshReflect:
        mc.select(meshReflect)
    else:
        mc.select(cl=1)
        print 'all aistandard shader has Refract <0,the meshs you select'

#SELECT MESH WITH SHADERS WITH REFLECTION ON SELECT GROUPS
def meshSpec():
    meshs=mc.ls(sl=1,l=1,tr=1)
    meshSpec=[]
    if meshs:
        for  mesh in meshs:
            shapes = mc.listRelatives(mesh, ad=1, ni=1, type='mesh', f=1)
            if not shapes:
                continue
            for shape in shapes:
                msg=mc.listConnections(shape,s=0,type = 'shadingEngine')
                obj=mc.listRelatives(shape,p=1,f=1)[0]
                if not msg:
                    continue
                shader=mc.listConnections('%s.surfaceShader' % msg[0])
                shader = shader[0]
                needShaders = mc.hyperShade(listUpstreamNodes = shader)
                if not needShaders:
                    continue
                if shader not in needShaders:
                    needShaders.append(shader)
                for checkShader in needShaders:
                    checkAttr = checkShader+'.Ks'
                    if (mc.ls(checkAttr) and mc.getAttr(checkAttr)>0) and obj not in meshSpec:
                        meshSpec.append(obj)

    #else:
    #    mc.error('======= Please select=======')       
    if meshSpec:
        mc.select(meshSpec)
    else:
        mc.select(cl=1)
        print 'all aistandard shader has Refract <0,the meshs you select'