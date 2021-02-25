import maya.cmds as mc
from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
reload(sk_infoConfig)
shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
cacheNode=mc.ls(type='cacheFile')
for one in cacheNode:
    mc.setAttr('%s.cachePath'%one,'Z:/Projects/DiveollyDive5/project/data/GeoCache/%s/%s/'%(shotInfos[1],shotInfos[2]),type='string')
mc.file(f=1,save=1)