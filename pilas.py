class Pila():
    lista = []
    tope = 0
    size = int

    def __init__(self, size) -> None:
        self.size = size
    
    def esta_vacia(self):
        if self.tope == 0:
            return True
        else:
            return False

    def insertar(self, dato):
        if self.tope < self.size:
            self.lista += [dato]
            self.tope += 1
        else:
            print("La pila esta llena!")

    def eliminar(self):
        dato = self.lista[self.tope-1]
        self.tope -= 1
        self.lista.pop()
        return dato

    def cima(self):
        print(self.lista[self.tope-1])