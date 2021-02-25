#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = call_doWin
__author__ = zhangben 
__mtime__ = 2019/3/27 : 12:22
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
"""

from myuis import doWin_ui
reload(doWin_ui)

import PyQt4.QtGui as qg
import PyQt4.QtCore as qc
import maya.OpenMayaUI as mui
import sip
import pymel.core as pm


def getMayaWindow():
    """
    get the maya main window as a QMainWndow instance
    :return:
    """
    ptr = mui.MQtUtil.mainWindow()
    return sip.wrapinstance(long(ptr),qc.QObject)


class Call_doWin(qg.QMainWindow,doWin_ui.Ui_doWin):
    def __init__(self,parent=getMayaWindow()):
        super(Call_doWin,self).__init__(parent)
        self.setupUi(self)

        self.add_bt.clicked.connect(self.get_sel_rb)

    def rt_selsnm(self):
        sels = pm.selected()
        rtlst = [easl.name() for easl in sels]

        cmdStr = " -root {}".format(" -root \n".join(rtlst))
        print rtlst
        self.cmdStr_l.setText(cmdStr)
        return cmdStr

    def get_sel_rb(self):
        str = self.mod_grp.checkedButton().text()
        if str=='reference':print "Ref"
        elif str =='import':print "IMP"

    def get_bx_sel_rb(self):
        selRb = None
        if self.bx_im_rb.isChecked():
            s = self.bx_im_rb.text()
            selRb = unicode(s, 'utf-8', 'ignor')
        elif self.bx_rf_rb.isChecked():
            s = self.bx_rf_rb.text()
            selRb = unicode(s, 'utf-8', 'ignor')
        print selRb

