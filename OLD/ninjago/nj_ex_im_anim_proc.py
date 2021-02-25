from pymel.core import *
import os,re,sys
import maya.cmds as mc
def nj_export_anim_by_ref():
    shotFile_path = sceneName()
    file_loc = shotFile_path.dirname() #file_loc = workspace.getcwd()
    shotName = shotFile_path.namebase
    record_note = u'%s/%s_referenceImfor.txt'%(file_loc,shotName)
    #new_folder = u'%s/%s/'%(file_loc,u'storage_2014')
    ref_list = listReferences()
    master_ctrl_ls = []
    fn = file(record_note,'w+')
    #fn.write(u'%s%s%s'%(new_folder,shotFile_path.basename(),os.linesep))
    for eachRef in ref_list:
        temp_line = u'%s||%s%s'%(eachRef.namespace,eachRef.path,os.linesep)
        fn.write(temp_line)
        p_master = re.compile(u'master$',re.I)
        temp = [each_node for each_node in eachRef.nodes() if each_node.type() == u'transform' and p_master.search(each_node.name())]
        master_ctrl_ls.extend(temp)
    fn.close()
    frame_min = playbackOptions(q=True,min=True)
    frame_max = playbackOptions(q=True,max=True)
    ani_file_loc = u'%s/%s_anim_files'%(file_loc,shotName)
    if not os.path.isdir(ani_file_loc):os.mkdir(ani_file_loc)
    for each_ctr in master_ctrl_ls:
        select(each_ctr)
        ani_file_name = u'%s/%s_anim.anim' % (ani_file_loc,each_ctr.namespace().split(u':')[0])
        exp_ani_option = """precision=8;intValue=17;nodeNames=1;verboseUnits=0;whichRange=1;range=%d:%d;options=keys;hierarchy=below;controlPoints=0;shapes=1;\
        helpPictures=0;useChannelBox=0;copyKeyCmd=-animation objects -option keys -hierarchy below -controlPoints 0 -shape 1 """%(frame_min,frame_max)
        try:
            mc.file(ani_file_name,force=True,options=exp_ani_option,type='animExport',pr=True,es=True)
        except:
            warning(u'==============reference node: %s has no any animationCurves connected==================='%each_ctr)
def nj_import_anim_by_ref(mayaLoc,fileFullName):
    mayaLoc = u'D:/Alias/Maya2014x64' #os.getenv("MAYA_LOCATION")
    fileFullName = u'E:/Ninjago/SQ_999/SC_999/scenes/nj_E0011_Q0294_S0020_an.ma'
    file_loc = os.path.dirname(fileFullName)
    stor_newFile_loc = u'%s/%s/'%(file_loc,u'storage_2014')
    shot_basename = os.path.basename(fileFullName)
    shot_name_base = os.path.splitext(os.path.basename(fileFullName))[0]
    record_note_loc = u'%s/%s_referenceImfor.txt'%(file_loc,shot_name_base)
    anim_files_loc = u'%s/%s_anim_files'%(file_loc,shot_name_base)
    if not os.path.isdir(stor_newFile_loc):os.mkdir(stor_newFile_loc)
    renameFile(u'%s%s' % (stor_newFile_loc,shot_basename))
    runtime.SaveScene()
    fn = open(record_note_loc,'r')
    for eachLine in fn:
        ref_ns = eachLine.split(u'||')[0]
        ref_path = eachLine.split(u'||')[1].strip(os.linesep)
        mc.file(ref_path,reference = 1,ignoreVersion=1,namespace=ref_ns)ani_file_full_name
    fn.close()
    for eachRef in listReferences():
        p_master = re.compile(u'master$',re.I)
        temp = [each_node for each_node in eachRef.nodes() if each_node.type() == u'transform' and p_master.search(each_node.name())]
        if temp:
            ani_ns = temp[0].namespace().split(u':')[0]
            ani_file_full_name = u'%s/%s_anim.anim'%(anim_files_loc,ani_ns)
            if os.path.isfile(ani_file_full_name):
                select(temp)
                imp_ani_option = """targetTime=4;copies=1;option=replace;pictures=0;connect=0;"""
                try:
                    mc.file(ani_file_full_name,i=True,type='animImport',ignoreVersion=True,ra=True,mergeNamespacesOnClash=False,namespace = u'%s_anim'%(ani_ns),options =imp_ani_option,pr=True)
                except:
                    pass
if __name__ == '__main__':
    nj_export_anim_by_ref()


