#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = cnvt_rsc2py
__author__ = zhangben 
__mtime__ = 2020/9/27 : 10:19
__description__: 

    code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""
import subprocess, os


def batch_imgs2qrc2py(folder):
    imagesFoder = os.path.abspath(os.path.join(folder,"../icons"))
    print(imagesFoder)


# def qrc2py():
#     images = os.listdir('./icons')
#     qss = os.listdir('./qss')
#     f = open('images.qrc', 'w+')
#     f.write(u'<!DOCTYPE RCC>\n<RCC version="1.0">\n<qresource>\n')
#
#     for item in images:
#         f.write(u'<file alias="icons/'+ item +'">icons/'+ item +'</file>\n')
#
#     for item in qss:
#         f.write(u'<file alias="qss/'+ item +'">qss/'+ item +'</file>\n')
#
#     f.write(u'</qresource>\n</RCC>')
#     f.close()
def qrc2py(qrcfpth):
    py_name = "{}_rc.py".format(os.path.splitext(qrcfpth)[0])
    pipe = subprocess.Popen(r'pyrcc4 -o {} {}'.format(py_name,qrcfpth), stdout = subprocess.PIPE, stdin = subprocess.PIPE, stderr = subprocess.PIPE, creationflags=0x08)

if __name__ == "__main__":
    import sys
    uSel = sys.argv[1]
    if os.path.isfile(uSel):
        print("You Need to Select a folder not a file....")
        qrc2py(uSel)
    else:
        print("EM.....................")
        batch_imgs2qrc2py(uSel)