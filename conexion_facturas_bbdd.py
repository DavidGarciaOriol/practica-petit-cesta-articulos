import sqlite3

def generar_Tabla_usuarios_bbdd():

    conexion_facturas_bbdd = sqlite3.connect('facturas_bbdd')

    cursor = conexion_facturas_bbdd.cursor()

    cursor.execute('''
        CREATE TABLE USUARIOS(
            ID_USUARIO INTEGER PRIMARY KEY,
            NOMBRE_USUARIO VARCHAR(128)
        )
    ''')

    