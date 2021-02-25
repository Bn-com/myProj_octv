# -*- coding: utf-8 -*-

import maya.cmds as mc

shader_lambert='drop_lambert'
shader_surface='drop_sruface'   
if  mc.ls(shader_lambert,type='lambert')==[] and mc.ls(shader_surface,type='surfaceShader')==[] and mc.ls(shader_lambert)==[] and mc.ls(shader_surface)==[]:            
    shader_lambert = mc.shadingNode('lambert', asShader=True, name='drop_lambert')
    mc.setAttr((shader_lambert+'.ambientColor'),1,1,1,type='double3')
    shader_surface = mc.shadingNode('surfaceShader', asShader=True, name='drop_sruface')
    file_node = mc.shadingNode('file', asShader=True, name='labert_drop_file')
    place2D=mc.shadingNode('place2dTexture', asShader=True, name='place2dTexture_drop')
    
    mc.connectAttr((place2D + '.rotateUV'), (file_node + '.rotateUV'))      
    mc.connectAttr((file_node + '.outColor'), (shader_lambert + '.color'))
    mc.connectAttr((file_node + '.outTransparency'), (shader_lambert + '.transparency'))
  
    
if mc.ls(sl=1)[0]=='drop_lambert':
    if mc.connectionInfo((shader_lambert+'.color'), isDestination=True):
        #mc.disconnectAttr((shader_lambert + '.outColor'), (shaderSG + '.surfaceShader'))
        mc.disconnectAttr((file_node + '.outColor'), (shader_lambert + '.color'))
        mc.disconnectAttr((file_node + '.outTransparency'), (shader_lambert + '.transparency'))
        
        #mc.connectAttr((shader_surface + '.outColor'), (shaderSG + '.surfaceShader'))    
        mc.connectAttr((file_node + '.outColor'), (shader_surface + '.outColor'))
        mc.connectAttr((file_node + '.outTransparency'), (shader_surface + '.outTransparency'))
        mc.connectAttr((file_node + '.outColor'), (shader_surface + '.outMatteOpacity'))
    else:
        mc.confirmDialog(title=u'警告', message=u'请选择你想转换的材质球节点', button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')
    
if mc.ls(sl=1)[0]=='drop_sruface':
    if mc.connectionInfo((shader_surface+'.outColor'), isDestination=True):
        #mc.disconnectAttr((shader_surface + '.outColor'), (shaderSG + '.surfaceShader'))
        mc.disconnectAttr((file_node + '.outColor'), (shader_surface + '.outColor'))
        mc.disconnectAttr((file_node + '.outTransparency'), (shader_surface + '.outTransparency'))
        mc.disconnectAttr((file_node + '.outColor'), (shader_surface + '.outMatteOpacity'))
        
        #mc.connectAttr((shader_lambert + '.outColor'), (shaderSG + '.surfaceShader'))    
        mc.connectAttr((file_node + '.outColor'), (shader_lambert + '.color'))
        mc.connectAttr((file_node + '.outTransparency'), (shader_lambert + '.transparency'))
    else:
        mc.confirmDialog(title=u'警告', message=u'请选择你想转换的材质球节点', button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')

if mc.ls(shader_lambert,type='lambert')!=[] and mc.ls(shader_surface,type='surfaceShader')!=[]:
    if (mc.ls(sl=1)==[]) or (mc.ls(sl=1)[0]!='drop_lambert' and mc.ls(sl=1)[0]!='drop_sruface'):
        mc.confirmDialog(title=u'警告', message=u'请选择你想转换的材质球节点', button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')
    
    

    
        
    
    


    
    

    
        
    
    

