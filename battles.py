from charactersitems import Weapon
from charactersitems import BossEnemy
from charactersitems import Enemy
from charactersitems import MainCharacter

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
                               else:
                                   player.MainCharacterGetEXP(enemy.expdrop)
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
                           move = random.randint(1, 100)
                           if move <= 20:
                               enemy.EnemyHeal(10)
                           elif move in (21, 40):
                               enemy.EnemySummon(enemies)
                           elif move in (41, 98):
                               print(f"{enemy.name} attempted to strike, but the attack was blocked!")
                           else:
                               enemy.MAKELIFEHELL(enemies)
                   previousinputs.clear()
                   previousinputs.append("BLOCK")
           if player.currenthp > 0:
               print(f"You have {player.currenthp} HP.")
           else:
               player.dead = True
               player.CharacterDeathMessage()
               enemies.clear()
               break

