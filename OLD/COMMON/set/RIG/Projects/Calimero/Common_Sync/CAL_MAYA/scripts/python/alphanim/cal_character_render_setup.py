'''
this script search and select surfaceshader and writetocolorbuffer by color.
'''

import maya.cmds as cmds

__author__  = 'Dimitri Gouacide'
__version__ = '1.0'
__date__    = '2013-05-07'

color_layout = ""
no_colorid_list = []
no_pure_colorid_list = []
def get_surfaceshader_writetocolorbuffer_with_color():
    global color_layout
    shader_list = cmds.ls(l=True, type="surfaceShader")
    color_search = cmds.colorSliderButtonGrp(color_layout, rgbValue = True, q = True )
    R = color_search[0]
    G = color_search[1]
    B = color_search[2]
    return_surfaceshader_list = []
    for shader in shader_list:
        color = cmds.getAttr(shader + ".outColor")    
        red = float(color[0][0])
        green = float(color[0][1])
        blue = float(color[0][2])
        if R == red and G == green and B == blue:
            return_surfaceshader_list.append(shader)
    shader_list = cmds.ls(l=True, type="writeToColorBuffer")
    color_search = cmds.colorSliderButtonGrp(color_layout, rgbValue = True, q = True )
    R = color_search[0]
    G = color_search[1]
    B = color_search[2]
    return_writetocolorbuffer_list = []
    for shader in shader_list:
        print shader
        color = cmds.getAttr(shader + ".color")    
        red = float(color[0][0])
        green = float(color[0][1])
        blue = float(color[0][2])
        if R == red and G == green and B == blue:
            return_writetocolorbuffer_list.append(shader)    
    if len(return_writetocolorbuffer_list) != 0 or len(return_surfaceshader_list) != 0:
        text = ""
        if len(return_surfaceshader_list) != 0:
            text += "Surface Shader Found:\n\n"
            for return_shader in return_surfaceshader_list:
                text += return_shader + "\n"
        text += "\n"
        if len(return_writetocolorbuffer_list) != 0:
            text += "WriteToColorBuffer Found:\n\n"
            for return_shader in return_writetocolorbuffer_list:
                text += return_shader + "\n"
        result = cmds.confirmDialog( title='Finished', message=text, button=['Select'] )
        if(result == "Select"):
            cmds.select(return_writetocolorbuffer_list + return_surfaceshader_list)
    else:
        result = cmds.confirmDialog( title='Finished', message="No Shader Found", button=['Confirm'] )
        
def open_hypershade():   
    if not cmds.objExists("hyperShadePanel"):
        cmds.HypershadeWindow()    
        
def check_color_id(arg):
    global no_colorid_list
    global no_pure_colorid_list
    no_colorid_list = []
    no_pure_colorid_list = []
    wrong_shader_naming = []
    shader_list = cmds.ls(l=True, materials=True)
    for shader in shader_list:
        if shader.find("_RGB") != -1 or shader.find("_RGBA") != -1:
            destination_list = cmds.connectionInfo(shader + ".outColor",
                                destinationFromSource = True) 
            count_color_id = 0
            if shader.find("_RGB1") == -1 and shader.find("_RGBA1") == -1:
                for destination in destination_list:
                    if (destination.find("ColorID_CHR") != -1 or (destination.find("ColorID") != -1 and destination.find("_CHR")==-1)) and destination.find("ColorID1")==-1 and destination.find("ColorID_CHR1")==-1:
                        count_color_id += 1
                        destination_name = destination.split(".")[0]
                        source_destination = cmds.connectionInfo(destination_name + ".color",
                                sourceFromDestination = True)
                        source_destination_name = source_destination.split(".")[0]
                        color = ""
                        if source_destination_name != "":
                            if cmds.objectType(source_destination_name) == "multiplyDivide":
                                source_muliply = cmds.connectionInfo(source_destination_name + ".input1",
                                    sourceFromDestination = True)
                                source_muliply_name = source_muliply.split(".")[0]
                                if cmds.objectType(source_muliply_name) == "surfaceShader" and source_muliply_name.find("_ID") !=0 :                                
                                    if (destination_name.find("ColorID") != -1 and destination_name.find("_CHR") == -1):
                                        cmds.setAttr(source_muliply_name + ".outColor", 1, 0, 0)
                                    color = cmds.getAttr(source_muliply_name + ".outColor")  
                        else:                       
                            if (destination_name.find("ColorID") != -1 and destination_name.find("_CHR") == -1):
                                cmds.setAttr(destination_name + ".color", 1, 0, 0)
                            color = cmds.getAttr(destination_name + ".color")  
                        red = float(color[0][0])
                        green = float(color[0][1])
                        blue = float(color[0][2])
                        print str(red)+","+str(green)+","+str(blue)
                        # if not(red == 0.0 or red == 1.0) or not(green == 0.0 or green == 1.0) or not(blue == 0.0 or blue == 1.0) and destination.find("ColorID_CHR") != -1                       
                        if not(red == 1.0 and green == 0.0 and blue == 0.0) and not(red == 0.0 and green == 1.0 and blue == 0.0) and not(red == 0.0 and green == 0.0 and blue == 1.0) :
                            no_pure_colorid_list.append(destination_name)
            if(count_color_id <2):
                if shader.find("_RGB1") == -1 and shader.find("_RGBA1") == -1:
                    no_colorid_list.append(shader)
                else:
                    wrong_shader_naming.append(shader)
                    
    print no_colorid_list         
    print no_pure_colorid_list
    if len(no_colorid_list) != 0 or len(no_pure_colorid_list)!=0:
        if (cmds.window("ColorID_Error_List", exists=True)):
                cmds.deleteUI("ColorID_Error_List")
        cmds.window("ColorID_Error_List", title = "ColorID Error List")
        cmds.paneLayout()
        text_textscroll_list=[]
        if len(no_colorid_list) != 0:
            text_textscroll_list += ["Select Shader_rgb without ColorID:", ""] + no_colorid_list
        if len(no_pure_colorid_list) != 0:
            text_textscroll_list += ["", "", "Select not pure colorID (R,G,B):", ""] + no_pure_colorid_list
        if len(wrong_shader_naming) != 0:
            text_textscroll_list += ["", "", "Wrong Shader Naming :", ""] + wrong_shader_naming         
        cmds.textScrollList("textScrollList", numberOfRows=8, allowMultiSelection=True,
                                append=text_textscroll_list,
                                selectCommand=select_command)
        cmds.showWindow()
        open_hypershade()
    else :
        if (cmds.window("ColorID_Error_List", exists=True)):
            cmds.deleteUI("ColorID_Error_List")
        result = cmds.confirmDialog(title='Finished',
                                     message="OK",
                                     button=['Close'])
def select_command():
    text_scroll_list_select=cmds.textScrollList("textScrollList",si=True,q=True)
    temp_list=[]
    for text_scroll in text_scroll_list_select:
        if text_scroll != "" and text_scroll != "Select Shader_rgb without ColorID:" and text_scroll != "Select not pur ColorID:":
            temp_list.append(text_scroll)
    if(len(temp_list) != 0):
        cmds.select(temp_list)

def select_colorid_red(arg):
    open_hypershade()
    shader_list = cmds.ls(l=True, materials=True)
    red_colorid_list=[]
    red_colorid_shader_list=[]
    for shader in shader_list:
        if shader.find("_RGB") != -1 or shader.find("_RGBA") != -1:
            destination_list = cmds.connectionInfo(shader + ".outColor",
                                destinationFromSource = True) 
            count_color_id = 0
            for destination in destination_list:
                if destination.find("ColorID_CHR") != -1 :
                    count_color_id += 1
                    destination_name = destination.split(".")[0]
                    color = cmds.getAttr(destination_name + ".color")    
                    red = float(color[0][0])
                    green = float(color[0][1])
                    blue = float(color[0][2])
                    print str(red)+","+str(green)+","+str(blue)
                    if ( red == 1.0) and (green == 0.0 ) and (blue == 0.0 ):
                        red_colorid_list.append(destination_name)
                        red_colorid_shader_list.append(shader)
    if len(red_colorid_shader_list) !=0:
        cmds.select(red_colorid_shader_list)
        cmds.hyperShade(objects="")
    if len(red_colorid_list) !=0:
        cmds.select(red_colorid_list, add=True)
    
    
def select_colorid_green(arg):
    open_hypershade()
    shader_list = cmds.ls(l=True, materials=True)
    green_colorid_list=[]
    green_colorid_shader_list=[]
    for shader in shader_list:
        if shader.find("_RGB") != -1 or shader.find("_RGBA") != -1:
            destination_list = cmds.connectionInfo(shader + ".outColor",
                                destinationFromSource = True) 
            count_color_id = 0
            for destination in destination_list:
                if destination.find("ColorID_CHR") != -1 :
                    count_color_id += 1
                    destination_name = destination.split(".")[0]
                    color = cmds.getAttr(destination_name + ".color")    
                    red = float(color[0][0])
                    green = float(color[0][1])
                    blue = float(color[0][2])
                    print str(red)+","+str(green)+","+str(blue)
                    if ( red == 0.0) and (green == 1.0 ) and (blue == 0.0 ):
                        green_colorid_list.append(destination_name)
                        green_colorid_shader_list.append(shader)
    if len(green_colorid_shader_list) !=0:
        cmds.select(green_colorid_shader_list)
        cmds.hyperShade(objects="")
    if len(green_colorid_list) !=0:
        cmds.select(green_colorid_list, add=True)
    
def set_colorid_red(arg):
    shader_list = cmds.ls(sl=True, l=True, materials=True)
    if len(shader_list)== 0:
        cmds.hyperShade(shaderNetworksSelectMaterialNodes = True)
        shader_list = cmds.ls(sl=True, l=True, materials=True)
    for shader in shader_list:
        if shader.find("_RGB") != -1 or shader.find("_RGBA") != -1:
            destination_list = cmds.connectionInfo(shader + ".outColor",
                                destinationFromSource = True)
            for destination in destination_list:
                if destination.find("ColorID_CHR") != -1:
                    destination_name = destination.split(".")[0]
                    color = cmds.setAttr(destination_name + ".color", 1.0, 0.0, 0.0) 
        elif shader.find("ColorID_CHR") != -1:
            color = cmds.setAttr(shader + ".color", 1.0, 0.0, 0.0)    

def set_colorid_green(arg):
    shader_list = cmds.ls(sl=True, l=True, materials=True)
    if len(shader_list)== 0:
        cmds.hyperShade(shaderNetworksSelectMaterialNodes = True)
        shader_list = cmds.ls(sl=True, l=True, materials=True)
    for shader in shader_list:
        if shader.find("_RGB") != -1 or shader.find("_RGBA") != -1:
            destination_list = cmds.connectionInfo(shader + ".outColor",
                                destinationFromSource = True)
            for destination in destination_list:
                if destination.find("ColorID_CHR") != -1:
                    destination_name = destination.split(".")[0]
                    color = cmds.setAttr(destination_name + ".color", 0.0, 1.0, 0.0) 
        elif shader.find("ColorID_CHR") != -1:
            color = cmds.setAttr(shader + ".color", 0.0, 1.0, 0.0)
            
def set_meshes_renderstats(arg):
    cmds.select("smooth2", r=True, ne = True)
    cmds.select(hierarchy = True)
    selection_list = cmds.ls(sl=True)
    text = "Meshes Renderstats Set on :\n"
    for selected in selection_list:
        text+=selected+"\n"
        cmds.setAttr( selected + ".displaySmoothMesh", 2)
        cmds.setAttr( selected + ".useSmoothPreviewForRender", 0)
        cmds.setAttr( selected + ".renderSmoothLevel", 2)
        cmds.setAttr( selected + ".receiveShadows", 1)
        if selected.find("msh") != -1 and selected.find("spec") != -1:
            cmds.setAttr( selected + ".castsShadows", 0)
        else:
            cmds.setAttr( selected + ".castsShadows", 1)
    
    result = cmds.confirmDialog(title = 'Finished',
                                 message=text,
                                 button=['Close'])
                                 
def character_render_setup_ui():
    global color_layout   
    if (cmds.window("Characters_Render_Setup", exists=True)):
        cmds.deleteUI("Characters_Render_Setup")
    cmds.window("Characters_Render_Setup",title="Characters Render Setup v"+__version__, resizeToFitChildren=True )   
    cmds.columnLayout()
    cmds.frameLayout( label='ColorID Setup', borderStyle='out', width = 300)
    # color_layout = cmds.colorSliderButtonGrp( label='Color', buttonLabel='search', rgb=(1, 0, 1), symbolButtonDisplay=True, columnWidth=(5, 30), buttonCommand=get_surfaceshader_writetocolorbuffer_with_color )
    cmds.button(label = 'Check ColorID / Shader Names', command = check_color_id, bgc=(0.3, 0.8, 0.3) )
    cmds.button(label = 'Select ColorID_CHR RED ', command = select_colorid_red)
    cmds.button(label = 'Select ColorID_CHR GREEN', command = select_colorid_green )
    cmds.separator(style='none')
    cmds.button(label = 'Set ColorID_CHR Selected to RED  (Skin)', command = set_colorid_red )    
    cmds.button(label = 'Set ColorID_CHR Selected to GREEN (Clothes/Accessories)', command = set_colorid_green )
    cmds.text(label = '' )
    cmds.text(label = '' )
    cmds.frameLayout( label='Meshes Renderstats Setup', borderStyle='out' )
    cmds.text(label = '' )
    cmds.button(label = 'Set Meshes Renderstats', command = set_meshes_renderstats )
    cmds.showWindow()
    
    