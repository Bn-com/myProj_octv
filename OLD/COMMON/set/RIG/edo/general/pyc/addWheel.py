def SK_addWheel(cusName):
    wheels = ls(sl = True)
    Name = cusName[0]
    jntsPos = []
    jnts = []
    Locs = []
    LocGeo = []
    LocPoint = []
    LocPointPos = []
    for i,wl in enumerate(wheels):
        pos = objectCenter(wl,gl = True)
        Loc = Name+'_LOC'
        locPos = xform(Loc,q = True,t = True,ws = True)
        select(cl = True)
        jnt = joint(p = pos,n = cusName[i]+'_JNT')
        
        LocPt = duplicate(Loc,n = cusName[i]+'_LOC_Point')[0]
        LocGo = duplicate(Loc,n = cusName[i]+'_LOC_Geometry')[0]
        addAttr(LocGo,at = 'float',ln = 'sign')
        PNTConstraint = pointConstraint(LocPt,LocGo,Loc)[0]
        pointConstraint(LocPt,LocGo)
        addAttr(jnt,at = 'float',ln = 'Lock',k = False)
        jntRV = createNode('reverse',n = cusName[i]+'_RV',ss = True)
        connectAttr(jnt+'.Lock',jntRV+'.inputX')
        connectAttr(jntRV+'.outputX',PNTConstraint+'.'+LocPt+'W0')
        connectAttr(jnt+'.Lock',PNTConstraint+'.'+LocGo+'W1')
#        connectAttr(curGrp+'.outbess'+str(i),jnt+'.Lock')    
        jnts.append(jnt)
        jntsPos.append(pos)
        LocPointPos.append(locPos)
        Locs.append(Loc)
        LocPoint.append(LocPt)
        LocGeo.append(LocGo)
    
#    LfCar = group(empty = True,n = 'Car_Con_'+Name)
#    xform(LfCar,t = LocPointPos[0],ws = True)
#    parent(LfCar,carName)
    
    PIOGRP = []
    upJntsGrp = ['UP','POI','NO','Trans','JUST','EX','MAN']
    for wheelJnt in upJntsGrp:
        for jnt in jnts:
            newGrp = group(jnt,n = jnt+'_'+wheelJnt)
            if wheelJnt == 'POI':
                pointConstraint(jnt.replace('JNT','LOC'),newGrp,mo  = True)
            if wheelJnt == 'UP':            
                PIOGRP.append(newGrp)
    
    addAttr('slectLock',at = 'float',ln = Name)            
    MidWheelUPLoc = spaceLocator(n = Name+'_Wheel_UP_LOC')[0]
    MidWheelDNLoc = spaceLocator(n = Name+'_Wheel_DN_LOC')[0]  
    TemNode = pointConstraint(Name+'_JNT',MidWheelUPLoc)
    delete(TemNode)
    TemNode = pointConstraint(Name+'_LOC',MidWheelDNLoc)
    delete(TemNode)    
    wheelNode = createNode('distanceBetween',n = Name+'_DIB')
    connectAttr(MidWheelUPLoc+'.worldMatrix',wheelNode+'.inMatrix1')
    connectAttr(MidWheelDNLoc+'.worldMatrix',wheelNode+'.inMatrix2')
    connectAttr(wheelNode+'.distance','slectLock.'+Name)
    parent(MidWheelUPLoc,MidWheelDNLoc,'rad_Grp')
    parent(LocGeo,'GeoLoc_All_GRP')
    parent(Locs,'GeoLoc_All_GRP')    
    parent(LocPoint,'Locator_All_GRP')
    

    wheelRadi = getAttr(wheelNode+'.distance')
    Rt_F_wheel = circle(ch = False,nr = (1,0,0),n = Name+'_wheel_C',r = wheelRadi)
    setAttr(Rt_F_wheel[0]+'.visibility',cb = False,k = False)
    addAttr(Rt_F_wheel,at = 'float',ln = 'frequency',dv = 30,k = True)
    addAttr(Rt_F_wheel,at = 'float',ln = 'sizeY',dv = 0,k = True)
    addAttr(Rt_F_wheel,at = 'float',ln = 'sizeZ',dv = 0,k = True)
    addAttr(Rt_F_wheel,at = 'float',ln = 'offset',dv = 0,k = True)
    connectAttr(Rt_F_wheel[0]+'.offset',Rt_F_wheel[0].replace('wheel_C','JNT_Trans')+'.ty')
    TemPoints = pointConstraint(Name+'_JNT',Rt_F_wheel)
    delete(TemPoints)
    parent(Rt_F_wheel,Name+'_JNT_MAN')
    makeIdentity(Rt_F_wheel,apply = True,s = True,r = True,t = True)
    parent(Name+'_JNT',Rt_F_wheel)
    
    parent(Name+'_JNT_UP','Wheel_All_GRP')
    connectAttr('MIS.sign',Name+'_LOC_Geometry.sign')
#    SK_hideWheelAttr(Rt_F_wheel)
    
def addlocators(cusName):
    wheels = ls(sl = True)           
    for i,wl in enumerate(wheels):
        minY = xform(wl,q = True,bb = True,ws = True)[1]
        pos = objectCenter(wl,gl = True)
        locPos = (pos[0],minY,pos[2])
        Loc = spaceLocator(n = cusName[i]+'_LOC')[0]
        xform(Loc,t = locPos,ws = True)
        select(cl = True)
        