def busqueda(lista, dato):
    izquierda = 0
    derecha = len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if dato == lista[medio]:
            return medio
        elif dato < lista[medio]:
            derecha = medio-1
        else:
            izquierda = medio+1    
    return None
 
def part(lista):
    pivote = lista[0]
    menores = []
    mayores = []

    for i in range(1, len(lista)):
        if(lista[i] < pivote):
            menores.append(lista[i])
        else:
            mayores.append(lista[i])

    return menores, pivote, mayores

def ordenamiento(lista):
    if(len(lista) < 2):
        return lista
    
    menores, pivote, mayores = part(lista)

    return ordenamiento(menores) + [pivote] + ordenamiento(mayores)

def run():
    lista = [8,5,20,2,4,89,65,74,82,90]
    lista_ordenada = ordenamiento(lista)
    ans = busqueda(lista_ordenada,9)
    if (ans != None):
        print("El elemento si esta en la lista")
    else:
        print("El elemento no esta en la lista")

if __name__ == "__main__":
    run()