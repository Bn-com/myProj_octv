import sys
rigPath = '\\\\file-cluster\\GDC\\Resource/Groups/Production/Modeling/Rigging 2009 Development Plan/BodyRiggingTools/script'
rigSyspath = sys.path

if rigPath in rigSyspath:
    pass
else:
    sys.path.append(rigPath)
    
from RIG.UI.MainUI import *
SK_IDMTRigUI()
