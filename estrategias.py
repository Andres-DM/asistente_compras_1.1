from abc import ABC, abstractmethod
from listas import ListaSimple
from modelos import Producto

class EstrategiaBusqueda(ABC):
    @abstractmethod
    def buscar(self, lista_compras, gestor_almacenes):
        pass

class BusquedaMejorPrecioStrategy(EstrategiaBusqueda):
    def buscar(self, lista_compras, gestor_almacenes):
        resultados = {alm: ListaSimple() for alm in gestor_almacenes.obtener_almacenes()}

        for prod_nombre in lista_compras.mostrar():
            p_lower = prod_nombre.lower()
            mejor_almacen = None
            mejor_precio = float('inf')

            for alm in gestor_almacenes.obtener_almacenes():
                for p in alm.inventario.mostrar():
                    if p.nombre.lower() == p_lower and p.precio < mejor_precio:
                        mejor_precio = p.precio
                        mejor_almacen = alm

            if mejor_almacen is not None and mejor_precio != float('inf'):
                resultados[mejor_almacen].agregar(Producto(prod_nombre, mejor_precio))

        return resultados