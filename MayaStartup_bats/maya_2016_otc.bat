@echo
xcopy F:\Development\MayaStartup_bats\maya\2016\oct\Maya.env C:\Users\zhangben\Documents\maya\2016 /Y
xcopy F:\Development\MayaStartup_bats\maya\2016\oct\scripts\usersetup.py C:\Users\zhangben\Documents\maya\2016\scripts /Y
set MAYA_MODULE_PATH=D:\devModule\OCT;
set MAYA_VERSION=2016
set MAYA_ENV_MODE=client_mode
"D:\Autodesk\Maya2016\bin\maya.exe"