# -*- coding: utf-8 -*-

# Copyright (C) 2000-2014 IDMT. All rights reserved.
'''
介绍:
此工具用来同步TD文件
编译方式：
E:\PyInstaller-2.1>python pyinstaller.py --onefile --windowed --icon=idmtSourceSafe.ico D:\Pluto\workspace\PlutoPip\MyLib\Utility\zzjIDMTSync.py
'''
__author__ = 'zhaozhongjie'
__date__ = '2014-03-26'


import sip
import re
sip.setapi('QString', 2)
sip.setapi('QVariant', 2)
import os , sys , datetime

from PyQt4.QtGui import *
from PyQt4.QtCore import *



class DropArea(QLabel):                                         #    <<<<<<    鼠标拖拽区域    >>>>>> 
    changed = pyqtSignal(QMimeData)
    
    def __init__(self, parent=None):
        super(DropArea, self).__init__(parent)
        self.setFrameStyle(QFrame.Sunken | QFrame.StyledPanel)
        self.setAlignment(Qt.AlignLeft)
        self.setAcceptDrops(True)
        self.setAutoFillBackground(True)
        self.clear()
        
    def dragEnterEvent(self, event):
        event.acceptProposedAction()

    def dropEvent(self, event):
        mimeData = event.mimeData()
        if mimeData.hasUrls():
            path = []
            for url in mimeData.urls():
                path.append(os.path.abspath(url.toLocalFile()))
            self.setText('\n'.join(path))

    def clear(self):
        self.setText(u"")
        self.setBackgroundRole(QPalette.Dark)

      
class WindowForm(QWidget):                                      #    <<<<<<    主界面    >>>>>>  
    '''
        #===========================================================================================
        #
        #                             OUTPUT    （信息反馈窗口）
        #        
        #===========================================================================================
        #                               B    (用户指定上传路径窗口)
        #===========================================================================================
        #
        #                               C1    (拖拽区域)
        #
        #===========================================================================================
        #
        #                               C2    (路径粘贴区域)
        #
        #===========================================================================================
        #                                                 CLEAN_A   CLEAN_B   CLEAN_C   CLEAN_D
        #===========================================================================================
        #                                                                 同步    退出
        #===========================================================================================
        
        程序设计思路：
        1.主窗口中，一个信息反馈框，三个输入框，做好三个输入框的输入过滤
        2.合并 C1 和 C2 区域中的文件列表，去重，去空。
        3.确定同步目录
        4.开始同步
        
    '''
    def __init__(self):                                         #    ------    初始化
        super(WindowForm, self).__init__()

        self.CREATE_UI()
        self.SET_LAYOUT()
        self.CONNECT()

        font = QFont()
        font.setPointSize(10)
        self.setFont(font)

        self.setWindowTitle(u"TD同步文件")
        self.resize(550, 800)  
              
    def CREATE_UI(self):                                        #    ------    创建控件
    #    1.信息反馈窗口
        self.OUTPUT = QTextEdit()
        self.OUTPUT.setStyleSheet("background:rgb(200, 200, 200)")
        self.OUTPUT.setReadOnly(1)

    #    2.用户指定上传路径窗口
        self.B = QLineEdit()

    #    3.拖拽区域
        self.C1 = DropArea()

    #    4.路径粘贴区域
        self.C2 = QTextEdit()

    #    5.清空，同步，退出按钮
        self.clearAButton = QPushButton(u"清空")
        self.clearAButton.setMaximumSize(QSize(40,20))
        self.clearBButton = QPushButton(u"清空")
        self.clearC1Button = QPushButton(u"清空")
        self.clearC1Button.setMaximumSize(QSize(40,20))
        self.clearC2Button = QPushButton(u"清空")
        self.clearC2Button.setMaximumSize(QSize(40,20))

        self.goButton = QPushButton(u"同步")
        self.quitButton = QPushButton("Quit")


        self.buttonBox = QDialogButtonBox()
        self.buttonBox.addButton(self.goButton, QDialogButtonBox.ActionRole)
        self.buttonBox.addButton(self.quitButton, QDialogButtonBox.RejectRole)

    def B_Filter(self):                                            #    ------    B窗口内容过滤器
        self.B.editingFinished.disconnect(
            self.B_Filter)
        text = self.B.text()
        if os.path.isdir(text):
            self.B.setText(text)

        else:
            self.B.setText('')
        self.B.editingFinished.connect(
            self.B_Filter)

    def C2_Filter(self):                                        #    ------    C2窗口内容过滤器
        self.C2.textChanged.disconnect(self.C2_Filter)
        text = self.C2.document().toPlainText()
        text_split = text.split('\n')

        exist_Paths = []

        for t in text_split:
            tt = t.strip(' ')           #    去除前后空格
            if os.path.isfile(tt) or os.path.isdir(tt):     #    文件盒文件夹都允许
                exist_Paths.append(os.path.abspath(tt))
        exist_Path = '\n'.join(exist_Paths)

        self.C2.setText(exist_Path)
        self.C2.textChanged.connect(
            self.C2_Filter)

    def SET_LAYOUT(self):                                       #    ------    设置控件位置
        infoLayout = QHBoxLayout()
        infoLayout.addWidget(QLabel(u'<h4>反馈消息：</h4>'))
        infoLayout.addWidget(self.clearAButton)
        
        fileLayout = QHBoxLayout()
        fileLayout.addWidget(QLabel(u'<h4>鼠标拖文件框：</h4>'))
        fileLayout.addWidget(self.clearC1Button)

        fileLayout2 = QHBoxLayout()
        fileLayout2.addWidget(QLabel(u'<h4>路径粘贴框：</h4>'))
        fileLayout2.addWidget(self.clearC2Button)
        
        
        mainLayout = QVBoxLayout()
        mainLayout.addLayout(infoLayout)
        mainLayout.addWidget(self.OUTPUT)
        mainLayout.addWidget(QLabel(u'<h4>指定渲染输出路径(如不指定，根据maya文件设定来)：</h4>'))
        mainLayout.addWidget(self.B)
        
        mainLayout.addLayout(fileLayout)
        mainLayout.addWidget(self.C1)
        
        mainLayout.addLayout(fileLayout2)
        mainLayout.addWidget(self.C2)
        
        mainLayout.addWidget(self.buttonBox)
        mainLayout.setStretch(0, 0)
        mainLayout.setStretch(1, 1)
        mainLayout.setStretch(2, 0)
        mainLayout.setStretch(3, 1)
        mainLayout.setStretch(4, 0)
        mainLayout.setStretch(5, 1)
        mainLayout.setStretch(6, 0)
        mainLayout.setStretch(7, 1)
        mainLayout.setStretch(8, 1)
        self.setLayout(mainLayout)

    def CONNECT(self):                                          #    ------    链接按钮
        
        self.C2.textChanged.connect(self.C2_Filter)
        self.B.editingFinished.connect(self.B_Filter)

        self.quitButton.clicked.connect(self.close)

        self.clearAButton.clicked.connect(self.OUTPUT.clear)
        self.clearBButton.clicked.connect(lambda:self.B.setText(''))
        self.clearC1Button.clicked.connect(self.C1.clear)
        self.clearC2Button.clicked.connect(lambda:self.C2.setText(''))
        

class TDSync(WindowForm):                                       #    <<<<<<    核心函数    >>>>>>
    def __init__(self):                                         
        super(TDSync, self).__init__()          #    继承主界面
        self.goButton.clicked.connect(self.GO)                  

    def GET_CList(self):                                        #    ------    获得文件上传列表
    #    合并两个C区的文件列表。
        C1_text = self.C1.text()
        C2_text = self.C2.document().toPlainText()
        
        C_text = C1_text + '\n' + C2_text
        C_List = C_text.split('\n')

    #    去重
        C_List = [ C_List[i] for i in range(len(C_List)) if C_List[i] not in C_List[:i]]
        
    #    去空
        C_List = [ C_List[i] for i in range(len(C_List)) if len(C_List[i]) ]

        return C_List

    def CALC_Target_Path(self,path,c_path):                            #    ------    求同步的目标路径
        '''
            如果存在B区路径，并且目标路径是一个文件夹的话，那么目标路径必须加上C区路径的最后一段文件夹名
        '''
        sync_A = '\\\\idmt-file09\\support'
        sync_B = '\\\\idmt-file15\\support'
        
        lower_path = path.lower()
        
        if lower_path[:6] not in ['\\\\idmt','\\\\file','z:\\res'] :
            return []
        
        if 'support\\python\\2.' in lower_path and lower_path[-3:] == '.py':
            sync_tmp = []
            sync_tmp.append(re.sub(r'2\.\w*-*\w*','2.4',lower_path,1))
            sync_tmp.append(re.sub(r'2\.\w*-*\w*','2.5',lower_path,1))
            sync_tmp.append(re.sub(r'2\.\w*-*\w*','2.6',lower_path,1))
            sync_tmp.append(re.sub(r'2\.\w*-*\w*','2.4-x64',lower_path,1))
            sync_tmp.append(re.sub(r'2\.\w*-*\w*','2.5-x64',lower_path,1))
            sync_tmp.append(re.sub(r'2\.\w*-*\w*','2.6-x64',lower_path,1))
            sync_tmp.append(re.sub(r'2\.\w*-*\w*','2.7-x64',lower_path,1))
            
            sync_path = []
            for a in sync_tmp:
                sync_path.append(sync_A + '\\'+ a.split('support')[1])
                sync_path.append(sync_B + '\\'+ a.split('support')[1])
            return sync_path
                 
            
            
        elif 'support' in lower_path :
            support_pre_length = len(lower_path.split('support')[0]) + len('support')
            
            sync_A += path[support_pre_length:]
            sync_B += path[support_pre_length:]
            
            if c_path:                                                     #    如果有B区路径
                if os.path.isdir(path):                                    #    如果是文件夹，则需要加上最后一段文件夹名
                    Last_Folder = os.path.split(c_path)[1]                 #    获得目录名
                    
                    sync_A += '\\' + Last_Folder
                    sync_B += '\\' + Last_Folder                
                    
            return [sync_A,sync_B]

    def CHECK_IN_File(self,path,Target):                        #    ------    上传
        #    如果C区是文件夹，用xcopy
        if os.path.isdir(path):
            os.system('xcopy "%s" "%s" /e /s /h /d /y /i /c'%(path , Target ))
            
        #    C区是文件，用copy命令
        elif os.path.isfile(path):        
            newTarget = os.path.dirname(Target) + '\\'          
            print newTarget
            os.system('xcopy "%s" "%s" /y'%(path , newTarget))                

    def GO(self):                                               #    ------    同步按钮
        C_List = self.GET_CList()
        
        B_Path = self.B.text()
        
        for C_Path in C_List:
            
            #    如果B区有路径,则根据B区获得最终上传目标路径：
            Target_Path_List = []
            if B_Path:
                Target_Path_List = self.CALC_Target_Path(B_Path , C_Path)        #    获得最终上传目录List

            #    如果B区没有路径,则根据每个C区的路径获得最终上传目标路径：    
            else:                           
                Target_Path_List = self.CALC_Target_Path(C_Path , 0)            #    获得最终上传目录List
            
            
            if len(Target_Path_List):
                Last_Name = os.path.split(C_Path)[1]
                self.OUTPUT.append(u'同步----->：%s' % (Last_Name))      
                QApplication.processEvents()
                for Target in Target_Path_List:    
                    self.CHECK_IN_File(C_Path, Target)                          #    上传文件
                
        
        CreateTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.OUTPUT.append(u'<font color=red>完成时间：%s</font>' % (CreateTime))

       
        
        


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = TDSync()
    window.show()
    sys.exit(app.exec_())        