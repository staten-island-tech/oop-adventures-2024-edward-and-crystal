import json
with open('saves.json', 'r') as file:
  saves = json.load(file)
  
saves.clear()

with open('saves.json', 'w') as file:
  json.dump(saves, file)
  
print(saves)