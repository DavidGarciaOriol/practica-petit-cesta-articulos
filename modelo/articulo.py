import string

class Articulo:

    nombre:string = ""
    precio:bool = 0
    cantidad:int = 1

    def __init__(self, nombre:string, precio:bool, cantidad:int):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    
    def aplicar_descuento(self, descuento):
        self.precio -= (self.precio*descuento/100)

    def aplicar_IVA(self):
        self.precio += (self.precio*21/100)

    def aplicar_multiplicador_cantidad(self):
        self.precio*=self.cantidad

