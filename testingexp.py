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
    def __init__(self, name, maxhp, currenthp, strength, weapon, inventory, gold, level, exp):
        super().__init__(name, maxhp, currenthp, strength, weapon)
        self.inventory = list(inventory)
        self.gold = gold
        self.level = level
        self.exp = exp

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

    def MainCharacterGetEXP(self, exp):
        self.exp += exp
        if self.exp >= 75:
            self.level += 1
            overflow = self.exp - 75
            self.exp = overflow
            self.strength += 5
            self.maxhp += 10
            self.currenthp += 5
            print(f"You have leveled up to {self.level}!")



class Enemy(Character):
    def __init__(self, name, maxhp, currenthp, strength, weapon, golddrop, weapondrop, expdrop):
        super().__init__(name, maxhp, currenthp, strength, weapon)
        self.golddrop = golddrop
        self.weapondrop = weapondrop
        self.expdrop = expdrop

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
    def __init__(self, name, maxhp, currenthp, strength, weapon, expdrop):
        super().__init__(name, maxhp, currenthp, strength, weapon)
        self.expdrop = expdrop

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
        summonable = Enemy("Summoned Orc", 20, 15, 10, woodclub, 0, 'nothing', 0)
        enemies.append(summonable)
        print(f"{self.name} has summoned a {summonable.name}! ")

    def MAKELIFEHELL(self, enemies):
        woodclub = Weapon('woodclub', 10, 10, 10)
        summonable = BossEnemy('SUMMONED BOSS', 100, 100, 10, woodclub, 0)
        enemies.append(summonable)
        print(f"{self.name} has summoned a {summonable.name}! Good Luck!!! ")

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
                        try:
                            enemies.remove(enemy)
                            print(f'{enemy.name} has died!')
                        
                            player.inventory.append(enemy.weapondrop)
                            player.gold += enemy.golddrop
                            player.MainCharacterGetEXP(enemy.expdrop)
                            print(player.exp)
                        except ValueError:
                            iwouldwin = False

                for enemy in enemies:
                    healorattack = random.randint(1,2)
                    if healorattack == 1:
                        enemy.EnemyHeal(5)
                    elif healorattack == 2:
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
                        print(f"You currently have {player.currenthp} HP.")
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
            if player.currenthp > 0:
                print(f"You have {player.currenthp} HP.")
            else:
                player.dead = True
                player.CharacterDeathMessage()
                enemies.clear()
                break

    def BossBattle(player, enemies):
        import random
        print(player.exp)
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
                        try:
                            enemies.remove(enemy)
                            print(f'{enemy.name} has died!')
                            try:
                                if isinstance(enemy, Enemy):
                                    player.inventory.append(enemy.weapondrop)
                                    player.gold += enemy.golddrop
                                    player.MainCharacterGetEXP(enemy.expdrop)
                                    print(player.exp)
                                else:
                                    player.MainCharacterGetEXP(enemy.expdrop)
                                    print(player.exp)
                            except ValueError:
                                iwouldwin = True
                        except ValueError:
                            iwouldwin = False
                for enemy in enemies:
                    if isinstance(enemy, Enemy):
                        move = random.randint(1,2)
                        if move == 1:
                            enemy.EnemyHit(player)
                            print(f"You currently have {player.currenthp} HP.")
                        else:
                            enemy.EnemyHeal(5)
                    elif isinstance(enemy, BossEnemy):
                        move = random.randint(1,100)
                        if move <= 60:
                            enemy.EnemyHit(player)
                            print(f"You currently have {player.currenthp} HP.")
                        elif move > 60 and move <= 80:
                            enemy.EnemyHeal(5)
                        elif move > 80 and move < 100:
                            enemy.EnemySummon(enemies)
                        else:
                            enemy.MAKELIFEHELL(enemies)
            
            elif blockorattack.upper() == "BLOCK":
                if previousinputs[0] == "BLOCK":
                    print("Your block has failed. Literally every video game does this. Do better. ")
                    for enemy in enemies:
                        enemy.EnemyHit(player)
                    previousinputs.clear()
                    previousinputs.append("BLOCK")
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
            if player.currenthp > 0:
                print(f"You have {player.currenthp} HP.")
            else:
                player.dead = True
                player.CharacterDeathMessage()
                enemies.clear()
                break

woodsword = Weapon('woodsword', 10, 10, 10)
woodclub = Weapon('woodclub', 15, 5, 5)
apple = HealingItem('apple', 5, 5)
woodsword.WeaponDictionary()
woodclub.WeaponDictionary()
apple.HealingItemDictionary()

inventory = [woodsword, woodclub, apple]
player = MainCharacter('player', 100, 100, 10, woodsword, inventory, 100, 0, 0)
boss = BossEnemy('SUPERMAN', 100, 100, 10, woodsword, 10)
goblin = Enemy('goblin', 10, 10, 10, woodclub, 10, 'nothing', 20)
goblinb = Enemy('goblinb', 10, 10, 10, woodclub, 10, 'nothing', 20)
goblinc = Enemy('goblinc', 10, 10, 10, woodclub, 10, 'nothing', 20)
goblind = Enemy('goblind', 10, 10, 10, woodclub, 10, 'nothing', 20)
enemies = [goblin, goblinb, goblinc, goblind]

BattleInteractions.Battles(player, enemies)