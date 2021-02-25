#-*- coding: utf-8 -*-
import maya.cmds as rig
from RIG.face.controlers import CreateControler
from RIG.face.baseClass import LockHideAttr
from RIG.face.controlUI import faceCoustom

class FC_ControlPosition(object):
    def __init__(self,eyeSign,tongueSign,faceSign,eyebrowSign,toothSign,face,signRun = True):
        self.eyeSn = eyeSign
        self.tongueSign = tongueSign
        self.faceSn = faceSign
        self.eyebrowSn = eyebrowSign
        self.toothSn = toothSign
        self.faceUI = face
        self.controller = CreateControler(13,[0.02,0.02,0.02])
        self.controller.signValue = 78
        self.positionInfo = {u'Lf_upLip_1_P': [[0.4577522202940788, -0.88940796081633167, 1.417898534744211], 22], u'Rt_upLip_1_P': [[-0.45775222778320313, -0.8894079327583313, 1.4178985357284546], 22], u'Lf_eyebrow_1_P': [[1.4552631170435382, 1.0109427040846835, 0.71208507180728153], 6], u'Lf_ear_P': [[1.6969779911728109, 0.30225545212855426, -0.83550711061509519], 22], u'Lf_eyebrow_3_P': [[0.83952074318038761, 1.2762483953898438, 1.3866029424173725], 6], u'Rt_upLip_2_P': [[-0.24067594110965729, -0.82347398996353149, 1.5329214334487915], 22], u'Rt_nose_P': [[-0.28455081582069397, -0.29319655895233154, 1.5947476625442505], 13], u'Lf_mouth_P': [[0.59368043681559712, -0.94644514607242525, 1.1507955018474469], 13], u'Rt_dnLip_1_P': [[-0.40149763226509094, -1.0502012968063354, 1.3711462020874023], 12], u'Rt_eyebrow_1_P': [[-1.4552631378173828, 1.0109426975250244, 0.7120850682258606], 6], u'Lf_dnLip_2_P': [[0.21610563619760767, -1.0877709665250357, 1.5105537251473589], 12], u'Lf_eyebrow_4_P': [[0.36489604932817388, 1.1127071207027288, 1.5045110865908411], 6], u'Rt_dnEyelid_3_P': [[-0.97799999999999998, 0.60090496740722077, 1.0512626650116561], 10], u'Lf_dnEyelid_2_P': [[0.80561238526187084, 0.56115445658376806, 1.1145096040896882], 10], u'Lf_dnEyelid_3_P': [[0.97829695568744968, 0.60090496740722077, 1.0512626650116561], 10], u'Lf_pull_P': [[1.1940568236640083, -0.74121844106321233, 0.60184938648410746], 6], u'Lf_dnLip_1_P': [[0.40149764130798138, -1.0502013047415499, 1.3711461657738258], 12], u'Rt_eyebrow_4_P': [[-0.36489605903625488, 1.1127071380615234, 1.5045111179351807], 6], u'Rt_eyebrow_3_P': [[-0.83952075242996216, 1.2762483358383179, 1.3866029977798462], 6], u'Mid_dnLip_P': [[0.0, -1.0725690595054045, 1.5188097774357625], 12], u'Rt_canthusOut_P': [[-1.1433006525039673, 0.70208227634429932, 0.92102342844009399], 13], u'Mid_base_P': [[0.0, 0.0, 0.0], 16],u'Rt_upEyelid_3_P': [[-0.98499999999999999, 0.81146603544601237, 1.0737908090959429], 22], u'Lf_eyebrow_2_P': [[1.2554887462609086, 1.2242805206272087, 1.0934283695974849], 6], u'Lf_canthusIn_P': [[0.43909954407376683, 0.6311377754074402, 1.0586760528711641], 13], u'Rt_ear_P': [[-1.696977972984314, 0.30225545167922974, -0.8355070948600769], 22], u'Rt_upEyelid_2_P': [[-0.76296061277389526, 0.84621930122375488, 1.1415883302688599], 22], u'Lf_cheekbone_P': [[1.2649382178275159, -0.13004048109449998, 0.95846824899201755], 22], u'Rt_dnLip_2_P': [[-0.21610563993453979, -1.087770938873291, 1.5105537176132202], 12], u'Lf_canthusOut_P': [[1.1433007061180056, 0.70208226194515522, 0.92102340618126766], 13], u'Rt_cheekbone_P': [[-1.2649382352828979, -0.1300404816865921, 0.95846825838088989], 22], u'Rt_upEyelid_1_P': [[-0.58767658472061157, 0.79538941383361816, 1.1090470552444458], 22], u'Lf_nose_P': [[0.28455081409851524, -0.2931965624518485, 1.594747668867244], 13], u'Lf_upLip_2_P': [[0.24067594423116645, -0.82347398074313027, 1.5329214512325766], 22], u'Rt_eyebrow_2_P': [[-1.2554887533187866, 1.2242804765701294, 1.093428373336792], 6], u'Lf_dnEyelid_1_P': [[0.59532230907410022, 0.58211628344290467, 1.0920294918149343], 10], u'Lf_upEyelid_1_P': [[0.58767656543479574, 0.79538939863679392, 1.1090470759223556], 22], u'Rt_canthusIn_P': [[-0.43909955024719238, 0.63113778829574585, 1.05867600440979], 13], u'Rt_dnEyelid_2_P': [[-0.80561238527297974, 0.56115448474884033, 1.1145095825195312], 10], u'Rt_dnEyelid_1_P': [[-0.59532231092453003, 0.58211630582809448, 1.0920294523239136], 10], u'Mid_upLip_P': [[0.0, -0.79989685162339896, 1.5986444439336869], 22], u'Rt_pull_P': [[-1.1940568685531616, -0.7412184476852417, 0.60184937715530396], 6], u'Lf_upEyelid_3_P': [[0.98455660606281059, 0.81146603544601237, 1.0737908090959429], 22], u'Mid_nose_P': [[0.0, -0.1841173100719343, 1.8619454284092736], 22], u'Lf_upEyelid_2_P': [[0.76296061594693798, 0.84621928539927671, 1.1415883252920129], 22], u'Rt_mouth_P': [[-0.59368044137954712, -0.94644516706466675, 1.1507954597473145], 13]}
        self.eyebrowPosInfo = {u'Lf_ebw_2_P': [[1.2539269262641821, 1.446814944148378, 1.0537070623711431], 13], u'Lf_ebw_1_P': [[1.4084910234031645, 1.3076079841558128, 0.80211524813419777], 13], u'Rt_ebw_4_P': [[-0.64794783800161104, 1.4254101271982282, 1.4431839608606198], 13], u'Lf_ebw_3_P': [[1.0037106276394581, 1.4898388225433679, 1.2718257991365869], 13], u'Lf_ebw_4_P': [[0.64794783800161104, 1.4254101271982282, 1.4431839608606198], 13], u'Rt_ebw_2_P': [[-1.2539269262641821, 1.446814944148378, 1.0537070623711431], 13], u'Rt_ebw_1_P': [[-1.4084910234031645, 1.3076079841558128, 0.80211524813419777], 13], u'Rt_ebw_3_P': [[-1.0037106276394581, 1.4898388225433679, 1.2718257991365869], 13]}
        if signRun:
            self.combine()
        
    def getPosition(self,controllers = []):
        positionDictData = dict([(obj,[rig.xform(obj,q = True,t = True,ws = True),rig.getAttr((rig.listRelatives(obj,s = True)[0])+'.overrideColor')])for obj in controllers ])
        return positionDictData
    
    def creatController(self,dictData):
        for eachControl in dictData:
            controlValue = dictData[eachControl]
            self.controller.setColor(int(controlValue[1]))
            controlName = self.controller.SK_b03(eachControl)
            rig.xform(controlName,t = controlValue[0],ws = True)
            
    def lockHideConnectCon(self,dictData):
        locks = LockHideAttr(1,0,0,0)
        for eachControl in dictData:
#  连接位移值
            if('Lf' == eachControl.split('_')[0]):
                RtConName = eachControl.replace('Lf','Rt')
                if(rig.objExists(RtConName)):
                    conNode = rig.createNode('multiplyDivide',n = eachControl+'_MD',ss = True)
                    rig.setAttr(conNode+'.input2X',-1)
                    rig.connectAttr(eachControl+'.translate',conNode+'.input1')
                    rig.connectAttr(conNode+'.output',RtConName+'.translate')
#   锁定translatex                             
            if ('Mid' == eachControl.split('_')[0]):
                rig.setAttr(eachControl+'.tx',cb = False,k = False,l = True)
#   锁定隐藏属性            
            locks.hideAndLockObj(eachControl)
            
    def createFaceCon(self):
        controller = CreateControler(13)
        controlName = controller.SK_b08('Face_Con')
        rig.addAttr('Face_ConShape',dt = 'string',ln = 'headFOL')
        rig.addAttr('Face_ConShape',dt = 'string',ln = 'headSKIN')
        rig.addAttr('Face_ConShape',dt = 'string',ln = 'eyeLeft')
        rig.addAttr('Face_ConShape',dt = 'string',ln = 'eyeRight')
        rig.addAttr('Face_ConShape',dt = 'string',ln = 'upTooth')
        rig.addAttr('Face_ConShape',dt = 'string',ln = 'dnTooth')
        rig.addAttr('Face_ConShape',dt = 'string',ln = 'eyebrowLeft')
        rig.addAttr('Face_ConShape',dt = 'string',ln = 'eyebrowRight')
        rig.addAttr('Face_ConShape',dt = 'string',ln = 'tongue')
        rig.addAttr( controlName, ln='scaleValue',at = 'double')
        rig.setAttr(controlName+'.rx',90)
        rig.makeIdentity(controlName,apply = True,t = True,r = True,s = True)
        return controlName
    
    
    def creatJawjoint(self):
        jntNames = [u'JawTip_JNT_P', u'Jaw_JNT_P', u'HeadRoot_JNT_P']
        jntPos = [[-1.9721522630525295e-031, -1.6991611811361911, 1.2772460195315276], [-1.9721522630525295e-031, -0.24193316678545695, -0.71455524677275717], [0.0, -3.877232277010112, -1.9775230127662995]] 
        for i,jnt in enumerate(jntNames):
            rig.select(cl = True)
            curJNT = rig.joint(n = jnt)
            rig.xform(curJNT,t = jntPos[i],ws = True)
        rig.parent('JawTip_JNT_P','Jaw_JNT_P')
        rig.parent('Jaw_JNT_P','HeadRoot_JNT_P')
        rig.parent('HeadRoot_JNT_P',self.FaceCon)
        
        self.controller.setColor(17)
        self.controller.signValue = 73
        jawCon = self.controller.SK_b03('Jaw_M') 
        rig.xform(jawCon,matrix = [11.093766471162281, 0.0, 0.0, 0.0, 0.0, 11.093766471162281, 0.0, 0.0, 0.0, 0.0, 11.093766471162281, 0.0, 0.0, -1.9479364224911047, 1.5001411259496222, 1.0])           
        rig.parent(jawCon,self.FaceCon)    
        rig.makeIdentity(jawCon,apply = True,s = True,r = True,t = True)
        
    def addEyebrow(self,sign):
        if sign:
            self.controller.signValue = 71
            self.creatController(self.eyebrowPosInfo)
            self.lockHideConnectCon(self.eyebrowPosInfo)        
            rig.parent(self.eyebrowPosInfo.keys(),self.grpName)

        
    def addMainController(self):
        self.creatController(self.positionInfo)
        self.lockHideConnectCon(self.positionInfo)
        rig.parent(self.positionInfo.keys(),self.grpName)
        
    def addEye(self,sign):
        if sign:
            LfJnt = rig.joint(n = 'Lf_EYE_JNT_P')
            rig.xform(LfJnt,t = [0.76887053415707951, 0.76097599414167427, 0.62705611174469811],ws = True)
            RtJnt = rig.joint(n = 'Rt_EYE_JNT_P')
            rig.xform(RtJnt,t = [-0.76887053415707951, 0.76097599414167427, 0.62705611174469811],ws = True)
            rig.parent(LfJnt,RtJnt,self.FaceCon)
            
            
            self.controller.setObjScale((1,1,1))
            self.controller.setColor(6)
            self.controller.signValue = 73
            eyeAllCon = self.controller.SK_b08('eye_M')
            rig.xform(eyeAllCon,matrix = [0.98195796671303204, 0.0, 0.0, 0.0, 0.0, 2.1803846877178224e-016, 0.98195796671303204, 0.0, 0.0, -0.4017168114352116, 8.9199050686874858e-017, 0.0, 0.0, 0.74691933784829889, 5.0041701361715383, 1.0])
            LfEyeCon = self.controller.SK_b08('Lf_eye_M')
            rig.xform(LfEyeCon,matrix = [0.27600951299477411, 0.0, 0.0, 0.0, 0.0, 6.1286423268474912e-017, 0.27600951299477416, 0.0, 0.0, -0.27600951299477416, 6.1286423268474912e-017, 0.0, 0.76756054849076027, 0.74691933784829911, 5.0041701361715401, 1.0])
            RtEyeCon = self.controller.SK_b08('Rt_eye_M')
            rig.xform(RtEyeCon,matrix = [-0.27600951299477411, 0.0, 0.0, 0.0, 0.0, 6.1286423268474912e-017, 0.27600951299477416, 0.0, 0.0, -0.27600951299477416, 6.1286423268474912e-017, 0.0, -0.76756054849076027, 0.74691933784829911, 5.0041701361715401, 1.0])
            rig.parent(LfEyeCon,RtEyeCon,eyeAllCon)
            rig.parent(eyeAllCon,self.grpName)
            rig.makeIdentity(eyeAllCon,apply = True,s = True,r = True,t = True)
            
    def addTongue(self,sign):
        if sign:
            jnts = [u'Tongue_1_JNT_P', u'Tongue_2_JNT_P', u'Tongue_3_JNT_P', u'Tongue_4_JNT_P', u'Tongue_5_JNT_P'] 
            jntPos = [[-2.4074124304840448e-034, -1.1828907427397966, 0.39945317842483419], [-1.9352787993130288e-019, -1.0414296961573679, 0.547367817822622], [-1.9352787993136451e-019, -0.98892292574879703, 0.74994385199198321], [-1.9352787993136451e-019, -1.0101921438931105, 0.98285235913741198], [-1.9352787993130904e-019, -1.1000491650967648, 1.1555898993095108]]
            rig.select(cl = True)
            for i,jnt in enumerate(jnts):
                curJnt = rig.joint(n = jnt)
                rig.xform(curJnt,t = jntPos[i],ws = True)
            rig.select(cl = True)
            rig.parent('Tongue_1_JNT_P',self.FaceCon)
            
            self.controller.setColor(13)
            self.controller.signValue = 73
            tongueCon = self.controller.SK_b03('Tongue_M') 
            rig.xform(tongueCon,matrix = [0.06444328794870588, 0.0, 0.0, 0.0, 0.0, 0.06444328794870588, 0.0, 0.0, 0.0, 0.0, 0.06444328794870588, 0.0, 0.0, -1.3071946345318575, 1.650696183174968, 1.0] )           
            rig.parent(tongueCon,self.FaceCon)    
            rig.makeIdentity(tongueCon,apply = True,s = True,r = True,t = True)
    def addTooth(self,sign):
        if sign:
            rig.select(cl = True)
            UpTooth = rig.joint(n = 'UpTooth_JNT_P')
            rig.xform(UpTooth,t = [0.0, -0.67428806973770494, 0.83475947289697605],ws = True)
            rig.select(cl = True)
            DnTooth = rig.joint(n = 'DnTooth_JNT_P')
            rig.xform(DnTooth,t = [0.0, -1.1574310052199537, 0.74481897781780426],ws = True)
            rig.parent(UpTooth,DnTooth,self.FaceCon)
                            
    def addFaceUI(self,sign):
        if sign:
            faceCon = faceCoustom()
            signStr = rig.textField(self.faceUI.bsFaceTF,q = True,tx = True)
            if signStr:
                strShape = signStr.split(' ')
                faceCon.extraE = strShape
            faceGrp = faceCon.merging()
            con = rig.group(faceGrp,n = 'Face_ALL_M_CON_GRP')
            rig.xform(con,ro = (-90,-180,0),wd = True)
            rig.xform(con,t = (-1.538,0,-4.267),wd = True)            
            
            
            
    def combine(self):
        self.FaceCon = self.createFaceCon()
        self.grpName = rig.group(n = 'face_Postion',empty = True)
        
        self.addMainController()
        self.addEyebrow(self.eyebrowSn)
        rig.parent(self.grpName,self.FaceCon)
        self.creatJawjoint()
        self.addEye(self.eyeSn)
        self.addTongue(self.tongueSign)
        self.addTooth(self.toothSn)
        self.addFaceUI(self.faceSn)
    
    
    
    
    
    
    
    