import sqlite3
import uuid

def introducir_usuarios_bbdd(id_usuario, nombre_usuario):

    conexion_facturas_bbdd = sqlite3.connect('facturas_bbdd')

    cursor_bbdd = conexion_facturas_bbdd.cursor()

    cursor_bbdd.execute('INSERT INTO USUARIOS VALUES (?, ?)', (id_usuario, nombre_usuario))

    conexion_facturas_bbdd.commit()

    conexion_facturas_bbdd.close()


# # # TEST PURPOSE # # #

random_uuid = uuid.uuid4()

# introducir_usuarios_bbdd(random_uuid,"Paco")