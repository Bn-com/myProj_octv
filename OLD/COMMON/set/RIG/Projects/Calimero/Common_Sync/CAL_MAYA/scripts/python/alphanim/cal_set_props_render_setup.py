'''
this script search and select surfaceshader and writetocolorbuffer by color.
'''

import maya.cmds as cmds
import cal_miLabel
__author__ = 'Dimitri Gouacide'
__version__ = '1.6'
__date__ = '2013-06-21'

color_layout = ""
no_colorid_list = []
no_pure_colorid_list = []

def get_shader_from_mesh():
    selection_list = cmds.ls(sl=True, l=True)
    shader_list = []
    for selection in selection_list:
        shapes = cmds.listRelatives(selection,shapes=True)
        destination_list = cmds.connectionInfo(shapes[0] + ".instObjGroups[0]",
                                    destinationFromSource=True)
        destination_list = cmds.connectionInfo(destination_list[0].split(".")[0] + ".surfaceShader",
                                    sourceFromDestination=True)
        shader_list.append(destination_list.split(".")[0])
    return shader_list
    
def get_surfaceshader_writetocolorbuffer_with_color():
    global color_layout
    shader_list = cmds.ls(l=True, type="surfaceShader")
    color_search = cmds.colorSliderButtonGrp(color_layout, rgbValue=True, q=True)
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
    color_search = cmds.colorSliderButtonGrp(color_layout, rgbValue=True, q=True)
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
        result = cmds.confirmDialog(title='Finished', message=text, button=['Select'])
        if(result == "Select"):
            cmds.select(return_writetocolorbuffer_list + return_surfaceshader_list)
    else:
        result = cmds.confirmDialog(title='Finished', message="No Shader Found", button=['Confirm'])
        
def open_hypershade():   
    if not cmds.objExists("hyperShadePanel"):
        cmds.HypershadeWindow()    
def replace_or_nothing(text, old, new):
    if text.find(old) == -1 :
        return ""
    text=text.replace(old,new)
    if text.find(old) != -1:
        return ""
    else:
        return text
def check_color_id(arg):
    global no_colorid_list
    global no_pure_colorid_list
    no_colorid_list = []
    no_pure_colorid_list = []
    wrong_colorid_list = []
    wrong_colorid3_list = []
    no_light_shader_for_glass =[]
    shader_list = cmds.ls(l=True, materials=True)
    for shader in shader_list:
        if (shader.find("_RGB") != -1 or shader.find("_RGBA") != -1 or
            shader.find("_ZDEPTH") != -1 or shader.find("_LIGHT") != -1):
            destination_list = cmds.connectionInfo(shader + ".outColor",
                                destinationFromSource=True) 
            count_color_id = 0
            if (shader.find("_RGB1") == -1 and shader.find("_RGBA1") == -1 and
                shader.find("_ZDEPTH1") == -1 and shader.find("_LIGHT1") == -1):
                if (((shader.find("_ZDEPTH") != -1 or shader.find("_LIGHT") != -1)) and
                      shader.find("glass_LIGHT") == -1):
                   count_color_id += 1
                else: 
                    for destination in destination_list:
                        if ((destination.find("ColorID3") != -1 or (destination.find("ColorID") != -1 and destination.find("ID3") == -1)) and
                            destination.find("ColorID1") == -1 and destination.find("ColorID31") == -1):
                            count_color_id += 1
                            destination_name = destination.split(".")[0]
                            source_destination = cmds.connectionInfo(destination_name + ".color",
                                    sourceFromDestination=True)
                            source_destination_name = source_destination.split(".")[0]
                            color = ""
                            if source_destination_name != "":
                                if cmds.objectType(source_destination_name) == "multiplyDivide":                                
                                    color = cmds.getAttr(source_destination_name + ".input1")  
                            else:                                                  
                                color = cmds.getAttr(destination_name + ".color")  
                            red = float(color[0][0])
                            green = float(color[0][1])
                            blue = float(color[0][2])
                            print str(red) + "," + str(green) + "," + str(blue) + " " + destination_name
                            if (not(red == 1.0 and green == 0.0 and blue == 0.0) and
                                not(red == 0.0 and green == 1.0 and blue == 0.0) and
                                not(red == 0.0 and green == 0.0 and blue == 1.0) and
                                not(red == 0.0 and green == 0.0 and blue == 0.0)):
                                no_pure_colorid_list.append(destination_name)
                            elif ((not(red == 1.0 and green == 0.0 and blue == 0.0) and
                                not(red == 0.0 and green == 0.0 and blue == 1.0)) and
                                destination_name.find("ColorID3") != -1) :
                                wrong_colorid3_list.append(destination_name)
                            elif (((red == 1.0 and green == 0.0 and blue == 0.0) or
                                (red == 0.0 and green == 0.0 and blue == 1.0)) and
                                (destination_name.find("ColorID") != -1 and destination_name.find("ColorID3") == -1)) :
                                wrong_colorid_list.append(destination_name)
            if(count_color_id < 1):
                no_colorid_list.append(shader)
        if(shader.find("_glass_RGB") != -1 or shader.find("_Glass_RGB") != -1 or shader.find("_glass_VALID") != -1 or shader.find("_Glass_VALID") != -1):
            print shader
            if ( not cmds.objExists(replace_or_nothing(shader, "_glass_VALIDA", "_glass_LIGHT")) and
                not cmds.objExists(replace_or_nothing(shader, "_Glass_VALIDA", "_Glass_LIGHT"))  and
                not cmds.objExists(replace_or_nothing(shader, "_Glass_VALID", "_Glass_LIGHT")) and
                not cmds.objExists(replace_or_nothing(shader, "_glass_VALID", "_glass_LIGHT")) and
                not cmds.objExists(replace_or_nothing(shader, "_glass_RGBA", "_glass_LIGHT")) and
                not cmds.objExists(replace_or_nothing(shader, "_Glass_RGBA", "_Glass_LIGHT"))  and 
                not cmds.objExists(replace_or_nothing(shader, "_glass_RGB", "_glass_LIGHT")) and 
                not cmds.objExists(replace_or_nothing(shader, "_Glass_RGB", "_Glass_LIGHT"))):
                print "hello"
                no_light_shader_for_glass.append(shader)           
    print no_colorid_list         
    print no_pure_colorid_list
    print no_light_shader_for_glass
    if len(no_colorid_list) != 0 or len(no_pure_colorid_list) != 0 or len(wrong_colorid_list) != 0 or len(wrong_colorid3_list) != 0 or len(no_light_shader_for_glass) != 0:
        text_textscroll_list=[]
        if len(no_colorid_list) != 0:
            text_textscroll_list += ["Select Shader_rgb without ColorID:", ""] + no_colorid_list
        if len(no_pure_colorid_list) != 0:
            text_textscroll_list += ["", "", "Select not pure colorID (R,G,B):", ""] + no_pure_colorid_list
        if len(wrong_colorid_list) != 0:
            text_textscroll_list += ["", "", "Select wrong colorID :", ""] + wrong_colorid_list
        if len(wrong_colorid3_list) != 0:
            text_textscroll_list += ["", "", "Select wrong colorID3 :", ""] + wrong_colorid3_list
        if len(no_light_shader_for_glass) != 0:
            text_textscroll_list += ["", "", "Select Glass Shader without Shader Light: ", ""] + no_light_shader_for_glass
        if (cmds.window("ColorID_Error_List", exists=True)):
                cmds.deleteUI("ColorID_Error_List")
        cmds.window("ColorID_Error_List", title="ColorID Error List")
        cmds.paneLayout()
        
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
    text_scroll_list_select = cmds.textScrollList("textScrollList", si=True, q=True)
    temp_list = []
    for text_scroll in text_scroll_list_select:
        if (text_scroll != "" and
            text_scroll != "Select Shader_rgb without ColorID:" and
            text_scroll != "Select not pur ColorID:"):
            temp_list.append(text_scroll)
    if(len(temp_list) != 0):
        cmds.select(temp_list)

def select_colorid3(r, g, b):
    open_hypershade()
    shader_list = cmds.ls(l=True, materials=True)
    green_colorid_list = []
    green_colorid_shader_list = []
    for shader in shader_list:
        first_shader=shader
        if(cmds.objExists(shader.replace("_VALID","_LIGHT"))):
            shader = shader.replace("_VALID","_LIGHT")
        if(cmds.objExists(shader.replace("_RGB","_LIGHT"))):
            shader = shader.replace("_RGB","_LIGHT")
        if(cmds.objExists(shader.replace("_VALIDA","_LIGHT"))):
            shader = shader.replace("_VALIDA","_LIGHT")
        if(cmds.objExists(shader.replace("_RGBA","_LIGHT"))):
            shader = shader.replace("_RGBA","_LIGHT")
        shader = shader.replace("_VALID","_RGB")
        # if (shader.find("_RGB") != -1 or shader.find("_RGBA") != -1 or
            # shader.find("_Glass_LIGHT") != -1 or  shader.find("_glass_LIGHT") != -1 or shader.find("_LIGHT") != -1
            # (shader.lower().find("bulb") != -1 and shader.find("_LIGHT") != -1)):
        if shader.find("_RGB") != -1 or shader.find("_RGBA") != -1 or shader.find("_LIGHT") != -1:
            destination_list = cmds.connectionInfo(shader + ".outColor",
                                destinationFromSource=True) 
            count_color_id = 0
            shader_is_assigned = False
            compt_shading_engine = 0
            print shader + "------------------------------------------"
            for destination in destination_list:
                if cmds.objectType(destination.split(".")[0]) == "shadingEngine":
                    compt_shading_engine += 1                 
                    compt_shading_mesh = 0
                    
                    dag_set_members = cmds.getAttr(destination.split(".")[0] + ".dagSetMembers", multiIndices=True)
                    for i in dag_set_members:
                        source = cmds.connectionInfo(destination.split(".")[0] + ".dagSetMembers["+str(i)+"]",
                                                        sourceFromDestination=True)
                        print cmds.objectType(source.split(".")[0])
                        if cmds.objectType(source.split(".")[0]) == "mesh":
                            compt_shading_mesh += 1
                    if compt_shading_mesh == 0:
                        shader_is_assigned = True
            if compt_shading_engine == 0:
                shader_is_assigned = True
            for destination in destination_list:  
                if destination.find("ColorID3") != -1 :
                    count_color_id += 1
                    destination_name = destination.split(".")[0]
                    color = cmds.getAttr(destination_name + ".color")    
                    red = float(color[0][0])
                    green = float(color[0][1])
                    blue = float(color[0][2])
                    print str( red) + "," + str(green) + "," + str(blue)
                    if ( red == r) and (green == g) and (blue == b):
                        green_colorid_list.append(destination_name)
                        if shader_is_assigned :
                            print shader
                            # shader = shader.replace("_RGB","_VALID").replace("_LIGHT","_VALID")
                            shader = first_shader
                        print shader + "*******************************************************"
                        green_colorid_shader_list.append(shader)
                        if(cmds.objExists(shader.replace("_LIGHT", "_RGB"))):
                            print shader + "++++++++++++++++++++++++++++++++++++++++++++++++"
                            green_colorid_shader_list.append(shader.replace("_LIGHT", "_RGB"))
                        if(cmds.objExists(shader.replace("_LIGHT", "_RGBA"))):
                            print shader + "++++++++++++++++++++++++++++++++++++++++++++++++"
                            green_colorid_shader_list.append(shader.replace("_LIGHT", "_RGBA"))
                        if(cmds.objExists(shader.replace("_LIGHT", "_VALID"))):
                            print shader + "++++++++++++++++++++++++++++++++++++++++++++++++"
                            green_colorid_shader_list.append(shader.replace("_LIGHT", "_VALID"))
                        if(cmds.objExists(shader.replace("_LIGHT", "_VALIDA"))):
                            print shader + "++++++++++++++++++++++++++++++++++++++++++++++++"
                            green_colorid_shader_list.append(shader.replace("_LIGHT", "_VALIDA"))
    cmds.select(cl=True)
    if len(green_colorid_shader_list) != 0:
        cmds.select( green_colorid_shader_list)
        cmds.hyperShade(objects="")
    if len( green_colorid_list) != 0:
        cmds.select( green_colorid_list, add=True)
        
def select_colorid_red_river(arg):
    select_colorid3(1.0, 0.0, 0.0)
    
def select_colorid_green_bulbe(arg):
    select_colorid3(0.0, 1.0, 0.0)
    
def select_colorid_blue_windows(arg):
    select_colorid3(0.0, 0.0, 1.0)

def select_colorid(r, g, b):
    open_hypershade()
    shader_list = cmds.ls(l=True, materials=True)
    green_colorid_list = []
    green_colorid_shader_list = []
    for shader in shader_list:
        shader = shader.replace("_VALID","_RGB")
        if shader.find("_RGB") != -1 or shader.find("_RGBA") != -1:
            destination_list = cmds.connectionInfo(shader + ".outColor",
                                destinationFromSource=True) 
            count_color_id = 0
            shader_is_assigned = False
            compt_shading_engine = 0
            
            for destination in destination_list:
                if cmds.objectType(destination.split(".")[0]) == "shadingEngine":
                    compt_shading_engine += 1                 
                    compt_shading_mesh = 0
                    dag_set_members = cmds.getAttr(destination.split(".")[0] + ".dagSetMembers", multiIndices=True)
                    for i in dag_set_members:
                        source = cmds.connectionInfo(destination.split(".")[0] + ".dagSetMembers["+str(i)+"]",
                                                        sourceFromDestination=True)
                        if cmds.objectType(source.split(".")[0]) == "mesh":
                            compt_shading_mesh += 1
                    if compt_shading_mesh == 0:
                        shader_is_assigned = True
            if compt_shading_engine == 0:
                shader_is_assigned = True
            for destination in destination_list:
                if shader_is_assigned :
                    shader = shader.replace("_RGB","_VALID")
                if destination.find("ColorID") != -1 :
                    count_color_id += 1
                    destination_name = destination.split(".")[0]
                    color = cmds.getAttr(destination_name + ".color")    
                    red = float(color[0][0])
                    green = float(color[0][1])
                    blue = float(color[0][2])
                    print str(red) + "," + str(green) + "," + str(blue)
                    if (red == r) and (green == g) and (blue == b):
                        green_colorid_list.append(destination_name)
                        green_colorid_shader_list.append(shader)
    cmds.select(cl=True)
    if len(green_colorid_shader_list) != 0:
        cmds.select(green_colorid_shader_list)
        cmds.hyperShade(objects="")
    if len(green_colorid_list) != 0:
        cmds.select(green_colorid_list, add=True) 
        
def select_colorid_green_vegetation(arg):
    select_colorid(0.0, 1.0, 0.0)

def select_colorid_blue_props(arg):
    select_colorid(0.0, 0.0, 1.0)       
        
def select_colorid_black(arg):
    select_colorid(0.0, 0.0, 0.0)
    
def set_colorid_red(arg):
    shader_list = cmds.ls(sl=True, l=True, materials=True)
    if len(shader_list) == 0:
        shader_list = cmds.ls(sl=True, l=True, type="writeToColorBuffer")
    if len(shader_list) == 0:
        cmds.hyperShade(shaderNetworksSelectMaterialNodes=True)
        shader_list = cmds.ls(sl=True, l=True, materials=True)
    for shader in shader_list:
        shader = shader.replace("_VALID","_RGB")
        if (shader.find("_RGB") != -1 or shader.find("_RGBA") != -1 or
            shader.find("_ZDEPTH") != -1 or shader.find("_LIGHT") != -1):
            destination_list = cmds.connectionInfo(shader + ".outColor",
                                destinationFromSource=True)
            for destination in destination_list :
                if destination.find("ColorID") != -1:
                    destination_name = destination.split(".")[0]
                    color = cmds.setAttr(destination_name + ".color", 1.0, 0.0, 0.0) 
        elif shader.find("ColorID") != -1:
            color = cmds.setAttr(shader + ".color", 1.0, 0.0, 0.0)    

def set_colorid_green(arg):
    shader_list = cmds.ls(sl=True, l=True, materials=True)
    if len(shader_list) == 0:
        shader_list = cmds.ls(sl=True, l=True, type="writeToColorBuffer")
    if len(shader_list) == 0:
        cmds.hyperShade(shaderNetworksSelectMaterialNodes=True)
        shader_list = cmds.ls(sl=True, l=True, materials=True)
    for shader in shader_list:
        shader = shader.replace("_VALID","_RGB")
        if (shader.find("_RGB") != -1 or shader.find("_RGBA") != -1 or
            shader.find("_ZDEPTH") != -1 or shader.find("_LIGHT") != -1):
            destination_list = cmds.connectionInfo(shader + ".outColor",
                                destinationFromSource=True)
            for destination in destination_list:
                if destination.find("ColorID") != -1 and destination.find("ColorID3") == -1:
                    destination_name = destination.split(".")[0]
                    color = cmds.setAttr(destination_name + ".color", 0.0, 1.0, 0.0) 
        elif shader.find("ColorID") != -1:
            color = cmds.setAttr(shader + ".color", 0.0, 1.0, 0.0)
            
def set_colorid(colorid, red, green, blue):
    print colorid
    destination_name = colorid.split(".")[0]
    source_destination = cmds.connectionInfo(destination_name + ".color",
                sourceFromDestination=True)
    source_destination_name = source_destination.split(".")[0]
    if source_destination_name != "":
        print "0 "+source_destination_name
        if cmds.objectType(source_destination_name) == "multiplyDivide":
            source_destination_multiply = cmds.connectionInfo(source_destination_name + ".input1",
                sourceFromDestination=True)
            source_destination_multiply_name = source_destination_multiply.split(".")[0]
            print source_destination_multiply
            if source_destination_multiply_name != "":
                cmds.setAttr(source_destination_multiply, red, green,blue)
            else:
                cmds.setAttr(source_destination_name + ".input1", red, green, blue)
    else:
        print "1 "+destination_name
        print str(red)+" "+str(green)+ " " +str(blue)
        cmds.setAttr(destination_name + ".color", red, green, blue)
        
def set_colorid3_main(r, g, b):
    compt_color_id = 0
    shader_list = cmds.ls(sl=True, l=True, materials=True)
    if len(shader_list) == 0:
        shader_list = cmds.ls(sl=True, l=True, type="writeToColorBuffer")
    if len(shader_list) == 0:        
        shader_list = get_shader_from_mesh()
    for shader in shader_list:
        compt_color_id = 0
        shader = shader.replace("_VALID","_RGB")
        if (shader.find("_RGB") != -1 or shader.find("_RGBA") != -1 or
            shader.find("_ZDEPTH") != -1 or shader.find("_LIGHT") != -1):
            destination_list = cmds.connectionInfo(shader + ".outColor",
                                destinationFromSource=True)
            for destination in destination_list:
                if destination.find("ColorID3") != -1:
                    compt_color_id += 1
                    set_colorid(destination, r, g, b)
                if destination.find("ColorID") != -1  and destination.find("ColorID3") == -1:
                    set_colorid(destination, 0.0, 0.0, 0.0)
            if compt_color_id == 0 :
                new_shader = shader.replace("_RGBA","_LIGHT").replace("_RGB", "_LIGHT").replace("_ZDEPTH", "_LIGHT")
                if(cmds.objExists(new_shader)):
                    destination_list = cmds.connectionInfo(new_shader+ ".outColor",
                                                           destinationFromSource=True)
                    for destination in destination_list:
                        if destination.find("ColorID3") != -1:
                            compt_color_id += 1
                            set_colorid(destination, r, g, b)
                        if destination.find("ColorID") != -1  and destination.find("ColorID3") == -1:
                            set_colorid(destination, 0.0, 0.0, 0.0)            
        elif shader.find("ColorID3") != -1:
            compt_color_id += 1
            set_colorid(shader, r, g, b)  
        elif shader.find("ColorID") != -1:
            compt_color_id += 1            
        if compt_color_id == 0:
            my_color_id = cmds.shadingNode('writeToColorBuffer', name = shader.replace("SHD_","").replace("_RGBA", "_ColorID3").replace("_RGB", "_ColorID3").replace("_LIGHT", "_ColorID3").replace("_ZDEPTH", "_ColorID3"), asUtility=True)
            cmds.setAttr(my_color_id + ".color", r, g, b)
            cmds.connectAttr(shader + ".outColor",my_color_id + ".evaluationPassThrough",force=True)

def set_colorid_main(r, g, b):
    shader_list = cmds.ls(sl=True, l=True, materials=True)
    if len(shader_list) == 0:
        shader_list = cmds.ls(sl=True, l=True, type="writeToColorBuffer")
    if len(shader_list) == 0:
        shader_list = get_shader_from_mesh()
    for shader in shader_list:
        shader = shader.replace("_VALID","_RGB")
        if (shader.find("_RGB") != -1 or shader.find("_RGBA") != -1 or
            shader.find("_ZDEPTH") != -1 or shader.find("_LIGHT") != -1):
            destination_list = cmds.connectionInfo(shader + ".outColor",
                                destinationFromSource=True)
            for destination in destination_list:
                if destination.find("ColorID") != -1 and destination.find("ColorID3") == -1:
                    set_colorid(destination,r, g, b)
                        
        elif shader.find("ColorID") != -1 and shader.find("ColorID3") == -1:
            set_colorid(shader,r, g, b) 
            
def set_colorid_red_river(arg):
    set_colorid3_main(1.0, 0.0, 0.0)
    result = cmds.confirmDialog(title='Finished',
                                 message="OK",
                                 button=['Close'])  
def set_colorid_green_bulbe(arg):
    set_colorid3_main(0.0, 1.0, 0.0)
    result = cmds.confirmDialog(title='Finished',
                                 message="OK",
                                 button=['Close'])  
def set_colorid_blue_windows(arg):
    set_colorid3_main(0.0, 0.0, 1.0)
    result = cmds.confirmDialog(title='Finished',
                                 message="OK",
                                 button=['Close'])  
def set_colorid_green_vegetation(arg):
    set_colorid_main(0.0, 1.0, 0.0)                       
    result = cmds.confirmDialog(title='Finished',
                                 message="OK",
                                 button=['Close'])  
def set_colorid_blue_props(arg):
    set_colorid_main(0.0, 0.0, 1.0)     
    result = cmds.confirmDialog(title='Finished',
                                 message="OK",
                                 button=['Close'])          
def set_colorid_black_except_vegation_windows(arg):
    set_colorid_main(0.0, 0.0, 0.0)  
    result = cmds.confirmDialog(title='Finished',
                                 message="OK",
                                 button=['Close'])        
def set_meshes_renderstats(arg):
    selection_list = cmds.ls(sl=True)
    text = "Meshes Renderstats Set on :\n"
    for selected in selection_list:
        text+=selected+"\n"
        cmds.setAttr(selected + ".castsShadows", 0)    
    result = cmds.confirmDialog(title='Finished',
                                 message=text,
                                 button=['Close'])
def config_milabel(arg):
    cal_miLabel.configMiLabel(recreate=False, log=True)
    
def set_props_render_setup_ui():
    global color_layout   
    if (cmds.window("Set_Prop_Render_Setup", exists=True)):
        cmds.deleteUI("Set_Prop_Render_Setup")
    cmds.window("Set_Prop_Render_Setup", title="Sets/Props Render Setup v" + __version__, resizeToFitChildren=True)   
    cmds.columnLayout()
    cmds.frameLayout(label='ColorID Setup', borderStyle='out', width=400)
    # color_layout = cmds.colorSliderButtonGrp( label='Color', buttonLabel='search', rgb=(1, 0, 1), symbolButtonDisplay=True, columnWidth=(5, 30), buttonCommand=get_surfaceshader_writetocolorbuffer_with_color )
    cmds.button(label='Check ColorID / Shader Names', command=check_color_id, bgc=(0.3, 0.8, 0.3))
    cmds.frameLayout(label='ColorID3 (Plug on LIGHT RenderLayer)', borderStyle='out', width=400)
    cmds.button(label='Select ColorID3 RED (River)', command=select_colorid_red_river)
    cmds.button(label='Select ColorID3 GREEN (Bulb Lamp)', command=select_colorid_green_bulbe)
    cmds.button(label='Select ColorID3 BLUE (Windows)', command=select_colorid_blue_windows)
    cmds.button(label='Set ColorID3 Selected to RED (River/Water)', command=set_colorid_red_river)    
    cmds.button(label='Set ColorID3 Selected to GREEN (Bulb Lamp)', command=set_colorid_green_bulbe)    
    cmds.button(label='Set ColorID3 Selected to BLUE (Windows)', command=set_colorid_blue_windows)
    cmds.frameLayout(label='ColorID (Plug on RGB RenderLayer)', borderStyle='out', width=400)
    cmds.button(label='Select ColorID GREEN (Vegetation)', command=select_colorid_green_vegetation)
    cmds.button(label='Select ColorID BLUE (Props)', command=select_colorid_blue_props)
    cmds.button(label='Select ColorID BLACK (Everything except Vegetation)', command=select_colorid_black)
    cmds.button(label='Set ColorID Selected to GREEN (Vegetation)', command=set_colorid_green_vegetation)
    cmds.button(label='Set ColorID Selected to BLUE (Props)', command=set_colorid_blue_props)
    cmds.button(label='Set ColorID Selected to BLACK (Everything except Vegetation)', command=set_colorid_black_except_vegation_windows)
    
    
    cmds.text(label='')
    cmds.text(label='')
    cmds.frameLayout(label='Meshes Renderstats Setup', borderStyle='out')
    cmds.text(label='')
    cmds.button(label='Set Cast Shadows OFF on selected meshes', command=set_meshes_renderstats)
    cmds.button(label='Config MiLabel', command=config_milabel)
    cmds.showWindow()
   