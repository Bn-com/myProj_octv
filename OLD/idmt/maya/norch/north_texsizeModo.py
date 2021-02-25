#python 
'''
Created on: 2015-6-12
Created for Modo

@author: liangyu
'''

import lx
import os

def north_SETtexture(button):
    path=''
    type=button
    try:
        filename= lx.eval("query layerservice model.curName ?")
        filever=filename.split('_')[1]
        path='Z:\\Projects\\North\\Project\\modomap\\sets\\'+filever+'\\map\\'
        
        if os.path.exists(path)==0:
            lx.out('please make sure existing the path of map')
            
    except:
        lx.out("please open a file")
        #关闭所有被选择项
        lx.eval("select.drop item")
        lx.eval("select.type vertex")
    
    
    selectionID = lx.eval("query sceneservice mask.N ?")
    msskgrp=[]    
    for x in range(0,selectionID):
        mask=lx.evalN("query sceneservice mask.children ? %d" % x)
        msskgrp.append(mask)
     
    t_imageMap=[]
    if msskgrp:
        for z in msskgrp:
            for y in z:
                if(y[:8]=='imageMap'):
                    t_imageMap.append(y)  
    
    imagename= []
    
    #path='M:\\sourceimages\\'
    
    lx.out(path)
    for x in t_imageMap:    
        Iname=lx.eval("query sceneservice imageMap.name ? %s" % x)
        lx.eval("select.subItem %s set textureLayer;render;environment;light;camera;scene;replicator;mediaClip;txtrLocator" % x)
        name=Iname.split('(')[0].replace(' ',"")
        newname=''
        if type=='half':
            if name.split('_')[-1]=='half':
                pass
            else:
                if name.split('_')[-1]=='quarter':                
                    newname=name.replace("quarter","half")
                    if os.path.isfile(path+newname+'.jpg') or os.path.isfile(path+newname+'.png') or os.path.isfile(path+newname+'.tga') or os.path.isfile(path+newname+'.tif') or os.path.isfile(path+newname+'.hdr'):                
                        if os.path.isfile(path+newname+'.jpg'):       
                            lx.eval("clip.addStill \"%s%s.jpg\"" % (path, newname))
                            lx.eval("texture.setIMap {%s:videoStill001}" % newname)
                        if os.path.isfile(path+newname+'.png'):
                            lx.eval("clip.addStill \"%s%s.png\"" % (path, newname))
                            lx.eval("texture.setIMap {%s:videoStill001}" % newname)
                        if os.path.isfile(path+newname+'.tga'):
                            lx.eval("clip.addStill \"%s%s.tga\"" % (path, newname))
                            lx.eval("texture.setIMap {%s:videoStill001}" % newname)
                        if os.path.isfile(path+newname+'.tif'):
                            lx.eval("clip.addStill \"%s%s.tif\"" % (path, newname))
                            lx.eval("texture.setIMap {%s:videoStill001}" % newname) 
                        if os.path.isfile(path+newname+'.iff'):                        
                            pass
                            lx.eval("texture.setIMap {%s:videoStill001}" % newname)  
                else:
                    newname=name+'_half'
                    if os.path.isfile(path+newname+'.jpg'):       
                        lx.eval("clip.addStill \"%s%s.jpg\"" % (path, newname))
                        lx.eval("texture.setIMap {%s:videoStill001}" % newname)
                    if os.path.isfile(path+newname+'.png'):
                        lx.eval("clip.addStill \"%s%s.png\"" % (path, newname))
                        lx.eval("texture.setIMap {%s:videoStill001}" % newname)
                    if os.path.isfile(path+newname+'.tga'):
                        lx.eval("clip.addStill \"%s%s.tga\"" % (path, newname))
                        lx.eval("texture.setIMap {%s:videoStill001}" % newname)
                    if os.path.isfile(path+newname+'.tif'):
                        lx.eval("clip.addStill \"%s%s.tif\"" % (path, newname))
                        lx.eval("texture.setIMap {%s:videoStill001}" % newname) 
                    if os.path.isfile(path+newname+'.iff'):
                        pass
                        lx.eval("texture.setIMap {%s:videoStill001}" % newname)  
        if type=='quarter':
            if name.split('_')[-1]=='quarter':
                pass
            else:
                if name.split('_')[-1]=='half':                
                    newname=name.replace("half","quarter")                                    
                    if os.path.isfile(path+newname+'.jpg'):       
                        lx.eval("clip.addStill \"%s%s.jpg\"" % (path, newname))
                        lx.eval("texture.setIMap {%s:videoStill001}" % newname)
                    if os.path.isfile(path+newname+'.png'):
                        lx.eval("clip.addStill \"%s%s.png\"" % (path, newname))
                        lx.eval("texture.setIMap {%s:videoStill001}" % newname)
                    if os.path.isfile(path+newname+'.tga'):
                        lx.eval("clip.addStill \"%s%s.tga\"" % (path, newname))
                        lx.eval("texture.setIMap {%s:videoStill001}" % newname)
                    if os.path.isfile(path+newname+'.tif'):
                        lx.eval("clip.addStill \"%s%s.tif\"" % (path, newname))
                        lx.eval("texture.setIMap {%s:videoStill001}" % newname) 
                    if os.path.isfile(path+newname+'.iff'):
                        pass                                    
                else:
                    newname=name+'_quarter'
                    if os.path.isfile(path+newname+'.jpg'):       
                        lx.eval("clip.addStill \"%s%s.jpg\"" % (path, newname))
                        lx.eval("texture.setIMap {%s:videoStill001}" % newname)
                    if os.path.isfile(path+newname+'.png'):
                        lx.eval("clip.addStill \"%s%s.png\"" % (path, newname))
                        lx.eval("texture.setIMap {%s:videoStill001}" % newname)
                    if os.path.isfile(path+newname+'.tga'):
                        lx.eval("clip.addStill \"%s%s.tga\"" % (path, newname))
                        lx.eval("texture.setIMap {%s:videoStill001}" % newname)
                    if os.path.isfile(path+newname+'.tif'):
                        lx.eval("clip.addStill \"%s%s.tif\"" % (path, newname))
                        lx.eval("texture.setIMap {%s:videoStill001}" % newname) 
                    if os.path.isfile(path+newname+'.iff'):
                        pass                                                                             
        if type=='full':
            if name.split('_')[-1]!='quarter' or name.split('_')[-1]!='half' :
                pass
            if name.split('_')[-1]=='half':              
                newname=name.replace("_half","")
                if os.path.isfile(path+newname+'.jpg') or os.path.isfile(path+newname+'.png') or os.path.isfile(path+newname+'.tga') or os.path.isfile(path+newname+'.tif') or os.path.isfile(path+newname+'.hdr'):                
                    lx.eval("texture.setIMap {%s:videoStill001}" % newname)
            if name.split('_')[-1]=='quarter':                
                newname=name.replace("_quarter","")
                if os.path.isfile(path+newname+'.jpg') or os.path.isfile(path+newname+'.png') or os.path.isfile(path+newname+'.tga') or os.path.isfile(path+newname+'.tif') or os.path.isfile(path+newname+'.hdr'):                
                    lx.eval("texture.setIMap {%s:videoStill001}" % newname)     
                                                                                                   
    lx.out("---------It's done------------------")

def fvaluedialog(title,name):
    #显示一个输入浮点值的对话框，并返回这个值,如果按取消按钮则返回None
    try:
        if not lx.eval("query scriptsysservice userValue.isDefined ? vvv"):
            lx.eval("user.defNew vvv string temporary")
            lx.eval("user.def vvv username {%s}" % name)
            lx.eval("user.def vvv dialogname {%s}" % title)
            #lx.eval("user.def vvv min 0.0")
            lx.eval("user.value vvv half")
        if(lx.eval("user.value vvv") == None):
            return lx.eval("user.value vvv ?")
    except:
        return None

s = fvaluedialog("texture size","full/half/quarter")
lx.out(s)
'''
if s=='full':
    north_SETtexture(s) 
else:
    if s!='half' or s!='quarter':
        sys.exit("LXe_FAILED:please make sure the spelling right")       

if s=='half':
    north_SETtexture(s) 
else:
    if s!='full' or s!='quarter':
        sys.exit("LXe_FAILED:please make sure the spelling right")  
    
if s=='quarter':
    north_SETtexture(s) 
else:
    if s!='half' or s!='full':
        sys.exit("LXe_FAILED:please make sure the spelling right")  
'''
north_SETtexture(s)    
#关闭所有被选择项
lx.eval("select.drop item")
lx.eval("select.type vertex")

   

    

      
    
   
      


