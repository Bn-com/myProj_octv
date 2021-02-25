from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
sys.path.append(r'C:\Python26x64\Lib\site-packages\PyQt4\examples\animation\animatedtiles')
import animatedtiles_rc

class View(QGraphicsView):
    def resizeEvent(self, event):
        super(View, self).resizeEvent(event)
        self.fitInView(self.sceneRect(), Qt.KeepAspectRatio)
        
class Button(QGraphicsWidget):
    pressed = pyqtSignal()
    def __init__(self, pixmap, parent=None):
        super(Button, self).__init__(parent)
        self._pix = pixmap
            
    def paint(self, painter, option, widget):
        down = option.state & QStyle.State_Sunken
        r = self.boundingRect()

        grad = QLinearGradient(r.topLeft(), r.bottomRight())
        painter.setPen(Qt.darkGray)
        painter.setBrush(grad)
        painter.drawEllipse(r)
        
    def mousePressEvent(self, ev):
        self.pressed.emit()
        self.update()        

class Pixmap(QObject):
    def __init__(self, pix):
        super(Pixmap, self).__init__()
        self.pixmap_item = QGraphicsPixmapItem(pix)
    def _set_pos(self, pos):
        self.pixmap_item.setPos(pos)
    pos = pyqtProperty(QPointF, fset=_set_pos)

        
if __name__ == '__main__':
    import sys
    import math

    app = QApplication(sys.argv)
    kineticPix = QPixmap(':/images/kinetic.png')
    scene = QGraphicsScene(-350, -350, 700, 700)

    items = []
    for i in range(64):
        item = Pixmap(kineticPix)
        item.pixmap_item.setOffset(-kineticPix.width() / 2,
                -kineticPix.height() / 2)
        items.append(item)
        scene.addItem(item.pixmap_item)

    # Buttons.
    tiledButton = Button(kineticPix)
    tiledButton.scale(0.75, 0.75)
    tiledButton.setPos(200, -200)
    scene.addItem(tiledButton)


    # States.
    rootState = QState()
    tiledState = QState(rootState)
    centeredState = QState(rootState)

    # Values.
    for i, item in enumerate(items):
        # Tiled.
        tiledState.assignProperty(item, 'pos',
                QPointF(((i % 8) - 4) * kineticPix.width() + kineticPix.width() / 2,
                        ((i // 8) - 4) * kineticPix.height() + kineticPix.height() / 2))


    
    # Ui.
    view = View(scene)
    view.show()

    states = QStateMachine()
    states.addState(rootState)
    states.setInitialState(rootState)
    rootState.setInitialState(centeredState)

    group = QParallelAnimationGroup()
    for i, item in enumerate(items):
        anim = QPropertyAnimation(item, 'pos')
        anim.setDuration(750 + i * 25)
        anim.setEasingCurve(QEasingCurve.InOutBack)
        group.addAnimation(anim)


    trans = rootState.addTransition(tiledButton.pressed, tiledState)
    trans.addAnimation(group)

    timer = QTimer()
    timer.start(125)
    timer.setSingleShot(True)

    states.start()    
    sys.exit(app.exec_())
