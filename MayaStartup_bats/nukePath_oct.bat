::REG delete HKCU\Environment /F /V NUKE_PATH
REG delete "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /V NUKE_PATH /f
setx NUKE_PATH "\\octvision.com\CG\Tech\Nuke" /m
::"C:\Program Files\Nuke9.0v3\Nuke9.0.exe"