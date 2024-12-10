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
