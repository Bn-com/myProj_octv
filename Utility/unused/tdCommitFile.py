#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = 'pc_checkinCommon'    
__author__ = zhangben
__mtime__ = 2018/12/7:12:00
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
'''
import sys,re,os
import py_compile
import subprocess
import shutil
def mainCopy(serverDir,pycDir): #main process  copy selected itme (nonsupport mutile select)
    fpth = sys.argv[-1]
    if os.path.isfile(fpth):
        pyc = copy2ser(fpth,serverDir,pycDir)
        if pyc:
            for ea_pyc in pyc:
                os.remove(ea_pyc)
                print("/////pyc removed: {}".format(ea_pyc))
    else:
        print(fpth)
        print(os.listdir(fpth))
        for root,dirs,files in os.walk(fpth):
            # for dir in dirs:
            #     if not os.path.exists(os.path.join(root,dir)): os.makedirs(os.path.join(root,dir))
            #     print os.path.join(root,dir)
            for eafile in files:
                print(os.path.join(root,eafile))
                pyc = copy2ser(os.path.join(root,eafile),serverDir,pycDir)
                if pyc:
                    for ea_pyc in pyc:
                        os.remove(ea_pyc)
                        print("/////pyc removed: {}".format(ea_pyc))

def copy2ser(fpth,serverDir,pycDir): # via file path copy to server
    maya_v_dict = {'sixteen':2016,'eighteen':2018,'nineteen':2019,'twentytwenty':2020,'dev':'dev'}
    fpth_spl = os.path.splitext(fpth)
    fpth_dir,f_name = os.path.split(fpth)
    f_baseName,f_ext = os.path.splitext(f_name)
    re_relatively = re.compile("(maya_sixteen)\S+|(Nuke)\S+|(Utility)\S+|(maya_eighteen)\S+|(maya_nineteen)\S+|(maya_dev)\S+|(Clarisse)\S+")
    if not re_relatively.search(fpth):
        raise Exception("your should select a py or mel file in repository")
    toolNm = re_relatively.search(fpth).group()
    copyFiles = [fpth]
    fpth_pyc = ""
    ret_pyc_f = []
    if fpth_spl[1] == '.py':
        print(">>Ready Generate PYC File......")
        import platform
        py_version = platform.python_version()
        print(">>>Python Version :< {} >".format(py_version))
        fpth_pyc = "{}.pyc".format(fpth_spl[0])
        print (">>PYC FILE Path :>> {}".format(fpth_pyc))
        if py_version.startswith('2.'):
            py_compile.compile(fpth)
        else:
            py_compile.compile(fpth,fpth_pyc)
        print(">>py file is< {} >".format(fpth))
        copyFiles.append(fpth_pyc)
        if os.path.isfile(fpth_pyc): print(" ====pyc file created")
        else:print("  ======pyc file Error!!!!!!!")


    copyFiles.reverse()
    print(len(copyFiles))
    for ea in copyFiles:
        print ("---Current Operate on: {}".format(ea))
        subPth = re_relatively.search(fpth).group()
        print(subPth)
        # serverDirS = [r"maya\\2016", r"maya\\2018",r"maya\\2019",r"maya\\2020"]
        dest_dir_lst = []
        # for ea_sver in serverDirS:
        #     subPth_serv = re.sub("maya_sixteen", ea_sver, subPth)
        #     if subPth_serv == subPth: subPth_serv = re.sub("maya_eighteen", ea_sver, subPth)
        #     subPth_serv_spl = os.path.split(subPth_serv)
        #     subdir_serv = subPth_serv_spl[0]
        #     dest_dir = os.path.join(serverDir, subdir_serv)
        #     if dest_dir not in dest_dir_lst: dest_dir_lst.append(dest_dir)
        for k,v in maya_v_dict.items():
            if not re.search("maya_{}".format(k),subPth): continue
            subPth_serv  = re.sub("maya_{}".format(k),r"maya\\{}".format(v),subPth)
            subPth_serv_spl = os.path.split(subPth_serv)
            subdir_serv = subPth_serv_spl[0]
            dest_dir = os.path.join(serverDir, subdir_serv)
            if dest_dir not in dest_dir_lst: dest_dir_lst.append(dest_dir)
            # if k in ['sixteen']:
            #     subPth_serv219 = re.sub("maya_{}".format(k),r"maya\\2019\\SD",subPth)
            #     subPth_serv_spl219 = os.path.split(subPth_serv)
            #     subdir_serv219 = subPth_serv_spl[0]
            #     dest_dir219 = os.path.join(serverDir,subdir_serv)
            #     if dest_dir219 not in dest_dir_lst:dest_dir_lst.append(dest_dir219)
        for edir in dest_dir_lst:
            print(" file :::{} copied to path ::{}".format(ea, edir))
            if copyFiles.index(ea) == 1:
                copy2(ea, edir)
                if re.search('maya_sixteen',ea):
                    dest219 = re.sub('maya\\\\2016','maya\\\\2019\\\\SD',edir)
                    print(">>To2019>>{}".format(dest219))
                    copy2(ea,dest219)
                    # dest219= os.path.join(edir,)
        if copyFiles.index(ea) == 0:
            pyc_dest_dir = os.path.join(pycDir, os.path.split(subPth)[0])
            copy2(ea, pyc_dest_dir)
            print (">>To 2016 pyc file :::{} copied to path ::{}".format(ea, pyc_dest_dir))
            pyc_dest_dir_18 = os.path.join(pycDir, re.sub(r"sixteen", "eighteen", os.path.split(subPth)[0]))
            pyc_dest_dir_19 = os.path.join(pycDir, re.sub(r"sixteen", "nineteen/SD", os.path.split(subPth)[0]))
            if pyc_dest_dir_18 != pyc_dest_dir:
                print("To 2018 pyc file :::{} copied to 18 path ::{}".format(ea, pyc_dest_dir_18))
                copy2(ea, pyc_dest_dir_18)
            if pyc_dest_dir_19 != pyc_dest_dir:
                print("To 2019 pyc file :::{} copied to 19 path ::{}".format(ea, pyc_dest_dir_19))
                copy2(ea,pyc_dest_dir_19)
        # print toolNm
        elif copyFiles.index(ea) != 0 and toolNm.split('\\')[0] in ["Nuke"]:
            pyc_dest_dir = os.path.join(pycDir, os.path.split(subPth)[0])
            # pyc_dest_dir_18 = os.path.join(pycDir, re.sub(r"sixteen", "eighteen", os.path.split(subPth)[0]))
            # print (" pyc file :::{} to path ::{}".format(ea, pyc_dest_dir))
            copy2(ea, pyc_dest_dir)
            print (" py file :::{} to path ::{}".format(ea, pyc_dest_dir))
        if os.path.isfile(fpth_pyc) and fpth_pyc not in ret_pyc_f:
            ret_pyc_f.append(fpth_pyc)

    return ret_pyc_f
            # copy2(ea, pyc_dest_dir_18)

def copy2(fn,destd_dir): # execute sys copy operation
    if not os.path.exists(destd_dir):
        os.makedirs(destd_dir)
    fn_nm = os.path.basename(fn)
    dest_full = os.path.join(destd_dir,fn_nm)
    shutil.copy2(fn,dest_full)
    # subprocess.Popen(["copy", fn, destd_dir], shell=True)
    # shutil.c
    # print "\n source: {}".format(fn)
    # print "\n destination: {}".format(destd_dir)
if __name__ == "__main__":
    # serverDir = r"Z:\TD\scripts_test\TD_update_test\server_dir"
    serverDir = r"\\192.168.80.204\test\Files"

    # pycDir = r"Z:\TD\scripts_test\TD_update_test\pyc_dir"
    pycDir = r"\\octvision.com\CG\Tech"
    myProjDir = r"F:\git_test_myProj"
    # serverDir = r"\\192.168.80.204\test\Files"
    # pycDir = r"\\octvision.com\CG\Tech"

    mainCopy(serverDir,pycDir)
    # print "HHH"