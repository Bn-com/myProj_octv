@echo off 
rem set MAYA_MODULE_PATH=D:\devModule\myDev_2019
set MAYA_VERSION=2020
echo CURRENT MAYA VERSION --- %MAYA_VERSION%
set MAYA_MODULE_PATH=F:\Development\octProj\oct\maya_dev\moudules
set DEVKIT_LOCATION=C:\Users\zhangben\devkitBase\
set MAYA_LOCATION=D:\Autodesk\maya%MAYA_VERSION%
set PATH=%PATH%;%MAYA_LOCATION%\bin
set MAYA_ENV_MODE=dev_mode
set batdir=%~dp0
set DEPLOYCMD=%batdir%MAYA_DEPLOY.bat
echo ...Start Deploy MAYA ENV and Startup Image : %DEPLOYCMD%
call %DEPLOYCMD%
"D:\Autodesk\Maya%MAYA_VERSION%\bin\maya.exe"