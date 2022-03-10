def busquedaLineal(dato, lista):
    for x in range(len(lista)):
        if lista[x] == dato:
            return x
    return None

def buscar(dato, lista):
    ans = busquedaLineal(dato, lista)
    if ans == None:
        return "El dato no se encontro"
    else:
        return f"El dato {dato} fue encontrado en la posicion {ans}"

if __name__ == "__main__":
    lista = [10,23,12,87,83,76,83]
    print(buscar(87, lista))