"""
            Archivo de ejecucion principal    
"""

from functions import *
from db_tables import *

# Creando tablas en base de datos
dbExecute()

# Ejecucion del programa
value = True
while value:
    try:
        usuario = input("Usuario: ")
        password = input("Contraseña: ")
        
        login(usuario, password)
        
    except ValueError:
        print("Valores ingresados no son correctos")
