import maya.cmds as cmds
import maya.mel
import os.path

def rename_namespace_of_ref_calimero_style(file):
    try:
        file = file.encode('ascii', 'ignore')
        namespace = ""
        if file.find("CHARACTERS")!=-1:
            namespace = file.split("/")[-4]
        if file.find("PROPS")!=-1:
            namespace = file.split("/")[-3]
        if file.find("SETS")!=-1:
            namespace = file.split("/")[-4]
        if file.find("CAMERA")!=-1:
            namespace = file.split("/")[-2]
        if file.find("ENV")!=-1:
            namespace = file.split("/")[-3]   
        if namespace != "":
            cmds.file(file,
                      e=True,
                      namespace=namespace.upper().replace("CHR_","CHAR_").replace("PRP_","PROP_"))
            print "Set this namespace " + namespace + " to this reference: " + file
    except:
        pass    

def switch_reference_anim_to_render(file):   
    if file.find("_anim") != -1:       
        if(os.path.exists(file.split("{")[0].replace("_anim", "_render"))):
            referenceNode = cmds.referenceQuery(file, rfn=True)
            try:
                cmds.file(file.replace("_anim", "_render"),
                          loadReference=referenceNode,
                          type="mayaAscii",
                          options="v=0")
                print referenceNode + " switched anim to render"
            except:
                pass
   
def create_group(group_name):
    if not cmds.objExists(group_name):
        cmds.group(em=True, name=group_name)
        print group_name + " created"
       
def parent_ref_node_to_group(ref_node,
                             word_to_find_in_ref_name_condition,
                             group):
    top_reference_node_parent = cmds.listRelatives( ref_node, parent=True )
    if top_reference_node_parent is None:
        top_reference_node_parent = [""]
    if (top_reference_node.find(word_to_find_in_ref_name_condition) != -1 and
        top_reference_node_parent[0] != group):
        cmds.parent(top_reference_node, group)
        print top_reference_node + " set in " + group

def create_group():
    list_file = cmds.file(q=True, l=True)
    print '====================!!!Conform namespace!!!===================='
    for file in list_file:
        switch_reference_anim_to_render(file)
        rename_namespace_of_ref_calimero_style(file)       
    print '====================!!!Conform Group!!!===================='       
    create_group("CHR_GRP")
    create_group("PRP_GRP")
    create_group("SET_GRP")
    create_group("CAM_GRP")
    reference_list = cmds.ls( type='reference' )
    for reference in reference_list:
        try:
            reference_node_list = cmds.referenceQuery(reference, nodes=True)
            top_reference_node = reference_node_list[0]
            parent_ref_node_to_group(top_reference_node, "CHAR_", "CHR_GRP")
            parent_ref_node_to_group(top_reference_node, "PROP_", "PRP_GRP")
            parent_ref_node_to_group(top_reference_node, "SET_", "SET_GRP")
            parent_ref_node_to_group(top_reference_node, "ENV_", "SET_GRP")
            parent_ref_node_to_group(top_reference_node, "COL_", "PRP_GRP")
            parent_ref_node_to_group(top_reference_node, "DZN_", "PRP_GRP")
            parent_ref_node_to_group(top_reference_node, "SKYDOME_", "SET_GRP")
            parent_ref_node_to_group(top_reference_node, "CYCLO_", "SET_GRP")
            parent_ref_node_to_group(top_reference_node, "CAMERA", "CAM_GRP")
        except:
            pass