# -*- coding: utf-8 -*-

'''
Created on 2014-3-27
@version:    2008,2009,2010,2011,2012,2014
@author: zhaozhongjie
usage:
'''

import sip
from PyQt4.uic import loadUi
import os , sys , datetime , time
# import sip
# sip.setapi('QString', 2)
# sip.setapi('QVariant', 2)
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from PyQt4.phonon import Phonon

import ImportExportAnim as ia;reload(ia)

def getMayaWindow():
    import maya.OpenMayaUI as apiUI
    ptr = apiUI.MQtUtil.mainWindow()
    return sip.wrapinstance(long(ptr), QObject)
'''
要实现的功能：
1.左边列表一点，右边更新
2.右边图标一点，下面播放动画
3.右边图标右键，弹出菜单
4.
'''
      
#===============================================================================
#     <<<<<<    主界面    >>>>>>  
#===============================================================================
class MainWindow(QMainWindow):                                     
    def __init__(self,parent = None): 
        super(MainWindow, self).__init__(parent)
        try:
            FILE = __file__
        except:
            FILE = r'D:\Pluto\workspace\PlutoPip\MyLib\PPanim\AnimLibrary\AnimLibrary.py'
        ui = os.path.join(os.path.dirname(FILE), 'AnimLibrary.myuis')

        self.win = loadUi(ui)
        self.setCentralWidget(self.win)
        self.setObjectName("PoseLibrary")
        
        # 设置第1个控件尺寸为56，第二个控件尺寸为0
        self.win.splitter_lr.setStretchFactor (1,1)    
        self.win.splitter_lr.setSizes([90,200])        
        # 设置splitter中间有一个按钮，可以一键隐藏左边的东西  
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0) 
        handle = self.win.splitter_lr.handle(1)
        button = QToolButton(handle)
        button.setArrowType(Qt.RightArrow)
        button.clicked.connect(self.handleSplitterButton)
        layout.addWidget(button)
        handle.setLayout(layout)

        # 帮助的图标        
        self.win.HELP.setIcon(self.win.HELP.style().standardIcon(QStyle.SP_MessageBoxQuestion))
        
        self.setWindowTitle(u"PoseLibrary")
        self.resize(960, 540)  

        # 1. 设置默认动作库路径
        self.URL = u'z:\\Projects\\Ninjago\\Ninjago_scratch\\Animation\\动作库' 
        shunliu = u'Z:\\Projects\\ShunLiu\\ShunLiu_Scratch\\Animation\\动作库'
        # 1.1 设置导入的动作库
        items = [
                     self.URL,
                     shunliu,
                     u'E:\PTAnimLibrary',
                 ]
        self.win.IM_URL.insertItems(0,items)
        
        # 1.2 设置导出的动作库
        self.win.export_Frame.setVisible(0)
        items = [
                     u'E:\PTAnimLibrary',
                     self.URL
                 ]
        self.win.EX_URL.insertItems(0,items)        
        
        # 2. 设置左侧的动作库列表
        self.setMyList()
        
        # 3. 并联动作
        self.connection()
        

    def handleSplitterButton(self):
        size = self.win.splitter_lr.sizes()
        if size[0]==0: 
            self.win.splitter_lr.setSizes([1, 1])
        else:
            self.win.splitter_lr.setSizes([0, 1]) 
 
        
    def connection(self):
        self.win.IM_URL.editTextChanged.connect(self.urlChanged)
        self.win.LIST.itemClicked.connect(self.MyListClicked)
        self.win.IFSHOW_ERROR.toggled.connect(ia.deleteCheckGroup)
        self.win.HELP.clicked.connect(self.help)
        self.win.EXPORT_BT.clicked.connect(self.exportAnim)
        self.win.CHANGE_RUL_BT.clicked.connect(self.changeExportURL_Bt)
        self.win.CONVERT_BT.clicked.connect(self.convertOldToNew_Bt)

    def convertOldToNew_Bt(self):
        s = QFileDialog.getExistingDirectory(parent=self, caption="select folder")
#         print type(s)
#         print unicode(s)
        import ConvertOldData as cd
        reload(cd)
        cd.walk(unicode(s))

    def changeExportURL_Bt(self):
        s = QFileDialog.getExistingDirectory(parent=self, caption="select folder")
        self.win.EX_URL.insertItem(0,s)
        self.win.EX_URL.setCurrentIndex(0)
        
        
    def exportAnim(self):
        path = unicode(self.win.EX_URL.currentText())
        chars = unicode(self.win.CHAR_GRP.text())
        char = unicode(self.win.CHAR.text())
        act = unicode(self.win.ACT.text())
        
        if len(path)==0:  
            QMessageBox(QMessageBox.Warning,'Warning!!','Please set the export folder !!').exec_()
            return
        
        if len(chars)==0:  
            QMessageBox(QMessageBox.Warning,'Warning!!','Please set the CharGroup name !!').exec_()
            return
        
        if len(char)==0:  
            QMessageBox(QMessageBox.Warning,'Warning!!','Please set the char name !!').exec_()
            return
        
        if len(act)==0:  
            QMessageBox(QMessageBox.Warning,'Warning!!','Please set the action name !!').exec_()
            return
        
        
        if not os.path.exists(path):
            os.mkdir(path)
        exportPath = path + '\\' + chars 
        if not os.path.exists(exportPath):
            os.mkdir(exportPath)
        exportPath += '\\' + char 
        if not os.path.exists(exportPath):
            os.mkdir(exportPath)
        exportPath += '\\' + act + '.pta'
            
#         导出动画
        ifctl = self.win.IFCTL.isChecked() 
        ifPlayBlast = self.win.IFPLAYBLAST.isChecked()
        ia.exportAnim(exportPath,ifctl,ifPlayBlast)
        
    
    def help(self):
        os.startfile(u'Z:/Resource/Groups/IT/TD/TD/Help/环球帮助/oneNote输出文档/动作库.mht')
    
    def urlChanged(self,text):
        self.URL = unicode(text)
        self.setMyList()            # 设置MyList
        
    def setMyList(self):            # 设置MyList    
        self.win.TAB.clear()
        self.win.LIST.clear()
        widgetList = []         # [['Z:\Scratch\Simon\动画库\YODA','YODA'],['Z:\Scratch\Simon\动画库\Wu','Wu']]
        
        # 1.获取动作库目录下的目录列表
        if os.path.exists(self.URL):
            for folder in os.listdir(self.URL):
                longPath = os.path.join(self.URL,folder)
                if os.path.isdir(longPath):
                    widgetList.append([ longPath , folder])
        
        # 2.设置左侧的动作库列表
        for w in widgetList:
            item = QListWidgetItem (w[1])
            item.setToolTip(w[0])
            self.win.LIST.addItem(item)
    
         
    def MyListClicked(self,item):
        self.win.TAB.clear()
        
        # 1.查找目录下所有角色文件夹。
        charFolder = unicode(item.toolTip())

        characters = []                 # [[u'Z:\\Projects\\YODA\\YODA_Scratch\\Animation\\Nya\\NYA', u'NYA']]
        if os.path.exists(charFolder):
            for folder in os.listdir(charFolder):
                longPath = os.path.join(charFolder,folder)
                if os.path.isdir(longPath):
                    characters.append([ longPath , folder])      
        
        # 2.创建Tab
        for char in characters:
            tabWidget = MyTab(char[0],self.win)
            
            tabWidget.MVC_V.OnClicked[str,list].connect(self.leftRightCMD)
            self.win.TAB.addTab(tabWidget,char[1])
            
            
    def leftRightCMD(self,left_right,datas):
        if left_right == 'left':
            for data in datas[1:]:
                label = os.path.split(data)[1]
                if label[-4:].lower() in ['.avi','.mov']:
                    self.setupPlayer('left',data,datas)
        else:
            self.createRightMenu(datas) 
            
            
    def createRightMenu(self,datas):
        menu = QMenu()
        for data in datas[1:]:
            label = os.path.split(data)[1]
            
            if label[-4:].lower() == '.pta':
                action = QAction(self)
                menu.addAction(action)
                action.setText(u'导入动画')
                path_S = data
                
                ifctl = self.win.IFCTL.isChecked()           # 判断导出到 角色 或 选择的曲线
                
                ifTimeRange = self.win.IFRANGE.isChecked()
                start = self.win.START.value()
                end = self.win.END.value()
                curveRange = []                              # 帧数范围，如果是整个曲线，范围为"[]"
                showError = self.win.IFSHOW_ERROR.isChecked()
                if ifTimeRange:    curveRange =[start,end]
                    
                ifConnect = self.win.IFCONNECT.isChecked()
                action.triggered.connect(lambda: ia.importAnim(path_S,ifctl=ifctl,ifConnect=ifConnect,
                                                               curveRange=curveRange,showError=showError))
                
            elif label[-4:].lower() == '.avi':
                action = QAction(self)
                menu.addAction(action)
                action.setText(u'打开AVI')
                path_a = data
                action.triggered.connect(lambda:os.startfile(path_a))
                
                action_L = QAction(self)
                menu.addAction(action_L)
                action_L.setText(u'    左边播放AVI')
                path_L = data
                action_L.triggered.connect(lambda:self.setupPlayer('left',path_L,datas))

                action_R = QAction(self)
                menu.addAction(action_R)
                action_R.setText(u'    右边播放AVI')
                path_R = data
                action_R.triggered.connect(lambda:self.setupPlayer('right',path_R,datas))
                
                
            elif label[-4:].lower() == '.mov':
                action = QAction(self)
                menu.addAction(action)
                action.setText(u'打开MOV')
                cmdM = data
                action.triggered.connect(lambda:os.startfile(cmdM))
        
        menu.exec_(QPoint(QCursor.pos()))





    
    def setupPlayer(self,left_right,path,datas):
        '''
        创建一个视频播放器控件，返回它的视频和控件
        '''
        if left_right == 'left':
            for a in self.win.Layout_L.children():
                if a.__class__.__name__ == 'VideoPlayer':
                    a.deleteLater()
            self.player_L = VideoPlayer(path,self.createRightMenu,datas)
            self.win.Layout_L.layout().addWidget(self.player_L)
        else:
            for a in self.win.Layout_R.children():
                if a.__class__.__name__ == 'VideoPlayer':
                    a.deleteLater()
            self.player_R = VideoPlayer(path,self.createRightMenu,datas)
            self.win.Layout_R.layout().addWidget(self.player_R)


#===============================================================================
#     <<<<<<    角色的动作标签    >>>>>>  
#===============================================================================
class MyTab(QWidget):
    def __init__(self,dir,win):
        super(MyTab, self).__init__()
        self.supportType = ['.avi','.bmp','.pta','.mov']
        self.dir = dir
        
        # 1.查找给定目录下所有的符合扩展名的文件。
        self.supportFiles = self.findSupportFiles()
        
        # 2.通过支持的文件类型，获得整理好的文件结构清单
        self.list = self.sortFile(self.supportFiles)
                
        # 3.通过 self.list ,创建一个TableView     ****************  重要  ********************
        self.MVC_V = MVC_V(win)
        model = MVC_M(self.list)
        self.MVC_V.setModel(model)
        
        # 4.创建一个Layout
        self.layout = QVBoxLayout(self)

        # 5.在layout里加入TableView
        self.layout.setContentsMargins (0,0,0,0)
        self.layout.setSpacing(0)
        self.layout.addWidget(self.MVC_V)

    
    def findSupportFiles(self):
        '''
        在一堆文件里查找支持的文件
        '''
        supportFiles = []
        for d in os.listdir(self.dir):
            longPath = os.path.join(self.dir,d)
            if os.path.isfile(longPath):
                extendName = os.path.splitext(longPath)[1]
                if  extendName.lower() in self.supportType:
                    supportFiles.append( longPath)       
        return supportFiles
        
    def sortFile(self,fileList):
        '''
        将支持的文件列表按文件名分组排序
        例：
        list = ['d:\a.avi','d:\a.bmp','d:\a.pta','d:\b.bmp','d:\c.avi']
        sortFile(list)
        Result:    [
                        ['d:\a.avi','d:\a.bmp','d:\a.pta'],
                        ['d:\b.bmp'],
                        ['d:\c.avi'],
                    ]
        '''
        tmp = {}
        
        # 找到所有的pta文件，先存到一个list里，准备做为字典的key
        pta_List = []
        
        # 剩下的文件类型放到一个list里
        graphic_List = []
        
        
        for f in fileList:
            if f[-4:].lower() == '.pta':
                pta_List.append(f)
            else:
                graphic_List.append(f)
                
        # 把pta文件 做为字典的key
        for pta in pta_List:
            name = os.path.split(pta)[1].split('.')[0]
            tmp[name] = [pta]
        
        # 把文件名一样的bmp，avi，mov等，放到相应的字典里
        for graphic in graphic_List:
            name = os.path.split(graphic)[1].split('.')[0]
            for key in tmp.keys():
                if name.lower() == key.lower():
                    tmp[key].append(graphic)
        
        # 把所有key对应的value前插入key，然后输出到finalList
        finalList = []
        for key in tmp.keys():
            x = tmp[key]
            x.insert(0,key)
            finalList.append(x)

        # list排序
        finalList.sort()
        return finalList
        '''
            print finalList
            Result ====================:
            [
                ['a','d:\a.pta','d:\a.bmp','d:\a.avi'],
                ['b','d:\b.pta'],
                ['c','d:\c.pta']
            ]
        '''
        
        
        
#===============================================================================
#      <<<<<<    播放器    >>>>>>  
#===============================================================================
class VideoPlayer(QWidget):   
    def __init__(self, url,function,datas):
        super(VideoPlayer, self).__init__()    
        
        self.url = url
        self.datas = datas
        self.createRightMenu = function
        self.loopTimes = 10000

        self.mSrc = Phonon.MediaSource(self.url)
        
        self.player = Phonon.VideoPlayer(Phonon.VideoCategory,self)
        self.player.load(self.mSrc)
        self.player.mediaObject().tick.connect(self.tock)
        self.player.mediaObject().stateChanged.connect(self.stateChanged)


        self.playPause_bt = QPushButton(self)
        self.playPause_bt.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playPause_bt.clicked.connect(self.playClicked)
        
        self.loopPlay_cb = QCheckBox()
        self.loopPlay_cb.setChecked(1)
        self.loopPlay()
        self.loopPlay_cb.clicked.connect(self.loopPlay)

        self.setupUI()
        self.player.setMinimumWidth(150)
        self.player.setMinimumHeight(200)
        self.player.play()
        
    def loopPlay(self):
        onOff = self.loopPlay_cb.isChecked()
        if onOff:
            self.player.load(self.mSrc)
            self.player.mediaObject().enqueue ([self.mSrc for i in range(self.loopTimes)])
        else:
            self.player.mediaObject().clearQueue()

    def playClicked(self):
        
        if self.player.mediaObject().state() == Phonon.PlayingState:
            self.player.pause()
        elif self.player.mediaObject().state() == Phonon.StoppedState:
            self.player.play()
        elif self.player.mediaObject().state() == Phonon.PausedState:
            if self.player.mediaObject().currentTime()==self.player.mediaObject().totalTime():
                self.player.mediaObject().seek(0)
            self.player.play()
    
    def mousePressEvent(self,QMouseEvent):
        QWidget.mousePressEvent(self,QMouseEvent)
        if QMouseEvent.button() == 1:
            self.playClicked()
        elif QMouseEvent.button() == 2:
            self.createRightMenu(self.datas)

    
    def stateChanged(self, new, old):
        if new == Phonon.PlayingState:
            self.playPause_bt.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.playPause_bt.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))

    def setupUI(self):
        self.slider = Phonon.SeekSlider(self.player.mediaObject() , self)
        self.status = QLabel(self)
        self.status.setMinimumWidth(50)
        self.status.setMinimumHeight(20)
        self.cycleLabel = QLabel('loop')
        topLayout = QVBoxLayout(self)
        topLayout.addWidget(self.player)
        topLayout.setContentsMargins(0,0,0,0)
        topLayout.setStretch(0,1)
        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.addWidget(self.playPause_bt)
        layout.addWidget(self.cycleLabel)
        layout.addWidget(self.loopPlay_cb)
        layout.addWidget(self.slider)
        layout.addWidget(self.status)
        topLayout.addLayout(layout)
        self.setLayout(topLayout)
        
    def tock(self, time):
        w = time%1000
        time = time/1000
        h = time/3600
        m = (time-3600*h) / 60
        s = (time-3600*h-m*60)
        self.status.setText('%02d:%02d:%03d'%(m,s,w))       
        
        
        
#===============================================================================
#      <<<<<<    图标显示    >>>>>>  
#===============================================================================
class MVC_M(QAbstractListModel):          
    def __init__(self ,datain ):
        super(MVC_M, self).__init__()
        self.datas = datain
        self.size = 64


    def rowCount(self, index=QModelIndex()):               # 设置有多少个数据  
        return len(self.datas)

    def data(self, index, role=Qt.DisplayRole):            # 数据的具体格式：对齐，显示，内容，范围等等。。。
        row = index.row()
        if role == Qt.DisplayRole:
            return self.datas[row][0]
        
        elif role == Qt.SizeHintRole:                      # 单元格大小
            return QSize(self.size+2,self.size+18)

        elif role == Qt.DecorationRole:                    # 图标
            bmp = ''
            for d in self.datas[row]:
                if d[-4:].lower() == '.bmp':
                    bmp = d
                    break
            pixmap = QPixmap(bmp)
            new = pixmap.scaled(64,64)
            icon = QIcon(new)
            return icon
        
        elif role == Qt.ToolTipRole:                       # 提示
            pta = ''
            for d in self.datas[row]:
                if d[-4:] == '.pta':
                    pta = os.path.splitext(os.path.split(d)[1])[0]  # 分割出短名
                    break
            return pta
        
        elif role == Qt.FontRole:                          # 字体大小
            return QFont("myFontFamily",pointSize = 9)



#===============================================================================
#      <<<<<<    显示    >>>>>>  
#===============================================================================
class MVC_V(QListView):
    OnClicked = pyqtSignal(str,list)
    def __init__(self,win,parent = None):
        super(MVC_V,self).__init__()
        self.win = win
        self.setViewMode(QListView.IconMode)
        self.setIconSize(QSize(150,150))
        self.setMouseTracking(1)                                    # 打开鼠标追踪，为了mouseMoveEvent可以实时查询鼠标位置
        self.lastModelIndex = ''
        self.currentModelIndex = ''
        
        self.clicked.connect(self.leftOrRight)
        self.mouse = ''
        self.currentSelectData = ''

        
    def mousePressEvent(self,QMouseEvent):
        QListView.mousePressEvent(self,QMouseEvent)
        self.mouse = QMouseEvent.button()
        
    # 判断左右键
    def leftOrRight(self,QModelIndex):
        
        index = QModelIndex.row()                                   # 选中的序号
        datas = self.model().datas[index]           # 选中的序号对应的数据
        
        if self.mouse == Qt.LeftButton:
            self.OnClicked.emit('left',datas)       # 播放动画
        elif self.mouse == Qt.RightButton:
            self.OnClicked.emit('right',datas)      # 创建菜单            
            
    
    
    def mouseMoveEvent(self,QMouseEvent):
        QListView.mouseMoveEvent(self,QMouseEvent)
        self.lastModelIndex = self.currentModelIndex
        self.currentModelIndex = self.indexAt(QMouseEvent.pos())

                
    def leaveEvent(self,QEvent):
        QListView.leaveEvent(self,QEvent)
    








def main():
    #    关闭存在的窗口
    for widget in qApp.allWidgets():
        if widget.objectName() == 'PoseLibrary':
            widget.close()
    if 'maya.exe' in sys.executable:
        global PlutoAnimLibrary
        PlutoAnimLibrary = MainWindow(parent = getMayaWindow())
        PlutoAnimLibrary.show()
    else:
        app = QApplication(sys.argv)
        PlutoAnimLibrary = MainWindow()
        PlutoAnimLibrary.show()
        sys.exit(app.exec_())         
    
        
if __name__ == "__main__":
    main()
    