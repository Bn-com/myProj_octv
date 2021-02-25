#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = 'pk_rnmtools_auto'    
__author__ = zhangben
__mtime__ = 2018/12/6:11:28
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
'''
import re
import pymel.core as pm
import maya.cmds as mc

import Pc_pubCheck as ppc
import Pc_scInfo as psi

#scinf = pc.major.Pc_scInfo.Pc_scInfo()

# reload(ppc)
# chk = ppc.Pc_pubCheck()
# chk.checkDonotNodeCleanBase()



# Pre_regNaming_fix('MSH__', 'MSH_')
# Pre_regNaming()


def Pre_regNaming_fix(pattern,repl,pos=False,ignCap = False,topSel=False):
    sel_MODEL = pm.selected()[0]
    getAll_trans = sel_MODEL.listRelatives(ad=True, c=True, type='transform')
    if not sel_MODEL: sel_MODEL = pm.selected()[0]
    for each in getAll_trans:
        # print ("will rename ======{}".format(each.name()))
        ea_nm = new_names(each)
        # print ea_nm
        if not ea_nm:continue
        # print("run line no  46==============")
        ea_nm = fix_modeName(pattern,repl,ea_nm,ignCap,pos)
        each.rename(ea_nm)
        # print('run line no   49 ======{}========='.format(each.name()))
    for each in getAll_trans:
        fix_suffix_num(each)
        # print ('======Rename object:{}================'.format(each.name()))
    sel_MODEL.rename(fix_modeName(pattern,repl,sel_MODEL.nodeName(),ignCap,pos))
    if not topSel:
        print(u'========regularizeed nodes name ==================')
        return None
    if sel_MODEL.name != u'MSH_all':
        sel_MODEL.rename(u'MSH_all')
    if not pm.objExists(u'MODEL'): pm.group(em=True,w=True,n=u'MODEL')
    sel_MODEL.setParent(u'MODEL')
    if not pm.objExists(u'MSH_geo'):
        geoGrp = pm.group(em=True,w=True,n=u'MSH_geo')
        geoGrp.setParent(u'MSH_all')
    if not pm.objExists(u'MSH_outfig'):
        outfitGrp = pm.group(em=True,w=True,n=u'MSH_outfit')
        outfitGrp.setParent(u'MSH_all')


def Pre_regNaming(sel_MODEL=None,topSel=False):#=========rename selecte group and children's  name =======main proc
    if not sel_MODEL: sel_MODEL = pm.selected()[0]
    getAll_trans = sel_MODEL.listRelatives(ad=True, c=True, type='transform')
    for each in getAll_trans:
        ea_nm = new_names(each)
        if ea_nm: each.rename(ea_nm)
    for each in getAll_trans:
        fix_suffix_num(each)
    sel_MODEL.rename(new_names(sel_MODEL))
    if not topSel:
        print(u'========regularizeed nodes name ==================')
        return None
    if sel_MODEL.name != u'MSH_all':
        sel_MODEL.rename(u'MSH_all')
    if not pm.objExists(u'MODEL'): pm.group(em=True,w=True,n=u'MODEL')
    sel_MODEL.setParent(u'MODEL')
    if not pm.objExists(u'MSH_geo'):
        geoGrp = pm.group(em=True,w=True,n=u'MSH_geo')
        geoGrp.setParent(u'MSH_all')
    if not pm.objExists(u'MSH_outfig'):
        outfitGrp = pm.group(em=True,w=True,n=u'MSH_outfit')
        outfitGrp.setParent(u'MSH_all')

def fix_modeName(pattern,repl,ndname,pos=False,ignCap = False):### sepecified a pattern replace source name
    newnm = None
    if pos == 'suffix':
        if ignCap:
            newnm = re.sub(u'{}$'.format(pattern),repl,ndname,re.I)
        else:
            newnm = re.sub(u'{}$'.format(pattern),repl,ndname)
    elif pos == 'prefix':
        if ignCap:
            newnm = re.sub(u'^{}'.format(pattern),repl,ndname,re.I)
        else:
            newnm = re.sub(u'^{}'.format(pattern),repl,ndname)
    else:
        if ignCap:
            newnm = re.sub(u'{}'.format(pattern),repl,ndname, re.I)
        else:
            newnm = re.sub(u'{}'.format(pattern),repl,ndname)
    return newnm

def fix_suffix_num(rnnode):#fix  "xxx_20"====> "xxx20_"
    ndname = rnnode.name()
    mod_idnm_search = re.search(u'_[\d]+$', ndname)
    if mod_idnm_search:
        suf_str = mod_idnm_search.group()
        idnm = re.search(u'\d+', mod_idnm_search.group()).group()
        rnnode.rename(re.sub(suf_str, u'{}_'.format(idnm), ndname))

def new_names(nodeObj, prifix=u'MSH', suffix=u'_', precision= None):# return the new name string
    if not precision:
        scinf = psi.Pc_scInfo()
        precision = scinf.assPrec
    # nodeObj = each
    nm_str = nodeObj.nodeName()
    nm_dic = get_name_membs(nm_str)
    # print nm_dic
    new_name_dict = {}
    if nm_dic['nm'] in [u'MSH_all',u'MSH_geo',u'MSH_outfit']: return None
    if nm_dic['nm'].startswith('MSH_'):
        nmsplt = nodeObj.nodeName().split('_')
        prifix = nmsplt[0]
        nm_dic['sd'] = nmsplt[1]
        precision = nmsplt[2]
        nm_dic['nm'] = nmsplt[3]
    if not nodeObj.getShape():
        suffix = None
    new_name_dict = {'pr': prifix, 'prec': precision, 'nm': nm_dic['nm'], 'side': nm_dic['sd'], 'id': nm_dic['id']}
    new_name_str = u'{}_'.format(new_name_dict['pr'])
    #print new_name_str
    for each in ['side', 'prec', 'nm', 'id']:
        if new_name_dict[each]:
            if each == 'nm':
                name_base = re.search(u'[\w]*[^0-9]+', new_name_dict['nm'], re.I).group()
                # name_base = re.sub(u'[_]+$',u'',name_base)
                name_base = re.sub(u'[\d_]+$', u'', name_base)
                new_name_str += u'{}'.format(name_base)
            elif each == 'id':
                suffix = None
                new_name_str += u'_{}'.format(new_name_dict[each])
            else:  # each = 'nm'
                new_name_str += u'{}_'.format(new_name_dict[each])

    if not suffix:
        new_name_str = re.sub(u'[_]+$', u'', new_name_str)
    else:
        new_name_str += suffix
    return new_name_str

def get_name_membs(nm_str): # return a dict, contains the new name needs membership
    new_name_dict = {}
    pk_sid = pick_side_desc(nm_str)
    new_name_dict['sd'] = u'c'
    new_name_dict['nm'] = nm_str
    new_name_dict['id'] = None
    if pk_sid:
        re_nm_str = re.compile(pk_sid.values()[0].keys()[0])
        nm_str_n = re_nm_str.sub('_', nm_str)
        new_name_dict['sd'] = pk_sid.keys()[0]
        new_name_dict['nm'] = nm_str_n
        new_name_dict['id'] = pk_sid.values()[0].values()[0]
    return new_name_dict


def pick_side_desc(nameStr): # on the basis of current mode's name,obtain model object on wich side including : r,l ,c
    re_pick_side = re.compile('(_|\s)[r|l][0-9]*[_]?', re.I)
    if not re_pick_side.search(nameStr):
        return None
    re_side = re.compile(u'r|l', re.I)
    re_num = re.compile(u'[0-9]+')
    side_dict = {}
    side_desc = ''
    mod_num = None
    side_desc = re_pick_side.search(nameStr).group()
    side_str = re_side.search(side_desc).group().lower()
    if re_num.search(side_desc):
        mod_num = re_num.search(side_desc).group()
    side_desc_dict = {side_desc: mod_num}
    side_dict[side_str] = side_desc_dict
    return side_dict

