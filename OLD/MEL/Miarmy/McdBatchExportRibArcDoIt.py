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
##  Module Name: McdAutoGenAgentCache.py
##
##  Description:
##    Generate agent cache in command line
##
## ===================================================================
## -

import maya.cmds as cmds
import maya.mel as mel
from McdGeneral import *
from McdRender import *
import os

def McdBatchExportRibArcDoIt():
    # ---------------------------------------
    # place agent out
    # turn off mesh drive and agent cache
    # go back to start frame
    # make agent cache
    # ---------------------------------------

    
    # place agent out
    cmd = "McdPlacementCmd -am 3 -ign 0;"
    mel.eval(cmd)
    McdAfterPlaceFunction()
    
    # turn off mesh drive and agent cache
    allGlb = cmds.ls(type = "McdGlobal")
    if McdIsBlank(allGlb):
        raise Exception("No found McdGlobal Node.")
        return
    for i in range(len(allGlb)):
        cmds.setAttr(allGlb[i] + ".enableMeshDrv", 0)
        cmds.setAttr(allGlb[i] + ".selectionCallback", 1)
    
    # make agent cache
    McdRenderBegin(1, 1, 1)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    