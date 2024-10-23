from characters import MainCharacter
'''wooden sword
10 strength
infinite durability (probably like 1024, just to make sure it doesnt break leaving the player no weapon)

bad club
12 strength
do we put durability? idk maybe its hard to code: but 10 durability if yes
durability could be implemented in a conditional statement. if weapon is used, -1 durability? if durability = 0, remove weapon from inventory

slime fist
15 strength
potential durability: 25

good club
20 strength
potential durability: 18

grifter staff
1000 strength
potential durability: 1

pretty solid sword
15 strength
potential durability: 20
cost: 40 gold

golden sword (like from minecraft)
35 strength
potential durability: 6
cost: 120 gold
'''

class Item:
    def __init__(self, name, strength, durability, cost):
        self.name = name
        self.strength = strength
        self.durability = durability
        self.cost = cost

    def weapon_broken(self):
        if self.durability == 0:
            Character.inventory.remove(self.name)
            print(f'Your {self.name} has broken! You can no longer use it')
    
    
class WoodenSword(Item):
    def __init__(self):
        super().__init__(name='Wooden Sword', strength=10, durability=1024, cost='cannot buy')
    
    


