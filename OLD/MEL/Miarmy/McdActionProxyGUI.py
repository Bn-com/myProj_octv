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
from McdGeneral import *
from McdSimpleCmd import *
from McdActionFunctions import *

if cmds.objExists('Miarmy_Contents'):
    activeAgnt = McdGetActiveAgentName()
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
mainWin='actionProxyGUI'
def McdActionProxyGUI():
    if(cmds.window(mainWin, ex=1)):
        cmds.deleteUI(mainWin)
    cmds.window(mainWin, t='actionProxyUI V 1.0', widthHeight=(400,500))
    cmds.scrollLayout( h=700,w=400, vis=1)
    #load active agent Name
    cmds.separator(h=20,style='none',w=400)
    mainUI=cmds.columnLayout(w=400,cal='center',adj=1)
    mainTab=cmds.tabLayout('mainTLO',imh=5,imw=5,w=400)
    #------------------------------------------------------# end of tabContent1
    cmds.setParent(mainTab)
    tabContent1=cmds.columnLayout(w=400)
    cmds.separator(h=5,style='none',w=400)
    #content
    actionProxyMainUI()
    #------------------------------------------------------# end of tabContent1
    cmds.setParent(mainTab)
    tabContent2=cmds.columnLayout(w=400)
    cmds.separator(h=5,style='none',w=400)
    #content
    #------------------------------------------------------# end of tabContent2
    cmds.tabLayout(mainTab,
        tl=[(tabContent1, 'ACTPRXY'),
            (tabContent2, 'STRYLST'),],e=1)
    #------------------------------------------------------# end Window
    cmds.showWindow(mainWin)
    #------------------------------------------------------# Main Tab

#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def actionProxyMainUI():
    activeAgnt = McdGetActiveAgentName()
    mainUI = cmds.columnLayout(w=400,adj=1)
    cmds.frameLayout(cll=1,cl=0,l="Action Proxy List",w=400,bs="etchedIn")
    actProxyUI = cmds.columnLayout(w=400,adj=1)
    cmds.button (label='Create Action Proxy', bgc=yellowBttn, w=400, h=40, command=lambda x: McdCreateActionProxyCmd())
    cmds.button (label='Select ActionProxyNode', bgc=lightGreyBttn, w=400, h=30, command=lambda x: cmds.select('actionProxy_'+activeAgnt))
    cmds.separator(h=10,style="none",w=400)
    cmds.rowColumnLayout(numberOfColumns=2)
    cmds.button ('actPrxyBttn',label='Enable Proxy', bgc=darkGreyBttn, w=195, h=30,command=lambda x: cmds.setAttr('actionProxy_'+activeAgnt+'.enable',1))
    cmds.button (label='Disable Proxy', bgc=greyBttn, w=200, h=30,command=lambda x: cmds.setAttr('actionProxy_'+activeAgnt+'.enable',0))
    cmds.setParent(actProxyUI)
    cmds.separator(h=5,style='none',w=400)
    RCOL =cmds.rowColumnLayout(numberOfColumns=2)
    ACOL=cmds.columnLayout(w=190,cal='center') # columnA
    loadALLActionNodeUI()
    cmds.setParent(RCOL)
    BCOL=cmds.columnLayout(w=200,cal='center') # columnB
    loadSelectActionNodeUI()
    cmds.setParent(actProxyUI)
    cmds.rowColumnLayout(nc=2,cw=[(1, 260), (2, 130)] )
    cmds.button (label='PLAY/STOP', bgc=redBttn, h=40,command=lambda x: playToggleOnOff())
    cmds.button (label='RESET', bgc=greyBttn, h=40,command=lambda x: mel.eval('playButtonStart'))
#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def loadALLActionNodeUI():
    listAction=[]
    mainUI=cmds.columnLayout(w=195)
    ##
    cmds.frameLayout(cll=1,cl=0,l="List Action Node",w=195,bs="etchedIn")
    #cmds.columnLayout(w=200)
    cmds.separator(h=5,style="none",w=195)
    cmds.button (label='Load Action Agent', bgc=darkGreyBttn,w=195, h=30,al='center',command=lambda x: appendActionListNode('actionsListTxSL',typeAct='action'))
    #select only one at the time
    cmds.textScrollList('actionsListTxSL',w=195,h=300,
                      ams = 0,
                      append=listAction,
                      sc="""import McdActionProxyGUI as myuis \nmyuis.selectItem('actionsListTxSL')""")
    cmds.button (label='>>>>-ADD->>>>', bgc=darkGreyBttn,w=195, h=30,al='center',command=lambda x:addList('actionsListTxSL','proxyListTxSL'))
    cmds.setParent(mainUI)
    cmds.separator(h=20,style="none",w=195)
#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def loadSelectActionNodeUI():
    listAction=[]
    mainUI=cmds.columnLayout(w=195)
    ##
    cmds.frameLayout(cll=1,cl=0,l="List Action Proxy List",w=195,bs="etchedIn")
    #cmds.columnLayout(w=200)
    cmds.separator(h=5,style="none",w=195)
    cmds.button (label='Clear List', bgc=darkGreyBttn,w=195, h=30,al='center',command=lambda x: cmds.textScrollList('proxyListTxSL',e=1,ra=1))
    # allow multiple selecttion
    cmds.textScrollList('proxyListTxSL',w=195,h=300,
                      ams = 1,
                      append=listAction)
    cmds.button (label='<<<<-REMOVE-<<<<', bgc=darkGreyBttn,w=195, h=30,al='center',command=lambda x:removeList('proxyListTxSL'))
    cmds.setParent(mainUI)
    cmds.separator(h=20,style="none",w=195)
#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def appendActionListNode(TxSCL,typeAct='action'):
    #get currect active agent
    activeAgnt = McdGetActiveAgentName()
    optA = cmds.ls(activeAgnt+':'+'Agent_*') # agent reference ex "stand:Agent_loco"
    optB = cmds.ls("*Agent_"+activeAgnt) # agent import with namespace on "stand_Agent_loco"
    if not len(optA)==0:
        nameSpace = optA[0].split(':')[0]
        AgentName = optA[0].split('_')[-1] # get last array
        listAction = cmds.ls(activeAgnt+':'+'*'+typeAct+'_'+AgentName)
    if not len(optB)==0:
        listAction = cmds.ls('*'+typeAct+'_'+activeAgnt)
    #remove all action from textScrollisr first
    cmds.textScrollList(TxSCL,e=1,ra=1)
    #append action
    cmds.textScrollList(TxSCL,e=1,append=listAction)
#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def selectItem(TxSCL):
    obj = cmds.textScrollList(TxSCL,q=1,si=1)[0]
    cmds.select(obj)
#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def addList(list1 ='actionsListTxSL',list2='proxyListTxSL'):
    #add from list1 to list2
    objs = cmds.textScrollList(list1,q=1,si=1)
    cmds.textScrollList(list2,e=1,a=objs)
#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def removeList(TxSCL):
    objs = cmds.textScrollList(TxSCL,q=1,si=1)
    cmds.textScrollList(TxSCL,e=1,ri=objs)
#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def playToggleOnOff():
    state = cmds.play( q=True, state=True )
    if state==0:cmds.play( forward=True )
    if state==1:cmds.play( state=False )
#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////