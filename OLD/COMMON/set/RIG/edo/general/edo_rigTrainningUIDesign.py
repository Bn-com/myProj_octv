# -*- coding: utf-8 -*-

# Form implementation generated from reading myuis file '//file-cluster/GDC/Resource/Support/Maya/extra/Rigging_Simulation/python/edo/general/edo_rigTrainningUI.myuis'
#
# Created: Tue Sep 10 15:01:48 2013
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_edo_rigTrainningUI(object):
    def setupUi(self, edo_rigTrainningUI):
        edo_rigTrainningUI.setObjectName(_fromUtf8("edo_rigTrainningUI"))
        edo_rigTrainningUI.resize(398, 400)
        edo_rigTrainningUI.setWindowTitle(QtGui.QApplication.translate("edo_rigTrainningUI", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.centralwidget = QtGui.QWidget(edo_rigTrainningUI)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.BT_elementary = QtGui.QPushButton(self.centralwidget)
        self.BT_elementary.setGeometry(QtCore.QRect(10, 10, 383, 107))
        self.BT_elementary.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/elementary/training_elementary.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BT_elementary.setIcon(icon)
        self.BT_elementary.setIconSize(QtCore.QSize(383, 107))
        self.BT_elementary.setObjectName(_fromUtf8("BT_elementary"))
        self.BT_upperIntermediate = QtGui.QPushButton(self.centralwidget)
        self.BT_upperIntermediate.setGeometry(QtCore.QRect(10, 130, 383, 107))
        self.BT_upperIntermediate.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/intermediate/training_intermediate.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BT_upperIntermediate.setIcon(icon1)
        self.BT_upperIntermediate.setIconSize(QtCore.QSize(383, 107))
        self.BT_upperIntermediate.setObjectName(_fromUtf8("BT_upperIntermediate"))
        self.BT_elementary_3 = QtGui.QPushButton(self.centralwidget)
        self.BT_elementary_3.setGeometry(QtCore.QRect(10, 250, 383, 107))
        self.BT_elementary_3.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/upperIntermediate/training_upperIntermediate.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BT_elementary_3.setIcon(icon2)
        self.BT_elementary_3.setIconSize(QtCore.QSize(383, 107))
        self.BT_elementary_3.setObjectName(_fromUtf8("BT_elementary_3"))
        edo_rigTrainningUI.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(edo_rigTrainningUI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 398, 18))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        edo_rigTrainningUI.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(edo_rigTrainningUI)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        edo_rigTrainningUI.setStatusBar(self.statusbar)

        self.retranslateUi(edo_rigTrainningUI)
        QtCore.QMetaObject.connectSlotsByName(edo_rigTrainningUI)

    def retranslateUi(self, edo_rigTrainningUI):
        pass

import RIG_trainningTool_icon_rc
