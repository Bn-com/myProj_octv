#-*- coding: gbk -*-
'''
Created on 2013-8-20
@contact:    power_zzj@163.com
@deffield    updated: Updated
@author: zhaozhongjie
usage:
    import idmt.maya.Pluto.Maya.Rnd.ImageSwitchPath as isp
    reload(isp)
    isp.main()
'''

import os,sys

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.uic import loadUi
import sip


class ImageSwitchPath(QMainWindow):
    '''
    classdocs
    '''
    FILE =''
    try:
        FILE = __file__
    except:
        FILE = r'\\file-cluster\GDC\Resource\Support\Python\2.6-x64\Lib\site-packages\idmt\maya\Pluto\Maya\Rnd\ImageSwitchPath\ImageSwitchPath2.py'
    UI = os.path.splitext(FILE)[0] + '.myuis'

    def __init__(self,parent =None):
        '''
        Constructor
        '''
        super(ImageSwitchPath, self).__init__(parent)
        self.setWindowTitle("ImageSwitchPath")
        self.setObjectName("ImageSwitchPath")
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.resize(800, 600)
        
        self.win = loadUi(self.UI,QMainWindow()) 
        self.setCentralWidget(self.win) 

        self.my_array = [
            MyNode('aaa|000:abccccccccccccccccccccccccc','10KB'),
            MyNode('bbb','10KB'),
            MyNode('bbb|111:def','10KB'),
            MyNode('bbb|111:def','10KB'),
            MyNode('bbb|111:def','10KB'),
            MyNode('bbb|111:def','10KB'),
            MyNode('bbb|111:def','10KB'),
            MyNode('ccc|222:ghi','10KB')
            ]
        
        
        self.tablemodel = MyModel(self.my_array  )
        self.win.listView.setModel(self.tablemodel)
        self.win.tableView.setModel(self.tablemodel)
        self.MyIconSize()
        

#    CONNECTIONS
        self.win.checkBox_showNameSpace.clicked.connect(self.MyCMD_Menu_NameSpace)
        self.win.bigIcon.toggled.connect(self.MyIconSize)
        self.win.midIcon.toggled.connect(self.MyIconSize)
        self.win.displayIcon.toggled.connect(self.MyIconSize)
        self.win.gridLength.valueChanged.connect(self.MyIconSize)
        
#         self.win.All_ToNet.clicked.connect(lambda: self.MyCMD_Button_Switch_L_N('AN'))
#         self.win.All_ToLocal.clicked.connect(lambda: self.MyCMD_Button_Switch_L_N('AL'))
#         self.win.Select_ToNet.clicked.connect(lambda: self.MyCMD_Button_Switch_L_N('SN'))
#         self.win.Select_ToLocal.clicked.connect(lambda: self.MyCMD_Button_Switch_L_N('SL'))
#         self.win.test.clicked.connect(self.test)
        
    def MyIconSize(self):                                   #    更新图标大小
        __size = 20
        __gridSize = 20               
        __gridLength = self.win.gridLength.value()
        self.tablemodel.gridSize[0] = __gridLength
                                        
        if not self.win.displayIcon.isChecked():
            __size , __gridSize= 0 , 20
            
        elif self.win.smallIcon.isChecked():
            __size , __gridSize = 20 , 20                        
        elif self.win.midIcon.isChecked():
            __size , __gridSize = 40 , 40            
        elif self.win.bigIcon.isChecked():
            __size , __gridSize = 80 , 80
        else:
            __size , __gridSize = 20 , 20
        
        self.win.listView.setIconSize(QSize(__gridSize,__gridSize))
        self.win.tableView.setIconSize(QSize(__gridSize,__gridSize))
        self.tablemodel.iconSize = __size
        
        
        for i in range(self.tablemodel.rowCount(self)):                                     #    设置Table的高度
            if __size ==0:
                __size = 20
            self.win.tableView.setRowHeight(i,__size)
#         self.win.tableView.setColumnWidth(0,300)                                          #    设置Table的宽度
#         self.win.tableView.setColumnWidth(1,100)                                          #    设置Table的宽度
#         self.win.tableView.horizontalHeader().setStretchLastSection(0)
        self.win.tableView.horizontalHeader().setResizeMode(0, QHeaderView.Stretch)
        
#         self.win.tableView.horizontalHeader().resizeSection(0, 300)
#         self.win.tableView.horizontalHeader().resizeSection(1, 80)
                
        self.tablemodel.reset()                                                                             #    刷新数据
        
    def test(self):
#         self.tablemodel.iconSize = 80
        self.tablemodel._nodes[1]._ifonline = 0
        self.tablemodel._nodes[1]._long = 'dfdf' 
        
        index = self.tablemodel.index(1,1)
        self.tablemodel.dataChanged.emit(index,index)
        
        
    def MyCMD_Menu_NameSpace(self):
        checked = self.win.checkBox_showNameSpace.isChecked()
        self.win.listView.model()._showNameSpace = checked
        self.win.listView.model().reset()
    def MyCMD_Button_Switch_L_N(self, place ):
        selected = self.win.listView.selectedIndexes()
        for s in selected:
            
            print s.data().toString()
            
            print s.model()._nodes[s.row()]



#===================================================================
#     Node
#===================================================================
class MyNode():
    _full = ''              #    'aaa|000:abccccccccccccccccccccccccc'
    _long = ''            #    '000:abccccccccccccccccccccccccc'
    _short = ''           #    'abccccccccccccccccccccccccc'
    _ifonline = 1
    _info = ''

    
    def __init__(self,name,info):
        self.MyInitVar(name,info)

    def MyInitVar(self,name,info = ''):                   #    初始化MyNode的数据
        self._full = name
        self._long = self._full.split('|')[-1]
        self._short = self._long.split(':')[-1]
        if len(info)>1:        self._info = info                       #    设置其他信息
        self.MyIfOnline()
        
    def MyIfOnline(self):                       #    判断是否路径在网上的函数
        if self._short[-1] in 'ci':
            self._ifonline = 0
        else:
            self._ifonline = 1        
                        
    def MyShortToFull(self, S=''):          #    从短名变成全名
        __short = S.split(':')[-1]
        __pre =self._full[ :-len(self._short)]
        __full = __pre + __short
        self.MyIfOnline()
        return __full

    def MyLongToFull(self, L=''):           #    从长名变成全名
        __long = self._full.split('|')[-1]
        __pre =self._full[ :-len(__long)]
        __full = __pre + L
        self.MyIfOnline()
        return __full    
    
    
#===================================================================
#     Model
#===================================================================
class MyModel(QAbstractTableModel):
    def __init__(self, datas = [] , iconSize = 80 ):
        super(MyModel, self).__init__()
        self._nodes = datas   
        self._showNameSpace = 1
        self.iconSize = 40
        self.gridSize = [ 200 , 40 ]
    
    def data(self,index,role = Qt.DisplayRole):
        __row = index.row()
        __txt = self._nodes[__row]._long                            #    显示的文字，默认用长名显示而不是用全名显示
        __info = self._nodes[__row]._info                          #    第二列显示扩展信息，比如贴图大小
        __ifonline = self._nodes[__row]._ifonline              #    是否在网上
        
        __iconSize = self.iconSize
        if self.iconSize == 0:
            self.gridSize[1] = 20
        else :
            self.gridSize[1] = self.iconSize
            
        if not self._showNameSpace :                                #    是否显示namespace，如果不显示，则用短名显示
            __txt = self._nodes[__row]._short
        column = index.column()
        if role == Qt.EditRole:                                            #    双击修改的时候，先保持之前的数值
            return __txt
        elif role == Qt.ToolTipRole:                                      #    消息提示
            return "Name:    " + __txt
        elif role == Qt.SizeHintRole:                                     #    单元格大小
            return QSize(self.gridSize[0] , self.gridSize[1])
        elif role == Qt.ForegroundRole:                              #    字体颜色
            if __ifonline:
                return QBrush(Qt.red)  
            else :
                return QBrush(Qt.black)  
        elif role == Qt.DecorationRole:                               #    图标
            if column == 0:
                color_red = QColor('#ff0000')
                color_green = QColor('#00ff00')
                pixmap = QPixmap( __iconSize ,__iconSize)
                if __ifonline:
                    pixmap.fill(color_red)
                else :
                    pixmap.fill(color_green)
                icon = QIcon(pixmap)
                return icon
            else:
                return
        elif role == Qt.TextAlignmentRole:                         #    对齐
            if column == 0:
                return QVariant(int(Qt.AlignLeft))
            if column == 1:
                return QVariant(int(Qt.AlignCenter))

        
        
        elif role == Qt.DisplayRole:                                      #    显示的数据
            if column == 0:
                return __txt
            elif column == 1:
                return __info            
            
            
    def headerData(self, section, orientation, role=Qt.DisplayRole):            #   标题
        if role == Qt.TextAlignmentRole:
            if orientation == Qt.Horizontal:
                return QVariant(int(Qt.AlignCenter))
            return QVariant(int(Qt.AlignRight|Qt.AlignVCenter))
        if role != Qt.DisplayRole:
            return QVariant()
        if orientation == Qt.Horizontal:
            if section == 0:
                return QVariant("Name")
            elif section == 1:
                return QVariant("Info")
        return QVariant(int(section + 1))        
        

        

    def setData(self,index,value,role = Qt.EditRole):
        if role == Qt.EditRole:
            __row = index.row()
            column = index.column()
            if value.isValid():
                if self._showNameSpace:
                    __L = str(value.toString())     
                    __full_new =  self._nodes[__row].MyLongToFull(__L)       
                    self._nodes[__row].MyInitVar( __full_new)    
                else:
                    __S = str(value.toString())     
                    __full_new =  self._nodes[__row].MyShortToFull(__S)       
                    self._nodes[__row].MyInitVar( __full_new)
                print index.row()
                
                self.dataChanged.emit(index,index)              #改完的数据同步
                
                return True
        return False



        
    def flags(self,index):
        return  Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable | Qt.ItemIsDragEnabled | Qt.ItemIsDropEnabled
               
    def rowCount(self,parent):
        return len(self._nodes)
     
    def columnCount(self, parent):                                     #   设置有多少列
        return 2




if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = ImageSwitchPath()
    window.show()
    sys.exit(app.exec_())        


    
    
