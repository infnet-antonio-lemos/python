def fibonacci():
    """
    Função para calcular uma série de 10 elementos de fibonacci
    
    Args:
    None
    
    Returns:
    fibonacci (list): uma lista contendo 10 elementos de fibonacci
    """
    serie = [0, 1]
    for i in range(8):
        serie.append(serie[i] + serie[i + 1])
    print(len(serie))
    return serie
    
print(fibonacci())