import maya.cmds as mc
import maya.mel as mm
def sk4_changeeye():    
    FaceSkinMesh=mc.ls('sk_sc*sour*:MSH_c_hi_body_faceCtrl',type='transform')[0]
    NameSpace=FaceSkinMesh.split(':')[0]
    BodyVtxs=[u'%s:MSH_c_hi_body_faceCtrl.vtx[1526]'%NameSpace, u'%s:MSH_c_hi_body_faceCtrl.vtx[1538]'%NameSpace, u'%s:MSH_c_hi_body_faceCtrl.vtx[1554]'%NameSpace, u'%s:MSH_c_hi_body_faceCtrl.vtx[1555]'%NameSpace, u'%s:MSH_c_hi_body_faceCtrl.vtx[1563]'%NameSpace, u'%s:MSH_c_hi_body_faceCtrl.vtx[1572]'%NameSpace, u'%s:MSH_c_hi_body_faceCtrl.vtx[1573]'%NameSpace, u'%s:MSH_c_hi_body_faceCtrl.vtx[1580]'%NameSpace, u'%s:MSH_c_hi_body_faceCtrl.vtx[1581]'%NameSpace, u'%s:MSH_c_hi_body_faceCtrl.vtx[1623]'%NameSpace, u'%s:MSH_c_hi_body_faceCtrl.vtx[1624]'%NameSpace, u'%s:MSH_c_hi_body_faceCtrl.vtx[1625]'%NameSpace, u'%s:MSH_c_hi_body_faceCtrl.vtx[1636]'%NameSpace, u'%s:MSH_c_hi_body_faceCtrl.vtx[1637]'%NameSpace, u'%s:MSH_c_hi_body_faceCtrl.vtx[1638]'%NameSpace, u'%s:MSH_c_hi_body_faceCtrl.vtx[1909]'%NameSpace, u'%s:MSH_c_hi_body_faceCtrl.vtx[2019]'%NameSpace, u'%s:MSH_c_hi_body_faceCtrl.vtx[2037]'%NameSpace, u'%s:MSH_c_hi_body_faceCtrl.vtx[2045]'%NameSpace, u'%s:MSH_c_hi_body_faceCtrl.vtx[2046]'%NameSpace, u'%s:MSH_c_hi_body_faceCtrl.vtx[2047]'%NameSpace, u'%s:MSH_c_hi_body_faceCtrl.vtx[2048]'%NameSpace, u'%s:MSH_c_hi_body_faceCtrl.vtx[2051]'%NameSpace, u'%s:MSH_c_hi_body_faceCtrl.vtx[2052]'%NameSpace, u'%s:MSH_c_hi_body_faceCtrl.vtx[2053]'%NameSpace, u'%s:MSH_c_hi_body_faceCtrl.vtx[2057]'%NameSpace, u'%s:MSH_c_hi_body_faceCtrl.vtx[2058]'%NameSpace, u'%s:MSH_c_hi_body_faceCtrl.vtx[2059]'%NameSpace, u'%s:MSH_c_hi_body_faceCtrl.vtx[2063]'%NameSpace, u'%s:MSH_c_hi_body_faceCtrl.vtx[2064]'%NameSpace, u'%s:MSH_c_hi_body_faceCtrl.vtx[2065]'%NameSpace, u'%s:MSH_c_hi_body_faceCtrl.vtx[2075]'%NameSpace, u'%s:MSH_c_hi_body_faceCtrl.vtx[2077]'%NameSpace, u'%s:MSH_c_hi_body_faceCtrl.vtx[3759]'%NameSpace, u'%s:MSH_c_hi_body_faceCtrl.vtx[3771]'%NameSpace, u'%s:MSH_c_hi_body_faceCtrl.vtx[3787]'%NameSpace, u'%s:MSH_c_hi_body_faceCtrl.vtx[3788]'%NameSpace, u'%s:MSH_c_hi_body_faceCtrl.vtx[3789]'%NameSpace, u'%s:MSH_c_hi_body_faceCtrl.vtx[3796]'%NameSpace, u'%s:MSH_c_hi_body_faceCtrl.vtx[3797]'%NameSpace, u'%s:MSH_c_hi_body_faceCtrl.vtx[3805]'%NameSpace, u'%s:MSH_c_hi_body_faceCtrl.vtx[3806]'%NameSpace, u'%s:MSH_c_hi_body_faceCtrl.vtx[3813]'%NameSpace, u'%s:MSH_c_hi_body_faceCtrl.vtx[3814]'%NameSpace, u'%s:MSH_c_hi_body_faceCtrl.vtx[3855]'%NameSpace, u'%s:MSH_c_hi_body_faceCtrl.vtx[3856]'%NameSpace, u'%s:MSH_c_hi_body_faceCtrl.vtx[3857]'%NameSpace, u'%s:MSH_c_hi_body_faceCtrl.vtx[3858]'%NameSpace, u'%s:MSH_c_hi_body_faceCtrl.vtx[3868]'%NameSpace, u'%s:MSH_c_hi_body_faceCtrl.vtx[3869]'%NameSpace, u'%s:MSH_c_hi_body_faceCtrl.vtx[3870]'%NameSpace, u'%s:MSH_c_hi_body_faceCtrl.vtx[3871]'%NameSpace, u'%s:MSH_c_hi_body_faceCtrl.vtx[4252]'%NameSpace, u'%s:MSH_c_hi_body_faceCtrl.vtx[4270]'%NameSpace, u'%s:MSH_c_hi_body_faceCtrl.vtx[4278]'%NameSpace, u'%s:MSH_c_hi_body_faceCtrl.vtx[4279]'%NameSpace, u'%s:MSH_c_hi_body_faceCtrl.vtx[4280]'%NameSpace, u'%s:MSH_c_hi_body_faceCtrl.vtx[4281]'%NameSpace, u'%s:MSH_c_hi_body_faceCtrl.vtx[4284]'%NameSpace, u'%s:MSH_c_hi_body_faceCtrl.vtx[4285]'%NameSpace, u'%s:MSH_c_hi_body_faceCtrl.vtx[4286]'%NameSpace, u'%s:MSH_c_hi_body_faceCtrl.vtx[4287]'%NameSpace, u'%s:MSH_c_hi_body_faceCtrl.vtx[4290]'%NameSpace, u'%s:MSH_c_hi_body_faceCtrl.vtx[4291]'%NameSpace, u'%s:MSH_c_hi_body_faceCtrl.vtx[4292]'%NameSpace, u'%s:MSH_c_hi_body_faceCtrl.vtx[4293]'%NameSpace, u'%s:MSH_c_hi_body_faceCtrl.vtx[4296]'%NameSpace, u'%s:MSH_c_hi_body_faceCtrl.vtx[4297]'%NameSpace, u'%s:MSH_c_hi_body_faceCtrl.vtx[4298]'%NameSpace, u'%s:MSH_c_hi_body_faceCtrl.vtx[4299]'%NameSpace, u'%s:MSH_c_hi_body_faceCtrl.vtx[4308]'%NameSpace, u'%s:MSH_c_hi_body_faceCtrl.vtx[4310]'%NameSpace]
    VtxsWeights=[[0.44947976379434834, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.15357315540313721, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.39694708080251451, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.50923246833412972, 0.0, 0.0, 0.0, 0.0, 0.0, 0.1674550324678421, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.26588838557977268, 0.057424113618255453, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.51491093633772023, 0.0040889455251835061, 0.021177015867964565, 0.0, 0.0, 0.0, 0.44806975126266479, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.011753351006466864, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.15886399344045493, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.59438097476959229, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.19686957133521546, 0.049885460454737317, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.090671079651413078, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.36814126372337341, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.44017448008352317, 0.10101317654169031, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.13170885983125796, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.057190953473744012, 0.45423337817192078, 0.0, 0.0, 0.0, 0.0, 0.0, 0.036390828868229308, 0.32047597965484792, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.15129006498837516, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.008322599259859724, 0.77772188186645508, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.06266545388531003, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.18621598268427714, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.059363104403018951, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.30519840219424132, 0.44922251071846264, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.26988947641539168, 0.0, 5.7527863413573141e-05, 0.0, 0.0, 0.0, 0.0, 0.097000002861022949, 0.18376503637324329, 0.0, 0.0, 0.0, 0.0, 0.0, 0.23555399982041894, 0.21373395666650966, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.15704079428986401, 0.0, 0.0020602638095059021, 0.0, 0.0, 0.0, 0.0, 0.026618487661676668, 0.75050818920135498, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.063772265037598447, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.3353219041887765, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.58676439523696899, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.07791370057425448, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.40201061622003265, 0.0, 0.0, 0.0, 0.0, 0.048798483335016962, 0.0, 0.0, 0.4108690619468689, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.082043136433552419, 0.056278702064529153, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.11410829018632263, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.55057746171951294, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.25995287864807909, 0.075361369446085319, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.1612470310688435, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0038165328822979709, 0.71598356962203979, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.11895286642681875, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.53417749243963553, 0.0, 0.0, 0.0, 0.0, 0.0, 0.32028114795684814, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.12495002759287632, 0.020591332010640052, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.47983085945251558, 0.0, 0.00050061198269191589, 0.0, 0.0, 0.023859485552462069, 0.0, 0.0059303289277052307, 0.48987871408462524, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.52417206160758556, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.073947541415691376, 0.0, 0.0, 0.0, 0.0, 0.0, 0.20211456246358767, 0.19976583451313534, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.32589214739232264, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.14509071271485724, 0.10644122213125229, 0.0, 0.0, 0.0, 0.0, 0.0, 0.42257591776156789, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.2104352742211868, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.17107323977557809, 0.34286138415336609, 0.0, 0.0, 0.0, 0.0, 0.0, 0.10264814506477196, 0.17298195678509712, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.18259857676546407, 0.0, 0.0034292216316480382, 0.0, 0.0, 0.0, 0.0, 0.21787282824516296, 0.48112596351176562, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.11497340984595923, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.14297990600609686, 0.0, 0.010951176473503146, 0.0, 0.0, 0.0, 0.0, 0.22154732048511505, 0.57787746237432391, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0052485471170927427, 0.041395587543868247, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.13929571982583225, 0.0, 0.025317571874275191, 0.0, 0.0, 0.0, 0.0, 0.16019941299935608, 0.6495821475982666, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.025605147702269907, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.45565144677457231, 0.0, 0.014740244796607491, 0.0, 0.0, 0.0, 0.13942873341432221, 0.14714083075523376, 0.0, 0.0, 0.0, 0.0, 0.0, 0.10603631385238094, 0.13700243040688317, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.4360864052092624, 0.0093342037122488668, 0.025323532997968703, 0.0, 0.0, 0.0, 0.27563969782121506, 0.16931067407131195, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0289836887868931, 0.055321797401100027, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.3703428031997123, 0.021678208112938024, 0.049889185506344635, 0.0, 0.0, 0.0, 0.38184358763494114, 0.17367096245288849, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0025752530931754192, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.34693260278504334, 0.0, 0.019456606901849763, 0.0, 0.0, 0.0, 0.048457569055735818, 0.31061825156211853, 0.023817515389447787, 0.0, 0.0, 0.0, 0.0, 0.0, 0.25071745430580478, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.33952104934637756, 0.01067653600408814, 0.034088858879972837, 0.0, 0.0, 0.0, 0.097356788008693462, 0.39928194880485535, 0.045292839062237626, 0.0, 0.0, 0.0, 0.0, 0.0, 0.073781979893775121, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.25710665929483967, 0.025827906822551389, 0.052830198450893491, 0.0, 0.0, 0.0, 0.14973893251011836, 0.4395429790019989, 0.066201638399041099, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0087516855205570874, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.28102847388915281, 0.0, 0.016124015473040352, 0.0, 0.0, 0.0, 0.0, 0.30566844344139099, 0.14836977589504916, 0.0, 0.0, 0.0, 0.0, 0.0, 0.24880929130136664, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.30145428479341052, 0.00062541352994162022, 0.023830042218206116, 0.0, 0.0, 0.0, 0.029257512622189528, 0.42237585783004761, 0.15454796491801434, 0.0, 0.0, 0.0, 0.0, 0.0, 0.067908924088190312, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.24018487590246304, 0.0091920880844489159, 0.040936611792279136, 0.0, 0.0, 0.0, 0.055487363474564746, 0.46587908267974854, 0.18242455627809839, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0058954217883973332, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.18949460057040393, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.029531903824804098, 0.30397641658782959, 0.0, 0.0, 0.0, 0.0, 0.0, 0.070167445121735325, 0.40682963389522697, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.14329722491679145, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.23335923254489899, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.51761594013984447, 0.10572760239846514, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.44951868306027765, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.15352420226275931, 0.0, 0.0, 0.0, 0.0, 0.0, 9.9664552630349481e-05, 0.39684826678712587, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.9016557965522922e-06, 5.2816814102284277e-06, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.50910341850373231, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.16711090638461437, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.26633594626695339, 0.057449728844699892, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.51526681324508161, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0040632430423555846, 0.021043900402536949, 0.0, 0.0, 0.0, 0.44703672610665024, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.012510583519667596, 7.8733683708023024e-05, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.15884905265606372, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.9512206402508792e-05, 0.0, 0.0, 0.59424483768158087, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.19692750703649015, 0.049959090419462747, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.28205513052041747, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.063880361677311606, 0.0, 0.0, 0.31680298706547622, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.14404435449308298, 0.19321716624371177, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.090720182556572118, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.6526441959588747e-06, 0.36843621842762225, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.43989280477430487, 0.10094914159730467, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.11713657132631283, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.063726962718142488, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.2501087683012102, 0.56902769765433447, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.13170891372114543, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.057190811582760966, 0.45423294672114889, 0.0, 0.0, 0.0, 0.0, 0.0, 0.036390841625584605, 0.32047633371703271, 1.5263232736278231e-07, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.15128930284238426, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.6088082507190738e-06, 0.0, 0.0, 0.0, 0.0, 0.0083322485819727135, 0.7777137408839504, 0.0, 0.0, 0.0, 0.0, 0.0, -6.0795624525138165e-11, 0.062663098944237508, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.18618416427578113, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.059414475360882353, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.30520765986849163, 0.44919370049484486, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.26988950732567696, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 5.7527849697861686e-05, 0.0, 0.0, 0.0, 0.0, 0.096999979734420094, 0.18376499256024442, 0.0, 0.0, 0.0, 0.0, 0.0, 0.23555402958867314, 0.2137339629412876, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.39259792236526836, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.018813469228817343, 0.038041327270616009, 0.0, 0.0, 0.0, 0.55044074914012731, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.00010653199517096194, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.15704051712425199, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0020635185779372838, 0.0, 0.0, 0.0, 0.0, 0.026632240167676281, 0.75049741893551636, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.063766305194618206, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.33508519908165962, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.2524976320173159e-06, 0.0, 0.0, 0.0, 0.0, 1.6182195993690612e-05, 0.58686947899543673, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.077991609857108554, 3.6277372169368252e-05, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.40160014061931865, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.048780721966266594, 0.0, 0.0, 0.41087467566263969, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.08224577358481136, 0.056498688108756127, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.27297231508716713, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.00049032398498035843, 0.0, 0.0, 0.17496955178279833, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.17248289037971043, 0.37908491876534389, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.11411159017058033, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5505238829816238, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.25998323405076995, 0.075381292797025864, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.16124635591142356, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.0471801782134317e-07, 0.0, 0.0, 0.0, 0.0, 0.0038245791064640978, 0.71597846616679861, 0.0, 0.0, 0.0, 0.0, 0.0, 1.9397241162091477e-07, 0.11895000012488435, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.53398650490566679, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.31962706045046424, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.12569967564837098, 0.020686758995498062, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.52419052531955934, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.073850947377132062, 0.0, 0.0, 0.0, 0.0, 0.0, 0.20218994945893026, 0.19965776524576803, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 8.3356076787522405e-05, 2.7456521822724045e-05, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.32589222640425886, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.14509055704941018, 0.10644110793221007, 0.0, 0.0, 0.0, 0.0, 0.0, 0.42257585106596202, 2.5754815891380997e-07, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.21043524727102447, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.8004989183900448e-11, 0.0, 0.0, 0.0, 0.0, 0.17107306721182927, 0.34286135970395804, 0.0, 0.0, 0.0, 0.0, 0.0, 0.10264819153382794, 0.17298213423135531, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.18259860663100039, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0034292179524923684, 0.0, 0.0, 0.0, 0.0, 0.21787277803465174, 0.48112581516996517, 0.0, 0.0, 0.0, 0.0, 0.0, 1.1012951202189298e-07, 0.11497347208237824, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.14297990600609686, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.010951176473503146, 0.0, 0.0, 0.0, 0.0, 0.22154732048511505, 0.57787746237432391, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0052485471170927427, 0.041395587543868247, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.13929572860961661, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.025317537622119409, 0.0, 0.0, 0.0, 0.0, 0.16019955926416543, 0.64958197664097495, 0.0, 0.0, 0.0, 0.0, 0.0, 1.251351146004854e-08, 0.025605185349612213, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.45577421967030946, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.014710151432799492, 0.0, 0.0, 0.0, 0.13933594331397406, 0.14690667421664955, 0.0, 0.0, 0.0, 0.0, 0.0, 0.10630553510875738, 0.13696747625750999, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.43625852165304063, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0093155433342392603, 0.02527740929197584, 0.0, 0.0, 0.0, 0.27567371115135741, 0.16901713423379619, 0.0, 0.0, 0.0, 0.0, 0.0, 0.029169762785873403, 0.055287917549717402, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.37050299254899499, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.02165850690132063, 0.049849772452902938, 0.0, 0.0, 0.0, 0.38207901224460417, 0.17332825216329528, 0.0, 0.0, 0.0, 0.0, 0.0, 1.1292422402671824e-05, 0.0025701712664792761, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.14632441206296415, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.039791461421775684, 0.051509913378532002, 0.0, 0.0, 0.0, 0.51504388172965432, 0.1743677647809827, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.00011664588226858704, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.072845920743822568, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.34701936919822146, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.9802130062677484e-06, 0.019456993781725045, 0.0, 0.0, 0.0, 0.048595234184159855, 0.31048469209176599, 0.023796679404238796, 0.0, 0.0, 0.0, 0.0, 5.9906314098519125e-05, 0.25058314481278404, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.33955605104887876, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.010689959465279624, 0.034108074344990962, 0.0, 0.0, 0.0, 0.097696818017653342, 0.39901399605649468, 0.045239313419570201, 0.0, 0.0, 0.0, 0.0, 0.0, 0.073695787647132499, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.25689921357358375, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.02585320656056268, 0.052829662337321691, 0.0, 0.0, 0.0, 0.15028108415491609, 0.4391557511159947, 0.066118540541850651, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0087369155201402014, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.00012562619563040586, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.092756296844799774, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.043877450907006788, 0.057132898186716054, 0.0, 0.0, 0.0, 0.23480007212082429, 0.3976577181371353, 0.10036695117672355, 0.0, 0.0, 0.0, 0.0, 0.0, 0.00040861369967782425, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.072999998927116394, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.28102835114074853, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -4.9858355123542691e-12, 0.01612398741214555, 0.0, 0.0, 0.0, -2.3324270814621244e-10, 0.30566820878551115, 0.14837011358178886, 0.0, 0.0, 0.0, 0.0, 0.0, 0.24880903893369702, 3.0038433742050146e-07, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.30147188228692939, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0006388719000286014, 0.023844560973511182, 0.0, 0.0, 0.0, 0.029336695454420605, 0.42236285743347135, 0.15444598195829676, 0.0, 0.0, 0.0, 0.0, 0.0, 0.067899149978790249, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.24017413611954877, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0092141811796771049, 0.040950846767211613, 0.0, 0.0, 0.0, 0.055609328460149654, 0.46584174251922539, 0.18229935451435664, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0058971349200084757, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.327553437429122e-05, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.12026647431930335, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.027087578806576983, 0.045501297833315288, 0.0, 0.0, 0.0, 0.065359463416922642, 0.42324001318516952, 0.24548494814469529, 0.0, 0.0, 0.0, 0.0, 0.0, 6.0225366900620237e-05, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.072999998927116394, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.18949463660434274, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.029531878741605337, 0.30397628706199398, 0.0, 0.0, 0.0, 0.0, 0.0, 0.070167405953390938, 0.40682973334721928, 5.8291447642787597e-08, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.14330336814967845, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.9270923991881575e-06, 0.23336862307415007, 0.0, 0.0, 0.0, 0.0, 0.0, 9.3307238856906601e-06, 0.51760120800256781, 0.10571354295731883, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]
    bodyInfJoints=[u'%s:faceRigBase_skin_joint'%NameSpace, u'%s:L_upperEyeLid_skin_joint'%NameSpace, u'%s:L_lowerEyeLid_skin_joint'%NameSpace, u'%s:L_upperEyeLid_skin_1_joint'%NameSpace, u'%s:L_upperEyeLid_skin_2_joint'%NameSpace, u'%s:L_upperEyeLid_skin_3_joint'%NameSpace, u'%s:L_lowerEyeLid_skin_1_joint'%NameSpace, u'%s:L_lowerEyeLid_skin_2_joint'%NameSpace, u'%s:L_lowerEyeLid_skin_3_joint'%NameSpace, u'%s:L_eyeBrow_skin_1_joint'%NameSpace, u'%s:L_eyeBrow_skin_2_joint'%NameSpace, u'%s:L_eyeBrow_skin_3_joint'%NameSpace, u'%s:L_eyeBrow_skin_4_joint'%NameSpace, u'%s:L_upperCheek_skin_1_joint'%NameSpace, u'%s:L_upperCheek_skin_2_joint'%NameSpace, u'%s:L_upperCheek_skin_3_joint'%NameSpace, u'%s:L_upperCheek_skin_4_joint'%NameSpace, u'%s:L_laughLine_skin_1_joint'%NameSpace, u'%s:L_laughLine_skin_2_joint'%NameSpace, u'%s:L_laughLine_skin_3_joint'%NameSpace, u'%s:L_laughLine_skin_4_joint'%NameSpace, u'%s:R_upperEyeLid_skin_joint'%NameSpace, u'%s:R_lowerEyeLid_skin_joint'%NameSpace, u'%s:R_upperEyeLid_skin_1_joint'%NameSpace, u'%s:R_upperEyeLid_skin_2_joint'%NameSpace, u'%s:R_upperEyeLid_skin_3_joint'%NameSpace, u'%s:R_lowerEyeLid_skin_1_joint'%NameSpace, u'%s:R_lowerEyeLid_skin_2_joint'%NameSpace, u'%s:R_lowerEyeLid_skin_3_joint'%NameSpace, u'%s:R_eyeBrow_skin_1_joint'%NameSpace, u'%s:R_eyeBrow_skin_2_joint'%NameSpace, u'%s:R_eyeBrow_skin_3_joint'%NameSpace, u'%s:R_eyeBrow_skin_4_joint'%NameSpace, u'%s:R_upperCheek_skin_1_joint'%NameSpace, u'%s:R_upperCheek_skin_2_joint'%NameSpace, u'%s:R_upperCheek_skin_3_joint'%NameSpace, u'%s:R_upperCheek_skin_4_joint'%NameSpace, u'%s:nose_skin_joint'%NameSpace, u'%s:L_nostril_skin_joint'%NameSpace, u'%s:R_nostril_skin_joint'%NameSpace, u'%s:upperLip_skin_1_joint'%NameSpace, u'%s:upperLip_skin_7_joint'%NameSpace, u'%s:upperLip_skin_2_joint'%NameSpace, u'%s:upperLip_skin_3_joint'%NameSpace, u'%s:upperLip_skin_4_joint'%NameSpace, u'%s:upperLip_skin_5_joint'%NameSpace, u'%s:upperLip_skin_6_joint'%NameSpace, u'%s:lowerLip_skin_1_joint'%NameSpace, u'%s:lowerLip_skin_2_joint'%NameSpace, u'%s:lowerLip_skin_3_joint'%NameSpace, u'%s:lowerLip_skin_4_joint'%NameSpace, u'%s:lowerLip_skin_5_joint'%NameSpace, u'%s:R_laughLine_skin_1_joint'%NameSpace, u'%s:R_laughLine_skin_2_joint'%NameSpace, u'%s:R_laughLine_skin_3_joint'%NameSpace, u'%s:R_laughLine_skin_4_joint'%NameSpace, u'%s:jawLine_skin_1_joint'%NameSpace, u'%s:jawLine_skin_2_joint'%NameSpace, u'%s:jawLine_skin_3_joint'%NameSpace, u'%s:jawLine_skin_4_joint'%NameSpace, u'%s:jawLine_skin_5_joint'%NameSpace, u'%s:jawLine_skin_6_joint'%NameSpace, u'%s:jawLine_skin_7_joint'%NameSpace, u'%s:jawLine_skin_8_joint'%NameSpace, u'%s:jaw_skin_joint'%NameSpace, u'%s:L_ear_skin_joint'%NameSpace, u'%s:R_ear_skin_joint'%NameSpace]
    for i in BodyVtxs:
        VtxIndex=BodyVtxs.index(i)
        for n in bodyInfJoints:
            JointIndex=bodyInfJoints.index(n)
            mc.skinPercent( '%s:skinCluster1'%NameSpace,i,tv=[n,VtxsWeights[VtxIndex][JointIndex]] )
    #------------------eyelashlwr-----------------
    mc.setAttr('%s:skinCluster51.envelope'%NameSpace,0)
    mc.setAttr('%s:MSH_r_hi_eyelash_parentConstraint1.w0'%NameSpace,lock=0)
    mc.setAttr('%s:MSH_r_hi_eyelash_parentConstraint1.Head_joint3W0'%NameSpace,0)
    mc.setAttr('%s:MSH_r_hi_eyelash_scaleConstraint1.w0'%NameSpace,lock=0)
    mc.setAttr('%s:MSH_r_hi_eyelash_scaleConstraint1.Head_joint3W0'%NameSpace,0)
    
    mc.setAttr('%s:skinCluster53.envelope'%NameSpace,0)
    mc.setAttr('%s:MSH_l_hi_eyelash_parentConstraint1.w0'%NameSpace,lock=0)
    mc.setAttr('%s:MSH_l_hi_eyelash_parentConstraint1.Head_joint3W0'%NameSpace,0)
    mc.setAttr('%s:MSH_l_hi_eyelash_scaleConstraint1.w0'%NameSpace,lock=0)
    mc.setAttr('%s:MSH_l_hi_eyelash_scaleConstraint1.Head_joint3W0'%NameSpace,0)
    
    mc.setAttr('%s:skinCluster1.envelope'%NameSpace,0)
    
    mc.select(['%s:MSH_c_hi_body_faceCtrl'%NameSpace,'%s:MSH_r_hi_eyelashlwr'%NameSpace],r=1)
    mc.copySkinWeights(noMirror=1,surfaceAssociation='closestPoint',influenceAssociation='closestJoint')
    mc.select(['%s:MSH_c_hi_body_faceCtrl'%NameSpace,'%s:MSH_l_hi_eyelashlwr'%NameSpace],r=1)
    mc.copySkinWeights(noMirror=1,surfaceAssociation='closestPoint',influenceAssociation='closestJoint')
    
    mc.setAttr('%s:skinCluster51.envelope'%NameSpace,1)
    mc.setAttr('%s:MSH_r_hi_eyelash_parentConstraint1.Head_joint3W0'%NameSpace,1)
    mc.setAttr('%s:MSH_r_hi_eyelash_parentConstraint1.w0'%NameSpace,lock=1)
    mc.setAttr('%s:MSH_r_hi_eyelash_scaleConstraint1.Head_joint3W0'%NameSpace,1)
    mc.setAttr('%s:MSH_r_hi_eyelash_scaleConstraint1.w0'%NameSpace,lock=1)
    
    mc.setAttr('%s:skinCluster53.envelope'%NameSpace,1)
    mc.setAttr('%s:MSH_l_hi_eyelash_parentConstraint1.Head_joint3W0'%NameSpace,1)
    mc.setAttr('%s:MSH_l_hi_eyelash_parentConstraint1.w0'%NameSpace,lock=1)
    mc.setAttr('%s:MSH_l_hi_eyelash_scaleConstraint1.Head_joint3W0'%NameSpace,1)
    mc.setAttr('%s:MSH_l_hi_eyelash_scaleConstraint1.w0'%NameSpace,lock=1)
    
    mc.setAttr('%s:skinCluster1.envelope'%NameSpace,1)
    
    mc.setAttr('%s:shader_file114.fileTextureName'%NameSpace,'\\\\file-cluster\GDC\Projects\Strawberry\Project\sourceimages\characters\sc069001sour\sc001001strawberry_skin_color_h.iff',type='string')    