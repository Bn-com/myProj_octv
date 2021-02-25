# coding:utf-8
import maya.cmds as mc

class checkAnimation(object):
    def __init__(self):
        pass

    def check(self):
        returnMode = 1
        from idmt.maya.commonCore.core_mayaCommon import sk_animFileCheck
        reload(sk_animFileCheck)
        errorInfoList = []
        '''
        # 检测ref
        errorList = sk_animFileCheck.sk_animFileCheck().shotAssetRefCheck('an', 1, returnMode=returnMode)
        if errorList:
            errorInfoList = errorInfoList + errorList
        '''
        # 检测非server参考
        errorList = sk_animFileCheck.sk_animFileCheck().checkNotServerAssetRef(returnMode=returnMode)
        if errorList:
            errorInfoList = errorInfoList + errorList
        	
        if errorInfoList:
            errorInfo = '--------请处理好这些错误--------'
            print errorInfo
            for errorLine in errorInfoList:
                print errorLine
            print errorInfo
            mc.error()