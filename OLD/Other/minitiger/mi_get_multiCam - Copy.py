# -*- coding: utf-8 -*-

# Form implementation generated from reading myuis file 'mi_get_multiCam.myuis'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(183, 111)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setMargin(3)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.f_cb = QtGui.QCheckBox(self.groupBox)
        self.f_cb.setObjectName(_fromUtf8("f_cb"))
        self.horizontalLayout.addWidget(self.f_cb)
        self.m_cb = QtGui.QCheckBox(self.groupBox)
        self.m_cb.setObjectName(_fromUtf8("m_cb"))
        self.horizontalLayout.addWidget(self.m_cb)
        self.n_cb = QtGui.QCheckBox(self.groupBox)
        self.n_cb.setObjectName(_fromUtf8("n_cb"))
        self.horizontalLayout.addWidget(self.n_cb)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.rb_add = QtGui.QRadioButton(self.groupBox)
        self.rb_add.setObjectName(_fromUtf8("rb_add"))
        self.horizontalLayout_2.addWidget(self.rb_add)
        self.rb_rep = QtGui.QRadioButton(self.groupBox)
        self.rb_rep.setObjectName(_fromUtf8("rb_rep"))
        self.horizontalLayout_2.addWidget(self.rb_rep)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.QPB_OK = QtGui.QPushButton(self.groupBox)
        self.QPB_OK.setObjectName(_fromUtf8("QPB_OK"))
        self.horizontalLayout_3.addWidget(self.QPB_OK)
        self.pushButton = QtGui.QPushButton(self.groupBox)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addWidget(self.groupBox)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.groupBox.setTitle(_translate("MainWindow", "reference camera:", None))
        self.f_cb.setText(_translate("MainWindow", "far", None))
        self.m_cb.setText(_translate("MainWindow", "mid", None))
        self.n_cb.setText(_translate("MainWindow", "near", None))
        self.rb_add.setText(_translate("MainWindow", "add", None))
        self.rb_rep.setText(_translate("MainWindow", "replace", None))
        self.QPB_OK.setText(_translate("MainWindow", "OK", None))
        self.pushButton.setText(_translate("MainWindow", "Cancel", None))

