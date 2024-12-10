def inserir_palavra(palavras: list, nova: str, position=0):
    if len(palavras) < 3:
        palavras.append(nova)
        return palavras
    palavras.insert(position, nova)
    return palavras


print(inserir_palavra(["a", "b"], "c"))
print(inserir_palavra(["a", "b", "c"], "d", 1))
