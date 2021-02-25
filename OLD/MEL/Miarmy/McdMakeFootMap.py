#!/usr/bin/env python
    
import maya.cmds as cmds
import maya.mel as mel
from McdGeneral import *
import os


def McdMakeFootMap():

    MakeFootMapPreCheck()

    # batch make cache: --------------------------------------------------------
    startFrame = cmds.playbackOptions(q =True, min = True)
    endFrame = cmds.playbackOptions(q =True, max = True)
    
    stat = cmds.confirmDialog(t = "Make Footprint Maps", m = "The maps information:\n" + \
                                            "Start Frame " + str(startFrame) + "\n" + \
                                            "End Frame: " + str(endFrame) + "\n" + \
                                            "If maps exist, new created maps will override the old ones.", \
                                            b = ["Continue", "Cancel"])
    if stat == "Cancel":
        return
    
    brainNode = mel.eval("McdSimpleCommand -execute 3")
    solverFrame = cmds.getAttr(brainNode + ".startTime")
    solverFrame -= 1
    if solverFrame > startFrame:
        solverFrame = startFrame
    
    amount = 0
    counter = 0
    totalCount = endFrame - startFrame
    cmds.progressWindow( title = "Making:", progress = 0, \
                      min = 0, max = 100, \
                      status = "Making", isInterruptable = True )
    
    # from solverFrame to endFrame:
    while(solverFrame <= endFrame):
        cmds.currentTime(solverFrame)
        
        if solverFrame >= startFrame:
            # deal with batch cache
            mel.eval("McdGenFootMapCmd;");
            
        solverFrame += 1
        
        ## progress operation: ////////////////////////////////////////////////
        if cmds.progressWindow( query = True, isCancelled = True ):
            break
        counter += 1
        amount = float(counter) / float(totalCount) * 100.0
        cmds.progressWindow( edit = True, progress = amount)
        
    cmds.progressWindow(endProgress=1)
    
def MakeFootMapPreCheck():
    # agent exist
    allAgents = cmds.ls(type = "McdAgent")
    if allAgents == [] or allAgents == None:
        cmds.confirmDialog(t = "Abort", m = "There is no agent in scene for making maps.")
        raise Exception("There is no agent in scene for making maps.")
        
    # path writable:
    globalNode = mel.eval("McdSimpleCommand -execute 2")
    cacheFolder = cmds.getAttr(globalNode + ".footMapPath")
    if cacheFolder == "" or cacheFolder == None:
        cmds.confirmDialog(t = "Error", m = "The output folder is not exist. Specify it in Miarmy > Miarmy Global.")
        raise Exception("The output folder is not exist.")
        
    if not os.access(cacheFolder, os.W_OK):
        cmds.confirmDialog(t = "Error", m = "The output folder is not writable. Specify it in Miarmy > Miarmy Global")
        raise Exception("The output folder is not exist.")


    cacheName = cmds.getAttr(globalNode + ".footMapName")
    if cacheName == "" or cacheName == None:
        cmds.confirmDialog(t = "Error", m = "Foot Map Name is blank, please fill at Miarmy > Miarmy Global.")
        raise Exception("Foot Map Name is blank, please fill at Miarmy > Miarmy Global.")
        
def CreateAndUpdateFootLoc(isFirstFrame = False):
    #run command and return values
    #stat info
    #find or create locator
    #keyframe
    
    #run command and return values
    returnVal = mel.eval("McdAgentMatchCmd -mm 5;")
    
    if McdIsBlank(returnVal):
        return
    
    feetNum = len(returnVal) / 4
    
    currentLoc = cmds.ls("McdFootLocatorGroup")
    if McdIsBlank(currentLoc):
        cmds.select(clear = True)
        cmds.group(n = "McdFootLocatorGroup", em = True)
    
    for i in range(feetNum):
        #find or create locator
        stri = str(i)
        locatorName = "McdFootLocator" + stri
        if isFirstFrame:
            try:
                currentLoc = cmds.ls(locatorName)[0]
            except:
                cmds.spaceLocator(n = locatorName)
        
        cmds.setAttr(locatorName + ".v", returnVal[i * 4])
        cmds.setAttr(locatorName + ".t", returnVal[i * 4 + 1], returnVal[i * 4 + 2], returnVal[i * 4 + 3])
        
        if isFirstFrame:
            cmds.parent(locatorName, "McdFootLocatorGroup")
        
        #keyframe
        cmds.setKeyframe(locatorName, at = "t")
        cmds.setKeyframe(locatorName, at = "v")
        
        
    
    
    
def McdMakeFootLocatorsSL():
    # stand alone
    
    autoKeyState = cmds.autoKeyframe( q = True, state = True)
    cmds.autoKeyframe( e = True, state = False)
    
    # batch make cache: --------------------------------------------------------
    startFrame = cmds.playbackOptions(q =True, min = True)
    endFrame = cmds.playbackOptions(q =True, max = True)
    totalFrame = endFrame - startFrame + 1
    
    stat = cmds.confirmDialog(t = "Generate Foot Locators", m = "The scene animation information:\n" + \
                                            "Start Frame " + str(startFrame) + "\n" + \
                                            "End Frame: " + str(endFrame) + "\n" + \
                                            "If animation exist, new created animation will override the old ones.", \
                                            b = ["Continue", "Cancel"])
    if stat == "Cancel":
        return
    
    amount = 0
    counter = 0
    cmds.progressWindow( title = "Generating:", progress = 0, \
                      min = 0, max = totalFrame, \
                      status = "Generating", isInterruptable = True )
    
    solverFrame = startFrame
    # from solverFrame to endFrame:
    for i in range(int(totalFrame)):
        cmds.currentTime(solverFrame)
        
        if i==0:
            CreateAndUpdateFootLoc(True)    # first frame
        else:
            CreateAndUpdateFootLoc()        # the rest
            
        solverFrame += 1
        
        ## progress operation: ////////////////////////////////////////////////
        if cmds.progressWindow( query = True, isCancelled = True ):
            break
        counter += 1
        
        cmds.progressWindow( edit = True, progress = i)
        
    cmds.progressWindow(endProgress=1)
    
    
    
    cmds.autoKeyframe( e = True, state = autoKeyState)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

