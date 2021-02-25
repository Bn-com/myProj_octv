## +
## ===================================================================
## Copyright(C) 2010 - 2012 Basefount Technology (Hong Kong) Limited.
## and/or its licensors.  All rights reserved.
##
## The coded instructions, statements, computer programs, and/or
## related material (collectively the "Data") in these files contain
## unpublished information proprietary to Basefount Technology
## (Hong Kong) Limitd. ("Basefount") and/or its licensors, which is
## protected by Hong Kong copyright law and by international treaties.
##
## The Data is provided for use exclusively by You. You have the right 
## to use, modify, and incorporate this Data into other products for 
## purposes authorized by the Basefount software license agreement, 
## without fee.
##
## The copyright notices in the Software and this entire statement, 
## including the above license grant, this restriction and the 
## following disclaimer, must be included in all copies of the 
## Software, in whole or in part, and all derivative works of 
## the Software, unless such copies or derivative works are solely 
## in the form of machine-executable object code generated by a 
## source language processor.
##
## THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND. 
## BASEFOUNT DOES NOT MAKE AND HEREBY DISCLAIMS ANY EXPRESS OR
## IMPLIED WARRANTIES INCLUDING, BUT NOT LIMITED TO, THE WARRANTIES
## OF NON-INFRINGEMENT, MERCHANTABILITY OR FITNESS FOR A PARTICULAR 
## PURPOSE, OR ARISING FROM A COURSE OF DEALING, USAGE, OR 
## TRADE PRACTICE. IN NO EVENT WILL BASEFOUNT AND/OR ITS LICENSORS 
## BE LIABLE FOR ANY LOST REVENUES, DATA, OR PROFITS, OR SPECIAL, 
## DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES, EVEN IF BASEFOUNTAIN 
## AND/OR ITS LICENSORS HAS BEEN ADVISED OF THE POSSIBILITY 
## OR PROBABILITY OF SUCH DAMAGES.
##
## ===================================================================
## -

## +
## ===================================================================
##  Module Name: McdMakeAgentCache.py
##
##  Description:
##    Make cache
##
## ===================================================================

import maya.cmds as cmds
import maya.mel as mel
from McdGeneral import *
from McdMakeFootMap import *
import os


def McdMakeAgentCache():

    performCachePreCheck()

    # batch make cache: --------------------------------------------------------
    startFrame = cmds.playbackOptions(q =True, min = True)
    endFrame = cmds.playbackOptions(q =True, max = True)
    
    stat = cmds.confirmDialog(t = "Agent Cache", m = "The agent cache information:\n" + \
                                            "Start Frame " + str(startFrame) + "\n" + \
                                            "End Frame: " + str(endFrame) + "\n" + \
                                            "If cache exist, new created cache will override the old one.", \
                                            b = ["Continue", "Cancel"])
    if stat == "Cancel":
        return
    
    globalNode = mel.eval("McdSimpleCommand -execute 2")
    
    isCallback = cmds.getAttr(globalNode + ".boolMaster[6]")
    if isCallback:
        executePreSim(globalNode)
    
    try:
        genFootLoc = cmds.getAttr(globalNode + ".genFootLoc")
    except:
        genFootLoc = 0
    
    brainNode = mel.eval("McdSimpleCommand -execute 3")
    solverFrame = cmds.getAttr(brainNode + ".startTime")
    solverFrame -= 1
    if solverFrame > startFrame:
        solverFrame = startFrame
    
    amount = 0
    counter = 0
    totalCount = endFrame - startFrame
    cmds.progressWindow( title = "Caching:", progress = 0, \
                      min = 0, max = 100, \
                      status = "caching", isInterruptable = True )
    
    # from solverFrame to endFrame:
    cmds.setAttr(globalNode + ".enableIDCM", 1)
    while(solverFrame <= endFrame):
        
        if isCallback:
            executePreFrame(globalNode)
        
        cmds.currentTime(solverFrame)
        
        if solverFrame >= startFrame:
            # deal with batch cache
            mel.eval("McdMakeCacheCmd;")
            
        if isCallback:
            executePostFrame(globalNode)
            
        if genFootLoc == 1:
            if counter == 0:
                CreateAndUpdateFootLoc(True)
            else:
                CreateAndUpdateFootLoc()
            
        solverFrame += 1
        
        ## progress operation: ////////////////////////////////////////////////
        if cmds.progressWindow( query = True, isCancelled = True ):
            cmds.setAttr(globalNode + ".enableIDCM", 0)
            break
        counter += 1
        amount = float(counter) / float(totalCount) * 100.0
        cmds.progressWindow( edit = True, progress = amount)
        
    cmds.progressWindow(endProgress=1)
    cmds.setAttr(globalNode + ".enableIDCM", 0)
    
    cmds.setAttr(globalNode + ".cacheVersion", 155)
    
    if isCallback:
        executePostSim(globalNode)
    
def performCachePreCheck():
    # agent exist
    allAgents = cmds.ls(type = "McdAgent")
    if allAgents == [] or allAgents == None:
        cmds.confirmDialog(t = "Auto abort", m = "There is no agent in scene for making cache.")
        raise Exception("There is no agent in scene for making cache.")
        
    # path writable:
    globalNode = mel.eval("McdSimpleCommand -execute 2")
    rawPath = cmds.getAttr(globalNode + ".cacheFolder")
    
    cacheFolder = envPath2AbsPath(rawPath)
    
    if cacheFolder == "" or cacheFolder == None:
        cmds.confirmDialog(t = "Error", m = "The output folder is not exist. Specify it in Miarmy > Miarmy Global.")
        raise Exception("The output folder is not exist.")
        
    if not os.access(cacheFolder, os.W_OK):
        cmds.confirmDialog(t = "Error", m = "The output folder is not writable. Specify it in Miarmy > Miarmy Global")
        raise Exception("The output folder is not exist.")
    

def McdMergeAgentCache():

    allAgent = cmds.ls(type = "McdAgent")
    if not McdIsBlank(allAgent):
        cmds.confirmDialog(t = "Error", m = "Please deplace agents.")
        return;

    # batch make cache: --------------------------------------------------------
    startFrame = cmds.playbackOptions(q =True, min = True)
    endFrame = cmds.playbackOptions(q =True, max = True)
    
    stat = cmds.confirmDialog(t = "Merge Cache", m = "The agent cache information:\n" + \
                                            "Start Frame " + str(startFrame) + "\n" + \
                                            "End Frame: " + str(endFrame) + "\n" + \
                                            "If cache exist, new created cache will override the old one.", \
                                            b = ["Continue", "Cancel"])
    if stat == "Cancel":
        return
    
    globalNode = mel.eval("McdSimpleCommand -execute 2")
    
    brainNode = mel.eval("McdSimpleCommand -execute 3")
    solverFrame = cmds.getAttr(brainNode + ".startTime")
    solverFrame -= 1
    if solverFrame > startFrame:
        solverFrame = startFrame
    
    amount = 0
    counter = 0
    totalCount = endFrame - startFrame
    cmds.progressWindow( title = "Caching:", progress = 0, \
                      min = 0, max = 100, \
                      status = "caching", isInterruptable = True )
    
    # from solverFrame to endFrame:
    while(solverFrame <= endFrame):
        cmds.currentTime(solverFrame)
        
        if solverFrame >= startFrame:
            # deal with batch cache
            mel.eval("McdSimpleCommand -exe 29")
            
        solverFrame += 1
        
        ## progress operation: ////////////////////////////////////////////////
        if cmds.progressWindow( query = True, isCancelled = True ):
            break
        counter += 1
        amount = float(counter) / float(totalCount) * 100.0
        cmds.progressWindow( edit = True, progress = amount)
        
    cmds.progressWindow(endProgress=1)
    
    cmds.setAttr(globalNode + ".cacheVersion", 155)
















