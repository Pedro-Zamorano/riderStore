
import cx_Oracle

# Validando si la tabla existe en la base de datos
def validadorTablas(tablename):
    connstr = "riderStore/RiderCore22@localhost:1521/XEPDB1"
    conn = cx_Oracle.connect(connstr)
    curs = conn.cursor()
    
    try:
        curs.execute("SELECT * FROM {}".format(tablename))
        return True
    except cx_Oracle.DatabaseError as e:
        x = e.args[0]
        if x.code == 942: ## Only catch ORA-00942: table or view does not exist error
            return False
        else:
            raise e
    finally:
        curs.close()

# Comprobando creacion de tablas: 
# Si existen, no se crean
# Si NO existen, se crean

# Conexion a base de datos
connstr = "riderStore/RiderCore22@localhost:1521/XEPDB1"
conn = cx_Oracle.connect(connstr)
curs = conn.cursor()

# TABLA PERSONA
def tablaPersona():
    if validadorTablas('persona'):
        print("Tabla 'PERSONA' existe en el sistema.")
    else:
        persona = '''CREATE TABLE persona(
            id INT PRIMARY KEY,
            nombre CHAR(20) NOT NULL,
            apellido_paterno CHAR(20),
            apellido_materno CHAR(20),
            rut CHAR(15) NOT NULL,
            direccion CHAR(50),
            ciudad CHAR(20),
            telefono INT,
            email CHAR(30)
        )'''
        curs.execute(persona)
        curs.close()
        conn.close()
        print("Se ha creado la tabla 'PERSONA'.")

# TABLA CLIENTE
def tablaCliente():
    if validadorTablas('cliente'):
        print("Tabla 'CLIENTE' existe en el sistema.")
    else:
        cliente = '''CREATE TABLE cliente(
            id INT PRIMARY KEY,
            nombre CHAR(20) NOT NULL,
            apellido_paterno CHAR(20),
            telefono INT,
            email CHAR(30)
        )'''
        curs.execute(cliente)
        print("Se ha creado la tabla 'CLIENTE'.")

# TABLA EMPRESA
def tablaEmpresa():
    if validadorTablas('empresa'):
        print("Tabla 'EMPRESA' existe en el sistema.")
    else:
        empresa = '''CREATE TABLE empresa(
            id INT PRIMARY KEY,
            razon_social CHAR(25),
            rut CHAR(15) NOT NULL,
            giro CHAR(30),
            direccion CHAR(50),
            ciudad CHAR(20),
            telefono INT,
            email CHAR(30),
            plazo INT,
            tipo_empresa CHAR(30),
            pagina_web CHAR(30),
            linkedin CHAR(50)
        )'''
        curs.execute(empresa)
        print("Se ha creado la tabla 'EMPRESA'.")

# TABLA COLABORADOR
def tablaColaborador():
    if validadorTablas('colaborador'):
        print("Tabla 'COLABORADOR' existe en el sistema.")
    else:
        colaborador = '''CREATE TABLE colaborador(
            id INT PRIMARY KEY,
            nombre CHAR(20) NOT NULL,
            apellido_paterno CHAR(20),
            rut CHAR(15),
            telefono INT,
            prevision CHAR(10),
            cargo CHAR(30),
            jefe_directo CHAR(20),
            tipo_contrato CHAR(15)
        )'''
        curs.execute(colaborador)
        print("Se ha creado la tabla 'COLABORADOR'.")

# TABLA FACTURA
def tablaFactura():
    if validadorTablas('factura'):
        print("Tabla 'FACTURA' existe en el sistema.")
    else:
        factura = '''CREATE TABLE factura(
            id INT PRIMARY KEY,
            numero_factura INT NOT NULL,
            rut CHAR(15),
            nombre CHAR(20)
        )'''
        curs.execute(factura)
        print("Se ha creado la tabla 'FACTURA'.")

# TABLA FACTURA_COMPRA
def tablaFCompra():
    if validadorTablas('factura_compra'):
        print("Tabla 'FACTURA_COMPRA' existe en el sistema.")
    else:
        f_compra = '''CREATE TABLE factura_compra(
            id INT PRIMARY KEY,
            giro CHAR(30),
            direccion CHAR(50)
        )'''
        curs.execute(f_compra)
        print("Se ha creado la tabla 'FACTURA_COMPRA'.")

# TABLA FACTURA_VENTA
def tablaFVenta():
    if validadorTablas('factura_venta'):
        print("Tabla 'FACTURA_VENTA' existe en el sistema.")
    else:
        f_venta = '''CREATE TABLE factura_venta(
        id INT PRIMARY KEY,
        giro CHAR(30),
        direccion CHAR(50)
        )'''
        curs.execute(f_venta)
        print("Se ha creado la tabla 'FACTURA_VENTA'.")

# TABLA DETALLE_FACTURA_COMPRA
def tablaDFCompra():
    if validadorTablas('detalle_factura_compra'):
        print("Tabla 'DETALLE_FACTURA_COMPRA' existe en el sistema.")
    else:
        det_fact_compra = '''CREATE TABLE detalle_factura_compra(
            id INT PRIMARY KEY,
            cantidad INT,
            precio INT
        )'''
        curs.execute(det_fact_compra)
        print("Se ha creado la tabla 'DETALLE_FACTURA_COMPRA'.")

# TABLA DETALLE_FACTURA_VENTA
def tablaDFVenta():
    if validadorTablas('detalle_factura_venta'):
        print("Tabla 'DETALLE_FACTURA_VENTA' existe en el sistema.")
    else:
        det_fact_venta = '''CREATE TABLE detalle_factura_venta(
            id INT PRIMARY KEY,
            cantidad INT,
            precio INT
        )'''
        curs.execute(det_fact_venta)
        print("Se ha creado la tabla 'DETALLE_FACTURA_VENTA'.")

# TABLA PRODUCTO
def tablaProducto():
    if validadorTablas('producto'):
        print("Tabla 'PRODUCTO' existe en el sistema.")
    else:
        producto = '''CREATE TABLE producto(
            id INT PRIMARY KEY,
            nombre CHAR(20),
            descripcion CHAR(100),
            familia_producto CHAR(20),
            stock INT,
            unidad_venta CHAR(10),
            posicion CHAR(20)
        )'''
        curs.execute(producto)
        print("Se ha creado la tabla 'PRODUCTO'.")

# TABLA GUIA_DESPACHO
def tablaGDespacho():
    if validadorTablas('guia_despacho'):
        print("Tabla 'GUIA_DESPACHO' existe en el sistema.")
    else:
        g_despacho = '''CREATE TABLE guia_despacho(
            id INT PRIMARY KEY,
            numero_guia INT NOT NULL,
            fecha_emision DATE,
            cliente CHAR(20),
            direccion CHAR(50)
        )'''
        curs.execute(g_despacho)
        print("Se ha creado la tabla 'GUIA_DESPACHO'.")

# TABLA DETALLE_GUIA_DESPACHO
def tablaDGDespacho():
    if validadorTablas('detalle_guia_despacho'):
        print("Tabla 'DETALLE_GUIA_DESPACHO' existe en el sistema.")
    else:
        det_guia_despacho = '''CREATE TABLE detalle_guia_despacho(
            id INT PRIMARY KEY,
            cantidad INT,
            precio INT
        )'''
        curs.execute(det_guia_despacho)
        print("Se ha creado la tabla 'DETALLE_GUIA_DESPACHO'.")

def dbExecute():
    tablaPersona()
    tablaCliente()
    tablaEmpresa()
    tablaColaborador()
    tablaFactura()
    tablaFCompra()
    tablaFVenta()
    tablaDFCompra()
    tablaDFVenta()
    tablaProducto()
    tablaGDespacho()
    tablaDGDespacho()
