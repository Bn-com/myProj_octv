#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''    
__author__ = 'zhangben'
__mtime__ = '2016/4/12'
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
'''


# -*- coding: utf-8 -*-
import sip
import sys
# from pymel.core import *
# import maya.cmds as mc
import re,os,sys

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from idmt.maya.py_common import sk_referenceConfig;reload(sk_referenceConfig)
from idmt.maya.py_common import sk_infoConfig;reload(sk_infoConfig)
import mi_get_multiCam;reload(mi_get_multiCam)

class QT_MainUI(QMainWindow):
    def __init__(self, parent=None):
        super(QT_MainUI, self).__init__(parent)
        self.ui = mi_get_multiCam.Ui_MainWindow()
        self.ui.setupUi(self)

        # Connection
        # self.myuis.f_cb.clicked.connect(self.xxx)
        #self.myuis.QPB_OK.clicked.connect(self.xxx)

    def xxx(self):
        user_cam_category = self.get_cam_category()
        user_op = self.get_operate()
        #self.mi_multiCam_toggle(user_op,*user_cam_category)
        #print self.myuis.m_cb.isChecked()
        #print(u' cam_category:'),user_cam_category
        # print(u' operation:'),user_op
        print self.ui.rb_rep
    def get_cam_category(self):
        cam_category = []
        if self.ui.f_cb.isChecked():cam_category.append(u'far')
        if self.ui.m_cb.isChecked():cam_category.append(u'mid')
        if self.ui.n_cb.isChecked():cam_category.append(u'near')
        return cam_category
    def get_operate(self):
        if self.ui.rb_add.isChecked():return u'add'
        else:return u'rep'
    def mi_multiCam_toggle(self,operate = u'rep',*cam_category):
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        cams_on_server = self.mi_get_camsOnServer()
        #camServerPath = u'%s/' % os.path.split(use_cam)[0]
        camServerPath = sk_infoConfig.sk_infoConfig().checkCameraServerPath()
        use_cam = ''
        p_cam_path = re.compile(u'%smi_%s_%s_cam[_(near)(far)(mid)]*.ma' % (camServerPath,shotInfo[1],shotInfo[2]))
        cam_refs = [each_ref for each_ref in listReferences() if p_cam_path.search(each_ref.path)]
        if not cam_refs: operate = u'add'# 无则导入参考相机
        if operate == u'add':#===============add  camera  operation ============================
            for each_cam_category in cam_category:
                use_cam_file = self.mi_getuseCam(each_cam_category,cams_on_server)
                mc.file(use_cam_file,reference = 1,ignoreVersion=1,namespace='CAM_%s'%(each_cam_category))
            return
        elif operate == u'rep': # ============replace camera operation ==========================
            if len(cam_category)>1:error(u'======================= more than one Cams you selected to replace referenc =================')
            if len(cam_refs) >1: # 当场景理有多个相机参考时，需要选择要替换的相机
                if not selected() or len(selected()) > 1: error(u'===========there more than one Cam Ref files in ,please select one to replace===================')
                elif not selected()[0].isReferenced() or not selected()[0].referenceFile() in cam_refs:error(u'==== please select cam ref to replace========')
                selected()[0].referenceFile().replaceWith(self.mi_getuseCam(cam_category[0],cams_on_server))
                print(u'==============camera change to %s =================') % cam_category
                #return
            elif len(cam_refs)==1:
                if cam_refs[0].path.find(cam_category[0])== -1: cam_refs[0].replaceWith(self.mi_getuseCam(cam_category[0],cams_on_server))
                else:print(u'======================the %s camera is already in the scene =================================' % (cam_category[0]))
    def mi_getuseCam(self,cam_categroy,cam_files_list):
        for each_cam in cam_files_list:
            if each_cam.find(u'%s' % cam_categroy)!=-1:return each_cam
    def mi_get_camsOnServer(self):
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        projectInfo = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(shotInfo[0])
        # serve目录
        camServerPath = sk_infoConfig.sk_infoConfig().checkCameraServerPath()
        #camServerPath = "//file-cluster/GDC/Projects/"+ projectInfo + "/Project/scenes/Animation/episode_" + shotInfo[1] + "/episode_camera/"
        shot_cam_file = u''
        info = 2
        shotID = u'_'.join(shotInfo[:info+1])
        p_shotId = re.compile(u'%s[_(far),(mid),(near)]*'%(shotID))
        shot_camFiles = []
        for each_camFile in os.listdir(camServerPath):
            if p_shotId.search(each_camFile) and os.path.splitext(each_camFile)[-1] == u'.ma': shot_camFiles.append(u'%s%s'%(camServerPath,each_camFile))
        return shot_camFiles
def main():
    app = QApplication(sys.argv)
    window = QT_MainUI()
    window.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()