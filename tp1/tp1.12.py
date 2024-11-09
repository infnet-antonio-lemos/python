while True:
  palavra = input('Insira qualquer palavra (mas somente uma): ')

  if len(palavra.split(' ')) > 1:
    print('Insira somente uma palavra')
    continue
  
  if len(palavra) < 5:
    print('Palavra curta')
    break
  print('Palavra longa')
  break