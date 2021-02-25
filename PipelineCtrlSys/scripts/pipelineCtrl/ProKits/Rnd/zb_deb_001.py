import maya.cmds as mc
import pymel.core as pm
import os, re
import shutil

notyp = pm.selected()[0].type()

cur_proj_path = pm.workspace(dir=True, q=True)

cur_proj_soursimgs = "{}/sourceimages/".format('/'.join(cur_proj_path.split('/')[:-2]))

allVmeshs = pm.ls(type=notyp)
VM_files = []
unExist_VM = []
for eaVM in allVmeshs:
    ms_file = eaVM.attr('fileName').get()
    ms_file_name = os.path.basename(ms_file)
    if not os.path.isfile(ms_file):
        unExist_VM.append(ms_file)
        continue
    targ_fpth = u'{}{}'.format(cur_proj_soursimgs, ms_file_name)
    shutil.copy2(os.path.abspath(ms_file), cur_proj_soursimgs)









