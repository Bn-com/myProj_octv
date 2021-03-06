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
##  Module Name: McdPlacementEditor.py
##
##  Description:
##    Deal with details of McdPlacementEditor.
##
## ===================================================================
## -

import maya.cmds as cmds
import maya.mel as mel
from McdGeneral import *

def FindAndPutAllAgents():
    returnList = []
    placeAgents = None;
    
    miarmyMain = cmds.ls("Miarmy_Contents")
    if miarmyMain == [] or miarmyMain == None:
        cmds.confirmDialog(t = "Error", m = "No found \"Miarmy_Countents\" group, please create it firstly.")
        raise Exception("No found \"Miarmy_Countents\" group, please create it firstly.")
    else:
        placeAgents = mel.eval('McdListPlaceAgentsCmd -all 0')
        
    if placeAgents == None or placeAgents == []:
        stat = cmds.confirmDialog(t = "Abort", m = 'No agent to place, please check your Original Agents Group.')
        raise Exception('No agent to place, please check your Original Agents Group.')
    
    for i in range(len(placeAgents)):
        if placeAgents[i].find(":") > 0:
            returnList.append(placeAgents[i].split(":")[0])
        else:    
            returnList.append(placeAgents[i].split("Agent_")[1])
        
    return returnList
    
def ReadProportion(allAgents):
    # find McdPlace
    selObj = cmds.ls(sl = True)
    placeNode = ""
    if selObj != [] and selObj != None:
        placeNodeTemp = selObj[0]
        if cmds.nodeType(placeNodeTemp) == "McdPlace":
            placeNode = placeNodeTemp
        else:
            allChildren = cmds.listRelatives(placeNodeTemp, c = True)
            if allChildren == [] or allChildren == None:
                return []
            else:
                if cmds.nodeType(allChildren[0]) == "McdPlace":
                    placeNode = allChildren[0]
                else:
                    return []
                    
    # we got placeNode, parse proportion:
    if placeNode == "":
        return
    
    findNext = True;
    proportionList = []
    i = 0;
    while(findNext == True):
        stri = str(i)
        stri1 = str(i+1)
        stri2 = str(i+2)
        agentid = cmds.getAttr(placeNode + ".proportion[" + stri + "]")
        agentNa = McdFromAgentID2Name(agentid)
        percent = cmds.getAttr(placeNode + ".proportion[" + stri2 + "]")
        if agentid == 0 and percent == 0:
            findNext = False
        else:
            proportionList.append(agentNa)
            proportionList.append(percent)
        i+= 3;
    
    
    
    
    # we got proportionList(name and percent), redrawthe slider!
    endOfList = False
    if proportionList != []:
        proportionListNew = normalizeProportionList(proportionList)

        i = 0;
        while(endOfList == False):
            stri = str(i)
            try:
                agentName = cmds.textField("tf_pe_agtN" + stri, q = True, tx = True)
                cmds.intSlider("is_pe_pro" + stri, e =True, v = 0)
                cmds.intField("if_pe_is" + stri, e = True, v = 0)
                
                for j in range(len(proportionList)/2):
                    if agentName == proportionList[j*2]:
                        vMod = proportionListNew[j]
                        cmds.intSlider("is_pe_pro" + stri, e =True, v = vMod)
                        cmds.intField("if_pe_is" + stri, e = True, v = vMod)
                        
            except:
                endOfList = True;
            i += 1;
    else:
        # we find active agent firstly!! make that 100%
        setActiveAgent = 0
        activeAgentName = McdGetActiveAgentName()
        endOfList = False
        i = 0;
        while(endOfList == False):
            stri = str(i)
            try:
                agentName = cmds.textField("tf_pe_agtN" + stri, q = True, tx = True)
                
                if agentName == activeAgentName:
                    cmds.intSlider("is_pe_pro" + stri, e =True, v = 100)
                    cmds.intField("if_pe_is" + stri, e = True, v = 100)
                    setActiveAgent = 1
                    break;
            except:
                endOfList = True;
            i += 1;
        
        
        # we are in default placement, make the first one 100%
        if setActiveAgent == 0:
            cmds.intSlider("is_pe_pro0", e =True, v = 100)
            cmds.intField("if_pe_is0", e = True, v = 100)
    
def normalizeProportionList(proportionList):
    newList = []
    numOfEle = len(proportionList) / 2
    
    for i in range(numOfEle):
        newList.append(1)
        
    rest = 100 - numOfEle
    for i in range(numOfEle):
        newList[i] += int(rest * proportionList[i*2 + 1])
        
    sum = 0;
    for i in range(numOfEle):
        sum += newList[i]
    
    if sum != 100:
        diff = 100 - sum
        
        # assign it to all of them! not only last one
        #newList[numOfEle-1] += diff
        
        # !!!!!!!!!!!!!!!! (new one:)
        looper = 0
        while diff > 0:
            
            newList[looper] += 1
            
            diff -= 1;
            looper += 1;
            if looper >= numOfEle:
                looper = 0
        
    
    return newList
        
    
    
def is_pe_dCommand(index):
    # search out others' silder with value! in otherEnableList
    otherEnableList = [] # record index list!
    otherEnableListValue = []
    totalValue = 0
    endOfList = False
    i = 0;
    while(endOfList == False):
        stri = str(i)
        try:
            value = cmds.intSlider("is_pe_pro" + stri, q = True, v = True)
            
            if i != index and value != 0:
                otherEnableList.append(i)
                otherEnableListValue.append(value)
                totalValue += value;
        except:
            endOfList = True;
        i += 1;
    
    # normalize otherEnableListValue:
    otherEnableListValueNormal = []
    enableListLen = len(otherEnableList);
    if enableListLen > 0:
        for i in range(enableListLen):
            otherEnableListValueNormal.append(float(otherEnableListValue[i]) / float(totalValue))
        
        # rest = 100 - numOfOtherEnableList
        currentValue = cmds.intSlider("is_pe_pro" + str(index), q = True, v = True)
        cmds.intField("if_pe_is" + str(index), e = True, v = currentValue)
        rest = 100 - enableListLen - currentValue
        
        # dispath rest to the otherEnableList
        otherEnableListValueNew = []
        for i in range(enableListLen):
            otherEnableListValueNew.append(int(float(rest) * otherEnableListValueNormal[i]));
        
        for i in range(enableListLen):
            # set value to slider and intbox:
            if otherEnableListValueNew[i] >= 1:
                cmds.intSlider("is_pe_pro" + str(otherEnableList[i]), e = True, v = otherEnableListValueNew[i])
                cmds.intField("if_pe_is" + str(otherEnableList[i]), e = True, v = otherEnableListValueNew[i])
            else:
                cmds.intSlider("is_pe_pro" + str(otherEnableList[i]), e = True, v = 1)
                cmds.intField("if_pe_is" + str(otherEnableList[i]), e = True, v = 1)
            
        # add otherEnableList at least 1 for each
    else:
        ###canncel slide!!!
        pass
    
def is_pe_cCommand(index):
    # refinement value in silder and intField!
    # find out all non 0 silder and index!!
    enableList = [] # record index list!
    enableListValue = []
    totalValue = 0
    endOfList = False
    i = 0;
    while(endOfList == False):
        stri = str(i)
        try:
            value = cmds.intSlider("is_pe_pro" + stri, q = True, v = True)
            
            if value != 0:
                enableList.append(i)
                enableListValue.append(value)
                totalValue += value;
        except:
            endOfList = True;
        i += 1;
        
    if enableList != []:
        # leave the lower value in 1:
        if totalValue != 100:
            toAdd = 100 - totalValue
            if len(enableList) >1:
                for i in range(len(enableListValue)):
                    if enableListValue[i] > abs(toAdd) + 5:
                        newValue = enableListValue[i] + toAdd
                        cmds.intSlider("is_pe_pro" + str(enableList[i]), e = True, v = newValue)
                        cmds.intField("if_pe_is" + str(enableList[i]), e = True, v = newValue)
                        break
            else:
                cmds.intSlider("is_pe_pro" + str(enableList[0]), e = True, v = 100)
                cmds.intField("if_pe_is" + str(enableList[0]), e = True, v = 100)
    else:
        # we find active agent firstly!! make that 100%
        
        cmds.intField("if_pe_is" + str(index), e = True, v = 0)
        
        setActiveAgent = 0
        activeAgentName = McdGetActiveAgentName()
        endOfList = False
        i = 0;
        while(endOfList == False):
            stri = str(i)
            try:
                agentName = cmds.textField("tf_pe_agtN" + stri, q = True, tx = True)
                
                if agentName == activeAgentName:
                    cmds.intSlider("is_pe_pro" + stri, e =True, v = 100)
                    cmds.intField("if_pe_is" + stri, e = True, v = 100)
                    setActiveAgent = 1
                    break;
            except:
                endOfList = True;
            i += 1;
        
        
        # we are in default placement, make the first one 100%
        if setActiveAgent == 0:
            cmds.intSlider("is_pe_pro0", e =True, v = 100)
            cmds.intField("if_pe_is0", e = True, v = 100)
    
    assignmentToProportionAttr()
    
def makePlacementEven():
    # make even
    # find out all non 0 silder and index!!
    enableList = [] # record index list!
    enableListValue = []
    totalValue = 0
    endOfList = False
    i = 0;
    while(endOfList == False):
        stri = str(i)
        try:
            value = cmds.intSlider("is_pe_pro" + stri, q = True, v = True)
            
            if value != 0:
                enableList.append(i)
                enableListValue.append(value)
                totalValue += value;
        except:
            endOfList = True;
        i += 1;
        
    if enableList != []:
        # leave the lower value in 1:
        eachValue = 100 / len(enableList)
        rest = 100 % len(enableList)
        for i in range(len(enableListValue)):
            if rest != 0:
                cmds.intSlider("is_pe_pro" + str(enableList[i]), e = True, v = eachValue +1)
                cmds.intField("if_pe_is" + str(enableList[i]), e = True, v = eachValue + 1)
                rest -= 1;
            else:
                cmds.intSlider("is_pe_pro" + str(enableList[i]), e = True, v = eachValue)
                cmds.intField("if_pe_is" + str(enableList[i]), e = True, v = eachValue)
    else:
        # we find active agent firstly!! make that 100%
        setActiveAgent = 0
        activeAgentName = McdGetActiveAgentName()
        endOfList = False
        i = 0;
        while(endOfList == False):
            stri = str(i)
            try:
                agentName = cmds.textField("tf_pe_agtN" + stri, q = True, tx = True)
                
                if agentName == activeAgentName:
                    cmds.intSlider("is_pe_pro" + stri, e =True, v = 100)
                    cmds.intField("if_pe_is" + stri, e = True, v = 100)
                    setActiveAgent = 1
                    break;
            except:
                endOfList = True;
            i += 1;
        
        
        # we are in default placement, make the first one 100%
        if setActiveAgent == 0:
            cmds.intSlider("is_pe_pro0", e =True, v = 100)
            cmds.intField("if_pe_is0", e = True, v = 100)
            
        
    assignmentToProportionAttr()
    
def assignmentToProportionAttr():
    enableListValue = []
    enableListID = []
    endOfList = False
    i = 0;
    while(endOfList == False):
        stri = str(i)
        try:
            value = cmds.intSlider("is_pe_pro" + stri, q = True, v = True)
            agentName = cmds.textField("tf_pe_agtN" + stri, tx = True, q = True)
            
            if value != 0:
                agentID = McdFromAgentName2ID(agentName)
                if agentID != None:
                    enableListValue.append(value)
                    enableListID.append(agentID)
        except:
            endOfList = True;
        i += 1;
        
    # parse and get idList and propotion value:(/100)
    #print enableListID
    #print enableListValue            

    # find McdPlace
    selObj = cmds.ls(sl = True)
    placeNode = ""
    if selObj != [] and selObj != None:
        placeNodeTemp = selObj[0]
        if cmds.nodeType(placeNodeTemp) == "McdPlace":
            placeNode = placeNodeTemp
        else:
            allChildren = cmds.listRelatives(placeNodeTemp, c = True)
            if allChildren == [] or allChildren == None:
                return []
            else:
                if cmds.nodeType(allChildren[0]) == "McdPlace":
                    placeNode = allChildren[0]
                else:
                    return []
                    
    # we got placeNode, parse proportion:
    if placeNode != "":
        if enableListValue != []:
            for k in range(len(enableListID) + 1):
                strk = str(k*3)
                strk1 = str(k*3+1)
                strk2 = str(k*3+2)
                if k == len(enableListID):
                    #last one:
                    cmds.setAttr(placeNode + ".proportion[" + strk + "]", 0)
                    cmds.setAttr(placeNode + ".proportion[" + strk1 + "]", 0)
                    cmds.setAttr(placeNode + ".proportion[" + strk2 + "]", 0)
                else:
                    cmds.setAttr(placeNode + ".proportion[" + strk + "]", enableListID[k])
                    cmds.setAttr(placeNode + ".proportion[" + strk1 + "]", enableListID[k])
                    cmds.setAttr(placeNode + ".proportion[" + strk2 + "]", float(enableListValue[k]) / 100.0)
    
    mel.eval("setAttr " + placeNode + "._EntryMsg 1;")
    
    
def addPlaceOffsetRecord(chID, opt):
    # find McdPlace
    selObj = cmds.ls(sl = True)
    placeNode = ""
    if selObj != [] and selObj != None:
        placeNodeTemp = selObj[0]
        if cmds.nodeType(placeNodeTemp) == "McdPlace":
            placeNode = placeNodeTemp
        else:
            allChildren = cmds.listRelatives(placeNodeTemp, c = True, path = True)
            if allChildren == [] or allChildren == None:
                cmds.confirmDialog(t = "Error", m = "Please select place node.")
                return
            else:
                if cmds.nodeType(allChildren[0]) == "McdPlace":
                    placeNode = allChildren[0]
                else:
                    cmds.confirmDialog(t = "Error", m = "Please select place node.")
                    return
    else:
        cmds.confirmDialog(t = "Error", m = "Please select place node.")
        return
    
    placerId = cmds.intField("placerID", q = True, v = True)
    
    strCh = str(chID)
    offVal = cmds.floatField("ff_off" + strCh, q = True, v = True)
    if opt == 0:
        offVal *= -1.0
    
    collectIds = []
    agentCounter = 0
    while(True):
        agentId = cmds.getAttr(placeNode + ".userOffset[" + str(agentCounter * 8) + "]")
        if int(agentId) == -1:
            break
        else:
            collectIds.append(int(agentId))
        agentCounter += 1;
    
    try:
        optIndex = collectIds.index(placerId)
    except:
        optIndex = -1
        
    if optIndex == -1:
        print "recored inserted..."
        optIndex = len(collectIds)
        cmds.setAttr(placeNode + ".userOffset[" + str(optIndex * 8) + "]", placerId)
        cmds.setAttr(placeNode + ".userOffset[" + str(optIndex * 8 + 1) + "]", 0)
        cmds.setAttr(placeNode + ".userOffset[" + str(optIndex * 8 + 2) + "]", 0)
        cmds.setAttr(placeNode + ".userOffset[" + str(optIndex * 8 + 3) + "]", 0)
        cmds.setAttr(placeNode + ".userOffset[" + str(optIndex * 8 + 4) + "]", 0)
        cmds.setAttr(placeNode + ".userOffset[" + str(optIndex * 8 + 5) + "]", 0)
        cmds.setAttr(placeNode + ".userOffset[" + str(optIndex * 8 + 6) + "]", 0)
        
        
    # operate on optIndex
    toModVal = cmds.getAttr(placeNode + ".userOffset[" + str(optIndex * 8 + chID) + "]")
    toModVal += offVal
    cmds.setAttr(placeNode + ".userOffset[" + str(optIndex * 8 + chID) + "]", toModVal)
    
    
def clearCurrentRecord():
    # find McdPlace
    selObj = cmds.ls(sl = True)
    placeNode = ""
    if selObj != [] and selObj != None:
        placeNodeTemp = selObj[0]
        if cmds.nodeType(placeNodeTemp) == "McdPlace":
            placeNode = placeNodeTemp
        else:
            allChildren = cmds.listRelatives(placeNodeTemp, c = True, path = True)
            if allChildren == [] or allChildren == None:
                cmds.confirmDialog(t = "Error", m = "Please select place node.")
                return
            else:
                if cmds.nodeType(allChildren[0]) == "McdPlace":
                    placeNode = allChildren[0]
                else:
                    cmds.confirmDialog(t = "Error", m = "Please select place node.")
                    return
    else:
        cmds.confirmDialog(t = "Error", m = "Please select place node.")
        return
    
    placerId = cmds.intField("placerID", q = True, v = True)
    
    
    collectIds = []
    agentCounter = 0
    while(True):
        agentId = cmds.getAttr(placeNode + ".userOffset[" + str(agentCounter * 8) + "]")
        if int(agentId) == -1:
            break
        else:
            collectIds.append(int(agentId))
        agentCounter += 1;
    
    try:
        optIndex = collectIds.index(placerId)
    except:
        optIndex = -1
        
    if optIndex == -1:
        cmds.confirmDialog(t = "Note", m = "No record for index: " + str(placerId))
        return
        
    # operate on optIndex
    for i in range(6):
        cmds.setAttr(placeNode + ".userOffset[" + str(optIndex * 8 + i + 1) + "]", 0)
    

def clearAllRecord():
    # find McdPlace
    selObj = cmds.ls(sl = True)
    placeNode = ""
    if selObj != [] and selObj != None:
        placeNodeTemp = selObj[0]
        if cmds.nodeType(placeNodeTemp) == "McdPlace":
            placeNode = placeNodeTemp
        else:
            allChildren = cmds.listRelatives(placeNodeTemp, c = True, path = True)
            if allChildren == [] or allChildren == None:
                cmds.confirmDialog(t = "Error", m = "Please select place node.")
                return
            else:
                if cmds.nodeType(allChildren[0]) == "McdPlace":
                    placeNode = allChildren[0]
                else:
                    cmds.confirmDialog(t = "Error", m = "Please select place node.")
                    return
    else:
        cmds.confirmDialog(t = "Error", m = "Please select place node.")
        return
    
    placerId = cmds.intField("placerID", q = True, v = True)
    
    
    collectIds = []
    agentCounter = 0
    while(True):
        agentId = cmds.getAttr(placeNode + ".userOffset[" + str(agentCounter * 8) + "]")
        if int(agentId) == -1:
            break
        else:
            collectIds.append(int(agentId))
        agentCounter += 1;
    
    if collectIds == []:
        return
        
    # operate on all
    for k in range(len(collectIds)):
        for i in range(6):
            cmds.setAttr(placeNode + ".userOffset[" + str(k * 8 + i + 1) + "]", 0)
    
    
def setGlobal(globalNode, index):
    if index == 0:
        qVal = cmds.intField("plStartID", q = True, v = True)
    else:
        qVal = cmds.intField("plEndID", q = True, v = True)
    cmds.setAttr(globalNode + ".placeAgent[" + str(index) + "]", qVal)
    
