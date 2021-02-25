#-*- coding: utf-8 -*-
'''
Created on 2014-1-13
@contact:     66372484@qq.com
@deffield    updated: Updated
@author: zhaozhongjie
'''

class MyClass(object):
    '''
    //    load
    nodePreset -load layer3 ddd;
    
    //    save
    nodePreset -save layer1 ddd;
    renderLayerSaveCustomPreset("layer1","ddd");
    
    nodePreset  -custom "renderLayerSaveCustomPreset(\"#nodeName\",\"#presetName\")" 
                -attributes "renderPassInfo attributeOverrideScript"
                -save layer1
                ddd
    '''


    def __init__(self,params):
        '''
        Constructor
        '''
        
if __name__ == '__main__':    
    pass        