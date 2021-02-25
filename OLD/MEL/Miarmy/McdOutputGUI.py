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
from McdMakeAgentCache import *
from McdMeshDriveSetup import *

# load MiarmyUI
#from McdPlacementEditorGUI import *
from McdMiarmyGlobalGUI import *
from McdPhysicsGlobalGUI import *
from McdRenderSettingGUI import *


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
mainWin='outputGUI'
def McdOutputGUI():
    if(cmds.window(mainWin, ex=1)):
        cmds.deleteUI(mainWin)
    cmds.window(mainWin, t='outputUI V 1.0', widthHeight=(400,500))
    cmds.scrollLayout( h=700,w=400, vis=1)
    #load active agent Name
    cmds.separator(h=20,style='none',w=400)
    mainUI=cmds.columnLayout(w=400,adj=1)
    #content
    outputUI()
    cmds.setParent(mainUI)
    cmds.showWindow(mainWin)
    #------------------------------------------------------# Main Tab

#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def outputUI():
    #cmds.scrollLayout(h=700, w=400, vis=1)
    #check status cache on or off
    import os
    cacheFolderName = 'miarmyCache'
    MD2FolderName = 'meshDrv2Cache'
    globalNode = McdListMcdGlobal() # auto create miarmyContent
    EnableCache = cmds.getAttr(globalNode + ".enableCache")
    EnableMeshDrive = cmds.getAttr(globalNode + ".enableMeshDrv")
    #create path folder and file info
    pathAgtCche=cmds.workspace(q=1, rootDirectory=1)+cacheFolderName
    if os.path.exists(pathAgtCche)==0:
        os.makedirs(pathAgtCche)
    pathAgtCche=cmds.workspace(q=1, rootDirectory=1)+cacheFolderName +'/'

    pathMD2=cmds.workspace(q=1, rootDirectory=1)+MD2FolderName
    if os.path.exists(pathMD2)==0:
        os.makedirs(pathMD2)
    pathMD2=cmds.workspace(q=1, rootDirectory=1)+MD2FolderName +'/'
    #get folder path
    cacheFolder = cmds.getAttr(globalNode + ".cacheFolder")
    if cacheFolder == None:
        cacheFolder = pathAgtCche
        #autoSet cache path
        cmds.setAttr(globalNode + ".cacheFolder", cacheFolder, type = "string")
    cacheName = cmds.getAttr(globalNode + ".cacheName")
    if cacheName == None:
        cacheName = "test"
        # autoSet cache name
        cmds.setAttr(globalNode + ".cacheName", cacheName, type = "string")

    MD2Folder = cmds.getAttr(globalNode + ".outMD2Folder")
    if MD2Folder==None:
        MD2Folder = pathMD2
        #autoSet cache path
        cmds.setAttr(globalNode + ".outMD2Folder", MD2Folder, type = "string")
    MD2Name = cmds.getAttr(globalNode + ".outMD2Name")
    if MD2Name == None:
        MD2Name = "testMD"
        # autoSet cache name
        cmds.setAttr(globalNode + ".outMD2Name", MD2Name, type = "string")
    if EnableCache ==1: bttnColor = redBttn
    if EnableCache ==0: bttnColor = greyBttn
    if EnableMeshDrive ==1: bttnMeshColor = redBttn
    if EnableMeshDrive ==0: bttnMeshColor = greyBttn

    mainUI=cmds.columnLayout(w=400,cat=("left", 5))
    ##
    cmds.frameLayout(cll=1,cl=0,l="Render and EXPORT",w=400,bs="etchedIn")
    cmds.columnLayout(w=400,adj=1)
    cmds.separator(h=10,style="none",w=400)
    cmds.button (label='Miarmy Global', bgc=darkGreyBttn, w=400, h=30, command=lambda x: McdMiarmyGlobalGUI())
    cmds.button (label='Physics Global', bgc=greyBttn, w=400, h=30, command=lambda x: McdPhysicsGlobalGUI())
    cmds.button (label='Render Global', bgc=lightGreyBttn, w=400, h=30, command=lambda x: McdRenderSettingGUI())
    cmds.separator(h=10,style="none",w=400)
    # agent cache section----------------------------------
    cmds.setParent(mainUI)
    cmds.frameLayout(cll=1,cl=0,l="Export AgentCache",w=400,bs="etchedIn")
    cmds.columnLayout(w=400,adj=1)
    cmds.textFieldGrp('cachePathTFG',cw=[(1, 80), (2, 320)],
        text=cacheFolder,
        cal=(1, 'center'),adj=2,label='Path Name:',
        cc =lambda x:updateCacheFolder())
    cmds.textFieldGrp('cacheFolderTFG',cw=[(1, 80), (2, 320)],
        text='',
        cal=(1, 'center'),adj=2,label='Folder Name:',
        cc =lambda x:updateCacheFolder())
    cmds.textFieldGrp('cacheFileTFG',cw=[(1, 80), (2, 320)],
        text=cacheName,
        cal=(1, 'center'),adj=2,label='File Name:',
        cc =lambda x:updateCacheFile())
    cmds.popupMenu('pathPOP',p='cachePathTFG')
    cmds.menuItem(c=lambda x: cmds.textFieldGrp('cachePathTFG',e=1,tx=''),l='empty')
    cmds.menuItem(c=lambda x: defaultCachePath('cachePathTFG'),l='defaultPath')

    cmds.popupMenu('folderPOP',p='cacheFolderTFG')
    cmds.menuItem(c=lambda x: cmds.textFieldGrp('cacheFolderTFG',e=1,tx=''),l='empty')
    cmds.menuItem(c=lambda x: cmds.textFieldGrp('cacheFolderTFG',e=1,tx='testA'),l='testA')
    cmds.popupMenu('filePOP',p='cacheFileTFG')
    cmds.menuItem(c=lambda x: cmds.textFieldGrp('cacheFileTFG',e=1,tx=''),l='empty')
    cmds.menuItem(c=lambda x: defaultCacheFile('cacheFileTFG'),l='test')

    cmds.button (label='Make Agent Cache', bgc=yellowBttn, w=400, h=40, command=lambda x: McdMakeAgentCache())
    cmds.rowColumnLayout(numberOfColumns=2)
    cmds.button ('cacheOnBttn',label='Enable Cache', bgc=bttnColor, w=200, h=30, command=lambda x: enableCache(1))
    cmds.button (label='Disable Cache', bgc=greyBttn, w=200, h=30, command=lambda x: enableCache(0))
    cmds.setParent(mainUI)
    # meshDrive 1.0 section----------------------------------
    cmds.frameLayout(cll=1,cl=1,l="Meshdrive 1.0",w=400,bs="etchedIn")
    cmds.columnLayout(w=400,adj=1)
    cmds.button (label='Duplicate Mesh drive', bgc=yellowBttn, w=400, h=40, command=lambda x: MDDuplicateStoreMem())
    cmds.rowColumnLayout(numberOfColumns=2)
    cmds.button ('meshDriveOnBttn',label='Enable MeshDrive', bgc=bttnMeshColor, w=200, h=30, command=lambda x: enableMeshDrive(1))
    cmds.button (label='Disable MeshDrive', bgc=greyBttn, w=200, h=30, command=lambda x: enableMeshDrive(0))
    # meshDrive 2.0section----------------------------------

    cmds.setParent(mainUI)
    cmds.frameLayout(cll=1,cl=0,l="Meshdrive 3.0",w=400,bs="etchedIn")
    cmds.columnLayout(w=400,adj=1)
    cmds.textFieldGrp('MD2PathTFG',cw=[(1, 80), (2, 320)],
        text=MD2Folder,
        cal=(1, 'center'),adj=2,label='Path Name:',
        cc =lambda x:updateMD2Folder())
    cmds.textFieldGrp('MD2FolderTFG',cw=[(1, 80), (2, 320)],
        text='',
        cal=(1, 'center'),adj=2,label='Folder Name:',
        cc =lambda x:updateMD2Folder())
    cmds.textFieldGrp('MD2FileTFG',cw=[(1, 80), (2, 320)],
        text=MD2Name,
        cal=(1, 'center'),adj=2,label='File Name:',
        cc =lambda x:updateMD2File())
    cmds.popupMenu('MD2pathPOP',p='MD2PathTFG')
    cmds.menuItem(c=lambda x: cmds.textFieldGrp('MD2PathTFG',e=1,tx=''),l='empty')
    cmds.menuItem(c=lambda x: defaultMD2Path('MD2PathTFG'),l='defaultPath')
    cmds.button (label='Make MD3 Cache', bgc=yellowBttn, w=400, h=40, command=lambda x: McdExportMD2Cache())
    cmds.text(l='<<<<<FOR RENDER PREVIEW IN MAYA >>>>>',al='center',h=20)
    cmds.button (label='Duplicate Mesh drive 3.0', bgc=cyanBttn, w=400, h=40, command=lambda x:duplicateMD3())
    cmds.rowColumnLayout(numberOfColumns=2)
    cmds.button ('meshDriveOnBttn',label='Enable MeshDrive3', bgc=bttnMeshColor, w=200, h=30, command=lambda x: enableMD3(1,1))
    cmds.button (label='Disable MeshDrive3', bgc=greyBttn, w=200, h=30, command=lambda x: enableMD3(0,0))
    cmds.setParent('..')
    cmds.button (label='Clear Mesh drive 3.0', bgc=redBttn, w=400, h=40, command=lambda x: McdMeshDrive2Clear())
    cmds.text(l='<<<<<FOR BATCH RENDER MAYA >>>>>',al='center',h=20)
    cmds.text(l='MAKE SURE YOU CREATE MESHDRIVE3.0 CACHE FIRST',al='center',h=20)
    cmds.button (label='Set up MeshDrive3.0 For BatchRender', bgc=redBttn, w=400, h=40, command=lambda x: setupMD3BatchRender())
    # footNMap section----------------------------------
    cmds.setParent(mainUI)
    cmds.frameLayout(cll=1,cl=1,l="FootMap generator",w=400,bs="etchedIn")
    cmds.columnLayout(w=400,adj=1)
    cmds.textFieldGrp('footMapPathTFG',cw=[(1, 80), (2, 320)],
        text='NOT FUNCTION AT THIS TIME',
        cal=(1, 'center'),
        adj=2,
        label='File Path:')
    cmds.textFieldGrp('footMapFileTFG',cw=[(1, 80), (2, 320)],
        text='NOT FUNCTION AT THIS TIME',
        cal=(1, 'center'),
        adj=2,
        label='File Name:')
    cmds.button (label='Make Foot Map', bgc=greyBttn, w=400, h=30, command=lambda x: McdMakeFootMap())
    cmds.setParent('..')
    cmds.separator(h=5,style="none",w=400)

    ##mentalRay ----------------------------------
    cmds.setParent(mainUI)
    cmds.frameLayout(cll=1,cl=1,l="Mental Ray",w=400,bs="etchedIn")
    cmds.columnLayout(w=400,adj=1)
    cmds.separator(h=5,style="none",w=400)
    cmds.rowColumnLayout(numberOfColumns=2)
    cmds.button (label='Setup Current Frame', bgc=greyBttn, w=200, h=30, command=lambda x: McdMRSetupCurrentFrame())
    cmds.button (label='Setup Scene Sequence', bgc=greyBttn, w=200, h=30, command=lambda x: McdMRSetupAllFrame())
    cmds.button (label='Export Shader MI Files', bgc=greyBttn, w=200, h=30, command=lambda x: McdMRExportShader())
    cmds.button (label='Replace MI Shader', bgc=greyBttn, w=200, h=40, command=lambda x: McdMRExportAndReplaceShader())
    cmds.button (label='Link Existed MI Sequence', bgc=greyBttn, w=200, h=30, command=lambda x: McdMRLinkMISequence())
    cmds.button (label='Clear MI Files', bgc=greyBttn, w=200, h=30, command=lambda x: McdClearMIs())
    cmds.button (label='Enable Update Render View', bgc=greyBttn, w=200, h=40, command=lambda x: McdUpdateRenderView(1))
    cmds.button (label='Diable Update Render View', bgc=greyBttn, w=200, h=30, command=lambda x: McdUpdateRenderView(0))
    cmds.setParent('..')
    cmds.separator(h=5,style="none",w=400)
#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def enableCache(value):
    #enableCache value=1
    #disableCache value=1
    globalNode = McdListMcdGlobal()
    if value==1:
        reverseValue=0
        #change color when cache turn on
        cmds.button ('cacheOnBttn',e=1, bgc=redBttn)
    if value==0:
        reverseValue=1
        #change color when cache turn off
        cmds.button ('cacheOnBttn',e=1, bgc=greyBttn)
    cmds.setAttr(globalNode + '.enableCache', value) #1 or 0
    allAgents = cmds.ls(type = "McdAgent")
    if allAgents != None and allAgents != []:
        for i in range(len(allAgents)):
            cmds.setAttr(allAgents[i] + ".fMark",reverseValue)
#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def enableMeshDrive(value):
    globalNode = McdListMcdGlobal()
    if value==1:
        reverseValue=0
        #change color when cache turn on
        cmds.button ('meshDriveOnBttn',e=1, bgc=redBttn)
    if value==0:
        reverseValue=1
        #change color when cache turn off
        cmds.button ('meshDriveOnBttn',e=1, bgc=greyBttn)
    cmds.setAttr(globalNode + '.enableMeshDrv', value) #1 or 0
#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def defaultCachePath(TFGrp):
    cacheFolderName = 'miarmyCache'
    globalNode = McdListMcdGlobal()
    #create path folder and file info
    path=cmds.workspace(q=1, rootDirectory=1)+cacheFolderName
    if os.path.exists(path)==0:
        os.makedirs(path)
    path=cmds.workspace(q=1, rootDirectory=1)+cacheFolderName +'/'
    cmds.textFieldGrp(TFGrp, e = 1, tx = path)
    #setGlobal
    cmds.setAttr(globalNode + ".cacheFolder", path, type = "string")
#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def defaultCacheFile(TFGrp,):
    cacheName = 'test'
    globalNode = McdListMcdGlobal()
    #create path folder and file info
    cmds.textFieldGrp(TFGrp, e = 1, tx = cacheName)
    #setGlobal
    cmds.setAttr(globalNode + ".cacheName", cacheName, type = "string")


#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def updateCacheFolder():
    path = cmds.textFieldGrp("cachePathTFG", q = 1, tx = 1)
    folder = cmds.textFieldGrp("cacheFolderTFG", q = 1, tx = 1)
    if not folder == '':
        folderPath = path+folder
        if os.path.exists(folderPath)==0:
            os.makedirs(folderPath)
        folder = folder+'/'
    folderName = path+folder
    cmds.setAttr(globalNode + ".cacheFolder", folderName, type = "string")
#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def updateCacheFile():
    fileName = cmds.textFieldGrp("cacheFileTFG", q = 1, tx = 1)
    if fileName == '':
        fileName = 'test'
        cmds.textFieldGrp("cacheFileTFG", e = 1, tx = fileName)
    cmds.setAttr(globalNode + ".cacheName", fileName, type = "string")
#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def updateMD2Folder():
    path = cmds.textFieldGrp("MD2PathTFG", q = 1, tx = 1)
    folder = cmds.textFieldGrp("MD2FolderTFG", q = 1, tx = 1)
    if not folder == '':
        folderPath = path+folder
        if os.path.exists(folderPath)==0:
            os.makedirs(folderPath)
        folder = folder+'/'
    folderName = path+folder
    cmds.setAttr(globalNode + ".outMD2Folder", folderName, type = "string")
#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def updateMD2File():
    fileName = cmds.textFieldGrp("MD2FileTFG", q = 1, tx = 1)
    if fileName == '':
        fileName = 'testMD'
        cmds.textFieldGrp("MD2FileTFG", e = 1, tx = fileName)
    cmds.setAttr(globalNode + ".outMD2Name", fileName, type = "string")
#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def defaultMD2Path(TFGrp):
    MD2FolderName = 'meshDrv2Cache'
    globalNode = McdListMcdGlobal()
    #create path folder and file info
    path=cmds.workspace(q=1, rootDirectory=1)+MD2FolderName
    if os.path.exists(path)==0:
        os.makedirs(path)
    path=cmds.workspace(q=1, rootDirectory=1)+MD2FolderName +'/'
    cmds.textFieldGrp(TFGrp, e = 1, tx = path)
    #setGlobal
    cmds.setAttr(globalNode + ".outMD2Folder", path, type = "string")
#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def enableMD3(toggle,showbar):
    #toggle = 1 # on
    #toggle = 0 # off
    #showbar =1 showProgress when driving mesh
    #showbar =0 show progress bar when driving mesh
    McdCreateMeshDriveIMNode(toggle,showbar)
#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def setupMD3BatchRender():
    # turn on

    #turn off showprogress for batch render
    listMeshDriveNode  = cmds.ls(type="McdMeshDriveIM")
    for o in listMeshDriveNode:
        cmds.setAttr(o+'.showProgress',0)
    MD2BatchCmd = 'McdBatchMeshDrive;'


#/////////////////////////////////////////////////////////
#
#/////////////////////////////////////////////////////////
def duplicateMD3():

    #deplace agent()
    dePlacementAgent()
    MDDuplicate()