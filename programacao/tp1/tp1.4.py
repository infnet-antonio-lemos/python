while True:
  try:
    operacao = int(input('Selecione uma operação: 1 - Adição 2- Subtração 3 - Multiplicação 4 - Divisão: '))
    num1 = int(input('Insira o primeiro número: '))
    num2 = int(input('Insira o segundo número: '))
    
    match operacao:
      case 1:
        print(f"Soma: {num1} + {num2} = {num1 + num2}")
      case 2:
        print(f"Subtração: {num1} - {num2} = {num1 - num2}")
      case 3:
        print(f"Multiplicação: {num1} * {num2} = {num1 * num2}")
      case 4:
        print(f"Divisão: {num1} / {num2} = {num1 / num2}")
      case _:
        print('Operação inválida, insira um número inteiro de 1 a 4')
        continue
    break
    
  except ValueError:
    print('insira um número válido')
    continue
  
  except ZeroDivisionError:
    print('Divisão por zero, tente novamente')