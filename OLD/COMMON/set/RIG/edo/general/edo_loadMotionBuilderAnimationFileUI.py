import maya.cmds as cmds

def edo_loadMotionBuilderAnimationFileUI():
    if cmds.window('edo_loadMotionBuilderAnimationFileUI',ex=1):
        cmds.deleteUI('edo_loadMotionBuilderAnimationFileUI')
    dialog1=cmds.loadUI(f='//file-cluster/GDC/Resource/Support/Maya/extra/Rigging_Simulation/python/edo/general/edo_loadMotionBuilderAnimationFileUI.myuis')
    cmds.showWindow(dialog1)
    cmds.window(dialog1,e=1,w=400,h=90)
    cmds.button('loadMotionBuilderAnimFileBt',e=1,c='edo_loadMbAnimFileCmd()')
    cmds.textField('mbAnimFileTf',e=1,cc='edo_textFieldChangeCmd()')
    

def edo_loadMbAnimFileCmd():
    filename=cmds.fileDialog2(dialogStyle=1,fm=1)
    if not filename==None:
        filename=filename[0]
        cmds.textField('mbAnimFileTf',e=1,tx=filename)
    edo_textFieldChangeCmd()
        
        
def edo_textFieldChangeCmd():
    text=cmds.textField('mbAnimFileTf',q=1,tx=1)
    print text
    edo_loadMotionBuilderTransformData(text)

    
#edo_loadMotionBuilderTransformData()
def edo_loadMotionBuilderTransformData(filename='D:/motionBuilderTransformData.lsa'):
    #filename='Z:/Projects/Daipa/Daipa_Scratch/rigging_simulation/simulation/reference/lipsyncAnimationData/DP_002_c001.lsa'
    fobj=open(filename,'r')
    line=fobj.readline()
    startFrame=None
    endFrame=None
    while (line[:-2]!='//theEnd'):
        line=fobj.readline()
        if line[:-2]=='//theEnd':
            break
        linesplit=line.split(':')
        frame=linesplit[0].replace('*','')
        objname=linesplit[1]
        tfs=linesplit[2]
        tfssplit=tfs.split(';')[:-1]
        translate=[float(tfssplit[0]),float(tfssplit[1]),float(tfssplit[2])]
        edo_setObjectKeyFrameFromData(objname,frame,translate)
        #print line
    fobj.close()

def edo_setObjectKeyFrameFromData(objname,frame,translate):
    #objname='AE_JNT'
    #frame=0
    #value=[-40.0, -1.3773699999999999e-16, 0.0]
    if not cmds.objExists(objname):
        print 'object is not exists!create now!\n'
        loc=cmds.spaceLocator(n=objname)
    cmds.setKeyframe(objname+'.translateX',t=[frame,frame],v=translate[0])
    cmds.setKeyframe(objname+'.translateY',t=[frame,frame],v=translate[1])
    cmds.setKeyframe(objname+'.translateZ',t=[frame,frame],v=translate[2])
    
edo_loadMotionBuilderAnimationFileUI()