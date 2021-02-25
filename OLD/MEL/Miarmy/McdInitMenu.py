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
##  Module Name: McdInitMenu.py
##
##  Description:
##    initialize the menu of Miarmy
##
## ===================================================================
## -

import maya.mel as mel
import maya.cmds as cmds

def McdReInitMenu():
    # reload button
    mel.eval("source McdMenu;");
    mel.eval("McdMenu;")

def McdInitMenu():
    try:
        cmds.setParent("MayaWindow")

        #add main menu
        try:
            cmds.menu("McdMenu", label= "Miarmy", tearOff = True, pmc = "McdReInitMenu()")
        except:
            pass
        try:
            cmds.menu("McdMenu", e = True, deleteAllItems = True)
        except:
            pass

        cmds.setParent("McdMenu", menu = True)

        cmds.menuItem("mcdmMGob", label = "Miarmy Ready!", c = "McdSelectMcdGlobal()");
        cmds.menuItem("mcdmMAcb", label = "Miarmy Contents Check", c = "McdAgentContainerBuild()")
        cmds.menuItem("mcdm12Imp", label = "Import without Namespace/Prefix", subMenu = True, tearOff = True );
        cmds.menuItem("mcdm12Ima", label = ".ma without name change", c = "Maya2012ImportMa()")
        cmds.menuItem("mcdm12Imb", label = ".mb without name change", c = "Maya2012ImportMb()")
        cmds.setParent("..", menu = True)
        cmds.menuItem(divider = True)

        ######################################################
        #cmds.menuItem("mcdm10", label = "Miarmy Solver", subMenu = True, tearOff = True)
        cmds.menuItem("mcdtoolsp", label = "Miarmy Tools...", c = "McdMiarmyToolsGUI()")
        cmds.menuItem(divider = True)
        cmds.menuItem("mcdmglb", label = "Miarmy Global...", c = "McdMiarmyGlobalGUI()")
        cmds.menuItem("mcdpxG", label = "Physics Global...", c = "McdPhysicsGlobalGUI()")
        #cmds.menuItem("mcdm01", label = "Disable Solver");
        #cmds.menuItem("mcdm02", label = "Enable Solver");
        #check tool here
        cmds.setParent("..", menu = True)
        #function tools here
        cmds.setParent("..", menu = True)

        cmds.menuItem(divider = True)

        ######################################################
        cmds.menuItem("mcdrndroot", label = "RENDER", subMenu = True, tearOff = True );
        
        cmds.menuItem("mcdmMRnd", label = "Render Global...", c = "McdRenderSettingGUI()");
        cmds.menuItem("mcdsrndfb", label = "Render Preview( 3delight )", c = "McdRenderBegin(-1)" )
        cmds.menuItem(divider = True)
        cmds.menuItem("mcdrndmu", label = "Renderman", subMenu = True, tearOff = True );
        cmds.menuItem("mcdfrgrnd", label = "Foreground Render", c = "McdForgroundRender()")
        cmds.menuItem(divider = True)
        cmds.menuItem("mcdsrnd", label = "Render batch to Image Files", c = "McdRenderBegin(0)" )
        cmds.menuItem("mcdsexrb", label = "Render batch to RIB Files", c = "McdRenderBegin(1)" );
        cmds.menuItem(divider = True)
        cmds.menuItem("mcdexahs", label = "Export Rib Archive Files", c = "McdRenderBegin(1, 1)");
        cmds.menuItem(divider = True)
        cmds.menuItem("mcdexpp", label = "Export Procedural Primitive Assets", c = "McdExportProcPrimAssets()" );
        cmds.menuItem(divider = True)
        #cmds.menuItem("mcdexahgo", label = "Export Rib Archive (Geo Only)", c = "McdRenderBegin(1, 1)");
        #cmds.menuItem("mcdexahs")

        cmds.menuItem("mcdrdatmu", label = "Add/Del Custom Attributes", subMenu = True, tearOff = True );
        cmds.menuItem(divider = True)
        cmds.menuItem("mcdsubd", label = "Add Subd Attribute", c = "McdAddSubdAttr()" )
        cmds.menuItem("mcdcsubd", label = "Delete Subd Attribute", c = "McdDeleteSubdAttr()" )
        cmds.menuItem(divider = True)
        cmds.menuItem("mcddispb", label = "Add Displacement Bound Attribute", c = "McdAddDispBAttr()" )
        cmds.menuItem("mcdcdispb", label = "Delete Displacement Bound Attribute", c = "McdDeleteDispBAttr()" )
        cmds.menuItem(divider = True)
        cmds.menuItem("mcdmtt", label = "Add Matte Attribute", c = "McdAddMatteAttr()" )
        cmds.menuItem("mcdcmtt", label = "Delete Matte Attribute", c = "McdDeleteMatteAttr()" )
        cmds.menuItem(divider = True)
        cmds.menuItem("mcdcum", label = "Add Custom String Attribute", c = "McdAddCustomStringAttr()" )
        cmds.menuItem("mcdccum", label = "Delete Custom String Attribute", c = "McdDeleteCustomStringAttr()" )
        cmds.menuItem(divider = True)
        cmds.menuItem("mcdaagw", label = "Add Geometry Select Weight", c = "McdAddGeoWeightAttr()" )
        cmds.menuItem("mcddagw", label = "Delete Geometry Select Weight", c = "McdDeleteGeoWeightAttr()" )
        cmds.menuItem(divider = True)
        cmds.menuItem("mcdarbaid", label = "Make Texture Random by Agent ID Only", c = "McdAddTexRandMethodToShaderAttr()" )
        cmds.menuItem("mcddrbaid", label = "Remove Texture Random by Agent ID Only", c = "McdDelTexRandMethodToShaderAttr()" )
        cmds.menuItem(divider = True)
        cmds.menuItem("mcdcumsd", label = "Add Shader Hull String Attribute", c = "McdAddShaderHullAttr()" )
        cmds.menuItem("mcddelcumsd", label = "Delete Shader Hull String Attribute", c = "McdDeleteShaderHullAttr()" )
        cmds.setParent("..", menu = True)
        cmds.setParent("..", menu = True)
        
        
        cmds.menuItem("mcdarmain", label = "Arnold", subMenu = True, tearOff = True );
        cmds.menuItem("mcdar_cf", label = "Setup Current Frame", c = "McdARSetupCurrentFrame()")
        cmds.menuItem("mcdar_sq", label = "Setup Scene Sequence", c = "McdARSetupAllFrame()")
        cmds.menuItem(divider = True)
        cmds.menuItem("mcdmr_esf", label = "Export Shader ASS Files", c = "McdMRExportShader()")
        cmds.menuItem(divider = True)
        cmds.menuItem("mcdaddaseed1", label = "Add Agent Seed Attr", c = "McdAddAgentSeedToSelected()")
        cmds.menuItem("mcddelaseed1", label = "Delete Agent Seed Attr", c = "McdDelAgentSeedToSelected()")
        cmds.setParent("..", menu = True)
        
        cmds.menuItem("mcdmrmain", label = "Mental Ray", subMenu = True, tearOff = True );
        cmds.menuItem("mcdmr_cf", label = "Setup Current Frame", c = "McdMRSetupCurrentFrame()")
        cmds.menuItem("mcdmr_sq", label = "Setup Scene Sequence", c = "McdMRSetupAllFrame()")
        cmds.menuItem(divider = True)
        cmds.menuItem("mcdmr_esf", label = "Export Shader MI Files", c = "McdMRExportShader()")
        cmds.menuItem("mcdmr_rsf", label = "Replace MI Shader to Current Setup", c = "McdMRExportAndReplaceShader()")
        cmds.menuItem(divider = True)
        cmds.menuItem("mcdmr_lksq", label = "Link Existed MI Sequence", c = "McdMRLinkMISequence()")
        cmds.menuItem(divider = True)
        cmds.menuItem("mcdmr_clr", label = "Clear MI Files", c = "McdClearMIs()")
        cmds.menuItem(divider = True)
        cmds.menuItem("mcdmr_ei", label = "Enable Update Render View", c = "McdUpdateRenderView(1)")
        cmds.menuItem("mcdmr_di", label = "Diable Update Render View", c = "McdUpdateRenderView(0)")
        cmds.menuItem(divider = True)
        cmds.menuItem("mcdfhmain", label = "Fur/Hair Tools", subMenu = True, tearOff = True );
        cmds.menuItem("mcdfh_exp", label = "Export Selected Fur/Hair", c = "McdExportMRHairFur()")
        cmds.menuItem("mcdfh_imp", label = "Import Selected Fur/Hair", c = "McdImportMRHairFur()")
        cmds.menuItem(divider = True)
        cmds.menuItem("mcdmr_esf", label = "Export Shader ASS Files", c = "McdMRExportShader()")
        cmds.setParent("..", menu = True)
        
        cmds.setParent("..", menu = True)
        
        cmds.menuItem("mcdvrmain", label = "V-Ray", subMenu = True, tearOff = True );
        cmds.menuItem("mcdvr_cf", label = "Setup Current Frame", c = "McdVRSetupCurrentFrame()")
        cmds.menuItem("mcdvr_sq", label = "Setup Scene Sequence", c = "McdVRSetupAllFrame()")
        cmds.menuItem(divider = True)
        cmds.menuItem("mcdvr_rsf", label = "Replace Shader to Current Setup", c = "McdVRReplaceShader()")
        cmds.menuItem(divider = True)
        cmds.menuItem("mcdvr_rtex", label = "Randomize Texture", c = "VRRandomTexture()")
        cmds.menuItem(divider = True)
        cmds.menuItem("mcdvr_clrn", label = "Clear VR Nodes in Scene", c = "McdVRClearVRNodes()")
        cmds.menuItem("mcdvr_clr", label = "Clear VRMesh on Disk", c = "McdVRClearVRMesh()")
        cmds.setParent("..", menu = True)
        
        cmds.menuItem("mcdabcmain", label = "Alembic", subMenu = True, tearOff = True )
        cmds.menuItem("mcdabc_ctc", label = "Create Alembic Cache (All)", c = "McdCreateAlembicCache()")
        cmds.menuItem(divider = True)
        cmds.menuItem("mcdabc_impc", label = "Import Alembic Cache", c = "McdImportAlembicCache()")
        cmds.setParent("..", menu = True)
        
        cmds.menuItem("mcdmd2main", label = "Mesh Drive 2.0", subMenu = True, tearOff = True );
        cmds.menuItem("mcdmd2_exp", label = "Export Cache", c = "McdExportMD2Cache()")
        cmds.menuItem("mcdmd2_setup", label = "Duplicate Meshes and Randomize Texture", c = "MDDuplicate()")
        cmds.menuItem(divider = True)
        cmds.menuItem("mcdmd2_enable", label = "Enable Mesh Drive", c = "McdCreateMeshDriveNode(1, 1)")
        cmds.menuItem("mcdmd2_disable", label = "Disable Mesh Drive", c = "McdCreateMeshDriveNode(0)")
        cmds.menuItem(divider = True)
        cmds.menuItem("mcdmd2_clear", label = "Clear Contents", c = "McdMeshDrive2Clear()")
        cmds.menuItem(divider = True)
        cmds.menuItem("mcdmd2_setbatch", label = "Setup Batch Render MEL", c = "McdSetupBatchRender()")
        cmds.menuItem(divider = True)
        cmds.setParent("..", menu = True)
        
        cmds.menuItem("mcdmd3main", label = "Mesh Drive 3.0", subMenu = True, tearOff = True );
        cmds.menuItem("mcdmd3_exp", label = "Export Cache", c = "McdExportMD2Cache()")
        cmds.menuItem("mcdmd3_stp", label = "Duplicate Meshes and Randomize Texture", c = "MDDuplicate()")
        cmds.menuItem(divider = True)
        cmds.menuItem("mcdmd3_enable", label = "Enable Mesh Drive", c = "McdCreateMeshDriveIMNode(1, 1)")
        cmds.menuItem("mcdmd3_disable", label = "Disable Mesh Drive", c = "McdCreateMeshDriveIMNode(0)")
        cmds.menuItem(divider = True)
        cmds.menuItem("mcdmd3_clear", label = "Clear Contents", c = "McdMeshDrive2Clear()")
        cmds.menuItem(divider = True)

        cmds.menuItem("mcdmd3_show", label = "Show Geometries (Selected)", c = "displayGeoMD()")
        cmds.menuItem("mcdmd3_hide", label = "Hide Geometires", c = "hideGeoMD()")
        cmds.menuItem(divider = True)

        cmds.menuItem("mcdmd2exp", label = "Driven Mesh Exporter", subMenu = True, tearOff = True );
        cmds.menuItem("mcdmd2expmrpms", label = "Export Mesh as MentalRay Proxy (Single Frame)", c = "MDExpandMRProxy(0)")
        cmds.menuItem("mcdmd2expmrpma", label = "Export Mesh as MentalRay Proxy (All Frames)", c = "MDExpandMRProxy(1)")
        cmds.menuItem("mcdmd2expvrpms", label = "Export Mesh as V-Ray vrmesh (Single Frame)", c = "MDExpandVRProxy(0)")
        cmds.menuItem("mcdmd2expvrpma", label = "Export Mesh as V-Ray vrmesh (All Frames)", c = "MDExpandVRProxy(1)")
        cmds.menuItem("mcdmd2expmrrs", label = "Export Mesh as MentalRay Renderable Scene (Single Frame)", c = "MDExpandMRRScene(0)")
        cmds.menuItem("mcdmd2expmrrss", label = "Export Mesh as MentalRay Renderable Scene (All Frames)", c = "MDExpandMRRScene(1)")
        cmds.setParent("..", menu = True)
        
        cmds.menuItem("mcdmd2tex", label = "Driven Mesh Texture Sequence", subMenu = True, tearOff = True );
        cmds.menuItem("mcdmd2texmark", label = "Mark Auto Texture Sequence (shape)", c = "McdMarkAutoTex()")
        cmds.menuItem("mcdmd2texclear", label = "Clear Auto Texture Sequence (shape)", c = "McdClearAutoTex()")
        cmds.menuItem(divider = True)
        cmds.menuItem("mcdmd2texrule", label = "Create Texture Sequence Maker", c = "McdCreateTexSeqRule()")
        cmds.menuItem("mcdmd2texlkact", label = "Link make to action", c = "McdLinkAutoTexAction()")
        cmds.setParent("..", menu = True)
        cmds.menuItem(divider = True)
        cmds.menuItem("mcdmd2shadermap", label = "Driven Mesh Shader Mapping (Selected)", c = "McdShaderMap()")
        
        cmds.menuItem(divider = True)
        cmds.menuItem("mcdrrandtsa", label = "Re-Randomize Texture Select Agent", c = "McdReRandomizeSelAgentTextures()" )
        cmds.menuItem("mcdrandtd", label = "Randomize Textures (Duplicate)", c = "McdRandomizeTexturesDuplicate()" )
        cmds.menuItem("mcdaddaseed", label = "Add Agent Seed Attr", c = "McdAddAgentSeedToSelected()")
        cmds.menuItem("mcddelaseed", label = "Delete Agent Seed Attr", c = "McdDelAgentSeedToSelected()")
        
        cmds.setParent("..", menu = True)
        
        cmds.menuItem(divider = True)
        cmds.menuItem("mcdhlst", label = "Hide List Options", subMenu = True, tearOff = True );
        cmds.menuItem("mcdadd2hl", label = "Add Selected Agents to Hide List", c = "McdHideListAdd()")
        cmds.menuItem("mcddelhl", label = "Clear Hide List", c = "McdHideListClear()")
        cmds.setParent("..", menu = True)
        
        
        cmds.setParent("..", menu = True) # end of renderers
        
    

        cmds.menuItem(divider = True)

        ######################################################
        if int(mel.eval("getApplicationVersionAsFloat")) <= 2010:
            cmds.menuItem("mcdmMAgM", label = "Agent Manager...", c = "McdAgentManagerOldGUI()")
        else:
            cmds.menuItem("mcdmMAgM", label = "Agent Manager...", c = "McdAgentManagerGUI()")
            
        cmds.menuItem("mcdmTerr", label = "Terrain Manager...", c = "McdTerrainManagerGUI()")
        cmds.menuItem("mcdmAgtPt", label = "Particle Emit Manager...", c = "McdAgentParticleEmitterGUI()")
        cmds.menuItem("mcdgvisM", label = "Geometry Hide Manager...", c = "McdGeoVisManagerGUI()")
        cmds.menuItem(divider = True)

        ######################################################
        cmds.menuItem("mcdmViewer", label = "Viewers", subMenu = True, tearOff = True)
        cmds.menuItem("mcdmMAgV", label = "Agent Viewer...", c = "McdAgentViewerGUI()")
        cmds.menuItem("mcdmTrMV", label = "Transition Map Viewer...", c = "McdTransitionMapViewerGUI()")
        cmds.menuItem("mcdmBrLV", label = "Brain Logic Viewer...", c = "McdBrainViewerGUI()")
        cmds.setParent("..", menu = True)
        cmds.menuItem(divider = True)

        ######################################################
        cmds.menuItem("mcdmVis", label = "Agent Visualization", subMenu = True, tearOff = True)
        cmds.menuItem("mcdmSound", label = "Sound Range Switch", c = "soundRangeSwitch()")
        cmds.menuItem("mcdmVision", label = "Vision Range Switch", c = "visionRangeSwitch()")
        cmds.menuItem("mcdmHP", label = "HP/MP Bar Switch", c = "HPSwitch()")
        cmds.menuItem("mcdmAction", label = "Action Info Switch", c = "actionSwitch()")
        cmds.menuItem("mcdmMaster", label = "Master -> Follower Switch", c = "actionSwitch()")
        cmds.menuItem("mcdmSyncWave", label = "Sync Wave Switch", c = "actionSwitch()")
        cmds.menuItem("mcdmSyncIK", label = "Auto IK Handle Switch", c = "actionSwitch()")        
        cmds.setParent("..", menu = True)
        cmds.menuItem(divider = True)

        ######################################################
        cmds.menuItem("mcdm1", label = "Setup Rig", subMenu = True, tearOff = True)
        cmds.menuItem("mcdm12", label = "Import Template", subMenu = True, tearOff = True)
        cmds.menuItem("mcdmcarm", label = "Arm", c = "HbImportTemple('Arm')")
        cmds.menuItem("mcdmcleg", label = "Leg", c = "HbImportTemple('Leg')")
        cmds.menuItem("mcdmcspline", label = "Spine", c = "HbImportTemple('Spline')")
        cmds.setParent("..", menu = True)

        cmds.menuItem("mcdm12pp", label = "Import Template (Preset Pose)", subMenu = True, tearOff = True)
        cmds.menuItem("mcdmcapp", label = "Arm", c = "HbImportTemplePreset('Arm')")
        cmds.menuItem("mcdmclpp", label = "Leg", c = "HbImportTemplePreset('Leg')")
        cmds.menuItem("mcdmcsplpp", label = "Spine", c = "HbImportTemplePreset('Spline')")
        cmds.setParent("..", menu = True)

        cmds.menuItem("mcdm13", label = "Setup Rig", c = "HbSetupWrapper()")
        cmds.menuItem(divider = True)
        cmds.menuItem("mcdm132", label = "Import Standard Bone Tree", c = "McdImportStdBipedBone()")

        # cmds.menuItem("mcdm111", label = "Check Naming")
        # cmds.menuItem("mcdm112", label = "Check Isolate bone")

        cmds.setParent("..", menu = True)
        
        ######################################################
        cmds.menuItem("mcdm4", label = "HumanIK", subMenu = True, tearOff = True)
        cmds.menuItem("mcdAImp", label = "Import Standard Bone Tree", c = "McdImportStdBipedBone()")
        cmds.menuItem("mcdm41", label = "HumanIK (avaliable next time)")
        cmds.menuItem("mcdm42", label = "Characterize (avaliable next time)")
        #check tool here HbImportMaxAnToMaya()
        cmds.setParent("..", menu = True)
        #function tools here
        cmds.setParent("..", menu = True)


        ######################################################
        cmds.menuItem("mcdm2", label = "Original Agents", subMenu = True, tearOff = True)
        cmds.menuItem("mcdmcsgaa", label = "Create Origianl Agent", c = "McdParseRootBoneCreateOAgent(0)")
        cmds.menuItem("mcdmcsgwpp", label = "Create Origianl Agent (Preset Pose)", c = "McdParseRootBoneCreateOAgent(1)")
        cmds.menuItem(divider = True)
        cmds.menuItem("mslupg", label = "Upgrade", c = "McdUpgradeOAgent()")
        cmds.menuItem(divider = True)
        cmds.menuItem("mslskbone", label = "Select Skin Bone and Geo", c = "McdSelectSkinBone()")
        #cmds.menuItem("mslskbs", label = "Bind Skin", c = "McdBindSkinPreset()")

        cmds.menuItem(divider = True)
        cmds.menuItem("hbonebox", label = "Hide Bone Shape", c = "cmds.hide(\"*_dummyShape_*\", \"*_phyJoint_*\")")
        cmds.menuItem("uhbonebox", label = "Unhide Bone Shape", c = "cmds.showHidden(\"*_dummyShape_*\", \"*_phyJoint_*\")")
        cmds.menuItem("mcdmrcsgaa", label = "Re-create Origianl Agent", c = "McdParseRootBoneReCreateOAgent()")
        cmds.menuItem("mcdmdsgaa", label = "Delete Origianl Agent", c = "McdParseRootBoneDeleteOAgent()")
        cmds.menuItem(divider = True)
        cmds.menuItem("mcdcbb", label = "Create Bounding Box for Agent", c = "MakeBoundingBoxForOriginalAgent()")
        cmds.menuItem(divider = True)
        cmds.menuItem("addaiml", label = "Add Aim Rotation Limit Attr", c = "AddAimRotationLimitAttr()")
        cmds.menuItem(divider = True)
        cmds.menuItem("mcdmoarb", label = "Go Original Pose")
        cmds.menuItem(divider = True)
        cmds.menuItem("mcdcgsoa", label = "Send Active Geo to Original Agent", c = "CopyGeoFromSetupAndSkinToOA()")
        cmds.setParent("..", menu = True)
        #function tools here
        cmds.setParent("..", menu = True)


        ######################################################
        cmds.menuItem("mcdmplc", label = "Placement", subMenu = True, tearOff = True)
        cmds.menuItem("mcdmcplcn", label = "Create Placement Node", c = "McdCreatePlacementNode()")
        cmds.menuItem("mcdmcplcnml", label = "Create Placement Node from", subMenu = True, tearOff = True)
        cmds.menuItem("mcdmcplmsh", label = "Mesh", c = "McdCreatePlacementNodeMesh()" )
        cmds.menuItem("mcdmcpllat", label = "Lattice", c = "McdCreatePlacementNodeLattice()" )
        cmds.menuItem(divider = True)
        cmds.menuItem("mcdmcplpt2d", label = "Particle 2D", c = "McdCreatePlacementNodeParticle(0)" )
        cmds.menuItem("mcdmcplpt3d", label = "Particle 3D", c = "McdCreatePlacementNodeParticle(1)" )
        cmds.menuItem(divider = True)
        cmds.menuItem("mcdmcplnpt3d", label = "nParticle 3D", c = "McdCreatePlacementNodeNParticle(1)" )
        
        cmds.setParent("..", menu = True)
        cmds.menuItem(divider = True)
        cmds.menuItem("mcdmplcgui", label = "Placement Editor ...", c = "McdPlacementEditorGUI()") # desiable undo
        cmds.menuItem(divider = True)
        cmds.menuItem("mcdmplace", label = "Place", c = "placementAgent()") # disable undo
        cmds.menuItem("mcdmplcsl", label = "Place (from Selected)", c = "placementAgentFromSelect()") # disable undo
        cmds.menuItem("mcdmdeplace", label = "De-Place (Delete All Agents) ", c = "dePlacementAgent()")
        cmds.menuItem(divider = True)
        cmds.menuItem("mcdmmkoagt", label = "Mark dead selected agents", c = "McdMarkAgentOut()")
        cmds.menuItem(divider = True)
        cmds.menuItem("mcdinvplace", label = "Inverse Place", c = "inversePlacementAgent()")
        cmds.menuItem(divider = True)
        cmds.menuItem("mcddupplace", label = "Duplicate Place Node", c = "duplicatePlacement()")
        cmds.menuItem(divider = True)
        cmds.menuItem("mcdterrain", label = "Attach Terrain", c = "McdAttachTerrain()")
        cmds.menuItem("mcddtrn", label = "Detach Terrain", c = "McdDetachTerrain()")
        cmds.menuItem(divider = True)
        cmds.menuItem("mcdmesh", label = "Attach Range Mesh", c = "McdAttachRangeMesh()")
        cmds.menuItem("mcddmesh", label = "Detach Range Mesh", c = "McdDetachRangeMesh()")
        cmds.menuItem(divider = True)
        cmds.menuItem("mcdcrvbound", label = "Attach Curve", c = "McdAttachCurve()" )
        cmds.menuItem("mcdcrvflw", label = "Detach Curve" )
        cmds.menuItem(divider = True)
        #check tool here

        #function tools here
        cmds.setParent("..", menu = True)

        ######################################################
        cmds.menuItem("mcdm5", label = "Actions", subMenu = True, tearOff = True)
        #cmds.menuItem("mcdCrActall", label = "Action All Control GUI(beta)", c = "McdNewActionMasterGUI()")
        #cmds.menuItem(divider = True)
        cmds.menuItem("mcdCrActs", label = "Create Action", c = "McdCreateActionCmd()")
        cmds.menuItem("mcdActEd", label = "Action Editor...", c = "McdActionEditorGUI()")
        cmds.menuItem(divider = True)
        cmds.menuItem("McdCrActPx", label = "Create Action Proxy", c = "McdCreateActionProxyCmd()")
        cmds.menuItem("mcdActPxEd", label = "Action Proxy Editor...", c = "McdActionProxyEditorGUI()")
        cmds.menuItem(divider = True)
        cmds.menuItem("McdCrStroy", label = "Create Story List", c = "McdCreateStoryListCmd()")
        cmds.menuItem("mcdStoryEd", label = "Story List Editor...", c = "McdStoryListEditorGUI()")
        cmds.menuItem(divider = True)
        cmds.menuItem("mcdActSyEd", label = "Action Synchronization Editor...", c = "McdActionSyncEditorGUI()")
        cmds.menuItem(divider = True)
        cmds.menuItem("mcdClCD", label = "Clear Hook Custom Data", c = "McdClearActionCDCmd()")
        cmds.menuItem(divider = True)
        cmds.menuItem("mcdbactgeo", label = "Bake Gemoetry Action", c = "McdBakeGeoAction()")
        #insert tools here
        cmds.setParent("..", menu = True)
        #function tools here
        cmds.setParent("..", menu = True)

        ######################################################
        cmds.menuItem("mcdm6", label = "Transition Map", subMenu = True, tearOff = True)
        cmds.menuItem("mcdmSAMo", label = "Move Tool", c = "McdStateContextToolOn()")
        cmds.menuItem(divider = True)
        cmds.menuItem("mcdCStat", label = "Create State", c = "McdCreateStateCmd()")
        cmds.menuItem("mcdCAct", label = "Create Action Shell", c = "McdCreateActionShellCmd()")
        cmds.menuItem(divider = True)
        cmds.menuItem("mcdaeag", label = "Add/Edit Action Group", c = "McdAssignActionGrp()")
        cmds.menuItem("mcdcagn", label = "Cancel Action Group", c = "McdCancelActionGrp()")
        cmds.menuItem(divider = True)
        cmds.menuItem("mcdaebag", label = "Add/Edit Blend Group", c = "McdAssignBlendGrp()")
        cmds.menuItem("mcdcbagn", label = "Cancel Blend Group", c = "McdCancelBlendGrp()")


        #function tools here
        cmds.setParent("..", menu = True)

        ######################################################
        cmds.menuItem("mcdmkp", label = "Knowledge Perception", subMenu = True, tearOff = True)
        cmds.menuItem("mcdksspc", label = "Create Solver Space", c = "McdCreateSolverSpace()")
        cmds.menuItem(divider = True)
        cmds.menuItem("mcdkpcc", label = "Create Road From Curve", c = "McdCreateRoad()")
        cmds.menuItem("mcdkpat", label = "Attach Road to Terrain", c = "McdAttachRoadToTerrain()")
        cmds.menuItem("mcdrdmd", label = "Road Mode Switch", subMenu = True, tearOff = True)
        cmds.menuItem("mcdrdmdf", label = "Flow Mode", c = "McdRoadFlowMode(1)")
        cmds.menuItem("mcdrdmdr", label = "Road Mode", c = "McdRoadFlowMode(0)")
        cmds.setParent("..", menu = True)
        cmds.menuItem(divider = True)
        cmds.menuItem("mcd3dp", label = "Create 3D Path", c = "McdCreatePath()")
        cmds.menuItem(divider = True)
        cmds.menuItem("mcdkc", label = "Create Bound", c = "McdCreateBound()")
        cmds.menuItem(divider = True)
        cmds.menuItem("mcdkpcswff", label = "Create Spot + Force Field Combo", c = "McdCreateSpotWithForceField()")
        cmds.menuItem("mcdkpcs", label = "Create Spot", c = "McdCreateSpot()")
        cmds.menuItem("mcdkpcff", label = "Create Force Field", c = "McdCreateSpotOnlyForceField()")
        cmds.menuItem(divider = True)
        cmds.menuItem("mcdkpwind", label = "Create Wind", c = "McdCreateWind()")
        cmds.menuItem(divider = True)
        cmds.menuItem("mcdkpcz", label = "Create Zone", c = "McdCreateZone()")
        cmds.menuItem("mcdkpgzn", label = "Select Zone Node", c = "McdGetZoneNode()")
        cmds.menuItem(divider = True)
        cmds.menuItem("mcdvarm", label = "Variables", subMenu = True, tearOff = True)
        cmds.menuItem("mcdvarh", label = "Create Agent Variable Host", c = "McdVarHostCreate()")
        cmds.menuItem("mcdvara", label = "Agent Variable Manager...", c = "McdVarManagerGUI()")
        cmds.menuItem("mcdvarlk", label = "Agent Variable Host Linker...", c = "McdGroupVarEditorGUI()")
        cmds.menuItem(divider = True)
        cmds.menuItem(divider = True)
        cmds.menuItem("mcdvargc", label = "Create Variable Proxy Node", c = "McdCreateGroupVar()")
        cmds.menuItem("mcdvarapx", label = "Variable Proxy Manager...", c = "McdVarPxyManagerGUI()")
        cmds.menuItem("mcdvarge", label = "Variable Proxy Linker...", c = "McdGroupVarEditorGUI()")
        cmds.setParent("..", menu = True)
        cmds.menuItem(divider = True)
        cmds.menuItem("mcdfmtatt", label = "Mark Formation Flag", c = "McdMarkFormation()")
        cmds.menuItem("mcdfmtael", label = "Select Associate Formation Node", c = "McdSelectFormation()")
        #check tool here
        cmds.setParent("..", menu = True)
        #function tools here
        cmds.setParent("..", menu = True)

        ######################################################
        cmds.menuItem("mcdm7", label = "Logic and Decision", subMenu = True, tearOff = True)
        cmds.menuItem("mcdCrDes", label = "Make Decision", c = "McdCreateDecisionCmd()")
        cmds.menuItem("mcdLgcV", label = "DecisionNode Editor ...", c = "McdDecisionEditorGUI()")
        cmds.menuItem(divider = True)
        cmds.menuItem("mcdLgPst", label = "Preset Logic Behavior" , subMenu = True, tearOff = True)
        cmds.menuItem("mcdLgPst1", label = "Blank Priority", c = "McdPLB_BlankPriority()")
        cmds.menuItem("mcdLgPst2_", label = "Avoid Collide by Sound (simple)", c = "McdPLB_collideAvoidSoundSimple()")
        cmds.menuItem("mcdLgPst3", label = "Avoid Spot", c = "McdPLB_AvoidSpot()")
        cmds.menuItem("mcdLgPst4", label = "Follow Spot", c = "McdPLB_FollowSpot()")
        cmds.menuItem("mcdLgPst5", label = "Follow Field", c = "McdPLB_FollowField()")
        cmds.menuItem("mcdLgPst6", label = "BlockVision if in bound", c = "McdPLB_InBoundBlkVis()")
        cmds.menuItem("mcdLgPst7", label = "Follow Terrain", c = "McdPLB_FollowTerrain()")
        cmds.menuItem("mcdLgPst8", label = "Follow RoadFlow", c = "McdPLB_RoadFlow()")
        cmds.menuItem("mcdLgPst9", label = "Follow Road", c = "McdPLB_Road()")
        cmds.menuItem("mcdLgPst2", label = "Avoid Collide by Sound (complex action)", c = "McdPLB_collideAvoidSound()")
        cmds.setParent("..", menu = True)
        
        cmds.menuItem(divider = True)
        cmds.menuItem("mcdLgSave", label = "Save Logic", c = "McdSaveLogic()")
        cmds.menuItem("mcdLgLoad", label = "Load Logic", c = "McdLoadLogic()")
        
        cmds.setParent("..", menu = True)
        #function tools here
        cmds.setParent("..", menu = True)


        ######################################################
        cmds.menuItem("mcdm8", label = "Physics", subMenu = True, tearOff = True)
        cmds.menuItem("mcdmoas", label = "Clothes", subMenu = True, tearOff = True)
        # physx function here
        cmds.menuItem(divider = True)
        cmds.menuItem("mcdmattc", label = "Attach Cloth (Select Pin Points)", c = "McdAttachClothCmd()")
        cmds.menuItem("mcdclrclo",label = "Clear Cloth", c = "McdClearCloth()")
        cmds.menuItem(divider = True)
        #cmds.menuItem("mcdmcltmr", label = "Cloth Manager...", c = "McdClothManagerGUI()")
        #cmds.menuItem(divider = True)
        cmds.menuItem("mcdclothp", label = "Cloth Presets", subMenu = True, tearOff = True)
        cmds.menuItem("mcdclada", label = "Flag", c = "McdClothPresetFlag()")
        cmds.menuItem("mcdcldea", label = "Cloak", c = "McdClothPresetCloak()")
        cmds.setParent("..", menu = True)
        cmds.setParent("..", menu = True)
        cmds.menuItem("mcdffi", label = "Force Fields", subMenu = True, tearOff = True)
        cmds.menuItem("mcdcffp",label = "Create Push Field", c = "createPxPushFF()")
        cmds.menuItem("mcdcffl",label = "Create Pull Field", c = "createPxPullFF()")
        cmds.menuItem("mcdcffv",label = "Create Vortex Field", c = "createPxVortexFF()")
        cmds.setParent("..", menu = True)
        cmds.menuItem("mcdkpr", label = "Kinematic Primitives", subMenu = True, tearOff = True)
        cmds.menuItem("mcdckpb",label = "Create Box Kine Prim", c = "createPxKineBox()")
        cmds.menuItem("mcdckps",label = "Create Sphere Kine Prim", c = "createPxKineSphere()")
        cmds.menuItem("mcdmkkpm",label = "Mark Kine Prim Mesh", c = "createMarkKineMesh()")
        cmds.setParent("..", menu = True)
        cmds.menuItem("mcdrbd", label = "RBD Emitter", subMenu = True, tearOff = True)
        cmds.menuItem("mcdcrbdps",label = "Create RBD Emitter", c = "createPxRBDEmitter()")
        cmds.menuItem("mcdmAgtrbd", label = "Agent RBD Emit Editor...", c = "McdAgentRBDEmitterGUI()")
        cmds.menuItem(divider = True)
        cmds.menuItem("mcdbkrbd",label = "Bake RBD Emitter", c = "BakeRBDObjects()")
        cmds.setParent("..", menu = True)
        cmds.menuItem(divider = True)
        cmds.menuItem("mcdddb",label = "Create PhysX Debug Node", c = "")
        #function tools here
        cmds.setParent("..", menu = True)

        ######################################################
        cmds.menuItem("mcdm9", label = "Debug Tools", subMenu = True, tearOff = True)
        cmds.menuItem("mcdam",label = "Agent Match", c = "oAgentMatchAgent()")
        cmds.menuItem("mcdar",label = "Agent Return", c = "oAgentResume()")
        cmds.menuItem(divider = True)
        cmds.menuItem("mcdcpdn",label = "Create PhysX Debug Node", c = "createPhyDebugNode()")
        cmds.menuItem(divider = True)
        cmds.menuItem("mcdtrag1",label = "Agent -> Group Info", c = "McdFromAgentToAgentGroup(True)")
        cmds.menuItem("mcdtrpl1",label = "Agent -> Place Node", c = "McdFromAgentToPlace(True)")
        cmds.menuItem(divider = True)
        cmds.menuItem("mcdckshader",label = "Mesh Drive 3.0 Shader", c = "McdCheckShaderForMD3()")


        #function tools here
        cmds.setParent("..", menu = True)

        ######################################################
        cmds.menuItem(divider = True)
        cmds.menuItem("mcdmsva", label = "Export Agent", c = "McdExportAgent()")
        cmds.menuItem("mcdmsvaws", label = "Select Global, Contents", c = "McdExportMiarmyAll()")
        cmds.setParent("..", menu = True)

        cmds.menuItem(divider = True)
        cmds.menuItem("mcdmInst", label = "Installation", subMenu = True, tearOff = True)
        cmds.menuItem("mcdmIns", label = "Re-Link Miarmy", c = "miarmyInstallWin()")
        cmds.menuItem("mcdmUnin", label = "Un-Link Miarmy", c = "McdUnlinkMiarmy()")
        cmds.menuItem("mcdRdF", label = "3delight Setup", subMenu = True, tearOff = True)
        cmds.menuItem("mcdmdlce", label = "Check Renderer Status", c = "McdCheckRendererStatus()")
        cmds.menuItem("mcdmdlcs", label = "Compile Shaders", c = "McdCompileShaders()")
        cmds.menuItem("mcdmDelit", label = "Remove 3Delight.dll", c = "McdRemoveDelight()")
        cmds.setParent("..", menu = True)
        cmds.setParent("..", menu = True)
        cmds.menuItem("mcdmHelp", label = "Help", c = 'cmds.launch(web="http://www.mayacrowd.com")')
        cmds.menuItem("mcdmAbout", label = "About Miarmy", c = "McdAboutMiarmy()")

    except:
        print "Initialize menu skipped or failed."


def McdAboutMiarmy():
    cmds.confirmDialog(t = "About Basefount Miarmy", m = "Miarmy For Maya Plugin \n\n\
                            Version: Miarmy(R) 2.5 \n\n\
                            Basefount Technology Limited.\n\n\
                            2011-2013(C) All rights reserved.\n\
                            (EN) www.basefount.com\n\
                            (CH) www.basefount.net")


