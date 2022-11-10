
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

class Factura:
    numero_factura = 0
    rut = ''
    nombre = ''

    def __init__(self, numero_factura, rut, nombre):
        self.numero_factura = numero_factura
        self.rut = rut
        self.nombre = nombre
    
    def muestraEstadoPago(self):
        pass
    
    def muestra(self):
        pass
    
    def agregarNuevaFactura(self):
        pass 
    
class Factura_compra(Factura):
    giro = ''
    direccion = ''

    def __init__(self, giro, direccion):
        self.giro = giro
        self.direccion = direccion
    
    def agregaDatosCliente(self):
        pass
    
    def agregaProductos(self):
        pass
    
    def agregaCantidad(self):
        pass
    
class Factura_venta(Factura):
    giro = ''
    direccion = ''

    def __init__(self, giro, direccion):
        self.giro = giro
        self.direccion = direccion
    
    def agregaDatosCliente(self):
        pass
    
    def descontarProductos(self):
        pass
    
    def agregaCantidad(self):
        pass   
    
class Detalle_factura_compra(Factura_compra):
    cantidad = 0
    precio = 0

    def __init__(self, cantidad, precio):
        self.cantidad = cantidad
        self.precio = precio

    def agregarProductoAFactura(self):
        pass
    
    def muestraNumeroFactura(self):
        pass

    def agregarProductoStock(self):
        pass

class Detalle_factura_venta(Factura_venta):
    cantidad = 0
    precio = 0   

    def __init__(self, cantidad, precio):
        self.cantidad = cantidad
        self.precio = precio
    
    def descontarProductoStock(self):
        pass
    
    def agregarProductoAFactura(self):
        pass
    
    def mostrarFechaFactura(self):
        pass

class Producto:
    nombre = ''
    descripcion = ''
    familia_producto = ''
    stock = 0
    unidad_venta = ''
    posicion = ''

    def __init__(self, nombre, descripcion, familia_producto, stock, unidad_venta, posicion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.familia_producto = familia_producto
        self.stock = stock
        self.unidad_venta = unidad_venta
        self.posicion = posicion
    
    def mostrarStockDisponible(self):
        pass
    
    def mostrarPrecioVenta(self):
        pass
    
    def actualizarPosicionBodega(self):
        pass  
    
class Guia_despacho:
    numero_guia = 0
    fecha_emision = ''
    cliente = ''
    direccion = ''

    def __init__(self, numero_guia, fecha_emision, cliente, direccion):
        self.numero_guia = numero_guia
        self.fecha_emision = fecha_emision
        self.cliente = cliente
        self.direccion = direccion
    
    def mostrarFechaDespacho(self):
        pass  
    
class Detalle_guia_despacho(Guia_despacho):
    cantidad = 0
    precio = 0    
    
    def __init__(self, cantidad, precio):
        self.cantidad = cantidad
        self.precio = precio
    
    def mostrarTotalProductosDespacho(self):
        pass
    
    def mostrarfechaEntrega(self):
        pass
