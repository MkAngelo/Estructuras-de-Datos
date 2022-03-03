def particionado(lista, menor, mayor):
    pivote = lista[menor]
    izq = menor + 1
    der = mayor

    while True:
        while izq <= der and lista[izq] <= pivote:
            izq += 1
        while izq <= der and lista[der] >= pivote:
            der -= 1
        if der < izq:
            break
        else:
            lista[izq], lista[der] = lista[der], lista[izq]
    
    lista[menor], lista[der] = lista[der], lista[menor]
    
    return der

def quicksort(lista, menor, mayor):
    if menor < mayor:
        pivote = particionado(lista,menor,mayor)
        quicksort(lista, menor, pivote - 1)
        quicksort(lista, pivote + 1, mayor)


lista = [30,45,50,5,25,10,20,35,40,15]
print(lista)
quicksort(lista, 0, len(lista)-1)
print(lista)