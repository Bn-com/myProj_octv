#-*- coding: utf-8 -*-
'''
Created on 2013-10-23
@contact:    power_zzj@163.com
@deffield    updated: Updated
@author: zhaozhongjie
'''
import os,sys
sys.path.append(r'//file-cluster/GDC/Resource/Support/Maya/Python')
import xlrd                             #    读取excel文件内容的包
import maya.cmds as cmds
import pymel.core as pm
import re
class MyClass():
    '''
    classdocs
    '''
    print 'xxxxxxxxxxxxxxxxxxxxxxx'
    __FILE =__file__
    __EXCEL = 'OpenSceneReplaceReference_xyj.xls'                                       #    如果在excel文件和py文件在同一目录下，excel对应的名称。
    __EXCEL_FULL = os.path.join(os.path.split(__FILE)[0] , __EXCEL)           #    excel文件的绝对路径。
    #__EXCEL_FULL = r'd:\abc.xls'                                                                #    你也可以手动指定excel文件的绝对路径。
    
    __LIST = []                     #    任务清单

    def __init__(self):
        '''
            使用xlrd查询excel文件，生成任务清单
        '''
        data = self.open_excel()                       #     读excel文件
        table = data.sheets()[0]
        nrows = table.nrows                                          #    行数
        ncols = table.ncols                                            #    列数
        self.scene_name_sht = cmds.file(q=1,sn=1)
        if nrows<3:
            print "数据错误"
            return
        
        for i in range( 2 , nrows):
            content =  table.row_values( i )                   #    某一行数据 
            self.__LIST.append( content)                        #    生成任务清单
        
        self.MyReplaceReference()                              #    执行任务清单
        sub_pair={"/nj_":"/Xyj_","/Ninjago/":"/XYJ/","\.ma":".mb","_ms_set":"_ms_anim"} ## I use "\.ma" instead of ".ma",because I use re.sub
        self.replace_ref_by_newFunction(**sub_pair)
        self.xy_saveAsFile()
#     函数：---读excel文件----------------------------------------------------------------------
    def open_excel(self , file = __EXCEL_FULL):                                         
        try:
            data = xlrd.open_workbook( file )
            return data
        except Exception , e :
            print str(e)
            
#     函数：---执行任务清单----------------------------------------------------------------------
    def MyReplaceReference(self ):      
        fileName = cmds.file(q=1,sn=1)                       
        for a in self.__LIST:
            sure_key = a[0].split(';')                     #    1.    必须有的关键字
            choice_key = a[1].split(';')                 #    2.    选择性的关键字
            unless_key = a[2].split(';')                  #    3.    排除掉的关键字?
            old_name = a[3]                   #    旧的参考名称
            new_name = a[4]                  #    替换参考名称
            new_reference = a[5]            #    替换参考的路径
            
            Condition1 = 1                               #    1.    判断是否包含关键字
            for x in sure_key:
                if x not in fileName:
                    Condition1 = 0
                    break
            
            Condition2 = 0                               #    2.    判断是否找到多选的关键字
            if choice_key ==['']:
                Condition2 = 1
            else:
                for x in choice_key:
                    if x in fileName:
                        Condition2 = 1
                        break     
            
            Condition3 = 0                                #    3.    判断是否找到排除的关键字
            if unless_key ==['']:
                Condition3 = 0
            else:            
                for x in unless_key:
                    if x in fileName:
                        Condition3 = 1
                        break

#===================================================================================================
#     如果满足 1 , 2 , 3 条条件，则开始替换参考：
#===================================================================================================
            if Condition1 ==1 and Condition2 ==1 and Condition3 == 0:       
                references = cmds.file(q=1,r=1)

                for r in references:
                    if old_name in r:
                        self.MyReplaceReferenceAndFixNameSapce( r, new_name , new_reference)
                        print ":::::::::::::::::::::::::::::::Reference Replaced By Excel Sheet Done!!!!!!!!!!<<<<{}>>>>".format(new_name)
#     函数：---替换参考并修正NameSpace----------------------------------------------------------------------                        
    def MyReplaceReferenceAndFixNameSapce(self , r , new_name , new_reference ):      
#    1.    替换参考
        rfn = cmds.file( r , q=1 , rfn = 1)                                     #    求rfn节点的名字
        if os.path.exists(new_reference):                                     #    这个文件前期还没出完，所以要判断一下。也有可能这个目标文件根本不存在
            cmds.file(new_reference , loadReference = rfn )       
        else:
            print("!!!!!!!!!!!!!!The file DO NOT EXIST!!!!!!!!!!!!::{}".format(new_reference))
            self.record_failse_info('{}:{}'.format(self.scene_name_sht,new_reference))
            return None
#    2.    修正namespace            
        cmds.namespace(setNamespace =":")
        for i in range(100):
            ns = new_name+"_" + str(i)
            #print "test ++++++++++++++++++++++++++++new_nameSpace:{}".format(ns)
            if cmds.namespace(exists=ns):    continue
            else:
                print "+++++++++++++++new namespace is :{}".format(ns)
                newR = cmds.referenceQuery(rfn,filename = 1)
                cmds.file(newR , edit=1 , namespace = ns )
                
                cmds.lockNode( rfn , lock =0, )                                                       #    解锁
                newRFN = new_name + "_" + str(i) + "RN"                                    #    新rfn名字
                if cmds.objExists(newRFN) :   newRFN+= "1"                                 #    判断如果存在这个名字，自动在后面加“1”   
                if cmds.objExists(newRFN) :   newRFN+= "1"                                 #    重复上面的操作，确保万无一失
                cmds.rename( rfn , newRFN)                                                           #   重命名
                cmds.lockNode(newRFN,lock=1, )                                                  #   上锁
                
                break
        cmds.namespace(setNamespace =":")
        return True
    def xy_saveAsFile(self,stor_path = os.path.abspath(ur'D:/temp_info/a2_rnmRef_nj2xy')):
        all_unk_plugins = pm.unknownPlugin(list=True,q=True)
        if all_unk_plugins:
            for each_unk_plg in all_unk_plugins:
                if each_unk_plg not in ['mtoa']:
                    pm.unknownPlugin(each_unk_plg,r=True)
        fn_read = cmds.file(shn=True,q=True,sn=True)
        p_prf_key = re.compile("^nj_")
        fn_new = p_prf_key.sub('xyj_',fn_read)
        if not os.path.isdir(stor_path):os.makedirs(stor_path)
        fn_new_full = os.path.join(stor_path,fn_new)
        cmds.file(rn=fn_new_full)
        pm.saveFile()
        print("==============={}==file saved success!!!!=====".format(fn_new_full))
    def generate_new_ref_info(self,each_ref,**sub_pair):
        old_path = each_ref.path
        new_path = old_path
        for each_sub_source in sub_pair:
            p_key = re.compile(each_sub_source)
            new_path = p_key.sub(sub_pair.get(each_sub_source),new_path)
        ref_new_name = '_'.join(os.path.basename(new_path).split('_')[:2])
        return {ref_new_name:new_path}
    def replace_ref_by_newFunction(self,**sub_pair):
        #sub_pair = {"/nj_":"/Xyj_","/Ninjago/":"/XYJ/","\.ma":".mb"}
        refs = pm.listReferences()#modify by zhangben 2017 08 10
                #references = cmds.file(q=1,r=1)
        for eachRef in refs:
            old_path = eachRef.path
            new_ref_info = self.generate_new_ref_info(eachRef,**sub_pair)
            if new_ref_info.values()[0] != old_path:
                print new_ref_info
                replace_result = self.MyReplaceReferenceAndFixNameSapce( old_path, new_ref_info.keys()[0] , new_ref_info.values()[0])
                if replace_result:print ":::::::::::::::::::::::::::::::Reference Replaced By New Function Done!!!!!!!!!!<<<<{}>>>>".format(new_ref_info.keys()[0])
    def record_failse_info(self,refs,stor_path = os.path.abspath(ur'D:/temp_info/a2_rnmRef_nj2xy')):
        rec_file = open(os.path.join(stor_path,'rec_failse_information.txt'),'a')
        rec_file.write('{}\n'.format(refs))
        rec_file.close()
if __name__ == '__main__':
    MyClass()



