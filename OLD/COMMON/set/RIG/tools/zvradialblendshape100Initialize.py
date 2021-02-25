import maya.cmds as cmds
import maya.OpenMaya as om
import sys
def zvradialblendshape100Initialize(path):
    #path='Z:/Resource/Groups/Production/Modeling/Rigging 2009 Development Plan/BodyRiggingTools/script/RIG/tools/zvradialblendshape100'
    mg=om.MGlobal()
    version=mg.mayaVersion()
    if '2009' in version and not '64' in version:
        print 'maya2009 x32'
        if not cmds.pluginInfo('radialBlendShape.mll',query=True,l=True):
            cmds.loadPlugin(path+'/Maya 2009/plug-ins/x86/radialBlendShape.mll')
        sys.path.append(path+'/Maya 2009/2013')
        import ZvRadialBlendShape
    if '2009' in version and '64' in version:
        print 'maya2009 x64'
        if not cmds.pluginInfo('radialBlendShape.mll',query=True,l=True):
            cmds.loadPlugin(path+'/Maya 2009/plug-ins/x64/radialBlendShape.mll')
        sys.path.append(path+'/Maya 2009/2013')
        import ZvRadialBlendShape
    if '2010' in version and not '64' in version:
        print 'maya2010 x32'
        if not cmds.pluginInfo('radialBlendShape.mll',query=True,l=True):
            cmds.loadPlugin(path+'/Maya 2010/plug-ins/x86/radialBlendShape.mll')
        sys.path.append(path+'/Maya 2010/2013')
        import ZvRadialBlendShape
    if '2010' in version and '64' in version:
        print 'maya2010 x64'
        if not cmds.pluginInfo('radialBlendShape.mll',query=True,l=True):
            cmds.loadPlugin(path+'/Maya 2010/plug-ins/x64/radialBlendShape.mll')
        sys.path.append(path+'/Maya 2010/2013')
        import ZvRadialBlendShape
    if '2011' in version and not '64' in version:
        print 'maya2011 x32'
        if not cmds.pluginInfo('radialBlendShape.mll',query=True,l=True):
            cmds.loadPlugin(path+'/Maya 2011/plug-ins/x86/radialBlendShape.mll')
        sys.path.append(path+'/Maya 2011/2013')
        import ZvRadialBlendShape
    if '2011' in version and '64' in version:
        print 'maya2011 x64'
        if not cmds.pluginInfo('radialBlendShape.mll',query=True,l=True):
            cmds.loadPlugin(path+'/Maya 2011/plug-ins/x64/radialBlendShape.mll')
        sys.path.append(path+'/Maya 2011/2013')
        import ZvRadialBlendShape
        import ZvRadialBlendShape
    if '2012' in version and not '64' in version:
        print 'maya2011 x32'
        if not cmds.pluginInfo('radialBlendShape.mll',query=True,l=True):
            cmds.loadPlugin(path+'/Maya 2012/plug-ins/x86/radialBlendShape.mll')
        sys.path.append(path+'/Maya 2011/2013')
        import ZvRadialBlendShape
    if '2012' in version and '64' in version:
        print 'maya2011 x64'
        if not cmds.pluginInfo('radialBlendShape.mll',query=True,l=True):
            cmds.loadPlugin(path+'/Maya 2012/plug-ins/x64/radialBlendShape.mll')
        sys.path.append(path+'/Maya 2012/2013')
        import ZvRadialBlendShape
    cmds.confirmDialog( title='warning', message='if you want use this plugin to rigging character,you must told TD to configure this plugin first!', button='yes,got it', defaultButton='Yes', cancelButton='YES', dismissString='YES')
    ZvRadialBlendShape.ZvRadialBlendShape()
zvradialblendshape100Initialize('Z:/Resource/Groups/Production/Modeling/Rigging 2009 Development Plan/BodyRiggingTools/script/RIG/tools/zvradialblendshape100')