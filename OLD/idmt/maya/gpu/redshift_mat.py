# -*- coding: utf-8 -*-
# 【通用】【redshift 材质工具】
#  Author : 韩虹
#  Data   : 2016_02
#  Mender:韩虹
#  Data  :2016_02


import maya.cmds as mc
import maya.mel as mel

class redshift_mat(object):
    def __init__(self):
        # namespace清理
        pass
#---------------------------------------------------
#其他材质转redshift材质工具（目前支持arnold aiStandard 材质）
#------HANHONG------------------------------------------
    def shadeShiftcover(self,shadetype='aiStandard',Del=0):
        rsmat=''
        infoold=[]
        infoRs=[]
        redshiftshades=[]
        if shadetype=='aiStandard':
            rsmat='rsMaterial'
            infoldco=['color','Kd','diffuseRoughness','Kb']
            infoRsco=['diffuse_color','diffuse_weight','diffuse_roughness','transl_weight']
            infoldspe=['KsColor','Ks','specularRoughness']
            infRscoat=['coat_color','coat_weight','coat_roughness']
            infooldref=['KrColor','Kr']
            infoRsref=['refl_color','refl_weight']
            infoldraf=['KtColor','Kt']
            infoRsraf=['refr_color','refr_weight']
            infoldSub=['KsssColor','Ksss']
            infoRsSub=['ms_color0','ms_weight0']
            infobump=['normalCamera']
            infoRsbump=['bump_input']
            infoold=[infoldco,infoldspe,infooldref,infoldraf,infoldSub,infobump]
            infoRs=[infoRsco,infRscoat,infoRsref,infoRsraf,infoRsSub,infoRsbump]
        shades=mc.ls(type=shadetype,l=1)
        if shades :
            for shade in shades:
                shadeShift=''
                shadeshort=''
                if ':' in shade:
                    shadeshort=shade.split(':')[-1]
                else:
                    shadeshort=shade
                if '_' in shadeshort:
                    shadeShift=shadeshort.split(shadeshort.split('_')[-1])[0]+rsmat
                else:
                    shadeShift=shadeshort+'_'+rsmat

                shadeShift=mc.shadingNode('RedshiftMaterial' , asShader=True,n=shadeShift)
                sgs=mc.listConnections(shade+'.outColor',type= 'shadingEngine')
                redshiftshades.append(shadeShift)
                if not sgs:
                    continue
                for sg in sgs:
                    try:
                        mc.connectAttr((shadeShift+'.outColor'),(sg+'.surfaceShader'),f=1)
                        print  u'【%s】材质球已转换redshift材质球====================' %shade
                    except:
                        mc.warning(u'【%s】材质无法连接【%s】SG节点，请检查' %(shadeShift,sg))
                for i in range(len(infoold)):
                    for j in range((len(infoold[i]))):
                        con=mc.listConnections((shade+'.'+infoold[i][j]),s=1,c=0,p=0)
                        conp=mc.listConnections((shade+'.'+infoold[i][j]),s=1,c=0,p=1)
                        GetN=mc.getAttr(shade+'.'+infoold[i][j])
                        if con and shadetype in ['aiStandard'] and mc.nodeType(con[0])=='file' and infoold[i][j] not in ['normalCamera']:
                            try:
                                mc.connectAttr(conp[0],(shadeShift+'.'+infoRs[i][j]), f=True)
                            except:
                                mc.warning(u'【%s】节点无法连接【%s】节点，请检查文件' %((conp[0],shadeShift+'.'+infoRs[i][j])))
                                pass
                        if con and shadetype in ['aiStandard'] and mc.nodeType(con[0])=='layeredTexture' and infoold[i][j] not in ['normalCamera']:
                            txShader=mc.shadingNode('RedshiftMaterialBlender' , asShader=True)
                            try:
                                mc.connectAttr((txShader+'.outColor'),(shadeShift+'.'+infoRs[i][j]), f=True)
                            except:
                                mc.warning(u'【%s】节点无法连接【%s】节点，请检查文件' %((conp[0],shadeShift+'.'+infoRs[i][j])))
                                pass
                        if con and shadetype in ['aiStandard'] and mc.nodeType(con[0])=='aiImage' and infoold[i][j] not in ['normalCamera']:
                            filName=shadeShift+'_file'
                            fil=mc.shadingNode('file' ,asTexture=True,n=filName)
                            img=mc.getAttr((con[0]+'.filename'),x=1)
                            try:
                                mc.setAttr((fil+'.fileTextureName'),img,type='string')
                                ctyp=conp[0].split('.')[-1]
                                mc.connectAttr((fil+'.'+ctyp),(shadeShift+'.'+infoRs[i][j]), f=True)
                            except:
                                pass
                        if con and shadetype in ['aiStandard'] and infoold[i][j] in ['normalCamera']:
                            utype=''
                            if mc.getAttr(con[0]+'.bumpInterp')==0:
                                utype='RedshiftBumpMap'
                            else:
                                utype='RedshiftNormalMap'
                            filn=mc.shadingNode(utype ,asTexture=True,n=(shadeShift+'_'+utype))
                            fil=mc.listConnections(con[0],d=0,s=1,c=0,p=0)
                            if fil and mc.nodeType(fil[0])=='file' and utype=='RedshiftNormalMap':
                                img=mc.getAttr(fil[0]+'.fileTextureName')
                                try:
                                    mc.setAttr((filn+'.tex0'),img,type='string')
                                    mc.connectAttr((filn+'.outDisplacementVector'),(shadeShift+'.'+infoRs[i][j]), f=True)
                                except:
                                    pass
                            if fil and utype=='RedshiftNormalMap':
                                filnn=mc.listConnections(con[0],d=0,s=1,c=0,p=1)
                                try:
                                    mc.connectAttr(filnn[0],(filn+'.input'), f=True)
                                    mc.connectAttr((filn+'.out'),(shadeShift+'.'+infoRs[i][j]),f=True)
                                except:
                                    pass
                        if not con and shadetype in ['aiStandard'] and  isinstance(GetN,list)==True:
                            mc.setAttr((shadeShift +'.'+infoRs[i][j]),GetN[0][0],GetN[0][1],GetN[0][2],type='double3')
                        if not con and shadetype in ['aiStandard'] and  isinstance(GetN,list)!=True and  infoRs[i][j]!='ms_weight0':
                            mc.setAttr((shadeShift+'.'+infoRs[i][j]),GetN)
                        if not con and shadetype in ['aiStandard'] and  isinstance(GetN,list)!=True and  infoRs[i][j]=='ms_weight0' and int(mc.getAttr(shade+'.'+infoold[i][j]))<1:
                            mc.setAttr((shadeShift+'.'+infoRs[i][j]),GetN)
                        if not con and shadetype in ['aiStandard'] and  isinstance(GetN,list)!=True and  infoRs[i][j]=='ms_weight0' and int(mc.getAttr(shade+'.'+infoold[i][j]))>=1:
                            mc.setAttr((shadeShift+'.'+infoRs[i][j]),1)
                        if Del==1:
                            try:
                                mc.delete(shade)
                            except:
                                pass
            print u'====================【%s】材质球已转换redshift材质球===================' %shadetype
            return [redshiftshades]