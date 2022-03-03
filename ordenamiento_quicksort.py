def particionado(lista):
    pivote = lista[0]
    menores = []
    mayores = []

    for i in range(1, len(lista)):
        if lista[i] < pivote:
            menores.append(lista[i])
        else:
            mayores.append(lista[i])
    return menores, pivote, mayores

def quicksort(lista):
    if len(lista) < 2:
        return lista
    
    menores, pivote, mayores = particionado(lista)

    return quicksort(menores) + [pivote] + quicksort(mayores)

def run():
    print(quicksort([8,20,1,23,0,2,3,45,12,5,7,9,5,8]))

if __name__ == "__main__":
    run()