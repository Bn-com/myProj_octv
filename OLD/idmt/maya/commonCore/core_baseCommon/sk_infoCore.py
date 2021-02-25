# -*- coding: utf-8 -*-
'''
Created on 2015.1.26

@author: shenkang
'''

class sk_infoCore(object):
    
    def __init__(self):
        self.printPre = '\n------[GDC Print]------\n'
        self.errorPre = '\n------[GDC Error]------\n'
    
    def sk_infoCore(self,num):
        infoResult = ''
        
        if num == 0:
            infoResult = self.printPre + '=====================Rg Cache Done=====================' + '\n'
            infoResult += u'>>>>>当前文件为您的rg文件模拟出的render文件'  + '\n'
            infoResult += u'>>>>>请滑动时间轴，看所有用于渲染的物体是否有动'  + '\n'
            infoResult += u'>>>>>如果有部分或全部没动，请检查cache list和_ca_标记'  + '\n'
            infoResult += u'>>>>>如果涉及到_ct_an标记，请检测与Master环约束的_ct_an是否运动'  + '\n'

        if num == 1:
            infoResult +=  u'=====================【错误】未发现cache物体 !!!】====================='

        if num == 2:
            infoResult = self.errorPre + u'-------------This File Is Not A Texture Step File-------------\n'

        if num == 3:
            infoResult = self.errorPre + u'-------------No Rig Asset File On Server Now ,Plase Test Later-------------\n'
            
        if num == 4:
            infoResult = self.printPre + u'=====================Tx Cache创建完毕=====================' + '\n'
            infoResult += u'>>>>>rg文件找不到大环控制器'  + '\n'
            infoResult += u'>>>>>请和rg确定，该asset rg文件是否cache测试正确'  + '\n'

        if num == 5:
            infoResult = self.printPre + u'=====================Tx Cache创建完毕=====================' + '\n'
            infoResult += u'>>>>>请滑动时间轴，看所有用于渲染的物体是否有动'  + '\n'
            infoResult += u'>>>>>如果有部分或全部没动，请检查cache list和_ca_标记'  + '\n'
            
        if num == 6:
            infoResult = self.printPre + u'=====================Tx Cache创建完毕=====================' + '\n'
            infoResult += u'>>>>>服务器端没有对应版本的rg文件'

        if num == 7:
            infoResult = self.printPre + u'=====================[AssetInfo][Server][Update] Done=====================' + '\n'
            
        if num == 8:
            infoResult = self.errorPre + u'-------------Asset has Arnold nodes，please export asset and clean them-------------' + '\n'
            infoResult +=  u'-------------当前Asset文件含有Arnold节点,请导出清理-------------'
            
        if num == 9:
            infoResult = self.errorPre + u'-------------[Face Shader]please fix the objects with face shader-------------' + '\n'
            infoResult +=  u'-------------[选面检测]请处理选面材质的物体-------------'
        
        if num == 10:
            infoResult = self.printPre + u'=====================[Check Mode]This Asset is in No-Check Mode=====================' + '\n'
            infoResult +=  u'-------------[检测模式]当前Asset处于检测豁免状态-------------'
            
        if num == 11:
            infoResult = self.errorPre + u'-------------[Check Mode]Different from rg and tx file , please fix it -------------' + '\n'
            infoResult +=  u'-------------[检测模式]rg和tx文件有差异，请处理-------------' 
            
        if num == 12:
            infoResult = self.errorPre + u'-------------[Cache] Different Name List-------------'+ '\n'
            infoResult +=  u'-------------[Cache]名字不匹配的物体清单-------------'
            
        if num == 13:
            infoResult = self.errorPre + u'-------------[Cache][this  file] Different Name List-------------'+ '\n'
            infoResult +=  u'-------------[Cache][本文件]名字不匹配的物体清单-------------' 
            
        if num == 14:
            infoResult = self.errorPre + u'-------------[Cache][other file] Different Name List-------------'+ '\n'
            infoResult +=  u'-------------[Cache][它文件]名字不匹配的物体清单-------------'
            
        if num == 15:
            infoResult = self.errorPre + u'-------------[Anim][this  file] Different Name List-------------' + '\n'
            infoResult +=  u'-------------[Anim][本文件]名字不匹配的物体清单-------------'
            
        if num == 16:
            infoResult = self.errorPre + u'-------------[Anim][other file] Different Name List-------------'  + '\n'
            infoResult +=  u'-------------[Anim][它文件]名字不匹配的物体清单-------------'
            
        if num == 17:
            infoResult = self.errorPre + u'-------------[MODEL][this  file] Different Name List-------------'  + '\n'
            infoResult +=  u'-------------[MODEL组][本文件]名字不匹配的物体清单-------------'
            
        if num == 18:
            infoResult = self.errorPre + u'-------------[Cache][Different Face|Vertext|UV][List]-------------'  + '\n'
            infoResult +=  u'-------------[Cache][点,线,面不同][清单]-------------'
            
        if num == 19:
            infoResult = self.printPre + u'=====================AnimRender Check Done====================='
            
        if num == 20:
            infoResult = self.errorPre + u'-------------[File Name]No Asset to check,please check the file name-------------' + '\n'
            infoResult +=  u'-------------[文件名]文件名未发现asset信息，请检查好文件名-------------'
            
        if num == 21:
            infoResult = self.errorPre + u'-------------[Cam]Please Clean the Cam:'+ '\n'
            infoResult +=  u'-------------[Cam]请清理相机\t'
            
        if num == 22:
            infoResult = self.printPre + u'=====================Start  [AniFile] Creating 001=====================' + '\n'
            infoResult +=  u'=====================[ani文件] 开始创建 001=====================' + '\n'
            
        if num == 23:
            infoResult = self.printPre + u'=====================Sucess [AniFile] Creation 001=====================' + '\n'
            infoResult +=  u'=====================[ani文件] 开始创建 001=====================' + '\n'
            
        if num == 24:
            infoResult = self.printPre + u'=====================Start  [RndFile] Creating 001=====================' + '\n'
            infoResult +=  u'=====================[rnd文件] 开始创建 001=====================' + '\n'
            
        if num == 25:
            infoResult = self.printPre + u'=====================Sucess [RndFile] Creation 001=====================' + '\n'
            infoResult +=  u'=====================[rnd文件] 开始创建 001=====================' + '\n'
            
        if num == 26:
            infoResult = self.printPre + u'=====================Start  [RndFile] Creating 002=====================' + '\n'
            infoResult +=  u'=====================[rnd文件] 开始创建 002=====================' + '\n'
            
        if num == 27:
            infoResult = self.printPre + u'=====================Sucess [RndFile] Creation 002=====================' + '\n'
            infoResult +=  u'=====================[rnd文件] 开始创建 002=====================' + '\n'
            
        if num == 28:
            infoResult = self.printPre + u'=====================Turn Back to Original File=====================' + '\n'
            infoResult +=  u'=====================返回原始文件=====================' + '\n'
            
        if num == 29:
            infoResult = self.printPre + u'===================== Start  [Check In]=====================' + '\n'
            infoResult +=  u'===================== 开始   [CheckIn] =====================' + '\n'
            
        if num == 30:
            infoResult = self.printPre + u'===================== Sucess [Check In]=====================' + '\n'
            infoResult +=  u'===================== 成功  [CheckIn] =====================' + '\n'
            
        if num == 31:
            infoResult = self.printPre + u'=====================Start  [AnimFile] Creating=====================' + '\n'
            infoResult +=  u'===================== 开始  [Ani文件] 创建  =====================' + '\n'
            
        if num == 32:
            infoResult = self.printPre + u'=====================Sucess [AnimFile] Creation=====================' + '\n'
            infoResult +=  u'===================== 成功  [Ani文件] 创建  =====================' + '\n'
            
        if num == 33:
            infoResult = self.printPre + u'=====================Start  [RenderFile] Creating=====================' + '\n'
            infoResult +=  u'===================== 开始  [Rnd文件] 创建  =====================' + '\n'
            
        if num == 34:
            infoResult = self.printPre + u'=====================Sucess [RenderFile] Creation=====================' + '\n'
            infoResult +=  u'===================== 成功  [Rnd文件] 创建  =====================' + '\n'
            
        if num == 35:
            infoResult = self.printPre + u'=====================No Cache File, clean history,copy to render file=====================' + '\n'

        if num == 36:
            infoResult = self.printPre + u'=====================Set_Asset,output anim file, copy to render file=====================' + '\n'
            
        if num == 37:
            infoResult = self.errorPre + u'-------------No MODEL Grp,please check the file-------------' + '\n'
            infoResult +=  u'-------------未发现 MODEL 组 ,请检查文件-------------' + '\n'
            
        if num == 38:
            infoResult = self.errorPre + u'-------------[Shader]Some objects can not be shadered-------------' + '\n'
            infoResult +=  u'-------------The object in bottom line is the wrong object-------------' + '\n'
            infoResult +=  u'-------------[着色]某些物体无法赋予材质，请查看下方物体-------------' + '\n'
            
        if num == 39:
            infoResult = self.errorPre + u'-------------[Shader]These objects can not be shadered,please go back to tx file and fix them-------------' + '\n'
            infoResult +=  u'-------------[着色]某些物体无法赋予材质，请处理好它们-------------' + '\n'
            
        if num == 40:
            infoResult = self.errorPre + u'-------------[Lost]These objects are not in the file-------------' + '\n'
            infoResult +=  u'-------------[Lose]这些物体没有在文件里-------------' + '\n'
            
        if num == 41:
            infoResult = self.errorPre + u'-------------Please check the object list of the file-------------' + '\n'
            infoResult +=  u'-------------请检查文件里的物体列表-------------' + '\n'
            
        if num == 42:
            infoResult = self.errorPre + u'-------------[Cam]Can\'t find the correct Cam-------------' + '\n'
            infoResult +=  u'-------------[Cam]未发现正确的相机名,如cam_镜头号-------------' + '\n'
            
        if num == 43:
            infoResult = self.printPre + u'=====================Sucess Update Camera to Server!=====================' + '\n'
            infoResult +=  u'=====================相机成功上传至服务器!=====================' + '\n'
            
        if num == 44:
            infoResult = self.errorPre + u'-------------[Ref]Some References can not be Modified!-------------' + '\n'
            infoResult +=  u'-------------[参考]某些参考被锁,无法编辑!-------------' + '\n'
            
        if num == 45:
            infoResult = self.errorPre + u'-------------[Ref]Some References have the same namespace!-------------' + '\n'
            infoResult +=  u'-------------[参考]某些参考是相同的namespace!-------------' + '\n'
            
        if num == 46:
            infoResult = self.errorPre + u'-------------[Lock]Some objects are Locked !-------------' + '\n'
            infoResult +=  u'-------------[Lock]某些物体被锁了   !-------------' + '\n'
            
        if num == 47:
            infoResult = self.errorPre + u'-------------[Lock]Some objects Unlocked Failed !-------------' + '\n'
            infoResult +=  u'-------------[Lock]某些物体解锁失败   !-------------' + '\n'
            
        if num == 48:
            infoResult = self.printPre + u'=====================Sucess Unlock !=====================' + '\n'
            infoResult +=  u'=====================成功解锁 !=====================' + '\n'
            
        if num == 49:
            infoResult = self.errorPre + u'-------------[Set]Didn\'t Find the Valueable Set Group !-------------' + '\n'
            infoResult +=  u'-------------[Set]未发现有效的quickSet组  !-------------' + '\n'
            
        if num == 50:
            infoResult = self.errorPre + u'-------------[Set]Wrong List In Set Group-------------' + '\n'
            infoResult +=  u'-------------[Set]quickSet组内容清单错误  !-------------' + '\n'
            
        if num == 51:
            infoResult = self.errorPre + u'-------------[Set]Didn\'t Find the Correct Set Group !-------------' + '\n'
            infoResult +=  u'-------------[Set]未发现正确的quickSet组  !-------------' + '\n'
            
        if num == 52:
            infoResult = self.errorPre + u'-------------[Set]Please check this object whether is Nurbs or not-------------' + '\n'
            infoResult +=  u'-------------[Set]请检查物体是否是Nurbs  !-------------' + '\n'
            
        if num == 53:
            infoResult = self.errorPre + u'-------------[Set]these asset havn\'t valueable set-------------' + '\n'
            infoResult +=  u'-------------[Set]请检查物体是否是Nurbs  !-------------' + '\n'
            
        if num == 54:
            infoResult = self.errorPre + u'-------------[File Name]please fix the file name to currect name-------------' + '\n'        
            infoResult +=  u'-------------[文件名]请把文件名修正确  !-------------' + '\n'
            
        if num == 55:
            infoResult = self.errorPre + u'-------------[Ref]Some References Do not Exist !-------------' + '\n'
            infoResult +=  u'-------------[参考]某些参考不存在  !-------------' + '\n'
            
        if num == 56:
            infoResult = self.errorPre + u'-------------[Ref]Some References have Problems !-------------' + '\n'   
            infoResult +=  u'-------------[参考]某些参考有问题  !-------------' + '\n'
            
        if num == 57:
            infoResult = self.printPre + u'=====================[Ref]Please Make Sure All References are loaded=====================' + '\n'
            infoResult +=  u'=====================[参考]请确保所有的参考都加载了=====================' + '\n'
            
        if num == 58:
            infoResult = self.printPre + u'=====================Sucess Constains Bake !=====================' + '\n'
            infoResult +=  u'=====================成功 烘焙 所有 约束 ！=====================' + '\n'
            
        if num == 59:
            infoResult = self.printPre + u'=====================No Constrain Exist !=====================' + '\n'
            infoResult +=  u'=====================未发现 约束 =====================' + '\n'
            
        if num == 60:
            infoResult = self.printPre + u'=====================Sucess Path Animation Bake !=====================' + '\n'
            infoResult +=  u'=====================成功 烘焙 路径动画=====================' + '\n'
            
        if num == 61:
            infoResult = self.printPre + u'=====================No Path Animation Exist !=====================' + '\n'
            infoResult +=  u'=====================未发现 路径动画=====================' + '\n'
            
        if num == 62:
            infoResult = self.errorPre + u'-------------[File Name]File Name Is Not Legal !-------------' + '\n'
            infoResult +=  u'-------------[文件名]文件名不正确,应为 [projSimp_ID_type_step_des_vision.format] ,详见命名规则帮助  !-------------' + '\n'
            
        if num == 63:
            infoResult = self.errorPre + u'-------------File Do Not Exist !-------------' + '\n'     
            infoResult +=  u'-------------文件不存在-------------' + '\n'
            
        if num == 64:
            infoResult = self.errorPre + u'-------------[Ref Lost] These References are lost in file -------------' + '\n' 
            infoResult +=  u'-------------[参考丢失] 文件里缺少这些参考-------------' + '\n'
            
        if num == 65:
            infoResult = self.errorPre + u'-------------[Ref More] These References don\'t need in file -------------' + '\n' 
            infoResult +=  u'-------------[参考多余] 文件里多了这些参考-------------' + '\n'
            
        if num == 66:
            infoResult = self.errorPre + u'-------------[Ref Error] Please fix the file\'s references -------------' + '\n' 
            infoResult +=  u'-------------[参考错误] 请处理好这些参考问题-------------' + '\n'
            
        if num == 67:
            infoResult = self.errorPre + u'-------------[Texture] These nodes have error image path info -------------' + '\n' 
            infoResult +=  u'-------------[贴图] 这些贴图节点路径异常-------------' + '\n'
            
        if num == 68:
            infoResult = self.errorPre + u'-------------[Texture] Please fix the shot\'s texture nodes -------------' + '\n' 
            infoResult +=  u'-------------[贴图] 请处理好镜头的贴图节点,若是参考的节点,和前期一同查看路径是否正确;若非参考,清理掉即可-------------' + '\n'
            
        if num == 69:
            infoResult = self.errorPre + u'-------------[File Name] No Info In Database ,Please check the file name -------------' + '\n'  
            infoResult +=  u'-------------[文件名] 数据库没有本文件信息，请检查文件名是否正确-------------' + '\n'
            
        if num == 70:
            infoResult = self.errorPre + u'-------------[Wrong File(CHR,PRP:rg | SET,ENV:tx)]-------------' + '\n'
            infoResult += u'-------------[MODEL Grp Must In Root\'s Leve 2 ]-------------' + '\n'
            infoResult += u'-------------[MODEL Grp Should have only one ]-------------' + '\n'
            infoResult += u'-------------MODEL组应该在第二层级,且应该只有一个-------------' + '\n'
            
        if num == 71:
            infoResult = self.errorPre + u'-------------[IDP] This Asset havn\'t valuebale IDP Info -------------' + '\n'  
            infoResult +=  u'-------------[IDP] 本Asset未发现有效的idpass信息-------------' + '\n'
            
        if num == 72:
            infoResult = self.errorPre + u'-------------[Comp] This Episode Info do not exist -------------' + '\n'  
            infoResult +=  u'-------------[合成] 本集信息不存在-------------' + '\n'
            
        if num == 73:
            infoResult = self.errorPre + u'-------------[Anim] Anim Info Error -------------' + '\n'  
            infoResult +=  u'-------------[Anim] Anim信息错误-------------' + '\n'
            
        if num == 74:
            infoResult = self.errorPre + u'-------------[Anim Curve] Please Check These Objects,whether Same Name , whether Keyable , whether Unlock -------------' + '\n'  
            infoResult +=  u'-------------[动画曲线] 请检查这些物体，是否重名,是否可K帧,是否锁住-------------' + '\n'
            
        if num == 75:
            infoResult = self.errorPre + u'-------------[Ref Info] This Shot Don\'t have the Rebuild Info -------------' + '\n'  
            infoResult +=  u'-------------[参考信息] 本镜头未发现重建Rebuild信息-------------' + '\n'
            
        if num == 75:
            infoResult = self.errorPre + u'-------------[Update File] Server Update Failed -------------' + '\n' 
            infoResult +=  u'-------------[上传文件] 上传服务器失败-------------' + '\n'
            
        if num == 76:
            infoResult = self.errorPre + u'-------------Please Check the Ani and Rnd File\'s Cache List-------------' + '\n' 
            infoResult +=  u'-------------[上传文件] 请检查Ani和Rnd的cache List-------------' + '\n'
            
        if num == 77:
            infoResult = self.errorPre + u'-------------[Rnd]These Asset\'s Render File Do Not Exist-------------' + '\n' 
            infoResult +=  u'-------------[Rnd] 这些 Asset 的 Rnd 文件不存在-------------' + '\n'            
            #print u'-------------------以上render文件不存在-------------------'
            #print u'==================请先检查shot文件确定参考是否正确=================='
            #print u'==================正确后请再和前期协商更新asset文件=================='
            
        if num == 78:
            infoResult = self.errorPre + u'-------------[Ref]No Reference In File , Please Check The Shot File-------------' + '\n' 
            infoResult +=  u'-------------[参考] 文件未发现参考,请检查文件-------------' + '\n'            
            #print(u'==================shot文件没有参考下请先检查shot文件确定参考是否正确，请和动画联系==================')

        if num == 79:
            infoResult = self.errorPre + u'-------------Please Fix These Errors -------------' + '\n' 
            infoResult +=  u'-------------请修正这些错误-------------' + '\n'      
            
        if num == 80:
            infoResult = self.errorPre + u'-------------[Preview File]The Preview File is not Legal -------------' + '\n' 
            infoResult +=  u'-------------[预览文件] 预览文件不正确-------------' + '\n'      
            
        if num == 81:
            infoResult = self.errorPre + u'-------------[Preview File]Asset step just need .jpg preview file -------------' + '\n' 
            infoResult +=  u'-------------[预览文件] Asset环节需要.jpg的预览文件-------------' + '\n'      
            
        if num == 82:
            infoResult = self.errorPre + u'-------------[Preview File]Anim step just need .mov playblast file -------------' + '\n' 
            infoResult +=  u'-------------[预览文件] Anim动画环节需要.mov的拍屏文件-------------' + '\n'    
            
        if num == 83:
            infoResult = self.errorPre + u'-------------[Anim Curve]No Ctrls select ! Please Select the Control Curves !-------------' + '\n'
            infoResult +=  u'-------------[动画曲线] 未发现控制器选中,请选中曲线控制器 -------------' + '\n'    
            
        if num == 84:
            infoResult = self.errorPre + u'-------------[Anim Curve]Ctrl name is not legal !-------------' + '\n'
            infoResult +=  u'-------------[动画曲线] 控制器名字不对 -------------' + '\n' 
            
        if num == 85:
            infoResult = self.errorPre + u'-------------[Anim Curve]Please Select the Exist Path !-------------' + '\n'
            infoResult +=  u'-------------[动画曲线] 请选择存在的路径 -------------' + '\n' 
      
        if num == 86:
            infoResult = self.errorPre + u'-------------[Asset Search]The File info is not Legal !-------------' + '\n'
            infoResult +=  u'-------------[搜索Asset] 文件信息错误 -------------' + '\n' 
      
        if num == 87:
            infoResult = self.errorPre + u'-------------[Asset Search]Please check the file , or check the maya version !-------------' + '\n'
            infoResult +=  u'-------------[搜索Asset] 请检查文件,或者检查maya版本 -------------' + '\n' 
            
        if num == 88:
            infoResult = self.errorPre + u'-------------[RenderLayers]Please check the masterLayer in file !-------------' + '\n'
            infoResult +=  u'-------------[渲染层] 请检查文件里的masterLayer层 -------------' + '\n' 
            
        if num == 89:
            infoResult = self.errorPre + u'-------------[DisplayLayers]Please Clean these Display Layers !-------------' + '\n'
            infoResult +=  u'-------------[显示层] 请清理这些显示层 -------------' + '\n' 
            
        if num == 90:
            infoResult = self.printPre + u'=====================[File Name]File Name Is Not Legal !=====================' + '\n'   
            infoResult += u'=====================File Name Like lb_xxx_xxx...=====================' + '\n'  
            infoResult +=  u'=====================文件名不正确,应像 lb_xxx_xxx,请查看命名规则帮助 !=====================' + '\n'
            
        if num == 91:
            infoResult = self.printPre + u'=====================Start  [AniFile] Creating 002=====================' + '\n'
            infoResult +=  u'=====================开始创建 [Ani文件] 002=====================' + '\n'
            
        if num == 92:
            infoResult = self.printPre + u'=====================Sucess [AniFile] Creation 002=====================' + '\n'
            infoResult +=  u'=====================成功创建 [Ani文件] 002=====================' + '\n'
            
        if num == 93:
            infoResult = self.printPre + u'=====================Start  [AniFile] Creating 003=====================' + '\n'
            infoResult +=  u'=====================开始创建 [Ani文件] 003=====================' + '\n'
            
        if num == 94:
            infoResult = self.printPre + u'=====================Sucess [AniFile] Creation 003=====================' + '\n'
            infoResult +=  u'=====================成功创建 [Ani文件] 003=====================' + '\n'
            
        if num == 95:
            infoResult = self.errorPre + u'-------------[File Node]Your texture file node should have the key info of \'sourceimages\'-------------' + '\n'
            infoResult +=  u'-------------[文件节点] 贴图节点应该有\'sourceimages\'信息-------------' + '\n' 
            
        if num == 96:
            infoResult = self.printPre + u'=====================[Layout]Asset List Update to DataBase Done!=====================' + '\n'
            infoResult +=  u'=====================[Layout] Asset清单已上传至服务器=====================' + '\n'
            
        if num == 97:
            infoResult = self.errorPre + u'-------------[Update File] The path don\'t legal,please check-------------' + '\n'
            infoResult +=  u'-------------[上传文件] 路径错误,请检查-------------' + '\n' 
            
        if num == 98:
            infoResult = self.errorPre + u'-------------[Update Cache] the cache path should have \'data\' folder-------------' + '\n'
            infoResult +=  u'-------------[上传cache] cache路径错误,需要有data文件夹,请检查-------------' + '\n' 
            
        if num == 99:
            infoResult = self.errorPre + u'-------------[Playblast Faile] failed to use playblast tool ,please restart maya or close the playblast process-------------' + '\n'
            infoResult +=  u'-------------[拍屏失败] 拍屏失败,请重启maya或者关掉已经打开的拍屏任务-------------' + '\n' 
            
        if num == 100:
            infoResult = self.errorPre + u'-------------[FPS] Your FPS setting is different from server database,please check it and fix it-------------' + '\n'
            infoResult +=  u'-------------[FPS] 文件的FPS设置和服务器端设置不一样,请检查修正-------------' + '\n' 
            
        if num == 101:
            infoResult = self.errorPre + u'-------------[FPS] No FPS data in Server database , please tell TD or PM-------------' + '\n'
            infoResult +=  u'-------------[FPS] 服务器端设置未发现FPS设置信息,请通知 TD 或者 项目经理 -------------' + '\n' 
            
        if num == 102:
            infoResult = self.errorPre + u'-------------[Frames] Your frames setting is different from server database,please check it and fix it-------------' + '\n'
            infoResult +=  u'-------------[帧范围] 文件的 帧范围信息 和 服务器端信息 不一样,请检查修正;若你对通知项目经理修正;若服务器端正确请打开文件修改-------------' + '\n' 
            
        if num == 103:
            infoResult = self.errorPre + u'-------------[Frames] No Shot frames info in Server database , please tell TD or PM-------------' + '\n'
            infoResult +=  u'-------------[帧范围] 服务器端设置未发现本镜头的帧范围信息,请通知 TD 或者 项目经理-------------' + '\n' 
            
        if num == 104:
            infoResult = self.errorPre + u'-------------[Ref] These assets have _h_ file ,please swith the reference to high mode file-------------' + '\n'
            infoResult +=  u'-------------[参考] 这些asset已经有高模,请切换到高模状态-------------' + '\n' 
            
        if num == 105:
            infoResult = self.errorPre + u'-------------[Anim Curve] The Source file\'s Control Curvs changed ,please ask Rig Maker for reason-------------' + '\n'
            infoResult +=  u'-------------[动画曲线] 源文件的控制器有改变,请联系设置制作者-------------' + '\n' 
            
        if num == 106:
            infoResult = self.errorPre + u'-------------[Img Update] The Source Path is a file ,please tell TD-------------' + '\n'
            infoResult +=  u'-------------[图片上传] 源文件是一个文件,请通知TD-------------' + '\n' 
            
        if num == 107:
            infoResult = self.errorPre + u'-------------[Camera Panel] Please Click the camera view sight panel-------------' + '\n'
            infoResult +=  u'-------------[相机面板] 请选中相机视野的面板-------------' + '\n' 
            
        if num == 108:
            infoResult = self.errorPre + u'-------------[Daily Error] The Daily Of This Shot in This Step didn\'t Pass!!!-------------' + '\n'
            infoResult +=  u'-------------[Daily错误] 本镜头的daily还未通过,通过后才能checkIn-------------' + '\n' 
            
        if num == 109:
            infoResult = self.errorPre + u'-------------[ASS Error] No Asset Info In ImagePath In The Ass File !!!-------------' + '\n'
            infoResult +=  u'-------------[ASS Error] 在ass文件的贴图路径未发现asset信息-------------' + '\n' 
            
        if num == 110:
            infoResult = self.errorPre + u'-------------[Asset Error] Some texture not on server, please turn on update iamges !!!-------------' + '\n'
            infoResult +=  u'-------------[ASS Error] 某些贴图不在服务器端,请开启 -上传贴图- 选项-------------' + '\n' 
            
        if num == 111:
            infoResult = self.errorPre + u'-------------[ASS Error] These Object Can not be hidden , please check !!!-------------' + '\n'
            infoResult +=  u'-------------[ASS Error] 这些物体不能被隐藏,请检查-------------' + '\n' 
            
        if num == 112:
            infoResult = self.errorPre + u'-------------[Asset Error] no ID in database , please check the name !!!-------------' + '\n'
            infoResult +=  u'-------------[ASS Error] 数据库未发现ID,请检查名字-------------' + '\n' 
            
        #sk_infoCore.sk_infoCore().sk_infoCore(7)

        return infoResult