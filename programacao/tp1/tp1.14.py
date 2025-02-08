continuar = True

votes = {
  'a': 0,
  'b': 0,
  'c': 0
}

while continuar:
  opcao = input('Escolha uma opção: A, B ou C: ')
  
  match opcao.lower():
    case 'a':
      votes['a'] = votes['a'] + 1
    case 'b':
      votes['b'] = votes['b'] + 1
    case 'c':
      votes['c'] = votes['c'] + 1
    case _:
      print('Opção inválida, insira A, B ou C')
      continue
    
  continuar = input('Deseja continuar? (1 - Sim, Outro valor - Não)') == '1'
  
print("Votação")
print(f"A: {votes['a']}")
print(f"B: {votes['b']}")
print(f"C: {votes['c']}")
  