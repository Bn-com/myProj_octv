__author__ = 'xuweijian'
import sqlite3

class sqlModule():
    def creatTable(self,path,sql):
        con = sqlite3.connect(path)
        cu=con.cursor()
        cu.execute(sql)