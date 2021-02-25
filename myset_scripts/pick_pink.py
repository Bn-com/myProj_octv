# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# """
# __title__ = pick_pink.py
# __author__ = zhangben
# __mtime__ = 2019/2/27 : 18:32
# # code is far away from bugs with the god animal protecting
# I love animals. They taste delicious.
# """

import numpy as np



#
# """
#
# analyzNd = nuke.selectedNode()
#
# ct = nuke.createNode('CurveTool')
#
# ct_sel = nuke.selectedNode()
# nuke.execute(ct_sel, nuke.frame(), nuke.frame())
#
# dat
# nuke.message('average luminance is %s' % dat)
#
# sel_nd = nuke.selectedNode()
#
# nuke.nodes.MinColor(target=1, inputs=sel_nd)
#
# ct = nuke.createNode('CurveTool')
#
# nuke.execute(ct, nuke.frame(), nuke.frame())
# dat = ct['intensitydata'].value()
# nuke.message('average luminance is %s' % dat)
#
# for eaknb in ct.allKnobs():
#     print eaknb
#
# print("\n".join(ct.allKnobs()))
#
# sel_crvt = nuke.selectedNode()
# sel_crvt['intensitydata'].value()
# nuke.execute(sel_crvt, nuke.frame(), nuke.frame())
# dat = sel_crvt['intensitydata'].value()
# whatSel = nuke.selectedNode()
# for eaknb in whatSel.knobs():
#
# whatSel['intensitydata'].getValue
# crvt = nuke.selectedNode()
# crvt['intensitydata'].value()[0]
#
# wrf = r"e:\dev_debug\pickPinkFram.txt"
# wf = open(wrf, 'w')
#
# nuke.execute(crvt, nuke.frame(), nuke.frame())
#
# stf = 443
# enf = 466
# while stf < end:
#     nuke.execute(crvt, stf, stf)
#     dat = ['intensitydata'].value()
#     print dat[0]
#     print dat[2]
#     stf += 1
# #
# #
# # lsa = [0.8,0.78,0.88,0.95,0.65,0.85]
# #
# # srclst = [0.83]
# #
# #
# # sel_nodes = nuke.selectedNodes()
# #
# #
# # ct = nuke.createNode('CurveTool')
# #
# #
# # stf = nuke.root().firstFrame()
# # enf = nuke.root().lastFrame()
# #
# # intnstyDates = {'intn_r':[],'intn_b':[],'intn_c':[]}
# #
# # while stf =< enf:
# #     nuke.execute(ct,stf,stf)
# #     sample_num = len(square_r_lst)
# #     temDate= ct['intensitydata'].value()
# #     intnstyDates['intn_r'].append(temDate[0])
# #     intnstyDates['intn_g'].append(temDate[1])
# #     intnstyDates['intn_b'].append(temDate[2])
# # import Image as
# #
# #
# # rdf = r"E:\dev_debug\pickPinkFram.txt"
# # readData = None
# # with open(rdf,'r') as rf:
# #     readData = json.load(rf)
# # # print readData
# #
# # color_r = readData[readData.keys()[0]]
# # # print color_r
# #
# # clrar =np.array(color_r)
# #
# # stdV = clrar.std()
# # medianV = np.median(clrar)
# #
# # diff = np.sum((clrar-medianV)**,axis=0)
# #
# #
# #
# # print stdV
# # print medianV
# # print diff
#
# # print(clrar-medianV)
# """
# """
# __title__ = pick_pink.py
# __author__ = zhangben
# __mtime__ = 2019/2/27 : 18:32
# # code is far away from bugs with the god animal protecting
# I love animals. They taste delicious.
# """
#
# """
# __title__ = pick_pink.py
# __author__ = zhangben
# __mtime__ = 2019/2/27 : 18:32
# # code is far away from bugs with the god animal protecting
# I love animals. They taste delicious.
# """
#
# import sys
# import json
# # if r"\\octvision.com\CG\Tech\Nuke\NukeToolSet_master\python" not in sys.path:
# #     sys.path.append(r"\\octvision.com\CG\Tech\Nuke\NukeToolSet_master\python")
# import json
# import numpy as np
# import os
# # import nuke
#
def wr_date2file(dataDict,stuffNm):
    wfpth = os.environ["TMP"]
    rec_file = os.path.join(wfpth,"{}.json".format(stuffNm))
    with open(rec_file,'w') as f:
        f.write(json.dumps(dataDict,indent=4))

def obtain_indentisyData():
    selRds = nuke.selectedNodes('Read')
    selRds[0].setSelected(1)
    imgpth = selRds[0]['file'].getValue()
    imgpth_spl = os.path.split(imgpth)
    imgpth_bsn = imgpth_spl[1].split('.')[0]

    ct = nuke.createNode('CurveTool')
    stf = selRds[0]['origfirst'].getValue()
    enf = selRds[0]['origlast'].getValue()
    intnstyDates = {'v_r': [], 'v_g': [], 'v_b': [], 'frm': []}
    while stf<= enf:
        nuke.execute(ct, int(stf),int(stf))
        temDate = ct['intensitydata'].value()
        intnstyDates['v_r'].append(temDate[0])
        intnstyDates['v_g'].append(temDate[1])
        intnstyDates['v_b'].append(temDate[2])
        intnstyDates['frm'].append(stf)
        stf += 1
    wr_date2file(intnstyDates,imgpth_bsn)
#
# # lstA = [1.2,2.2,3.02,1.4,3.5,15,1.085]
#
# def mad_outlier_baseon_median(lstA,bias = 0.6745):
#     tmpA = np.array(lstA)
#     tmp_av = tmpA.mean()
#     tmp_med = np.median(tmp_av)
#     # print tmp_av
#     # print tmp_av
#     diff_1 = np.sum((tmpA - tmp_med)**2,axis=-1)
#     # print diff_1
#     diff_1 = np.sqrt(diff_1)
#     # print diff_1
#     # print np.median(diff_1)
#     # iffy_datas = []
#     # print(np.std(tmpA))
#     # print(np.var(tmpA))
#     # for each_v in color_r:
#     new_tmp = np.abs(tmpA - tmp_med)
#     print new_tmp
#     mad = bias*np.median(new_tmp)
#     lower_limit = tmp_med - (3*mad)
#     upper_limit = tmp_med + (3*mad)
#     print lower_limit,upper_limit
#     for ea in lstA:
#         if not lower_limit < ea < upper_limit:
#             print ea
#
# #
# # selRds = nuke.selectedNodes('Read')
# # selRds[0].setSelected(1)
# # imgpth = selRds[0]['file'].getValue()
# # imgpth_spl = os.path.split(imgpth)
# # imgpth_bsn = imgpth_spl[1].split('.')[0]
# #
# # stuffNm = imgpth_bsn
# # wfpth = os.environ["TMP"]
# # rec_file = os.path.join(wfpth, "{}.json".format(stuffNm))
# # readDate_dict = ''
# # with open(rec_file, 'r') as rf:
# #     readDate_dict = json.load(rf)
# #
# # index = readDate_dict['frm'].index(490.0)
# #
# # readDate_dict['frm'].index(490.0)
# #
# # # def mad_outlier_baseon_median(lstA,bias = 0.6745):
# # lstA = readDate_dict['v_b']
# #
# # lstA[51]
# #
# # frmLst[51]
# #
# # frmLst = readDate_dict['frm']
# # tmpA = np.array(lstA)
# # tmp_av = tmpA.mean()
# #
# # tmp_med2 = np.median(tmp_av)
# #
# # tmp_med = np.median(tmpA)
# #
# # tem_sdt = tmpA.std(doff=1)
# # # print tmp_av
# # # print tmp_av
# #
# # for ea in lstA:
# #     if not lower_limit < ea < upper_limit:
# #         frmNm = frmLst[lstA.index(ea)]
# #         iffy_fram.append("{}:{}".format(frmNm, ea))
# #
# # diff_1 = np.sum((tmpA - tmp_med) ** 2, axis=-1)
# # # print diff_1
# # diff_1 = np.sqrt(ddof_1)
# #
# # new_tmp = np.abs(tmpA - tmp_med)
# # print new_tmp
# #
# # bias = 0.2
# # mad = bias * np.median(new_tmp)
# # lower_limit = tmp_med - (3 * mad)
# # upper_limit = tmp_med + (3 * mad)
# # print lower_limit, upper_limit
# # iffy_fram = []
# #
# # lstA[51]
# #
# # ea = lstA[50]
# # for ea in lstA:
# #     if not lower_limit < ea < upper_limit:
# #         frmNm = frmLst[lstA.index(ea)]
# #         iffy_fram.append("{}:{}".format(frmNm, ea))
# #
# # if __name__ == "__main__":
# #     obtain_indentisyData()
#
#
#
#
#
#
# dt_r_lst = [0.0815583547613288, 0.08124188172226038, 0.08642637350072215, 0.08134640715286423, 0.08127849492722009, 0.08140541954620378, 0.08119514295826649, 0.08114549632292917, 0.08102155634590089, 0.08108698036747025, 0.08102946482809632, 0.08100068106236019, 0.08097997925373572, 0.08088861727617314, 0.0808620486475383]
#
# ar_1 = np.array(dt_r_lst)
#
# # std_v = ar_1.std(ddof=1)
# std_v_total = ar_1.std(ddof=0)
# # print std_v
# # print std_v_total
# avr_v = ar_1.mean()
# # print avr_v
# sub_avr = ar_1
# # print sub_avr
#
#
# selRds = nuke.selectedNodes('Read')
# selRds[0].setSelected(1)
# imgpth = selRds[0]['file'].getValue()
# imgpth_spl = os.path.split(imgpth)
# imgpth_bsn = imgpth_spl[1].split('.')[0]
#
# stuffNm = imgpth_bsn
# wfpth = os.environ["TMP"]
# rec_file = os.path.join(wfpth, "{}.json".format(stuffNm))
# readDate_dict = ''
# with open(rec_file, 'r') as rf:
#     readDate_dict = json.load(rf)
#
# index = readDate_dict['frm'].index(490.0)
#
# readDate_dict['frm'].index(490.0)
#
# # def mad_outlier_baseon_median(lstA,bias = 0.6745):
# dt_r_lst = readDate_dict['v_r'][5: 20]
#
# dt_r_lst = [0.0815583547613288, 0.08124188172226038, 0.08642637350072215, 0.08134640715286423, 0.08127849492722009, 0.08140541954620378, 0.08119514295826649,
#            0.08114549632292917, 0.08102155634590089, 0.08108698036747025, 0.08102946482809632, 0.08100068106236019, 0.08097997925373572, 0.08088861727617314,
#            0.0808620486475383]
#
#
# def mad_outlier(dt_r_lst):
#     ar_1 = np.array(dt_r_lst)
#     std_v = ar_1.std(ddof=1)
#     std_v_total = ar_1.std(ddof=0)
#     # print std_v
#     # print std_v_total
#     avr_v = ar_1.mean()
#     # print avr_v
#     sub_avr = np.abs(ar_1 - avr_v)
#
#     outlier = {}
#
#     for ea_sub in sub_avr:
#         if ea_sub > std_v * 3:
#             indx = sub_avr.argwhere(a=ea_sub)
#             outlier[indx] = ea_sub
#     # print outlier
#     return outlier
#
#
# outlier_r = mad_outlier(readDate_dict['v_r'])
# # print sub_avr
#
#
#
#
#
#
#
#
#
#
#
#
# import numpy as np
#
# a = np.array(([3,2,1],[2,5,7],[4,7,8]))
# idex_n = np.argwhere(a==7)
#
# a = {1:'a'}
# type(a.keys()[0])
#
#
#

# selRds = nuke.selectedNodes('Read')
# selRds[0].setSelected(1)
# imgpth = selRds[0]['file'].getValue()
# imgpth_spl = os.path.split(imgpth)
# imgpth_bsn = imgpth_spl[1].split('.')[0]

# stuffNm = imgpth_bsn
# wfpth = os.environ["TMP"]
# rec_file = os.path.join(wfpth, "{}.json".format(stuffNm))
# readDate_dict = ''
import json,re,os,sys
import numpy as np

rec_file = r"E:\dev_temp\camM.json"
with open(rec_file, 'r') as rf:
    readDate_dict = json.load(rf)

index = readDate_dict['frm'].index(490.0)

readDate_dict['frm'].index(490.0)

# def mad_outlier_baseon_median(lstA,bias = 0.6745):
dt_r_lst = readDate_dict['v_r'][5: 20]

ar_dic = np.array(readDate_dict['v_r'])



# np.argwhere(ar_dic == 0.0815583547613288)


def mad_outlier(dateDic):
    dt_r_lst = dateDic['v_r']
    td_b_lst = dateDic['v_b']
    ar_1 = np.array(dt_r_lst)
    std_v = ar_1.std(ddof=1)
    std_v_total = ar_1.std(ddof=0)
    # print std_v
    # print std_v_total
    avr_v = ar_1.mean()
    # print avr_v
    sub_avr = np.abs(ar_1 - avr_v)

    outlier = {}

    for ea_sub in sub_avr:
        if ea_sub > std_v * 3:
            indx_echo = np.argwhere(sub_avr == ea_sub)
            indx = indx_echo[0, 0]
            outlier[indx] = ea_sub
    # print outlier
    return outlier


outlier_r = mad_outlier(readDate_dict)
# print sub_avr
for eaId in outlier_r:
    print eaId

frm_num = readDate_dict['frm'][eaId]
#