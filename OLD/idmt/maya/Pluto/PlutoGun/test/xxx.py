import maya.OpenMayaUI as apiUI
from PyQt4 import QtGui, QtCore
from PyQt4 import QtCore
import sip

import maya.cmds as cmds




class MayaSubWindow(QtGui.QMainWindow):
    maya_ptr = apiUI.MQtUtil.mainWindow()
    ptr = sip.wrapinstance(long(maya_ptr), QtCore.QObject)    
    def __init__(self, parent = ptr):
        super(MayaSubWindow, self).__init__(parent)

        form = cmds.formLayout()
        editor = cmds.modelEditor()
        column = cmds.columnLayout('true')
        cmds.formLayout( form, edit=True, attachForm=[(column, 'top', 0), (column, 'left', 0), (editor, 'top', 0), (editor, 'bottom', 0), (editor, 'right', 0)], attachNone=[(column, 'bottom'), (column, 'right')], attachControl=(editor, 'left', 0, column))

        camera= cmds.camera(centerOfInterest=2.450351,
                                position = (1.535314, 1.135712, 1.535314),
                                rotation = (-27.612504, 45, 0),
                                worldUp = (-0.1290301, 0.3488592, -0.1290301))
        
        cmds.modelEditor( editor, edit=True, camera=camera[0] )



        self.layout = form


        qtObj = self.toQtObject(self.layout)
        #Fill the window, could use qtObj.setParent
        #and then add it to a layout.
        self.setCentralWidget(qtObj)


    def toQtObject(self, mayaName):
        '''
        Given the name of a Maya UI element of any type,
        return the corresponding QWidget or QAction.
        If the object does not exist, returns None
        '''
        ptr = apiUI.MQtUtil.findControl(mayaName)
        if ptr is None:
            ptr = apiUI.MQtUtil.findLayout(mayaName)
        if ptr is None:
            ptr = apiUI.MQtUtil.findMenuItem(mayaName)
        if ptr is not None:
            return sip.wrapinstance(long(ptr), QtCore.QObject)







myWindow = MayaSubWindow()


myWindow.show()
