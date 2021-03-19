::REG delete HKCU\Environment /V NUKE_PATH /f
REG delete "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /V NUKE_PATH /f
setx NUKE_PATH "F:\Development\octProj\oct\Nuke"  /m
::"C:\Program Files\Nuke9.0v3\Nuke9.0.exe"