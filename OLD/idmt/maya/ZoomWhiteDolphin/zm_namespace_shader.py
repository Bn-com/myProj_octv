# -*- coding: utf-8 -*-

'''
Created on 2014-10-29

@author: liangyu

导入参考后，为SG和file节点添加namespace
'''


import maya.cmds as mc

def renamespaceUI():
    result = mc.promptDialog(title='Add namespace for SG AND FILE', message='namespace:',button=['OK', 'Cancel'],defaultButton='OK',cancelButton='Cancel',dismissString='Cancel')
    if result == 'OK':
            text = mc.promptDialog(query=True, text=True)
            renamespace(text)

def renamespace(namespaces=''):
    shadinggroup=[]
    files=[]                
    SGs=mc.ls(type = 'shadingEngine')
    for sg in SGs:
        if ':' not in sg:
            shadinggroup.append(sg)
                
    Files=mc.ls(textures=1)
    for File in Files:
        if ':' not in File:
            files.append(File)
                                            
    if shadinggroup:
        shadinggroup.remove('initialParticleSE')
        shadinggroup.remove('initialShadingGroup')
        for obj in shadinggroup:
            mc.rename(obj,(namespaces+':'+obj))
            
    if files:
        for obj in files:
            mc.rename(obj,(namespaces+':'+obj))
            
            
    if mc.ls(type='reverse'):
        for obj in mc.ls(type='reverse'):
            mc.rename(obj,(namespaces+':'+obj))