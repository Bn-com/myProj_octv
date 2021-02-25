#-*- coding: utf-8 -*-
'''
Created on 2014年8月26日
@author: zhaozhongjie
import idmt.maya.Pluto.Utility.EclipseToMaya as etm;reload(etm);etm.main()

源代码：

import maya.cmds as cmds
if cmds.commandPort(':7720', q=True) !=1:
    cmds.commandPort(n=':7720', eo = False, nr = True)
'''

def main():
    
    import maya.cmds as cmds
    import os
#    if os.getenv('USERNAME') != 'zhaozhongjie':
#        return 
    Port = ''
    for i in range(100):
        testPort = ':%s'%(str(7720+i))
    
        if cmds.commandPort(testPort, q=True) ==1:
            Port = testPort
            break
        else:
            try: 
                cmds.commandPort(n=testPort, eo = False, nr = True)
                Port = testPort
                break
            except:
                continue
    print '-------   '+Port+'   -------'        
