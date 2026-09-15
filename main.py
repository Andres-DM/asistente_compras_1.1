from listas import CarritoCompras
from interfaz import InterfazUsuario
from controlador import ControladorCompras

# PATRÓN 5: BOOTSTRAPPER 

def main():
    # Inicialización del Modelo y la Vista
    carrito_model = CarritoCompras()
    vista_ui = InterfazUsuario()
    
    # Inicialización del Controlador con sus dependencias
    controlador = ControladorCompras(carrito_model, vista_ui)
    
    # Arrancar la aplicación
    controlador.ejecutar()

if __name__ == "__main__":
    main()