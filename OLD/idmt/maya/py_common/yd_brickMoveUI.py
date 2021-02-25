from PySide import QtGui, QtCore
import maya.cmds as mc
import maya.OpenMayaUI as mui
import shiboken
import functools



# all the BrickMover functions

# turn off or on move incrementals
def moveIncrementalOffOn():
    if mc.manipMoveContext('Move', q=True, snap=True):
        mc.manipMoveContext('Move', e=True, snap=False)

    else:
        mc.manipMoveContext('Move', e=True, snap=True)

# turn off or on move relative
def moveRelativeOffOn():
    if mc.manipMoveContext('Move', q=True, snapRelative=True):
        mc.manipMoveContext('Move', e=True, snapRelative=False)

    else:
        mc.manipMoveContext('Move', e=True, snapRelative=True)
    moveRelative.setCheckState(QtCore.Qt.Checked if mc.manipMoveContext('Move', q=True, snapRelative=True) else QtCore.Qt.Unchecked)

#set move incremental presets
def moveIncrementalPresets(value):
    if mc.manipMoveContext('Move', q=True, snapValue=True) == moveIncMulti.value() * value: 
        mc.manipMoveContext('Move', e=True, snap=not mc.manipMoveContext('Move', q=True, snap=True), snapValue=moveIncMulti.value() * value)
    else:
        mc.manipMoveContext('Move', e=True, snap=True, snapValue=moveIncMulti.value() * value)
    moveIncremental.setCheckState(QtCore.Qt.Checked if mc.manipMoveContext('Move', q=True, snap=True) else QtCore.Qt.Unchecked)


# turn off or on rotate incrementals
def rotateIncrementalOffOn():
    if mc.manipRotateContext('Rotate', q=True, snap=True):
        mc.manipRotateContext('Rotate', e=True, snap=False)

    else:
        mc.manipRotateContext('Rotate', e=True, snap=True)

# turn off or on rotate relative
def rotateRelativeOffOn():
    if mc.manipRotateContext('Rotate', q=True, snapRelative=True):
        mc.manipRotateContext('Rotate', e=True, snapRelative=False)

    else:
        mc.manipRotateContext('Rotate', e=True, snapRelative=True)
    
#set rotate incremental presets
def rotateIncrementalPresets(value):
    if mc.manipRotateContext('Rotate', q=True, snapValue=True) == value: 
        mc.manipRotateContext('Rotate', e=True, snap=not mc.manipRotateContext('Rotate', q=True, snap=True), snapValue=value)
    else:
        mc.manipRotateContext('Rotate', e=True, snap=True, snapValue=value)
    rotateIncremental.setCheckState(QtCore.Qt.Checked if mc.manipRotateContext('Rotate', q=True, snap=True) else QtCore.Qt.Unchecked)


# turn off or on rotate relative
#def rotateRelativeOffOn():        

#Align Object Tool
def alignObj():
    #This created prarent constraint with no offset
    prtCns = mc.parentConstraint()
    #This delete the parent constrint
    mc.delete(prtCns)

#Align Position Tool
def alignPoi():
    #This created point constraint with no offset
    poiCns = mc.pointConstraint()
    #This delete the point constrint
    mc.delete(poiCns)

#Align Rotation Tool
def alignRot():
    #This created orient constraint with no offset
    oriCns = mc.orientConstraint()
    #This delete the orient constrint
    mc.delete(oriCns)


#make the BrickMover UI
def getMayaWindow():
    pointer = mui.MQtUtil.mainWindow()
    return shiboken.wrapInstance(long(pointer), QtGui.QWidget)

def brickMover_UI():
    
    objectName = 'brickMoverMasterWin'
    
    #check to see if the UI already exists and if se, delete
    if mc.window('brickMoverMasterWin', exists = True):
        mc.deleteUI('brickMoverMasterWin', wnd = True)

    #create the window
    parent = getMayaWindow()
    window = QtGui.QMainWindow(parent)
    window.setObjectName(objectName)
    window.setWindowTitle('Brick Mover 1.0')
    #window.setMinimumSize(400, 150)
    #window.setMaximumSize(400, 150)

    #create the main widget
    mainWidget = QtGui.QWidget()
    window.setCentralWidget(mainWidget)

    #create our main vertical layout
    verticalLayout = QtGui.QVBoxLayout(mainWidget)

    #create font and assign
    fontBold = QtGui.QFont()
    fontBold.setPointSize(10)
    fontBold.setBold(True)

    #create checkBoxMoveIncremental
    checkBoxMoveInc = QtGui.QHBoxLayout()
    label = QtGui.QLabel('Move Incremental')
    checkBoxMoveInc.addWidget(label)   
    #add spacer
    spacer = QtGui.QSpacerItem(84,0)
    checkBoxMoveInc.addSpacerItem(spacer)
    global moveIncremental
    moveIncremental = QtGui.QCheckBox()
    moveIncremental.clicked.connect(moveIncrementalOffOn)
    checkBoxMoveInc.addWidget(moveIncremental)
    verticalLayout.addLayout(checkBoxMoveInc)

    #create moveIncrementalMultiply spinBox and chekcBox
    moveIncrementalMulti = QtGui.QHBoxLayout()
    label = QtGui.QLabel('Move Incremental Multiply')
    moveIncrementalMulti.addWidget(label)   
    global moveIncMulti
    moveIncMulti = QtGui.QSpinBox()
    moveIncMulti.setValue(1)
    moveIncMulti.setMinimum(1)
    moveIncrementalMulti.addWidget(moveIncMulti)
    verticalLayout.addLayout(moveIncrementalMulti)

    #create checkBoxMoveRelative
    checkBoxMoveRelative = QtGui.QHBoxLayout() 
    label = QtGui.QLabel('Move Relative')
    checkBoxMoveRelative.addWidget(label)   
    #add spacer
    spacer = QtGui.QSpacerItem(103,0)
    checkBoxMoveRelative.addSpacerItem(spacer)
    global moveRelative
    moveRelative = QtGui.QCheckBox()
    moveRelative.clicked.connect(moveRelativeOffOn)
    checkBoxMoveRelative.addWidget(moveRelative)
    verticalLayout.addLayout(checkBoxMoveRelative)

    #create label spacer
    presetMove = QtGui.QVBoxLayout()
    presetMoveLabel = QtGui.QLabel('Preset Incremental Move')
    presetMove.addWidget(presetMoveLabel)
    verticalLayout.addLayout(presetMove)

    #create the preset move incremental button
    presetMove = QtGui.QHBoxLayout()
    button080 = QtGui.QPushButton('0.80 One Stud')
    presetMove.addWidget(button080)
    button080.clicked.connect(functools.partial(moveIncrementalPresets, 0.8))
    button040 = QtGui.QPushButton('0.40 Half Stud')
    presetMove.addWidget(button040)
    button040.clicked.connect(functools.partial(moveIncrementalPresets, 0.4))
    verticalLayout.addLayout(presetMove)

    #create the preset move incremental button
    presetMove2 = QtGui.QHBoxLayout()
    button096 = QtGui.QPushButton('0.96 Brick Hight')
    presetMove2.addWidget(button096)
    button096.clicked.connect(functools.partial(moveIncrementalPresets, 0.96))
    button032 = QtGui.QPushButton('0.32 Plate Hight')
    presetMove2.addWidget(button032)
    button032.clicked.connect(functools.partial(moveIncrementalPresets, 0.32))
    verticalLayout.addLayout(presetMove2)

    #create checkBox for rotate Incremental
    checkBoxRotateInc = QtGui.QHBoxLayout()
    label = QtGui.QLabel('Rotate Incremental')
    checkBoxRotateInc.addWidget(label)   
    #add spacer
    spacer = QtGui.QSpacerItem(79,0)
    checkBoxRotateInc.addSpacerItem(spacer)
    global rotateIncremental
    rotateIncremental = QtGui.QCheckBox()
    rotateIncremental.clicked.connect(rotateIncrementalOffOn)
    checkBoxRotateInc.addWidget(rotateIncremental)
    verticalLayout.addLayout(checkBoxRotateInc)

    #create checkBox for rotate Relative
    checkBoxRotateRelative = QtGui.QHBoxLayout()
    label = QtGui.QLabel('Rotate Relative')
    checkBoxRotateRelative.addWidget(label)   
    #add spacer
    spacer = QtGui.QSpacerItem(97,0)
    checkBoxRotateRelative.addSpacerItem(spacer)
    rotateRelative = QtGui.QCheckBox()
    rotateRelative.clicked.connect(rotateRelativeOffOn)
    checkBoxRotateRelative.addWidget(rotateRelative)
    verticalLayout.addLayout(checkBoxRotateRelative)

    #create label spacer
    presetDegrees = QtGui.QVBoxLayout()
    presetDegreesLabel = QtGui.QLabel('Preset Incremental Degrees')
    presetDegrees.addWidget(presetDegreesLabel)
    verticalLayout.addLayout(presetDegrees)

    #create the preset rotate incremental button
    presetRotate = QtGui.QHBoxLayout()
    button90 = QtGui.QPushButton('90')
    button90.clicked.connect(functools.partial(rotateIncrementalPresets, 90))
    presetRotate.addWidget(button90)
    button45 = QtGui.QPushButton('45')
    button45.clicked.connect(functools.partial(rotateIncrementalPresets, 45))
    presetRotate.addWidget(button45)
    verticalLayout.addLayout(presetRotate)

    #create labels for rotateOption and rotateDegrees
    rotateHelp = QtGui.QHBoxLayout()
    rotateOptionLabel = QtGui.QLabel('Rot Option')
    rotateDegreesLabel = QtGui.QLabel('Inc Degrees')
    rotateHelp.addWidget(rotateOptionLabel)
    rotateHelp.addWidget(rotateDegreesLabel)
    verticalLayout.addLayout(rotateHelp)
    
    #create comboBox for rotate option and spinBox for degrees
    rotateHelp2 = QtGui.QHBoxLayout()
    rotateOptionComboBox = QtGui.QComboBox()
    rotateOptionComboBox.addItems(['World', 'Local', 'Gimbel'])
    rotateHelp2.addWidget(rotateOptionComboBox)
    rotateDegreesSpinBox = QtGui.QDoubleSpinBox()
    rotateHelp2.addWidget(rotateDegreesSpinBox)
    verticalLayout.addLayout(rotateHelp2)

    #create spacer for Rotate helpers
    rotateHelper = QtGui.QVBoxLayout()
    rotateHelperLabel = QtGui.QLabel('Rotate Helper')
    rotateHelperLabel.setFont(fontBold)
    rotateHelper.addWidget(rotateHelperLabel)
    verticalLayout.addLayout(rotateHelper)

    #create the preset incremental button
    positionRotate = QtGui.QHBoxLayout()
    buttonPlusX = QtGui.QPushButton('+X')
    positionRotate.addWidget(buttonPlusX)
    buttonPlusY = QtGui.QPushButton('+Y')
    positionRotate.addWidget(buttonPlusY)
    buttonPlusZ = QtGui.QPushButton('+Z')
    positionRotate.addWidget(buttonPlusZ)
    verticalLayout.addLayout(positionRotate)

    #create the preset incremental button
    negativeRotate = QtGui.QHBoxLayout()
    buttonMinusX = QtGui.QPushButton('-X')
    negativeRotate.addWidget(buttonMinusX)
    buttonMinusY = QtGui.QPushButton('-Y')
    negativeRotate.addWidget(buttonMinusY)
    buttonMinusZ = QtGui.QPushButton('-Z')
    negativeRotate.addWidget(buttonMinusZ)
    verticalLayout.addLayout(negativeRotate)

    #create align brick buttons
    alignBricks = QtGui.QVBoxLayout()
    alignBricksLabel = QtGui.QLabel('Align Bricks')
    alignBricksLabel.setFont(fontBold)
    alignBricks.addWidget(alignBricksLabel)
    alignBrick = QtGui.QPushButton('align Brick')
    alignBricks.addWidget(alignBrick)
    alignBrick.clicked.connect(alignObj)
    alingTranslate = QtGui.QPushButton('align Brick Translate Only')
    alignBricks.addWidget(alingTranslate)
    alingTranslate.clicked.connect(alignPoi)
    alignRotate = QtGui.QPushButton('align Brick Rotate Only')
    alignBricks.addWidget(alignRotate)
    alignRotate.clicked.connect(alignRot)
    verticalLayout.addLayout(alignBricks)


    #Show the window
    window.show()
    
brickMover_UI()  