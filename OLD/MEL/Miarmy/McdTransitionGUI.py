#####################################################################################
#  SCRIPT:
#  AUTHOR: Thanapoom Siripopungul
#  E-MAIL: Thanapooms@gmail.com
#  DATE:
#  2013:

#  REQUAIRED:

#
#####################################################################################

import maya.cmds as cmds
import maya.mel as mel
#miarmy script
from McdAgentManager import *
from McdGeneral import *
from McdSimpleCmd import *
from McdActionFunctions import *
#import McdMainGUI
#reload(McdMainGUI)
#from McdMainGUI import *

if cmds.objExists('Miarmy_Contents'):
    activeAgnt = McdGetActiveAgentName()
    listAgents =McdGetAllAgentTypeNIDWithColor()[0]
    globalNode = McdGetMcdGlobalNode()
    #incase active agent not in scene, we need to force change active agent to another one to provide error
    if not activeAgnt in listAgents:
        # force assign active to first agent
        cmds.setAttr(globalNode + ".activeAgentName", listAgents[0], type = "string")
else:
    activeAgnt =''
#note for button color
yellowBttn = [0.8,0.7,0.3]
redBttn  = [0.6,0.3,0.3]
greenBttn  = [0.3,0.6,0.3]
cyanBttn = [0.3,0.5,0.6]
greyBttn = [0.5,0.5,0.5]
darkGreyBttn = [0.4,0.4,0.4]
lightGreyBttn = [0.6,0.6,0.6]

#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
mainWin='transitionGUI'
def McdTransitionGUI():
    if(cmds.window(mainWin, ex=1)):
        cmds.deleteUI(mainWin)
    cmds.window(mainWin, t='actionUI V 1.1', widthHeight=(400,500))
    cmds.scrollLayout( h=700,w=400, vis=1)
    #load active agent Name
    cmds.separator(h=20,style='none',w=400)
    mainUI=cmds.columnLayout(w=400,adj=1)
    #content
    transitionUI()
    cmds.setParent(mainUI)
    cmds.showWindow(mainWin)
    #------------------------------------------------------# Main Tab
#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def transitionUI():
    #cmds.scrollLayout(h=520, w=400, vis=1)
    globalNode = McdListMcdGlobal()
    EnableSimple = cmds.getAttr(globalNode + ".smpTrans")
    if EnableSimple ==1: bttnColor = redBttn
    if EnableSimple ==0: bttnColor = greyBttn
    listAction=[]
    mainUI=cmds.columnLayout(w=400,adj=1)
    cmds.frameLayout(cll=1,cl=0,l="Transition Map",w=400,bs="etchedIn")
    cmds.columnLayout(w=400,adj=1)
    cmds.separator(h=10,style="none",w=400)
    cmds.rowColumnLayout(numberOfColumns=2)
    cmds.button ("simTransBttn",label='Enable Simple Transition', bgc= bttnColor, w=200, h=30 ,command=lambda x:enableSimpleTrans(1))
    cmds.button (label='Disable Simple Transition', bgc=greyBttn, w=200, h=30,command=lambda x:enableSimpleTrans(0))
    cmds.setParent('..')
    cmds.button (label='Move Tool', bgc= yellowBttn, w=400, h=30, command=lambda x: McdStateContextToolOn())
    cmds.rowColumnLayout(numberOfColumns=2)
    cmds.button (label='Create State', bgc= greyBttn, w=200, h=30, command=lambda x: McdCreateStateCmd())
    cmds.button (label='Create Action Shell', bgc=greyBttn, w=200, h=30, command=lambda x: McdCreateActionShellCmd())
    cmds.button (label='Add/Edit Action Group', bgc=greyBttn, w=200, h=30, command=lambda x: McdAssignActionGrp())
    cmds.button (label='Cancel Action Group', bgc=greyBttn, w=200, h=30, command=lambda x: McdCancelActionGrp())
    cmds.setParent(mainUI)
    stateFLO = cmds.frameLayout(cll=1,cl=0,l="List  state Node",w=400,bs="etchedIn")
    tranRCLO = cmds.rowColumnLayout(nc=2,cw =[(1, 200), (2,200)])
    cmds.button (label='Load state Node ', bgc=darkGreyBttn,w=200, h=30,al='center',command=lambda x: appendListNode('stateNodeTxSL',typeAct='state'))
    cmds.button (label='CLEAR ', bgc=darkGreyBttn,w=200, h=30,al='center',command=lambda x: removeAllListNode('stateNodeTxSL'))
    cmds.setParent(stateFLO)
    cmds.textScrollList('stateNodeTxSL',w=400,h=80,ams = 0,append=listAction)
    stateCnxRCLO = cmds.rowColumnLayout(nc=2,cw =[(1, 200), (2,200)])
    cmds.button (label='Connect To State', bgc=darkGreyBttn, w=200, h=30,command=lambda x:connectToState())
    cmds.button (label='', bgc=darkGreyBttn, w=200, h=30)
    cmds.setParent(mainUI)
    tranFLO = cmds.frameLayout(cll=1,cl=0,l="List  Node",w=400,bs="etchedIn")
    tranRCLO = cmds.rowColumnLayout(nc=2,cw =[(1, 200), (2,195)])
    COLA = cmds.columnLayout(w=200,adj=1)
    cmds.setParent(tranRCLO)
    COLB = cmds.columnLayout(w=195,adj=1)
    cmds.setParent(COLA)
    cmds.separator(h=5,style="none",w=200)
    cmds.button (label='Load Actions Node ', bgc=darkGreyBttn,w=200, h=30,al='center',command=lambda x: appendListNode('actNodeTxSL',typeAct='action'))
    cmds.button (label='CLEAR ', bgc=darkGreyBttn,w=200, h=30,al='center',command=lambda x: removeAllListNode('actNodeTxSL'))

    cmds.textScrollList('actNodeTxSL',w=200,h=320,ams = 1,append=listAction)
    cmds.setParent(COLB)
    cmds.separator(h=5,style="none",w=200)
    cmds.button (label='Load ActionShell' , bgc=darkGreyBttn,w=200, h=30,al='center',command=lambda x: appendListNode('tranNodeTxSL',typeAct='actionShell'))
    cmds.button (label='CLEAR ' , bgc=darkGreyBttn,w=200, h=30,al='center',command=lambda x: removeAllListNode('tranNodeTxSL'))

    cmds.textScrollList('tranNodeTxSL',w=175,h=320,ams = 1,append=listAction)
    cmds.separator(h=5,style="none",w=200)
    cmds.setParent(tranFLO)
    cmds.rowColumnLayout(nc=2)
    cmds.button (label='Create Multiple Action Shell', bgc=greyBttn, w=200, h=30,command=lambda x:createMultiActionShell())
    cmds.button (label='Create Multiple Action Group', bgc=greyBttn, w=200, h=30,command=lambda x:createMultiActionGroup())
    cmds.button (label='remove Multiple Action Group', bgc=greyBttn, w=200, h=30,command=lambda x:removeMultiActionGroup())
    cmds.button (label='', bgc=greyBttn, w=200, h=30)

    cmds.setParent(mainUI)
    cmds.separator(h=5,style="none",w=400)
    #auto Add action into shell list
    appendListNode('actNodeTxSL',typeAct='action')
    appendListNode('tranNodeTxSL',typeAct='actionShell')
    appendListNode('stateNodeTxSL',typeAct='state')
#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def appendListNode(TxSCL,typeAct='action'):

    if cmds.objExists('Miarmy_Contents'):
        #get currect active agent
        activeAgnt = McdGetActiveAgentName()
        # get realName of agent and agentwithor without nameSpace
        agentInfo = getAgentRealName()
        realName = agentInfo[0]
        agentWithNameSpace = agentInfo[1]
        if agentWithNameSpace ==1:
            listAction = cmds.ls(activeAgnt+':'+'*'+typeAct+'_'+realName)
        if agentWithNameSpace ==0:
            listAction = cmds.ls('*'+typeAct+'_'+realName)
    else:
        activeAgnt =''
        listAction =[]
    #remove all action from textScrollisr first
    cmds.textScrollList(TxSCL,e=1,ra=1)
    #append action
    cmds.textScrollList(TxSCL,e=1,append=listAction)

#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def getAgentRealName():
    activeAgnt = McdGetActiveAgentName()
    """ use for realname when agent has nameSpace on
    return
    -RealName and
    -withNameSpace 1 is true  0 in false
    """
    activeAgnt = McdGetActiveAgentName()
    optA = cmds.ls(activeAgnt+':'+'Agent_*') # agent reference ex "stand:Agent_loco"
    optB = cmds.ls("*Agent_"+activeAgnt) # agent import with namespace on "stand_Agent_loco"
    if not len(optA)==0:
        agentWithNameSpace =1 # True
        nameSpace = optA[0].split(':')[0]
        realAgentName = optA[0].split('_')[-1] # get last array
    if not len(optB)==0:
        agentWithNameSpace =0 # False
        realAgentName = activeAgnt
    listName = [realAgentName,agentWithNameSpace]
    return listName
#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def createMultiActionShell():
    list = cmds.textScrollList('actNodeTxSL',q=1,si=1)
    activeAgentName = McdGetActiveAgentName()
    for act in list:
        #getName of action
        newAction = act.split('_action_')[0]
        A = McdGetOrCreateActionShellGrp(activeAgentName, 1)
        McdCreateAction(newAction, activeAgentName)
#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def createMultiActionGroup():
    listActionShell = cmds.textScrollList('tranNodeTxSL',q=1,si=1)
    optionActShell = cmds.promptDialog(t="Action shell Group",m = "Specify the action group name: ", \
                                                button = ["Assign", "Cancel"],\
                                                defaultButton = "Assign", cancelButton = "Cancel", \
                                                dismissString = "Cancel")
    if optionActShell == "Assign":
        newAction = cmds.promptDialog(query=True, text=True)
    for obj in listActionShell:
        cmds.setAttr(obj + ".group", newAction, type = "string")
#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def removeMultiActionGroup():
    listActionShell = cmds.textScrollList('tranNodeTxSL',q=1,si=1)
    for obj in listActionShell:
        cmds.setAttr(obj + ".group", "", type = "string")
#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def removeAllListNode(TxSCL):
    cmds.textScrollList(TxSCL,e=1,ra=1)

#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def enableSimpleTrans(value):
    globalNode = McdListMcdGlobal()
    if value==1:
        reverseValue=0
        #change color when cache turn on
        cmds.button ('simTransBttn',e=1, bgc=redBttn)
    if value==0:
        reverseValue=1
        #change color when cache turn off
        cmds.button ('simTransBttn',e=1, bgc=greyBttn)
    cmds.setAttr(globalNode + '.smpTrans', value) #1 or 0

#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def connectToState():
    import pymel.core as pm
    state = cmds.textScrollList('stateNodeTxSL',q=1,si=1)[0]
    actShell = cmds.textScrollList('tranNodeTxSL',q=1,si=1)
    # connect
    for o in actShell:
        cmds.connectAttr(state+'.exitAction',o+'.input',f=1)
        i = 0
        destArray = pm.Attribute(state+'.entryAction')
        srcAttr = pm.Attribute(o+'.output')
        while True:
            destAttr = destArray[i]
            #print "checking:", destAttr
            if not destAttr.inputs():
                #print "   ...it had no inputs!"
                pm.connectAttr(srcAttr, destAttr)
                break
            i += 1
#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def disconnectToState():
    """
    still not 100% function cause cycleLoop in some case
    """
    import pymel.core as pm
    state = cmds.textScrollList('stateNodeTxSL',q=1,si=1)[0]
    actShell = cmds.textScrollList('tranNodeTxSL',q=1,si=1)
    #disconnect
    for o in actShell:
        if  pm.isConnected(state+'.exitAction',o+'.input'):
            pm.disconnectAttr(state+'.exitAction',o+'.input')
        """
        i = 0
        destArray = pm.Attribute(state+'.entryAction')
        srcAttr = pm.Attribute(o+'.output')
        while True:
            destAttr = destArray[i]
            #print "checking:", destAttr
            if  pm.isConnected(srcAttr,destAttr):
                pm.disconnectAttr(srcAttr,destAttr)
                break
            i += 1
        """
#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////