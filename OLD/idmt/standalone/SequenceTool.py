# -*- coding: utf-8 -*-

import glob
import os
import re
import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sip

import idmt.pipeline.service

try:
	_fromUtf8 = QString.fromUtf8
except AttributeError:
	_fromUtf8 = lambda s: s

class MyAbstractItemModel(QAbstractTableModel):
	'''
	派生的模式类，用于序列的操作
	'''
	def __init__(self, parent = None):
		super(MyAbstractItemModel, self).__init__(parent)
		self.sequence = []
		self.order = Qt.AscendingOrder
		self.pattern = ''
		self.start = 1
 
	def columnCount(self, parent = QModelIndex()): 
		return 2

	def rowCount(self, parent = QModelIndex()): 
		return len(self.sequence)

	def data(self, index, role = Qt.DisplayRole):
		if not index.isValid(): 
			return QVariant() 
		elif role != Qt.DisplayRole: 
			return QVariant() 
		i = index.row()
		path = self.sequence[i]
		filename = os.path.basename(path)
		if index.column() == 0:
			return _fromUtf8(filename)
		elif index.column() == 1:
			i = self.start + i
			filename = self.pattern
			m = re.search(r'#+', filename)
			if m != None:
				filename = re.sub('#+', '%%0%dd' % len(m.group(0)) % i, filename)
			return _fromUtf8(filename)

	def GetFrame(self, filename):
		seq = None
		frame = None
		m = re.search(r'(-?\d+)(\.[^\.]+)?$', filename)
		if m != None:
			frame = int(m.group(1))
			if m.group(2) != None:
				seq = re.sub(r'(-?\d+)(\.[^\.]+)?$', r'####\g<2>', filename)
			else:
				seq = re.sub(r'(-?\d+)(\.[^\.]+)?$', '####', filename)
		return [seq, frame]

	def dropped(self, paths):
		self.emit(SIGNAL("layoutAboutToBeChanged()"))
		for path in paths:
			exists = False
			index = len(self.sequence)
			r = range(len(self.sequence))
			if self.order == Qt.DescendingOrder:
				index = -1
				r = range(len(self.sequence)-1, -1, -1)

			filename = os.path.basename(path)
			buf = self.GetFrame(filename)
			seq = buf[0]
			frame = buf[1]
			for i in r:
				currentFilename = os.path.basename(self.sequence[i])
				if filename.lower() == currentFilename.lower():
					exists = True
					break
				buf = self.GetFrame(currentFilename)
				currentSeq = buf[0]
				currentFrame = buf[1]
				if frame != None and currentFrame != None:
					if seq.lower() == currentSeq.lower():
						if frame < currentFrame:
							index = i
							break
						elif frame == currentFrame:
							if filename.lower() < currentFilename.lower():
								index = i
								break
					elif filename.lower() < currentFilename.lower():
						index = i
						break
				elif filename.lower() < currentFilename.lower():
					index = i
					break
			if exists:
				continue
			if self.order == Qt.DescendingOrder:
				index = index + 1
			if seq != None:
				self.pattern = seq
				if (self.order == Qt.AscendingOrder and index == 0) or (self.order == Qt.DescendingOrder and index == len(self.sequence)):
					self.start = frame
			self.sequence.insert(index, path)
		self.emit(SIGNAL("layoutChanged()"))

	def headerData(self, section, orientation, role = Qt.DisplayRole):
		header = QVariant()
		if orientation == Qt.Horizontal and role == Qt.DisplayRole:
			if section == 0:
				#print "Filename"
				header = self.tr("Filename")
				#print str(_fromUtf8(header))
			elif section == 1:
				header = self.tr("New Filename")
		return header

	def rename(self):
		self.emit(SIGNAL("layoutAboutToBeChanged()"))
		for i in range(len(self.sequence)):
			frame = self.start + i
			filename = self.pattern
			m = re.search(r'#+', filename)
			if m != None:
				filename = re.sub('#+', '%%0%dd' % len(m.group(0)) % frame, filename)
			newFilename = os.path.join(os.path.dirname(self.sequence[i]), filename)
			os.rename(self.sequence[i], newFilename)
			self.sequence[i] = newFilename
		self.emit(SIGNAL("layoutChanged()"))

	def sort(self, column, order = Qt.AscendingOrder):
		if column != 0:
			return
		if order != self.order:
			self.order = order
			self.emit(SIGNAL("layoutAboutToBeChanged()"))
			self.sequence.reverse()
			self.emit(SIGNAL("layoutChanged()"))

	def delete(self, selected):
		selected.sort()
		selected.reverse()
		for i in selected:
			self.sequence.pop(i)
		self.emit(SIGNAL("layoutChanged()"))

class MyTableView(QTableView):
	'''
	派生的视图类，支持拖放
	'''
	def __init__(self, parent = None):
		super(MyTableView, self).__init__(parent)
		self.setAcceptDrops(True)
 
	def dragEnterEvent(self, event):
		if event.mimeData().hasUrls:
			event.accept()
		else:
			event.ignore()
 
	def dragMoveEvent(self, event):
		if event.mimeData().hasUrls:
			#event.setDropAction(Qt.CopyAction)
			event.accept()
		else:
			event.ignore()
 
	def dropEvent(self, event):
		if event.mimeData().hasUrls:
			#event.setDropAction(Qt.CopyAction)
			event.accept()
			links = []
			for url in event.mimeData().urls():
				path = unicode(url.toLocalFile().toUtf8(), 'utf-8')
				if os.path.isfile(path):
					links.append(path)
			self.emit(SIGNAL("dropped"), links)
		else:
			event.ignore()

	def keyPressEvent(self, event):
		if event.key() == Qt.Key_Delete:
			selecteds = []
			for selected in self.selectedIndexes():
				if not selected.row() in selecteds:
					selecteds.append(selected.row())
			self.emit(SIGNAL("delete"), selecteds)


class MyHorizontalHeaderView(QHeaderView):
	'''
	派生的表头类，只允许第一列用于排序
	'''
	def __init__(self, parent = None):
		super(MyHorizontalHeaderView, self).__init__(Qt.Horizontal, parent)

		self.setDefaultAlignment(Qt.AlignLeft)

		self.setClickable(True)
		self.setSortIndicatorShown(True)
		self.setSortIndicator(0, Qt.AscendingOrder)
		self.mySortIndicatorOrder = self.sortIndicatorOrder()
		self.sectionClicked.connect(self.OnSectionClicked)

	def OnSectionClicked(self, logicalIndex):
		if logicalIndex == 0:
			self.mySortIndicatorOrder = self.sortIndicatorOrder()
		else:
			self.setSortIndicator(0, self.mySortIndicatorOrder)

class Dialog(QDialog):
	'''
	主界面，可以切换显示语言
	'''
	def __init__(self, parent = None):
		#变量
		self.pattern = ''
		self.start = 1

		#maya2011以上里面调用方法
		if re.search(r'^Maya-\d{4}(-x64)?$', str(qApp.applicationName())) != None:
			import maya.OpenMayaUI
			#删除旧窗口
			oldDialog = maya.OpenMayaUI.MQtUtil.findWindow('SequenceTool')
			if oldDialog != None:
				sip.wrapinstance(long(oldDialog), QWidget).close()
			#将maya主窗口设为父窗口，否则将会出现在任务栏
			ptr = maya.OpenMayaUI.MQtUtil.mainWindow()
			parent = sip.wrapinstance(long(ptr), QWidget)

		super(Dialog, self).__init__(parent)
		self.setObjectName(_fromUtf8("SequenceTool"))
		windowFlags = self.windowFlags()
		windowFlags = windowFlags & ~Qt.WindowContextHelpButtonHint	# 去掉帮助按钮
		windowFlags = windowFlags | Qt.WindowMinimizeButtonHint		# 最小化按钮
		windowFlags = windowFlags | Qt.WindowStaysOnTopHint
		self.setWindowFlags(windowFlags)
		self.setAttribute(Qt.WA_DeleteOnClose)

		'''
		列出可选择的界面语言
		列出i18n目录里面所有qm文件，并从里面翻译出"English"这个词，于是就得到一个类似这样的字典：
		{"en" : "English", "zh_CN", "简体中文"}
		'''
		locales = {}
		fnlist = glob.glob(os.path.join(os.path.dirname(os.path.dirname(__file__)), "i18n", "SequenceTool_*.qm"))
		for fn in fnlist:
			locale = os.path.basename(fn)[13:-3]
			if not locales.has_key(locale):
				translator = QTranslator()
				translator.load(fn)
				locales[locale] = translator.translate("Dialog", "English")
		if not locales.has_key("en"):
			locales["en"] = _fromUtf8("English")

		# 从数据库读出用户的语言偏好
		registery = idmt.pipeline.service.Service()
		language = registery.RegQueryValue('language', QLocale.system().name())
		if not locales.has_key(locale):
			language = "en"
		self.translator = QTranslator()
		self.translator.load("SequenceTool_" + language, os.path.join(os.path.dirname(os.path.dirname(__file__)), 'i18n'))
		qApp.installTranslator(self.translator)

		# 菜单
		self.helpAct = QAction(self.tr("Online Support"), self, statusTip = self.tr("Show the online support page"), triggered = self.help)
		self.menuBar = QMenuBar()
		self.helpMenu = QMenu(self.tr("Help"), self)
		self.helpMenu.addAction(self.helpAct)
		self.menuBar.addMenu(self.helpMenu)

		# comboBox，可选择的界面语言
		self.comboBox = QComboBox(self)
		self.comboBox.setObjectName(_fromUtf8("comboBoxLanguage"))
		localeList = locales.keys()
		localeList.sort()
		for locale in localeList:
			self.comboBox.addItem(locales[locale], QVariant(locale))
		index = self.comboBox.findData(str(language))
		self.comboBox.setCurrentIndex(index)

		self.setWindowTitle(self.tr("Sequence Rename"))
		self.resize(960, 640)

		self.tableView = MyTableView(self)
		self.tableView.setAlternatingRowColors(True)
		self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
		#self.tableView.setIconSize(QSize(72, 72))

		self.model = MyAbstractItemModel(self)
		self.model.setObjectName(_fromUtf8("model"))
		self.model.pattern = self.pattern
		self.model.start = self.start

		self.tableView.setModel(self.model)
		hHeader = MyHorizontalHeaderView(self.tableView)

		self.tableView.setHorizontalHeader(hHeader)
		hHeader.resizeSection(0, 440)
		hHeader.resizeSection(1, 440)
		self.tableView.verticalHeader().setVisible(False)
		self.tableView.setSortingEnabled(True)

		self.labelPattern = QLabel(self.tr("Pattern:"))
		self.lineEditPattern = QLineEdit(self.pattern)
		self.lineEditPattern.setObjectName(_fromUtf8("lineEditPattern"))
		self.labelStart = QLabel(self.tr("Start:"))
		self.lineEditStart = QLineEdit(str(self.start))
		self.lineEditStart.setObjectName(_fromUtf8("lineEditStart"))
		self.lineEditStart.setValidator(QIntValidator(self.lineEditStart))

		buttonBox = QDialogButtonBox()
		self.pushButtonRename = buttonBox.addButton(self.tr("Rename"), QDialogButtonBox.ApplyRole)

		gridLayout = QGridLayout()
		gridLayout.setMenuBar(self.menuBar)
		gridLayout.addWidget(self.comboBox, 0, 0)
		gridLayout.addWidget(self.tableView, 1, 0, 1, 2)
		gridLayout.addWidget(self.labelPattern, 2, 0)
		gridLayout.addWidget(self.lineEditPattern, 2, 1)
		gridLayout.addWidget(self.labelStart, 3, 0)
		gridLayout.addWidget(self.lineEditStart, 3, 1)
		gridLayout.addWidget(buttonBox, 4, 0, 1, 2)
		self.setLayout(gridLayout)

		self.connect(self.tableView, SIGNAL("dropped"), self.pictureDropped)
		self.connect(self.tableView, SIGNAL("delete"), self.model.delete)
		#self.lineEditPattern.textChanged.connect(self.OnLineEditPatternTextChanged)
		#self.lineEditStart.textChanged.connect(self.OnLineEditStartTextChanged)
		self.pushButtonRename.clicked.connect(self.model.rename)
		QMetaObject.connectSlotsByName(self)

	def on_comboBoxLanguage_currentIndexChanged(self, index):
		if type(index) != int:
			return
		language = self.comboBox.itemData(index).toString()
		registery = idmt.pipeline.service.Service()
		registery.RegSetValue('language', language)
		
		registery = idmt.pipeline.service.Service()
		self.translator = QTranslator()
		self.translator.load("SequenceTool_" + language, os.path.join(os.path.dirname(os.path.dirname(__file__)), 'i18n'))
		qApp.installTranslator(self.translator)

	def pictureDropped(self, url):
		self.model.dropped(url)
		self.lineEditPattern.setText(self.model.pattern)
		self.lineEditStart.setText(str(self.model.start))

	def on_lineEditPattern_textChanged(self, text):
		self.model.pattern = unicode(text.toUtf8(), 'utf-8')
		self.model.emit(SIGNAL("layoutChanged()"))

	def on_lineEditStart_textChanged(self, text):
		try:
			self.model.start = int(text)
			self.model.emit(SIGNAL("layoutChanged()"))
		except:
			pass

	def changeEvent(self, e):
		if e.type() == QEvent.LanguageChange:
			self.retranslateUi()
			e.accept()
		QDialog.changeEvent(self, e)

	def retranslateUi(self):
		self.helpMenu.setTitle(self.tr("Help"))
		self.helpAct.setText(self.tr("Online Support"))
		self.helpAct.setStatusTip(self.tr("Show the online support page"))
		self.setWindowTitle(self.tr("Sequence Rename"))
		self.labelPattern.setText(self.tr("Pattern:"))
		self.labelStart.setText(self.tr("Start:"))
		self.pushButtonRename.setText(self.tr("Rename"))

	def help(self):
		import webbrowser
		webbrowser.open('http://talk.idmt.com.cn/viewthread.php?tid=67662')

#命令行运行
if __name__ == '__main__':
	app = QApplication(sys.argv)
	dialog = Dialog()
	sys.exit(dialog.exec_())