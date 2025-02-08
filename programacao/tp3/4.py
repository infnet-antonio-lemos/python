def substitui_str(string: str, ocorrencia: str, substituicao: str):
    return string.replace(ocorrencia, substituicao)


print(substitui_str("teste", "t", "b"))
