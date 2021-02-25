# -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import json
import sip
from pymel.all import *
import maya.OpenMayaUI as apiUI

import Maya___Main_QT;reload(Maya___Main_QT)

import UI_Main;reload(UI_Main)
import GS_Pix_BG;reload(GS_Pix_BG)
import GS_Pix_Control;reload(GS_Pix_Control)


def getMayaWindow():
    ptr = apiUI.MQtUtil.mainWindow()
    return sip.wrapinstance(long(ptr), QObject)

class Maya_Main(Maya___Main_QT.DesignerUI):
    # json_file="GS__Data.json"
    # with open(json_file, "r") as f:
    #     json_data = json.loads(f.read().decode("gbk"), encoding="utf-8")

    def __init__(self, parent=getMayaWindow()):
        super(Maya_Main, self).__init__(parent)

        # 元素
        # self.item_1 = GS_GraphicEllipseItem(parent=None, scene=self.scene)
        # self.item_1.setPos(30,30)

        # SIZE = self.json_data[u"空间大小"]

        # self.json_data[u"图片组"]

        # 背景组
        # for bg in self.json_data[u"背景组"]:
        #     if bg["type"] == u"背景":
        #         print bg["png"]
                # self.bg = GS_GraphicPixmap_BG(QPixmap(bg["url"]), parent=None, scene=self.scene)
            # elif bg["type"] == u"标志":
            #     pass
            #     print bg["url"]

        # 数据组
        # for dt in self.json_data[u"数据组"]:
            # if dt[u"Maya名称"] == "Master":
                # print dt[u"图片类型"],'-------',dt[u"Maya名称"]
                # url = self.json_data[u"图片组"][dt[u"图片类型"]]["url"]
                # size = self.json_data[u"图片组"][dt[u"图片类型"]]["size"]
                # p_x = dt["pos"][0] *500 /SIZE
                # p_y = dt["pos"][1] *500 /SIZE

                # p = GS_GraphicPixmap(QPixmap(url), parent=None, scene=self.scene, pos=QPoint(p_x, p_y), size=size)
                # p.setOffset(off_QP)

        # 不缩放的元素
        # self.no_scale_items.append(p1)
        # self.no_scale_items.append(p2)
        # self.no_scale_items.append(p3)

        # logo
        # self.logo = GSGraphicText(text=u"测试版本", parent=None, scene=self.scene)
        # self.logo.setPos(self.mapToScene(20, 20))
        # self.no_scale_items.append(self.logo)
        # logo_font = QFont()
        # logo_font.setPointSize(16)
        # self.logo.setFont(logo_font)





def main():
    global win
    try: win.close()
    except: pass
    win = Maya_Main()
    win.show()

if __name__ == '__main__':
    main()