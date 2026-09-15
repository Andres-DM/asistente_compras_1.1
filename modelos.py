from listas import ListaSimple

class Producto:
    def __init__(self, nombre: str, precio: float):
        self.nombre = nombre
        self.precio = precio

    def __repr__(self):
        return f"{self.nombre} - ${self.precio:.2f}"

class Almacen:
    def __init__(self, id_almacen: int, nombre: str):
        self.id_almacen = id_almacen
        self.nombre = nombre
        self.inventario = ListaSimple()

class GestorAlmacenes:
    def __init__(self):
        self.almacenes = []

    def agregar_almacen(self, almacen: Almacen):
        self.almacenes.append(almacen)

    def obtener_almacenes(self):
        return self.almacenes