#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'zhangben'
__mtime__ = '2017/10/12:16:08'
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
"""
import re
import maya.cmds as mc
import pymel.core as pm
class A2_copyDrivenKey(object):
    def __init__(self):
        self.original_drvnKey_infoDict = {}
    @staticmethod
    def get_drivenKey_information(): # obtain driven key data
        original_grp = pm.ls(sl=True)
        original_grp.reverse()
        original_driver = original_grp[0] # confirm original driver object is select list first item
        #original_driver.listConnections(d=True)
        lst_all_drvKeyPair = original_driver.connections(type='animCurve',s=False,d=True,p=True,c=True)
        drvKey_infor = {}
        for eachPair in lst_all_drvKeyPair:
            #eachPair = lst_all_drvKeyPair[5]
            driver_attr_nm = eachPair[0].attrName(longName=True)
            key_aniCurve = eachPair[1].node()
            driven_attr_info = key_aniCurve.output.outputs(p=True)[0]
            driven_attr_nm = driven_attr_info.longName()
            driven_obj = driven_attr_info.node()
            # dispose driven key data
            if driven_obj not in original_grp[1:]:continue
            #pm.select(key_aniCurve)
            driver_vals = pm.keyframe(driven_attr_info,q=True,fc=True)
            driven_vals = pm.keyframe(driven_attr_info,q=True,vc=True)
            if not drvKey_infor.has_key('{}||{}'.format(driven_obj.name(),original_grp.index(driven_obj))):
                drvKey_infor['{}||{}'.format(driven_obj.name(),original_grp.index(driven_obj))] = [{"driver":{driver_attr_nm:driver_vals},"driven":{driven_attr_nm:driven_vals}}]
            else:
                drvKey_infor['{}||{}'.format(driven_obj.name(),original_grp.index(driven_obj))].append({"driver":{driver_attr_nm:driver_vals},"driven":{driven_attr_nm:driven_vals}})
        return drvKey_infor
    @staticmethod
    def reset_drvnKey_info(single_DrvnKey_Info,assignAttr = None,inverse=False):
        #assignAttr = 'rotateY'
        single_DrvnKey_Info['driven'][single_DrvnKey_Info['driven'].keys()[0]] = [(inverse and -1 or 1)*n for n in single_DrvnKey_Info['driven'].values()[0]]
        if assignAttr:
            single_DrvnKey_Info['driven']= {assignAttr:single_DrvnKey_Info['driven'].values()[0]}
        return single_DrvnKey_Info
    @staticmethod
    def separate_info(drvnK_infDic,hunt_keyword):#from original selected objects obtain set driven keyframe data,contains both driver and drivens attributes & datas
        if isinstance(hunt_keyword,int):
            p_locating = re.compile('[^|]*$')
            for eachDriven in drvnK_infDic:
                if p_locating.search(eachDriven) and int(p_locating.search(eachDriven).group()) == hunt_keyword:
                    return drvnK_infDic[eachDriven]
        else:
            p_locating =  re.compile('[^0-9a-zA-Z]+\w*')
            for eachDriven in drvnK_infDic:
                if p_locating.search(eachDriven) and p_locating.search(eachDriven).group() == p_locating.search(hunt_keyword.nodeName()).group():
                    return drvnK_infDic[eachDriven]
    def record_original_drvn_datas(self):
        self.original_drvnKey_infoDict = self.get_drivenKey_information()
    def copy_past_setDrivenKey(self,byOrder=False,inverse=False):
        #drivenKeyFrame_infoDict = self.get_drivenKey_information()
        target_grp = pm.ls(sl=True)
        target_grp.reverse()
        target_driver = target_grp[0]
        #target_drivens = target_grp[1:]
        #matchStyle = 'name'
        for each_tg_drvn in target_grp[1:]:
            huntKeyWord = byOrder and target_grp.index(each_tg_drvn) or each_tg_drvn
            obtainDrvInfo = self.separate_info(self.original_drvnKey_infoDict,huntKeyWord)
            for each_old_drvnKey in obtainDrvInfo:
                each_drvnKey = self.reset_drvnKey_info(each_old_drvnKey,assignAttr=False,inverse=inverse)
                targ_driven_attr_nm = each_drvnKey['driven'].keys()[0]
                targ_driver_attr_nm = each_drvnKey['driver'].keys()[0]
                driver_v =  each_drvnKey['driver'].values()[0]
                driven_v =  each_drvnKey['driven'].values()[0]
                for  n in range(len(driver_v)):
                    t_driver_at = target_driver.attr(targ_driver_attr_nm)
                    #t_driver_at.set(driver_v[n])
                    pm.setDrivenKeyframe(each_tg_drvn,at = targ_driven_attr_nm,cd = t_driver_at,dv = driver_v[n],v=driven_v[n])

    def gene_target_drvnKey_data(self,orig_dict,byOrder=False):
        target_grp = pm.ls(sl=True)
        target_grp.reverse()
        if len(target_grp) != len(orig_dict.keys())+1:pm.error("Please check target driver and driven objects has the same number as the original")
        target_driver = target_grp[0]
        targ_drvnKey_info_dict = {}
        for each_tg_drvn in target_grp[1:]:
            huntKeyWord = byOrder and target_grp.index(each_tg_drvn) or each_tg_drvn
            obtainDrvInfo = self.separate_info(orig_dict,huntKeyWord)
            targ_drvnKey_info_dict[each_tg_drvn] = obtainDrvInfo
        return {target_driver:targ_drvnKey_info_dict}

class A2_copyDrivenKeyUI(A2_copyDrivenKey):
    def __init__(self):
        super(self.__class__,self).__init__()
        self.obtain_orig_infoDict = {}
        self.gen_targ_infoDict = {}
        self.targ_driver = None
    @staticmethod
    def call_setDrivenKeyToolsUI():
        if pm.window('setDrivenKeyTools_mainWin',exists=True):
            pm.deleteUI('setDrivenKeyTools_mainWin',window=True)
        pm.window('setDrivenKeyTools_mainWin',title='Copy SetDrivenKey Tools')
        pm.formLayout('main_form')
        pm.button('rec_bt',l='Select Original And PUSH',c = 'import Other.studio_a2.scripts.RIG.A2_copyDrivenKey as acdk\nreload(acdk)\nins_ui = acdk.A2_copyDrivenKeyUI()\nins_ui.load_original_data_btCMD()')
        pm.optionMenuGrp('order_omg',l='Order Method')
        pm.menuItem(l='by driven name')
        pm.menuItem(l='by select order')
        pm.button('tag_bt',l='Select Target And PUSH',c = 'ins_ui.list_target_data_btCMD()')
        pm.button('cpy_all_bt',l='Copy All SetDrivenKeyFrames',c = 'ins_ui.copy_all_BT_cmd()')
        pm.scrollLayout('main_scr',horizontalScrollBarThickness=16,verticalScrollBarThickness=16,w=800,h=500)
        pm.frameLayout('main_frame',lv = False,bv=True)
        pm.setParent('..')
        pm.formLayout('main_form',e=True,attachForm = [('rec_bt','top',5),('rec_bt','left',15),('tag_bt','top',5),('order_omg','top',5),
                ('main_scr','left',5),('main_scr','right',5),('cpy_all_bt','top',5),('cpy_all_bt','right',5)],
                attachControl = [('main_scr','top',15,'rec_bt'),('order_omg','left',25,'rec_bt'),('tag_bt','left',25,'order_omg'),
                ('tag_bt','right',25,'cpy_all_bt')])
        mc.showWindow('setDrivenKeyTools_mainWin')
    @staticmethod
    def derive_attrGrp_info(drvn_attr_nm):
        get_attr_list = ['{}{}'.format(re.search('[^X-Z]+',drvn_attr_nm).group(),eachAxis) for eachAxis in ['X','Y','Z']]
        return {get_attr_list.index(drvn_attr_nm)+1:get_attr_list}
    @staticmethod
    def by_order():
        return pm.optionMenuGrp('order_omg',q=True,v=True) == 'by select order'
    def load_original_data_btCMD(self):#select original dirver and drivens objects,and then load the datas
        self.obtain_orig_infoDict = super(A2_copyDrivenKeyUI,self).get_drivenKey_information()
        print("Record Original set driven key datas!!!!")
        print self.obtain_orig_infoDict.keys()


    def list_target_data_btCMD(self):
        self.gen_targ_infoDict = super(A2_copyDrivenKeyUI,self).gene_target_drvnKey_data(self.obtain_orig_infoDict,self.by_order())
        #print target_drvnKey_infoDict.keys()
        self.targ_driver = self.gen_targ_infoDict.keys()[0]
        targ_drvn_data = self.gen_targ_infoDict.values()[0]
        data_frame_list = pm.frameLayout('main_frame',q=True,ca=True)
        if data_frame_list:
            pm.deleteUI(data_frame_list)
        for each_driven_data in targ_drvn_data:
            single_drvn_nd_nm = each_driven_data.nodeName()
            single_drvn_nd_fnm = each_driven_data.longName()
            single_drv_ly_nm = '{}__ly'.format(single_drvn_nd_nm)
            pm.frameLayout(single_drv_ly_nm,label= '{}=>{}'.format(single_drvn_nd_nm,single_drvn_nd_fnm),bv=True,parent = 'main_frame',w=800)
            merge_all_attr = '{}___cpdvk___'.format(single_drvn_nd_nm)
            for each_drvn_attr_data in targ_drvn_data[each_driven_data]:
                drver_attr_nm = each_drvn_attr_data['driver'].keys()[0]
                drvn_attr_nm = each_drvn_attr_data['driven'].keys()[0]
                single_key_char = '{}__{}'.format(single_drvn_nd_nm,drvn_attr_nm)
                #print single_key_char
                pm.rowLayout('{}__rlyt'.format(single_key_char),numberOfColumns=3, columnWidth3=(60,450,80),
                            columnAlign=(1, 'left'), columnAttach=[(1, 'both', 0), (2, 'both', 0), (3, 'both', 0)] )
                pm.checkBox('{}__cbx'.format(single_key_char),l='inverse')
                attr_dic = self.derive_attrGrp_info(drvn_attr_nm)
                pm.radioButtonGrp('{}__rbg'.format(single_key_char),label = '{}-->{}:'.format(drver_attr_nm,drvn_attr_nm),labelArray3=attr_dic.values()[0],nrb=3,
                    columnAttach = [1,'right',35],sl=attr_dic.keys()[0],cc="ins_ui.rb_ch_cmd(\'{}\',\'{}\')".format(single_drvn_nd_nm,drvn_attr_nm))
                pm.button('{}__copyBT'.format(single_key_char),l='copy driven key',c='ins_ui.single_copy_BT_cmd(\'{}\')'.format(single_key_char))
                pm.setParent('..')
                merge_all_attr += '{}___cpdvk___'.format(drvn_attr_nm)
            pm.button('{}_objCPBT'.format(merge_all_attr),l = 'Copy DrivenKeys 2 Target Object : {}'.format(single_drvn_nd_nm),
                w=120,p=single_drv_ly_nm,c='ins_ui.obj_copy_BT_cmd(\'{}\',\'{}\')'.format(each_driven_data,merge_all_attr))
    def rb_ch_cmd(self,objNm,attrNm):#切换轴向，自动切换 相应轴向的属性名称
        get_attr_list = ['{}{}'.format(re.search('[^X-Z]+',attrNm).group(),eachAxis) for eachAxis in ['X','Y','Z']]
        cur_rbg_name = '{}__{}__rbg'.format(objNm,attrNm)
        single_attr_rly = pm.radioButtonGrp(cur_rbg_name,q=True,p=True)
        #single_frm = pm.rowLayout(single_attr_rly,q=True,p=True)
        p_rowLyt = re.compile('__rlyt$')
        single_row_childs = pm.frameLayout(pm.rowLayout(single_attr_rly,q=True,p=True),q=True,ca=True)
        attr_row_list = [each for each in single_row_childs if p_rowLyt.search(each)]
        other_attr_rbg_list = []
        for each_row in attr_row_list:
            p_rbg = re.compile('__rbg$')
            other_attr_rbg_list.extend([each_ctrl for each_ctrl in pm.rowLayout(each_row,q=True,ca=True)
                if p_rbg.search(each_ctrl)and each_ctrl != cur_rbg_name])
        change_id = pm.radioButtonGrp(cur_rbg_name,q=True,sl=True)
        spec_newAttr = pm.radioButtonGrp(cur_rbg_name,q=True,la3=True)[change_id-1]
        for each_oth_rbg in other_attr_rbg_list:
            cur_sel_rd_id = pm.radioButtonGrp(each_oth_rbg,q=True,sl=True)
            cur_sel_attr = pm.radioButtonGrp(each_oth_rbg,q=True,la3=True)[cur_sel_rd_id-1]
            if cur_sel_attr == spec_newAttr:
                exact_rbg =  each_oth_rbg
                secondary_attr_rbg_list = []
                for each_row in attr_row_list:
                    p_rbg = re.compile('__rbg$')
                    secondary_attr_rbg_list.extend([each_ctrl for each_ctrl in pm.rowLayout(each_row,q=True,ca=True)
                        if p_rbg.search(each_ctrl)and each_ctrl != exact_rbg])
                collect_SELed = []
                for each_sec in secondary_attr_rbg_list:
                    sec_id = pm.radioButtonGrp(each_sec,q=True,sl=True)
                    sec_attr = pm.radioButtonGrp(each_sec,q=True,la3=True)[sec_id-1]
                    collect_SELed.append(sec_attr)
                unsel = [each_attr for each_attr in get_attr_list if each_attr not in  collect_SELed][0]
                pm.radioButtonGrp(exact_rbg,e=True,sl = self.derive_attrGrp_info(unsel).keys()[0])
    def single_copy_BT_cmd(self,key_char):
        targ_drvn_objnm = key_char.split('__')[0]
        rbg_name = '{}__rbg'.format(key_char)
        inv_cbx = '{}__cbx'.format(key_char)
        drvn_frm = '{}__ly'.format(targ_drvn_objnm)
       # drvn_char =  pm.frameLayout(drvn_frm,q=True,l=True)
        drver_obj = self.gen_targ_infoDict.keys()[0]
        dvn_obj_label_nm = pm.frameLayout(drvn_frm,q=True,l=True).split('=>')[1]
        driven_obj_single = [each_dvn for each_dvn in self.gen_targ_infoDict.values()[0].keys() if each_dvn.longName() == dvn_obj_label_nm][0]
        orig_drvn_attr = rbg_name.split('__')[1]
        set2attr = pm.radioButtonGrp(rbg_name,q=True,la3=True)[pm.radioButtonGrp(rbg_name,q=True,sl=True)-1]
        inverse = pm.checkBox(inv_cbx,q=True,v=True)
        single_obj_dvn_data = self.gen_targ_infoDict.values()[0][driven_obj_single]
        #new_data_pair = {}
        for eachDvnData in single_obj_dvn_data:
            if eachDvnData['driven'].keys()[0] == orig_drvn_attr:
                reset_driven_values = [(inverse and -1 or 1)*n for n in eachDvnData['driven'].values()[0]]
                #new_attr_info = {reset2attr:reset_driven_values}
                driver_attr = eachDvnData['driver'].keys()[0]
                driver_v = eachDvnData['driver'].values()[0]
                if driven_obj_single.attr(set2attr).isConnected():
                        get_keyAniCurver = driven_obj_single.attr(set2attr).listConnections()
                        pm.delete(get_keyAniCurver[0])
                for  n in range(len(driver_v)):
                    pm.setDrivenKeyframe(driven_obj_single,at = set2attr,cd =drver_obj.attr(driver_attr),dv = driver_v[n],v=reset_driven_values[n])
        print("Driven Key Frame of {}:{} copied succeed!!!".format(drver_obj.nodeName(),key_char))
    def obj_copy_BT_cmd(self,drivenObj,key_char):
        driven_attr_list = key_char.split('___cpdvk___')[1:-1]
        for each_attr in driven_attr_list:
            print ('copy {} attribute :{} driven keyframe'.format(drivenObj,each_attr))
            single_key_char02 = '{}__{}'.format(drivenObj,each_attr)
            self.single_copy_BT_cmd(single_key_char02)
    def copy_all_BT_cmd(self):
        object_frame_lst = pm.frameLayout('main_frame',q=True,ca=True)
        for each_obj_frm in object_frame_lst:
            p_copyBt = re.compile('___objCPBT$')
            obj_copy_BT = [each_ctrl for each_ctrl in pm.frameLayout(each_obj_frm,q=True,ca=True) if p_copyBt.search(each_ctrl)][0]
            driven_obj = pm.PyNode(pm.frameLayout(each_obj_frm,q=True,l=True).split('=>')[1])
            self.obj_copy_BT_cmd(driven_obj,obj_copy_BT)





