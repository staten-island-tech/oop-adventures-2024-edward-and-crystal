import tkinter as tk
from charactersitems import Weapon
from charactersitems import BossEnemy
from charactersitems import Enemy
from charactersitems import MainCharacter

class Battles():
    def BattleAction(action, actionvar):
        actionvar.set(action)

    def PlayerAction(window, enemies):
        global attack_button
        global block_button
        global enemylabels

        actionvar = tk.StringVar()
        enemylabels = []
        for enemy in enemies:
            enemyLabel = tk.Label(window, text=f'{enemy.name} ) {enemy.currenthp} HP')
            enemyLabel.pack()
            enemylabels.append(enemyLabel)

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
        global enemylabels
        import random
        enemylabels = [ ]
        if action == 'BLOCKFAIL':
            blockfail = tk.Label(window, text='Your block has failed!')
            blockfail.pack()
            enemylabels.append(blockfail)

        for enemy in enemies:
            if enemy.currenthp <= 0:
                try:
                    enemies.remove(enemy)
                    enemydie = tk.Label(window, text=f'{enemy.name} has died!')
                    enemydie.pack()
                    enemylabels.append(enemydie)
                    try:
                        if isinstance(enemy, Enemy):
                            if len(player.inventory) > 25:
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
                        enemyblocked = tk.Label(window, text=f'{enemy.name} tried to attack, but you blocked!')
                        enemyblocked.pack()
                        enemylabels.append(enemyblocked)
                    else:
                        enemy.EnemyHit(player)
                        enemyhit = tk.Label(window, text=f'{enemy.name} attacks you!')
                        enemyhit.pack()
                        enemylabels.append(enemyhit)
                        if player.currenthp <= 0:
                            player.currenthp = 0
                            players.remove(player)
                            break
                        playerhealth = tk.Label(window, text=f'You have {player.currenthp} HP')
                        playerhealth.pack()
                        enemylabels.append(playerhealth)
                else:
                    enemy.EnemyHeal(5)
                    enemyheal = tk.Label(window, text=f'{enemy.name} healed 5 HP!')
                    enemyheal.pack()
                    enemylabels.append(enemyheal)
            elif isinstance(enemy, BossEnemy): # a bunch of boss enemies
                move = random.randint(1,100)
                orcnumber = 0 # finding how many orcs there are
                for findorc in enemies:
                    if findorc.name == "Summoned Orc":
                        orcnumber += 1

                if orcnumber < 4: # i like stupidly unfair video games but too many orcs might break the window
                    if move <= 60:
                        if action == 'BLOCKWORK':
                            enemyblocked = tk.Label(window, text=f'{enemy.name} tried to attack, but you blocked!')
                            enemyblocked.pack()
                            enemylabels.append(enemyblocked)
                        else:
                            enemy.EnemyHit(player)
                            enemyhit = tk.Label(window, text=f'{enemy.name} attacks you!')
                            enemyhit.pack()
                            enemylabels.append(enemyhit)
                            if player.currenthp <= 0:
                                playerhealth = tk.Label(window, text='You have died!')
                                playerhealth.pack()
                                enemylabels.append(playerhealth)
                                player.currenthp = 0
                                players.remove(player)
                                break
                            playerhealth = tk.Label(window, text=f'You have {player.currenthp} HP')
                            playerhealth.pack()
                            enemylabels.append(playerhealth)
                    elif move > 60 and move <= 80:
                        enemy.EnemyHeal(5)
                        enemyheal = tk.Label(window, text=f'{enemy.name} healed 5 HP!')
                        enemyheal.pack()
                        enemylabels.append(enemyheal)
                    elif move > 80 and move < 100:
                        enemy.EnemySummon(enemies)
                        enemysummon = tk.Label(window, text=f'{enemy.name} summons an Orc!')
                        enemysummon.pack()
                        enemylabels.append(enemysummon)
                    else:
                        enemy.MAKELIFEHELL(enemies)
                        enemybosssummon = tk.Label(window, text=f'{enemy.name} summons another BOSS!')
                        enemybosssummon.pack()
                        enemylabels.append(enemybosssummon)
                else:
                    if move <= 75:
                        if action == 'BLOCKWORK':
                            enemyblocked = tk.Label(window, text=f'{enemy.name} tried to attack, but you blocked!')
                            enemyblocked.pack()
                            enemylabels.append(enemyblocked)
                        else:
                            enemy.EnemyHit(player)
                            enemyhit = tk.Label(f'{enemy.name} attacks you!')
                            enemyhit.pack()
                            enemylabels.append(enemyhit)
                    else: # ahh but the boss can heal 5x more if there are too many orcs
                        enemy.EnemyHeal(25)
                        enemyheal = tk.Label(window, text=f'{enemy.name} healed 25 HP!')
                        enemyheal.pack()
                        enemylabels.append(enemyheal)
            
    def DeleteThing(label):
        label.destroy()
        
    def DeleteThings(labels):
        for label in labels:
            label.destroy()

    def MainCharacterAttack(player, enemy):
        damage = player.strength + player.weapon.strength
        enemy.currenthp -= damage
        print(f'You attacked the {enemy.name}')

    def Continue(continuevar):
            continuee.destroy()
            continuevar.set('continue')
            try:
                wow.destroy()
            except:
                pass

    def Battle(window, player, enemies):
        global attack_button
        global block_button
        global enemybuttons
        global continuee
        global wow

        window.title('Battle')
        previousinputs = 'attack'
        players = [player]
        playerbeforelevel = player.level

        while len(enemies) > 0 and len(players) > 0:
            try:
                Battles.DeleteThings(enemylabels)
                continuee.destroy()
            except:
                pass
            action = Battles.PlayerAction(window, enemies)
            if action == 'attack':
                Battles.DeleteThings(enemylabels)
                previousinputs = 'attack'
                block_button.destroy()
                attack_button.destroy()
                enemy = Battles.PlayerChooseEnemy(window, enemies)
                Battles.MainCharacterAttack(player, enemy)
                Battles.EnemyTurn(enemies, player, players, 'ATTACK')
                for button in enemybuttons:
                    button.destroy()

            elif action == 'block':
                import random
                for label in enemylabels:
                    label.destroy()
                if previousinputs == 'attack':
                    player.PlayerHeal(random.randint(5, 10))
                    Battles.EnemyTurn(enemies, player, players, 'BLOCKWORK')
                    attack_button.destroy()
                    block_button.destroy()
                    previousinputs = 'block'
                else:
                    Battles.EnemyTurn(enemies, player, players, 'BLOCKFAIL')
                    attack_button.destroy()
                    block_button.destroy()
                    previousinputs = 'block'
            
            continuevar = tk.StringVar()
            continuee = tk.Button(window, text='Continue', command=lambda: Battles.Continue(continuevar))
            continuee.pack()

            window.wait_variable(continuevar)
            continuevariable = continuevar.get()
            if continuevariable == 'continue':
                for label in enemylabels:
                    label.destroy()
                
        if len(enemies) == 0:
            wow = tk.Label(window, text='You win!')
            wow.pack()
            playernewlevel = player.level
            if playernewlevel > playerbeforelevel:
                levelup = tk.Label(window, text=f'You have leveled up to Level {player.level}!')
                levelup.pack()
        if len(players) == 0:
            wow = tk.Label(window, text='You died!')
            wow.pack()

        continuee = tk.Button(window, text='End Battle', command=lambda: Battles.Continue(continuevar))
        continuee.pack()

        window.wait_variable(continuevar)
        try:
            levelup.destroy()
        except:
            pass 
        
window = tk.Tk()
window.title("Battle Mode")
from menus import Menu
weapon = Weapon('weapon', 0, 10, 10)

player = MainCharacter('name', 100, 100, 10, weapon, [], 0, 1, 70)
enemy1 = Enemy('enemy1', 1, 1, 1, weapon, 10, weapon, 10)
enemy2 = Enemy('enemy2', 1, 1, 1, weapon, 10, weapon, 10)
enemy3 = Enemy('enemy3', 1, 1, 1, weapon, 10, weapon, 10)
boss = BossEnemy('boos', 30, 30, 1, weapon, 1)
enemies = [enemy1, enemy2, enemy3, boss]
for i in range (25):
    player.inventory.append(Weapon(f'weapon{i}', 1, 1, 1))
Menu.PlayerMenu(window, player)
Battles.Battle(window, player, enemies)
Menu.PlayerMenu(window, player)
window.mainloop()