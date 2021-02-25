#-*- coding: utf-8 -*-

import maya.cmds as rig
import RIG.WDface.WD_MainClass as CA
import maya.OpenMaya as om
import copy

class RigStart():
    def __init__(self):
        self.model = []
        self.scale = 1
        self.grp = 'Head_Control_GRP'
        self.CTRLBsCurves = []
        self.CTRLMacroCurves = []
        self.CVDict = {u'+translateX':'cv[1]', u'+translateY':'cv[6]', u'+translateZ':'cv[3]',u'-translateX':'cv[0]', u'-translateY':'cv[7]', u'-translateZ':'cv[4]'} 
        self.BSDict = {u'+translateX':'OUT', u'+translateY':'UP', u'+translateZ':'Front',u'-translateX':'IN', u'-translateY':'DN', u'-translateZ':'BACK'} 

        print 'joint'
        
    def getData(self):
        self.CTRLBsCurves = rig.listConnections(self.grp+'.CTRLBsCurve',s = False, d = True)
        self.CTRLMacroCurves = rig.listConnections(self.grp+'.CTRLMacroCurve',s = False, d = True)  
        self.CTRLJoints = rig.listConnections(self.grp+'.CTRLJoint',s = False, d = True)       
    
    def getScale(self):
        self.scale = CA.distance().getScale('Head_Tip_Joint', 'Head_Joint', 3.05659974721) 
    #------------------------------------------------------- 对macro控制器和bs控制器打组并清零
    def grpAndClear(self):
        CTRLBsCurves = copy.deepcopy(self.CTRLBsCurves)
        CTRLMacroCurves = copy.deepcopy(self.CTRLMacroCurves)    
        
        CTRLBsCurves.extend(CTRLMacroCurves)
        for con in CTRLBsCurves:
            parentObj = rig.listRelatives(con,p = True)[0]#得到它上面的组
            M = rig.getAttr(con+'.worldMatrix')
            PosGrp = rig.group(empty = True,n = con+'_Position_GRP')
            Grp = rig.group(PosGrp,n = con+'_GRP')
            rig.xform(Grp,m = M)
            rig.parent(con,PosGrp)
            rig.parent(Grp,parentObj)#将组放回到以前的位置
    
    #创建ramp节点并限制范围
    def rampAndLimit(self,con,attrs):
        stMit = setLimit(con)
        shapes = rig.listRelatives(con,s = True)#找到cross形节点
        if shapes and len(shapes) > 1:
            shape = shapes[1]
            for att in attrs:
                pos = rig.xform(shape+'.'+self.CVDict[att],q = True,t = True,wd = True)
                value = pos[0] + pos[1] + pos[2]
                stMit.done(att, value)#限定范围
                
                preWord = att[0]
                attrName = att.replace(preWord,'')#得到属性名
                RV = rig.createNode('remapValue', n = con+'_'+self.BSDict[att]+'_RV',ss = True)#创建remapValue节点
    
                rig.addAttr(RV,at = 'float', ln = 'limitValue', dv = value)
                
                rig.connectAttr(con+'.'+attrName,RV+'.inputValue')
                
        if not shapes:
            for att in attrs:
                bsCon = con.replace('_Rotation','')
                value = rig.getAttr(bsCon+'.'+self.TranslateToRotate[att])
                print att,value
                stMit.done(att, value)#限定范围
                
                stMit = setLimit(bsCon)
                print att[0]+'rotate'+att[-1],value
                stMit.done(att[0]+'rotate'+att[-1], value/57.295666666666662)#限定范围
                
                preWord = att[0]
                attrName = att.replace(preWord,'')#得到属性名
                RV = rig.createNode('remapValue', n = con+'_'+self.BSDict[att]+'_RV',ss = True)#创建remapValue节点
    
                rig.deleteAttr(bsCon, at = self.TranslateToRotate[att])
                rig.addAttr(RV,at = 'float', ln = 'limitValue', dv = value)
                rig.connectAttr(con+'.'+attrName,RV+'.inputValue')            
            
            
    #--------------------------------------------------------- 限制属性并创建remapValue节点
    def linkLimitAttr(self):
        attr4 = [u'+translateX', u'+translateY',u'-translateX', u'-translateY'] 
        attr6Cons = [u'Rt_Brow_M', u'Lf_Brow_M', u'Mouth_Tip_M',u'JawMain_M',u'Lf_Cheek_M', u'Rt_Cheek_M', u'Lf_CornerLip_M', u'Rt_CornerLip_M', u'Up_Lip_M', u'Dn_Lip_M']
        attr6 = [u'+translateX', u'+translateY', u'+translateZ',u'-translateX', u'-translateY', u'-translateZ'] 
        
        self.RotateToTranslate = {u'limitMaxrx':u'+translateX', u'limitMinx':u'-translateX', u'limitMaxry':u'+translateY', u'limitMinry':u'-translateY', u'limitMaxrz':u'+translateZ', u'limitMinrz':u'-translateZ',}
        self.TranslateToRotate = dict([(self.RotateToTranslate[attr], attr )for attr in self.RotateToTranslate])
        
        linkAttr = CA.connectAttribute()
        linkAttr.attrType = 'float'
        linkAttr.sourceAttr = 'CTRLBSRotate'
        linkAttr.targetAttr = 'CTRLBSRotate'
        
        subCon = [u'Nose_M']
        cons = [con for con in self.CTRLBsCurves if not(con in subCon)]
        for con in cons:
            rotateLimit = rig.listAttr(con,ud = True, k = True)
            if rotateLimit:
                
                attrs = []
                print con+'------------>'
                matCon = rig.getAttr(con+'.worldMatrix')
                conGrp = rig.group(empty = True, n = con+'_Rotation')
                linkAttr.connect(self.grp, [conGrp])#连接属性
                rig.xform(conGrp, m = matCon)
                rig.parent(conGrp, con)
                
                for rl in rotateLimit:#迭代旋转属性
                    attrs.append(self.RotateToTranslate[rl])
                    grpAttr = conGrp+'.t'+rl[-1]
                    if not rig.connectionInfo(grpAttr, isDestination=True):
                        rig.connectAttr(con+'.'+rl[-2::], grpAttr, f = True)
                        
                self.rampAndLimit(conGrp, attrs) 
                
                
                
            if con in attr6Cons:
                self.rampAndLimit(con, attr6)
            else:
                self.rampAndLimit(con, attr4)
        
        
    def mouthSetup(self):
        jaw = 'JawMain_M' #下巴控制器
        jawJoint = 'Jaw_Joint'     #下颚骨
        head = 'Head_Joint'  #头骨
        swivleJoint = 'Jaw_Swivle_Joint'#下巴整体骨头
        
        #对骨骼校正轴向
        oj = 'zyx'
        secondaryAxisOrient = 'yup'
        orientJoints = [jnt for jnt in self.CTRLJoints if not (jnt.replace('_Joint','_Macro_M') in self.CTRLMacroCurves)]#排除不需要校正轴向的骨骼
        for jnt in orientJoints:
            rig.joint(jnt,e = True, oj = oj, secondaryAxisOrient = secondaryAxisOrient, ch = False, zso = True)
        
        
        #增加jawJoint中间的两根骨头
        rig.select(cl = True)
        JawParent = rig.listRelatives(jawJoint,p = True)[0]#找到以前的parent物体
        JawMat = rig.getAttr(jawJoint+'.worldMatrix')
        JawTopJnt = rig.joint(n = jawJoint+'_Top')
        JawUpJnt = rig.joint(n = jawJoint+'_UP')
        rig.xform(JawTopJnt,m = JawMat)
        rig.parent(JawTopJnt,JawParent)
        rig.parent(jawJoint,JawUpJnt)
        
        #增加swivleJoint中间的两根骨头
        rig.select(cl = True)
        swivleParent = rig.listRelatives(swivleJoint,p = True)[0]#找到以前的parent物体
        swivleMat = rig.getAttr(swivleJoint+'.worldMatrix')
        swivleTopJnt = rig.joint(n = swivleJoint+'_Top')
        swivleUpJnt = rig.joint(n = swivleJoint+'_UP')
        rig.xform(swivleTopJnt,m = swivleMat)
        rig.parent(swivleTopJnt,swivleParent)    
        rig.parent(swivleJoint,swivleUpJnt)
                
        #连接下巴位移
        jawParent = rig.listRelatives(jaw,p = True)[0]
        JawTranslateMD = rig.createNode('multiplyDivide',n = jaw+'_Translate_MD')
        rig.addAttr(jawParent,at = 'float',ln = 'jaw_Tz',dv = 1,k = True)
        rig.connectAttr(jawParent+'.jaw_Tz',JawTranslateMD+'.input1X')
        rig.connectAttr(jaw+'.tz',JawTranslateMD+'.input2X')        
        rig.connectAttr(JawTranslateMD+'.outputX',jawJoint+'.tz')         
        
        
        #连接下巴旋转
        jawParent = rig.listRelatives(jaw,p = True)[0]
        JawRotateMD = rig.createNode('multiplyDivide',n = jaw+'_Rotate_MD')
        JawRotateSR = rig.createNode('setRange',n = jaw+'_Rotate_SR')
        JawRotatePMA = rig.createNode('plusMinusAverage',n = jaw+'_Rotate_PMA')
        
        TyDN,TyUP= rig.transformLimits(jaw, q = True, ty = True)#设置JawRotateSR的值
        rig.setAttr(JawRotateSR+'.minX', 0)
        rig.setAttr(JawRotateSR+'.minY', TyDN)
        rig.setAttr(JawRotateSR+'.maxX', TyUP)
        rig.setAttr(JawRotateSR+'.maxY', 0)
        rig.setAttr(JawRotateSR+'.oldMinX', 0)
        rig.setAttr(JawRotateSR+'.oldMinY', TyDN)
        rig.setAttr(JawRotateSR+'.oldMaxX', TyUP)
        rig.setAttr(JawRotateSR+'.oldMaxY', 0)
        
        
        rig.addAttr(jawParent,at = 'float', ln = 'jaw_Tx', dv = 35/self.scale, k = True)
        rig.addAttr(jawParent,at = 'float', ln = 'jaw_Ty', dv = -35/self.scale, k = True)
        rig.addAttr(jawParent,at = 'float', ln = 'jaw_TyUp', dv = 0.1*self.scale, k = True)
        
        rig.connectAttr(jawParent+'.jaw_Tx',JawRotateMD+'.input1X')
        rig.connectAttr(jawParent+'.jaw_Ty',JawRotateMD+'.input1Y')
        rig.connectAttr(jawParent+'.jaw_TyUp',JawRotateSR+'.maxX')        
        
        rig.connectAttr(jaw+'.ty', JawRotateSR+'.valueX')
        rig.connectAttr(jaw+'.ty', JawRotateSR+'.valueY')
        rig.connectAttr(JawRotateSR+'.outValueX', JawRotatePMA+'.input1D[0]')
        rig.connectAttr(JawRotateSR+'.outValueY', JawRotatePMA+'.input1D[1]')
        rig.connectAttr(JawRotatePMA+'.output1D', JawRotateMD+'.input2Y') 
        
        rig.connectAttr(jaw+'.tx',JawRotateMD+'.input2X')            
#        rig.connectAttr(jaw+'.ty',JawRotateMD+'.input2Y')  
              
        rig.connectAttr(JawRotateMD+'.outputX',jawJoint+'.ry')  
        rig.connectAttr(JawRotateMD+'.outputY',jawJoint+'.rx')                       
        rig.connectAttr(jaw+'.rz',jawJoint+'.rz')                       
    
    #增加嘴角设置
    def mouthCorner(self):
        jaw = 'JawMain_M' #下巴控制器
        jawParent = rig.listRelatives(jaw, p = True)[0]
        jawJoint = 'Jaw_Joint'     #下颚骨
        joints = [u'Lf_CornerLip_Joint', u'Rt_CornerLip_Joint', u'Mouth_Tip_Joint', u'Dn_Lip_Joint', u'JawMain_Joint']  
        attrs = ['rotateX','rotateY','rotateZ']
        
        jawMat = rig.getAttr(jawJoint+'.worldMatrix')
        for jnt in joints:
            rig.select(cl = True)
            jntTop = rig.joint(n = jnt+'_Top')
            jntUp = rig.joint(n = jnt+'_Up')
            rig.xform(jntTop,m = jawMat)

            
            rig.parent(jntTop,jawJoint)
            rig.parent(jnt, jntUp)
            
            MD = rig.createNode('multiplyDivide', ss = True, n = jnt+'_Rotate_MD')
            rig.connectAttr(jawJoint+'.rotate',MD+'.input1')
            rig.connectAttr(MD+'.output',jntUp+'.rotate')
            for attr in attrs:
                currentAttr = jnt+attr
                rig.addAttr(jawParent,at = 'float', ln = currentAttr, k = True ,dv = 1)
                rig.connectAttr(jawParent+'.'+currentAttr, MD+'.input2'+attr[-1])    
                
        #设置嘴角初始值    
        rig.setAttr(jawParent+'.Lf_CornerLip_JointrotateX', 0)
        rig.setAttr(jawParent+'.Rt_CornerLip_JointrotateX', 0)
        rig.setAttr(jawParent+'.Mouth_Tip_JointrotateX', 0)
                
    #连接骨骼位移
    def linkJointTransform(self):
        #在每根骨骼上加两个组，并用控制器的位移连接到此骨骼上.
        jnts = [jnt.replace('Macro_M','_Joint') for jnt in self.CTRLMacroCurves]#通过控制器得到骨骼
        for jnt in jnts:
            Macro = jnt.replace('_Joint','Macro_M')
            parentObj = rig.listRelatives(jnt,p = True)[0]#得到它上面的组
            M = rig.getAttr(jnt+'.worldMatrix')
            PosGrp = rig.group(jnt,n = jnt+'_Position_GRP')
            rig.setAttr(jnt+'.tx',0)
            rig.setAttr(jnt+'.ty',0)
            rig.setAttr(jnt+'.tz',0)
            rig.setAttr(jnt+'.rx',0)
            rig.setAttr(jnt+'.ry',0)
            rig.setAttr(jnt+'.rz',0)
            rig.setAttr(jnt+'.sx',1)
            rig.setAttr(jnt+'.sy',1)
            rig.setAttr(jnt+'.sz',1)
            
            Grp = rig.group(PosGrp,n = jnt+'_GRP')
            rig.parent(Grp,w = True)
            rig.xform(Grp,m = M)
            rig.parent(Grp,parentObj)#将组放回到以前的位置

            rig.connectAttr(Macro+'.translate',jnt+'.translate')#连接位移
            
    #连接隐藏控制器
    def linkVis(self):
        connectVisibility = CA.connectAttribute()
        connectVisibility.sourceAttr = 'mainVis'
        connectVisibility.connect(self.grp,[rig.listRelatives(grp, p = True)[0] for grp in self.CTRLBsCurves])
        connectVisibility.sourceAttr = 'macroVis'
        connectVisibility.connect(self.grp,[rig.listRelatives(grp, p = True)[0] for grp in self.CTRLMacroCurves])

    #创建Set
    def skinSet(self):
        InfSets = CA.addSets()
        InfSets.componentSets = 'Face_Main_Sets'
        infs = [u'JawMain_Joint_Up', u'Nose_Joint', u'Head_Joint']
        InfSets.startAdd(infs)
    
    #增加rigging属性
    def addRiggingAttr(self):
        rig.addAttr(self.grp, at = 'long', ln = 'rigging', dv = 1)
        
                    
    def done(self):
        self.getData()
        self.getScale()
        self.addRiggingAttr()
        self.grpAndClear()
        self.linkLimitAttr()
        self.mouthSetup()
        self.mouthCorner()
        self.linkJointTransform()
        self.linkVis()
        self.skinSet()
    
    
class setLimit():
    def __init__(self,obj):
        self.obj = obj
        self.k = ['kScaleMinX', 'kScaleMaxX', 'kScaleMinY', 'kScaleMaxY', 'kScaleMinZ', 'kScaleMaxZ', 'kShearMinXY', 'kShearMaxXY', 'kShearMinXZ', 'kShearMaxXZ', 'kShearMinYZ', 'kShearMaxYZ', 'kRotateMinX', 'kRotateMaxX', 'kRotateMinY', 'kRotateMaxY', 'kRotateMinZ', 'kRotateMaxZ', 'kTranslateMinX', 'kTranslateMaxX', 'kTranslateMinY', 'kTranslateMaxY', 'kTranslateMinZ', 'kTranslateMaxZ']
        self.attr = ['-scaleX', '+scaleX', '-scaleY', '+scaleY', '-scaleZ', '+scaleZ', '-shearXY', '+shearXY', '-shearXZ', '+shearXZ', '-shearYZ', '+shearYZ', '-rotateX', '+rotateX', '-rotateY', '+rotateY', '-rotateZ', '+rotateZ', '-translateX', '+translateX', '-translateY', '+translateY', '-translateZ', '+translateZ']
        
    def done(self,attr,value):
        MSobj = om.MSelectionList()
        MSobj.add(self.obj)
        
        path = om.MDagPath()
        MSobj.getDagPath(0,path)
        
        objTran = om.MFnTransform(path)
        objTran.enableLimit(self.attr.index(attr),True)
        objTran.setLimit(self.attr.index(attr),value)
    