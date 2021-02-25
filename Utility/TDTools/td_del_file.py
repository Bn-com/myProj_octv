#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = 'pc_checkinCommon'
__author__ = zhangben
__mtime__ = 2018/12/7:12:00
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
'''
import sys,re,os,shutil,datetime
import py_compile
import subprocess

def mainDel(serverDir,pycDir): #main process  copy selected itme (nonsupport mutile select)
    fpth = sys.argv[-1]
    delFile(fpth,serverDir,pycDir)


def delFile(fpth,serverDir,pycDir): # via file path copy to server
    if os.path.isfile(fpth):
        fpth_spl = os.path.splitext(fpth)
        re_relatively = re.compile("(maya_sixteen)\S+|(Nuke)\S+|(Utility)\S+|(maya_eighteen)\S+")
        if not re_relatively.search(fpth):
            raise Exception("your should select a py or mel file in repository")
        copyFiles = [fpth]
        if fpth_spl[1] == '.py':
            fpth_pyc = "{}.pyc".format(fpth_spl[0])
            py_compile.compile(fpth)
            copyFiles.append(fpth_pyc)
        copyFiles.reverse()
        for ea in copyFiles:
            subPth = re_relatively.search(fpth).group()
            serverDirS = [r"maya\\2016", r"maya\\2018"]
            dest_dir_lst = []
            fpth_spl_fn = os.path.split(ea)
            for ea_sver in serverDirS:
                subPth_serv = re.sub("maya_sixteen", ea_sver, subPth)
                if subPth_serv == subPth: subPth_serv = re.sub("maya_eighteen", ea_sver, subPth)
                subPth_serv_spl = os.path.split(subPth_serv)
                subdir_serv = subPth_serv_spl[0]
                dest_dir = os.path.join(serverDir, subdir_serv)
                if dest_dir not in dest_dir_lst: dest_dir_lst.append(dest_dir)
                # print("line 43")
                # print dest_dir_lst
            for edir in dest_dir_lst:
                rm_path = os.path.join(edir, fpth_spl_fn[-1])
                # print(" file :::{} to path ::{}".format(rm_path, edir))
                if os.path.isfile(rm_path):
                    # bk_del_targ(serverDir,subPth)
                    os.remove(rm_path)
                    print ("50:::py file>>>{} remove from path ::{}".format(rm_path, edir))
            if copyFiles.index(ea) == 0:
                pyc_dest_dir = os.path.join(pycDir, os.path.split(subPth)[0])
                pyc_dest_dir_18 = os.path.join(pycDir, re.sub(r"sixteen", "eighteen", os.path.split(subPth)[0]))
                if os.path.isfile(os.path.join(pyc_dest_dir,fpth_spl_fn[-1])):
                    os.remove(os.path.join(pyc_dest_dir,fpth_spl_fn[-1]))
                    print (" 56 pyc file :::{} remove from path ::{}".format(fpth_spl_fn[-1], pyc_dest_dir))
                if os.path.isfile(os.path.join(pyc_dest_dir_18, fpth_spl_fn[-1])):
                    os.remove(os.path.join(pyc_dest_dir_18, fpth_spl_fn[-1]))
                    print (" 59 pyc file :::{} remove from path ::{}".format(fpth_spl_fn[-1], pyc_dest_dir_18))
            os.remove(ea)
    elif os.path.isdir(fpth):
        re_relatively = re.compile("(maya_sixteen)\S+|(Nuke)\S+|(Utility)\S+|(maya_eighteen)\S+")
        serverDirS = [r"maya\\2016", r"maya\\2018"]
        subPth = re_relatively.search(fpth).group()
        pyc_2016 = os.path.abspath(os.path.join(pycDir, subPth))
        if os.path.exists(pyc_2016):  shutil.rmtree(pyc_2016)
        pyc_2018 = os.path.join(pycDir, re.sub("maya_sixteen", "maya_eighteen", subPth))
        print("The Folder << {} >> removed from server ::: {} ".format(subPth, pycDir))
        if pyc_2018 != pyc_2016 and os.path.exists(pyc_2018):
            shutil.rmtree(os.path.abspath(pyc_2018))
            print("The Folder << {} >> removed from server ::: {} ".format(re.sub("maya_sixteen", "maya_eighteen", subPth), pycDir))
        del_fold_lst = []
        # for ea_sver in serverDirS:
        #     subPth_serv = re.sub("maya_sixteen", ea_sver, subPth)
        #     if subPth_serv == fpth: subPth_serv = re.sub("maya_eighteen", ea_sver, subPth)
        #     del_fold_pth = os.path.abspath(os.path.join(serverDir, subPth_serv))
        #     if del_fold_pth not in del_fold_lst: del_fold_lst.append(del_fold_pth)
        # for ea_dir in del_fold_lst:
        #     if os.path.isdir(ea_dir):
        #         # print ea_dir
        #         # print subPth
        #         # bk_del_targ(serverDir,subPth)
        #         print del_fold_pth
        #         # shutil.rmtree(del_fold_pth)
        #         print(" 79 The Folder << {} >> removed from server ::: {} ".format(ea_dir, serverDir))
        print fpth
        print(os.path.islink(fpth))
        # os.system("rd/s/q {}".format(fpth))
#
#
# def bk_del_targ(serverDir,subPth,bkPth=r'F:\Development\delbak'):
#     # re_relatively = re.compile("(maya_sixteen)\S+|(Nuke)\S+|(Utility)\S+|(maya_eighteen)\S+")
#     print("================")
#     print ("89 {}".format(subPth))
#     src_dir = os.path.join(serverDir,subPth)
#     print("81 {}".format(src_dir))
#     targ = os.path.join(bkPth,subPth)
#     # if os.path.exists(bk_dir):
#     targ_upper_folder = os.path.dirname(targ)
#     print("95 {}".format(targ_upper_folder))
#     f_bnm = os.path.basename(subPth)
#     f_bnm_splx = os.path.splitext(f_bnm)
#     bkf_bnm = "{}_{}".format(f_bnm_splx[0],(datetime.datetime.now().strftime('%Y_%d_%m_%H%M%S')))
#     bk_f_bnm_hole = "{}{}".format(bkf_bnm,f_bnm_splx[-1])
#     bk_f_nm_full = os.path.join(targ_upper_folder,f_bnm)
#     bk_f_nm_full_new = os.path.join(targ_upper_folder,bk_f_bnm_hole)


    # print(src_dir)
    # print(targ_upper_folder)
    # # print(bk_f_nm_full)
    # print("========================================")
    # print (bk_f_nm_full_new)
    # shutil.move(src_dir,targ_upper_folder)
    # os.rename(bk_f_nm_full,bk_f_nm_full_new)
    #
    # # shutil.move(src_dir, bk_nm_top)
    # # os.rename()
    # print ("88 {}".format(bk_nm_new))
    # shutil.move(src_dir,bk_nm_new)


     # = os.path.join(bkPth,'{}_{}'.format((datetime.datetime.now().strftime('%Y_%d_%m_%H%M%S'),subPth))

if __name__ == "__main__":
    # serverDir = r"Z:\TD\scripts_test\TD_update_test\server_dir"
    serverDir = r"\\192.168.80.204\test\Files"
    # pycDir = r"Z:\TD\scripts_test\TD_update_test\pyc_dir"
    pycDir = r"\\octvision.com\CG\Tech"
    myProjDir = r"F:\git_test_myProj"
    # serverDir = r"\\192.168.80.204\test\Files"
    # pycDir = r"\\octvision.com\CG\Tech"

    mainDel(serverDir,pycDir)