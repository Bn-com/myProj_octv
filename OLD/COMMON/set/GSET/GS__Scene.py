# -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
"""
View(视口)--Scene(场景)--Item(元素)
"""
class GSScene(QGraphicsScene):
    """
    Scene(场景)
    """
    MY_QTIMER = QTimer()
    MY_SIGNAL = pyqtSignal()
    def __init__(self, parent=None):
        super(GSScene, self).__init__(parent)
        self.max_z_value = 0
        self.control_moveable = True

        self.MY_QTIMER.timeout.connect(self.MY_SIGNAL.emit)
        self.MY_QTIMER.setInterval(1000)

    def keyPressEvent(self, event):
        """快捷键--- 缩放控制器、选中所有控制器"""
        super(GSScene, self).keyPressEvent(event)
        if event.modifiers() & Qt.ControlModifier:
            if event.key() == 91:             # “ctrl + [” 键，缩小图标
                self.my_scale_ctrl('out')
            elif event.key() == 93:           # “ctrl + ]” 键，放大图标
                self.my_scale_ctrl('in')
            elif event.key() == 65:           # “ctrl + a” 键，选择全部控制器
                for item in self.items():
                    item.setSelected(1)
        # super(GSScene, self).keyPressEvent(event)





    def mousePressEvent(self, event):
        super(GSScene, self).mousePressEvent(event)
        if event.button() == Qt.LeftButton:
            if len(self.selectedItems())>0:
                current_z_value = self.max_z_value + 1

                self.selectedItems()[0].setZValue(current_z_value)
                self.max_z_value = current_z_value
                self.MY_QTIMER.start(100)

            for item in self.items():
                if item.MY_TYPE == 'CONTROL':
                    item.my_enable_highlight = 0
                    item.update()
            for item in self.selectedItems():
                item.my_enable_highlight = 1
                item.update()


    def mouseReleaseEvent(self, event):
        super(GSScene, self).mouseReleaseEvent(event)
        for c in self.items():
            if c.MY_TYPE == "CONTROL":
                c.use_pos[0] = c.pos().x()
                c.use_pos[1] = c.pos().y()
        self.MY_QTIMER.stop()




# def mouseMoveEvent(self, event):
            #     super(GSScene, self).mouseMoveEvent(event)
            # if self.bton == 1:
            #     self.MY_QTIMER.start(1)

    def my_scale_ctrl(self, zoom="in"):
        """缩放控制器"""
        for item in self.selectedItems():
            if zoom == "in":
                item.setScale(item.scale()*1.1)
            elif zoom == "out":
                item.setScale(item.scale()/1.1)



    def dragMoveEvent(self,event):
        super(GSScene, self).dragMoveEvent(event)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    view = QGraphicsView()
    scene = GSScene(view)
    view.show()
    sys.exit(app.exec_())