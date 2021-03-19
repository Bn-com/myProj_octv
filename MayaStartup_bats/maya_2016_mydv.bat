@echo
xcopy F:\Development\MayaStartup_bats\maya\2016\mydev\Maya.env C:\Users\zhangben\Documents\maya\2016 /Y
xcopy F:\Development\MayaStartup_bats\maya\2016\mydev\scripts\usersetup.py C:\Users\zhangben\Documents\maya\2016\scripts /Y
set MAYA_MODULE_PATH=D:\devModule\myModule
set MAYA_ENV_MODE=dev_mode
set MAYA_VERSION=2016
"D:\Autodesk\Maya2016\bin\maya.exe"