@echo off
::����maya2016ע���İ�װĿ¼
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
echo maya �����ļ����Ѿ���棬������������Ƴ��Ѿ����ڵ�maya�����ļ���
rmdir /s /q %MAYA_DOCUMENT% && echo �ٴ�����maya����Ĭ����������  || echo ���������Ѿ�����ɾ����������������쳣����ȷ���ļ����Ƿ����
