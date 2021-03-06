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
## TRADE PRACTICE. IN NO EVENT WILL BASEFOUNTAIN AND/OR ITS LICENSORS 
## BE LIABLE FOR ANY LOST REVENUES, DATA, OR PROFITS, OR SPECIAL, 
## DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES, EVEN IF BASEFOUNTAIN 
## AND/OR ITS LICENSORS HAS BEEN ADVISED OF THE POSSIBILITY 
## OR PROBABILITY OF SUCH DAMAGES.
##
## ===================================================================
## -

## +
## ===================================================================
##  Module Name: RBD emitter Editor
##
##  Description:
##    For managing RBD in scene, globally.
##
## ===================================================================
## -

import maya.cmds as cmds
from McdGeneral import *
from McdSimpleCmd import *
from McdAgentRBDEmitterGUI import *


def McdExpandSlotRBDEmitter(rbdNode):
    nbSlot = cmds.getAttr(rbdNode + ".active")
    nbSlot += 1
    cmds.setAttr(rbdNode + ".active", nbSlot)
    
    McdRefreshAgentRBDEmitter()
        
def McdShrinkSlotRBDEmitter(rbdNode):
    nbSlot = cmds.getAttr(rbdNode + ".active")
    nbSlot -= 1
    cmds.setAttr(rbdNode + ".active", nbSlot)
    
    McdRefreshAgentRBDEmitter()

# ##########################################################################
def changeRBDEmitterAN(rbdNode, index):
    stri = str(index)
    value = cmds.textField("actionName_tfrb" + stri, q = True, tx = True)
    
    cmds.setAttr(rbdNode + ".actionName[" + stri + "]", value, type = "string")
    
def changeRBDEmitterBN(rbdNode, index):
    stri = str(index)
    value = cmds.textField("boneName_tfrb" + stri, q = True, tx = True)
    
    cmds.setAttr(rbdNode + ".boneName[" + stri + "]", value, type = "string")

def changeRBDEmitterSF(rbdNode, index):
    stri = str(index)
    value = cmds.intField("startFrame_ffrb" + stri, q = True, v = True)
    
    cmds.setAttr(rbdNode + ".startFrame[" + stri + "]", value)
    
def changeRBDEmitterEF(rbdNode, index):
    stri = str(index)
    value = cmds.intField("endFrame_ffrb" + stri, q = True, v = True)
    
    cmds.setAttr(rbdNode + ".endFrame[" + stri + "]", value)
    

def changeRBDEmitterEX(rbdNode, index):
    stri = str(index)
    value = cmds.floatField("emitX_ffrb" + stri, q = True, v = True)
    
    cmds.setAttr(rbdNode + ".emitDirX[" + stri + "]", value)

def changeRBDEmitterEY(rbdNode, index):
    stri = str(index)
    value = cmds.floatField("emitY_ffrb" + stri, q = True, v = True)
    
    cmds.setAttr(rbdNode + ".emitDirY[" + stri + "]", value)
    
def changeRBDEmitterEZ(rbdNode, index):
    stri = str(index)
    value = cmds.floatField("emitZ_ffrb" + stri, q = True, v = True)
    
    cmds.setAttr(rbdNode + ".emitDirZ[" + stri + "]", value)
    
def changeRBDEmitterER(rbdNode, index):
    stri = str(index)
    value = cmds.floatField("emitR_ffrb" + stri, q = True, v = True)
    
    cmds.setAttr(rbdNode + ".randDir[" + stri + "]", value)

