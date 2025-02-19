import csv
import sqlite3
import datetime


def ler_csv(nome_arquivo):
    with open(nome_arquivo, "r") as arquivo:
        leitor = csv.DictReader(arquivo)
        dados = [linha for linha in leitor]
    return dados


cargos = ler_csv("cargos.csv")
departamentos = ler_csv("departamentos.csv")
dependentes = ler_csv("dependentes.csv")
funcionarios = ler_csv("funcionarios.csv")
pagamentos_salarios = ler_csv("pagamentos_salarios.csv")
projetos = ler_csv("projetos.csv")
recursos_projetos = ler_csv("recursos_projetos.csv")


def criar_tabelas():
    conexao = sqlite3.connect("empresa.db")
    cursor = conexao.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS `funcionarios` (
            `id` INTEGER PRIMARY KEY,
            `nome` TEXT NOT NULL,
            `salario` REAL NOT NULL,
            `cargo_id` INTEGER NOT NULL,
            `departamento_id` INTEGER NOT NULL
        );
        """
    )
    print("Tabela funcionarios criada")
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS `cargos` (
            `id` INTEGER PRIMARY KEY,
            `descricao` TEXT NOT NULL,
            `salario_base` REAL NOT NULL,
            `nivel` TEXT CHECK(nivel IN ('estagiario', 'tecnico', 'analista', 'gerente', 'diretor')) NOT NULL
        );
        """
    )
    print("Tabela cargos criada")
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS `departamentos` (
            `id` INTEGER PRIMARY KEY,
            `nome` TEXT NOT NULL,
            `gerente_id` INTEGER,
            `andar` INTEGER NOT NULL,
            FOREIGN KEY (`gerente_id`) REFERENCES `funcionarios` (`id`)
        );
        """
    )
    print("Tabela departamentos criada")
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS `pagamentos_salario` (
            `id` INTEGER PRIMARY KEY,
            `data_pagamento` DATE NOT NULL,
            `valor` REAL NOT NULL,
            `funcionario_id` INTEGER NOT NULL,
            FOREIGN KEY (`funcionario_id`) REFERENCES `funcionarios` (`id`)
        );
    """
    )
    print("Tabela pagamentos_salario criada")
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS `dependentes` (
        `id` INTEGER PRIMARY KEY,
        `nome` TEXT NOT NULL,
        `relacao` TEXT CHECK(relacao IN ('filhos', 'netos', 'conjugues', 'pais', 'avos', 'tios', 'outros')) NOT NULL,
        `funcionario_id` INTEGER NOT NULL,
        `genero` TEXT CHECK(genero IN ('masculino', 'feminino')) NOT NULL,
        `idade` INTEGER NOT NULL,
        FOREIGN KEY (`funcionario_id`) REFERENCES `funcionarios` (`id`)
    );
    """
    )
    print("Tabela dependentes criada")
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS `projetos` (
            `id` INTEGER PRIMARY KEY,
            `nome` TEXT NOT NULL,
            `descricao` TEXT NOT NULL,
            `data_inicio` DATE NOT NULL,
            `data_conclusao` DATE NULL,
            `custo` REAL NOT NULL,
            `status` TEXT CHECK(status IN ('planejamento', 'execução', 'concluído', 'cancelado')) NOT NULL,
            `funcionario_id` INTEGER NOT NULL,
            FOREIGN KEY (`funcionario_id`) REFERENCES `funcionarios` (`id`)
        );
        """
    )
    print("Tabela projetos criada")
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS `recursos_projetos` (
            `id` INTEGER PRIMARY KEY,
            `projeto_id` INTEGER NOT NULL,
            `descricao` TEXT NOT NULL,
            `tipo` TEXT CHECK(tipo IN ('financeiro', 'material', 'humano')),
            `quantidade` INTEGER NOT NULL,
            `data_utilizacao` DATE NOT NULL,
            FOREIGN KEY (`projeto_id`) REFERENCES `projetos` (`id`)
        );
        """
    )
    print("Tabela recursos_projetos criada")
    conexao.commit()
    conexao.close()


def popular_tabelas():
    conexao = sqlite3.connect("empresa.db")
    cursor = conexao.cursor()
    for cargo in cargos:
        cursor.execute(
            """
            INSERT OR IGNORE INTO `cargos` (`id`, `descricao`, `salario_base`, `nivel`)
            VALUES (?, ?, ?, ?);
            """,
            (cargo["id"], cargo["descricao"], cargo["salario_base"], cargo["nivel"]),
        )
    print("Tabela cargos populada")
    for departamento in departamentos:
        cursor.execute(
            """
            INSERT OR IGNORE INTO `departamentos` (`id`, `nome`, `gerente_id`, `andar`)
            VALUES (?, ?, ?, ?);
            """,
            (
                departamento["id"],
                departamento["nome"],
                departamento["gerente_id"],
                departamento["andar"],
            ),
        )
    print("Tabela departamentos populada")
    for dependente in dependentes:
        cursor.execute(
            """
            INSERT OR IGNORE INTO `dependentes` (`id`, `nome`, `relacao`, `funcionario_id`, `genero`, `idade`)
            VALUES (?, ?, ?, ?, ?, ?);
            """,
            (
                dependente["id"],
                dependente["nome"],
                dependente["relacao"],
                dependente["funcionario_id"],
                dependente["genero"],
                dependente["idade"],
            ),
        )
    print("Tabela dependentes populada")
    for funcionario in funcionarios:
        cursor.execute(
            """
            INSERT OR IGNORE INTO `funcionarios` (`id`, `nome`, `salario`, `cargo_id`, `departamento_id`)
            VALUES (?, ?, ?, ?, ?);
            """,
            (
                funcionario["id"],
                funcionario["nome"],
                funcionario["salario"],
                funcionario["cargo_id"],
                funcionario["departamento_id"],
            ),
        )
    print("Tabela funcionarios populada")
    for pagamento_salario in pagamentos_salarios:
        cursor.execute(
            """
            INSERT OR IGNORE INTO `pagamentos_salario` (`id`, `data_pagamento`, `valor`, `funcionario_id`)
            VALUES (?, ?, ?, ?);
            """,
            (
                pagamento_salario["id"],
                pagamento_salario["data_pagamento"],
                pagamento_salario["valor"],
                pagamento_salario["funcionario_id"],
            ),
        )
    print("Tabela pagamentos_salario populada")
    for projeto in projetos:
        cursor.execute(
            """
            INSERT OR IGNORE INTO `projetos` (`id`,`nome`,`descricao`,`data_inicio`,`data_conclusao`,`custo`,`status`,`funcionario_id`)
            VALUES (?, ? ,? ,? ,? ,? ,? ,?);
            """,
            (
                projeto["id"],
                projeto["nome"],
                projeto["descricao"],
                projeto["data_inicio"],
                projeto["data_conclusao"],
                projeto["custo"],
                projeto["status"],
                projeto["funcionario_id"],
            ),
        )
    print("Tabela projetos populada")
    for recurso in recursos_projetos:
        cursor.execute(
            """
            INSERT OR IGNORE INTO `recursos_projetos` (
                `id`,`projeto_id`,`descricao`,`tipo`,`quantidade`,`data_utilizacao`
            )
            VALUES (
                ?, ?, ?, ?, ?, ?
            )
            """,
            (
                recurso["id"],
                recurso["projeto_id"],
                recurso["descricao"],
                recurso["tipo"],
                recurso["quantidade"],
                recurso["data_utilizacao"],
            ),
        )
    print("Tabela recursos_projetos populada")
    conexao.commit()
    conexao.close()


def listar_tabelas():
    # csv
    print("Cargos")
    for cargo in cargos:
        print(cargo)
    print("Departamentos")
    for departamento in departamentos:
        print(departamento)
    print("Dependentes")
    for dependente in dependentes:
        print(dependente)
    print("Funcionarios")
    for funcionario in funcionarios:
        print(funcionario)
    print("Pagamentos Salarios")
    for pagamento_salario in pagamentos_salarios:
        print(pagamento_salario)


def listar_funcionarios():
    # csv
    for funcionario in funcionarios:
        cargo = [cargo for cargo in cargos if cargo["id"] == funcionario["cargo_id"]][0]
        departamento = [
            departamento
            for departamento in departamentos
            if departamento["id"] == funcionario["departamento_id"]
        ][0]
        depentendes = [
            dependente
            for dependente in dependentes
            if dependente["funcionario_id"] == funcionario["id"]
        ]
        print(f"Funcionario: {funcionario['nome']}, id: {funcionario['id']}")
        print(f"Cargo: {cargo['descricao']}, Nivel: {cargo['nivel']}")
        print(f"Departamento: {departamento['nome']}")
        print(
            f"Dependentes: {', '.join([depentendes['nome'] for depentendes in depentendes])}"
        )
        print("\n")


def listar_funcionarios_aumento_salarial():
    # csv
    funcionarios_com_aumento = []
    for funcionario in funcionarios:
        salarios = [
            salario
            for salario in pagamentos_salarios
            if salario["funcionario_id"] == funcionario["id"]
        ]
        salarios = sorted(
            salarios,
            key=lambda x: datetime.datetime.strptime(x["data_pagamento"], "%Y-%m-%d"),
            reverse=True,
        )
        if salarios[0]["valor"] > salarios[3]["valor"]:
            funcionarios_com_aumento.append(funcionario)
    for funcionario in funcionarios_com_aumento:
        print(f"Funcionario: {funcionario['nome']}, id: {funcionario['id']}")


def listar_media_idade_filhos():
    # sql
    conexao = sqlite3.connect("empresa.db")
    cursor = conexao.cursor()
    resultado = cursor.execute(
        """
        SELECT AVG(dependentes.idade), departamentos.nome 
        FROM funcionarios
            INNER JOIN dependentes ON funcionarios.id = dependentes.funcionario_id
            INNER JOIN departamentos ON funcionarios.departamento_id = departamentos.id
        WHERE dependentes.relacao = 'filhos'
        GROUP BY departamentos.id
        """
    )
    for media in resultado:
        print(f"Departamento: {media[1]} / Media de idade dos filhos: {media[0]}")


def listar_estagiario_filho():
    # sql
    conexao = sqlite3.connect("empresa.db")
    cursor = conexao.cursor()
    resultado = cursor.execute(
        """
        SELECT funcionarios.nome, dependentes.nome
        FROM funcionarios
            INNER JOIN dependentes ON funcionarios.id = dependentes.funcionario_id
            INNER JOIN cargos ON funcionarios.cargo_id = cargos.id
        WHERE cargos.nivel = 'estagiario' AND dependentes.relacao = 'filhos'
        """
    )
    for estagiario in resultado:
        print(f"Estagiario: {estagiario[0]} / Filho: {estagiario[1]}")


def listar_funcionario_salario_medio():
    # sql
    conexao = sqlite3.connect("empresa.db")
    cursor = conexao.cursor()
    resultado = cursor.execute(
        """
        SELECT funcionarios.nome, AVG(pagamentos_salario.valor), funcionarios.id
        FROM funcionarios
            INNER JOIN pagamentos_salario ON funcionarios.id = pagamentos_salario.funcionario_id
        GROUP BY funcionarios.id
        ORDER BY AVG(pagamentos_salario.valor) DESC
        LIMIT 1;
    """
    )
    for salario in resultado:
        print(
            f"Funcionario: {salario[0]} / Salario medio: {salario[1]} / id: {salario[2]}"
        )


def listar_analista_2_filhas():
    # sql
    conexao = sqlite3.connect("empresa.db")
    cursor = conexao.cursor()
    resultado = cursor.execute(
        """
        SELECT analistas.id, analistas.nome 
        FROM (
            SELECT
                COUNT(dependentes.id) as filhas,
                funcionarios.id as id,
                funcionarios.nome as nome
            FROM funcionarios
            INNER JOIN cargos ON funcionarios.cargo_id = cargos.id
            INNER JOIN dependentes ON funcionarios.id = dependentes.funcionario_id
            WHERE cargos.nivel = 'analista'
                AND dependentes.genero = 'feminino'
                AND dependentes.relacao = 'filhos'
            GROUP BY funcionarios.id
        ) as analistas
        WHERE filhas >= 2
        """
    )
    for funcionario in resultado:
        print(funcionario)


def listar_analista_salario_alto():
    # sql
    conexao = sqlite3.connect("empresa.db")
    cursor = conexao.cursor()
    resultado = cursor.execute(
        """
        SELECT
            funcionarios.nome,
            funcionarios.id,
            funcionarios.salario
        FROM funcionarios
        INNER JOIN cargos ON cargos.id = funcionarios.cargo_id
        WHERE cargos.nivel = 'analista'
        AND funcionarios.salario BETWEEN 5000 AND 9000
        ORDER BY funcionarios.salario DESC
        LIMIT 1
        """
    )
    for funcionario in resultado:
        print(
            f"Funcionário: {funcionario[0]} / id: {funcionario[1]} / Salário: {funcionario[2]}"
        )


def departamento_numero_dependentes():

    maior_departamento = None
    maior_contagem = 0
    for departamento in departamentos:
        dependentes_count = 0
        funcs = [
            funcionario
            for funcionario in funcionarios
            if funcionario["departamento_id"] == departamento["id"]
        ]
        for func in funcs:
            deps = [dep for dep in dependentes if dep["funcionario_id"] == func["id"]]
            dependentes_count += len(deps)
        if dependentes_count > maior_contagem or maior_departamento is None:
            maior_departamento = departamento
            maior_contagem = dependentes_count
    print(
        f"Departamento: {maior_departamento['nome']} / id: {maior_departamento['id']}"
    )


def media_salario_por_departamento():
    # csv
    medias_por_departamento = []
    for departamento in departamentos:
        salarios = [
            float(func["salario"])
            for func in funcionarios
            if func["departamento_id"] == departamento["id"]
        ]
        medias_por_departamento.append(
            {
                "id": departamento["id"],
                "nome": departamento["nome"],
                "media_salarial": sum(salarios) / len(salarios),
            }
        )
    ordenado_descrescente = sorted(
        medias_por_departamento, key=lambda x: x["media_salarial"], reverse=True
    )
    for dep in ordenado_descrescente:
        print(
            f"Departamento: {dep['nome']} / id: {dep['id']} / Média: {dep['media_salarial']}"
        )


def media_salario_projetos_concluidos():
    conexao = sqlite3.connect("empresa.db")
    cursor = conexao.cursor()
    resultado = cursor.execute(
        """
        SELECT
            d.nome,
            AVG(ps.valor) AS media
        FROM funcionarios f
        INNER JOIN (
            SELECT
                funcionario_id,
                MAX(data_pagamento) AS ultima_data
            FROM
                pagamentos_salario ps
            GROUP BY
                funcionario_id
        ) up ON up.funcionario_id = f.id
        INNER JOIN projetos p
            ON p.funcionario_id = f.id
        INNER JOIN departamentos d
            ON f.departamento_id = d.id
        INNER JOIN pagamentos_salario ps
            ON ps.funcionario_id = f.id
            AND ps.data_pagamento = up.ultima_data
        WHERE p.status = 'concluído'
        GROUP BY d.id;
        """
    )
    for linha in resultado:
        print(linha)


def recursos_mais_usados():
    conexao = sqlite3.connect("empresa.db")
    cursor = conexao.cursor()
    resultado = cursor.execute(
        """
        SELECT 
            descricao,
            quantidade
        FROM recursos_projetos rp
        ORDER BY rp.quantidade DESC
        LIMIT 3;
        """
    )
    for linha in resultado:
        print(linha)


def custo_projetos():
    conexao = sqlite3.connect("empresa.db")
    cursor = conexao.cursor()
    resultado = cursor.execute(
        """
        SELECT
            SUM(p.custo),
            d.nome
        FROM projetos p
        INNER JOIN funcionarios f
            ON f.id = p.funcionario_id
        INNER JOIN departamentos d
            ON d.id = f.departamento_id
        WHERE p.status = 'concluído'
        GROUP BY d.id;
        """
    )
    for linha in resultado:
        print(linha)


def projetos_em_execucao():
    conexao = sqlite3.connect("empresa.db")
    cursor = conexao.cursor()
    resultado = cursor.execute(
        """
        SELECT
            p.nome,
            p.descricao,
            p.custo,
            p.data_inicio,
            p.data_conclusao,
            f.nome
        FROM projetos p
        INNER JOIN funcionarios f
            ON f.id = p.funcionario_id
        WHERE p.status = 'execução';
        """
    )
    for linha in resultado:
        print(linha)


if __name__ == "__main__":
    criar_tabelas()
    popular_tabelas()
