
import cx_Oracle

def creandoTablas():

    # Conexion a base de datos
    connstr = "system/Hola.2022@localhost:1521/XEPDB1"
    conn = cx_Oracle.connect(connstr)
    curs = conn.cursor()

    # TABLA PERSONA
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

    # TABLA CLIENTE
    cliente = '''CREATE TABLE cliente(
        id INT PRIMARY KEY,
        nombre CHAR(20) NOT NULL,
        apellido_paterno CHAR(20),
        telefono INT,
        email CHAR(30)
    )'''
    
    # Cargando la creacion de las tablas en la base de datos
    curs.execute(persona)
    curs.execute(cliente)
    
    # Cerrando la conexion a la base de datos
    curs.close()
    conn.close()
    
    # Mensaje de confirmación
    print("Tablas creadas")

# No dentro de la prueba
    """ # TABLA EMPRESA
    empresa = '''CREATE TABLE empresa(
        id INT PRIMARY KEY,
        razon_social CHAR(255),
        rut CHAR(255) NOT NULL,
        giro CHAR(255),
        direccion CHAR(255),
        ciudad CHAR(255),
        telefono INT,
        email CHAR(255),
        metodo_pago = CHAR(255),
        plazo INT,
        tipo_empresa CHAR(255),
        pagina_web CHAR(255),
        linkedin CHAR(255),
    )'''

    # TABLA COLABORADOR
    colaborador = '''CREATE TABLE colaborador(
        id INT PRIMARY KEY,
        nombre CHAR(255) NOT NULL,
        apellido_paterno CHAR(255),
        rut CHAR(255),
        telefono CHAR(255),
        prevision CHAR(255),
        cargo CHAR(255),
        jefe_directo CHAR(255),
        tipo_contrato CHAR(255),
    )'''
    # TABLA FACTURA (EL NUMERO DE FACTURA DEBE AUTO-ASIGNARSE)
    factura = '''CREATE TABLE factura(
        id INT PRIMARY KEY,
        numero_factura INT NOT NULL AUTO_INCREMENT,
        rut CHAR(255),
        nombre CHAR(255),
    )'''

    # TABLA FACTURA_COMPRA
    f_compra = '''CREATE TABLE factura_compra(
        id INT PRIMARY KEY,
        giro CHAR(255),
        direccion CHAR(255),
    )'''

    # TABLA FACTURA_VENTA
    f_venta = '''CREATE TABLE factura_venta(
        id INT PRIMARY KEY,
        giro CHAR(255),
        direccion CHAR(255),
    )'''

    # TABLA DETALLE_FACTURA_COMPRA
    det_fact_compra = '''CREATE TABLE detalle_factura_compra(
        id INT PRIMARY KEY,
        cantidad INT,
        precio INT,
    )'''

    # TABLA DETALLE_FACTURA_VENTA
    det_fact_venta = '''CREATE TABLE detalle_factura_venta(
        id INT PRIMARY KEY,
        cantidad INT,
        precio INT,
    )'''

    # TABLA PRODUCTO
    producto = '''CREATE TABLE producto(
        id INT PRIMARY KEY,
        nombre CHAR(255),
        descripcion CHAR(255),
        familia_producto CHAR(255),
        stock INT,
        unidad_venta CHAR(255),
        posicion CHAR(255),
    )'''

    # TABLA GUIA_DESPACHO
    g_despacho = '''CREATE TABLE guia_despacho(
        id INT PRIMARY KEY,
        numero_guia INT NOT NULL AUTO_INCREMENT
        fecha_emision DATE,
        cliente CHAR(255),
        direccion CHAR(255),
    )'''

    # TABLA DETALLE_GUIA_DESPACHO
    det_guia_despacho = '''CREATE TABLE detalle_guia_despacho(
        id INT PRIMARY KEY,
        cantidad INT,
        precio INT,
    )'''

    # TABLA VENTAS
    venta = '''CREATE TABLE venta(
        id id INT PRIMARY KEY,
    )''' """

