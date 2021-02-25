#-*- coding: utf-8 -*-
import maya.cmds as rig
from RIG.combine import SK_combinationFinal
from RIG.selectProject import SK_SelectProject

class AutoRigging():
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
        self.returnLayout = rig.columnLayout(w =100,h=650,columnAlign='center')
        rig.button(label = u'     导入模版     ',w=322 ,  c='SK_BodyJointPosition()')
        rig.separator(w = 322,h=15,style='in')
        rig.setParent(self.returnLayout)
        
        rig.intSliderGrp('fingerNumsField',field=True, label=u'手指个数:',minValue=0, maxValue=5, fieldMinValue=0, fieldMaxValue=100, value=5,columnAttach=[(1,'left',0),(2,'left',0),(3,'both',0)],columnWidth3 = (55,50,222))
        rig.intSliderGrp('toesNumsField', field=True, label=u'脚趾个数:',minValue=0, maxValue=5, fieldMinValue=0, fieldMaxValue=100, value=5,columnAttach=[(1,'left',0),(2,'left',0),(3,'both',0)],columnWidth3 = (55,50,222))
        rig.intSliderGrp('neckSegsField', field=True, label=u'脖子段数:',minValue=2, maxValue=5, fieldMinValue=2, fieldMaxValue=100, value=2,columnAttach=[(1,'left',0),(2,'left',0),(3,'both',0)],columnWidth3 = (55,50,222))
        rig.intSliderGrp('waistSegsField', field=True, label=u'腰部段数:',minValue=3, maxValue=10, fieldMinValue=4, fieldMaxValue=100, value=0,columnAttach=[(1,'left',0),(2,'left',0),(3,'both',0)],columnWidth3 = (55,50,222))
        rig.setParent(self.returnLayout)
        
        rig.separator(w = 322,h=15,style='in')
        
        rig.rowColumnLayout(numberOfColumns = 2,columnWidth=[(1, 161), (2,  161)],columnAttach=(2,'both',0) )
        rig.button(label=u' 刷新模版  ',w = 130,c='SK_refreshTemp()')
        rig.button(label=u' 镜像骨骼 ',w=130,c='orientAndMirrorJoint ()')
        rig.setParent(self.returnLayout)
    
        rig.separator(w = 322,h=15,style='in')
        
        rig.text(l = u'选择项目')#选择项目
        rig.radioCollection()
        rig.rowColumnLayout(nc = 3,columnWidth = [(1,100),(2,100),(3,100)])
        self.OrigenRB = rig.radioButton( label= u'初始版本',sl = 1)
        self.WoodliesRB = rig.radioButton( label='Woodlies' )
        self.MotionBuilder = rig.radioButton( label='MotionBuilder')
        self.WinxTVRB = rig.radioButton( label='WinxTV',vis = False)
        rig.setParent(self.returnLayout)
    
        rig.button(label=u' 生成身体设置  ',w = 322,h = 40, c = lambda x:self.buildSetup())
        
        rig.separator(w = 322,h=15,style='in')
        
        rig.columnLayout('MeshListLayout')
        rig.textScrollList('meshList',w=322,h=100,allowMultiSelection=True,deleteKeyCommand='SK_delMeshList() ')
        rig.setParent(self.returnLayout)
        
        rig.separator(w = 322,h=15,style='in')
        
        rig.rowColumnLayout(numberOfColumns = 2,columnWidth=[(1, 161), (2,  161)],columnAttach=(2,'both',0) )
        rig.button(label= u' 添加绑定模型 ',w = 130,c='SK_addMeshList()')
        rig.button(label= u' 对绑定模型蒙皮 ',w=130,c='SK_rigSkin()')
        rig.setParent(self.returnLayout)
        
        rig.separator(w = 322,h=15,style='in')
        rig.button(l= u'IK<-->FK',w=322,h=40,c = 'SK_IKFKSwitchCommand()')

        rig.separator(w = 322,h=15,style='in')
        rig.button(l= u'恢复初始POSE',w=322,h=40,c = 'SK_creatConDefaultPos(0)')
        
        #calimero
        rig.separator(w = 322,h=15,style='in')
        rig.button(l= u'calimeroFeetRigging',w=322,h=40,c = 'execfile(\'Z:/Resource/Groups/Production/Modeling/Rigging 2009 Development Plan/BodyRiggingTools/script/RIG/edo_calimeroFeetRiggingMainUI.py\')')
        
        rig.separator(w = 322,h=15,style='in')
        rig.button(l= u'设置文件控制器规范检查',w=322,h=40,c = 'execfile(\'Z:/Resource/Groups/Production/Modeling/Rigging 2009 Development Plan/BodyRiggingTools/script/RIG/tools/edo_checkRiggingFileUI.py\')')
        rig.separator(w = 322,h=15,style='in')
        rig.button(l= u'联合HUMAN IK使用',w=322,h=40,c = 'execfile(\'Z:\Resource\Groups\Production\Modeling\Rigging 2009 Development Plan\BodyRiggingTools\script\RIG\edo_motionBuilderControlGdcRigUI.py\');edo_motionBuilderControlGdcRigUI()')
        return self.returnLayout
    
    def buildSetup(self):
        SK_combinationFinal()
        SK_SelectProject(self.OrigenRB,self.WoodliesRB,self.WinxTVRB,self.MotionBuilder)#选择项目
