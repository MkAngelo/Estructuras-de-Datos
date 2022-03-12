from hashlib import new
from pilas import Pila

if __name__ == "__main__":
    pilita = Pila(5)
    pilita.insertar(5)
    pilita.insertar(6)
    pilita.cima()
    pilita.eliminar()
    pilita.esta_vacia()
