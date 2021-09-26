
import pyodbc
import time 

server = 'stardestroyer\sqlexpress'
database = 'TEST'
"""
username = 'user'
password = 'password'
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost:1433;DATABASE=Test')
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
"""
conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database)
cursor = conn.cursor()

#Sample select query
cursor.execute("SELECT @@version;")
row = cursor.fetchone()
while row:
    print(row[0])
    row = cursor.fetchone()
cursor.close()


how_many = conn.getinfo(pyodbc.SQL_MAX_CONCURRENT_ACTIVITIES)
print("Max concurrent activities", how_many)

scriptPath = 'D:\Programming\TACM\src\main\python\database\sql3.sql'

def runSQL(c, scriptPath):
    sqlQuery = ''
    with open(scriptPath, 'r') as inp:
        for line in inp:
            if line == 'GO\n':
                print(sqlQuery)
                c.execute(sqlQuery)
                sqlQuery = ''
            elif 'PRINT' in line:
                disp = line.split("'")[1]
                print(disp, '\r')
            else:
                sqlQuery = sqlQuery + line
    inp.close()
    print('done')
cursor3 = conn.cursor()
runSQL(cursor3, scriptPath)
cursor3.execute('COMMIT;')

cursor3.close()
cursor2 = conn.cursor()
cursor2.execute('SELECT * FROM TEST.dbo.testTable')
for row in cursor2:
    print(row)
cursor2.close()

conn.close()