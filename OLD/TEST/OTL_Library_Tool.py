import sys
#import hou
from PySide.QtCore import *
#from PySide.QtWidgets import *
from PySide.QtGui import *

class effectType(QWidget):
    
    def __init__(self):
        QWidget.__init__(self)
        
        self.setWindowTitle(u'OTL 库')
        self.setMinimumSize(450,400)
        #self.resize(self.sizeHint())
        self.layout=QVBoxLayout()
        self.tabWidget = QTabWidget()
        self.layout.addWidget(self.tabWidget)
        self.setLayout(self.layout)
        self.effectTypes=[u'火',
                          u'水',
                          u'烟',
                          u'灰尘',
                          u'爆炸'
                          ]
        for i in range(0,len(self.effectTypes)):
            self.tab=QWidget()
            self.tabLayout=QVBoxLayout()
            
            self.tab.setLayout(self.tabLayout)

            self.tabWidget.addTab(self.tab,self.effectTypes[i])

            try:
                self.tabWidget.setStyleSheet("""QTabBar::tab {min-width: 60px;min-height: 30px;font: bold; font-size:17px}""")
            except:
                pass 
            self.formLayout=QFormLayout()
            self.formLayout.setObjectName('tabForm'+str(i))
            self.tabLayout.addLayout(self.formLayout)

            self.CreateQC('tabQC'+str(i))            
            self.formLayout.addRow(u'项目:',self.QC)
            self.formLayout.addRow(self.childFormLayout)
            if self.effectTypes[i]==u'火':                
                self.CreateFireChildWidget('tabQC'+str(i))
            


    def CreateQC(self,TypName):                
        self.projectNames=[u'顺溜',
                          u'玩偶奇兵',
                          u'乐高',
                          u'Maya Bee',
                          u'忍者'
                          ]
        self.QC=QComboBox(self)
        self.QC.setObjectName(TypName)
        self.QC.setMinimumSize(350,30)
        self.QC.addItems(self.projectNames)
        self.childFormLayout=QFormLayout()
        try:
            self.QC.setFont(QFont('',11))
            self.QC.setStyleSheet("""font-size:15px;}""")
        except:
            pass
            #self.myPrint()

        
    def CreateFireChildWidget(self,TypName):
        self.childWidget=''
        self.childWidgetNames=[]
        for i in range(0,len(self.projectNames)):
            self.childWidget=QWidget()
            self.childFormLayout.addRow(self.childWidget)
            self.childWidget.setObjectName(self.QC.objectName()+'_childWidget'+str(i))
            self.childWidgetNames.append(self.childWidget.objectName())
            self.childFormLayout.addRow(self.childWidget)
            self.butformLayout=QFormLayout()
            self.childWidget.setLayout(self.butformLayout)
            self.childFormLayout.addRow(self.butformLayout)
            if self.childWidgetNames[i][-1]=='0':
                self.childWidget.setVisible(1)
            else:
                self.childWidget.setVisible(0)
            self.CreateFireBut_1(self.projectNames[i])
            self.CreateFireBut_2(self.projectNames[i])
        print self.childWidgetNames
            
    def CreateFireBut_1(self,projectName):
        self.currentFireLayout=''
        self.fireButs=[]
        self.fireTypes=[u'大火',
                        u'中火',
                        u'小火',
                        u'火灾',
                        u'烛火',
                        u'炉火',
                        u'天火']
        self.icon_paths=['M:\leo369\images\pyside_test\images\Chrysanthemum.jpg',
                         'M:\leo369\images\pyside_test\images\Desert.jpg',
                         'M:\leo369\images\pyside_test\images\Hydrangeas.jpg',
                         'M:\leo369\images\pyside_test\images\Jellyfish.jpg',
                         'M:\leo369\images\pyside_test\images\Koala.jpg',
                         'M:\leo369\images\pyside_test\images\Lighthouse.jpg',
                         'M:\leo369\images\pyside_test\images\Penguins.jpg']
        for i in range(0,len(self.fireTypes)):
            if i%3==0:
                self.currentFireLayout=QHBoxLayout()
                self.butformLayout.addRow(self.currentFireLayout)
                
            self.fireBut=QPushButton(self.fireTypes[i])
            self.fireBut.setObjectName(projectName+'_fireBut'+str(i))
            self.fireBut.setIcon(QIcon(self.icon_paths[i]))
            self.fireBut.setIconSize(QSize(100,80))
            self.fireBut.setMinimumSize(135,80)
            self.fireBut.setMaximumSize(135,80)
            self.fireBut.setFlat(1)
            self.currentFireLayout.addWidget(self.fireBut)
            print self.fireBut.objectName()
            #self.fireBut.clicked.connect(self.fireButCmd)

    def CreateFireBut_2(self,projectName):
        self.currentFireLayout1=''
        self.fireButs1=[]
        self.fireTypes1=[u'大火1',
                        u'中火1',
                        u'小火1',
                        u'火灾1',
                        u'烛火1',
                        u'炉火1',
                        u'天火1']
        for i in range(0,len(self.fireTypes1)):
            if i%3==0:
                self.currentFireLayout1=QHBoxLayout()
                self.butformLayout.addRow(self.currentFireLayout1)
                
            self.fireBut1=QPushButton(self.fireTypes[i])
            self.fireBut1.setObjectName(projectName+'_fireBut'+str(i))
            #self.fireBut1.setIcon(QIcon(self.icon_paths[i]))
            #self.fireBut1.setIconSize(QSize(100,80))
            self.fireBut1.setMinimumSize(135,80)
            self.fireBut1.setMaximumSize(135,80)
            #self.fireBut1.setFlat(1)
            self.currentFireLayout1.addWidget(self.fireBut)
            print self.fireBut1.objectName()
            #self.fireBut1.clicked.connect(self.fireButCmd)

    def run(self):
        self.show()
        
app=effectType()
app.run()
                