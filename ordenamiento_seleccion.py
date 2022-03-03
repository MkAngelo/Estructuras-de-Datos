"""
ORDENAMIENTO POR SELECCION

Es un algoritmo que consiste en ordenar los elementos de manera ascendente o descendente

Funcionamiento:
- Buscar el dato mas pequeno de la lista
- Intercambiarlo por el actual
- Seguir buscandoe el dato mas pequeno de la lista
- Intercambiarlo por el actual
- Asi sucesivamente
"""

lista = [4,2,6,8,5,7,0]

for i in range(len(lista)):
    minimo = i
    for x in range(i, len(lista)):
        if lista[x] < lista[minimo]:
            minimo = x
    aux = lista[i]
    lista[i] = lista[minimo]
    lista[minimo] = aux

print(lista)
