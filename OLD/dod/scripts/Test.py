import os
from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
fn_sh = os.path.splitext(sceneName().basename())[0]
shotInfo = fn_sh.split(u'_')
projectInfo = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(shotInfo[0]) 
serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
idp_info_stor = u'%s/data/RLayerInfo/RGB' % serverPath
assetRecordFolders = []#=======找到文件中场景对应的idp信息======================
setMembers = PyNode(u'SET_GRP').getChildren()
assetID_list = []
for eachSet in setMembers:
    setNSP = eachSet.namespace()
    assetID_list.append(re.match(u'[\w]+',(setNSP.split(u'_')[-1])).group())
for root,dirs,files in os.walk(idp_info_stor):
    for eachDir in dirs:
        if eachDir in assetID_list: 
            assetRecordFolders.append(os.path.join(root,eachDir).replace(u'\\',u'/'))
            #assetRecordFolders.append(os.path.abspath(os.path.join(root,eachDir)))
for eachRecFolder in assetRecordFolders: pass
idNum = os.path.split(os.path.dirname(eachRecFolder))[-1]
fileList = [os.path.join(eachRecFolder,eachfile).replace(u'\\',u'/') for eachfile in os.listdir(eachRecFolder)]
for eachRecFile in fileList:pass
idp_mark = eachRecFile.split(u'_')[-2]
recFile = open(eachRecFile


abc = selected()[0]
abc.stripNamespace().longName()


rndMeshes = (eachMesh for eachMesh in abc.getShapes(ad=True,type=u'mesh') if not eachMesh.isIntermediateObject())
for eachOne in rndMeshes:pass
add_idpAttr(eachOne,u'IDP11')
add_idpAttr(eachOne,u'IDP12')
add_idpAttr(eachOne,u'IDP13')



def add_idpAttr(dagNode,attrName):
    dagNode.addAttr(attrName,dt =u'stinrg',dv = u'No')
    dagNode.addAttr(u'%s_clr' % attrName,usedAsColor=True, attributeType='float3')
    dagNode.addAttr( 'redChannel',sn=u'rch', attributeType='float', parent=attr_ln,dv=0.15)
    dagNode.addAttr( 'greenChannel',sn=u'gch', attributeType='float', parent=attr_ln,dv=0.15)
    dagNode.addAttr( 'blueChannel',sn=u'bch', attributeType='float', parent=attr_ln,dv=0.15)
def set_idpAttr(dagNode,attrName,attrValue):
attrName,attrValue,dagNode = u'id13',u'R',eachOne

idpAttrCoupleDict = {u'R':(1,0,0),u'G':(0,1,0),u'B':(0,0,1),u'A':(1,1,1),u'M':(0,0,0)}
dagNode.attr(attrName).set(attrValue)
dagNode.attr(u'%s_clr.rch'%attrName).set(
dagNode.addAttr(u'%s_clr' % attrName,usedAsColor=True, attributeType='float3')
dagNode.addAttr( 'redChannel',sn=u'rch', attributeType='float', parent=attr_ln,dv=0.15)
dagNode.addAttr( 'greenChannel',sn=u'gch', attributeType='float', parent=attr_ln,dv=0.15)
dagNode.addAttr( 'blueChannel',sn=u'bch', attributeType='float', parent=attr_ln,dv=0.15)


def VisitDir(arg,dirname,names):
    for filespath in names: print os.path.join(dirname,filespath)






