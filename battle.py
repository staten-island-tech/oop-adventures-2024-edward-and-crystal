import tkinter as tk
from charactersitems import Weapon
from charactersitems import BossEnemy
from charactersitems import Enemy
from charactersitems import MainCharacter
from charactersitems import HealingItem
from charactersitems import Grifter
window = tk.Tk()

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
    
    def EnemyTurn(enemies, player, players, action): # action is similar to the prompt command in menus
        global enemylabels
        import random
        enemylabels = [ ]
        if action == 'BLOCKFAIL':
            blockfail = tk.Label(window, text='Your block has failed!')
            blockfail.pack()
            enemylabels.append(blockfail)
        
        currentlevel = player.level
        for enemy in enemies:
            if enemy.currenthp <= 0:
                try:
                    enemies.remove(enemy)
                    enemydie = tk.Label(window, text=f'{enemy.name} has died!')
                    enemydie.pack()
                    enemylabels.append(enemydie)
                    try:
                        if isinstance(enemy, Enemy) or isinstance(enemy, Grifter):
                            droprate = random.randint(1, 6)
                            if len(player.inventory) <= 25 and droprate == 6:
                                if isinstance(enemy.weapondrop, Weapon) or isinstance(enemy.weapondrop, HealingItem):
                                    #basically, i have weapondrop listed as 'nothing' for some enemies
                                    #and ive decided to have some enemies that drop healing items
                                    player.inventory.append(enemy.weapondrop)
                            player.gold += enemy.golddrop
                            player.MainCharacterGetEXP(enemy.expdrop)
                        else:
                            player.MainCharacterGetEXP(enemy.expdrop)
                    except ValueError:
                        iwouldwin = True
                except ValueError:
                    iwouldwin = False
                    
        newlevel = player.level
        if newlevel > currentlevel:
            levelup = tk.Label(window, text=f'You have leveled up to level {newlevel}!')
            levelup.pack()
            enemylabels.append(levelup)
        
        for enemy in enemies:
            if isinstance(enemy, Grifter):
                move = random.randint(1,10)
                print(len(player.inventory))
                if move < 10 or len(player.inventory) == 1: # if the only item in the inventory is their held weapon i wont let them steal
                    steal = (enemy.strength / 100)
                    stolengold = round(steal * player.gold, 0)
                    player.gold -= stolengold
                    enemystole = tk.Label(window, text=f"{enemy.name} stole {stolengold} gold!")
                    enemystole.pack()
                    enemylabels.append(enemystole)
                else:
                    for item in player.inventory: 
                        if player.weapon.name == item.name: # checking to see if the item in the inventory is the equipped one
                            weapon = item
                            break
                     
                    playerinventory = player.inventory
                    playerinventory.remove(weapon)
                    
                    stolenitem = playerinventory[random.randint(1, len(playerinventory)) - 1]
                    playerinventory.remove(stolenitem)
                    player.inventory = playerinventory
                    enemySTOLE = tk.Label(window, text=f"{enemy.name} stole your {stolenitem.name}!")
                    enemySTOLE.pack()
                    enemylabels.append(enemySTOLE)
                    
            elif isinstance(enemy, Enemy):
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

                if orcnumber < 4: # i like stupidly unfair video games but too many orcs would make whalen ragequit maybe?
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
    
    def BattleInitiation(player, room):
        import random
        if player.level <= 4:
            enemynumber = random.randint(1,2)
        elif player.level <= 6 and player.level >= 4:
            enemynumber = random.randint(1,3)
        elif player.level <= 10 and player.level >= 7:
            enemynumber = random.randint(2,4)
        elif player.level <= 15 and player.level >= 11:
            enemynumber = random.randint(3,4)
        else:
            chance = random.randint(1,5)
            if chance == 5:
                enemynumber = 5
            else:
                enemynumber = 4
              
                
        for enemy in range(enemynumber):
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
        if len(players) == 0:
            wow = tk.Label(window, text='You died!')
            wow.pack()

        continuee = tk.Button(window, text='End Battle', command=lambda: Battles.Continue(continuevar))
        continuee.pack()

        window.wait_variable(continuevar)

