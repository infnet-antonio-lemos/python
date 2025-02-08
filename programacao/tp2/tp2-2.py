try:
  number = int(input('Insira um número inteiro: '))
  odd_count = 0
  for i in range(number + 1):
    if (i % 2 == 1):
      odd_count += 1
  print(f'Existem {odd_count} números ímpares de 0 a {number}')
except:
  print('Falha ao converter para inteiro')