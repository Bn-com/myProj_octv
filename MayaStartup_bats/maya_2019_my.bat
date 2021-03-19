@echo off 
rem set MAYA_MODULE_PATH=D:\devModule\myDev_2019
REM set MAYA_MODULE_PATH=F:\Development\octProj\oct\maya_nineteen\moudules
set MAYA_MODULE_PATH=F:\Development\octProj\oct\maya_nineteen\moudules
set DEVKIT_LOCATION=C:\Users\zhangben\devkitBase\
set MAYA_LOCATION=D:\Autodesk\maya2019
set PATH=%PATH%;%MAYA_LOCATION%\bin
set MAYA_ENV_MODE=dev_mode
REM set MAYA_ENABLE_LEGACY_VIEWPORT=1
set MAYA_VERSION=2019
set DPRT=dprint
set batdir=%~dp0
set DEPLOYCMD=%batdir%MAYA_DEPLOY.bat
echo ...Start Deploy MAYA ENV and Startup Image : %DEPLOYCMD%
call %DEPLOYCMD%
echo ...Ready Startup MAYA APP...
"D:\Autodesk\Maya2019\bin\maya.exe"
echo ....exit cmd window.......
cmd.exe exit 