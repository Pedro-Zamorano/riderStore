from functions import * 

value = True
while value:
    try:
        usuario = input("Usuario: ")
        password = input("Contraseña: ")
        
        login(usuario, password)
        
    except ValueError:
        print("Valores ingresados no son correctos")
