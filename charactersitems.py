import json

class Weapon:
    def __init__(self, name, strength, durability, cost):
        self.name = name
        self.strength = strength
        self.durability = durability
        self.cost = cost

    def WeaponDictionary(self):
        return {
            'name': self.name,
            'strength': self.strength,
            'durability': self.durability,
            'cost': self.cost
        }
    
class OtherStuff():
    def __init__(self, name):
        self.name = name

class HealingItem:
    def __init__(self, name, heal, cost):
        self.name = name
        self.heal = heal
        self.cost = cost
    
    def HealingItemDictionary(self):
        return {
            'name': self.name,
            'heal': self.heal,
            'cost': self.cost
            }

    def UseHealingItem(self, player):
        healingamount = self.heal
        player.currenthp += healingamount

class Character:
    def __init__(self, name, maxhp, currenthp, strength, weapon):
        self.name = name
        self.maxhp = maxhp
        self.currenthp = currenthp 
        self.strength = strength
        self.weapon = weapon
        self.dead = False

    def CharacterDeathMessage(self):
        print(f"{self.name} has DIED.")

    def CharacterDamageCalc(self):
        damage = self.strength + self.weapon.strength
        return damage

class MainCharacter(Character):
    def __init__(self, name, maxhp, currenthp, strength, weapon, inventory, gold):
        super().__init__(name, maxhp, currenthp, strength, weapon)
        self.inventory = list(inventory)
        self.gold = gold

    def PlayerTakeDamage(self):
            super().CharacterTakeDamage()
            self.CharacterDeathMessage()
  
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
 
    def PlayerEquipWeapon(self, weapon):
        self.weapon = weapon
        
    def CharacterDeathMessage(self):
        print(f"{self.name} has DIED.")

    def MainCharacterChooseEnemy(self, enemies):
        selectedenemies = []
        found = False
        for enemy in enemies:
                print(f"{enemy.name} ) {enemy.currenthp} HP")
        while found == False:
           request = input("Who would you like to attack? ")
           for enemy in enemies:
               if request.upper() in enemy.name.upper():
                   selectedenemies.append(enemy)
                   found = True

        functiondone = False

        if len(selectedenemies) == 1:
            return selectedenemies[0]
        else:
            while functiondone == False:
               theenemy = 0
               for request in selectedenemies:
                   confirmchoice = input(f"Do you want to attack the {selectedenemies[theenemy].name}? ")
                   if confirmchoice.upper() == "YES":
                       functiondone = True
                       return selectedenemies[theenemy]
                   else:
                       theenemy += 1
  
    def MainCharacterAttack(self, enemies):
       selectedenemy = self.MainCharacterChooseEnemy(enemies)
       print(f"{self.name} attacks {selectedenemy.name}!")
       damage = super().CharacterDamageCalc()
       selectedenemy.currenthp -= damage
       self.weapon.durability -= 1


class Enemy(Character):
    def __init__(self, name, maxhp, currenthp, strength, weapon, golddrop, weapondrop):
        super().__init__(name, maxhp, currenthp, strength, weapon)
        self.golddrop = golddrop
        self.weapondrop = weapondrop

    def EnemyTakeDamage(self, damage):
        self.currenthp -= damage
        if self.currenthp < 0:
            self.dead = True
            self.currenthp = 0
            self.EnemyDie(self)
    
    def EnemyDie(self):
        self.EnemyDeathMessage(self)
        self.gold += self.golddrop
        self.inventory.append(self.weapondrop)

    def EnemyHeal(self, heal):
        self.currenthp += heal
        if self.currenthp >= self.maxhp:
            self.currenthp = self.maxhp
            print(f"{self.name} has restored to full health!")

    def EnemyDealDamage(self, player):
        weaponstrength = self.weapon['strength']
        damage = self.strength + weaponstrength
        player.health -= damage

    def EnemyHit(self, player):
        print(f"{self.name} attacks {player.name}!")
        damage = super().CharacterDamageCalc()
        player.currenthp -= damage

class BossEnemy(Character):
    def __init__(self, name, maxhp, currenthp, strength, weapon):
        super().__init__(name, maxhp, currenthp, strength, weapon)

    def EnemyHit(self, player):
        print(f"{self.name} attacks {player.name}!")
        damage = super().CharacterDamageCalc()
        player.currenthp -= damage

    def EnemyHeal(self, heal):
        self.currenthp += heal
        if self.currenthp >= self.maxhp:
            self.currenthp = self.maxhp
            print(f"{self.name} has restored to full health!")
    
    def EnemySummon(self, enemies):
        woodclub = Weapon('woodclub', 10, 10, 10)
        summonable = Enemy("Summoned Orc", 20, 15, 10, woodclub, 0, 'nothing')
        enemies.append(summonable)
        print(f"{self.name} has summoned a {summonable.name}! ")

    def MAKELIFEHELL(self, enemies):
        woodclub = Weapon('woodclub', 10, 10, 10)
        summonable = BossEnemy("Summoned Boss", 100, 50, 20, woodclub, 0, 'nothing')
        enemies.append(summonable)
        print(f"{self.name} has summoned a {summonable.name}! Good Luck!!! ")

woodclub = Weapon('woodclub', 10, 10, 10)
enemies = [ ]
boss = BossEnemy('a', 1, 1, 1, woodclub)