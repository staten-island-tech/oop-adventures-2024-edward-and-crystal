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

    def CharacterDamageCalc(self):
        damage = self.strength + self.weapon['strength']
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
       if selectedenemy.currenthp > 0:
           print(f"{selectedenemy.name} now has {selectedenemy.currenthp} health!")
           selectedenemy.dead = True
       else:
           print(f"{selectedenemy.name} has died.")

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

    def EnemyHit(self, player):
       print(f"{self.name} attacks {player.name}!")
       damage = super().CharacterDamageCalc()
       player.currenthp -= damage
       if player.currenthp > 0:
           print(f"{player.name} lost {damage} HP, and now has {player.currenthp} HP!")
       elif player.currenthp == 0:
           print(f"{player.name} has died.")
           player.dead = True

    
class BattleInteractions(MainCharacter, Enemy):
    def DamageCalc(attacker, defender):
        damage = attacker.strength + attacker.weapon['strength']

    def Battles(player, enemies):
        while len(enemies) > 0:
            player.MainCharacterAttack(enemies)

            for enemy in enemies:
                if enemy.currenthp <= 0:
                    enemy.dead = True
                if enemy.dead is True:
                    enemies.remove(enemy)

            for enemy in enemies:
                enemy.EnemyHit(player)
                print(player.currenthp)
                if player.currenthp <= 0:
                    enemies.clear()
                    break



                    
player = MainCharacter('player', 100, 100, 10, {'strength': 100}, [], 0)
goblin = Enemy('goblin', 10, 10, 10, {'strength': 20}, 10, 'gobbysword')
goblin2 = Enemy('goblin2', 10, 10, 10, {'strength': 20}, 10, 'gobbysword')
goblin3 = Enemy('goblin3', 10, 10, 10, {'strength': 20}, 10, 'gobbysword')
goblin4 = Enemy('goblin4', 10, 10, 10, {'strength': 20}, 10, 'gobbysword')

enemies = [goblin, goblin2, goblin3, goblin4]

BattleInteractions.Battles(player, enemies)
#:LALAALALLALALALAL IT WORKS !!!!!!!! no it doesnt