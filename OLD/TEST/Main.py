# -*- coding: utf-8 -*-
import sip
sip.setapi('QString', 2)
sip.setapi('QVariant', 2)
import sys

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import UI_Main  # 界面.ui转py的文件

class MainUI(QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()
        self.ui = UI_Main.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.xxx)



    def xxx(self):
        text1 = self.ui.radioButton.text()
        text2 = self.ui.radioButton_2.text()
        if self.ui.radioButton.isChecked():
            self.ui.label.setText(text1)
        else:
            self.ui.label.setText(text2)





if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = MainUI()
    window.show()
    sys.exit(app.exec_())
