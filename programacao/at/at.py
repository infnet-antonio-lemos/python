medicamentos = []


def cadastrar_medicamento(descricao, codigo, quantidade_disponivel, preco_venda):
    """
    Cadastra um medicamento.

    Esta função valida os dados informados e adiciona um medicamento à lista. Se algum valor for inválido, a
    função imprime uma mensagem de erro apropriada e não realiza o cadastro.

    Parâmetros:
    descricao (str): Descrição do medicamento. Deve ser uma string não vazia.
    codigo (int): Código único do medicamento. Deve ser um número inteiro maior que zero.
    quantidade_disponivel (int): Quantidade disponível do medicamento. Deve ser um número inteiro não negativo.
    preco_venda (float): Preço de venda do medicamento. Deve ser um número de ponto flutuante não negativo.

    Retorna:
    Nenhum valor.
    """
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
    print(
        "Código".ljust(10),
        "Descrição".ljust(15),
        "Quantidade Disponível".ljust(25),
        "Valor Unitário".ljust(20),
    )
    print("-" * 70)
    for medicamento in medicamentos:
        print(
            f'{medicamento["codigo"]}'.ljust(10),
            f'{medicamento["descricao"]}'.ljust(15),
            f'{medicamento["quantidade_disponivel"]}'.ljust(25),
            f'{medicamento["preco_venda"]}'.ljust(20),
        )


def ordenar_quantidade(desc=False):
    """
    Ordena a lista de medicamentos pela quantidade disponível, em ordem crescente ou decrescente.

    Esta função ordena os medicamentos com base no valor da chave `quantidade_disponivel` de cada medicamento.
    O parâmetro `desc` determina a ordem de classificação:
    - Se `desc` for `False` (padrão), os medicamentos serão ordenados em ordem crescente de quantidade disponível.
    - Se `desc` for `True`, os medicamentos serão ordenados em ordem decrescente de quantidade disponível.

    Após ordenar, a função chama `listar_medicamentos` para exibir a lista de medicamentos ordenada.

    Parâmetros:
    desc (bool, opcional): Determina a ordem de classificação. O valor padrão é `False`, ou seja, ordem crescente.

    Retorna:
    Nenhum valor.
    """
    medicamentos_ordenados = sorted(
        medicamentos, key=lambda x: x["quantidade_disponivel"], reverse=desc
    )
    listar_medicamentos(medicamentos_ordenados)


def buscar_medicamento(busca):
    """
    Busca um medicamento na lista de medicamentos com base no código ou descrição.

    A função permite buscar medicamentos filtrando por dois critérios:
    - `codigo`: Busca um medicamento pelo seu código único.
    - `descricao`: Busca um medicamento pela descrição fornecida.

    Dependendo do formato do parâmetro `busca`, a função realiza a busca e filtra os medicamentos na lista `medicamentos`.
    Se nenhum medicamento for encontrado, a função exibe a mensagem "Nenhum medicamento encontrado!".
    Se o parâmetro fornecido não for válido, a função exibe a mensagem "Parâmetro inválido, use 'codigo' ou 'descricao'".

    Parâmetros:
    busca (str): O parâmetro de busca. Deve ser uma string no formato:
                 - "codigo=<codigo>" para buscar por código.
                 - "descricao=<descricao>" para buscar por descrição.

    Exceções:
    - Caso o valor de `busca` não comece com "codigo" ou "descricao", a função imprime a mensagem de erro informando o parâmetro inválido.
    - Se não houver nenhum medicamento que corresponda à busca, a função imprime a mensagem "Nenhum medicamento encontrado!".

    Retorna:
    Nenhum valor.
    """
    if busca.startswith("codigo"):
        codigo = busca.split("=")[1]
        medicamentos_filtrados = list(
            filter(lambda x: codigo in str(x["codigo"]), medicamentos)
        )

        if len(medicamentos_filtrados) == 0:
            print("Nenhum medicamento encontrado!")

        return listar_medicamentos(medicamentos_filtrados)
    elif busca.startswith("descricao"):
        descricao = busca.split("=")[1]
        medicamentos_filtrados = list(
            filter(lambda x: descricao in x["descricao"], medicamentos)
        )

        if len(medicamentos_filtrados) == 0:
            print("Nenhum medicamento encontrado!")
        return listar_medicamentos(medicamentos_filtrados)
    else:
        print('Parâmetro inválido, use "codigo" ou "descricao"')


def remover_medicamento(codigo):
    """
    Remove um medicamento da lista com base no código fornecido.

    A função percorre a lista `medicamentos` e remove o medicamento que possui o código correspondente ao valor
    fornecido. Se o medicamento com o código especificado não for encontrado, a função imprime a mensagem
    "Medicamento não encontrado!". Se o código não for um número válido, a função imprime a mensagem
    "Insira um valor válido para o código".

    Parâmetros:
    codigo (int ou str): O código do medicamento a ser removido. Deve ser um número inteiro ou uma string que
                         possa ser convertida para inteiro.

    Exceções:
    - Caso o valor fornecido para `codigo` não seja um número inteiro válido, a função exibe a mensagem de erro
      "Insira um valor válido para o código".
    - Se o código não corresponder a nenhum medicamento na lista, a função imprime a mensagem "Medicamento não encontrado!".

    Retorna:
    Nenhum valor.
    """
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
    """
    Consulta e exibe os medicamentos com quantidade disponível igual a zero.

    A função filtra os medicamentos da lista `medicamentos` para identificar aqueles que possuem
    `quantidade_disponivel` igual a zero, ou seja, que estão esgotados. Em seguida, a função chama
    `listar_medicamentos` para exibir os medicamentos esgotados encontrados.

    Parâmetros:
    Nenhum.

    Retorna:
    Nenhum valor.
    """
    esgotados = list(filter(lambda x: x["quantidade_disponivel"] == 0, medicamentos))
    return listar_medicamentos(esgotados)


def listar_baixa_quantidade(quantidade=5):
    """
    Lista os medicamentos com quantidade disponível abaixo ou igual a um valor especificado.

    A função filtra os medicamentos na lista `medicamentos` para encontrar aqueles cuja
    `quantidade_disponivel` seja menor ou igual ao valor fornecido no parâmetro `quantidade`.
    O parâmetro `quantidade` tem um valor padrão de 5. Após o filtro, a função chama `listar_medicamentos`
    para exibir a lista de medicamentos com baixa quantidade.

    Parâmetros:
    quantidade (int, opcional): O limite de quantidade para filtrar os medicamentos. O valor padrão é 5.

    Exceções:
    - Caso o valor de `quantidade` não seja um número inteiro válido, a função imprime a mensagem de erro
      "Insira um número inteiro!".

    Retorna:
    Nenhum valor.
    """
    try:
        quantidade = int(quantidade)
        baixa_quantidade = list(
            filter(lambda x: x["quantidade_disponivel"] <= quantidade, medicamentos)
        )
        return listar_medicamentos(baixa_quantidade)
    except ValueError:
        print("Insira um número inteiro!")


def atualizar_disponibilidade(codigo, operacao, quantidade):
    """
    Atualiza a quantidade disponível de um medicamento na lista `medicamentos`.

    A função permite aumentar ou diminuir a quantidade disponível de um medicamento identificado
    pelo `codigo`. Dependendo da operação especificada no parâmetro `operacao`, a quantidade do
    medicamento será alterada:
    - Se `operacao` for "aumentar", a quantidade disponível será incrementada pelo valor de `quantidade`.
    - Se `operacao` for "diminuir", a quantidade disponível será decrementada, mas não pode ser reduzida
      abaixo de zero.

    Parâmetros:
    codigo (int): O código do medicamento a ser atualizado. Deve ser um número inteiro positivo.
    operacao (str): A operação a ser realizada. Deve ser "aumentar" ou "diminuir".
    quantidade (int): A quantidade a ser adicionada ou subtraída. Deve ser um número inteiro maior que zero.

    Exceções:
    - Caso `codigo` ou `quantidade` não sejam números inteiros válidos, a função imprime a mensagem de erro
      "Valor inválido para código ou quantidade".

    Retorna:
    Nenhum valor.
    """
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
    """
    Atualiza o preço de venda de um medicamento na lista `medicamentos`.

    A função permite atualizar o preço de venda de um medicamento identificado pelo `codigo`. O novo preço
    só será aceito se for maior ou igual ao preço atual. Caso o novo preço seja inferior ao preço atual,
    a função não realizará a alteração e exibirá a mensagem "O valor não pode ser reduzido!".

    Parâmetros:
    codigo (int): O código do medicamento a ser atualizado. Deve ser um número inteiro positivo.
    preco_venda (float): O novo preço de venda do medicamento. Deve ser um número de ponto flutuante positivo.

    Exceções:
    - Caso `codigo` ou `preco_venda` não sejam números válidos (inteiro e float, respectivamente), a função imprime
      a mensagem "Insira valores válidos para codigo e preco_venda".

    Retorna:
    Nenhum valor.
    """
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
    """
    Calcula e exibe o valor total de um medicamento com base no seu preço de venda e na quantidade disponível.

    A função busca um medicamento na lista `medicamentos` pelo `codigo` fornecido. Se o medicamento for encontrado,
    ela calcula o valor total multiplicando o preço de venda (`preco_venda`) pela quantidade disponível (`quantidade_disponivel`)
    e imprime o resultado. Caso contrário, a função imprime a mensagem "Medicamento não encontrado".

    Parâmetros:
    codigo (int): O código do medicamento para o qual o valor total será calculado. Deve ser um número inteiro positivo.

    Exceções:
    - Caso o valor de `codigo` não seja um número inteiro válido, a função imprime a mensagem de erro
      "Insira um valor inteiro para código".

    Retorna:
    Nenhum.
    """
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


def calcular_lucro_presumido():
    """
    Calcula o lucro presumido total de todos os medicamentos, considerando diferentes margens de lucro
    com base no preço de venda.

    A função percorre todos os medicamentos na lista `medicamentos` e calcula o lucro presumido para cada um,
    aplicando diferentes margens de custo de acordo com o preço de venda:
    - Para medicamentos com preço de venda menor ou igual a 500, a margem de custo é de 25% (lucro de 75%).
    - Para medicamentos com preço de venda entre 501 e 700, a margem de custo é de 20% (lucro de 80%).
    - Para medicamentos com preço de venda superior a 700, a margem de custo é de 15% (lucro de 85%).

    O lucro de cada medicamento é calculado como o valor de venda multiplicado pela margem de lucro e pela quantidade
    disponível, sendo somado ao lucro total.

    Parâmetros:
    Nenhum.

    Retorna:
    Lucro total (float).
    """
    # custo - 25% items com valor <= 500
    # custo - 20% items com 500 < valor <= 700
    # custo - 15% valor > 700
    lucro_total = 0
    for medicamento in medicamentos:
        if medicamento["preco_venda"] <= 500:
            lucro_medicamento = (medicamento["preco_venda"] * 0.75) * medicamento[
                "quantidade_disponivel"
            ]
            lucro_total += lucro_medicamento
        elif medicamento["preco_venda"] <= 700:
            lucro_medicamento = (medicamento["preco_venda"] * 0.80) * medicamento[
                "quantidade_disponivel"
            ]
            lucro_total += lucro_medicamento
        else:
            lucro_medicamento = (medicamento["preco_venda"] * 0.85) * medicamento[
                "quantidade_disponivel"
            ]
            lucro_total += lucro_medicamento
    print(f"Lucro Total: {lucro_total}")
    return lucro_total


def relatorio_geral():
    print(
        "Descrição".ljust(15),
        "Código".ljust(10),
        "Quantidade".ljust(12),
        "Preço".ljust(10),
        "Valor Total".ljust(15),
    )
    print("-" * 62)
    faturamento = 0

    for medicamento in medicamentos:
        faturamento += medicamento["preco_venda"] * medicamento["quantidade_disponivel"]
        print(
            medicamento["descricao"].ljust(15),
            f'{medicamento["codigo"]}'.ljust(10),
            f'{medicamento["quantidade_disponivel"]}'.ljust(12),
            f'{medicamento["preco_venda"]}'.ljust(10),
            f'{medicamento["preco_venda"] * medicamento["quantidade_disponivel"]}'.ljust(
                15
            ),
        )
    print("-" * 62)
    lucro = calcular_lucro_presumido()
    custo_total = faturamento - lucro
    print(f"Custo total: {custo_total}")
    print(f"Faturamento: {faturamento}")


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
lucro_total
relatorio
finalizar

"""
    )
    # adicionar
    if comando.startswith("adicionar"):
        try:
            _, codigo, descricao, quantidade_disponivel, preco_venda = (
                comando.strip().split(" ")
            )
            cadastrar_medicamento(descricao, codigo, quantidade_disponivel, preco_venda)
        except ValueError:
            print("Quantidade inválida de argumentos")
    # listar
    elif comando.startswith("listar"):
        listar_medicamentos(medicamentos)
    # buscar
    elif comando.startswith("buscar"):
        try:
            _, busca = comando.strip().split(" ")
            buscar_medicamento(busca)
        except ValueError:
            print("Quantidade inválida de argumentos")
    # remover
    elif comando.startswith("remover"):
        try:
            _, codigo = comando.strip().split(" ")
            remover_medicamento(codigo)
        except ValueError:
            print("Quantidade inválida de argumentos")
    # consultar_esgotados
    elif comando.startswith("consultar_esgotados"):
        consultar_esgotados()
    # consultar_baixa_quantidade
    elif comando.startswith("consultar_baixa_quantidade"):
        argumentos = comando.strip().split(" ")
        if len(argumentos) == 2:
            quantidade = argumentos[1]
            listar_baixa_quantidade(quantidade)
        elif len(argumentos) == 1:
            listar_baixa_quantidade()
        else:
            print("Quantidade inválida de argumentos")
    # atualizar_disponibilidade
    elif comando.startswith("atualizar_disponibilidade"):
        try:
            _, codigo, operacao, quantidade = comando.strip().split(" ")
            atualizar_disponibilidade(codigo, operacao, quantidade)
        except ValueError:
            print("Quantidade inválida de argumentos")
    # atualizar_preco
    elif comando.startswith("atualizar_preco"):
        try:
            _, codigo, preco = comando.strip().split(" ")
            atualizar_preco(codigo, preco)
        except ValueError:
            print("Quantidade inválida de argumentos")
    # valor_total
    elif comando.startswith("valor_total"):
        try:
            _, codigo = comando.strip().split(" ")
            valor_total(codigo)
        except ValueError:
            print("Quantidade inválida de argumentos")
    # lucro_total
    elif comando.startswith("lucro_total"):
        calcular_lucro_presumido()
    # relatorio
    elif comando.startswith("relatorio"):
        relatorio_geral()
    # finalizar
    elif comando.startswith("finalizar"):
        break

    else:
        print("Comando inválido, tente novamente")
