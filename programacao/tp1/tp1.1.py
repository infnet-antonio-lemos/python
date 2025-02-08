while True:
  try:     
    first_number = float(input('Insira o primeiro número:'))
    second_number = float(input('Insira o segundo número:'))

    soma = first_number + second_number
    subtracao = first_number - second_number
    multiplicacao = first_number * second_number
    divisao = first_number / second_number
    divisao_inteira = first_number // second_number

    print(soma)
    print(subtracao)
    print(multiplicacao)
    print(divisao)
    print(divisao_inteira)
    break
  except ValueError:
    print('Insira um número válido')
    