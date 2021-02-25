#-*- coding: utf-8 -*-

import maya.cmds as rig
from RIG.face.controlers import CreateControler
import RIG.WDface.WD_MainClass as CA
import re

def WD_buildPostion(main,ear,eye,eyebrow,tongue,tooth,joints,eyebrowNum,mouthNum,nasolabialGrooveNum):
    if main:
        mainObject = BuildMainController(eyebrowNum ,mouthNum,nasolabialGrooveNum)
        mainObject.done()
        
#        rig.connectAttr('LfUpLip_0M.translate', 'LfDnLip_0M.translate')
#        rig.connectAttr('RtUpLip_0M.translate', 'RtDnLip_0M.translate')
        
    if ear:
        earObject = BuildEarController()
        earObject.done()
        
    if eye:
        eyeObject = BuildEyeController()
        eyeObject.num = 3
        eyeObject.done()
        
    if eyebrow:
        eyebrowObject = BuildEyebrowController()
        eyebrowObject.done()

    if tongue:
        tongueObject = BuildTongueController()
        tongueObject.num = 5
        tongueObject.done()
        
    if tooth:
        toothObject = BuildToothController()
        toothObject.done()

    if joints:
        jointsObject = BuildjointsController()
        jointsObject.done()
        
    faceRig = CA.getRigGrp().createGrp()#生成空组Head_FaceRig_Control_GRP
    rig.select(cl = True)
    jnt = rig.joint(p = (0, 15, 0.44), n = 'Head_Zero_Joint')
    jntGrp = rig.group(jnt, n = jnt+'_GRP')
    rig.parent(jntGrp, faceRig)
    
    grps = [u'Main_Control_GRP', u'Ear_Control_GRP', u'Eye_Control_GRP', u'Eyebrow_Control_GRP', u'Tongue_Control_GRP', u'Tooth_Control_GRP', u'Head_Control_GRP']    
    for grp in grps:#将每个部件的组P给Head_FaceRig_Control_GRP
        if rig.objExists(grp):
            rig.parent(grp, faceRig)
    
    rig.select(faceRig)#选择Head_FaceRig_Control_GRP
    rig.xform(faceRig, cp = True, p = True)
        
class BuildMainController():
    def __init__(self,eyebrowNum = 17,mouthNum = 8,nasolabialGrooveNum = 6):
        self.eyebrowNum = eyebrowNum
        self.mouthNum = mouthNum
        self.nasolabialGrooveNum = nasolabialGrooveNum
        self.otherNum = 5
        self.grp = 'Main_Control_GRP'
        self.colors = [17,20,18,21,30,17,20,18,21,30]#控制器颜色
        self.names = ['Mask','LfCheek','RtCheek','UpLip','DnLip','Mask_Back','LfCheek_Back','RtCheek_Back','UpLip_Back','DnLip_Back',]#控制器名字
                
        self.allLoftCurve = ['out_eyebrowCurve','out_LfNasolabialCurve','out_RtNasolabialCurve','out_UpMouthCurve','out_DnMouthCurve','in_eyebrowCurve','in_LfNasolabialCurve','in_RtNasolabialCurve','in_UpMouthCurve','in_DnMouthCurve']
        self.out_eyebrowCurve = [[0.093062852370000004, 16.389567700000001, 1.4692475060000001], [0.29171828280000006, 16.33245921, 1.434800531], [0.58931531940000004, 16.1797884, 1.4346487199999998], [0.80840389990000006, 16.332057420000005, 1.2264007159999999], [0.84761215310000004, 16.662736349999999, 1.2148513409999997], [0.78997980180000005, 16.901615830000001, 1.3686666619999999], [0.52970747460000001, 16.978361509999999, 1.5675650589999999], [0.2368713137, 16.94852208, 1.611703119], [4.7459452820000001e-10, 16.942525150000002, 1.6105279539999997], [-0.23687131700000003, 16.948522570000002, 1.611703157], [-0.52970749139999995, 16.97836113, 1.5675650839999999], [-0.78997981549999996, 16.901615140000001, 1.3686666489999999], [-0.84761214259999995, 16.662736890000001, 1.214851379], [-0.80840390920000005, 16.332057949999999, 1.226400733], [-0.58931529520000003, 16.179788590000001, 1.4346487519999997], [-0.29171827440000003, 16.332458500000001, 1.434800506], [-0.093062855299999997, 16.389568329999999, 1.4692474600000001]]
        self.out_LfNasolabialCurve = [[0.12853086629999999, 16.056616170000002, 1.880558196], [0.29613769290000008, 16.04691266, 1.8838864850000001], [0.57040166340000009, 15.851219260000001, 1.8094772379999997], [0.68277786080000014, 15.5620008, 1.6781279119999999], [0.36871645380000001, 15.203506880000001, 1.7264631449999999], [0.1012533285, 15.112757370000002, 1.8398065629999998]]
        self.out_RtNasolabialCurve = [[-0.12853085989999999, 16.056615829999998, 1.8805582519999999], [-0.29613769050000005, 16.046913150000002, 1.8838864559999999], [-0.57040166850000007, 15.851219179999999, 1.8094772099999998], [-0.68277788160000008, 15.56200123, 1.6781278849999999], [-0.36871644850000002, 15.203506470000002, 1.7264631989999997], [-0.1012533307, 15.112757680000001, 1.8398065569999997]]
        self.out_UpMouthCurve = [[0.29424550690000006, 15.4890, 1.8539631219999997], [0.23497731230000002, 15.52935735, 1.904742556], [0.1413239892, 15.536002889999999, 1.9783556369999997], [-0.00032652201299999999, 15.53671256, 2.0012264590000002], [-0.14132398369999999, 15.536003109999999, 1.9783556459999998], [-0.23497730490000002, 15.529356959999999, 1.9047425989999998], [-0.29424551130000004, 15.489294, 1.8539631369999996]]
        self.out_DnMouthCurve = [[0.29424550690000006, 15.48929504, 1.8539631219999997], [0.21801089480000002, 15.44684151, 1.8921622629999997], [0.11959018110000001, 15.428295059999998, 1.9599677899999999], [0.0032144452140000002, 15.430541549999999, 1.9787172189999997], [-0.1195901781, 15.428295139999999, 1.9599677319999995], [-0.21801088750000003, 15.446841239999999, 1.8921622039999995], [-0.29424551130000004, 15.489295009999999, 1.8539631369999996]]
        self.in_eyebrowCurve = [[0.046531423559999979, 16.505567188540041, 0.70791284695301715], [0.14585913877499998, 16.477012943540039, 0.69068935945301713], [0.29465765707500002, 16.400677538540041, 0.6906134539530171], [0.40420194732499992, 16.47681204854004, 0.58648945195301705], [0.42380607392500003, 16.642151513540039, 0.58071476445301706], [0.39498989827499997, 16.76159125354004, 0.65762242495301715], [0.26485373467499995, 16.799964093540037, 0.75707162345301715], [0.11843565422499998, 16.785044378540039, 0.77914065345301708], [-2.3877027588044447e-09, 16.782045913540038, 0.77855307095301707], [-0.11843566112500002, 16.785044623540038, 0.7791406724530171], [-0.26485374832499997, 16.799963903540039, 0.75707163595301707], [-0.39498991037499998, 16.76159090854004, 0.65762241845301705], [-0.42380607392500003, 16.64215178354004, 0.58071478345301708], [-0.40420195722500007, 16.476812313540041, 0.58648946045301709], [-0.29465765022500001, 16.400677633540042, 0.69061346995301709], [-0.14585913982500001, 16.477012588540042, 0.69068934695301709], [-0.046531430275000021, 16.505567503540039, 0.70791282395301713]] 
        self.in_LfNasolabialCurve =  [[-0.13174236417500002, 15.724271086267061, 0.64834173949759855], [-0.047938950874999997, 15.71941933126706, 0.65000588399759862], [0.08919303437499998, 15.62157263126706, 0.61280126049759864], [0.145381133075, 15.476963401267062, 0.54712659749759873], [-0.011649570425000005, 15.297716441267061, 0.57129421399759872], [-0.145381133075, 15.252341686267062, 0.62796592299759868]]
        self.in_RtNasolabialCurve = [[0.13174237312499998, 15.724270923767058, 0.64834178149759836], [0.047938957824999989, 15.71941958376706, 0.65000588349759836], [-0.089193031174999993, 15.62157259876706, 0.61280126049759853], [-0.145381137725, 15.476963623767061, 0.54712659799759855], [0.011649578824999979, 15.297716243767061, 0.57129425499759845], [0.145381137725, 15.25234184876706, 0.62796593399759848]]
        self.in_UpMouthCurve = [[0.14712275455000001, 15.476452013767057, 0.56175040649759844], [0.11748865724999999, 15.496483168767057, 0.58714012349759848], [0.070661995699999994, 15.499805938767057, 0.62394666399759846], [-0.00016325990650000613, 15.500160773767059, 0.63538207499759869], [-0.070661990750000001, 15.499806048767056, 0.6239466684975985], [-0.11748865135, 15.496482973767057, 0.58714014499759848], [-0.14712275454999998, 15.476451998767057, 0.56175041399759851]]
        self.in_DnMouthCurve = [[0.14712275455000001, 15.503556381267058, 0.56737771649759861], [0.10900544849999999, 15.482329616267059, 0.5864772869975986], [0.059795091649999993, 15.473056391267059, 0.6203800504975987], [0.0016072237069999938, 15.474179636267058, 0.62975476499759864], [-0.059795087950000006, 15.473056431267059, 0.62038002149759863], [-0.10900544265000001, 15.482329481267058, 0.5864772574975986], [-0.14712275454999998, 15.503556366267057, 0.56737772399759867]]
#        self.done()

    #-------------------------------------------------------------------- 生成新的曲线
    def createCurve(self,data,name,num):
        tempCurveName = rig.curve(d =3,p = data)
        curCurveName = rig.rename(tempCurveName,name)
        self.connectAddAttr(curCurveName,'LoftCurve')#连接属性
        rig.rebuildCurve(curCurveName,ch = False,rpo = 1,rt = 0,end = 1,kr = 0,kcp = 0,kep = 1,kt = 0,s = num -3,d = 3,tol = 0.01)
    
    #-------------------------------------------------------------------- 生成所有曲线
    def createAllCurve(self):
        for BaseCurve in self.allLoftCurve:
            if 'eyebrowCurve' in BaseCurve:
                num = self.eyebrowNum
            elif 'MouthCurve' in BaseCurve:
                num = self.mouthNum
            elif 'NasolabialCurve' in BaseCurve:
                num = self.nasolabialGrooveNum
            else:
                num = self.otherNum
                
            self.createCurve(self.__dict__[BaseCurve],BaseCurve,num)
            
    #---------------------------------------------------------------------- 生成曲面
    def loftCurve(self):
        outLoftCurve = [outCurve for outCurve in self.allLoftCurve if 'out_' in outCurve]#所有out曲线
        for cur in outLoftCurve:
            LoftNode = rig.createNode('loft',n = cur.replace('out_','Loft_'))#创建Loft节点
            rig.connectAttr(rig.listRelatives(cur,s = True)[0]+'.worldSpace[0]',LoftNode+'.inputCurve[0]')
            rig.connectAttr(rig.listRelatives(cur.replace('out_','in_'),s = True)[0]+'.worldSpace[0]',LoftNode+'.inputCurve[1]')
        
            tempMeshNode = rig.createNode('mesh')#创建mesh节点
            MeshTransform = rig.rename(rig.listRelatives(tempMeshNode,p = True)[0],cur.replace('out_','Loft_')+'_Mesh')
            MeshNode = rig.listRelatives(MeshTransform,s = True)[0]
            self.connectAddAttr(MeshTransform,'LoftMesh')#连接属性
            nurbsTessellateNode = rig.createNode('nurbsTessellate',n = cur.replace('out_','nurbsTessellate_'))#创建nurbsTessellate节点
            #设置nurbsTessellate节点属性
            rig.setAttr(nurbsTessellateNode+'.polygonType',1)
            rig.setAttr(nurbsTessellateNode+'.format',2)
            rig.setAttr(nurbsTessellateNode+'.uNumber',1)
            rig.setAttr(nurbsTessellateNode+'.vNumber',3)
            rig.setAttr(nurbsTessellateNode+'.useChordHeightRatio',0)
            
            
            rig.connectAttr(LoftNode+'.outputSurface',nurbsTessellateNode+'.inputSurface')
            rig.connectAttr(nurbsTessellateNode+'.outputPolygon',MeshNode+'.inMesh')
    
    #--------------------------------------------------------------------- 生成控制器
    def createController(self):

        
        vtxNum = 0
        for i,cur in enumerate(self.allLoftCurve):
            color = self.colors[i]
            controllers = CreateControler(color,(0.02,0.02,0.02))
            controllers.signValue = 18424
            
            #区分控制器的左右和控制器的编号
            vtxs = rig.ls(rig.listRelatives(cur,s = True)[0]+'.cv[*]',fl = True)#控制器点数
            LenVtx = len(vtxs)
            vtxNums = []
            LfRtVtxs = []
            if len(vtxs)%2:
                average = ( LenVtx - 1 )/2
                for num in range(average):#左边控制器编号
                    LfRtVtxs.append('Lf')
                    vtxNums.append(num)
                vtxNums.append(0)
                LfRtVtxs.append('Md')
                for num in range(average):#左边控制器编号
                    vtxNums.append(average - num -1)
                    LfRtVtxs.append('Rt')
                
                
            else:
                average = (LenVtx)/2
                for num in range(average):#左边控制器编号
                    LfRtVtxs.append('Lf')
                    vtxNums.append(num)
                for num in range(average):#右边控制器编号
                    vtxNums.append(average - num -1)
                    LfRtVtxs.append('Rt')
            
            #控制器是否左右对称
            if re.compile(r'(out_Lf[A-Z]+|out_Rt[A-Z]+)').match(cur) or re.compile(r'(in_Lf[A-Z]+|in_Rt[A-Z]+)').match(cur):
                LfRt = True
            else:
                LfRt = False 
            
            
            for j,vtx in enumerate(vtxs):
                
                if LfRt:
                    conName = self.names[i]+'_'+str(j)+'M'#控制器名字
                else:
                    conName = LfRtVtxs[j]+self.names[i]+'_'+str(vtxNums[j])+'M'#控制器名字
                con = controllers.SK_b03(conName)
                rig.addAttr(con,at = 'long',ln = 'vtxNum', dv = vtxNum)#增加属性
                rig.setAttr(con+'.vtxNum',l = True)#锁定属性
                self.connectAddAttr(con,'CTRLCurve')#连接属性
                pos = rig.xform(vtx,q = True,t = True,ws = True)
                rig.xform(con,t = pos,ws = True)
                
                rig.connectAttr(con+'.translate',vtx.replace('.cv[','.controlPoints['))#将控制器的位移属性连接到曲线的控制点上
                vtxNum += 1

    
    
    def createEmptyGrp(self):#生成空组
        if rig.objExists(self.grp):
            self.grpName = self.grp
        else:
            self.grpName = rig.group(empty = True,n = self.grp)
#        rig.addAttr(self.grpName,at = 'long',ln = 'LoftMesh')
#        rig.addAttr(self.grpName,at = 'long',ln = 'LoftCurve')
#        rig.addAttr(self.grpName,at = 'long',ln = 'CTRLCurve')
        
        
    def connectAddAttr(self,AddObj,Attr):#增加并连接属性
        rig.addAttr(AddObj,at = 'long',ln = Attr)
        if not rig.attributeQuery(Attr,node = self.grpName,ex = True):
            rig.addAttr(self.grpName,at = 'long',ln = Attr)
        rig.connectAttr(self.grpName+'.'+Attr,AddObj+'.'+Attr)  
     
    def Groups(self):#整理层级
        LoftMeshs = rig.listConnections(self.grpName+'.LoftMesh',s = False, d = True)
        LoftCurves = rig.listConnections(self.grpName+'.LoftCurve',s = False, d = True)
        CTRLCurves = rig.listConnections(self.grpName+'.CTRLCurve',s = False, d = True)
        
        LoftMeshGRP = rig.group(LoftMeshs, n = self.grpName+'_LoftMesh')
        rig.setAttr(LoftMeshGRP+'.template',1)
        rig.setAttr(LoftMeshGRP+'.inheritsTransform',0)
        LoftCurveGRP = rig.group(LoftCurves, n = self.grpName+'_LoftCurve')
        rig.setAttr(LoftCurveGRP+'.template',1)
        CTRLCurveGRP = rig.group(CTRLCurves, n = self.grpName+'_CTRLCurve')
        
        rig.parent(LoftMeshGRP,LoftCurveGRP,CTRLCurveGRP,self.grpName)
        
        
          
    #-------------------------------------------------------------------- 完成主要模版
    def done(self):
        self.createEmptyGrp()#生成空组
        self.createAllCurve()#生成曲线
        self.loftCurve()#生成曲面
        self.createController()#生成控制器
        self.Groups()#整理层级
    #----------------------------------------------------------------- 获得选择的曲线的点的位置
    def getPosition(self):
        vtxs = rig.ls(rig.ls(sl = True)[0]+'.cv[*]',fl = True)
        allPos = []
        for vtx in vtxs:
            pos = rig.xform(vtx,q = True,t = True,ws = True)
            allPos.append(pos)
        return allPos

class BuildEarController():
    def __init__(self):
        self.grp = 'Ear_Control_GRP'
        self.ctrlName = 'Era_Joint'
        
        
    def createJoint(self):
        rig.select(cl = True)
        LfPos = (0.97724950312632142, 16.17158651352031, 0.022281996905576196)
        LfJnt = rig.joint(p = LfPos,n = 'Lf'+self.ctrlName)
        self.connectAddAttr(LfJnt,'CTRLJoint')#连接属性
        rig.select(cl = True)
        RtPos = (-0.97724950312632142, 16.17158651352031, 0.022281996905576196)
        RtJnt = rig.joint(p = RtPos,n = 'Rt'+self.ctrlName)
        self.connectAddAttr(RtJnt,'CTRLJoint')#连接属性
        
    def createEmptyGrp(self):#生成空组
        if rig.objExists(self.grp):
            self.grpName = self.grp
        else:
            self.grpName = rig.group(empty = True,n = self.grp)       
        
        
    def connectAddAttr(self,AddObj,Attr):#增加并连接属性
        rig.addAttr(AddObj,at = 'long',ln = Attr)
        if not rig.attributeQuery(Attr,node = self.grpName,ex = True):
            rig.addAttr(self.grpName,at = 'long',ln = Attr)
        rig.connectAttr(self.grpName+'.'+Attr,AddObj+'.'+Attr)  
        
    def Groups(self):#整理层级
        CTRLJoints = rig.listConnections(self.grpName+'.CTRLJoint',s = False, d = True)
        CTRLJointGRP = rig.group(CTRLJoints, n = self.grpName+'_CTRLJoint')
        rig.parent(CTRLJointGRP,self.grpName)
#        CTRLJointGRP = rig.group(self.name+'_0Joint', n = self.grpName+'_CTRLJoint')
#        rig.parent(CTRLJointGRP,self.grpName)
            
    def done(self):
        self.createEmptyGrp()#生成空组
        self.createJoint()
        self.Groups()#整理层级

class BuildEyeController():
    def __init__(self):
        self.controller = CreateControler()
        self.grp = 'Eye_Control_GRP'
        self.ctrlName = 'Eye_M'
        self.num = 3
        self.conPos = [(0.0, 16.623626770105922, 4.1056612661848035),(0.47205042927365248, 16.623626770105922, 4.1056612661848035),(-0.47205042927365248, 16.623626770105922, 4.1056612661848035)]
        self.jointPos = [([0, 16.600944519043441, 1.3624849915501727]),(0.47289100288351393, 16.600944519043441, 1.3624849915501727),(-0.47289100288351393, 16.600944519043441, 1.3624849915501727)]
        self.Lf_LidPos = [[0.51449495125093525, 16.614712948647536, 1.6282982423800447],[0.51446175243023684, 16.524417626257684, 1.6211440872455507]]
        self.Rt_LidPos = [[-0.51449495125093525, 16.614712948647536, 1.6282982423800447],[-0.51446175243023684, 16.524417626257684, 1.6211440872455507]]

    def getController(self):#得到控制器名
        if self.num == 1:
            self.NewCons = [self.ctrlName]
        if self.num > 1:
            self.NewCons = []
            LfNum = 0#左边编号
            RtNum = 0#右边编号
            for i in range(self.num):
                if 0 == i:
                    self.NewCons.append(self.ctrlName)
                else:
                    mainPre = self.ctrlName.split('_')[0]
                    if i%2:
                        self.NewCons.append('Lf_'+mainPre+'_'+str(LfNum)+'M')
                        LfNum += 1
                    else:
                        self.NewCons.append('Rt_'+mainPre+'_'+str(RtNum)+'M')
                        RtNum += 1
                        
    def createCons(self):#生成所有控制器
        for con in self.NewCons:
            if 'Lf_' == con[0:3]:
                self.controller.setColor(6)
                ts = self.conPos[1]
                jntPos = self.jointPos[1]
                sc = [1,1,1]
                self.eyelip(con, True)
            elif 'Rt_' == con[0:3]:
                self.controller.setColor(6)
                ts = self.conPos[2]
                jntPos = self.jointPos[2]
                sc = [1,1,1]
                self.eyelip(con, False)
            else:
                self.controller.setColor(13)#对控制器设置颜色
                ts = self.conPos[0]
                jntPos = self.jointPos[0]
                sc = [4.373,1,1.828]
                
            rt = [90,1,1]
            self.singeCon(con, rt, ts, sc)
            
            #生成眼睛骨骼
            rig.select(cl = True)
            jntName = rig.joint(p = jntPos,n = re.compile('M\Z').sub('Joint',con))
            self.connectAddAttr(jntName,'CTRLJoint')#连接属性

    def eyelip(self,name, UpDn):#增加眼皮控制器
        if UpDn:
            UpPos = self.Lf_LidPos[0]
            DnPos = self.Lf_LidPos[1]
        else:
            UpPos = self.Rt_LidPos[0]
            DnPos = self.Rt_LidPos[1]
        
        self.controller.setObjScale([0.05, 0.05, 0.05,])#对控制器进行缩放
        self.controller.signValue = 1258
        Con = self.controller.SK_b03(name.replace('_Eye','_UpLid'))
        self.connectAddAttr(Con,'CTRLCurve')#连接属性
        rig.xform(Con,t = UpPos,ws = True)
        Con = self.controller.SK_b03(name.replace('_Eye','_DnLid'))
        self.connectAddAttr(Con,'CTRLCurve')#连接属性
        rig.xform(Con,t = DnPos,ws = True)
        
    def singeCon(self,name,rt,ts,sc):#生成控制器

        self.controller.setObjScale([i*0.135 for i in sc])#对控制器进行缩放
        self.controller.signValue = 1548
        Con = self.controller.SK_b08(name)
        self.connectAddAttr(Con,'CTRLCurve')#连接属性
        rig.xform(Con,t = ts,ws = True)
        rig.xform(Con,ro = rt,ws = True)
        

    def createEmptyGrp(self):#生成空组
        if rig.objExists(self.grp):
            self.grpName = self.grp
        else:
            self.grpName = rig.group(empty = True,n = self.grp)
            
            
    def connectAddAttr(self,AddObj,Attr):#增加并连接属性
        rig.addAttr(AddObj,at = 'long',ln = Attr)
        if not rig.attributeQuery(Attr,node = self.grpName,ex = True):
            rig.addAttr(self.grpName,at = 'long',ln = Attr)
        rig.connectAttr(self.grpName+'.'+Attr,AddObj+'.'+Attr)  
    
    def extraAddControl(self):
        posInfo = [[0.73614344582613733, 16.604239304623771, 1.4948541970870548], [0.65308174148532172, 16.645676611373496, 1.5729513008857312], [0.54766851673494632, 16.64837652763509, 1.6214938988508214], [0.44244251319713446, 16.643562775959364, 1.619578378724102], [0.32071235980511059, 16.597797824873869, 1.596789667911807], [0.4362284617401162, 16.559762331346164, 1.6209728592220456], [0.54223046060668201, 16.550345353518203, 1.6173481804777063], [0.64635945406333351, 16.546858303215856, 1.5722915627040193]]
        LfName = ['Lf_CornerInLidMin_0','Lf_UpLidMin_1','Lf_UpLidMin_2','Lf_UpLidMin_3','Lf_CornerOutLidMin_0','Lf_DnLidMin_3','Lf_DnLidMin_2','Lf_DnLidMin_1']
        RtName = ['Rt_CornerInLidMin_0','Rt_UpLidMin_1','Rt_UpLidMin_2','Rt_UpLidMin_3','Rt_CornerOutLidMin_0','Rt_DnLidMin_3','Rt_DnLidMin_2','Rt_DnLidMin_1']

        for i,pos in enumerate(posInfo):
            self.controller.setColor(13)
            self.controller.setObjScale([0.02, 0.02, 0.02,])#对控制器进行缩放
            self.controller.signValue = 11548
            LfCon = self.controller.SK_b03(LfName[i]+'M')
            RtCon = self.controller.SK_b03(RtName[i]+'M')
            self.connectAddAttr(LfCon,'CTRLCurve')#连接属性
            self.connectAddAttr(RtCon,'CTRLCurve')#连接属性
            rig.xform(LfCon,t = pos,ws = True) 
            pos[0] = pos[0]*-1           
            rig.xform(RtCon,t = pos,ws = True)          
        
    def Groups(self):#整理层级
        CTRLCurves = rig.listConnections(self.grpName+'.CTRLCurve',s = False, d = True)
        CA.freezeObj().freeze(CTRLCurves)
        CTRLJoints = rig.listConnections(self.grpName+'.CTRLJoint',s = False, d = True)
        
        CTRLCurveGRP = rig.group(CTRLCurves, n = self.grpName+'_CTRLCurve')
        CTRLJointGRP = rig.group(CTRLJoints, n = self.grpName+'_CTRLJoint')
        
        mainCons = [con for con in CTRLCurves if re.match('Eye_M', con)]
        secCons = [con for con in CTRLCurves if re.match('\ALf_Eye_\d+M|\ARt_Eye_\d+M', con)]
        if secCons:
            rig.parent(secCons,mainCons[0])

        rig.parent(CTRLCurveGRP,CTRLJointGRP,self.grpName)


      
    def done(self):
        self.createEmptyGrp()#生成空组
        self.getController()
        self.createCons() 
        self.extraAddControl()#增加眼睛周围的控制器
        self.Groups()#整理层级
        
        
class BuildEyebrowController():
    def __init__(self):
        self.grp = 'Eyebrow_Control_GRP'
        
    
    def done(self):
        rig.group(empty = True, n = self.grp)    


class BuildTongueController():
    def __init__(self):
        self.num = 5
        self.curve = [[0.0, 15.118087009113706, 0.40258722240805223], [0.0, 15.347370535457042, 0.63976746277523944], [0.0, 15.040964717090555, 1.0819408985006895], [0.0, 14.882214111225489, 1.4111297441894901], [0.0, 14.769216472947335, 1.6032325024770482]]
        self.tempCruveName = 'Temp_Curve_Tongue_TP'
        self.grp = 'Tongue_Control_GRP'
        self.name = 'Tongue'

        
    def createJoint(self):
        tempCurveName = rig.curve(d =3,p = self.curve)#生成曲线
        curCurveName = rig.rename(tempCurveName,self.tempCruveName)#重命名曲线
        curCurveNameShape = rig.listRelatives(curCurveName,s = True)[0]#获得形节点
        CurveInfo = CA.curveAverage()
        posInfo = CurveInfo.getInfo(curCurveNameShape, self.num)[1]#获得位置信息
        rig.delete(curCurveName)#删除曲线
        
        #生成骨骼
        rig.select(cl = True)
        for i,pos in enumerate(posInfo):
            jnt = rig.joint(p = pos,n = self.name+'_'+str(i)+'Joint')
            self.connectAddAttr(jnt,'CTRLJoint')#连接属性
        
 
    def createEmptyGrp(self):#生成空组
        if rig.objExists(self.grp):
            self.grpName = self.grp
        else:
            self.grpName = rig.group(empty = True,n = self.grp)       
        
        
    def connectAddAttr(self,AddObj,Attr):#增加并连接属性
        rig.addAttr(AddObj,at = 'long',ln = Attr)
        if not rig.attributeQuery(Attr,node = self.grpName,ex = True):
            rig.addAttr(self.grpName,at = 'long',ln = Attr)
        rig.connectAttr(self.grpName+'.'+Attr,AddObj+'.'+Attr)  
        
    def Groups(self):#整理层级
#        CTRLJoints = rig.listConnections(self.grpName+'.CTRLJoint',s = False, d = True)
#        CTRLJointGRP = rig.group(CTRLJoints, n = self.grpName+'_CTRLJoint')
#        rig.parent(CTRLJointGRP,self.grpName)
        CTRLJointGRP = rig.group(self.name+'_0Joint', n = self.grpName+'_CTRLJoint')
        rig.parent(CTRLJointGRP,self.grpName)

    def done(self):
        self.createEmptyGrp()#生成空组
        self.createJoint()
        self.Groups()#整理层级
        
#class BuildToothController(BuildMainController):
#    def __init__(self):
#        BuildMainController.__init__(self)
#        self.out_UpToothCurve = [[0.42627990367563268, 15.567103173297172, 1.559218903204648], [0.3155343438365758, 15.56710317329717, 1.7614594626323425], [0.003974563096613243, 15.567103173297175, 1.9966628974143283], [-0.31553435325622559, 15.567103385925295, 1.7614594697952264], [-0.42627990245819092, 15.567103385925295, 1.5592188835144036]] 
#        self.in_UpToothCurve = [[0.21313995153345591, 15.488306333110033, 0.48920524711773972], [0.15776717161392748, 15.488306333110032, 0.59032552683158701], [0.0019872812439461819, 15.488306333110035, 0.70792724422257991], [-0.15776717693247322, 15.488306439424093, 0.59032553041302893], [-0.21313995153345588, 15.488306439424093, 0.48920523727261755]] 
#        self.out_DnToothCurve = [[0.4499726071727172, 15.300131007381125, 1.4961614096012203], [0.36592660612563599, 15.300131007381125, 1.6579895315041979], [0.003974563096613243, 15.300131007381129, 1.9786103844935152], [-0.365926593542099, 15.300130844116213, 1.6579895019531248], [-0.44997259974479675, 15.300130844116213, 1.4961614608764646]] 
#        self.in_DnToothCurve = [[0.2249863017293785, 15.488306427083288, 0.47795399702452501], [0.1829633012058379, 15.488306427083288, 0.5588680579760138], [0.0019872796913265101, 15.488306427083289, 0.71917848447067245], [-0.1829632986280296, 15.488306345450832, 0.55886804320047723], [-0.22498630172937847, 15.488306345450832, 0.47795402266214715]]
#    
#    def done(self):
#        self.out_DnMouthCurve = self.out_UpToothCurve
#        self.in_DnMouthCurve = self.out_DnToothCurve
#        self.out_eyebrowCurve = self.in_UpToothCurve
#        self.in_eyebrowCurve = self.in_DnToothCurve        
#        self.allLoftCurve = ['out_UpToothCurve','out_DnToothCurve','in_UpToothCurve','in_DnToothCurve']
#        self.colors = [16,16,16,16]
#        self.names = ['UpTeeth','DnTeeth','UpTeeth_Back','DnTeeth_Back']
#        self.otherNum = 5
#        self.grp = 'Tooth_Control_GRP'
#        BuildMainController.done(self)


class BuildToothController(BuildMainController):
    def __init__(self):
        self.grp = 'Tooth_Control_GRP'
        self.ctrlName = 'Tooth_Joint'
        
        
    def createJoint(self):
        rig.select(cl = True)
        DnPos = (0.0, 15.314, 1.572)
        DnJnt = rig.joint(p = DnPos,n = 'Dn'+self.ctrlName)
        self.connectAddAttr(DnJnt,'CTRLJoint')#连接属性
        rig.select(cl = True)
        UpPos = (0.0, 15.619, 1.572)
        UpJnt = rig.joint(p = UpPos,n = 'Up'+self.ctrlName)
        self.connectAddAttr(UpJnt,'CTRLJoint')#连接属性
        
    def createEmptyGrp(self):#生成空组
        if rig.objExists(self.grp):
            self.grpName = self.grp
        else:
            self.grpName = rig.group(empty = True,n = self.grp)       
        
        
    def connectAddAttr(self,AddObj,Attr):#增加并连接属性
        rig.addAttr(AddObj,at = 'long',ln = Attr)
        if not rig.attributeQuery(Attr,node = self.grpName,ex = True):
            rig.addAttr(self.grpName,at = 'long',ln = Attr)
        rig.connectAttr(self.grpName+'.'+Attr,AddObj+'.'+Attr)  
        
    def Groups(self):#整理层级
        CTRLJoints = rig.listConnections(self.grpName+'.CTRLJoint',s = False, d = True)
        CTRLJointGRP = rig.group(CTRLJoints, n = self.grpName+'_CTRLJoint')
        rig.parent(CTRLJointGRP,self.grpName)
#        CTRLJointGRP = rig.group(self.name+'_0Joint', n = self.grpName+'_CTRLJoint')
#        rig.parent(CTRLJointGRP,self.grpName)
            
    def done(self):
        self.createEmptyGrp()#生成空组
        self.createJoint()
        self.Groups()#整理层级

class BuildjointsController():
    def __init__(self):
        self.grp = 'Head_Control_GRP'
        self.scale = 1.0
        self.dictData = {
                        'Lf_Brow_Joint':(0.52970747460000012, 16.978361509999996, 1.5675650590000001),\
                        'Rt_Brow_Joint':(-0.52970749139999995, 16.97836113, 1.5675650840000004),\
                        'Lf_Cheek_Joint':(0.57040166340000009, 15.851219259999999, 1.8094772380000006),\
                        'Rt_Cheek_Joint':(-0.57040166850000007, 15.851219179999998, 1.8094772099999994),\
                        'Lf_CornerLip_Joint':(0.29424550690000006, 15.489295039999998, 1.853963122000001),\
                        'Rt_CornerLip_Joint':(-0.29424551130000004, 15.489295009999998, 1.8539631370000014),\
                        'Head_Tip_Joint':(-1.8936342055413511e-15, 18.176273285631765, 0.42382953477964685),\
                        'Nose_Tip_Joint':(3.7252772616798423e-06, 16.13139252135085, 2.1118795985890495),\
                        'Up_Lip_Joint':(-0.00032652201300000004, 15.536712559999996, 2.0012264590000006),\
                        'Dn_Lip_Joint':(0.0032144452140000015, 15.430541549999996, 1.9787172190000013),\
                        'Mouth_Tip_Joint':(1.1008416803683136e-11, 15.485612458286568, 1.9737175928710387),\
                        'Nose_Joint':(3.7252775300860405e-06, 16.115815162658528, 1.8522569537162907),\
                        'Jaw_Joint':(1.1026239024313745e-11, 15.48215450695643, 0.47058776821107384),\
                        'Jaw_Swivle_Joint':(1.9753607085891104e-14, 16.061475636433023, 0.31298615302869193),\
                        'Head_Joint':(5.7478743986649761e-11, 15.119725877731762, 0.44171690152889548),\
                        'JawMain_Joint':(5.7478743986649761e-11, 14.967464561347001, 2.0707833113127512)
                        }
        
    def createJoints(self):#生成骨骼
        for jnt in self.dictData:
            rig.select(cl = True)
            jntName = rig.joint(p = self.dictData[jnt],n = jnt)
            self.connectAddAttr(jntName,'CTRLJoint')#连接属性
            
    #生成控制器        
    def buildController(self):
        size = [(0.1,0.1,0.1),(0.1,0.1,0.1),(0.1,0.1,0.1),(0.1,0.1,0.1),(0.1,0.1,0.1),(0.1,0.1,0.1),(0.1,0.1,0.1),(0.1,0.1,0.1),(0.1,0.1,0.1),(0.1,0.1,0.1),(0.1,0.1,0.1)]
        colors = [12,12,12,12,12,12,12,12,12,12,12]
        conJoint = [u'Lf_Brow_Joint', u'Rt_Brow_Joint', u'Lf_Cheek_Joint', u'Rt_Cheek_Joint', u'Lf_CornerLip_Joint', u'Rt_CornerLip_Joint', u'Up_Lip_Joint', u'Mouth_Tip_Joint', u'Dn_Lip_Joint', u'Nose_Joint','JawMain_Joint']
        #生成Macro控制器
        for i,jnt in enumerate(conJoint):
            pos = rig.xform(jnt,q = True,t = True,ws = True)
            controllers = CreateControler(15,[j*self.scale*0.6 for j in size[i]])
            controllers.signValue = 18290
            
            controllers.color = colors[i]    
            con = controllers.SK_b03(jnt.replace('_Joint','Macro_M'))
            rig.xform(con,t = pos,ws = True)
            
            self.connectAddAttr(con,'CTRLMacroCurve')#连接属性
            
        #生成blendShape控制器
        crossColor = [17 for i in range(11)]#cross控制器颜色
        colors = [13,13,13,13,13,13,13,13,13,13,17]#blendShape控制器颜色
        for i,jnt in enumerate(conJoint):
            pos = rig.xform(jnt,q = True,t = True,ws = True)#获得位置信息
            controllers = CreateControler(15,[j*self.scale for j in size[i]])
            controllers.signValue = 44390
            
            controllers.color = colors[i]             
            if 'JawMain_Joint' ==  jnt:
                con = controllers.SK_b01(jnt.replace('_Joint','_M'))
            else: 
                con = controllers.SK_b03(jnt.replace('_Joint','_M')) #blendShape控制器
            self.connectAddAttr(con,'CTRLBsCurve')#连接属性
            
            controllers.color =  crossColor[i]
            controllers.setObjScale([i*1.6 for i in controllers.curveSale])         
            conCross = controllers.SK_b16(jnt.replace('_Joint','Cross_M'))#cross控制器
            
            rig.xform(con,t = pos,ws = True)
            rig.xform(conCross,t = pos,ws = True)
            
            rig.parent(rig.listRelatives(conCross,s = True)[0], con, s = True, add = True)#parent形节点
            rig.delete(conCross)#删除cross控制器
         
         
        #生成jawSwivel控制器   
        controllers.setRelativesScale([0.3, 0.3, 0.3])
        jawSwivel = controllers.SK_b01('jawSwivel_M')
        rig.xform(jawSwivel,t = (0, 15.97, 2.485), ws = True)
        self.connectAddAttr(jawSwivel,'CTRLBsCurve')#连接属性  
        
        rig.hide('Mouth_TipMacro_MShape')
        #增加旋转blendShape属性
        rig.addAttr('JawMain_M', at = 'float', ln = 'limitMinrz', dv = -30,k = True)
        rig.addAttr('JawMain_M', at = 'float', ln = 'limitMaxrz', dv = 30,k = True)
        
        rig.addAttr('jawSwivel_M', at = 'float', ln = 'limitMinrz', dv = -30,k = True)
        rig.addAttr('jawSwivel_M', at = 'float', ln = 'limitMaxrz', dv = 30,k = True)
        
        rig.addAttr('Mouth_Tip_M', at = 'float', ln = 'limitMinrz', dv = -30,k = True)
        rig.addAttr('Mouth_Tip_M', at = 'float', ln = 'limitMaxrz', dv = 30,k = True)      
        
        rig.addAttr('Lf_Brow_M', at = 'float', ln = 'limitMinrz', dv = -30,k = True)
        rig.addAttr('Lf_Brow_M', at = 'float', ln = 'limitMaxrz', dv = 30,k = True)
        
        rig.addAttr('Rt_Brow_M', at = 'float', ln = 'limitMinrz', dv = -30,k = True)
        rig.addAttr('Rt_Brow_M', at = 'float', ln = 'limitMaxrz', dv = 30,k = True)    
        
        
                             
    def buildGRP(self):
        rig.parent(u'Head_Tip_Joint', u'Rt_Brow_Joint', u'Lf_Brow_Joint',u'Head_Joint')
        
        rig.parent(u'Nose_Tip_Joint',u'Nose_Joint')
        
        rig.parent(u'Nose_Joint', u'Lf_Cheek_Joint', u'Rt_Cheek_Joint', u'Up_Lip_Joint',u'Jaw_Swivle_Joint')

        rig.parent(u'Mouth_Tip_Joint', u'Rt_CornerLip_Joint', u'Lf_CornerLip_Joint', u'Dn_Lip_Joint',u'Jaw_Joint')
        
        rig.parent(u'Jaw_Joint',u'Jaw_Swivle_Joint')
        
        rig.parent(u'Jaw_Swivle_Joint',u'Head_Joint')
        
        rig.parent(u'JawMain_Joint',u'Jaw_Joint')

        
        CTRLJointGRP = rig.group('Head_Joint', n = self.grpName+'_CTRLJoint')
        rig.parent(CTRLJointGRP,self.grpName)
        
        CTRLBsCurves = rig.listConnections(self.grpName+'.CTRLBsCurve',s = False, d = True)
        CTRLMacroCurves = rig.listConnections(self.grpName+'.CTRLMacroCurve',s = False, d = True)
        
        CTRLBsCurveGRP = rig.group(CTRLBsCurves, n = self.grpName+'_CTRLBsCurve')
        CTRLMacroCurveGRP = rig.group(CTRLMacroCurves, n = self.grpName+'_CTRLMacroCurve')
        
        rig.parent(CTRLBsCurveGRP,CTRLMacroCurveGRP,self.grpName)
    def createEmptyGrp(self):#生成空组
        if rig.objExists(self.grp):
            self.grpName = self.grp
        else:
            self.grpName = rig.group(empty = True,n = self.grp)       
        
        
    def connectAddAttr(self,AddObj,Attr):#增加并连接属性
        rig.addAttr(AddObj,at = 'long',ln = Attr)
        if not rig.attributeQuery(Attr,node = self.grpName,ex = True):
            rig.addAttr(self.grpName,at = 'long',ln = Attr)
        rig.connectAttr(self.grpName+'.'+Attr,AddObj+'.'+Attr)  
        
    def done(self):
        self.createEmptyGrp()#生成空组
        self.createJoints()
        self.buildController()
        self.buildGRP()#整理层级
    
    
       