import os
import xlrd

# 根据镜头号设置Muster的优先级，黄仲维写
def getPriority(episode, shot = ''):
	priority = 50
#	excel = os.path.dirname(__file__) + os.path.sep + 'MusterPriority.xls'
	excel = r'\\file-cluster\GDC\Projects\WinxClubII\WinxClubII_Scratch\rendering\Priorities\MusterPriority.xls'
	try:
		book = xlrd.open_workbook(excel)
		thesheet = book.sheet_by_index(0)
		for rx in range(1, thesheet.nrows):
			if thesheet.cell_value(rx, 0) == episode or thesheet.cell_value(rx, 0) == episode + '_' + shot:
				priority = int(thesheet.cell_value(rx, 1))
				break
	except:
		pass
	return priority