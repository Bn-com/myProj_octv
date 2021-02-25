#!/usr/bin/env python

import maya.cmds as cmds
import maya.mel as mel
from McdMakeAgentCache import *
from McdGeneral import *
from McdRenderFBXFunctions import *
from McdSimpleCmd import *

def McdCreatePlacementNode():
    miarmyMain = cmds.ls("Miarmy_Contents")
    if miarmyMain == [] or miarmyMain == None:
        cmds.confirmDialog(t = "Error", m = 'Cannot find "Miarmy_Contents" Group.')
        raise Exception('Cannot find "Miarmy_Contents" Group.')
    placementGrp = cmds.ls("Placement_Set")
    if placementGrp == [] or placementGrp == None:
        #create one and parent
        cmds.group(n = "Placement_Set", em = True)
        cmds.parent("Placement_Set", "Miarmy_Contents")
    else:
        #try to parent
        try:
            placeParent = cmds.listRelatives("Placement_Set", c = False, p = True)[0]
            if placeParent != "Miarmy_Contents":
                cmds.parent("Placement_Set", "Miarmy_Contents")
        except:
            pass
        
        
    #create node and place it to group
    nbPlace = str(McdGetNumOfThisType("McdPlace"))
    newNodeTrans = cmds.createNode("transform", n = "McdPlace" + nbPlace)
    newNode = cmds.createNode("McdPlace", n = "McdPlace" + nbPlace + "Shape", p = newNodeTrans)
    
    tranNode = cmds.listRelatives(newNode, parent = True, c = False, path = True)[0]
    
    cmds.connectAttr(tranNode + ".tx", newNode + ".localPositionX")
    cmds.connectAttr(tranNode + ".ty", newNode + ".localPositionY")
    cmds.connectAttr(tranNode + ".tz", newNode + ".localPositionZ")
    
    cmds.setAttr(tranNode + ".rx", lock = True, k = False)
    cmds.setAttr(tranNode + ".ry", lock = True, k = False)
    cmds.setAttr(tranNode + ".rz", lock = True, k = False)
    
    cmds.setAttr(tranNode + ".sx", lock = True, k = False)
    cmds.setAttr(tranNode + ".sy", lock = True, k = False)
    cmds.setAttr(tranNode + ".sz", lock = True, k = False)
    
    cmds.setAttr(newNode + ".localPositionX", cb = False)
    cmds.setAttr(newNode + ".localPositionY", cb = False)
    cmds.setAttr(newNode + ".localPositionZ", cb = False)
    
    cmds.setAttr(newNode + ".localScaleX", cb = False)
    cmds.setAttr(newNode + ".localScaleY", cb = False)
    cmds.setAttr(newNode + ".localScaleZ", cb = False)
    
    cmds.setAttr(newNode + ".proportion[0]", 0)
    cmds.setAttr(newNode + ".proportion[1]", 0)
    cmds.setAttr(newNode + ".proportion[2]", 1)
    cmds.setAttr(newNode + ".proportion[3]", 0)
    cmds.setAttr(newNode + ".proportion[4]", 0)
    cmds.setAttr(newNode + ".proportion[5]", 0)
    
    cmds.parent(tranNode, "Placement_Set")


def placementAgent():
    # set time:
    globalNode = McdGetMcdGlobalNode()
    startTime = cmds.playbackOptions(q = True, ast = True)
    allBrainNodes = cmds.ls(type = "McdBrain")
    if allBrainNodes != [] and allBrainNodes != None:
        startTimeInNode = cmds.getAttr(allBrainNodes[0] + ".startTime")
        if startTime > startTimeInNode + 0.1:
            stat = cmds.confirmDialog(t = "Question", m = 'Detecte StartTime in Brain Node is smaller than value in timeslider, fix it??', \
                                                        b = ["Yes", "Cancel"])
            if stat == "Yes":
                cmds.setAttr(allBrainNodes[0] + ".startTime", startTime)
    
    # check whether inverse placement and normal place node both exited
    stat = "none"
    placed = False
    if checkInverseAndNormalExist() == True:
        stat = cmds.confirmDialog(t = "Question", m = 'Detected both "normal place node" and "place node generated from inverse place" existed\n' + \
                                                    'Please choose the the way you want to place: ', \
                                                    b = ["Place Both", "Place Only from Inverse Placement", "Cancel"])
        
        if stat == "Place Only from Inverse Placement":
            cmd = "McdPlacementCmd -am 0 -ign 1;"
            placed = mel.eval(cmd)
            McdAfterPlaceFunction()
        elif stat == "Place Both":
            cmd = "McdPlacementCmd -am 0 -ign 0;"
            placed = mel.eval(cmd)
            McdAfterPlaceFunction()
    else:
        cmd = "McdPlacementCmd -am 0 -ign 0;"
        placed = mel.eval(cmd)
        McdAfterPlaceFunction()
        
    if placed:
        isHide = False
        
        hideAttr = cmds.getAttr(globalNode + ".funcParamList[0]")
        if hideAttr == 1:
            isHide = True
        elif hideAttr == 2:
            isHide = False
        else:
            stat = cmds.confirmDialog(t = "Question", m = 'Are you willing to hide all Original Agent and Place Node?', \
                                                    b = ["Hide", "Hide and not mention again", "Show it and not mention again", "No"])
            if stat == "Hide":
                isHide = True
            elif stat == "Hide and not mention again":
                isHide = True
                cmds.setAttr(globalNode + ".funcParamList[0]", 1)
            elif stat == "Show it and not mention again":
                cmds.setAttr(globalNode + ".funcParamList[0]", 2)
        
        if isHide == True:
            allAgentGrp = cmds.ls(type = "McdAgentGroup")
            try:
                cmds.hide(allAgentGrp)
            except:
                pass
            
            allPlaceNodes = cmds.ls(type = "McdPlace")
            try:
                for i in range(len(allPlaceNodes)):
                    transform = cmds.listRelatives(allPlaceNodes[i], p = True, c = False)[0]
                    cmds.hide(transform)
            except:
                pass
    
    # check "PhysX" plugin:
    if cmds.pluginInfo( "physx.mll", query = True, loaded = True ):
        cmds.confirmDialog(t = "Warning", m = "Load both Miarmy and Maya Physx together may cause unstable.\nFor disable this warning, please:\n" + \
                         "* Unload physx.mll plugin\n* Or modify the McdPlacementFunctions.py in you Miarmy installation place.")


def placementAgentRange():
    # set time:
    globalNode = McdGetMcdGlobalNode()
    startTime = cmds.playbackOptions(q = True, ast = True)
    allBrainNodes = cmds.ls(type = "McdBrain")
    if allBrainNodes != [] and allBrainNodes != None:
        startTimeInNode = cmds.getAttr(allBrainNodes[0] + ".startTime")
        if startTime > startTimeInNode + 0.1:
            stat = cmds.confirmDialog(t = "Question", m = 'Detecte StartTime in Brain Node is smaller than value in timeslider, fix it??', \
                                                        b = ["Yes", "Cancel"])
            if stat == "Yes":
                cmds.setAttr(allBrainNodes[0] + ".startTime", startTime)
    
    # check whether inverse placement and normal place node both exited
    stat = "none"
    placed = False
    if checkInverseAndNormalExist() == True:
        stat = cmds.confirmDialog(t = "Question", m = 'Detected both "normal place node" and "place node generated from inverse place" existed\n' + \
                                                    'Please choose the the way you want to place: ', \
                                                    b = ["Place Both", "Place Only from Inverse Placement", "Cancel"])
        
        if stat == "Place Only from Inverse Placement":
            cmd = "McdPlacementCmd -am 4 -ign 1;"
            placed = mel.eval(cmd)
            McdAfterPlaceFunction()
        elif stat == "Place Both":
            cmd = "McdPlacementCmd -am 4 -ign 0;"
            placed = mel.eval(cmd)
            McdAfterPlaceFunction()
    else:
        cmd = "McdPlacementCmd -am 4 -ign 0;"
        placed = mel.eval(cmd)
        McdAfterPlaceFunction()
        
    if placed:
        isHide = False
        
        hideAttr = cmds.getAttr(globalNode + ".funcParamList[0]")
        if hideAttr == 1:
            isHide = True
        elif hideAttr == 2:
            isHide = False
        else:
            stat = cmds.confirmDialog(t = "Question", m = 'Are you willing to hide all Original Agent and Place Node?', \
                                                    b = ["Hide", "Hide and not mention again", "Show it and not mention again", "No"])
            if stat == "Hide":
                isHide = True
            elif stat == "Hide and not mention again":
                isHide = True
                cmds.setAttr(globalNode + ".funcParamList[0]", 1)
            elif stat == "Show it and not mention again":
                cmds.setAttr(globalNode + ".funcParamList[0]", 2)
        
        if isHide == True:
            allAgentGrp = cmds.ls(type = "McdAgentGroup")
            try:
                cmds.hide(allAgentGrp)
            except:
                pass
            
            allPlaceNodes = cmds.ls(type = "McdPlace")
            try:
                for i in range(len(allPlaceNodes)):
                    transform = cmds.listRelatives(allPlaceNodes[i], p = True, c = False)[0]
                    cmds.hide(transform)
            except:
                pass
    
    # check "PhysX" plugin:
    if cmds.pluginInfo( "physx.mll", query = True, loaded = True ):
        cmds.confirmDialog(t = "Warning", m = "Load both Miarmy and Maya Physx together may cause unstable.\nFor disable this warning, please:\n" + \
                         "* Unload physx.mll plugin\n* Or modify the McdPlacementFunctions.py in you Miarmy installation place.")

def placementAgentFromSelect():
    # set time:
    globalNode = McdGetMcdGlobalNode()
    startTime = cmds.playbackOptions(q = True, ast = True)
    allBrainNodes = cmds.ls(type = "McdBrain")
    if allBrainNodes != [] and allBrainNodes != None:
        startTimeInNode = cmds.getAttr(allBrainNodes[0] + ".startTime")
        if startTime > startTimeInNode + 0.1:
            stat = cmds.confirmDialog(t = "Question", m = 'Detecte StartTime in Brain Node is smaller than value in timeslider, fix it??', \
                                                        b = ["Yes", "Cancel"])
            if stat == "Yes":
                cmds.setAttr(allBrainNodes[0] + ".startTime", startTime)
    
    # check whether inverse placement and normal place node both exited
    stat = "none"
    placed = False

    cmd = "McdPlacementCmd -am 2 -ign 0;"
    placed = mel.eval(cmd)
    McdAfterPlaceFunction()
        
    if placed:
        isHide = False
        
        hideAttr = cmds.getAttr(globalNode + ".funcParamList[0]")
        if hideAttr == 1:
            isHide = True
        elif hideAttr == 2:
            isHide = False
        else:
            stat = cmds.confirmDialog(t = "Question", m = 'Are you willing to hide all Original Agent and Place Node?', \
                                                    b = ["Hide", "Hide and not mention again", "Show it and not mention again", "No"])
            if stat == "Hide":
                isHide = True
            elif stat == "Hide and not mention again":
                isHide = True
                cmds.setAttr(globalNode + ".funcParamList[0]", 1)
            elif stat == "Show it and not mention again":
                cmds.setAttr(globalNode + ".funcParamList[0]", 2)
        
        if isHide == True:
            allAgentGrp = cmds.ls(type = "McdAgentGroup")
            try:
                cmds.hide(allAgentGrp)
            except:
                pass
            
            allPlaceNodes = cmds.ls(type = "McdPlace")
            try:
                for i in range(len(allPlaceNodes)):
                    transform = cmds.listRelatives(allPlaceNodes[i], p = True, c = False)[0]
                    cmds.hide(transform)
            except:
                pass
    
    # check "PhysX" plugin:
    if cmds.pluginInfo( "physx.mll", query = True, loaded = True ):
        cmds.confirmDialog(t = "Warning", m = "Load both Miarmy and Maya Physx together may cause unstable.\nFor disable this warning, please:\n" + \
                         "* Unload physx.mll plugin\n* Or modify the McdPlacementFunctions.py in you Miarmy installation place.")
        
    
def dePlacementAgent():
    #cmd = "McdPlacementCmd -am 1 -ign 0;"
    # mel.eval(cmd)
    
    # #################################
    # delete agents
    # unhide
    # agent return
    # delete all geo without geo cache
    #     # check pre 10 objects
    # clear all MDGGrp_*
    
    McdMarkClothMeshSkinClusterOnAndOff(1)
    
    allMDNodes = cmds.ls(type = "McdMeshDrive")
    if not McdIsBlank(allMDNodes):
        for i in range(len(allMDNodes)):
            try:
                cmds.delete(allMDNodes[i])
            except:
                pass
    
    allAgentShapes = cmds.ls(type = "McdAgent")
    if allAgentShapes != [] and allAgentShapes != None:
        cmds.select(clear = True)
        for i in range(len(allAgentShapes)):
            agentParent = cmds.listRelatives(allAgentShapes[i], p = True)[0]
            try:
                cmds.delete(agentParent)
            except:
                pass
    
    cmds.flushUndo() # clear dump
    
    # showHidden
    allAgentGrp = cmds.ls(type = "McdAgentGroup")
    try:
        cmds.showHidden(allAgentGrp)
    except:
        pass
    
    allPlaceNodes = cmds.ls(type = "McdPlace")
    try:
        for i in range(len(allPlaceNodes)):
            transform = cmds.listRelatives(allPlaceNodes[i], p = True, c = False)[0]
            cmds.showHidden(transform)
    except:
        pass
    
    # agent return:
    try:
        cmd = "McdAgentMatchCmd -mm 0;"
        mel.eval(cmd)
    except:
        pass
    
    allMDMesh = cmds.ls("MDG_*", type = "mesh")
    if allMDMesh == [] or allMDMesh == None:
        cmds.flushUndo() # clear memory
        return
    
    counter = 10
    cached = False
    for i in range(len(allMDMesh)):
        allHis = cmds.listConnections(allMDMesh, s = True, d = False)
        try:
            if allHis != None and allHis != []:
                for j in range(len(allHis)):
                    if cmds.nodeType(allHis[j]) == "historySwitch":
                        cached = True
        except:
            pass
        
        if counter < 0:
            break
        counter -= 1
        
    if not cached:
        stat = cmds.confirmDialog(t = "Question", m = "Do you want to delete duplicated meshes?", b = ["Yes", "No"])
        if stat == "No":
            cmds.flushUndo() # clear memory
            return
    
        allGrps = cmds.ls("MDGGrp_*", l = True)
        if allGrps != [] and allGrps != None:
            for i in range(len(allGrps)):
                try:
                    cmds.delete(allGrps[i])
                except:
                    pass

        allGrps = cmds.ls("MDG_*", l = True)
        if allGrps != [] and allGrps != None:
            for i in range(len(allGrps)):
                try:
                    cmds.delete(allGrps[i])
                except:
                    pass
        
        stat = cmds.confirmDialog(t = "Question", m = "Do you want to delete useless shader?", b = ["Yes", "No"])
        if stat == "Yes":
            McdClearUselessShader()
        
        
    cmds.flushUndo() # clear dump

def McdAttachTerrain():
    selObj = cmds.ls(sl = True)
    if selObj == [] or selObj == None:
        cmds.confirmDialog(t = "Error", m = 'First select placement node, then terrain geometry, and try again.')
        raise Exception('First select placement node, then terrain geometry.')
    if len(selObj) < 2:
        cmds.confirmDialog(t = "Error", m = 'First select placement node, then terrain geometry, and try again.')
        raise Exception('First select placement node, then terrain geometry.')
    
    placeNode = ""
    placeTransform = ""
    terrainNode = ""
    terrainTransform = ""
    if cmds.nodeType(selObj[0]) == "McdPlace":
        placeNode = selObj[0]
        placeTransform = cmds.listRelatives(placeNode, c = False, p = True)[0]
    else:
        allChild = cmds.listRelatives(selObj[0]);
        if allChild == [] or allChild == None:
            cmds.confirmDialog(t = "Error", m = 'First select placement node, then terrain geometry, and try again.')
            raise Exception('First select placement node, then terrain geometry.')
        if cmds.nodeType(allChild[0]) == "McdPlace":
            placeNode = allChild[0]
        else:
            cmds.confirmDialog(t = "Error", m = 'First select placement node, then terrain geometry, and try again.')
            raise Exception('First select placement node, then terrain geometry.')
        placeTransform = selObj[0]
            
    if cmds.nodeType(selObj[1]) == "mesh":
        terrainNode = selObj[1]
        terrainTransform = cmds.listRelatives(terrainNode, c = False, p = True)[0]
    else:
        allChild = cmds.listRelatives(selObj[1]);
        if allChild == [] or allChild == None:
            cmds.confirmDialog(t = "Error", m = 'First select placement node, then terrain geometry, and try again.')
            raise Exception('First select placement node, then terrain geometry.')
        if cmds.nodeType(allChild[0]) == "mesh":
            terrainNode = allChild[0]
        else:
            cmds.confirmDialog(t = "Error", m = 'First select placement node, then terrain geometry, and try again.')
            raise Exception('First select placement node, then terrain geometry.')
        terrainTransform = selObj[1]
        
    # test terrain world transform:
    nillMat = True;
    trnWMat = cmds.getAttr(terrainTransform + ".worldMatrix")
    for i in range(16):
        if i == 0 or i == 5 or i == 10 or i == 15:
            if not isFloatEqual(trnWMat[i], 1.0):
                nillMat = False
        else:
            if not isFloatEqual(trnWMat[i], 0.0):
                nillMat = False
             
    stat = ""   
    if not nillMat:
        # check already parented.
        allParents = cmds.listRelatives(placeTransform, c = False, p = True)
        if allParents == [] or allParents == None:
            allParents = []
        if terrainTransform not in allParents:
            stat = cmds.confirmDialog(t = "Warning", m = 'System detect your terrain mesh with translate, rotate, or scale. ' + \
                                                        'Attach this terrain may cause "shift" problem. \nTo solve this, you can parent ' + \
                                                        'your place node to the terrain. Are you willing to parent it?', \
                                                        b = ["Yes", "Help", "Cancel"])
            if stat == "Yes":
                try:
                    cmds.parent(placeTransform, terrainTransform)
                except:
                    pass
                try:
                    cmds.connectAttr(terrainNode + ".outMesh", placeNode + ".inTerrain", f = True)
                except:
                    pass
        else:
            try:
                # connect directly:
                cmds.connectAttr(terrainNode + ".outMesh", placeNode + ".inTerrain", f = True)
            except:
                pass

        clearTransform(placeTransform)
    else:
        try:
            # connect directly:
            cmds.connectAttr(terrainNode + ".outMesh", placeNode + ".inTerrain", f = True)
        except:
            pass
          
          
def McdDetachTerrain():
    selObj = cmds.ls(sl = True)
    if selObj == [] or selObj == None:
        cmds.confirmDialog(t = "Error", m = 'Please select a placement node, and try again.')
        return
    if len(selObj) < 1:
        cmds.confirmDialog(t = "Error", m = 'Please select a placement node, and try again.')
        return
        
        
def McdAttachRangeMesh():
    selObj = cmds.ls(sl = True)
    if selObj == [] or selObj == None:
        cmds.confirmDialog(t = "Error", m = 'First select placement node, then polygon mesh, and try again.')
        return
    if len(selObj) < 2:
        cmds.confirmDialog(t = "Error", m = 'First select placement node, then polygon mesh, and try again.')
        return
    
    placeNode = ""
    placeTransform = ""
    terrainNode = ""
    terrainTransform = ""
    if cmds.nodeType(selObj[0]) == "McdPlace":
        placeNode = selObj[0]
        placeTransform = cmds.listRelatives(placeNode, c = False, p = True)[0]
    else:
        allChild = cmds.listRelatives(selObj[0]);
        if allChild == [] or allChild == None:
            cmds.confirmDialog(t = "Error", m = 'First select placement node, then polygon mesh, and try again.')
            return
        if cmds.nodeType(allChild[0]) == "McdPlace":
            placeNode = allChild[0]
        else:
            cmds.confirmDialog(t = "Error", m = 'First select placement node, then polygon mesh, and try again.')
            return
        placeTransform = selObj[0]
            
    if cmds.nodeType(selObj[1]) == "mesh":
        terrainNode = selObj[1]
        terrainTransform = cmds.listRelatives(terrainNode, c = False, p = True)[0]
    else:
        allChild = cmds.listRelatives(selObj[1]);
        if allChild == [] or allChild == None:
            cmds.confirmDialog(t = "Error", m = 'First select placement node, then polygon mesh, and try again.')
            return
        if cmds.nodeType(allChild[0]) == "mesh":
            terrainNode = allChild[0]
        else:
            cmds.confirmDialog(t = "Error", m = 'First select placement node, then polygon mesh, and try again.')
            return
        terrainTransform = selObj[1]
        
    # test terrain world transform:
    nillMat = True;
    trnWMat = cmds.getAttr(terrainTransform + ".worldMatrix")
    for i in range(16):
        if i == 0 or i == 5 or i == 10 or i == 15:
            if not isFloatEqual(trnWMat[i], 1.0):
                nillMat = False
        else:
            if not isFloatEqual(trnWMat[i], 0.0):
                nillMat = False
             
    stat = ""   
    if not nillMat:
        # check already parented.
        allParents = cmds.listRelatives(placeTransform, c = False, p = True)
        if allParents == [] or allParents == None:
            allParents = []
        if terrainTransform not in allParents:
            stat = cmds.confirmDialog(t = "Warning", m = 'System detect your range mesh with translate, rotate, or scale. ' + \
                                                        'Attach this terrain may cause "shift" problem. \nTo solve this, you can parent ' + \
                                                        'your place node to the terrain. Are you willing to parent it?', \
                                                        b = ["Yes", "Help", "Cancel"])
            if stat == "Yes":
                try:
                    cmds.parent(placeTransform, terrainTransform)
                except:
                    pass
                try:
                    cmds.connectAttr(terrainNode + ".outMesh", placeNode + ".inPolygon", f = True)
                except:
                    pass
        else:
            try:
                # connect directly:
                cmds.connectAttr(terrainNode + ".outMesh", placeNode + ".inPolygon", f = True)
            except:
                pass

        clearTransform(placeTransform)
    else:
        try:
            # connect directly:
            cmds.connectAttr(terrainNode + ".outMesh", placeNode + ".inPolygon", f = True)
        except:
            pass
          
          
def McdDetachRangeMesh():
    selObj = cmds.ls(sl = True)
    if selObj == [] or selObj == None:
        cmds.confirmDialog(t = "Error", m = 'Please select a placement node, and try again.')
        return
    if len(selObj) < 1:
        cmds.confirmDialog(t = "Error", m = 'Please select a placement node, and try again.')
        return

        
def McdAttachCurve():
    selObj = cmds.ls(sl = True)
    if selObj == [] or selObj == None:
        cmds.confirmDialog(t = "Error", m = 'First select placement node, then nurbs curve, and try again.')
        return
    if len(selObj) < 2:
        cmds.confirmDialog(t = "Error", m = 'First select placement node, then nurbs curve, and try again.')
        return
        
    placeNode = ""
    curveNode = ""
    if cmds.nodeType(selObj[0]) == "McdPlace":
        placeNode = selObj[0]
    else:
        allChild = cmds.listRelatives(selObj[0]);
        if allChild == [] or allChild == None:
            cmds.confirmDialog(t = "Error", m = 'First select placement node, then nurbs curve, and try again.')
            return
        if cmds.nodeType(allChild[0]) == "McdPlace":
            placeNode = allChild[0]
        else:
            cmds.confirmDialog(t = "Error", m = 'First select placement node, then nurbs curve, and try again.')
            return
            
    if cmds.nodeType(selObj[1]) == "nurbsCurve":
        curveNode = selObj[1]
    else:
        allChild = cmds.listRelatives(selObj[1]);
        if allChild == [] or allChild == None:
            cmds.confirmDialog(t = "Error", m = 'First select placement node, then nurbs curve, and try again.')
            return
        if cmds.nodeType(allChild[0]) == "nurbsCurve":
            curveNode = allChild[0]
        else:
            cmds.confirmDialog(t = "Error", m = 'First select placement node, then nurbs curve, and try again.')
            return
            
    try:
        cmds.connectAttr(curveNode + ".worldSpace", placeNode + ".inCurve", f = True)
    except:
        pass
            
            
def inversePlacementAgent():
    cmd = "McdInvPlacementCmd;"
    placeNode = mel.eval(cmd)
    
def duplicatePlacement():
    allGlobal = cmds.ls(type = "McdGlobal")
    
    if MIsBlank(allGlobal):
        cmds.confirmDialog(t = "Abort", m = 'No found McdGlobal node, please click Miarmy Ready.')
        return
    
    selObj = getSelection("McdPlace")
    
    # type filter
    ptype = cmds.getAttr(selObj + ".placeType")
    if ptype == 1 or ptype == 2 or ptype == 3:
        cmds.confirmDialog(t = "Abort", m = 'Cannot duplicate circle, curve, and polygon type.')
        return
    
    # McdGlobal enable
    for i in range(len(allGlobal)):
        cmds.setAttr(allGlobal[i] + ".boolMaster[4]", 1)
    
    # duplicate selObj
    dupNode = cmds.duplicate(selObj, rr = True)[0]
    
    # connect attr:
    cmds.connectAttr(dupNode + ".translateX", dupNode + ".localPositionX")
    cmds.connectAttr(dupNode + ".translateY", dupNode + ".localPositionY")
    cmds.connectAttr(dupNode + ".translateZ", dupNode + ".localPositionZ")
    
    
    # McdGlobal disable
    for i in range(len(allGlobal)):
        cmds.setAttr(allGlobal[i] + ".boolMaster[4]", 0)
    


def checkInverseAndNormalExist():
    allPlaceNode = cmds.ls(type = "McdPlace")
    if allPlaceNode == [] or allPlaceNode == None:
        return False
    if len(allPlaceNode) < 2:
        return False
    
    gotNormalPlace = False
    gotInversePlace = False
    
    for i in range(len(allPlaceNode)):
        placeType = cmds.getAttr(allPlaceNode[i] + ".placeType")
        if placeType != 5:
            # we got normal node
            gotNormalPlace = True
        else:
            # we got custom place node:
            parent0 = cmds.getAttr(allPlaceNode[i] + ".parentSet[0]")
            if parent0 != "" and parent0 != None:
                # we got inverse place node:
                gotInversePlace = True
            else:
                gotNormalPlace = True
    
    if gotNormalPlace and gotInversePlace:
        return True
    
    return False

def McdFromAgentsGetPlace(allSelAgents):
    
    allPlaceNodes = cmds.ls(type = "McdPlace")
    allPlacePlid = []
    for i in range(len(allPlaceNodes)):
        plid = cmds.getAttr(allPlaceNodes[i] + ".plid")
        allPlacePlid.append(plid)
        
    result = []
    for i in range(len(allSelAgents)):
        plid = cmds.getAttr(allSelAgents[i] + ".plid")
        plaid = cmds.getAttr(allSelAgents[i] + ".plaid")
        for j in range(len(allPlacePlid)):
            if plid == allPlacePlid[j]:
                result.append(allPlaceNodes[j])
                result.append(plaid)
        
    return result

def McdMarkAgentOut():
    selAgents = cmds.ls(sl = True)
    if McdIsBlank(selAgents):
        cmds.confirmDialog(t = "Error", m = "Please firstly select some agents node, and try again.")
        return
    
    haveError = False
    agentShapes = []
    for i in range(len(selAgents)):
        shapeNode = cmds.listRelatives(selAgents[i], c = True, p = False)
        if McdIsBlank(shapeNode):
            haveError = True
            break
        if cmds.nodeType(shapeNode[0]) != "McdAgent":
            haveError = True
            break
        else:
            agentShapes.append(shapeNode[0])
            
    if haveError:
        cmds.confirmDialog(t = "Error", m = "Some of your selected, are not agent transform node")
        return
    
    agent_place_Info = McdFromAgentsGetPlace(agentShapes)
    
    allPlaceNodes = cmds.ls(type = "McdPlace")
    allPlacePlid = []
    for i in range(len(allPlaceNodes)):
        plid = cmds.getAttr(allPlaceNodes[i] + ".plid")
        allPlacePlid.append(plid)
    
    
    # mark out
    nbMarkOut = len(agent_place_Info) / 2
    for i in range(nbMarkOut):
        cmds.setAttr(agent_place_Info[i*2] + ".extraPlacement[" + str(agent_place_Info[i*2+1]) + "].extraPlace[4]", 1)
    
    # if have cache enable, prompt , and redo the cache
    globalNode = McdGetMcdGlobalNode()
    enableCache = cmds.getAttr(globalNode + ".enableCache")
    
    if enableCache == 1:
        # hide agent and redo cache
        stat1 = "Rebuild"
        stat = cmds.confirmDialog(t = "Warning!!", m = "We detected you're using agent cache, rebuild it now??", b = ["Yes", "No", "Cancel Operation"])
        if stat == "Cancel Operation":
            return;
        if stat == "No":
            stat1 = cmds.confirmDialog(t = "Warning!! Warning!!", m = "If you not rebuild your agent cache, your old cache will useless, because agent number changes", b = ["Rebuild", "No"])
        
        if stat1 == "Rebuild":
            nbMarkOut = len(agent_place_Info) / 2
            for i in range(nbMarkOut):
                cmds.setAttr(agent_place_Info[i*2] + ".extraPlacement[" + str(agent_place_Info[i*2+1]) + "].extraPlace[4]", 1)
                
            cmds.hide() # hide all selected agents:
            cmds.setAttr(globalNode + ".funcParamList[1]", 1)
            if mel.eval("McdMakeCacheCmd;") == True:
                # re-set the caceh folder;
                cacheName = cmds.getAttr(globalNode + ".cacheName")
                cachenameNew = cacheName + "_new"
                cmds.setAttr(globalNode + ".cacheName", cachenameNew, type = "string")
            
            # deplace
            cmds.confirmDialog(t = "Warning", m = "Please save your scene, \notherwise agent place skip flags will discard and agent cache will useless.")
            dePlacementAgent()
                
        
        
    else:
        nbMarkOut = len(agent_place_Info) / 2
        for i in range(nbMarkOut):
            cmds.setAttr(agent_place_Info[i*2] + ".extraPlacement[" + str(agent_place_Info[i*2+1]) + "].extraPlace[4]", 1)
        cmds.confirmDialog(t = "Warning", m = "Please save your scene, and re-place agents")
        dePlacementAgent()
    
    
def McdCreatePlacementNodeMesh():
    
    # test mesh selected?
    # read info from mesh
    
    meshNode = getSelection("mesh")
    allPointsData = mel.eval("McdSimpleCommand -exe 32");
    if MIsBlank(allPointsData):
        cmds.confirmDialog(t = "Error", m = "Mesh data error");
        return;
    
    McdCreatePlacementNode()
    
    selObj = getSelection()
    
    # set to posLock Mode
    nbPoints = len(allPointsData) / 3
    
    cmds.setAttr(selObj + ".placeType", 5)
    cmds.setAttr(selObj + ".numOfAgent", nbPoints)
    
    for i in range(nbPoints):
        cmds.setAttr(selObj + ".placement[" + str(i) + "].agentPlace[1]", allPointsData[i * 3])
        cmds.setAttr(selObj + ".placement[" + str(i) + "].agentPlace[2]", allPointsData[i * 3 + 1])
        cmds.setAttr(selObj + ".placement[" + str(i) + "].agentPlace[3]", allPointsData[i * 3 + 2])
        
    # important!! connect message!
    allConns = cmds.listConnections(meshNode, s = False, d = True, shapes = True, type = "McdFormation")
    if MIsBlank(allConns):
        cmds.confirmDialog(t = "Warning!", m = "cannot detect formation node, may cause formation not useable")
        return
    formationNode = allConns[0]
    placeNode = selObj
    try:
        cmds.connectAttr(formationNode + ".outEntity", placeNode + ".formationEntity", force = True)
    except:
        cmds.confirmDialog(t = "Warning!", m = "Mesh entity connection failure, may cause formation not useable")
        
    
def McdCreatePlacementNodeLattice():
    # test lattice selected?
    # read info from mesh
    
    latticeNode = getSelection("lattice")
    allPointsData = mel.eval("McdSimpleCommand -exe 33");
    if MIsBlank(allPointsData):
        cmds.confirmDialog(t = "Error", m = "lattice data error");
        return;
    
    McdCreatePlacementNode()
    
    selObj = getSelection()
    
    # set to posLock Mode
    nbPoints = len(allPointsData) / 3
    
    cmds.setAttr(selObj + ".placeType", 5)
    cmds.setAttr(selObj + ".numOfAgent", nbPoints)
    
    for i in range(nbPoints):
        cmds.setAttr(selObj + ".placement[" + str(i) + "].agentPlace[1]", allPointsData[i * 3])
        cmds.setAttr(selObj + ".placement[" + str(i) + "].agentPlace[2]", allPointsData[i * 3 + 1])
        cmds.setAttr(selObj + ".placement[" + str(i) + "].agentPlace[3]", allPointsData[i * 3 + 2])
        
    # important!! connect message!
    allConns = cmds.listConnections(latticeNode, s = False, d = True, shapes = True, type = "McdFormation")
    if MIsBlank(allConns):
        cmds.confirmDialog(t = "Warning!", m = "cannot detect formation node, may cause formation not useable")
        return
    formationNode = allConns[0]
    placeNode = selObj
        
    try:
        cmds.connectAttr(formationNode + ".outEntity", placeNode + ".formationEntity", force = True)
    except:
        cmds.confirmDialog(t = "Warning!", m = "Lattice entity connection failure, may cause formation not useable")
    
    
    
def McdCreatePlacementNodeParticle(is3D):
    # test lattice selected?
    # read info from mesh
    
    ptNode = getSelection("particle")
    allPointsData = []
    ptCount = cmds.getAttr(ptNode + ".count")
    
    if ptCount == 0:
        cmds.confirmDialog(t = "Abort", m = "No particle instance in particle shape.");
        return; 
    
    for i in range(ptCount):
        stri = str(i)
        currentPos = cmds.xform(ptNode + '.pt[' + stri + ']', q = True, t = True)
        for j in range(3):
            allPointsData.append(currentPos[j])

    McdCreatePlacementNode()
    
    selObj = getSelection()
    
    # set to posLock Mode
    nbPoints = len(allPointsData) / 3
    
    cmds.setAttr(selObj + ".placeType", 5)
    cmds.setAttr(selObj + ".numOfAgent", nbPoints)
    
    if is3D == 0:
        for i in range(nbPoints):
            cmds.setAttr(selObj + ".placement[" + str(i) + "].agentPlace[1]", allPointsData[i * 3])
            cmds.setAttr(selObj + ".placement[" + str(i) + "].agentPlace[2]", 0.0)
            cmds.setAttr(selObj + ".placement[" + str(i) + "].agentPlace[3]", allPointsData[i * 3 + 2])
    else:
        for i in range(nbPoints):
            cmds.setAttr(selObj + ".placement[" + str(i) + "].agentPlace[1]", allPointsData[i * 3])
            cmds.setAttr(selObj + ".placement[" + str(i) + "].agentPlace[2]", allPointsData[i * 3 + 1])
            cmds.setAttr(selObj + ".placement[" + str(i) + "].agentPlace[3]", allPointsData[i * 3 + 2])
    
    
    stat = cmds.confirmDialog(t = "Particle Following", m = "Do you want to link particle system to place node??\n" + \
                     "This can enable particle following feature.\n\n\n" + \
                     "If you dont want to use it please do not link for saving memory.", b = ["Link", "Do not Link"]);
    
    if stat == "Link":
        placeNode = cmds.listRelatives(selObj, c = True, p = False)[0]
        cmds.connectAttr(ptNode + ".count", placeNode + ".localScaleX")
    
    
    
    
def McdCreatePlacementNodeNParticle(is3D):
    # test lattice selected?
    # read info from mesh
    
    ptNode = getSelection("nParticle")
    allPointsData = []
    ptCount = cmds.getAttr(ptNode + ".count")
    
    if ptCount == 0:
        cmds.confirmDialog(t = "Abort", m = "No nParticle instance in particle shape.");
        return; 
    
    for i in range(ptCount):
        stri = str(i)
        currentPos = cmds.xform(ptNode + '.pt[' + stri + ']', q = True, t = True)
        for j in range(3):
            allPointsData.append(currentPos[j])

    McdCreatePlacementNode()
    
    selObj = getSelection()
    
    # set to posLock Mode
    nbPoints = len(allPointsData) / 3
    
    cmds.setAttr(selObj + ".placeType", 5)
    cmds.setAttr(selObj + ".numOfAgent", nbPoints)
    
    if is3D == 0:
        for i in range(nbPoints):
            cmds.setAttr(selObj + ".placement[" + str(i) + "].agentPlace[1]", allPointsData[i * 3])
            cmds.setAttr(selObj + ".placement[" + str(i) + "].agentPlace[2]", 0.0)
            cmds.setAttr(selObj + ".placement[" + str(i) + "].agentPlace[3]", allPointsData[i * 3 + 2])
    else:
        for i in range(nbPoints):
            cmds.setAttr(selObj + ".placement[" + str(i) + "].agentPlace[1]", allPointsData[i * 3])
            cmds.setAttr(selObj + ".placement[" + str(i) + "].agentPlace[2]", allPointsData[i * 3 + 1])
            cmds.setAttr(selObj + ".placement[" + str(i) + "].agentPlace[3]", allPointsData[i * 3 + 2])
    
    stat = cmds.confirmDialog(t = "Particle Following", m = "Do you want to link particle system to place node??\n" + \
                     "This can enable particle following feature.\n\n\n" + \
                     "If you dont want to use it please do not link for saving memory.", b = ["Link", "Do not Link"]);
    
    if stat == "Link":
        placeNode = cmds.listRelatives(selObj, c = True, p = False)[0]
        cmds.connectAttr(ptNode + ".count", placeNode + ".localScaleX")
        
    
    
    
    
    
    

