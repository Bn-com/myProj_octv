@echo off

setlocal enabledelayedexpansion
set KEY_NAME=HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\Autodesk Maya 2016
set VALUE_NAME=InstallLocation
set TYPE_NAME="REG_SZ"
set str=
for /f "delims=" %%i in ('reg query "%KEY_NAME%" /v "%VALUE_NAME%"') do set str=!str!%%i
for /f "tokens=6-7 delims= " %%i in ("%str%") do set CopyDPath=%%i%%j
xcopy /y /i "\\octvision.com\CG\Tech\maya_sixteen\moudules\Vray\vrayplugins" "%CopyDPath%bin\vray"
"%CopyDPath%bin\maya.exe"