from typing import Optional, Iterator

class NodoSimple:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente: Optional['NodoSimple'] = None

class ListaSimple:
    def __init__(self):
        self.cabeza: Optional[NodoSimple] = None
        self.cola: Optional[NodoSimple] = None

    def esta_vacia(self) -> bool:
        return self.cabeza is None

    def agregar(self, dato):
        nuevo_nodo = NodoSimple(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            if self.cola is not None:
                self.cola.siguiente = nuevo_nodo
                self.cola = nuevo_nodo

    def mostrar(self) -> Iterator:
        actual = self.cabeza
        while actual is not None:
            yield actual.dato
            actual = actual.siguiente

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente: Optional['Nodo'] = None
        self.anterior: Optional['Nodo'] = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza: Optional[Nodo] = None
        self.cola: Optional[Nodo] = None

    def esta_vacia(self) -> bool:
        return self.cabeza is None

    def agregar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None or self.cola is None:
            self.cabeza = self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.cola
            self.cola = nuevo_nodo

    def agregar_al_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None or self.cola is None:
            self.cabeza = self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo

    def eliminar(self, dato) -> bool:
        actual = self.cabeza
        while actual is not None:
            if actual.dato == dato:
                if actual.anterior is not None:
                    actual.anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente

                if actual.siguiente is not None:
                    actual.siguiente.anterior = actual.anterior
                else:
                    self.cola = actual.anterior
                return True
            actual = actual.siguiente
        return False

    def mostrar(self) -> Iterator:
        actual = self.cabeza
        while actual is not None:
            yield actual.dato
            actual = actual.siguiente

class CarritoCompras(ListaDoblementeEnlazada):
    def __init__(self):
        super().__init__()

    def agregar(self, dato):
        self.agregar_al_final(dato)

    def obtener_items(self) -> list:
        return list(self.mostrar())