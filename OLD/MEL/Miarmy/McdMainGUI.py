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
from McdAgentManager import *
from McdOriginalAgentFunctions import *
from McdPlacementFunctions import *
from McdActionFunctions import *
from McdKnowledgeFunctions import *
from McdRenderFBXFunctions import *
from McdRenderMRFunctions import *

#UI
from McdPlacementEditorGUI import *
from McdAgentManagerGUI import *
from McdAgentViewerGUI import *
from McdActionEditorGUI import *
from McdActionProxyEditorGUI import *
from McdStoryListEditorGUI import *
from McdAgentViewerGUI import *
from McdAgentManagerGUI import *
from McdTerrainManagerGUI import *
from McdDecisionEditorGUI import *
from McdMiarmyGlobalGUI import *
from McdPhysicsGlobalGUI import *
from McdRenderSettingGUI import *
from McdMakeAgentCache import *
#use for luma PipeLine
#note if you don't have riggTool script pleasecomment line 40,41,180 ( look for keyword "luma')
#import riggTool.utilTool.TS_miarmySetup as miarmy
#reload(miarmy)
import McdActionGUI as act
reload(act)
import McdTransitionGUI as trans
reload(trans)
import McdLogicBehaviorPreset as preset
reload(preset)
import McdOutputGUI as output
reload(output)

uiVersion = "Miarmy UI V.20"
#check miarmy content first
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
#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
mainWin='miarmyUI'
def McdMainGUI():
    if(cmds.window(mainWin, ex=1)):
        cmds.deleteUI(mainWin)
    cmds.window(mainWin, t='miarmyUI', widthHeight=(410,500))
    cmds.scrollLayout( h=700,w=400, vis=1)
    #load active agent Name
    cmds.separator(h=10,style='none',w=400)
    mainUI=cmds.columnLayout(w=400,cal='center',adj=1)
    cmds.text(l='<<<<<'+uiVersion+'>>>>>',al='center')
    cmds.separator(h=10,style='none',w=400)
    cmds.button (label='Refresh Miarmy UI', bgc= darkGreyBttn, w=400, h=30, command=lambda x: refreshUI('miarmyUI'))
    #content
    agentManagerUI()
    cmds.setParent(mainUI)
    playbackUI()
    cmds.setParent(mainUI)
    #miarmyToolUI()
    mainTab=cmds.tabLayout('mainTLO',imh=5,imw=5,w=400)
    #------------------------------------------------------# Main Tab
    tabContent1=cmds.columnLayout(w=400)
    cmds.separator(h=5,style='none',w=400)
    #content
    agentLayoutUI()
    #------------------------------------------------------# end of tabContent1
    cmds.setParent(mainTab)
    tabContent2=cmds.columnLayout(w=400)
    cmds.separator(h=5,style='none',w=400)
    #content
    act.actionMainUI()

    #------------------------------------------------------# end of tabContent2
    cmds.setParent(mainTab)
    tabContent3=cmds.columnLayout(w=400)
    cmds.separator(h=5,style='none',w=400)
    #content
    trans.transitionUI()
    #------------------------------------------------------# end of tabContent3
    cmds.setParent(mainTab)
    tabContent4=cmds.columnLayout(w=400)
    cmds.separator(h=5,style='none',w=400)
    #content
    decisionUI()
    cmds.setParent(tabContent4)
    loadDecisionNodeUI()
    #------------------------------------------------------# end of tabContent4
    cmds.setParent(mainTab)
    tabContent5=cmds.columnLayout(w=400)
    cmds.separator(h=5,style='none',w=400)
    #content
    output.outputUI()
    #------------------------------------------------------# end of tabContent5
    cmds.setParent(mainTab)
    tabContent6=cmds.columnLayout(w=400)
    cmds.separator(h=5,style='none',w=400)
    #content
    miarmyToolUI()
    cmds.setParent(tabContent5)
    #------------------------------------------------------# end of tabContent6
    cmds.setParent(mainTab)
    tabContent7=cmds.columnLayout(w=400)
    cmds.separator(h=5,style='none',w=400)
    #content
    allMiarmyUI()
    #------------------------------------------------------# end of tabContent7
    cmds.tabLayout(mainTab,
        tl=[(tabContent1, 'CREATE'),
            (tabContent2, 'ACT'),
            (tabContent3, 'MAP'),
            (tabContent4, 'DCSN'),
            (tabContent5, 'OUTPUT'),
            (tabContent6, 'TOOL'),
            (tabContent7, 'UI')],e=1)
    #------------------------------------------------------# end Window

    cmds.setParent(mainUI)


    cmds.showWindow(mainWin)
#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
#note for button color
yellowBttn = [0.8,0.7,0.3]
redBttn  = [0.6,.3,0.3]
cyanBttn = [0.3,0.5,0.6]
greyBttn = [0.5,0.5,0.5]
darkGreyBttn = [0.4,0.4,0.4]
lightGreyBttn = [0.6,0.6,0.6]
#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////

def playbackUI():
    #cmds.scrollLayout(h=520, w=400, vis=1)

    cmds.frameLayout(cll=1,cl=0,l="Playback UI",w=400,bs="etchedIn")
    mainUI=cmds.columnLayout(w=400,adj=1)
    cmds.rowColumnLayout(nc=2,cw=[(1, 200), (2, 200)] )
    cmds.button (label='PLACE', bgc=lightGreyBttn, h=35, command=lambda x: placementAgent())
    cmds.button (label='De-PLACE', bgc=lightGreyBttn, h=35, command=lambda x: dePlacementAgent())
    cmds.setParent(mainUI)
    cmds.rowColumnLayout(nc=2,cw=[(1, 260), (2, 140)] )
    cmds.button (label='PLAY/STOP', bgc=redBttn, h=35,command=lambda x: playToggleOnOff())
    cmds.button (label='RESET', bgc=greyBttn, h=35,command=lambda x: mel.eval('playButtonStart'))
    cmds.setParent(mainUI)
    cmds.button (label='PLAY BY FRAME', bgc=cyanBttn, h=35,command=lambda x:playBackNextFrame())

#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def agentLayoutUI():
    #cmds.scrollLayout(h=600, w=400, vis=1)
    mainUI=cmds.columnLayout(w=400)
    ##
    cmds.frameLayout(cll=1,cl=0,l="Create Agent" ,w=400,bs="etchedIn")
    agentCOL = cmds.columnLayout(w=400)
    cmds.separator(h=10,style="none",w=400)
    cmds.button (label='Miarmy Ready!', bgc= yellowBttn, w=400, h=40, command=lambda x: McdSelectMcdGlobal())
    cmds.separator(h=10,style="none",w=400)
    cmds.button (label='CREATE ORIGINAL AGENT', bgc=yellowBttn, w=400, h=40, command=lambda x: McdParseRootBoneCreateOAgent(0))
    cmds.separator(h=10,style="none",w=400)
    #cmds.button (label='Luma Miarmy Preset', bgc=greyBttn, w=400, h=30, command=lambda x: miarmy.lumaAgentPreset())
    cmds.button (label='createGeoForAgent', bgc=cyanBttn, w=400, h=30, command=lambda x: CopyGeoFromSetupAndSkinToOA())
    cmds.setParent(agentCOL)
    cmds.rowColumnLayout(numberOfColumns=2)
    cmds.button (label='Delete Agent', bgc=greyBttn, w=200, h=30, command=lambda x: McdParseRootBoneDeleteOAgent())
    cmds.button (label='Re-create Agent', bgc=greyBttn, w=200, h=30, command=lambda x: McdParseRootBoneReCreateOAgent())
    cmds.button (label='Agent Viewer', bgc=darkGreyBttn, w=200, h=30, command=lambda x: McdAgentViewerGUI())
    cmds.button (label='Agent Manager', bgc=darkGreyBttn, w=200, h=30, command=lambda x: McdAgentManagerGUI())
    cmds.setParent('..')
    cmds.separator(h=5,style="none",w=400)
    ##
    cmds.setParent(mainUI)
    cmds.frameLayout(cll=1,cl=0,l="Create Placement" ,w=400,bs="etchedIn")
    placementCOL = cmds.columnLayout(w=400)
    cmds.rowLayout(numberOfColumns=2)
    cmds.button (label='CreatePlacementNode', bgc=greyBttn, w=200, h=30, command=lambda x: McdCreatePlacementNode())
    cmds.button (label='Placement UI', bgc=greyBttn, w=200, h=30, command=lambda x: McdPlacementEditorGUI())
    cmds.setParent(placementCOL)
    cmds.separator(h=10,style="none",w=400)
    cmds.button (label='PLACE', bgc=yellowBttn, w=400, h=30, command=lambda x: placementAgent())
    cmds.button (label='PLACE From Selected', bgc=yellowBttn, w=400, h=30, command=lambda x: placementAgentFromSelect())
    cmds.button (label='De-PLACE', bgc=redBttn, w=400, h=30, command=lambda x: dePlacementAgent())
    cmds.button (label='INVERSE PLACE', bgc=cyanBttn, w=400, h=30, command=lambda x: inversePlacementAgent())
    cmds.separator(h=10,style="none",w=400)
    cmds.setParent(placementCOL)
    cmds.rowColumnLayout(numberOfColumns=2)

    cmds.button (label='Attach Terrain', bgc=greyBttn, w=200, h=30, command=lambda x: McdAttachTerrain())
    cmds.button (label='Detach Terrain', bgc=greyBttn, w=200, h=30, command=lambda x: McdDetachTerrain())
    cmds.button (label='Attach Curve', bgc=greyBttn, w=200, h=30, command=lambda x: McdAttachCurve())
    #cmds.button (label='Detach Curve', bgc=greyBttn, w=200, h=30)
    cmds.setParent(placementCOL)
    cmds.button (label='Create PolyMesh', bgc=cyanBttn, w=400, h=30, command=lambda x:cmds.setToolTo('polyCreateFacetContext'))
    cmds.rowColumnLayout(numberOfColumns=2)
    cmds.button (label='Attach Mesh', bgc=greyBttn, w=200, h=30, command=lambda x: McdAttachRangeMesh())
    cmds.button (label='Detach Mesh', bgc=greyBttn, w=200, h=30, command=lambda x: McdDetachRangeMesh())



    cmds.setParent('..')
    cmds.separator(h=5,style="none",w=400)


#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def decisionUI():
    #cmds.scrollLayout(h=700, w=400, vis=1)
    mainUI=cmds.columnLayout(w=400,cat=("left", 5))
    ##
    cmds.frameLayout(cll=1,cl=0,l="Logic and Decision",w=400,bs="etchedIn")
    cmds.columnLayout(w=400,adj=1)
    cmds.separator(h=10,style="none",w=400)
    cmds.button (label='MAKE DECISION', bgc=yellowBttn, w=400, h=40, command=lambda x: McdCreateDecisionCmd())
    cmds.separator(h=10,style="none",w=400)
    cmds.button (label='Decision UI', bgc=greyBttn, w=400, h=30, command=lambda x: McdDecisionEditorGUI())
    cmds.rowColumnLayout(numberOfColumns=2)
    cmds.button (label='Turn Off Decision', bgc= darkGreyBttn, w=200, h=30, command=lambda x: enableDecision(0))
    cmds.button (label='Turn On Decision', bgc=darkGreyBttn, w=200, h=30, command=lambda x: enableDecision(1))

    ##
    cmds.setParent(mainUI)
    cmds.separator(h=5,style="none",w=400)
    cmds.frameLayout(cll=1,cl=0,l="Knowledge Perception",w=400,bs="etchedIn")
    cmds.separator(h=5,style="none",w=400)
    cmds.rowColumnLayout(numberOfColumns=2)
    cmds.button (label='Create Solver Space', bgc= greyBttn, w=200, h=30, command=lambda x: McdCreateSolverSpace())
    cmds.button (label='Create Road', bgc=greyBttn, w=200, h=30, command=lambda x: McdCreateRoad())
    cmds.button (label='Create Bound', bgc=greyBttn, w=200, h=30, command=lambda x: McdCreateBound())
    cmds.button (label='Create Spot', bgc=greyBttn, w=200, h=30, command=lambda x: McdCreateSpot())
    cmds.button (label='Create Spot + Force Field', bgc=greyBttn, w=200, h=30, command=lambda x: McdCreateSpotWithForceField())
    cmds.button (label='Create Force Field', bgc=greyBttn, w=200, h=30, command=lambda x: McdCreateSpotOnlyForceField())
    cmds.button (label='Create Wind', bgc=greyBttn, w=200, h=30, command=lambda x: McdCreateWind())
    cmds.button (label='Create Zone', bgc=greyBttn, w=200, h=30, command=lambda x: McdCreateZone())
    cmds.button (label='Attach Road To Terrain', bgc=greyBttn, w=200, h=30, command=lambda x: McdAttachRoadToTerrain())
    cmds.button (label='Select Zone Node', bgc=greyBttn, w=200, h=30, command=lambda x: McdGetZoneNode())
    cmds.setParent('..')
    #cmds.separator(h=2,style="none",w=400)
    cmds.rowColumnLayout(numberOfColumns=2)
    cmds.button (label='Switch RoadFlow', bgc=darkGreyBttn, w=200, h=30, command=lambda x: McdRoadFlowMode(1))
    cmds.button (label='Switch Road', bgc=darkGreyBttn, w=200, h=30, command=lambda x: McdRoadFlowMode(0))
    cmds.setParent('..')
    cmds.separator(h=5,style="none",w=400)
    cmds.setParent('..')
    cmds.frameLayout(cll=1,cl=1,l="Preset Logic" ,w=400,bs="etchedIn")
    cmds.rowColumnLayout(numberOfColumns=2)
    cmds.button(label = "Blank Priority", bgc=greyBttn, w=200, h=30,command=lambda x:preset.McdPLB_BlankPriority())
    cmds.button( label = "Avoid Sound",bgc=greyBttn, w=200, h=30,command=lambda x:preset.McdPLB_collideAvoidSound())
    cmds.button(label = "Avoid Spot", bgc=greyBttn, w=200, h=30,command=lambda x:preset.McdPLB_AvoidSpot())
    cmds.button(label = "Avoid Zone", bgc=greyBttn, w=200, h=30,command=lambda x:preset.McdPLB_AvoidZone())
    cmds.button(label = "Follow Spot",bgc=greyBttn, w=200, h=30, command=lambda x:preset.McdPLB_FollowSpot())
    cmds.button(label = "Follow Field", bgc=greyBttn, w=200, h=30,command=lambda x:preset.McdPLB_FollowField())
    cmds.button(label = "Follow Terrain",bgc=greyBttn, w=200, h=30,command=lambda x:preset.McdPLB_FollowTerrain())
    cmds.button(label = "Follow RoadFlow", bgc=greyBttn, w=200, h=30,command=lambda x:preset.McdPLB_RoadFlow())
    cmds.button(label = "Follow Road",bgc=greyBttn, w=200, h=30, command=lambda x:preset.McdPLB_Road())
    cmds.button(label = "BlockVision if in bound",bgc=greyBttn, w=200, h=30, command=lambda x:preset.McdPLB_InBoundBlkVis())

#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def refreshUI(mainWin):
    if(cmds.window(mainWin, ex=1)):
        cmds.deleteUI(mainWin)
    McdMainGUI()
#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def allMiarmyUI():
    #cmds.scrollLayout(h=700, w=400, vis=1)
    mainUI=cmds.columnLayout(w=400)
    ##
    cmds.frameLayout(cll=1,cl=0,l="Agent",w=400,bs="etchedIn")
    cmds.columnLayout(w=400)
    cmds.separator(h=10,style="none",w=400)
    cmds.button (label='Placement UI', bgc=greyBttn, w=400, h=30, command=lambda x: McdPlacementEditorGUI())
    cmds.button (label='Agent Viewer', bgc=greyBttn, w=400, h=30, command=lambda x: McdAgentViewerGUI())
    cmds.button (label='Agent UI', bgc=greyBttn, w=400, h=30, command=lambda x: McdAgentManagerGUI())
    cmds.button (label='Terrain UI', bgc=greyBttn, w=400, h=30, command=lambda x: McdTerrainManagerGUI())
    cmds.button (label='Action UI', bgc= greyBttn, w=400, h=30, command=lambda x: McdActionEditorGUI())
    cmds.button (label='Action Proxy UI', bgc=greyBttn, w=400, h=30, command=lambda x: McdActionProxyEditorGUI())
    cmds.button (label='Story List UI', bgc=greyBttn, w=400, h=30, command=lambda x: McdStoryListEditorGUI())
    cmds.button (label='Decision UI', bgc=greyBttn, w=400, h=30, command=lambda x: McdDecisionEditorGUI())
    cmds.separator(h=20,style="none",w=400)
#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def loadActionNodeUI():
    listAction=[]
    mainUI=cmds.columnLayout(w=400,cat=("left", 5))
    ##
    cmds.frameLayout(cll=1,cl=1,l="List Action Node",w=400,bs="etchedIn")
    cmds.columnLayout(w=400)
    cmds.separator(h=5,style="none",w=400)
    cmds.button (label='Load Action Agent', bgc=darkGreyBttn,w=400, h=30,al='center',command=lambda x: appendListNode('actionNodeTxSL',typeAct='action'))
    cmds.textScrollList('actionNodeTxSL',w=400,h=400,ams = 0,append=listAction,sc="""import McdMainGUI as myuis \nmyuis.selectItem('actionNodeTxSL')""")
    cmds.setParent(mainUI)
    cmds.separator(h=20,style="none",w=400)
#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def loadDecisionNodeUI():
    listDecision=[]
    mainUI=cmds.columnLayout(w=400,cat=("left", 5))
    ##
    cmds.frameLayout(cll=1,cl=1,l="List Decision Node",w=400,bs="etchedIn")
    cmds.columnLayout(w=400)
    cmds.separator(h=5,style="none",w=400)
    cmds.button (label='Load Decision Agent', bgc=darkGreyBttn,w=400, h=30,al='center',command=lambda x: appendListNode('desionNodeTxSL',typeAct='decision'))
    cmds.textScrollList('desionNodeTxSL',w=400,h=250,ams = 0,append=listDecision,sc="""import McdMainGUI as myuis \nmyuis.selectItem('desionNodeTxSL')""")
    cmds.setParent(mainUI)
    cmds.separator(h=20,style="none",w=400)
#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def miarmyToolUI(name='A'):
    "name = use for add Name on UI to make it Unique"
    mainUI=cmds.columnLayout(w=400)
    cmds.frameLayout(cll=1,cl=0,l="Tool ",w=400,bs="etchedIn")
    COL1 = cmds.columnLayout(w=400)
    cmds.separator(h=10,style="none",w=400)
    cmds.button (label='SWITCH TO PERSP', bgc= yellowBttn, w=400, h=30, command=lambda x: switchToCamView(0))
    cmds.button (label='SWITCH TO BRAIN VIEWER', bgc= yellowBttn, w=400, h=30, command=lambda x: switchToCamView(1))
    cmds.button (label='SWITCH TO TRANSITION MAP', bgc= yellowBttn, w=400, h=30, command=lambda x: switchToCamView(2))
    cmds.button (label='CAMERA FOLLOW AGENT', bgc= cyanBttn, w=400, h=30, command=lambda x: duplicateCamAndParentLook())
    cmds.button (label='Mark Agent Selected (Re cache)', bgc= cyanBttn, w=400, h=30, command=lambda x: McdMarkAgentOut())


    cmds.separator(h=5,style="none",w=400)
    cmds.rowColumnLayout(numberOfColumns=2)
    cmds.button (label='Mark Selected Agents', bgc= lightGreyBttn,w=200,  h=30,command=lambda x:markSelectedAgents())
    cmds.button (label='UnMark All Agents', bgc= greyBttn,w=200, h=30,command=lambda x:unMarkAllAgents())
    cmds.button (label='Agent Match', bgc= lightGreyBttn,w=200,  h=30, command=lambda x: oAgentMatchAgent())
    cmds.button (label='Agent Return', bgc= greyBttn,w=200, h=30, command=lambda x: oAgentResume())
    cmds.button (label='Bake Anim To Skeleton ALL', bgc=darkGreyBttn,w=200, h=30, command=lambda x: McdBakeAgentToAnimatedBone(0))
    cmds.button (label='Bake Anim To Skeleton SELECTED', bgc=darkGreyBttn,w=200,  h=30, command=lambda x: McdBakeAgentToAnimatedBone(1))
    ##
    cmds.setParent(COL1)
    cmds.separator(h=10,style="none",w=400)
    cmds.frameLayout(cll=1,cl=0,l="Visibility" ,w=400,bs="etchedIn")
    visCOL = cmds.columnLayout(w=400)
    cmds.rowColumnLayout(numberOfColumns=2)
    cmds.button (label='Sound Visibility', bgc=redBttn, w=200, h=30, command=lambda x: soundRangeSwitch())
    cmds.button (label='Vision Visibility', bgc=cyanBttn, w=200, h=30, command=lambda x: visionRangeSwitch())
    cmds.button (label='HP/MP Visibility', bgc=redBttn, w=200, h=30, command=lambda x: HPSwitch())
    cmds.button (label='Action Info Visiblity', bgc=cyanBttn, w=200, h=30, command=lambda x: actionSwitch())
    cmds.button (label='Show BoundingBox', bgc=redBttn, w=200, h=30, command=lambda x: boundingVis(vis=1))
    cmds.button (label='Hide BoundingBox', bgc=cyanBttn, w=200, h=30, command=lambda x: boundingVis(vis=0))
    cmds.button (label='Show Bone', bgc=greyBttn, w=200, h=30, command=lambda x: cmds.showHidden("*_dummyShape_*", "*_phyJoint_*"))
    cmds.button (label='Hide Bone', bgc=greyBttn, w=200, h=30, command=lambda x: cmds.hide("*_dummyShape_*", "*_phyJoint_*"))
    # duplicate node
    cmds.setParent(COL1)
    cmds.separator(h=5,style="none",w=400)
    listAgent =McdGetAllAgentTypeNIDWithColor()[0]
    cmds.text(l='  Duplicate Node: Select Nodes First',al='left')
    cmds.separator(h=10,style="none",w=400)
    #cmds.button (label='Refresh Agent Name', bgc=yellowBttn, w=400, h=20, command=lambda x: refreshAgentName())
    cmds.optionMenu('agentoOpt'+name,l="  Pick Agent Name     :  ",w=380)
    for agnt in listAgent:
        cmds.menuItem(l=agnt)
    cmds.separator(h=10,style="none",w=400)
    cmds.button (label='Duplicate Actions,Decisions,and Transitions', bgc=yellowBttn, w=400, h=30, command=lambda x: duplicateNodeForUI(name))
    cmds.separator(h=10,style="none",w=400)
    cmds.setParent(mainUI)
    cmds.separator(h=10,style="none",w=400)





#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def activeActionProxy():
    activeAgnt = McdGetActiveAgentName()
    cmds.select('actionProxy_'+activeAgnt)
    McdActionProxyEditorGUI()
#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def appendListNode(TxSCL,typeAct='action'):
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
    #remove all action from textScrollisr first
    cmds.textScrollList(TxSCL,e=1,ra=1)
    #append action
    cmds.textScrollList(TxSCL,e=1,append=listAction)
#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def activeAgent(TxSCL):
    globalNode = McdGetMcdGlobalNode()
    agentName = cmds.textScrollList(TxSCL,q=1,si=1)[0]
    cmds.setAttr(globalNode + ".activeAgentName", agentName, type = "string")
    #getIndexClor
    clr = getClrIDActiveAgent()
    #update textFiledGrp
    cmds.textFieldGrp('activeAgentTFGrp',e=1,tx= agentName,bgc=setColorOfDraw(clr))
#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def reloadActiveAgent(TFGrp):
    activeAgnt = McdGetActiveAgentName()
    cmds.textFieldGrp(TFGrp,tx= activeAgnt,e=1)
#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def refreshAgentName():
    listAgent =McdGetAllAgentTypeNIDWithColor()[0]
#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def selectItem(TxSCL):
    obj = cmds.textScrollList(TxSCL,q=1,si=1)[0]
    cmds.select(obj)
#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def duplicateNodeForUI(name):
    agentName = cmds.optionMenu('agentoOpt'+name,q=1,v=1)
    duplicateNode(agentName)
#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def duplicateNode(agentName):
    """
    select action node or decision node or transition map to duplicate
    prefix  by defualt always be '' but if agent name def_Agent_loco , then prefix will be "def_"
    """
    sel =cmds.ls(sl=1)
    if len(sel) == 0:
        cmds.confirmDialog(message = 'select node that you want to duplicate first',
            button = 'ok',defaultButton = 'Yes',
            title = 'Confirm')
        cmds.error('select node that you want to duplicate first')
    prefix =''
    #check out that is any agent name XXX_Agent_XXX or not
    # if so prefix = "XXX_"
    # if agent is ref Agent will return []
    optA = cmds.ls(agentName+':'+'Agent_*')
    optB = cmds.ls("*Agent_"+agentName)
    realAgentName = agentName
    agentWithNameSpace = 0 # default no nameSpace
    if not len(optA) == 0:
        agentWithNameSpace =1 # True
        #find realName of agent
        nameSpace = optA[0].split(':')[0]
        realAgentName = optA[0].split('_')[-1]
    if not len(optB) == 0:
        agentWithNameSpace =0 # False
        if len(optB[0].split('_'))>2:
            prefix = optB[0].split('_')[0]+'_'

    for obj in sel:
        names = obj.split('_')
        #check for ":"
        if agentWithNameSpace==1: #convert to realAgentName if object has namespace
            prefix = nameSpace+':'
        if len(names)>2: # work with 3 tokens
            noneRefName = names[-3].split(':')[-1]
            newName = prefix+noneRefName+'_'+names[-2]
        if len(names)==2: # for duplicate actionProxy
            noneRefName = ''
            newName = prefix+noneRefName+names[-2]
        dupNode = cmds.duplicate(obj,n=newName+'_'+realAgentName)[0]
        if names[-2]=='action':
            if agentWithNameSpace==1:
                Action = cmds.ls(agentName+':'+'Action_*')
            if agentWithNameSpace==0: #not ref
                Action = cmds.ls("*Action_"+agentName) # only work for non Ref
                #if not len(Action)==0:
            cmds.parent(dupNode,Action[0])
        if names[-2]=='decision':
            if agentWithNameSpace==1:
                Decision = cmds.ls(agentName+':'+'Decision_*')
            if agentWithNameSpace==0: #not ref
                Decision = cmds.ls("*Decision_"+agentName)
                #if not len(Decision)==0:
            cmds.parent(dupNode,Decision[0])
        if names[-2]=='state':
            if agentWithNameSpace==1:
                State = cmds.ls(agentName+':'+'State_*')
            if agentWithNameSpace==0: #not ref
                State = cmds.ls("*State_"+agentName)
                #if not len(State)==0:
            cmds.parent(dupNode,State[0])
        if names[-2]=='actionShell':
            if agentWithNameSpace==1:
                ActionShell = cmds.ls(agentName+':'+'ActionShell_*')
            if agentWithNameSpace==0: #not ref
                ActionShell = cmds.ls("*ActionShell_"+agentName)
                #if not len(ActionShell)==0:
            cmds.parent(dupNode,ActionShell[0])
        if names[-2]=='actionProxy':
            if agentWithNameSpace==1:
                ActionProxy = cmds.ls(agentName+':'+'ActionProxy*')
            if agentWithNameSpace==0: #not ref
                ActionProxy = cmds.ls("*ActionProxy"+agentName)
                #if not len(ActionShell)==0:
            cmds.parent(dupNode,ActionProxy[0])
#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def enableDecision(value):
    """select decisionNode
    """
    sel = cmds.ls(sl=1)
    for o in sel:
        if cmds.objExists(o+'.enable'):
            cmds.setAttr(o+'.enable',value)

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
def playToggleOnOff():
    state = cmds.play( q=True, state=True )
    if state==0:cmds.play( forward=True )
    if state==1:cmds.play( state=False )
#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def playBackNextFrame():
    #get maya version
    currentFrame = cmds.currentTime(q = True)
    currentFrame+=1
    cmds.currentTime(currentFrame)

#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def boundingVis(vis=0):
    """
    vis = 0 revertback to agentProxy box
    vis =1 show boundingBox
    """
    sel = cmds.ls(sl=1)
    if not len(sel) == 0:
        for obj in sel:
            shapeNode = cmds.listRelatives(obj,s=1)
            if cmds.objExists(shapeNode[0]+'.boundMode'):
                    cmds.setAttr(shapeNode[0]+'.boundMode',vis)

#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def markSelectedAgents():
    sel = cmds.ls(sl=1)
    if len(sel)==0:
        cmds.confirmDialog(t = "Please select Agent first", m = "Please select Agent first.")
        raise Exception("Please select Agent first.")
    B = McdFromAgentToPlace(1)
    for i in xrange(0, len(B), 2):
        nodeName = B[i]
        num  = B[i + 1]
        cmds.setAttr(nodeName+".placement["+str(num,)+"].agentPlace[8]", 1)
    #deplace agent
    dePlacementAgent()
    #replace agent
    placementAgent()
#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def unMarkAllAgents():
    listPlac = cmds.ls(type="McdPlace")
    for o in listPlac:
        #get placement
        plc = cmds.listRelatives(o,p=1)[0]
        num = cmds.getAttr(o+'.numOfAgent')
        for i in range (0, num):
            cmds.setAttr (plc+".placement["+str(i)+"].agentPlace[8]", 0)
        #deplace agent
    dePlacementAgent()
    #replace agent
    placementAgent()

#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def switchToCamView(cam):
    import pymel.core as pm
    if cam == 0:
        camType = ['base_OpenGL_Renderer','persp']
    if cam == 1:
        camType  = ['McdBrainView','Cam_Brain_View']
    if cam == 2:
        camType = ['McdTransitionMap','Cam_Transition_Map']
    panelSel = pm.getPanel( withFocus=True )
    pm.mel.lookThroughModelPanel('persp',panelSel)
    panelSel = pm.getPanel( withFocus=True )
    pm.mel.setRendererInModelPanel( camType[0], panelSel)
    pm.lookThru( camType[1] )