@set PATH=\\file-cluster\GDC\Resource\Support\Python\Python26;\\file-cluster\GDC\Resource\Support\Python\2.6\Lib\site-packages\pywin32_system32;%PATH%;\\file-cluster\GDC\Resource\Support\bin
@set PYTHONPATH=\\file-cluster\GDC\Resource\Support\Python\Python26\Lib\site-packages;\\file-cluster\GDC\Resource\Support\Python\2.6\DLLs;\\file-cluster\GDC\Resource\Support\Python\2.6\Lib\site-packages
@set PYTHONDONTWRITEBYTECODE=x
@set PYTHONIOENCODING=gbk
@python.exe \\file-cluster\GDC\Resource\Development\Maya\GDC\Plug\Python\GDC\Other\studio_a2\scripts\Modify_winClipboard.py
@exit %errorlevel%