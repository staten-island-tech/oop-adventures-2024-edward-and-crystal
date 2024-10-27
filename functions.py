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
        summonable = Enemy("Summoned Orc", 20, 15, 10, woodclub, 0, 'nothing')
        enemies.append(summonable)
        print(f"{self.name} has summoned a {summonable.name}! ")

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
                if isinstance(selecteditem, Weapon):
                    print(f"name) {selecteditem.name})")
                    print(f"strength) {selecteditem.strength}")
                    if selecteditem.durability > 500: # nobody is swinging their sword 7700 times in this game.
                        print("Infinite Durability")
                    else:
                        print(f"durability) {selecteditem.durability}")
                    equip = input("Would you like to equip this item? ")
                    if equip.upper() == "YES":
                        player.weapon = selecteditem
                        print(f"You have equipped the {selecteditem.name}. ")
                        finish = True
                elif isinstance(selecteditem, HealingItem):
                    print(f"name) {selecteditem.name}")
                    print(f"heal amount) {selecteditem.heal}")
                    use = input("Would you like to use this item? ")
                    if use.upper() == "YES":
                        print(f"You have {player.currenthp}, and use the {selecteditem.name}")
                        player.PlayerHeal(selecteditem.heal)
                        try:
                            player.inventory.remove(selecteditem)
                        except ValueError:
                            pass
                        print(player.inventory)
                        print(f"Now you have {player.currenthp} HP! ")
                        finish = True
            else:
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

    def Shop(player):
        woodensword = Weapon('Wooden Sword', 5, 8192, 10)
        stonesword = Weapon('Stone Sword', 10, 15, 18)
        goldsword = Weapon('Gold Sword', 35, 6, 20)
        apple = HealingItem('Apple', 10, 5)
        healingpotion = HealingItem('Healing Potion', 35, 15)
        endshopping = OtherStuff('End Shopping')
        shopitems = [ ]
        shopitems.append(woodensword)
        shopitems.append(stonesword)
        shopitems.append(goldsword)
        shopitems.append(apple)
        shopitems.append(healingpotion)
        shopitems.append(endshopping)
        for item in shopitems[:5]:
            print(f"{item.name} ) {item.cost} Gold")
        print(endshopping.name)
        finish = False
        x = 0
        while finish == False:
            selecteditem = shopitems[x]
            if isinstance(selecteditem, OtherStuff):
                confirm = input('Would you like to finish shopping? ')
                if confirm.upper() == "YES":
                    finish = True
            else:
                print(f"You are currently hovering over the {selecteditem.name}. ")
                confirm = input("Would you like to inspect this item? ")
                if confirm.upper() == "YES":
                    if isinstance(selecteditem, Weapon):
                        print(selecteditem.name)
                        print(f"{selecteditem.strength} Damage")
                        if selecteditem.durability > 4000:
                            print("Infinite Durability")
                        else:
                            print(f"{selecteditem.durability} Durability")
                        print(f"Costs {selecteditem.cost} Gold")
                        if selecteditem.cost > player.gold:
                            print("You cannot afford this item. ")
                        else:
                            confirmB = input("Would you like to buy this item? ")
                            if confirmB.upper() == 'YES':
                                player.gold -= selecteditem.cost
                                player.inventory.append(selecteditem)
                                print(f"You have bought the {selecteditem.name}. Now you have {player.gold} gold.")
                                keepgoing = input("Are you finished shopping? ")
                                if keepgoing.upper() == "YES":
                                    finish = True
                    elif isinstance(selecteditem, HealingItem):
                        print(selecteditem.name)
                        print(f"Heals {selecteditem.heal} HP")
                        print(f"Costs {selecteditem.cost} Gold")
                        if selecteditem.cost > player.gold:
                            print("You cannot afford this item. ")
                        else:
                            confirmB = input("Would you like to buy this item? ")
                            if confirmB.upper() == 'YES':
                                player.gold -= selecteditem.cost
                                player.inventory.append(selecteditem)
                                print(f"You have bought the {selecteditem.name}. Now you have {player.gold} gold.")
                                keepgoing = input("Are you finished shopping? ")
                                if keepgoing.upper() == "YES":
                                    finish = True
                    else:
                        finish = True
                else:
                    move = input("Press Z to move up the menu and X to move down the menu. ")
    
                    if move.upper() == "Z":
                        if x != 0:
                            x -= 1
                        else:
                            x = len(shopitems) - 1
                    elif move.upper() == "X":
                        if x != len(shopitems) - 1:
                            x += 1
                        else:
                            x = 0
                    else:
                        print("That is not a valid input.")

    
class BattleInteractions(MainCharacter, Enemy, BossEnemy):
    def Battles(player, enemies):
        import random
        players = []
        players.append(player)
        previousinputs = ['nothing.']
        while len(enemies) != 0 and len(players) > 0:
            for enemy in enemies:
                print(f"{enemy.name} ) {enemy.currenthp} HP")
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
        if len(enemies) == 0:
            print(f"You have won!!!")

    def BossBattle(player, enemies):
        import random
        previousinputs = ['nothing.']
        players = [player]
        while len(enemies) != 0 and len(players) == 1:
            for enemy in enemies:
                print(f"{enemy.name} ) {enemy.currenthp} HP")
            blockorattack = input("Would you like to block or attack? ")
            if blockorattack.upper() == "ATTACK":
                player.MainCharacterAttack(enemies)
                previousinputs.clear()
                previousinputs.append("ATTACK")
                for enemy in enemies:
                    if enemy.currenthp <= 0:
                        print(f"{enemy.name} has died!")
                        try:
                            enemies.remove(enemy)
                        except ValueError:
                            wouldyoucode = "nah, i'd make this function incredibly stupid why is my life miserable"
                for enemy in enemies:
                    if isinstance(enemy, Enemy):
                        move = random.randint(1,2)
                        if move == 1:
                            enemy.EnemyHit(player)
                        else:
                            enemy.EnemyHeal(5)
                    elif isinstance(enemy, BossEnemy):
                        move = random.randint(1,5)
                        if move == 1 or move == 2 or move == 3:
                            enemy.EnemyHit(player)
                            print('enemyhit')
                        elif move == 4:
                            enemy.EnemyHeal(5)
                        else:
                            enemy.EnemySummon(enemies)
            
            elif blockorattack.upper() == "BLOCK":
                if previousinputs[0] == "BLOCK":
                    print("Your block has failed. Literally every video game does this. Do better. ")
                    for enemy in enemies:
                        enemy.EnemyHit(player)
                else:
                    player.PlayerHeal(15)
                    print(f"Blocking has allowed you to regain some stamina. You now have {player.currenthp} health.")
                    for enemy in enemies:
                        if isinstance(enemy, Enemy):
                            healorattack = random.randint(1,2)
                            if healorattack == 1:
                                print(f"{enemy.name} attempted to strike, but the attack was blocked!")
                            else:
                                enemy.EnemyHeal(5)
                        elif isinstance(enemy, BossEnemy):
                            move = random.randint(1, 5)
                            attack = [1, 2, 3]
                            heal = [4]
                            summon = [5]
                            if move in heal:
                                enemy.EnemyHeal(10)
                            elif move in summon:
                                enemy.EnemySummon(enemies)
                            elif move in attack:
                                print(f"{enemy.name} attempted to strike, but the attack was blocked!")
                    previousinputs.clear()
                    previousinputs.append("BLOCK")
                
            if player.currenthp <= 0:
                player.dead = True
                print(f"{player.name} has died! You lost!!!! HAHAHAH!!!")
                enemies.clear()
            else:
                print(f"You have {player.currenthp} HP.")
        if len(enemies) == 0:
            print(f"You have won!!!")




woodsword = Weapon('woodsword', 10, 10, 10)
woodclub = Weapon('woodclub', 15, 5, 5)
apple = HealingItem('apple', 5, 5)
woodsword.WeaponDictionary()
woodclub.WeaponDictionary()
apple.HealingItemDictionary()

inventory = [woodsword, woodclub, apple]

player = MainCharacter('player', 100, 100, 10, woodsword, inventory, 100)
boss = BossEnemy('SUPERMAN', 100, 100, 10, woodsword)
goblin = Enemy('goblin', 10, 10, 10, woodclub, 10, 'nothing')
BattleInteractions.BossBattle(player, [boss, goblin])
    


