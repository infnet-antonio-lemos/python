from datetime import datetime

tarefas = []
urgencias = ['baixa', 'media', 'alta']
sequential_id = 1

def adicionar_tarefa(descricao, prazo_final, urgencia):
  """
  Adiciona uma nova tarefa à lista de tarefas, fazendo validação do prazo final e da urgência.
  
  Args:
  descricao (str): Descrição da tarefa
  prazo_final (str): Data limite para conclusão da tarefa no formato "YYYY-MM-DD"
  urgencia (str): Urgência da tarefa (baixa, media, alta).
  
  Returns:
  tarefa (dictionary): É retornado o dicionário referente à tarefa inserida.
  
  Exceptions:
  ValueError: Exception lançada quando o formato do prazo_final é inválido.
  """
  try:
    prazo_final_date = datetime.strptime(prazo_final, "%Y-%m-%d")
    if urgencia not in urgencias:
      print(f"Valor inválido para urgência. Insira um dos seguintes valores: {(', ').join(urgencias)}")
      return
    if descricao == '':
      print("Preencha a descrição da tarefa!")
      return
    
    global sequential_id
    tarefa = {
      'id': sequential_id,
      'descricao': descricao,
      'data_criacao': datetime.now(),
      'prazo_final': prazo_final_date,
      'urgencia': urgencia,
      'concluido': False
    }
    sequential_id += 1
    tarefas.append(tarefa)
    print('Tarefa inserida!')
    return tarefa
  except ValueError:
    print('Formato de data inválido!')
    return
  
def listar_tarefas():
  """
  Lista todas as tarefas cadastradas
  
  Args:
  None
  
  Returns:
  None: Não retorna nada, apenas imprime os valores no console.
  """
  def print_row(col1, col2, col3, col4, col5, col6):
    print(f'{col1:<5} {col2:<25} {col3:<16} {col4:<16} {col5:<10} {col6:<9}')
  print('Tarefas cadastradas: ')
  print_row('ID','Descrição','Data de Criação','Prazo Final','Urgência', 'Concluída')
  for tarefa in tarefas:
    data_criacao = tarefa['data_criacao'].strftime('%Y-%m-%d')
    prazo_final = tarefa['prazo_final'].strftime('%Y-%m-%d')
    print_row(
      tarefa['id'], 
      tarefa['descricao'], 
      data_criacao, 
      prazo_final, 
      tarefa['urgencia'], 
      'Sim' if tarefa['concluido'] else 'Não')

def concluir_tarefa(id):
  """
  Marca uma tarefa como concluída ('concluido' = True) baseado no id fornecido.
  
  Args:
  id (int or str): O ID da tarefa a ser marcada como concluída
  
  Returns:
  None
  
  Exceptions:
  ValueError: Caso o ID fornecido não seja convertível para inteiro.
  """
  try:
    number_id = int(id)
    for tarefa in tarefas:
      if tarefa['id'] == number_id:
        tarefa['concluido'] = True
        print('Tarefa concluída!')
        return tarefa
    print('Tarefa não encontrada.')
    return
  except ValueError:
    print('ID inválido')

def remover_tarefa(id):
  """
  Remover uma tarefa baseado no id fornecido.
  
  Args:
  id (int or str): O ID da tarefa a ser removida
  
  Returns:
  None
  
  Exceptions:
  ValueError: Caso o ID fornecido não seja convertível para inteiro.
  """
  try:
    number_id = int(id)
    for index, tarefa in enumerate(tarefas):
      if tarefa['id'] == number_id:
        tarefas.pop(index)
        print('Tarefa removida')
        return
    print('Tarefa não encontrada!')
  except ValueError:
    print('ID inválido!')
    

print('Bem-vindo ao seu gerenciador de tarefas')
while True:
  print('--------------')
  print('1 - Adicionar Tarefa')
  print('2 - Listar Tarefas')
  print('3 - Marcar Tarefa como concluída')
  print('4 - Remover Tarefa')
  print('5 - Sair')
  escolha = input('Escolha uma opção: ')
  match escolha:
    case '1':
      descricao = input('Descrição da tarefa: ')
      prazo_final = input('Insira o prazo final da sua tarefa (YYYY-MM-DD): ')
      urgencia = input(f'Insira a urgência da sua tarefa({urgencias}): ')
      tarefa = {
        'id': id,
        'descricao': descricao,
        'prazo_final': prazo_final,
        'urgencia': urgencia,
        'data_criacao': datetime.now(),
        'concluida': False
      }
      print(adicionar_tarefa(descricao, prazo_final, urgencia))
    case '2':
      listar_tarefas()
    case '3':
      id = input('Insira o ID da tarefa que deseja marcar como concluída: ')
      print(concluir_tarefa(id))
    case '4':
      id = input('Insira o ID da tarefa que deseja remover: ')
      remover_tarefa(id)
    case '5':
      break
    case _:
      print('Insira um valor válido (1, 2, 3, 4 ou 5)')
      
