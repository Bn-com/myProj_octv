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
import sys,re,os,copy,inspect,random,yaml,io
import logging
logger = logging.getLogger(__name__)
try:
    from PySide.QtGui import *
    from PySide.QtCore import *
    from PySide.QtUiTools import QUiLoader
    import pysideuic as uic

except:
    from PySide2.QtWidgets import *
    from PySide2.QtGui import *
    from PySide2.QtCore import *
    from PySide2.QtUiTools import QUiLoader
    import pyside2uic as uic

class PermissionsManager_UI(QMainWindow):
    def __init__(self, parent=None):
        super(PermissionsManager_UI, self).__init__(parent)
        self.setObjectName('PermissionsManager_mainWin')
        self.setWindowTitle("YML File Manager")
        # self.setStyleSheet("background-color:#5a5d63")
        self.centralwidget = QWidget(self)
        self.v_layout = QVBoxLayout(self.centralwidget)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName('widget')
        self.v_layout_2 = QVBoxLayout(self.widget)
        self.v_layout_2.setObjectName('v_layout_2')
        #add button
        self.pbtn_new = QPushButton(self.widget)
        self.pbtn_new.setText("New yml file...")
        self.v_layout_2.addWidget(self.pbtn_new)
        self.pbtn = QPushButton(self.widget)
        self.pbtn.setText("Load yml file....")
        self.v_layout_2.addWidget(self.pbtn)
        self.pbtn_save = QPushButton(self.widget)
        self.pbtn_save.setText("Save yml file.....")
        self.v_layout_2.addWidget(self.pbtn_save)
        self.pbtn_add = QPushButton(self.widget)
        self.pbtn_add.setText("add under selected group....")
        self.v_layout_2.addWidget(self.pbtn_add)
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
        self.pbtn.clicked.connect(self._fn_loading)
        self.pbtn_save.clicked.connect(self.saving)
        self.pbtn_add.clicked.connect(self.addOneElement)
        self.pbtn_new.clicked.connect(self.newFile)
        #=======================================================
        self._addedElements = []
        self._ReadYMLdata = {}
        self._profiles = None
        self._ControlTier = {}
        self._DATA_DICT={}
        self._titleTier = "root"
        self.resize(300,500)
        # self.setupUi2()
        # self._fn_popmenu()
    @property
    def profiles(self):
        return self._profiles
    @profiles.setter
    def profiles(self,fpath):
        self._profiles = fpath
    def setupUi2(self):
        pass
    def addOneElement(self):
        self._fn_titleAndGroup()

        addDialog = QInputDialog()
        self.add_item, addOrNot = addDialog.getText(self, "add an Item","add what?", QLineEdit.Normal,"Enter .....")
        add2wd = self
        for e_tier in self.add_item.split('.'):
            if e_tier in self.titleNgroup:
                add2wd = self.titleNgroup[e_tier]
            else:
                addOne = AddAGroup(e_tier,parent = add2wd)
                add2wd._addGroup(addOne)
                add2wd = addOne
        self._fn_titleAndGroup()
    def _fn_titleAndGroup(self):
        self.titleNgroup = {}
        for egrp in self.findChildren(QGroupBox):
            g_t = egrp.title()
            self.titleNgroup.update({g_t: egrp})

        # oneGrp = AddAGroup(key, parent=parent)
        # self.focusNextPrevChild(True)
        # widget = QApplication.focusWidget()
        # print(widget)

    #     self.frame.setContextMenuPolicy(Qt.CustomContextMenu)
    #     self.frame.customContextMenuRequested.connect(self.on_context_menu)
    #     self._fn_popmenu()
    # def _fn_popmenu(self):
    #     self.popMenu = QMenu(self)
    #     self.popMenu.addAction(QAction("Add Single Item",self))
    #     self.popMenu.addAction(QAction("Add Multiple Items",self))
    #     # self.popMenu.exec_()
    # def on_context_menu(self,point):
    #     # print(self.popMenu.pos())
    #     self.popMenu.exec_(self.frame.mapToGlobal(point))
    #     # print(self.popMenu.pos())
    #
    #     widget = QApplication.focusWidget()
    #     print(widget)
    #
    # def eventFilter(self, obj, event):
    #     if event.type() == QEvent.FocusIn:
    #         # if obj == self.lineEdit:
    #         #     print("lineedit")
    #         # elif obj == self.pushButton:
    #         #     print("pushbutton")
    #         # elif obj == self.comboBox:
    #         #     print("combobox")
    #         # el
    #         print(obj)
    #     return super(PermissionsManager_UI, self).eventFilter(obj, event)
    #


    #====================================================================================
    def newFile(self):
        self._resetUI()
        self.profiles = None
        print("ready for a new yml file..>>{0}".format(self.profiles))
    def saving(self):
        """
            save date
        :return:
        """
        self.fn_via_ui_save_data()
        if not self.profiles:
            name = QFileDialog.getSaveFileName(self, 'Save File')
            if not name[0]:return
            self.profiles = name[0]
        else:
            opr = self.warMSG()
            if not opr: return
        self._fn_control_yml(self._profiles,'w',self._DATA_DICT)
        self.profiles = None
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
        for e_grp in self.findChildren(QGroupBox):
            # e_grp = xx.findChildren(QGroupBox)[0]
            if (e_grp.findChildren(QGroupBox) or e_grp.findChildren(QListView) or e_grp.findChildren(QLineEdit)): continue
            tiers = e_grp._titleTier.split('.')[1:]
            self.nested_set(self._DATA_DICT, tiers, None)

    def _fn_loading(self):
        searchDir = os.path.dirname(self.profiles) if self.profiles else ""
        fname = QFileDialog.getOpenFileName(self, 'select yml config file', searchDir, "yml files (*.yml)")
        if not fname[0]: return
        self.profiles = fname[0]
        self.loadFromYml()
    def loadFromYml(self):
        # if not self.profiles:
        self._ReadYMLdata = self._fn_control_yml(self.profiles,'r')
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
            ??????????????????
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
            print("Save File <{}>".format(filepath))
    def _addGroup(self,groupObj):
        # oneGrp = AddAGroup(self)
        self.v_layout_4.addWidget(groupObj)
        return groupObj
    def _addElements(self,lableText):
        elem_frame = AddAFrame(lableText,parent=self)
        self.v_layout_4.addWidget(elem_frame)
        return elem_frame
    def _set_all_elements(self,parentControl, _configData):
        # print("~~~~~~~~~~~~~~~~~~~~0001")
        # print(parentControl)
        # print(self)
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
            else:
                oneGrp = AddAGroup(key,parent=parent)
                parentControl._addGroup(oneGrp)

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
        msgBox.setText(u"????????????????????????????????????????????????")
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
        self.h_layout = QHBoxLayout()
        self.h_layout.setObjectName("h_layout")
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.h_layout.addItem(spacerItem)
        self.btn_del = QPushButton(self)
        self.btn_del.setText("delete...")
        self.h_layout.addWidget(self.btn_del)
        self.v_layout.addLayout(self.h_layout)
        self._titleTier = self._fn_get_titletier()
        self.setCheckable(True)
        # self.toggled.connect(self.coolapseGroup)
        self.toggled.connect(self.group_box_size_change)
        self.btn_del.clicked.connect(self.deleteLater)
        self._height = None
        self.setupUi2()
    def setupUi2(self):
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.on_context_menu)
        # self.popMenu.exec_()
    def on_context_menu(self,point):
        curPos = QCursor.pos()
        print(curPos)
        p_wgt = QApplication.widgetAt(curPos)
        p_wgt_nm = str(p_wgt.objectName())

        self.popMenu = QMenu(self)
        self.popMenu.addAction(QAction("Add Single Item", self))
        self.popMenu.addAction(QAction("Add Multiple Items", self))
        self.popMenu.triggered[QAction].connect(lambda q, x=p_wgt_nm: self._fn_popActionRun(q, x))  # lambda  ????????????????????????action ??????
        # print(self.popMenu.pos())
        # widget = QApplication.focusWidget()
        # print(widget)
        self.popMenu.exec_(self.mapToGlobal(point))
    def _fn_popActionRun(self,q,name):
        addDialog = QInputDialog()
        self.add_item, addOrNot = addDialog.getText(self, "Item Title", "add what?", QLineEdit.Normal, ".....")
        if not self.add_item:return
        add_elemt = self._addElements(self.add_item)
        if q.text() == 'Add Single Item':
            add_elemt._method_addItems("..")
        else:
            add_elemt._method_addItems([])
        # print(name)
        # print(self._titleTier)
        self.sg_titleTier.emit(self._titleTier)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.FocusIn:
            # if obj == self.lineEdit:
            #     print("lineedit")
            # elif obj == self.pushButton:
            #     print("pushbutton")
            # elif obj == self.comboBox:
            #     print("combobox")
            # el
            print(obj)
        return super(PermissionsManager_UI, self).eventFilter(obj, event)









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
        # print(add_a_element._titleTier)
        return add_a_element
    def _addGroup(self,groupObj):
        # add_a_group = AddAGroup(parent=self)
        # add_a_group.setTitle(labelText)
        self.v_layout.addWidget(groupObj)
        # self.sg_titleTier.emmit("{}{}")
        return groupObj
    def coolapseGroup(self,state):
        print(state)
        if not state:
            self._height = self.size().height()
            self.setSize

    def group_box_size_change(self):
        duration = 200
        self.animaiton_gb = QPropertyAnimation(self, b"size")
        self.animaiton_gb.setDuration(duration)
        self.animaiton_gb.setStartValue(QSize(self.width(), self.height()))
        if self.isChecked():
            self.animaiton_gb.setEndValue(
                QSize(self.width(), self.sizeHint().height()))
        else:
            self.animaiton_gb.setEndValue(QSize(self.width(), 49))
        self.animaiton_gb.start()



class AddAFrame(QGroupBox):
    # KVPair = Signal(dict)
    def __init__(self,*args,**kwargs):
        super(AddAFrame,self).__init__(*args,**kwargs)
        self.vLayout = QVBoxLayout(self)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QSpacerItem(40, 20,QSizePolicy.Expanding,QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.btn_del = QPushButton(self)
        self.btn_del.setText("delete...")
        self.horizontalLayout_2.addWidget(self.btn_del)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.vLayout.addLayout(self.horizontalLayout_2)
        self.vLayout.addLayout(self.horizontalLayout)
        # self.setLayout(self.horizontalLayout)
        self.setLayout(self.vLayout)
        self.oneItemHeigth = 22
        self._titleTier = "{}.{}".format(self.parent()._titleTier, self.title()) if getattr(self.parent(),'_titleTier',None) else self.title()
        self.btn_del.clicked.connect(self.deleteLater)
        # self.setStyleSheet("QGroupBox:title {color: rgb(1, 130, 153);}")
        self.setStyleSheet("QGroupBox:title {color: #ff5a54;}")
        # self._titleTier = "{}.{}".format(self.parent()._titleTier, self.title())
    def _add_singleLine(self,lineText=""):
        self.line_e = T_QLineEdit(self)
        self.line_e.setText(lineText)
        self.horizontalLayout.addWidget(self.line_e)
    def _add_list(self):
        self.lstwidget = T_QListWidget(self)
        self.horizontalLayout.addWidget(self.lstwidget)
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
            itemOrItemList.sort()
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
    if os.getenv('username') not in ['renhj','weij','yangh','dengtao','zhangben']:
        logger.error(u'??????????????????????????????????????????????????? Sorry! You have no permission to use this function! Contact Tech Section Please!')
        return
    for widget in qApp.allWidgets():
        if hasattr(widget, "objectName"):
            # if widget.objectName() == '****':
            if widget.objectName() == "PermissionsManager_mainWin": #'Ui_MainWindow'
                widget.close()
    view = PermissionsManager_UI(getMayaWindow())
    view.profiles = profpth
    view.show()
    view.loadFromYml()
if __name__ == '__main__':
    import sys
    r"""
    import sys
    from PySide2.QtWidgets import *
    sys.path.append(r'F:\Development\octProj\oct\maya_sixteen\Python\OCT_Pipeline\scripts\utility')
    import permissionsManager as xxx;reload(xxx)
    #xxx.main_ui()
    for widget in qApp.allWidgets():
        if hasattr(widget, "objectName"):
            if widget.objectName() == "PermissionsManager_mainWin":
                widget.close()
    xx = xxx.PermissionsManager_UI(xxx.getMayaWindow())
    xx.show()
    """
    app = QApplication(sys.argv)
    # view = UI()
    view = PermissionsManager_UI()
    view.show()
    sys.exit(app.exec_())

