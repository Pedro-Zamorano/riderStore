import cx_Oracle

# Conexion a la BBDD
connstr = "riderStore/RiderCore22@localhost:1521/XEPDB1"
conn = cx_Oracle.connect(connstr)
curs = conn.cursor()

busqueda = input("Ingrese el codigo del producto: ") #FE200

curs.execute("SELECT * FROM producto WHERE codigo_producto = '%s'"% busqueda)

products = curs.fetchall()

for product in products:
    print(product)

curs.close()
conn.close()
