# -*- coding: utf-8 -*-
from PySide.QtCore import *
from PySide.QtGui import *

import My_TableModel;reload(My_TableModel)
NAME ,VIS,  SPEED , LENGTH = range(4)


class My_TableView(QTableView):  # 自定义的tableView
    def __init__(self, parent=None):
        super(My_TableView, self).__init__(parent)

        self.model = My_TableModel.ShipTableModel(self)
        self.setModel(self.model)
        self.setItemDelegate(My_TableModel.ShipDelegate(self))

        self.horizontalHeader().setResizeMode(0, QHeaderView.Stretch)
        self.horizontalHeader().resizeSection(1, 35)
        self.horizontalHeader().resizeSection(2, 50)
        self.horizontalHeader().resizeSection(3, 50)

    def keyPressEvent(self, event):  # 键盘事件
        super(My_TableView, self).keyPressEvent(event)
        if event.key() == Qt.Key_Delete:
            list = []
            for indexSel in self.selectedIndexes():
                if indexSel.column() == NAME:
                    list.append(indexSel.row())
            list.sort()
            list.reverse()
            for row in list:
                self.model.removeRow(row)
            # event.accept()
        else:
            event.ignore()
        # else:
        #     super(My_TableView, self).keyPressEvent(event)



    def mouseReleaseEvent(self, QMouseEvent):
        super(My_TableView, self).mouseReleaseEvent(QMouseEvent)
        self.window().Z_selectOBJ()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    PlutoGW = My_TableView()
    PlutoGW.show()
    sys.exit(app.exec_())