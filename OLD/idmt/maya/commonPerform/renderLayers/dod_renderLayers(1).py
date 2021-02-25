# -*- coding: utf-8 -*-

'''
Created on 2014��1��24��

@author: shenkang
'''

import maya.cmds as mc
import maya.mel as mel

class dod_renderLayers(object):
    def __init__(self):
        pass
    
    # Occlusion层Arnold版
    # No Lights
    def dodRLAOArnoldCreate(self, layerType, selectObjType= 1 ,transMode = 1):
        print(u'===============!!!Start 【Arnold】【%s】!!!===============' % (u'%s_AO层' % layerType))
        print('Working...')
        
        from idmt.maya.commonCore.core_renderLayer import sk_renderLayerCore
        reload(sk_renderLayerCore)
        
        # 物体
        if layerType == 'CHR':
            layerName = 'CHR_AO'
        if layerType == 'BG':
            layerName = 'BG_AO' 

        rlObjs = []
        # 选取模式
        if selectObjType == 1:
            rlObjs = mc.ls(sl=1,l=1)
        
        if rlObjs:
            # 灯光
            lights = []
            if selectObjType == 0:
                lights = mc.ls(type='light',l = 1)
            
            if selectObjType == 1:
                lightsNeed = []
                for obj in rlObjs:
                    if 'light' in mc.nodeType(obj):
                        lightsNeed.append(obj)
                    else:
                        shape = mc.listRelatives(obj,c = 1 ,ni =1,f = 1)
                        if shape:
                            if 'light' in mc.nodeType(shape[0]):
                                lightsNeed.append(obj)
                    lights = lightsNeed       
    
            # 特殊处理，半透明用,网络读取
            if transMode:
                transpancyObjs = sk_renderLayerCore.sk_renderLayerCore().idmtRLTransparencyObjs()
                transpancySGNodes   =   transpancyObjs[0]
                transpancyMeshes    =   transpancyObjs[1]
                transpancyNode      =   transpancyObjs[2]
            
            if transMode == 0:
                transpancyObjs = sk_renderLayerCore.sk_renderLayerCore().idmtRLTransparencyObjsOld()
                transpancySGNodes = []
                transpancyMeshes = []
                transpancyNode = []
                if transpancyObjs:
                    for transGrp in transpancyObjs:
                        transpancySGNodes.append(transGrp[0])
                        transpancyMeshes.append(transGrp[1])
                        transpancyNode.append(transGrp[2])

            # 创建RenderLayer    
            if mc.ls(layerName):
                mc.delete(layerName)

            mc.createRenderLayer(rlObjs , name=layerName , noRecurse=1 , makeCurrent=1)
    
            # 材质
            AO_Shader = 'SHD_' + layerType + '_AO'
            if mc.ls( AO_Shader ):
                mc.delete(AO_Shader)
            AO_SG = 'SHD_' + layerType + '_AO_SG'
            if mc.ls( AO_SG ):
                mc.delete( AO_SG )
            AO_Shader = mc.shadingNode ('aiAmbientOcclusion', asShader=True, name= AO_Shader)  
            AO_SG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=( AO_SG ))
            mc.connectAttr('%s.%s' % (AO_Shader , 'outColor') , '%s.%s' % (AO_SG , 'surfaceShader'), f=True)
            # 优先全局着色
            for obj in rlObjs:
                mesh = mc.listRelatives(obj,c= 1 , ni = 1 ,type = 'mesh',f = 1)
                if mc.ls(mesh):
                    #if '_MESHES|' not in mesh[0]:
                    #    continue
                    mesh = mesh[0]
                    #print('========')
                    #print(obj.split('|')[-1])
                    try:
                        mc.sets(mesh, e=1, forceElement= AO_SG )
                    except:
                        if '.f[' not in mesh:
                            # 获取物体面数
                            obj = mc.listRelatives(mesh,p=1 , f = 1)[0]
                            faceNum = mc.polyEvaluate(obj, face=1)
                            try:
                                mc.sets((obj + u'.f[0:' + str(faceNum -1) + u']'),e=1, forceElement= AO_SG)
                            except:
                                # 该死的maybug！！！再次分解
                                print(obj + u'.f[0:' + str(int(faceNum -1)/2) + u']')
                                mc.sets((obj + u'.f[0:' + str(int(faceNum -1)/2) + u']'),e=1, forceElement= AO_SG)
                                mc.sets((obj + u'.f[' + str(int(faceNum -1)/2 + 1) + ':' + str(faceNum -1) + u']'),e=1, forceElement= AO_SG)
                        else:
                            print(u'>-------------->')
                            print(mesh)
                            # 获取面数
                            faceInfo = mesh.split('.f[')[-1]
                            if ':' in faceInfo:
                                faceInfoList = faceInfo.split(':')
                                faceNumPre = int(faceInfoList[0])
                                faceNumPos = int(faceInfoList[1][:-1])
                                # 该死的maybug！！！再次分解
                                if faceNumPos == faceNumPre + 1:
                                    mc.sets((obj + u'.f[' + str(faceNumPre) + u']'),e=1, forceElement= AO_SG)
                                    mc.sets((obj + u'.f[' + str(faceNumPos) + u']'),e=1, forceElement= AO_SG)
                                else:
                                    mc.sets((obj + u'.f[' + str(faceNumPre) + ':' + str(int(faceNumPre + (faceNumPos -faceNumPre)/2)) + u']'),e=1, forceElement= AO_SG)
                                    mc.sets((obj + u'.f[' + str(int(faceNumPre + 1 + (faceNumPos -faceNumPre)/2)) + ':' + str(faceNumPos) + u']'),e=1, forceElement= AO_SG)
                            else:
                                mc.warning(u'--------------请检测[%s]---------------'%mesh)

            #mc.sets(rlObjs, e=1, forceElement= AOSG )
            #mc.connectAttr('%s.%s' % (layerSG , 'message') , '%s.%s' % (layerName , 'shadingGroupOverride'), f=True)
    
            noNeedAsset = ['_s401001']
            
            # 特殊物体着色
            if transpancySGNodes:
                for i in range(len(transpancySGNodes)):
                    if mc.ls(transpancySGNodes[i]):
                        keySGInfo = str(i)
                        #if '_' not in transpancySGNodes[i]:
                        #    print(u'>>>>>>[注意][%s]名字需要最少有1个_分隔符'%transpancySGNodes[i])
                        #else:
                        #    keySGInfo = transpancySGNodes[i].split('_')[-2]
                        meshes = transpancyMeshes[i]
                        shaderNode = transpancyNode[i]
                        
                        # 有着色物体时才进行
                        if meshes:
                            # 对某些特殊的layerShader不处理
                            if '[food]' not in shaderNode:
                                if mc.nodeType(shaderNode) == 'layeredShader':
                                    checkAsset = 0
                                    for info in noNeedAsset:
                                        if info in meshes[0]:
                                            checkAsset = 1
                                    if checkAsset == 1:
                                        continue
                            
                            AOShader = 'SHD_' + layerType  + '_' + keySGInfo + '_AO'
                            if mc.ls( AOShader ):
                                mc.delete(AOShader)
                            AOSG = 'SHD_' + layerType  + '_' + keySGInfo + '_AO_SG'
                            if mc.ls( AOSG ):
                                mc.delete( AOSG )
                            # 创建
                            AOShader = mc.shadingNode ('aiAmbientOcclusion', asShader=True, name= AOShader) 
                            AOSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=( AOSG )) 
                            # 连接
                            mc.connectAttr('%s.%s' % (AOShader , 'outColor') , '%s.%s' % (AOSG , 'surfaceShader'), f=True)
                            # 透明连接
                            if transpancyNode[i][:6] == '[food]':
                                transValue = float(transpancyNode[i][7:])
                                mc.setAttr((AOShader + '.opacity'),transValue,transValue,transValue,type = 'double3')
                            else:
                                if mc.nodeType(transpancyNode[i].split('.')[0]) in ['layeredShader','surfaceShader']:
                                    mc.connectAttr('%s.%s' % (transpancyNode[i].split('.')[0] , 'outTransparency') , '%s.%s' % (AOShader , 'opacity'), f=True)
                                else:
                                    if mc.nodeType(transpancyNode[i].split('.')[0]) in ['ramp','file']:
                                        mc.connectAttr('%s.%s' % (transpancyNode[i].split('.')[0] , 'outColor') , '%s.%s' % (AOShader , 'opacity'), f=True)
                                    else:
                                        mc.connectAttr('%s.%s' % (transpancyNode[i].split('.')[0] , 'outAlpha') , '%s.%s' % (AOShader , 'opacity'), f=True)
                            # 着色
                            for mesh in meshes:
                                fullName = mc.ls(mesh,l =1)
                                if fullName:
                                    #if '_MESHES|' not in fullName[0]:
                                    #    continue
                                    try:
                                        mc.sets(mesh, e=1, forceElement= AOSG )
                                    except:
                                        if '.f[' not in mesh:
                                            # 获取物体面数
                                            obj = mc.listRelatives(mesh,p=1 , f = 1)[0]
                                            faceNum = mc.polyEvaluate(obj, face=1)
                                            try:
                                                mc.sets((obj + u'.f[0:' + str(faceNum -1) + u']'),e=1, forceElement= AOSG)
                                            except:
                                                # 该死的maybug！！！再次分解
                                                mc.sets((obj + u'.f[0:' + str(int(faceNum -1)/2) + u']'),e=1, forceElement= AOSG)
                                                mc.sets((obj + u'.f[' + str(int(faceNum -1)/2 + 1) + ':' + str(faceNum -1) + u']'),e=1, forceElement= AOSG)
                                        else:
                                            print(u'>-------------->')
                                            print(mesh)
                                            # 获取面数
                                            faceInfo = mesh.split('.f[')[-1]
                                            if ':' in faceInfo:
                                                faceInfoList = faceInfo.split(':')
                                                faceNumPre = int(faceInfoList[0])
                                                faceNumPos = int(faceInfoList[1][:-1])
                                                # 获取物体面数
                                                obj = mc.listRelatives(mesh,p=1 , f = 1)[0]
                                                faceNum = mc.polyEvaluate(obj, face=1)
                                                # 先判断是否完整整体
                                                if (faceNumPos - faceNumPre + 1 ) ==  faceNum:
                                                    mc.sets(obj, e=1, forceElement= AOSG )
                                                else:
                                                    # 该死的maybug！！！再次分解
                                                    if faceNumPos == faceNumPre + 1:
                                                        mc.sets((obj + u'.f[' + str(faceNumPre) + u']'),e=1, forceElement= AOSG)
                                                        mc.sets((obj + u'.f[' + str(faceNumPos) + u']'),e=1, forceElement= AOSG)
                                                    else:
                                                        mc.sets((obj + u'.f[' + str(faceNumPre) + ':' + str(int(faceNumPre + (faceNumPos -faceNumPre)/2)) + u']'),e=1, forceElement= AOSG)
                                                        mc.sets((obj + u'.f[' + str(int(faceNumPre + 1 + (faceNumPos -faceNumPre)/2)) + ':' + str(faceNumPos) + u']'),e=1, forceElement= AOSG)
                                            else:
                                                mc.warning(u'--------------请检测[%s]---------------'%mesh)
                            # mc.sets(meshes, e=1, forceElement= AOSG )
                            # Arnold Mesh处理
                            for mesh in meshes:
                                fullName = mc.ls(mesh,l =1)
                                if fullName:
                                    if '_MESHES|' not in fullName[0]:
                                        continue
                                    if mc.ls(mesh + '.aiOpaque'):
                                        mc.editRenderLayerAdjustment(mesh + '.aiOpaque')
                                        #mel.eval("editRenderLayerAdjustment \"" + mesh + ".aiOpaque\";")
                                        mc.setAttr((mesh + '.aiOpaque'),0)
    
            # 隐藏灯光
            if lights:
                for light in lights:
                    lightGrp = mc.listRelatives(light, p=1,type = 'transform' , f = 1)[0]
                    mc.editRenderLayerAdjustment(lightGrp + '.v')
                    mc.setAttr((light + '.v'), 0)
                    mc.editRenderLayerAdjustment(light + '.intensity')
                    mc.setAttr((light + '.intensity'), 0)
    
            # 层设置
            if(layerType == 'BG'):
                mc.editRenderLayerAdjustment('defaultArnoldRenderOptions.AASamples')
                mc.setAttr(('defaultArnoldRenderOptions.AASamples'), 5)
            else:
                mc.editRenderLayerAdjustment('defaultArnoldRenderOptions.AASamples')
                mc.setAttr(('defaultArnoldRenderOptions.AASamples'), 4)
            # 防止间接照明
            mc.editRenderLayerAdjustment('defaultArnoldRenderOptions.GIDiffuseSamples')
            mc.setAttr(('defaultArnoldRenderOptions.GIDiffuseSamples'), 0)
            mc.editRenderLayerAdjustment('defaultArnoldRenderOptions.GIGlossySamples')
            mc.setAttr(('defaultArnoldRenderOptions.GIGlossySamples'), 0)
            mc.editRenderLayerAdjustment('defaultArnoldRenderOptions.GIRefractionSamples')
            mc.setAttr(('defaultArnoldRenderOptions.GIRefractionSamples'), 0)
    
            # 设置
            # self.zmRLCommonConfig()
    
            # 渲染设置
            mc.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
            #mel.eval("editRenderLayerAdjustment \"defaultRenderGlobals.currentRenderer\";")
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'arnold', type='string')
            
            # 层名
            fileName = mc.file(exn=1,q=1)
            fileName = fileName.split('/')[-1].split('.')[0]
            layerImageName = fileName + layerName
            mc.editRenderLayerAdjustment('defaultRenderGlobals.imageFilePrefix')
            mc.setAttr('defaultRenderGlobals.imageFilePrefix',layerImageName,type = 'string')
            
            # 格式命名
            mc.setAttr('defaultRenderGlobals.animation',1)
            mc.setAttr('defaultRenderGlobals.putFrameBeforeExt',1)
            mc.setAttr('defaultRenderGlobals.periodInExt',1)
            mc.setAttr('defaultRenderGlobals.extensionPadding',4)
            if mc.getAttr('defaultRenderGlobals.outFormatControl') == 1:
                mc.setAttr('defaultRenderGlobals.outFormatControl',0)

            # Back To MasterLayer
            mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')
            # Unrender MasterLayer
            mel.eval(r'renderLayerEditorRenderable RenderLayerTab "defaultRenderLayer" "0";')

            # exr
            # 已经默认
    
            # 16位zip压缩
            # 已经默认
            
            print(u'===============!!!Done 【Arnold】【%s】!!!===============' % (u'%s_AO层' % layerType))
            print('\n')
        else:
            print(u'===============!!!Error 【Arnold】【%s】无物体!!!===============' % (u'%s_AO层' % layerType))
            print('\n')

    # Occlusion层Arnold版
    # No Lights
    # transMode 0 本文件读取 | 1 服务器端读取asset
    def dodRLNMArnoldCreate(self, layerType, selectObjType= 1 ,transMode = 1):
        print(u'===============!!!Start 【Arnold】【%s】!!!===============' % (u'%s_NM层' % layerType))
        print('Working...')

        from idmt.maya.commonCore.core_renderLayer import sk_renderLayerCore
        reload(sk_renderLayerCore)

        rlObjs = []
        
        # 物体
        if layerType == 'CHR':
            layerName = 'CHR_NM'
        if layerType == 'BG':
            layerName = 'BG_NM' 
        
        # 选取模式
        if selectObjType == 1:
            rlObjs = mc.ls(sl=1,l= 1)
        
        if rlObjs:
            # 灯光
            lights = []
            if selectObjType == 0:
                lights = mc.ls(type='light',l= 1)
            
            if selectObjType == 1:
                lightsNeed = []
                for obj in rlObjs:
                    if 'light' in mc.nodeType(obj):
                        lightsNeed.append(obj)
                    else:
                        shape = mc.listRelatives(obj,c = 1 ,ni =1,f = 1)
                        if shape:
                            if 'light' in mc.nodeType(shape[0]):
                                lightsNeed.append(obj)
                    lights = lightsNeed        
    
            # 特殊处理，半透明用,网络读取
            if transMode:
                transpancyObjs = sk_renderLayerCore.sk_renderLayerCore().idmtRLTransparencyObjs()
                transpancySGNodes   =   transpancyObjs[0]
                transpancyMeshes    =   transpancyObjs[1]
                transpancyNode      =   transpancyObjs[2]
            
            if transMode == 0:
                transpancyObjs = sk_renderLayerCore.sk_renderLayerCore().idmtRLTransparencyObjsOld()
                transpancySGNodes = []
                transpancyMeshes = []
                transpancyNode = []
                if transpancyObjs:
                    for transGrp in transpancyObjs:
                        transpancySGNodes.append(transGrp[0])
                        transpancyMeshes.append(transGrp[1])
                        transpancyNode.append(transGrp[2])

    
            # 创建RenderLayer   
            if mc.ls(layerName):
                mc.delete(layerName)
                
            mc.createRenderLayer(rlObjs , name=layerName , noRecurse=1 , makeCurrent=1)
    
            # 材质
            NM_Shader = 'SHD_' + layerType + '_NM'
            if mc.ls( NM_Shader ):
                mc.delete(NM_Shader)
            NM_SG = 'SHD_' + layerType + '_NM_SG'
            if mc.ls( NM_SG ):
                mc.delete( NM_SG )
            NM_Shader = mc.shadingNode ('aiUtility', asShader=True, name= NM_Shader)  
            NM_SG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=( NM_SG ))
            mc.setAttr((NM_Shader + '.shadeMode') , 2)
            mc.setAttr((NM_Shader + '.colorMode') , 3)
            mc.connectAttr('%s.%s' % (NM_Shader , 'outColor') , '%s.%s' % (NM_SG , 'surfaceShader'), f=True)
            # 优先全局着色
            for obj in rlObjs:
                mesh = mc.listRelatives(obj,ni = 1 ,type = 'mesh',f = 1)
                if mc.ls(mesh):
                    mesh = mesh[0]
                    try:
                        mc.sets(mesh, e=1, forceElement= NM_SG )
                    except:
                        if '.f[' not in mesh:
                            # 获取物体面数
                            obj = mc.listRelatives(mesh,p=1 , f = 1)[0]
                            faceNum = mc.polyEvaluate(obj, face=1)
                            try:
                                mc.sets((obj + u'.f[0:' + str(faceNum -1) + u']'),e=1, forceElement= NM_SG)
                            except:
                                print('------')
                                print(obj.split('|')[-1])
                                # 该死的maybug！！！再次分解
                                mc.sets((obj + u'.f[0:' + str(int(faceNum -1)/2) + u']'),e=1, forceElement= NM_SG)
                                mc.sets((obj + u'.f[' + str(int(faceNum -1)/2 + 1) + ':' + str(faceNum -1) + u']'),e=1, forceElement= NM_SG)
                        else:
                            # 获取面数
                            faceInfo = mesh.split('.f[')[-1]
                            if ':' in faceInfo:
                                faceInfoList = faceInfo.split(':')
                                faceNumPre = int(faceInfoList[0])
                                faceNumPos = int(faceInfoList[1][:-1])
                                # 该死的maybug！！！再次分解
                                if faceNumPos == faceNumPre + 1:
                                    print('------')
                                    print(obj.split('|')[-1])
                                    mc.sets((obj + u'.f[' + str(faceNumPre) + u']'),e=1, forceElement= NM_SG)
                                    mc.sets((obj + u'.f[' + str(faceNumPos) + u']'),e=1, forceElement= NM_SG)
                                else:
                                    print('------')
                                    print(obj.split('|')[-1])
                                    mc.sets((obj + u'.f[' + str(faceNumPre) + ':' + str(int(faceNumPre + (faceNumPos -faceNumPre)/2)) + u']'),e=1, forceElement= NM_SG)
                                    mc.sets((obj + u'.f[' + str(int(faceNumPre + 1 + (faceNumPos -faceNumPre)/2)) + ':' + str(faceNumPos) + u']'),e=1, forceElement= NM_SG)
                            else:
                                mc.warning(u'--------------请检测[%s]---------------'%mesh)

            #mc.sets(rlObjs, e=1, forceElement= NMSG )
            #mc.connectAttr('%s.%s' % (layerSG , 'message') , '%s.%s' % (layerName , 'shadingGroupOverride'), f=True)

            noNeedAsset = ['_s401001']

            # 特殊物体着色,同一类物体强制一个材质球
            if transpancySGNodes:
                for i in range(len(transpancySGNodes)):
                    if mc.ls(transpancySGNodes[i]):
                        keySGInfo = str(i)
                        #if '_' not in transpancySGNodes[i]:
                        #    print(u'>>>>>>[注意][%s]名字需要最少有1个_分隔符'%transpancySGNodes[i])
                        #else:
                        #    keySGInfo = transpancySGNodes[i].split('_')[-2]
                        meshes = transpancyMeshes[i]
                        shaderNode = transpancyNode[i]
                        # 有着色物体时才进行
                        if meshes:
                            # 对某些特殊的layerShader不处理
                            if '[food]' not in shaderNode:
                                if mc.nodeType(shaderNode) == 'layeredShader':
                                    checkAsset = 0
                                    for info in noNeedAsset:
                                        if info in meshes[0]:
                                            checkAsset = 1
                                    if checkAsset == 1:
                                        continue
                            NMShader = 'SHD_' + layerType  + '_' + keySGInfo + '_NM'
                            if mc.ls( NMShader ):
                                mc.delete(NMShader)
                            NMSG = 'SHD_' + layerType  + '_' + keySGInfo + '_NM_SG'
                            if mc.ls( NMSG ):
                                mc.delete( NMSG )
                            # 创建
                            NMShader = mc.shadingNode ('aiUtility', asShader=True, name= NMShader) 
                            NMSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=( NMSG )) 
                            mc.setAttr((NMShader + '.shadeMode') , 2)
                            mc.setAttr((NMShader + '.colorMode') , 3)
                            # 连接
                            mc.connectAttr('%s.%s' % (NMShader , 'outColor') , '%s.%s' % (NMSG , 'surfaceShader'), f=True)
                            # 透明连接
                            if transpancyNode[i][:6] == '[food]':
                                transValue = float(transpancyNode[i][7:])
                                mc.setAttr((NMShader + '.opacity'),transValue)
                            else:
                                if mc.nodeType(transpancyNode[i].split('.')[0]) in  ['layeredShader','surfaceShader']:
                                    mc.connectAttr('%s.%s' % (transpancyNode[i].split('.')[0] , 'outTransparencyR') , '%s.%s' % (NMShader , 'opacity'), f=True)
                                else:
                                    if mc.nodeType(transpancyNode[i].split('.')[0]) in ['ramp','file']:
                                        mc.connectAttr('%s.%s' % (transpancyNode[i].split('.')[0] , 'outColorR') , '%s.%s' % (NMShader , 'opacity'), f=True)
                                    else:
                                        mc.connectAttr('%s.%s' % (transpancyNode[i].split('.')[0] , 'outAlpha') , '%s.%s' % (NMShader , 'opacity'), f=True)
                                    #mc.connectAttr('%s.%s' % (transpancyNode[i].split('.')[0] , 'outAlpha') , '%s.%s' % (NMShader , 'opacity'), f=True)
                            # 着色

                            for mesh in meshes:
                                fullName = mc.ls(mesh,l =1)
                                if fullName:
                                    #if '_MESHES|' not in fullName[0]:
                                    #    continue
                                    try:
                                        mc.sets(mesh, e=1, forceElement= NMSG )
                                    except:
                                        if '.f[' not in mesh:
                                            # 获取物体面数
                                            obj = mc.listRelatives(mesh,p=1 , f = 1)[0]
                                            faceNum = mc.polyEvaluate(obj, face=1)
                                            try:
                                                mc.sets((obj + u'.f[0:' + str(faceNum -1) + u']'),e=1, forceElement= NMSG)
                                            except:
                                                # 该死的maybug！！！再次分解
                                                mc.sets((obj + u'.f[0:' + str(int(faceNum -1)/2) + u']'),e=1, forceElement= NMSG)
                                                mc.sets((obj + u'.f[' + str(int(faceNum -1)/2 + 1) + ':' + str(faceNum -1) + u']'),e=1, forceElement= NMSG)
                                        else:
                                            #print(u'>-------------->')
                                            #print(mesh)
                                            # 获取面数
                                            faceInfo = mesh.split('.f[')[-1]
                                            if ':' in faceInfo:
                                                faceInfoList = faceInfo.split(':')
                                                faceNumPre = int(faceInfoList[0])
                                                faceNumPos = int(faceInfoList[1][:-1])
                                                # 获取物体面数
                                                obj = mc.listRelatives(mesh,p=1 , f = 1)[0]
                                                faceNum = mc.polyEvaluate(obj, face=1)
                                                # 先判断是否完整整体
                                                if (faceNumPos - faceNumPre + 1 ) ==  faceNum:
                                                    mc.sets(obj, e=1, forceElement= NMSG )
                                                # 该死的maybug！！！再次分解
                                                else:
                                                    if faceNumPos == faceNumPre + 1:
                                                        mc.sets((obj + u'.f[' + str(faceNumPre) + u']'),e=1, forceElement= NMSG)
                                                        mc.sets((obj + u'.f[' + str(faceNumPos) + u']'),e=1, forceElement= NMSG)
                                                    else:
                                                        mc.sets((obj + u'.f[' + str(faceNumPre) + ':' + str(int(faceNumPre + (faceNumPos -faceNumPre)/2)) + u']'),e=1, forceElement= NMSG)
                                                        mc.sets((obj + u'.f[' + str(int(faceNumPre + 1 + (faceNumPos -faceNumPre)/2)) + ':' + str(faceNumPos) + u']'),e=1, forceElement= NMSG)
                                            else:
                                                mc.warning(u'--------------请检测[%s]---------------'%mesh)
                            #mc.sets(meshes, e=1, forceElement= NMSG )
                            # Arnold Mesh处理
                            for mesh in meshes:
                                fullName = mc.ls(mesh,l =1)
                                if fullName:
                                    if '_MESHES|' not in fullName[0]:
                                        continue
                                    if mc.ls(mesh + '.aiOpaque'):
                                        mc.editRenderLayerAdjustment( mesh + '.aiOpaque')
                                        #mel.eval("editRenderLayerAdjustment \"" + mesh + ".aiOpaque\";")
                                        mc.setAttr((mesh + '.aiOpaque'),0)
    

            # 隐藏灯光
            if lights:
                for light in lights:
                    lightGrp = mc.listRelatives(light, p=1,type = 'transform' , f = 1)[0]
                    mc.editRenderLayerAdjustment(lightGrp + '.v')
                    mc.setAttr((light + '.v'), 0)
                    mc.editRenderLayerAdjustment(light + '.intensity')
                    mc.setAttr((light + '.intensity'), 0)
    
            # 层设置
            if layerType == 'BG':
                mc.editRenderLayerAdjustment('defaultArnoldRenderOptions.AASamples')
                mc.setAttr('defaultArnoldRenderOptions.AASamples', 5)
            else:
                mc.editRenderLayerAdjustment('defaultArnoldRenderOptions.AASamples')
                mc.setAttr('defaultArnoldRenderOptions.AASamples', 4)
            # 防止间接照明
            mc.editRenderLayerAdjustment('defaultArnoldRenderOptions.GIDiffuseSamples')
            mc.setAttr('defaultArnoldRenderOptions.GIDiffuseSamples', 0)
            mc.editRenderLayerAdjustment('defaultArnoldRenderOptions.GIGlossySamples')
            mc.setAttr('defaultArnoldRenderOptions.GIGlossySamples', 0)
            mc.editRenderLayerAdjustment('defaultArnoldRenderOptions.GIRefractionSamples')
            mc.setAttr('defaultArnoldRenderOptions.GIRefractionSamples', 0)
    
            # 设置
            # self.zmRLCommonConfig()
    
            # 渲染设置
            mc.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
            #mel.eval("editRenderLayerAdjustment \"defaultRenderGlobals.currentRenderer\";")
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'arnold', type='string')
    
            # 格式命名
            mc.setAttr('defaultRenderGlobals.animation',1)
            mc.setAttr('defaultRenderGlobals.putFrameBeforeExt',1)
            mc.setAttr('defaultRenderGlobals.periodInExt',1)
            mc.setAttr('defaultRenderGlobals.extensionPadding',4)
            if mc.getAttr('defaultRenderGlobals.outFormatControl') == 1:
                mc.setAttr('defaultRenderGlobals.outFormatControl',0)
            
            # 层名
            fileName = mc.file(exn=1,q=1)
            fileName = fileName.split('/')[-1].split('.')[0]
            layerImageName = fileName + layerName
            mc.editRenderLayerAdjustment('defaultRenderGlobals.imageFilePrefix')
            mc.setAttr('defaultRenderGlobals.imageFilePrefix',layerImageName,type = 'string')
            
            # Back To MasterLayer
            mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')
            # Unrender MasterLayer
            mel.eval(r'renderLayerEditorRenderable RenderLayerTab "defaultRenderLayer" "0";')
            
            # exr
            # 已经默认
    
            # 16位zip压缩
            # 已经默认

            
            print(u'===============!!!Done 【Arnold】【%s】!!!===============' % (u'%s_NM层' % layerType))
            print('\n')
        else:
            print(u'===============!!!Error 【Arnold】【%s】无物体!!!===============' % (u'%s_NM层' % layerType))
            print('\n')
            
    # transMode 0 本文件读取 | 1 服务器端读取asset
    def dodRlCoAOVsArnold(self, layerName = 'char_fish', selectObjType= 0 ,transMode = 1 ,batch = 0):
        print(u'===============!!!Start 【Arnold】【%s】!!!===============' % (u'%s_层' % layerName))
        
        from idmt.maya.commonCore.core_renderLayer import sk_renderLayerCore
        reload(sk_renderLayerCore)
        from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
        reload(sk_infoConfig)
        from idmt.maya.commonCore.core_mayaCommon import sk_hbExportCam
        reload(sk_hbExportCam)

        # 选取模式
#        rlObjs = []
#        if mc.ls('MDGGRPMASTER'):
#            rlObjs = ['MDGGRPMASTER']
#        if selectObjType == 1:
#            rlObjs = mc.ls(sl=1,l= 1)
#韩虹修改，加入cLUSTER_GRP，加入相机导入
# 选取模式
        rlObjs = []
        if mc.ls('MDGGRPMASTER') or mc.ls('cLUSTER_GRP'):
            rlObjs = mc.ls('MDGGRPMASTER',l=1)+mc.ls('cLUSTER_GRP',l=1)
        if selectObjType == 1:
            rlObjs = mc.ls(sl=1,l= 1)
          
#######################################################        
        rlObjsAll = rlObjs
        
        # 处理地面
        needGrp = ''
        floor = mc.ls('*:*_floor_*',type = 'transform',l= 1 )
        # 无则导入
        baseGroundPath = '//file-cluster/GDC/Projects/DiveollyDive4/DiveollyDive4_Scratch/TD/fishes_file/'
        if not floor:
            shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
            if shotInfo[1] == '016' or shotInfo[1] == '016a':
                filePath = baseGroundPath + '016/do4_ground.ma'
                mc.file(filePath , i = 1 , namespace = 'do4Ground')
                floor = mc.ls('*:*_floor_*',type = 'transform',l= 1 )
        if floor:
            needGrp = mc.listRelatives(floor,p=1,type = 'transform',f = 1)[0]
        if needGrp:
            rlObjsAll = rlObjs + [needGrp]
        
        # 分层开始
        if rlObjs:
            
            # 灯光
            lights = []
            if selectObjType == 0:
                lights = mc.ls(type='light')
            
            if selectObjType == 1:
                lightsNeed = []
                for obj in rlObjs:
                    if 'light' in mc.nodeType(obj):
                        lightsNeed.append(obj)
                    else:
                        shape = mc.listRelatives(obj,c = 1 ,ni =1,f = 1)
                        if shape:
                            if 'light' in mc.nodeType(shape[0]):
                                lightsNeed.append(obj)
                    lights = lightsNeed        
    
            # 特殊处理，半透明用,网络读取
            if transMode:
                transpancyObjs = sk_renderLayerCore.sk_renderLayerCore().idmtRLTransparencyObjs()
                transpancySGNodes   =   transpancyObjs[0]
                transpancyMeshes    =   transpancyObjs[1]
                transpancyNode      =   transpancyObjs[2]
            
            if transMode == 0:
                transpancyObjs = sk_renderLayerCore.sk_renderLayerCore().idmtRLTransparencyObjsOld()
                transpancySGNodes = []
                transpancyMeshes = []
                transpancyNode = []
                if transpancyObjs:
                    for transGrp in transpancyObjs:
                        transpancySGNodes.append(transGrp[0])
                        transpancyMeshes.append(transGrp[1])
                        transpancyNode.append(transGrp[2])

            # skyDomeLight
            skyDomeLight = 'idmt_skyDome'
            if mc.ls(skyDomeLight):
                mc.delete(skyDomeLight)
            skyTransform = 'idmt_skyDome_transform'
            if mc.ls(skyTransform):
                mc.delete(skyTransform)
            #skyDomeLight = mc.createNode('aiSkyDomeLight' ,name = skyDomeLight)
            skyDomeLight = mc.shadingNode('aiSkyDomeLight',asUtility = 1 , name = skyDomeLight)
            skyTransform = mc.listRelatives(skyDomeLight , f = 1, p = 1)[0]
            skyTransform = mc.rename(skyTransform , 'idmt_skyDome_transform')
            #mc.connectAttr('%s.%s' % ('transform1' , 'instObjGroups') , '%s.%s' % ('defaultLightSet' , 'dagSetMembers'), f=True)
            mc.connectAttr("%s.instObjGroups" % skyTransform, "defaultLightSet.dagSetMembers", nextAvailable=True)
            mc.setAttr((skyDomeLight + '.intensity'),0.6)
            mc.setAttr((skyDomeLight + '.aiSamples'),3.0)
            
            
            # 创建RenderLayer   
            if mc.ls(layerName):
                mc.delete(layerName)
            
            # 建立层
            mc.createRenderLayer((rlObjsAll + [skyDomeLight]) , name=layerName , noRecurse=1 , makeCurrent=1)

            # 处理群组专用
            if mc.ls('MDGGRPMASTER'):
                # 修正贴图
                meshes = mc.listRelatives('MDGGRPMASTER',ad = 1,type = 'mesh',f =1 )
                '''
                chooseObj = mc.listRelatives(meshes[0],p = 1 ,type ='transform',f = 1)[0]
                mc.select(chooseObj)
                import idmt.maya.DOD.DODIV.Maya.do_renderTools_uicmd as rtuc
                rtuc.imporove_crowdFishMat()
                mc.select(cl =1)
                '''
                # 参考相机
                sk_hbExportCam.sk_hbExportCam().camServerReference()  
                # smoothSet
                # 设置属性
                value_aiSubdivIterations = 3
                value_aiSubdivPixelError = 1
                for mesh in meshes:
                    mc.setAttr((mesh + '.aiSubdivType'),1)
                    mc.setAttr((mesh + '.aiSubdivIterations'),value_aiSubdivIterations)
                    mc.setAttr((mesh + '.aiSubdivAdaptiveMetric'),0)
                    mc.setAttr((mesh + '.aiSubdivPixelError'),value_aiSubdivPixelError)
                
            # 处理石头和地面
            if needGrp:
                meshesNeed = mc.listRelatives(needGrp,ad = 1 ,type = 'mesh',f =1 )
                if meshesNeed:
                    for mesh in meshesNeed:
                        mc.editRenderLayerAdjustment(mesh + '.primaryVisibility')
                        mc.setAttr((mesh + '.primaryVisibility'),0)
            
            # layerImageName
            shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
            fileName = mc.file(exn=1,q=1)
            fileName = fileName.split('/')[-1].split('.')[0]
            layerImageName = fileName + layerName
            #layerImageName = shotInfo[0] + '_' + str(shotInfo[1]) + '_' + str(shotInfo[2]) + '_l1Sccolor_lr_c001_' + layerName
            mc.editRenderLayerAdjustment('defaultRenderGlobals.imageFilePrefix')
            mc.setAttr('defaultRenderGlobals.imageFilePrefix',layerImageName,type = 'string')
####加入相机
            if mc.ls('CAM:cam_'+ shotInfo[1]+'_'+ shotInfo[2]+'_bake')==[]:          
                sk_hbExportCam.sk_hbExportCam().camServerReference(2)              
############################
            # setting
            mc.editRenderLayerAdjustment('defaultArnoldDriver.halfPrecision')
            mc.setAttr('defaultArnoldDriver.halfPrecision',1)
            mc.editRenderLayerAdjustment('defaultArnoldDriver.autocrop')
            mc.setAttr('defaultArnoldDriver.autocrop',1)
            mc.editRenderLayerAdjustment('defaultArnoldRenderOptions.AASamples')
            mc.setAttr('defaultArnoldRenderOptions.AASamples',4)
            mc.editRenderLayerAdjustment('defaultArnoldRenderOptions.GIDiffuseSamples')
            mc.setAttr('defaultArnoldRenderOptions.GIDiffuseSamples',0)
            mc.editRenderLayerAdjustment('defaultArnoldRenderOptions.GIGlossySamples')
            mc.setAttr('defaultArnoldRenderOptions.GIGlossySamples',0)
            mc.editRenderLayerAdjustment('defaultArnoldRenderOptions.GIRefractionSamples')
            mc.setAttr('defaultArnoldRenderOptions.GIRefractionSamples',0)
            mc.editRenderLayerAdjustment('defaultArnoldRenderOptions.sssBssrdfSamples')
            mc.setAttr('defaultArnoldRenderOptions.sssBssrdfSamples',3)
            mc.editRenderLayerAdjustment('defaultArnoldRenderOptions.lock_sampling_noise')
            mc.setAttr('defaultArnoldRenderOptions.lock_sampling_noise',1)
            mc.editRenderLayerAdjustment('defaultArnoldRenderOptions.textureAutomip')
            mc.setAttr('defaultArnoldRenderOptions.textureAutomip',1)
            mc.editRenderLayerAdjustment('defaultArnoldRenderOptions.textureAcceptUnmipped')
            mc.setAttr('defaultArnoldRenderOptions.textureAcceptUnmipped',1)
            mc.editRenderLayerAdjustment('defaultArnoldRenderOptions.use_existing_tiled_textures')
            mc.setAttr('defaultArnoldRenderOptions.use_existing_tiled_textures',1)
            
            # shader
            # occ
            AOShader = 'SHD_AO'
            if mc.ls( AOShader ):
                mc.delete(AOShader)
            AOSG = 'SHD_AO_SG'
            if mc.ls( AOSG ):
                mc.delete( AOSG )
            AOShader = mc.shadingNode ('aiAmbientOcclusion', asShader=True, name= AOShader)  
            AOSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=( AOSG ))
            mc.connectAttr('%s.%s' % (AOShader , 'outColor') , '%s.%s' % (AOSG , 'surfaceShader'), f=True)
            # nomal
            NMShader = 'SHD_NM'
            if mc.ls( NMShader ):
                mc.delete(NMShader)
            NMSG = 'SHD_NM_SG'
            if mc.ls( NMSG ):
                mc.delete( NMSG )
            NMShader = mc.shadingNode ('aiUtility', asShader=True, name= NMShader)  
            NMSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=( NMSG ))
            mc.setAttr((NMShader + '.shadeMode') , 2)
            mc.setAttr((NMShader + '.colorMode') , 3)
            mc.connectAttr('%s.%s' % (NMShader , 'outColor') , '%s.%s' % (NMSG , 'surfaceShader'), f=True)
            # fresnel
            FNShader = 'SHD_Fresnel'
            if mc.ls( FNShader ):
                mc.delete(FNShader)
            FNRamp = 'SHD_Fresnel_ramp'
            if mc.ls( FNRamp ):
                mc.delete(FNRamp)
            FNSample = 'SHD_Fresnel_Sample'
            if mc.ls( FNSample ):
                mc.delete(FNSample)
            FNSG = 'SHD_Fresnel_SG'
            if mc.ls( FNSG ):
                mc.delete( FNSG )
            FNShader = mc.shadingNode ('aiUtility', asShader=True, name= FNShader)  
            FNRamp = mc.shadingNode ('ramp', asShader=True, name= FNRamp)  
            FNSample = mc.shadingNode ('samplerInfo', asShader=True, name= FNSample)  
            FNSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=( FNSG ))
            mc.removeMultiInstance((FNRamp + '.colorEntryList[1]') , b = 1)
            mc.setAttr((FNShader + '.shadeMode'),2)
            mc.setAttr((FNRamp + '.interpolation'),3)
            mc.setAttr((FNRamp + '.colorEntryList[2].position'),1)
            mc.setAttr((FNRamp + '.colorEntryList[0].position'),0)
            mc.setAttr((FNRamp + '.colorEntryList[2].color'),0,0,0,type = 'double3')
            mc.setAttr((FNRamp + '.colorEntryList[0].color'),1,1,1,type = 'double3')
            mc.connectAttr('%s.%s' % (FNShader , 'outColor') , '%s.%s' % (FNSG , 'surfaceShader'), f=True)
            mc.connectAttr('%s.%s' % (FNSample , 'facingRatio') , '%s.%s' % (FNRamp , 'uCoord'), f=True)
            mc.connectAttr('%s.%s' % (FNSample , 'facingRatio') , '%s.%s' % (FNRamp , 'vCoord'), f=True)
            mc.connectAttr('%s.%s' % (FNRamp , 'outColor') , '%s.%s' % (FNShader , 'color'), f=True)

            # dirver
            mc.setAttr('defaultArnoldDriver.mergeAOVs',1)
            # renderpass
            # Z
            ZArnoldPass = 'aiAOV_Z'
            if mc.ls(ZArnoldPass) :
                if mc.nodeType(ZArnoldPass) =='aiAOV':
                    pass
                else:
                    mc.delete(ZArnoldPass)
                    mc.createNode('aiAOV',name = ZArnoldPass)
            else:
                mc.createNode('aiAOV',name = ZArnoldPass )
            mc.setAttr((ZArnoldPass + '.name'),'Z',type = 'string')
            mc.setAttr((ZArnoldPass + '.type'),4)
            # occ
            occArnoldPass = 'aiAOV_occ'
            if mc.ls(occArnoldPass) :
                if mc.nodeType(occArnoldPass) =='aiAOV':
                    pass
                else:
                    mc.delete(occArnoldPass)
                    mc.createNode('aiAOV',name = occArnoldPass)
            else:
                mc.createNode('aiAOV',name = occArnoldPass )
            mc.setAttr((occArnoldPass + '.name'),'occ',type = 'string')
            mc.setAttr((occArnoldPass + '.type'),5)
            # normal
            nmArnoldPass = 'aiAOV_normal'
            if mc.ls(nmArnoldPass) :
                if mc.nodeType(nmArnoldPass) =='aiAOV':
                    pass
                else:
                    mc.delete(nmArnoldPass)
                    mc.createNode('aiAOV',name = nmArnoldPass)
            else:
                mc.createNode('aiAOV',name = nmArnoldPass )
            mc.setAttr((nmArnoldPass + '.name'),'normal',type = 'string')
            mc.setAttr((nmArnoldPass + '.type'),5)
            # frese1
            fresenlArnoldPass = 'aiAOV_fresnel'
            if mc.ls(fresenlArnoldPass) :
                if mc.nodeType(fresenlArnoldPass) =='aiAOV':
                    pass
                else:
                    mc.delete(fresenlArnoldPass)
                    mc.createNode('aiAOV',name = fresenlArnoldPass)
            else:
                mc.createNode('aiAOV',name = fresenlArnoldPass )
            mc.setAttr((fresenlArnoldPass + '.name'),'fresnel',type = 'string')
            mc.setAttr((fresenlArnoldPass + '.type'),5)
            # aiAOVFilter
            # closset
            aiAOVFilter_Closset =  'defaultArnoldFilter_Closset'
            if mc.ls(aiAOVFilter_Closset) :
                if mc.nodeType(aiAOVFilter_Closset) =='aiAOVFilter':
                    pass
                else:
                    mc.delete(aiAOVFilter_Closset)
                    mc.createNode('aiAOVFilter',name = aiAOVFilter_Closset)
            else:
                mc.createNode('aiAOVFilter',name = aiAOVFilter_Closset )

            # 连接
            # Z
            try:
                mc.disconnectAttr('%s.%s' % ('defaultArnoldDriver' , 'message') , '%s.%s' % (ZArnoldPass , 'outputs[0].driver'))
            except:
                pass
            mc.connectAttr('%s.%s' % ('defaultArnoldDriver' , 'message') , '%s.%s' % (ZArnoldPass , 'outputs[0].driver'), f=True)
            try:
                mc.disconnectAttr('%s.%s' % ( aiAOVFilter_Closset , 'message') , '%s.%s' % (ZArnoldPass, 'outputs[0].filter'))
            except:
                pass
            mc.connectAttr('%s.%s' % ( aiAOVFilter_Closset , 'message') , '%s.%s' % (ZArnoldPass, 'outputs[0].filter'), f=True)
            try:
                mc.disconnectAttr('%s.%s' % ( ZArnoldPass , 'message') , '%s.%s' % ('defaultArnoldRenderOptions' , 'aovList[0]'))
            except:
                pass
            mc.connectAttr('%s.%s' % ( ZArnoldPass , 'message') , '%s.%s' % ('defaultArnoldRenderOptions' , 'aovList[0]'), f=True)
            # occ
            try:
                mc.disconnectAttr('%s.%s' % ('defaultArnoldDriver' , 'message') , '%s.%s' % (occArnoldPass , 'outputs[0].driver'))
            except:
                pass
            mc.connectAttr('%s.%s' % ('defaultArnoldDriver' , 'message') , '%s.%s' % (occArnoldPass , 'outputs[0].driver'), f=True)
            try:
                mc.disconnectAttr('%s.%s' % ( 'defaultArnoldFilter' , 'message') , '%s.%s' % (occArnoldPass, 'outputs[0].filter'))
            except:
                pass
            mc.connectAttr('%s.%s' % ( 'defaultArnoldFilter' , 'message') , '%s.%s' % (occArnoldPass, 'outputs[0].filter'), f=True)
            try:
                mc.disconnectAttr('%s.%s' % ( AOShader , 'outColor') , '%s.%s' % (occArnoldPass, 'defaultValue'))
            except:
                pass
            mc.connectAttr('%s.%s' % ( AOShader , 'outColor') , '%s.%s' % (occArnoldPass, 'defaultValue'), f=True)
            mc.setAttr((AOShader + '.samples'),4)
            try:
                mc.disconnectAttr('%s.%s' % ( occArnoldPass , 'message') , '%s.%s' % ('defaultArnoldRenderOptions' , 'aovList[1]'))
            except:
                pass
            mc.connectAttr('%s.%s' % ( occArnoldPass , 'message') , '%s.%s' % ('defaultArnoldRenderOptions' , 'aovList[1]'), f=True)
            # normal
            try:
                mc.disconnectAttr('%s.%s' % ('defaultArnoldDriver' , 'message') , '%s.%s' % (nmArnoldPass , 'outputs[0].driver'))
            except:
                pass
            mc.connectAttr('%s.%s' % ('defaultArnoldDriver' , 'message') , '%s.%s' % (nmArnoldPass , 'outputs[0].driver'), f=True)
            try:
                mc.disconnectAttr('%s.%s' % ( 'defaultArnoldFilter' , 'message') , '%s.%s' % (nmArnoldPass , 'outputs[0].filter'))
            except:
                pass
            mc.connectAttr('%s.%s' % ( 'defaultArnoldFilter' , 'message') , '%s.%s' % (nmArnoldPass , 'outputs[0].filter'), f=True)
            try:
                mc.disconnectAttr('%s.%s' % ( NMShader , 'outColor') , '%s.%s' % (nmArnoldPass, 'defaultValue'))
            except:
                pass
            mc.connectAttr('%s.%s' % ( NMShader , 'outColor') , '%s.%s' % (nmArnoldPass, 'defaultValue'), f=True)
            try:
                mc.disconnectAttr('%s.%s' % ( nmArnoldPass , 'message') , '%s.%s' % ('defaultArnoldRenderOptions' , 'aovList[2]'))
            except:
                pass
            mc.connectAttr('%s.%s' % ( nmArnoldPass , 'message') , '%s.%s' % ('defaultArnoldRenderOptions' , 'aovList[2]'), f=True)
            # frese
            try:
                mc.disconnectAttr('%s.%s' % ('defaultArnoldDriver' , 'message') , '%s.%s' % (fresenlArnoldPass , 'outputs[0].driver'))
            except:
                pass
            mc.connectAttr('%s.%s' % ('defaultArnoldDriver' , 'message') , '%s.%s' % (fresenlArnoldPass , 'outputs[0].driver'), f=True)
            try:
                mc.disconnectAttr('%s.%s' % ( 'defaultArnoldFilter' , 'message') , '%s.%s' % (fresenlArnoldPass , 'outputs[0].filter'))
            except:
                pass
            mc.connectAttr('%s.%s' % ( 'defaultArnoldFilter' , 'message') , '%s.%s' % (fresenlArnoldPass , 'outputs[0].filter'), f=True)
            try:
                mc.disconnectAttr('%s.%s' % ( FNShader , 'outColor') , '%s.%s' % (fresenlArnoldPass, 'defaultValue'))
            except:
                pass
            mc.connectAttr('%s.%s' % ( FNShader , 'outColor') , '%s.%s' % (fresenlArnoldPass, 'defaultValue'), f=True)
            try:
                mc.disconnectAttr('%s.%s' % ( fresenlArnoldPass , 'message') , '%s.%s' % ('defaultArnoldRenderOptions' , 'aovList[3]'))
            except:
                pass
            mc.connectAttr('%s.%s' % ( fresenlArnoldPass , 'message') , '%s.%s' % ('defaultArnoldRenderOptions' , 'aovList[3]'), f=True)
            
            # 单独的地面occ
            if needGrp:
                # 建立层
                layerName = 'occShadow'
                if mc.ls(layerName):
                    mc.delete(layerName)
                mc.createRenderLayer(rlObjsAll , name=layerName , noRecurse=1 , makeCurrent=1)

                needMeshes = []
                if rlObjs:
                    for grp in rlObjs:
                        meshes = mc.listRelatives(grp,ad = 1 ,ni =1 ,type = 'mesh',f =1 )
                        needMeshes = needMeshes + meshes
                needMeshes = list(set(needMeshes))
                if needMeshes:
                    for mesh in needMeshes:
                        mc.editRenderLayerAdjustment(mesh + '.primaryVisibility')
                        mc.setAttr((mesh + '.primaryVisibility'),0)

                # renderpass
                mc.editRenderLayerAdjustment(ZArnoldPass + '.enabled')
                mc.setAttr((ZArnoldPass + '.enabled'),0)
                mc.editRenderLayerAdjustment(nmArnoldPass + '.enabled')
                mc.setAttr((nmArnoldPass + '.enabled'),0)
                mc.editRenderLayerAdjustment(fresenlArnoldPass + '.enabled')
                mc.setAttr((fresenlArnoldPass + '.enabled'),0)
                
                
            # 层名
            fileName = mc.file(exn=1,q=1)
            fileName = fileName.split('/')[-1].split('.')[0]
            layerImageName = fileName + layerName
            mc.editRenderLayerAdjustment('defaultRenderGlobals.imageFilePrefix')
            mc.setAttr('defaultRenderGlobals.imageFilePrefix',layerImageName,type = 'string')
                
            # Back To MasterLayer
            mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')
            # Unrender MasterLayer
            mc.setAttr("defaultRenderLayer.renderable",0)

            # 渲染Camera
            shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
            camInfo = ('*:*_' + str(shotInfo[1]) + '_' + str(shotInfo[2]) + '_baked*')
            cameras =mc.ls(camInfo,type = 'camera')
            if cameras:
                for camShape in cameras:
                    #isRef = mc.referenceQuery(camShape,isNodeReferenced = 1)
                    #if isRef:
                    mc.setAttr((camShape + '.renderable'),0)
            mc.setAttr('CAM:stereoCameraRightShape.renderable',1)
            mc.setAttr('CAM:stereoCameraLeftShape.renderable',1)
            try:
                mc.setAttr(('perspShape.renderable'),0)
            except:
                pass

            print(u'===============!!!Done 【Arnold】【%s】!!!===============' % (u'%s_层' % layerName))
            print('\n')
            
            # 批处理另存
            if batch:
                pathLocal = sk_infoConfig.sk_infoConfig().checkRenderLayerLocalPath().replace('D:','E:')
                mc.sysFile(pathLocal, makeDir=True)
                # 保存
                fileNameOld = mc.file(exn = 1, q = 1).split('/')[-1]
                fileNameNew = pathLocal + shotInfo[0]+'_'+shotInfo[1]+'_'+shotInfo[2]+'_l4_'+shotInfo[3]+'_lr_c001.mb'
                mc.file(rename= fileNameNew )
                print('-----')
                print(fileNameOld)
                print(fileNameNew)
                mc.file(s = 1, f = 1)
                print('\n')
                print(u'Please Go To This Path To Find The Last RenderLayer Files')
                print(u'------------------------------------------------------------------------')
                print(pathLocal)
                print(u'------------------------------------------------------------------------')
                print('\n')
                
        else:
            print(u'===============!!!Error 【Arnold】【%s】无物体!!!===============' % (u'%s_层' % layerName))
            print('\n')
            