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

    def PlayerOpenShop(self):
        print('shop')

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
       self.weapon['durability']
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

class Menu(Weapon, HealingItem):
    def Inventory(player):
        inventory = list(player.inventory)
        finish = False
        for item in inventory:
            print(item.name)
        x = 0
        while finish == False:
            selecteditem = inventory[x]
            print(f"You are currently hovering over the {selecteditem.name}.")
            confirm = input("Would you like to select this item?")
            if confirm.upper() == "YES":
                try: # basically an ifelse statement, tries to see if its a weapon and if it isnt it's gotta be a healing item unless something happened
                    print(selecteditem.name)
                    print(selecteditem.strength)
                    print(selecteditem.durability)
                    equip = input("Would you like to equip this item? ")
                    if equip.upper() == "YES":
                        player.weapon = selecteditem
                        print(f"You have equipped the {selecteditem.name}. ")
                        finish = True
                except ValueError:
                    print(selecteditem.name)
                    print(selecteditem.heal)
                    use = input("Would you like to use this item? ")
                    if use.upper() == "YES":
                        player.PlayerHeal(selecteditem['heal'])
                        player.inventory.remove(selecteditem)
                        print(f"You have used the {selecteditem.name}. ")
                        finish = True
            
                move = input("Press Z to move up the menu and X to move down the menu. ")
    
                if move.upper() == "Z":
                    if x != 0:
                        x -= 1
                    else:
                        x = len(inventory) - 1
                elif move.upper() == "X":
                    if x != len(inventory) - 1:
                        x += 1
                    else:
                        x = 0
                else:
                    print("That is not a valid input.")


    
class BattleInteractions(MainCharacter, Enemy):

    def Battles(player, enemies):
        import random
        players = []
        players.append(player)
        previousinputs = ['nothing.']
        while len(enemies) != 0 and len(players) > 0:
            blockorattack = input("Would you like to block or attack? ")
            if blockorattack.upper() == "ATTACK":
                player.MainCharacterAttack(enemies)
                previousinputs.clear()
                previousinputs.append("ATTACK")
                for enemy in enemies:
                    if enemy.currenthp <= 0:
                        enemy.dead = True
                    if enemy.dead is True:
                        enemies.remove(enemy)

                for enemy in enemies:
                    healorattack = random.randint(1,2)
                    if healorattack == 1:
                        enemy.EnemyHeal(5)
                    if healorattack == 2:
                        enemy.EnemyHit(player)

                    if player.currenthp <= 0:
                        enemies.clear()
                        try:
                            players.remove(player)
                            player.CharacterDeathMessage()
                        except ValueError:
                            pass
            
            elif blockorattack.upper() == "BLOCK":
                if previousinputs[0] == "BLOCK":
                    print("Your block has failed. Literally every video game does this. Do better. ")
                    for enemy in enemies:
                        enemy.EnemyHit(player)
                    if player.currenthp <= 0:
                        enemies.clear()
                        try:
                            players.remove(player)
                            player.CharacterDeathMessage()
                        except ValueError:
                            pass
                else:
                    player.PlayerHeal(15)
                    print(f"Blocking has allowed you to regain some stamina. You now have {player.currenthp} health.")
                    for enemy in enemies:
                        healorattack = random.randint(1,2)
                        if healorattack == 1:
                            print(f"{enemy.name} attempted to strike, but the attack was blocked!")
                        else:
                            enemy.EnemyHeal(5)
                    previousinputs.clear()
                    previousinputs.append("BLOCK")


woodsword = Weapon('woodsword', 10, 10, 10)
woodclub = Weapon('woodsword', 15, 5, 5)
apple = HealingItem('apple', 5, 5)
woodsword.WeaponDictionary()
woodclub.WeaponDictionary()
apple.HealingItemDictionary()

inventory = [woodsword, woodclub, apple]

player = MainCharacter('player', 100, 100, 10, woodsword, inventory, 0)

Menu.Inventory(player)


#:LALAALALLALALALAL IT WORKS !!!!!!!! no it doesnt