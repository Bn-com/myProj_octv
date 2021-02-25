# -*- coding: utf-8 -*-
from __future__ import division
#from __future__ import print_function
from __future__ import unicode_literals
from future_builtins import *

from PlutoGun_Slider import Slider

import platform
from PyQt4.QtCore import *
from PyQt4.QtGui import *
NAME ,VIS,  SPEED = range(3)






class ShipTableModel(QAbstractTableModel):             #       数据模型
    def __init__(self ):
        super(ShipTableModel, self).__init__()
        self.ships = []
        self.tableView = None


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

    def data(self, index, role=Qt.DisplayRole):                                          #   数据的具体格式：对齐，显示，内容，范围等等。。。
        if (not index.isValid() or
            not (0 <= index.row() < len(self.ships))):
            return QVariant()
        ship = self.ships[index.row()]
        
        column = index.column()
        if role == Qt.DisplayRole:
            if column == NAME:
                return QVariant(ship.name)
            elif column == VIS:
                return QVariant(ship.vis)
            elif column == SPEED:
                return QVariant(QString("%L1").arg(ship.speed))
        elif role == Qt.TextAlignmentRole:
            if column == VIS:
                return QVariant(int(Qt.AlignCenter))
            if column == SPEED:
                return QVariant(int(Qt.AlignRight|Qt.AlignVCenter))
            return QVariant(int(Qt.AlignLeft|Qt.AlignVCenter))
        elif role == Qt.TextColorRole and column == VIS:
            if ship.vis == '1':
                return QVariant(QColor(Qt.green))
            else:
                return QVariant(QColor(Qt.red))
        elif role == Qt.TextColorRole and column == SPEED:
            if ship.speed < 3:
                return QVariant(QColor(Qt.lightGray))
            elif ship.speed < 5:
                return QVariant(QColor(Qt.yellow))
            elif ship.speed < 8:
                return QVariant(QColor(Qt.green))
            else:
                return QVariant(QColor(Qt.red))
        elif role == Qt.BackgroundColorRole:
            QVariant()


    def headerData(self, section, orientation, role=Qt.DisplayRole):            #   标题的数据设置
        if role == Qt.TextAlignmentRole:
            if orientation == Qt.Horizontal:
                return QVariant(int(Qt.AlignLeft|Qt.AlignVCenter))
            return QVariant(int(Qt.AlignRight|Qt.AlignVCenter))
        if role != Qt.DisplayRole:
            return QVariant()
        if orientation == Qt.Horizontal:
            if section == NAME:
                return QVariant("Name")
            elif section == VIS:
                return QVariant("Vis")
            elif section == SPEED:
                return QVariant("Speed")
        return QVariant(int(section + 1))


    def rowCount(self, index=QModelIndex()):                                          #   设置有多少行  
        return len(self.ships)


    def columnCount(self, index=QModelIndex()):                                     #   设置有多少列
        return 3
        

    def removeRows(self, position, rows=1, index=QModelIndex()):            #   书上说必须得要抄这段，否则removeRow没效果
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
            if column == NAME:
                ship.name = value.toString()
            elif column == VIS:
                ship.vis = value.toString()
            elif column == SPEED:
                value, ok = value.toFloat()
                if ok:
                    ship.speed = value
            self.emit(SIGNAL("dataChanged(QModelIndex,QModelIndex)"),index, index)
            return True
        return False


class ShipDelegate(QStyledItemDelegate):                #       控制器
    def __init__(self,   parent=None):
        super(ShipDelegate, self).__init__(parent)
#        self.msw = parent
        
    def createEditor(self, parent, option, index):
        if index.column() == SPEED:
            ctrl = QSpinBox(parent)
#            ctrl = Slider(Qt.Horizontal, parent)
#            ctrl = QLineEdit( parent)
#            ctrl.setRange(0.1, 10)
#            ctrl.setSingleStep(0.1)
#            ctrl.setDecimals(3)
#            ctrl.setAlignment(Qt.AlignRight|Qt.AlignVCenter)
            return ctrl
            
        elif index.column() == NAME:
            editor = QLineEdit(parent)
            return editor
            
        elif index.column() == VIS:
            spinBox = QSpinBox(parent)
            spinBox.setRange(0, 1)
            spinBox.setSingleStep(1)
            spinBox.setAlignment(Qt.AlignRight|Qt.AlignVCenter)
            return spinBox
        else:
            return QStyledItemDelegate.createEditor(self, parent, option,
                                                    index)


#----------------------------------------双击的时候的数据--------------------------------------------
    def setEditorData(self, editor, index):
#        停止计时器工作
#        self.msw.timer.stop()
        text = index.model().data(index, Qt.DisplayRole).toString()
        if index.column() == SPEED:
            editor.setValue(text.toFloat()[0])            
        elif index.column() == VIS:
            editor.setValue(text.toInt()[0])            
        elif index.column() == NAME:
            editor.setText(text)
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
            elif indexSel.column() == VIS and value<=1:
                list.append(indexSel)
                

        for i in list:
            model.setData(i, QVariant(value))        

#        计时器继续工作
#        self.msw.timer.start( 1000 )



