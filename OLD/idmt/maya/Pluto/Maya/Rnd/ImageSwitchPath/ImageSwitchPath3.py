# -*- coding: utf-8 -*-
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
                    print __full_new
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

















        
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = ImageSwitchPath()
    window.show()
    sys.exit(app.exec_())      