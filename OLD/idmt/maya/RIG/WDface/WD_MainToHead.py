#-*- coding: utf-8 -*-

import maya.cmds as rig
import RIG.WDface.WD_MainClass as CA
import RIG.WDface.WD_SkinBlendShape as SBS
import copy
import re

#===============================================================================
# 将main和head两部分进行关联设置
#===============================================================================
class mainToHead():
    def __init__(self):
        self.main = 'Main_Control_GRP'
        self.head = 'Head_Control_GRP'

        self.tempCurve = []#临时曲线
        self.tempJoint = []#临时骨骼
        
    
        self.deformerGrp = CA.getRigGrp()
        self.deformerGrp.grp = 'Head_FaceDeformers_GRP'
    #------------------------------------------------------------------- 获得需要的数据
    def getData(self):
        ControllerDict = dict([(rig.getAttr(con+'.vtxNum'),con) for con in rig.listConnections(self.main+'.CTRLCurve', s = False, d = True) if  not re.match('\w+_Back_\d+M',con)])#创建控制器字典
        nums = [i for i in ControllerDict.keys()]#获得编号
        nums.sort()#对编号进行排序
        
        self.curveToController = dict([(ControllerDict[num],i) for i,num in enumerate(nums)])#建立base曲线点与控制器的字典
        self.numToController = dict([(rig.listConnections(ControllerDict[con], s = False, d = True, p = True)[0],ControllerDict[con]) for con in ControllerDict])#建立base曲线点与控制器的字典
        
        self.baseCurve = rig.listConnections(self.main+'.CTRLBaseCurve', s = False, d = True)[0]
        self.origentCurve = rig.listConnections(self.main+'.CTRLOrigenCurve', s = False, d = True)[0]
        
    #---------------------------------------------------------------------- 计算权重
    def computeWeights(self,sSkin,tSkin,listInfs):
        sInfs = rig.skinCluster(sSkin,q = True,inf = True)
        tInfs = rig.skinCluster(tSkin,q = True,inf = True)
        sShape = rig.skinCluster(sSkin,q = True,g = True)[0]
        tShape = rig.skinCluster(tSkin,q = True,g = True)[0]
        
        allVtxs = rig.ls(sShape+'.cv[*]',fl = True)
        tvtxInfo = []
        for vtx in allVtxs:
            sWeights = rig.skinPercent(sSkin,vtx,q = True,v = True)
            sWeightsDict = dict([(sInfs[i],value) for i,value in enumerate(sWeights)])
            tWeights = []#存放目标物体权重
            for inf in tInfs:#开始计算权重
                weight = 0.0
                sInf =  listInfs[inf]
                if 'list' == type(sInf).__name__:
                    for tInf in sInf:
                        weight += sWeightsDict[tInf]
                else:
                    weight = sWeightsDict[sInf]
                
                tWeights.append(weight)
            
            weithsInfo = zip(tInfs,tWeights)
            tvtxInfo.append(weithsInfo)
            
        for i,vtx in enumerate(allVtxs):#设置权重
            rig.skinPercent(tSkin,tShape+'.'+vtx.split('.')[-1],tv = tvtxInfo[i])
               
        
    #--------------------------------------------------------------------- 对曲线蒙皮
    def skinCurve(self):
        jointCurve = {
                      'out_LfNasolabialCurve':[u'Lf_Cheek_Joint', u'JawMain_Joint', u'Head_Joint'],
                      'out_eyebrowCurve':[u'Lf_Brow_Joint', u'Rt_Brow_Joint', u'Head_Joint'],
                      'out_RtNasolabialCurve':[u'Rt_Cheek_Joint', u'JawMain_Joint', u'Head_Joint'],
                      'out_UpMouthCurve':[u'Rt_CornerLip_Joint', u'Up_Lip_Joint', u'Lf_CornerLip_Joint'],
                      'out_DnMouthCurve':[u'Dn_Lip_Joint', u'Rt_CornerLip_Joint', u'Lf_CornerLip_Joint']
                      }
        
        
        #----------------------------------------------- 创建新的的曲线和骨骼并蒙皮，用于生成临时的权重
        for cur in jointCurve:
            tempCurveOrigen = rig.duplicate(cur,n = cur+'_Skin')[0]#复制InputCurve曲线
            self.tempCurve.append(tempCurveOrigen)#增加到临时组
            
            SkinOrigen = rig.skinCluster(tempCurveOrigen,jointCurve[cur],tsb = True)[0]#蒙皮
            
            if cur == 'out_LfNasolabialCurve':
                joints = []
                tempCurve = rig.duplicate(cur,n = cur+'_Skin_CA')[0]#复制InputCurve曲线
                self.tempCurve.append(tempCurve)#增加到临时组
                tempCurveShape = rig.listRelatives(tempCurve,s = True)[0]#形节点
                TempCA = CA.curveAverage()
                curvePos = TempCA.getInfo(tempCurveShape,3)[1]
                for i,pos in enumerate(curvePos):#生成临时骨骼
                    rig.select(cl = True)
                    jnt = rig.joint(p = pos,n = cur+'_'+str(i)+'Joint')
                    joints.append(jnt)
                    self.tempJoint.append(jnt)#增加到临时组
                Skin = rig.skinCluster(tempCurve,joints,tsb = True)[0]#蒙皮      
                listInfs = {'Lf_Cheek_Joint':'out_LfNasolabialCurve_1Joint',
                            'JawMain_Joint':'out_LfNasolabialCurve_2Joint',
                            'Head_Joint':'out_LfNasolabialCurve_0Joint'
                            }
                self.computeWeights(Skin, SkinOrigen, listInfs)        
                  
            if cur == 'out_eyebrowCurve':
                joints = []
                tempCurve = rig.duplicate(cur,n = cur+'_Skin_CA')[0]#复制InputCurve曲线
                self.tempCurve.append(tempCurveOrigen)#增加到临时组
                tempCurveShape = rig.listRelatives(tempCurve,s = True)[0]#形节点
                TempCA = CA.curveAverage()
                curvePos = TempCA.getInfo(tempCurveShape,9)[1]
                for i,pos in enumerate(curvePos):#生成临时骨骼
                    rig.select(cl = True)
                    jnt = rig.joint(p = pos,n = cur+'_'+str(i)+'Joint')
                    joints.append(jnt)
                    self.tempJoint.append(jnt)#增加到临时组
                Skin = rig.skinCluster(tempCurve,joints,tsb = True)[0]#蒙皮        
                listInfs = {'Lf_Brow_Joint':'out_eyebrowCurve_3Joint',
                            'Rt_Brow_Joint':'out_eyebrowCurve_5Joint',
                            'Head_Joint':[u'out_eyebrowCurve_2Joint', u'out_eyebrowCurve_1Joint', u'out_eyebrowCurve_0Joint', u'out_eyebrowCurve_8Joint', u'out_eyebrowCurve_7Joint', u'out_eyebrowCurve_6Joint', u'out_eyebrowCurve_4Joint']
                            }
                self.computeWeights(Skin, SkinOrigen, listInfs) 
            
            if cur == 'out_RtNasolabialCurve':
                joints = []
                tempCurve = rig.duplicate(cur,n = cur+'_Skin_CA')[0]#复制InputCurve曲线
                self.tempCurve.append(tempCurveOrigen)#增加到临时组
                tempCurveShape = rig.listRelatives(tempCurve,s = True)[0]#形节点
                TempCA = CA.curveAverage()
                curvePos = TempCA.getInfo(tempCurveShape,3)[1]
                for i,pos in enumerate(curvePos):#生成临时骨骼
                    rig.select(cl = True)
                    jnt = rig.joint(p = pos,n = cur+'_'+str(i)+'Joint')
                    joints.append(jnt)
                    self.tempJoint.append(jnt)#增加到临时组
                Skin = rig.skinCluster(tempCurve,joints,tsb = True)[0]#蒙皮        
                listInfs = {'Rt_Cheek_Joint':'out_RtNasolabialCurve_1Joint',
                            'JawMain_Joint':'out_RtNasolabialCurve_2Joint',
                            'Head_Joint':'out_RtNasolabialCurve_0Joint'
                            }
                self.computeWeights(Skin, SkinOrigen, listInfs) 
                
            if cur == 'out_UpMouthCurve':
                pass
            if cur == 'out_DnMouthCurve':
                pass            
        
        #------------------------------------------------------------- 对base曲线蒙皮
        allInfsJoint = []
        for cur in jointCurve:
            curShape = rig.listRelatives(cur+'_Skin',s = True)[0]#获得形节点
            SkinClus = CA.getDeformerNode()
            skin = SkinClus.getInfo(curShape)#获得skincluster
            infs = rig.skinCluster(skin,q = True,inf = True)
            allInfsJoint.extend(infs)
        infsSet = set(allInfsJoint)
        baseSkin = rig.skinCluster([inf for inf in infsSet],self.baseCurve,tsb = True)[0]
        
        

        #--------------------------------------------------------- 将权重拷贝到base曲线上
        for cur in jointCurve:
            curShape = rig.listRelatives(cur+'_Skin',s = True)[0]#获得形节点
            SkinClus = CA.getDeformerNode()
            skin = SkinClus.getInfo(curShape)#获得skincluster
            
            vtxs = rig.ls(curShape+'.cv[*]',fl = True)
            infs = rig.skinCluster(skin,q = True,inf = True)
            for vtx in vtxs:
                Weights = rig.skinPercent(skin,vtx,q = True,v = True)
                tvInfo = zip(infs,Weights)#权重数据
                cv = vtx.replace('_Skin.cv','Shape.controlPoints')#切分成CV点
                con = self.numToController[cv]#找到对应控制器
                baseVtx = self.curveToController[con]#找到点的
                rig.skinPercent(baseSkin,self.baseCurve+'.cv['+str(baseVtx)+']',tv = tvInfo)#设置base曲线权重
    
    #-------------------------------------------------------------- 创建自动生成blendShape
    def setBlendShape(self):
        CreateBS = createBlendShape()
        CreateBS.done()
    
    #--------------------------------------------------------------- 对back曲线进行蒙皮
    def skinClusterBack(self):
        #断开组对nurbsCurve点的连接
#        allBackConGrps = [con+'_GRP' for con in rig.listConnections(self.main+'.CTRLCurve', s = False, d = True) if re.match('\w+_Back_\d+M\Z',con)]
#        for grp in allBackConGrps:
#            plus = rig.listConnections(grp+'.translate', s = False, d = True, p = True)
#            if plus:
#                print plus
#                rig.disconnectAttr(grp+'.translate', plus[0])
        
        skinCurves = [cur for cur in rig.listConnections(self.main+'.LoftCurve', s = False, d = True) if  re.match('\Ain_',cur)]#获得蒙皮曲线

        for cur in skinCurves:
            rig.skinCluster(cur,'Head_Joint',n = cur+'_skinClusterNode', tsb = True)
            
    #--------------------------------------------------------- 清除为了分配权重时新建的骨骼和曲线
    def clearNode(self):
        rig.delete(self.tempCurve,self.tempJoint)
    
    
    def connectTranslateToMacro(self):
        rigGrp = CA.getRigGrp().createGrp()#创建rig组
        #--------------------------------------------------- 连接main控制器到macro控制器上
        mainCons = [u'Nose_M']
        for con in mainCons:
            macroCon = re.compile('_M\Z').sub('Macro_M',con)
            macroConShape = rig.listRelatives(macroCon,s = True)[0]
            rig.hide(macroConShape)#隐藏形节点
            rig.connectAttr(con+'.translate', macroCon+'.translate')#连接translate
            noseJnt = re.compile('_M\Z').sub('_Joint',con)
            rig.connectAttr(con+'.rotate', noseJnt+'.rotate')#连接 rotate
                    
        #---------------------------------------------------------------- 设置嘴唇旋转
        backCons = [con for con in rig.listConnections(self.main+'.CTRLCurve', s = False, d = True) if re.match('\w+Lip_Back_\d+M\Z',con)]
        allBackCons = [con for con in rig.listConnections(self.main+'.CTRLCurve', s = False, d = True) if re.match('\w+_Back_\d+M\Z',con)]
        allBackGRP = rig.group([con+'_GRP' for con in allBackCons],n = self.main+'_BackCon')
        upLipCons = [con for con in backCons if re.match('\w+UpLip_Back_\d+M\Z',con)]
        dnLipCons = [con for con in backCons if re.match('\w+DnLip_Back_\d+M\Z',con)]  
        
        
        upSmallCon = []#上嘴唇back控制器
        if len(upLipCons)%2:
            i = (len(upLipCons)-1)/2-1
            upSmallCon.append('LfUpLip_Back_'+str(i)+'M')
            upSmallCon.append('RtUpLip_Back_'+str(i)+'M') 
            upSmallCon.append('MdUpLip_Back_'+str(0)+'M')                          
        else:
            i = len(upLipCons)/2-1
            upSmallCon.append('LfUpLip_Back_'+str(i)+'M')
            upSmallCon.append('RtUpLip_Back_'+str(i)+'M')   
 
        dnSmallCon = []#下嘴唇back控制器
        if len(upLipCons)%2:
            i = (len(dnLipCons)-1)/2-1
            dnSmallCon.append('LfDnLip_Back_'+str(i)+'M')
            dnSmallCon.append('RtDnLip_Back_'+str(i)+'M') 
            dnSmallCon.append('MdDnLip_Back_'+str(0)+'M')                          
        else:
            i = len(upLipCons)/2-1
            dnSmallCon.append('LfDnLip_Back_'+str(i)+'M')
            dnSmallCon.append('RtDnLip_Back_'+str(i)+'M')    
        
        rotateJointGrp = []
        for con in  upSmallCon:
            lipJoint = 'Up_Lip_Joint'
            lipCon = 'Up_Lip_M'
            if not rig.objExists(lipJoint+'_RotateLip'):
                lipRotateJoint = rig.duplicate(lipJoint, n = lipJoint+'_RotateLip')[0]
                lipGrp = rig.group(lipRotateJoint, n = lipJoint+'_RotateLip_GRP')
                rig.connectAttr(lipCon+'.rotate',lipRotateJoint+'.rotate')   
            else:
                lipRotateJoint = lipJoint+'_RotateLip'
                lipGrp = lipJoint+'_RotateLip_GRP'
                
            
            conParent = rig.listRelatives(con+'_GRP', p = True)[0]
            posMat = rig.getAttr(con+'_GRP.worldMatrix')
            posGrp = rig.group(empty = True, n = con+'_Loc_GRP')
            rig.xform(posGrp, m = posMat)
            rig.parent(posGrp, conParent)
            
            rig.parentConstraint(lipRotateJoint,posGrp, mo = True)

            rig.connectAttr(posGrp+'.translate',con+'_GRP.translate')                          

            rotateJointGrp.append(lipGrp)
        for con in  dnSmallCon:
            lipJoint = 'Dn_Lip_Joint'
            lipCon = 'Dn_Lip_M'
            if not rig.objExists(lipJoint+'_RotateLip'):
                lipRotateJoint = rig.duplicate(lipJoint, n = lipJoint+'_RotateLip')[0]
                lipGrp = rig.group(lipRotateJoint, n = lipJoint+'_RotateLip_GRP')
                rig.connectAttr(lipCon+'.rotate',lipRotateJoint+'.rotate')    
            else:
                lipRotateJoint = lipJoint+'_RotateLip'
                lipGrp = lipJoint+'_RotateLip_GRP'
                
            
            conParent = rig.listRelatives(con+'_GRP', p = True)[0]
            posMat = rig.getAttr(con+'_GRP.worldMatrix')
            posGrp = rig.group(empty = True, n = con+'_Loc_GRP')
            rig.xform(posGrp, m = posMat)
            rig.parent(posGrp, conParent)
            
            rig.parentConstraint(lipRotateJoint,posGrp, mo = True)

            rig.connectAttr(posGrp+'.translate',con+'_GRP.translate') 
            
            rotateJointGrp.append(lipGrp)            
        
        rotateGrp = rig.group(rotateJointGrp, n = 'Mouth_rotate_GRP')   
        rig.parent(rotateGrp, rigGrp) 
        #--------------------------------------------------- 将main和macroCon控制器放到适当的jaw骨骼下
        cons = [u'Lf_CornerLip_M', u'Rt_CornerLip_M', u'Dn_Lip_M', u'Mouth_Tip_M']
        jaw =  'Jaw_Joint' 
        jawSwivle = 'Jaw_Swivle_Joint_UP'
        moutTip = 'jawSwivel_M'
        
        jawSwivleMat = rig.getAttr(jawSwivle+'.worldMatrix')        
        jawMat = rig.getAttr(jaw+'.worldMatrix')
        jawGrpUp = rig.group(empty = True, n = jaw.replace('_Joint', 'Move_Up'))
        jawGrpTop = rig.group(jawGrpUp, n = jaw.replace('_Joint', 'Move_Top')) 
        rig.xform(jawGrpTop, m = jawMat) 
        
        SwivleGrp = rig.group(empty = True, n = 'awSwivle_Rotate_GRP')
        rig.xform(SwivleGrp, m = jawSwivleMat)
        SwivleGrpTop = CA.addGrp().grp(SwivleGrp, 'mouth')
              
        for con in cons:
            jntUP = re.compile('_M\Z').sub('_Joint_Up', con)
            mainCon = re.compile('_M\Z').sub('_M_GRP', con)
            macroCon = re.compile('_M\Z').sub('Macro_M_GRP', con)
            
            jntTop = rig.listRelatives(jntUP,p = True)[0]
            TopMat = rig.getAttr(jntTop+'.worldMatrix')
            
            newUp = rig.group(empty = True, n = jntUP.replace('_Joint', 'Move'))
            newTop = rig.group(newUp, n = jntTop.replace('_Joint', 'Move'))
            
            rig.xform(newTop, m = TopMat)
            rig.connectAttr(jntUP+'.rotate', newUp+'.rotate')
            
            rig.parent(mainCon, newUp)
            rig.parent(macroCon, newUp)
            rig.parent(newTop,jawGrpUp)
            
        rig.connectAttr(jaw+'.rotate', jawGrpUp+'.rotate')
        rig.connectAttr(moutTip+'.rotate', jawSwivle+'.rotate')
        rig.connectAttr(moutTip+'.rotate', SwivleGrp+'.rotate')            
        rig.parent(jawGrpTop, SwivleGrp)
        rig.parent(SwivleGrpTop, rigGrp)
        
        rig.parentConstraint(moutTip, 'JawMain_M_GRP', mo = True)
        rig.parentConstraint(moutTip, 'Up_Lip_M_GRP', mo = True)
            
        
        #-------------------------------------------------------------- 将控制器P给rigGrp
        rig.parent(self.head+'_CTRLBsCurve',rigGrp)
        rig.parent(self.head+'_CTRLMacroCurve',rigGrp)
        rig.parent(self.main+'_CTRLCurve',rigGrp)
        
         
        #----------------------------------------------------------------- 隐藏控制器
        for con in allBackCons:#隐藏back控制器的shape节点
            conShape = rig.listRelatives(con, s = True)[0]
            rig.hide(conShape)
            
        hideCon = CA.changeController()
        hideCon.operate = 'hide'
        hideCon.selectTypes('small')#隐藏main控制器
        hideCon.selectTypes('macro')#隐藏macro控制器
        hideCon.selectTypes('cross')#隐藏cross控制器
        
        hideJnts = [u'Lf_CornerLip_Joint', u'Rt_CornerLip_Joint', u'Mouth_Tip_Joint', u'Dn_Lip_Joint', u'JawMain_Joint', u'Lf_Cheek_Joint', u'Rt_Cheek_Joint', u'Up_Lip_Joint', u'Up_Lip_Joint_RotateLip', u'Dn_Lip_Joint_RotateLip', u'Rt_Brow_Joint', u'Lf_Brow_Joint', u'Nose_Joint'] 
        rig.hide(hideJnts)#隐藏骨骼

    def Groups(self):
        rig.parent(self.main,self.deformerGrp.createGrp())
        rig.parent(self.head,self.deformerGrp.createGrp())
        
    def done(self):
        self.getData()
        self.skinCurve() 
        self.setBlendShape()
#        self.skinClusterBack()
        self.clearNode()
        self.connectTranslateToMacro()
        self.Groups()
        
        
#===============================================================================
# 用于建立或修改blendShape        
#===============================================================================
class createBlendShape():
    def __init__(self):
        self.allBsCurve = []
        self.auto = False#是否打开自动调整blendShape曲线
        self.main = 'Main_Control_GRP'
        self.head = 'Head_Control_GRP'
        self.BSDict = {u'+translateX':'OUT', u'+translateY':'UP', u'+translateZ':'Front',u'-translateX':'IN', u'-translateY':'DN', u'-translateZ':'BACK'} 
        self.getData()
         
    def getData(self):
        self.baseCurve = rig.listConnections(self.main+'.CTRLBaseCurve', s = False, d = True)[0]
        self.origentCurve = rig.listConnections(self.main+'.CTRLOrigenCurve', s = False, d = True)[0]
        self.macro =  rig.listConnections(self.head+'.CTRLMacroCurve', s = False, d = True)
        self.small = rig.listConnections(self.main+'.CTRLCurve', s = False, d = True)
        self.bsCon = rig.listConnections(self.head+'.CTRLBsCurve', s = False, d = True)
        self.bsRoCon = rig.listConnections(self.head+'.CTRLBSRotate', s = False, d = True)
        self.bsDataRV,self.bsDataAtt,self.bsDataValue = self.getBsData()
        self.bsDataSet = set([att for att in self.bsDataAtt])
        
        #得到控制器与曲线点的对应关系
        ControllerDict = dict([(rig.getAttr(con+'.vtxNum'),con) for con in self.small if  not re.match('\w+_Back_\d+M',con)])#创建控制器字典
        nums = [i for i in ControllerDict.keys()]#获得编号
        nums.sort()#对编号进行排序
        self.cons = [ControllerDict[i] for i in nums]#对macro控制器排序
        
    #得到带有blendShape的属性
    def getBsData(self):
        bsDataRV = {}
        bsDataAtt = []
        bsDataValue = []
        BSDict = dict([(self.BSDict[translate],translate) for translate in self.BSDict])
        allBsCons = copy.deepcopy(self.bsCon)
        allBsCons.extend(self.bsRoCon)
        for con in allBsCons:
            RVS = rig.listConnections(con, s = False, d = True, type = 'remapValue')#列出remapValue节点
            if RVS:#如果存在
                bsDataRV[con] = RVS#增加到字典
                for RV in RVS:
                    translate = BSDict[RV.split('_')[-2]][1::]#得到位移属性
                    value = rig.getAttr(RV+'.limitValue')#得到位移值
                    
                    if value < 0:#设置remapValue节点的参数
                        rig.setAttr(RV+'.inputMin',value)
                        rig.setAttr(RV+'.inputMax',0)
                        rig.setAttr(RV+'.value[0].value_Position',0)
                        rig.setAttr(RV+'.value[0].value_FloatValue',1)
                        rig.setAttr(RV+'.value[1].value_Position',1)
                        rig.setAttr(RV+'.value[1].value_FloatValue',0)
                    else:
                        rig.setAttr(RV+'.inputMin',0)
                        rig.setAttr(RV+'.inputMax',value)
                    
                    bsDataAtt.append(con+'.'+translate)
                    bsDataValue.append(value)

                  
        return bsDataRV,bsDataAtt,bsDataValue
        
    #设置blendShape控制器的值
    def setDynValue(self):
        self.auto = True
        for i,att in enumerate(self.bsDataAtt):

            plug =  rig.listConnections(att, s = True, d = False, p = True, scn = True)
            if plug:
                rig.setAttr(plug[0],self.bsDataValue[i]) 
                self.addBlendShapeControl()
                rig.setAttr(plug[0],0)
                print plug[0],self.bsDataValue[i]
            else:
                rig.setAttr(att,self.bsDataValue[i])
                self.addBlendShapeControl()
                rig.setAttr(att,0)
                print att,self.bsDataValue[i]
            
            
#            rig.setAttr(att,0)#将值设为0
            
    #创建或修改blendShape
    def CMblendShape(self,RV):
        pointPos  = [rig.xform(con,q = True,t = True,ws = True)for con in self.cons]#获得控制器位置信息

        
        existsCurve = rig.listConnections(RV, s = False, d = True, type = 'blendShape')
        if existsCurve:#是否连接到blendShape节点上
            #生成曲线
            tempCurve = rig.curve(d = 1,p = pointPos)
            curveName = rig.rename(tempCurve,RV+'_Curve_Edit')
            
            if re.match('\AJawMain_M_', RV):#如果是下巴控制器
                self.clearController()
                Sbs = SBS.SkinBlendShape(self.baseCurve,curveName)
                Sbs.computeNewPosition()   
                
                
            if re.match('\AjawSwivel_M_', RV):#如果是下巴旋转控制器
                self.clearController()
                Sbs = SBS.SkinBlendShape(self.baseCurve,curveName)
                Sbs.computeNewPosition() 
                         
            #blendShape节点是否存在
            BS = CA.getDeformerNode()
            BS.Deform = 'blendShape'
            existsBS = BS.getInfo(self.baseCurve)
            
            if existsBS:
                pointPos = rig.xform(curveName+'.cv[*]', q = True, t = True, ws = True)
                rig.setAttr(RV+'_Curve.cv[*]',*pointPos, type = 'double3')
                self.clearController() 
                rig.delete(curveName)            
            else:
                pass

        else:
            #生成曲线
            tempCurve = rig.curve(d = 1,p = pointPos)
            curveName = rig.rename(tempCurve,RV+'_Curve')
            
            if re.match('\AJawMain_M_', RV):#如果是下巴控制器
                self.clearController()
                Sbs = SBS.SkinBlendShape(self.baseCurve,curveName)
                Sbs.computeNewPosition()
            
            #blendShape节点是否存在
            BS = CA.getDeformerNode()
            BS.Deform = 'blendShape'
            existsBS = BS.getInfo(self.baseCurve)
            
            self.allBsCurve.append(curveName)#增加到列表
            if existsBS:
                num = rig.blendShape(existsBS, q = True, wc = True)
                rig.blendShape(existsBS, e = True, t = (self.baseCurve,num+1,curveName,1))
                rig.connectAttr(RV+'.outValue',existsBS+'.'+curveName)
            else:
                BS = rig.blendShape(curveName,self.baseCurve, frontOfChain = True)[0]
                rig.connectAttr(RV+'.outValue',BS+'.'+curveName)
    
    #将small和macro控制器归零
    def clearController(self):
        zero = (0,0,0)
        for con in self.macro:
            rig.xform(con,t = zero,wd = True)

        for con in self.small:
            rig.xform(con,t = zero,wd = True)

        
    #增加blendShape        
    def addBlendShapeControl(self):
        Tol = 0.0001
        for conAtt in self.bsDataSet:
            value = rig.getAttr(conAtt)
            if Tol < value or value< -1*Tol:
                if value < 0:
                    conAttrList = conAtt.split('.')
                    con = conAttrList[0]
                    att = self.BSDict['-'+conAttrList[1]]
                    RVname = con+'_'+att+'_RV' #得到remapValue节点  
                else:
                    conAttrList = conAtt.split('.')
                    con = conAttrList[0]
                    att = self.BSDict['+'+conAttrList[1]]
                    RVname = con+'_'+att+'_RV' #得到remapValue节点     
                    
                if RVname in self.bsDataRV[con]:
                    macroSign = self.auto and (not re.match('\AJawMain_M_', RVname))#是否设置macro控制器的值
                    if macroSign:#设置macro控制器的值
                        macroCon = conAtt.replace('_M.','Macro_M.')
                        plug =  rig.listConnections(macroCon, s = True, d = False, p = True, scn = True)
                        if plug:
                           rig.setAttr(plug[0],value) 
                        else:
                            rig.setAttr(macroCon,value)
                        
                    self.CMblendShape(RVname)
                    
                    if macroSign:#将macro控制器归零
                        macroCon = conAtt.replace('_M.','Macro_M.')
                        if plug:
                           rig.setAttr(plug[0],0) 
                        else:
                            rig.setAttr(macroCon,0)
                            
    def Groups(self):
        print self.allBsCurve
        allBsCurve = rig.group(self.allBsCurve,n = self.main+'_BSCurve')
        rig.setAttr(allBsCurve+'.template',1)
        rig.parent(allBsCurve,self.main)
    
        
    def done(self):
        self.setDynValue()
        self.Groups()