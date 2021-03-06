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

import maya.cmds as cmds
from McdGeneral import *
from McdActionProxyEditorGUI import *

def McdActionProxyGetNodeNameFromGUI():
    actionProxyName = cmds.textField("ActionProxyNodeName", q = True, tx = True)
    return actionProxyName

def setupOmActionProxy(index):
    allActions = cmds.ls(type = "McdAction")
    typeActions = []
    if allActions != [] and allActions != None:
        for i in range(len(allActions)):
            isAct = McdCheckNodeActiveCmd(allActions[i])
            if isAct == True:
                typeActions.append(allActions[i])
    
    if typeActions != []:
        for i in range(len(typeActions)):
            actionName = typeActions[i].split("_action_")[0]
            cmds.menuItem(l = actionName)

def cb_apx_active(index):
    apxNode = McdActionProxyGetNodeNameFromGUI()
    cmds.setAttr(apxNode + ".active[" + str(index) + "]", True)
    McdActionProxyEditorGUI()

def cb_apx_deActive(index):
    apxNode = McdActionProxyGetNodeNameFromGUI()
    cmds.setAttr(apxNode + ".active[" + str(index) + "]", False)
    McdActionProxyEditorGUI()

def btn_apx_set(index):
    stri = str(index)
    apxNode = McdActionProxyGetNodeNameFromGUI()
    tex = cmds.optionMenu("om_apx_actName" + stri, q = True, v = True)
    cmds.setAttr(apxNode + ".playList[" + stri + "]", tex, type = "string")
    cmds.textField("tf_apx_actionName" + stri, e = True, tx = tex)
    
def tn_apx_pyls(index):
    stri = str(index)
    apxNode = McdActionProxyGetNodeNameFromGUI()
    tex = cmds.textField("tf_apx_actionName" + stri, q = True, tx = True)
    cmds.setAttr(apxNode + ".playList[" + stri + "]", tex, type = "string")
    McdActionProxyEditorGUI()

def dcc_addProxy(proxyNode):
    choiceText = cmds.textScrollList("tsl_actprxy", q = True, si = True)[0]
    print choiceText
    print proxyNode
    
    # find action proxy node
    # enable late check and fill string
    
    cmds.select(proxyNode)

def bnt_apx_checkAct():
    allActions = cmds.ls(type = "McdAction")
    typeActions = []
    typeNamesOfAction = [];
    if allActions != [] and allActions != None:
        for i in range(len(allActions)):
            isAct = McdCheckNodeActiveCmd(allActions[i])
            if isAct == True:
                typeActions.append(allActions[i])
    
    if typeActions != []:
        for i in range(len(typeActions)):
            actionName = typeActions[i].split("_action_")[0]
            typeNamesOfAction.append(actionName)
    
    apxNode = McdActionProxyGetNodeNameFromGUI()
    for i in range(50):
        stri = str(i)
        isActive = cmds.getAttr(apxNode + ".active[" + stri + "]")
        if isActive == 1:
            playAction = cmds.getAttr(apxNode + ".playList[" + stri + "]")
            if playAction not in typeNamesOfAction:
                cmds.setAttr(apxNode + ".playList[" + stri + "]", "", type = "string")
                cmds.textField("tf_apx_actionName" + stri, e = True, tx = "")
        else:
            break;


































    