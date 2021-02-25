from PySide2.QtCore import *
from PySide2.QtQuickWidgets import *

win=QWidget()
win.setWindowTitle('Test Window')

btn=QPushButton('Test',win)

@Slot()

def on_click():
    print('clicked')

@Slot()

def on_press():
    print('pressed')

@Slot()

def on_release():
    print('released')

btn.clicked.connect(on_click)
btn.press.connect(on_press)
btn.release.connect(on_release)

win.show()