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
