# -*- coding: utf-8 -*-
import maya.cmds as mc
import maya.mel as mel
import os
import re
def csl_fixReferenceNamespaceWin():
    if mc.window('csl_fixNamespaceWin',exists = True):
        mc.deleteUI('csl_fixNamespaceWin')

    mc.window('csl_fixNamespaceWin', title = u'csl -- fix reference namespace', width = 500, height = 180, sizeable = True)
    mc.columnLayout(rowSpacing=2, columnAttach = ['both',5],columnWidth = 500, columnAlign = 'left')
    mc.textFieldButtonGrp('pathText', label=u'路径：', text=u'输入要修改的文件的路径 如： D:\csl', buttonLabel='List Files', buttonCommand = 'csl_listFiles()')
    mc.separator( height = 3, style='none' )
    mc.textScrollList('maFiles', allowMultiSelection = True, selectCommand = 'mc.button("change", e = True, label = u"Change By Selected File")')
    mc.popupMenu()
    mc.menuItem(label = 'deselectAll', c = 'mc.textScrollList("maFiles", e = True , deselectAll = True)\r\nmc.button("change", e = True, label = u"Change All Files")')

    mc.button('change',label = 'Change All Files', c = 'cls_doFixProc()')
    mc.showWindow( 'csl_fixNamespaceWin' )

def csl_listFiles():
    path = mc.textFieldButtonGrp('pathText', q = True , text = True)
    allFiles = os.listdir(path)
    mc.textScrollList('maFiles', e = True , ra = True)
    for ma in allFiles:
        if ma.find('.ma') > -1:
            mc.textScrollList('maFiles', e = True , append = ma)

def cls_doFixProc():
    keyWords = '-rpr'
    dollaWords = '-ns'
    pattern = re.compile('^file ')

    path = mc.textFieldButtonGrp('pathText', q = True , text = True) + '\\'
    selItems = mc.textScrollList('maFiles', q = True , selectItem = True)
    if not selItems:
        selItems = mc.textScrollList('maFiles', q = True , allItems = True)
    fixedPath = path + '/Fixed/'
    if not os.path.isdir(fixedPath):
        os.mkdir(fixedPath)

    amount = 0
    itemsNum = len(selItems)
    mc.progressWindow(title = "csl fix namespace", progress =  amount, status = u'请等待......', min = 0, max = itemsNum, isInterruptable = True)

    for item in selItems:
        if mc.progressWindow (query = True, isCancelled = True ):
            break
        if mc.progressWindow (query = True, progress = True) > itemsNum :
            break
        mc.progressWindow( edit = True, progress = amount, status = u'请等待......')


        maFile = path + item
        fh = open(maFile,'r')
        fh2 = open(fixedPath + item,'w')
        for i in fh.readlines():
            if pattern.match(i):
                i = i.replace(keyWords,dollaWords)

                fh2.writelines(i)

            else:
                fh2.writelines(i)

        fh.close()
        fh2.close()
        amount = amount + 1

    mc.progressWindow ( endProgress = True )

    tmpPath = 'system("load ' + fixedPath + '" )'
    print tmpPath
    mel.eval(tmpPath) 
    
    
csl_fixReferenceNamespaceWin()
