#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = TransFacialAnimData
__author__ = zhangben 
__mtime__ = 2019/12/13 : 16:01
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
"""

import pymel.core as pm
import re


# ==========================
class TransFacialAnimData(object):
    def __init__(self):
        self.pSels = None
        self.pHead = None
        self.pJnts = []
        self.conBlnds = []
    def trans_anim_data(self):
        if not self.pSels:
            self.pSels = pm.selected()
            if not self.pSels: return
            for pSel in self.pSels:
                if pSel.getShape() and pSel.getShape().nodeType() == 'mesh':
                    self.pHead = pSel.getShape()
                else:
                    self.pJnts.append(pSel)
        # pm.select(psel.listRelatives(ad=True))
        # pSelShp = pSels[0].getShape()
        #conBlnds = []
            tmp = [self.conBlnds.extend(s.listConnections(type='blendShape')) for s in self.pHead.listConnections(type='objectSet') if
                   s.listConnections(type='blendShape') and s.listConnections(type='blendShape')[0] not in self.conBlnds]
        for eb in self.conBlnds:
            blndNm_strip = eb.name(stripNamespace=True)
            src_w_attr = eb.attr('weight')[0]
            dest_blnd = pm.PyNode(blndNm_strip)
            dest_blnd_w_attr = dest_blnd.attr('weight')[0]
            dest_blnd_w_attr.set(src_w_attr.get())
        for ejnt in self.pJnts:
            rot_attrs = ['rx', 'ry', 'rz']
            jnts_nm_strip = ejnt.name(stripNamespace=True)
            dest_jnt = pm.PyNode(jnts_nm_strip)
            for er in rot_attrs:
                dest_jnt.attr(er).set(ejnt.attr(er).get())


trnFacAnim = TransFacialAnimData()
# ================================================================================================
trnFacAnim.trans_anim_data()
