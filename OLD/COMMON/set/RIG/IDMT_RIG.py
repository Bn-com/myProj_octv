import sys
import headfile as headfile
toolpath=headfile.__file__
rigPath = toolpath.replace('\\','/').replace('headfile.py','')
rigSyspath = sys.path
if rigPath in rigSyspath:
    pass
else:
    sys.path.append(rigPath)
from RIG.UI.MainUI import *
SK_IDMTRigUI()