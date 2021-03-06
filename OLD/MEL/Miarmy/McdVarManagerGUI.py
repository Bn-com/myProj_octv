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

import McdVarManager
reload(McdVarManager)
from McdVarManager import *


def McdVarManagerGUI():
    
    winName = "McdVarManager"
    if cmds.window(winName, ex = True):
        cmds.deleteUI(winName)
    
    globalNode = McdGetMcdGlobalNode()
        
    cmds.window(winName, title = "Agent/Host Variable Manager",rtf =True,menuBar=True, width=250)
    cmds.menu( label='Options')
    cmds.menuItem( label='Refresh contents', c = "McdRefreshVarManager()")
    cmds.menuItem( label='Help' )
    cmds.menuItem( divider=True )
    cmds.menuItem( label='Exit', c = "McdExitVarManager()" )

    form = cmds.formLayout()
    tabs = cmds.tabLayout(innerMarginWidth=5, innerMarginHeight=5)
    cmds.formLayout( form, edit=True, attachForm=((tabs, 'top', 0), (tabs, 'left', 0), \
                                                (tabs, 'bottom', 0), (tabs, 'right', 0)) )
    
    #++++++++++++++++++++++++++++ Var List Setup +++++++++++++++++++++++++++++#
    selObj = cmds.ls(sl = True, long = True)
    if selObj != [] and selObj != None:
        dcNode = selObj[0]
    
    child0 = cmds.columnLayout(adj = True)
    
    cmds.rowColumnLayout(nc = 3, cw = [(1,100),(2,100),(3,100)])
    cmds.text(l = "Node Name:")
    try:
        cmds.textField("AgentGrpNodeTF1", ed = False, tx = dcNode)
    except:
        pass
    cmds.text(l = "")
    cmds.setParent("..")


    selObj = cmds.ls(sl = True, long = True)
    
    # for input perception:
    cmds.rowColumnLayout(nc = 4, cw = [(1,40),(2,100),(3,60),(4,60)])
    cmds.text(l = "Active", fn = "smallBoldLabelFont", align = "center")
    cmds.text(l = "Variable Name", fn = "smallBoldLabelFont", align = "center")
    cmds.text(l = "Min", fn = "smallBoldLabelFont", align = "center")
    cmds.text(l = "Max", fn = "smallBoldLabelFont", align = "center")
    
    # for parsing selected object and fill contents;
    
    if selObj != [] and selObj != None:
        dcNode = selObj[0]
        typeName = cmds.nodeType(dcNode)
        if typeName == "McdAgentGroup" or typeName == "McdVarHost":
            # for displaying detail of node:
            varCount = 0
            while(1):
                stri = str(varCount)
                # active value:
                dActive = cmds.getAttr(dcNode + ".avActive[" +stri+ "]")
                if dActive == 0:
                    cmds.checkBox("cb_av_active" + stri,l = "", v = 0, onc = "cb_av_active(" + stri + ")") #active
                    cmds.textField("tf_av_avName" + stri, en = False)
                    cmds.floatField("btn_av_avMin" + stri, en = False)
                    cmds.floatField("om_av_avMax" + stri, en = False)
                    break
                
                dAvName = cmds.getAttr(dcNode + ".avNames[" + stri + "]")
                dAvMin = cmds.getAttr(dcNode + ".avMin[" + stri + "]")
                dAvMax = cmds.getAttr(dcNode + ".avMax[" + stri + "]")
                
                cmds.checkBox("cb_av_active" + stri,l = "", v = dActive, ofc = "cb_av_deactive(" + stri + ")") #active
                cmds.textField("tf_av_avName" + stri, tx = dAvName, cc = "tf_av_avName(" + stri + ")")
                cmds.floatField("btn_av_avMin" + stri, v = dAvMin, pre = 2, cc = "ff_av_avMin(" + stri + ")")
                cmds.floatField("om_av_avMax" + stri, v = dAvMax, pre = 2, cc = "ff_av_avMax(" + stri + ")")

                varCount += 1
            
    cmds.setParent("..")
    
    
    cmds.setParent("..")
    
    
    #+++++++++++++++++++++++++++++++ Instant Tips ++++++++++++++++++++++++++++++++#
    child1 = cmds.columnLayout(adj = True)
    #separator(h = 10)
    cmds.text(l = "Instant Tips for Agent Variable Manager", fn = "smallBoldLabelFont", align = "left")
    cmds.text(l = "* Setup agent variable on agent group nodes.", align = "left")
    cmds.button(l = "Check detailed help", h = 40)
    
    cmds.setParent( '..' )
    #----------------------------- End Instant Tips -------------------------------#
    
    cmds.tabLayout( tabs, edit=True,tabLabel=((child0, "Agent Variable Setup"),\
                                            (child1, "Instant Tips")))
    cmds.showWindow(winName)



def McdRefreshVarManager():
    McdVarManagerGUI()

def McdExitVarManager():
    try:
        cmds.deleteUI("McdVarManager")
    except:
        pass



