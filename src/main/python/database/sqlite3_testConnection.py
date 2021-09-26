"""
Based off sqlitetutorial.net example
https://www.sqlitetutorial.net/sqlite-python/creating-database/
"""
import sqlite3
from sqlite3 import Error

def create_connection(db_file):#edit for no file if doing memory database
    """
    Create a database connection to a database that resides in the memory
    """
    conn = None
    try:
        #create in memory
        #conn = sqlite3.connect(':memory:')
        conn
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
    return conn

def create_table(conn, create_table_sql):
    """
    Create a table from the create_table_sql statement
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

if __name__ == '__main__':
    #for memory database
    #create_connection()
    test_database = "D:\\Programming\\test.db"
    create_connection(test_database)

    sql_table = """ CREATE TABLE IF NOT EXISTS
    
                """

