from modelo.articulo import Articulo
from modelo.cesta import Cesta
from controlador.controlador import *

articulo_1 = Articulo("patatas", precio=3, cantidad=5)
articulo_2 = Articulo("espaguetis", precio=2, cantidad=10)
articulo_3 = Articulo("macarrones", precio=2.5, cantidad=4)
articulo_4 = Articulo("lejía", precio=6, cantidad=2)

lista_articulos = [articulo_1, articulo_2, articulo_3, articulo_4]

lista_descuentos = [10, 25, 20, 10]

cesta_1 = Cesta(lista_articulos, lista_descuentos)

cesta_1.generar_factura_final()

print(cesta_1)

