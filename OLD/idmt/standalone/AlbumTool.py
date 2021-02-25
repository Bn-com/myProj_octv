# -*- coding: utf-8 -*-
# Copyright (C) 2000-2010 IDMT. All rights reserved.
'''
Album Tool:
拼图工具
'''
__author__	= 'huangzhongwei@idmt.com.cn'
__date__	= '2011-01-13'

import os
#import tkFileDialog
import tkMessageBox
import tempfile
import Tix
#import time
from Tkinter import *
#import sys
import pymssql
from win32com.client import Dispatch
import Image
import ImageDraw
import re

import idmt.pipeline.project

repositories = [r'\\file-cluster\GDC\Projects', r'\\file-cluster\GDC\Projects\SideProjects\TestProjects']
sequenceProjects = ['Woodlies', 'Ninjago', 'GummiTarzan']

class openDialog(Frame):
	def __init__(self, master=None):
		self.root = master
		self.createWidgets()

	def createWidgets(self):
		""" Create widgets
		"""
		self.fFrame = Frame(self.root)

		optionList = []
		for repository in repositories:
			if not os.path.isdir(repository):
				continue
			projects = os.listdir(repository)
			for project in projects:
				if not os.path.isdir(os.path.join(repository, project)):
					continue
				if not project in optionList:
					optionList.append(project)
		optionList.sort()

		self.projectName = StringVar()
		self.projectName.set(optionList[0])
		self.om = OptionMenu(self.fFrame, self.projectName, *optionList)
		self.om.pack(anchor = W)

		self.svDir = StringVar()
		self.eDir  = Entry(self.fFrame, width=30, textvariable=self.svDir)
		self.eDir.pack()

		Button(self.fFrame, text = "开拼", command = self.getStart).pack()
		self.fFrame.pack()

	def getStart(self):
		project = self.projectName.get()
		episode = self.svDir.get()

		CreateAlbum(project, episode)

def GetFolder(root, folderName):
	if not os.path.isdir(root):
		return None
	if re.search(r'^[a-z][0-9]{4}$', folderName, re.IGNORECASE) != None:	# Ninjago 的episode 少了E
		folderName = re.sub(r'^[^0-9]+', '', folderName)
	folders = os.listdir(root)
	for folder in folders:
		path = os.path.join(root, folder)
		if not os.path.isdir(path):
			continue
		if re.compile(r'%s$' % (folderName), re.IGNORECASE).search(folder) != None:
			return path
	return None

def CreateAlbum(project, episode):
	# project
	repositoryFolder = ''
	for repository in repositories:
		repositoryFolder = os.path.join(repository, project)
		if os.path.isdir(repositoryFolder):
			break
	if not os.path.isdir(repositoryFolder):
		tkMessageBox.showwarning(title = '出错啦！', message = '找不到 %s 项目' % (project))
		return

	# parity
	parityFolder = ''
	parity = idmt.pipeline.project.GetParity(episode)
	parityFolder = os.path.join(repositoryFolder, r'Production\Render\Compositing', parity)

	# episode
	episodeFolder = GetFolder(parityFolder, episode)
	if episodeFolder == None:	# Ninjago 放错了奇偶
		if parity == 'ODD':
			episodeFolder = GetFolder(os.path.join(repositoryFolder, r'Production\Render\Compositing', 'EVEN'), episode)
		else:
			episodeFolder = GetFolder(os.path.join(repositoryFolder, r'Production\Render\Compositing', 'ODD'), episode)
	if episodeFolder == None:
		tkMessageBox.showwarning(title = '出错啦！', message = '找不到 %s 集：\n\n%s' % (episode, parityFolder))
		return

	# db shots
	shots = []
	try:
		conn = pymssql.connect(host = '192.168.168.16', user = 'ECAUser', password = 'hk#$G#324f', database = 'idmtPlex_' + project)
		cur = conn.cursor()
		sqlCmd = "SELECT ISNULL(Tag, '') AS Tag, anim_sc FROM TB_Anim WHERE (anim_ep = '%s') ORDER BY Tag, anim_sc" % (episode)
		cur.execute(sqlCmd)
		for row in cur:
			shots.append([row[0], row[1]])
	except:
		tkMessageBox.showwarning(title = '出错啦！', message = '查询数据库镜头出错：\n\n%s' % (sys.exc_info()[1]))
		return
	if len(shots) == 0:
		tkMessageBox.showwarning(title = '出错啦！', message = '数据库还没有建立 %s 集的镜头' % (episode))
		return

	# image
	width = 1650
	height = (len(shots) / 4 + 1) * 300
	im = Image.new('RGB', (width, height), 0)
        draw = ImageDraw.Draw(im)
        draw.text((50, 50), "%s-%s auto generated." % (project, episode))
        
	# has sequence
	#hasSeq = False
	#for i in range(len(sequenceProjects)):
	#	if re.compile(r'%s$' % (project), re.IGNORECASE).search(sequenceProjects[i]) != None:
	#		hasSeq = True
	#		break
	hasSeq = idmt.pipeline.project.project().HasSeq(project)

	# forder shot
	for i in range(len(shots)):
		print 'Finish: %d%%' % (float(i) / len(shots) * 100)

		sequence = shots[i][0]
		shot = shots[i][1]

		x = (i + 1) % 4 * 410 + 20
		y = (i + 1) / 4 * 300 + 15
		if re.search('[0-9a-zA-Z]', sequence) == None:
			draw.text((x, y - 10), '%s_%s' % (episode, shot))
		else:
			draw.text((x, y - 10), '%s_%s_%s' % (episode, sequence, shot))

		# sequence
		sequenceFolder = ''
		if hasSeq:
			sequenceFolder = GetFolder(episodeFolder, sequence)
			if sequenceFolder == None:
				continue
		else:
			sequenceFolder = episodeFolder

		# shot
		shotFolder = GetFolder(sequenceFolder, shot)
		if shotFolder == None:
			continue

		# frame
		frame = ''
		for root, dirs, files in os.walk(shotFolder):
			if re.compile(r'[/\\](right|old)[/\\]|[/\\](right|old)$', re.IGNORECASE).search(root) == None:
				if 'Thumbs.db' in files:
					files.remove('Thumbs.db')
				if files != []:
					img = os.path.join(root, files[int(len(files)*0.618)])
					#if re.compile(r'\.(jpeg|jpg|tga|tif|tiff)$', re.IGNORECASE).search(img) != None:
					frame = img
		if not os.path.isfile(frame):
			continue
		print frame

		temp = ''
		if re.compile(r'\.(dpx|tif|tiff)$', re.IGNORECASE).search(frame) != None:
			temp = os.path.join(tempfile.gettempdir(), '%s.jpg' % (os.path.basename(frame)))
			if os.path.isfile(temp):
				os.remove(temp)
			command = "\\\\file-cluster\\GDC\\Resource\\Support\\Others\\ImageMagick-5.4.6-Q16\\convert.exe \"%s\" \"%s\"" % (frame, temp)
			os.system(command)
			frame = temp
		try:
			thumbnail = Image.open(frame)
			thumbnail = thumbnail.resize((384, 216))
			im.paste(thumbnail, (x, y))
		except:
			continue
		if os.path.isfile(temp):
			os.remove(temp)

	print "Finish: 100% Done."

	temp = os.path.join(tempfile.gettempdir(), '%s_%s.jpg' % (project, episode))
	im.save(temp)
	ie = Dispatch("InternetExplorer.Application")
	ie.visible = 1
	ie.navigate(temp)

if __name__ == "__main__":
	root = Tix.Tk()
	root.title("拼图工具")
	od = openDialog(root)
	root.mainloop()