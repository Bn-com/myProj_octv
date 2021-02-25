@echo off
::或许maya2016注册表的安装目录
setlocal enabledelayedexpansion
set KEY_NAME=HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\Autodesk Maya 2016
set VALUE_NAME=InstallLocation
set TYPE_NAME="REG_SZ"
set str=
for /f "delims=" %%i in ('reg query "%KEY_NAME%" /v "%VALUE_NAME%"') do set str=!str!%%i
for /f "tokens=6 delims= " %%i in ("%str%") do set CopyDPath=%%i
xcopy /y /i "\\octvision.com\cg\Tech\maya_sixteen\CopyFile\2016\bin" "%CopyDPath%bin"
xcopy /y /i "\\octvision.com\cg\Tech\maya_sixteen\CopyFile\2016\rendererDesc" "%CopyDPath%bin\rendererDesc"
xcopy /y /i /e "\\octvision.com\cg\Tech\maya_sixteen\CopyFile\2016\maya" "%userprofile%\Documents\maya"
if exist "%CopyDPath%resources\l10n\zh_CN" (ren "%CopyDPath%resources\l10n\zh_CN" "zh_CNBaked")