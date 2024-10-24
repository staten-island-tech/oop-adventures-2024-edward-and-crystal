
'''wooden sword
10 strength
infinite durability (probably like 1024, just to make sure it doesnt break leaving the player no weapon)

bad club
12 strength
do we put durability? idk maybe its hard to code: but 10 durability if yes

slime fist
15 strength
potential durability: 25
gold 45

good club
20 strength
potential durability: 18

grifter staff
1000 strength
potential durability: 1

golden sword (like from minecraft)
35 strength
potential durability: 6
cost: 120 gold
'''

class Weapon:
  
    def __init__(self, name):
        self.name = name
        self.strength = Weapon.strength[name]
        self.gold = Weapon.gold[name]
        self.durability = Weapon.durability[name]

    def attack(self):
        return f"{self.name} deals {self.strength} damage."
    
print(Weapon('Wooden Sword').strength)

#create new instances of weapon, add stuff into dicts into attrbiutes

Wooden
  strength = {
        'Wooden Sword': 10,
        'Bad Club': 12,
        'Slime Fist': 15,
        'Good Club': 20,
        'Grifter Staff': 1000,
        'Golden Sword': 35
    }
    durability = {
        'Wooden Sword': 10000,
        'Bad Club': 10,
        'Slime Fist': 25,
        'Good Club': 18,
        'Grifter Staff': 1,
        'Golden Sword': 6
    }
    
    gold = {
        'Wooden Sword': 0,
        'Bad Club': 20,
        'Slime Fist': 45,
        'Good Club': 60,
        'Grifter Staff': 1000000000,
        'Golden Sword': 120
    }

