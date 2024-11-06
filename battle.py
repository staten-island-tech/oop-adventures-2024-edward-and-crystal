import tkinter as tk

from charactersitems import Weapon
from charactersitems import BossEnemy
from charactersitems import Enemy
from charactersitems import MainCharacter

def battle_action(action):
    action_var.set(action)

def battle():
    global action_var
    
    window = tk.Tk()
    window.title("Battle Mode")
    
    action_var = tk.StringVar()
    
    attack_button = tk.Button(window, text="Attack", command=lambda: battle_action("attack"))
    block_button = tk.Button(window, text="Block", command=lambda: battle_action("block"))
    
    attack_button.pack()
    block_button.pack()
    
    window.wait_variable(action_var)

    action_taken = action_var.get()
    print(f"Action taken: {action_taken}")


class Battles:
    def BattleAction(action):
        global actionvar
        actionvar.set(action)
        window.quit()

    def PlayerAction(window):
        global actionvar

        actionvar = tk.StringVar()

        attack_button = tk.Button(window, text="Attack", command=lambda: Battles.BattleAction("attack"))
        block_button = tk.Button(window, text="Block", command=lambda: Battles.BattleAction("block"))

        attack_button.pack()
        block_button.pack()

        window.update()

        window.wait_variable(actionvar)
        action = actionvar.get()
        return action
    
    def EnemyChosen(enemy):
        global enemyvar
        enemyvar.set(enemy)

    def AttackEnemies(window, player, enemies):
        global enemyvar
        
        enemyvar = tk.StringVar()

        for enemy in range(min(8, len(enemies))): 
            enemy_button = tk.Button(window, text=enemies[enemy].name, command=lambda enemy=enemy: Battles.EnemyChosen(enemy))
            enemy_button.pack()
        
        window.update_idletasks()
        window.wait_variable(enemyvar)
        enemy = enemyvar.get()
        MainCharacter.MainCharacterAttack(player, enemy)


    def EnemyTurn(enemies, player, block):
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
                    if block == True:
                        print(f'{enemy.name} attempted to attack, but it was blocked!')
                    else:
                        enemy.EnemyHit(player)
                        print(f"You currently have {player.currenthp} HP.")
                else:
                    enemy.EnemyHeal(5)
            elif isinstance(enemy, BossEnemy):
                move = random.randint(1,100)
                if len(enemies) < 8:
                    if move <= 60:
                        if block == True:
                            print(f'{enemy.name} attempted to attack, but it was blocked!')
                        else:
                            enemy.EnemyHit(player)
                            print(f"You currently have {player.currenthp} HP.")
                    elif move > 60 and move <= 80:
                        enemy.EnemyHeal(5)
                    elif move > 80 and move < 100:
                        enemy.EnemySummon(enemies)
                    else:
                        enemy.MAKELIFEHELL(enemies)
                else:
                    if move <= 75:
                        if block == True:
                            print(f'{enemy.name} attempted to attack, but it was blocked!')
                        else:
                            enemy.EnemyHit(player)
                            print(f"You currently have {player.currenthp} HP.")
                    else:
                        enemy.EnemyHeal(15)
    
    def Battle(player, enemies, window):
        window.mainloop()

        previousinputs = 'nothing'
        players = [player]
        while len(enemies) > 0 and len(players) > 0:
            action = Battles.PlayerAction(window)
            previousinputs = action
            if action == 'attack':
                Battles.AttackEnemies(window, player, enemies)
                Battles.EnemyTurn(enemies, player, False)
            else:
                if previousinputs == 'block':
                    print('Your block has failed.')
                    Battles.EnemyTurn(enemies, player, False)
                else:
                    Battles.EnemyTurn(enemies, player, True)



window = tk.Tk()
window.title("Battle Mode")

weapon = Weapon('weapon', 10, 10, 10)

player = MainCharacter('name', 10, 10, 10, weapon, [], 0, 0, 0)
enemy1 = Enemy('enemy1', 1, 1, 1, weapon, 10, weapon, 10)
enemy2 = Enemy('enemy2', 1, 1, 1, weapon, 10, weapon, 10)
enemy3 = Enemy('enemy3', 1, 1, 1, weapon, 10, weapon, 10)
enemies = [enemy1, enemy2, enemy3]

Battles.Battle(player, enemies, window)