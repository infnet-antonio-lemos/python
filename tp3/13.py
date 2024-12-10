def apagar_duplicatas(palavras: list):
    return list(set(palavras))


print(apagar_duplicatas(["a", "a", "b"]))
