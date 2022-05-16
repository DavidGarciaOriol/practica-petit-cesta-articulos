import sqlite3

def introducir_campo_usuarios_facturas_bbdd(id_usuario, nombre_usuario, nombre_factura, contenido_factura):

    conexion_facturas_bbdd = sqlite3.connect('facturas_bbdd')

    cursor_bbdd = conexion_facturas_bbdd.cursor()

    cursor_bbdd.execute('INSERT INTO USUARIOS_FACTURAS VALUES (?,?,?,?)', (id_usuario, nombre_usuario, nombre_factura, contenido_factura))

    conexion_facturas_bbdd.commit()

    conexion_facturas_bbdd.close()


# # # TEST PURPOSE # # #

contenido_factura_test = '''
    - - - Tu Cesta - - - 

patatas: 16.34 €     
espaguetis: 18.15 €  
macarrones: 9.68 €   
lejía: 13.07 €       
Papel Higiénico: 9.68 €
Papel de Cocina: 5.81 €

TOTAL: 72.73 €
IVA y Descuentos ya aplicados.
'''

# introducir_campo_usuarios_facturas_bbdd(22224444, "Paco", "Factura X", contenido_factura_test)