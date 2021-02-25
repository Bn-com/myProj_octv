#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = Path2ModuleStyle
__author__ = zhangben 
__mtime__ = 2020/3/23 : 11:42
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
"""
import socket
import os,sys,re
def path2ModuleStype(mod_f_path):
    f_pth_norm = os.path.normpath(mod_f_path)
    mod_path =  re.sub(r'\\','.',f_pth_norm)
    relative_path = re.search("Python.[\w.]+[^.py]",mod_path).group()
    HOST = '127.0.0.1'
    PORT = 4434
    ADDRS = (HOST,PORT)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(ADDRS)
    sndMsg = 'print "\\n{}"'.format(relative_path)
    s.send(sndMsg.encode('utf-8'))
    # s.send(exeCmd)
    # exec(exeCmd)
    print('---------------------')
    modifiedMessage, serverAddress = s.recvfrom(2048)
    print (modifiedMessage)
    s.close()
    # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # s.connect(ADDRS)
    # myMsg="import pymel.core as pm\npm.polyCube()"
    # s.send(myMsg.encode('utf-8'))
    # print('============================')
    # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # s.connect(ADDRS)
    # print(cmdStr2)
    # myMsg = cmdStr2
    # s.send(myMsg.encode('utf-8'))
    # s.close()
    # print('=====================')
if __name__ == "__main__":
    fpth_full = sys.argv[1]
    path2ModuleStype(fpth_full)
    # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # s.connect(('127.0.0.1', 4434))
    # s.send('print "Hello World"')