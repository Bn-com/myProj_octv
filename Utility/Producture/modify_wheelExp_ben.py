#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = modify_wheelExp_ben
__author__ = zhangben 
__mtime__ = 2019/4/1 : 17:05
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
"""

import re
import os
all_exps = pm.ls(type = 'expression')
#ea_ex = all_exps[3]
for ea_ex in all_exps:
    ex_codes = ea_ex.getExpression()
    ex_cd_spl = ex_codes.split(".diameter;\n")
    if len(ex_cd_spl) == 1 :continue
    new_code = """.diameter;\nif ($diameter == 0){$diameter = 0.0001;}\n""".join(ex_cd_spl)
    ea_ex.setExpression(new_code)
    print(ea_ex.getExpression())




# wheelCtrl = [ea.getParent() for ea in pm.ls(type='nurbsCurve') if ea.getParent().hasAttr("diameter")]