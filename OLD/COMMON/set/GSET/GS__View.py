# -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import GS__Scene;reload(GS__Scene)
"""
View(视口)--Scene(场景)--Item(元素)
"""

class GSView(QGraphicsView):
    """
    View(视口)
    """
    def __init__(self, parent=None):
        super(GSView, self).__init__(parent)
        self.setGeometry(100, 100, 600, 600)

        self.setMouseTracking(True)
        self.setDragMode(self.RubberBandDrag)
        # self.setRenderHint(QPainter.HighQualityAntialiasing)
        # self.setRenderHint(QPainter.TextAntialiasing)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.setAlignment(Qt.AlignJustify)
        self.view_sacle = 1

        # 不随视口一起缩放的元素
        self.no_scale_items = []

        # 场景
        self.scene = GS__Scene.GSScene(self)
        self.scene.setSceneRect(-250, 0, 500, 500)
        self.setScene(self.scene)

        # 视口的 Y 轴倒置
        self.scale(1, -1)

    def my_scale(self, x, y):
        self.scale(x,y)
        for a in self.no_scale_items:
            a.scale(1/x, 1/y)

    def wheelEvent(self, event):
        """鼠标事件--滚轮滚动"""
        super(GSView, self).wheelEvent(event)
        factor = 1.1 ** (event.delta() / 240.0)
        self.my_scale(factor, factor)
        self.view_sacle = self.view_sacle / factor
        # self.logo.setPos(self.mapToScene(20, 20))

    def keyPressEvent(self, event):
        super(GSView, self).keyPressEvent(event)
        if event.key() == Qt.Key_Alt:   # Alt 键按下
            self.setDragMode(self.ScrollHandDrag)
            event.accept()

    def keyReleaseEvent(self, event):
        super(GSView, self).keyReleaseEvent(event)
        if event.key() == Qt.Key_Alt:   # Alt 键抬起
            self.setDragMode(self.RubberBandDrag)
            event.accept()

    def enterEvent(self, event):
        self.setDragMode(self.RubberBandDrag)

    # def leaveEvent(self, event):
    #     self.setDragMode(self.RubberBandDrag)
    #     print 222222222222

    def mouseDoubleClickEvent(self, event):
        """鼠标事件，双击 --- 复制选中的控制器"""
        super(GSView, self).mouseDoubleClickEvent(event)

    def drawBackground(self, painter, rect):
        """场景的填充和阴影"""
        # 阴影.
        sceneRect = self.sceneRect()
        w = 10
        rightShadow = QRectF(300, - 50 - w, w, 600)
        bottomShadow = QRectF(-300 + w, 0, 600, -50 - w)
        if rightShadow.intersects(rect) or rightShadow.contains(rect):
            painter.fillRect(rightShadow, Qt.black)
        if bottomShadow.intersects(rect) or bottomShadow.contains(rect):
            painter.fillRect(bottomShadow, Qt.black)

        # 背景渐变填充.
        gradient = QLinearGradient(QPointF(-300, 0), QPointF(300.0, 600.0))
        gradient.setColorAt(0, Qt.white)
        gradient.setColorAt(1, Qt.darkCyan)
        painter.fillRect(rect.intersect(QRectF(-300.0, -50.0, 600.0, 600.0)), QBrush(gradient))
        # painter.setBrush(Qt.NoBrush)
        painter.drawRect(-300, -50, 600, 600)

        # painter.setBrush(Qt.CrossPattern)

        pen = QPen(Qt.darkRed, 2, Qt.DotLine)
        painter.setPen(pen)
        painter.drawRoundedRect(QRectF(-250, 0, 500, 500), 1, 1)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    view = GSView()
    view.show()
    sys.exit(app.exec_())