# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import unicode_literals
from future_builtins import *


import platform
from PySide.QtCore import *
from PySide.QtGui import *
NAME ,VIS,  SPEED , LENGTH = range(4)

class PlutoGunShip(object):
    def __init__(self, name, vis, speed, length):
        self.name = name
        self.vis = vis
        self.speed = speed
        self.length = length








class ShipTableModel(QAbstractTableModel):             #       数据模型
    def __init__(self, tableView = ""):
        super(ShipTableModel, self).__init__()
        self.ccc = "ares"
        self.ships = []
        # self.ships = [PlutoGunShip("aaa",1,7,3)]
        # self.ships.append(PlutoGunShip("bbb",0,5,2))
        self.tableView = tableView


    def flags(self, index):                                                                       #    设置数据是否可编辑，选择，拖拽，翻译                                                         
        column = index.column()
        if not index.isValid():
            return Qt.ItemIsEnabled
        elif column == NAME:                                        #   Name是不能修改的
            return Qt.ItemFlags(
                    QAbstractTableModel.flags(self, index)
                    )
        elif column == VIS:
            return Qt.ItemFlags(
                    QAbstractTableModel.flags(self, index)|
                    Qt.ItemIsEditable
                    )                              
        return Qt.ItemFlags(
                QAbstractTableModel.flags(self, index)|
                Qt.ItemIsEditable)                    

    def data(self, index, role=Qt.DisplayRole):              #   数据的具体格式：对齐，显示，内容，范围等等。。。
        if not index.isValid() or not (0 <= index.row() < len(self.ships)):
            return ""
        ship = self.ships[index.row()]
        
        column = index.column()
        if role == Qt.DisplayRole:                                                                 #    DisplayRole
            if column == 0:
                return ship.name
            elif column == 1:
                return ship.vis
            elif column == 2:
                return ship.speed
            elif column == 3:
                return ship.length

        elif role == Qt.TextAlignmentRole:                                                  #    TextAlignmentRole
            if column == VIS:
                return Qt.AlignCenter
            if column == SPEED:
                return Qt.AlignCenter
            return Qt.AlignCenter

        elif role == Qt.TextColorRole:                                                           #    TextColorRole
            if column == VIS:
                if ship.vis == 1:
                    return QColor(Qt.green)
                else:
                    return QColor(Qt.red)
            elif column == NAME:
                if 'green' in ship.name:
                    return QColor(Qt.green)
                elif 'blue' in ship.name:
                    return QColor(Qt.blue)
                else:
                    return QColor(Qt.red)
            elif column == SPEED:
                if ship.speed < 3:
                    return QColor(Qt.lightGray)
                elif ship.speed < 5:
                    return QColor(Qt.yellow)
                elif ship.speed < 8:
                    return QColor(Qt.green)
                else:
                    return QColor(Qt.red)
        elif role == Qt.BackgroundColorRole:
            return ""


    def headerData(self, section, orientation, role=Qt.DisplayRole):            #   标题的数据设置
        if role == Qt.TextAlignmentRole:                                                        #    TextAlignmentRole
            return int(Qt.AlignHCenter|Qt.AlignVCenter)

        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            if section == 0:
                return "Name"
            elif section == 1:
                return "Vis"
            elif section == 2:
                return "Speed"
            elif section == 3:
                return "Length"
            # return self.header_labels[section]
        return QAbstractTableModel.headerData(self, section, orientation, role)

    def rowCount(self, index=QModelIndex()):                                          #   设置有多少行
        return len(self.ships)

    def columnCount(self, index=QModelIndex()):                                     #   设置有多少列
        return 4
        
    def removeRows(self, position, rows=1, index=QModelIndex()):          #   书上说必须得要抄这段，否则removeRow没效果
        self.beginRemoveRows(QModelIndex(), position,
        position + rows - 1)
        self.ships = self.ships[:position] + \
        self.ships[position + rows:]
        self.endRemoveRows()
        self.dirty = True
        return True



    def setData(self, index, value, role=Qt.EditRole):                                  #   修改数据时的动作
        if index.isValid() and 0 <= index.row() < len(self.ships):
            ship = self.ships[index.row()]
            column = index.column()

            if column == VIS:
                ship.vis = value

            elif column == SPEED:
                if value>0:
                    ship.speed = value

            elif column == LENGTH:
                if value>0:
                    ship.length = value
            self.dataChanged.emit(index, index)
            return True
        return False





class ShipDelegate(QStyledItemDelegate):                #       控制器
    def __init__(self,   parent=None):
        super(ShipDelegate, self).__init__(parent)

    def createEditor(self, parent, option, index):
        if index.column() == VIS:
            spinBox = QSpinBox(parent)
            spinBox.setRange(0, 1)
            spinBox.setSingleStep(1)
            spinBox.setAlignment(Qt.AlignRight|Qt.AlignVCenter)
            return spinBox

        elif index.column() == SPEED:
            ctrl = QSpinBox(parent)
            return ctrl

        elif index.column() == LENGTH:
            ctrl2 = QDoubleSpinBox(parent)
            return ctrl2

        else:
            return QStyledItemDelegate.createEditor(self, parent, option,
                                                    index)


#----------------------------------------双击的时候的数据--------------------------------------------
    def setEditorData(self, editor, index):
        text = index.model().data(index, Qt.DisplayRole)

        if index.column() == SPEED:
            editor.setValue(int(text))
        elif index.column() == LENGTH:
            editor.setValue(float(text))
        elif index.column() == VIS:
            editor.setValue(int(text))
        else:
            QStyledItemDelegate.setEditorData(self, editor, index)

#----------------------------------------输入的数据进行处理--------------------------------------------
    def setModelData(self, editor, model, index):
        value = editor.value()
        indexes = index.model().tableView.selectedIndexes()
        list = []

        for indexSel in indexes:
            if indexSel.column() == SPEED:
                list.append(indexSel)
            elif indexSel.column() == LENGTH:
                list.append(indexSel)
            elif indexSel.column() == VIS and value<=1:
                list.append(indexSel)

        for i in list:
            model.setData(i, value)

