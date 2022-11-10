
#import cx_Oracle
import db_tables

try:
    db_tables.creandoTablas()
    
    if db_tables.creandoTablas() == True:
        print("Entramos al if")
    else:
        print("Entramos al else")

except ValueError:
    print("Tablas creadas previamente")


"""
import cx_Oracle

connstr = "system/Hola.2022@localhost:1521"
conn = cx_Oracle.connect(connstr)
curs = conn.cursor()

curs.arraysize=50
curs.execute("SELECT * FROM help")

print('Campo 1')

for column_1 in curs.fetchall():
    print(column_1)

curs.close()
conn.close()
"""