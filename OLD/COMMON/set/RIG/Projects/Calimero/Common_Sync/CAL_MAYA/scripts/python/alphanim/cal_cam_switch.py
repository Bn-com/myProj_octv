'''
this script all the cameras in a maya scene and copy the translate, rotate, scale, focal on one camera in differente frame.
'''

__author__ = 'Dimitri Gouacide'
__version__ = '1.0'
__date__ = '2013-05-28'

import maya.cmds as cmds

def camera_switch():
    if cmds.objExists('CAM'):
      cmds.delete('CAM')
    camera_list = cmds.ls(l=True, cameras=True, v=True)
    current_time = 1
    cmds.currentTime( current_time )
    transform_camera_render = cmds.camera(name="CAM")
    transform_camera_render = cmds.rename("CAM1", "CAM")
    camera_render = cmds.listRelatives( transform_camera_render, shapes=True)
    camera_render = camera_render[0]
    camera_group = ""
    for camera in camera_list:
        transform_camera = cmds.listRelatives( camera, parent=True, type="transform" )
        transform_camera = transform_camera[0]
        camera_group = cmds.listRelatives( transform_camera, parent=True, type="transform" )
        camera_group = camera_group[0]
        focal_length=cmds.getAttr(camera+".focalLength")
        cmds.setAttr(camera_render+".focalLength", focal_length)
        translate_x=cmds.getAttr(transform_camera+".translateX")
        cmds.setAttr(transform_camera_render+".translateX", translate_x)
        translate_y=cmds.getAttr(transform_camera+".translateY")
        cmds.setAttr(transform_camera_render+".translateY", translate_y)
        translate_z=cmds.getAttr(transform_camera+".translateZ")
        cmds.setAttr(transform_camera_render+".translateZ", translate_z)
        rotate_x=cmds.getAttr(transform_camera+".rotateX")
        cmds.setAttr(transform_camera_render+".rotateX", rotate_x)
        rotate_y=cmds.getAttr(transform_camera+".rotateY")
        cmds.setAttr(transform_camera_render+".rotateY", rotate_y)
        rotate_z=cmds.getAttr(transform_camera+".rotateZ")
        cmds.setAttr(transform_camera_render+".rotateZ", rotate_z)
        scale_x=cmds.getAttr(transform_camera+".scaleX")
        cmds.setAttr(transform_camera_render+".scaleX", scale_x)
        scale_y=cmds.getAttr(transform_camera+".scaleY")
        cmds.setAttr(transform_camera_render+".scaleY", scale_y)
        scale_z=cmds.getAttr(transform_camera+".scaleZ")
        cmds.setAttr(transform_camera_render+".scaleZ", scale_z)
        visibility=cmds.getAttr(transform_camera+".visibility")
        cmds.setAttr(transform_camera_render+".visibility", True)
        cmds.setKeyframe("CAMShape.fl")
        cmds.setKeyframe("CAM.translateX")
        cmds.setKeyframe("CAM.translateY")
        cmds.setKeyframe("CAM.translateZ")    
        cmds.setKeyframe("CAM.rotateX")    
        cmds.setKeyframe("CAM.rotateY")    
        cmds.setKeyframe("CAM.rotateZ")    
        cmds.setKeyframe("CAM.scaleX")  
        cmds.setKeyframe("CAM.scaleY")    
        cmds.setKeyframe("CAM.scaleZ")  
        cmds.setKeyframe("CAM.visibility")
        current_time += 1
        cmds.currentTime( current_time )
    print camera_group
    cmds.delete(camera_group)
    cmds.setAttr(camera_render+".focalLength", l=True)   
    cmds.setAttr(transform_camera_render+".translateX", l=True)
    cmds.setAttr(transform_camera_render+".translateY", l=True)
    cmds.setAttr(transform_camera_render+".translateZ", l=True)
    cmds.setAttr(transform_camera_render+".rotateX", l=True)
    cmds.setAttr(transform_camera_render+".rotateY", l=True)
    cmds.setAttr(transform_camera_render+".rotateZ", l=True)
    cmds.setAttr(transform_camera_render+".scaleX", l=True)
    cmds.setAttr(transform_camera_render+".scaleY", l=True)
    cmds.setAttr(transform_camera_render+".scaleZ", l=True)