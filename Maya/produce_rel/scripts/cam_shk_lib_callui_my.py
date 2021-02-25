#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''    
__author__ = 'zhangben'
__mtime__ = '2016/4/12'
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
'''
import re,os,sys
import sip
# import pymel.core as pm
import maya.cmds as mc
from PyQt4 import QtGui,QtCore,uic
import maya.OpenMayaUI as apiUI

#file_path = os.path.split(os.path.realpath(__file__))[0]
file_path = "E:\MineScript\GDC_Repository\Other\studio_a2\scripts"
qtCreateFile = u'{}\CameraShakeLibrary_MW.myuis'.format(file_path)

Ui_MainWindow,QtBassClass = uic.loadUiType(qtCreateFile)

def getMayaWindow():#=====get maya window
    ptr = apiUI.MQtUtil.mainWindow()
    return sip.wrapinstance(long(ptr),QtCore.QObject)

class CamSkLibMayaWindow(QtGui.QMainWindow,Ui_MainWindow): #  main class process
    def __init__(self, parent=getMayaWindow()):
        QtGui.QMainWindow.__init__(self,parent)
        Ui_MainWindow.__init__(self,parent)
        # super(CamSkLibMayaWindow, self).__init__(parent)
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)
        self.shk_lib_dir = ur'Z:\Resource\Groups\Studio_FantasyImage\TD\a2_work_proj\other'
        # add propety stor shake camera 
        self.shk_cam_file_lst = []
        self.shk_cam_describe_file_lst = []
        self.get_lib_info()        
        # Connection
        self.ui.pb_0.clicked.connect(self.xxx)
        self.update_shk_list()
        # self.myuis.QPB_OK.clicked.connect(self.xxx)
        self.ui.shk_lst.currentItemChanged.connect(self.update_descript)
    def xxx(self):#  only button  command
        sel_item = self.ui.shk_lst.currentItem()
        if sel_item:
            for each_cam in self.shk_cam_file_lst:
                if each_cam.find(sel_item.text())!= -1:
                    print each_cam
                    self.transmit_camShk_aniCvs(each_cam)
    def update_shk_list(self):# update  shake style list on leftside of UI
        for each_mb in self.shk_cam_file_lst:
            p_fn = re.compile(u"[^_]*$")
            shake_style = p_fn.search(os.path.splitext(each_mb)[0]).group()
            self.ui.shk_lst.addItem(shake_style)
    def get_lib_info(self):# get the shake camera library information and storage them to instance variables
        for root,dir,files in os.walk(self.shk_lib_dir):
            for each in files:
                each_full = os.path.join(root,each)
                #print each_full
                if os.path.isfile(each_full) and os.path.splitext(each_full)[1] == '.mb':
                    self.shk_cam_file_lst.append(each_full)
                elif os.path.isfile(each_full) and os.path.splitext(each_full)[1] == '.txt':
                    self.shk_cam_describe_file_lst.append(each_full)
    def update_descript(self):#  right side description area load information
        sel_item =  self.ui.shk_lst.currentItem()
        if sel_item:
            print sel_item.text()
        #self.myuis.desc_text.setText(itemName)
            #print "okokokok"e ,ta
            for each_desc in self.shk_cam_describe_file_lst:
                if each_desc.find(sel_item.text()) != -1:
                    with open(each_desc) as read_desc:
                        data = read_desc.read()
                        #print data
                        self.ui.desc_text.setText(QtCore.QString(unicode(data,'gb2312','ignore')))
    ######======================under is main code of maya opration===========================================
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