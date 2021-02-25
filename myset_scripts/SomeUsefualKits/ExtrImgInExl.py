#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ExtrImgInExl
__author__ = zhangben 
__mtime__ = 2019/10/11 : 18:15
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
"""
import win32com.client       # Need pywin32 from pip
from PIL import ImageGrab    # Need PIL as well
import os
#
# excel = win32com.client.Dispatch("Excel.Application")
# workbook = excel.ActiveWorkbook
# #
# # wb_folder = workbook.Path
# wb_name = workbook.Name
# wb_path = os.path.join(wb_folder, wb_name)
#
# #print "Extracting images from %s" % wb_path
# print("Extracting images from", wb_path)
#
# image_no = 0
#
# for sheet in workbook.Worksheets:
#     for n, shape in enumerate(sheet.Shapes):
#         if shape.Name.startswith("Picture"):
#             # Some debug output for console
#             image_no += 1
#             print("---- Image No. %07i ----", image_no)
#
#             # Sequence number the pictures, if there's more than one
#             num = "" if n == 0 else "_%03i" % n
#
#             filename = sheet.Name + num + ".jpg"
#             file_path = os.path.join (wb_folder, filename)
#
#             #print "Saving as %s" % file_path    # Debug output
#             print('Saving as ', file_path)
#
#             shape.Copy() # Copies from Excel to Windows clipboard
#
#             # Use PIL (python imaging library) to save from Windows clipboard
#             # to a file
#             image = ImageGrab.grabclipboard()
#             image.save(file_path,'jpeg')
#


# from PIL import ImageGrab
# import win32com.client as win32
#
# excel = win32.gencache.EnsureDispatch('Excel.Application')
# workbook = excel.Workbooks.Open(r'E:\dev_debug\actorFacial.xlsx')
#
# for sheet in workbook.Worksheets:
#     for i, shape in enumerate(sheet.Shapes):
#         print i,shape.Name
#         if shape.Name.startswith('Picture'):
#             shape.Copy()
#             image = ImageGrab.grabclipboard()
#             image.save('{}.jpg'.format(i+1), 'jpeg')


import xlrd
import json
import codecs
import os
exf = r"E:\dev_debug\exl\wbook.xlsx"
get_data = xlrd.open_workbook(exf)

wkSheets = get_data.sheet_names()
for eaSht in wkSheets:
    print ('{}--{}'.format(wkSheets.index(eaSht),eaSht))
