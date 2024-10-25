


class Weapon:
  
    def __init__(self, strength, gold, durability):
        self.strength = strength
        self.gold = gold
        self.durability = durability

    def attack(self):
        return f"{self.name} deals {self.strength} damage."
    
print(Weapon('Wooden Sword').strength)

#create new instances of weapon, add stuff into dicts into attrbiutes

wooden_sword = Weapon(10, 0, 1000)
bad_club = Weapon(12, 20, 10)
slime_fist = Weapon(15, 45, 25)
good_club = Weapon(20, 60, 18)
grifter_staff = Weapon(1000, 100000, 1)
golden_sword = Weapon(35, 120, 6)


