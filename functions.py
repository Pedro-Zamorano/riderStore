from riderStoreCore import *

# Menu principal
def menu():
    value = True
    while value:   
        try:
            print("""
                *** Bienvenido al Menú ***\n
                1.- Registrar usuario
                2.- Iniciar venta
                3.- Mostrar todas las ventas
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
    # Registrar usuario
    if opc == 1:
        print("opcion 1")
    
    # Iniciar venta
    elif opc == 2: 
        main = Producto()
        main.mostrarProducto()
    
    # Mostrar todas las ventas
    elif opc == 3:
        print("opcion 3")
    
    # Salir
    elif opc == 4:
        print("Cerrando programa")
        exit()