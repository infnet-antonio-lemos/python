try:
  numero = int(input('Insira um número inteiro: '))
  i = 0
  while (i <= numero):
    print(i)
    i+=1
except ValueError:
  print('Insira um número válido!')