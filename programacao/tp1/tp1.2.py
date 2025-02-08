while True:
  try:     
    minutos = float(input('Insira a duração em minutos:'))
    
    horas_conversao = minutos // 60
    minutos_conversao = minutos % 60

    print(f"{horas_conversao} hora(s)")
    print(f"{minutos_conversao} minuto(s)")
    
    horas = float(input('Insira a duração em horas:'))
    minutos = float(input('Insira a duração em minutos:'))
    
    minutos_conversao = horas * 60 + minutos
    print(f"{minutos_conversao} minuto(s)")

    break
  except ValueError:
    print('Insira um número válido')
    