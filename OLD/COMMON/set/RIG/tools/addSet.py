#-*- coding: utf-8 -*-
import maya.cmds as rig
from RIG.commonly.resetControllerDefaultPose import SK_creatConDefaultPos


def SK_AddToSet(SetName,AddObjs,backup = False):
    if rig.objExists(SetName):
        if AddObjs:
            rig.sets(AddObjs,add = SetName)
            if backup:
                SK_creatConDefaultPos(1)
        else:
            rig.warning(u'没有选择物体')
    
    else:
        ret = rig.confirmDialog(t = u'警告',\
                            m = u'在文件中没有找到boydSet.\n\nnew---将重新生成一个bodySet.\ncancel---将结束操作.',\
                            ma = 'left',\
                            button = ('new','cancel'),\
                            defaultButton = 'new',\
                            cancelButton = 'cancel',\
                            dismissString = 'cancel')
        if ('new' == ret):
            if AddObjs:
                rig.sets(AddObjs,n = SetName)
                if backup:
                    SK_creatConDefaultPos(1)
            else:
                rig.warning(u'没有选择物体')
            
        elif('cancel' == ret):
            print 'exit'
            
