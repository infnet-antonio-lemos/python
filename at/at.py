from tabulate import tabulate

medicamentos = []


def cadastrar_medicamento(descricao, codigo, quantidade_disponivel, preco_venda):
    try:
        codigo = int(codigo)
        quantidade_disponivel = int(quantidade_disponivel)
        preco_venda = float(preco_venda)

        if codigo <= 0:
            print("Código deve ser maior que zero")
            return
        if quantidade_disponivel < 0:
            print("Quantidade disponível não pode ser negativa")
            return
        if preco_venda < 0:
            print("Preço não pode ser negativo")
            return
        if not descricao:
            print("Insira uma descrição!")
            return

        for medicamento in medicamentos:
            if medicamento["codigo"] == codigo:
                print("Já existe um medicamento com esse código cadastrado!")
                return

        medicamento = {
            "preco_venda": preco_venda,
            "descricao": descricao,
            "quantidade_disponivel": quantidade_disponivel,
            "codigo": codigo,
        }
        medicamentos.append(medicamento)
    except ValueError:
        print("Insira um valor válido para os números")


def inicializar_disponibilidade():
    disponibilidade_inicial = "Ozempic;201;15;1200.00#Victoza;202;10;700.00#Trulicity;203;50;800.00#Byetta;204;40;500.00#Bydureon;205;10;550.00#Rybelsus;206;8;600.00#Metformina;207;30;100.00#Jardiance;208;25;400.00#Farxiga;209;5;450.00#Invokana;210;3;400.00#Amaryl;211;12;150.00#Glifage;212;7;100.00"
    medicamentos = disponibilidade_inicial.split("#")
    for medicamento in medicamentos:
        [descricao, codigo, quantidade_disponivel, preco_venda] = medicamento.split(";")
        cadastrar_medicamento(descricao, codigo, quantidade_disponivel, preco_venda)


def listar_medicamentos(medicamentos):
    data = []
    for medicamento in medicamentos:
        row = [
            medicamento["codigo"],
            medicamento["descricao"],
            medicamento["quantidade_disponivel"],
            medicamento["preco_venda"],
        ]
        data.append(row)
    print(
        tabulate(
            data,
            headers=["codigo", "descrição", "quantidade disponível", "valor unitário"],
        )
    )


def ordenar_quantidade(desc=False):
    medicamentos_ordenados = sorted(
        medicamentos, key=lambda x: x["quantidade_disponivel"], reverse=desc
    )
    listar_medicamentos(medicamentos_ordenados)


def buscar_medicamento(busca):
    if busca.startswith("codigo"):
        codigo = int(busca.split("=")[1])
        medicamentos_filtrados = list(
            filter(lambda x: x["codigo"] == codigo, medicamentos)
        )

        if len(medicamentos_filtrados) == 0:
            print("Nenhum medicamento encontrado!")

        return listar_medicamentos(medicamentos_filtrados)
    elif busca.startswith("descricao"):
        descricao = busca.split("=")[1]
        medicamentos_filtrados = list(
            filter(lambda x: x["descricao"] == descricao, medicamentos)
        )

        if len(medicamentos_filtrados) == 0:
            print("Nenhum medicamento encontrado!")
        return listar_medicamentos(medicamentos_filtrados)
    else:
        print('Parâmetro inválido, use "codigo" ou "descricao"')


def remover_medicamento(codigo):
    try:
        codigo = int(codigo)
        for medicamento in medicamentos:
            if medicamento["codigo"] == codigo:
                medicamentos.remove(medicamento)
                return listar_medicamentos(medicamentos)
        print("Medicamento não encontrado!")
    except ValueError:
        print("Insira um valor válido para o código")


def consultar_esgotados():
    esgotados = list(filter(lambda x: x["quantidade_disponivel"] == 0, medicamentos))
    return listar_medicamentos(esgotados)


def listar_baixa_quantidade(quantidade=5):
    try:
        quantidade = int(quantidade)
        baixa_quantidade = list(
            filter(lambda x: x["quantidade_disponivel"] <= quantidade, medicamentos)
        )
        return listar_medicamentos(baixa_quantidade)
    except ValueError:
        print("Insira um número inteiro!")


def atualizar_disponibilidade(codigo, operacao, quantidade):
    try:
        codigo = int(codigo)
        quantidade = int(quantidade)

        if codigo <= 0:
            return print("Insira um valor positivo para o código")
        if quantidade <= 0:
            return print("Insira um valor maior ou igual a zero para a quantidade")
        if operacao != "aumentar" and operacao != "diminuir":
            return print('operacao deve ser "aumentar" ou "diminuir"')

        for medicamento in medicamentos:
            if medicamento["codigo"] == codigo:
                if operacao == "aumentar":
                    medicamento["quantidade_disponivel"] += quantidade
                elif operacao == "diminuir":
                    if quantidade > medicamento["quantidade_disponivel"]:
                        return print("Não pode diminuir mais do que tem disponível!")
                    medicamento["quantidade_disponivel"] -= quantidade
                return
        return print("Medicamento não encontrado!")

    except ValueError:
        print("Valor inválido para código ou quantidade")


def atualizar_preco(codigo, preco_venda):
    try:
        codigo = int(codigo)
        preco_venda = float(preco_venda)

        if preco_venda < 0:
            return print("Insira um valor positivo para o preço de venda")

        for medicamento in medicamentos:
            if medicamento["codigo"] == codigo:
                if preco_venda < medicamento["preco_venda"]:
                    return print("O valor não pode ser reduzido!")
                medicamento["preco_venda"] = preco_venda
                return
        return print("Medicamento não encontrado")
    except ValueError:
        print("Insira valores válidos para codigo e preco_venda")


def valor_total(codigo):
    try:
        codigo = int(codigo)

        for medicamento in medicamentos:
            if medicamento["codigo"] == codigo:
                return print(
                    medicamento["preco_venda"] * medicamento["quantidade_disponivel"]
                )
        return print("Medicamento não encontrado")
    except ValueError:
        print("Insira um valor inteiro para código")


inicializar_disponibilidade()
while True:
    comando = input(
        """Menu:
adicionar <codigo> <descricao> <quantidade_disponivel> <preco_venda>
listar
buscar <'codigo=xx' ou 'descricao=yy'>
remover <codigo>
consultar_esgotados
consultar_baixa_quantidade <quantidade_limite - opcional - padrão = 5>
atualizar_disponibilidade <codigo> <operacao - 'aumentar' ou 'diminuir'> <quantidade>
atualizar_preco <codigo> <preco_venda>
valor_total <codigo>

"""
    )
    if comando.startswith("adicionar"):
        try:
            _, codigo, descricao, quantidade_disponivel, preco_venda = (
                comando.strip().split(" ")
            )
            cadastrar_medicamento(descricao, codigo, quantidade_disponivel, preco_venda)
        except ValueError:
            print("Quantidade inválida de argumentos")
    elif comando.startswith("listar"):
        listar_medicamentos(medicamentos)
    elif comando.startswith("buscar"):
        try:
            _, busca = comando.strip().split(" ")
            buscar_medicamento(busca)
        except ValueError:
            print("Quantidade inválida de argumentos")
    elif comando.startswith("remover"):
        try:
            _, codigo = comando.strip().split(" ")
            remover_medicamento(codigo)
        except ValueError:
            print("Quantidade inválida de argumentos")
    elif comando.startswith("consultar_esgotados"):
        consultar_esgotados()
    elif comando.startswith("consultar_baixa_quantidade"):
        argumentos = comando.strip().split(" ")
        if len(argumentos) == 2:
            quantidade = argumentos[1]
            listar_baixa_quantidade(quantidade)
        elif len(argumentos) == 1:
            listar_baixa_quantidade()
        else:
            print("Quantidade inválida de argumentos")
    elif comando.startswith("atualizar_disponibilidade"):
        try:
            _, codigo, operacao, quantidade = comando.strip().split(" ")
            atualizar_disponibilidade(codigo, operacao, quantidade)
        except ValueError:
            print("Quantidade inválida de argumentos")
    elif comando.startswith("atualizar_preco"):
        try:
            _, codigo, preco = comando.strip().split(" ")
            atualizar_preco(codigo, preco)
        except ValueError:
            print("Quantidade inválida de argumentos")
    elif comando.startswith("valor_total"):
        try:
            _, codigo = comando.strip().split(" ")
            valor_total(codigo)
        except ValueError:
            print("Quantidade inválida de argumentos")
