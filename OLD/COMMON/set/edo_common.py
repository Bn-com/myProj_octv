import maya.OpenMayaUI as omui
import sip
import PyQt4.QtCore as QtCore,PyQt4.QtGui as QtGui

def edo_getMayaWindow():
    ptr = omui.MQtUtil.mainWindow()
    return sip.wrapinstance(long(ptr), QtCore.QObject)