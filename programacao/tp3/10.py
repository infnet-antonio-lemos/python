def caracteres_em_comum(string1: str, string2: str):
    set_1 = set(string1)
    set_2 = set(string2)

    return list(set_1.intersection(set_2))


print(caracteres_em_comum("baba", "yaga"))
