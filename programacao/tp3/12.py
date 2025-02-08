def combinar_listas(lista1: list, lista2: list):
    lista1.extend(lista2)
    return lista1


print(combinar_listas([1], [2]))
