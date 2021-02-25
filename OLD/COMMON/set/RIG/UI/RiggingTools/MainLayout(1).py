#-*- coding: utf-8 -*-
import maya.cmds as rig
import headfile
bodyrigpath=headfile.__file__.replace('headfile.py','RIG/').replace('\\','/')

class RiggingTools():
    def __init__(self, parentLayout):
        self.parent = parentLayout
        self.returnLayout = ''
        self.createLayout()

    
    def createLayout(self):
        rig.setParent(self.parent)
        self.runLayout()
        rig.setParent(self.parent)
    
    def getLayout(self):
        return self.returnLayout      
    
    def runLayout(self):
        self.returnLayout = rig.columnLayout(w =300,h=355)
        
        #------------------------------------------------------------------------------ 
        modelFL = rig.frameLayout(w=327,label= u"模型工具", borderStyle='in' ,cll=True ,cl=True)
        rig.frameLayout(modelFL,edit=True,expandCommand="rig.frameLayout(\""+modelFL+"\" ,edit=True,h=200)")
        rig.frameLayout(modelFL,edit=True,collapseCommand="rig.frameLayout(\""+modelFL+"\" ,edit=True,h=20)")
        rig.columnLayout()
    
        rig.separator(w = 312,h=5,style='in')
        rig.button(label = u' 打开模型工具窗口 ' ,w=312 ,c = 'from RIG.tools.modelTools.modelUI import *; SK_modelUI()')
        
        rig.setParent(self.returnLayout)    
        #------------------------------------------------------------------------------ 
        simulationFL = rig.frameLayout(w=327,label= u"解算设置工具", borderStyle='in' ,cll=True ,cl=True)
        rig.frameLayout(simulationFL,edit=True,expandCommand="rig.frameLayout(\""+simulationFL+"\" ,edit=True,h=200)")
        rig.frameLayout(simulationFL,edit=True,collapseCommand="rig.frameLayout(\""+simulationFL+"\" ,edit=True,h=20)")
        rig.columnLayout()
    
        rig.separator(w = 312,h=5,style='in')
        rig.text(u'增加布料设置')
        rig.button(label = u' 打开布料设置窗口 ' ,w=312 ,c = 'from RIG.simulation.simulationUI import *; SK_simulationUI()')
        
        rig.separator(w = 312,h=5,style='in')
        rig.text(u'增加动力学IK设置')
        rig.button(label = u' 打开动力学IK设置设置窗口 ' ,w=312 ,c = 'from RIG.tools.dynamicCurve.DC_dynamicCurveUI import *; SK_dynamicIKUI()')
        
        rig.separator(w = 312,h=5,style='in')
        rig.text(u'导入导出头发Cache工具')
        rig.button(label = u' 打开头发Cache窗口 ' ,w=312 ,c = 'from RIG.tools.ImportExportHairCache.hairCacheUI import *; SK_HairCacheUI()')
           
        rig.setParent(self.returnLayout)
        #------------------------------------------------------------------------------ 
        fingerFL = rig.frameLayout(w=327,label= u"手指工具", borderStyle='in' ,cll=True ,cl=True)
        rig.frameLayout(fingerFL,edit=True,expandCommand="rig.frameLayout(\""+fingerFL+"\" ,edit=True,h=200)")
        rig.frameLayout(fingerFL,edit=True,collapseCommand="rig.frameLayout(\""+fingerFL+"\" ,edit=True,h=20)")
        rig.scrollLayout()
        fingerMoLayout = rig.columnLayout()
    
        rig.separator(w = 312,h=5,style='in')
        rig.text(u' 增加手指工具')
        rig.button(label = u' 打开窗口 ' ,w=312 ,c = 'SK_fingerAnimUI()')
        rig.setParent(self.returnLayout)
        #------------------------------------------------------------------------------ 
        resetFL = rig.frameLayout(w=327,label= u"恢复工具", borderStyle='in' ,cll=True ,cl=True)
        rig.frameLayout(resetFL,edit=True,expandCommand="rig.frameLayout(\""+resetFL+"\" ,edit=True,h=200)")
        rig.frameLayout(resetFL,edit=True,collapseCommand="rig.frameLayout(\""+resetFL+"\" ,edit=True,h=20)")
        rig.scrollLayout()
        resetMoLayout = rig.columnLayout()
        
        rig.text(u"重新恢复到模版文件")
        rig.button( label = u' 恢复 ' ,w=312 ,c = 'SK_restoreJoint(True)')
        rig.setParent(self.returnLayout)
        #------------------------------------------------------------------------------ 
        curveFL = rig.frameLayout(w=327,label= u"曲线工具", borderStyle='in' ,cll=True ,cl=True)
        rig.frameLayout(curveFL,edit=True,expandCommand="rig.frameLayout(\""+curveFL+"\" ,edit=True,h=200)")
        rig.frameLayout(curveFL,edit=True,collapseCommand="rig.frameLayout(\""+curveFL+"\" ,edit=True,h=20)")
        curveMoScr = rig.scrollLayout()
        rig.columnLayout()
    
        rig.text(u" 导入-导出控制器形状 ")
        rig.button(label = u' 打开窗口' ,w=312 ,c =  'from RIG.tools.importExputCurveShape import *\nSK_ImportExportUI().displayUI()')
        rig.separator(w = 312,h=15,style='in')
        
        rig.text(u"镜像控制器形状")
        rig.rowColumnLayout('curveMirrorLayout' , numberOfColumns=2,columnWidth = [(1,156),(2,156)],columnAttach = (2,'both',0))
        rig.button(l= u'左 ——>右',c='SK_MirrorCurveControlCmd(1)')
        rig.button(l= u'右 ——>左',c='SK_MirrorCurveControlCmd(0)')
        rig.separator(w = 312,h=15,style='in')
        rig.setParent( '..' )
        
        rig.text(u" 增加控制器到bodySet ")
        rig.button(label = u' 增加' ,w=312 ,c =  'from RIG.tools.addSet import *\nSK_AddToSet("bodySet",rig.ls(sl = True),True)')
        rig.separator(w = 312,h=15,style='in')
        rig.setParent(self.returnLayout) 
        #------------------------------------------------------------------------------ 
        extraFL = rig.frameLayout('extraFrame',w=327,label= u"附加工具", borderStyle='in' ,cll=True ,cl=True)
        rig.frameLayout(extraFL,edit=True,expandCommand="rig.frameLayout(\""+extraFL+"\" ,edit=True,h=300)")
        rig.frameLayout(extraFL,edit=True,collapseCommand="rig.frameLayout(\""+extraFL+"\" ,edit=True,h=20)")
        rig.columnLayout()
    
        #   选择骨骼增加控制器
        rig.text(u'为选择的骨骼添加控制器:')
        rig.button(label = u'确定' ,w=312 ,c =  'buildSKTOCON()')
        rig.separator(w = 312,h=15,style='in')

        rig.text(u'物体蒙皮状态下修改骨骼位置:')
        rig.button(label = u'重定义骨骼位置与轴向' ,w=312 ,c ='from RIG.tools.edo_rebuildBindPreMatrix import *\nedo_rebuildBindPreMatrix()')
        rig.separator(w = 312,h=15,style='in')
        
        rig.text(u'给skinCluster添加交互式权重:')
        rig.button(label = u'skinBindingUI' ,w=312 ,c ='from RIG.tools.edo_SkinBindingUI import *\nedo_SkinBindingUI()')
        rig.separator(w = 312,h=15,style='in')
        #   将软选择变形器转为CLUSTER
        rig.text(u'将softMod转为cluster:')
        rig.button(label = u'确定' ,w=312 ,c =  'softModToCluster()')
        rig.separator(w = 312,h=15,style='in')
            
        rig.text(u'重设簇的形节点位置:')
        rig.button(label = u'确定' ,w=312 ,c =  'resetClusterPos()')
        rig.separator(w = 312,h=15,style='in')

        rig.text(u'关闭场景中局部旋转轴向显示:')
        rig.button(label = u'确定' ,w=312 ,c =  'TL_CloseDisplayLocalAxis()')
        rig.separator(w = 312,h=15,style='in')
                    
        rig.text(u'创建线性IK:')
        rig.button(label = u'打开窗口' ,w=312 ,c =  'from RIG.tools.IKsplineTool.ikSpline import * \nIKSplineUI()')
        rig.setParent(self.returnLayout)
        #------------------------------------------------------------------------------ 
        skinFL = rig.frameLayout('skinTools',w=327,label= u"权重工具", borderStyle='in' ,cll=True ,cl=True)
        rig.frameLayout(skinFL,edit=True,expandCommand="rig.frameLayout(\""+skinFL+"\" ,edit=True,h=200)")
        rig.frameLayout(skinFL,edit=True,collapseCommand="rig.frameLayout(\""+skinFL+"\" ,edit=True,h=20)")
        rig.columnLayout()
    
        rig.separator(w = 312,h=5,style='in')
        rig.text(u' 将一个物体的权重拷给多个物体')
        rig.button(label = u' 确定 ' ,w = 312 ,c = 'from RIG.tools.copyWeigths import *\nSK_copyWeightToOtherObj()')
        
        rig.separator(w = 312,h=5,style='in')
        rig.text(u'检测是否有影响物体重叠')
        rig.button(label = u' 确定 ' ,w = 312 ,c = 'from RIG.tools.detectInfluence import *\ndetectInfluenceObj()')
        
        rig.separator(w = 312,h=5,style='in')
        rig.text(u'导入导出权重')
        rig.button(label = u' 打开工具窗口 ' ,w = 312 ,c = 'from RIG.tools.IOWeights.IOWeightsUI import *\nSK_IOWeightsUI()')
        
        rig.setParent(self.returnLayout)
        
        #------------------------------------------------------------------------------ 
        follicleFL = rig.frameLayout('follicleTools',w=327,label= u"毛囊设置工具", borderStyle='in' ,cll=True ,cl=True)
        rig.frameLayout(follicleFL,edit=True,expandCommand="rig.frameLayout(\""+follicleFL+"\" ,edit=True,h=200)")
        rig.frameLayout(follicleFL,edit=True,collapseCommand="rig.frameLayout(\""+follicleFL+"\" ,edit=True,h=20)")
        rig.columnLayout()
    
        rig.separator(w = 312,h=5,style='in')
        rig.text(u' 将一个物体的权重拷给多个物体')
        rig.button(label = u' 确定 ' ,w = 312 ,c = 'import RIG.tools.FollicleSetup.createFollicle as Ctemp; Ctemp.SK_CreateJontCTRL_UI()')
 
        rig.setParent(self.returnLayout)

        #-----------------------------------------------------------------------
        #   目标体工具
        blendShapeFL = rig.frameLayout('blendShapeTools',w=327,label= u"目标体工具", borderStyle='in' ,cll=True ,cl=True)
        rig.frameLayout(blendShapeFL,edit=True,expandCommand="rig.frameLayout(\""+blendShapeFL+"\" ,edit=True,h=200)")
        rig.frameLayout(blendShapeFL,edit=True,collapseCommand="rig.frameLayout(\""+blendShapeFL+"\" ,edit=True,h=20)")
        rig.columnLayout()

        rig.separator(w = 312,h=5,style='in')
        rig.text(u' zvradialblendshape ')
        rig.button(label = u' 【plugin】弧形运动目标体 ' ,w = 312 ,c ='execfile(bodyrigpath+\'tools/zvradialblendshape100Initialize.py\')')

        rig.setParent(self.returnLayout)
        return self.returnLayout
