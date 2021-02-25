#-*- coding: utf-8 -*-
import maya.cmds as rig
from RIG.face.faceTemp import FC_ControlPosition
from RIG.face.faceFinish import FC_FaceSetup
from RIG.face.projectsConfig import extraModify
from RIG.face.baseClass import SK_ConOrientation
from RIG.face.baseClass import SK_mirrorEyebrowBS
from RIG.face.baseClass import SK_mirrorRoateCons
from RIG.face.controlUI import faceCoustom
from RIG.face.controlUI import conWidge
import maya.mel as MEL
import math


class FaceUI(object):
    def DisPlay(self):
        faceUI = 'FACE_UI'
        if(rig.window(faceUI,ex = True)):
            rig.deleteUI(faceUI,window = True)
        else:
            rig.window(faceUI,t = 'FACE_RIG', s = True, tb = True)
            rig.columnLayout('mainLayout') 
            
            tabs = rig.tabLayout(innerMarginWidth=5,innerMarginHeight=5)
            child1 = rig.columnLayout(columnAlign='center')
               
            rig.rowColumnLayout(nc = 5,columnWidth = [(1,60),(2,60),(3,60),(4,60),(5,60)])
            self.eyeCB = rig.checkBox(l = u'眼睛',v = True,changeCommand = lambda i:self.eye())
            self.tongueCB = rig.checkBox(l = u'舌头',v = True,changeCommand = lambda i:self.tongue())
            self.faceCB = rig.checkBox(l = u'面板',v = False)
            self.eyebrowCB = rig.checkBox(l = u'眉毛',v = True,changeCommand = lambda i:self.eyebrow())
            self.toothCB = rig.checkBox(l = u'牙床',v = True,changeCommand = lambda i:self.tooth())
            rig.setParent('..')
            
            importBT = rig.button(l = u'导入模版',w = 300,c = 'FC_importTemp()',bgc = (0.84,0.32,0.895))
            rig.separator(w = 300)
            rig.separator(w = 300)   
            
            rig.text(u'头部模型:') 
            rig.rowColumnLayout(nc = 2,columnWidth = [(1,150),(2,150)])
            rig.button(l = u'载入头部模型',w = 150,c = 'FC_loadHead()')
            rig.button(l = u'载入蒙皮头部模型',w = 150,c = 'FC_loadSkinHead()')
            rig.setParent('..')
            rig.rowColumnLayout(nc = 2,columnWidth = [(1,150),(2,150)])
            self.headTF = rig.textField(w = 150,enable = False)
            self.skinHeadTF = rig.textField(w = 150,enable = False)
            rig.setParent('..')
            
            rig.text(u'眼睛模型:') 
            rig.rowColumnLayout(nc = 2,columnWidth = [(1,150),(2,150)])
            self.LfEyeBT = rig.button(l = u'载入左眼',w = 150,c = 'FC_loadLfEye()')
            self.RtEyeBT = rig.button(l = u'载入右眼',w = 150,c = 'FC_loadRtEye()')
            rig.setParent('..')
            rig.rowColumnLayout(nc = 2,columnWidth = [(1,150),(2,150)])
            self.loadLfEyeTF = rig.textField(w = 150,enable = False)
            self.loadRtEyeTF = rig.textField(w = 150,enable = False)
            rig.setParent('..')
            
            rig.text(u'牙床模型:') 
            rig.rowColumnLayout(nc = 2,columnWidth = [(1,150),(2,150)])
            self.LfToothBT = rig.button(l = u'载入上牙床',w = 150,c = 'FC_loadUpTooth()')
            self.RtToothBT = rig.button(l = u'载入下牙床',w = 150,c = 'FC_loadDnTooth()')
            rig.setParent('..')
            rig.rowColumnLayout(nc = 2,columnWidth = [(1,150),(2,150)])
            self.loadUpToothTF = rig.textField(w = 150,enable = False)
            self.loadDnToothTF = rig.textField(w = 150,enable = False)
            rig.setParent('..')

            rig.text(u'眉毛模型:') 
            rig.rowColumnLayout(nc = 2,columnWidth = [(1,150),(2,150)])
            self.LfEyebrowBT = rig.button(l = u'载入左边眉毛',w = 150,c = 'FC_loadLfEyebrow()')
            self.RtEyebrowBT = rig.button(l = u'载入右边眉毛',w = 150,c = 'FC_loadRtEyebrow()')
            rig.setParent('..')
            rig.rowColumnLayout(nc = 2,columnWidth = [(1,150),(2,150)])
            self.loadLfEyebrowTF = rig.textField(w = 150,enable = False)
            self.loadRtEyebrowTF = rig.textField(w = 150,enable = False)
            rig.setParent('..')
                        
            rig.text(u'舌头模型:') 
            self.tongueBT = rig.button(l = u'载入舌头',w = 300,c = 'FC_loadTongue()')
            self.loadTongueTF = rig.textField(w = 300,enable = False)  
            
            rig.text(u'blendShape控制器名称:') 
            self.bsFaceTF = rig.textField(w = 300,tx = 'A B C D E')  

            rig.separator(w = 300)
            rig.separator(w = 300)            
            rig.radioCollection()
            rig.text(u'选择项目:')
            rig.rowColumnLayout(nc = 3,columnWidth = [(1,100),(2,100),(3,100)])
            self.OrigenRB = rig.radioButton( label= u'初始版本',sl = 1)
            self.RainbowRidersRB = rig.radioButton( label='RainbowRiders' )
            self.WinxTVRB = rig.radioButton( label='WinxTV' )
            rig.setParent('..')
#            rig.rowColumnLayout(nc = 3,columnWidth = [(1,100),(2,100),(3,100)])
#            rig.radioButton( label= u'初始版本' )
#            rig.radioButton( label='WinxTV' )
#            rig.radioButton( label='RainbowRiders ' )
#            rig.setParent('..')
            
            rig.button(l = u'生成面部设置',w = 300,c = 'FC_doneSetup()',bgc = (0.84,0.32,0.895))
            
            rig.separator(w = 300)
            rig.separator(w = 300)
            
            rig.text(u'调整控制器位置:') 
            rig.rowColumnLayout(nc = 3,columnWidth = [(1,100),(2,100),(3,100)])
            rig.button(l = u'生成定位Locator',w = 100,c = 'FC_selcetController()')
            rig.button(l = u'完成调整',w = 100,c = 'FC_finshJust()')
            rig.button(l = u'完成调整并对称',w = 100,c = 'FC_finshJust(True)')
            rig.setParent('..')

            rig.separator(w = 300)
            rig.separator(w = 300)
                        
            rig.text(u'调整控制器旋转') 
            rig.rowColumnLayout(nc = 2,columnWidth = [(1,150),(2,150)])
            rig.button(l = u'完成调整',w = 150,c = 'FC_finshRotateJust()')
            rig.button(l = u'完成调整并对称',w = 150,c = 'FC_finshRotateJust(True)')
            rig.setParent('..')

            rig.separator(w = 300)
            rig.separator(w = 300)
            
            rig.text(u'将模型绑定到头部:') 
            self.AddBT = rig.button(l = u'增加',w = 300,c = 'FC_addNewObj()')
            
            rig.separator(w = 300)
            rig.separator(w = 300)
            
            rig.text(u'   ') 
            self.BlendShapeBT = rig.button(l = u'镜像眉毛BlendShape',w = 300,c = 'FC_MirrorEyebrowBS()')
            rig.setParent('..')
            
            child2 = rig.columnLayout(columnAlign='center')
            
            rig.button(l = u'导入BlendShape面板',w = 300,c = 'FC_importFaceControl()')

            
            rig.text(u'增加单值控制器: ——————>输入控制器名称') 
            rig.rowColumnLayout(nc = 2,columnWidth = [(1,150),(2,150)])
            self.bsFaceOneTF = rig.textField(w = 150)
            rig.button(l = u'完成添加',w = 150,c = 'FC_AddOneSlide()')
            rig.setParent('..')
            
            rig.text(u'增加多值控制器: ——————>输入控制器名称') 
            rig.rowColumnLayout(nc = 2,columnWidth = [(1,150),(2,150)])
            self.bsFaceFourTF = rig.textField(w = 150)
            rig.button(l = u'完成添加',w = 150,c = 'FC_AddFourSlide()')
            rig.setParent('..')
            
            rig.tabLayout( tabs,edit=True,tabLabel=((child1,u'模版'),(child2,u'BlendShape面板')))
            self.setDefaultObj()
            rig.window(faceUI,e=True,wh=(329,690))                        
            rig.showWindow(faceUI)
            
    def eye(self):
        sign = rig.checkBox(self.eyeCB,q = True,v = True)
        if sign:
            rig.button(self.LfEyeBT,e = True,enable = True)
            rig.button(self.RtEyeBT,e = True,enable = True)
        else:
            rig.button(self.LfEyeBT,e = True,enable = False)
            rig.button(self.RtEyeBT,e = True,enable = False)
    
    def tongue(self):
        sign = rig.checkBox(self.tongueCB,q = True,v = True)
        if sign:
            rig.button(self.tongueBT,e = True,enable = True)
        else:
            rig.button(self.tongueBT,e = True,enable = False)
    
    def eyebrow(self):
        sign = rig.checkBox(self.eyebrowCB,q = True,v = True)
        if sign:
            rig.button(self.LfEyebrowBT,e = True,enable = True)
            rig.button(self.RtEyebrowBT,e = True,enable = True)
        else:
            rig.button(self.LfEyebrowBT,e = True,enable = False)
            rig.button(self.RtEyebrowBT,e = True,enable = False)
    
    def tooth(self):
        sign = rig.checkBox(self.toothCB,q = True,v = True)
        if sign:
            rig.button(self.LfToothBT,e = True,enable = True)
            rig.button(self.RtToothBT,e = True,enable = True)
        else:
            rig.button(self.LfToothBT,e = True,enable = False)
            rig.button(self.RtToothBT,e = True,enable = False)

    def setDefaultObj(self):
        if rig.objExists('Face_ConShape'):
            if FC_getObjName('headFOL'):
                rig.textField(self.headTF,e = True,tx = FC_getObjName('headFOL'))
            if FC_getObjName('headSKIN'):
                rig.textField(self.skinHeadTF,e = True,tx = FC_getObjName('headSKIN'))
            if FC_getObjName('eyeLeft'):
                rig.textField(self.loadLfEyeTF,e = True,tx = FC_getObjName('eyeLeft'))
            if FC_getObjName('eyeRight'):
                rig.textField(self.loadRtEyeTF,e = True,tx = FC_getObjName('eyeRight'))
            if FC_getObjName('upTooth'):
                rig.textField(self.loadUpToothTF,e = True,tx = FC_getObjName('upTooth'))
            if FC_getObjName('dnTooth'):
                rig.textField(self.loadDnToothTF,e = True,tx = FC_getObjName('dnTooth'))
            if FC_getObjName('eyebrowLeft'):
                rig.textField(self.loadLfEyebrowTF,e = True,tx = FC_getObjName('eyebrowLeft'))
            if FC_getObjName('eyebrowRight'):
                rig.textField(self.loadRtEyebrowTF,e = True,tx = FC_getObjName('eyebrowRight'))
            if FC_getObjName('tongue'):
                rig.textField(self.loadTongueTF,e = True,tx = FC_getObjName('tongue'))

                        
face = FaceUI()  
   
def OpenFaceUI():
    face.DisPlay() 
            
    
    
def FC_loadHead():
    slObj = rig.ls(sl = True)
    if slObj:
        TF = face.headTF
        rig.textField(TF,e = True,tx = slObj[0])
        FC_AddObjAttr('headFOL',slObj[0])

def FC_loadSkinHead():
    slObj = rig.ls(sl = True)
    if slObj:
        TF = face.skinHeadTF
        rig.textField(TF,e = True,tx = slObj[0])
        FC_AddObjAttr('headSKIN',slObj[0])

def FC_loadLfEye():
    slObj = rig.ls(sl = True)
    if slObj:
        TF = face.loadLfEyeTF
        rig.textField(TF,e = True,tx = slObj[0])
        FC_AddObjAttr('eyeLeft',slObj[0])

def FC_loadRtEye():
    slObj = rig.ls(sl = True)
    if slObj:
        TF = face.loadRtEyeTF
        rig.textField(TF,e = True,tx = slObj[0])
        FC_AddObjAttr('eyeRight',slObj[0])

def FC_loadUpTooth():
    slObj = rig.ls(sl = True)
    if slObj:
        TF = face.loadUpToothTF
        rig.textField(TF,e = True,tx = slObj[0])
        FC_AddObjAttr('upTooth',slObj[0])

def FC_loadDnTooth():
    slObj = rig.ls(sl = True)
    if slObj:
        TF = face.loadDnToothTF
        rig.textField(TF,e = True,tx = slObj[0])
        FC_AddObjAttr('dnTooth',slObj[0])

def FC_loadLfEyebrow():
    slObj = rig.ls(sl = True)
    if slObj:
        TF = face.loadLfEyebrowTF
        rig.textField(TF,e = True,tx = slObj[0])
        FC_AddObjAttr('eyebrowLeft',slObj[0])

def FC_loadRtEyebrow():
    slObj = rig.ls(sl = True)
    if slObj:
        TF = face.loadRtEyebrowTF
        rig.textField(TF,e = True,tx = slObj[0])
        FC_AddObjAttr('eyebrowRight',slObj[0])

def FC_loadTongue():
    slObj = rig.ls(sl = True)
    if slObj:
        TF = face.loadTongueTF
        rig.textField(TF,e = True,tx = slObj[0])
        FC_AddObjAttr('tongue',slObj[0])
        
def FC_importTemp():
    eyeSign = rig.checkBox(face.eyeCB,q = True,v = True)
    tongueSign = rig.checkBox(face.tongueCB,q = True,v = True)
    faceSign = rig.checkBox(face.faceCB,q = True,v = True)
    eyebrowSign = rig.checkBox(face.eyebrowCB,q = True,v = True)
    toothSign = rig.checkBox(face.toothCB,q = True,v = True)   
    faceTemp = FC_ControlPosition(eyeSign,tongueSign,faceSign,eyebrowSign,toothSign,face)

def FC_doneSetup():
    eyeSign = rig.checkBox(face.eyeCB,q = True,v = True)
    tongueSign = rig.checkBox(face.tongueCB,q = True,v = True)
    faceSign = rig.checkBox(face.faceCB,q = True,v = True)
    eyebrowSign = rig.checkBox(face.eyebrowCB,q = True,v = True)
    toothSign = rig.checkBox(face.toothCB,q = True,v = True)  
    FaceDone = FC_FaceSetup(eyeSign,tongueSign,faceSign,eyebrowSign,toothSign,face)
    
    extraModify(face) 
    
def FC_importFaceControl():
    faceCon = faceCoustom()
    faceGrp = faceCon.merging()
    con = rig.group(faceGrp,n = 'Face_ALL_M_CON_GRP')
    rig.xform(con,ro = (-90,-180,0),wd = True)
    rig.xform(con,t = (-1.538,0,-4.267),wd = True)    
    
def FC_selcetController():
    slObj = rig.ls(sl = True)
    if slObj:
       for obj in slObj:
           pos = rig.xform(obj,q = True,t = True,ws = True)
           Loc = rig.spaceLocator(n = obj+'_Position_Face_LOC')
           rig.xform(Loc,t = pos,ws = True)
           
def FC_finshJust(sign = False):
    slObj = rig.ls('*_Position_Face_LOC')
    if slObj:
       if sign:
           RtLocs = [loc.replace('Lf_','Rt_')for loc in slObj]
           for loc in RtLocs:
               rig.spaceLocator(n = loc)
               pos = rig.xform(loc.replace('Rt_','Lf_'),q = True,t = True,ws = True)
               pos[0] = pos[0]*-1
               rig.xform(loc,t = pos,ws = True)
           slObj.extend(RtLocs)
               
       for obj in slObj:
           FOLShape = obj.replace('_M_Position_Face_LOC','_P_FOLShape')
           MeshShape = rig.listConnections(FOLShape+'.inputWorldMatrix',s = True,d = False,type = 'mesh',sh = True)[0]
           faceCLM = rig.listConnections(MeshShape,s = False,d = True,type = 'closestPointOnMesh')[0]
           pos = rig.xform(obj,q = True,t = True,ws = True)
           rig.setAttr(faceCLM+'.inPositionX',pos[0])
           rig.setAttr(faceCLM+'.inPositionY',pos[1])
           rig.setAttr(faceCLM+'.inPositionZ',pos[2])           
           U = rig.getAttr(faceCLM+'.result.parameterU')
           V = rig.getAttr(faceCLM+'.result.parameterV') 
           rig.setAttr(FOLShape+'.parameterU',U)    
           rig.setAttr(FOLShape+'.parameterV',V)
           rig.delete(obj)
           
           MorrirGrp = obj.replace('_Position_Face_LOC','_Mirror_GRP')
           RX = MorrirGrp+'.rx'
           RY = MorrirGrp+'.ry'
           RZ = MorrirGrp+'.rz'
           DRX = rig.listConnections(RX,s = True,d = False,p = True)
           DRY = rig.listConnections(RY,s = True,d = False,p = True)
           DRZ = rig.listConnections(RZ,s = True,d = False,p = True)
           if DRX:
               rig.disconnectAttr(DRX[0],RX)
               rig.disconnectAttr(DRY[0],RY)
               rig.disconnectAttr(DRZ[0],RZ)
           SK_ConOrientation(obj.replace('_Position_Face_LOC',''))
           if DRX:
               OCT = obj.replace('_Position_Face_LOC','_OCT')
               ro = rig.xform(MorrirGrp,q = True,ro = True,wd = True)
               WsRo = rig.xform(MorrirGrp,q = True,ro = True,ws = True)
               rig.setAttr(MorrirGrp+'.X',ro[0])
               rig.setAttr(MorrirGrp+'.Y',ro[1])
               rig.setAttr(MorrirGrp+'.Z',ro[2])               
               rig.connectAttr(DRX[0],RX)
               rig.connectAttr(DRY[0],RY)
               rig.connectAttr(DRZ[0],RZ)
               rig.setAttr(OCT+'.offsetX',WsRo[0])
               rig.setAttr(OCT+'.offsetY',WsRo[1])
               rig.setAttr(OCT+'.offsetZ',WsRo[2])
           
def FC_addNewObj():
    slObj = rig.ls(sl = True)
    if slObj:
        for obj in slObj:
            newObj = rig.duplicate(obj,rr = True,n = obj+'_Skin_Mesh')[0]
            rig.blendShape(obj,newObj,w = (0,1),n = obj+'_Mesh_BS')
            
            JNTS = [jnt+'_JNT' for jnt in rig.listConnections('Face_Scale_Grp.signA',s = False,d = True)]
            SkinClus = rig.skinCluster(JNTS,newObj,n = obj+'_BlendShape_SKIN')[0]
            infs = rig.skinCluster(SkinClus,q = True,inf = True)
            for i,inf in enumerate(infs):
                MirrorGRP = inf.replace('_M_JNT','_M_Mirror_GRP')
                rig.connectAttr(MirrorGRP+'.worldInverseMatrix[0]',SkinClus+'.bindPreMatrix['+str(i)+']')
#           重新命名眼睫毛名字 
            ModiObj = rig.rename(obj,obj+'_Skin')
            rig.rename(newObj,obj)
            rig.parent(ModiObj,'Face_Deformers_Grp')
            
def FC_finshRotateJust(sign = False):
    slObj = rig.ls(sl = True)
    if slObj:
       for obj in slObj:
           Ro = rig.xform(obj,q = True,ro = True,wd = True)
           SK_mirrorRoateCons(obj)
           if sign:
               RtObj = obj.replace('Lf_','Rt_')
               Ro = (Ro[0],Ro[1]*-1,Ro[2]*-1)
               print Ro
               rig.xform(RtObj,ro = Ro,wd = True)
               print RtObj
               SK_mirrorRoateCons(RtObj)

           
              
def FC_MirrorEyebrowBS():
    SK_mirrorEyebrowBS()    
    
    
def FC_AddOneSlide(conName = ''):
    TF = face.bsFaceOneTF
    
    if not conName:#如果没有给的参数
        conName = rig.textField(TF,q = True,tx = True)
        
    if conName:
        faceCon = faceCoustom()
        cons = conName.split(' ')
        faceCon.MainCon = 'Face_M_CON_GRP'
        pos = rig.xform(faceCon.MainCon,q = True,t = True,ws = True)
        addWidge = faceCon.addExtraExpress(cons)
        rig.move(pos[0],pos[1],pos[2],addWidge,rpr = True)
        rig.xform(addWidge,ro = (-90,180,0),wd = True)
        rig.delete(rig.listRelatives(addWidge,c = True)[0])
        rig.parent(addWidge,'Face_M')
    

def FC_AddFourSlide():
    TF = face.bsFaceFourTF
    conName = rig.textField(TF,q = True,tx = True)
    if conName:
        faceCon = faceCoustom()
        cons = conName.split(' ')
        faceCon.MainCon = 'Face_M_CON_GRP'
        pos = rig.xform(faceCon.MainCon,q = True,t = True,ws = True)
        for con in cons:
            faceCon.mouthData = ('Lf_'+con,'Rt_'+con,con)
            addWidge = faceCon.mouth()
            rig.move(pos[0],pos[1],pos[2],addWidge,rpr = True)
            rig.xform(addWidge,ro = (-90,180,0),wd = True)
            rig.parent(addWidge,'Face_M')    
            
def FC_getObjName(attr):
    if rig.attributeQuery( attr, node='Face_ConShape',ex = True):
        obj = rig.getAttr('Face_ConShape.'+attr)
        return obj
    else:
        return False
    
def FC_AddObjAttr(attr,inputSrc):
    if not rig.attributeQuery( attr, node='Face_ConShape',ex = True):
        rig.addAttr('Face_ConShape',dt = 'string',ln = attr)
    rig.setAttr('Face_ConShape.'+attr,inputSrc,type = "string")
    