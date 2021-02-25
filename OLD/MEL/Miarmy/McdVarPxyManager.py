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
from McdVarPxyManagerGUI import *

def McdVarPxyMngGetNodeNameFromGUI():
    agentGroupName = cmds.textField("VarGrpNodeTF1", q = True, tx = True)
    return agentGroupName

def cb_avp_active(index):
    agtGrpNode = McdVarPxyMngGetNodeNameFromGUI()
    cmds.setAttr(agtGrpNode + ".active[" + str(index) + "]", True)
    McdVarPxyManagerGUI()
    
def cb_avp_deactive(index):
    agtGrpNode = McdVarPxyMngGetNodeNameFromGUI()
    cmds.setAttr(agtGrpNode + ".active[" + str(index) + "]", False)
    McdVarPxyManagerGUI()

def tf_avp_avName(index):
    stri = str(index)
    agtGrpNode = McdVarPxyMngGetNodeNameFromGUI()
    fillName = cmds.intField("tf_avp_avPlace" + stri, q = True, v = True)
    cmds.setAttr(agtGrpNode + ".placeId[" + str(index) + "]", fillName)
    
def ff_avp_avMin(index):
    stri = str(index)
    agtGrpNode = McdVarPxyMngGetNodeNameFromGUI()
    fillVal = cmds.intField("btn_avp_avMin" + stri, q = True, v = True)
    cmds.setAttr(agtGrpNode + ".placeAgentIdStart[" + str(index) + "]", fillVal)
    
def ff_avp_avMax(index):
    stri = str(index)
    agtGrpNode = McdVarPxyMngGetNodeNameFromGUI()
    fillVal = cmds.intField("om_avp_avMax" + stri, q = True, v = True)
    cmds.setAttr(agtGrpNode + ".placeAgentIdEnd[" + str(index) + "]", fillVal)
    

