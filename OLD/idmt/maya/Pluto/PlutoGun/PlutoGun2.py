# -*- coding: utf-8 -*-

import sip,sys
sip.setapi('QString', 2)
sip.setapi('QVariant', 2)

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class PlutoGunShip(object):

    def __init__(self, name, vis, speed, length):
        self.name = name
        self.vis = vis


class PlutoGunTable(QTableView):  # 自定义的tableView
    def __init__(self, PGW):
        super(PlutoGunTable, self).__init__()
        self.msw = PGW
        
        self.clicked.connect(self.aaa)
    
    def aaa(self):
        print self.selectedIndexes()


class ShipTableModel(QAbstractTableModel):     
    def __init__(self ):
        super(ShipTableModel, self).__init__()
        self.ships = []
        self.tableView = None
    def data(self, index, role=Qt.DisplayRole):    
        ship = self.ships[index.row()]
        
        column = index.column()
        if role == Qt.DisplayRole:                 
            if column == 0:
                return ship.name
            elif column == 1:
                return ship.vis
            
    def rowCount(self, index=QModelIndex()):   
        return len(self.ships)
    def columnCount(self, index=QModelIndex()):           
        return 2

class PlutoGunWindow(QMainWindow):  # PlutoGunWindow窗口

    def __init__(self, parent=None):
        super(PlutoGunWindow, self).__init__(parent)
        self.resize(850, 600)
        
        self.tableView = PlutoGunTable(self)

        self.model = ShipTableModel()
        self.model.tableView = self.tableView

        self.tableView.setModel(self.model)

        self.setCentralWidget(self.tableView)

        ship = PlutoGunShip('name', 0, 1, 2)
        self.model.ships.append(ship)
        self.model.reset()



def main():
    PlutoGW = PlutoGunWindow()
    PlutoGW.show()
    
# app = QApplication(sys.argv)
# main()
# sys.exit(app.exec_())

