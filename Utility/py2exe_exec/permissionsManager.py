#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = permissionsManager.py
__author__ = zhangben 
__mtime__ = 2021/1/8 : 15:32
__description__: 

    code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""
import sys,copy,yaml
# try:
#     from PySide.QtGui import *
#     from PySide.QtCore import *
#     from PySide.QtUiTools import QUiLoader
    # import pysideuic as uic
# except:
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtUiTools import QUiLoader
# import pyside2uic as uic
# if str(sys.executable).endswith("maya.exe"):
#     import maya.cmds as mc
#     import pymel.core as pm
#     import maya.OpenMaya as om
#     import maya.api.OpenMaya as om2
#     import maya.OpenMayaUI as mui
#     try:
#         import shiboken as sbk
#     except:
#         import shiboken2 as sbk
# def getMayaWindow():
#     ptr = mui.MQtUtil.mainWindow()
#     if ptr is not None:
#         return sbk.wrapInstance(long(ptr), QWidget)
class PermissionsManager_UI(QMainWindow):
    def __init__(self, parent=None):
        super(PermissionsManager_UI, self).__init__(parent)
        self.setObjectName('PermissionsManager_mainWin')
        self.setWindowTitle("OCT Premissions Manager")
        # self.setStyleSheet("background-color:#5a5d63")
        self.centralwidget = QWidget(self)
        self.v_layout = QVBoxLayout(self.centralwidget)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName('widget')
        self.v_layout_2 = QVBoxLayout(self.widget)
        self.v_layout_2.setObjectName('v_layout_2')
        #add button
        self.pbtn = QPushButton(self.widget)
        self.pbtn.setText("select yml file....")
        self.v_layout_2.addWidget(self.pbtn)
        self.pbtn_save = QPushButton(self.widget)
        self.pbtn_save.setText("Save yml file.....")
        self.v_layout_2.addWidget(self.pbtn_save)
        # frame
        self.frame = QFrame(self.widget)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")
        # v 3
        self.v_layout_3 = QVBoxLayout(self.frame)
        self.v_layout_3.setObjectName('v_layout_3')
        # scroll area
        self.scrollArea = QScrollArea(self.frame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        # widget
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 687, 433))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        # v 4
        self.v_layout_4 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.v_layout_4.setObjectName('v_layout_4')
        self.widget_2 = T_QWidget(self.scrollAreaWidgetContents)
        self.widget_2.setObjectName('widget_2')
        self.v_layout_4.addWidget(self.widget_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.v_layout_3.addWidget(self.scrollArea)
        self.v_layout_2.addWidget(self.frame)
        self.v_layout.addWidget(self.widget)

        self.setCentralWidget(self.centralwidget)

        # self.setStyleSheet("background-color:#51555a")
        self.pbtn.clicked.connect(self.addOneItem)
        self.pbtn_save.clicked.connect(self.saving)
        #=======================================================
        self._addedElements = []
        self._ReadYMLdata = {}
        self._profile = None
        self._ControlTier = {}
        self._DATA_DICT={}
        self._titleTier = "root"
    def setupUi2(self):
        print("ok")
    def saving(self):
        """
            save date
        :return:
        """
        self.fn_via_ui_save_data()
        opr = self.warMSG()
        if not opr: return
        self._fn_control_yml(self._profile,'w',self._DATA_DICT)
    def fn_via_ui_save_data(self):
        """
            via ui save data to dictionary
        :return:
        """
        for e_line in self.findChildren(QLineEdit):
            tiers = e_line._titleTier.split('.')[1:]
            data = self._fn_obtainWidgetData(e_line)
            self.nested_set(self._DATA_DICT, tiers, data)
        for e_lst in self.findChildren(QListWidget):
            tiers = e_lst._titleTier.split('.')[1:]
            data = self._fn_obtainWidgetData(e_lst)
            self.nested_set(self._DATA_DICT, tiers, data)
    def addOneItem(self):
        fname = QFileDialog.getOpenFileName(self, 'select yml config file','', "yml files (*.yml)")
        if not fname[0]: return
        self._profile = fname[0]
        self._ReadYMLdata = self._fn_control_yml(self._profile,'r')
        ymldata = copy.deepcopy(self._ReadYMLdata)
        self._resetUI()
        self._set_all_elements(self,ymldata)
    def _resetUI(self):
        for e_Grp in self.findChildren(QGroupBox):
            e_Grp.deleteLater()
    def someFunc(self,q):
        print(q.objectName())
    @staticmethod
    def _fn_control_yml(filepath=None,mode='r',data=None):
        u"""
            处理配置文件
        :param filepath:
        :param mode:
        :param data:
        :return:
        """
        if mode in['r','read']:
            with open(filepath, 'r') as fr:
                readYMLdata = yaml.full_load(fr)
            return readYMLdata
        elif mode in ['wr','w']:
            with open(filepath,'w') as wf:
                yaml.dump(data,wf)
    def _addGroup(self,groupObj):
        # oneGrp = AddAGroup(self)
        self.v_layout_4.addWidget(groupObj)
        return groupObj
    def _addElements(self,lableText):
        elem_frame = AddAFrame(lableText,parent=self)
        self.v_layout_4.addWidget(elem_frame)
        return elem_frame
    def _set_all_elements(self,parentControl, _configData):
        print("~~~~~~~~~~~~~~~~~~~~0001")
        print(parentControl)
        print(self)
        parent = self.widget_2 if parentControl is self else parentControl
        for key, valuse in _configData.items():
            if isinstance(valuse, dict):
                oneGrp = AddAGroup(key,parent=parent)
                print(oneGrp._titleTier)
                parentControl._addGroup(oneGrp)
                self._set_all_elements(oneGrp,valuse)
            elif isinstance(valuse,(str,int,float,list)):
                add_elem = parentControl._addElements(key)
                add_elem._method_addItems(valuse)
    @staticmethod
    def _listData(e_lstw):
        """
            listWidget items....
        :param e_lstw:
        :return:
        """
        content = [e_lstw.item(n).text() for n in range(e_lstw.count())]
        return content

    def _fn_obtainWidgetData(self,qObject):
        """
            obtain specific qWidget contains data
        :return:
        """
        if isinstance(qObject,QLineEdit): return qObject.text()
        elif isinstance(qObject,QListWidget): return self._listData(qObject)
    @staticmethod
    def nested_get(dic, keys):
        for key in keys:
            dic = dic[key]
        return dic
    @staticmethod
    def nested_set(dic, keys, value):
        for key in keys[:-1]:
            dic = dic.setdefault(key, {})
        dic[keys[-1]] = value
    def warMSG(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(u"是否保存当前数据替换原配置文件？")
        msgBox.setWindowTitle("Override Warning")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = msgBox.exec_()
        if returnValue == QMessageBox.Ok: return True
        else: return None














    def _parse_data(self,qObj, data=None):
        if not data: data = qObj.text() if isinstance(qObj, QLineEdit) else self._listData(qObj)
        # data = data_3
        pGrp = qObj.parent()
        if pGrp is self.mainWidget:
            self._DATA_DICT.update(data)
        else:
            pGrp_t = pGrp.title()
            newData = {pGrp_t: data}
            self._parse_data(pGrp, newData)


    def _qGrpNData(self,qGrp):
        """
            get the k-v pair of QGroupbox title and  it  contains data
        :return:
        """
        return {qGrp.title(): self.fn_qGrpContainData(qGrp)}

    def fn_qGrpContainData(self,qGrp):
        """
            groupbox contain qlineedit or qlistWigdget .. get the data
        :param qGrp:
        :return:
        """
        if qGrp.findChildren(QListWidget):
            return self._listData(qGrp.findChildren(QListWidget)[0])
        else:
            return qGrp.findChildren(QLineEdit)[0].text()

    def _iterrate_dict(diction, keys):
        """

        a_dct = {'a':{'b':{'c':3}}}
        keys = ['a','b','c']
        _iterrate_dict(a_dct,keys) = 3
        :param keys:
        :return:
        """
        for ek in keys:
            diction = diction[ek]
        return diction

"""
for e_grp in qObj.findChildren(QGroupBox):
e_grp = qObj.findChildren(QGroupBox)[1]
grp_t = e_grp.title()
if not data :data = {grp_t:None}
     
#addedKey.append(key)
chgrps = e_grp.findChildren(QGroupBox)
if not chgrps:
    data_ch = e_grp.findChildren(QLineEdit)[0] if e_grp.findChildren(QLineEdit) else e_grp.findChildren(QListWidget)[0] 
    detail_data = data_ch.text() if isinstance(data_ch,QLineEdit) else xx._listData(data_ch)
    data.update({grp_t:detail_data})
    _DATA_DICT.update(data)
else:
    for e_ch_grp in chgrp:
#e_ch_grp = chgrps[0]        
        ch_t = e_ch_grp.title()
        data.update({grp_t:{ch_t:None}})

"""

class AddAGroup(QGroupBox):
    sg_titleTier = Signal(str)
    def __init__(self,*args,**kwargs):
        super(AddAGroup,self).__init__(*args,**kwargs)
        self.v_layout = QVBoxLayout(self)
        self._titleTier = self._fn_get_titletier()
    # @property
    # def titleTier(self):
    #     if not self._titleTier:
    #         print(self.parent)
    #         self._titleTier = "{}.{}".format(self.parent._titleTier, self.title()) if self.parent.__getattribute__('_titleTier') else self.title()
    #     return self._titleTier
    def _fn_get_titletier(self):
        if getattr(self.parent(),'_titleTier',None):
            return "{}.{}".format(self.parent()._titleTier, self.title())
        else:
            return self.title()
    def _addElements(self,lableText):
        add_a_element = AddAFrame(lableText,parent=self)
        self.v_layout.addWidget(add_a_element)
        # self.sg_titleTier.emit("{}.{}".format(self._titleTier,lableText))
        print(add_a_element._titleTier)
        return add_a_element
    def _addGroup(self,groupObj):
        # add_a_group = AddAGroup(parent=self)
        # add_a_group.setTitle(labelText)
        self.v_layout.addWidget(groupObj)
        # self.sg_titleTier.emmit("{}{}")
        return groupObj
class AddAFrame(QGroupBox):
    KVPair = Signal(dict)
    def __init__(self,*args,**kwargs):
        super(AddAFrame,self).__init__(*args,**kwargs)
        self.horizontalLayout = QHBoxLayout(self)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.setLayout(self.horizontalLayout)
        self._titleTier = "{}.{}".format(self.parent()._titleTier, self.title()) if getattr(self.parent(),'_titleTier',None) else self.title()
        # self._titleTier = "{}.{}".format(self.parent()._titleTier, self.title())
    def _add_singleLine(self,lineText=""):
        self.line_e = T_QLineEdit(self)
        self.line_e.setText(lineText)
        self.horizontalLayout.addWidget(self.line_e)
    def _add_list(self):
        self.lstwidget = T_QListWidget(self)
        self.horizontalLayout.addWidget(self.lstwidget)
        self.oneItemHeigth = 22
        self.lstwidget.setFixedHeight(0)
        self.bt_add = QPushButton(self)
        self.bt_add.setObjectName("addItem_pb")
        self.bt_add.setText('+')
        self.bt_minus = QPushButton(self)
        self.bt_minus.setObjectName("minusItem_pb")
        self.bt_minus.setText('-')
        self.horizontalLayout.addWidget(self.bt_add)
        self.horizontalLayout.addWidget(self.bt_minus)
        # self.show()
        self.lstwidget.itemDoubleClicked.connect(self._handelDoubleClicked)
        self.bt_add.clicked.connect(self._method_addItem)
        self.bt_minus.clicked.connect(self._method_minusItem)
    def _handelDoubleClicked(self,item):
        item.setFlags(item.flags()|Qt.ItemIsEditable)
    def _method_addItems(self,itemOrItemList):
        if isinstance(itemOrItemList,list):
            self._add_list()
            for e_itm in itemOrItemList:
                self._method_addItem(e_itm)
        else:
            self._add_singleLine(itemOrItemList)
    def _method_addItem(self,itemText=''):
        add_1itm = QListWidgetItem(itemText)
        add_1itm.setSizeHint(QSize(add_1itm.sizeHint().width(),self.oneItemHeigth))
        self.lstwidget.addItem(add_1itm)
        self._listHeight()
    def _method_minusItem(self):
        selItems = self.lstwidget.selectedItems()
        for e_item in selItems:
            self.lstwidget.takeItem(self.lstwidget.row(e_item))
        self._listHeight()
    def _listHeight(self):
        rowCnt = self.lstwidget.count()
        set_h = rowCnt*self.oneItemHeigth
        self.lstwidget.setFixedHeight(set_h+5)


class T_QListWidget(QListWidget):
    def __init__(self,*args,**kwargs):
        super(T_QListWidget,self).__init__(*args,**kwargs)
        self._titleTier = self.parent()._titleTier

class T_QLineEdit(QLineEdit):
    def __init__(self,*args,**kwargs):
        super(T_QLineEdit,self).__init__(*args,**kwargs)
        self._titleTier = self.parent()._titleTier

class T_QWidget(QWidget):
    def __init__(self,*args,**kwargs):
        super(T_QWidget,self).__init__(*args,**kwargs)
        self._titleTier = 'root'
    # def _addGroup(self,groupObj):
    #     # oneGrp = AddAGroup(self)
    #     self.v_layout.addWidget(groupObj)
    #     return groupObj
    # def _addElements(self,lableText):
    #     elem_frame = AddAFrame(lableText,parent=self)
    #     self.layout().addWidget(elem_frame)
    #     return elem_frame
def main_ui():
    for widget in qApp.allWidgets():
        if hasattr(widget, "objectName"):
            # if widget.objectName() == '****':
            if widget.objectName() == "permissionsManager_mainWin": #'Ui_MainWindow'
                widget.close()
    view = PermissionsManager_UI()
    view.show()
if __name__ == '__main__':
    import sys
    """
import sys
sys.append("")
from PySide2.QtWidgets import *
sys.path.append(r'')
import permissionsManager as xxx;reload(xxx)
#xxx.main_ui()
for widget in qApp.allWidgets():
    if hasattr(widget, "objectName"):
        if widget.objectName() == "permissionsManager_mainWin":
            widget.close()
xx = xxx.permissionsManager_UI(xxx.getMayaWindow())
xx.show()
    """
    app = QApplication(sys.argv)
    # view = UI()
    view = PermissionsManager_UI()
    view.show()
    sys.exit(app.exec_())

