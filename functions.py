from riderStoreCore import *
import cx_Oracle

# Conexion a la BBDD
# connstr = "riderStore/RiderCore22@localhost:1521/XEPDB1" # Acceso BBDD PC escritorio
connstr = "SYSTEM/Password.2022@192.168.56.1:1521/XEPDB1" # Acceso BBDD Notebook
conn = cx_Oracle.connect(connstr)
curs = conn.cursor()

# Funciones para el login
def login(user, password):
    
    # Consulta a la BBDD sobre usuario y contraseña
    curs.execute("SELECT TRIM(nombre), TRIM(contrasena), privilegio FROM colaborador")
    access = curs.fetchall()
    
    for userPass in access:
        #print(userPass)
        if userPass[0] == str(user) and userPass[1] == str(password) and userPass[2] == 1:
            print("Login Correcto!!")
            menuVendedor()
        elif userPass[0] == str(user) and userPass[1] == str(password) and userPass[2] == 2:
            print("Login Correcto!!")
            menuAdmin()
        
    else:
        print("Login Fallido!!!,\n Intente nuevamente\n")

# Menu principal VENDEDOR
def menuVendedor():
    value = True
    while value:   
        try:
            print("""
                *** Bienvenido al Menú ***\n
                1.- Iniciar venta
                2.- Realizar cotización
                3.- Consultar producto
                4.- Salir
                \n""")
            
            option = int(input("Ingrese su opción: "))
            
            if option < 1 or option > 4:
                print("\nLa opción ingresada esta fuera de rango!. \nIntente nuevamente...\n")
                value = True
            else:
                opcMenu(option)
        
        except ValueError:
            print("El dato ingresado no es un numero! \nIngrese nuevamente...\n")
            value = True


def opcMenu(opc):
    # Inicio Venta
    if opc == 1:
        print("opcion 1")
        #inicioVenta()
    
    # Realizar Cotización
    elif opc == 2:
        print("opcion 2")
        #pass
        
    # Consultar Producto
    elif opc == 3:
        print("opcion 3")
        #pass
        
    # Salir
    elif opc == 4:
        print("opcion 4... SALIENDO")
        exit()


# Menu principal ADMINISTRADOR
def menuAdmin():
    value = True
    while value:   
        try:
            print("""
                *** Bienvenido al Menú de ADMINISTRADOR ***\n
                1.- Reporte de ventas
                2.- Consultar productos
                3.- Registrar productos
                4.- Registrar nuevo usuario
                5.- Salir
                \n""")
            
            option = int(input("Ingrese su opción: "))
            
            if option < 1 or option > 5:
                print("\nLa opción ingresada esta fuera de rango!. \nIntente nuevamente...\n")
                value = True
            else:
                print(f"Selecciono la opcion {option}")
        
        except ValueError:
            print("El dato ingresado no es un numero! \nIngrese nuevamente...\n")
            value = True