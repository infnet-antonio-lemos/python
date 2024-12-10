try:
  number = int(input('Insira um número: '))
  
  for i in range(number, -1, -1):
    print(i)
except:
  print('Número inválido')