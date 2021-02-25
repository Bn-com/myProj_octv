import os
import sys
dir = os.path.dirname(__file__)
sys.path.append(dir + '\\xlrd-0.9.2')
import xlrd


class xls_info(object):
    xls_path = None
    def __init__(self,xls_path = ""):
        self.xls_path = xls_path
        
    def get_column_with_name_in_excel(self, column_name):
        wb = xlrd.open_workbook(self.xls_path)
        sh = wb.sheet_by_index(0)
        column_index = 0
        asset_name_list = []    
        for rownum in range(sh.nrows):
            for i, value in enumerate(sh.row_values(rownum)):
                try:            
                    if str(value).lower().find(column_name.lower()) != -1 : 
                        column_index = i 
                        return column_index
                except:
                    pass

    def get_status_info_by_asset_name(self,column_index):  
        wb = xlrd.open_workbook(self.xls_path)
        sheet = wb.sheet_by_index(0)
        name_is_find = False
        column_cell_value_list = []
        for rownum in range(sheet.nrows):
            column_cell_value_list.append(sheet.row_values(rownum)[column_index])
        return column_cell_value_list


           
            