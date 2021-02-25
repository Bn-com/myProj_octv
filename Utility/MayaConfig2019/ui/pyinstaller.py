#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = pyinstaller.py
__author__ = zhangben
__mtime__ = 2019/5/5 : 16:01
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
"""
import os

if __name__ == "__main__":
    from PyInstaller.__main__ import run
    # opts = ['Setup.py','-F','-w']
    opts = ['MayaConfig.py','-F','-w','-p \"C:\\Python27\\Lib\\site-packages\\PyQt4\"']
    run(opts)