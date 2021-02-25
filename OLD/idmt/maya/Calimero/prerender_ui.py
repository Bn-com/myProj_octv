import sys
import maya.cmds as cmds
import maya.mel as mel
import os.path
current_dir = os.path.dirname(__file__)
#current_dir = 'M:/CAL_RSYNC/renderstore/CAL_RENDER/Prerender'
sys.path.append(current_dir )
sys.path.append(current_dir + "/TOOLS/Maya_Shelf_Buttons")
import slk_renderLayer_CalimeroXE_v2_5 as slk
import GRP_BUTTON as grp_button
reload(slk)
reload(grp_button)

def prerender_button(*args):
    clr = slk.cllRLConfig(correctTexturesAndSave=True)
    clr.cllRLAutoCreate()
    
def create_asset_group(*args):
    grp_button.create_group()
    
def exclude_selection_of_the_occlusion(*args):
    import maya.cmds as cmds
    selection_list = cmds.ls(sl=True, long=True)
    for selection in selection_list:
        if not cmds.attributeQuery( 'miLabel', node=selection, exists=True ):
            cmds.addAttr(selection, ln='miLabel', attributeType='long', dv=1 )
            cmds.setAttr(selection+".miLabel", keyable=True)
    
def light_set_import_button(*args):
    light_set_import.light_set_import()
    
def ftm(*args):
    mel.eval('source "' + current_dir + '/TOOLS/FTM/FileTextureManager.mel";FileTextureManager;')

def create_character_alpha_set(*args):
    selection_list = cmds.ls(sl=True)
    if selection_list is not None:
        if cmds.objExists("STAGE_CH_ALPHA"):
            cmds.sets( edit=True, forceElement="STAGE_CH_ALPHA")
        else:
            cmds.sets(name="STAGE_CH_ALPHA")
        
def create_character_alpha_set(*args):
    selection_list = cmds.ls(sl=True)
    if selection_list is not None:
        if cmds.objExists("CHARACTER_ALPHA"):
            cmds.sets( edit=True, forceElement="CHARACTER_ALPHA")
        else:
            cmds.sets(name="CHARACTER_ALPHA")

def create_volumetric_set(*args):
    selection_list = cmds.ls(sl=True)
    if selection_list is not None:
        name = prompt()
        set_name = name + "_VOLUMETRIC"
        if cmds.objExists(set_name + "_VOLUMETRIC"):
            cmds.sets( edit=True, forceElement=set_name)
        else:
            cmds.sets(name=set_name)
   
def create_specific_alpha_set(*args):
    selection_list = cmds.ls(sl=True)
    if selection_list is not None:
        name = prompt()
        set_name = name + "_ALPHA"
        if cmds.objExists(set_name):
            cmds.sets( edit=True, forceElement=set_name)
        else:
            cmds.sets(name=set_name)
def primary_visibility_on(*args):
    selection_list = cmds.ls(sl=1)
    print selection_list
    for selection in selection_list:
        try:
            cmds.setAttr( selection + '.primaryVisibility', 1)
            print selection + '_Done'
        except:
            print selection + '_Not Done'

def primary_visibility_off(*args):
    selection_list = cmds.ls(sl=1)
    print selection_list
    for selection in selection_list:
        try:
            cmds.setAttr( selection + '.primaryVisibility', 0)
            print selection + '_Done'
        except:
            print selection + '_Not Done'
            
def create_exclude_set(*args):
    selection_list = cmds.ls(sl=True)
    if selection_list is not None:
        name = cmds.textScrollList( "scroll" ,query=True, si=True)
        set_name = name[0] + "_EXCLUDE"
        if cmds.objExists(set_name):
            cmds.sets( edit=True, forceElement=set_name)
        else:
            cmds.sets(name=set_name)
        
def set_scroll_list(*args):
    from functools import partial
    all_set_list = cmds.ls(sets=True)
    set_list = []
    for set in all_set_list:
        if ("_ALPHA" in set or "_VOLUMETRIC" in set) and not "_EXCLUDE" in set:
            set_list.append(set)
    window = cmds.window(title='Select a Base Name For The Exclude Set')
    cmds.rowColumnLayout(  numberOfRows=2 )
    cmds.textScrollList( "scroll" , numberOfRows=8, allowMultiSelection=True,
                            append=set_list,
                            showIndexedItem=4 )
    b1 = cmds.button(l='OK', c=create_exclude_set)
    cmds.showWindow()
  
def prompt():
    text = ""
    result = cmds.promptDialog(
                title='Name of the specific_set',
                message='Enter Name:',
                button=['OK', 'Cancel'],
                defaultButton='OK',
                cancelButton='Cancel',
                dismissString='Cancel')
    if result == 'OK':
            text = cmds.promptDialog(query=True, text=True)      
    return text

def MipMap_to_Quadratic(*args): 
    list_file = cmds.ls(l=True, type="file")
    for file in list_file:
        filter_type = cmds.getAttr(file + ".filterType")
        if filter_type == 1:
            cmds.setAttr(file + ".filterType",3)
            
def MipMap_to_off(*args): 
    list_file = cmds.ls(l=True, type="file")
    for file in list_file:
        filter_type = cmds.getAttr(file + ".filterType")
        if filter_type == 1:
            cmds.setAttr(file + ".filterType",0)

def Quadratic_to_off(*args): 
    list_file = cmds.ls(l=True, type="file")
    for file in list_file:
        filter_type = cmds.getAttr(file + ".filterType")
        if filter_type == 3:
            cmds.setAttr(file + ".filterType",0)

def show_ui():
    if (cmds.window("Prerender_ui", exists=True)):
        cmds.deleteUI("Prerender_ui")
    cmds.window("Prerender_ui",title="Prerender_ui",
                resizeToFitChildren=True )
    cmds.scrollLayout( verticalScrollBarThickness=16,width = 276,height = 390)
    cmds.columnLayout()
    cmds.frameLayout( label='Prerender', borderStyle='out', width = 250, bgc=(0.3, 0.3, 0.6))
    cmds.button(label = 'Prerender', command = prerender_button, annotation="prerender" )
    cmds.frameLayout( label='Prerender tools', borderStyle='out', width = 250, bgc=(0.6, 0.3, 0.3))
    cmds.button(label = 'Create Asset Group', command = create_asset_group, annotation="Create asset group " )
    cmds.button(label = 'Exclude The Selection From The Occlusion', command = exclude_selection_of_the_occlusion, annotation="add miLabel 1 to the selection" )
    cmds.button(label = 'Primary Visibility ON', command = primary_visibility_on , annotation="set the attribute primary visibility of the selection to True" )
    cmds.button(label = 'Primary Visibility OFF', command = primary_visibility_off , annotation="set the attribute primary visibility of the selection to False" )
    cmds.button(label = 'FTM', command = ftm , annotation="file texture manager" )
    cmds.frameLayout( label='Switch Texture Filter', borderStyle='out', width = 250, bgc=(0.3, 0.6, 0.6))
    cmds.button(label = 'MipMap --> Quadratic', command = MipMap_to_Quadratic, annotation="Change the filter type from MipMap to Quadratic" )
    cmds.button(label = 'MipMap --> Off', command = MipMap_to_off, annotation="Change the filter type from MipMap to Off" )
    cmds.button(label = 'Quadratic --> Off', command = Quadratic_to_off, annotation="Change the filter type from Quadratic to Off" )
    cmds.frameLayout( label='Create Prerender Set', borderStyle='out', width = 250, bgc=(0.3, 0.6, 0.3))
    cmds.button(label = 'CHARACTER ALPHA', command = create_character_alpha_set , annotation="create_character_alpha_set" )
    cmds.button(label = 'SPECIFIC ALPHA', command = create_specific_alpha_set , annotation="create_specific_alpha_set" )
    cmds.button(label = 'VOLUMETRIC', command = create_volumetric_set , annotation="create_character_alpha_set" )
    cmds.button(label = 'EXCLUDE', command = set_scroll_list , annotation="create_exclude_set" )
    cmds.showWindow()
