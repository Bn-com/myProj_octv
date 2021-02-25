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
##  Module Name: McdActionSyncEditorGUI
##
##  Description:
##    Miarmy Global
##
## ===================================================================
## -

import maya.cmds as cmds
import maya.mel as mel
from McdGeneral import *
from McdSimpleCmd import *

import McdActionSyncEditor
reload(McdActionSyncEditor)
from McdActionSyncEditor import *

def McdActionSyncEditorGUI():
    
    winName = "McdActionSyncEditor"
    if cmds.window(winName, ex = True):
        cmds.deleteUI(winName)
        
    cmds.window(winName, title = "Action Synchronization Editor",rtf =True,menuBar=True, width=250)
    cmds.menu( label='Options')
    cmds.menuItem( label='Refresh contents', c = "McdRefreshActionSyncEditor()")
    cmds.menuItem( label='Help' )
    cmds.menuItem( divider=True )
    cmds.menuItem( label='Exit', c = "McdExitActionSyncEditor()" )

    form = cmds.formLayout()
    tabs = cmds.tabLayout(innerMarginWidth=5, innerMarginHeight=5)
    cmds.formLayout( form, edit=True, attachForm=((tabs, 'top', 0), (tabs, 'left', 0), \
                                                (tabs, 'bottom', 0), (tabs, 'right', 0)) )
    
    infoData = queryActionSyncInfo()
    
    child0 = cmds.columnLayout(adj = True)
    cmds.rowColumnLayout(nc = 4, cw = [(1, 200), (2, 50), (3, 200), (4, 100)])
    cmds.text(l = "Subjective Actions", fn = "smallBoldLabelFont", align = "left")
    cmds.text(l = "")
    cmds.text(l = "Objective Actions", fn = "smallBoldLabelFont", align = "left")
    cmds.text(l = "")
    
    if infoData != []:
        for i in range(len(infoData) / 2):
            stri = str(i)
            if i % 2 == 0:
                color = [.2,.2,.2]
            else:
                color = [.15,.15,.15]
            cmds.text("actSub" + stri, l = infoData[i*2], bgc = color)
            cmds.text(l = "->", bgc = color)
            cmds.text("actObj" + stri, l = infoData[i*2+1], bgc = color)
            cmds.button(l = "Clear This Link", c = "clearActionSyncRec(" + stri + ")")
    
    cmds.setParent("..") # end of row column layout
    
    cmds.rowColumnLayout(nc = 3, cw = [(1, 100), (2, 100)])
    cmds.button(l = "Link Selections", c = "establishActionSyncLink()")
    cmds.button(l = "Clear All Links", c = "clearAllActionSyncLinks()")
    cmds.setParent("..") # end of row column layout
    cmds.setParent("..") # enf of tab layout
    
    # -------------------------------------------------------------------------------
    child1 = cmds.columnLayout(adj = True)
    
    cmds.text(l = "One action can link to multi actions", fn = "smallBoldLabelFont", align = "left", h = 20)
    cmds.text(l = "One action can link to multi actions", fn = "smallBoldLabelFont", align = "left", h = 20)

    cmds.setParent( '..' )
    
    
    cmds.tabLayout( tabs, edit=True, tabLabel=((child0, "Action Pairs"), (child1, "Instant Tip")))
    cmds.showWindow(winName)

def McdRefreshActionSyncEditor():
    McdActionSyncEditorGUI()

def McdExitActionSyncEditor():
    try:
        cmds.deleteUI("McdActionSyncEditor")
    except:
        pass
























