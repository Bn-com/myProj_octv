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
## DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES, EVEN IF BASEFOUNT 
## AND/OR ITS LICENSORS HAS BEEN ADVISED OF THE POSSIBILITY 
## OR PROBABILITY OF SUCH DAMAGES.
##
## ===================================================================
## -

## +
## ===================================================================
##  Module Name: McdRenderABCFunctions.py
##
##  Description:
##    Create Alembic cache for agents
##
## ===================================================================
## -

import os
import shutil
import maya.cmds as cmds
import maya.mel as mel
import McdPlacementFunctions

def McdCreateAlembicCache():
    
    # clear exist contents;
    # read export path name from MGlobal
    # read export file name from MGlobal
    # check availablity
    # create extra path
    # execute
    
    allAgents = cmds.ls(type = "McdAgent")
    if allAgents == [] or allAgents == None:
        cmds.confirmDialog(t = "Error", m = 'Please Place your agents firstly.')
        return
    
    try:
        globalNode = mel.eval("McdSimpleCommand -exe 2;")
        if globalNode == "_NULL_":
            raise
    except:
        cmds.confirmDialog(t = "Error", m = "Cannot find Miarmy Global Node, please create it in Miarmy > Miarmy Ready")
        return;
    
    outputPath = cmds.getAttr(globalNode + ".outABCFolder")
    outputName = cmds.getAttr(globalNode + ".outABCName")
    
    # check availablity
    if outputPath == None:
        cmds.confirmDialog(t = "Error", m = "Cannot write alembic cache to disk, specify right path in: \nMiarmy > Render Global > Other Renders Tab")
        return;
    if not os.access(outputPath, os.W_OK):
        cmds.confirmDialog(t = "Error", m = "Cannot write alembic cache to disk, specify right path in: \nMiarmy > Render Global > Other Renders Tab")
        return;    
 
    minFrame = cmds.playbackOptions(q = True, min = True)
    maxFrame = cmds.playbackOptions(q = True, max = True)
    nbFrame = int(maxFrame - minFrame + 1)
    
    stat = cmds.confirmDialog(t = "Note", m = "Export Alembic Cache from " + str(minFrame) + " to " + str(maxFrame) + "\n" + \
                                     "We recommend you save your sence before exporting, continue?", b = ["Proceed", "Cancel"])
    
    if stat == "Cancel":
        return;


    # execute
    # refer: McdRenderExportCmd -r 5 -fp "d:/abc" -fn "ffff";
    melCmd = 'McdRenderExportCmd -r 5 -filePath "' + outputPath + '" -fileName "' + outputName + '"'
    mel.eval(melCmd)


def McdImportAlembicCache():
    
    # clear exist contents;
    # read export path name from MGlobal
    # read export file name from MGlobal
    # check availablity
    # create extra path
    # execute
    
    allAgents = cmds.ls(type = "McdAgent")
    if allAgents != [] and allAgents != None:
        stat = cmds.confirmDialog(t = "Question", m = 'Do you want to de-place your agent before importing Alembic Cache?', \
                                b = ["Delete", "Don't delete"])
        if stat == "Delete":
            McdPlacementFunctions.dePlacementAgent()
            
    try:
        globalNode = mel.eval("McdSimpleCommand -exe 2;")
        if globalNode == "_NULL_":
            raise
    except:
        cmds.confirmDialog(t = "Error", m = "Cannot find Miarmy Global Node, please create it in Miarmy > Miarmy Ready")
        return;
    
    outputPath = cmds.getAttr(globalNode + ".outABCFolder")
    outputName = cmds.getAttr(globalNode + ".outABCName")
    
    # check availablity
    if outputPath == None:
        cmds.confirmDialog(t = "Error", m = "Cannot write alembic cache to disk, specify right path in: \nMiarmy > Render Global > Other Renders Tab")
        return;
    if not os.access(outputPath, os.W_OK):
        cmds.confirmDialog(t = "Error", m = "Cannot write alembic cache to disk, specify right path in: \nMiarmy > Render Global > Other Renders Tab")
        return;
    
    allFiles = os.listdir(outputPath)
    if allFiles == [] or allFiles == None:
        cmds.confirmDialog(t = "Abort", m = "No cache file found.")
        return;
        
    allCacheFiles = []
    for i in range(len(allFiles)):
        if allFiles[i].find(outputName) == 0:
            if allFiles[i][-3] == "a":
                allCacheFiles.append(allFiles[i])
                
    if allCacheFiles == []:
        cmds.confirmDialog(t = "Abort", m = "No cache file found.")
        return;
        
    
    stat = cmds.confirmDialog(t = "Note", m = "Ready to import Alembic Cache... \n" + \
                                        "Total: ( " + str(len(allCacheFiles)) + " ) alembic files\n" + \
                                        "We recommend you save your sence before exporting, continue?", b = ["Proceed", "Cancel"])
    
    if stat == "Proceed":
        # refer: AbcImport -mode import "D:/abc/ffff.2.abc";
        for i in range(len(allCacheFiles)):
            melCmd = 'AbcImport -mode import "' + outputPath + '/' + allCacheFiles[i] + '"'
            try:
                mel.eval(melCmd)
            except:
                pass




























