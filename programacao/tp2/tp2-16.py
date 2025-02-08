questionario = []
resultado = {
  'acertos': 0,
  'erros': 0,
  'respostas': []
}

def ciar_questionario():
  """
  Função para criar o questionário com 3 perguntas e gabaritos.
  
  Args:
  None
  
  Returns:
  questionario (list): lista de dicionários contendo pergunta e gabarito
  """
  while len(questionario) < 3:
    pergunta = input('Insira a pergunta: ')
    if (pergunta == ''):
      print('Preencha com algum valor!')
      continue
    
    gabarito = input('Insira a resposta: ')
    if (gabarito == ''):
      print('Preencha com algum valor!')
      continue
    
    questionario.append({
      'pergunta': pergunta,
      'gabarito': gabarito
    })
  return questionario
    
def aplicar_prova():
  """
  Função para aplicar a prova.
  
  Argumentos:
  None
  
  Returns:
  resultado (dictionary): dicionário contendo a quantidade de acertos, erros e a folha de resposta do usuário.
  """
  for questao in questionario:
    print('Leia a pergunta e depois insira sua resposta')
    print(questao['pergunta'])
    resposta = input('Insira sua resposta: ')
    resultado['respostas'].append(questao | {'resposta': resposta})
  return calcular_resultado()
    
def calcular_resultado():
  """
  Função para calcular a quantidade de acertos e erros da prova.
  
  Args:
  None
  
  Returns:
  resultado (dictionary): dicionário contendo a quantidade de acertos, erros e a folha de resposta do usuário.
  """
  for resposta in resultado['respostas']:
    if resposta['gabarito'] == resposta['resposta']:
      resultado['acertos'] += 1
    else:
      resultado['erros'] += 1
  return resultado

def exibir_resultado():
  """
  Função para exibir o resultado de forma mais amigável no console
  
  Args:
  None
  
  Returns: 
  None
  """
  for questao in resultado['respostas']:
    print(f"Pergunta: {questao['pergunta']}")
    print(f"Resposta: {questao['resposta']}")
    print(f"Gabarito: {questao['gabarito']}")
    print(f"Resultado: {'Correto' if questao['resposta'] == questao['gabarito'] else 'Incorreto'}")
    print()
  print(f"Acertos: {resultado['acertos']}")
  print(f"Erros: {resultado['erros']}")
      
ciar_questionario()
aplicar_prova()
exibir_resultado()