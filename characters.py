import json

class Character:
    def __init__(self, name, maxhp, currenthp, strength, weapon):
        self.name = name
        self.maxhp = maxhp
        self.currenthp = currenthp 
        self.strength = strength
        self.weapon = weapon
        self.dead = False

class MainCharacter(Character):
    def __init__(self, name, maxhp, currenthp, strength, weapon, inventory, gold):
        super().__init__(name, maxhp, currenthp, strength, weapon)
        self.inventory = list(inventory)
        self.gold = gold
    
    def PlayerDeadMessage(self):
        print(f"{self.name} has DIED.")

    def CharacterTakeDamage(self, damage):
        self.currenthp -= damage
        if self.currenthp < 0:
            self.currenthp = 0
            self.dead = True
            self.PlayerTakeDamage
  
    def PlayerHeal(self, heal):
        self.currenthp += heal
        if self.currenthp > self.maxhp:
            self.currenthp = self.maxhp   

    def PlayerGainGold(self, newgold):
        self.gold += newgold
    
    def PlayerPurchaseItem(self, cost, item):
        self.gold -= cost
        self.inventory.append(item)

    def PlayerGetItem(self, item):
        self.inventory.append(item)

    def PlayerSellsItem(self, value, item):
        self.gold += value
        self.inventory.remove(item)

    def PlayerDamageCalc(self, weaponstrength):
        damage = self.strength + weaponstrength
        return damage
    
    def PlayerHit(self):
        weaponstrength = player.weapon['strength']
        damage = self.PlayerDamageCalc(weaponstrength)
        return damage

    def PlayerEquipWeapon(self, weapon):
        player.weapon = weapon

    def PlayerSaveFileReady(self):
        return {
            'name': self.name,
            'strength': self.strength,
            'maxhp': self.maxhp,
            'currenthp': self.currenthp,
            'gold': self.gold,
            'inventory': self.inventory
        }

    def PlayerCreateSave(self):
        savefile = self.PlayerSaveFileReady()
        with open('charactersave.json', 'w') as file:
            json.dump(savefile, file)

    def PlayerLoadSave(self): 
        with open('charactersave.json', 'r') as file:
            sf = json.load(file)
            # sf is short for savefile
        player = MainCharacter(sf['name'], sf['strength'], sf['maxhp'], sf['currenthp'], sf['gold'], sf['inventory'])
        return player      

class Enemy(Character):
    def __init__(self, name, maxhp, currenthp, strength, weapon, dead, golddrop, weapondrop):
        super().__init__(name, maxhp, currenthp, strength, weapon, dead)
        self.golddrop = golddrop
        self.weapondrop = weapondrop
    
    def EnemyDeathMessage(self, player):
        print(f"{self.name} has been killed by {player}")

    def EnemyTakeDamage(self, damage):
        self.currenthp -= damage
        if self.currenthp < 0:
            self.dead = True
            self.currenthp = 0
            self.EnemyDie(self)
    
    def EnemyDie(self):
        self.EnemyDeathMessage(player.name)
        player.gold += self.golddrop
        player.inventory.append(self.weapondrop)

    def EnemyHeal(self, heal):
        self.currenthp += heal
        if self.currenthp >= self.maxhp:
            self.currenthp = self.maxhp
            print(f"{self.name} has restored to full health!")

    def EnemyDealDamage(self, player):
        weaponstrength = self.weapon['strength']
        damage = self.strength + weaponstrength
        player.health -= damage


player = MainCharacter('name', 1, 1, 1, )



"""Player Character:
‘id’ : 1
‘name’ : “playerperson”
‘maxhp’: 75
‘currenthp’: 75 (will change)
‘strength’: 5
‘gold’: 0 (will change)
‘inventory’: [list of dictionaries with different items]
sample item dictionary, all the items are weapons to simplify things

‘Name’: wooden sword
‘damage’: 10

Enemy Characters:

‘id’ : 2
‘name’ : “slime”
‘maxhp’: 20
‘currenthp’: 20 (will change)
‘strength’: 5
‘golddrop’: 10
‘weapondrop’ : “nothing”

"""
