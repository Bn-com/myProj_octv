@echo off
::或许maya2016注册表的安装目录
setlocal enabledelayedexpansion
setx MAYA_MODULE_PATH ""
REG delete HKCU\Environment /F /V MAYA_MODULE_PATH
echo -----------------------------------------------------------------------------
set MAYA_DOCUMENT=%userprofile%\Documents\maya
set datestamp=%date:~0,4%%date:~5,2%%date:~8,2%
set hour=%time:~0,2%
set timestamp=%hour: =0%%time:~3,2%%time:~6,2%
set datetimeStamp=%datestamp%%timestamp%
REM echo %datetimeStamp%
xcopy /y /i %MAYA_DOCUMENT% %MAYA_DOCUMENT%_%datetimeStamp%
echo maya 配置文件夹已经另存，接下来程序会移除已经存在的maya配置文件夹
rmdir /s /q %MAYA_DOCUMENT% && echo 再次启动maya将以默认配置启动  || echo 可能是您已经做过删除操作或出现其他异常，请确认文件夹是否清除
