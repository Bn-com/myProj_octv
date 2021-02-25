#!/usr/bin/env python

"""
__title__ = pick_pink_v02
__author__ = zhangben 
__mtime__ = 2019/3/10 : 19:23
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
"""
import sys, os, re
import json

if r"\\octvision.com\CG\Tech\Nuke\NukeToolSet_master\python" not in sys.path:
    sys.path.append(r"\\octvision.com\CG\Tech\Nuke\NukeToolSet_master\python")
import numpy as np
import copy
import nuke

def wr_date2file(dataDict, stuffNm, wfpth=None):
    if not wfpth:
        wfpth = os.environ["TMP"]
    rec_file = os.path.join(wfpth, "{}.json".format(stuffNm))
    with open(rec_file, 'w') as f:
        f.write(json.dumps(dataDict, indent=4))


def obtain_indentisyData():
    selRds = nuke.selectedNodes('Read')
    selRds[0].setSelected(1)
    imgpth = selRds[0]['file'].getValue()
    imgpth_spl = os.path.split(imgpth)
    imgpth_bsn = imgpth_spl[1].split('.')[0]

    ct = nuke.createNode('CurveTool')
    stf = int(selRds[0]['origfirst'].getValue())
    enf = int(selRds[0]['origlast'].getValue())
    intnstyDates = {'v_r': {}, 'v_g': {}, 'v_b': {}}
    # intnstyDates = {'v_r': [], 'v_g': [], 'v_b': []}
    while stf <= enf:
        nuke.execute(ct, stf, stf)
        temDate = ct['intensitydata'].value()
        # intnstyDates['v_r'].append({stf:temDate[0]})
        # intnstyDates['v_g'].append({stf:temDate[1]})
        # intnstyDates['v_b'].append({stf:temDate[2]})
        intnstyDates['v_r'][stf] = temDate[0]
        intnstyDates['v_g'][stf] = temDate[1]
        intnstyDates['v_b'][stf] = temDate[2]
        stf += 1
    wr_date2file(intnstyDates, imgpth_bsn)
    nuke.delete(ct)


selRds = nuke.selectedNodes('Read')
selRds[0].setSelected(1)
imgpth = selRds[0]['file'].getValue()
imgpth_spl = os.path.split(imgpth)
imgpth_bsn = imgpth_spl[1].split('.')[0]

stuffNm = imgpth_bsn
wfpth = os.environ["TMP"]
rec_file = os.path.join(wfpth, "{}.json".format(stuffNm))

readDate_dict = ''
with open(rec_file, 'r') as rf:
    readDate_dict = json.load(rf)

new_data = mad_outlier(readDate_dict, stuffNm, r"E:\dev_proj", 0.3, None)


# mad_outlier(readDate_dict)

# mad_outlier(readDate_dict)
def mad_outlier(readDate_dict, stuffNm, outPath=None, bias=1, interectMod=True, counter=1):
    # outPath = r"E:\dev_proj"
    print("the {}th time running ".format(counter))
    if outPath == None:
        outPath = os.environ["TMP"]
    outFile = os.path.abspath("{}_outlierDate.txt".format(os.path.join(outPath, stuffNm)))
    if counter == 1 and os.path.isfile(outFile):
        os.remove(outFile)
    dateDic = copy.deepcopy(readDate_dict)
    outlier_frms_dict = {}
    k = ['v_r', 'v_b']
    for ea_k in k:
        dateDict = dateDic[ea_k]
        ret = sorted(dateDict.items(), key=lambda item: item[0])
        if len(ret) == 0:
            return None
        # print("now data leaves: {}".format(len(ret)))
        a = np.array(ret).T
        # check array rows and columns
        # a.shape
        a_num = a.astype(float)
        needDate = a_num[1]
        std_v = needDate.std(ddof=1)
        avr_v = needDate.mean()
        sub_avr = np.abs(needDate - avr_v)
        outlier = []
        for ea_sub in sub_avr:
            if ea_sub > std_v * 3 * bias:
                indx_echo = np.argwhere(sub_avr == ea_sub).T
                indx = [n for n in indx_echo[0]]
                frm_nm = a_num[0][indx].tolist()
                # print ("outlier frames : {} ".format(frm_nm))
                addTmp = [ea for ea in frm_nm if ea not in outlier]
                outlier.extend(addTmp)
            # print(" finde outlier {} value {} at frame {}".format(ea_k,ea_sub,frm_nm))
        outlier_frms_dict[ea_k] = outlier
    if interectMod:
        outlier_frms_lst = [ea_frm for ea_frm in outlier_frms_dict['v_r'] if ea_frm in outlier_frms_dict['v_b']]
    else:
        outlier_frms_lst = [ea_frm for ea_frm in outlier_frms_dict['v_r']]
        # print (" frames in r chanle: {}".format(outlier_frms_lst))
        outlier_frms_vb = [ea_frm for ea_frm in outlier_frms_dict['v_b'] if ea_frm not in outlier_frms_lst]
        # print ("frames in b chanle: {}".format(outlier_frms_vb))
        outlier_frms_lst.extend(outlier_frms_vb)
    # print ("collect frames: {}".format(outlier_frms_lst))
    rcd_frm_str = ""
    print  ("============={}".format(len(outlier_frms_lst)))
    if len(outlier_frms_lst) != 0:
        for ea_frm in outlier_frms_lst:
            rcd_frm_str += "{} ".format(int(ea_frm))
            print rcd_frm_str
            dateDic['v_r'].pop(str(int(ea_frm)))
            dateDic['v_b'].pop(str(int(ea_frm)))
    if dateDic != readDate_dict:
        # print (" 01 Counter = {}".format(counter))
        read_str_frm_f = ""
        if os.path.isfile(outFile):
            with open(outFile, 'r') as rf0:
                read_str_frm_f = rf0.read()
        print ("read  data frams : {} ".format(read_str_frm_f))
        read_str_frm_f += rcd_frm_str
        print ("now finde outlier frames: {} ".format(read_str_frm_f))
        tmp_spl = read_str_frm_f.split(" ")
        wrt_frm_st = ''
        for eaf in sorted(tmp_spl):
            wrt_frm_st += "{} ".format(eaf)
        print ("writing string is ::: {} ".format(wrt_frm_st))
        with open(outFile, 'w') as af:
            af.write(wrt_frm_st)
        counter += 1
        # print ("mad time is {}".format(counter))
        #        print (" 02 Counter = {}".format(counter))
        mad_outlier(dateDic, stuffNm, outPath, bias, interectMod, counter)
        # print (" 03 Counter = {}".format(counter))
    else:
        print("there is no outlier value")
        read_str_frm_f = ""
        with open(outFile, 'r') as rf0:
            read_str_frm_f = rf0.read()
        tmp_spl = read_str_frm_f.split(" ")
        frm_nums = len(tmp_spl)
        final_str = "there are {} frames: {}".format(frm_nums, read_str_frm_f)
        with open(outFile, 'w') as af:
            af.write(final_str)
        frmLst = None
        with open(outFile, 'r') as rf:
            frmsStr = rf.read()
        frmLst = frmsStr.split(" ")
        rtstr = "Num: {}   == {}".format(len(frmLst), sorted(frmLst))
        # print rtstr
        return rtstr


new_data = mad_outlier(readDate_dict, stuffNm, r"E:\dev_proj", 0.6, None)






