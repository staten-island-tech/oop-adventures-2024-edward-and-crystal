import json


with open('enemies.json', 'r') as file:
    sup = json.load(file)


sup.remove("hi")
    
with open('enemies.json', 'w') as file:
    json.dump(sup, file, indent = 2)