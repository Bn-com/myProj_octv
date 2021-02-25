'''
this script adds AO to foliage_RGBA shader if doesn't exist.
'''

import maya.cmds as cmds

__author__  = 'Dimitri Gouacide'
__version__ = '1.0.0'
__date__    = '2013-05-07'

def add_AO_to_foliage_RGBA():
    shader_list = cmds.ls(l=True, type="lambert")
    foliage_rgba_without_ao_list = []
    for shader in shader_list:
        if shader.find("Foliage_RGBA") != -1:
            input_ambient_connection = cmds.connectionInfo(shader + ".ambientColor",
                                                           sourceFromDestination = True)    
            if(input_ambient_connection.find("AO_BIL") == -1):           
                my_amb_occlusion = cmds.shadingNode('mib_amb_occlusion', 
                                                    name = shader.replace("_RGBA", "_AO_BIL"),
                                                    asUtility=True)
                cmds.setAttr(my_amb_occlusion + ".samples", 32)
                cmds.setAttr(my_amb_occlusion + ".bright", 1, 1, 1 )
                cmds.setAttr(my_amb_occlusion + ".dark", 0.739557, 0.842, 0.719068 )
                cmds.setAttr(my_amb_occlusion + ".spread", 2)
                cmds.setAttr(my_amb_occlusion + ".max_distance", 150)
                cmds.setAttr(my_amb_occlusion + ".id_inclexcl", -5)
                cmds.connectAttr(my_amb_occlusion + ".outValue",
                                 shader + ".ambientColor",
                                 force=True)
                foliage_rgba_without_ao_list.append(shader)
    if len(foliage_rgba_without_ao_list) != 0:
        text = "foliage_rgba modified:\n\n"
        for foliage_rgba_without_ao in foliage_rgba_without_ao_list:
            text += foliage_rgba_without_ao + "\n"
        result = cmds.confirmDialog(title='Finished',
                                     message=text,
                                     button=['Confirm'])
    else:
        result = cmds.confirmDialog(title='Finished',
                                     message="NO foliage_RGBA without AO_BIL found",
                                     button=['Confirm'])