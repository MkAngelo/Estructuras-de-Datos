from hashlib import new
from pilas import Pila

if __name__ == "__main__":
    size = int(input("De que tamaño quieres la pila? "))
    pilita = Pila(size)

    while True:

        opcion = int(input("--------PILAS---------\n" +
        "1. Agregar elemento\n" +
        "2. Quitar elemento\n" +
        "3. Pila esta vacia?\n" +
        "4. Que elemento esta en la cima?\n" +
        "5. Salir\n" +
        "Selección: " 
        ))

        if (opcion == 1):
            elemento = int(input("Ingresa el elemento a insertar: "))
            pilita.push(elemento)
        elif(opcion == 2):
            if not pilita.empty:
                elemento = pilita.pop
                print(f"El elemento eliminado es: {elemento}")
            else:
                print("La pila esta vacia!")
        elif(opcion == 3):
            if pilita.empty:
                print("La pila esta vacia")
            else:
                print("La pila esta llena!")
        elif(opcion == 4):
            if not pilita.empty:
                elemento = pilita.last
                print(f"El elemento en la cima es: {elemento}")
            else:
                print("La pila esta vacia!")
        elif(opcion == 5):
            False
        else:
            print("Opción incorrecta")
