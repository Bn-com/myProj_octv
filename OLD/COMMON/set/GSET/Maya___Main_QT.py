# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys, json, os, math
from functools import partial

"""
                  _ooo0ooo_
                 o888888888o
                 888" . "888
                (|   -_-   |)
                 0\   =   /0
               ____/`---'\____
             .' \\|       |// '.
            / \\|||   :   |||// \
           / _|||||  -:-  |||||- \
          |   | \\\   -   /// |   |
          | \_|  ''\ --- /''  |_/ |
          \  .-\__   '-'   ___/-. /
        ___'. .'   /--.--\   `. .'___
     ."" '<   `.___\_<|>_/___.'  >' "".
    | | :  `-  \`.;`\ _ /`;.` /  - ` : | |
    \  \ `_.    \_ __\ /__ _/    .-` /  /
=====`-.____`.___  \_____/ ___.-`___.-'=====
                  `=-----='
该代码已经做开光处理，佛祖保佑永无错误
"""

import UI_Main;reload(UI_Main)
import GS__Scene;reload(GS__Scene)
import GS_Pix_BG;reload(GS_Pix_BG)
import GS_Pix_BG;reload(GS_Pix_BG)
import GS_Pix_Control;reload(GS_Pix_Control)
import GS_JSON_Base;reload(GS_JSON_Base)

class DesignerUI(QMainWindow):
    """这个是给 Qt Designer 设计界面用的，在 Python 模式下调试的"""
    CONTRL = []
    IF_MAYA_SELECT_CONNECT = True
    BG_OPACITY = 1
    PARENT = os.path.split(__file__)[0]
    GS_Data_json_file = os.path.join(PARENT,"data/GS__Data.json")
    with open(GS_Data_json_file, "r") as f:
        DATA = json.loads(f.read().decode("utf-8"), encoding="utf-8")
    CNBOX = False


    def __init__(self, parent=None):
        super(DesignerUI, self).__init__(parent)
        self.ui = UI_Main.Ui_MainWindow()
        self.ui.setupUi(self)

        # 设置 UI
        self.ui.splitter = QSplitter(self.ui.centralwidget)
        self.ui.centralLayout.addWidget(self.ui.splitter)
        self.ui.splitterLayout = QHBoxLayout(self.ui.splitter)
        self.ui.splitter.addWidget(self.ui.frame_left)
        self.ui.splitter.addWidget(self.ui.frame_right)
        self.ui.splitter.setSizes([600, 200])
        self.ui.splitter.setHandleWidth(3)

        self.if_control_moveable = True
        self.view = self.ui.QGraphicsView_Main
        self.scene = self.ui.QGraphicsView_Main.scene


        # 读取数据=========***********以下非常重要
        self.read_datas(os.path.join(self.PARENT,"data/GS__Data_CHR_01.json"))
        # 清空内容
        self.scene.clear()
        # 不随视口一起缩放的元素
        self.view.no_scale_items = []
        self.CONTRL = []
        # 设置图片位置，缩放，透明度...
        self.my_setup_data()

        # 链接
        self.scene.selectionChanged.connect(self.my_select_changed)         # 并联 Maya选择物体
        self.ui.QCheckBox_Maya_Selection.toggled.connect(self.my_if_maya_select_connect)     # Maya选择物体开关
        self.ui.QTableWidget_Data.cellClicked.connect(self.set_CNBOX)       # 通道栏开关
        self.ui.QTableWidget_Data.cellChanged.connect(self.my_CNBOX_Changed)    # 通道栏改变控制器的属性

        self.ui.QPushButton_test.clicked.connect(self.test_bt)
        self.ui.QPushButton_test2.clicked.connect(self.test_bt2)

        self.scene.MY_SIGNAL.connect(self.my_refresh_channel_box)

    def test_bt(self):
        for item in [i for i in self.scene.items() if i.MY_TYPE == 'CONTROL']:
            # print item.my_opacity
            print item.use_name
            print item.opacity()

            # self.xxx = xx
            # item.scale(pow(1/xx,0.5), pow(1/xx,0.5))

    def fff(self):
        print 4444444

    def test_bt2(self):
        print self.view.view_sacle

    def keyPressEvent(self, event):
        if event.modifiers() & Qt.ControlModifier:
            if event.key() == Qt.Key_D:             # “ctrl + d” 键，复制控制器
                self.on_QPushButton_Duplicate_clicked()
        if event.key() == Qt.Key_Delete:
            self.on_QPushButton_Delete_clicked()


    def set_CNBOX(self):
        self.CNBOX = True

    def read_datas(self, json_file_path):
        """读取json文件，设置全局信息"""
        with open(json_file_path, "r") as f:
            self.DATA_CHR = json.loads(f.read().decode("utf-8"), encoding="utf-8")

        self.SIZE = 500/self.DATA_CHR[u"空间大小"]
        self.DATA_BG = self.DATA_CHR[u"背景组"]
        self.DATA_LOGO = self.DATA_CHR[u"标志组"]
        self.DATA_DATA = self.DATA_CHR[u"数据组"]

    def my_if_maya_select_connect(self):
        self.IF_MAYA_SELECT_CONNECT = 1-self.IF_MAYA_SELECT_CONNECT

    def my_CNBOX_Changed(self, x, y):
        if self.CNBOX is True:
            for item in self.scene.selectedItems():
                value = self.ui.QTableWidget_Data.item(x, y).text()
                if x == 0:
                    item.use_name = str(value)
                if x == 1:          #   图片类型
                    uni_value = unicode(value)
                    if self.DATA["body"].has_key(uni_value):
                        url = self.DATA["body"][uni_value]["url"]
                        url = os.path.join(self.PARENT, url)
                        item.setPixmap(QPixmap(url))
                        item.use_type = uni_value
                    else:
                        table = self.ui.QTableWidget_Data
                        table.removeCellWidget(1, 0)
                        TB_item_type = QTableWidgetItem(item.use_type)
                        table.setItem(1, 0, TB_item_type)

                if x == 2:          #   位置 X
                    item.setX(float(value))
                if x == 3:          #   位置 Y
                    item.setY(float(value))
                if x == 4:          #   缩放
                    item.setScale(float(value))
                if x == 5:          #   透明度
                    if item.MY_TYPE == 'CONTROL':
                        item.setOpacity(float(value))
                        item.my_enable_highlight = 0
                        item.my_opacity = float(value)

            self.CNBOX = False

    def my_refresh_channel_box(self):
        """ 选择的最后一个控制器，刷新它在channal box 的属性 """
        if len(self.scene.selectedItems()) > 0:
            item = self.scene.selectedItems()[0]
            if item.MY_TYPE == 'CONTROL':
                table = self.ui.QTableWidget_Data
                TB_item_name = QTableWidgetItem(item.use_name)
                TB_item_type = QTableWidgetItem(item.use_type)
                TB_item_pos_x = QTableWidgetItem(str(item.pos().x()))
                TB_item_pos_y = QTableWidgetItem(str(item.pos().y()))
                TB_item_scale = QTableWidgetItem(str(item.scale()))
                TB_item_opacity = QTableWidgetItem(str(item.my_opacity))
                table.removeCellWidget(0, 0)
                table.setItem(0, 0, TB_item_name)
                table.removeCellWidget(1, 0)
                table.setItem(1, 0, TB_item_type)
                table.removeCellWidget(2, 0)
                table.setItem(2, 0, TB_item_pos_x)
                table.removeCellWidget(3, 0)
                table.setItem(3, 0, TB_item_pos_y)
                table.removeCellWidget(4, 0)
                table.setItem(4, 0, TB_item_scale)
                table.removeCellWidget(5, 0)
                table.setItem(5, 0, TB_item_opacity)

    def my_select_changed(self):
        """选中的元素改变时，进行如下操作"""
        #   1.  设置单个透明度控制器
        self.view.setDragMode(self.view.RubberBandDrag)
        items = self.scene.selectedItems()
        # if len(items)>0:
        #     self.myuis.QSlider_CT_Opacity_Selected.setValue(int(items[0].opacity()*100))

        #   2.  在 Maya 里选中物体
        # print [a.use_name for a in self.scene.selectedItems()]
        if 'maya.exe' in sys.executable:
            if self.IF_MAYA_SELECT_CONNECT:
                try:
                    from pymel.all import *
                    select([a.use_name for a in self.scene.selectedItems()])
                except:
                    pass

    @pyqtSignature("bool")
    def on_QPushButton_Duplicate_clicked(self):
        """ 复制控制器 """
        new_select_item = []
        for item in self.scene.selectedItems():
            z_value = item.zValue()
            url = self.DATA["body"][item.use_type]["url"]
            url_path = os.path.join(self.PARENT, url)

            p_x = item.pos().x() + 10
            p_y = item.pos().y() + 10

            scale = item.scale()

            opacity = item.opacity()
            p = GS_Pix_Control.GSControl(pixmap=QPixmap(url_path), parent=None, scene=self.scene,
                    use_name=item.use_name + "_xxx", use_type=item.use_type, use_pos=[p_x, p_y, 0],
                    use_scale=scale, use_view_scale=self.view.view_sacle, use_opacity=opacity
                                      )
            item.setSelected(0)
            p.setZValue(z_value+1)
            p.setSelected(1)

            self.CONTRL.append(p)
            self.view.no_scale_items.append(p)
            new_select_item.append(p)

    @pyqtSignature("bool")
    def on_QPushButton_Delete_clicked(self):
        """ 删除控制器 """
        for item in self.scene.selectedItems():
            self.CONTRL.remove(item)
            self.view.no_scale_items.remove(item)
            self.scene.removeItem(item)
            # del item


    @pyqtSignature("bool")
    def on_QCheckBox_Control_Moveable_toggled(self, ifClicked):
        """ checkbox设置控制器是否可移动 """
        self.scene.control_moveable = ifClicked
        for c in self.CONTRL:
            c.set_moveable(ifClicked)

    @pyqtSignature("int")
    def on_QSlider_BG_Opacity_valueChanged(self, xx):
        """slider设置背景透明度"""
        op = xx/100.0
        self.BG.setOpacity(op)
        self.BG_OPACITY = op

    @pyqtSignature("int")
    def on_QSlider_CT_Opacity_Selected_valueChanged(self, xx):
        """slider设置所选控制器透明度"""
        op = xx/100.0
        for item in self.scene.selectedItems():
            if item.MY_TYPE == 'CONTROL':
                item.setOpacity(op)
                item.my_enable_highlight = 0
                item.my_opacity = op
        self.my_refresh_channel_box()

    @pyqtSignature("bool")
    def on_QPushButton_EXPORT_clicked(self):
        """导出json文件"""
        # 1.读取选择的路径
        settings = QSettings("GDCs","GSET")
        folder = settings.value("LastOpenedFolder").toString()
        filename = QFileDialog.getSaveFileName(self, QString("Select File"), folder, QString("Json Files ( *.json)"))
        settings.setValue("LastOpenedFolder",filename)
        # 2.读取配置：
        #   2.1. 总体
        json_size = 500/self.SIZE
        #   2.2. 背景
        json_bg = self.DATA_BG
        for bg in self.DATA_BG:
            bg[u"透明度"] = self.BG_OPACITY
        #   2.3. 标志
        json_logo = self.DATA_LOGO
        #   2.4. 控制器
        json_datas = {}
        for c in self.CONTRL:
            pos = [c.pos().x()/self.SIZE, c.pos().y()/self.SIZE, c.use_pos[2]/self.SIZE]
            json_datas[c.use_name] = {u"可否选择": True, u"图片类型": c.use_type, u"位置": pos, u"缩放": c.scale(), u"透明度": c.my_opacity}
        # 3. *** 导出文件 ***：
        GS_JSON_Base.write_json_file(filename, size=json_size, bg=json_bg, logo=json_logo, datas=json_datas)



    @pyqtSignature("bool")
    def on_QPushButton_IMPORT_clicked(self):
        """导人json文件"""
        settings = QSettings("GDCs","GSET")
        folder = settings.value("LastOpenedFolder").toString()
        filename = QFileDialog.getOpenFileName(self, QString("Select File"), folder, QString("Json Files ( *.json)"))
        filename = filename.toAscii()
        settings.setValue("LastOpenedFolder", filename)
        if len(filename)>2:
            # 读取数据=========***********以下三个非常重要
            self.read_datas(filename)
            # 清空内容
            self.scene.clear()
            # 不随视口一起缩放的元素
            self.view.no_scale_items = []
            self.CONTRL = []
            # 加载内容
            self.my_setup_data()


    def my_setup_data(self):
        """ 设置图片位置，缩放，透明度... """
        # 背景组
        for bg in self.DATA_BG:
            if bg["type"] == u"背景":
                url = bg["url"]
                url = os.path.join(self.PARENT, url)
                opacity = bg[u"透明度"]
                self.BG = GS_Pix_BG.GSBG(QPixmap(url), parent=None, scene=self.scene, opacity=opacity)

        # 数据组
        for dt in self.DATA_DATA.keys():
            # if dt[u"Maya名称"] == "Master":
            type = self.DATA_DATA[dt][u"图片类型"]
            url = self.DATA["body"][type]["url"]
            url_path = os.path.join(self.PARENT, url)

            p_x = self.DATA_DATA[dt][u"位置"][0] * self.SIZE
            p_y = self.DATA_DATA[dt][u"位置"][1] * self.SIZE
            p_z = self.DATA_DATA[dt][u"位置"][2] * self.SIZE

            scale = self.DATA_DATA[dt][u"缩放"]
            opacity = self.DATA_DATA[dt][u"透明度"]

            p = GS_Pix_Control.GSControl(pixmap=QPixmap(url_path), parent=None, scene=self.scene,
                    use_name=dt, use_type=type, use_pos=[p_x, p_y, p_z],
                    use_scale=scale,  use_view_scale=self.view.view_sacle, use_opacity=opacity
                                        )


            self.CONTRL.append(p)
            self.view.no_scale_items.append(p)

    def closeEvent(self, *args, **kwargs):
        pass
        # self.My_Timer.deleteLater()

def main():
    app = QApplication(sys.argv)
    window = DesignerUI()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()