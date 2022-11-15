import cx_Oracle

# Conexion a la BBDD
# connstr = "riderStore/RiderCore22@localhost:1521/XEPDB1" # Acceso BBDD PC escritorio
connstr = "SYSTEM/Password.2022@192.168.56.1:1521/XEPDB1" # Acceso BBDD Notebook
conn = cx_Oracle.connect(connstr)
curs = conn.cursor()

busqueda = input("Ingrese el codigo del producto: ") #FTB

curs.execute("SELECT * FROM producto WHERE codigo_producto = '%s'"% busqueda)
#curs.execute("SELECT * FROM colaborador")

products = curs.fetchall()

for product in products:
    print(product)

curs.close()
conn.close()
