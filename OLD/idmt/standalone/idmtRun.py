# -*- coding: utf-8 -*-
# Copyright (C) 2000-2015 IDMT. All rights reserved.
'''
'''
__author__    = 'huangzhongwei@idmt.com.cn'
__date__    = '2015-11-27'

import json
import os
import socket
import sys
import threading
import time

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *

try:
    _fromUtf8 = QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

port0 = 8270
port = 8271

class Dialog(QDialog):
    def __init__(self, parent = None):
        super(Dialog, self).__init__(parent)
        self.setObjectName(_fromUtf8(u"GDCminiBox"))
        self.setWindowTitle(_fromUtf8(u"GDC"))
        windowFlags = self.windowFlags()
        windowFlags = windowFlags & ~Qt.WindowContextHelpButtonHint    # 去掉帮助按钮
        windowFlags = windowFlags | Qt.WindowMinimizeButtonHint        # 最小化按钮
        windowFlags = windowFlags | Qt.WindowStaysOnTopHint
        self.setWindowFlags(windowFlags)
        #self.setAttribute(Qt.WA_DeleteOnClose)
        self.resize(720, 405)
        webView = QWebView()
        #webView.load(QUrl("file:///E:/Noname3.html"))
        webView.load(QUrl("http://info-srv/TD/box.jpg"))

        gridLayout = QGridLayout()
        gridLayout.addWidget(webView)
        self.setLayout(gridLayout)

class myApplication(QApplication):
    def __init__(self, argv, s0):
        super(myApplication, self).__init__(argv)
        self.s0 = s0

        self.dialog = None
        self.connect(self, SIGNAL("box"), self.box)

        self.connect(self, SIGNAL("shutdown"), self.shutdown)
        self.connect(self, SIGNAL("restart"), self.restart) 

        self.thread = threading.Thread(target = self.pump, args = ())
        self.thread.start()

    def pump(self):
        global stop
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        s.bind(('', port))
        while not stop:
            message, address = s.recvfrom(8192)
            cmd = json.loads(message)
            print cmd
            stop = (cmd["cmd"] in [u"shutdown", u"restart"])
            self.emit(SIGNAL(cmd["cmd"]), cmd, address)
        s.close()

    def box(self, cmd, address):
        #if os.getenv('USERNAME') != "huangzhongwei":
        #    return
        #if self.dialog:
        #    try:
        #        self.dialog.close()
        #        #self.dialog = None
        #    except:
        #        pass
        dialog = Dialog()
        dialog.exec_()

    def shutdown(self, cmd, address):
        self.quit()

    def restart(self, cmd, address):
        s0.close()
        python = sys.executable
        os.execl(python, python, * sys.argv)

if __name__ == "__main__":
    host = socket.gethostname()
    s0 = socket.socket()
    try:
        s0.bind((host, port0))
    except:
        sys.exit()

    global stop
    stop = False
    app = myApplication(sys.argv, s0)
    while not stop:
        app.exec_()

    s0.close()