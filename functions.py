from riderStoreCore import *

# Funciones para el vendedor
def login(user, password):
    if user == "v" and password == "1": # Validar con usuarios en base de datos
        print("\nLogin satisfactorio\n")        
        # Llamado a función MENU
        menu()

    elif user != "v":
        print("Usuario no valido\n")
        return True

    elif password != "1":
        print("Contraseña no valida\n")
        return True


def menu(): 
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
