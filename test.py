import json
from charactersitems import MainCharacter

player = MainCharacter('j', 20, 20, 6,  {
      "name": "NONE",
      "strength": 0,
      "durability": 8192,
      "cost": 0
    },
    
        {"name": "Goblin Club",
        "strength": 6,
        "durability": 10,
        "cost": 6
      }, 0, 0, 0)


print(player.__dict__)