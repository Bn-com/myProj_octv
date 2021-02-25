# -*- coding: utf-8 -*-

# Form implementation generated from reading myuis file 'm:\sync_kp\script\pyqt_study\a2_work_proj\cam_shk_lib_oneButton.myuis'
#
# Created: Tue Jun 20 14:47:24 2017
#      by: PyQt4 UI code generator 4.10
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
        MainWindow.resize(280, 180)
        MainWindow.setMinimumSize(QtCore.QSize(279, 179))
        MainWindow.setMaximumSize(QtCore.QSize(280, 180))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(260, 135))
        self.frame.setMaximumSize(QtCore.QSize(265, 140))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.widget = QtGui.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(10, 10, 241, 111))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.im_bt1 = QtGui.QPushButton(self.widget)
        self.im_bt1.setObjectName(_fromUtf8("im_bt1"))
        self.horizontalLayout_2.addWidget(self.im_bt1)
        self.plainTextEdit = QtGui.QPlainTextEdit(self.widget)
        self.plainTextEdit.setToolTip(_fromUtf8(""))
        self.plainTextEdit.setOverwriteMode(False)
        self.plainTextEdit.setCenterOnScroll(True)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.horizontalLayout_2.addWidget(self.plainTextEdit)
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 280, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Camera Shake Library TestButton", None))
        self.im_bt1.setText(_translate("MainWindow", "import cam data", None))
        self.plainTextEdit.setStatusTip(_translate("MainWindow", "description", None))
        self.plainTextEdit.setDocumentTitle(_translate("MainWindow", "desciption", None))

def main():
    app = QApplication(sys.argv)
    window = QT_MainUI()
    window.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()