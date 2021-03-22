@echo off
::或许maya2016注册表的安装目录
setlocal enabledelayedexpansion
SET OCTV_TECH=\\octvision.com\CG\Tech
::通用配置执行common deploy bat
set BATSDIR=%~dp0
set DEPLOYBAT=%BATSDIR%Maya_common_deploy.bat
echo ...Start Deploy MAYA ENV --- 
:: use common deploy script set one by one
::  maya 2019
set MAYA_VERSION=2019
call %DEPLOYBAT%
::  maya 2016
set MAYA_VERSION=2016
:: maya 2016 need  copy some vray plugin necessary script to maya setup root
set KEY_NAME=HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\Autodesk Maya %MAYA_VERSION%
set VALUE_NAME=InstallLocation
set TYPE_NAME="REG_SZ"
set str=
for /f "delims=" %%i in ('reg query "%KEY_NAME%" /v "%VALUE_NAME%"') do set str=!str!%%i
for /f "tokens=6 delims= " %%i in ("%str%") do set CopyDPath=%%i
xcopy /y /i "\\octvision.com\cg\Tech\maya_sixteen\CopyFile\%MAYA_VERSION%\bin" "%CopyDPath%bin"
xcopy /y /i "\\octvision.com\cg\Tech\maya_sixteen\CopyFile\%MAYA_VERSION%\rendererDesc" "%CopyDPath%bin\rendererDesc"
xcopy /y /i /e "\\octvision.com\cg\Tech\maya_sixteen\CopyFile\%MAYA_VERSION%\maya" "%userprofile%\Documents\maya"
echo ==============================================
if exist "%CopyDPath%resources\l10n\zh_CN" (ren "%CopyDPath%resources\l10n\zh_CN" "zh_CNBaked")
echo ==============================================
REM delete OCT_Pipeline Shelf
call %DEPLOYBAT%
:: set MAYA_MODULE_PATH
set MAYA_19_MOD_PATH=%OCTV_TECH%\maya_nineteen\moudules
set MAYA_16_MOD_PATH=%OCTV_TECH%\maya_dev\moudules\maya2016
setx MAYA_MODULE_PATH "%MAYA_19_MOD_PATH%;%MAYA_16_MOD_PATH%"
setX MAYA_UI_LANGUAGE en_US
echo -----------------------------------------------------------------------------
