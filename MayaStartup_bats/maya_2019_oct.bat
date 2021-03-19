@echo off
REM set MAYA_MODULE_PATH=\\octvision.com\CG\Tech\maya_nineteen\moudules
set MAYA_MODULE_PATH=\\octvision.com\CG\Tech\maya_nineteen\moudules
set MAYA_ENV_MODE=client_mode
set MAYA_VERSION=2019
set batdir=%~dp0
set DEPLOYCMD=%batdir%MAYA_DEPLOY.bat
echo ...Start Deploy MAYA ENV and Startup Image : %DEPLOYCMD%
call %DEPLOYCMD%
"D:\Autodesk\Maya2019\bin\maya.exe"