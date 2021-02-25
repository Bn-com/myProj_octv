#-*- coding: utf-8 -*-
import maya.cmds as cmds
import headfile
AutoRigPath = headfile.__file__.replace('headfile.py','RIG/').replace('\\','/')
import sys
sys.path.append(AutoRigPath+'Projects/Calimero/Common_Sync/CAL_MAYA/2013/python/teamto')
from cal_check_gdc import *
execfile(AutoRigPath+'edo/general/edo_clearUpScene.py')

def edo_cl_checkRiggingFileUI():
    if cmds.window('cl_checkRiggingFileUI',ex=1):
        cmds.deleteUI('cl_checkRiggingFileUI')
    cmds.window('cl_checkRiggingFileUI',w=400,h=800)
    cmds.tabLayout('cl_checkRiggingFileUI_TAB',innerMarginWidth=5, innerMarginHeight=5)
    #
    cmds.columnLayout('checkRiggingFileUI_CL01',adj=1)
    cmds.text('===clear garbage will spend a lot of time - \nif your scene has a great amount of garbage nodes===')
    cmds.button('checkRiggingFileUI_check_groupId_button',l='CLEAR GARBAGE',c='edo_clearGarbageNodes()',bgc=[0.8,0.6,0.2],h=30)
    cmds.text('===============================================')
    cmds.frameLayout('checkRiggingFileUI_FR01',l=u'检查控制器',borderStyle='in',cll=1)
    cmds.button('checkRiggingFileUI_BT01',l=u'检查重名控制器',c='edo_cl_checkCtrlMoreThanOneNameCmd()')
    cmds.textScrollList('checkRiggingFileUI_TL01',ams=1,h=150,sc='edo_cl_checkRiggingFileUI_TL01_ccCmd()')
    cmds.popupMenu('checkRiggingFileUI_PPM01',b=3)
    cmds.menuItem('checkRiggingFileUI_MIT01',l=u'选择所有相同名称物体',c='edo_cl_selectSameNameControlCmd()')
    cmds.setParent('checkRiggingFileUI_CL01')
    cmds.frameLayout('checkRiggingFileUI_FR02',l=u'检查SET',borderStyle='in',cll=1)
    cmds.button('checkRiggingFileUI_BT02',l=u'检查没放入SET的控制器',c='edo_cl_checkCtrlSetCmd()')
    cmds.textScrollList('checkRiggingFileUI_TL02',ams=1,h=150,sc='edo_cl_checkRiggingFileUI_TL02_ccCmd()')
    cmds.popupMenu('checkRiggingFileUI_PPM02',b=3)
    cmds.menuItem('checkRiggingFileUI_MIT02',l=u'加入bodySet',c='edo_cl_addSelectToBodySetCmd()')
    cmds.menuItem('checkRiggingFileUI_MIT03',l=u'加入facialSet',c='edo_cl_addSelectToFacialSetCmd()')
    cmds.setParent('checkRiggingFileUI_CL01')
    cmds.frameLayout('checkRiggingFileUI_FR03',l=u'检查头文字 c_ ',borderStyle='in',cll=1)
    cmds.button('checkRiggingFileUI_checkC_button',l=u'检查控制器是否都具备头文字 c_',c='edo_cl_check_c()')
    cmds.columnLayout('checkRiggingFileUI_checkC_CL',adj=1)
    cmds.rowLayout('checkRiggingFileUI_checkC_RW',numberOfColumns=2,columnWidth2=[199,199])
    cmds.columnLayout('checkRiggingFileUI_checkC_RW_CL01',columnWidth=199,adj=1)
    cmds.text(l=u'以下列表中为没有加',bgc=[0.7,0.75,0.1])
    cmds.text(l=u'头文字 c_ 的控制器',bgc=[0.7,0.75,0.1])
    cmds.textScrollList('checkRiggingFileUI_checkC_RW_TL01',ams=1,w=199,h=150,sc='edo_cl_checkRiggingFileUI__checkC_RW_TL01_ccCmd()')
    cmds.popupMenu('checkRiggingFileUI_PPM03',b=3)
    cmds.menuItem('checkRiggingFileUI_MIT04',l=u'添加 头文字 c_',c='edo_cl_add_c_()')
    cmds.setParent('checkRiggingFileUI_checkC_RW')
    cmds.columnLayout('checkRiggingFileUI_checkC_RW_CL02',adj=1)
    cmds.text(l=u'以下列表中为不应该有',bgc=[0.7,0.75,0.7])
    cmds.text(l=u'头文字 c_ 的控制器',bgc=[0.7,0.75,0.7])
    cmds.textScrollList('checkRiggingFileUI_checkC_RW_TL02',ams=1,w=199,h=150,sc='edo_cl_checkRiggingFileUI__checkC_RW_TL02_ccCmd()')
    cmds.popupMenu('checkRiggingFileUI_PPM04',b=3)
    cmds.menuItem('checkRiggingFileUI_MIT05',l=u'删除 头文字 c_',c='edo_cl_remove_c_()')
    #
    cmds.setParent('checkRiggingFileUI_CL01')
    cmds.frameLayout('checkRiggingFileUI_FR04',l=u'检查控制器数值和key帧',borderStyle='in',cll=1)
    cmds.button('checkRiggingFileUI_BT03',l=u'检查是否存在Transform不是默认值以及被key帧的控制器',c='edo_cl_checkCtrlChannel()')
    cmds.columnLayout('checkRiggingFileUI_CL02',adj=1)
    cmds.rowLayout('checkRiggingFileUI_RW01',numberOfColumns=3,columnWidth3=[133,133,133])
    cmds.columnLayout('checkRiggingFileUI_CL03',adj=1)
    cmds.text(l=u'以下列表中为',bgc=[0.7,0.25,0.1])
    cmds.text(l=u'被key帧的控制器',bgc=[0.7,0.25,0.1])
    cmds.textScrollList('checkRiggingFileUI_TL03',ams=1,w=133,h=150,sc='edo_cl_checkRiggingFileUI_TL03_ccCmd()')
    cmds.setParent('checkRiggingFileUI_RW01')
    cmds.columnLayout('checkRiggingFileUI_CL04',adj=1)
    cmds.text(l=u'以下列表中为',bgc=[0.78,0.75,0.72])
    cmds.text(l=u'Transform有数值的控制器',bgc=[0.78,0.75,0.72])
    cmds.textScrollList('checkRiggingFileUI_TL04',ams=1,w=133,h=150,sc='edo_cl_checkRiggingFileUI_TL04_ccCmd()')
    cmds.setParent('checkRiggingFileUI_RW01')
    cmds.columnLayout('checkRiggingFileUI_CL05',adj=1)
    cmds.text(l=u'以下列表中为被隐藏的曲线',bgc=[0.28,0.2,0.12])
    cmds.text(l=u'请检查其中有误隐藏的控制器',bgc=[0.28,0.2,0.12])
    cmds.textScrollList('checkRiggingFileUI_TL05',ams=1,w=133,h=150,sc='edo_cl_checkRiggingFileUI_TL05_ccCmd()')
    #
    cmds.setParent('cl_checkRiggingFileUI_TAB')
    cmds.columnLayout('checkRiggingFileUI_TAB_CL01',adj=1)
    cmds.frameLayout('checkRiggingFileUI_TAB_CL01_FR00',l=u'检查模型',borderStyle='in',cll=1)
    cmds.button('checkRiggingFileUI_TAB_CL01_FR00_BT01',l=u'检查重名模型',c='edo_cl_check_moreThanOneNameMeshes()')
    cmds.textScrollList('checkRiggingFileUI_TAB_CL01_FR00_TL01',ams=1,h=150,sc='edo_cl_checkRiggingFileUI_TAB_CL01_FR00_TL01_ccCmd()')
    cmds.popupMenu('checkRiggingFileUI_PPM05',b=3)
    cmds.menuItem('checkRiggingFileUI_MIT06',l=u'选择所有相同名称模型',c='edo_cl_selectSameNameModelCmd()')
    #
    cmds.setParent('checkRiggingFileUI_TAB_CL01')
    cmds.frameLayout('checkRiggingFileUI_CHECKOTHERS_FL01',l=u'检查头文字 msh_ ',borderStyle='in',cll=1)
    cmds.button('checkRiggingFileUI_check_msh_button',l=u'检查所有模型是否都具有头文字 msh_',c='edo_cl_check_msh()')
    cmds.columnLayout('checkRiggingFileUI_CHECKOTHERS_FL01_CL',adj=1)
    cmds.rowLayout('checkRiggingFileUI_CHECKOTHERS_FL01_CL_RW',numberOfColumns=2,columnWidth2=[199,199])
    cmds.columnLayout('checkRiggingFileUI_CHECKOTHERS_FL01_CL_RW_CL01',columnWidth=199,adj=1)
    cmds.text(l=u'以下列表中为没有加',bgc=[0.7,0.75,0.1])
    cmds.text(l=u'头文字 msh_ 的模型',bgc=[0.7,0.75,0.1])
    cmds.textScrollList('checkRiggingFileUI_CHECKOTHERS_FL01_CL_RW_TL01',ams=1,w=199,h=150,sc='edo_cl_checkRiggingFileUI_CHECKOTHERS_FL01_CL_RW_TL01_ccCmd()')
    cmds.popupMenu('checkRiggingFileUI_PPM06',b=3)
    cmds.menuItem('checkRiggingFileUI_MIT07',l=u'添加 头文字 msh_',c='edo_cl_add_msh_()')
    cmds.setParent('checkRiggingFileUI_CHECKOTHERS_FL01_CL_RW')
    cmds.columnLayout('checkRiggingFileUI_CHECKOTHERS_FL01_CL_RW_CL02',adj=1)
    cmds.text(l=u'以下列表中为不应该有',bgc=[0.7,0.75,0.7])
    cmds.text(l=u'头文字 msh_ 的模型',bgc=[0.7,0.75,0.7])
    cmds.textScrollList('checkRiggingFileUI_CHECKOTHERS_FL01_CL_RW_TL02',ams=1,w=199,h=150,sc='edo_cl_checkRiggingFileUI_CHECKOTHERS_FL01_CL_RW_TL02_ccCmd()')
    cmds.popupMenu('checkRiggingFileUI_PPM07',b=3)
    cmds.menuItem('checkRiggingFileUI_MIT08',l=u'删除 头文字 msh_',c='edo_cl_remove_msh_()')
    #
    cmds.setParent('checkRiggingFileUI_TAB_CL01')
    cmds.frameLayout('checkRiggingFileUI_CHECKOTHERS_FL02',l=u'检查缩放有负值的模型',borderStyle='in',cll=1)
    cmds.button('checkRiggingFileUI_check_msh_scale_button',l=u'检查缩放有负值的模型',c='edo_cl_check_wrongScaleMeshes()')
    cmds.columnLayout('checkRiggingFileUI_CHECKOTHERS_FL02_CL',adj=1)
    cmds.textScrollList('checkRiggingFileUI_CHECKOTHERS_FL02_CL_RW_TL01',ams=1,w=199,h=150,sc='edo_cl_checkRiggingFileUI_CHECKOTHERS_FL02_CL_RW_TL01_ccCmd()')
    #
    cmds.setParent('checkRiggingFileUI_TAB_CL01')
    cmds.frameLayout('checkRiggingFileUI_CHECKOTHERS_FL03',l=u'检查没放入set的模型',borderStyle='in',cll=1)
    cmds.button('checkRiggingFileUI_check_msh_smoothSet_button',l=u'检查没放入set的模型',c='edo_cl_check_model_in_set()')
    cmds.columnLayout('checkRiggingFileUI_CHECKOTHERS_FL03_CL',adj=1)
    cmds.textScrollList('checkRiggingFileUI_CHECKOTHERS_FL03_CL_RW_TL01',ams=1,w=199,h=150,sc='edo_cl_checkRiggingFileUI_CHECKOTHERS_FL03_CL_RW_TL01_ccCmd()')
    #
    cmds.setParent('cl_checkRiggingFileUI_TAB')
    cmds.columnLayout('checkRiggingFileUI_TAB_CL02',adj=1)
    cmds.frameLayout('checkRiggingFileUI_TAB_CL02_FR00',l=u'检查模型上级带缩放的组和未知节点',borderStyle='in',cll=1)
    cmds.button('checkRiggingFileUI_check_negativeGroup_button',l=u'检查有负值缩放并且组下面有mesh节点的的group',c='edo_cl_check_negative_group()')
    #cmds.columnLayout('checkRiggingFileUI_CHECKOTHERS_FL04_CL',adj=1)
    cmds.textScrollList('checkRiggingFileUI_CHECKOTHERS_FL04_CL_RW_TL01',ams=1,w=199,h=150,sc='edo_cl_checkRiggingFileUI_CHECKOTHERS_FL04_CL_RW_TL01_ccCmd()')
    cmds.button('checkRiggingFileUI_check_unknownodes_button',l=u'检查未知节点',c='edo_cl_check_unknownode()')
    cmds.textScrollList('checkRiggingFileUI_CHECKOTHERS_FL05_CL_RW_TL01',ams=1,w=199,h=150,sc='edo_cl_checkRiggingFileUI_CHECKOTHERS_FL05_CL_RW_TL01_ccCmd()')
    cmds.popupMenu('checkRiggingFileUI_clearUnknowNodes_POPM',b=3)
    cmds.menuItem('checkRiggingFileUI_clearUnknowNodes_POPM_MI01',l=u'清除未知节点',c='edo_cl_clear_unknownode()')
    cmds.setParent('checkRiggingFileUI_TAB_CL02')
    #cmds.button('checkRiggingFileUI_check_topGroup_button',l=u'检查文件名和最上级角色组命名规范',c='')
    cmds.button('checkRiggingFileUI_check_topGroup_button',l='CHECK_SCRIPT_PUBLISH',c='edo_cl_check_script_publish()',bgc=[0.2,0.8,0.2],h=30)
    cmds.tabLayout('cl_checkRiggingFileUI_TAB', edit=True, tabLabel=(('checkRiggingFileUI_CL01','CHECK_CTRL'),('checkRiggingFileUI_TAB_CL01','CHECK_MODELS'),('checkRiggingFileUI_TAB_CL02','CHECK_OTHERS')))
    cmds.showWindow('cl_checkRiggingFileUI')
    cmds.window('cl_checkRiggingFileUI',e=1,w=400,h=800)

def edo_clearGarbageNodes():
    print 'clear scriptNodes'
    edo_deleteGDCriggingScriptNode()
    print 'clear useless group parts node, groupId node and polynormal node'
    edo_clearUpScenes()
    
def edo_deleteGDCriggingScriptNode():
    gdcsns=[]
    allnodes=cmds.ls(type='script')
    for n in allnodes:
        if 'GDC_BODYRIG2009_SCRIPTNODE' in n:
            if not n=='GDC_BODYRIG2009_SCRIPTNODE':
                gdcsns.append(n)
    print 'delete script:'
    print gdcsns
    if gdcsns:
        cmds.delete(gdcsns)

def edo_cl_checkCtrlMoreThanOneNameCmd():
    print 'check more than one name control'
    cmds.textScrollList('checkRiggingFileUI_TL01',e=1,ra=1)
    curveShapes=cmds.ls(type='nurbsCurve',ap=1,ni=1)
    curveTransforms=[]
    for c in curveShapes:
        t=cmds.listRelatives(c,p=1,pa=1)[0]
        if cmds.nodeType(t)=='transform' or cmds.nodeType(t)=='joint':
            if '|' in t:
                if not t in curveTransforms:
                    curveTransforms.append(t)
    print curveTransforms
    for ct in curveTransforms:
        shape=cmds.listRelatives(ct,s=1,ni=1,pa=1,type='nurbsCurve')[0]
        if edo_cl_getCurveIsHided(shape)=='hided':
            print ct+' is  hided,pass this nurbs curve..\n'
        else:
            cmds.textScrollList('checkRiggingFileUI_TL01',e=1,a=ct)
    
    
def edo_cl_checkRiggingFileUI_TL01_ccCmd():
    selText=cmds.textScrollList('checkRiggingFileUI_TL01',q=1,si=1)
    cmds.select(cl=1)
    cmds.select(selText)
    
def edo_cl_checkRiggingFileUI_TL02_ccCmd():
    selText=cmds.textScrollList('checkRiggingFileUI_TL02',q=1,si=1)
    cmds.select(cl=1)
    cmds.select(selText)
    
def edo_cl_checkRiggingFileUI_TL03_ccCmd():
    selText=cmds.textScrollList('checkRiggingFileUI_TL03',q=1,si=1)
    cmds.select(cl=1)
    cmds.select(selText)
    
def edo_cl_checkRiggingFileUI_TL04_ccCmd():
    selText=cmds.textScrollList('checkRiggingFileUI_TL04',q=1,si=1)
    cmds.select(cl=1)
    cmds.select(selText)
    
def edo_cl_checkRiggingFileUI_TL05_ccCmd():
    selText=cmds.textScrollList('checkRiggingFileUI_TL05',q=1,si=1)
    cmds.select(cl=1)
    cmds.select(selText)
#
def edo_cl_checkRiggingFileUI__checkC_RW_TL01_ccCmd():
    selText=cmds.textScrollList('checkRiggingFileUI_checkC_RW_TL01',q=1,si=1)
    cmds.select(cl=1)
    cmds.select(selText)
    
def edo_cl_checkRiggingFileUI__checkC_RW_TL02_ccCmd():
    selText=cmds.textScrollList('checkRiggingFileUI_checkC_RW_TL02',q=1,si=1)
    cmds.select(cl=1)
    cmds.select(selText)
    
def edo_cl_checkRiggingFileUI_TAB_CL01_FR00_TL01_ccCmd():
    selText=cmds.textScrollList('checkRiggingFileUI_TAB_CL01_FR00_TL01',q=1,si=1)
    cmds.select(cl=1)
    cmds.select(selText)
    
def edo_cl_checkRiggingFileUI_CHECKOTHERS_FL01_CL_RW_TL01_ccCmd():
    selText=cmds.textScrollList('checkRiggingFileUI_CHECKOTHERS_FL01_CL_RW_TL01',q=1,si=1)
    cmds.select(cl=1)
    cmds.select(selText)
    
def edo_cl_checkRiggingFileUI_CHECKOTHERS_FL01_CL_RW_TL02_ccCmd():
    selText=cmds.textScrollList('checkRiggingFileUI_CHECKOTHERS_FL01_CL_RW_TL02',q=1,si=1)
    cmds.select(cl=1)
    cmds.select(selText)
    
def edo_cl_checkRiggingFileUI_CHECKOTHERS_FL02_CL_RW_TL01_ccCmd():
    selText=cmds.textScrollList('checkRiggingFileUI_CHECKOTHERS_FL02_CL_RW_TL01',q=1,si=1)
    cmds.select(cl=1)
    cmds.select(selText)
    
def edo_cl_checkRiggingFileUI_CHECKOTHERS_FL03_CL_RW_TL01_ccCmd():
    selText=cmds.textScrollList('checkRiggingFileUI_CHECKOTHERS_FL03_CL_RW_TL01',q=1,si=1)
    cmds.select(cl=1)
    cmds.select(selText)
    
def edo_cl_checkRiggingFileUI_CHECKOTHERS_FL04_CL_RW_TL01_ccCmd():
    selText=cmds.textScrollList('checkRiggingFileUI_CHECKOTHERS_FL04_CL_RW_TL01',q=1,si=1)
    cmds.select(cl=1)
    cmds.select(selText)
    
def edo_cl_checkRiggingFileUI_CHECKOTHERS_FL05_CL_RW_TL01_ccCmd():
    selText=cmds.textScrollList('checkRiggingFileUI_CHECKOTHERS_FL05_CL_RW_TL01',q=1,si=1)
    cmds.select(cl=1)
    cmds.select(selText)

def edo_cl_selectSameNameControlCmd():
    selText=cmds.textScrollList('checkRiggingFileUI_TL01',q=1,si=1)
    cmds.select(cl=1)
    for s in selText:
        ts=s.split('|')
        ctn=ts[len(ts)-1]
        cmds.select('*'+ctn,add=1)
    allsel=cmds.ls(sl=1,ni=1,ap=1)
    cmds.textScrollList('checkRiggingFileUI_TL01',e=1,si=allsel)
    
def edo_cl_selectSameNameModelCmd():
    selText=cmds.textScrollList('checkRiggingFileUI_TAB_CL01_FR00_TL01',q=1,si=1)
    cmds.select(cl=1)
    for s in selText:
        ts=s.split('|')
        ctn=ts[len(ts)-1]
        cmds.select('*'+ctn,add=1)
    allsel=cmds.ls(sl=1,ni=1,ap=1)
    cmds.textScrollList('checkRiggingFileUI_TAB_CL01_FR00_TL01',e=1,si=allsel)
    
def edo_cl_checkCtrlSetCmd():
    cmds.select(all=1)
    grp=cmds.ls(sl=1,ni=1,type='transform')
    cmds.select(cl=1)
    if len(grp)>1:
        click=cmds.confirmDialog( title=u'设置文件还不够规范', message=u'设置文件场景最终只能有1个大组，现在又多个，请整理。',button=['yes,god it!','igron'],defaultButton='YES',cancelButton='YES', dismissString='YES')
        if click=='yes,god it!':
            return 0
    if not cmds.objExists('bodySet') or not cmds.objExists('facialSet'):
        click=cmds.confirmDialog( title=u'设置文件还不够规范', message=u'角色文件种必须有bodySet和facialSet，并分别将控制器分类放入其中,是否需要自动创建',button=['auto create,thanks','not at all,create it by my self!'],defaultButton='YES',cancelButton='YES', dismissString='YES')
        if click=='not at all,create it by my self!':
            return 0
        if click=='auto create,thanks':
            if not cmds.objExists('bodySet'):
                cmds.sets(n='bodySet')
            if not cmds.objExists('facialSet'):
                cmds.sets(n='facialSet')
    curveShapes=cmds.ls(type='nurbsCurve',ap=1,ni=1)
    curveTransforms=[]
    for c in curveShapes:
        #c='c_Lf_up_eyelids_CTRL_up|curveShape73''c_Lf_up_eyelids_CTRL_fourAxislf'[-16:]
        #print c
        t=cmds.listRelatives(c,p=1,pa=1)[0]
        if t[-6:] == '_frame' or t[-6:] == '_FRAME':
            continue
        if t[-8:]=='_CTRL_up'    or    t[-8:]=='_CTRL_dn'    or    t[-8:]=='_CTRL_lf'    or   t[-8:]=='_CTRL_rt'    or   t[-10:]=='_CTRL_lfup'    or   t[-10:]=='_CTRL_lfdn'   or   t[-10:]=='_CTRL_rtup'   or   t[-10:]=='_CTRL_rtdn'   or   t[-16:]=='_CTRL_fourAxisup'   or   t[-16:]=='_CTRL_fourAxisdn'   or   t[-16:]=='_CTRL_fourAxislf'   or   t[-16:]=='_CTRL_fourAxisrt'   or   t[-13:]=='_connectCurve':
            print t + 'is just for blendshape rig.It\'s not a controler'
            continue
        if cmds.nodeType(t)=='transform' or cmds.nodeType(t)=='joint':
            bset=cmds.listSets(o=t)
            if not bset==None:
                if not 'bodySet' in cmds.listSets(o=t) and not 'facialSet' in cmds.listSets(o=t):
                    if not t in curveTransforms:
                        curveTransforms.append(t)
            else:
                if not t in curveTransforms:
                    curveTransforms.append(t)
    #print curveTransforms
    cmds.textScrollList('checkRiggingFileUI_TL02',e=1,ra=1)
    for ct in curveTransforms:
        #ct='Lf_elbow_display'
        shape=cmds.listRelatives(ct,s=1,ni=1,pa=1,type='nurbsCurve')[0]
        if edo_cl_getCurveIsHided(shape)=='hided':
            print ct+' is  hided,pass this nurbs curve..\n'
        else:
            channelBoxAttr=cmds.listAttr(ct,k=1,se=1,u=1)
            if not channelBoxAttr==None:
                cmds.textScrollList('checkRiggingFileUI_TL02',e=1,a=ct)
    return 1
    
def edo_cl_addSelectToBodySetCmd():
    print 'add the select to bodySet now...\n'
    selText=cmds.textScrollList('checkRiggingFileUI_TL02',q=1,si=1)
    cmds.sets(selText,include='bodySet')
    
def edo_cl_addSelectToFacialSetCmd():
    print 'add the select to facialSet now...\n'
    selText=cmds.textScrollList('checkRiggingFileUI_TL02',q=1,si=1)
    cmds.sets(selText,include='facialSet')

def edo_cl_checkCtrlChannel():
    print 'check control value'
    bc=None
    fc=None
    if cmds.objExists('bodySet'):
        bc=cmds.sets('bodySet',q=True)
    if cmds.objExists('facialSet'):
        fc=cmds.sets('facialSet',q=True)
    tctrls=[]
    if not bc==None and fc==None:
        tctrls=bc
    if not fc==None and bc==None:
        tctrls=fc
    if not bc==None and not fc==None:
        tctrls=bc+fc
    if bc==None and fc==None:
        return 0
    tf=cmds.ls(tctrls,type='transform')
    jn=cmds.ls(tctrls,type='joint')
    ctrls=tf+jn
    keyctrl=[]
    transformCtrl=[]
    visCtrl=[]
    cmds.textScrollList('checkRiggingFileUI_TL03',e=1,ra=1)
    cmds.textScrollList('checkRiggingFileUI_TL04',e=1,ra=1)
    cmds.textScrollList('checkRiggingFileUI_TL05',e=1,ra=1)
    for c in ctrls:
        #c='c_eye_M'
        #print c
        #channelBoxAttr=cmds.listAttr(c,k=1,se=1,u=1)
        channelBoxAttr=[]
        channelBoxAttrs=['translateX','translateY','translateZ', 'rotateX', 'rotateY', 'rotateZ', 'scaleX', 'scaleY', 'scaleZ']
        for a in channelBoxAttrs:
            #a=channelBoxAttr[0]
            if not cmds.getAttr(c+'.'+a,l=1):
                channelBoxAttr.append(a)
        vis=None
        shape=cmds.listRelatives(c,s=1,ni=1,pa=1,type='nurbsCurve')[0]
        if edo_cl_getCurveIsHided(shape)=='hided':
            vis=True
        else:
            vis=False
        if not channelBoxAttr==None:
            for a in channelBoxAttr:
                #a='translateY'
                #print c+'.'+a
                inputNode=cmds.listConnections(c+'.'+a,s=1,d=0)
                if not inputNode==None and not c in keyctrl:
                    if 'animCurveT' in cmds.nodeType(inputNode):
                        keyctrl.append(c)
                        cmds.textScrollList('checkRiggingFileUI_TL03',e=1,a=c)
                value=int((cmds.getAttr(c+'.'+a)+0.0005)*1000)
                if inputNode==None and not c in transformCtrl:
                    if vis==False:
                        if a=='translateX' and not value==0:
                            transformCtrl.append(c)
                            cmds.textScrollList('checkRiggingFileUI_TL04',e=1,a=c)
                        if a=='translateY' and not value==0:
                            transformCtrl.append(c)
                            cmds.textScrollList('checkRiggingFileUI_TL04',e=1,a=c)
                        if a=='translateZ' and not value==0:
                            transformCtrl.append(c)
                            cmds.textScrollList('checkRiggingFileUI_TL04',e=1,a=c)
                        if a=='rotateX' and not value==0:
                            transformCtrl.append(c)
                            cmds.textScrollList('checkRiggingFileUI_TL04',e=1,a=c)
                        if a=='rotateY' and not value==0:
                            transformCtrl.append(c)
                            cmds.textScrollList('checkRiggingFileUI_TL04',e=1,a=c)
                        if a=='rotateZ' and not value==0:
                            transformCtrl.append(c)