# -*- coding: utf-8 -*-
import maya.cmds
import maya.OpenMaya
import os

def test_print():
    f = os.popen('D:\\Alias\\MAYA2012x64\\bin\\render.exe -sw:mm 128 -rd E:\\SC_099\\images C:\\Users\\huangzhongwei\\Documents\\maya\\projects\\default\\scenes\\prv_do4_005_051_ly_003.ma')
    while True:
        line = f.readline()
        if line == None:
            break
        print line
    f.close()