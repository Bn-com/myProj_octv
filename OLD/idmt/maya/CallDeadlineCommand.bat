@ECHO OFF



::参数
SET COMPUTER=%1
SET OUTPUT_DIRECTORY=%2
SET SUBMISSION=%3



::安装Deadline8
IF NOT EXIST C:\tools64\Thinkbox\Deadline8 XCOPY /E \\file-cluster\GDC\Scratch\IT\CMR\03_NetRender\C1_Deadline\Deadline8.0.12.4\tools64\Thinkbox\Deadline8 C:\tools64\Thinkbox\Deadline8\
IF NOT EXIST C:\ProgramData\Thinkbox\Deadline8 XCOPY /E \\file-cluster\GDC\Scratch\IT\CMR\03_NetRender\C1_Deadline\Deadline8.0.12.4\ProgramData\Thinkbox\Deadline8 C:\ProgramData\Thinkbox\Deadline8\
SET DEADLINE_PATH=C:\tools64\Thinkbox\Deadline8\bin
SET PATH=%DEADLINE_PATH%;%PATH%



::工程目录
SET PARITY=Even
IF %COMPUTER:~-1% == 1 SET PARITY=Odd
IF %COMPUTER:~-1% == 3 SET PARITY=Odd
IF %COMPUTER:~-1% == 5 SET PARITY=Odd
IF %COMPUTER:~-1% == 7 SET PARITY=Odd
IF %COMPUTER:~-1% == 9 SET PARITY=Odd
SET ProjectPath=\\file-cluster\GDC\Netrender\Maya_%PARITY%\%COMPUTER%
IF NOT EXIST %ProjectPath% MD %ProjectPath%
IF NOT EXIST %ProjectPath%\images MD %ProjectPath%\images
IF NOT EXIST %ProjectPath%\workspace.mel COPY \\file-cluster\GDC\Resource\Support\Maya\Import\projects\8.5\workspace.mel %ProjectPath%\workspace.mel



::输出路径
IF NOT EXIST %OUTPUT_DIRECTORY% MD %OUTPUT_DIRECTORY%



::提交
CD %DEADLINE_PATH%

ECHO ON
%DEADLINE_PATH%\deadlinecommand.exe %SUBMISSION% 2> nul