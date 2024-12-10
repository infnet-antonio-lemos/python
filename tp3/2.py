def comeca_com(string, prefixo):
    return string[: len(prefixo) :] == prefixo


print(comeca_com("teste", "tes"))
