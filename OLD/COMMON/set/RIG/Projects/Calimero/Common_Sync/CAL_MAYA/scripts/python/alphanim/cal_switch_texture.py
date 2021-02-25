'''
this script switch texture from tga or map to png an from png to map.
'''

import os.path
import sys
import maya.cmds as cmds

__author__  = 'Dimitri Gouacide'
__version__ = '1.0'
__date__    = '2013-05-07'

temp = ""
first_button_text = ""
second_button_text = ""
third_button_text = ""
fourth_button_text = ""
comment = ""
    
def search_and_replace_file_path(path, to_replace, new_word):
    new_file_path = path.replace(to_replace, new_word)
    return new_file_path
    
def search_and_replace_texture(file, to_replace, new_word):
    file_path=cmds.getAttr(file + ".fileTextureName")
    new_file_path = search_and_replace_file_path(file_path, to_replace,new_word)
    new_file_path = search_and_replace_file_path(new_file_path,
                                                 to_replace,
                                                 new_word)
    if(file_path != new_file_path):
        if(os.path.exists(new_file_path.replace("${IDMT_PROJECTS}","Z:/Projects/Calimero/Project/sourceimages"))):
            cmds.setAttr(file + ".fileTextureName", new_file_path, type = "string")
            return True
        else:
            return False
    else:
        return None
        
def search_and_replace_all_texture( to_replace, new_word):
    list_file = cmds.ls(l=True, type="file")
    log = ""
    replaced_file_log = ""
    not_replaced_file_log = "" 
    returned_value = False
    for file in list_file:
        result = search_and_replace_texture(file, to_replace, new_word)        
        if(result == True):
            replaced_file_log += (file + " " +
                                 cmds.getAttr(file + ".fileTextureName") +
                                 "\n")
        elif result is not None:
            not_replaced_file_log += ("not replaced File: " +
                                      file +
                                      ",\t\tPATH = " +
                                      cmds.getAttr(file + ".fileTextureName") +
                                      "\n")   
    if(replaced_file_log != ""):        
        log += "replaced file " + to_replace + "->" + new_word + ":\n\n"
        log += replaced_file_log + "\n"
        returned_value = True
    elif(not_replaced_file_log != ""):
        log += "not replaced file " + to_replace + "->" + new_word + ":\n\n"
        log += not_replaced_file_log + "\n" 
        returned_value = False
    else:
        return None
    print log
    return returned_value
    
def replace_tga_and_map_to_png(arg):
    global first_button_text
    global comment
    result = search_and_replace_all_texture(".tga", ".png") 
    result = result or search_and_replace_all_texture(".map", ".png")
    cmds.text(fourth_button_text, label = '',enableBackground=False, e = True)
    cmds.text(second_button_text, label = '',enableBackground=False, e = True)
    cmds.text(third_button_text, label = '',enableBackground=False, e = True)
    if(result == True):
         cmds.text(first_button_text, label = ' OK. ', backgroundColor=(0,1,0), e = True)
         cmds.text(comment, label = '',enableBackground=False, e = True)
    elif(result is not None):
         cmds.text(first_button_text,
                   label = ' Error : missing png ',
                   backgroundColor=(1,0,0),
                   e = True)
         cmds.text(comment,
                   label = ' Path not found: \nSee the Script Editor ',
                   backgroundColor=(1,0,0),
                   e = True)
    else:
        cmds.text(first_button_text,
                  label = ' No tga or map ',
                  backgroundColor=(0,1,0),
                  e = True)
        cmds.text(comment, label = '',enableBackground=False, e = True)

def replace_map_to_tga(arg):
    global third_button_text
    global comment
    result = search_and_replace_all_texture(".map", ".tga") 
    cmds.text(fourth_button_text, label = '',enableBackground=False, e = True)
    cmds.text(second_button_text, label = '',enableBackground=False, e = True)
    cmds.text(first_button_text, label = '',enableBackground=False, e = True)
    if(result == True):
         cmds.text(third_button_text, label = 'OK. ', backgroundColor=(0,1,0), e = True)
         cmds.text(comment, label = '',enableBackground=False, e = True)
    elif(result is not None):
         cmds.text(third_button_text,
                   label = ' Error : missing tga ',
                   backgroundColor=(1,0,0),
                   e = True)
         cmds.text(comment,
                   label = ' Path not found: \nSee the Script Editor',
                   backgroundColor=(1,0,0),
                   e = True)
    else:
        cmds.text(third_button_text,
                  label = ' No map ',
                  backgroundColor=(0,1,0),
                  e = True)
        cmds.text(comment, label = '', enableBackground=False, e = True)

def replace_png_to_map(arg):
    global second_button_text
    global comment
    result = search_and_replace_all_texture(".png", ".map")
    result2 = search_and_replace_all_texture(".png", ".tga")
    cmds.text(fourth_button_text, label = '', enableBackground=False, e = True)
    cmds.text(first_button_text, label = '', enableBackground=False, e = True)
    cmds.text(third_button_text, label = '', enableBackground=False, e = True)
    if(result == True or result2 == True):
        cmds.text(second_button_text, label = ' OK ', backgroundColor=(0,1,0), e = True)
        cmds.text(comment, label = '',enableBackground=False, e = True)
    elif(result is not None or result2 is not None):
        if result2 is not None:
            cmds.text(second_button_text,
                  label = ' Error : missing tga ',
                  backgroundColor=(1,0,0),
                  e = True)
            cmds.text(comment,
                      label = ' Path not found: \nSee the Script Editor ',
                      backgroundColor=(1,0,0),
                      e = True)
        else:
            cmds.text(second_button_text,
                      label = ' Error : missing map or tga ',
                      backgroundColor=(1,0,0),
                      e = True)
            cmds.text(comment,
                      label = ' Path not found: \nSee the Script Editor ',
                      backgroundColor=(1,0,0),
                      e = True)
    else:
        cmds.text(second_button_text,
                  label = ' No png ',
                  backgroundColor=(0,1,0),
                  e = True)
        cmds.text(comment, label = '',enableBackground=False, e = True)
        
def replace_tga_to_map(arg):
    global fourth_button_text
    global comment
    result = search_and_replace_all_texture(".tga", ".map")
    cmds.text(second_button_text, label = '',enableBackground=False, e = True)
    cmds.text(first_button_text, label = '', enableBackground=False, e = True)
    cmds.text(third_button_text, label = '', enableBackground=False, e = True)
    if(result == True ):
        cmds.text(fourth_button_text, label = ' OK ', backgroundColor=(0,1,0), e = True)
        cmds.text(comment, label = '',enableBackground=False, e = True)
    elif(result is not None ):
        if result is not None:
            cmds.text(fourth_button_text,
                  label = ' Error : missing map ',
                  backgroundColor=(1,0,0),
                  e = True)
            cmds.text(comment,
                      label = ' Path not found: \nSee the Script Editor ',
                      backgroundColor=(1,0,0),
                      e = True)
    else:
        cmds.text(fourth_button_text,
                  label = ' No tga ',
                  backgroundColor=(0,1,0),
                  e = True)
        cmds.text(comment, label = '',enableBackground=False, e = True)

def get_resolved_path(path):
    list_file = cmds.file(q=True, l=True)
    for file in list_file:
        file.encode('utf-8')
        if file.find(path) != -1:
            return file
    return path    
    
def convert_map_to_tga(arg):
    mayaBin = os.path.split(sys.executable)[0] + "\\"
    list_file = cmds.ls(l=True, type="file")
    replaced_file_log = ".map Converted to .tga: \n\n" 
    for file in list_file:
        file_texture_path = get_resolved_path(cmds.getAttr(file + ".fileTextureName"))
        if file_texture_path.find(".map") != -1: 
            destination_file_path = file_texture_path.replace(".map", ".tga")
            if os.path.exists(file_texture_path):
                os.system("\""+mayaBin + "imf_copy.exe\" -p %s %s" %(file_texture_path, destination_file_path) )
                cmds.setAttr(file + ".fileTextureName", destination_file_path, type="string")
                replaced_file_log += file_texture_path + "\n"
    result = cmds.confirmDialog( title='Finished', message=replaced_file_log, button=['Close'] )
            
def convert_map_to_png(arg):
    mayaBin = os.path.split(sys.executable)[0] + "\\"
    list_file = cmds.ls(l=True, type="file")
    replaced_file_log = ".map Converted to .png(256x256): \n\n"
    for file in list_file:
        file_texture_path = get_resolved_path(cmds.getAttr(file + ".fileTextureName"))
        if file_texture_path.find(".map") != -1: 
            destination_file_path = file_texture_path.replace(".map", ".png")
            if os.path.exists(file_texture_path):
                os.system("\""+mayaBin + "imf_copy.exe\" -p %s %s" %(file_texture_path, destination_file_path) )
                os.system("\""+mayaBin + "imconvert.exe\" %s %s %s" %(destination_file_path, "-resize 256", destination_file_path) )
                cmds.setAttr(file + ".fileTextureName", destination_file_path, type="string")
                replaced_file_log += file_texture_path + "\n"
    result = cmds.confirmDialog( title='Finished', message=replaced_file_log, button=['Close'] )
           
def switch_texture_main():
    global first_button_text 
    global second_button_text
    global third_button_text
    global fourth_button_text
    global comment
    if (cmds.window("Swich_Texture", exists=True)):
        cmds.deleteUI("Swich_Texture")   
    cmds.window("Swich_Texture", width=350, title="Switch Textures UI v"+__version__)
    cmds.frameLayout( label='Switch Texture', borderStyle='out' )
    cmds.rowColumnLayout(numberOfRows=5,
                         rowHeight =[(1, 20), (2, 20)],
                         width =200, columnSpacing=[(1, 20), (2, 20)],
                         rowSpacing=[(1, 5), (2, 5), (3, 5), (4, 5)])
    
    cmds.button(label = 'tga map -> png', command = replace_tga_and_map_to_png)
    cmds.button(label = 'png -> map', command =replace_png_to_map )
    cmds.button(label = 'map -> tga', command =replace_map_to_tga )
    cmds.button(label = 'tga -> map', command =replace_tga_to_map )
    temp = cmds.text(label = '', align = "left" )
    first_button_text = cmds.text(label = 'Waiting', align = "left" )
    second_button_text = cmds.text(label = 'Waiting', align = "left" )
    third_button_text = cmds.text(label = 'Waiting', align = "left" )
    fourth_button_text = cmds.text(label = 'Waiting', align = "left" )
    comment = cmds.text(label = '', align = "left" )
    cmds.setParent( '..' )
    cmds.setParent( '..' )
    cmds.frameLayout( label='Convert Texture', borderStyle='out', collapse = True)
    cmds.button(label = 'convert map -> tga', command =convert_map_to_tga )
    cmds.button(label = 'convert map -> png (256x256)', command =convert_map_to_png )
    cmds.showWindow()
