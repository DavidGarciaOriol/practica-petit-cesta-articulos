import sqlite3

def generar_tabla_usuarios_bbdd():

    conexion_facturas_bbdd = sqlite3.connect('facturas_bbdd')

    cursor = conexion_facturas_bbdd.cursor()

    cursor.execute('''
        CREATE TABLE USUARIOS(
            ID_USUARIO INTEGER PRIMARY KEY,
            NOMBRE_USUARIO VARCHAR(128)
        )
    ''')

    conexion_facturas_bbdd.close()

def generar_tabla_facturas_bbdd():

    conexion_facturas_bbdd = sqlite3.connect('facturas_bbdd')

    cursor = conexion_facturas_bbdd.cursor()

    cursor.execute('''
        CREATE TABLE FACTURAS(
            ID_FACTURA INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE_FACTURA VARCHAR(128),
            CONTENIDO_FACTURA VARCHAR
        )
    ''')

    conexion_facturas_bbdd.close()

def generar_tabla_usuarios_facturas_bbdd():

    conexion_facturas_bbdd = sqlite3.connect('facturas_bbdd')

    cursor = conexion_facturas_bbdd.cursor()

    cursor.execute('''
        CREATE TABLE USUARIOS_FACTURAS(
        ID_USUARIO INTEGER,
        NOMBRE_USUARIO VARCHAR(128),
        NOMBRE_FACTURA VARCHAR(128),
        CONTENIDO_FACTURA VARCHAR,
        FOREIGN KEY(ID_USUARIO) REFERENCES USUARIOS(ID_USUARIO),
        FOREIGN KEY(NOMBRE_USUARIO) REFERENCES USUARIOS(NOMBRE_USUARIO),
        FOREIGN KEY(NOMBRE_FACTURA) REFERENCES FACTURAS(NOMBRE_FACTURA),
        FOREIGN KEY(CONTENIDO_FACTURA) REFERENCES FACTURAS(CONTENIDO_FACTURA)
        )
    ''')

    conexion_facturas_bbdd.close()


# # # GENERAR TABLAS # # #

#generar_tabla_usuarios_bbdd()
#generar_tabla_facturas_bbdd()
#generar_tabla_usuarios_facturas_bbdd()