@echo off
::或许maya2016注册表的安装目录
setlocal enabledelayedexpansion
set BATSDIR=%~dp0
set MAYA_VERSION=2016
set KEY_NAME=HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\Autodesk Maya %MAYA_VERSION%
set VALUE_NAME=InstallLocation
set TYPE_NAME="REG_SZ"
set str=
for /f "delims=" %%i in ('reg query "%KEY_NAME%" /v "%VALUE_NAME%"') do set str=!str!%%i
for /f "tokens=6 delims= " %%i in ("%str%") do set CopyDPath=%%i
xcopy /y /i "\\octvision.com\cg\Tech\maya_sixteen\CopyFile\%MAYA_VERSION%\bin" "%CopyDPath%bin"
xcopy /y /i "\\octvision.com\cg\Tech\maya_sixteen\CopyFile\%MAYA_VERSION%\rendererDesc" "%CopyDPath%bin\rendererDesc"
REM delete OCT_Pipeline Shelf
set MAYA_DOC=%userprofile%\documents\maya
set MAYA_DOC_CURRENT_VERS=%MAYA_DOC%\%MAYA_VERSION%
set MAYA_DOC_PREFS=%MAYA_DOC_CURRENT_VERS%\prefs
set MAYA_DOC_ICON_DIR=%MAYA_DOC_PREFS%\icons
set MAYA_STARTUP_IMG=%MAYA_DOC_ICON_DIR%\MayaStartupImage.png
rem set batdir=%~dp0
rem maya env file 
set MAYA_ENV_FILE=%MAYA_DOC_CURRENT_VERS%\maya.env
echo ...Step 1 deal with maya env file ............
if exist %MAYA_DOC_CURRENT_VERS% (
	echo ... Folder %MAYA_DOC_CURRENT_VERS% exists
) else (
	REM echo We need To Create Folder:>>%MAYA_DOC_CURRENT_VERS%
	md %MAYA_DOC_CURRENT_VERS%
	echo ... Created Folder %MAYA_DOC_CURRENT_VERS% !
)
echo %MAYA_ENV_FILE%
if exist %MAYA_ENV_FILE% (
	echo Delete Existed maya env file
	del %MAYA_ENV_FILE%
	fsutil file createNew %MAYA_ENV_FILE% 0
) else (
	REM echo We need To Create Folder:>>%MAYA_DOC_CURRENT_VERS%
	echo echo We need To Create Folder %MAYA_ENV_FILE%
	REM echo >%MAYA_ENV_FILE%
	fsutil file createNew %MAYA_ENV_FILE% 0
)
echo ...Step 2 deal with usersetup.py.......
set USER_SETUP_PY_FILE=%MAYA_DOC_CURRENT_VERS%\scripts\usersetup.py
echo %USER_SETUP_PY_FILE%
if exist %USER_SETUP_PY_FILE% (
	echo Delete usersetup.py file
	del %USER_SETUP_PY_FILE%
)
echo ...Step 3 deal with shelf.....
set MAYA_DOC_SHELFS=%userprofile%\Documents\maya\%MAYA_VERSION%\prefs\shelves
echo %MAYA_DOC_SHELFS%\shelf_OCTPipeline.mel
if exist %MAYA_DOC_SHELFS%\shelf_OCTPipeline.mel (
	echo %MAYA_DOC_SHELFS%\shelf_OCTPipeline.mel exists.
	del %MAYA_DOC_SHELFS%\shelf_OCTPipeline.mel
	)
echo ...Final STEP set maya module path
:: set MAYA_MODULE_PATH
set MAYA_19_MOD_PATH=%OCTV_TECH%\maya_nineteen\moudules
set MAYA_16_MOD_PATH=%OCTV_TECH%\maya_dev\moudules\maya2016
setx MAYA_MODULE_PATH "%MAYA_19_MOD_PATH%;%MAYA_16_MOD_PATH%"
echo -----------------------------------------------------------------------------
setX MAYA_UI_LANGUAGE en_US
echo -----------------------------------------------------------------------------

