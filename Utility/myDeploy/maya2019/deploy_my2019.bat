@echo off
setx MAYA_MODULE_PATH \\octvision.com\CG\Tech\maya_nineteen\moudules
setX MAYA_UI_LANGUAGE en_US
set MAYA_VERS=2020
set MAYA_DOC=%userprofile%\documents\maya
set MAYA_DOC_CURRENT_VERS=%MAYA_DOC%\%MAYA_VERS%
set MAYA_ENV_FILE=%MAYA_DOC_CURRENT_VERS%\maya.env

if exist %MAYA_DOC_CURRENT_VERS% (
	echo Folder %MAYA_DOC_CURRENT_VERS% exists
) else (
	REM echo We need To Create Folder:>>%MAYA_DOC_CURRENT_VERS%
	md %MAYA_DOC_CURRENT_VERS%
	echo Created Folder %MAYA_DOC_CURRENT_VERS% !
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

