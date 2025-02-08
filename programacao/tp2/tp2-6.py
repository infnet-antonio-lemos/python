sum = 0
count = 0
average = 0
while True:
  try:
    number = int(input('Insira um número: '))
    
    if number < 0:
      if (count != 0):
        average = sum / count
        print(f'Média: {average}')
      else:
        print(f'Média: {average}')
      break
    
    sum += number
    count += 1
  except ValueError:
    print('Número inválido')
    continue