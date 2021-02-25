# -*- coding: utf-8 -*-

'''
Created on 2014

GDC 检测上传工具【通用】

@author: hanhong
'''

import maya.cmds as mc
import maya.mel as mel

from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
reload(sk_infoConfig)

from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
reload(sk_infoConfig)

import idmt.pipeline.db
import os

from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
reload(sk_referenceConfig)

from idmt.maya.py_common import GDC_TransInfoProce

reload(GDC_TransInfoProce)

#GPUCache上传
#@author: hanhong
#Data：2015/9/16
#----------------------------------------------------------------------------------------------------------#
class GDC_checkin(object):
    def __init__(self):
        pass
#前期文件上传前检测面板【通用】
#@author: hanhong
#Data：2015/9/16
#----------------------------------------------------------------------------------------------------------#
    def gdc_checkToolsUI(self):
    # 窗口
        mel.eval('source \"mtCheckModel.mel\"')
        if mc.window('gdc_checkTools', exists=True):
            mc.deleteUI('gdc_checkTools')
        mc.window('gdc_checkTools', title=u'checkTools',
                  bgc=[0, 0, 0.0],width=350, height=350, sizeable=True)
         # 面板
        form = mc.formLayout()
        mc.frameLayout(label='', bgc=[0, 0, 0.0], borderStyle='in', cll=0,cl=0)
        mc.rowColumnLayout(numberOfColumns=2)
        collectionocc = mc.radioCollection()
        # 文件结构检测
        check01 = mc.checkBox('check01', label=u'文件结构检测', visible=1, v=1,
                             bgc=[0.13, 0.15, 0.25], height=30, width=250)
        mc.button(label=u'check', bgc=[
                  0, 0, 0.0], width=100, height=30, command='from idmt.maya.py_common import GDC_checkin\nreload(GDC_checkin)\nGDC_checkin.GDC_checkin().yd_checkGeo()')
        collection01 = mc.radioCollection()
        # 模型命名检测
        check01A = mc.checkBox('check01A', label=u'模型命名检测', visible=1, v=1,
                             bgc=[0.13, 0.15, 0.25], height=30, width=250)
        mc.button(label=u'check', bgc=[
                  0, 0, 0.0], width=100, height=30, command='from idmt.maya.py_common import GDC_checkin\nreload(GDC_checkin)\nGDC_checkin.GDC_checkin().yd_checkMeshName()')
        collection01 = mc.radioCollection()
        # 非法模型检测
        check02= mc.checkBox('check02',label=u'非法模型检测', visible=1, v=1,
                             bgc=[0.13, 0.15, 0.25], height=30, width=130)
        mc.button(label=u'check', bgc=[
                  0, 0, 0.0], width=110, height=30, command='from idmt.maya.py_common import GDC_checkin\nreload(GDC_checkin)\nGDC_checkin.GDC_checkin().gdc_geocheck()')

        collection02 = mc.radioCollection()
        # UV空间检测
        check03 = mc.checkBox('check03',label=u'模型UV空间检测', visible=1,
                             v=0, bgc=[0.13, 0.15, 0.25], height=30, width=130)
        mc.button(label=u'check', bgc=[
                  0, 0, 0.0], width=110, height=30, command='from idmt.maya.py_common import GDC_checkin\nreload(GDC_checkin)\nGDC_checkin.GDC_checkin().gdc_UVcheck(0)')

        collection03 = mc.radioCollection()

        # NO Freeze检测
        check04 = mc.checkBox('check04',label=u'no frezze检测', visible=1, v=1,
                             bgc=[0.13, 0.15, 0.25], height=30, width=130)
        mc.button(label=u'check', bgc=[
                  0, 0, 0.0], width=110, height=30, command='from idmt.maya.py_common import GDC_checkin\nreload(GDC_checkin)\nGDC_checkin.GDC_checkin().gdc_nofrezzeCheck()')
        collection04 = mc.radioCollection()
        # 面赋检测
        check05 = mc.checkBox('check05',label=u'面赋材质检测', visible=1, v=0,
                             bgc=[0.13, 0.15, 0.25], height=30, width=130)
        mc.button(label=u'check', bgc=[
                  0, 0, 0.0], width=110, height=30, command='from idmt.maya.py_common import GDC_checkin\nreload(GDC_checkin)\nGDC_checkin.GDC_checkin().GDC_faceAssignments()')
        collection05 = mc.radioCollection()
        # smoothSet检测
        check06 = mc.checkBox('check06',label=u'smoothSet检测', visible=1, v=1,
                             bgc=[0.13, 0.15, 0.25], height=30, width=130)
        mc.button(label=u'check', bgc=[
                  0, 0, 0.0], width=110, height=30, command='from idmt.maya.py_common import GDC_checkin\nreload(GDC_checkin)\nGDC_checkin.GDC_checkin().GDC_smoothCheck()')

        collectionid06 = mc.radioCollection()

        # 灯光检测
        check07 = mc.checkBox('check07',label=u'灯光检测', visible=1, v=1,
                             bgc=[0.13, 0.15, 0.25], height=30, width=130)
        mc.button(label=u'check', bgc=[
                  0, 0, 0.0], width=110, height=30, command='from idmt.maya.Hh_common import csl_checkCommon\nreload(csl_checkCommon)\ncsl_checkCommon.csl_checkTools().checkLightCP()')
        collection07 = mc.radioCollection()
        #  非法层检测
        check08 = mc.checkBox('check08',label=u'非法层检测', visible=1, v=1,
        bgc=[0.13, 0.15, 0.25], height=30, width=130)
        mc.button(label=u'check', bgc=[
                  0, 0, 0.0], width=110, height=30, command='from idmt.maya.py_common import GDC_checkin\nreload(GDC_checkin)\nGDC_checkin.GDC_checkin().gdc_LayerCheck()')
        collection08 = mc.radioCollection()
        #  检测 NODE
        check08A = mc.checkBox('check08A',label=u'客户不需要节点检测', visible=1, v=1,
        bgc=[0.13, 0.15, 0.25], height=30, width=130)
        mc.button(label=u'check', bgc=[
                  0, 0, 0.0], width=110, height=30, command='from idmt.maya.py_common import GDC_checkin\nreload(GDC_checkin)\nGDC_checkin.GDC_checkin().GDC_NodeCheck()')
        collection08 = mc.radioCollection()

        # 清理空组
        check09 = mc.checkBox('check09',label=u'清理空组(mo文件使用，设置文件慎用）', visible=1,
                             v=0, bgc=[0.13, 0.15, 0.25], height=30, width=130)
        mc.button(label=u'clear', bgc=[
                  0, 0, 0.0], width=110, height=30, command='from idmt.maya.py_common import GDC_checkin\nreload(GDC_checkin)\nGDC_checkin.GDC_checkin().GDC_nullCheck(d=1)')

        collection09 = mc.radioCollection()
        # 删除未知节点
        check10 = mc.checkBox('check10',label=u'清理未知节点', visible=1, v=1,
                             bgc=[0.13, 0.15, 0.25], height=30, width=130)
        mc.button(label=u'clear', bgc=[
                  0, 0, 0.0], width=150, height=30, command='from idmt.maya.py_common import GDC_checkin\nreload(GDC_checkin)\nGDC_checkin.GDC_checkin().gdc_unknownPluginRemove()\nGDC_checkin.GDC_checkin().gdc_unkonwDelete()')
        collectionid10 = mc.radioCollection()
        # 检测smooth 节点(nj17项目专用）
        check11 = mc.checkBox('check11',label=u'Subdivision', visible=1, v=1,
                             bgc=[0.13, 0.15, 0.25], height=30, width=130)
        mc.button(label=u'check', bgc=[
                  0, 0, 0.0], width=150, height=30, command='from idmt.maya.py_common import GDC_checkin\nreload(GDC_checkin)\nGDC_checkin.GDC_checkin().gdc_unknownPluginRemove()\nGDC_checkin.GDC_checkin().nj17_vsmothInfo()')
        collectionid10 = mc.radioCollection()
        check12 = mc.checkBox('check12',label=u'透明节点检测', visible=1, v=1,
                             bgc=[0.13, 0.15, 0.25], height=30, width=130)
        mc.button(label=u'check', bgc=[
                  0, 0, 0.0], width=150, height=30, command='from idmt.maya.py_common import GDC_TransInfoProce\nreload(GDC_TransInfoProce)\nGDC_TransInfoProce.GDC_TransInfoProce().gdc_TrShadeCheck()')
        collectionid10 = mc.radioCollection()
        mc.setParent( '..' )
        form = mc.formLayout()
        mc.rowColumnLayout(numberOfColumns=1)
        mc.button(
            label=u'【全自动】check', bgc=[0, 0, 0.0],width=400, height=40, command='from idmt.maya.py_common import GDC_checkin\nreload(GDC_checkin)\nGDC_checkin.GDC_checkin().gdc_AutoCheck()')
        # 渲染常用工具组
        mc.setParent( '..' )

        mc.showWindow('gdc_checkTools')

#----------------------------------------------------------------------------------------------------------#
#【通用】全自动检测
#@author: hanhong
#Data：2015/10/21
#----------------------------------------------------------------------------------------------------------#
    def gdc_AutoCheck(self):
        #检测内容
        check01=mc.checkBox('check01',q=1,v=1)
        check01A=mc.checkBox('check01A',q=1,v=1)
        check02=mc.checkBox('check02',q=1,v=1)
        check03=mc.checkBox('check03',q=1,v=1)
        check04=mc.checkBox('check04',q=1,v=1)
        check05=mc.checkBox('check05',q=1,v=1)
        check06=mc.checkBox('check06',q=1,v=1)
        check07=mc.checkBox('check07',q=1,v=1)
        check08=mc.checkBox('check08',q=1,v=1)
        check08A=mc.checkBox('check08A',q=1,v=1)
        check09=mc.checkBox('check09',q=1,v=1)
        check10=mc.checkBox('check10',q=1,v=1)
        check11=mc.checkBox('check11',q=1,v=1)
        check12=mc.checkBox('check12',q=1,v=1)
        # 文件结构检测
        if check01 == True :
            self.yd_checkGeo()
        # 文件结构检测
        if check01A == True :
            self.yd_checkMeshName()
        # 非法模型检测
        if check02 == True :
            self.gdc_geocheck()
        # UV空间检测
        if check03 == True :
            self.gdc_UVcheck(0)
        # no freeze检测
        if check04 == True :
            self.gdc_nofrezzeCheck()
        # 面赋材质检测
        if check05 == True :
            self.GDC_faceAssignments()
        # smoothSet检测
        if check06 == True :
            self.GDC_smoothCheck()
        # 灯光检测
        if check07 == True :
            from idmt.maya.Hh_common import csl_checkCommon
            reload(csl_checkCommon)
            csl_checkCommon.csl_checkTools().checkLightCP()
        # 非法层检测
        if check08 == True :
            self.gdc_LayerCheck()
        #  检测 NODE
        if check08A == True :
            self.GDC_NodeCheck()
        # 清理空组
        if check09 == True :
            self.GDC_nullCheck(d=1)
        # 删除未知节点
        if check10 == True :
            self.gdc_unknownPluginRemove()
            self.gdc_unkonwDelete()
        # 检测smooth节点（nj17项目专用）
        if check11 == True :
            self.nj17_vsmothInfo()
        if check12 == True :
            GDC_TransInfoProce.GDC_TransInfoProce().gdc_TrShadeCheck()
        return 0

#----------------------------------------------------------------------------------------------------------#
#【通用】上传gpucache
#@author: hanhong
#Data：2015/10/21
#----------------------------------------------------------------------------------------------------------#
    def GDC_alembicCheckin(self,server=1,sl=1,shotType=1,infotype='gpuCache'):
        serverpath=sk_infoConfig.sk_infoConfig().alembicServerPath(shotType)
        gpuCaches=[]
        if sl==0:
            gpuCaches=mc.ls(type=infotype,l=1)
        else:
            objs=mc.ls(sl=1,l=1)
            for obj in objs:
                if mc.listRelatives(obj,s=1,f=1) and mc.nodeType(mc.listRelatives(obj,s=1,f=1)[0])==infotype:
                    gpuCaches.append(mc.listRelatives(obj,s=1,f=1)[0])
        if gpuCaches:
            for gpu in gpuCaches:
                if mc.objExists(gpu+'.cacheFileName') and mc.getAttr(gpu+'.cacheFileName'):
                    cacheFilen=mc.getAttr(gpu+'.cacheFileName')
                    shortName=cacheFilen.split('/')[-1]

                    updateCacheCMD = 'zwSysFile "copy" ' + '"' + (cacheFilen) + '"' + ' ' + '"' + (serverpath + shortName) + '"' + ' true'
                    mel.eval(updateCacheCMD)
                    try:
                        mc.setAttr((gpu+'.cacheFileName'),(serverpath + shortName),type='string')
                    except:
                        pass
        print u'===[Updating Info To Server]===传输[%s]完毕==='%infotype
#----------------------------------------------------------------------------------------------------------#
#【通用】检测面赋材质
#@author: hanhong
#Data：2015/9/17

#----------------------------------------------------------------------------------------------------------#
    def GDC_faceAssignments(self):
        faceAss=[]
        meshs=[]
        SGS=mc.ls(type='shadingEngine')
        if SGS:
            for i in range(len(SGS)):
                members=mc.sets(SGS[i],q=1)
                if members:
                    for  j in range(len(members)):
                        if '.f[' in members[j]:
                            faceAss.append(members[j])
        if faceAss:
            for face in faceAss:
                mesh=face.split('.f[')[0]
                mesh=mc.ls(mesh,l=1)
                if mesh:
                    mesh=mesh[0]
                if mesh not in meshs and '|MODEL|' in mesh:
                    meshs.append(mesh)

        if meshs:
            mc.select(meshs)
            print u'=====================有面赋材质问题，请检查以下物体====================='
            print u'--------------------------------------------------------------'
            for k in range(len(meshs)):
                print (meshs[k])
            print u'--------------------------------------------------------------'+'/n'
            mc.error(u'有面赋材质，请检查文件')
        else:
            print u'\n\n已检测，文件中无面赋材质'
        return 0
#----------------------------------------------------------------------------------------------------------#
#【通用】检查并删除空组
#@author: hanhong
#Data：2015/9/17
#d==1，删除，d==0,只报错，不删除
#----------------------------------------------------------------------------------------------------------#
    def GDC_nullCheck(self,d=1):
        nuls=[]
        objs=mc.ls(tr=1,l=1)
        for obj in objs:
            chs=mc.listRelatives(obj,ad = 1,f=1)
            if chs:
                pass
            else:
                nuls.append(obj)
        if nuls:
            if d==1:
                print u'=====================开始删除空组节点=================='
                mc.delete(nuls)
                print u'=====================已删除空组节点=================='
            if d==0:
                print u'======有空组物体=============='
                mc.select(nuls)
                print u'======已选择空组节点，请处理========='
                mc.error(u'请处理已选择的空组节点')
        else:
            print u'=====================已检测，无空组================='
#----------------------------------------------------------------------------------------------------------#
#【通用】检测smoothset
#----------------------------------------------------------------------------------------------------------#
    def GDC_smoothCheck(self):
        smoothSet=[]
        if mc.objExists('smooth_2'):
            smoothSet= mc.sets('smooth_2',q=1)
        if smoothSet:
            pass
        elif mc.objExists('smooth_1'):
            smoothSet = mc.sets('smooth_1',q=1)
            if smoothSet:
                pass
            elif mc.objExists('smooth_0'):
                smoothSet = mc.sets('smooth_0',q=1)
                if smoothSet:
                    pass
                else:
                    mc.error(u'文件中没有设置smooth物体')
        print '\n\n'
        print u'smoothSet检测OK'
        return 0
#----------------------------------------------------------------------------------------------------------#
#【通用】检测显示层及渲染
#@author: hanhong
#Data：2015/9/24

#---------------------------------------------------
    def gdc_LayerCheck(self):
        info=mc.ls(type='displayLayer',l=1)
        if mc.objExists('defaultLayer'):
            info.remove('defaultLayer')
        else:
            mc.error(u'文件中有非法显示层，请修改文件')
        if mc.ls(info):
            mc.error(u'文件中有非法显示层，请修改文件')
        rinfo=mc.ls(type='renderLayer',l=1)
        if mc.objExists('defaultRenderLayer'):
            rinfo.remove('defaultRenderLayer')
        else:
            mc.error(u'文件中有非法渲染层，请修改文件')
        if mc.ls(rinfo):
            mc.error(u'文件中有非法渲染层，请修改文件')
        print u'\n\n 层检测OK'
        return 0

#----------------------------------------------------------------------------------------------------------#
#【通用】贴图路径
#@author: hanhong
#ass=1,YODA,Ninjago等带集数文件夹的项目，ass=0，其他项目
#---------------------------------------------------
    def gdc_imagePath(self,line='Pre',ass=1):
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        if line=='Pre':
            shotInfos= sk_infoConfig.sk_infoConfig().checkShotInfo()
            chatype=''
            if 'c' in shotInfos[1][0]:
                chatype='characters'
            if 'p' in shotInfos[1][0]:
                chatype='props'
            if 's' in shotInfos[1][0]:
                chatype='sets'
            if ass==1:
                asset = idmt.pipeline.db.GetAssetByFilename(shotInfos[0]+ '_'+shotInfos[1] +"_h_ms_anim"+ '.mb')
                if asset:
                    EP=asset.code
                    serverimagepath= serverPath+'sourceimages/'+chatype+'/'+EP+'/'+shotInfos[1]+'/'
                else:
                    serverimagepath= serverPath+'sourceimages/'+chatype+'/'+shotInfos[1]+'/'
            else:
                serverimagepath= serverPath+'sourceimages/'+chatype+'/'+shotInfos[1]+'/'
            temimagepath='D:/Info_Temp/temp/texScale/' + str(shotInfos[1]) + '/'
            texpath=[temimagepath,serverimagepath]
        if line == 'Render':
            temimagepath=[]
            serverimagepath=[]
            refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
            refNamespace = refInfos[2][0]
            for ns in refNamespace:
                shotInfos=ns.split('_')
                if shotInfos[0] in ['csl','nj']:
                    chatype=''
                    if 'c' in shotInfos[1][0]:
                        chatype='characters'
                    if 'p' in shotInfos[1][0]:
                        chatype='props'
                    if 's' in shotInfos[1][0]:
                        chatype='sets'
                    serverimgpath=serverPath+'sourceimages/'+chatype+'/'+shotInfos[1]+'/'
                    temimgpath='D:/Info_Temp/texScale/' + str(shotInfos[1]) + '/'
                    temimagepath.append(temimgpath)
                    serverimagepath.append(serverimgpath)
                    texpath=[temimagepath,serverimagepath]
        return texpath
#----------------------------------------------------------------------------------------------------------#
#【通用】转换贴图格式
#@author: hanhong
#ass=1,YODA,Ninjago等带集数文件夹的项目，ass=0，其他项目；imgtype为转后的格式
#---------------------------------------------------
    def gdc_texCover(self,imgtype='.tif'):
        serverimagepath=self.gdc_imagePath('Pre',1)[1]
        temimagepath=self.gdc_imagePath('Pre',1)[0]
        mel.eval('source "zwImgcvt.mel"')
        mc.sysFile(temimagepath, makeDir=True)
        texs=mc.ls(tex=1,l=1)
        texN=[]
        imgs=[]
        if texs:
            for tex in texs:
                if mc.objExists(tex+'.fileTextureName'):
                    img=mc.getAttr(tex+'.fileTextureName')
                    imgN=serverimagepath+img.split('/')[-1].split('.')[0]+imgtype
                    if img !=imgN:
                        imgs.append(img)
                        texN.append(tex+'.fileTextureName')
        if imgs:
            for i in range(len(imgs)):
                shortName=imgs[i].split('/')[-1].split('.')[0]+imgtype
                cmd='zwImgcvt' +' "'+ imgs[i]+'" "'+(temimagepath + shortName)+'"'
                mel.eval(cmd)
                upCMD = 'zwSysFile "copy" ' + '"' + (temimagepath + shortName) + '"' + ' ' + '"' + (serverimagepath + shortName) + '"' + ' true'
                mel.eval(upCMD)
                try:
                    mc.setAttr(texN[i],(serverimagepath + shortName),type='string')
                except:
                    mc.error(u'==[%s]转换贴图未成功，缺少这个贴图==='%(serverimagepath + shortName))
        print u'===============贴图转tif已完成================='
        return 0

#----------------------------------------------------------------------------------------------------------#
#【通用】清理unknow节点
#@author: hanhong
#date：2015/9/29
#---------------------------------------------------
    def gdc_unkonwDelete(self):
        removeNodesFromPlugins = [
            'mtoa',
            'turtle'
        ]
        unknownNodes = mc.ls(type='unknown')
        for node in unknownNodes:
            if mc.objExists(node):  # Deleting some nodes might remove others also, so important to check
                plugin = mc.unknownNode(node, query=True, plugin=True)
                if plugin in removeNodesFromPlugins:
                    try:
                        mc.delete(node)
                        print 'deleted', node
                    except:
                        mc.error(u'==[%s]该unkonwn节点不能删除，请检查并修改后上传==='%node)
        print u'\n\n 已清理unknown节点'
        return 0

#----------------------------------------------------------------------------------------------------------#
#【通用】插件清理
#@author: hanhong
#date：2015/9/29
#---------------------------------------------------
    def gdc_unknownPluginRemove(self):
        pluginsToRemove = [
            'mtoa',
            'maxwell',
            'stereoCamera',
            'pdiMaya2x',
            'RenderMan_for_Maya',
            'LXFMLImport',
            'LEGO_EasyFlex',
            'afiLocatorNode',
            'BI'
        ]
        version = mc.about(v=1)
        unknownPlugins=''
        if version=='2016':
            unknownPlugins = mc.unknownPlugin(query=True, list=True)
        if unknownPlugins:
            for plugin in unknownPlugins:
                if plugin in pluginsToRemove:
                    mc.unknownPlugin(plugin, remove=True)
                    print 'Removed dependency on plugin:', plugin
                    print u'\n\n 已清理unknownPlugin'
        else:
            from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools
            reload(sk_sceneTools)
            sk_sceneTools.sk_sceneTools().checkDonotNodeClean()
        return 0
#----------------------------------------------------------------------------------------------------------#
#【通用】检测非法模型
#@author: hanhong
#date：2015/9/29
#---------------------------------------------------

    def gdc_geocheck(self):
        objs=mc.ls(tr=1,l=1)
        meshs=[]
        for obj in objs:
            if '|MODEL|' in obj:
                meshs.append(obj)
        mc.select(meshs)
        nonMani= mc.polyInfo(nonManifoldEdges=True)
        if nonMani:
            print u'\n\n有nonManifoldEdges，如下'
            print nonMani

            mc.select(nonMani)
            mc.error(u'\n\n 有nonManifoldEdges，请检查选择的物体')

        nonV=mc.polyInfo(nonManifoldVertices=True)
        if nonV:
            print u'\n\n有nonManifoldVertices，如下'
            print nonV
            mc.select(nonV)
            mc.error(u'\n\n 有nonManifoldVertices，请检查选择的物体')

        lamFace=mc.polyInfo(laminaFaces=True)
        if lamFace:
            print u'\n\n有laminaFaces，如下'
            print lamFace
            mc.select(lamFace)
            mc.error(u'\n\n 有laminaFaces，请检查选择的物体')

        print u'\n\n 已检测非法模型'

        return 0

#----------------------------------------------------------------------------------------------------------#
#【通用】检测uv在0-1范围外的物体
#@author: hanhong
#date：2015/10/15
# sl==1，物体为选择物体，sl==0，物体为文件中所有poly物体
#---------------------------------------------------

    def gdc_UVcheck(self,sl=0):
        info = sk_infoConfig.sk_infoConfig().checkShotInfo()
        fileFormat = sk_infoConfig.sk_infoConfig().checkProjectFileFormat(info[0])
        if sl==1:
            objs=mc.ls(sl=1,l=1)
        else:
            objs=[]
            meshs=mc.ls(tr=1,l=1)
            for mesh in meshs:
                if mc.listRelatives(mesh,s=1) and mc.nodeType(mc.listRelatives(mesh,s=1,f=1)[0])=='mesh' and '|MODEL|' in mesh:
                    objs.append(mesh)
        errors=[]
        errors02=[]
        if objs:
            for obj in objs:
                if mc.polyEvaluate(obj,uv=1) and not mc.objExists(obj+'.UV'):
                    try:
                        uvs=int(mc.polyEvaluate(obj,uv=1))-1
                        uv=obj+'.map[0:'+'%d'%uvs+']'
                        mc.select(uv)
                        maxmins=mc.polyEvaluate(boundingBoxComponent2d=1)
                        if maxmins[0][0]<0 or maxmins[0][1]>1 or maxmins[1][0]<0 or maxmins[1][1]>1:
                            errors.append(obj)
                    except:
                        errors02.append(obj)

        else:
            print u'文件内模型为空'
        mc.select(cl=1)
        if errors:
            print '\n\n'
            print u'下列物体UV超出了0-1范围，请检查'
            print errors
            mc.select(errors)
            print '\n\n'
            mc.error(u'\n\n 所选择物体UV超出了0-1范围，请检查')
        if errors02:
            print '\n\n'
            print u'下列物体为空组或者出现模型父子问题，请检查'
            print errors02
            mc.select(errors02)
            print '\n\n'
            mc.error(u'\n\n 所选择物体为空组或者出现模型父子问题，请检查')

        print u'\n\n 已检测UV'
        return 0
#----------------------------------------------------------------------------------------------------------#
#【通用】前期文件结构检测
#@author:韩虹
#data：2015/10/16
#---------------------------------------------------

    def gdc_checkstructure(self):
        errors = []
        mo = 0
        # 文件名检测，判断环节

        info = sk_infoConfig.sk_infoConfig().checkShotInfo()
        fileFormat = sk_infoConfig.sk_infoConfig().checkProjectFileFormat(info[0])
        #加检rg环节
        second=[]
        if info[3]==('rg' +fileFormat):
            objs=mc.ls(tr=1,l=1)
            for obj in objs:
                if '|' in obj:
                    info=obj.split('|')
                    if len(info)==3:
                        second.append(obj.split('|')[-1])
            if info[0] != u'mi' and second !=['DEFORMERS', 'FX', 'MODEL', 'RIG']:
                print '\n\n'
                mc.error(u'该设置文件，第二大组，需要是[“DEFORMERS”, “FX”, “MODEL”, “RIG”]，请检查')
            elif info[0] == u'mi' and second !=['DEFORMERS', 'FX', 'MODEL', 'RIG',u'FUR_GRP',u'SHAVE']:
                print '\n\n'
                mc.error(u'该设置文件，第二大组，需要是[“DEFORMERS”, “FX”, “MODEL”, “RIG”,u"FUR_GRP"]，请检查')
        if info[1][0] in ['c','p','s'] and len(info) > 3:
            # 错误检测，根据阶段不同而不同

            if info[3] == ('mo' +fileFormat):
                mo = 1
            if mo==1:
                model=mc.ls('MODEL',tr=1,l=1)
                if len(model)==1 :
                    if model[0].split('|')[0]!='':
                        print '\n\n'
                        mc.error(u'该模型文件，MODEL没有在根目录，请检查')
                    grps=mc.listRelatives(model[0], c=1, type='transform', ad=1, f=1)
                    if grps:
                        for grp in grps:
                            if '|' in grp:
                                grpinfo=grp.split('|')
                                if len(grpinfo)>2 and  'MSH_all' not in grpinfo:
                                    mc.error(u'no MSH_all')
                    else:
                        print '\n\n'
                        mc.error(u'MODEL组是空组，请检查文件')
                elif len(model)==0:
                     print '\n\n'
                     mc.error(u'文件中没有MODEL组，请检查')
                else:
                     print '\n\n'
                     mc.error(u'文件中有多个MODEL组，请检查')
            else:
                info = sk_infoConfig.sk_infoConfig().checkShotInfo()
                grpup=''
                if info[1][0] =='c':
                    grpup='CHR'

                elif info[1][0] =='s':
                    grpup='SET'

                elif info[1][0]=='p'and info[0] not in [u'mi']:
                    grpup='Pro'
                elif info[1][0]=='p' and info[0] in [u'mi']:#====add by zhangben for minitiger properties group named :PROP  2016.3.14=======
                    grpup='PROP'
                grpups=mc.ls(grpup,tr=1,l=1)
                errors=[]
                if len(grpups)==1:
                    if grpups[0].split('|')[0]!='':
                        print '\n\n'
                        mc.error(u'文件[%s]没有在根目录，请检查'%grpup)
                    grps=mc.listRelatives(grpups[0], c=1, type='transform', ad=1, f=1)
                    if grps:
                        for grp in grps:
                            if '|' in grp:
                                grpinfo=grp.split('|')
                                #if info[0] == u'mi' and len(grpinfo)==3 and grpinfo[2] not in ['FX','RIG','DEFORMERS','MODEL']:
                                if info[0] == u'mi' and len(grpinfo)==3 and grpinfo[2] not in ['FX','RIG','DEFORMERS','MODEL','FUR_GRP','SHAVE']:
                                    print '\n\n'
                                    mc.error(u'[%s]没有在[“FX”,“RIG”,“DEFORMERS”,“MODEL”]，请检查多余组'%grpinfo[2])
                                #elif info[0] == u'mi' and len(grpinfo)==3 and grpinfo[2] not in ['FX','RIG','DEFORMERS','MODEL','FUR_GRP','SHAVE']:
                                #    print '\n\n'
                                #    mc.error(u'[%s]没有在[“FX”,“RIG”,“DEFORMERS”,“MODEL”,u"FUR_GRP"]，请检查多余组'%grpinfo[2])
                                elif len(grpinfo)==4 and grpinfo[2]=='MODEL' and grpinfo[3]!='MSH_all':
                                    print '\n\n'
                                    mc.error(u'no MSH_all ')
                                elif len(grpinfo)>4 and grpinfo[2]=='MODEL' and grpinfo[3]=='MSH_all' and grpinfo[4]!='MSH_geo' and info[0] != 'mi':
                                    print '\n\n'
                                    mc.error(u'no MSH_geo')
                                #elif info[0] == 'mi' and len(grpinfo)>4 and grpinfo[2]=='MODEL' and grpinfo[3]=='MSH_all' and grpinfo[4]not in [u'MSH_geo',u'MSH_outfit'] :
                                #    print '\n\n'
                                #    mc.error(u'no MSH_geo or no MSH_outfit' )
                                elif len(grpinfo)==5 and info[-1]=='rg' +fileFormat and grpinfo[2]=='RIG'  and grpinfo[4]=='Master' and grpinfo[3]!='Master_GRP':
                                    print '\n\n'
                                    mc.error(u'no Master_GRP ')
                                elif len(grpinfo)==5 and info[-1]=='rg' +fileFormat and grpinfo[2]=='RIG'  and grpinfo[3]=='Master_GRP'  and grpinfo[4]!='Master':
                                    print '\n\n'
                                    mc.error(u'no Master Circle')
                                elif  len(grpinfo)==6 and info[-1]=='rg' +fileFormat and grpinfo[2]=='RIG'  and grpinfo[3]=='Master_GRP'  and grpinfo[4]=='Master' and grpinfo[5]!='Move_ctrl' :
                                    print '\n\n'
                                    mc.error(u'no Move_ctrl Circle')
                                elif  len(grpinfo)>6 and info[-1]=='rg' +fileFormat and grpinfo[2]=='RIG'  and grpinfo[3]=='Master_GRP'  and grpinfo[4]=='Master' and grpinfo[5]=='Move_ctrl' and grpinfo[6]!='Character':
                                    print '\n\n'
                                    mc.error(u'no Character Circle')
                    else:
                        print '\n\n'
                        mc.error(u'[%s]组是空组，请检查文件'%grpup)
                if len(grpups)>1:
                    print '\n\n'
                    mc.error(u'[%s]有不止一个，请检查文件'%grpup)
                if len(grpups)==0:
                    print '\n\n'
                    mc.error(u'缺少[%s]，请检查文件'%grpup)


        # 输出错误消息
        if errors:
            print (u'文件中以下存在文件结构问题')
        #print(unicode('=============================【文件中错误如下】=============================', 'utf8'))
            print(u'=============================【文件以下物体，有文件结构问题，请检查文件】=============================')
            for er  in errors:
                #print(unicode('%s' % (str(info)), 'utf8'))
                print er
            mc.error(u'文件有文件结构问题，请检查文件')
        else:
            print u'文件结构正确'

        return errors

#----------------------------------------------------------------------------------------------------------#
#【YD】按编号检测模型命名
#@author:韩虹
#data：2015/12/04
#---------------------------------------------------
    def yd_checkMeshName(self):
        idNum=self.yd_idNum()
        if idNum == 6:
            self.gdc_ModelNameCheck(mo=2)
            print u'\n\n 模型命名OK'
        else:
            self.gdc_ModelNameCheck(mo=1)
            print u'\n\n 模型命名OK'
        return 0
#----------------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------#
#【通用】模型命名检测
#@author: hanhong
#Data：2015/12/02
#mo为1时，检测普通模型文件，mo为2时，检测高低模文件
#---------------------------------------------------
    def gdc_ModelNameCheck(self,mo=1):
        errorInfo=[]
        errorInfo01=[]
        errorInfo02=[]
        shotInfos= sk_infoConfig.sk_infoConfig().checkShotInfo()
        if mo==1 and shotInfos[1][0] in ['c','p']:
            meshs=mc.ls(type='mesh',l=1)
            if meshs:
                for mesh in meshs:
                    objn=mc.listRelatives(mesh,p=1,f=1)
                    if objn and '|MODEL|' in objn[0] and '_' in objn[0]:
                        obj=objn[0]
                        objshort=obj.split('|')[-1]
                        if objshort.split('_')[0]!='MSH':
                            errorInfo.append(obj)
                        if objshort.split('_')[-1]!='':
                            errorInfo01.append(obj)
            if  errorInfo:
                print u'文件中下列物体命名不正确，请检查并修改'
                for err in errorInfo:
                    mc.warning(u'【%s】该物体应该"MSH" 开头，请修改命名'%err)
            if  errorInfo01:
                print u'文件中下列物体命名不正确，请检查并修改'
                for err in errorInfo01:
                    mc.warning(u'【%s】该物体应该"_" 结尾，请修改命名'%err)
        errors= errorInfo+ errorInfo01
        if errors:
            mc.error(u'文件中有错误命名模型，请检查并修改')
        if mo==2:
            meshs=mc.ls(type='mesh',l=1)
            if meshs:
                for mesh in meshs:
                    objn=mc.listRelatives(mesh,p=1,f=1)
                    if objn and '|' in objn[0] and '_' in objn[0]:
                        obj=objn[0]
                        objshort=obj.split('|')[-1].split('_')
                        if objshort[0]!=shotInfos[1] or  objshort[1]!=shotInfos[2] or objshort[-1]!='':
                            errorInfo02.append(obj.split('|')[-1])
            if errorInfo02:
                print u'===================请检查下列不正确命模型，并修改===================='
                for err in errorInfo02:
                    mc.warning(u'【%s】该模型命名错误，请修改命名'%err)
                mc.error(u'文件中有错误命名模型，请检查并修改')
#        return 0

#----------------------------------------------------------------------------------------------------------#
#【通用】高低模文件结构检测
#@author:韩虹
#data：2015/10/28
#---------------------------------------------------
    def gdc_switchstructure(self):
        info = sk_infoConfig.sk_infoConfig().checkShotInfo()
        if len(info)>3:
            grp=info[1]+'_'+info[2]+'_grp'
            pro=info[1]+'_'+info[2]
            ctrName=info[1]+'_'+info[2]+'_ctrl'
        else:
            mc.error(u'文件命名不正确，请检查')
        ctrl=mc.ls(type='nurbsCurve',l=1)
        if len(ctrl)==0:
            mc.error(u'高低模转换工具，需要添加"_ctrl"控制线圈，请修改文件')
        if len(ctrl)>1:
            mc.error(u'有两个或两个以上控制圈，请检查并修改文件')

        if len(ctrl)==1:
            ctr=mc.listRelatives(ctrl[0],p=1,f=1)
            cr=ctr[0].split('|')
            if cr[0]!='':
                mc.error(u'控制线圈没有在根目录，请检查')
            if cr[-1] !=ctrName:
                print '\n\n'
                print(u'=============控制圈的命名不正确，正确命名应该是 "%s"=============='%ctrName)
                print '\n\n'
                mc.error(u'=============控制圈的命名不正确，正确命名应该是 "%s"=============='%ctrName)
        meshs=mc.ls(type='mesh',l=1)
        for mesh in meshs:
            obj=mc.listRelatives(mesh,p=1,f=1)
            objinfo=obj[0].split('|')
            if objinfo[1]!=ctrName:
                print '\n\n'
                print(u'=============模型需要在线圈"%s" 组下=============='%ctrName)
                mc.error(u'模型没有在线圈"%s"组下' %ctrName)
            if objinfo[2]!=grp:
                print '\n\n'
                print(u'=============模型需要在"%s" 组下=============='%grp)
                print '\n\n'
                mc.error(u'模型没有在"%s"组下' %grp)
            if pro  not in objinfo[-1] :
                print '\n\n'
                print(u'============="%s" 模型命名不正确，请检查=============='%obj)
                print '\n\n'
                mc.error(u'"%s" 模型命名不正确，请检查' %obj)
        print '\n\n'
        print u'高低模文件结构已检测'


    # 非法mesh检测
    # 这个处理大纲里显示为空组，但实际上有mesh节点的情况
    def checkMeshError(self):
        shaderSGList = self.checkCacheRecordMaterial()
        errorInfo = []
        if shaderSGList:
            keys = shaderSGList.keys()
            for key in keys:
                objs = shaderSGList[key]
                if objs:
                    for obj in objs:
                        if mc.ls(obj):
                            pass
                        else:
                            errorInfo.append(obj)
        return errorInfo

#----------------------------------------------------------------------------------------------------------#
#【通用】前期文件检测豁免
#data\localAsset.txt
#@author:韩虹 (修改自沈康相似脚本）
#data：2015/10/16
#---------------------------------------------------
    def checkInfo(self):
        strangeID=self.checkStrangeIDInfo()
        shotInfo=sk_infoConfig.sk_infoConfig().checkShotInfo()
        check=1
        if shotInfo[1] in strangeID:
            check=0
        else:
            check=1
        return check

    def checkStrangeIDInfo(self):
        dataPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()+ 'data/localAsset.txt'
        strangeID = self.checkFileRead(dataPath)
        if strangeID:
            strangeID.remove(strangeID[0])
        return strangeID
#动画文件检测豁免
#data\localAnim.txt
#----------------------------------------------------------------------------------------------------------#
    def checkAnimShotInfo(self):
        dataPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()+ 'data/localAnim.txt'
        AnimShot = self.checkFileRead(dataPath)
        if AnimShot:
            AnimShot.remove(AnimShot[0])
        return AnimShot
#----------------------------------------------------------------------------------------------------------#
#【通用】动画文件检测豁免
#data\localAnim.txt
#@author:韩虹 (修改自沈康相似脚本）
#data：2017/4/13
#---------------------------------------------------
    def AnimcheckInfo(self):
        strangeID=self.checkAnimShotInfo()
        shotInfo=sk_infoConfig.sk_infoConfig().checkShotInfo()
        shotName=''
        if shotInfo[0] in ['Yak']:
            shotName=shotInfo[0]+'_'+shotInfo[1]+'_'+shotInfo[2]
        check=1
        if shotName in strangeID:
            check=0
        else:
            check=1
        return check
#【通用】信息读取
#@author:沈康 (修改自沈康相似脚本）
#data：2014
#---------------------------------------------------
    def checkFileRead(self, path):
        print u'>>>>>>[read]'
        print path
        txt = open(path, 'r');
        try:
            fileContent = txt.readlines()
            print('Loading........')
        finally:
            txt.close()
        result = []
        for info in fileContent:
            if '\r\n' in info:
                result.append(info.split('\r\n')[0])
            else:
                result.append(info)
        return result
#----------------------------------------------------------------------------------------------------------#
#【YD】读取末尾编号数字
#@author:韩虹
#data：2014
#---------------------------------------------------
    def yd_idNum(self):
        import re
        idNum=''
        shotInfo=sk_infoConfig.sk_infoConfig().checkShotInfo()
        IN=re.search(r"\d{6,}(.*)$", shotInfo[1])
        if IN:
            id=IN.group(1)
        else:
            mc.warning(u'=============================文件名不正确，缺少ID编号======================')
            mc.error(u'=============================文件名不正确，缺少ID编号======================')
        if id:
            idNum=shotInfo[1].split(id)[0][-1]
        return idNum
#----------------------------------------------------------------------------------------------------------#

#----------------------------------------------------------------------------------------------------------#
#【NJ】读取三位编号数字（辨别nj17)
#@author:韩虹
#data：2016
    #---------------------------------------------------
    def NumNJ17(self):
        idNum=''
        shotInfo=sk_infoConfig.sk_infoConfig().checkShotInfo()
        id=shotInfo[1][2]
        if id in ['7','w']:
            idNum=1
        else:
            idNum=0
        return idNum
#----------------------------------------------------------------------------------------------------------#

#----------------------------------------------------------------------------------------------------------#
#【YD】按编号检测文件结构
#@author:韩虹
#data：2015/11/27
#---------------------------------------------------
    def yd_checkGeo(self):
        idNum=self.yd_idNum()
        if idNum == 6:
            self.gdc_switchstructure()
            print u'\n\n 文件结构OK'
        else:
            self.gdc_checkstructure()
            print u'\n\n 文件结构OK'
        return 0
#----------------------------------------------------------------------------------------------------------#
#【通用】no freeze检测
#@author:韩虹
#data：2014
#---------------------------------------------------
    def gdc_nofrezzeCheck(self):
        '''
        sn = mc.file(q = True,sn = True, shortName = True).find('yd_') #屏蔽YD项目
        if sn == 0:
            return 0
        '''
        trees=self.gdc_treeCheckNew()
        wrongTransforms=[]
        allTransforms=mc.ls(tr=1,l=1)
        attrs = ['.tx','.ty','.tz','.rx','.ry','.rz','.sx','.sy','.sz']
        if allTransforms:
            for obj in allTransforms:
                if '|MODEL|' in obj and obj not in wrongTransforms:
                    infotype=0
                    for attr in attrs:
                        cons = mc.listConnections( obj + attr, d = False, s = True)
                        attrVal = mc.getAttr(obj + attr)
                        compareVal = 0
                        if attr in ['.sx','.sy','.sz']:
                            compareVal = 1
                        if attrVal != compareVal and not cons :
                            infotype=1
                    if infotype==1 and obj not in wrongTransforms:
                        wrongTransforms.append(obj)
        shotInfos= sk_infoConfig.sk_infoConfig().checkShotInfo()
        if shotInfos[1][0] in ['s','S']:
            ff=[]
            if wrongTransforms:
                for wr in   wrongTransforms:
                    if mc.listRelatives(wr,s=1,f=1) and mc.nodeType(mc.listRelatives(wr,s=1,f=1)[0])=='nurbsCurve':
                        ff.append(wr)
            for f in ff:
                if f in  wrongTransforms:
                    wrongTransforms.remove(f)
            if trees:
                for tree in trees:
                    if tree in  wrongTransforms:
                        wrongTransforms.remove(tree)

        if  wrongTransforms:
            mc.select(wrongTransforms)
            print '\n\n'
            mc.warning(u'有no freeze，请检查以下物体')
            print '============================='
            for wr in  wrongTransforms:
                print wr
            print '============================='
            mc.error(u'文件中有nofreeze物体，请检查选择物体')
        else:
            print '\n\n'
            mc.warning(u'no freeze检测OK')
        return 0
#----------------------------------------------------------------------------------------------------------#
#【通用】检测Tree属性物体（cur)，以进行Freeze免检
#@author:韩虹
#data：2016
#---------------------------------------------------
    def gdc_treeCheck(self):
        curs=mc.ls(type='nurbsCurve',l=1)
        treeList=[]
        if curs:
            for cur in curs:
                tr=mc.listRelatives(cur,p=1,f=1)
                if tr and mc.objExists(tr[0]+'.tree'):
                    treeList.append(tr[0])
        return treeList
#----------------------------------------------------------------------------------------------------------#
#【通用】检测所有有tree属性的物体
#@author:韩虹
#data：2016
#---------------------------------------------------
    def gdc_treeCheckNew(self):
        objs=mc.ls(tr=1,l=1)
        treeList=[]
        if objs:
            for obj in objs:
                if mc.objExists(obj+'.tree'):
                    treeList.append(obj)
        return treeList


#----------------------------------------------------------------------------------------------------------#
#【YODA项目】激光检测
#@author:韩虹
#data：2015-12-02
#re 为是否检测客户激光，me 为是否检测内部激光命名
#---------------------------------------------------
    def GDC_LaserShotCheck(self,re=1,me=1):
        warnInfos=[]
        warnInfos03=[]
        warnInfos01=[]
        if re==1:
            refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
            refNamespace = refInfos[2][0]
            refRN=refInfos[0][0]
            if refRN:
                for ref in refRN:
                    if 'LaserShots' in ref:
                        warnInfos.append(ref)
            if warnInfos:
                print u'文件中有客户激光文件，请检查并删除'
                for warn in warnInfos:
                    mc.warning(u'【%s】参考为客户激光文件，请检查并删除'%warn)

            meshs=mc.ls(type='mesh',l=1)
            if meshs:
                for mesh in meshs:
                    objn=mc.listRelatives(mesh,p=1,f=1)
                    if objn:
                        obj=objn[0]
                    if obj !='':
                        objshort=obj.split('|')[-1]
                    if objshort and 'LaserShots' in objshort :
                        warnInfos01.append(obj)
            if warnInfos01:
                print u'文件中有客户激光文件，请检查并删除'
                for warn in warnInfos01:
                    mc.warning(u'【%s】参考为客户激光模型，请检查并删除'%warn)
        if me==1:
            meshs=mc.ls(type='mesh',l=1)
            mc.select(warnInfos03)
            if meshs:
                for mesh in meshs:
                    objn=mc.listRelatives(mesh,p=1,f=1)
                    if objn:
                        obj=objn[0]
                    if obj !='':
                        objshort=obj.split('|')[-1]
                    if objshort and 'laser_lightInder' in objshort and '____PlutoGun____' in obj and objshort.split('_')[2] not in ['red','green','blue']:
                        warnInfos03.append(obj)
        errorinfo=warnInfos+warnInfos03+warnInfos01
        if errorinfo:
            print u'文件中有非适当激光物体，请关注上列warn警报'
            mc.error(u'文件中有客户激光物体，或非适当激光命名，请检查并修改')
        return errorinfo



#----------------------------------------------------------------------------------------------------------#
#【通用】TPose检测
#@author:韩虹
#data：2015-11-20
#---------------------------------------------------
    def GDC_TPOSECheck(self,infotype=3):
        Tpose=['ce0101001001DarthSidious','ce0101002001DarthSidiousHologram','ce0101003001DarthVader','ce0101004001DarthVaderHologram','ce0101012001MasterKendu','ce0101013001MasterKenduEvil',
        'ce0101014001MasterKenduHologram','ce0101015001Naare','ce0101026001JediWithHood']
        shotInfo=sk_infoConfig.sk_infoConfig().checkShotInfo()
        project=sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(shotInfo[0])
        if infotype==3:
            info=self.GDC_tposeMsSQL(project,shotInfo[1],shotInfo[2],shotInfo[3])
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        TposeNSpace=[]
        for i in range(len(refInfos[0][0])):
            if refInfos[1][0][i].split('/')[-1].split('_')[1] in Tpose:
                TposeNSpace.append(refInfos[2][0][i])
        TposeType=0
        errorinfo=[]
        if TposeNSpace:
            for Tpo in TposeNSpace:
                if mc.ls(Tpo+':Character'):
                    ctr=mc.ls((Tpo+':Character'),l=1)[0]
                    frams=mc.keyframe(ctr,q=1)
                    if frams and int('950') in frams:
                        TposeType=1
                    else:
                        errorinfo.append(Tpo)


        if info[3]!='' and TposeType==0:
            print '======================================'
            mc.warning(u'该镜头需要APose，而文件内未设置APose，请检查文件并正确设置')
            print u'=======【%s】=============='%errorinfo
            print '======================================'
            mc.error(u'该镜头需要APose，而文件内未设置APose，请检查文件并正确设置')

        else:
            print '======================================'
            print(u'已进行Apose检测')
            print '======================================'

        return 0

#----------------------------------------------------------------------------------------------------------#
#【通用】TPose设置
#@author:韩虹
#data：2015-11-23
#T=1,Tpose，T=0,Apose
#---------------------------------------------------
    def GDC_TPOSESet(self,infotype=3,T=1):
        Tposeframe=['950','980']

        Tpose=['ce0101001001DarthSidious','ce0101002001DarthSidiousHologram','ce0101003001DarthVader','ce0101004001DarthVaderHologram','ce0101012001MasterKendu','ce0101013001MasterKenduEvil',
        'ce0101014001MasterKenduHologram','ce0101015001Naare','ce0101026001JediWithHood']
        shotInfo=sk_infoConfig.sk_infoConfig().checkShotInfo()
        project=sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(shotInfo[0])
        if infotype==3:
            info=self.GDC_tposeMsSQL(project,shotInfo[1],shotInfo[2],shotInfo[3])
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        TposeNSpace=[]
        for i in range(len(refInfos[0][0])):
            if refInfos[1][0][i].split('/')[-1].split('_')[1] in Tpose:
                TposeNSpace.append(refInfos[2][0][i])
        ctrls=[]
        if info[3]!='' and TposeNSpace:
            for Tpo in TposeNSpace:
                if mc.ls(Tpo+':bodySet'):
                    set=mc.ls((Tpo+':bodySet'),l=1)[0]
                    ctr=mc.sets(set,q=1,no=1)
                    if ctr:
                        for ct in ctr:
                            if ct !=(Tpo+':Master'):
                                ct=mc.ls(ct,l=1)
                                if ct:
                                    for cn in ct:
                                        if cn and cn not in ctrls :
                                            ctrls.append(cn)

# 在980 帧K一帧
        '''
        mc.currentTime(int(Tposeframe[1]))
        curs=mc.ls(type='nurbsCurve',l=1)
        if curs:
            for ctrl in curs:
                obj=mc.listRelatives(ctrl,p=1,f=1)
                try:
                    mc.setKeyframe(obj[0],t=int(Tposeframe[1]))
                except:
                    #print '==========[%s]此属性已经锁定，无法K帧=============' %(ctrl +att)
                    pass
        '''
# 在950帧，设置TPose，并K帧
        if T==1 and info[3]!='':
            mc.currentTime(Tposeframe[0])
            attrs = ['.tx','.ty','.tz','.rx','.ry','.rz','.rotateX','.rotateY','.rotateZ','.raiseBall','.translateX','.translateY','.translateZ','.raiseBall','.raiseToe']
            if ctrls:
                for ctrl in ctrls:
                    try:
                        mc.setKeyframe(ctrl)
                    except:
                        pass

                    for att in attrs:
                        if mc.objExists(ctrl +att):
                            try:
                                mc.setAttr((ctrl +att),0)
                                mc.setKeyframe(ctrl +att)
                            except:
                                pass

#APose
        if T==0 and info[3]!='':
            mc.currentTime(Tposeframe[0])
            AposePath='Z:/Projects/YODA/YODA_Scratch/VFX/A pose/Info/'
            AposeInfo=self.checkFileRead(AposePath+'Apose.txt')
            AposeList=[]
            if AposeInfo:
                for i in range(len(AposeInfo)):
                    if ';' in AposeInfo[i]:
                        inf=AposeInfo[i].split(';')
                        AposeList.append(inf)
                    else:
                        inf=[AposeInfo[i]]
                        AposeList.append(inf)
            Apose=[]
            if  AposeList:
                for i in range(len(AposeList)):
                    if i==0:
                        Apose=AposeList[i]
                    else:
                        Apose=Apose+AposeList[i]

            AposeNSpace=[]
            AposeID=[]
            for i in range(len(refInfos[0][0])):
                if refInfos[1][0][i].split('/')[-1].split('_')[1] in Apose:
                    AposeNSpace.append(refInfos[2][0][i])
                    AposeID.append(refInfos[1][0][i].split('/')[-1].split('_')[1])
            ctrls=[]
            if AposeNSpace:
                for Apo in AposeNSpace:
                    if mc.ls(Apo+':bodySet'):
                        set=mc.ls((Apo+':bodySet'),l=1)[0]
                        ctr=mc.sets(set,q=1,no=1)
                        if ctr:
                            for ct in ctr:
                                if ct !=(Apo+':Master'):
                                    ct=mc.ls(ct,l=1)
                                    if ct:
                                        for cn in ct:
                                            if cn and cn not in ctrls :
                                                ctrls.append(cn)

            # 在950帧，设置TPose，并K帧
            mc.currentTime(Tposeframe[0])
            attrs = ['.tx','.ty','.tz','.rx','.ry','.rz','.rotateX','.rotateY','.rotateZ','.raiseBall','.translateX','.translateY','.translateZ','.raiseBall','.raiseToe']
            if ctrls:
                for ctrl in ctrls:
                    try:
                        mc.setKeyframe(ctrl)
                    except:
                        pass

                    for att in attrs:
                        if mc.objExists(ctrl +att):
                            try:
                                mc.setAttr((ctrl +att),0)
                                mc.setKeyframe(ctrl +att)
                            except:
                                pass

            if AposeID:
                for j in range(len(AposeID)):
                    infoFil=''
                    if os.path.exists(AposePath+AposeID[j]+'.txt'):
                        infoFil=AposePath+AposeID[j]+'.txt'
                    else:
                        for k in range(len(AposeList)):
                            if AposeID[j] in AposeList[k] and os.path.exists(AposePath+AposeList[k][0]+'.txt'):
                                infoFil=AposePath+AposeList[k][0]+'.txt'
                                break
                    if infoFil!='':
                        infoN=self.checkFileRead(infoFil)
                        for inf in infoN:
                            if len(inf.split(' '))>1:
                                print inf.split(' ')[0]
                                objatt=inf.split(' ')[0]
                                try:
                                    Num=float(inf.split(' ')[1])
                                except:
                                    Num=inf.split(' ')[1]
                                objattN=AposeNSpace[j]+':'+objatt
                                if mc.objExists(objattN):
                                    try:
                                        mc.cutKey(objattN,time=(950,980))
                                    except:
                                        pass
                                    mc.setKeyframe(objattN,t=int(Tposeframe[0]))
                                    mc.setAttr(objattN,Num)
                            else:
                                print inf
                                mc.warning(u'=========【%s】这个文件上列行有问题，请检查========'%infoFil)
                    else:
                        mc.warning(u'=========【%s】缺少APose信息========'%AposeID[j])
        if info[3]=='':
            print u'===========该镜头是非Tpose 镜头========='
        elif info[3]!='' and T==1:
            print u'===========已设置TPOSE==========='
        elif info[3]!='' and T==0:
            print u'===========已设置APOSE==========='

        return 0

#----------------------------------------------------------------------------------------------------------#
#【通用】数据库TPOSE查询
#@author:韩虹
#data：2015-11-20
#---------------------------------------------------

    def GDC_tposeMsSQL(self,project,ep,sq,sc,tp=0):
        import pyodbc
        try:
            cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=idmt-engine08;DATABASE=idmtPlex_%s;UID=EReader;PWD=123123'%(project))
        except:
            return None
        cursor = cnxn.cursor()
        cmd_sql = '''select VSAS.anim_ep,VSAS.Tag,VSAS.anim_sc,VSAS.unfixed8
         from dbo.View_SsomGetAnimStatus VSAS
         WHERE VSAS.anim_ep = \'%s\' AND VSAS.Tag = \'%s\' AND VSAS.anim_sc = \'%s\''''%(ep,sq,sc)
        if tp==0:
            scInfo = cursor.execute(cmd_sql).fetchone()
        else:
            scInfo = cursor.execute(cmd_sql).fetchall()
        return scInfo
#----------------------------------------------------------------------------------------------------------#
#【通用】模型解锁
#@author:韩虹
#data：2015-12-15
#---------------------------------------------------

    def GDC_MeshUnLock(self):
        meshs=mc.ls(type='mesh',l=1)
        objs=[]
        if meshs:
            for mesh in meshs:
                if mc.objExists(mesh+'.overrideEnabled'):
                    mc.setAttr((mesh+'.overrideEnabled'),0)
                obj=mc.listRelatives(mesh, p=1,f=1)
                if obj:
                    obj=obj[0]
                    objs.append(obj)
        else:
            mc.error(u'=========NO MESH===========')
        '''
        if objs:
            for obj in objs:
                Attrs=mc.listAttr(obj,keyable=1)
                if Attrs:
                    for att in Attrs:
                        try:
                            mc.setAttr((obj+'.'+att),l=0)
                        except:
                            mc.warning(u'===============[%s]无法解锁============')
                            pass
        '''
        return 0

    def GDC_NodeCheck(self):
        nodetypes=['vectorRenderGlobals','colorCorrect']
        nodeerrors=[]
        for nodetype in nodetypes:
            checkNodes=mc.ls(type=nodetype)
            if checkNodes:
                print '\n\n'
                print '=============================================================================='
                mc.warning(u'=================文件中有【%s】节点，请检查文件并修改===================='%nodetype)
                for node in checkNodes:
                    mc.warning(u'=================【%s】是【%s】节点，请检查并修改===================='%(node,nodetype))
                    nodeerrors.append(node)
        if nodeerrors:
            mc.error(u'=================文件中有【%s】节点，请检查文件并修改===================='%nodetypes)
        else:
            print u'=================非法节点（客户不需要）检测已OK======================'
        return 0
#----------------------------------------------------------------------------------------------------------#
#【YD】检测cache唯一性
#@author:韩虹
#data：2016-1-26
#---------------------------------------------------
    def YD_CachePathCheck(self):
        cacheFils=mc.ls(type='cacheFile',l=1)
        if cacheFils:
            for fil in cacheFils:
                if mc.ls(fil+'.cachePath'):
                    filepath=mc.getAttr(fil+'.cachePath')
                    if filepath.split('/')[-1]=='':
                        path=filepath.split('/')[-2]
                    else:
                        path=filepath.split('/')[-1]
                    paths=filepath.split(path)[0]
                    fil=mc.getFileList(folder=paths)
                    if len(fil)<2:
                        break
                    else:
                        mc.warning(u'该镜头有不止一个cache目录，请检查【%s】'%fil)
                        mc.error(u'该镜头有不止一个cache目录，请检查')
        print u'=================已检测cache路径唯一======================'
        return 0
#----------------------------------------------------------------------------------------------------------#
#【YD】检测文件中未激活动画层
#@author:韩虹
#data：2016-1-27
#---------------------------------------------------
    def YD_animLayerCheck(self):
        Layers=mc.ls(type='animLayer',l=1)
        layererrors=[]
        for layer in Layers:
            if mc.animLayer(layer,q=1,mute=1)==True:
                layererrors.append(layer)
        if  layererrors:
            mc.warning(u'============文件中有未激活动画层，请检查===============')
            print layererrors
            mc.error (u'============文件中有未激活动画层，请检查===============')
        else:
            print (u'============动画层激活状态已检测===============')
        return 0
#----------------------------------------------------------------------------------------------------------#
#【YD】检测ce0101015001Naare眉毛，并K帧
#@author:韩虹
#data：2016-2-01
#---------------------------------------------------
    def YD_animFrame(self):
        refInfo = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refNodes = refInfo[2][0]
        refs=[]
        if refNodes:
            for ref in refNodes:
                if 'ce0101015001Naare' in ref:
                    refs.append(ref)
        if refs:
            for re in refs:
                frames=re+':frame'
                if mc.ls(frames) and mc.objExists(frames+'.brow_side'):
                    mc.cutKey(frames+'.brow_side')
                    mc.setAttr((frames+'.brow_side'),0.1)
                    mc.setKeyframe((frames+'.brow_side'),t=1000)
            print u'===========ce0101015001Naare角色眉毛属性已K帧=============='
        return 0
#----------------------------------------------------------------------------------------------------------#
#【NJ2017】渲染代理判断
#@author:韩虹
#data：2016-6-15
#---------------------------------------------------
    def nj17_proxyInfo(self):
        path='Z:\Projects\Ninjago\Project\data\proxy\NJ2017\proxyID.txt'
        proxyID=self.checkFileRead(path)
        shotInfos= sk_infoConfig.sk_infoConfig().checkShotInfo()
        proxyInfo=0
        if shotInfos[1] in proxyID:
            proxyInfo=1
        return proxyInfo
#----------------------------------------------------------------------------------------------------------#
#【NJ2017】smooth节点检测
#@author:韩虹
#data：2016-6-16
    #---------------------------------------------------
    def nj17_vsmothInfo(self):
        objs=mc.ls(tr=1,l=1)
        errors=[]
        if objs:
            for obj in objs:
                meshs=mc.listRelatives(obj,s=1,type='mesh',ni=1,f=1)
                if meshs and mc.objExists(obj+'.nosmoothV')==0 and '|MODEL|' in meshs[0]  and '|DEFORMERS|' not in meshs[0] and '|RIG|' not in meshs[0] and  mc.objExists(meshs[0]+'.vraySubdivEnable')==0:
                    errors.append(obj)
        if errors:
            mc.select(errors)
            errors=errors
            for er in errors:
                mc.warning(u'============【%s】缺少smooth节点，请检测文件========='%er)
            mc.error(u'============文件中有缺少smooth节点的物体，请关注上面警告信息=========')
        else:
            print(u'==============Subdivision 已检测==============')
        return 0
#----------------------------------------------------------------------------------------------------------#
#【NJ2017】前期文件路径，本机路径，渲染代理路径
#@author:韩虹
#data：2016-6-16
    #---------------------------------------------------
    def gdc_proxyPath(self):
        shotInfo=sk_infoConfig.sk_infoConfig().checkShotInfo()
        fileName=mc.file(q=1,sn=1,shn=1)
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        proxypath=serverPath+'data/proxy/NJ2017/'
        shotInfos= sk_infoConfig.sk_infoConfig().checkShotInfo()
        chatype=''
        line=''
        if 'c' in shotInfos[1][0]:
            chatype='characters'
        if 'p' in shotInfos[1][0]:
            chatype='props'
        if 's' in shotInfos[1][0]:
            chatype='sets'
        if '.' in shotInfo[-1] and shotInfo[-1].split('.')[0]=='rg':
            line='rigging'
        if '.' in shotInfo[-1] and shotInfo[-1].split('.')[0]=='tx':
            line='texture'
        if shotInfo[3]=='ms':
            line='master'
        asset = idmt.pipeline.db.GetAssetByFilename(fileName)
        if asset:
            EP=asset.code
            serverimagepath= serverPath+'scenes/'+chatype+'/'+EP+'/'+shotInfos[1]+'/'+line+'/'
        else:
            serverimagepath= serverPath+'scenes/'+chatype+'/'+shotInfos[1]+'/'
        temimagepath='D:/Info_Temp/proxy/' + str(shotInfos[1]) + '/'
        mc.sysFile(temimagepath, makeDir=True)
        texpath=[temimagepath,serverimagepath,proxypath]
        return texpath
#----------------------------------------------------------------------------------------------------------#
#【通用】高模 ，低模，渲染代理物体
#@author:韩虹
#data：2016-6-17
    #---------------------------------------------------
    def proxyMeshInfo(self):
        shotInfo=sk_infoConfig.sk_infoConfig().checkShotInfo()
        meshsH=[]
        meshsL=[]
        meshsP=[]
        ctrlH=shotInfo[1]+'_h_ctrl'
        ctrlL=shotInfo[1]+'_l_ctrl'
        ctrlP=shotInfo[1]+'_proxy'
        meshs=mc.ls(type='mesh',l=1)
        if meshs:
            for mesh in meshs:
                obj=mc.listRelatives(mesh,p=1,type='transform',f=1)
                if obj and ctrlH in obj[0]:
                    meshsH.append(obj[0])
                if obj and ctrlL in obj[0]:
                    meshsL.append(obj[0])
                if obj and ctrlP in obj[0]:
                    meshsP.append(obj[0])
        return [meshsH,meshsL,meshsP]
#----------------------------------------------------------------------------------------------------------#
#【通用】高模 ，低模，渲染代理结构信息
#@author:韩虹
#data：2016-6-17
    #---------------------------------------------------
    def proxyGeoInfo(self,typ='p'):
        shotInfo=sk_infoConfig.sk_infoConfig().checkShotInfo()
        ctrl=shotInfo[1]+'_'+typ+'_ctrl'
        grp=shotInfo[1]+'_'+typ+'_grp'
        pre=shotInfo[1]+'_'+typ+'_'
        return [ctrl,grp,pre]
#----------------------------------------------------------------------------------------------------------#
#【通用】高模 ，低模，渲染代理结构信息
#@author:韩虹
#data：2016-6-17
    #---------------------------------------------------
    def proxyCreatCheckin(self,server=1):
        shotInfo=sk_infoConfig.sk_infoConfig().checkShotInfo()
        servpath=sk_infoConfig.sk_infoConfig().checkProjectAssetNames()
        fileName=mc.file(q=1,sn=1,shn=1)
        path=self.gdc_proxyPath()
        tempath=path[0]
        serverpath=path[1]
        proxypath=path[2]
        proxyInfo=self.nj17_proxyInfo()
        vrmesh=shotInfo[1]+'.vrmesh'
        if os.path.exists(proxypath+vrmesh):
            mc.sysFile(proxypath+'/his', makeDir=True)
            mc.sysFile(proxypath+vrmesh, move=proxypath+'/his/'+vrmesh)
        proxyName=shotInfo[1]+'_proxy'
        modelH=shotInfo[0]+'_'+shotInfo[1]+'_h_rg.mb'
        modelL=shotInfo[0]+'_'+shotInfo[1]+'_l_rg.mb'
        modelP=shotInfo[0]+'_'+shotInfo[1]+'_p_rg.mb'
        if shotInfo[0]=='nj' and proxyInfo==1 and shotInfo[2]=='h' and shotInfo[3]=='rg.mb' and os.path.exists(serverpath+modelL):
            mc.file((serverpath+modelL),i=1)
        if shotInfo[0]=='nj' and proxyInfo==1 and shotInfo[2]=='l' and shotInfo[3]=='rg.mb' and os.path.exists(serverpath+modelH):
            mc.file((serverpath+modelH),i=1)
        meshs=self.proxyMeshInfo()
        meshsH=meshs[0]
        meshsL=meshs[1]
        if meshsH and meshsL:
            mc.select(cl=1)
            mc.select(meshsH)
            mc.select(meshsL,add=1)
            cmdPath='vray setConfValue "proxyPath" '+ '"'+ proxypath+'"'
            cmdExport='vray setConfValue "proxyExportType" 1'
            cmdanm='vray setConfValue "proxyAnimOn" 0'
            cmdOver='vray setConfValue "proxyOverwriteExisting" 1'
            cmdLast='vray setConfValue "proxyLastSelectedAsPreview" 1'
            cmdPreview='vray setConfValue "proxyPreviewType" "combined"'
            cmdVertexcolor='vray setConfValue "proxyVertexColorsOn" 0'
            cmdnodeName='textFieldGrp -e -text ' +'"'+proxyName+'" vraycpNewNodeNameCtrl'
            cmdFileName='textFieldGrp -e -text ' +'"'+vrmesh+'" vraycpFileNameCtrl'
            mel.eval(cmdPath)
            mel.eval(cmdExport)
            mel.eval(cmdOver)
            mel.eval(cmdLast)
            mel.eval(cmdPreview)
            mel.eval(cmdVertexcolor)
            mel.eval('vrayCreateCreateProxyWindow()')
            mel.eval(cmdnodeName)
            mel.eval(cmdFileName)
            mc.checkBoxGrp('vraycpAutoCreateCtrl',e=1,v1=1)
            mel.eval('vrayCreateProxyButtonPressed()')
            meshs=self.proxyMeshInfo()
            meshsP=meshs[2]
            proxygeo=self.proxyGeoInfo('p')
            logeo=self.proxyGeoInfo('l')
            ctrll=logeo[0]
            grpl=logeo[1]
            ctrlp=proxygeo[0]
            grpp=proxygeo[1]
            prep=proxygeo[2]
            proxyfinal=prep+'mesh_'
            if mc.objExists(ctrlp):
                mc.delete(ctrlp)
            if mc.objExists(ctrll):
                mc.rename(ctrll,ctrlp)
            if mc.ls(meshsP)==[]:
                mc.error(u'========未生成代理文件，请检查===========')
            if len(meshsP)>1:
                mc.error(u'==========不止一个代理文件，请检查===========')
            if mc.objExists(grpl):
                mc.delete(grpl)
            mc.rename(meshsP[0], proxyfinal)
            mc.group(proxyfinal, n=grpp)
            proxLight=self.proxyLightInfo()
            checklight=proxLight[0]
            treelights=proxLight[1]
            if checklight==1:
                for light in treelights:
                    if (shotInfo[1]+'_h') in light and (shotInfo[1]+'_p') not in light:
                        lightn=light.split('|')[-1].replace((shotInfo[1]+'_h'),(shotInfo[1]+'_p'))
                        lightn=mc.rename(light.split('|')[-1],lightn)
                        mc.parent(lightn,grpp)
            mc.parent(grpp,ctrlp)
            mc.select(ctrlp)
            mc.file((tempath+modelP),options='v=0',f=1,type='mayaBinary',preserveReferences=1,es=1)
            print '==============================='
            print u'==============渲染代理已生成==========='
            print tempath+modelP
            print '==============================='
            if server==1:
                userName = os.environ['USERNAME']
                mc.file((tempath+modelP),options='v=0',type='mayaBinary',f=1,o=1)
                projectInfo = 'Ninjago'
                fileName=mc.file(q=1,sn=1,shn=1)
                fileInfo='1|' + projectInfo + '|' + fileName + '|' + userName
                checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
                mel.eval(checkOutCmd)
                description = u'渲染代理'
                # checkIn
                mel.eval('idmtProject -checkin -description \" ' + description + '\"')
                print u'\n'
                print (u'===============!!!End 【%s】!!!===============' % (u'%s_已上传渲染代理文件' % fileName))
        else:
            mc.warning(u'===============文件结构不正确请检查===========')
            mc.error(u'===============文件结构不正确请检查===========')
        return 0
#----------------------------------------------------------------------------------------------------------#
#【nj2017】自动渲染代理
#@author:韩虹
#data：2016-6-17
    #---------------------------------------------------
    def proxyCreatCheckinF(self,server=1):
        fileName=mc.file(q=1,sn=1,shn=1)
        shotInfo=sk_infoConfig.sk_infoConfig().checkShotInfo()
        proxyInfo=self.nj17_proxyInfo()
        servpath=sk_infoConfig.sk_infoConfig().checkProjectAssetNames()
        path=self.gdc_proxyPath()
        tempath=path[0]
        serverpath=path[1]
        proxypath=path[2]
        modelH=shotInfo[0]+'_'+shotInfo[1]+'_h_rg.mb'
        modelL=shotInfo[0]+'_'+shotInfo[1]+'_l_rg.mb'
        modelP=shotInfo[0]+'_'+shotInfo[1]+'_p_rg.mb'
        check=0
        if shotInfo[0]=='nj' and proxyInfo==1 and shotInfo[2]=='h' and shotInfo[3]=='rg.mb' and os.path.exists(serverpath+modelL):
            check=1
        if shotInfo[0]=='nj' and proxyInfo==1 and shotInfo[2]=='l' and shotInfo[3]=='rg.mb' and os.path.exists(serverpath+modelH):
            check=1
        if check==1:
            mc.file(rename=(tempath+fileName))
            mc.file(save=1,type = 'mayaBinary',f = 1)
            self.proxyCreatCheckin(server)
            mc.file((tempath+fileName),options='v=0',type='mayaBinary',f=1,o=1)
        if check==0:
            pass
        return 0
#----------------------------------------------------------------------------------------------------------#
#【通用】自动创建代理结构
#@author:韩虹
#data：2016-6-17
    #---------------------------------------------------
    def proxyCreatGeo(self,typ='h'):
        GeoInfo=self.proxyGeoInfo(typ)
        objs=mc.ls(sl=1,tr=1,l=1)
        ctrl=GeoInfo[0]
        grp=GeoInfo[1]
        pre=GeoInfo[2]
        #打组
        if mc.objExists(grp)==False:
            mc.group(objs, n=grp)
        #重命名
        self.proxyRenameProxy()
        #创建ctrl
        if mc.objExists(ctrl)==False:
            mc.circle(c=(0,0,0),nr=(0,1,0),n=ctrl)
            mc.setAttr((ctrl+'.scaleX'),10)
            mc.setAttr((ctrl+'.scaleY'),10)
            mc.setAttr((ctrl+'.scaleZ'),10)
            mc.select(ctrl)
            mc.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
        #ctrl 与grp打组
        mc.parent(grp,ctrl)
        return 0
#----------------------------------------------------------------------------------------------------------#
#【通用】自动创建代理结构(根据文件名判断）
#@author:韩虹
#data：2016-6-17
    #---------------------------------------------------
    def proxyCreatGeoAuto(self):
        proxyInfo=self.nj17_proxyInfo()
        shotInfo=sk_infoConfig.sk_infoConfig().checkShotInfo()
        if shotInfo[2]  in ['h','l','p'] and  proxyInfo==1:
            self.proxyCreatGeo(shotInfo[2])
        else:
            mc.error(u'===========请检查文件名,该文件不是渲染代理编号文件============')
        return 0
#----------------------------------------------------------------------------------------------------------#
#【通用】自动重命名工具（渲染代理文件）
#@author:韩虹
#data：2016-6-17
    #---------------------------------------------------
    def proxyRenameProxy(self):
        shotInfo=sk_infoConfig.sk_infoConfig().checkShotInfo()
        proxyInfo=self.nj17_proxyInfo()
        GeoInfo=self.proxyGeoInfo(shotInfo[2])
        if shotInfo[2] not in ['h','l','p'] or proxyInfo!=1:
            mc.error(u'========请检查文件名,该文件不是渲染代理编号文件==============')
        objs=mc.ls(sl=1,tr=1,l=1)
        pre=GeoInfo[2]
        if objs:
            for obj in objs:
                chrs=mc.listRelatives(obj, c=1, type='transform', ad=1, f=1)
                objShort=obj.split('|')[-1]
                if pre not in objShort:
                    objPre=obj.split(objShort)[0]
                    objN=pre+objShort
                    mc.rename(objShort,objN)
                if chrs:
                    for chr in chrs:
                        chrShort=chr.split('|')[-1]
                        if pre not in chrShort:
                            chrN=pre+chrShort
                            mc.rename(chrShort,chrN)
        else:
            print(u'============Please Select==============')
            mc.error(u'============Please Select==============')
        return 0
#----------------------------------------------------------------------------------------------------------#
#【通用】代理灯光信息
#@author:韩虹
#data：2016-6-17
    #---------------------------------------------------
    def proxyLightInfo(self):
        objs=mc.ls(tr=1,l=1)
        trees=[]
        lightcheck=0
        for obj in objs:
            if mc.objExists(obj+'.tree') and mc.listRelatives(obj,s=1,f=1) and mc.nodeType(mc.listRelatives(obj,s=1,f=1)[0])=='VRayLightSphereShape'  :
                trees.append(obj)
        if trees:
            lightcheck=1
        return [lightcheck,trees]
#【通用】缺失贴图检测
#@author:韩虹
#data：2016-6-28
    #---------------------------------------------------
    def FileMapCheck(self):
        files=mc.ls(type='file',l=1)
        fileMapN=[]
        if files:
            for fil in files:
                if mc.objExists(fil+'.fileTextureName'):
                    maps=mc.getAttr(fil+'.fileTextureName')
                    if '${IDMT_PROJECTS}' in maps:
                        maps=maps.replace('${IDMT_PROJECTS}','//file-cluster/gdc/projects')
                    if not maps or os.path.isfile(maps)==False:
                        fileMapN.append(fil)
        if fileMapN:
            for fi in fileMapN:
                mc.warning(u'==========【%s】缺失贴图========='%fi)
            mc.error(u'==========文件中有缺失贴图，请查看警告信息=================')
        return 0







