story_tree = [{
  'name': 'era uma vez',
  'children': [
    {
      'name': 'um rato em seu esconderijo secreto',
      'children': [
        {
          'name': 'certo dia o rato decidiu mudar sua vida'
        },
        {
          'name': 'acomodado com a vida, ele decidiu continuar por alí'
        }
      ]
    },
    {
      'name': 'um pássaro que sobrevoava a cidade',
      'children': [
        {
          'name': 'um belo dia ele avistou uma bela e grandiosa ave',
          'children': [
            {
              'name': 'se apaixonaram e viveram felizes para sempre',
            },
            {
              'name': 'infelizmente era um grande gavião que o devorou sem piedade'
            }
          ]
        }
      ]
    }
  ]
}]

current = story_tree
options = list(map(lambda x: x['name'], current))

story = []

while True:
  try:
    for i, value in enumerate(options):
      print(f"{i}: {value}")
    index = int(input('Escolha uma opção: '))
  
    if index >= len(options) or index < 0:
      print('Valor inválido, insira um número apresentado nas opções')
      continue
    
    story.append(current[index]['name'])
    
    if current[index].get('children') == None:
      print('Fim da história')
      break
    current = current[index]['children']
    options = list(map(lambda x: x['name'], current))
  except ValueError:
    print('Insira uma opção válida')
    continue

print(story)