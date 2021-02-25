# -*- coding: gbk -*-
import maya.cmds as cmd
import maya.mel as mel
import re 

mel.eval('source "D:/Alias/MAYA8.5/2013/others/showEditor.mel"')
mel.eval('source "//file-cluster/GDC/Resource/Support/AnimalLogic/mayaman2.0.7/mel/AEMayaManCustomShaderTemplate.mel"')
furRIBoption = 'Attribute "dice" "hair" [1]\
\nAttribute "stochastic" "int sigma" [1]'

def ysfixBaldnessMap():
    furs = cmd.ls(type='FurDescription')
    for cloak in furs:
        baldTexName = ''
        # Confirm baldness map will be used or not
        if cmd.getAttr(cloak+'.BaldnessMap[0]') == None:
            confirmDialog = cmd.confirmDialog(title='confirmDialog', message=u'没有“剃毛”，是否继续？',\
                                              button=['Yes', 'No'], dismissString='No',defaultButton='Yes', cancelButton='No')
            if confirmDialog == 'No':
                return
            else:
                cmd.setAttr(cloak+'.Density', 3500000) 
                print u'该镜头是远景镜头'
        
        # Update bald attribute of fur
        Baldness = cmd.listConnections('furDesc_cloak.Baldness', source=True, destination=False)
        if Baldness != None:
            cmd.disconnectAttr(Baldness[0]+'.outAlpha', cloak+'.Baldness')
            baldTexName = Baldness[0]
            
            cmd.setAttr(cloak+'.BaldnessMap[0]', lock=False)
            cmd.connectAttr(baldTexName+'.fileTextureName', cloak+'.BaldnessMap[0]', force=True)
            cmd.setAttr(cloak+'.BaldnessMap[0]', lock=True)           
            
def ysMarionFur():
    # Remove namespace and check amount of Fur description
    mel.eval('source "//file-cluster/GDC/Resource/Support/Maya/2013/zjRemoveNamespace.mel"')
    mel.eval('zjRemoveNamespace;')
    furs = cmd.ls(type='FurDescription')
    if len(furs) > 1:
        cmd.confirmDialog(title='confirmDialog', message=u'请删除多余的Fur物体！', button='OK')
        cmd.select(furs)
        print u'场景中包含'+str(len(furs))+u'个Fur物体，请删除。'
        return
    
    try:
        cmd.setAttr("SLP_cloak.visibility", 1)
        cmd.setAttr("MSH_cloak_.visibility", 0)
    except:
        pass
    
    # Modify Fur's attributes and MayaManAttrsNode
    for item in furs:
        extraAttr = cmd.listAttr(item, ud=1)
        if "MayaManAttsNode" in extraAttr:    
            mmmodelAttr = cmd.listConnections(item+'.MayaManAttsNode', s=1, d=0)
            if mmmodelAttr == None:
                cmd.delete(item)
            if mmmodelAttr != None:
                cmd.setAttr(item+'.BaseWidth', 0.08)
                cmd.setAttr(item+'.TipWidth', 0.010)
                cmd.setAttr(item+'.Density', 4500000)
                cmd.setAttr(item+'.Scraggle', 0)
                cmd.setAttr(item+'.ScraggleFrequency', 0)
                cmd.setAttr(item+'.ScraggleCorrelation', 0)
                cmd.setAttr(mmmodelAttr[0]+'.mmma_UserRib', furRIBoption, type='string')
                if cmd.getAttr(mmmodelAttr[0]+'.mmma_MaterialOverride') == 1:
                    furmmshdr = cmd.listConnections(mmmodelAttr[0]+'.mmma_Material', s=1, d=0)
                    if len(furmmshdr) != 0:
                        mmshdrNode = cmd.listConnections(furmmshdr[0]+'.surfaceShader', s=1, d=0)
                        mel.eval('showEditor("'+mmshdrNode[0]+'")')
                        mel.eval('callCSUpdateCustomShader("'+mmshdrNode[0]+'", "'+mmshdrNode[0]+'.ShaderFile")')
                        cmd.setAttr(mmshdrNode[0]+'.rootOpacity', 1)
                        cmd.setAttr(mmshdrNode[0]+'.tipOpacity', 0)
                        cmd.setAttr(mmshdrNode[0]+'.tipFade', 0)
                        cmd.select(cl=True)

    for mla in cmd.ls(type='MayaManLightAtts'):
        try:
            cmd.setAttr(mla+'.mmla_PixelSamplesX', 16)
            cmd.setAttr(mla+'.mmla_PixelSamplesY', 16)
            cmd.setAttr(mla+'.mmla_ShadowMapSamples', 64)
            cmd.setAttr(mla+'.mmla_DeepShadows', 1)
        except:
            pass
    
    for lgts in cmd.ls(type='spotLight'):
        if re.search('key_light', lgts):
            try:
                cmd.setAttr(lgts+'.dmapResolution', 1024)
                cmd.setAttr(lgts+'.dmapFilterSize', 16)
            except:
                pass 
            
    cmd.setAttr("MayaManNugget.ShadowShadingRateScale", 2)
    cmd.setAttr("MayaManNugget.ShadowDispShaders", 0)
    cmd.setAttr("MayaManNugget.ShadowSurfShaders", 0)
    cmd.setAttr("MayaManNugget.PixelSamplesX", 16)
    cmd.setAttr("MayaManNugget.PixelSamplesY", 16)
    cmd.setAttr("MayaManNugget.NumCpus", 4)
    cmd.setAttr('MayaManNugget.PreScript', 'set MMFUR_OLD_CLUMP=1', type='string')
    cmd.setAttr('MayaManNugget.UserRibOptions', 'Hider "stochastic" "int sigma" [1] "float sigmablur" [2.0]', type='string')
    ysfixBaldnessMap()
    