# -*- coding: utf-8 -*-

'''
project class
'''
__author__    = 'huangzhongwei'
__date__    = '2011-08-18'

import os
import pyodbc
import re
import shutil
import sqlite3
import tempfile

def myCmd(command, source, dest):
    cmd = r'%s "%s" "%s"' % (command, source, dest)
    os.system(r'\\file-cluster\GDC\Resource\Support\bin\checkinClient ' + cmd)

def yun360():
    temp = tempfile.gettempdir()
    
    cx = sqlite3.connect('%s/idmtPlex.db' % temp)
    cu = cx.cursor()
    cu.execute('CREATE TABLE TB_Project (id integer primary key, name varchar(50), shortName varchar(50), repository varchar(255), fps int, resolution varchar(50))') 

    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=192.168.168.16;DATABASE=idmtPlex;UID=EWAUser;PWD=hk#$G#324f')
    cursor = cnxn.cursor()
    cmd_name = 'P_TD_GetProjects'
    sqlquery = cursor.execute(cmd_name)
    data = sqlquery.fetchone()
    while data:
        cu.execute('INSERT INTO TB_Project VALUES((?), (?), (?), (?), (?), (?))', (data[0], data[1], data[2], data[3], data[5], data[4]))
        data = sqlquery.fetchone()
    cx.commit() 
    cursor.close()
    cnxn.close()

    cu.execute('CREATE TABLE TB_Anim (pid integer, anim_id integer, anim_ep varchar(50), Tag varchar(50), anim_sc varchar(50), length integer, frmStart integer, frmEnd integer, primary key (pid, anim_id))')
    cu.execute('CREATE TABLE TB_Asset (pid integer, asset_id integer, asset_type varchar(50), asset_name varchar(255), primary key (pid, asset_id))')
    cu.execute('CREATE TABLE TB_AssetFileSer (pid integer, fs_id integer, asset_id integer, asset_sep varchar(255), primary key (pid, fs_id))')
    cu.execute('CREATE TABLE TB_AssetFileSerInAnim (pid integer, afsa_id integer, fs_id integer, anim_id integer, primary key (pid, afsa_id))')
    projects = {60: 'Calimero', 79: 'DiveOllyDive5', 34: 'Ninjago', 76: 'ShunLiu', 5: 'Strawberry', 52: 'ZoomWhiteDolphin'}
    for projectId in projects.keys():
        cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=192.168.168.16;DATABASE=idmtPlex_%s;UID=EWAUser;PWD=hk#$G#324f' % projects[projectId])
        cursor = cnxn.cursor()
        
        cmd_name = 'SELECT anim_id, anim_ep, Tag, anim_sc, length, frmStart, frmEnd FROM TB_Anim'
        sqlquery = cursor.execute(cmd_name)
        data = sqlquery.fetchone()
        while data:
            cu.execute('INSERT INTO TB_Anim VALUES((?), (?), (?), (?), (?), (?), (?), (?))', (projectId, data[0], data[1], data[2], data[3], data[4], data[5], data[6]))
            data = sqlquery.fetchone()
        cx.commit()
        
        cmd_name = 'SELECT asset_id, asset_type, asset_name FROM TB_Asset'
        sqlquery = cursor.execute(cmd_name)
        data = sqlquery.fetchone()
        while data:
            cu.execute('INSERT INTO TB_Asset VALUES((?), (?), (?), (?))', (projectId, data[0], data[1], data[2]))
            data = sqlquery.fetchone()
        cx.commit()

        cmd_name = 'SELECT fs_id, asset_id, asset_sep FROM TB_AssetFileSer'
        sqlquery = cursor.execute(cmd_name)
        data = sqlquery.fetchone()
        while data:
            cu.execute('INSERT INTO TB_AssetFileSer VALUES((?), (?), (?), (?))', (projectId, data[0], data[1], data[2]))
            data = sqlquery.fetchone()
        cx.commit()

        cmd_name = 'SELECT afsa_id, fs_id, anim_id FROM TB_AssetFileSerInAnim'
        sqlquery = cursor.execute(cmd_name)
        data = sqlquery.fetchone()
        while data:
            cu.execute('INSERT INTO TB_AssetFileSerInAnim VALUES((?), (?), (?), (?))', (projectId, data[0], data[1], data[2]))
            data = sqlquery.fetchone()
        cx.commit()
        
        cursor.close()
        cnxn.close()

    cu.close()
    cx.close()

    #shutil.move('%s/idmtPlex.db' % temp, r'Z:\Resource\Support\Python\2.6-x64\Lib\site-packages\idmt\pipeline\idmtPlex.db')
    #shutil.move('%s/idmtPlex.db' % temp, r'E:\idmtPlex.db')
    #shutil.move('%s/idmtPlex.db' % temp, r'Z:\Resource\Support\Python\DB\idmtPlex.db')
    #myCmd('copy', '%s/idmtPlex.db' % temp, r'\\idmt-file09\support\Python\DB\idmtPlex.db')
    myCmd('move', '%s/idmtPlex.db' % temp, r'\\file-cluster\GDC\Resource\Library\OEM\ShunLiu\Python\2.7-x64\idmt\pipeline\idmtPlex.db')

if __name__ == "__main__":
    yun360()