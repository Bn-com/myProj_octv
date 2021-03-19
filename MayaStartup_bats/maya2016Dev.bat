@echo on
REM SETLOCAL ENABLEDELAYEDEXPANSION 
set MAYA_VERSION=2016
set MAYA_ENV_MODE=dev_mode
REM for /F %%I in ("%~dp0..\") do set ENV_ROOT=%%~dpI
for %%f in ("%cd%\..") do set "ENV_DEV_ROOT=%%~ff"
set MAYA_MODULE_PATH=%MAYA_MODULE_PATH%;%ENV_DEV_ROOT%\octProj\oct\maya_dev\moudules
echo %MAYA_MODULE_PATH%
set DEVKIT_LOCATION=C:\Users\zhangben\devkitBase\
set MAYA_LOCATION=D:\Autodesk\maya2016
set PATH=%PATH%;%MAYA_LOCATION%\bin
REM set MAYA_ENABLE_LEGACY_VIEWPORT=1
set DPRT=dprint
set batdir=%~dp0
set DEPLOYCMD=%batdir%MAYA_DEPLOY.bat
echo ...Start Deploy MAYA ENV and Startup Image : %DEPLOYCMD%
call %DEPLOYCMD%
echo ...Ready Startup MAYA APP...
"D:\Autodesk\Maya2016\bin\maya.exe"
echo ....exit cmd window.......
cmd.exe exit 


