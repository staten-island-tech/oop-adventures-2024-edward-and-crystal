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
            print('You landed a critical hit!')
            enemy.currenthp -= 2*damage
        else:
            enemy.currenthp -= damage
        self.weapon.durability -= 1
        if self.weapon.durability == 0:
            print(f'Your {self.weapon.name} has broken!')
            try:
                self.inventory.remove(self.weapon)
            except ValueError:
                pass  
            self.weapon = Weapon('Nothing', 0, random.randint(100, 100000000000000000000000), 0) # sets the weapon to nothing so that the damage calc doesn't break 😧

    def MainCharacterGetEXP(self, exp):
        self.exp += exp
        if self.exp >= 75:
            hppercent = self.currenthp / self.maxhp
            levels = int(self.exp / 75)
            self.level += levels
            overflow = self.exp % 75
            self.exp = overflow
            self.strength += 5*levels
            self.maxhp += 10*levels
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

class Grifter(Enemy):
    def __init__(self, name, maxhp, currenthp, steal, weapon, golddrop, weapondrop, expdrop):
        super().__init__(name, maxhp, currenthp, steal, weapon, golddrop, weapondrop, expdrop)
        self.steal = steal

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


grifter = Grifter('g', 100, 100, 100, 100, 100, 100, 100)        
grifter.EnemyTakeDamage(10)
print(grifter.maxhp)
print(grifter.currenthp)