# -*- coding: utf-8 -*-

# Form implementation generated from reading myuis file 'M:\Sync_KP\Script\a2_work_proj\other\UI\CopySetDrivenKeyTools.myuis'
#
# Created: Wed Oct 18 11:10:32 2017
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
import sys
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
        MainWindow.resize(800, 442)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.drvn_obj_info_gbx = QtGui.QGroupBox(self.centralwidget)
        self.drvn_obj_info_gbx.setGeometry(QtCore.QRect(40, 90, 531, 111))
        self.drvn_obj_info_gbx.setObjectName(_fromUtf8("drvn_obj_info_gbx"))
        self.widget = QtGui.QWidget(self.drvn_obj_info_gbx)
        self.widget.setGeometry(QtCore.QRect(40, 30, 336, 19))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.inv_cb = QtGui.QCheckBox(self.widget)
        self.inv_cb.setObjectName(_fromUtf8("inv_cb"))
        self.horizontalLayout.addWidget(self.inv_cb)
        self.attr_X_rb = QtGui.QRadioButton(self.widget)
        self.attr_X_rb.setObjectName(_fromUtf8("attr_X_rb"))
        self.horizontalLayout.addWidget(self.attr_X_rb)
        self.attr_Y_rb = QtGui.QRadioButton(self.widget)
        self.attr_Y_rb.setObjectName(_fromUtf8("attr_Y_rb"))
        self.horizontalLayout.addWidget(self.attr_Y_rb)
        self.attr_Z_rb = QtGui.QRadioButton(self.widget)
        self.attr_Z_rb.setObjectName(_fromUtf8("attr_Z_rb"))
        self.horizontalLayout.addWidget(self.attr_Z_rb)
        self.src_objs_pb = QtGui.QPushButton(self.centralwidget)
        self.src_objs_pb.setGeometry(QtCore.QRect(40, 40, 291, 23))
        self.src_objs_pb.setObjectName(_fromUtf8("src_objs_pb"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.show()
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.drvn_obj_info_gbx.setTitle(_translate("MainWindow", "GroupBox", None))
        self.inv_cb.setText(_translate("MainWindow", "inverse", None))
        self.attr_X_rb.setText(_translate("MainWindow", "attr_rb", None))
        self.attr_Y_rb.setText(_translate("MainWindow", "attr_rb", None))
        self.attr_Z_rb.setText(_translate("MainWindow", "RadioButton", None))
        self.src_objs_pb.setText(_translate("MainWindow", "selecte source set driven key objects", None))


# def mywindow():
#     mywindow = Ui_MainWindow()
#     mywindow().show
#     return mywindow
# # def main():
# #     app = QtGui.QApplication(sys.argv)
# #     window = Ui_MainWindow()
# #     window.show()
# #     sys.exit(app.exec_())
#
# if __name__ == '__main__':
#     app = QtGui.QApplication(sys.argv)
#     myobj = mywindow()
#     sys.exit(app.exec_())

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())