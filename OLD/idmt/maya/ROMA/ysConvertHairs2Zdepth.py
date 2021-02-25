import maya.cmds as cmd
import maya.mel as mel

def ysConvertHairs2Zdepth():
    '''Create two type of depth shader for geometry and hair object respectively'''
    
    geoDepth = cmd.shadingNode('surfaceShader', asShader=1, name='winxII_geoDepth')
    geoDepthSG = cmd.sets(renderable=True, noSurfaceShader=True, empty=1, name='geoDepthSG')
    cmd.connectAttr(geoDepth+'.outColor', geoDepthSG+'.surfaceShader', force=1)
    
    geoSLCode = cmd.shadingNode('SLCodeNode', asUtility=1, name='geoSLCode')
    cmd.addAttr(geoSLCode, ln='outColor', usedAsColor=1, at='float3')
    cmd.addAttr(geoSLCode, ln='outColorR', at='float', p='outColor', dv=1)
    cmd.addAttr(geoSLCode, ln='outColorG', at='float', p='outColor', dv=1)
    cmd.addAttr(geoSLCode, ln='outColorB', at='float', p='outColor', dv=1)
    cmd.addAttr(geoSLCode, ln='outTransp', usedAsColor=1, at='float3')
    cmd.addAttr(geoSLCode, ln='outTranspR', at='float', p='outTransp', dv=0)
    cmd.addAttr(geoSLCode, ln='outTranspG', at='float', p='outTransp', dv=0)
    cmd.addAttr(geoSLCode, ln='outTranspB', at='float', p='outTransp', dv=0)
    cmd.addAttr(geoSLCode, ln='transparencyMap', usedAsColor=1, at='float3')
    cmd.addAttr(geoSLCode, ln='transparencyMapR', at='float', p='transparencyMap', dv=0)
    cmd.addAttr(geoSLCode, ln='transparencyMapG', at='float', p='transparencyMap', dv=0)
    cmd.addAttr(geoSLCode, ln='transparencyMapB', at='float', p='transparencyMap', dv=0)
    cmd.setAttr(geoSLCode+'.SLOutputs', 'outColor outTransp', type='string')
    cmd.setAttr(geoSLCode+'.SLCode', 'color $outTransp = color(1,1,1);\ncolor $outColor = color(1,1,1);\n{\n\
    color zdepth = depth(P);\n    $outTransp = $transparencyMap;\n    $outColor = zdepth * (1-$outTransp);\n}', type='string')
    
    cmd.connectAttr(geoSLCode+'.outColor', geoDepth+'.outColor', force=1)
    cmd.connectAttr(geoSLCode+'.transparencyMap', geoDepth+'.outTransparency', force=1)
    
    mel.eval('source "D:/Alias/MAYA8.5/2013/others/showEditor.mel"')
    mel.eval('source "//file-cluster/GDC/Resource/Support/AnimalLogic/mayaman2.0.7/mel/AEMayaManCustomShaderTemplate.mel"')
#    hairsDepth = cmd.shadingNode('MayaManCustomShader', asShader=True, name='hairsDepth')
#    mel.eval('showEditor("'+hairsDepth+'")')
#    mel.eval('AEMayaManCustomShaderBrowseFile("'+hairsDepth+'.ShaderFile", "//file-cluster/GDC/Resource/Support/Pixar/Shader/RBW_Zdepth_Hairs.slo", "RenderMan Shader")')
#    mel.eval('callCSUpdateCustomShader("RBW_Zdepth_Hairs", "RBW_Zdepth_Hairs.ShaderFile")')
#    hairsDepth = cmd.rename('RBW_Zdepth_Hairs', 'hairsDepth')
#    hairsDepthSG = cmd.sets(renderable=True, noSurfaceShader=True, empty=1, name='hairsDepthSG')
#    cmd.connectAttr(hairsDepth+'.outColor', hairsDepthSG+'.surfaceShader', force=1)
    
    mmshr = cmd.ls(type='MayaManCustomShader')
    for item in mmshr:
        mel.eval('showEditor("'+item+'")')
        mel.eval('AEMayaManCustomShaderBrowseFile("'+item+'.ShaderFile", "//file-cluster/GDC/Resource/Support/Pixar/Shader/RBW_Zdepth_Hairs.slo", "RenderMan Shader")')
        
    meshs = [item for item in cmd.ls(geometry=True, dag=True)]
    cmd.select(meshs)
    cmd.sets(e=1, forceElement=geoDepthSG)
    cmd.select(cl=True)