numero_mapper = {
    "0": "zero",
    "1": "um",
    "2": "dois",
    "3": "três",
    "4": "quatro",
    "5": "cinco",
    "6": "seis",
    "7": "sete",
    "8": "oito",
    "9": "nove",
}


def numero_em_portugues(numero: int):
    return [numero_mapper[x] for x in str(numero)]


print(numero_em_portugues(32))
