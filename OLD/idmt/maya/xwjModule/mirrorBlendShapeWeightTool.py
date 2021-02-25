import maya.cmds as mc
import maya.cmds as mc
from functools import partial
import pymel.core as pm
from pprint import pprint
#pprint(pm.ls())
from idmt.maya.xwjModule.commonModule import modelModule
from idmt.maya.xwjModule.commonModule import riggingModule
reload(modelModule)
reload(riggingModule)
modelIns=modelModule.modelModule()
rigIns=riggingModule.riggingModule()

class mirrorBlendShapeWeightTool():
    def creatUI(self):
        if mc.window('mirrorBlendShapeTool',ex=1):
            mc.deleteUI('mirrorBlendShapeTool')
        mc.window('mirrorBlendShapeTool')
        mc.formLayout('fl_main',numberOfDivisions=100)

        mc.textFieldButtonGrp('tfb_obj',cw3=[100,200,100],adj=2,l='blendshape object:',bl='<<<',bc=partial(self.getObj),ed=0)
        mc.textScrollList( 'tsl_Layer',numberOfRows=8, allowMultiSelection=True,
                                append=[],
                                showIndexedItem=4 )

        mc.text('tx_lable',l='Mirror across:')

        mc.optionMenu('om_mirrorPlane',w=100 )
        mc.menuItem( label='XY' ,p='om_mirrorPlane')
        mc.menuItem( label='ZY' ,p='om_mirrorPlane')


        mc.checkBox( 'cb_invers',label='inversion(- to +)' )




        mc.button('btn_mirror',h=50,l='mirror',c=partial(self.mirrorBlendShape))
        #column = mc.columnLayout()
        #mc.button()
        #mc.button()
        #mc.button()

        mc.formLayout( 'fl_main', edit=True,
        attachForm=[('tfb_obj','top',5),('tfb_obj','left',5),('tfb_obj','right',5)      ,('tsl_Layer','left',10)       ,('om_mirrorPlane','right',10)        ,('btn_mirror','bottom',5),('btn_mirror','left',10),('btn_mirror','right',10)         ,('tx_lable','right',35)       ,('cb_invers','right',5)     ],
        attachControl=[('tsl_Layer','top',5,'tfb_obj'),('tsl_Layer','bottom',5,'btn_mirror'),('tsl_Layer','right',10,'om_mirrorPlane')      ,('tx_lable','bottom',5,'om_mirrorPlane')         ,('cb_invers','top',5,'om_mirrorPlane')           ],
        attachPosition=[('om_mirrorPlane','top',0,40)]
         )

        mc.showWindow( 'mirrorBlendShapeTool' )



    def getObj(self):
        obj=''
        selectObj=mc.ls(sl=1,l=1)
        if selectObj:
            if len(selectObj)==1:
                obj=selectObj[0]
                mc.textFieldButtonGrp('tfb_obj',e=1,tx=obj)
            else:
                mc.confirmDialog(m='more than one obj',b='OK')
                mc.textScrollList('tsl_Layer',e=1,ra=1)
        else:
            mc.confirmDialog(m='no object',b='OK')
            mc.textScrollList('tsl_Layer',e=1,ra=1)
        if obj:
            relativeNode=mc.listHistory(obj,lv=1)
            #print relativeNode
            BSnodes=[]
            for oneNode in relativeNode:
                if mc.nodeType(oneNode)=="blendShape":
                    BSnodes.append(oneNode)
            #print BSnodes
            if BSnodes:
                if len(BSnodes)==1:
                    #print BSnodes[0]
                    txtList=[]
                    txtList.append(BSnodes[0])
                    target=mc.blendShape(BSnodes,q=1,t=1)
                    for one in target:
                        txtList.append(one)
                    #print txtList
                    mc.textScrollList('tsl_Layer',e=1,ra=1)
                    mc.textScrollList('tsl_Layer',e=1,append=txtList)
                else:
                    mc.textScrollList('tsl_Layer',e=1,ra=1)
                    mc.confirmDialog(m='more than one blendshape',b='OK')
            else:
                mc.textScrollList('tsl_Layer',e=1,ra=1)
                mc.confirmDialog(m='object no blendshape node',b='OK')



    def mirrorBlendShape(self,UI=''):
        tslList=mc.textScrollList('tsl_Layer',q=1,sii=1)
        plane=mc.optionMenu('om_mirrorPlane',q=1,v=1 )
        print tslList
        obj=mc.textFieldButtonGrp('tfb_obj',q=1,tx=1)
        shapes=mc.listRelatives(obj,c=1,shapes=1)
        orgShape=''
        for oneShape in shapes:
            orgShape=oneShape
        #print tslList
        for one in tslList:
            index=int(one)-1
            halfVertx=modelIns.getHalfVertex(obj,plane)
            mc.checkBox( 'cb_invers',q=1,v=1)
            sourceVertex=[]
            if mc.checkBox( 'cb_invers',q=1,v=1):
                sourceVertex=halfVertx[1]
            else:
                sourceVertex=halfVertx[0]
            #print len(halfVertx[0])
            for oneVertex in sourceVertex:
                print one
                targetVertx=modelIns.findMirrorVertex(oneVertex,plane=plane,org=1)[0]
                print '--'+targetVertx
                #print targetVertx
                rigIns.copyBlendShapeWeight(oneVertex,targetVertx,index)
        

    