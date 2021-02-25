#-*- coding: utf-8 -*-
'''
Created on 2014年9月15��

@author: zhaozhongjie
'''
import PtaFile as rj
import os,sys
if 'MAYA_APP_DIR' in os.environ:
    from pymel.core import *

# path_S =r"D:\FastRun.pta"

def cleanDatas(datas):
    rv = {}
    for d in datas.keys():
        if '|' in d:    continue
        name,attribute = d.split(':')[-1].split('.')
        dat = datas[d]
        if rv.has_key(name):
            rv[name][attribute]=dat
        else:
            rv[name] = {attribute:dat}
    return rv

def deleteCheckGroup(showError):
    if 'MAYA_APP_DIR' not in os.environ:    return          #    判断是否在Maya里运行
    if not showError:
        try:
            delete('AnimLibrary_CheckGroup')
        except:
            pass
        
def importAnim(path_S,ifctl=0,ifConnect=0,curveRange=[],showError=0):
    '''
    1.合并，清理数据。
        数据清理到 merge_datas 这个字典里，格式：
        {  'Master':
            {
                'rotateX':[1,0,null,...],
                'rotateY':[1,0,null,...]
            }
        }
        
    2.传递动画
        ifctl=0 有两种情况:一、手动选择一些控制器导动画，二、选择物体，获得namespace，导动画
    '''
    if 'MAYA_APP_DIR' not in os.environ:    return          #    判断是否在Maya里运行
    selectObj = selected()
    if len(selectObj)==0:
        confirmDialog(message=u'请选择一个角色！！')
        return
    
# 1.合并，清理数据。
    datas = rj.PtaRW().readFile(path_S)
    a_datas = datas["zzj_anim"]
    n_datas = datas["zzj_non_anim"]
    
    merge_datas = dict(a_datas, **n_datas)                  #    合并两个字典
    clean_datas = cleanDatas(merge_datas)                   #    规整后的 K帧 数据
    
# 2.传递动画
    try:
        undoInfo(openChunk=True)                            #    传动画期间不记录操作
        transAnim(selectObj,clean_datas,ifConnect,ifctl,curveRange,showError)
    finally:
        undoInfo(closeChunk=True)
    

def transAnim(selectObj,datas,ifConnect=0,ifctl=0,curveRange=[],showError=0):
    wrongInfo = []                                  # 错误信息
    for n in datas:
        data = datas[n]
        for d in data:
            name,att,value = n , d , data[d]                #    数据中的 名字，属性，值
            targetObj = selectObj[0].namespace()+name       #    场景中的目标物体

# 0. 如果选择控制器，则检测数据库里有没有动画，如果没有，就跳过
            if not objExists(targetObj):    continue
            if ifctl and targetObj not in selectObj:  continue 
        
# 1. 创建一个小球
            sphere = polySphere()[0]
            if not objExists('AnimLibrary_CheckGroup'):
                group( em=True, name='AnimLibrary_CheckGroup' )
            sphere.setParent('AnimLibrary_CheckGroup')
                
# 2. 如果小球上没有那个属性，则添加那个属性    
            sphere.setAttr( att, 0, keyable =1,  force=1 )
                
# 3. 把value的值 setKey 到小球上
            # ============================== K 帧数据 ==============================
            if isinstance(value,  list ):
                for val in value:
                    f = val[0]
                    setKeyframe(sphere, v=val[1], at=att, t=f)
                    if val[2]!=None:    keyTangent(sphere,edit=1,t=(f,f),itt= val[2])
                    if val[3]!=None:    keyTangent(sphere,edit=1,t=(f,f),ott= val[3])
                    if val[4]!=None:    keyTangent(sphere,edit=1,t=(f,f), wt= val[4])   # 设置wl前，要先开wt
                    if val[4]!=None:    keyTangent(sphere,edit=1,t=(f,f), wl= val[4])
                    if val[5]!=None:    keyTangent(sphere,edit=1,t=(f,f), ia= val[5])
                    if val[6]!=None:    keyTangent(sphere,edit=1,t=(f,f), oa= val[6])
                    if val[7]!=None:    keyTangent(sphere,edit=1,t=(f,f), iw= val[7])
                    if val[8]!=None:    keyTangent(sphere,edit=1,t=(f,f), ow= val[8])
            # ============================== 非 K 帧数据 ==============================
            else:
                setKeyframe(sphere, v=value, at=att,)

# 4. 曲线调成循环的模式
            setInfinity(sphere,at=att, poi='constant' )
                
# 5. bake小球,复制动画曲线
            # ---复制曲线
            if curveRange!=[]:
                bakeResults( sphere , t=curveRange, attribute =att )
                copyKey( sphere, attribute=att ,t = curveRange)
            else :
                copyKey( sphere, attribute=att )
            # ---粘贴曲线
            try:
                pasteKey( targetObj, attribute=att ,connect = ifConnect , t = (currentTime(),currentTime()))
            except:
                wrongInfo.append( "copy %s.%s to %s.%s failed"%(sphere,att,targetObj,att))
# 6. 删除小球
            if not showError:
                delete('AnimLibrary_CheckGroup')
    
    if showError:   
        confirmDialog(message=u'请查看Script Editor里的反馈信息')
        print '\n'.join(wrongInfo)
        confirmDialog(message=u'请注意outliner里的AnimLibrary_CheckGroup这个组，检查完了，可以删除')


def exportAnim(path , ifctl=0 , ifPlayBlast=0):
    data = {}
    data['angularUnit'] = optionVar['workingUnitAngular']
    data['linearUnit'] = optionVar['workingUnitLinear']
    data['mayaVersion'] = about(v=1)
    data['timeUnit'] = optionVar['workingUnitTime']
    
    zzj_anim = {}
    zzj_non_anim = {}
    
    if len(selected())==0:  
        confirmDialog(message=u'请选择控制器')
        return
    
# 导出的控制器    
    selectObj = selected()                     
    allContrls = []
    if ifctl:                                               # 1.用户框选的控制器
        allContrls = selectObj
    else:                                                   # 2.用户选择的角色的控制器  
        topParent = selected()[0].getParent(-1)
        allContrls = ls(topParent,dag=1,type='transform')
    select(cl=1)                                            # 3.清空选择

    for ac in allContrls:
        for att in ac.listAttr(k=1,v=1):                             #    keyable 和 visible的属性
            for name,curve in att.connections(c=1):
                if  nodeType(curve)[:9] == 'animCurve':
                    for t,v in keyframe(curve,q=1,tc=1,vc=1):
                        tmp = keyTangent(curve,q=1,t=(t,t),ia= 1,oa=1,iw=1,ow=1,itt=1,ott=1,wl=1)
                        info = [t,v,tmp[4],tmp[5],tmp[6],tmp[0],tmp[1],tmp[2],tmp[3]]
                        if not zzj_anim.has_key(att.name()):
                            zzj_anim[att.name()] = [info]
                        else:
                            zzj_anim[att.name()].append(info)
            if not zzj_anim.has_key(att.name()):
                zzj_non_anim[att.name()] = att.get()

    data['zzj_anim'] = zzj_anim
    data['zzj_non_anim'] = zzj_non_anim
    
    rj.PtaRW().writeFile(path,data)    
    
# PlayBlast,截图
    if ifPlayBlast:
        # 1. 关闭Attribute Editor 和 Channel Box
        attr = mel.getUIComponentDockControl("Attribute Editor",0)
        chan = mel.getUIComponentDockControl("Channel Box / Layer Editor",0)
        if dockControl(attr, q=1, visible=1)==1 and dockControl(attr, q=1, floating=1)==0:
            dockControl(attr, e=1, visible=0)
        if dockControl(chan, q=1, visible=1)==1 and dockControl(chan, q=1, floating=1)==0:
            dockControl(chan, e=1, visible=0)
        
        # 2. playBlaste
        avi = path[:-4]+'.avi'
        try:
            playblast(f=avi,format="avi", compression ='None',viewer=0 ,forceOverwrite = 1 , widthHeight = [640,360],orn=0,percent=100)
        except:
            confirmDialog(message=u'AVI 文件被占用，写入失败,请依次尝试如下步骤：\n1.关闭此程序。\n2.关闭相关播放器。\n3.重启Maya。\n4.重启计算机。')
            select(selectObj)
            return
        # 3. 转码
        
        ffmpeg = os.path.join( os.path.dirname(__file__),'ffmpeg.exe')
        new = avi[:-4] + '_.avi'
        bmp = avi[:-4] + '.bmp'
        ffmpegCMD = '%s -y -i %s -c:v libx264 -pix_fmt yuv420p -b 5000k %s'%(ffmpeg,avi,new)
        os.system(ffmpegCMD)
        os.remove(avi)
        os.rename(new,avi)    
        
        # 4. 截图
        ffmpegCMD = '%s -y -i %s -filter:v "crop=360:360:140:0" -s 60x60 %s'%(ffmpeg,avi,bmp)
        os.system(ffmpegCMD)

        
        
        
    
    select(selectObj)      
