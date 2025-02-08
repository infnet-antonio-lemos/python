# QUESTÃO 1
print("QUESTÃO 1")


def metades(valor):
    metade = len(valor) // 2
    primeira_metade = valor[0:metade]
    segunda_metade = valor[metade::]

    return [primeira_metade, segunda_metade]


print(metades("testes"))

# QUESTÃO 2
print("QUESTÃO 2")


def comeca_com(string, prefixo):
    return string[: len(prefixo) :] == prefixo


print(comeca_com("teste", "tes"))

# QUESTÃO 3
print("QUESTÃO 3")


def string_to_list(string):
    return [x for x in string]


print(string_to_list("teste"))

# QUESTÃO 4
print("QUESTÃO 4")


def substitui_str(string: str, ocorrencia: str, substituicao: str):
    return string.replace(ocorrencia, substituicao)


print(substitui_str("teste", "t", "b"))


# QUESTÃO 5
print("QUESTÃO 5")


def is_numeric_string(string: str):
    return string.isnumeric()


print(is_numeric_string("123"))
print(is_numeric_string("123a"))


# QUESTÃO 6
print("QUESTÃO 6")


def numero_reverso(numero: int):
    return str(numero)[::-1]


print(numero_reverso(123))


# QUESTÃO 7
print("QUESTÃO 7")
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


# QUESTÃO 8
print("QUESTÃO 8")


def remove_duplicados(lista: list):
    return list(set(lista))


print(remove_duplicados(["a", "a", "b"]))


# QUESTÃO 9
print("QUESTÃO 9")


def soma_dos_digitos(numero: int):
    soma = 0
    for digit in str(numero):
        soma += int(digit)
    return soma


print(soma_dos_digitos(32))


# QUESTÃO 10
print("QUESTÃO 10")


def caracteres_em_comum(string1: str, string2: str):
    set_1 = set(string1)
    set_2 = set(string2)

    return list(set_1.intersection(set_2))


print(caracteres_em_comum("baba", "yaga"))


# QUESTÃO 11
print("QUESTÃO 11")


def inserir_palavra(palavras: list, nova: str, position=0):
    if len(palavras) < 3:
        palavras.append(nova)
        return palavras
    palavras.insert(position, nova)
    return palavras


print(inserir_palavra(["a", "b"], "c"))
print(inserir_palavra(["a", "b", "c"], "d", 1))


# QUESTÃO 12
print("QUESTÃO 12")


def combinar_listas(lista1: list, lista2: list):
    lista1.extend(lista2)
    return lista1


print(combinar_listas([1], [2]))


# QUESTÃO 13
print("QUESTÃO 13")


def apagar_duplicatas(palavras: list):
    return list(set(palavras))


print(apagar_duplicatas(["a", "a", "b"]))


# QUESTÃO 14
print("QUESTÃO 14")


def organizar_compras(itens: list):
    if len(itens) == 0:
        print("Não há mais itens para remover")
        return
    print(f"Item removido: {itens.pop()}")
    print("Sua lista de compras:")
    for x in itens:
        print(x)
    return itens


organizar_compras(["a", "b", "c"])


# QUESTÃO 15
print("QUESTÃO 15")


def manusear_string(string: str):
    print(string)
    try:
        inicio = int(input("Insira o índice de início: "))
        fim = int(input("Insira o índice de fim: "))

        if inicio < 0 or inicio >= len(string):
            print("Valor inválido para o início")
            return
        if fim > len(string) or fim < inicio:
            print("Valor inválido para o fim!")
            return

        return string[inicio:fim]
    except ValueError:
        print("Valor inválido, insira um inteiro")


print(manusear_string("string"))


# QUESTÃO 16
print("QUESTÃO 16")


def administrar_lista_compras(lista_compras):
    while True:
        print("\n\nLista de Compras:", lista_compras)
        comando = input(
            "'fim' - encerrar \n'retirar <nome ou índice>' - remover um item\n'acrescentar <índice> <produto>' - adicionar um item\n"
        )

        if comando.startswith("fim"):
            print("Lista de compras finalizada.")
            break
        elif comando.startswith("retirar"):
            try:
                item = comando[len("retirar") :].strip()

                if item.isdigit():
                    index = int(item)
                    if 0 <= index < len(lista_compras):
                        lista_compras.pop(index)
                        print(f"Item no índice {index} foi removido.")
                    else:
                        print("Índice inválido.")
                else:
                    if item in lista_compras:
                        lista_compras.remove(item)
                        print(f"O item '{item}' foi removido.")
                    else:
                        print(f"O item '{item}' não está na lista.")
            except:
                print(f"Erro ao tentar remover item")
        elif comando.startswith("acrescentar"):
            try:
                partes = comando[len("acrescentar") :].strip().split(" ", 1)
                if len(partes) == 2:
                    index = int(partes[0])
                    item = partes[1]

                    if item.isnumeric():
                        print("Não insira números!")
                        continue

                    if 0 <= index <= len(lista_compras):
                        lista_compras.insert(index, item)
                        print(f"Item '{item}' foi adicionado no índice {index}.")
                    else:
                        print("Índice inválido.")
                else:
                    print(
                        "Comando 'acrescentar' inválido. Certifique-se de usar 'acrescentar <índice> <produto>'."
                    )
            except ValueError:
                print("Índice inválido. Deve ser um número inteiro.")
            except:
                print(f"Erro ao tentar acrescentar item")
        else:
            print("Comando inválido. Tente novamente.")


lista_compras = ["leite", "pão", "banana"]
administrar_lista_compras(lista_compras)
