# -*- coding: utf-8 -*-

'''
Created on 2015-4-12

@author: liangyu
'''

import maya.cmds as mc
import maya.mel as mel

class sk_zmProjectTools(object):
    def __init__(self):
        #namespace清理
        pass
    
    '''
            【UI篇】【FinalLayout前台工具】
    '''
    # finalLayout界面
    def sk_sceneFinalLayoutUI(self):
        from idmt.maya.py_common import sk_checkCommon
        reload(sk_checkCommon)
        from idmt.maya.py_common import sk_camMatrixScene
        reload(sk_camMatrixScene)
        
        # 窗口
        if mc.window ("sk_sceneFinalLayoutTools",ex=1):
            mc.deleteUI( "sk_sceneFinalLayoutTools", window=True )
        mc.window("sk_sceneFinalLayoutTools",title="FinalLayout Tools", widthHeight=(260, 375),menuBar=0)
        
        # 面板
        mc.scrollLayout( 'scrollLayout' )
        
        # finalLayout自动
        mc.frameLayout( label=u'FinalLayout Auto| 自动化FinalLayout', borderStyle='etchedOut' ,width = 250 )
        mc.rowLayout(numberOfColumns = 1,columnWidth2=(120, 250))
        mc.button(l=u'Alembic[ABC]完整版',bgc = [0.2,0.2,0.5],width = 250,height = 30,c ='from idmt.maya.norch import north_alembicCommon\nreload(north_alembicCommon)\nnorth_alembicCommon.GDCAlembicCommon().GDC_FinaloutABC(1,0,2,1)')       
        mc.setParent( '..' )
        mc.setParent( '..' )
        
        mc.frameLayout( label=u'FinalLayout bake| bake约束', borderStyle='etchedOut' ,width = 250 )
        mc.rowLayout(numberOfColumns = 1,columnWidth2=(120, 250))
        mc.button(l=u'约束BAKE',bgc = [0.2,0.8,0.2],width = 250,height = 22,c ='from idmt.maya.norch import north_alembicCommon\nreload(north_alembicCommon)\nnorth_alembicCommon.GDCAlembicCommon().sk_checkBakeConstraints()')       
        mc.setParent( '..' )
        
        # finalLayout分解导出
        mc.frameLayout( label=u'FinalLayout Export| cache导出信息', borderStyle='etchedOut' ,width = 250 )
        mc.rowLayout(numberOfColumns = 2,columnWidth2=( 120 ,80))
        
        mc.button(l=u'输出mesh—cache',bgc = [0.2,0.5,0.2],width = 125,height = 22,c ='from idmt.maya.norch import north_alembicCommon\nreload(north_alembicCommon)\nnorth_alembicCommon.GDCAlembicCommon().GDC_alembicExr(1,0,2,0,1)')       
        mc.button(l=u'输出curve—cache',bgc = [0.2,0.5,0.2],width = 125,height = 22,c='from idmt.maya.norch import north_alembicCommon\nreload(north_alembicCommon)\nnorth_alembicCommon.GDCAlembicCommon().GDC_shavealembicExr(1,2,0,1)')       
        mc.setParent( '..' )
        
        mc.frameLayout( label=u'FinalLayout Import| 【Fs】导入信息', borderStyle='etchedOut' ,width = 250 )
        mc.rowLayout(numberOfColumns = 2,columnWidth2=(120 ,80 ))
        mc.button(l=u'输入mesh—cache',bgc = [0.2,0.5,0.2],width = 125,height = 22,c ='from idmt.maya.norch import north_alembicCommon\nreload(north_alembicCommon)\nnorth_alembicCommon.GDCAlembicCommon().GDC_alembicImp(\"fs\",1,2,1)')       
        mc.button(l=u'输入curve—cache',bgc = [0.2,0.5,0.2],width = 125,height = 22,c ='from idmt.maya.norch import north_alembicCommon\nreload(north_alembicCommon)\nnorth_alembicCommon.GDCAlembicCommon().GDC_curvealembicImp(1,2,1)')       
        mc.setParent( '..' )
        # finalLayout分解导入
        mc.frameLayout( label=u'FinalLayout Import| 【Fs】链接信息', borderStyle='etchedOut' ,width = 250 )
        mc.rowLayout(numberOfColumns = 2,columnWidth2=(120 ,80 ))
        mc.button(l=u'mesh—cache链接',bgc = [0.2,0.5,0.2],width = 125,height = 22,c ='from idmt.maya.norch import north_alembicCommon\nreload(north_alembicCommon)\nnorth_alembicCommon.GDCAlembicCommon().LY_alembicMeshImp()')       
        mc.button(l=u'curve—cache链接',bgc = [0.2,0.5,0.2],width = 125,height = 22,c ='from idmt.maya.norch import north_alembicCommon\nreload(north_alembicCommon)\nnorth_alembicCommon.GDCAlembicCommon().LY_alembicCurveImp()')       
        mc.setParent( '..' )              
        mc.setParent( '..' )
                      
        # 参考材质历史清理
        mc.frameLayout( label=u'清理非参考的ABC CACHE节点', borderStyle='etchedOut' ,width = 250 )
        mc.rowLayout()
        mc.button(l=u'=====【Fs文件】开始清理ABC节点=====',bgc = [0.2,0.2,0.5],width = 250,height = 28,c ='from idmt.maya.norch import north_alembicCommon\nreload(north_alembicCommon)\nnorth_alembicCommon.GDCAlembicCommon().LY_deleteABCImp()')
        mc.setParent( '..' )
        mc.setParent( '..' )

        # 导入bake相机
        mc.frameLayout( label=u'参考bake相机', borderStyle='etchedOut' ,width = 250 )
        mc.rowLayout()
        mc.button(l=u'=====【Fs文件】参考bake相机=====',bgc = [0.2,0.2,0.2],width = 250,height = 28,c ='from idmt.maya.commonCore.core_mayaCommon import sk_hbExportCam\nreload(sk_hbExportCam)\nsk_hbExportCam.sk_hbExportCam().camServerReference(info=2)')
        mc.setParent( '..' )
        mc.setParent( '..' )  
              
        mc.showWindow( "sk_sceneFinalLayoutTools" )
    


 