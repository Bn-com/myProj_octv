# -*- coding: utf-8 -*-
import maya.cmds as cmds
import maya.mel as mel
import os as os
def edo_findCachePathFromFileName():
    cachePath='Z:/Projects/WAWA/Project/data/crowd/'
    character=''
    animation=''
    cf=cmds.file(sn=1,shn=1,q=1)
    tmp=cf.split('_')
    if len(tmp)==5 and tmp[1]=='library' and tmp[3]=='dy':
        all=tmp[2].split('0')
        chr=all[0]+'0'+all[1][0]
        if chr=='man01':
            character='c001001man'
        if chr=='man02':
            character='c001002man'
        if chr=='man03':
            character='c001003man'
        if chr=='woman01':
            character='c002001women'
        if chr=='woman02':
            character='c002002women'
        if chr=='woman03':
            character='c002003women'
        print character
        if character=='':
            return False
        zero=''
        if len(all)==3:
            zero='0'
            animation=all[1].replace(chr[len(chr)-1],'')+zero+all[2]
        if len(all)==2:
            zero=''
            animation=all[1].replace(chr[len(chr)-1],'')+zero
        print animation
        outCachePath=cachePath+character
        outCacheName=animation
        return [outCachePath,outCacheName]
    else:
        return False

def edo_findCachePathFromChrName():
    cachePath='Z:/Projects/WAWA/Project/data/crowd/'
    character=''
    cf=cmds.file(sn=1,shn=1,q=1)
    tmp=cf.split('_')
    if len(tmp)==5 and tmp[4]=='cache.ma':
        chr=tmp[1]
        chrCachePath=cachePath+chr
        return chrCachePath
    else:
        return False
        
def edo_createBodyGeometryCache():
    chrs=cmds.ls('wa_c*:MESHES')
    if chrs==None:
        cmds.confirmDialog( title='群组文件不规范', message='此群组文件有多余的角色存在!', button='知道了!',defaultButton='Yes', cancelButton='No', dismissString='No')
        return False
    if len(chrs)==1:
        outCs=edo_findCachePathFromFileName()
        if outCs==False:
            cmds.confirmDialog( title='群组文件不规范', message='此群组文件名不规范，请另存为<wa_library_chrXXanimXX_dy_cXXX.ma>!', button='知道了!',defaultButton='Yes', cancelButton='No', dismissString='No')
            return False
        chr=chrs[0]
        tmp=chr.split(':')
        if len(tmp)==2:
            nameSpace=tmp[0]
            #output body cache
            meshsSetName=nameSpace+':'+'MESHES'
            if cmds.objExists(meshsSetName):
                meshes=cmds.sets(meshsSetName,q=1)
                if meshes==None:
                    cmds.confirmDialog( title='群组文件不规范', message='此角色名为MESHES的set没有存入要导出cache的模型,反馈给环节负责人!', button='知道了!',defaultButton='Yes', cancelButton='No', dismissString='No')
                    return False
                bodycachepath=outCs[0]+'/body/'
                bodycachename=outCs[1]
                cmds.select(meshes,r=1)
                mel.eval('doCreateGeometryCache 5 { "2", "1", "10", "OneFilePerFrame", "1", "'+bodycachepath+'","0","'+bodycachename+'","0", "add", "0", "1", "1","0","1","mcc" }')
            else:
                cmds.confirmDialog( title='群组文件不规范', message='此角色没有建立名为MESHES的set,反馈给环节负责人!', button='知道了!',defaultButton='Yes', cancelButton='No', dismissString='No')
                return False
        else:
            cmds.confirmDialog( title='群组文件不规范', message='角色名称空间不正确!', button='知道了!',defaultButton='Yes', cancelButton='No', dismissString='No')
            return False
        meshs=cmds.sets('MESHES',q=1)
        cmds.select(meshs,r=1)
    else:
        cmds.confirmDialog( title='群组文件不规范', message='此群组文件有多余的角色存在!', button='知道了!',defaultButton='Yes', cancelButton='No', dismissString='No')
        return False


def edo_createHairGeometryCache():
    chrs=cmds.ls('wa_c*:CHN')
    if chrs==None:
        cmds.confirmDialog( title='群组文件不规范', message='此群组文件有多余的角色存在!', button='知道了!',defaultButton='Yes', cancelButton='No', dismissString='No')
        return False
    if len(chrs)==1:
        outCs=edo_findCachePathFromFileName()
        if outCs==False:
            cmds.confirmDialog( title='群组文件不规范', message='此群组文件名不规范，请另存为<wa_library_manXXanimXX_dy_cXXX.ma 或 wa_library_womanXXanimXX_dy_cXXX.ma>!', button='知道了!',defaultButton='Yes', cancelButton='No', dismissString='No')
            return False
        chr=chrs[0]
        tmp=chr.split(':')
        if len(tmp)==2:
            nameSpace=tmp[0]
            #output hair cahce
            chnSetName=nameSpace+':'+'CHN'
            if cmds.objExists(chnSetName):
                chns=cmds.sets(chnSetName,q=1)
                if chns==None:
                    cmds.confirmDialog( title='群组文件不规范', message='此角色名为CHN的set没有存入要导出cache的模型,反馈给环节负责人!', button='知道了!',defaultButton='Yes', cancelButton='No', dismissString='No')
                    return False
                haircachepath=outCs[0]+'/hair/'
                haircachename=outCs[1]
                cmds.select(chns,r=1)
                mel.eval('doCreateGeometryCache 5 { "2", "1", "10", "OneFilePerFrame", "1", "'+haircachepath+'","0","'+haircachename+'","0", "add", "0", "1", "1","0","1","mcc" }')
            else:
                cmds.confirmDialog( title='群组文件不规范', message='此角色没有建立名为MESHES的set,反馈给环节负责人!', button='知道了!',defaultButton='Yes', cancelButton='No', dismissString='No')
                return False
        else:
            cmds.confirmDialog( title='群组文件不规范', message='角色名称空间不正确!', button='知道了!',defaultButton='Yes', cancelButton='No', dismissString='No')
            return False
        meshs=cmds.sets('MESHES',q=1)
        cmds.select(meshs,r=1)
    else:
        cmds.confirmDialog( title='群组文件不规范', message='此群组文件有多余的角色存在!', button='知道了!',defaultButton='Yes', cancelButton='No', dismissString='No')
        return False


def edo_findSpFile(path):
    #path=chrHairCachePath
    allfile=os.listdir(path)
    if allfile==None:
        return False
    xmls=[]
    for f in allfile:
        if '.xml' in f:
            xmls.append(f)
    return xmls

def edo_connectAllStringFromList(list):
    #list=chns
    st=''
    for l in list:
        if st=='':
            st='"'+l+'"'+','
        else:
            if l==list[len(list)-1]:
                st=st+'"'+l+'"'
            else:
                st=st+'"'+l+'",'
    return st

def edo_importHairGeometryCache():
    #input hair cahce
    chrCachePath=edo_findCachePathFromChrName()
    chrHairCachePath=chrCachePath+'/hair/'
    imcfs=edo_findSpFile(chrHairCachePath)
    if imcfs==False or imcfs==[]:
        cmds.confirmDialog( title='群组文件不规范', message='该角色毛发还没有创建过cache到网上DATA/CROWD目录,请先创建!', button='知道了!',defaultButton='Yes', cancelButton='No', dismissString='No')
        return False
    imcf=chrHairCachePath+imcfs[0]
    if chrCachePath==False:
        cmds.confirmDialog( title='群组文件不规范', message='此群组文件名不规范，请检查文件名是否为<wa_cXXXXXXxxxx_h_ms_cache.ma>!', button='知道了!',defaultButton='Yes', cancelButton='No', dismissString='No')
        return False
    chnSetName='CHN'
    if cmds.objExists(chnSetName):
        chns=cmds.sets(chnSetName,q=1)
        if chns==None:
            cmds.confirmDialog( title='群组文件不规范', message='此角色名为CHN的set没有存入要导入cache的模型,反馈给环节负责人!', button='知道了!',defaultButton='Yes', cancelButton='No', dismissString='No')
            return False
        geos='{'+edo_connectAllStringFromList(chns)+'}'
        mel.eval('doImportCacheFile("'+imcf+'","XML",'+geos+',{});')
        cmds.select(chns,r=1)
        mel.eval("zwOptimizeGeoCache;")
        nodes=cmds.listHistory(chns[0])
        bodyCache=edo_findNodeByType(nodes,'cacheFile')
        cmds.rename(bodyCache[0],'hairCache')
    else:
        cmds.confirmDialog( title='群组文件不规范', message='此角色没有建立名为CHN的set,反馈给环节负责人!', button='知道了!',defaultButton='Yes', cancelButton='No', dismissString='No')
        return False
        
        
def edo_importBodyGeometryCache():
    #input body cahce
    chrCachePath=edo_findCachePathFromChrName()
    chrHairCachePath=chrCachePath+'/body/'
    imcfs=edo_findSpFile(chrHairCachePath)
    if imcfs==False or imcfs==[]:
        cmds.confirmDialog( title='群组文件不规范', message='该角色毛发还没有创建过cache到网上DATA/CROWD目录,请先创建!', button='知道了!',defaultButton='Yes', cancelButton='No', dismissString='No')
        return False
    imcf=chrHairCachePath+imcfs[0]
    if chrCachePath==False:
        cmds.confirmDialog( title='群组文件不规范', message='此群组文件名不规范，请检查文件名是否为<wa_cXXXXXXxxxx_h_ms_cache.ma>!', button='知道了!',defaultButton='Yes', cancelButton='No', dismissString='No')
        return False
    meshSetName='MESHES'
    if cmds.objExists(meshSetName):
        meshes=cmds.sets(meshSetName,q=1)
        if meshes==None:
            cmds.confirmDialog( title='群组文件不规范', message='此角色名为MESHES的set没有存入要导入cache的模型,反馈给环节负责人!', button='知道了!',defaultButton='Yes', cancelButton='No', dismissString='No')
            return False
        geos='{'+edo_connectAllStringFromList(meshes)+'}'
        mel.eval('doImportCacheFile("'+imcf+'","XML",'+geos+',{});')
        cmds.select(meshes,r=1)
        mel.eval("zwOptimizeGeoCache;")
        nodes=cmds.listHistory(meshes[0])
        bodyCache=edo_findNodeByType(nodes,'cacheFile')
        cmds.rename(bodyCache[0],'bodyCache')
    else:
        cmds.confirmDialog( title='群组文件不规范', message='此角色没有建立名为MESHES的set,反馈给环节负责人!', button='知道了!',defaultButton='Yes', cancelButton='No', dismissString='No')
        return False
        
        
def edo_findNodeByType(nodes,type):
    n=[]
    for node in nodes:
        if cmds.nodeType(node)==type:
            n.append(node)
    return n
        

        
def edo_findBodyCacheNode():
    bodyCacheNode=[]
    allcf=cmds.ls(type='cacheFile')
    for cf in allcf:
        cp=cmds.getAttr(cf+'.cachePath')
        if '/body/' in cp:
            bodyCacheNode.append(cf)
    print bodyCacheNode
    return bodyCacheNode
    
def edo_findHairCacheNode():
    hairCacheNode=[]
    allcf=cmds.ls(type='cacheFile')
    for cf in allcf:
        cp=cmds.getAttr(cf+'.cachePath')
        if '/hair/' in cp:
            hairCacheNode.append(cf)
    print hairCacheNode
    return hairCacheNode

##rigging the cache file
def edo_wawa_rigTheCacheFile():
    if cmds.objExists('Master'):
        cmds.confirmDialog( title='error', message='Master ctrl is already exists,please delete it before click this button!', button='got it!',defaultButton='Yes', cancelButton='No', dismissString='No')
        return 0
    if cmds.objExists("hairCache") and cmds.objExists("bodyCache"):
        cmds.circle(o=1,nr=[0,1,0],r=2.5,n='Master')
        edo_addCacheRigAttribute()
        cmds.setAttr('bodyCache.preCycle',100)
        cmds.setAttr('bodyCache.postCycle',100)
        cmds.setAttr('hairCache.preCycle',100)
        cmds.setAttr('hairCache.postCycle',100)
        cmds.createNode("plusMinusAverage",n="CacheOffsetPlugs")
        cmds.createNode("multiplyDivide",n="CacheOffsetMultiply")
        cmds.connectAttr("time1.outTime","CacheOffsetMultiply.input1X",f=1)
        cmds.connectAttr("CacheOffsetMultiply.outputX","CacheOffsetPlugs.input3D[0].input3Dx",f=1)
        cmds.connectAttr("CacheOffsetPlugs.output3Dx","bodyCache.time",f=1)
        cmds.connectAttr("CacheOffsetPlugs.output3Dx","hairCache.time",f=1)
        cmds.connectAttr("Master.timeScale","CacheOffsetMultiply.input2X",f=1)
        cmds.connectAttr("Master.timeOffset","CacheOffsetPlugs.input3D[1].input3Dx",f=1)
        cmds.connectAttr("Master.reverse","bodyCache.reverse",f=1)
        cmds.connectAttr("Master.reverse","hairCache.reverse",f=1)
        cmds.connectAttr("Master.oscillate","bodyCache.oscillate",f=1)
        cmds.connectAttr("Master.oscillate","hairCache.oscillate",f=1)
        cmds.connectAttr("Master.multiThread","bodyCache.multiThread",f=1)
        cmds.connectAttr("Master.multiThread","hairCache.multiThread",f=1)
        if cmds.objExists('CacheEx'):
            cmds.delete('CacheEx')
        txt=open('//file-cluster/GDC/Resource/Support/Maya/extra/Rigging_Simulation/python/edo/project/wawa/expression/cacheEx.txt','r')
        expressionTxt=txt.read()
        txt.close()
        cmds.expression(n='cacheEx',s= expressionTxt,ae=1,uc='all')
    else:
        cmds.confirmDialog( title='顺序错误', message='此角色还未导入bodyCache和hairCache!', button='知道了!',defaultButton='Yes', cancelButton='No', dismissString='No')
        return 0
    return 1
    
def edo_addCacheRigAttribute():
    if not cmds.objExists("Master"):
        cmds.confirmDialog( title='error', message='Master is not exists,please add it!', button='got it!',defaultButton='Yes', cancelButton='No', dismissString='No')
        return 0;
    if not cmds.attributeQuery("cacheSelect",node="Master",ex=1):
        cmds.addAttr('Master',ln='cacheSelect',at='enum',en='0:1')
        cmds.setAttr('Master.cacheSelect',cb=1,k=0)
    if not cmds.attributeQuery("dirtyAttr",node="Master",ex=1):
        cmds.addAttr('Master',ln='dirtyAttr',at='long')
        cmds.setAttr('Master.dirtyAttr',cb=0,k=0)
    if not cmds.attributeQuery("timeScale",node="Master",ex=1):
        cmds.addAttr('Master',ln='timeScale',at='double')
        cmds.setAttr('Master.timeScale',1,k=1) 
    if not cmds.attributeQuery("timeOffset",node="Master",ex=1):
        cmds.addAttr('Master',ln='timeOffset',at='double')
        cmds.setAttr('Master.timeOffset',k=1)
    if not cmds.attributeQuery("reverse",node="Master",ex=1):
        cmds.addAttr('Master',ln='reverse',at='bool')
        cmds.setAttr('Master.reverse',k=1)
    if not cmds.attributeQuery("oscillate",node="Master",ex=1):
        cmds.addAttr('Master',ln='oscillate',at='bool')
        cmds.setAttr('Master.oscillate',k=1)  
    if not cmds.attributeQuery("multiThread",node="Master",ex=1):
        cmds.addAttr('Master',ln='multiThread',at='bool')
        cmds.setAttr('Master.multiThread',k=1)
    for i in range(0,20):
        if not cmds.attributeQuery("cacheEndTime"+str(i),node="Master",ex=1):
            cmds.addAttr('Master',ln="cacheEndTime"+str(i),at='long')
            cmds.setAttr('Master.cacheEndTime'+str(i),k=0)
        
def edo_connectAnimCurve():
    animCurves=cmds.ls(type='animCurveTL')
    for ac in animCurves:
        cmds.connectAttr('animCacheOffsetPlugs.output3Dx',ac+'.input',f=1)
        
##rig the cache file

def wawa_riggingAndSimulationTool():
    if cmds.window('wawa_croudGeometryCacheMaker',ex=1):
        cmds.deleteUI('wawa_croudGeometryCacheMaker')
    cmds.window('wawa_croudGeometryCacheMaker',t='wawa_croudGeometryCacheMaker',w=400,h=120)
    cmds.columnLayout('wawa_croudGeometryCacheMakerColumnLayout',adjustableColumn=True)
    cmds.tabLayout('wawa_croudGeometryCacheMakerTabLayout')
    cmds.columnLayout('SIMULATION',adjustableColumn=True)
    cmds.frameLayout( 'wawa_croudGeometryCacheMakerFrame',label='wawa群组解算',borderStyle='in',cll=True)
    cmds.columnLayout('wawa_croudGeometryCacheMakerFrameColumnLayout',adjustableColumn=True,bgc=[0.5,0.4,0.2],rs=10)
    cmds.button('wawa_createBodyCache',l='创建身体cache到数据库',bgc=[0.3,0.2,0.05],c="edo_createBodyGeometryCache()")
    cmds.button('wawa_createHairCache',l='创建头发cache到数据库',bgc=[0.3,0.2,0.05],c="edo_createHairGeometryCache()")
    cmds.button('wawa_importBodyCache',l='导入并合并的身体cache',bgc=[0.3,0.2,0.05],c='edo_importBodyGeometryCache()')
    cmds.button('wawa_importHairCache',l='导入并合并的头发cache',bgc=[0.3,0.2,0.05],c='edo_importHairGeometryCache()')
    cmds.button('wawa_rigCacheFile',l='添加群组文件Master控制器',bgc=[0.3,0.2,0.05],c='edo_wawa_rigTheCacheFile()')
    cmds.window('wawa_croudGeometryCacheMaker',e=1,w=180,h=120)
    cmds.showWindow('wawa_croudGeometryCacheMaker')
    cmds.window('wawa_croudGeometryCacheMaker',e=1,w=180,h=230)

wawa_riggingAndSimulationTool()