import random

while True:
  try:
    dice_amount = int(input('Quantos dados deseja rolar?: '))
    rolls = []
    
    for i in range(dice_amount):
      rolls.append(random.randint(1, 6))
    
    print(f"Resultados: {rolls}")
    break
  except ValueError:
    print('Insira um número válido')
    continue