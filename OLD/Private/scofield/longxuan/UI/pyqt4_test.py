__author__ = 'liangyu'

import sip
sip.setapi('QString', 2)
sip.setapi('QVariant', 2)

import sys
import time
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import urllib2


class MyTable(QMainWindow):
    def __init__(self,parent=None):
        QMainWindow.__init__(self)


        self.setWindowTitle("Scofield Console")
        self.setGeometry(100,200,700,370)

        exit = QAction(QIcon('icons/web.png'), 'Exit', self)
        exit.setShortcut('Ctrl+Q')
        exit.setStatusTip('Exit application')
        self.connect(exit, SIGNAL('triggered()'), SLOT('close()'))
        menubar = self.menuBar()
        Add = menubar.addMenu('&File')
        Add.addAction(exit)
        Help=menubar.addMenu("&Help")
        Help.addAction(exit)

        self.label = QLabel()
        self.label.setMaximumHeight(90)
        self.label.setText("")
        self.label.setPixmap(QPixmap("F:/Development/myProj/OLD/idmt/maya/norch/QT/icon/w.jpg"))
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label.setTextInteractionFlags(Qt.LinksAccessibleByMouse)
        self.label.setObjectName("label")

        self.centralwidget = QWidget(self)
        self.toobar=QToolBar()
        self.toolbutton01=QToolButton(self.centralwidget)
        self.toolbutton02=QToolButton(self.centralwidget)
        self.toolbutton03=QToolButton(self.centralwidget)
        self.toolbutton04=QToolButton(self.centralwidget)
        self.toolbutton01.setText(" Add Task ")
        self.toolbutton04.setText("Clear Task")
        self.toolbutton02.setText(" Run ")
        self.toolbutton03.setText(" Stop ")
        self.toobar.addWidget(self.toolbutton01)
        self.toobar.addWidget(self.toolbutton04)
        self.toobar.addWidget(self.toolbutton02)
        self.toobar.addWidget(self.toolbutton03)

        self.testtable = LYtable(200,6)
        xxx = QWidget(self)
        self.setCentralWidget(xxx)
        Layout=QHBoxLayout(xxx)
        Vlayout=QVBoxLayout()
        Vlayout.addWidget(self.label)
        Vlayout.addWidget(self.toobar)
        # Vlayout.addLayout(toobarLayoou)
        Vlayout.addWidget(self.testtable)
        Layout.addLayout(Vlayout)

        self.toolbutton01.clicked.connect(self.testtable.AddEvent)
        self.toolbutton02.clicked.connect(self.testtable.RunEvent)
        self.toolbutton03.clicked.connect(self.testtable.StopEvent)
        self.toolbutton04.clicked.connect(self.my_clearContents)

        self.testtable.createContextMenu()

    def my_clearContents(self):
        self.testtable.clearContents()
        self.testtable.datas = []


class LYtable(QTableWidget):
    changed = pyqtSignal(QMimeData)
    datas = []


    def __init__(self, *args, **kwargs):
        super(LYtable,self).__init__(*args, **kwargs)


        self.setAcceptDrops(True)
        # mytable=QTableWidget(15,6)
        self.setHorizontalHeaderLabels(['State','Job','Operation','Start time','End time',''])
        self.verticalHeader().setVisible(False)
        self.setEditTriggers(QTableWidget.NoEditTriggers)
        # self.setSelectionMode(QTableWidget.NoSelection)
        self.setSelectionBehavior(QTableWidget.SelectRows)
        self.setStyleSheet("QHeaderView::section{background:#d9d8d2;}")
        self.setStyleSheet("gridline-color: rgb(220, 210, 210)")
        self.setColumnWidth(0, 60)
        self.setColumnWidth(1, 300)
        self.setColumnWidth(2, 170)
        self.setColumnWidth(3, 110)
        self.setColumnWidth(4, 110)
        self.verticalHeader().setDefaultSectionSize(18)



    def my_updata(self):
        self.clearContents()
        self.my_set_text()

    def AddEvent(self, column=0, row=0, text=""):
        # fileName = QFileDialog.getOpenFileName(self,'choose the file',options = QFileDialog.DontUseNativeDialog)
        filename = QFileDialog.getOpenFileName(self, 'Open file', './')
        file=filename.split('/')[-1]
        self.datas.append(file)
        self.my_set_text()

    def StopEvent(self,column=0, row=0, text=""):
        for i in range(len(self.datas)):
            TtemStratTime=QTableWidgetItem(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
            self.setItem(i,4,TtemStratTime)
            ItemState=QTableWidgetItem('Stop')
            self.setItem(i,0,ItemState)

        print(self.item(0,3).text())

    def my_set_text(self, column=0, row=0, text=""):
        for i in range(len(self.datas)):
            widget = QLabel(self.datas[i])
            self.setCellWidget(i, 1, widget)
            if self.datas[i] != "":
                ItemState=QTableWidgetItem('Ready')
                TtemOperation=QTableWidgetItem('batch')
                self.setItem(i,0,ItemState)
                self.setItem(i,2,TtemOperation)

    def dropEvent(self, event):
        mimeData = event.mimeData()
        if mimeData.hasImage():
            self.setPixmap(QPixmap(mimeData.imageData()))
        elif mimeData.hasHtml():
            self.setText(mimeData.html())
            self.setTextFormat(Qt.RichText)
        elif mimeData.hasText():
            self.setText(mimeData.text())
            self.setTextFormat(Qt.PlainText)
        elif mimeData.hasUrls():
            paths = [url.path().split('/')[-1] for url in mimeData.urls()]
            for path in paths:
                self.datas.append(path)
            self.my_set_text()
        else:
            self.setText("Cannot display data")

        self.setBackgroundRole(QPalette.Dark)
        event.acceptProposedAction()

    def dragEnterEvent(self, event):
        event.acceptProposedAction()
        self.changed.emit(event.mimeData())

    def dragMoveEvent(self, event):
        event.acceptProposedAction()

    def dragLeaveEvent(self, event):
        self.clear()
        event.accept()

    def clear(self):
        self.changed.emit(None)

    def createContextMenu(self):
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.showContextMenu)
        self.contextMenu = QMenu(self)
        self.actionA = self.contextMenu.addAction('Run[Selection]')
        self.actionB = self.contextMenu.addAction('Delete[Selection]')
        self.actionC = self.contextMenu.addAction('Stop[Selection]')
        # self.contextMenu.exec_(QCursor.pos())
        self.actionA.triggered.connect(self.actionHandler)
        self.actionB.triggered.connect(self.actionHandler)
        self.actionB.triggered.connect(self.actionHandler)

    def showContextMenu(self):
        # self.contextMenu.move(self.pos() + pos)
        self.contextMenu.move(QCursor.pos())
        self.contextMenu.show()


    # def actionHandler(self):
    #     # items=self.selectedRanges()
    #     # num=items.count()
    #     # print num
    #     pop_list = []
    #     for item in self.selectedItems():
    #         pop_list.append(item.row())
    #     pop_list.sort()
    #     pop_list = list(set(pop_list))
    #     pop_list.reverse()
    #     #print pop_list
    #
    #     for i in pop_list:
    #         self.datas.pop(i)
    #     #for i in range(0,2):
    #     #    index=self.currentIndex()
    #     #    row=index.row()
    #     #   self.datas.pop(row)
    #     print self.datas
    #     print 99999990000000000000
    #     self.my_updata()

    def actionHandler(self):
        pop_list = []
        for item in self.selectedItems():
            pop_list.append(item.row())
        pop_list.sort()
        pop_list = list(set(pop_list))
        pop_list.reverse()

        for i in pop_list:
            self.datas.pop(i)
            self.removeRow(i)
            self.insertRow(199-i)

        # print(self.rowCount())


    def RunEvent(self,column=0, row=0, text=""):
        self.td = []
        # self.my_thread0 = MyWorkerThread(eval("self"), 0)
        # self.my_thread1 = MyWorkerThread(eval("self"), 1)
        for i in range(len(self.datas)):
            my_thread = MyWorkerThread(eval("self"), i)
            self.td.append(my_thread)

        for i in range(len(self.td)-1):
            self.td[i].finished.connect(self.td[i+1].start)

        if self.td:
            self.td[0].start()



class MyWorkerThread(QThread):
    def __init__(self, ctrl, id, parent=None):
        QThread.__init__(self)
        self.ctrl = ctrl
        self.id = id

    def __del__(self):
        self.wait()

    def run(self):
        TtemStratTime=QTableWidgetItem(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        self.ctrl.setItem(self.id, 3, TtemStratTime)
        ItemState=QTableWidgetItem('Start')
        self.ctrl.setItem(self.id,0,ItemState)

        time.sleep(3)

        TtemEndTime=QTableWidgetItem(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        self.ctrl.setItem(self.id, 4, TtemEndTime)
        ItemState=QTableWidgetItem('End')
        self.ctrl.setItem(self.id, 0, ItemState)




app=QApplication(sys.argv)
mainWindow=MyTable()
mainWindow.show()
sys.exit(app.exec_())


