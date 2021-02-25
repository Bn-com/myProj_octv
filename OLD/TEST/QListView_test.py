from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

list=QListView()
list.setWindowTitle('Example List')
list.setMinimumSize(300,100)

model=QStandardItemModel(list)

foods=['Cookie dough','Hummus','Spaghetti','Dal makhani','Chocolate whipped cream']

for food in foods:
    item=QStandardItem(food)

    item.setCheckable(True)

    model.appendRow(item)


def on_item_changed():
    if not item.checkState():
        return
    i=0
    while model.item(i):
        if not model.item(i).checkState():
            return
        i+=1

model.itemChanged.connect(on_item_changed)
list.setModel(model)
list.show()
