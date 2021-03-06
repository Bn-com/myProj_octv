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
##  Module Name: McdActionSyncInfo
##
##  Description:
##    Miarmy Global
##
## ===================================================================
## -


import maya.cmds as cmds
import maya.mel as mel
from McdGeneral import *
from McdMiarmyGlobal import *
from McdActionSyncEditorGUI import *

def queryActionSyncInfo():
    queryData = []
    
    # find all actions
    allActions = cmds.ls(type = "McdAction")
    if MIsBlank(allActions):
        return queryData
        
    # for each, list connections
    for i in range(len(allActions)):
        # find connect in:
        allConns = cmds.listConnections(allActions[i], d = True, s = False)
        if MIsBlank(allConns):
            continue
        for j in range(len(allConns)):
            queryData.append(allActions[i]);
            queryData.append(allConns[j])
    
    return queryData

def clearActionSyncRec(idx):
    stri = str(idx)
    subAct = cmds.text("actSub" + stri, q = True, l = True)
    objAct = cmds.text("actObj" + stri, q = True, l = True)
    
    allConns = cmds.listConnections(subAct, d = True, s = False, p = True)
    for i in range(len(allConns)):
        if allConns[i].find(objAct + ".") >= 0:
            cmds.disconnectAttr(subAct + ".syncTo", allConns[i])
            
    McdActionSyncEditorGUI()

def clearAllActionSyncLinks():
    # find all actions
    allActions = cmds.ls(type = "McdAction")
    if MIsBlank(allActions):
        return queryData
    
    for j in range(len(allActions)):
        allConns = cmds.listConnections(allActions[j], d = True, s = False, p = True)
        if not MIsBlank(allConns):
            for i in range(len(allConns)):
                cmds.disconnectAttr(allActions[j] + ".syncTo", allConns[i])
    
    McdActionSyncEditorGUI()

def establishActionSyncLink():
    # check 2 selectins
    selObjs = cmds.ls(sl = True)
    if MIsBlank(selObjs):
        cmds.confirmDialog(t = "Error", m = "Please select one subjective action, and then another one objective action.")
        return
    
    if len(selObjs) != 2:
        cmds.confirmDialog(t = "Error", m = "Please select one subjective action, and then another one objective action.")
        return
    
    if cmds.nodeType(selObjs[0]) != "McdAction":
        cmds.confirmDialog(t = "Error", m = "Please select one subjective action, and then another one objective action.")
        return
    
    if cmds.nodeType(selObjs[1]) != "McdAction":
        cmds.confirmDialog(t = "Error", m = "Please select one subjective action, and then another one objective action.")
        return
    
    # link it super connect
    mel.eval("McdSimpleCommand -execute 34;")
    
    McdActionSyncEditorGUI()



















