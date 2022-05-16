import sqlite3
from bbdd.agregar_usuarios_tabla_usuarios_bbdd import introducir_usuarios_bbdd
from bbdd.agregar_facturas_tabla_facturas_bbdd import introducir_facturas_bbdd
from bbdd.agregar_campo_tabla_usuarios_facturas_bbdd import introducir_campo_usuarios_facturas_bbdd
from bbdd.obtener_lista_facturas_usuario_bbdd import obtener
from modelo.usuario import Usuario

def registrar_usuario(usuario:Usuario):
    id_usuario = usuario.id_usuario
    nombre_usuario = usuario.nombre_usuario

    try:
        existe_usuario = introducir_usuarios_bbdd(id_usuario, nombre_usuario)
    except sqlite3.Error as error:
        print('SQLite error: %s' % (' '.join(error.args)))
        print("Exception class is: ", error.__class__)

        print(f"ERROR AL REGISTRAR USUARIO EN LA BASE DE DATOS.")
    else:
        if existe_usuario:
            print(f"ES POSIBLE QUE EL USUARIO {nombre_usuario} YA EXISTA EN LA BASE DE DATOS.")
        else:
            print(f"USUARIO '{nombre_usuario}' REGISTRADO CORRECTAMENTE.")

def guardar_factura(id_usuario, nombre_usuario, nombre_factura, contenido_factura):
    try:
        print("GUARDANDO FACTURA...")

        introducir_facturas_bbdd(nombre_factura, contenido_factura)
        introducir_campo_usuarios_facturas_bbdd(id_usuario, nombre_usuario, nombre_factura, contenido_factura)

    except sqlite3.Error as error:
        print('SQLite error: %s' % (' '.join(error.args)))
        print("Exception class is: ", error.__class__)

        print("ERROR AL ALMACENAR LA FACTURA EN LA BASE DE DATOS.")

    else:
        print("LA FACTURA HA SIDO ALMACENADA SATISFACTORIAMENTE.")

def mostrar_lista_facturas_usuario():
    pass

def mostrar_factura():
    pass