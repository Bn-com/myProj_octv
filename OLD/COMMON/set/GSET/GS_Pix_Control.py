# -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
"""
View(视口)--Scene(场景)--Item(元素)
"""
import os



class GSControl(QGraphicsPixmapItem):
    MY_TYPE = 'CONTROL'

    def __init__(self, pixmap, parent=None, scene=None,
                 use_name="",
                 use_type="",
                 use_pos=[0, 0],
                 use_view_scale=1,
                 use_scale=1,
                 use_opacity=1
                 ):
        super(GSControl, self).__init__(pixmap, parent, scene)
        self.setTransformationMode(Qt.SmoothTransformation)

        self.setPixmap(pixmap)
        self.scale(1, -1)
        self.scale(use_view_scale, use_view_scale)
        self.setScale(use_scale)
        self.my_opacity = use_opacity
        self.my_enable_highlight = 0
        self.xxx = 0

        #   设置初始化属性
        if scene.control_moveable:
            self.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable)

        self.setPos(QPoint(use_pos[0], use_pos[1]))
        self.setOpacity(use_opacity)
        self.setZValue(1)

        #   需要保存的数据
        self.use_name = use_name
        self.use_type = use_type
        self.use_pos = use_pos
        self.scale()
        self.use_opacity = use_opacity
        #   允许鼠标悬停状态事件
        self.setAcceptHoverEvents(1)

        stroker = QPainterPathStroker()
        stroker.setWidth(2)
        self.stroker_shape = stroker.createStroke(self.shape())




    def paint(self, painter, option, QWidget):
        painter.setRenderHint(painter.HighQualityAntialiasing)
        if option.state & QStyle.State_Selected:
            option.state = option.state & ~QStyle.State_Selected
            super(GSControl, self).paint(painter, option, QWidget)
            painter.fillPath(self.stroker_shape, QBrush(Qt.green))
            painter.fillPath(self.shape(), QBrush(Qt.green))
            if self.my_enable_highlight == 1:
                self.setOpacity(1, method=1)
                self.update()
        else:
            self.setOpacity(self.my_opacity, method=2)
            super(GSControl, self).paint(painter, option, QWidget)
            # super(GSControl, self).paint(painter, option, QWidget)



    def setOpacity(self, p_float, method=0):
        self.my_enable_highlight = 0
        if method == 1:
            if self.xxx == 0:
                # print "yes,yes,yes"
                self.my_opacity = self.opacity()
                p_float = 1

                self.xxx = 1
        elif method == 2:
            # print "no,no,no,no"
            self.xxx = 0

        super(GSControl, self).setOpacity(p_float)
        self.my_enable_highlight = 1

    def setPixmap(self, pix):
        super(GSControl, self).setPixmap(pix)
        self.setOffset(-self.pixmap().width()/2, -self.pixmap().height()/2)

    def set_moveable(self, moveable):
        """设置元素是否可以移动"""
        if moveable is True:
            self.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable)
        else:
            self.setFlags(QGraphicsItem.ItemIsSelectable )

    # def setPos(self, pos):
    #     super(GSControl, self).setPos(pos)

    # def hoverEnterEvent(self, event):
    #     super(GSControl, self).hoverEnterEvent(event)
    #
    # def hoverLeaveEvent(self, event):
    #     super(GSControl, self).hoverLeaveEvent(event)
        # try:
        #     self.MY_QTIMER.stop()
        # except:
        #     print 22222222222222222

    # def pos(self):
    #     print 22
    #     return self.pos()
    #     super(GSControl, self).pos()

    # def __pos__(self):
    #     print 22222


    # def mousePressEvent(self, event):
    #     super(GSControl, self).mousePressEvent(event)


    #         # self.MY_QTIMER.start(1)
    #         self.MY_QTIMER.singleShot(10,self.MY_SIGNALOBJ.MouseMoveSignal.emit)
    #         # self.MY_QTIMER.stop()
    #         event.accept()
    #
    #         print self



    # def mouseReleaseEvent(self, event):
    #     super(GSControl, self).mouseReleaseEvent(event)
    #     if event.button() == Qt.LeftButton:
    #         # self.MY_QTIMER.singleShot(10,self.MY_SIGNALOBJ.MouseMoveSignal.emit)
    #
    #         self.MY_QTIMER.start(10)
    #         self.MY_QTIMER.stop()
    #         # event.accept()

    # def mouseMoveEvent(self, event):
    #     super(GSControl, self).mouseMoveEvent(event)
        # self.MY_QTIMER.singleShot(1000,self.MY_SIGNALOBJ.MouseMoveSignal.emit)
        # if self.pos() != self.ct:
        #     print 2


    # def mouseDoubleClickEvent(self, event):
    #     super(GSControl, self).mouseDoubleClickEvent(event)
