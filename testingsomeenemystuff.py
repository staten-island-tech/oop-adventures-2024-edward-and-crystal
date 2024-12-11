import json

with open('enemies.json', 'r') as file:
    enemies = json.load(file)
    
for enemy in enemies:
    try:
        print(enemy['weapondrop'])
    except KeyError:
        print(enemy['name'])