import pymel.core as pm
import maya.OpenMaya as om
import maya.OpenMayaUI as mui
import re
import os

def delOutOffScreen():
    
    currentPanel = pm.getPanel( wf = True)
    pm.modelEditor(currentPanel, e = True, allObjects = False)
    pm.modelEditor(currentPanel, e = True, polymeshes = True)


    framesRange = pm.idmtProject( timeLine = True, echo  = False)

    activeView = mui.M3dView.active3dView()
    w = activeView.portWidth()
    h = activeView.portHeight()

    transforms = []
    pattern = re.compile('^csl_s')
    refFiles = pm.system.listReferences()
    for refFile in refFiles:
        fname =  os.path.basename(refFile.path)
        if pattern.match(fname):
            
            if not refFile.isLoaded():
                refFile.load()
            refFile.selectAll()
            
            # meshes = pm.ls(sl = True, type = 'mesh')
            # for m in meshes:
            #     t = m.getParent()
            #     transforms.append(t)
                
            refFile.importContents()

    meshes = pm.ls(type = 'mesh')
    for m in meshes:
        t = m.getParent()
        transforms.append(t)
    pm.select(transforms, r = True)

    for f in range(framesRange[0], framesRange[1] + 1):
        pm.currentTime(f)
        om.MGlobal.selectFromScreen(0,0,w, h, om.MGlobal.kRemoveFromList)
        
    pm.delete(pm.ls(sl = True))
