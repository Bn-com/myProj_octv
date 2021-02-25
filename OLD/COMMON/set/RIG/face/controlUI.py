#-*- coding: utf-8 -*-
import maya.cmds as rig
from RIG.face.controlers import CreateControler
from RIG.face.baseClass import *

class conWidge(object):
    def __init__(self):
        self.Color = 17
        
        
    def slideSinge(self,Text,sign = 'DEL'):
        WD = CreateControler(self.Color,(1,1,-1))
        AR = WD.SK_b09(Text+'_M')
        ARGRP = rig.group(AR,n = AR+'_CON_GRP',r = True)
        rig.setAttr(ARGRP+'.sx',0.08)
        rig.setAttr(ARGRP+'.sy',0.08)
        rig.setAttr(ARGRP+'.sz',0.08)
        rig.move(0,0,0.165959,AR+'.scalePivot',AR+'.rotatePivot')
        rig.setAttr(ARGRP+'.tz',-0.166)
        
        SQ = WD.SK_b13(Text+'_RANGE_SQ')
        SQGRP = rig.group(SQ,n = SQ+'_RANGE_GRP',r = True)
        rig.setAttr(SQGRP+'.sx',0.08)
        rig.setAttr(SQGRP+'.sy',0.08)
        rig.setAttr(SQGRP+'.sz',0.337)                
        rig.setAttr(SQGRP+'.tz',0.674)  
        
        TX = self.text(Text)
        TXGRP = rig.group(TX,n = TX+'_TEXT_GRP',r = True)
        rig.setAttr(TXGRP+'.sx',0.08)
        rig.setAttr(TXGRP+'.sy',0.08)
        rig.setAttr(TXGRP+'.sz',0.08)
        
        if 'up' == sign:
            rig.setAttr(TXGRP+'.tz',1.519) 
        if 'dn' == sign:
            rig.setAttr(TXGRP+'.ry',90)
            MinZ = rig.xform(TXGRP,q = True,bb = True,ws = True)[2]
            MaxZ = rig.xform(TXGRP,q = True,bb = True,ws = True)[5]        
            TZ =  ((MaxZ - MinZ)/-2) - 0.2
            rig.setAttr(TXGRP+'.tz',TZ) 
        if 'lf' == sign:
            rig.setAttr(TXGRP+'.ry',90)
            rig.xform(TXGRP,t = [0.34603909286553236, 0.0, 0.67400000000000027],wd = True) 
        if 'rt' == sign:
            rig.setAttr(TXGRP+'.ry',90)
            rig.xform(TXGRP,t = [-0.33073309305179166, 0.0, 0.67400000000000027],wd = True) 
        
        partConGRP = rig.group(TXGRP,SQGRP,ARGRP,n = Text+'_WIDGE_GRP')
        rig.makeIdentity(partConGRP,apply = True,s = True,t = True,r = True)
        
        rig.transformLimits(AR,tz = (0,1),etz = (1,1))
        rig.setAttr(TXGRP+'.overrideEnabled',1)
        rig.setAttr(TXGRP+'.overrideDisplayType',2)
        rig.setAttr(SQGRP+'.template',1)

        if 'DEL' == sign:
            rig.delete(TXGRP)
        
        return partConGRP,AR
        
    def square(self,Text,sign = False):
        WD = CreateControler(self.Color,(1,1,-1))
        AR = WD.SK_b13(Text+'_M')
        ARGRP = rig.group(AR,n = AR+'_CON_GRP',r = True)
        rig.makeIdentity(ARGRP,apply = True,t = True,s = True,r = True)
        if sign:
            ARShape = rig.listRelatives(AR,s = True)[0]
            rig.setAttr(ARShape+'.overrideEnabled',0)            
            rig.setAttr(AR+'.overrideEnabled',1)
            rig.setAttr(AR+'.overrideDisplayType',2)
        
        return ARGRP,AR
    
    def fourSlide(self,Text,sign = 'DEL'):
        WD = CreateControler(self.Color,(1,1,-1))
        AR = WD.SK_b06(Text+'_M')
        ARGRP = rig.group(AR,n = AR+'_CON_GRP',r = True)
        rig.setAttr(ARGRP+'.sx',0.1)
        rig.setAttr(ARGRP+'.sy',0.1)
        rig.setAttr(ARGRP+'.sz',0.1)

        
        SQ = WD.SK_b13(Text+'_RANGE_SQ')
        SQGRP = rig.group(SQ,n = SQ+'_RANGE_GRP',r = True)
        rig.setAttr(SQGRP+'.sx',0.6)
        rig.setAttr(SQGRP+'.sy',0.6)
        rig.setAttr(SQGRP+'.sz',0.6)              

        
        TX = self.text(Text)
        TXGRP = rig.group(TX,n = TX+'_TEXT_GRP',r = True)
        rig.setAttr(TXGRP+'.sx',0.14)
        rig.setAttr(TXGRP+'.sy',0.14)
        rig.setAttr(TXGRP+'.sz',0.14)
        
        if 'up' == sign:
            rig.setAttr(TXGRP+'.tz',1.6) 
        if 'dn' == sign:
            rig.setAttr(TXGRP+'.tz',-1.6) 
        if 'lf' == sign:
            rig.setAttr(TXGRP+'.tx',1.6) 
        if 'rt' == sign:
            rig.setAttr(TXGRP+'.tx',-1.6)  
        
        partConGRP = rig.group(TXGRP,SQGRP,ARGRP,n = Text+'_WIDGE_GRP')
        rig.makeIdentity(partConGRP,apply = True,s = True,t = True,r = True)
        
        rig.transformLimits(AR,tz = (-1,1),etz = (1,1))
        rig.transformLimits(AR,tx = (-1,1),etx = (1,1))
        rig.setAttr(TXGRP+'.overrideEnabled',1)
        rig.setAttr(TXGRP+'.overrideDisplayType',2)
        rig.setAttr(SQGRP+'.template',1)
        
        if 'DEL' == sign:
            rig.delete(TXGRP)
            
#        setRangeNode
        rig.addAttr(AR,at = 'float',ln = AR+'_up',k = True)
        rig.addAttr(AR,at = 'float',ln = AR+'_dn',k = True)        
        rig.addAttr(AR,at = 'float',ln = AR+'_lf',k = True)
        rig.addAttr(AR,at = 'float',ln = AR+'_rt',k = True)
        RNDX = rig.createNode('setRange',n = AR+'_SR',ss = True)
        rig.connectAttr(AR+'.tx',RNDX+'.valueX')
        rig.connectAttr(AR+'.tx',RNDX+'.valueY')
        rig.setAttr(RNDX+'.minX',0)
        rig.setAttr(RNDX+'.minY',1)
        rig.setAttr(RNDX+'.maxX',1)
        rig.setAttr(RNDX+'.maxY',0)
        rig.setAttr(RNDX+'.oldMinX',0)
        rig.setAttr(RNDX+'.oldMinY',-1)
        rig.setAttr(RNDX+'.oldMaxX',1)
        rig.setAttr(RNDX+'.oldMaxY',0)
        rig.connectAttr(RNDX+'.outValueX',AR+'.'+AR+'_lf')
        rig.connectAttr(RNDX+'.outValueY',AR+'.'+AR+'_rt')
                        
        RNDY = rig.createNode('setRange',n = AR+'_SR',ss = True)        
        rig.connectAttr(AR+'.tz',RNDY+'.valueX')
        rig.connectAttr(AR+'.tz',RNDY+'.valueY')
        rig.setAttr(RNDY+'.minX',0)
        rig.setAttr(RNDY+'.minY',1)
        rig.setAttr(RNDY+'.maxX',1)
        rig.setAttr(RNDY+'.maxY',0)
        rig.setAttr(RNDY+'.oldMinX',0)
        rig.setAttr(RNDY+'.oldMinY',-1)
        rig.setAttr(RNDY+'.oldMaxX',1)
        rig.setAttr(RNDY+'.oldMaxY',0)
        rig.connectAttr(RNDY+'.outValueX',AR+'.'+AR+'_up')
        rig.connectAttr(RNDY+'.outValueY',AR+'.'+AR+'_dn')
        # end
                    
        return partConGRP,AR
    

    def text(self,Name,sign = False):
        curveTextName = rig.textCurves(n = 'T_'+Name+'_Text',t = Name,o = True)[0]
        rig.xform(curveTextName,cp = True)
        childObj = rig.listRelatives(curveTextName,c = True,ad = True)
        rig.delete(rig.listConnections(rig.listRelatives(curveTextName,c = True)[0],s = True,d = False)[0])
        rig.move(0,0,0,curveTextName,rpr = True)
        rig.setAttr(curveTextName+'.ry',180)
        rig.setAttr(curveTextName+'.rx',-90)
        rig.makeIdentity(curveTextName,apply = True,s = True,r = True,t = True)

        TransObj = rig.ls(childObj,type = 'transform')
        for i,obj in enumerate(TransObj):
            rig.rename(obj,'T_'+Name+'_'+str(i)+'_C')
            
        if sign:
            rig.setAttr(curveTextName+'.overrideEnabled',1)
            rig.setAttr(curveTextName+'.overrideDisplayType',2)
        
        return curveTextName
    

class faceCoustom(object):
    def __init__(self):
        self.widge = conWidge()
        self.MainCon = 'Face_M'
        self.Lock = LockHideAttr(False,False,False,False)
        self.mouthData = ('Lf_Mouth','Rt_Mouth','Mouth')
        self.eyebrowData = ('Lf_eyeBrow','Rt_eyeBrow','eyebrow')
        self.eyeCloseData = ('Lf_upEye_Close','Lf_dnEye_Close','Lf_Eye','Rt_upEye_Close','Rt_dnEye_Close','Rt_Eye','Close_eye')
        self.extraE = ('A','E','O','U','S','F','BM')

    
    def eyebrow(self):
        eyebrowGrp = self.doubleCon(self.eyebrowData[0], self.eyebrowData[1],self.eyebrowData[2])
        NewEyebrow = rig.rename(eyebrowGrp,eyebrowGrp.replace(self.eyebrowData[0],'Eyebrow_Double'))
        
        rig.setAttr(NewEyebrow+'.tz',7.5)
        return NewEyebrow
    
    def mouth(self):
        mouthGrp = self.doubleCon(self.mouthData[0], self.mouthData[1],self.mouthData[2])
        NewMouth = rig.rename(mouthGrp,mouthGrp.replace(self.mouthData[0],'Mouth_Double'))
        return NewMouth
    
    def eyeClose(self):
        LfSQGRP = self.doubleEye(self.eyeCloseData[0],self.eyeCloseData[1],self.eyeCloseData[2])
        rig.xform(LfSQGRP,t = (-1.459,0,7.52),wd = True)
        RtSQGRP = self.doubleEye(self.eyeCloseData[3],self.eyeCloseData[4],self.eyeCloseData[5])
        rig.xform(RtSQGRP,t = (1.459,0,7.52),wd = True)
        rig.setAttr(RtSQGRP+'.rz',180)
        
        SqGrp,Sq = self.widge.square(self.eyeCloseData[6],True)
        rig.xform(SqGrp,t = (0,0,8.045),wd = True) 
        rig.setAttr(SqGrp+'.sx',1.387)
        rig.setAttr(SqGrp+'.sy',1.139)
        rig.setAttr(SqGrp+'.sz',0.859)
          
        Text = self.widge.text(self.eyeCloseData[6],True)
        rig.xform(Text,t = (0,0,9.14),wd = True)  
        rig.setAttr(Text+'.sx',0.186)
        rig.setAttr(Text+'.sy',0.186)
        rig.setAttr(Text+'.sz',0.186)
        
        grp = rig.group(LfSQGRP,RtSQGRP,SqGrp,Text,n = self.eyeCloseData[0]+'Eye_Close_GRP')
        rig.setAttr(grp+'.tz',-3.921)
        return grp
   
    def doubleCon(self,LfCon,RtCon,titles):
        LfconGrp,Lfcon = self.widge.fourSlide(LfCon)
        rig.setAttr(LfconGrp+'.tx',-1.5)
        RtconGrp,Rtcon = self.widge.fourSlide(RtCon)
        rig.setAttr(RtconGrp+'.tx',1.5)
        UpRtCon = rig.listRelatives(Rtcon,p = True)[0]
        rig.setAttr(UpRtCon+'.rz',180)
        
        Text = self.widge.text(titles,True)
        rig.setAttr(Text+'.sx',0.186)
        rig.setAttr(Text+'.sy',0.186)
        rig.setAttr(Text+'.sz',0.186)
        rig.setAttr(Text+'.tz',1.7)
        
        SqGrp,Sq = self.widge.square(titles,True)
        rig.setAttr(SqGrp+'.sx',1.387)
        rig.setAttr(SqGrp+'.sy',1.139)
        rig.setAttr(SqGrp+'.sz',0.859)
        rig.setAttr(SqGrp+'.tz',0.45)
        
        self.conAttrFour(Lfcon)
        self.conAttrFour(Rtcon)
        Grp = rig.group(LfconGrp,RtconGrp,Text,SqGrp,n = LfCon+'_Widge_CN_GRP')
        
        self.Lock.hideInvertAttr(Lfcon,('translateZ','translateX'))
        self.Lock.hideInvertAttr(Rtcon,('translateZ','translateX'))
        return Grp
          
    def doubleEye(self,up,dn,titles):
        upeye = self.widge.slideSinge(up)
        rig.xform(upeye[0],t = (0.7,0,-0.518),wd = True) 
        rig.setAttr(upeye[0]+'.ry',180)   
        dneye = self.widge.slideSinge(dn)
        rig.xform(dneye[0],t = (0.17,0,-0.707),wd = True)  
        
        SqGrp,Sq = self.widge.square(titles,True)
        rig.setAttr(SqGrp+'.sx',0.5)
        rig.setAttr(SqGrp+'.sy',0.5)
        rig.setAttr(SqGrp+'.sz',0.5) 
        
        self.conAttr(upeye[1]+'.tz')
        self.conAttr(dneye[1]+'.tz')
        eyeGrp = rig.group(upeye[0],dneye[0],SqGrp,n = titles+'_eyeGRP_Con',r = True)
        
        self.Lock.hideInvertAttr(upeye[1],('translateZ'))
        self.Lock.hideInvertAttr(dneye[1],('translateZ'))
        return eyeGrp
    
    def slideMouth(self,ConName):
        slidsArray = ['M_'+str(conArrow) for conArrow in range(20)]
        Z = 9.38
        textGrp = []
        sqGrp = []
        for i in range(len(slidsArray)):
            numChar = str(i)
            Text = self.widge.text(numChar,True)
            rig.xform(Text,t = (0,0,9.14),wd = True)  
            rig.setAttr(Text+'.sx',0.1)
            rig.setAttr(Text+'.sy',0.1)
            rig.setAttr(Text+'.sz',0.1)
            SqGrp,Sq = self.widge.square('SQ_'+numChar,True)
            rig.setAttr(SqGrp+'.sx',0.1)
            rig.setAttr(SqGrp+'.sy',0.1)
            rig.setAttr(SqGrp+'.sz',0.1) 
            
            rig.xform(Text,t = (5.45,0,Z),wd = True)
            rig.xform(SqGrp,t = (4.9,0,Z),wd = True)
            Z -= 0.5
            
            textGrp.append(Text)
            sqGrp.append(SqGrp)
            
        ConGrp,Con = self.widge.slideSinge(ConName)
        squareCon = Con.replace('_Switch_M','_Switch_RANGE_SQ')
        rig.transformLimits(Con,tz = (0,len(slidsArray)-1),etz = (1,1))
        rig.xform(squareCon,t = (0,0,3.997),wd = True)
        rig.setAttr(squareCon+'.sz',6.945)

        rig.xform(ConGrp,t = (4.905,0,8.55),wd = True)
        rig.setAttr(ConGrp+'.sx',1.375)        
        rig.setAttr(ConGrp+'.sy',1)
        rig.setAttr(ConGrp+'.sz',0.509)        
        rig.setAttr(ConGrp+'.ry',180)
        
        rig.hide(squareCon)
        TConGrp = self.addExtraExpress(slidsArray)
        SCNode = SK_createCompoundAttrs(TConGrp,len(slidsArray))
        SCJawNode = rig.createNode('choice',n = Con+'_SC',ss = True)
        rig.connectAttr(Con+'.tz',SCNode+'.selector')
        rig.connectAttr(Con+'.tz',SCJawNode+'.selector')
        rig.addAttr(ConGrp,at = 'float',ln = 'outJaw',k = True)
        for i,ArCon in enumerate(slidsArray):
            rig.addAttr(ConGrp,at = 'float',ln = ArCon,k = True)
#            rig.connectAttr(ConGrp+'.'+ArCon,SCNode+'.inData.bess'+str(i))  
            rig.connectAttr(TConGrp+'.outbess'+str(i),ArCon+'_M.tz') 
            rig.connectAttr(ConGrp+'.'+ArCon,SCJawNode+'.input['+str(i)+']')
        rig.connectAttr(SCJawNode+'.output',ConGrp+'.outJaw')
        
        midGrp = rig.group(textGrp,sqGrp,n = ConGrp+'_Text_slide_GRP')
        rig.hide(TConGrp)
        grp = rig.group(ConGrp,TConGrp,midGrp,n = ConGrp+'_Slide_GRP')
        
        self.Lock.hideInvertAttr(Con,('translateZ'))
        
        mouthShape = CreateControler()
        MSgrp = mouthShape.mouthControl('MouthShape')
        rig.parent(MSgrp,grp)

        return grp
    
        
    def addExtraExpress(self,AddCons = []):
        allWidge = []
        addZ = -1.392
        for miroCon in AddCons:
            ConGrp,Con = self.widge.slideSinge(miroCon, 'dn')
            rig.setAttr(ConGrp+'.ry',-90)
#            rig.move(pos[0],pos[1],pos[2],ConGrp+'.rotatePivot',ConGrp+'.scalePivot')
            rig.xform(ConGrp,t = (4.153,0,addZ),wd = True)
            pos = rig.xform(Con,q = True,piv = True,ws = True)[0:3]
            X = pos[0] - 4.5
            rig.move(0,0,X,ConGrp,os = True,r = True)
            addZ += 0.5
            
            self.conAttr(Con+'.tz')
            allWidge.append(ConGrp)
            self.Lock.hideInvertAttr(Con,('translateZ'))
            
        
        SqGrp,Sq = self.widge.square(AddCons[0]+'_Extra',True)
        rig.setAttr(SqGrp+'.sx',0.71)
        rig.setAttr(SqGrp+'.sy',1)
        rig.setAttr(SqGrp+'.sz',2.73)
        rig.xform(SqGrp,t = (4.486,0,4.22),wd = True)
        
        grp = rig.group(SqGrp,allWidge,n = AddCons[0]+'_All_Cons',r = True)
        return grp
    def mainControl(self):
        SqGrp,Sq = self.widge.square('Face')
        self.FaceCon = Sq
        rig.setAttr(SqGrp+'.sx',2.463)
        rig.setAttr(SqGrp+'.sy',2.4)
        rig.setAttr(SqGrp+'.sz',3.028) 
        rig.xform(SqGrp,t = (1.538,0,4.267),wd = True) 
        self.MainCon = SqGrp
        
        return SqGrp,Sq
    
    def conAttr(self,attributs):
        att = attributs.split('.')[0]
        rig.addAttr(self.MainCon,at = 'float',ln = att,k = True)
        rig.connectAttr(attributs,self.MainCon+'.'+att)

    def conAttrFour(self,con):
        attrs = rig.listAttr(con,ud = True)[1:5]
        for att in attrs:
            rig.addAttr(self.MainCon,at = 'float',ln = att,k = True)
            rig.connectAttr(con+'.'+att,self.MainCon+'.'+att)
               
    def merging(self):
#        self.widge = conWidge()
        mainConGrp,mainCon = self.mainControl()
        mouth = self.mouth()
        eyebrow = self.eyebrow()
        eye = self.eyeClose()
        extra = self.addExtraExpress(self.extraE)
        slideCon = self.slideMouth('Mouth_Switch')
        rig.parent(slideCon,mouth,eyebrow,eye,extra,mainCon)
        self.Lock.hideAndLockObj(mainConGrp)
        return mainConGrp    