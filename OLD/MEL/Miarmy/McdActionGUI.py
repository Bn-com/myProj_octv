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
import McdMainGUI
reload(McdMainGUI)
from McdMainGUI import *

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
mainWin='actionGUI'
def McdActionGUI():
    if(cmds.window(mainWin, ex=1)):
        cmds.deleteUI(mainWin)
    cmds.window(mainWin, t='actionUI V 1.1', widthHeight=(400,500))
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
    actionMainUI()
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
def actionMainUI():
    textFieldName = 'ActionProxyNode'
    #activeAgnt = McdGetActiveAgentName()
    mainUI = cmds.columnLayout(w=400,adj=1)
    cmds.frameLayout(cll=1,cl=0,l="Action Main UI",w=400,bs="etchedIn")
    actUI = cmds.columnLayout(w=400,adj=1)

    actFLO = cmds.frameLayout(cll=1,cl=0,l="create Action Node",w=400,bs="etchedIn")
    cmds.rowColumnLayout(numberOfColumns=3)
    cmds.button (label='Create Action', bgc= yellowBttn, w=133, h=30, command=lambda x: McdCreateActionCmd())
    cmds.button (label='Create Action Proxy', bgc=yellowBttn, w=133, h=40, command=lambda x: McdCreateActionProxyCmd())
    cmds.button (label='Create Story List', bgc=yellowBttn, w=133, h=30, command=lambda x: McdCreateStoryListCmd())
    cmds.setParent(actFLO)
    cmds.rowColumnLayout(numberOfColumns=2)
    cmds.button (label='Action Editor', bgc= greyBttn, w=200, h=30, command=lambda x: McdActionEditorGUI())
    cmds.button (label='Story List Editor', bgc=greyBttn, w=200, h=30, command=lambda x: McdStoryListEditorGUI())
    cmds.setParent(actFLO)
    #cmds.separator(h=10,style='none',w=300)
    cmds.text(l='Note : Action ProxyList not work on Agent with NameSpace')
    #cmds.separator(h=10,style='none',w=300)
    cmds.rowColumnLayout(numberOfColumns=2)
    cmds.button (label='Select ActionProxyNode', bgc=yellowBttn, w=195, h=30, command=lambda x: selectAndUpdateProxyNode(textFieldName,'proxyListTxSL'))
    cmds.textField(textFieldName,ed=1,w=200,h=25)
    # action editor
    cmds.setParent(actUI)
    actionEditorUI()
    cmds.popupMenu('proxyPOP',p=textFieldName)
    cmds.menuItem(c=lambda *args: cmds.textField(textFieldName,e=1,tx='',ed=1),l='clear')


    cmds.separator(h=5,style='none',w=400)
    RCOL =cmds.rowColumnLayout(numberOfColumns=2)
    ACOL=cmds.columnLayout(w=190,cal='center') # columnA
    loadALLActionNodeUI()
    cmds.setParent(RCOL)
    BCOL=cmds.columnLayout(w=200,cal='center') # columnB
    proxyListUI()
    cmds.setParent(actUI)

#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def loadALLActionNodeUI():
    listAction=[]
    mainUI=cmds.columnLayout(w=195,adj=1)
    ##
    cmds.frameLayout(cll=1,cl=0,l="List Action Node",bs="etchedIn")
    #cmds.columnLayout(w=200)
    cmds.separator(h=5,style="none",w=195)
    cmds.button (label='Load Action Agent', bgc=darkGreyBttn,w=195, h=30,al='center',command=lambda x: appendActionListNode('actionsListTxSL',typeAct='action'))
    #select only one at the time
    cmds.textScrollList('actionsListTxSL',h=320,
                      ams = 0,
                      append=listAction,
                      sc="""import McdActionGUI as myuis \nmyuis.selectItem('actionsListTxSL')""")

    cmds.setParent(mainUI)
    cmds.separator(h=10,style="none",w=195)
    #autoAdd action node
    appendActionListNode('actionsListTxSL',typeAct='action')
#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def actionEditorUI():
    listAction=[]
    mainUI=cmds.columnLayout(w=400)
    ##
    cmds.frameLayout(cll=1,cl=1,l="Action Editor ",w=400,bs="etchedIn")
    actEdUI = cmds.columnLayout(w=400,adj =1)
    cmds.separator(h=5,style="none",w=400)
    infoCOL =cmds.rowColumnLayout(nc=3,cw =[(1, 80), (2,180), (3, 130)])
    cmds.text(l='Agent Name')
    cmds.text(l='Action Node')
    cmds.text(l='Action Name')
    cmds.textField('agentNameTFGrp',text= activeAgnt,ed=0)
    cmds.textField('actNodeTFGrp',text= '',ed=0)
    cmds.textField('actNameTFGrp',text= '',ed=0)
    cmds.separator(h=5,style="none",w=400)
    cmds.setParent(actEdUI)
    RCOL =cmds.rowColumnLayout(nc=4,cw =[(1, 60), (2,80), (3, 190),(4,70)])
    ACOL=cmds.columnLayout(w=60,cal='center') # columnA
    cmds.checkBox('isFinalCB', l = "IsFinal",cc=lambda x:setIsFinal())
    cmds.checkBox('isCycleCB', l = "IsCycle",cc=lambda x:setIsCycle())
    cmds.checkBox('matchNameCB', l = "MatchName",cc=lambda x:setMatchName())
    cmds.setParent(RCOL)
    BCOL=cmds.columnLayout(w=80,adj=1) # columnB
    cmds.intFieldGrp('lengthIntFG', nf=1,cw=[(1,40),(2,40)], label='Length', en=0,v1 =0)
    cmds.floatFieldGrp('rateFG', nf=1,cw=[(1,40),(2,40)],  label='Rate',  v1=1,cc=lambda x:setRate())
    cmds.intFieldGrp('frameTotalFFGrp', nf=1,cw=[(1,40),(2,40)], label='Total Fr.', en=0, v1 =0)
    cmds.setParent(RCOL)
    CCOL=cmds.columnLayout(w=185,cal='center') # columnC
    cmds.floatSliderGrp('CycleFSLGrp', l='Cycle %',cw3=(50,40,90),field=True, min=-0, max=100.0, fmn=0, fmx=100.0, value=0 ,cc=lambda x:setCycleFilter())
    cmds.floatSliderGrp('entryFSLGrp', l='Entry %',cw3=(50,40,90),field=True, min=-0, max=100.0, fmn=0, fmx=100.0, value=0 ,cc=lambda x:setEntryRange())
    cmds.floatSliderGrp('exitFSLGrp', l='Exit %',cw3=(50,40,90),field=True, min=-0, max=100.0, fmn=0, fmx=100.0, value=0 ,cc=lambda x:setExitRange())
    cmds.setParent(RCOL)
    DCOL=cmds.columnLayout(w=70,cal='center') # columnD
    cmds.intFieldGrp('frameCycleFFGrp', nf=1,cw=[(1,30),(2,40)], label='F', en=0, v1 =0)
    cmds.intFieldGrp('frameEntryFFGrp', nf=1,cw=[(1,30),(2,40)],  label='F',en=0, v1=0)
    cmds.intFieldGrp('frameExitFFGrp', nf=1,cw=[(1,30),(2,40)],  label='F', en=0, v1=0)
    cmds.setParent(actEdUI)
    entryRandRCOL =cmds.rowColumnLayout(nc=2,cw =[(1, 140), (2,260)])
    cmds.floatFieldGrp('entryRand1FG', nf=1,cw=[(1,100),(2,40)],  label='Entry Random',  v1=1,cc=lambda x:setEntryRandA())
    cmds.floatFieldGrp('entryRand2FG', nf=1,cw=[(1,50),(2,40)],  label='to',  v1=1,cc=lambda x:setEntryRandB())
    cmds.setParent(actEdUI)
    cmds.frameLayout(cll=1,cl=1,l="Exit Action  ",w=400,bs="etchedIn")
    extCOL =cmds.rowColumnLayout(nc=3,cw =[(1, 200), (2,100), (3, 100)])
    cmds.textFieldGrp("exitActA",text= '',cw2=(80, 120),cal=(1,'left'),l='Exit Action',cc=lambda x:setExitChoicesA())
    cmds.intFieldGrp('startFrameA', nf=1,cw=[(1,60),(2,40)], label='start',v1 =0,cc=lambda x:setExitStartFrameA())
    cmds.intFieldGrp('endFrameA', nf=1,cw=[(1,40),(2,60)], label='end',v1 =0,cc=lambda x:setExitEndFrameA())
    cmds.textFieldGrp("exitActB",text= '',cw2=(80, 120),cal=(1,'left'),l='Exit Action',cc=lambda x:setExitChoicesB())
    cmds.intFieldGrp('startFrameB', nf=1,cw=[(1,60),(2,40)], label='start',v1 =0,cc=lambda x:setExitStartFrameB())
    cmds.intFieldGrp('endFrameB', nf=1,cw=[(1,40),(2,60)], label='end',v1 =0,cc=lambda x:setExitEndFrameB())
    cmds.textFieldGrp("exitActC",text= '',cw2=(80, 120),cal=(1,'left'),l='Exit Action',cc=lambda x:setExitChoicesC())
    cmds.intFieldGrp('startFrameC', nf=1,cw=[(1,60),(2,40)], label='start',v1 =0,cc=lambda x:setExitStartFrameC())
    cmds.intFieldGrp('endFrameC', nf=1,cw=[(1,40),(2,60)], label='end',v1 =0,cc=lambda x:setExitEndFrameC())
    cmds.textFieldGrp("exitActD",text= '',cw2=(80, 120),cal=(1,'left'),l='Exit Action',cc=lambda x:setExitChoicesD())
    cmds.intFieldGrp('startFrameD', nf=1,cw=[(1,60),(2,40)], label='start',v1 =0,cc=lambda x:setExitStartFrameD())
    cmds.intFieldGrp('endFrameD', nf=1,cw=[(1,40),(2,60)], label='end',v1 =0,cc=lambda x:setExitEndFrameD())
    cmds.setParent(mainUI)
    cmds.separator(h=10,style="none",w=400)
#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def proxyListUI():

    #get actionProxyNode
    dcNode = getActionProxyNode ()
    if not dcNode =='':
        val = cmds.getAttr(dcNode +'.enable')
        if val ==1:
            color = redBttn
        else :
            color = greyBttn
    if dcNode =='':
        color = greyBttn
    listAction=[]
    mainUI=cmds.columnLayout(w=195)
    ##
    cmds.frameLayout(cll=1,cl=0,l="List Action Proxy List",w=195,bs="etchedIn")
    #cmds.columnLayout(w=200)
    cmds.separator(h=5,style="none",w=195)
    cmds.button (label='Clear List', bgc=darkGreyBttn,w=195, h=30,al='center',command=lambda x: clearList('proxyListTxSL'))
    # allow multiple selecttion
    cmds.textScrollList('proxyListTxSL',w=195,h=170,
                      ams = 0,
                      append=listAction,
                      sc="""import McdActionGUI as myuis \nmyuis.selectItem('proxyListTxSL',selObj=0)""")
    cmds.button (label='>>>>-ADD->>>>', bgc=darkGreyBttn,w=100, h=30,al='center',command=lambda x:addList('actionsListTxSL','proxyListTxSL'))
    cmds.button (label='<<<<-REMOVE-<<<<', bgc=darkGreyBttn,w=100, h=30,al='center',command=lambda x:removeList('proxyListTxSL'))

    cmds.rowColumnLayout(numberOfColumns=2)
    cmds.button (label='UP', bgc=darkGreyBttn,w=100, h=30,al='center',command=lambda x:moveUp('proxyListTxSL'))
    cmds.button (label='DN', bgc=darkGreyBttn,w=100, h=30,al='center',command=lambda x:moveDn('proxyListTxSL'))


    cmds.button ('actPrxyBttn',label='Enable Proxy', bgc=color, w=100, h=30,command=lambda x:enableActionProxy(1) )
    cmds.button (label='Disable Proxy', bgc=greyBttn, w=100, h=30,command=lambda x:enableActionProxy(0) )

    cmds.setParent(mainUI)
    cmds.separator(h=10,style="none",w=195)
    # update proxyList
    updateProxyNodeByDefault('proxyListTxSL')
#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def enableActionProxy(on=1):
    #check MiarmyContent first
    if cmds.objExists('Miarmy_Contents'):
        #get currect active agent
        activeAgnt = McdGetActiveAgentName()
        cmds.setAttr('actionProxy_'+activeAgnt+'.enable',on)
    if on == 1:
        cmds.button ('actPrxyBttn',e=1,bgc = redBttn)
    if on == 0:
        cmds.button ('actPrxyBttn',e=1,bgc = greyBttn)
#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def appendActionListNode(TxSCL,typeAct='action'):
    #check MiarmyContent first
    if cmds.objExists('Miarmy_Contents'):
        #get currect active agent
        activeAgnt = McdGetActiveAgentName()
        agentInfo = getAgentRealName()
        agentWithNameSpace = agentInfo[1]
        AgentName = agentInfo[0]
        if agentWithNameSpace==1:
            listAction = cmds.ls(activeAgnt+':'+'*'+typeAct+'_'+AgentName)
        if agentWithNameSpace==0:
            listAction = cmds.ls('*'+typeAct+'_'+AgentName)
        #remove all action from textScrollisr first
        cmds.textScrollList(TxSCL,e=1,ra=1)
        #append action
        cmds.textScrollList(TxSCL,e=1,append=listAction)
    else:
        cmds.textScrollList(TxSCL,e=1,ra=1)
#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def selectItem(TxSCL,selObj=1):
    #find out that agent has nameSpace or not
    agentInfo = getAgentRealName()
    agentWithNameSpace = agentInfo[1]
    obj = cmds.textScrollList(TxSCL,q=1,si=1)[0]
    if selObj==1:
        cmds.select(obj)
    #update into action Editor info
    #update actNode
    cmds.textField('actNodeTFGrp',e=1,ed=0,tx=obj)
    #update actName

    if agentWithNameSpace==1:
        prefix =obj.split('_')[-3]
        actName = prefix.split(':')[-1]
    if agentWithNameSpace==0:
        actName =obj.split('_')[-3]
    cmds.textField('actNameTFGrp',e=1,ed=0,tx=actName)
    updateActEditorInfo(obj)

#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def addList(list1 ='actionsListTxSL',list2='proxyListTxSL'):
    #add from list1 to list2
    objs = cmds.textScrollList(list1,q=1,si=1)
    cmds.textScrollList(list2,e=1,a=objs)
    updateProxyList(list2)
#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def removeList(TxSCL):
    #need to remove by index , remove by name not stable
    index = cmds.textScrollList(TxSCL,q=1,sii=1)
    #need to remove high index first use for multipleselection
    #index.reverse()
    cmds.textScrollList(TxSCL,e=1,rii=index)
    updateProxyList(TxSCL)
#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def clearList(TxSCL):
    #need all list
    cmds.textScrollList(TxSCL,e=1,ra=1)
    #update
    updateProxyList(TxSCL)

#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def selectAndUpdateProxyNode(TSL,TxSL):
    activeAgnt = McdGetActiveAgentName()
    dcNode = getActionProxyNode ()
    #check actionProxy Node
    if dcNode =='':
        cmds.confirmDialog(t = "ActionProxy Node Not Exists", m = "ActionProxy Node Not Exists, Please Create ActionProxy firsts.")
        cmds.textField (TSL, e=1, ed=1,text= '')
        raise Exception("Create ActionProxy firsts.")
    cmds.select(dcNode)
    selObj = cmds.ls(sl = 1)
    #isAct = 0
    if selObj != [] and selObj != None:
        if cmds.nodeType(dcNode) == "McdActionProxy" :
            cmds.textField (TSL, e=1, ed=0,text= dcNode)
    else:
        cmds.textField (TSL, e=1, ed=1,text= '')
    #append to proxyScrollList
    updateProxyNodeByDefault(TxSL)
#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def updateProxyNodeByDefault(TxSL):
    if cmds.objExists('Miarmy_Contents'):
        activeAgnt = McdGetActiveAgentName()
        dcNode = getActionProxyNode ()
        #append to proxyScrollList
        playlist = []
        # only have actionProxy in scene , if no actionProxy return nothing
        if not dcNode == '':
            for i in range(50):
                stri = str(i)
                # active value:
                dActive = cmds.getAttr(dcNode + ".active[" +stri+ "]")
                dPlayList = cmds.getAttr(dcNode + ".playList[" + stri + "]")
                if not dPlayList== None:
                    proxyList = dPlayList+'_action_'+ activeAgnt
                    if cmds.objExists(proxyList) and cmds.nodeType(proxyList) == "McdAction" :
                        playlist.append(proxyList)
            cmds.textScrollList(TxSL,e=1,ra=1)
            cmds.textScrollList(TxSL,e=1,append=playlist)
#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def getActionProxyNode ():
    activeAgnt = McdGetActiveAgentName()
    realName = getAgentRealName()
    typeAct = 'actionProxy'
    if realName[1] ==1: # True
        listDcNode = cmds.ls(activeAgnt+':'+'*'+typeAct+'_'+realName[0])
    if realName[1] ==0:# False
        listDcNode = cmds.ls('*'+typeAct+'_'+realName[0])
    if not len(listDcNode)==0 and cmds.nodeType(listDcNode[0])== "McdActionProxy" :
        dcNode = listDcNode[0]
    else:
        dcNode = ''
    return dcNode

#/////////////////////////////////////////////////////////
#TSL,TxSL
#/////////////////////////////////////////////////////////
def updateProxyList(TxSL):
    """
    limit action proxy 30 actions
    """
    activeAgnt = McdGetActiveAgentName()
    listProxy = cmds.textScrollList(TxSL,q=1,ai=1)
    typeAct = 'actionProxy'
    dcNode = getActionProxyNode ()
    actionName = []
    if listProxy==None:
        # turn off active and remove action Name
        for i in range(30):
            cmds.setAttr(dcNode + ".active[" + str(i) + "]", 0)
            cmds.setAttr(dcNode + ".playList[" + str(i) + "]",'', type = "string")
    if not listProxy==None:
        for obj in listProxy:
            names = obj.split('_')[0]
            if len(names.split(':'))>1: #check for nameSpace
                actName = names.split(':')[-1]
                actionName.append(actName)
            if len(names.split(':'))==1:
                actionName.append(names)
        for i in range(0,len(actionName)):
            cmds.setAttr(dcNode + ".active[" + str(i) + "]", 1)
            cmds.setAttr(dcNode + ".playList[" + str(i) + "]", actionName[i], type = "string")
        # reset the rest active=0
        for i in range(len(actionName),30):
            cmds.setAttr(dcNode + ".active[" + str(i) + "]", 0)
            cmds.setAttr(dcNode + ".playList[" + str(i) + "]",'', type = "string")
#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def moveUp(TxSL):
    A = cmds.textScrollList(TxSL,q=1,sii=1)[0]-1
    B = cmds.textScrollList(TxSL,q=1,si=1)[0]
    allItems = cmds.textScrollList(TxSL,q=1,ai=1)
    allItems[A] = allItems[A-1]
    allItems[A-1] = B
    cmds.textScrollList(TxSL,e=1,ra=1)
    cmds.textScrollList(TxSL,e=1,append=allItems)
    #continueSelect
    cmds.textScrollList(TxSL,e=1,sii=A)
#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def moveDn(TxSL):
    A = cmds.textScrollList(TxSL,q=1,sii=1)[0]-1
    B = cmds.textScrollList(TxSL,q=1,si=1)[0]
    allItems = cmds.textScrollList(TxSL,q=1,ai=1)
    allItems[A] = allItems[A+1]
    allItems[A+1] = B
    cmds.textScrollList(TxSL,e=1,ra=1)
    cmds.textScrollList(TxSL,e=1,append=allItems)
    #continueSelect
    cmds.textScrollList(TxSL,e=1,sii=A+2)
#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def updateActEditorInfo(obj):

    #getInfo from action Node
    # note cyle,Entry,Exit *100
    isCycle  = cmds.getAttr(obj+'.isCycle')
    isFinal = cmds.getAttr(obj+'.isFinalAction')
    match= cmds.getAttr(obj+'.matchName')
    length = cmds.getAttr(obj+'.length')
    rate = cmds.getAttr(obj+'.rate')
    cycle = cmds.getAttr(obj+'.cycleFilter')*100
    entry = cmds.getAttr(obj+'.transIn')*100
    exit = cmds.getAttr(obj+'.transOut')*100

    entryRandA = cmds.getAttr(obj+'.entryMin')
    entryRandB = cmds.getAttr(obj+'.entryMax')

    actA = cmds.getAttr(obj+'.exitChoices[0]')
    actB = cmds.getAttr(obj+'.exitChoices[1]')
    actC = cmds.getAttr(obj+'.exitChoices[2]')
    actD = cmds.getAttr(obj+'.exitChoices[3]')

    startA = cmds.getAttr(obj+'.exitStartFrame[0]')
    endA = cmds.getAttr(obj+'.exitEndFrame[0]')

    startB = cmds.getAttr(obj+'.exitStartFrame[1]')
    endB = cmds.getAttr(obj+'.exitEndFrame[1]')

    startC = cmds.getAttr(obj+'.exitStartFrame[2]')
    endC = cmds.getAttr(obj+'.exitEndFrame[2]')

    startD = cmds.getAttr(obj+'.exitStartFrame[3]')
    endD = cmds.getAttr(obj+'.exitEndFrame[3]')

    if actA==None: actA=''
    if actB==None: actB=''
    if actC==None: actC=''
    if actD==None: actD=''
    cmds.checkBox('isFinalCB',e=1,v=isFinal)
    cmds.checkBox('isCycleCB',e=1,v=isCycle)
    cmds.checkBox('matchNameCB',e=1,v=match)
    cmds.intFieldGrp('lengthIntFG', e=1,v1=length)
    cmds.floatFieldGrp('rateFG',e=1,v1=rate)
    cmds.floatSliderGrp('CycleFSLGrp',e=1,v=cycle)
    cmds.floatSliderGrp('entryFSLGrp',e=1,v=entry)
    cmds.floatSliderGrp('exitFSLGrp',e=1,v=exit)
    cmds.floatFieldGrp('entryRand1FG',e=1,v1=entryRandA)
    cmds.floatFieldGrp('entryRand2FG',e=1,v1=entryRandB)
    cmds.textFieldGrp('exitActA',e=1,tx=actA)
    cmds.textFieldGrp('exitActB',e=1,tx=actB)
    cmds.textFieldGrp('exitActC',e=1,tx=actC)
    cmds.textFieldGrp('exitActD',e=1,tx=actD)

    cmds.intFieldGrp('startFrameA',e=1,v1=startA)
    cmds.intFieldGrp('endFrameA',e=1,v1=endA)
    cmds.intFieldGrp('startFrameB',e=1,v1=startB)
    cmds.intFieldGrp('endFrameB',e=1,v1=endB)
    cmds.intFieldGrp('startFrameC',e=1,v1=startC)
    cmds.intFieldGrp('endFrameC',e=1,v1=endC)
    cmds.intFieldGrp('startFrameD',e=1,v1=startD)
    cmds.intFieldGrp('endFrameD',e=1,v1=endD)

    setCycleFrame()
    setInFrame()
    setOutFrame()
    setFrameTotal()
    setRate()
    #setEntryRandA()
    #setEntryRandB()
#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def setCycleFilter():
    #get actionNode
    obj = cmds.textField('actNodeTFGrp',q=1,tx=1)
    if cmds.nodeType(obj)=='McdAction':
        cycle = cmds.floatSliderGrp('CycleFSLGrp',q=1,v=1)
        cmds.setAttr(obj+'.cycleFilter',cycle/100)
    setCycleFrame()
def setEntryRange():
    #get actionNode
    obj = cmds.textField('actNodeTFGrp',q=1,tx=1)
    if cmds.nodeType(obj)=='McdAction':
        entry = cmds.floatSliderGrp('entryFSLGrp',q=1,v=1)
        cmds.setAttr(obj+'.transIn',entry/100)
    setInFrame()
    setFrameTotal()
def setExitRange():
    #get actionNode
    obj = cmds.textField('actNodeTFGrp',q=1,tx=1)
    if cmds.nodeType(obj)=='McdAction':
        exit = cmds.floatSliderGrp('exitFSLGrp',q=1,v=1)
        cmds.setAttr(obj+'.transOut',exit/100)
    setOutFrame()
    setFrameTotal()
def setRate():
    #get actionNode
    obj = cmds.textField('actNodeTFGrp',q=1,tx=1)
    if cmds.nodeType(obj)=='McdAction':
        rate = cmds.floatFieldGrp('rateFG',q=1,v1=1)
        cmds.setAttr(obj+'.rate',rate)
def setIsFinal():
    #get actionNode
    obj = cmds.textField('actNodeTFGrp',q=1,tx=1)
    if cmds.nodeType(obj)=='McdAction':
        isFinal = cmds.checkBox('isFinalCB',q=1,v=1)
        cmds.setAttr(obj+'.isFinalAction',isFinal )
def setIsCycle():
    obj = cmds.textField('actNodeTFGrp',q=1,tx=1)
    if cmds.nodeType(obj)=='McdAction':
        isCycle = cmds.checkBox('isCycleCB',q=1,v=1)
        cmds.setAttr(obj+'.isCycle',isCycle)
def setMatchName():
    #get actionNode
    obj = cmds.textField('actNodeTFGrp',q=1,tx=1)
    if cmds.nodeType(obj)=='McdAction':
        match = cmds.checkBox('matchNameCB',q=1,v=1)
        cmds.setAttr(obj+'.matchName',match )

def setCycleFrame():
    length = cmds.intFieldGrp('lengthIntFG',q=1,v1=1)
    cycle = cmds.floatSliderGrp('CycleFSLGrp',q=1,v=1)
    cycleFrame = length*cycle/100
    cmds.intFieldGrp('frameCycleFFGrp',e=1,en=0,v1=cycleFrame)

def setInFrame():
    length = cmds.intFieldGrp('lengthIntFG',q=1,v1=1)
    entry = cmds.floatSliderGrp('entryFSLGrp',q=1,v=1)
    entryFrame = length*entry/100
    cmds.intFieldGrp('frameEntryFFGrp',e=1,en=0,v1=entryFrame)

def setOutFrame():
    length = cmds.intFieldGrp('lengthIntFG',q=1,v1=1)
    exit = cmds.floatSliderGrp('exitFSLGrp',q=1,v=1)
    exitFrame = length*(100-exit)/100
    cmds.intFieldGrp('frameExitFFGrp',e=1,en=0,v1=exitFrame)


def setFrameTotal():
    length = cmds.intFieldGrp('lengthIntFG',q=1,v1=1)
    entry = cmds.floatSliderGrp('entryFSLGrp',q=1,v=1)
    exit = cmds.floatSliderGrp('exitFSLGrp',q=1,v=1)
    entryFrame = length*entry/100
    exitFrame = length*(100-exit)/100
    totalFrame = length-entryFrame-exitFrame
    cmds.intFieldGrp('frameTotalFFGrp',e=1,en=0,v1=totalFrame)


def setEntryRandA():
    #get EntryRandA
    obj = cmds.textField('actNodeTFGrp',q=1,tx=1)
    if cmds.nodeType(obj)=='McdAction':
        A = cmds.floatFieldGrp('entryRand1FG',q=1,v1=1)
        cmds.setAttr(obj+'.entryMin',A)

def setEntryRandB():
    #get EntryRandB
    obj = cmds.textField('actNodeTFGrp',q=1,tx=1)
    if cmds.nodeType(obj)=='McdAction':
        A = cmds.floatFieldGrp('entryRand2FG',q=1,v1=1)
        cmds.setAttr(obj+'.entryMax',A)

def setExitChoicesA():
    obj = cmds.textField('actNodeTFGrp',q=1,tx=1)
    if cmds.nodeType(obj)=='McdAction':
        act = cmds.textFieldGrp('exitActA',q=1,tx=1)
        cmds.setAttr(obj+'.exitChoices[0]',act, type = "string")
def setExitChoicesB():
    obj = cmds.textField('actNodeTFGrp',q=1,tx=1)
    if cmds.nodeType(obj)=='McdAction':
        act = cmds.textFieldGrp('exitActB',q=1,tx=1)
        cmds.setAttr(obj+'.exitChoices[1]',act, type = "string")
def setExitChoicesC():
    obj = cmds.textField('actNodeTFGrp',q=1,tx=1)
    if cmds.nodeType(obj)=='McdAction':
        act = cmds.textFieldGrp('exitActC',q=1,tx=1)
        cmds.setAttr(obj+'.exitChoices[2]',act, type = "string")
def setExitChoicesD():
    obj = cmds.textField('actNodeTFGrp',q=1,tx=1)
    if cmds.nodeType(obj)=='McdAction':
        act = cmds.textFieldGrp('exitActD',q=1,tx=1)
        cmds.setAttr(obj+'.exitChoices[3]',act, type = "string")
def setExitStartFrameA():
    obj = cmds.textField('actNodeTFGrp',q=1,tx=1)
    if cmds.nodeType(obj)=='McdAction':
        int = cmds.intFieldGrp('startFrameA',q=1,v1=1)
        cmds.setAttr(obj+'.exitStartFrame[0]',int)
def setExitStartFrameB():
    obj = cmds.textField('actNodeTFGrp',q=1,tx=1)
    if cmds.nodeType(obj)=='McdAction':
        int = cmds.intFieldGrp('startFrameB',q=1,v1=1)
        cmds.setAttr(obj+'.exitStartFrame[1]',int)
def setExitStartFrameC():
    obj = cmds.textField('actNodeTFGrp',q=1,tx=1)
    if cmds.nodeType(obj)=='McdAction':
        int = cmds.intFieldGrp('startFrameC',q=1,v1=1)
        cmds.setAttr(obj+'.exitStartFrame[2]',int)
def setExitStartFrameD():
    obj = cmds.textField('actNodeTFGrp',q=1,tx=1)
    if cmds.nodeType(obj)=='McdAction':
        int = cmds.intFieldGrp('startFrameD',q=1,v1=1)
        cmds.setAttr(obj+'.exitStartFrame[3]',int)

def setExitEndFrameA():
    obj = cmds.textField('actNodeTFGrp',q=1,tx=1)
    if cmds.nodeType(obj)=='McdAction':
        int = cmds.intFieldGrp('endFrameA',q=1,v1=1)
        cmds.setAttr(obj+'.exitEndFrame[0]',int)
def setExitEndFrameB():
    obj = cmds.textField('actNodeTFGrp',q=1,tx=1)
    if cmds.nodeType(obj)=='McdAction':
        int = cmds.intFieldGrp('endFrameB',q=1,v1=1)
        cmds.setAttr(obj+'.exitEndFrame[1]',int)
def setExitEndFrameC():
    obj = cmds.textField('actNodeTFGrp',q=1,tx=1)
    if cmds.nodeType(obj)=='McdAction':
        int = cmds.intFieldGrp('endFrameC',q=1,v1=1)
        cmds.setAttr(obj+'.exitEndFrame[2]',int)
def setExitEndFrameD():
    obj = cmds.textField('actNodeTFGrp',q=1,tx=1)
    if cmds.nodeType(obj)=='McdAction':
        int = cmds.intFieldGrp('endFrameD',q=1,v1=1)
        cmds.setAttr(obj+'.exitEndFrame[3]',int)
#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
"""


    cmds.intFieldGrp('startFrameA', nf=1,cw=[(1,60),(2,40)], label='start',v1 =0,cc=lambda x:setExitStartFrameA())
    cmds.intFieldGrp('endFrameA', nf=1,cw=[(1,40),(2,60)], label='end',v1 =0,cc=lambda x:setExitEndFrameA())

    cmds.intFieldGrp('startFrameB', nf=1,cw=[(1,60),(2,40)], label='start',v1 =0,cc=lambda x:setExitStartFrameB())
    cmds.intFieldGrp('endFrameB', nf=1,cw=[(1,40),(2,60)], label='end',v1 =0,cc=lambda x:setExitEndFrameB())

    cmds.intFieldGrp('startFrameC', nf=1,cw=[(1,60),(2,40)], label='start',v1 =0,cc=lambda x:setExitStartFrameC())
    cmds.intFieldGrp('endFrameC', nf=1,cw=[(1,40),(2,60)], label='end',v1 =0,cc=lambda x:setExitEndFrameC())

    cmds.intFieldGrp('startFrameD', nf=1,cw=[(1,60),(2,40)], label='start',v1 =0,cc=lambda x:setExitStartFrameD())
    cmds.intFieldGrp('endFrameD', nf=1,cw=[(1,40),(2,60)], label='end',v1 =0,cc=lambda x:setExitEndFrameD())




    cmds.intFieldGrp('startFrameA')
    cmds.intFieldGrp('endFrameA')

    cmds.intFieldGrp('startFrameB')
    cmds.intFieldGrp('endFrameB')

    cmds.intFieldGrp('startFrameC')
    cmds.intFieldGrp('endFrameC')

    cmds.intFieldGrp('startFrameD')
    cmds.intFieldGrp('endFrameD')

#getInfo from action Node
# note cyle,Entry,Exit *100

length = cmds.intFieldGrp('lengthIntFG',q=1,v1=1)
cycle = cmds.floatSliderGrp('CycleFSLGrp',q=1,v=1)
entry = cmds.floatSliderGrp('entryFSLGrp',q=1,v=1)
exit = cmds.floatSliderGrp('exitFSLGrp',q=1,v=1)

cycleFrame = length*cycle/100
entryFrame = length*entry/100
exitFrame = length*(100-exit)/100
totalFrame = length-entryFrame-exitFrame
cmds.intFieldGrp('frameCycleFFGrp',e=1,en=0,v1=cycleFrame)
cmds.intFieldGrp('frameEntryFFGrp',e=1,en=0,v1=entryFrame)
cmds.intFieldGrp('frameExitFFGrp',e=1,en=0,v1=exitFrame)
cmds.intFieldGrp('frameTotalFFGrp',e=1,en=0,v1=totalFrame)
getFrameTotal('frameTotalFFGrp')
getCycleFrame('frameCycleFFGrp')
getInFrame('frameEntryFFGrp')
getOutFrame('frameExitFFGrp')
"""