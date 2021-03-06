@echo on
rem set MAYA_MODULE_PATH=D:\devModule\myDev_2019
rem set MAYA_ENV_MODE=dev_mode
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
REM echo ....Step 2 deal with usersetup file ............

rem maya start up image -------------------------------
echo ....Step 2 deal with startup image ............
set USE_STARTUP_IMG=%batdir%icons\MayaStartup\maya%MAYA_VERSION%\%MAYA_ENV_MODE%\MayaStartupImage.png
echo ---------------------------------
echo USE_STARTUP_IMG %USE_STARTUP_IMG%
echo =================================
echo MAYA_STARTUP_IMG %MAYA_STARTUP_IMG%
echo .................................

if exist %MAYA_DOC_ICON_DIR% (
	echo Folder %MAYA_DOC_ICON_DIR% exists
) else (
	REM echo We need To Create Folder:>>%MAYA_DOC_CURRENT_VERS%
	md %MAYA_DOC_ICON_DIR%
	echo Created Folder %MAYA_DOC_ICON_DIR% !
)
if exist %MAYA_STARTUP_IMG% (
	echo ...2.1 Step : Delete Existed maya startupimag file
	del %MAYA_STARTUP_IMG%
	rem fsutil file createNew %MAYA_ENV_FILE% 0
	echo ...2.2 Step : copy maya start up image
	echo f | xcopy %USE_STARTUP_IMG% %MAYA_DOC_ICON_DIR% /Y
) else (
	REM echo We need To Create Folder:>>%MAYA_DOC_CURRENT_VERS%
	echo ...2.3 Step : Just copy maya startup image %USE_STARTUP_IMG%
	echo f | xcopy %USE_STARTUP_IMG% %MAYA_DOC_ICON_DIR% /Y
	REM echo >%MAYA_ENV_FILE%
	rem fsutil file createNew %MAYA_ENV_FILE% 0
)
REM delete shelves folder
set MAYA_DOC_SHELFS=%MAYA_DOC_PREFS%\shelves
echo %MAYA_DOC_SHELFS%
if exist %MAYA_DOC_SHELFS% (
	echo Shelf folder exists.
	rmdir  %MAYA_DOC_SHELFS% /q /s 
	)
	
