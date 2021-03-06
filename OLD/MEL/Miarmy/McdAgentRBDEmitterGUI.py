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
##  Module Name: RBD Editor
##
##  Description:
##    For managing RBD in scene, globally.
##
## ===================================================================
## -

import maya.cmds as cmds
from McdGeneral import *
from McdSimpleCmd import *

import McdAgentRBDEmitter
reload(McdAgentRBDEmitter)
from McdAgentRBDEmitter import *


def McdAgentRBDEmitterGUI():
    
    winName = "McdAgentRBDEmitter"
    if cmds.window(winName, ex = True):
        cmds.deleteUI(winName)
    cmds.window(winName, title = "Agent RBD Emitter Manager",rtf =True,menuBar=True, width=200)
    
    cmds.menu( label='Options')
    cmds.menuItem( label='Refresh contents', c = "McdRefreshAgentRBDEmitter()")
    cmds.menuItem( label='Help' )
    cmds.menuItem( divider=True )
    cmds.menuItem( label='Exit', c = "McdExitAgentRBDEmitter()" )
    
    form = cmds.formLayout()
    tabs = cmds.tabLayout(innerMarginWidth=5, innerMarginHeight=5)
    cmds.formLayout( form, edit=True, attachForm=((tabs, 'top', 0), (tabs, 'left', 0), (tabs, 'bottom', 0), (tabs, 'right', 0)) )
    
    info = []
    
    rbdNode = ""
    selObj = cmds.ls(sl = True)
    if not McdIsBlank(selObj):
        if (cmds.nodeType(selObj[0]) == "McdRBDEmitter"):
            rbdNode = selObj[0]
        else:
            allChild = getAllChildren(selObj[0])
            if not MIsBlank(allChild):
                if (cmds.nodeType(allChild[0]) == "McdRBDEmitter"):
                    rbdNode = allChild[0];
    else:
        rbdNode = ""
    
    child0 = cmds.columnLayout(adj = True)
    
    #(4,80)
    if rbdNode == "":
        cmds.text(l = "Please select one of RBD emitter")
    else:
        nbSlot = cmds.getAttr(rbdNode + ".active")
        
        cmds.rowColumnLayout(nc = 8, cw = [(1,100),(2,100),(3,50),(4,50),(5, 50), (6, 50),(7, 50),(8, 80)])
        cmds.text(l = "Action Name", align = "left", font = "smallBoldLabelFont")
        cmds.text(l = "Bone Name", align = "left", font = "smallBoldLabelFont")
        cmds.text(l = "Start", align = "left", font = "smallBoldLabelFont")
        cmds.text(l = "End", align = "left", font = "smallBoldLabelFont")
        cmds.text(l = "Dir X", align = "left", font = "smallBoldLabelFont")
        cmds.text(l = "Dir Y", align = "left", font = "smallBoldLabelFont")
        cmds.text(l = "Dir Z", align = "left", font = "smallBoldLabelFont")
        cmds.text(l = "Dir Rand", align = "left", font = "smallBoldLabelFont")
    
        # fill contents here:
        for i in range(nbSlot):
            stri = str(i)
            
            actionName = cmds.getAttr(rbdNode + ".actionName[" + stri + "]")
            if actionName == None or actionName == []:
                actionName = ""
            boneName = cmds.getAttr(rbdNode + ".boneName[" + stri + "]")
            if boneName == None or boneName == []:
                boneName = ""
            dStartFrame = cmds.getAttr(rbdNode + ".startFrame[" + stri + "]")
            dEndFrame = cmds.getAttr(rbdNode + ".endFrame[" + stri + "]")
            dEmitX = cmds.getAttr(rbdNode + ".emitDirX[" + stri + "]")
            dEmitY = cmds.getAttr(rbdNode + ".emitDirY[" + stri + "]")
            dEmitZ = cmds.getAttr(rbdNode + ".emitDirZ[" + stri + "]")
            dRandDir = cmds.getAttr(rbdNode + ".randDir[" + stri + "]")
            
            
            cmds.textField("actionName_tfrb" + stri, tx = actionName, cc = "changeRBDEmitterAN('" + rbdNode + "', "+stri+")")
            cmds.textField("boneName_tfrb" + stri, tx = boneName, cc = "changeRBDEmitterBN('" + rbdNode + "', "+stri+")")
            cmds.intField("startFrame_ffrb" + stri, v = dStartFrame, cc = "changeRBDEmitterSF('" + rbdNode + "', "+stri+")")
            cmds.intField("endFrame_ffrb" + stri, v = dEndFrame, cc = "changeRBDEmitterEF('" + rbdNode + "', "+stri+")")
            cmds.floatField("emitX_ffrb" + stri, v = dEmitX, cc = "changeRBDEmitterEX('" + rbdNode + "', "+stri+")")
            cmds.floatField("emitY_ffrb" + stri, v = dEmitY, cc = "changeRBDEmitterEY('" + rbdNode + "', "+stri+")")
            cmds.floatField("emitZ_ffrb" + stri, v = dEmitZ, cc = "changeRBDEmitterEZ('" + rbdNode + "', "+stri+")")
            cmds.floatField("emitR_ffrb" + stri, v = dRandDir, cc = "changeRBDEmitterER('" + rbdNode + "', "+stri+")")
    
        cmds.setParent("..")
    
    # expand and shink button
    cmds.rowColumnLayout(nc = 6, cw = [(1,120),(2,10),(3,120),(4, 10),(5, 170)])
    cmds.button(l = "Expand Slot", c = 'McdExpandSlotRBDEmitter("' + rbdNode + '")')
    cmds.text(l ="")
    cmds.button(l = "Shink Slot", c = 'McdShrinkSlotRBDEmitter("' + rbdNode + '")')
    cmds.setParent("..")
    
    
    cmds.setParent("..")
    
    
    #------------------------------- Cricial Help --------------------------------#
    child1 = cmds.columnLayout(adj = True)
    cmds.text(l = "* Edit RBD emitter from agent bone", fn = "smallBoldLabelFont", align = "left")
    
    cmds.separator(h = 10)
    cmds.button(l = "Check detailed help")
    
    cmds.setParent( '..' )
    
    
    cmds.tabLayout( tabs, edit=True,tabLabel=((child0, "RBD Emitter"),(child1, "Quick Tips")))
    cmds.showWindow(winName)



def McdRefreshAgentRBDEmitter():
    McdAgentRBDEmitterGUI()

def McdExitAgentRBDEmitter():
    try:
        cmds.deleteUI("McdAgentRBDEmitter")
    except:
        pass


