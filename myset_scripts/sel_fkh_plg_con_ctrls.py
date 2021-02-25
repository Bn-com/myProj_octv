#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = sel_fkh_plg_con_ctrls
__author__ = zhangben 
__mtime__ = 2019/5/21 : 17:42
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
"""

all_fkhs = pm.ls(type='KLJZ_dts')
ctrls = []
for ea in all_fkhs:
    get_ctrl = ea.listConnections(d=True, type='transform', et=True)
    exact = [get_ctrl[n] for n in range(len(get_ctrl)) if get_ctrl[n] not in get_ctrl[:n]]
    ctrls.extend(exact)

pm.select(ctrls)