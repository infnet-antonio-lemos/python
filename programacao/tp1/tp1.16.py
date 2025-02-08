while True:
  try:
    number = float(input('Insira um número: '))
    if number % 2 == 0:
      print('O número fornecido é par')
      break
    print('O número fornecido é ímpar');
    break
  except ValueError:
    print('Insira um número válido')
    continue