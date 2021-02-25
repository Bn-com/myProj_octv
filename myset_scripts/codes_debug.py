# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# """
# __title__ = codes_debug.py
# __author__ = zhangben
# __mtime__ = 2019/3/8 : 10:11
# # code is far away from bugs with the god animal protecting
# I love animals. They taste delicious.
# # """
#
# import sys, os, re
# import json
# import nuke
# if r"\\octvision.com\CG\Tech\Nuke\NukeToolSet_master\python" not in sys.path:
#     sys.path.append(r"\\octvision.com\CG\Tech\Nuke\NukeToolSet_master\python")
# import numpy as np
#
# import sys, os, re
# import json
#
# if r"\\octvision.com\CG\Tech\Nuke\NukeToolSet_master\python" not in sys.path:
#     sys.path.append(r"\\octvision.com\CG\Tech\Nuke\NukeToolSet_master\python")
# import numpy as np
#
#
# def wr_date2file(dataDict, stuffNm, wfpth=None):
#     if not wfpth:
#         wfpth = os.environ["TMP"]
#     rec_file = os.path.join(wfpth, "{}.json".format(stuffNm))
#     with open(rec_file, 'w') as f:
#         f.write(json.dumps(dataDict, indent=4))
#
#
# def obtain_indentisyData():
#     selRds = nuke.selectedNodes('Read')
#
#
# selRds[0].setSelected(1)
# imgpth = selRds[0]['file'].getValue()
# imgpth_spl = os.path.split(imgpth)
# imgpth_bsn = imgpth_spl[1].split('.')[0]
#
# ct = nuke.createNode('CurveTool')
# stf = int(selRds[0]['origfirst'].getValue())
# enf = int(selRds[0]['origlast'].getValue())
# intnstyDates = {'v_r': {}, 'v_g': {}, 'v_b': {}}
# # intnstyDates = {'v_r': [], 'v_g': [], 'v_b': []}
# while stf <= enf:
#     nuke.execute(ct, stf, stf)
#     temDate = ct['intensitydata'].value()
#     # intnstyDates['v_r'].append({stf:temDate[0]})
#     # intnstyDates['v_g'].append({stf:temDate[1]})
#     # intnstyDates['v_b'].append({stf:temDate[2]})
#     intnstyDates['v_r'][stf] = temDate[0]
#     intnstyDates['v_g'][stf] = temDate[1]
#     intnstyDates['v_b'][stf] = temDate[2]
#     stf += 1
# wr_date2file(intnstyDates, imgpth_bsn)
# nuke.delete(ct)
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
#
# readDate_dict = ''
# with open(rec_file, 'r') as rf:
#     readDate_dict = json.load(rf)
#
#
# # mad_outlier(readDate_dict)
#
#
# def mad_outlier(dateDic, k=['v_r', 'v_b']):
#     dateDic = readDate_dict
#
#
# for ea_k in k: pass
# dateDict = dateDic[ea_k]
# ret = sorted(dateDict.items(), key=lambda item: item[0])
# a = np.array(ret).T
# # check array rows and columns
# # a.shape
# a_num = a.astype(float)
#
# needDate = a_num[1]
#
# std_v = needDate.std(ddof=1)
# avr_v = needDate.mean()
#
# np.argwhere(a == a[0][1])
#
# ar_1 = np.array(dateDict)
# std_v = ar_1.std(ddof=1)
# # print std_v
# # print std_v_total
# # print avr_v
# sub_avr = np.abs(ar_1 - avr_v)
#
# outlier = {}
#
# for ea_sub in sub_avr:
#     if ea_sub > std_v * 3:
#         indx_echo = np.argwhere(sub_avr == ea_sub)
#         indx = indx_echo[0, 0]
#         outlier[indx] = ea_sub
# # print outlier
# return outlier
#
# dt_r = sorted(intnstyDates['v_r'].items(), key=lambda item: item[0])
#
# res = intnstyDates.items()
#
#
# def mad_outlier(dateDic):
#     dateLst = dateDic['v_r']
#     ar_1 = np.array(dateLst)
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
#             indx_echo = np.argwhere(sub_avr == ea_sub)
#             indx = indx_echo[0, 0]
#             outlier[indx] = ea_sub
#     # print outlier
#     return outlier
#
#
# outlier_r = mad_outlier(readDate_dict['v_r'])
# # print sub_avr
# for eaId in outlier_r:
#     print eaId
#
# frm_num = readDate_dict['frm'][eaId]
#
#
# # def rm_v(condition, lst):
# #     tmp_lst = lst
# #     for each in lst:
# #         print each
# #         if condition(each):
# #             tmp_lst.remove(each)
# #         print("remove item {}".format(each))
# #     print("============\n the list now is ===========")
# #     print tmp_lst
# #     if tmp_lst != lst:
# #         rm_v(condition, tmp_lst)
# #     else:
# #         return tmp_lst
# #
# # def rm_v(condition, lst):
# #     tmp_lst = lst
# #     for each in lst:
# #         print each
# #         if condition(each):
# #             tmp_lst.remove(each)
# #     #     print("remove item {}".format(each))
# #     # return lst
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
#
#
#
# def rm_v(lst):
#     avr_v = avr(lst)
#     print 'average : {} '.format(avr_v)
#     tmplst = []
#     tmplst.extend(lst)
#     print tmplst
#     for ea in lst:
#         print("current item: {}".format(ea))
#         if ea > avr_v:
#             tmplst.remove(ea)
#         print lst
#         print tmplst
#     if lst != tmplst:
#         rm_v(tmplst)
#     else:
#         return tmplst
#
# def avr(lst):
#     total = 0
#     for ea in lst:
#         total += ea
#     # print total/len(lst)
#     return total/len(lst)
#
#
#
# def cm(item):
#     print (" now check item : {}".format(item))
#     print " {} %  {} = {}".format(item,2,item%2)
#     return item%2
#
#
#
# # print(avr([1]))
# print(rm_v([1,2,5,6,7,15]))
