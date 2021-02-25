

import ctypes
import maya.OpenMaya

def BeforeCreateReference_Calimero(retCode, file, clientData):
    ctypes.cast(long(retCode), ctypes.POINTER(ctypes.c_ubyte)).contents.value = True
    pathOld = file.rawFullName()
    from idmt.maya.py_common import sk_referenceConfig
    reload(sk_referenceConfig);
    pathNew = sk_referenceConfig.sk_referenceConfig().calimeroPathToGDC(pathOld)
    #pathNew = 'E:/' + file.rawName()
    file.setRawFullName(pathNew)

beforeCreateReferenceCheckId_Calimero = maya.OpenMaya.MSceneMessage.addCheckFileCallback(maya.OpenMaya.MSceneMessage.kBeforeCreateReferenceCheck, BeforeCreateReference_Calimero)
#maya.OpenMaya.MSceneMessage.removeCallback(beforeCreateReferenceCheckId)
