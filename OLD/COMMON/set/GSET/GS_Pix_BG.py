# -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
"""
View(视口)--Scene(场景)--Item(元素)
"""
class GSBG(QGraphicsPixmapItem):
    MY_TYPE = 'BG'
    def __init__(self, pixmap, parent=None, scene=None, pos=QPoint(-250, 500), opacity=1):
        super(GSBG, self).__init__(pixmap, parent, scene)
        self.setTransformationMode(Qt.SmoothTransformation)
        self.pix = pixmap
        self.setPixmap(self.pix)
        # self.setFlags(QGraphicsItem.ItemIsSelectable)
        # self.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsFocusable | QGraphicsItem.ItemIsMovable)
        # text_flags = Qt.TextEditorInteraction
        # self.setRect (30,30,30,30)
        # self.setScale(0.5)
        self.setPos(pos)
        self.scale(0.55, -0.55)
        self.moveBy(-25,25)
        self.setZValue(-1)
        self.setOpacity(opacity)


    # def mousePressEvent(self, *args, **kwargs):
    #     print ''
        # print self.scenePos()