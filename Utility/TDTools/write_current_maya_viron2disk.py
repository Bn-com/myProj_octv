#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = write_current_maya_viron2disk
__author__ = zhangben 
__mtime__ = 2020/6/4 : 10:31
__description__: 

    code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""
import re,os,sys

def main():
    env_mode = os.getenv('MAYA_ENV_MODE') if os.getenv('MAYA_ENV_MODE') else 'client_mode'
    maya_v = os.getenv('MAYA_VERSION')
    outDir = r"E:\dev_maya_env_compare"
    write_f = "{}\MAYA{}_{}_environ.vrs".format(outDir,maya_v,env_mode)
    var_data = os.environ.data
    var = var_data.keys()
    var.sort()

    if not os.path.isdir(outDir):os.makdirs(outDir)
    with open(write_f,'w') as wf:
        wf.write("::maya version {}   | maya env mode: {}{}".format(maya_v,env_mode,os.linesep))
        for v in var:
            wf.write("<<  {}  >> :{}".format(v,os.linesep))
            v_v = var_data[v]
            v_v_wr = "{}\t".format(os.linesep).join(v_v.split(';'))
            wf.write("\t{}{}".format(v_v_wr,os.linesep))

if __name__ == '__main__':
    main()