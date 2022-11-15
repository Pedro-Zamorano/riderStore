
class Persona:
    nombre = ''
    apellido_paterno = ''
    apellido_materno = ''
    rut = ''
    direccion = ''
    ciudad = ''
    telefono = 0
    email = ''

    def __init__(self, nombre, apellido_paterno, apellido_materno, rut, direccion, ciudad, telefono, email):
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.rut = rut
        self.direccion = direccion
        self.ciudad = ciudad
        self.telefono = telefono
        self.email = email
    
    def mostrarFechaNac(self):
        pass
    
    def mostrarSexo(self):
        pass
    
    def agregar(self):
        pass


class Cliente:
    nombre = ''
    apellido_paterno = ''
    telefono = 0
    email = ''
    
    def __init__(self, nombre, apellido_paterno, telefono, email):
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.telefono = telefono
        self.email = email 
    
    def muestraFechaRegistro(self):
        pass

    def muestraEstado(self):
        pass

    def agregarMetodoPago(self):
        pass         


class Empresa:
    razon_social = ''
    rut = ''
    giro = ''
    direccion = ''
    ciudad = ''
    telefono = 0
    email = ''
    metodo_pago = ''
    plazo = 0
    tipo_empresa = ''
    pagina_web = ''
    linkedin = ''

    def __init__(self, razon_social, rut, giro, direccion, ciudad, telefono, email, metodo_pago, plazo, tipo_empresa, pagina_web, linkedin):
        self.razon_social = razon_social
        self.rut = rut
        self.giro = giro
        self.direccion = direccion
        self.ciudad = ciudad
        self.telefono = telefono
        self.email = email
        self.metodo_pago = metodo_pago
        self.plazo = plazo
        self.tipo_empresa = tipo_empresa
        self.pagina_web = pagina_web
        self.linkedin = linkedin
    
    def mostrarPago(self):
        pass
    
    def mostrarPlazoDeEntrega(self):
        pass
    
    def agregarTipoEmpresa(self):
        pass


class Colaborador:
    nombre = ''
    apellido_paterno = ''
    rut = ''
    telefono = ''
    prevision = ''
    cargo = ''
    jefe_directo = ''
    tipo_contrato = ''
    
    def __init__(self, nombre, apellido_paterno, rut, telefono, prevision, cargo, jefe_directo, tipo_contrato):
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.rut = rut
        self.telefono = telefono
        self.prevision = prevision
        self.cargo = cargo
        self.jefe_directo = jefe_directo
        self.tipo_contrato = tipo_contrato

    def agregarNuevoColaborador(self):
        pass
    
    def muestraFechaRegistro(self):
        pass


class Producto:
    nombre = ''
    descripcion = ''
    familia_producto = ''
    stock = 0
    unidad_venta = ''
    posicion = ""
    codigo_producto = ''

    def __init__(self, nombre, descripcion, familia_producto, stock, unidad_venta, posicion, codigo_producto):
        self.nombre = nombre
        self.descripcion = descripcion
        self.familia_producto = familia_producto
        self.stock = stock
        self.unidad_venta = unidad_venta
        self.posicion = posicion
        self.codigo_producto = codigo_producto
    
    def buscarProducto(self):
        # Buscando producto en la tabla
        pass

