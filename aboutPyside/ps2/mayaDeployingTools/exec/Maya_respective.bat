@echo off
::或许maya2016注册表的安装目录
setlocal enabledelayedexpansion
set MAYA_VERSION=2016
set KEY_NAME=HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\Autodesk Maya %MAYA_VERSION%
set VALUE_NAME=InstallLocation
set TYPE_NAME="REG_SZ"
set str=
for /f "delims=" %%i in ('reg query "%KEY_NAME%" /v "%VALUE_NAME%"') do set str=!str!%%i
for /f "tokens=6 delims= " %%i in ("%str%") do set CopyDPath=%%i
xcopy /y /i "\\octvision.com\cg\Tech\maya_sixteen\CopyFile\%MAYA_VERSION%\bin" "%CopyDPath%bin"
xcopy /y /i "\\octvision.com\cg\Tech\maya_sixteen\CopyFile\%MAYA_VERSION%\rendererDesc" "%CopyDPath%bin\rendererDesc"
xcopy /y /i /e "\\octvision.com\cg\Tech\maya_sixteen\CopyFile\%MAYA_VERSION%\maya" "%userprofile%\Documents\maya"
if exist "%CopyDPath%resources\l10n\zh_CN" (ren "%CopyDPath%resources\l10n\zh_CN" "zh_CNBaked")
REM delete OCT_Pipeline Shelf

set MAYA_DOC_SHELFS=%userprofile%\Documents\maya\%MAYA_VERSION%\prefs\shelves
echo %MAYA_DOC_SHELFS%\shelf_OCTPipeline.mel
if exist %MAYA_DOC_SHELFS%\shelf_OCTPipeline.mel (
	echo %MAYA_DOC_SHELFS%\shelf_OCTPipeline.mel exists.
	del %MAYA_DOC_SHELFS%\shelf_OCTPipeline.mel
	)