while True:
  try:
    massa = float(input('Insira sua massa em kgs: '))
    altura = float(input('Insira sua altura em metros: '))
    
    imc = massa / altura ** 2
    
    if imc < 18.8:
      print('Abaixo do peso')
      break
    if imc > 25:
      print('Acima do peso')
      break
    print('Peso normal')
    break
  except ValueError:
    print('Insira um número válido')
    continue