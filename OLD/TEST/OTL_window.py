# -*- coding: utf-8 -*-
import sys
#import hou
from PySide.QtCore import *
#from PySide2.QtWidgets import *
from PySide.QtGui import *

class effectType(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle(u'OTL 库')
        self.setMinimumSize(450,400)

        self.layout=QVBoxLayout()
        self.tabWidget = QTabWidget()
        self.layout.addWidget(self.tabWidget)
        self.setLayout(self.layout)
        self.projectNames=[u'顺溜',
                           u'玩偶奇兵',
                           u'乐高',
                           u'Maya Bee',
                           u'忍者']
        for i in range(0,len(self.projectNames)):
            self.tab=QWidget()
            self.tabLayout=QVBoxLayout()
            
            self.tab.setLayout(self.tabLayout)

            self.tabWidget.addTab(self.tab,self.projectNames[i])

            try:
                self.tabWidget.setStyleSheet("""QTabBar::tab {min-width: 100px;min-height: 30px;font: bold; font-size:17px}""")
            except:
                pass
            if self.projectNames[i]==u'顺溜':
                self.shunliu_formLayout=QFormLayout()
                self.tabLayout.addLayout(self.shunliu_formLayout)
                self.shunliu_formLayout.setObjectName(self.projectNames[i]+'_formLayout')
                self.CreateShunliuQC(self.projectNames[i])
        
                self.shunliu_formLayout.addRow(u'&OTL 类型:',self.shunliuQC)
                        
                self.CreateShunliuFireBut()
                self.CreateShunliuWaterBut()
                self.CreateShunliuSomkeBut()
                self.CreateShunliuDustBut()
                self.CreateShunliuBlastBut()
                self.shunliu_formLayout.addRow(self.shunliuFireButWidget)
                self.shunliu_formLayout.addRow(self.shunliuWaterButWidget)
                self.shunliu_formLayout.addRow(self.shunliuSomkeButWidget)
                self.shunliu_formLayout.addRow(self.shunliuDustButWidget)
                self.shunliu_formLayout.addRow(self.shunliuBlastButWidget)
                
                self.shunliuFireButWidget.setVisible(1)
                self.shunliuWaterButWidget.setVisible(0)        
                self.shunliuSomkeButWidget.setVisible(0)
                self.shunliuDustButWidget.setVisible(0)
                self.shunliuBlastButWidget.setVisible(0)
                self.shunliuQC.currentIndexChanged.connect(self.shunliu_on_changed)

            elif self.projectNames[i]==u'玩偶奇兵':
                self.miniTiger_formLayout=QFormLayout()
                self.tabLayout.addLayout(self.miniTiger_formLayout)
                self.miniTiger_formLayout.setObjectName(self.projectNames[i]+'_formLayout')
                self.CreateMiniTigerQC(self.projectNames[i])
        
                self.miniTiger_formLayout.addRow(u'&OTL 类型:',self.miniTigerQC)
                        
                self.CreateMiniTigerFireBut()
                self.CreateMiniTigerWaterBut()
                self.CreateMiniTigerSomkeBut()
                self.CreateMiniTigerDustBut()
                self.CreateMiniTigerBlastBut()
                self.miniTiger_formLayout.addRow(self.miniTigerFireButWidget)
                self.miniTiger_formLayout.addRow(self.miniTigerWaterButWidget)
                self.miniTiger_formLayout.addRow(self.miniTigerSomkeButWidget)
                self.miniTiger_formLayout.addRow(self.miniTigerDustButWidget)
                self.miniTiger_formLayout.addRow(self.miniTigerBlastButWidget)
                
                self.miniTigerFireButWidget.setVisible(1)
                self.miniTigerWaterButWidget.setVisible(0)        
                self.miniTigerSomkeButWidget.setVisible(0)
                self.miniTigerDustButWidget.setVisible(0)
                self.miniTigerBlastButWidget.setVisible(0)
                self.miniTigerQC.currentIndexChanged.connect(self.miniTiger_on_changed)

            elif self.projectNames[i]==u'乐高':
                self.Lego_formLayout=QFormLayout()
                self.tabLayout.addLayout(self.Lego_formLayout)
                self.Lego_formLayout.setObjectName(self.projectNames[i]+'_formLayout')
                self.CreateLegoQC(self.projectNames[i])

                self.Lego_formLayout.addRow(u'&OTL 类型:',self.LegoQC)

                #print self.Lego_formLayout.objectName()
                #print self.LegoQC.objectName()

                self.CreateLegoFireBut()
                self.CreateLegoWaterBut()
                self.CreateLegoSomkeBut()
                self.CreateLegoDustBut()
                self.CreateLegoBlastBut()
                self.Lego_formLayout.addRow(self.LegoFireButWidget)
                self.Lego_formLayout.addRow(self.LegoWaterButWidget)
                self.Lego_formLayout.addRow(self.LegoSomkeButWidget)
                self.Lego_formLayout.addRow(self.LegoDustButWidget)
                self.Lego_formLayout.addRow(self.LegoBlastButWidget)

                self.LegoFireButWidget.setVisible(1)
                self.LegoWaterButWidget.setVisible(0)
                self.LegoSomkeButWidget.setVisible(0)
                self.LegoDustButWidget.setVisible(0)
                self.LegoBlastButWidget.setVisible(0)
                self.LegoQC.currentIndexChanged.connect(self.Lego_on_changed)

            elif self.projectNames[i]==u'Maya Bee':
                self.MayaBee_formLayout=QFormLayout()
                self.tabLayout.addLayout(self.MayaBee_formLayout)
                self.MayaBee_formLayout.setObjectName(self.projectNames[i]+'_formLayout')
                self.CreateMayaBeeQC(self.projectNames[i])

                self.MayaBee_formLayout.addRow(u'&OTL 类型:',self.MayaBeeQC)

                #print self.MayaBee_formLayout.objectName()
                #print self.MayaBeeQC.objectName()

                self.CreateMayaBeeFireBut()
                self.CreateMayaBeeWaterBut()
                self.CreateMayaBeeSomkeBut()
                self.CreateMayaBeeDustBut()
                self.CreateMayaBeeBlastBut()
                self.MayaBee_formLayout.addRow(self.MayaBeeFireButWidget)
                self.MayaBee_formLayout.addRow(self.MayaBeeWaterButWidget)
                self.MayaBee_formLayout.addRow(self.MayaBeeSomkeButWidget)
                self.MayaBee_formLayout.addRow(self.MayaBeeDustButWidget)
                self.MayaBee_formLayout.addRow(self.MayaBeeBlastButWidget)

                self.MayaBeeFireButWidget.setVisible(1)
                self.MayaBeeWaterButWidget.setVisible(0)
                self.MayaBeeSomkeButWidget.setVisible(0)
                self.MayaBeeDustButWidget.setVisible(0)
                self.MayaBeeBlastButWidget.setVisible(0)
                self.MayaBeeQC.currentIndexChanged.connect(self.MayaBee_on_changed)

            elif self.projectNames[i]==u'忍者':
                self.Ninjago_formLayout=QFormLayout()
                self.tabLayout.addLayout(self.Ninjago_formLayout)
                self.Ninjago_formLayout.setObjectName(self.projectNames[i]+'_formLayout')
                self.CreateNinjagoQC(self.projectNames[i])

                self.Ninjago_formLayout.addRow(u'&OTL 类型:',self.NinjagoQC)

                print self.Ninjago_formLayout.objectName()
                print self.NinjagoQC.objectName()

                self.CreateNinjagoFireBut()
                self.CreateNinjagoWaterBut()
                self.CreateNinjagoSomkeBut()
                self.CreateNinjagoDustBut()
                self.CreateNinjagoBlastBut()
                self.Ninjago_formLayout.addRow(self.NinjagoFireButWidget)
                self.Ninjago_formLayout.addRow(self.NinjagoWaterButWidget)
                self.Ninjago_formLayout.addRow(self.NinjagoSomkeButWidget)
                self.Ninjago_formLayout.addRow(self.NinjagoDustButWidget)
                self.Ninjago_formLayout.addRow(self.NinjagoBlastButWidget)

                self.NinjagoFireButWidget.setVisible(1)
                self.NinjagoWaterButWidget.setVisible(0)
                self.NinjagoSomkeButWidget.setVisible(0)
                self.NinjagoDustButWidget.setVisible(0)
                self.NinjagoBlastButWidget.setVisible(0)
                self.NinjagoQC.currentIndexChanged.connect(self.Ninjago_on_changed)


        #self.setLayout(self.layout)
        
        
#-------------------Shunliu------------------------------------------------------------------
    def CreateShunliuQC(self,projectName):
        self.ShunliuEffectTypes=[u'火',
                                 u'水',
                                 u'烟',
                                 u'灰尘',
                                 u'爆炸']
        self.shunliuQC=QComboBox(self)
        self.shunliuQC.setObjectName(projectName+'_QC')
        self.shunliuQC.setMinimumSize(400,30)
        self.shunliuQC.addItems(self.ShunliuEffectTypes)
        try:
            self.shunliuQC.setFont(QFont('',11))
            self.shunliuQC.setStyleSheet("""font-size:15px;}""")
        except:
            pass                   
                        

    def CreateShunliuFireBut(self):
        self.shunliuFireButWidget=QWidget()
        self.shunliuFireFormLayout=QFormLayout()
        self.shunliuFireButWidget.setLayout(self.shunliuFireFormLayout)    
        self.shunliuCurrentFireLayout=''
        self.shunliuFireButs=[]
        self.shunliuFireTypes=[u'大火',
                               u'中火',
                               u'小火',
                               u'火灾',
                               u'烛火',
                               u'炉火',
                               u'天火']
        self.shunliuFireIcon_paths=['M:\leo369\images\pyside_test\images\Chrysanthemum.jpg',
                                    'M:\leo369\images\pyside_test\images\Desert.jpg',
                                    'M:\leo369\images\pyside_test\images\Hydrangeas.jpg',
                                    'M:\leo369\images\pyside_test\images\Jellyfish.jpg',
                                    'M:\leo369\images\pyside_test\images\Koala.jpg',
                                    'M:\leo369\images\pyside_test\images\Lighthouse.jpg',
                                    'M:\leo369\images\pyside_test\images\Penguins.jpg']
        for i in range(0,len(self.shunliuFireTypes)):
            if i%3==0:
                self.shunliuCurrentFireLayout=QHBoxLayout()
                self.shunliuFireFormLayout.addRow(self.shunliuCurrentFireLayout)
                
            self.shunliuFireBut=QPushButton(self.shunliuFireTypes[i])
            self.shunliuFireBut.setObjectName('shunliuFireBut'+str(i))
            self.shunliuFireBut.setIcon(QIcon(self.shunliuFireIcon_paths[i]))
            self.shunliuFireBut.setIconSize(QSize(100,80))
            self.shunliuFireBut.setMinimumSize(135,80)
            self.shunliuFireBut.setMaximumSize(135,80)
            self.shunliuFireBut.setFlat(1)
            self.shunliuCurrentFireLayout.addWidget(self.shunliuFireBut)

            self.shunliuFireBut.clicked.connect(self.shunliuFireButCmd)
                #self.buts_layout.addSpacing(10)

    def CreateShunliuWaterBut(self):
        self.shunliuWaterButWidget=QWidget()
        self.shunliuWaterFormLayout=QFormLayout()
        self.shunliuWaterButWidget.setLayout(self.shunliuWaterFormLayout) 
        self.shunliuCurrentWaterLayout=''
        
        self.shunliuWaterTypes=[u'酒水',
                                u'洪水',
                                u'海洋',
                                u'海啸',
                                u'水花',
                                u'洗澡',
                                u'漩涡',
                                u'倒水']               

        for i in range(0,len(self.shunliuWaterTypes)):
            if i%3==0:
                self.shunliuCurrentWaterLayout=QHBoxLayout()
                self.shunliuWaterFormLayout.addRow(self.shunliuCurrentWaterLayout)

            self.shunliuWaterBut=QPushButton(self.shunliuWaterTypes[i],self)
            self.shunliuWaterBut.setObjectName('shunliuWaterBut'+str(i))
            self.shunliuWaterBut.setMinimumSize(135,80)
            self.shunliuWaterBut.setMaximumSize(135,80)
            self.shunliuWaterBut.setFlat(1)
            self.shunliuCurrentWaterLayout.addWidget(self.shunliuWaterBut)

            self.shunliuWaterBut.clicked.connect(self.shunliuWaterButCmd)


    def CreateShunliuSomkeBut(self):
        self.shunliuSomkeButWidget=QWidget()
        self.shunliuSomekFormLayout=QFormLayout()
        self.shunliuSomkeButWidget.setLayout(self.shunliuSomekFormLayout)
        self.shunliuCurrentSomkeLayout=''

        self.shunliuSomkeTypes=[u'轻烟',
                                u'浓烟']

        for i in range(0,len(self.shunliuSomkeTypes)):
            if i%3==0:
                self.shunliuCurrentSomkeLayout=QHBoxLayout()
                self.shunliuSomekFormLayout.addRow(self.shunliuCurrentSomkeLayout)

            self.shunliuSomkeBut=QPushButton(self.shunliuSomkeTypes[i],self)
            self.shunliuSomkeBut.setObjectName('shunliuSomkeBut'+str(i))
            self.shunliuSomkeBut.setMinimumSize(135,80)
            self.shunliuSomkeBut.setMaximumSize(135,80)
            self.shunliuSomkeBut.setFlat(1)
            self.shunliuCurrentSomkeLayout.addWidget(self.shunliuSomkeBut)

            self.shunliuSomkeBut.clicked.connect(self.shunliuSomkeButCmd)

    def CreateShunliuDustBut(self):
        self.shunliuDustButWidget=QWidget()
        self.shunliuDustFormLayout=QFormLayout()
        self.shunliuDustButWidget.setLayout(self.shunliuDustFormLayout)
        self.shunliuCurrentDustLayout=''

        self.shunliuDustTypes=[u'满天扬沙',
                               u'风沙',
                               u'沙尘暴'
                               ]
        for i in range(0,len(self.shunliuDustTypes)):
            if i%3==0:
                self.shunliuCurrentDustLayout=QHBoxLayout()
                self.shunliuDustFormLayout.addRow(self.shunliuCurrentDustLayout)

            self.shunliuDustBut=QPushButton(self.shunliuDustTypes[i],self)
            self.shunliuDustBut.setObjectName('shunliuDustBut'+str(i))
            self.shunliuDustBut.setMinimumSize(135,80)
            self.shunliuDustBut.setMaximumSize(135,80)
            self.shunliuDustBut.setFlat(1)
            self.shunliuCurrentDustLayout.addWidget(self.shunliuDustBut)

            self.shunliuDustBut.clicked.connect(self.shunliuDustButCmd)
            
    def CreateShunliuBlastBut(self):
        self.shunliuBlastButWidget=QWidget()
        self.shunliuBlastFormLayout=QFormLayout()
        self.shunliuBlastButWidget.setLayout(self.shunliuBlastFormLayout)
        self.shunliuCurrentBlastLayout=''

        self.shunliuBlastTypes=[u'核弹爆炸',
                                u'炸弹爆炸',
                                u'子弹爆炸',
                                u'汽油爆炸']
        for i in range(0,len(self.shunliuBlastTypes)):
            if i%3==0:
                self.shunliuCurrentBlastLayout=QHBoxLayout()
                self.shunliuBlastFormLayout.addRow(self.shunliuCurrentBlastLayout)

            self.shunliuBlastBut=QPushButton(self.shunliuBlastTypes[i],self)
            self.shunliuBlastBut.setObjectName('shunliuBlastBut'+str(i))
            self.shunliuBlastBut.setMinimumSize(135,80)
            self.shunliuBlastBut.setMaximumSize(135,80)
            self.shunliuBlastBut.setFlat(1)
            self.shunliuCurrentBlastLayout.addWidget(self.shunliuBlastBut)

            self.shunliuBlastBut.clicked.connect(self.shunliuBlastButCmd)

    def shunliu_on_changed(self,index):
        if index==0:
            self.shunliuFireButWidget.setVisible(1)
            self.shunliuWaterButWidget.setVisible(0)
            self.shunliuSomkeButWidget.setVisible(0)
            self.shunliuDustButWidget.setVisible(0)
            self.shunliuBlastButWidget.setVisible(0)
        elif index==1:
            self.shunliuFireButWidget.setVisible(0)
            self.shunliuWaterButWidget.setVisible(1)
            self.shunliuSomkeButWidget.setVisible(0)
            self.shunliuDustButWidget.setVisible(0)
            self.shunliuBlastButWidget.setVisible(0)
        elif index==2:
            self.shunliuFireButWidget.setVisible(0)
            self.shunliuWaterButWidget.setVisible(0)
            self.shunliuSomkeButWidget.setVisible(1)
            self.shunliuDustButWidget.setVisible(0)
            self.shunliuBlastButWidget.setVisible(0)
        elif index==3:
            self.shunliuFireButWidget.setVisible(0)
            self.shunliuWaterButWidget.setVisible(0)
            self.shunliuSomkeButWidget.setVisible(0)
            self.shunliuDustButWidget.setVisible(1)
            self.shunliuBlastButWidget.setVisible(0)
        elif index==4:
            self.shunliuFireButWidget.setVisible(0)
            self.shunliuWaterButWidget.setVisible(0)
            self.shunliuSomkeButWidget.setVisible(0)
            self.shunliuDustButWidget.setVisible(0)
            self.shunliuBlastButWidget.setVisible(1)

    def shunliuFireButCmd(self):
        if self.sender().objectName()=='shunliuFireBut0':
            print 'shunliu_a'
        elif self.sender().objectName()=='shunliuFireBut1':
            print 'shunliu_b'
        elif self.sender().objectName()=='shunliuFireBut2':
            print 'shunliu_c'
        elif self.sender().objectName()=='shunliuFireBut3':
            print 'shunliu_d'
        elif self.sender().objectName()=='shunliuFireBut4':
            print 'shunliu_e'
        elif self.sender().objectName()=='shunliuFireBut5':
            print 'shunliu_f'
        elif self.sender().objectName()=='shunliuFireBut6':
            print 'shunliu_g'


    def shunliuWaterButCmd(self):
        if self.sender().objectName()=='shunliuWaterBut0':
            print 'shunliu_aa'
        elif self.sender().objectName()=='shunliuWaterBut1':
            print 'shunliu_bb'
        elif self.sender().objectName()=='shunliuWaterBut2':
            print 'shunliu_cc'
        elif self.sender().objectName()=='shunliuWaterBut3':
            print 'shunliu_dd'
        elif self.sender().objectName()=='shunliuWaterBut4':
            print 'shunliu_ee'
        elif self.sender().objectName()=='shunliuWaterBut5':
            print 'shunliu_ff'
        elif self.sender().objectName()=='shunliuWaterBut6':
            print 'shunliu_gg'
        elif self.sender().objectName()=='shunliuWaterBut7':
            print 'shunliu_hh'


    def shunliuSomkeButCmd(self):
        if self.sender().objectName()=='shunliuSomkeBut0':
            print 'shunliu_aaa'
        elif self.sender().objectName()=='shunliuSomkeBut1':
            print 'shunliu_bbb'


    def shunliuDustButCmd(self):
        if self.sender().objectName()=='shunliuDustBut0':
            print 'shunliu_aaaa'
        elif self.sender().objectName()=='shunliuDustBut1':
            print 'shunliu_bbbb'
        elif self.sender().objectName()=='shunliuDustBut2':
            print 'shunliu_cccc'


    def shunliuBlastButCmd(self):
        if self.sender().objectName()=='shunliuBlastBut0':
            print 'shunliu_aaaaa'
        elif self.sender().objectName()=='shunliuBlastBut1':
            print 'shunliu_bbbbb'
        elif self.sender().objectName()=='shunliuBlastBut2':
            print 'shunliu_ccccc'
        elif self.sender().objectName()=='shunliuBlastBut3':
            print 'shunliu_ddddd'

#-------------------MiniTiger------------------------------------------------------------------
    def CreateMiniTigerQC(self,projectName):
        self.MiniTigerEffectTypes=[u'火',
                                   u'水',
                                   u'烟',
                                   u'灰尘',
                                   u'爆炸']

        self.miniTigerQC=QComboBox(self)
        self.miniTigerQC.setObjectName(projectName+'_QC')
        self.miniTigerQC.setMinimumSize(400,30)
        self.miniTigerQC.addItems(self.MiniTigerEffectTypes)
        try:
            self.miniTigerQC.setFont(QFont('',11))
            self.miniTigerQC.setStyleSheet("""font-size:15px;}""")
        except:
            pass


    def CreateMiniTigerFireBut(self):
        self.miniTigerFireButWidget=QWidget()
        self.miniTigerFireFormLayout=QFormLayout()
        self.miniTigerFireButWidget.setLayout(self.miniTigerFireFormLayout)
        self.miniTigerCurrentFireLayout=''
        self.miniTigerFireButs=[]
        self.miniTigerFireTypes=[u'大火',
                                 u'中火',
                                 u'小火',
                                 u'火灾',
                                 u'烛火',
                                 u'炉火',
                                 u'天火']
        self.miniTigerFireIcon_paths=['M:\leo369\images\pyside_test\images\Chrysanthemum.jpg',
                                      'M:\leo369\images\pyside_test\images\Desert.jpg',
                                      'M:\leo369\images\pyside_test\images\Hydrangeas.jpg',
                                      'M:\leo369\images\pyside_test\images\Jellyfish.jpg',
                                      'M:\leo369\images\pyside_test\images\Koala.jpg',
                                      'M:\leo369\images\pyside_test\images\Lighthouse.jpg',
                                      'M:\leo369\images\pyside_test\images\Penguins.jpg']
        for i in range(0,len(self.miniTigerFireTypes)):
            if i%3==0:
                self.miniTigerCurrentFireLayout=QHBoxLayout()
                self.miniTigerFireFormLayout.addRow(self.miniTigerCurrentFireLayout)

            self.miniTigerFireBut=QPushButton(self.miniTigerFireTypes[i])
            self.miniTigerFireBut.setObjectName('miniTigerFireBut'+str(i))
            self.miniTigerFireBut.setIcon(QIcon(self.miniTigerFireIcon_paths[i]))
            self.miniTigerFireBut.setIconSize(QSize(100,80))
            self.miniTigerFireBut.setMinimumSize(135,80)
            self.miniTigerFireBut.setMaximumSize(135,80)
            self.miniTigerFireBut.setFlat(1)
            self.miniTigerCurrentFireLayout.addWidget(self.miniTigerFireBut)

            self.miniTigerFireBut.clicked.connect(self.miniTigerFireButCmd)


    def CreateMiniTigerWaterBut(self):
        self.miniTigerWaterButWidget=QWidget()
        self.miniTigerWaterFormLayout=QFormLayout()
        self.miniTigerWaterButWidget.setLayout(self.miniTigerWaterFormLayout)
        self.miniTigerCurrentWaterLayout=''

        self.miniTigerWaterTypes=[u'酒水',
                                  u'洪水',
                                  u'海洋',
                                  u'海啸',
                                  u'水花',
                                  u'洗澡',
                                  u'漩涡',
                                  u'倒水']

        for i in range(0,len(self.miniTigerWaterTypes)):
            if i%3==0:
                self.miniTigerCurrentWaterLayout=QHBoxLayout()
                self.miniTigerWaterFormLayout.addRow(self.miniTigerCurrentWaterLayout)

            self.miniTigerWaterBut=QPushButton(self.miniTigerWaterTypes[i],self)
            self.miniTigerWaterBut.setObjectName('miniTigerWaterBut'+str(i))
            self.miniTigerWaterBut.setMinimumSize(135,80)
            self.miniTigerWaterBut.setMaximumSize(135,80)
            self.miniTigerWaterBut.setFlat(1)
            self.miniTigerCurrentWaterLayout.addWidget(self.miniTigerWaterBut)

            self.miniTigerWaterBut.clicked.connect(self.miniTigerWaterButCmd)


    def CreateMiniTigerSomkeBut(self):
        self.miniTigerSomkeButWidget=QWidget()
        self.miniTigerSomekFormLayout=QFormLayout()
        self.miniTigerSomkeButWidget.setLayout(self.miniTigerSomekFormLayout)
        self.miniTigerCurrentSomkeLayout=''

        self.miniTigerSomkeTypes=[u'轻烟',
                                  u'浓烟']

        for i in range(0,len(self.miniTigerSomkeTypes)):
            if i%3==0:
                self.miniTigerCurrentSomkeLayout=QHBoxLayout()
                self.miniTigerSomekFormLayout.addRow(self.miniTigerCurrentSomkeLayout)

            self.miniTigerSomkeBut=QPushButton(self.miniTigerSomkeTypes[i],self)
            self.miniTigerSomkeBut.setObjectName('miniTigerSomkeBut'+str(i))
            self.miniTigerSomkeBut.setMinimumSize(135,80)
            self.miniTigerSomkeBut.setMaximumSize(135,80)
            self.miniTigerSomkeBut.setFlat(1)
            self.miniTigerCurrentSomkeLayout.addWidget(self.miniTigerSomkeBut)

            self.miniTigerSomkeBut.clicked.connect(self.miniTigerSomkeButCmd)

    def CreateMiniTigerDustBut(self):
        self.miniTigerDustButWidget=QWidget()
        self.miniTigerDustFormLayout=QFormLayout()
        self.miniTigerDustButWidget.setLayout(self.miniTigerDustFormLayout)
        self.miniTigerCurrentDustLayout=''

        self.miniTigerDustTypes=[u'满天扬沙',
                                 u'风沙',
                                 u'沙尘暴']
        for i in range(0,len(self.miniTigerDustTypes)):
            if i%3==0:
                self.miniTigerCurrentDustLayout=QHBoxLayout()
                self.miniTigerDustFormLayout.addRow(self.miniTigerCurrentDustLayout)

            self.miniTigerDustBut=QPushButton(self.miniTigerDustTypes[i],self)
            self.miniTigerDustBut.setObjectName('miniTigerDustBut'+str(i))
            self.miniTigerDustBut.setMinimumSize(135,80)
            self.miniTigerDustBut.setMaximumSize(135,80)
            self.miniTigerDustBut.setFlat(1)
            self.miniTigerCurrentDustLayout.addWidget(self.miniTigerDustBut)

            self.miniTigerDustBut.clicked.connect(self.miniTigerDustButCmd)

    def CreateMiniTigerBlastBut(self):
        self.miniTigerBlastButWidget=QWidget()
        self.miniTigerBlastFormLayout=QFormLayout()
        self.miniTigerBlastButWidget.setLayout(self.miniTigerBlastFormLayout)
        self.miniTigerCurrentBlastLayout=''

        self.miniTigerBlastTypes=[u'核弹爆炸',
                                  u'炸弹爆炸',
                                  u'子弹爆炸',
                                  u'汽油爆炸']

        for i in range(0,len(self.miniTigerBlastTypes)):
            if i%3==0:
                self.miniTigerCurrentBlastLayout=QHBoxLayout()
                self.miniTigerBlastFormLayout.addRow(self.miniTigerCurrentBlastLayout)

            self.miniTigerBlastBut=QPushButton(self.miniTigerBlastTypes[i],self)
            self.miniTigerBlastBut.setObjectName('miniTigerBlastBut'+str(i))
            self.miniTigerBlastBut.setMinimumSize(135,80)
            self.miniTigerBlastBut.setMaximumSize(135,80)
            self.miniTigerBlastBut.setFlat(1)
            self.miniTigerCurrentBlastLayout.addWidget(self.miniTigerBlastBut)

            self.miniTigerBlastBut.clicked.connect(self.miniTigerBlastButCmd)

    def miniTiger_on_changed(self,index):
        if index==0:
            self.miniTigerFireButWidget.setVisible(1)
            self.miniTigerWaterButWidget.setVisible(0)
            self.miniTigerSomkeButWidget.setVisible(0)
            self.miniTigerDustButWidget.setVisible(0)
            self.miniTigerBlastButWidget.setVisible(0)
        elif index==1:
            self.miniTigerFireButWidget.setVisible(0)
            self.miniTigerWaterButWidget.setVisible(1)
            self.miniTigerSomkeButWidget.setVisible(0)
            self.miniTigerDustButWidget.setVisible(0)
            self.miniTigerBlastButWidget.setVisible(0)
        elif index==2:
            self.miniTigerFireButWidget.setVisible(0)
            self.miniTigerWaterButWidget.setVisible(0)
            self.miniTigerSomkeButWidget.setVisible(1)
            self.miniTigerDustButWidget.setVisible(0)
            self.miniTigerBlastButWidget.setVisible(0)
        elif index==3:
            self.miniTigerFireButWidget.setVisible(0)
            self.miniTigerWaterButWidget.setVisible(0)
            self.miniTigerSomkeButWidget.setVisible(0)
            self.miniTigerDustButWidget.setVisible(1)
            self.miniTigerBlastButWidget.setVisible(0)
        elif index==4:
            self.miniTigerFireButWidget.setVisible(0)
            self.miniTigerWaterButWidget.setVisible(0)
            self.miniTigerSomkeButWidget.setVisible(0)
            self.miniTigerDustButWidget.setVisible(0)
            self.miniTigerBlastButWidget.setVisible(1)

    def miniTigerFireButCmd(self):
        if self.sender().objectName()=='miniTigerFireBut0':
            print 'miniTiger_a'
        elif self.sender().objectName()=='miniTigerFireBut1':
            print 'miniTiger_b'
        elif self.sender().objectName()=='miniTigerFireBut2':
            print 'miniTiger_c'
        elif self.sender().objectName()=='miniTigerFireBut3':
            print 'miniTiger_d'
        elif self.sender().objectName()=='miniTigerFireBut4':
            print 'miniTiger_e'
        elif self.sender().objectName()=='miniTigerFireBut5':
            print 'miniTiger_f'
        elif self.sender().objectName()=='miniTigerFireBut6':
            print 'miniTiger_g'


    def miniTigerWaterButCmd(self):
        if self.sender().objectName()=='miniTigerWaterBut0':
            print 'miniTiger_aa'
        elif self.sender().objectName()=='miniTigerWaterBut1':
            print 'miniTiger_bb'
        elif self.sender().objectName()=='miniTigerWaterBut2':
            print 'miniTiger_cc'
        elif self.sender().objectName()=='miniTigerWaterBut3':
            print 'miniTiger_dd'
        elif self.sender().objectName()=='miniTigerWaterBut4':
            print 'miniTiger_ee'
        elif self.sender().objectName()=='miniTigerWaterBut5':
            print 'miniTiger_ff'
        elif self.sender().objectName()=='miniTigerWaterBut6':
            print 'miniTiger_gg'
        elif self.sender().objectName()=='miniTigerWaterBut7':
            print 'miniTiger_hh'


    def miniTigerSomkeButCmd(self):
        if self.sender().objectName()=='miniTigerSomkeBut0':
            print 'miniTiger_aaa'
        elif self.sender().objectName()=='miniTigerSomkeBut1':
            print 'miniTiger_bbb'


    def miniTigerDustButCmd(self):
        if self.sender().objectName()=='miniTigerDustBut0':
            print 'miniTiger_aaaa'
        elif self.sender().objectName()=='miniTigerDustBut1':
            print 'miniTiger_bbbb'
        elif self.sender().objectName()=='miniTigerDustBut2':
            print 'miniTiger_cccc'


    def miniTigerBlastButCmd(self):
        if self.sender().objectName()=='miniTigerBlastBut0':
            print 'miniTiger_aaaaa'
        elif self.sender().objectName()=='miniTigerBlastBut1':
            print 'miniTiger_bbbbb'
        elif self.sender().objectName()=='miniTigerBlastBut2':
            print 'miniTiger_ccccc'
        elif self.sender().objectName()=='miniTigerBlastBut3':
            print 'miniTiger_ddddd'

#-------------------Lego------------------------------------------------------------------
    def CreateLegoQC(self,projectName):
        self.LegoEffectTypes=[u'火',
                              u'水',
                              u'烟',
                              u'灰尘',
                              u'爆炸']

        self.LegoQC=QComboBox(self)
        self.LegoQC.setObjectName(projectName+'_QC')
        self.LegoQC.setMinimumSize(400,30)
        self.LegoQC.addItems(self.LegoEffectTypes)
        try:
            self.LegoQC.setFont(QFont('',11))
            self.LegoQC.setStyleSheet("""font-size:15px;}""")
        except:
            pass


    def CreateLegoFireBut(self):
        self.LegoFireButWidget=QWidget()
        self.LegoFireFormLayout=QFormLayout()
        self.LegoFireButWidget.setLayout(self.LegoFireFormLayout)
        self.LegoCurrentFireLayout=''
        self.LegoFireButs=[]
        self.LegoFireTypes=[u'大火',
                            u'中火',
                            u'小火',
                            u'火灾',
                            u'烛火',
                            u'炉火',
                            u'天火']
        self.LegoFireIcon_paths=['M:\leo369\images\pyside_test\images\Chrysanthemum.jpg',
                                 'M:\leo369\images\pyside_test\images\Desert.jpg',
                                 'M:\leo369\images\pyside_test\images\Hydrangeas.jpg',
                                 'M:\leo369\images\pyside_test\images\Jellyfish.jpg',
                                 'M:\leo369\images\pyside_test\images\Koala.jpg',
                                 'M:\leo369\images\pyside_test\images\Lighthouse.jpg',
                                 'M:\leo369\images\pyside_test\images\Penguins.jpg']
        for i in range(0,len(self.LegoFireTypes)):
            if i%3==0:
                self.LegoCurrentFireLayout=QHBoxLayout()
                self.LegoFireFormLayout.addRow(self.LegoCurrentFireLayout)

            self.LegoFireBut=QPushButton(self.LegoFireTypes[i])
            self.LegoFireBut.setObjectName('LegoFireBut'+str(i))
            self.LegoFireBut.setIcon(QIcon(self.LegoFireIcon_paths[i]))
            self.LegoFireBut.setIconSize(QSize(100,80))
            self.LegoFireBut.setMinimumSize(135,80)
            self.LegoFireBut.setMaximumSize(135,80)
            self.LegoFireBut.setFlat(1)
            self.LegoCurrentFireLayout.addWidget(self.LegoFireBut)

            self.LegoFireBut.clicked.connect(self.LegoFireButCmd)


    def CreateLegoWaterBut(self):
        self.LegoWaterButWidget=QWidget()
        self.LegoWaterFormLayout=QFormLayout()
        self.LegoWaterButWidget.setLayout(self.LegoWaterFormLayout)
        self.LegoCurrentWaterLayout=''

        self.LegoWaterTypes=[u'酒水',
                             u'洪水',
                             u'海洋',
                             u'海啸',
                             u'水花',
                             u'洗澡',
                             u'漩涡',
                             u'倒水']

        for i in range(0,len(self.LegoWaterTypes)):
            if i%3==0:
                self.LegoCurrentWaterLayout=QHBoxLayout()
                self.LegoWaterFormLayout.addRow(self.LegoCurrentWaterLayout)

            self.LegoWaterBut=QPushButton(self.LegoWaterTypes[i],self)
            self.LegoWaterBut.setObjectName('LegoWaterBut'+str(i))
            self.LegoWaterBut.setMinimumSize(135,80)
            self.LegoWaterBut.setMaximumSize(135,80)
            self.LegoWaterBut.setFlat(1)
            self.LegoCurrentWaterLayout.addWidget(self.LegoWaterBut)

            self.LegoWaterBut.clicked.connect(self.LegoWaterButCmd)


    def CreateLegoSomkeBut(self):
        self.LegoSomkeButWidget=QWidget()
        self.LegoSomekFormLayout=QFormLayout()
        self.LegoSomkeButWidget.setLayout(self.LegoSomekFormLayout)
        self.LegoCurrentSomkeLayout=''

        self.LegoSomkeTypes=[u'轻烟',
                             u'浓烟']

        for i in range(0,len(self.LegoSomkeTypes)):
            if i%3==0:
                self.LegoCurrentSomkeLayout=QHBoxLayout()
                self.LegoSomekFormLayout.addRow(self.LegoCurrentSomkeLayout)

            self.LegoSomkeBut=QPushButton(self.LegoSomkeTypes[i],self)
            self.LegoSomkeBut.setObjectName('LegoSomkeBut'+str(i))
            self.LegoSomkeBut.setMinimumSize(135,80)
            self.LegoSomkeBut.setMaximumSize(135,80)
            self.LegoSomkeBut.setFlat(1)
            self.LegoCurrentSomkeLayout.addWidget(self.LegoSomkeBut)

            self.LegoSomkeBut.clicked.connect(self.LegoSomkeButCmd)

    def CreateLegoDustBut(self):
        self.LegoDustButWidget=QWidget()
        self.LegoDustFormLayout=QFormLayout()
        self.LegoDustButWidget.setLayout(self.LegoDustFormLayout)
        self.LegoCurrentDustLayout=''

        self.LegoDustTypes=[u'满天扬沙',
                            u'风沙',
                            u'沙尘暴']
        for i in range(0,len(self.LegoDustTypes)):
            if i%3==0:
                self.LegoCurrentDustLayout=QHBoxLayout()
                self.LegoDustFormLayout.addRow(self.LegoCurrentDustLayout)

            self.LegoDustBut=QPushButton(self.LegoDustTypes[i],self)
            self.LegoDustBut.setObjectName('LegoDustBut'+str(i))
            self.LegoDustBut.setMinimumSize(135,80)
            self.LegoDustBut.setMaximumSize(135,80)
            self.LegoDustBut.setFlat(1)
            self.LegoCurrentDustLayout.addWidget(self.LegoDustBut)

            self.LegoDustBut.clicked.connect(self.LegoDustButCmd)

    def CreateLegoBlastBut(self):
        self.LegoBlastButWidget=QWidget()
        self.LegoBlastFormLayout=QFormLayout()
        self.LegoBlastButWidget.setLayout(self.LegoBlastFormLayout)
        self.LegoCurrentBlastLayout=''

        self.LegoBlastTypes=[u'核弹爆炸',
                             u'炸弹爆炸',
                             u'子弹爆炸',
                             u'汽油爆炸']

        for i in range(0,len(self.LegoBlastTypes)):
            if i%3==0:
                self.LegoCurrentBlastLayout=QHBoxLayout()
                self.LegoBlastFormLayout.addRow(self.LegoCurrentBlastLayout)

            self.LegoBlastBut=QPushButton(self.LegoBlastTypes[i],self)
            self.LegoBlastBut.setObjectName('LegoBlastBut'+str(i))
            self.LegoBlastBut.setMinimumSize(135,80)
            self.LegoBlastBut.setMaximumSize(135,80)
            self.LegoBlastBut.setFlat(1)
            self.LegoCurrentBlastLayout.addWidget(self.LegoBlastBut)

            self.LegoBlastBut.clicked.connect(self.LegoBlastButCmd)

    def Lego_on_changed(self,index):
        if index==0:
            self.LegoFireButWidget.setVisible(1)
            self.LegoWaterButWidget.setVisible(0)
            self.LegoSomkeButWidget.setVisible(0)
            self.LegoDustButWidget.setVisible(0)
            self.LegoBlastButWidget.setVisible(0)
        elif index==1:
            self.LegoFireButWidget.setVisible(0)
            self.LegoWaterButWidget.setVisible(1)
            self.LegoSomkeButWidget.setVisible(0)
            self.LegoDustButWidget.setVisible(0)
            self.LegoBlastButWidget.setVisible(0)
        elif index==2:
            self.LegoFireButWidget.setVisible(0)
            self.LegoWaterButWidget.setVisible(0)
            self.LegoSomkeButWidget.setVisible(1)
            self.LegoDustButWidget.setVisible(0)
            self.LegoBlastButWidget.setVisible(0)
        elif index==3:
            self.LegoFireButWidget.setVisible(0)
            self.LegoWaterButWidget.setVisible(0)
            self.LegoSomkeButWidget.setVisible(0)
            self.LegoDustButWidget.setVisible(1)
            self.LegoBlastButWidget.setVisible(0)
        elif index==4:
            self.LegoFireButWidget.setVisible(0)
            self.LegoWaterButWidget.setVisible(0)
            self.LegoSomkeButWidget.setVisible(0)
            self.LegoDustButWidget.setVisible(0)
            self.LegoBlastButWidget.setVisible(1)

    def LegoFireButCmd(self):
        if self.sender().objectName()=='LegoFireBut0':
            print 'Lego_a'
        elif self.sender().objectName()=='LegoFireBut1':
            print 'Lego_b'
        elif self.sender().objectName()=='LegoFireBut2':
            print 'Lego_c'
        elif self.sender().objectName()=='LegoFireBut3':
            print 'Lego_d'
        elif self.sender().objectName()=='LegoFireBut4':
            print 'Lego_e'
        elif self.sender().objectName()=='LegoFireBut5':
            print 'Lego_f'
        elif self.sender().objectName()=='LegoFireBut6':
            print 'Lego_g'


    def LegoWaterButCmd(self):
        if self.sender().objectName()=='LegoWaterBut0':
            print 'Lego_aa'
        elif self.sender().objectName()=='LegoWaterBut1':
            print 'Lego_bb'
        elif self.sender().objectName()=='LegoWaterBut2':
            print 'Lego_cc'
        elif self.sender().objectName()=='LegoWaterBut3':
            print 'Lego_dd'
        elif self.sender().objectName()=='LegoWaterBut4':
            print 'Lego_ee'
        elif self.sender().objectName()=='LegoWaterBut5':
            print 'Lego_ff'
        elif self.sender().objectName()=='LegoWaterBut6':
            print 'Lego_gg'
        elif self.sender().objectName()=='LegoWaterBut7':
            print 'Lego_hh'


    def LegoSomkeButCmd(self):
        if self.sender().objectName()=='LegoSomkeBut0':
            print 'Lego_aaa'
        elif self.sender().objectName()=='LegoSomkeBut1':
            print 'Lego_bbb'


    def LegoDustButCmd(self):
        if self.sender().objectName()=='LegoDustBut0':
            print 'Lego_aaaa'
        elif self.sender().objectName()=='LegoDustBut1':
            print 'Lego_bbbb'
        elif self.sender().objectName()=='LegoDustBut2':
            print 'Lego_cccc'


    def LegoBlastButCmd(self):
        if self.sender().objectName()=='LegoBlastBut0':
            print 'Lego_aaaaa'
        elif self.sender().objectName()=='LegoBlastBut1':
            print 'Lego_bbbbb'
        elif self.sender().objectName()=='LegoBlastBut2':
            print 'Lego_ccccc'
        elif self.sender().objectName()=='LegoBlastBut3':
            print 'Lego_ddddd'


#-------------------Maya Bee------------------------------------------------------------------
    def CreateMayaBeeQC(self,projectName):
        self.MayaBeeEffectTypes=[u'火',
                                 u'水',
                                 u'烟',
                                 u'灰尘',
                                 u'爆炸']

        self.MayaBeeQC=QComboBox(self)
        self.MayaBeeQC.setObjectName(projectName+'_QC')
        self.MayaBeeQC.setMinimumSize(400,30)
        self.MayaBeeQC.addItems(self.MayaBeeEffectTypes)
        try:
            self.MayaBeeQC.setFont(QFont('',11))
            self.MayaBeeQC.setStyleSheet("""font-size:15px;}""")
        except:
            pass


    def CreateMayaBeeFireBut(self):
        self.MayaBeeFireButWidget=QWidget()
        self.MayaBeeFireFormLayout=QFormLayout()
        self.MayaBeeFireButWidget.setLayout(self.MayaBeeFireFormLayout)
        self.MayaBeeCurrentFireLayout=''
        self.MayaBeeFireButs=[]
        self.MayaBeeFireTypes=[u'大火',
                               u'中火',
                               u'小火',
                               u'火灾',
                               u'烛火',
                               u'炉火',
                               u'天火']
        self.MayaBeeFireIcon_paths=['M:\leo369\images\pyside_test\images\Chrysanthemum.jpg',
                                    'M:\leo369\images\pyside_test\images\Desert.jpg',
                                    'M:\leo369\images\pyside_test\images\Hydrangeas.jpg',
                                    'M:\leo369\images\pyside_test\images\Jellyfish.jpg',
                                    'M:\leo369\images\pyside_test\images\Koala.jpg',
                                    'M:\leo369\images\pyside_test\images\Lighthouse.jpg',
                                    'M:\leo369\images\pyside_test\images\Penguins.jpg']
        for i in range(0,len(self.MayaBeeFireTypes)):
            if i%3==0:
                self.MayaBeeCurrentFireLayout=QHBoxLayout()
                self.MayaBeeFireFormLayout.addRow(self.MayaBeeCurrentFireLayout)

            self.MayaBeeFireBut=QPushButton(self.MayaBeeFireTypes[i])
            self.MayaBeeFireBut.setObjectName('MayaBeeFireBut'+str(i))
            self.MayaBeeFireBut.setIcon(QIcon(self.MayaBeeFireIcon_paths[i]))
            self.MayaBeeFireBut.setIconSize(QSize(100,80))
            self.MayaBeeFireBut.setMinimumSize(135,80)
            self.MayaBeeFireBut.setMaximumSize(135,80)
            self.MayaBeeFireBut.setFlat(1)
            self.MayaBeeCurrentFireLayout.addWidget(self.MayaBeeFireBut)

            self.MayaBeeFireBut.clicked.connect(self.MayaBeeFireButCmd)


    def CreateMayaBeeWaterBut(self):
        self.MayaBeeWaterButWidget=QWidget()
        self.MayaBeeWaterFormLayout=QFormLayout()
        self.MayaBeeWaterButWidget.setLayout(self.MayaBeeWaterFormLayout)
        self.MayaBeeCurrentWaterLayout=''

        self.MayaBeeWaterTypes=[u'酒水',
                                u'洪水',
                                u'海洋',
                                u'海啸',
                                u'水花',
                                u'洗澡',
                                u'漩涡',
                                u'倒水']

        for i in range(0,len(self.MayaBeeWaterTypes)):
            if i%3==0:
                self.MayaBeeCurrentWaterLayout=QHBoxLayout()
                self.MayaBeeWaterFormLayout.addRow(self.MayaBeeCurrentWaterLayout)

            self.MayaBeeWaterBut=QPushButton(self.MayaBeeWaterTypes[i],self)
            self.MayaBeeWaterBut.setObjectName('MayaBeeWaterBut'+str(i))
            self.MayaBeeWaterBut.setMinimumSize(135,80)
            self.MayaBeeWaterBut.setMaximumSize(135,80)
            self.MayaBeeWaterBut.setFlat(1)
            self.MayaBeeCurrentWaterLayout.addWidget(self.MayaBeeWaterBut)

            self.MayaBeeWaterBut.clicked.connect(self.MayaBeeWaterButCmd)


    def CreateMayaBeeSomkeBut(self):
        self.MayaBeeSomkeButWidget=QWidget()
        self.MayaBeeSomekFormLayout=QFormLayout()
        self.MayaBeeSomkeButWidget.setLayout(self.MayaBeeSomekFormLayout)
        self.MayaBeeCurrentSomkeLayout=''

        self.MayaBeeSomkeTypes=[u'轻烟',
                                u'浓烟']

        for i in range(0,len(self.MayaBeeSomkeTypes)):
            if i%3==0:
                self.MayaBeeCurrentSomkeLayout=QHBoxLayout()
                self.MayaBeeSomekFormLayout.addRow(self.MayaBeeCurrentSomkeLayout)

            self.MayaBeeSomkeBut=QPushButton(self.MayaBeeSomkeTypes[i],self)
            self.MayaBeeSomkeBut.setObjectName('MayaBeeSomkeBut'+str(i))
            self.MayaBeeSomkeBut.setMinimumSize(135,80)
            self.MayaBeeSomkeBut.setMaximumSize(135,80)
            self.MayaBeeSomkeBut.setFlat(1)
            self.MayaBeeCurrentSomkeLayout.addWidget(self.MayaBeeSomkeBut)

            self.MayaBeeSomkeBut.clicked.connect(self.MayaBeeSomkeButCmd)

    def CreateMayaBeeDustBut(self):
        self.MayaBeeDustButWidget=QWidget()
        self.MayaBeeDustFormLayout=QFormLayout()
        self.MayaBeeDustButWidget.setLayout(self.MayaBeeDustFormLayout)
        self.MayaBeeCurrentDustLayout=''

        self.MayaBeeDustTypes=[u'满天扬沙',
                               u'风沙',
                               u'沙尘暴']
        for i in range(0,len(self.MayaBeeDustTypes)):
            if i%3==0:
                self.MayaBeeCurrentDustLayout=QHBoxLayout()
                self.MayaBeeDustFormLayout.addRow(self.MayaBeeCurrentDustLayout)

            self.MayaBeeDustBut=QPushButton(self.MayaBeeDustTypes[i],self)
            self.MayaBeeDustBut.setObjectName('MayaBeeDustBut'+str(i))
            self.MayaBeeDustBut.setMinimumSize(135,80)
            self.MayaBeeDustBut.setMaximumSize(135,80)
            self.MayaBeeDustBut.setFlat(1)
            self.MayaBeeCurrentDustLayout.addWidget(self.MayaBeeDustBut)

            self.MayaBeeDustBut.clicked.connect(self.MayaBeeDustButCmd)

    def CreateMayaBeeBlastBut(self):
        self.MayaBeeBlastButWidget=QWidget()
        self.MayaBeeBlastFormLayout=QFormLayout()
        self.MayaBeeBlastButWidget.setLayout(self.MayaBeeBlastFormLayout)
        self.MayaBeeCurrentBlastLayout=''

        self.MayaBeeBlastTypes=[u'核弹爆炸',
                             u'炸弹爆炸',
                             u'子弹爆炸',
                             u'汽油爆炸']

        for i in range(0,len(self.MayaBeeBlastTypes)):
            if i%3==0:
                self.MayaBeeCurrentBlastLayout=QHBoxLayout()
                self.MayaBeeBlastFormLayout.addRow(self.MayaBeeCurrentBlastLayout)

            self.MayaBeeBlastBut=QPushButton(self.MayaBeeBlastTypes[i],self)
            self.MayaBeeBlastBut.setObjectName('MayaBeeBlastBut'+str(i))
            self.MayaBeeBlastBut.setMinimumSize(135,80)
            self.MayaBeeBlastBut.setMaximumSize(135,80)
            self.MayaBeeBlastBut.setFlat(1)
            self.MayaBeeCurrentBlastLayout.addWidget(self.MayaBeeBlastBut)

            self.MayaBeeBlastBut.clicked.connect(self.MayaBeeBlastButCmd)

    def MayaBee_on_changed(self,index):
        if index==0:
            self.MayaBeeFireButWidget.setVisible(1)
            self.MayaBeeWaterButWidget.setVisible(0)
            self.MayaBeeSomkeButWidget.setVisible(0)
            self.MayaBeeDustButWidget.setVisible(0)
            self.MayaBeeBlastButWidget.setVisible(0)
        elif index==1:
            self.MayaBeeFireButWidget.setVisible(0)
            self.MayaBeeWaterButWidget.setVisible(1)
            self.MayaBeeSomkeButWidget.setVisible(0)
            self.MayaBeeDustButWidget.setVisible(0)
            self.MayaBeeBlastButWidget.setVisible(0)
        elif index==2:
            self.MayaBeeFireButWidget.setVisible(0)
            self.MayaBeeWaterButWidget.setVisible(0)
            self.MayaBeeSomkeButWidget.setVisible(1)
            self.MayaBeeDustButWidget.setVisible(0)
            self.MayaBeeBlastButWidget.setVisible(0)
        elif index==3:
            self.MayaBeeFireButWidget.setVisible(0)
            self.MayaBeeWaterButWidget.setVisible(0)
            self.MayaBeeSomkeButWidget.setVisible(0)
            self.MayaBeeDustButWidget.setVisible(1)
            self.MayaBeeBlastButWidget.setVisible(0)
        elif index==4:
            self.MayaBeeFireButWidget.setVisible(0)
            self.MayaBeeWaterButWidget.setVisible(0)
            self.MayaBeeSomkeButWidget.setVisible(0)
            self.MayaBeeDustButWidget.setVisible(0)
            self.MayaBeeBlastButWidget.setVisible(1)

    def MayaBeeFireButCmd(self):
        if self.sender().objectName()=='MayaBeeFireBut0':
            print 'MayaBee_a'
        elif self.sender().objectName()=='MayaBeeFireBut1':
            print 'MayaBee_b'
        elif self.sender().objectName()=='MayaBeeFireBut2':
            print 'MayaBee_c'
        elif self.sender().objectName()=='MayaBeeFireBut3':
            print 'MayaBee_d'
        elif self.sender().objectName()=='MayaBeeFireBut4':
            print 'MayaBee_e'
        elif self.sender().objectName()=='MayaBeeFireBut5':
            print 'MayaBee_f'
        elif self.sender().objectName()=='MayaBeeFireBut6':
            print 'MayaBee_g'


    def MayaBeeWaterButCmd(self):
        if self.sender().objectName()=='MayaBeeWaterBut0':
            print 'MayaBee_aa'
        elif self.sender().objectName()=='MayaBeeWaterBut1':
            print 'MayaBee_bb'
        elif self.sender().objectName()=='MayaBeeWaterBut2':
            print 'MayaBee_cc'
        elif self.sender().objectName()=='MayaBeeWaterBut3':
            print 'MayaBee_dd'
        elif self.sender().objectName()=='MayaBeeWaterBut4':
            print 'MayaBee_ee'
        elif self.sender().objectName()=='MayaBeeWaterBut5':
            print 'MayaBee_ff'
        elif self.sender().objectName()=='MayaBeeWaterBut6':
            print 'MayaBee_gg'
        elif self.sender().objectName()=='MayaBeeWaterBut7':
            print 'MayaBee_hh'


    def MayaBeeSomkeButCmd(self):
        if self.sender().objectName()=='MayaBeeSomkeBut0':
            print 'MayaBee_aaa'
        elif self.sender().objectName()=='MayaBeeSomkeBut1':
            print 'MayaBee_bbb'


    def MayaBeeDustButCmd(self):
        if self.sender().objectName()=='MayaBeeDustBut0':
            print 'MayaBee_aaaa'
        elif self.sender().objectName()=='MayaBeeDustBut1':
            print 'MayaBee_bbbb'
        elif self.sender().objectName()=='MayaBeeDustBut2':
            print 'MayaBee_cccc'


    def MayaBeeBlastButCmd(self):
        if self.sender().objectName()=='MayaBeeBlastBut0':
            print 'MayaBee_aaaaa'
        elif self.sender().objectName()=='MayaBeeBlastBut1':
            print 'MayaBee_bbbbb'
        elif self.sender().objectName()=='MayaBeeBlastBut2':
            print 'MayaBee_ccccc'
        elif self.sender().objectName()=='MayaBeeBlastBut3':
            print 'MayaBee_ddddd'


#-------------------Ninjago------------------------------------------------------------------
    def CreateNinjagoQC(self,projectName):
        self.NinjagoEffectTypes=[u'火',
                                 u'水',
                                 u'烟',
                                 u'灰尘',
                                 u'爆炸']

        self.NinjagoQC=QComboBox(self)
        self.NinjagoQC.setObjectName(projectName+'_QC')
        self.NinjagoQC.setMinimumSize(400,30)
        self.NinjagoQC.addItems(self.NinjagoEffectTypes)
        try:
            self.NinjagoQC.setFont(QFont('',11))
            self.NinjagoQC.setStyleSheet("""font-size:15px;}""")
        except:
            pass


    def CreateNinjagoFireBut(self):
        self.NinjagoFireButWidget=QWidget()
        self.NinjagoFireFormLayout=QFormLayout()
        self.NinjagoFireButWidget.setLayout(self.NinjagoFireFormLayout)
        self.NinjagoCurrentFireLayout=''
        self.NinjagoFireButs=[]
        self.NinjagoFireTypes=[u'大火',
                               u'中火',
                               u'小火',
                               u'火灾',
                               u'烛火',
                               u'炉火',
                               u'天火']
        self.NinjagoFireIcon_paths=['M:\leo369\images\pyside_test\images\Chrysanthemum.jpg',
                                    'M:\leo369\images\pyside_test\images\Desert.jpg',
                                    'M:\leo369\images\pyside_test\images\Hydrangeas.jpg',
                                    'M:\leo369\images\pyside_test\images\Jellyfish.jpg',
                                    'M:\leo369\images\pyside_test\images\Koala.jpg',
                                    'M:\leo369\images\pyside_test\images\Lighthouse.jpg',
                                    'M:\leo369\images\pyside_test\images\Penguins.jpg']
        for i in range(0,len(self.NinjagoFireTypes)):
            if i%3==0:
                self.NinjagoCurrentFireLayout=QHBoxLayout()
                self.NinjagoFireFormLayout.addRow(self.NinjagoCurrentFireLayout)

            self.NinjagoFireBut=QPushButton(self.NinjagoFireTypes[i])
            self.NinjagoFireBut.setObjectName('NinjagoFireBut'+str(i))
            self.NinjagoFireBut.setIcon(QIcon(self.NinjagoFireIcon_paths[i]))
            self.NinjagoFireBut.setIconSize(QSize(100,80))
            self.NinjagoFireBut.setMinimumSize(135,80)
            self.NinjagoFireBut.setMaximumSize(135,80)
            self.NinjagoFireBut.setFlat(1)
            self.NinjagoCurrentFireLayout.addWidget(self.NinjagoFireBut)

            self.NinjagoFireBut.clicked.connect(self.NinjagoFireButCmd)


    def CreateNinjagoWaterBut(self):
        self.NinjagoWaterButWidget=QWidget()
        self.NinjagoWaterFormLayout=QFormLayout()
        self.NinjagoWaterButWidget.setLayout(self.NinjagoWaterFormLayout)
        self.NinjagoCurrentWaterLayout=''

        self.NinjagoWaterTypes=[u'酒水',
                                u'洪水',
                                u'海洋',
                                u'海啸',
                                u'水花',
                                u'洗澡',
                                u'漩涡',
                                u'倒水']

        for i in range(0,len(self.NinjagoWaterTypes)):
            if i%3==0:
                self.NinjagoCurrentWaterLayout=QHBoxLayout()
                self.NinjagoWaterFormLayout.addRow(self.NinjagoCurrentWaterLayout)

            self.NinjagoWaterBut=QPushButton(self.NinjagoWaterTypes[i],self)
            self.NinjagoWaterBut.setObjectName('NinjagoWaterBut'+str(i))
            self.NinjagoWaterBut.setMinimumSize(135,80)
            self.NinjagoWaterBut.setMaximumSize(135,80)
            self.NinjagoWaterBut.setFlat(1)
            self.NinjagoCurrentWaterLayout.addWidget(self.NinjagoWaterBut)

            self.NinjagoWaterBut.clicked.connect(self.NinjagoWaterButCmd)


    def CreateNinjagoSomkeBut(self):
        self.NinjagoSomkeButWidget=QWidget()
        self.NinjagoSomekFormLayout=QFormLayout()
        self.NinjagoSomkeButWidget.setLayout(self.NinjagoSomekFormLayout)
        self.NinjagoCurrentSomkeLayout=''

        self.NinjagoSomkeTypes=[u'轻烟',
                                u'浓烟']

        for i in range(0,len(self.NinjagoSomkeTypes)):
            if i%3==0:
                self.NinjagoCurrentSomkeLayout=QHBoxLayout()
                self.NinjagoSomekFormLayout.addRow(self.NinjagoCurrentSomkeLayout)

            self.NinjagoSomkeBut=QPushButton(self.NinjagoSomkeTypes[i],self)
            self.NinjagoSomkeBut.setObjectName('NinjagoSomkeBut'+str(i))
            self.NinjagoSomkeBut.setMinimumSize(135,80)
            self.NinjagoSomkeBut.setMaximumSize(135,80)
            self.NinjagoSomkeBut.setFlat(1)
            self.NinjagoCurrentSomkeLayout.addWidget(self.NinjagoSomkeBut)

            self.NinjagoSomkeBut.clicked.connect(self.NinjagoSomkeButCmd)

    def CreateNinjagoDustBut(self):
        self.NinjagoDustButWidget=QWidget()
        self.NinjagoDustFormLayout=QFormLayout()
        self.NinjagoDustButWidget.setLayout(self.NinjagoDustFormLayout)
        self.NinjagoCurrentDustLayout=''

        self.NinjagoDustTypes=[u'满天扬沙',
                               u'风沙',
                               u'沙尘暴']
        for i in range(0,len(self.NinjagoDustTypes)):
            if i%3==0:
                self.NinjagoCurrentDustLayout=QHBoxLayout()
                self.NinjagoDustFormLayout.addRow(self.NinjagoCurrentDustLayout)

            self.NinjagoDustBut=QPushButton(self.NinjagoDustTypes[i],self)
            self.NinjagoDustBut.setObjectName('NinjagoDustBut'+str(i))
            self.NinjagoDustBut.setMinimumSize(135,80)
            self.NinjagoDustBut.setMaximumSize(135,80)
            self.NinjagoDustBut.setFlat(1)
            self.NinjagoCurrentDustLayout.addWidget(self.NinjagoDustBut)

            self.NinjagoDustBut.clicked.connect(self.NinjagoDustButCmd)

    def CreateNinjagoBlastBut(self):
        self.NinjagoBlastButWidget=QWidget()
        self.NinjagoBlastFormLayout=QFormLayout()
        self.NinjagoBlastButWidget.setLayout(self.NinjagoBlastFormLayout)
        self.NinjagoCurrentBlastLayout=''

        self.NinjagoBlastTypes=[u'核弹爆炸',
                                u'炸弹爆炸',
                                u'子弹爆炸',
                                u'汽油爆炸']

        for i in range(0,len(self.NinjagoBlastTypes)):
            if i%3==0:
                self.NinjagoCurrentBlastLayout=QHBoxLayout()
                self.NinjagoBlastFormLayout.addRow(self.NinjagoCurrentBlastLayout)

            self.NinjagoBlastBut=QPushButton(self.NinjagoBlastTypes[i],self)
            self.NinjagoBlastBut.setObjectName('NinjagoBlastBut'+str(i))
            self.NinjagoBlastBut.setMinimumSize(135,80)
            self.NinjagoBlastBut.setMaximumSize(135,80)
            self.NinjagoBlastBut.setFlat(1)
            self.NinjagoCurrentBlastLayout.addWidget(self.NinjagoBlastBut)

            self.NinjagoBlastBut.clicked.connect(self.NinjagoBlastButCmd)

    def Ninjago_on_changed(self,index):
        if index==0:
            self.NinjagoFireButWidget.setVisible(1)
            self.NinjagoWaterButWidget.setVisible(0)
            self.NinjagoSomkeButWidget.setVisible(0)
            self.NinjagoDustButWidget.setVisible(0)
            self.NinjagoBlastButWidget.setVisible(0)
        elif index==1:
            self.NinjagoFireButWidget.setVisible(0)
            self.NinjagoWaterButWidget.setVisible(1)
            self.NinjagoSomkeButWidget.setVisible(0)
            self.NinjagoDustButWidget.setVisible(0)
            self.NinjagoBlastButWidget.setVisible(0)
        elif index==2:
            self.NinjagoFireButWidget.setVisible(0)
            self.NinjagoWaterButWidget.setVisible(0)
            self.NinjagoSomkeButWidget.setVisible(1)
            self.NinjagoDustButWidget.setVisible(0)
            self.NinjagoBlastButWidget.setVisible(0)
        elif index==3:
            self.NinjagoFireButWidget.setVisible(0)
            self.NinjagoWaterButWidget.setVisible(0)
            self.NinjagoSomkeButWidget.setVisible(0)
            self.NinjagoDustButWidget.setVisible(1)
            self.NinjagoBlastButWidget.setVisible(0)
        elif index==4:
            self.NinjagoFireButWidget.setVisible(0)
            self.NinjagoWaterButWidget.setVisible(0)
            self.NinjagoSomkeButWidget.setVisible(0)
            self.NinjagoDustButWidget.setVisible(0)
            self.NinjagoBlastButWidget.setVisible(1)

    def NinjagoFireButCmd(self):
        if self.sender().objectName()=='NinjagoFireBut0':
            print 'Ninjago_a'
        elif self.sender().objectName()=='NinjagoFireBut1':
            print 'Ninjago_b'
        elif self.sender().objectName()=='NinjagoFireBut2':
            print 'Ninjago_c'
        elif self.sender().objectName()=='NinjagoFireBut3':
            print 'Ninjago_d'
        elif self.sender().objectName()=='NinjagoFireBut4':
            print 'Ninjago_e'
        elif self.sender().objectName()=='NinjagoFireBut5':
            print 'Ninjago_f'
        elif self.sender().objectName()=='NinjagoFireBut6':
            print 'Ninjago_g'


    def NinjagoWaterButCmd(self):
        if self.sender().objectName()=='NinjagoWaterBut0':
            print 'Ninjago_aa'
        elif self.sender().objectName()=='NinjagoWaterBut1':
            print 'Ninjago_bb'
        elif self.sender().objectName()=='NinjagoWaterBut2':
            print 'Ninjago_cc'
        elif self.sender().objectName()=='NinjagoWaterBut3':
            print 'Ninjago_dd'
        elif self.sender().objectName()=='NinjagoWaterBut4':
            print 'Ninjago_ee'
        elif self.sender().objectName()=='NinjagoWaterBut5':
            print 'Ninjago_ff'
        elif self.sender().objectName()=='NinjagoWaterBut6':
            print 'Ninjago_gg'
        elif self.sender().objectName()=='NinjagoWaterBut7':
            print 'Ninjago_hh'


    def NinjagoSomkeButCmd(self):
        if self.sender().objectName()=='NinjagoSomkeBut0':
            print 'Ninjago_aaa'
        elif self.sender().objectName()=='NinjagoSomkeBut1':
            print 'Ninjago_bbb'


    def NinjagoDustButCmd(self):
        if self.sender().objectName()=='NinjagoDustBut0':
            print 'Ninjago_aaaa'
        elif self.sender().objectName()=='NinjagoDustBut1':
            print 'Ninjago_bbbb'
        elif self.sender().objectName()=='NinjagoDustBut2':
            print 'Ninjago_cccc'


    def NinjagoBlastButCmd(self):
        if self.sender().objectName()=='NinjagoBlastBut0':
            print 'Ninjago_aaaaa'
        elif self.sender().objectName()=='NinjagoBlastBut1':
            print 'Ninjago_bbbbb'
        elif self.sender().objectName()=='NinjagoBlastBut2':
            print 'Ninjago_ccccc'
        elif self.sender().objectName()=='NinjagoBlastBut3':
            print 'Ninjago_ddddd'

    def run(self):
        self.show()

app=effectType()
app.run()