from PyQt4 import QtCore, QtGui
from PyQt4.uic import loadUi
import sys
sys.path.append(r'F:\my_python_folder\PlutoGun')
import image_qrc

class Pixmap(QtCore.QObject):
    def __init__(self, pix):
        super(Pixmap, self).__init__()
        self.pixmap_item = QtGui.QGraphicsPixmapItem(pix)
 
    def _set_pos(self, pos):
        self.pixmap_item.setPos(pos) 
    pos = QtCore.pyqtProperty(QtCore.QPointF, fset=_set_pos)




app = QtGui.QApplication(sys.argv)
#win = loadUi("win.myuis",QtGui.QMainWindow())
win = QtGui.QMainWindow()

gunPix = QtGui.QPixmap(':/images/gun001.jpg')
bgPix = QtGui.QPixmap(':/images/grid.jpg')
#bgPix = QtGui.QPixmap(':/images/StarWar.jpg')

scene = QtGui.QGraphicsScene(0, 0, 1024, 610)
#   backGround
#scene.addItem(QtGui.QGraphicsPixmapItem(bgPix))
items = []

for i in range(5):
    item = Pixmap(gunPix)
    item.pixmap_item.setOffset(300,300)
    item.pixmap_item.setZValue(i)
    
    items.append(item)
    
    scene.addItem(item.pixmap_item)





tiledState = QtCore.QState()

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



tiledButton = QtGui.QPixmap(':/images/tile.png')
tiledButton.setPos(900, 500)
trans = tiledState.addTransition(tiledButton.pressed, tiledState)
trans.addAnimation(group)


timer = QtCore.QTimer()
timer.start(1)
timer.setSingleShot(True)
#trans = tiledState.addTransition(timer.timeout, tiledState)
#trans.addAnimation(group)

states.start()

'''

'''






wd = QtGui.QGraphicsView(scene)
wd.setBackgroundBrush(QtGui.QBrush(bgPix))
wd.setCacheMode(QtGui.QGraphicsView.CacheBackground)   
win.setCentralWidget(wd)
win.show()
sys.exit(app.exec_())






