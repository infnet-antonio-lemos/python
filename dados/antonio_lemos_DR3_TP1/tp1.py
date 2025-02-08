def ex1():
    medicamentos = {
        "dipirona": 5.00,
    }
    medicamentos["paracetamol"] = 10.00
    print(medicamentos)


def ex2():
    produtos = {
        "arroz": 10,
        "feijão": 5,
        "macarrão": 7,
    }
    produtos.pop("feijão")
    print(produtos)


def ex3():
    contatos = {
        "joão": "9999-9999",
        "maria": "8888-8888",
    }
    contatos["joão"] = "7777-7777"
    print(contatos)


def ex4():
    filmes = {
        "Titanic": 7.5,
        "matrix": 8.0,
        "aftersun": 9.0,
        "Emilia Perez": 3.0,
        "driver": 7.0,
    }
    filmes_acima_de_7 = {filme: nota for filme, nota in filmes.items() if nota > 7}
    print(filmes_acima_de_7)


def ex5():
    quartos = {
        "Quarto padrão": 100.00,
        "Quarto luxuoso": 200.00,
        "Suíte": 300.00,
    }
    for quarto, preco in quartos.items():
        print(f"{quarto}: R$ {preco:.2f}")


def ex6():
    sales = {}

    def register_sale(piece, price):
        if piece in sales:
            sales[piece] += price
        else:
            sales[piece] = price

    def remove_piece(piece):
        if piece in sales:
            del sales[piece]
        else:
            print("Peça não encontrada.")

    def show_sales():
        if not sales:
            print("Nenhuma venda registrada.")
        else:
            for piece, price in sales.items():
                print(f"{piece}: R$ {price:.2f}")

    while True:
        print("Registro de Vendas:")
        print("1 - Registrar venda")
        print("2 - Remover peça")
        print("3 - Exibir vendas")
        print("0 - Sair")
        choice = input("Escolha uma opção: ")

        if choice == "1":
            piece = input("Informe o nome da peça: ")
            try:
                value = float(input("Informe o valor da venda: "))
            except ValueError:
                print("Valor inválido. Tente novamente.")
                continue
            register_sale(piece, value)
        elif choice == "2":
            piece = input("Informe o nome da peça a remover: ")
            remove_piece(piece)
        elif choice == "3":
            show_sales()
        elif choice == "0":
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")


def ex7():
    z = {x: x**2 for x in range(1, 10, 2)}
    print(z)


def ex8():
    access_log = [
        "accessed: /home",
        "accessed: /about",
        "accessed: /home",
        "accessed: /contact",
        "accessed: /about",
        "accessed: /home",
    ]
    histogram = {}
    for access in access_log:
        url = access.split(": ")[1]
        if url in histogram:
            histogram[url] += 1
        else:
            histogram[url] = 1
    print(histogram)


def ex9():
    filmes = ["wildrobot", "everything, everywhere all at once", "challengers"]
    filmes_tupla = tuple(filmes)
    print(filmes_tupla)


def ex10():
    livro = ["Duna", "João Duna", 1970]
    livro_tupla = tuple(livro)
    titulo, autor, ano = livro_tupla
    print(f"Título: {titulo}")
    print(f"Autor: {autor}")
    print(f"Ano: {ano}")


def ex11():
    itens = set(["dipirona", "paracetamol"])
    itens.add("ibuprofeno")
    print(itens)


def ex12():
    produtos = ["arroz", "feijão", "macarrão", "arroz", "feijão"]
    produtos_set = set(produtos)

    def disponivel(produto):
        return produto in produtos_set

    print(disponivel("arroz"))


def ex13():
    filmes1 = set(["Titanic", "substance", "godzilla minus one"])
    filmes2 = set(["Titanic", "Emilia Perez", "driver"])
    filmes_intersection = filmes1.intersection(filmes2)
    print(filmes_intersection)


def ex14():
    perefencias = set(["arroz", "feijão", "macarrão"])

    def remover_preferencia(item):
        perefencias.discard(item)

    remover_preferencia("arroz")
    print(perefencias)


def ex15():
    musicas_favoritas_1 = [
        "long season",
        "ordinary joe",
        "time",
    ]
    musicas_favoritas_2 = ["time", "read my mind", "final days"]

    playlist = set(musicas_favoritas_1 + musicas_favoritas_2)
    print(playlist)
    print(len(playlist))


def ex16():
    ingredientes = set(["pimenta do reino", "sal", "ovos", "farinha"])

    def adicionar_ingrediente(ingrediente):
        ingredientes.add(ingrediente)

    def remover_ingrediente(ingrediente):
        ingredientes.discard(ingrediente)

    def imprimir_ingredientes():
        print(ingredientes)

    adicionar_ingrediente("açúcar")
    remover_ingrediente("sal")
    imprimir_ingredientes()
