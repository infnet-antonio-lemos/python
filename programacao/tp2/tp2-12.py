def contar_palavras(frase = ''):
  """
  Conta a quantidade de palavras de uma frase.
  
  Args:
  frase (str): String representando a frase
  
  Returns:
  count (int): A quantidade de palavras
  """
  return len(frase.strip().split(' '))

frase = input('Insira uma frase: ')
print(f'Quantidade de palavras: {contar_palavras(frase)}')