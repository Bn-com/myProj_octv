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

import McdAgentManager
reload(McdAgentManager)
from McdAgentManager import *


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

mainWin='agentManagerGUI'

def McdAgentManagerGUI():

    if(cmds.window(mainWin, ex=1)):
        cmds.deleteUI(mainWin)
    cmds.window(mainWin, t='agentManagerUI V 1.0', widthHeight=(400,500))
    cmds.scrollLayout( h=350,w=410, vis=1)
    #load active agent Name
    cmds.separator(h=20,style='none',w=400)
    mainUI=cmds.columnLayout(w=400,cal='center',adj=1)
    mainTab=cmds.tabLayout('mainTLO',imh=5,imw=5,w=400)
    cmds.setParent(mainTab)
    tabContent1=cmds.columnLayout(w=400)
    cmds.separator(h=5,style='none',w=400)
    #content
    agentManagerUI(TFGrp='activeAgentStdAlneTFGrp',TxSCL ='agentStdAlneTxSL')
    #------------------------------------------------------# end of tabContent1
    cmds.setParent(mainTab)
    tabContent2=cmds.columnLayout(w=400)
    cmds.separator(h=5,style='none',w=400)
    #content
    tipsUI()
    #------------------------------------------------------# end of tabContent2
    cmds.tabLayout(mainTab,
        tl=[(tabContent1, 'AGENT'),
            (tabContent2, 'TipS'),],e=1)
    #------------------------------------------------------# end Window
    cmds.showWindow(mainWin)
    #------------------------------------------------------# Main Tab

#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////

def agentManagerUI(TFGrp='activeAgentTFGrp',TxSCL ='agentTxSL'):

    #check miarmy_content first
    if cmds.objExists('Miarmy_Contents'):
        listAgents = McdGetAllAgentTypeNIDWithColor()[0]
        activeAgnt = McdGetActiveAgentName()
        globalNode = McdGetMcdGlobalNode()
        #incase active agent not in scene, we need to force change active agent to another one to provide error
        if not activeAgnt in listAgents:
            # force assign active to first agent
            cmds.setAttr(globalNode + ".activeAgentName", listAgents[0], type = "string")
        clr = getClrIDActiveAgent()
    else:
        activeAgnt =''
        clr = 0
        listAgents =[]
    mainUI=cmds.columnLayout(w=400,cal='center',adj=1)
    cmds.separator(h=10,style="none",w=400)
    cmds.textFieldGrp(TFGrp,text= activeAgnt,cw2=(100, 250),cal=(1,'left'),l='   ActiveAgent',bgc=setColorOfDraw(clr))

    cmds.separator(h=10,style="none",w=400)
    ##
    cmds.frameLayout(cll=1,cl=1,l="Agent list" ,w=400,bs="etchedIn")
    agentCOL = cmds.columnLayout(w=400,adj=1)
    RCOL =cmds.rowColumnLayout(numberOfColumns=2)
    ACOL=cmds.columnLayout(w=190,cal='center') # columnA
    cmds.rowColumnLayout( w=200,h=150, vis=1)
    cmds.textScrollList(TxSCL,w=150,h=150, ams = 0,append=listAgents,sc="""import McdAgentManagerGUI as agent\nreload(agent)\nagent.activeAgent('"""+TFGrp+"""','"""+TxSCL+"""')""")
    cmds.setParent(RCOL)
    BCOL=cmds.columnLayout(w=200,cal='center') # columnB
    cmds.button (label='Add AGENT',bgc=darkGreyBttn, w=200, h=30,command=lambda x:addAgent(TxSCL))
    cmds.button (label='Modify AGENT',bgc=darkGreyBttn, w=200, h=30,command=lambda x:modifyAgent(TFGrp,TxSCL))
    cmds.button (label='Remove AGENT',bgc=darkGreyBttn, w=200, h=30,command=lambda x:removeAgent(TxSCL))
    cmds.button (label='reload Active Agent', bgc=darkGreyBttn, w=200, h=30, command=lambda x: reloadActiveAgent(TFGrp,TxSCL))

    cmds.setParent(agentCOL)
    cmds.separator(h=10,style="none",w=400)
    cmds.rowColumnLayout(nc = 15, cw = [(1,22),(2,22),(3,22),(4,22),(5,22),(6,22),(7,22),(8,22),\
                                      (9,22),(10,22),(11,22),(12,22),(13,22),(14,22),(15,22)])
    cmds.button(l = "", bgc = setColorOfDraw(0),c=lambda x:updateAgentClr(0,TFGrp))
    cmds.button(l = "", bgc = setColorOfDraw(1),c=lambda x:updateAgentClr(1,TFGrp))
    cmds.button(l = "", bgc = setColorOfDraw(2),c=lambda x:updateAgentClr(2,TFGrp))
    cmds.button(l = "", bgc = setColorOfDraw(3),c=lambda x:updateAgentClr(3,TFGrp))
    cmds.button(l = "", bgc = setColorOfDraw(4),c=lambda x:updateAgentClr(4,TFGrp))
    cmds.button(l = "", bgc = setColorOfDraw(5),c=lambda x:updateAgentClr(5,TFGrp))
    cmds.button(l = "", bgc = setColorOfDraw(6),c=lambda x:updateAgentClr(6,TFGrp))
    cmds.button(l = "", bgc = setColorOfDraw(7),c=lambda x:updateAgentClr(7,TFGrp))
    cmds.button(l = "", bgc = setColorOfDraw(8),c=lambda x:updateAgentClr(8,TFGrp))
    cmds.button(l = "", bgc = setColorOfDraw(9),c=lambda x:updateAgentClr(9,TFGrp))
    cmds.button(l = "", bgc = setColorOfDraw(10),c=lambda x:updateAgentClr(10,TFGrp))
    cmds.button(l = "", bgc = setColorOfDraw(11),c=lambda x:updateAgentClr(11,TFGrp))
    cmds.button(l = "", bgc = setColorOfDraw(12),c=lambda x:updateAgentClr(12,TFGrp))
    cmds.button(l = "", bgc = setColorOfDraw(13),c=lambda x:updateAgentClr(13,TFGrp))
    cmds.button(l = "", bgc = setColorOfDraw(14),c=lambda x:updateAgentClr(14,TFGrp))

    cmds.setParent(mainUI)
    cmds.separator(h=10,style="none",w=400)
#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def tipsUI():
    cmds.columnLayout(adj = True)
    cmds.text(l = "* List all the agents in scene", fn = "smallBoldLabelFont", align = "left")
    cmds.text(l = "      Agent: children groups of \"Miarmy_Contents\"", align = "left")
    cmds.text(l = '      Naming Convention: Agent_<agentName>' , align = "left")
    cmds.text(l = '      Attribute: each group has "colorID", "agentID" attribute.' , align = "left")
    cmds.text(l = "")
    cmds.text(l = "* Agents Manager Functions", fn = "smallBoldLabelFont", align = "left")
    cmds.text(l = "      Create, modify, delete agents group", align = "left")
    cmds.separator(h = 10)
    cmds.button(l = "Check detailed help")
    cmds.setParent( '..' )

#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def activeAgent(TFGrp,TxSCL):
    globalNode = McdGetMcdGlobalNode()
    agentName = cmds.textScrollList(TxSCL,q=1,si=1)[0]
    cmds.setAttr(globalNode + ".activeAgentName", agentName, type = "string")
    #getIndexClor
    clr = getClrIDActiveAgent()
    #update textFiledGrp
    cmds.textFieldGrp(TFGrp,e=1,tx= agentName,bgc=setColorOfDraw(clr))
#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def reloadActiveAgent(TFGrp,TxSCL):

    #remove all agent in list
    cmds.textScrollList(TxSCL,e=1,ra=1)
    #list all agent
    listAgents =McdGetAllAgentTypeNIDWithColor()[0]
    cmds.textScrollList(TxSCL,e=1,append=listAgents)
    # find active agent
    clr = getClrIDActiveAgent() #getIndexClor
    activeAgnt = McdGetActiveAgentName()
    cmds.textFieldGrp(TFGrp,e=1,tx= activeAgnt,bgc=setColorOfDraw(clr))


#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def updateAgentClr(index,TFGrp):

    cmds.textFieldGrp(TFGrp,e=1,bgc=setColorOfDraw(index))
    activeAgnt = McdGetActiveAgentName()
    # there are 3 possibility
    optA = cmds.ls(activeAgnt+':'+'Agent_*') # agent reference ex "stand:Agent_loco"
    optB = cmds.ls("*Agent_"+activeAgnt) # agent import with namespace on "stand_Agent_loco" or "Agent_loco"
    # get color ID of active agent
    if not len(optA)==0:
        index = cmds.setAttr(optA[0]+".colorId", index)
    if not len(optB)==0:
        index = cmds.setAttr(optB[0]+".colorId", index)
    #cmds.setAttr("Agent_" + aaName + ".colorId", index)
#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def addAgent(TxSCL):
    #remove all agent in list
    McdAddAgentGroup()
    cmds.textScrollList(TxSCL,e=1,ra=1)
    #list all agent
    listAgents =McdGetAllAgentTypeNIDWithColor()[0]
    cmds.textScrollList(TxSCL,e=1,append=listAgents)
#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def removeAgent(TxSCL):
    agentName = cmds.textScrollList(TxSCL,q=1,si=1)[0]
    stat = cmds.confirmDialog(t = "Delete Agent?", m = "Are you sure to delete agent?",
        button=['Yes','No'], defaultButton='Yes', cancelButton='No', dismissString='No' )
    if stat != 'Yes':
        return
    cmds.delete('Agent_'+agentName)
    cmds.textScrollList(TxSCL,e=1,ri=agentName)
#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def modifyAgent(TFGrp,TxSCL):
    #get index from list
    #getAgent Name
    agentName = cmds.textScrollList(TxSCL,q=1,si=1)[0]
    AM_Mod(agentName)
    reloadActiveAgent(TFGrp,TxSCL)
#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def McdRefreshAgentManager():
    McdAgentManagerGUI()
#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def McdExitAgentManager():
    try:
        cmds.deleteUI("McdAgentManager")
    except:
        pass
#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
