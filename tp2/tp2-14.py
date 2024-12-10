def imprimir_tabuada(n = 0):
  """
  Imprime a tabuada do número fornecido de 1 até 10.
  
  Args:
  n (int): Número para mostrar a tabuada
  
  Returns:
  None
  """
  for i in range(1, 11):
    print(f'{i:<2} x {n:<2} = {i * n:<2}')
    
imprimir_tabuada(5)