#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = td_src_py_mod.py
__author__ = zhangben 
__mtime__ = 2019/7/9 : 11:59
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
"""
import socket
import os,sys,re
def im_py_mod(mod_f_path):
    f_pth_norm = os.path.normpath(mod_f_path)
    f_dir,f_nm = os.path.split(f_pth_norm)
    mod_path =  re.sub(r'\\','.',f_pth_norm)
    under_python_module = re.search("Python.[\w.]+[^.py]",mod_path)
    cmdStr_head,cmdStr='',''
    pth, mod_nm = '',''
    if under_python_module:
        relative_path = under_python_module.group()
        pth,mod_nm = ".".join(relative_path.split('.')[1:-1]),relative_path.split('.')[-1]
        cmdStr = "from {0} import {1};reload({1})".format(pth, mod_nm)
    else:
        print(">>not under python module....")
        pth = re.sub(r'\\','.',f_dir)
        mod_nm = os.path.splitext(f_nm)[0]
        cmdStr_head = "import sys;sys.path.insert(0,r\"{}\"){}".format(f_dir,os.linesep)
        cmdStr = "{0}import {1};reload({1})".format(cmdStr_head, mod_nm)
    print cmdStr
    exeCmd = "print \"{}\"".format(cmdStr)
    # exeCmd = ("print 'ok'")
    # print exeCmd

    HOST = '127.0.0.1'
    PORT = 4434
    ADDRS = (HOST,PORT)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(ADDRS)
    sndMsg = 'print "\\n{}"'.format(cmdStr)
    s.send(sndMsg.encode('utf-8'))
    # s.send(exeCmd)
    # exec(exeCmd)
    print('---------------------')
    modifiedMessage, serverAddress = s.recvfrom(2048)
    print (modifiedMessage)
    s.close()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(ADDRS)
    # myMsg="import pymel.core as pm\npm.polyCube()"
    # s.send(myMsg.encode('utf-8'))
    # print('============================')
    # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # s.connect(ADDRS)
    # cmdStr2 = "from {0} import {1};reload({1})".format(pth,mod_nm)
    cmdStr2 = cmdStr
    print(cmdStr2)
    myMsg = cmdStr2
    s.send(myMsg.encode('utf-8'))
    s.close()
    print('=====================')
if __name__ == "__main__":
    fpth_full = sys.argv[1]
    im_py_mod(fpth_full)
    # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # s.connect(('127.0.0.1', 4434))
    # s.send('print "Hello World"')