# -*- coding: utf-8 -*-

import sys
from PyQt4.QtCore import * 
from PyQt4.QtGui import * 


#################################################################### 
def main(): 
    app=QApplication(sys.argv)

    #新建一个自定义Model
    model=MyListModel()
    #新建一个委托(Delagate)
    delegate=MyDelegate()

    #新建一个ListView
    view=QTableView()

    #设置view的model，这里设置为代理
    view.setModel(model)
    #设置view的delegate
    view.setItemDelegate(delegate)

    view.show()
    sys.exit(app.exec_())
#################################################################### 
class MyListModel(QAbstractListModel):
    """
    我的第一个模型
    """
    def __init__(self,parent=None):
        super(MyListModel,self).__init__(parent)
        #这是数据
        self._data=[70,90,20,50]


    def rowCount(self, parent=QModelIndex()):
        """
        这个方法返回了数据的行数
        也就是有多少个条目得数据
        """

        return len(self._data)

    def data(self,index,role=Qt.DisplayRole):
        """
        根据当前index索引，返回当前的数据
        然后再由Qt进行渲染显示
        """
        #如果当前得索引是不活动得
        if not index.isValid() or not \
        0<=index.row() <self.rowCount():
            #亦或者当前的索引值不在合理范围，即小于等于0，超出总行数
            return QVariant() #返回一个QVariant，相当与空条目

        #从索引取得当前的航号
        row=index.row()

        #如果当前角色是DisplayRole
        if role==Qt.DisplayRole:
            #返回当前行的数据
            return self._data[row]

        #当前角色为编辑模式，显示原本数据
        #这样，当我们双击单元项时，不至于什么都不显示
        if role==Qt.EditRole:
            return self._data[row]

        #如果角色不满足需求，则返回QVariant
        return QVariant()

    def flags(self, index):
        """
        flag描述了view中数据项的状态信息
        """

        #首先获取超类的flags返回值
        flag=super(MyListModel,self).flags(index)

        #或运算，将ItemIsEditable（可编辑）标志叠加上去
        return flag | Qt.ItemIsEditable

    def setData(self,index,value,role=Qt.EditRole):
        """
        设置数据
        """

        #如果当前为编辑角色
        if role==Qt.EditRole:
            #QVariant的这个方法，返回的bool类型表示这个值是否可以被转为int类型
            value_int, ok=value.toInt()

            #如果可以转为int类型
            if ok:
                #保存数据
                self._data[index.row()]=value_int
                #发射数据更改信号，以便让view更新
                self.dataChanged.emit(index,index)

                return True

            return False














#################################################################### 
class MyDelegate(QStyledItemDelegate):
    """
    自定义的委托
    用来在Model获取后，view显示前，再将数据渲染一次
    """
#    def paint(self,painter,option,index):
#        """
#        paint，有了画布画笔，想怎么显示就怎么显示，画什么按自己的想法来
#        """
#
#        #首先，从索引获取数据，这里获取当前索引角色为DisplayQole的数据
#        item_var=index.data(Qt.DisplayRole) #[QVariant]
#        #数据是C格式，我们再转为Python格式，记住这点
#        item_str=item_var.toPyObject() #[QVariant] -> str
#
#        #我们将数据以进度条的方式显现
#        opts=QStyleOptionProgressBarV2()
#        opts.rect=option.rect #进度条所占的矩形大小
#        opts.minimum=0
#        opts.maximum=100
#        opts.text=str(item_str) #显示的内容
#        opts.textAlignment=Qt.AlignCenter
#        opts.textVisible=True
#        opts.progress=int(item_str) #设置当前进度
#
#        #这是关键
#        #让QApplication根据当前的风格渲染控件并画出来
#        QApplication.style().drawControl(QStyle.CE_ProgressBar,opts,painter) 
#
#    def createEditor(self,parent,option,index):
#        """
#        创建编辑器
#        """
#
#        #创建一个QSPinBox
#        sbox=QSpinBox(parent)
#        sbox.setRange(0,100)
#
#        #返回这个QSpinBox
#        return sbox

#    def setEditorData(self,editor,index):
#        """
#        设置编辑器数据
#        """
#
#        item_var=index.data(Qt.DisplayRole)
#        item_str=item_var.toPyObject()
#        item_int=int(item_str)
#
#        #设置编辑器的数据为当前索引的值
#        editor.setValue(item_int)

#    def setModelData(self,editor,model,index):
#        """
#        给model设置编辑后的数据
#        """
#
#        #获取编辑器的数据
#        data_int=editor.value()
#        #把数据封装为Qt类型
#        data_var=QVariant(data_int)
#
#        #设置Model的数据，当前索引与数据
#        model.setData(index,data_var)  

#################################################################### 

if __name__ == "__main__": 
    main()
