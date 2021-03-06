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
import maya.mel as mel
from McdGeneral import *

import McdStoryListEditor
reload(McdStoryListEditor)
from McdStoryListEditor import *


def McdStoryListEditorGUI():
    
    winName = "McdStoryListEditor"
    if cmds.window(winName, ex = True):
        cmds.deleteUI(winName)
    
    globalNode = McdGetMcdGlobalNode()
        
    cmds.window(winName, title = "Story List Editor",rtf =True,menuBar=True, width=250)
    cmds.menu( label='Options')
    cmds.menuItem( label='Refresh contents', c = "McdRefreshStoryEditor()")
    cmds.menuItem( label='Help' )
    cmds.menuItem( divider=True )
    cmds.menuItem( label='Exit', c = "McdExitStoryEditor()" )

    form = cmds.formLayout()
    tabs = cmds.tabLayout(innerMarginWidth=5, innerMarginHeight=5)
    cmds.formLayout( form, edit=True, attachForm=((tabs, 'top', 0), (tabs, 'left', 0), \
                                                (tabs, 'bottom', 0), (tabs, 'right', 0)) )
    
    #++++++++++++++++++++++++++++ Story List Setup +++++++++++++++++++++++++++++#
    dcNode = ""
    selObj = cmds.ls(sl = True, long = True)
    selType = ""
    if selObj != [] and selObj != None:
        selType = cmds.nodeType(selObj[0])
        if selType == "McdStoryList":
            dcNode = selObj[0]
            
    if not McdCheckNodeActiveCmd(dcNode):
        dcNode = ""
            
        
    child0 = cmds.columnLayout(adj = True)
    
    if dcNode != "":
        
        dInterruptible = cmds.getAttr(dcNode + ".interruptible")
        dPureStateNode = cmds.getAttr(dcNode + ".playMode")
        
        cmds.rowColumnLayout(nc = 4, cw = [(1,100),(2,100),(3,100), (4,200)])
        cmds.text(l = "Node Name:")
        try:
            cmds.textField("StoryNodeTF", ed = False, tx = dcNode)
        except:
            pass
        cmds.checkBox("storyItrp_cb", v = dInterruptible, l = "Interruptible", onc = "storyInterruptible(1)", \
                                                                             ofc = "storyInterruptible(0)")
        
        cmds.checkBox("puresm_cb", v = dPureStateNode, l = "Pure State Node", onc = "storySM(1)", ofc = "storySM(0)")
        
        cmds.setParent("..")    
        selObj = cmds.ls(sl = True, long = True)
        
        allTypeActions = findAllTypeActions()
        allStoryNames = getAllStoryNames(dcNode)
        
        cmds.rowColumnLayout(nc = 4, cw = [(1, 200), (2, 200), (3, 200), (4, 200)])
        
        # // line 1
        if not dPureStateNode:
            cmds.text(l = "All Actions")
            cmds.text("sto_t1", l = "(ID) Story Main")
            cmds.text("sto_t2", l = "(Weight) Story Branch")
            cmds.text(l = "All Actions")
        else:
            cmds.text(l = "All Actions")
            cmds.text("sto_t1", l = "State Actions")
            cmds.text("sto_t2", l = "(Weight) Exit Actions")
            cmds.text(l = "All Actions")
        
        # // line 2
        cmds.textScrollList("sto_tsl_allact1", numberOfRows = 16, append = allTypeActions)
        cmds.textScrollList("sto_tsl_main", numberOfRows = 16, append = allStoryNames, sc = "updateStoryBranchList()")
        cmds.textScrollList("sto_tsl_bnch", numberOfRows = 16, dcc = "changeBranchWeight()")
        cmds.textScrollList("sto_tsl_allact2", numberOfRows = 16, append = allTypeActions, en = False)
        
        # // line 3
        cmds.button(l = "Add ->", c = "addToStoryList()")
        cmds.rowColumnLayout(nc = 2, cw = [(1, 100), (2, 100)])
        cmds.button(l = "Move Up", c = "moveupInStoryList()")
        cmds.button(l = "Remove", c = "removeFromStoryList()")
        cmds.setParent("..")
        cmds.rowColumnLayout(nc = 2, cw = [(1, 100), (2, 100)])
        cmds.button(l = "Move Up", c = "moveupInBranchList()")
        cmds.button(l = "Remove", c = "removeFromBranchList()")
        cmds.setParent("..")
        cmds.button("addToBranch_btn", l = "<- Add", c = "addToBranchList()", en = False)
        
        cmds.setParent("..")

    else:
        cmds.columnLayout(adj  = 1)
        cmds.text(l = "Please select active story list node")
        cmds.setParent("..")
    
    
    cmds.setParent("..")
    
    
    #+++++++++++++++++++++++++++++++ Instant Tips ++++++++++++++++++++++++++++++++#
    child1 = cmds.columnLayout(adj = True)
    #separator(h = 10)
    cmds.text(l = "Instant Tips for Story Editor", fn = "smallBoldLabelFont", align = "left")
    cmds.text(l = "* State machine for arranging the pre-define actions playback list.", align = "left")
    cmds.button(l = "Check detailed help", h = 40)
    
    cmds.setParent( '..' )
    #----------------------------- End Instant Tips -------------------------------#
    
    cmds.tabLayout( tabs, edit = True, tabLabel=((child0, "Agent Variable Setup"), (child1, "Instant Tips")))
    cmds.showWindow(winName)



def McdRefreshStoryListEditor():
    McdStoryListEditorGUI()

def McdExitStoryListEditor():
    try:
        cmds.deleteUI("McdStoryListEditor")
    except:
        pass

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
