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
import re
import sys
import sip

import pymel.core as pm
import maya.cmds as mc
from PyQt4 import QtGui,QtCore
import maya.OpenMayaUI as apiUI

from  Other.studio_a2.scripts import ui_CameraShakeLibrary_MW;reload(ui_CameraShakeLibrary_MW)

def getMayaWindow():
    ptr = apiUI.MQtUtil.mainWindow()
    return sip.wrapinstance(long(ptr),QtCore.QObject)

class CamSkLibMayaWindow(QtGui.QMainWindow):
    def __init__(self, parent=getMayaWindow()):
        super(CamSkLibMayaWindow, self).__init__(parent)
        self.ui = ui_CameraShakeLibrary_MW.Ui_MainWindow()
        self.ui.setupUi(self)
        self.shk_cams_dir = ur'Z:\Resource\Groups\Studio_FantasyImage\TD\a2_work_proj\other'
        # Connection
        self.ui.pb_0.clicked.connect(self.xxx)
        # self.myuis.QPB_OK.clicked.connect(self.xxx)
    def xxx(self):
        print 'Hahaha'
        cam_file_path = '{}\\cam_sk_fighting.mb'.format(self.shk_cams_dir)
        print cam_file_path
        self.transmit_camShk_aniCvs(cam_file_path)
    def transmit_camShk_aniCvs(self,shk_cam_file,paste_key_time=None):
        #paste_key_time = 0
        cam_ns = 'shk_cam'
        #current_proj_dir = pm.workspace(query=True,dir=1)
        #shk_cam_file = '{}cam_sk_fighting.mb'.format(current_proj_dir)
        #os.path.isfile(shk_cam_file)
        select_cam = ''
        try:
            select_cam = pm.selected()[0]
        except IndexError,e:
            print e.message
            pm.error('Please select the camera to add shakeData')
        pm.importFile(shk_cam_file,i = True, namespace=cam_ns)
        shk_cam_imp_nd = [self.get_root(each_cam) for each_cam in pm.ls('{}:*'.format(cam_ns),ca=True)]
        shk_cam_imp_trans_nd = [shk_cam_imp_nd[i] for i in range(len(shk_cam_imp_nd)) if shk_cam_imp_nd[i] not in shk_cam_imp_nd[:i]]
        if not paste_key_time: paste_key_time = mc.playbackOptions(min=True,q=True)
        temLoc = pm.spaceLocator(name = 'temp_loc',p = (0,0,0))
        store_attr_aniCvs  = self.trans_ani_curves(select_cam,temLoc,paste_key_time)
        for each_at in store_attr_aniCvs:
            if re.search(u'[s]+[x-z]+',each_at.attrName()):each_at.set(1)
            else:each_at.set(0)
        cam_grp_node = pm.group(n='{}_grp'.format(select_cam.name()),em=True,w=True)
        pm.parent(select_cam,cam_grp_node)
        cam_grp_node.rename(select_cam.name())
        self.trans_ani_curves(shk_cam_imp_trans_nd[0],select_cam,paste_key_time)
        self.trans_ani_curves(temLoc,cam_grp_node,paste_key_time)
        pm.delete(temLoc)
        pm.delete(shk_cam_imp_trans_nd)
        pm.namespace(removeNamespace = 'shk_cam',dnc=True)
    def trans_ani_curves(self,sourceObj,targetObj,paste_key_time,re_attr = u'source'):#sourceObj,targetObj = shk_cam_imp_trans_nd[0],select_cam
        aniCurve_types = [u'animCurveTL', u'animCurveTU', u'animCurveTA']
        p_tr_at = re.compile(u'[trs]+[x-z]+')
        ani_curves_dict = dict([each_con for each_con in sourceObj.listConnections(c=True) if pm.nodeType(each_con[1]) in aniCurve_types and  p_tr_at.search(each_con[0].attrName())])
        attr_list = [each_at.attrName() for each_at in ani_curves_dict.keys()]
        for each_at_aniCvs in ani_curves_dict:
            pm.selectKey(ani_curves_dict[each_at_aniCvs])
            pm.copyKey()
            attr_name = each_at_aniCvs.attrName()
            pm.pasteKey(targetObj,at = attr_name,t = (paste_key_time,paste_key_time))
        pm.selectKey(ani_curves_dict.values())
        pm.cutKey(clear=True)
        if re_attr == u'source':return ani_curves_dict.keys()
        else:return dict([each_con for each_con in targetObj.listConnections(c=True) if pm.nodeType(each_con[1]) in aniCurve_types and  p_tr_at.search(each_con[0].attrName())]).keys()
    def get_root(self,nodeName):
       # nodeName = each_cam
        rt_nm = nodeName
        pr_nd = nodeName.getParent()
        while pr_nd:
            rt_nm = pr_nd
            pr_nd = rt_nm.getParent()
        return rt_nm

def main():
    # app = QtCore.QCoreApplication(sys.argv)
    window = CamSkLibMayaWindow()
    window.show()
    # sys.exit(app.exec_())

if __name__ == '__main__':
    main()