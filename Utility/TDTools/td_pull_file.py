#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = td_pull_file.py
__author__ = zhangben
__mtime__ = 2019/1/30 : 11:33
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
"""

import os,re,sys
import py_compile
import subprocess
import time
# from PyQt4 import QtGui
# from PyQt4 import QtCore
#
# from PyQt4 import QtWidgets

# import Tkinter
# import tkMessageBox

# serverDir = r"Z:\TD\scripts_test\TD_update_test\server_dir"
# pycDir = r"Z:\TD\scripts_test\TD_update_test\pyc_dir"


# fpth_full = r'Z:\TD\scripts_test\TD_update_test\pyc_dir\Utility'
#
# class MyWin(QtGui.QtWid)
#
# app = QtGui.QApplication(sys.argv)
# msg_box = QtGui.QMessageBox.information("the file on server is older","are you want to copy?",QtGui.QMessageBox.Yes|QtGui.QMessageBox.No)
# msg_box.show()
# app.exec_()

# customMsgBox = QtGui.QMessageBox(self)



def refreshScript(remoteFile,localFile,refOlder=True,override=False):
    lclf_mt = os.stat(localFile).st_mtime
    if not os.path.isfile(remoteFile):
        print("There is not corresponding file on the server")
        return None
    rmtf_mt = os.stat(remoteFile).st_mtime
    print "remote file modified time is {}".format(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(rmtf_mt)))
    print "local file modified time is {}".format(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(lclf_mt)))

    if time.localtime(rmtf_mt) != time.localtime(lclf_mt) and not refOlder:
        print("the file [{}] on remote is older ".format(remoteFile))
        return None
    if not override: return

    with open(remoteFile) as books:
        rdlns = books.readlines()

    with open(localFile,'w') as upBooks:
        upBooks.writelines(rdlns)
    print("file refereshed : {}".format(localFile))

def pullFromRemote(fpth,serverDir,refOlder=True,ovr=False): # 从服务器端同步本地脚本文件
    # fpth_spl = os.path.splitext(fpth)
    re_relatively = re.compile("(maya_sixteen)\S+|(Nuke)\S+|(Utility)\S+")
    if not re_relatively.search(fpth):
        raise Exception("your should select a py or mel file in repository")
    subPth = re_relatively.search(fpth).group()
    # print subPth
    subPth_serv = re.sub("maya_sixteen", r"maya\\2016", subPth)
    # if subPth_serv == subPth: subPth_serv = re.sub(r"maya\\2016","maya_sixteen",subPth)
    # print subPth_serv
    # raise Exception ("Td Check")
    fpth_serve = os.path.join(serverDir, subPth_serv)
    # print fpth_serve
    if os.path.isfile(fpth):
        refreshScript(fpth_serve,fpth,refOlder,ovr)
    elif os.path.isdir(fpth):
        for root,dirs,files in os.walk(fpth_serve):
            for ea_f in files:
                targFile = os.path.join(root,ea_f)
                pullFromRemote(targFile,serverDir,True)


if __name__ == "__main__":
    # """
    # serverDir = r"Z:\TD\scripts_test\TD_update_test\server_dir"
    serverDir = r"\\192.168.80.204\test\Files"
    fpth_full = sys.argv[1]
    forceArg = int(sys.argv[-1])
    pullFromRemote(fpth_full,serverDir,forceArg,True)
    # """
    # print fpth_full
    # print forceArg

