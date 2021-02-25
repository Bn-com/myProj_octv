from PyQt4.QtGui import *
from PyQt4.QtCore import *
class MyButton(QPushButton):
    def __init__(self,parent=None):
        super(MyButton, self).__init__(parent)

    def keyPressEvent(self,event):
        print event.key()

    def mousePressEvent(self, *args, **kwargs):
        print event.key()