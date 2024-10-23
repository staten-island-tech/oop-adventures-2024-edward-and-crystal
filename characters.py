import json

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

    
class BattleInteractions(Character):
    def DamageCalc(attacker, defender):
        damage = attacker.strength + attacker.weapon['strength']

    def CharacterAttack(attacker, defender):
        damage = BattleInteractions.DamageCalc(attacker, defender)
        newdefenderhealth = defender.health - damage

        if newdefenderhealth <= 0:
            defender.dead = True
            defender.CharacterDeathMessage()
            return newdefenderhealth

        else:
            return newdefenderhealth

    def PlayerAttack(player, enemies):
        enemysearch = input("Who would you like to attack? ")
        done = False

        while done == False:
            for enemy in enemies:
                if enemysearch in enemy.name:
                    confirm = input(f"Would you like to attack {enemy.name}? ")
                    if confirm.upper == "YES":
                        enemyhealth = BattleInteractions.CharacterAttack(player, enemy)
                        print(f"{player.name} attacks {enemy.name}, and {enemy.name} now has {enemyhealth}.")
                        done = True
    
    def EnemyAttack(enemy, player):
        newdefenderhealth = BattleInteractions.CharacterAttack(enemy, player)
        print(f"{enemy.name} attacks you. You now have {newdefenderhealth}.")

    def Battles(player, enemies):


    
player = MainCharacter('player', 10, 10, 100, {'strength': 100}, [], 0)
goblin = Enemy('goblin', 10, 10, 10, {'gobsword': 100}, 10, 'gobbysword')

BattleInteractions.DamageCalc(player, goblin)
