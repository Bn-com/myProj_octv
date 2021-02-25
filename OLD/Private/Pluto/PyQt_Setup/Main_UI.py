# -*- coding: utf-8 -*-
import sip
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import UI_Main as UI_Main;reload(UI_Main)

class DesignerUI(QMainWindow):
    """这个是给 Qt Designer 设计界面用的，在 Python 模式下调试的"""
    def __init__(self, parent=None):
        super(DesignerUI, self).__init__(parent)
        self.ui = UI_Main.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.splitter = QSplitter(self.ui.centralwidget)
        # self.myuis.splitter.setFrameShape(QFrame.Panel)
        # self.myuis.splitter.setFrameShadow(QFrame.Raised)
        self.ui.centralLayout.addWidget(self.ui.splitter)
        self.ui.splitterLayout = QHBoxLayout(self.ui.splitter)
        self.ui.splitter.addWidget(self.ui.frame_left)
        self.ui.splitter.addWidget(self.ui.frame_right)
        self.ui.splitter.setSizes([500, 300])
        self.ui.splitter.setHandleWidth(3)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DesignerUI()
    window.show()
    sys.exit(app.exec_())