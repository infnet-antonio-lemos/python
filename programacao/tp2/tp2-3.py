try:
  numero = int(input('Insira um número inteiro: '))
  soma = 0
  for i in range(numero + 1):
    if (i % 2 == 0):
      soma += i
  print(f'Soma dos números pares de 0 a {numero}: {soma}')
except:
  print('Insira um número válido')