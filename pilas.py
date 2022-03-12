from xmlrpc.client import boolean


class Pila():
    lista = []
    tope = 0
    size = int

    def __init__(self, size) -> None:
        self.size = size
    
    def empty(self) -> boolean:
        if self.tope == 0:
            return True
        else:
            return False

    def push(self, dato) -> None:
        if self.tope < self.size:
            self.lista.append(dato)
            self.tope += 1
        else:
            print("La pila esta llena!")

    def pop(self) -> int:
        dato = self.lista[self.tope]
        self.lista.pop()
        self.tope -= 1
        return dato

    def last(self) -> int:
        return self.lista[self.tope]