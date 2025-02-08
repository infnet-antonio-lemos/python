def soma_dos_digitos(numero: int):
    soma = 0
    for digit in str(numero):
        soma += int(digit)
    return soma


print(soma_dos_digitos(32))
