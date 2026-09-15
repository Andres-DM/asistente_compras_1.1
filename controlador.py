from listas import CarritoCompras
from modelos import Almacen, GestorAlmacenes, Producto
from estrategias import BusquedaMejorPrecioStrategy

class ControladorCompras:
    def __init__(self, carrito_model: CarritoCompras, vista_ui):
        self.lista_compras = carrito_model
        self.vista = vista_ui
        self.gestor_almacenes = GestorAlmacenes()
        self.estrategia_busqueda = BusquedaMejorPrecioStrategy()

        for i in range(1, 4):
            self.gestor_almacenes.agregar_almacen(Almacen(id_almacen=i, nombre=f"Almacen {i}"))

    def agregar_producto_usuario(self, nombre: str):
        if nombre.strip():
            self.lista_compras.agregar_al_final(nombre.strip())

    def eliminar_producto_usuario(self, nombre: str) -> bool:
        return self.lista_compras.eliminar(nombre.strip())

    def obtener_compras_usuario(self):
        return list(self.lista_compras.mostrar())

    def agregar_producto_almacen(self, id_almacen: int, nombre: str, precio: float):
        prod = Producto(nombre, precio)
        for alm in self.gestor_almacenes.obtener_almacenes():
            if alm.id_almacen == id_almacen:
                alm.inventario.agregar(prod)
                break

    def ejecutar_busqueda_precios(self):
        return self.estrategia_busqueda.buscar(self.lista_compras, self.gestor_almacenes)

    def ejecutar(self):
        self.vista.set_controlador(self)
        self.vista.ejecutar()