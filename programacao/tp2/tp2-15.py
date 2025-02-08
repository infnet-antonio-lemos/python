contatos = []

def print_row(col1, col2):
  print(f'{col1:<15} {col2:<15}')
def mostrar_contatos():
  print_row('Nome', 'Telefone')
  for contato in contatos:
    print_row(contato['nome'], contato['numero'])
  

for i in range(5):
  nome = input('Insira o nome do contato: ')
  numero = input('Insira o número do contato: ')
  
  contato = {
    'nome': nome,
    'numero': numero
  }
  contatos.append(contato)

mostrar_contatos()