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
##  Module Name: McdDecisionEditorGUI.py
##
##  Description:
##    Deal with details of McdDecisionNode.
##
## ===================================================================
## -

import maya.cmds as cmds
from McdGeneral import *
from McdDecisionEditorGUI import *
from McdSentencePresetListGUI import *
from McdDecisionPresetListGUI import *

def getIdString(i):
    if i == 0:
        return "A"
    elif i == 1:
        return "B"
    elif i == 2:
        return "C"
    elif i == 3:
        return "D"
    elif i == 4:
        return "E"
    elif i == 5:
        return "F"
    elif i == 6:
        return "G"
    elif i == 7:
        return "H"
    elif i == 8:
        return "I"
    elif i == 9:
        return "J"
    elif i == 10:
        return "K"
    elif i == 11:
        return "L"
    elif i == 12:
        return "M"
    elif i == 13:
        return "N"
    elif i == 14:
        return "O"
    elif i == 15:
        return "P"
    elif i == 16:
        return "Q"
    elif i == 17:
        return "R"
    elif i == 18:
        return "S"
    elif i == 19:
        return "T"
    elif i == 20:
        return "U"
    elif i == 21:
        return "V"
    elif i == 22:
        return "W"
    elif i == 23:
        return "X"
    elif i == 24:
        return "Y"
    elif i == 25:
        return "Z"
    
def McdDecisionGetNodeNameFromGUI():
    decisionNode = ""
    decisionName = cmds.textField("DecisionNodeName", q = True, tx = True)
    if isReferenceScene():
        decisionNode = decisionName
    else:
        activeAgent = McdGetActiveAgentName()
        decisionNode = decisionName + "_decision_" + activeAgent;
    return decisionNode

def switchDecisionMode():
    dsnNode = McdDecisionGetNodeNameFromGUI()
    if cmds.getAttr(dsnNode + ".absMode") == 1:
        cmds.setAttr(dsnNode + ".absMode", 0)
    else:
        cmds.setAttr(dsnNode + ".absMode", 1)
    McdRefreshDecisionEditor()

# active and de-active:
def cb_dn_active(index):
    dsnNode = McdDecisionGetNodeNameFromGUI()
    cmds.setAttr(dsnNode + ".active[" + str(index) + "]", True)
    McdRefreshDecisionEditor()
def cb_dn_deActive(index):
    dsnNode = McdDecisionGetNodeNameFromGUI()
    cmds.setAttr(dsnNode + ".active[" + str(index) + "]", False)
    McdRefreshDecisionEditor()
  
def cb_dno_active(index):
    dsnNode = McdDecisionGetNodeNameFromGUI()
    cmds.setAttr(dsnNode + ".outputActive[" + str(index) + "]", True)
    McdRefreshDecisionEditor()
def cb_dno_deActive(index):
    dsnNode = McdDecisionGetNodeNameFromGUI()
    cmds.setAttr(dsnNode + ".outputActive[" + str(index) + "]", False)
    McdRefreshDecisionEditor()
    
    
# priority
def in_dn_prio(index):
    dsnNode = McdDecisionGetNodeNameFromGUI()
    value = cmds.intField("if_dn_priority" + str(index), q = True, v = True)
    cmds.setAttr(dsnNode + ".priority[" + str(index) + "]", value)
    upDataParseDecisionString()
    
#logic
def om_dn_logic(index):
    # 0: and &&
    # 1: or  ||
    value = cmds.optionMenu("if_dn_logic" + str(index), q = True, v = True)
    dLogic = 0
    newValue = "&&"
    if value == "||":
        dLogic = 1
        newValue = "||"
    elif value == "xor":
        dLogic = 2
        newValue = "xor"
    dsnNode = McdDecisionGetNodeNameFromGUI()
    cmds.setAttr(dsnNode + ".logic[" + str(index) + "]", dLogic)
    cmds.optionMenu("if_dn_logic" + str(index), e = True, v = newValue)
    upDataParseDecisionString()
        
def setupOmDecisionLogic(dLogic, stri):
    cmds.menuItem(label = "&&")
    cmds.menuItem(label = "||")
    cmds.menuItem(label = "xor")
    # 0: and &&
    # 1: or  ||
    valueL = "&&"
    if dLogic == 1:
        valueL = "||"
    elif dLogic == 2:
        valueL = "xor"
    cmds.optionMenu("if_dn_logic" + stri, e = True, v = valueL)

#input type:
def om_dn_inTyp(index):
    # 0: and &&
    # 1: or  ||
    value = cmds.optionMenu("if_dn_inTyp" + str(index), q = True, v = True)
    dInTyp = 0
    newValue = "max"
    if value == "average":
        dInTyp = 1
        newValue = "average"
    dsnNode = McdDecisionGetNodeNameFromGUI()
    cmds.setAttr(dsnNode + ".inputType[" + str(index) + "]", dInTyp)
    cmds.optionMenu("if_dn_inTyp" + str(index), e = True, v = newValue)
    upDataParseDecisionString()

def setupOmDecisionInTyp(dInTyp, stri):
    cmds.menuItem(label = "max")
    cmds.menuItem(label = "average")
    # 0: max
    # 1: average
    valueL = "max"
    if dInTyp == 1:
        valueL = "average"
    cmds.optionMenu("if_dn_inTyp" + stri, e = True, v = valueL)

#false
        
def cb_dns_False_on(index):
    dsnNode = McdDecisionGetNodeNameFromGUI()
    cmds.checkBox("cd_dn_false" + str(index), e = True, v = 1)
    cmds.setAttr(dsnNode + ".not[" + str(index) + "]", 1)
    newText = "not " + getIdString(index) + " "
    cmds.text("t_dn_id" + str(index), e = True, l = newText)
    upDataParseDecisionString()
    
    
def cb_dns_False_off(index):
    dsnNode = McdDecisionGetNodeNameFromGUI()
    cmds.checkBox("cd_dn_false" + str(index), e = True, v = 0)
    cmds.setAttr(dsnNode + ".not[" + str(index) + "]", 0)
    newText = getIdString(index) + " "
    cmds.text("t_dn_id" + str(index), e = True, l = newText)
    upDataParseDecisionString()
    
def cb_dns_infMin_on(index):
    dsnNode = McdDecisionGetNodeNameFromGUI()
    cmds.checkBox("cd_dn_infMin" + str(index), e = True, v = 1)
    cmds.setAttr(dsnNode + ".inputInfinityMin[" + str(index) + "]", 1)
    McdRefreshDecisionEditor()

def cb_dns_infMin_off(index):
    dsnNode = McdDecisionGetNodeNameFromGUI()
    cmds.checkBox("cd_dn_infMin" + str(index), e = True, v = 0)
    cmds.setAttr(dsnNode + ".inputInfinityMin[" + str(index) + "]", 0)
    McdRefreshDecisionEditor()
    
def cb_dns_infMax_on(index):
    dsnNode = McdDecisionGetNodeNameFromGUI()
    cmds.checkBox("cd_dn_infMax" + str(index), e = True, v = 1)
    cmds.setAttr(dsnNode + ".inputInfinityMax[" + str(index) + "]", 1)
    McdRefreshDecisionEditor()
    
def cb_dns_infMax_off(index):
    dsnNode = McdDecisionGetNodeNameFromGUI()
    cmds.checkBox("cd_dn_infMax" + str(index), e = True, v = 0)
    cmds.setAttr(dsnNode + ".inputInfinityMax[" + str(index) + "]", 0)
    McdRefreshDecisionEditor()

    
# input
def tf_dns_inputCC(index):
    dsnNode = McdDecisionGetNodeNameFromGUI()
    value = cmds.textField("if_dn_input" + str(index), q = True, tx = True)
    valueWithoutBlank = removeBlank(value)
    cmds.setAttr(dsnNode + ".input[" + str(index) + "]", valueWithoutBlank, type = "string")
    
    
# value min
def ff_inputVMinCC(index):
    dsnNode = McdDecisionGetNodeNameFromGUI()
    value = cmds.floatField("if_dn_min" + str(index), q = True, v = True)
    cmds.setAttr(dsnNode + ".inputValueMin[" + str(index) + "]", value)
    updatePSRNodeDataWrapper(index, dsnNode)
    
# value max
def ff_inputVMaxCC(index):
    dsnNode = McdDecisionGetNodeNameFromGUI()
    value = cmds.floatField("if_dn_max" + str(index), q = True, v = True)
    cmds.setAttr(dsnNode + ".inputValueMax[" + str(index) + "]", value)
    updatePSRNodeDataWrapper(index, dsnNode)
    
# fuzzy low bound:
def ff_inputFVMinCC(index):
    dsnNode = McdDecisionGetNodeNameFromGUI()
    value = cmds.floatField("if_dn_fzmin" + str(index), q = True, v = True)
    cmds.setAttr(dsnNode + ".fuzzyIn[" + str(index) + "]", value)
    updatePSRNodeDataWrapper(index, dsnNode)
    
def ff_inputFVMinCC2(index):
    dsnNode = McdDecisionGetNodeNameFromGUI()
    value = cmds.floatField("if_dn_fzmin" + str(index), q = True, v = True)
    cmds.setAttr(dsnNode + ".fuzzyIn[" + str(index) + "]", value)
    
    cmds.floatField("if_dn_fzmax" + str(index), e = True, v = value)
    cmds.setAttr(dsnNode + ".fuzzyOut[" + str(index) + "]", value)
    updatePSRNodeDataWrapper(index, dsnNode)
    
def ff_inputFVMaxCC(index):
    dsnNode = McdDecisionGetNodeNameFromGUI()
    value = cmds.floatField("if_dn_fzmax" + str(index), q = True, v = True)
    cmds.setAttr(dsnNode + ".fuzzyOut[" + str(index) + "]", value)
    updatePSRNodeDataWrapper(index, dsnNode)
    
#---------------------------------------------------------------------
# output
def tf_dn_outCC(index):
    dsnNode = McdDecisionGetNodeNameFromGUI()
    value = cmds.textField("tf_dn_out" + str(index), q = True, tx = True)
    valueWithoutBlank = removeBlank(value)
    #if cmds.getAttr(dsnNode + ".default") == 1:
    #    if (value.find("dynamics.active")>=0):
    #        cmds.confirmDialog(t = "Warning", m = "Please do not fill dynamic active channel in default decision.\nAuto erase for you.")
    #        cmds.textField("tf_dn_out" + str(index), e = True, tx = "")
    #        cmds.setAttr(dsnNode + ".output[" + str(index) + "]", "", type = "string")
    #        return;
    
    cmds.setAttr(dsnNode + ".output[" + str(index) + "]", valueWithoutBlank, type = "string")
    
def ff_dn_ovCC(index):
    dsnNode = McdDecisionGetNodeNameFromGUI()
    value = cmds.floatField("ff_dn_ov" + str(index), q = True, v = True)
    cmds.setAttr(dsnNode + ".outputValue[" + str(index) + "]", value)

def ff_dn_esCC(index):
    dsnNode = McdDecisionGetNodeNameFromGUI()
    value = cmds.floatField("ff_dn_else" + str(index), q = True, v = True)
    cmds.setAttr(dsnNode + ".outputElse[" + str(index) + "]", value)
    
def om_dn_outFilter(index):
    dsnNode = McdDecisionGetNodeNameFromGUI()
    value = cmds.intField("ff_dn_frt" + str(index), q = True, v = True)
    cmds.setAttr(dsnNode + ".outputFilter[" + str(index) + "]", value)


# output type
def setupOmDecisionOutType(dType, stri):
    cmds.menuItem(label = "Value")
    cmds.menuItem(label = "Change Rate")
    # 0: value
    # 1: change rate
    valueL = "Value"
    if dType == 1:
        valueL = "Change Rate"
    cmds.optionMenu("om_dn_otype" + stri, e = True, v = valueL)
    
def om_dn_outType(index):
    # 0: value
    # 1: change rate
    value = cmds.optionMenu("om_dn_otype" + str(index), q = True, v = True)
    dType = 0
    newValue = "Value"
    if value == "Change Rate":
        dType = 1
        newValue = "Change Rate"
    dsnNode = McdDecisionGetNodeNameFromGUI()
    cmds.setAttr(dsnNode + ".outputType[" + str(index) + "]", dType)
    cmds.optionMenu("om_dn_otype" + str(index), e = True, v = newValue)
    
    
def setupOmDecisionDfzType(dType, stri):
    cmds.menuItem(label = "Average")
    cmds.menuItem(label = "Max")
    cmds.menuItem(label = "Blend")
    # 0: value
    # 1: change rate
    valueL = "Average"
    if dType == 1:
        valueL = "Max"
    elif dType == 2:
        valueL = "Blend"
    cmds.optionMenu("om_dn_dfztype" + stri, e = True, v = valueL)
    
def om_dn_dfzType(index):
    # 0: value
    # 1: change rate
    value = cmds.optionMenu("om_dn_dfztype" + str(index), q = True, v = True)
    dType = 0
    newValue = "Average"
    if value == "Max":
        dType = 1
        newValue = "Max"
    elif value == "Blend":
        dType = 2
        newValue = "Blend"
    dsnNode = McdDecisionGetNodeNameFromGUI()
    cmds.setAttr(dsnNode + ".defuzzType[" + str(index) + "]", dType)
    cmds.optionMenu("om_dn_dfztype" + str(index), e = True, v = newValue)
    
    
def upDataParseDecisionString():
    inputResult = mel.eval("McdParseDecisionCmd;")
    cmds.textField("parseResult", e = True, tx = inputResult)
    
    
def decisionNotesChange(dcNode):
    try:
        dNotes = cmds.textField("DecisionComments", q = True, tx = True)
        cmds.setAttr(dcNode + ".comment", dNotes, type = "string")
    except:
        try:
            cmds.addAttr(dcNode, ln = "comment", dt = "string")
            dNotes = cmds.textField("DecisionComments", q = True, tx = True)
            cmds.setAttr(dcNode + ".comment", dNotes, type = "string")
        except:
            pass
        
        
def moveUpSentence(index, dcNode, isUpdate = 0):
    #priority, logic, not, input, inputValueMin, inputValueMax, fuzzyIn, fuzzyOut
    indexUp = index - 1
    stri = str(index)
    striUp = str(indexUp)
    
    # fetch current
    dPriority = cmds.getAttr(dcNode + ".priority[" +stri+ "]")
    dLogic = cmds.getAttr(dcNode + ".logic[" +stri+ "]")
    dNot = cmds.getAttr(dcNode + ".not[" +stri+ "]")
    dInput = cmds.getAttr(dcNode + ".input[" +stri+ "]")
    dMin = cmds.getAttr(dcNode + ".inputValueMin[" +stri+ "]")
    dMinInf = cmds.getAttr(dcNode + ".inputInfinityMin[" + stri + "]")
    dMax = cmds.getAttr(dcNode + ".inputValueMax[" +stri+ "]")
    dMaxInf = cmds.getAttr(dcNode + ".inputInfinityMax[" + stri + "]")
    dFuzzyIn = cmds.getAttr(dcNode + ".fuzzyIn[" +stri+ "]")
    dFuzzyOut = cmds.getAttr(dcNode + ".fuzzyOut[" +stri+ "]")
    dInputType = cmds.getAttr(dcNode + ".inputType[" +stri+ "]")
    
    # fetch up
    dPriorityUp = cmds.getAttr(dcNode + ".priority[" +striUp+ "]")
    dLogicUp = cmds.getAttr(dcNode + ".logic[" +striUp+ "]")
    dNotUp = cmds.getAttr(dcNode + ".not[" +striUp+ "]")
    dInputUp = cmds.getAttr(dcNode + ".input[" +striUp+ "]")
    dMinUp = cmds.getAttr(dcNode + ".inputValueMin[" +striUp+ "]")
    dMinInfUp = cmds.getAttr(dcNode + ".inputInfinityMin[" + striUp + "]")
    dMaxUp = cmds.getAttr(dcNode + ".inputValueMax[" +striUp+ "]")
    dMaxInfUp = cmds.getAttr(dcNode + ".inputInfinityMax[" + striUp + "]")
    dFuzzyInUp = cmds.getAttr(dcNode + ".fuzzyIn[" +striUp+ "]")
    dFuzzyOutUp = cmds.getAttr(dcNode + ".fuzzyOut[" +striUp+ "]")
    dInputTypeUp = cmds.getAttr(dcNode + ".inputType[" +striUp+ "]")
    
    # set up: current!
    cmds.setAttr(dcNode + ".priority[" +stri+ "]", dPriorityUp)
    cmds.setAttr(dcNode + ".logic[" +stri+ "]", dLogicUp)
    cmds.setAttr(dcNode + ".inTyp[" +stri+ "]", dInputTypeUp)
    cmds.setAttr(dcNode + ".not[" +stri+ "]", dNotUp)
    if dInputUp == None:
        cmds.setAttr(dcNode + ".input[" +stri+ "]", "" , type = "string")
    else:
        cmds.setAttr(dcNode + ".input[" +stri+ "]", dInputUp , type = "string")
    cmds.setAttr(dcNode + ".inputValueMin[" +stri+ "]", dMinUp)
    cmds.setAttr(dcNode + ".inputValueMax[" +stri+ "]", dMaxUp)
    cmds.setAttr(dcNode + ".inputInfinityMin[" +stri+ "]", dMinInfUp)
    cmds.setAttr(dcNode + ".inputInfinityMax[" +stri+ "]", dMaxInfUp)
    cmds.setAttr(dcNode + ".fuzzyIn[" +stri+ "]", dFuzzyInUp)
    cmds.setAttr(dcNode + ".fuzzyOut[" +stri+ "]", dFuzzyOutUp)
    
    # set up: up!
    cmds.setAttr(dcNode + ".priority[" +striUp+ "]", dPriority)
    cmds.setAttr(dcNode + ".logic[" +striUp+ "]", dLogic)
    cmds.setAttr(dcNode + ".inTyp[" +striUp+ "]", dInputType)
    cmds.setAttr(dcNode + ".not[" +striUp+ "]", dNot)
    if dInput == None:
        cmds.setAttr(dcNode + ".input[" +striUp+ "]", "", type = "string")
    else:
        cmds.setAttr(dcNode + ".input[" +striUp+ "]", dInput, type = "string")
    cmds.setAttr(dcNode + ".inputValueMin[" +striUp+ "]", dMin)
    cmds.setAttr(dcNode + ".inputValueMax[" +striUp+ "]", dMax)
    cmds.setAttr(dcNode + ".inputInfinityMin[" +striUp+ "]", dMinInf)
    cmds.setAttr(dcNode + ".inputInfinityMax[" +striUp+ "]", dMaxInf)
    cmds.setAttr(dcNode + ".fuzzyIn[" +striUp+ "]", dFuzzyIn)
    cmds.setAttr(dcNode + ".fuzzyOut[" +striUp+ "]", dFuzzyOut)

    # check connection
    allConns = cmds.listConnections(dcNode + ".active["+ stri +"]", d = True, s = False)
    psrNode = ""
    if MIsBlank(allConns):
        # if not create and connect
        psrNode = cmds.createNode("polySplitRing", ss = True)
        cmds.connectAttr(dcNode + ".active["+ stri +"]", psrNode + ".worldSpace")
    else:
        psrNode = allConns[0]
        
    allConns = cmds.listConnections(dcNode + ".active["+ striUp +"]", d = True, s = False)
    psrNodeUp = ""
    if MIsBlank(allConns):
        # if not create and connect
        psrNodeUp = cmds.createNode("polySplitRing", ss = True)
        cmds.connectAttr(dcNode + ".active["+ striUp +"]", psrNodeUp + ".worldSpace")
    else:
        psrNodeUp = allConns[0]
        
    cmds.disconnectAttr(dcNode + ".active["+ stri +"]", psrNode + ".worldSpace")
    cmds.disconnectAttr(dcNode + ".active["+ striUp +"]", psrNodeUp + ".worldSpace")
    cmds.connectAttr(dcNode + ".active["+ stri +"]", psrNodeUp + ".worldSpace")
    cmds.connectAttr(dcNode + ".active["+ striUp +"]", psrNode + ".worldSpace")
    
    
    if isUpdate == 1:
        McdRefreshDecisionEditor()


def deleteSentence(index, dcNode):
    stat = cmds.confirmDialog(t = "Note", m = "Are your sure to delete this sentence?", b = ["Delete", "Cancel"])
    if stat == "Delete":
        # if next available, move next sentence up
        dActive = cmds.getAttr(dcNode + ".active[" +str(index+1)+ "]")
        escape = 50;
        while(dActive == 1 and escape > 0):
            # move up:
            moveUpSentence(index+1, dcNode)
            index += 1;
            dActive = cmds.getAttr(dcNode + ".active[" +str(index+1)+ "]")
            escape -= 1;
        
        #deactivate index
        cmds.setAttr(dcNode + ".active[" +str(index)+ "]", 0)
        McdRefreshDecisionEditor()
    
def MakeDecisionNonDefault(dcNode):
    globalNode = McdGetMcdGlobalNode()
    allDcNodes = cmds.ls(type = "McdDecision", l = True)
    allActiveNodes = []
    for i in range(len(allDcNodes)):
        cmds.setAttr(globalNode + ".nextAgentType", allDcNodes[i], type = "string")
        isAct = mel.eval("McdCheckNodeActiveCmd;")
        if isAct == 1:
            allActiveNodes.append(allDcNodes[i])
    
    for i in range(len(allActiveNodes)):
        cmds.setAttr(allActiveNodes[i] + ".default", 0)
        
    cmds.select(dcNode)
        
    
def MakeDecisionDefault(dcNode):
    globalNode = McdGetMcdGlobalNode()
    allDcNodes = cmds.ls(type = "McdDecision", long = True)
    allActiveNodes = []
    for i in range(len(allDcNodes)):
        cmds.setAttr(globalNode + ".nextAgentType", allDcNodes[i], type = "string")
        isAct = mel.eval("McdCheckNodeActiveCmd;")
        if isAct == 1:
            allActiveNodes.append(allDcNodes[i])
    
    for i in range(len(allActiveNodes)):
        cmds.setAttr(allActiveNodes[i] + ".default", 0)
        
    cmds.setAttr(dcNode + ".default", 1)
    
    #dynIndexList = []
    #counter = 0;
    #while (cmds.getAttr(dcNode + ".outAtv[" + str(counter) + "]") == 1):
    #    outVal = cmds.getAttr(dcNode + ".output[" + str(counter) + "]")
    #    if outVal != None:        
    #        if outVal.find("dynamics.active")>=0:
    #            dynIndexList.append(counter)
    #    counter += 1;
    #    
    #if dynIndexList != []:
    #    cmds.confirmDialog(t = "Warning", m = "Please do not fill dynamic active channel in default decision.\nAuto erase for you.")
    #    
    #    for i in range(len(dynIndexList)):
    #        cmds.setAttr(dcNode + ".output[" + str(dynIndexList[i]) + "]", "", type = "string")
    
    cmds.select(dcNode)
    
def editDefaultAction(dcNode):
    newDefaultActionName = cmds.textField("TF_defaultAction", q = True, tx = True)
    cmds.setAttr( dcNode + ".defaultAction", newDefaultActionName, type = "string")


def autoFillSentence(i, dcNode):
    McdSentencePresetListGUI(i, dcNode)

def autoFillDecision(i, dcNode):
    McdDecisionPresetListGUI(i, dcNode)

def checkAndGetPolySplitRing(i, dcNode):
    stri = str(i)
    # check connection
    allConns = cmds.listConnections(dcNode + ".active["+ stri +"]", d = True, s = False)
    psrNode = ""
    if MIsBlank(allConns):
        # if not create and connect
        psrNode = cmds.createNode("polySplitRing", ss = True)
        cmds.connectAttr(dcNode + ".active["+ stri +"]", psrNode + ".worldSpace")
    else:
        psrNode = allConns[0]

            
    return psrNode


def updatePSRNodeData(i, dcNode, dInfMin, dInfMax, dMin, dMax, dFuzzyIn, dFuzzyOut, psrNode):
    stri = str(i)
    floatFieldData = []
    floatFieldData.append(0.0)
    floatFieldData.append(0.0)
    floatFieldData.append(0.0)
    floatFieldData.append(0.0)
    
    if dFuzzyIn < 0.01:
        dFuzzyIn = 0.001
    if dFuzzyOut < 0.01:
        dFuzzyOut = 0.001
    
    
    isAbsMode = False
    try:
        if cmds.getAttr(dcNode + ".absMode") == 1:
            isAbsMode = True
    except:
        pass
    
    if isAbsMode:
        # re order the values:
        dMin = (dMin + (dMin - dFuzzyIn)) * 0.5
        dMax = (dMax + (dMax + dFuzzyOut)) * 0.5
        dFuzzyIn *= 0.5
        dFuzzyOut *= 0.5
    
    
    if psrNode == "None":
        # check connection
        allConns = cmds.listConnections(dcNode + ".active["+ stri +"]", d = True, s = False)
        psrNode = ""
        if MIsBlank(allConns):
            # if not create and connect
            psrNode = cmds.createNode("polySplitRing", ss = True)
            cmds.connectAttr(dcNode + ".active["+ stri +"]", psrNode + ".worldSpace")
                
        else:
            psrNode = allConns[0]
            
    # solve bounding:
    boundMin = 0.0
    boundMax = 0.0
    
    bothRange = False
    middleValue = 0
    
    if dInfMin == 1 and dInfMax == 0:
        boundMax = dMax + dFuzzyOut
        boundMin = dMax - dFuzzyOut
    elif dInfMin == 0 and dInfMax == 1:
        boundMin = dMin - dFuzzyIn
        boundMax = dMin + dFuzzyIn
    else:
        if dMin > dMax:
            dTemp = dMin
            dMin = dMax
            dMax = dTemp
            dTemp = dFuzzyIn
            dFuzzyIn = dFuzzyOut
            dFuzzyOut = dTemp
            
        bothRange = True
        
        part1 = dMin + dFuzzyIn
        part2 = dMax - dFuzzyOut
        if part1 > dMax:
            part1 = dMax
        if part2 < dMin:
            part2 = dMin
            
        middleValue = (part1 + part2) * 0.5
            
        boundMin = dMin - dFuzzyIn
        boundMax = dMax + dFuzzyOut
        
        
    totalBoundOrg = boundMax - boundMin
    
    absMin = abs(dMin)
    absMax = abs(dMax)
    if absMin == absMax:
        decr = 5 + totalBoundOrg * 0.2
        incr = 5 + totalBoundOrg * 0.2
    elif absMin > absMax:
        decr = 5 + totalBoundOrg * 0.4
        incr = 5 + totalBoundOrg * 0.1
    else:
        decr = 5 + totalBoundOrg * 0.1
        incr = 5 + totalBoundOrg * 0.4
        
    boundMin -= decr
    boundMax += incr
            
    totalBound = boundMax - boundMin
    
    # if init, ignore it!
    if abs(dMin) < 0.01 and abs(dMax) < 0.01 and abs(dFuzzyIn) < 0.01 and abs(dFuzzyOut) < 0.01:
        return floatFieldData
    
    if totalBound > 0.01:
        pos1 = (dMin - dFuzzyIn - boundMin) / totalBound
        pos2 = (dMin + dFuzzyIn - boundMin) / totalBound
        pos3 = (dMax - dFuzzyOut - boundMin) / totalBound
        pos4 = (dMax + dFuzzyOut - boundMin) / totalBound
        val1 = dMin - dFuzzyIn
        val2 = dMin + dFuzzyIn
        val3 = dMax - dFuzzyOut
        val4 = dMax + dFuzzyOut
        
        
        if bothRange:
            middleValueOrg = middleValue
            middleValue -= boundMin
            middleLimit = middleValue / totalBound
            if pos2 > middleLimit:
                pos2 = middleLimit
                val2 = middleValueOrg
            if pos3 < middleLimit:
                pos3 = middleLimit
                val3 = middleValueOrg
        
        floatFieldData[0] = val1
        floatFieldData[1] = val2
        floatFieldData[2] = val3
        floatFieldData[3] = val4
        

        try:
            cmds.floatField("gfpos1" + stri, e = True, v = val1) # graphic
            cmds.floatField("gfpos2" + stri, e = True, v = val2) # graphic
        except:
            pass
        try:
            cmds.floatField("gfpos3" + stri, e = True, v = val3) # graphic
            cmds.floatField("gfpos4" + stri, e = True, v = val4) # graphic
        except:
            pass
        
        if dInfMin == 1:
            cmds.setAttr( psrNode + ".profileCurve[0].profileCurve_Interp", 1)
            cmds.setAttr( psrNode + ".profileCurve[0].profileCurve_Position", 0)
            cmds.setAttr( psrNode + ".profileCurve[0].profileCurve_FloatValue", 1.0)
    
            cmds.setAttr( psrNode + ".profileCurve[1].profileCurve_Interp", 1)
            cmds.setAttr( psrNode + ".profileCurve[1].profileCurve_Position", 0.03)
            cmds.setAttr( psrNode + ".profileCurve[1].profileCurve_FloatValue", 1.0)
        else:
            cmds.setAttr( psrNode + ".profileCurve[0].profileCurve_Interp", 1)
            cmds.setAttr( psrNode + ".profileCurve[0].profileCurve_Position", pos1)
            cmds.setAttr( psrNode + ".profileCurve[0].profileCurve_FloatValue", 0.0)
    
            cmds.setAttr( psrNode + ".profileCurve[1].profileCurve_Interp", 1)
            cmds.setAttr( psrNode + ".profileCurve[1].profileCurve_Position", pos2)
            cmds.setAttr( psrNode + ".profileCurve[1].profileCurve_FloatValue", 1.0)
    
        if dInfMax == 1:
            cmds.setAttr( psrNode + ".profileCurve[2].profileCurve_Interp", 1)
            cmds.setAttr( psrNode + ".profileCurve[2].profileCurve_Position", 0.97)
            cmds.setAttr( psrNode + ".profileCurve[2].profileCurve_FloatValue", 1.0)
    
            cmds.setAttr( psrNode + ".profileCurve[3].profileCurve_Interp", 1)
            cmds.setAttr( psrNode + ".profileCurve[3].profileCurve_Position", 1.0)
            cmds.setAttr( psrNode + ".profileCurve[3].profileCurve_FloatValue", 1.0)
        else:
            cmds.setAttr( psrNode + ".profileCurve[2].profileCurve_Interp", 1)
            cmds.setAttr( psrNode + ".profileCurve[2].profileCurve_Position", pos3)
            cmds.setAttr( psrNode + ".profileCurve[2].profileCurve_FloatValue", 1.0)
    
            cmds.setAttr( psrNode + ".profileCurve[3].profileCurve_Interp", 1)
            cmds.setAttr( psrNode + ".profileCurve[3].profileCurve_Position", pos4)
            cmds.setAttr( psrNode + ".profileCurve[3].profileCurve_FloatValue", 0.0)
            
            
    return floatFieldData


def updatePSRNodeDataWrapper(i, dcNode):
    
    stri = str(i)
    # check connection
    allConns = cmds.listConnections(dcNode + ".active["+ stri +"]", d = True, s = False)
    psrNode = ""
    if MIsBlank(allConns):
        # if not create and connect
        psrNode = cmds.createNode("polySplitRing", ss = True)
        cmds.connectAttr(dcNode + ".active["+ stri +"]", psrNode + ".worldSpace")
    else:
        psrNode = allConns[0]
        
    dMin = cmds.getAttr(dcNode + ".inputValueMin[" +stri+ "]")
    dInfMin = cmds.getAttr(dcNode + ".inputInfinityMin[" +stri+ "]")
    dMax = cmds.getAttr(dcNode + ".inputValueMax[" +stri+ "]")
    dInfMax = cmds.getAttr(dcNode + ".inputInfinityMax[" +stri+ "]")
    dFuzzyIn = cmds.getAttr(dcNode + ".fuzzyIn[" +stri+ "]")
    dFuzzyOut = cmds.getAttr(dcNode + ".fuzzyOut[" +stri+ "]")


    updatePSRNodeData(i, dcNode, dInfMin, dInfMax, dMin, dMax, dFuzzyIn, dFuzzyOut, psrNode)






    