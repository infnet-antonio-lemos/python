password = input('Insira uma senha: ')

has_six_characters = len(password) >= 6
has_upper = False
has_numeric = False
for char in password:
  if (char.isupper()):
    has_upper = True
  if (char.isnumeric()):
    has_numeric = True

if (has_six_characters and has_upper and has_numeric):
  print('Senha forte!')
else:
  print('Senha fraca!')
  if (not has_six_characters):
    print('Insira pelo menos 6 caracteres')
  if (not has_upper):
    print('Insira pelo menos uma letra maiúscula')
  if (not has_numeric):
    print('Insira pelo menos um número')
  