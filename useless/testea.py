import cx_Oracle
# Conexion a la BBDD
#connstr = "riderStore/RiderCore22@localhost:1521/XEPDB1" # Acceso BBDD PC escritorio
connstr = "riderStore/RiderCore22@192.168.56.1:1521/XEPDB1" # Acceso BBDD Notebook
conn = cx_Oracle.connect(connstr)
curs = conn.cursor()

# Itera el ID de VENTA
sql_id = "SELECT id_venta FROM venta"
curs.execute(sql_id)
ids = curs.fetchall()
for id in ids:
    id
last_id_venta = id[0]

# Itera ventas para extraer valores de la tabla VENTA
sql_venta = "SELECT precio_total, iva, metodo_pago, id_producto FROM venta WHERE id_venta="+str(last_id_venta)
curs.execute(sql_venta)
datosVenta = curs.fetchall()
for datos in datosVenta:
    print(datos)
precioTotal = datos[0]
iva = datos[1]
metodoPago = datos[2]
idProducto = datos[3]


curs.close()
conn.close()
