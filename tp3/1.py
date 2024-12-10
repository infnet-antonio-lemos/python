def metades(valor):
    metade = len(valor) // 2
    primeira_metade = valor[0:metade]
    segunda_metade = valor[metade::]

    return [primeira_metade, segunda_metade]


print(metades("testes"))
