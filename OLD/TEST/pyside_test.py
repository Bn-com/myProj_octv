import sys
from PySide2.QtCore import *
from PySide2.QtWidgets import *

class LayoutExample(QWidget):

    def __init__(self):
        QWidget.__ini__(self)

        self.setWindowTitel('Dynamic Greeter')
        self.setMinimumSize(600,400)

        sefl.layout=QVBoxLayout()

        self.form_layout=QFormLayout()

        self.sals=['Ahoy','Good day','Hello','Heyo','Hi','Salutations','Wassup','Yo']

        self.sal=QComboBox(self)
        self.sal.addItems(self.sals)

        self.form_layout.addRow('&Salutation:',self.sal)

        self.recipient =QLineEdit(self)
        self.recipient.setPlaceholderText("e.g. 'world' or 'Matey'")
        self.form_layout.addRow(self.recipient)

        self.layout.addLayout(self.form_layout)

        self.setLayout(sefl.layout)


    def run(self):
        self.show()

app=LayoutExample()
app.run()

