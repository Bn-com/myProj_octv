# Copyright (c) 2007 The Foundry Visionmongers Ltd.  All Rights Reserved.

# This file is sourced by Nuke whenever it is run, either
# interactively or in order to run a script. The main purpose is
# to setup the plugin_path and to set variables used to generate
# filenames.

import sys
import os
import platform
import nuke

import re

# pywin32
path = os.getenv('PATH')
if re.search('32 bit', sys.version) == None:
	path = '//file-cluster/GDC/Resource/Support/Python/%s-x64/Lib/site-packages/pywin32_system32;%s' % (sys.winver, path)
	sys.path.append(r'\\file-cluster\GDC\Resource\Support\Python\%s-x64\Lib\site-packages\win32' % sys.winver)
	sys.path.append(r'\\file-cluster\GDC\Resource\Support\Python\%s-x64\Lib\site-packages\win32\lib' % sys.winver)
	sys.path.append(r'\\file-cluster\GDC\Resource\Support\Python\%s-x64\Lib\site-packages\Pythonwin' % sys.winver)
else:
	path = '//file-cluster/GDC/Resource/Support/Python/%s/Lib/site-packages/pywin32_system32;%s' % (sys.winver, path)
	sys.path.append(r'\\file-cluster\GDC\Resource\Support\Python\%s\Lib\site-packages\win32' % sys.winver)
	sys.path.append(r'\\file-cluster\GDC\Resource\Support\Python\%s\Lib\site-packages\win32\lib' % sys.winver)
	sys.path.append(r'\\file-cluster\GDC\Resource\Support\Python\%s\Lib\site-packages\Pythonwin' % sys.winver)
os.environ['PATH'] = path

#
if nuke.env['NukeVersionString'] == '6.3v1':
	domain = 'PRODUCT'
	username = 'superpub'
	password = '5D6D903FC267336E93BE404DBDC6B522'

	import pyUtil3 as pyUtil
	password = pyUtil.idmtService('Decrypt', password)

	import win32security
	import win32api

	hLogonToken = win32security.OpenProcessToken(win32api.GetCurrentProcess(), win32security.TOKEN_QUERY)
	hLogonToken = win32security.LogonUser (username, domain, password, win32security.LOGON32_LOGON_NEW_CREDENTIALS, win32security.LOGON32_PROVIDER_DEFAULT)
	hAdminToken = win32security.DuplicateTokenEx(hLogonToken, win32security.SecurityIdentification, win32security.TOKEN_ALL_ACCESS, win32security.TokenPrimary)
	win32security.ImpersonateLoggedOnUser(hAdminToken)
