import random

random_number = random.randint(1, 200)
user_choice = None

while (user_choice != random_number):
  try:
    user_choice = int(input('Advinhe o número secreto (inteiro de 1 a 200): '))
    if user_choice < random_number:
      print('Muito baixo')
      continue
    if user_choice > random_number:
      print('Muito alto')
      continue
    break
  except ValueError:
    print('Insira um número válido')
    continue
print('Acertou!')