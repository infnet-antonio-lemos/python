frase = input('Insira uma palavra ou frase: ')

frase_normalizada = frase.lower().replace(' ', '')
reverso_normalizado = frase_normalizada[::-1]

if frase_normalizada == reverso_normalizado:
  print('É um palíndromo!')
else:
  print('Não é um palíndromo :(')