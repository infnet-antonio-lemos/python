def calcular_media(nota1, nota2, nota3):
    """Função para calcular a média das duas maiores notas

    Args:
    nota1 (int or float): valor numérico da nota1
    nota2 (int or float): valor numérico da nota2
    nota3 (int or float): valor numérico da nota3

    Returns:
    media (float): valor numérico da média das duas maiores notas
    """
    notas = [nota1, nota2, nota3]
    notas.sort()
    average = (notas[1] + notas[2]) / 2
    return average

try:
    nota1 = float(input('Insira a nota 1: '))
    nota2 = float(input('Insira a nota 2: '))
    nota3 = float(input('Insira a nota 3: '))
    
    print(calcular_media(nota1, nota2, nota3))
except ValueError:
    print('Insira um número válido')