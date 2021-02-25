import maya.cmds as cmds
import maya.mel as mel

def select_command():
    text_scroll_list_select = cmds.textScrollList("textScrollList", si=True, q=True)
    cmds.select(text_scroll_list_select)

def get_controller_list_in_anim_file(scene_path):
    controller_list_in_anim_file = []
    file = open(scene_path, 'r')
    content = file.read()
    file.close()
    content_split = content.split('"c_')  
    for content_part in content_split:
        controller_name_in_anim_file = "c_" + content_part.split('"')[0]
        if (controller_list_in_anim_file.count(controller_name_in_anim_file) == 0 and
            controller_name_in_anim_file.find("Shape") == -1 and 
            controller_name_in_anim_file.find(".") == -1):
            controller_list_in_anim_file.append(controller_name_in_anim_file)
    return controller_list_in_anim_file

def get_controller_list_not_in_anim_and_render(transform_list, controller_list_in_anim_file ):
    controller_name_in_anim_not_in_render = list(controller_list_in_anim_file) 
    controller_name_in_render_not_in_anim = []
    for transform in transform_list:
        transform_name_in_render_scn = transform.split("|")[-1]
        if transform_name_in_render_scn.find("c_") == 0:
            if controller_list_in_anim_file.count(transform_name_in_render_scn) == 0: 
                controller_name_in_render_not_in_anim += [transform_name_in_render_scn] 
            else:
                controller_name_in_anim_not_in_render.remove(transform_name_in_render_scn)
    return [controller_name_in_render_not_in_anim, controller_name_in_anim_not_in_render]
 
def open_textscrolllist(windows_name, title, content_list, select= False):
    if (cmds.window(windows_name, exists=True)):
            cmds.deleteUI(windows_name)
    cmds.window(windows_name, title=title)
    cmds.paneLayout()
    if select :
        cmds.textScrollList("textScrollList", numberOfRows=8, allowMultiSelection=True,
                                append=content_list,
                                selectCommand=select_command )
    else:
        cmds.textScrollList("truc", numberOfRows=8, allowMultiSelection=True,
                                append=content_list
                                 )
    cmds.showWindow()

def controller_without_tt_visibility_list(transform_list):
    controllers_without_ttvisibility=[]
    for transform in transform_list:
            if transform.split("|")[-1].find("c_") == 0:
                if not cmds.attributeQuery("tt_visibility",node=transform, exists=True):
                    controllers_without_ttvisibility.append(transform.split("|")[-1])
    return controllers_without_ttvisibility

def controller_that_not_exists_list(transform_list):
    no_match_name = []
    for transform in transform_list:
            if not cmds.objExists(transform) and transform.split("|")[-1].find("c_") == 0:
                no_match_name += [transform.split("|")[-1]] 
    return no_match_name
    
def check_integrity_between_scenes_with_switch_scene():
    """
    Open the anim scene and select the top node before use this function.
    """
    selected_object = cmds.ls(l=True, sl=True)
    controllers_without_ttvisibility = ["Controllers Without TT Visibility In Anim File:"]
    controllers_without_ttvisibility.append("")
    if len(selected_object) == 1:
        transform_list = cmds.listRelatives(selected_object, allDescendents=True, fullPath=True, type="transform")
        controllers_without_ttvisibility += controller_without_tt_visibility_list(transform_list)
        mel.eval("projectViewer Open;")
        no_match_name = []
        controllers_without_ttvisibility.append("")
        controllers_without_ttvisibility.append("Controllers Without TT Visibility In Render File:")
        controllers_without_ttvisibility.append("")
        no_match_name = controller_that_not_exists_list(transform_list) 
        transform_list = cmds.ls(l=True, type="transform")
        controllers_without_ttvisibility += controller_without_tt_visibility_list(transform_list)             
        open_textscrolllist("No_Match_Names", "No_Match_Names or Hierarchy", no_match_name)
        open_textscrolllist("controllers_without_ttvisibility", "Controller wihtout tt_visibility", controllers_without_ttvisibility)

    else:
        result = cmds.confirmDialog(title='Warning',
                                     message="Select a top node.",
                                     button=['Close'])
                                     
check_integrity_between_scenes_with_switch_scene()