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
