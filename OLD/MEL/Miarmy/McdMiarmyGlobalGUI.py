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
##  Module Name: McdMiarmyGlobal
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

import McdMiarmyGlobal
reload(McdMiarmyGlobal)
from McdMiarmyGlobal import *

def McdMiarmyGlobalGUI():
    
    winName = "McdMiarmyGlobal"
    if cmds.window(winName, ex = True):
        cmds.deleteUI(winName)
    
    activeName = McdGetActiveAgentName()
        
    cmds.window(winName, title = "Miarmy Global",rtf =True,menuBar=True, width=250)
    cmds.menu( label='Options')
    cmds.menuItem( label='Refresh contents', c = "McdRefreshMiarmyGlobal()")
    cmds.menuItem( label='Help' )
    cmds.menuItem( divider=True )
    cmds.menuItem( label='Exit', c = "McdExitMiarmyGlobal()" )

    form = cmds.formLayout()
    tabs = cmds.tabLayout(innerMarginWidth=5, innerMarginHeight=5)
    cmds.formLayout( form, edit=True, attachForm=((tabs, 'top', 0), (tabs, 'left', 0), \
                                                (tabs, 'bottom', 0), (tabs, 'right', 0)) )
    
    #--------------------------  Main GUI  --------------------------#
    globalNode = McdListMcdGlobal()
    brainNode = McdListMcdBrain()
    
    dSimpleTrans = cmds.getAttr(globalNode + ".smpTrans")
    dFeedback = cmds.getAttr(globalNode + ".selectionCallback")
    dSloverRight = cmds.getAttr(globalNode + ".solverRight")
    dStartTime = cmds.getAttr(brainNode + ".startTime")
    
    dDisableCB = cmds.getAttr(globalNode + ".disableCB")
    
    dTbbEnable = cmds.getAttr(brainNode + ".tbbEnable")
    
    dBoolMaster0 = cmds.getAttr(globalNode + ".boolMaster[0]")
    dBoolMaster1 = cmds.getAttr(globalNode + ".boolMaster[1]")
    
    dBoolMaster3 = cmds.getAttr(globalNode + ".boolMaster[3]")
    
    dAutoAvoid = cmds.getAttr(globalNode + ".boolMaster[7]")
    dAvoidSpeed = cmds.getAttr(globalNode + ".avdSpd")
    
    dHookCD = cmds.getAttr(globalNode + ".hookCustomData")
    dEnScale = cmds.getAttr(globalNode + ".enableScale")
    
    dDifferCC = cmds.getAttr(brainNode + ".differCTime")
    dCStartTime = cmds.getAttr(brainNode + ".startCTime")
    
    child0 = cmds.columnLayout(adj = True)
    cmds.columnLayout(adj = True)
    cmds.text(l = "Transition Type", fn = "smallBoldLabelFont", align = "left", h = 20)
    cmds.checkBoxGrp("mgspt_cbg", l = "Use Simple Transition", v1 = dSimpleTrans, \
                   on1 = 'setSingleNumericAttrSliderGrpMiG(0, "mgspt_cbg", "'+globalNode+'", "smpTrans")',\
                   of1 = 'setSingleNumericAttrSliderGrpMiG(0, "mgspt_cbg", "'+globalNode+'", "smpTrans")')
    
    cmds.text(l = "")
    cmds.text(l = "Solver Options", fn = "smallBoldLabelFont", align = "left", h = 20)
    cmds.checkBoxGrp("mgfbk_cbg", l = "Stop Feedback", v1 = dFeedback, \
                   on1 = 'setSingleNumericAttrSliderGrpMiG(0, "mgfbk_cbg", "'+globalNode+'", "selectionCallback")',\
                   of1 = 'setSingleNumericAttrSliderGrpMiG(0, "mgfbk_cbg", "'+globalNode+'", "selectionCallback")')
    
    cmds.checkBoxGrp("mgsrt_cbg", l = "Pause Solve", v1 = dSloverRight, \
                   on1 = 'setSingleNumericAttrSliderGrpMiG(0, "mgsrt_cbg", "'+globalNode+'", "solverRight")',\
                   of1 = 'setSingleNumericAttrSliderGrpMiG(0, "mgsrt_cbg", "'+globalNode+'", "solverRight")')
    
    cmds.floatFieldGrp("mbsst1_ifg", l = "Start Time:", v1 = dStartTime, \
                   cc = 'setSingleNumericAttrFieldGrpMiGA(2, "mbsst1_ifg", "'+brainNode+'", "startTime")')
    
    cmds.checkBoxGrp("mgtbb_dfcst", l = "Differ Char Cache Start Time", v1 = dDifferCC, \
                   on1 = 'setSingleNumericAttrSliderGrpMiG(0, "mgtbb_dfcst", "'+brainNode+'", "differCTime")',\
                   of1 = 'setSingleNumericAttrSliderGrpMiG(0, "mgtbb_dfcst", "'+brainNode+'", "differCTime")')
    
    if dDifferCC == 1:
        cmds.floatFieldGrp("mbsst1_ccst", l = "Char Cache Start Time:", v1 = dCStartTime, \
                   cc = 'setSingleNumericAttrFieldGrpMiGA(2, "mbsst1_ccst", "'+brainNode+'", "startCTime")')
    else:
        cmds.floatFieldGrp("mbsst1_ccst", l = "Char Cache Start Time:", v1 = dCStartTime, \
                   cc = 'setSingleNumericAttrFieldGrpMiGA(2, "mbsst1_ccst", "'+brainNode+'", "startCTime")', en = False)
    
    cmds.text(l = "")
    cmds.checkBoxGrp("mgtbb_cbg", l = "TBB Parallel Computing", v1 = dTbbEnable, \
                   on1 = 'setSingleNumericAttrSliderGrpMiG(0, "mgtbb_cbg", "'+brainNode+'", "tbbEnable")',\
                   of1 = 'setSingleNumericAttrSliderGrpMiG(0, "mgtbb_cbg", "'+brainNode+'", "tbbEnable")')
    
    cmds.text(l = "")
    cmds.text(l = "Auto Collision Avoidance", fn = "smallBoldLabelFont", align = "left", h = 20)
    cmds.checkBoxGrp("mgaca_cbg", l = "Enable Auto Avoid", v1 = dAutoAvoid, \
                   cc = 'setSingleNumericAttrSliderGrpMiG(0, "mgaca_cbg", "'+globalNode+'", "boolMaster[7]")')
    
    cmds.floatFieldGrp("mgaspd_ffg", l = "Speed(0-1)", v1 = dAvoidSpeed, \
                   cc = 'setSingleNumericAttrFieldGrpMiGA(2, "mgaspd_ffg", "'+globalNode+'", "avdSpd")')
    
    
    cmds.text(l = "")
    cmds.text(l = "Placement Hide", fn = "smallBoldLabelFont", align = "left", h = 20)
    cmds.checkBoxGrp("mgaplchl_cbg", l = "Place from Hide List", v1 = dBoolMaster3, \
                   on1 = 'setSingleNumericAttrSliderGrpMiG(0, "mgaplchl_cbg", "'+globalNode+'", "boolMaster[3]")',\
                   of1 = 'setSingleNumericAttrSliderGrpMiG(0, "mgaplchl_cbg", "'+globalNode+'", "boolMaster[3]")')
    
    
    cmds.text(l = "")
    cmds.text(l = "Decision Node", fn = "smallBoldLabelFont", align = "left", h = 20)
    cmds.checkBoxGrp("mgafsvfi_cbg", l = "Auto Fill Fuzzy Out ", v1 = dBoolMaster0, \
                   on1 = 'setSingleNumericAttrSliderGrpMiG(0, "mgafsvfi_cbg", "'+globalNode+'", "boolMaster[0]")',\
                   of1 = 'setSingleNumericAttrSliderGrpMiG(0, "mgafsvfi_cbg", "'+globalNode+'", "boolMaster[0]")')
    cmds.checkBoxGrp("mgaflavm_cbg", l = "Fuzzy Value Absolute Mode", v1 = dBoolMaster1, \
                   on1 = 'setSingleNumericAttrSliderGrpMiG(0, "mgaflavm_cbg", "'+globalNode+'", "boolMaster[1]")',\
                   of1 = 'setSingleNumericAttrSliderGrpMiG(0, "mgaflavm_cbg", "'+globalNode+'", "boolMaster[1]")')
    
    cmds.setParent("..")

    cmds.text(l = "")
    cmds.text(l = "Mesh Drive Save Block", fn = "smallBoldLabelFont", align = "left", h = 20)
    cmds.checkBoxGrp("mguswdm_cbg", l = "Unlock save with MeshDrive", v1 = dDisableCB, \
                   on1 = 'setSingleNumericAttrSliderGrpMiG(0, "mguswdm_cbg", "'+globalNode+'", "disableCB")',\
                   of1 = 'setSingleNumericAttrSliderGrpMiG(0, "mguswdm_cbg", "'+globalNode+'", "disableCB")')


    cmds.text(l = "")
    cmds.text(l = "Bone Infrastructure Features", fn = "smallBoldLabelFont", align = "left", h = 20)
    cmds.checkBoxGrp("mghcd_cbg", l = "Hook Custom Data", v1 = dHookCD, \
                   on1 = 'setSingleNumericAttrSliderGrpMiG(0, "mghcd_cbg", "'+globalNode+'", "hookCustomData")',\
                   of1 = 'setSingleNumericAttrSliderGrpMiG(0, "mghcd_cbg", "'+globalNode+'", "hookCustomData")')
    cmds.checkBoxGrp("mged_cbg", l = "Enable Joint Scale", v1 = dEnScale, \
                   on1 = 'setSingleNumericAttrSliderGrpMiG(0, "mged_cbg", "'+globalNode+'", "enableScale")',\
                   of1 = 'setSingleNumericAttrSliderGrpMiG(0, "mged_cbg", "'+globalNode+'", "enableScale")')


    cmds.setParent( '..' )
    
    
    cmds.tabLayout( tabs, edit=True, tabLabel=((child0, "Miarmy Global")))
    cmds.showWindow(winName)

def McdRefreshMiarmyGlobal():
    McdMiarmyGlobalGUI()

def McdExitPhysicsGlobal():
    try:
        cmds.deleteUI("McdMiarmyGlobal")
    except:
        pass
























