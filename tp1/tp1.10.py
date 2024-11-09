import random

characters = ['superhomem', 'bob esponja', 'faustão']
actions = ['brigou', 'salvou pessoas', 'apresentou o programa']
locations = ['na terra', 'em um incêndio', 'na globo']

random_character = characters[random.randint(0, len(characters) -1)]
random_action = actions[random.randint(0, len(actions) - 1)]
random_location = locations[random.randint(0, len(locations) - 1)]

print(f"O {random_character} {random_action} {random_location}")