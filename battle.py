import tkinter as tk
from charactersitems import Weapon
from charactersitems import BossEnemy
from charactersitems import Enemy
from charactersitems import MainCharacter

class Battles():
    def BattleAction(action, actionvar):
        actionvar.set(action)

    def PlayerAction(window):
        global attack_button
        global block_button

        actionvar = tk.StringVar()

        attack_button = tk.Button(window, text="Attack", command=lambda: Battles.BattleAction("attack", actionvar))
        block_button = tk.Button(window, text="Block", command=lambda: Battles.BattleAction("block", actionvar))

        attack_button.pack()
        block_button.pack()
        window.update()

        window.wait_variable(actionvar)
        action = actionvar.get()
        return action
    
    def EnemyChosen(enemy, enemyvar):
        enemyvar.set(enemy)
    
    def PlayerChooseEnemy(window, enemies):
        global enemybuttons
        enemyvar = tk.IntVar()  # stores a specific spot in the list of enemies, so we can call it
        enemybuttons = []

        for index, enemy in enumerate(enemies):
            enemy_button = tk.Button(window, text=enemy.name, command=lambda i=index: Battles.EnemyChosen(i, enemyvar))
            enemy_button.pack()
            enemybuttons.append(enemy_button)

        window.update()
        window.wait_variable(enemyvar)
        index = enemyvar.get()  
        return enemies[index] 
    
    def EnemyTurn(enemies, player, players, action):
        if action == 'BLOCKFAIL':
            print('Your block has failed!')

        import random
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
                    if action == 'BLOCKWORK':
                        print(f'{enemy.name} attempted to attack, but it was blocked!')
                    else:
                        enemy.EnemyHit(player)
                        if player.currenthp <= 0:
                                print(f"You currently have 0 HP.")
                                player.currenthp = 0
                                players.remove(player)
                                break
                        print(f"You currently have {player.currenthp} HP.")
                else:
                    enemy.EnemyHeal(5)
            elif isinstance(enemy, BossEnemy): # a bunch of boss enemies
                move = random.randint(1,100)
                orcnumber = 0 # finding how many orcs there are
                for findorc in enemies:
                    if findorc.name == "Summoned Orc":
                        orcnumber += 1

                if orcnumber < 4: # i like stupidly unfair video games but too many orcs might break the window
                    if move <= 60:
                        if action == 'BLOCKWORK':
                            print(f'{enemy.name} attempted to attack, but it was blocked!')
                        else:
                            enemy.EnemyHit(player)
                            if player.currenthp <= 0:
                                print(f"You currently have 0 HP.")
                                player.currenthp = 0
                                players.remove(player)
                                break
                            print(f"You currently have {player.currenthp} HP.")
                    elif move > 60 and move <= 80:
                        enemy.EnemyHeal(5)
                    elif move > 80 and move < 100:
                        enemy.EnemySummon(enemies)
                    else:
                        enemy.MAKELIFEHELL(enemies)
                else:
                    if move <= 75:
                        if action == 'BLOCKWORK':
                            print(f'{enemy.name} attempted to attack, but it was blocked!')
                        else:
                            enemy.EnemyHit(player)
                            print(f"You currently have {player.currenthp} HP.")
                    else: # ahh but the boss can heal 5x more if there are too many orcs
                        enemy.EnemyHeal(25)
            


    def MainCharacterAttack(player, enemy):
        damage = player.strength + player.weapon.strength
        enemy.currenthp -= damage
        print(f'You attacked the {enemy.name}')

    def Battle(window, player, enemies):
        global attack_button
        global block_button
        global enemybuttons
        
        previousinputs = 'attack'
        players = [player]
        while len(enemies) > 0 and len(players) > 0:
            action = Battles.PlayerAction(window)
            if action == 'attack':
                previousinputs = 'attack'
                block_button.destroy()
                attack_button.destroy()
                enemy = Battles.PlayerChooseEnemy(window, enemies)
                Battles.MainCharacterAttack(player, enemy)
                Battles.EnemyTurn(enemies, player, players, 'ATTACK')
                for button in enemybuttons:
                    button.destroy()

            elif action == 'block':
                if previousinputs == 'attack':
                    Battles.EnemyTurn(enemies, player, players, 'BLOCKWORK')
                    attack_button.destroy()
                    block_button.destroy()
                    previousinputs = 'block'
                else:
                    Battles.EnemyTurn(enemies, player, players, 'BLOCKFAIL')
                    attack_button.destroy()
                    block_button.destroy()
                    previousinputs = 'block'

            print('turn over')
        if len(enemies) == 0:
            print('You won!')
        if len(players) == 0:
            print('Womp WOmp')


window = tk.Tk()
window.title("Battle Mode")

weapon = Weapon('weapon', 0, 10, 10)

player = MainCharacter('name', 10, 10, 10, weapon, [], 0, 0, 0)
enemy1 = Enemy('enemy1', 1, 1, 1, weapon, 10, weapon, 10)
enemy2 = Enemy('enemy2', 1, 1, 1, weapon, 10, weapon, 10)
enemy3 = Enemy('enemy3', 1, 1, 1, weapon, 10, weapon, 10)
boss = BossEnemy('boos', 30, 30, 1, weapon, 1)
enemies = [enemy1, enemy2, enemy3, boss]

Battles.Battle(window, player, enemies)
window.mainloop()