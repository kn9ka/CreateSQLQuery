#!/usr/bin/env python
''' dat code need for create table for test
    for db_file in db_test_objects:
        print(db_file)
        odbc_conn_str = "DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=%s; UID=%s; PWD=%s" % (db_file, user, password)
        conn = pyodbc.connect(odbc_conn_str)
        odbc_cursor = conn.cursor()

        NewQuery = "CREATE TABLE TestTable (symbol varchar(15), leverage double, shares integer, price double)"
        odbc_cursor.execute(NewQuery)
        conn.commit()
        conn.close()
'''

import pyodbc

odbc_driver = r"{Microsoft Access Driver (*.mdb, *.accdb)}"
db_test1 = r'''D:\Users\40196482\Desktop\Query Testing\Test #1.accdb'''
db_test2 = r'''D:\Users\40196482\Desktop\Query Testing\Test #2.accdb'''
db_test3 = r'''D:\Users\40196482\Desktop\Query Testing\Test #3.accdb'''
db_test4 = r'''D:\Users\40196482\Desktop\Query Testing\Test #4.accdb'''

db_test_objects = [db_test1, db_test2, db_test3, db_test4]

user = 'PYTHON_SCRIPT'
password = ''


def createQuery(db_file, user, password):

    odbc_conn_str = "Driver=%s;DBQ=%s;UID=%s;PWD=%s" % (odbc_driver, db_file, user, password)
    print(odbc_conn_str)

    conn = pyodbc.connect(odbc_conn_str)
    odbc_cursor = conn.cursor()

    sql = """\
    CREATE VIEW TestQuery AS
    SELECT * FROM TestTable
    """
    odbc_cursor.execute(sql)
    conn.commit()
    conn.close()


def deleteQuery(db_file, user=None, password=None):

    odbc_conn_str = "Driver=%s;DBQ=%s;UID=%s;PWD=%s" % (odbc_driver, db_file, user, password)
    print(odbc_conn_str)

    conn = pyodbc.connect(odbc_conn_str)
    odbc_cursor = conn.cursor()

    sql = """\
    DROP TABLE TestQuery
    """
    odbc_cursor.execute(sql)
    conn.commit()
    conn.close()


def showData(db_file, user=None, password=None):
    odbc_conn_str = "Driver=%s;DBQ=%s;UID=%s;PWD=%s" % (odbc_driver, db_file, user, password)
    print(odbc_conn_str)
    conn = pyodbc.connect(odbc_conn_str)
    odbc_cursor = conn.cursor()

    sql = """\
    SELECT * FROM TestTable
    """
    odbc_cursor.execute(sql)
    row = odbc_cursor.fetchone()
    
    conn.commit()
    conn.close()
    
    return row


if __name__ == '__main__':
    #createQuery(db_test4, user, password)
    deleteQuery(db_test4, user, password)
    #print (showData(db_test1))