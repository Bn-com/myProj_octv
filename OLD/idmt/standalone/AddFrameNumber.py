# -*- coding: utf-8 -*-

import glob
import json
import os
import re
import subprocess
import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import uic
import sip

import idmt.pipeline.service

try:
    _fromUtf8 = QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

__ffmpeg__ = "\\\\file-cluster\\GDC\\Resource\\Support\\ffmpeg-20140818-git-3c19744-win64-static\\bin\\ffmpeg.exe"
__ffprobe__ = "\\\\file-cluster\\GDC\\Resource\\Support\\ffmpeg-20140818-git-3c19744-win64-static\\bin\\ffprobe.exe"

class ColorPicker(QLabel):
     def __init__(self, parent = None, color = Qt.white):
        super(ColorPicker, self).__init__(parent)
        self.setFrameStyle(QFrame.Sunken | QFrame.Panel)
        self.color = color
        self.update()

     def mouseReleaseEvent(self, event):
         color = QColorDialog.getColor(self.color, self)
         if color.isValid():
             self.color = color
             self.update()
             registery = idmt.pipeline.service.Service()
             registery.RegSetValue('AddFrameNumber/fontcolor', color.name())

     def update(self):
         self.setText(self.color.name().toUpper())
         self.setPalette(QPalette(self.color))
         self.setAutoFillBackground(True)

class AddFrameNumber(QDialog):
    def __init__(self, parent = None):
        super(AddFrameNumber, self).__init__(parent)
        
        registery = idmt.pipeline.service.Service()
        self.dirSource = registery.RegQueryValue('AddFrameNumber/dirSource', 'E:')
        if not os.path.isdir(self.dirSource):
            self.dirSource = 'E:'
        self.dirDest = None
        
        windowFlags = self.windowFlags()
        windowFlags = windowFlags & ~Qt.WindowContextHelpButtonHint
        windowFlags = windowFlags | Qt.WindowMinimizeButtonHint
        windowFlags = windowFlags | Qt.WindowStaysOnTopHint
        self.setWindowFlags(windowFlags)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setWindowTitle(u"视频加时间帧字幕")
        self.resize(640, 200)
        labelSource = QLabel(u"视频文件：")
        self.editSource = QLineEdit()
        btnBrowse = QPushButton(u"浏览")
        btnBrowse.clicked.connect(self.on_btnBrowse_click)
        labelShot = QLabel(u"镜头号：")
        self.editShot = QLineEdit()
        labelColor = QLabel(u"字幕颜色：")
        fontcolor = QColor()
        fontcolor.setNamedColor(registery.RegQueryValue('AddFrameNumber/fontcolor', '#00FF00'))
        self.colorPicker = ColorPicker(self, fontcolor)
        buttonBox = QDialogButtonBox()
        btnSaveAs = buttonBox.addButton(u"另存", QDialogButtonBox.ApplyRole)
        btnSaveAs.clicked.connect(self.on_btnSaveAs_click)

        gridLayout = QGridLayout()
        gridLayout.addWidget(labelSource, 0, 0, Qt.AlignRight)
        gridLayout.addWidget(self.editSource, 0, 1)
        gridLayout.addWidget(btnBrowse, 0, 2)
        gridLayout.addWidget(labelShot, 1, 0, Qt.AlignRight)
        gridLayout.addWidget(self.editShot, 1, 1)
        gridLayout.addWidget(labelColor, 2, 0, Qt.AlignRight)
        gridLayout.addWidget(self.colorPicker, 2, 1)
        gridLayout.setRowStretch(3, 1)
        gridLayout.addWidget(buttonBox, 4, 0, 1, 3)
        self.setLayout(gridLayout)

    def on_btnBrowse_click(self):
        source = QFileDialog.getOpenFileName(self, directory = self.dirSource, filter = u'视频文件(*.avi;*.mov);;*.*')
        if source == '':
            return
        source = source.replace('/', '\\')
        self.editSource.setText(source)
        dir = os.path.dirname('%s' % source)
        if dir != self.dirSource:
            self.dirSource = dir
            registery = idmt.pipeline.service.Service()
            registery.RegSetValue('AddFrameNumber/dirSource', dir)

    def on_btnSaveAs_click(self):
        source = self.editSource.text().replace('/', '\\')
        if source == '':
            return

        if self.dirDest == None:
            self.dirDest = os.path.dirname('%s' % source)
        filter = re.search(r'[^\.\\\/]+$', source).group()
        dest = QFileDialog.getSaveFileName(self, directory = self.dirDest, filter = u'*.%s' % filter)
        if dest == '':
            return
        self.dirDest = os.path.dirname('%s' % dest)

        color = self.colorPicker.color.name()
        color = color.replace('#', '0x')
        dest = dest.replace('/', '\\')
        if source.compare(dest, Qt.CaseInsensitive) == 0:
            QMessageBox.critical(self, self.windowTitle(), u'不允许直接覆盖原文件')
            return
        codecv = ""
        command = "%s -v quiet -print_format json -show_format -show_streams \"%s\"" % (__ffprobe__, source)
        p = subprocess.Popen(command, shell = True, stdout = subprocess.PIPE)
        info = p.stdout.read()
        codecv = None
        width = 720
        try:
            dt = json.loads(info)
            for stream in dt["streams"]:
                if stream["codec_type"] == "video":
                    codecv = stream["codec_name"]
                    width = stream["width"]
                    break
        except:
            pass
        print codecv
        if codecv == None:
            QMessageBox.critical(self, self.windowTitle(), u'不能获取原文件编码')
            return
        shot = self.editShot.text()
        x = width * 0.4
        command = "%s -y -i \"%s\" -vf drawtext=\"fontfile=\'C\\:/Windows/Fonts/ARIAL.TTF\':fontsize=24:x=0:y=0:fontcolor=%s:text=\'%%{eif\\:n\\:d\\:4}\'\",drawtext=\"fontfile=\'C\\:/Windows/Fonts/ARIAL.TTF\':fontsize=24:x=%d:y=0:fontcolor=%s:text=\'%s\'\" -c copy -c:v %s -q:v 0 -q:a 0 \"%s\"" % (__ffmpeg__, source, color, x, color, shot, codecv, dest)
        print command
        #subprocess.Popen(command, shell = True)
        os.popen(command).read()
        QMessageBox.about(self, self.windowTitle(), u'处理完毕，请检查')

#命令行运行
if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = AddFrameNumber()
    sys.exit(dialog.exec_())