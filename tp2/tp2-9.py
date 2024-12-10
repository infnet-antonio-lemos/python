def saudacoes(nome):
    """Função para exibir na tela uma saudação personalizada.
    
    Args:
    nome (str): Uma string representando o nome do vocativo.
    
    Returns:
    None
    """
    print(f"Olá, {nome}! Tudo bem? Vamos estudar Python!")
    
nome = input('Insira seu nome: ')
saudacoes(nome)