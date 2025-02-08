while True:
  try:
    idade = float(input('Insira sua idade: '))
    
    if idade < 0:
      print('Como assim você tem idade negativa? Digita de novo')
      continue
    if idade >= 18:
      print('Você já é maior de idade')
      break
    print('Você ainda não é maior de idade')
    break
  except ValueError:
    print('Insira um número válido')
    continue