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

    def CharacterDamageCalc(self):
        damage = self.strength + self.weapon.strength
        return damage

    def EnemySpawn(enemies):
        for enemy in enemies:
            enemytype = enemy['type']
            if enemytype == 'REGULAR':
                name = enemy['name']
                maxhp = enemy['maxhp']
                currenthp = enemy['currenthp']
                strength = enemy['strength']
                golddrop = enemy['golddrop']
                expdrop = enemy['expdrop']
            
                weapon = Weapon(enemy['weapon']['name'], enemy['weapon']['strength'], enemy['weapon']['durability'], 0)

                drop = enemy['weapondrop']
                droptype = drop['type']
                if droptype == 'WEAPON':
                    itemname = drop['name']
                    itemstrength = drop['strength']
                    itemdurability = drop['durability']
                    itemcost = drop['cost']
                    weapondrop = Weapon(itemname, itemstrength, itemdurability, itemcost)
                elif droptype == 'HEALING ITEM':
                    itemname = drop['name']
                    itemheal = drop['heal']
                    itemcost = drop['cost']
                    weapondrop = HealingItem(itemname, itemheal, itemcost)
                else:
                    weapondrop = 'nothing'
            

                enemies.append(Enemy(name, maxhp, currenthp, strength, weapon, golddrop, weapondrop, expdrop))
        
            elif enemytype == 'GRIFTER':
                name = enemy['name']
                maxhp = enemy['maxhp']
                currenthp = enemy['currenthp']
                steal = enemy['steal']
                golddrop = enemy['golddrop']
                expdrop = enemy['expdrop']
                weapon = Weapon(enemy['weapon']['name'], enemy['weapon']['strength'], enemy['weapon']['durability'], 0)
            
                drop = enemy['weapondrop']
                itemname = drop['name']
                itemstrength = drop['strength']
                itemdurability = drop['durability']
                itemcost = drop['cost']
                weapondrop = Weapon(itemname, itemstrength, itemdurability, itemcost)

                enemies.append(Grifter(name, maxhp, currenthp, steal, weapon, golddrop, weapondrop, expdrop))

            elif enemytype == 'BOSS':
                name = enemy['name']
                maxhp = enemy['maxhp']
                currenthp = enemy['currenthp']
                strength = enemy['strength']
                expdrop = enemy['expdrop']
                weapon = Weapon(enemy['weapon']['name'], enemy['weapon']['strength'], enemy['weapon']['durability'], 0)
            
                enemies.append(BossEnemy(name, maxhp, currenthp, strength, weapon, expdrop))

            else:
                print('bad this is bad this is pretty darn bad :(')


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
        currenthp = self.currenthp
        maxhp = self.maxhp
        if currenthp + heal <= maxhp:
            self.currenthp = currenthp + heal
        else:
            self.currenthp = maxhp

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

    def MainCharacterAttack(self, enemy):
        print(f"{self.name} attacks {enemy.name}!")
        damage = super().CharacterDamageCalc()
        import random
        if random.randint(1,10) == 10:
            enemy.currenthp -= 2*damage
        else:
            enemy.currenthp -= damage
        self.weapon.durability -= 1
        if self.weapon.durability == 0:
            try:
                self.inventory.remove(self.weapon)
            except ValueError:
               pass  
            self.weapon = Weapon('Nothing', 0, 100, 0) # sets the weapon to nothing so that the damage calc doesn't break 😧

    def MainCharacterGetEXP(self, exp):
        self.exp += exp
        if self.exp >= 60:
            hppercent = self.currenthp / self.maxhp
            levels = int(self.exp / 60)
            self.level += levels
            overflow = self.exp % 60
            self.exp = overflow
            self.strength += 2*levels
            self.maxhp += 5*levels
            self.currenthp = self.maxhp*hppercent

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
            


    def EnemyDealDamage(self, player):
        weaponstrength = self.weapon['strength']
        damage = self.strength + weaponstrength
        player.health -= damage


    def EnemyHit(self, player):
        print(f"{self.name} attacks {player.name}!")
        damage = super().CharacterDamageCalc()
        player.currenthp -= damage

class Grifter(Enemy): # grifter hell :D
    def __init__(self, name, maxhp, currenthp, strength, weapon, golddrop, weapondrop, expdrop, steal):
        super().__init__(name, maxhp, currenthp, strength, weapon, golddrop, weapondrop, expdrop)
        self.steal = steal
        
        
    def GrifterCalc(self):
        return 1 - (self.steal / 100)
    
    def GrifterHeal(self, heal):
        heal = self.maxhp * (heal / 100)
        self.currenthp += heal
        if self.currenthp > self.maxhp:
            self.currenthp = self.maxhp

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
   
    def EnemySummon(self, enemies):
        woodclub = Weapon('woodclub', 10, 10, 10)
        summonable = Enemy("Summoned Orc", 20, 15, 10, woodclub, 0, 'nothing', 0)
        enemies.append(summonable)

    def MAKELIFEHELL(self, enemies):
        woodclub = Weapon('woodclub', 10, 10, 10)
        summonable = BossEnemy('SUMMONED BOSS', 100, 100, 10, woodclub, 0)
        enemies.append(summonable)