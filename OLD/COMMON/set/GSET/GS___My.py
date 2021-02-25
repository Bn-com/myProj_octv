# -*- coding: utf-8 -*-
import json

from PyQt4.QtCore import *

from PyQt4.QtGui import *

from COMMON.set.GSET.GS__View import GSView
from GS_Pix_BG import GSBG
from GS_Pix_Control import GSControl


class GSMy(GSView):
    json_file="GS__Data.json"
    with open(json_file, "r") as f:
        json_data = json.loads(f.read().decode("gbk"), encoding="utf-8")

    def __init__(self, parent=None):
        super(GSMy, self).__init__(parent)

    #     # 元素
    #     self.item_1 = GS_GraphicEllipseItem(parent=None, scene=self.scene)
    #     self.item_1.setPos(30,30)
    #
        SIZE = self.json_data[u"空间大小"]

        # self.json_data[u"图片组"]

        # 背景组
        for bg in self.json_data[u"背景组"]:
            if bg["type"] == u"背景":
                # print bg["png"]
                self.bg = GSBG(QPixmap(bg["url"]), parent=None, scene=self.scene)
            elif bg["type"] == u"标志":
                pass
                # print bg["url"]

        # 数据组
        for dt in self.json_data[u"数据组"]:
            # if dt[u"Maya名称"] == "Master":
                # print dt[u"图片类型"],'-------',dt[u"Maya名称"]
                url = self.json_data[u"图片组"][dt[u"图片类型"]]["url"]
                size = self.json_data[u"图片组"][dt[u"图片类型"]]["size"]
                p_x = dt["pos"][0] *500 /SIZE
                p_y = dt["pos"][1] *500 /SIZE

                p = GSControl(QPixmap(url), parent=None, scene=self.scene, pos=QPoint(p_x, p_y), size=size)
                # p.setOffset(off_QP)

    #     # 不缩放的元素
    #     self.no_scale_items.append(p1)
    #     self.no_scale_items.append(p2)
    #     self.no_scale_items.append(p3)
    #
    #     # logo
    #     self.logo = GSGraphicText(text=u"测试版本", parent=None, scene=self.scene)
    #     self.logo.setPos(self.mapToScene(20, 20))
    #     self.no_scale_items.append(self.logo)
    #     logo_font = QFont()
    #     logo_font.setPointSize(16)
    #     self.logo.setFont(logo_font)
    #



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    # print app.font().StyleHint()
    view = GSMy()
    view.show()
    sys.exit(app.exec_())