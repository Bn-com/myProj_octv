@echo off
::或许maya2016注册表的安装目录
setlocal enabledelayedexpansion
setx MAYA_MODULE_PATH ""
REG delete HKCU\Environment /F /V MAYA_MODULE_PATH
echo -----------------------------------------------------------------------------
set MAYA_DOCUMENT=%userprofile%\Documents\maya
REM set timestamp=%DATE:/=-%_%TIME::=-%
REM set timestamp=%timestamp: =%
REM echo %timestamp%
set emm='date /t'
echo %emm%
for /F "tokens=2" %%i in ('date /t') do set mydate=%%i
echo %mydate%
For /f "tokens=1-3 delims=/:/ " %%a in ('time /t') do (set mytime=%%a-%%b-%%c)
set mytime=%mytime: =% 
echo %mydate%_%mytime%
REM xcopy MAYA_DOCUMENT 
