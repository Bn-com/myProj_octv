#-*- coding: gbk -*-
'''
Created on 2013-8-20
@contact:    power_zzj@163.com
@deffield    updated: Updated
@author: zhaozhongjie
usage:
    import idmt.maya.Pluto.Maya.Rnd.ImageSwitchPath as isp
    reload(isp)
    isp.main()
'''

import os,sys
import PyQt4


from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.uic import loadUi
import sip
import dockwidgets_rc

try:
    import maya.OpenMayaUI as apiUI
    import maya.cmds as cmds
    import maya.mel as mel
except:
    pass    

def getMayaWindow():
    ptr = apiUI.MQtUtil.mainWindow()
    return sip.wrapinstance(long(ptr), QtCore.QObject)

class MainWindow(QtGui.QMainWindow):
    parent = None
    appName = qApp.applicationName()
    if 'Maya' in appName:
        parent = getMayaWindow()
    
    def __init__(self , p = parent):
        super(MainWindow, self).__init__(p)

#         self.textEdit = QtGui.QTextEdit()
#         self.setCentralWidget(self.textEdit)
        self.resize(1024, 768)
        
        self.createActions()
        self.createMenus()
        self.createToolBars()
        self.createStatusBar()
        self.createDockWindows()

        self.setWindowTitle("Pluto_ImageFileManager")

        self.setUnifiedTitleAndToolBarOnMac(True)

    def save(self):
        filename = QtGui.QFileDialog.getSaveFileName(self,
                "Choose a file name", '.', "HTML (*.html *.htm)")
        if not filename:
            return

        file = QtCore.QFile(filename)
        if not file.open(QtCore.QFile.WriteOnly | QtCore.QFile.Text):
            QtGui.QMessageBox.warning(self, "Dock Widgets",
                    "Cannot write file %s:\n%s." % (filename, file.errorString()))
            return

        out = QtCore.QTextStream(file)
        QtGui.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        out << self.textEdit.toHtml()
        QtGui.QApplication.restoreOverrideCursor()

        self.statusBar().showMessage("Saved '%s'" % filename, 2000)

    def undo(self):
        document = self.textEdit.document()
        document.undo()

    def optionCMD(self):
        print 'configure'

    def fullScreenCMD(self):
        print 'fullScreen'

    def refreshCMD(self):
        print 'refresh'

    def infoCMD(self):
        print 'info'
        
    def about(self):
        QtGui.QMessageBox.about(self, "About Dock Widgets",
                "The <b>Dock Widgets</b> example demonstrates how to use "
                "Qt's dock widgets. You can enter your own text, click a "
                "customer to add a customer name and address, and click "
                "standard paragraphs to add them.")

    def restoreWindow(self):
        
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.dock_icon)
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.dock_browse)
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.dock_tools)
        
        self.dock_icon.setFloating(0)
        self.dock_browse.setFloating(0)
        self.dock_tools.setFloating(0)
        self.dock_icon.show()
        self.dock_browse.show()
        self.dock_tools.show()
        
        self.fileToolBar.setAllowedAreas(Qt.BottomToolBarArea)
        self.editToolBar.setAllowedAreas(Qt.BottomToolBarArea)



#         self.fileToolBar.setMovable(0)
#         self.editToolBar.setMovable(0)

        
        self.addToolBar(self.fileToolBar) 
        self.addToolBar(self.editToolBar) 

    def createActions(self):	                  	                     	    #    ====Action====
#    Action_1.    全屏
        ico = QImageReader('ico/fullScreen.ico')
        ico.jumpToImage(1)
        ico = QIcon(QPixmap.fromImage(ico.read()))
        self.fullScreenAct = QtGui.QAction(ico,
                "&FullScreen", self, shortcut=QtGui.QKeySequence.Save,
                statusTip=u"全屏显示图片",
                triggered=self.fullScreenCMD)
        
#    Action_2.    刷新
        self.refreshAct = QtGui.QAction( self.style().standardIcon(  QtGui.QStyle.SP_BrowserReload ),
                u"&R刷新", self,
                statusTip=u"刷新显示",
                triggered =self.refreshCMD)

#    Action_3.    信息
        self.infoAct = QtGui.QAction( self.style().standardIcon(  QtGui.QStyle.SP_MessageBoxInformation ),
                u"&I信息", self,
                statusTip=u"图片的信息",
                triggered =self.infoCMD)
        
#    Action_4.    配置
        ico = QImageReader('ico/configure.ico')
        ico.jumpToImage(1)
        ico = QIcon(QPixmap.fromImage(ico.read()))
        self.optionAct = QtGui.QAction(ico,
                "&Option", self, shortcut=QtGui.QKeySequence.New,
                statusTip=u"详细配置",
                triggered=self.optionCMD)
        
        
        
        self.saveAct = QtGui.QAction(QtGui.QIcon(':/images/save.png'),
                "&Save...", self, shortcut=QtGui.QKeySequence.Save,
                statusTip="Save the current form letter",
                triggered=self.save)

        self.printAct = QtGui.QAction(QtGui.QIcon(':/images/print.png'),
                "&Print...", self, shortcut=QtGui.QKeySequence.Print,
                statusTip="Print the current form letter",
                triggered=self.save)

        
        self.undoAct = QtGui.QAction(QtGui.QIcon(':/images/undo.png'),
                "&Undo", self, shortcut=QtGui.QKeySequence.Undo,
                statusTip="Undo the last editing action", triggered=self.undo)

        unuseList = [
        'SP_MessageBoxWarning','SP_MessageBoxQuestion',
        'SP_DriveFDIcon','SP_DirOpenIcon',
        'SP_DialogApplyButton',
        'SP_ArrowUp','SP_ArrowDown','SP_ArrowLeft','SP_ArrowRight',
        'SP_BrowserStop','SP_DesktopIcon',
        'SP_MediaPlay','SP_MediaStop','SP_MediaPause','SP_MediaSkipForward','SP_MediaSkipBackward','SP_MediaSeekForward','SP_MediaSeekBackward','SP_MediaVolume','SP_MediaVolumeMuted'
                     ]
        
        xxxxList = [
        'SP_MessageBoxCritical'
        ]
        
        self.actxxx = []
        for x in xxxxList:
            tmp = QtGui.QAction( self.style().standardIcon(  eval('QtGui.QStyle.'+x) ),x,self)
            self.actxxx.append(tmp)
        

        self.quitAct = QtGui.QAction("&Quit", self, shortcut="Ctrl+Q",
                statusTip="Quit the application", triggered=self.close)

        self.aboutAct = QtGui.QAction("&About", self,
                statusTip="Show the application's About box",
                triggered=self.about)

        self.aboutQtAct = QtGui.QAction("About &Qt", self,
                statusTip="Show the Qt library's About box",
                triggered=QtGui.qApp.aboutQt)

        self.restroeDockAct = QtGui.QAction(  u"&R重置所有窗口", self,
                statusTip=u"重置所有窗口",
                triggered =self.restoreWindow)

    def createMenus(self):                     	                     	    #    ====Menu====
#    File 
        self.fileMenu = self.menuBar().addMenu(u"文件(&F)")
        self.fileMenu.setTearOffEnabled(1)
        
        self.fileMenu.addAction(self.saveAct)
        self.fileMenu.addAction(self.printAct)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.quitAct)

#    Edit
        self.editMenu = self.menuBar().addMenu(u"编辑(&E)")
        self.editMenu.setTearOffEnabled(1)
        
        self.editMenu.addAction(self.undoAct)

#    Tools
        self.toolMenu = self.menuBar().addMenu(u"工具(&T)")
        self.toolMenu.setTearOffEnabled(1)
        
        self.toolMenu.addAction(self.refreshAct)
        self.toolMenu.addAction(self.infoAct)
        self.toolMenu.addAction(self.optionAct)

#    Window
        self.windowMenu = self.menuBar().addMenu(u"窗口(&W)")
        self.windowMenu.setTearOffEnabled(1)
        
        self.windowMenu.addAction(self.restroeDockAct)
        

#    Help
        self.helpMenu = self.menuBar().addMenu(u"帮助(&H)")
        self.helpMenu.setTearOffEnabled(1)
        
        self.helpMenu.addAction(self.aboutAct)
        self.helpMenu.addAction(self.aboutQtAct)


    def createToolBars(self):	                                     	    #    ====ToolBar====
#    ToolBar_1.    Tool
        self.fileToolBar = self.addToolBar("File")
        self.fileToolBar.addAction(self.fullScreenAct)
        self.fileToolBar.addAction(self.refreshAct)
        self.fileToolBar.addAction(self.infoAct)
        self.fileToolBar.addAction(self.optionAct)

#    ToolBar_2.    Edit
        self.editToolBar = self.addToolBar("Edit")
        self.editToolBar.addAction(self.saveAct)
        self.editToolBar.addAction(self.undoAct)
        for x in self.actxxx:
            self.editToolBar.addAction(x)
            
#         self.fileToolBar.setEnabled(0)
#         self.editToolBar.setEnabled(0)
            
        
#    设置主窗口ToolBars图标大小
        toolbars = self.findChildren(QToolBar)
        for toolbar in toolbars:
            toolbar.setIconSize(QSize(24,24))

    def createStatusBar(self):
        self.statusBar().showMessage("Ready")

    def createDockWindows(self):
        self.dock_icon = QtGui.QDockWidget(u"图标", self)
        self.setCentralWidget(self.dock_icon)
#         self.dock_icon.setAllowedAreas(QtCore.Qt.RightDockWidgetArea)
        self.dock_icon.setWidget(QtGui.QTextEdit())
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.dock_icon)
#         self.dock_icon.setFeatures(QtGui.QDockWidget.NoDockWidgetFeatures  )


        self.dock_browse = QtGui.QDockWidget(u"浏览图片", self)
        self.dock_browse.setWidget(QtGui.QTextEdit())
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.dock_browse)



        self.dock_tools = QtGui.QDockWidget(u"工具", self)
        self.dock_tools.setWidget(QtGui.QTextEdit())
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.dock_tools)


        self.windowMenu.addAction(self.dock_icon.toggleViewAction())
        self.windowMenu.addAction(self.dock_browse.toggleViewAction())
        self.windowMenu.addAction(self.dock_tools.toggleViewAction())
        



def main():
    appName = qApp.applicationName()
    
    if 'Maya'in appName:
        mainWin = MainWindow()
        mainWin.show()        
    else:
        app = QtGui.QApplication(sys.argv)
        mainWin = MainWindow()
        mainWin.show()
        sys.exit(app.exec_())


if __name__ == '__main__':
    main()
    
    
