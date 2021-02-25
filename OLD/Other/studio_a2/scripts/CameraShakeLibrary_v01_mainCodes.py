#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''    
__author__ = 'zhangben'
__mtime__ = '2016/4/12'
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
'''


# -*- coding: utf-8 -*-
# from pymel.core import *
# import maya.cmds as mc
import sys

from PyQt4.QtGui import *
# from idmt.maya.py_common import sk_referenceConfig;reload(sk_referenceConfig)
# from idmt.maya.py_common import sk_infoConfig;reload(sk_infoConfig)
import ui_CameraShakeLibrary_MW;reload(ui_CameraShakeLibrary_MW)

class QT_MainUI(QMainWindow):
    def __init__(self, parent=None):
        super(QT_MainUI, self).__init__(parent)
        self.ui = ui_CameraShakeLibrary_MW.Ui_MainWindow()
        self.ui.setupUi(self)

        # Connection
        # self.myuis.f_cb.clicked.connect(self.xxx)
        # self.myuis.QPB_OK.clicked.connect(self.xxx)


def main():
    app = QApplication(sys.argv)
    window = QT_MainUI()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()