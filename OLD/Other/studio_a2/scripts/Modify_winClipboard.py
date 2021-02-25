#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''    
__author__ = 'zhangben'
__mtime__ = '2017/6/27:9:43'
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
'''

import win32con
import win32clipboard as w

def getText():
    d = ""
    if w.IsClipboardFormatAvailable(win32con.CF_UNICODETEXT):
        w.OpenClipboard()
        d = w.GetClipboardData(win32con.CF_UNICODETEXT)
        w.CloseClipboard()
    return d

def setText(aString):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT, aString)
    w.CloseClipboard()

if __name__ == "__main__":
    getStr = getText()
    # print getStr
    modi_str = ur"\\192.168.168.14\Home\projects%s" % getStr
    setText(modi_str)

