from PyQt4 import QtCore, QtGui

import animatedtiles


# PyQt doesn't support deriving from more than one wrapped class so we use
# composition and delegate the property.
class Pixmap(QtCore.QObject):
    def __init__(self, pix):
        super(Pixmap, self).__init__()

        self.pixmap_item = QtGui.QGraphicsPixmapItem(pix)
        
        
    def _set_pos(self, pos):
        self.pixmap_item.setPos(pos)
        
        
    def _set_scale(self, sc):
        self.pixmap_item.setScale(0.9)            

    pos = QtCore.pyqtProperty(QtCore.QPointF, fset=_set_pos)
    sc = QtCore.pyqtProperty(QtCore.QSizeF, fset=_set_scale)


#    self.pushButton = QtGui.QPushButton()
#    QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), exit())

    

class Button(QtGui.QGraphicsWidget):
    pressed = QtCore.pyqtSignal()

    def __init__(self, pix, parent=None):
        super(Button, self).__init__(parent)

        self._pix = pix

        self.setAcceptHoverEvents(True)
        self.setCacheMode(QtGui.QGraphicsItem.DeviceCoordinateCache)

    def boundingRect(self):
        return QtCore.QRectF(-65, -65, 130, 130)

    def shape(self):
        path = QtGui.QPainterPath()
        path.addEllipse(self.boundingRect())

        return path

    def paint(self, painter, option, widget):
        down = option.state & QtGui.QStyle.State_Sunken
        r = self.boundingRect()

        grad = QtGui.QLinearGradient(r.topLeft(), r.bottomRight())
        if option.state & QtGui.QStyle.State_MouseOver:
            color_0 = QtCore.Qt.white
        else:
            color_0 = QtCore.Qt.lightGray

        color_1 = QtCore.Qt.darkGray

        if down:
            color_0, color_1 = color_1, color_0

        grad.setColorAt(0, color_0)
        grad.setColorAt(1, color_1)

        painter.setPen(QtCore.Qt.darkGray)
        painter.setBrush(grad)
        painter.drawEllipse(r)

        color_0 = QtCore.Qt.darkGray
        color_1 = QtCore.Qt.lightGray

        if down:
            color_0, color_1 = color_1, color_0

        grad.setColorAt(0, color_0)
        grad.setColorAt(1, color_1)

        painter.setPen(QtCore.Qt.NoPen)
        painter.setBrush(grad)

        if down:
            painter.translate(2, 2)

        painter.drawEllipse(r.adjusted(5, 5, -5, -5))
        painter.drawPixmap(-self._pix.width() / 2, -self._pix.height() / 2,
                self._pix)



    def mousePressEvent(self, ev):

        self.update()

    def mouseReleaseEvent(self, ev):
        self.pressed.emit()
        self.update()
        





class View(QtGui.QGraphicsView):
    def resizeEvent(self, event):
        super(View, self).resizeEvent(event)
        self.fitInView(self.sceneRect(), QtCore.Qt.KeepAspectRatio)


if __name__ == '__main__':

    import sys
    import math

    app = QtGui.QApplication(sys.argv)

    kineticPix = QtGui.QPixmap(':/images/gun001.jpg')
    bgPix = QtGui.QPixmap(':/images/StarWar.jpg')

    scene = QtGui.QGraphicsScene(0, 0, 1024, 610)
    
    QtGui.QPushButton()    
    items = []
    for i in range(12):
        item = Pixmap(kineticPix)
        item.pixmap_item.setOffset(300,500)
        item.pixmap_item.setZValue(i)
        
        items.append(item)
        
        scene.addItem(item.pixmap_item)

    # Buttons.
    tiledButton = Button(QtGui.QPixmap(':/images/tile.png'), None)
    tiledButton.setPos(900, 500)
    
    scene.addItem(tiledButton)
    tiledButton.setZValue(50)

    # States.
    tiledState = QtCore.QState()

    # Values.
    for i, item in enumerate(items):
        # Tiled.
        tiledState.assignProperty(item, 'pos',
                QtCore.QPointF(((i % 4) -2) * kineticPix.width() ,
                        ((i // 4) -2) * kineticPix.height()))
                        
        tiledState.assignProperty(item, 'sc' , QtCore.QSizeF(0.9,0.9))
    # Ui.
    view = View(scene)
    view.setWindowTitle("Pluto_Gun")
    view.setViewportUpdateMode(QtGui.QGraphicsView.BoundingRectViewportUpdate)
    view.setBackgroundBrush(QtGui.QBrush(bgPix))
    view.setCacheMode(QtGui.QGraphicsView.CacheBackground)
    view.setRenderHints(QtGui.QPainter.Antialiasing | QtGui.QPainter.SmoothPixmapTransform)
    view.show()

    states = QtCore.QStateMachine()
    states.addState(tiledState)
    states.setInitialState(tiledState)
    tiledState.setInitialState(tiledState)

    group = QtCore.QParallelAnimationGroup()
    for i, item in enumerate(items):
        anim = QtCore.QPropertyAnimation(item, 'pos')
        anim.setDuration(750 + i * 225)
        anim.setEasingCurve(QtCore.QEasingCurve.InOutBack)
        group.addAnimation(anim)


    trans = tiledState.addTransition(tiledButton.pressed, tiledState)
    trans.addAnimation(group)


    timer = QtCore.QTimer()
    timer.start(1)
    timer.setSingleShot(True)
    trans = tiledState.addTransition(timer.timeout, tiledState)
    trans.addAnimation(group)

    states.start()

    sys.exit(app.exec_())
