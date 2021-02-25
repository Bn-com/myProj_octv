# -*- coding: utf-8 -*-
'''
Created on 2014-7-25

@author: liangyu
'''

import maya.cmds as mc
import sys


def sksavefile(spe):
    
    con=mc.confirmDialog( title=u'请确认', message=u'确定看清楚了，不是手快了', button=['Yes','No'], defaultButton='Yes', cancelButton='No', dismissString='No' )
    if con=='Yes':
        space=mc.workspace(q=1,fn=1)
        filenames=mc.file(q=1,sceneName=1,shortName=1)
        
        buff=filenames.split('_')
        
        pro=buff[0]
        EP=buff[1]
        SC=buff[2]
        
        path= space+'/scenes/'
        
        filename = "sk_"+EP+"_"+SC+"_"+spe+"_lr_c001.mb"
        
        mc.file(rename=path+filename)
        mc.file(save=1)
        
    else:
        print u'笨死了'



def sk4_seperateUITools():
    ui = '//file-cluster/GDC/Resource/Support/Maya/projects/Strawberry4/sk4_seperatefile.myuis'
    if mc.window('sk4_seperateTools', ex=1):
        mc.deleteUI('sk4_seperateTools')
    mui = mc.loadUI(f=ui)

    mc.window("sk4_seperateTools", e=1, tlc=(10, 10))
    mc.showWindow(mui)
     
    mc.radioButton("MRBG_Ridio",e=1,onc='sk4_seperateTools.sksavefile(\'MRBG\')')
    mc.radioButton("MRCHR_Ridio",e=1,onc='sk4_seperateTools.sksavefile(\'MRCHR\')')
    mc.radioButton("MRhair_Ridio",e=1,onc='sk4_seperateTools.sksavefile(\'MRhair\')')
    mc.radioButton("SWBG_Ridio",e=1,onc='sk4_seperateTools.sksavefile(\'SWBG\')')
    mc.radioButton("SWCHR_Ridio",e=1,onc='sk4_seperateTools.sksavefile(\'SWCHR\')')   
    mc.radioButton("SWRGB_Ridio",e=1,onc='sk4_seperateTools.sksavefile(\'SWRGB\')')
                   
                
                

  