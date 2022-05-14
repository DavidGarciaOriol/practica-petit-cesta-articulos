import string
from articulo import Articulo

class Cesta:

    lista_articulos = []
    lista_descuentos = []

    precio_cesta_total = 0

    factura_final = {}

    def __init__(self, lista_articulos:list[Articulo]=[Articulo("Vacío", 0, 1)], lista_descuentos:list[float]=[0]):

        self.lista_articulos = lista_articulos
        self.lista_descuentos = lista_descuentos

        ## Si pasas un artículo en vez de una lista de artículos, este segmento se encarga de transformarlo a una lista con un artículo.
        if type(self.lista_articulos) == Articulo:
            lista_temp = []
            lista_temp.append(lista_articulos)
            self.lista_articulos = lista_temp

        ## Si la lista de artículos es mayor a la lista de posibles descuentos, este segmento iguala los valores añadiendo descuentos a cero para evitar errores.
        if len(self.lista_articulos) > len(self.lista_descuentos):
            for i in range(len(self.lista_articulos)-len(self.lista_descuentos)):
                self.lista_descuentos.append(0)

    def agregar_a_lista_articulos(self, nombre:string, precio:bool, cantidad:int, descuento=0):
        articulo = Articulo(nombre, precio, cantidad)
        self.lista_articulos.append(articulo)
        self.lista_descuentos.append(descuento)

    def aplicar_tarifas_a_precios_factura(self):

        precios_finales = []
        index = 0
        for articulo in self.lista_articulos:
            articulo.aplicar_IVA()
            articulo.aplicar_descuento(self.lista_descuentos[index])
            articulo.aplicar_multiplicador_cantidad()
            precio_final = articulo.precio
            precios_finales.append(round(precio_final, 2))
            index=index+1

        return precios_finales

    def calcular_total(self):
        total = 0
        for item in self.factura_final.keys():
            total+=self.factura_final[item]
        return round(total, 2)

    def generar_factura_final(self):
        precios_finales = self.aplicar_tarifas_a_precios_factura()

        index = 0
        for articulo in self.lista_articulos:
            self.factura_final[articulo.nombre] = precios_finales[index]
            index = index+1

    def __str__(self):
        str = ""
        str+="- - - Tu Cesta - - - \n\n"

        for item in self.factura_final.keys():
            str+=f"{item}: {self.factura_final[item]} €\n"

        str+=f"\nTOTAL: {self.calcular_total()} €"
        str+="\nIVA y Descuentos ya aplicados."    
        return str