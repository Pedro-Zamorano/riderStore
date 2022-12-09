import cx_Oracle

# Conexion a la BBDD
#connstr = "riderStore/RiderCore22@localhost:1521/XEPDB1" # Acceso BBDD PC escritorio
connstr = "riderStore/RiderCore22@192.168.56.1:1521/XEPDB1" # Acceso BBDD Notebook
conn = cx_Oracle.connect(connstr)
curs = conn.cursor()

rut= input("ingrese su rut: ")
nombre= input("ingrese su nombre: ")
apellido_paterno = input("Ingrese su apellido paterno: ")
apellido_materno = input("Ingrese su apellido materno: ")
email=input("ingrese su email: ")
telefono = input("Ingrese su numero de telefono: ")
direccion = input("Ingrese su direccion: ")
ciudad = input("Ciudad: ")


sql_idPersona = "SELECT id_persona from persona ORDER BY id_persona"
curs.execute(sql_idPersona)
idPersona = curs.fetchall()
for ids in idPersona:
    ids
last_idPers = ids[0]+1

print("Antes del INSERT\n")
sql_addPersona = "INSERT INTO persona(id_persona, nombre, apellido_paterno, apellido_materno, rut, direccion, ciudad, telefono, email) VALUES("\
    +str(last_idPers)+",'"+nombre+"','"+apellido_paterno+"','"+apellido_materno+"','"+rut+"','"+direccion+"','"+ciudad+"','"+telefono+"','"+email+"')"
curs.execute(sql_addPersona)
conn.commit()
print("PERSONA INSERTADA EN LA DB")