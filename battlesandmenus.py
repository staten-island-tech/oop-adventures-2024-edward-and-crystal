from charactersitems import Weapon
from charactersitems import HealingItem
from charactersitems import OtherStuff
from charactersitems import BossEnemy
from charactersitems import Enemy
from charactersitems import MainCharacter

class Menu(Weapon, HealingItem):
    def Inventory(player):
        inventory = [ ]
        close = OtherStuff('Close Menu')
        for item in player.inventory:
            inventory.append(item)
        inventory.append(close)
        finish = False
        for item in inventory[: - 1]:
            print(item.name)
        print(close.name)
        x = 0
        while finish == False:
            selecteditem = inventory[x]
            if isinstance(selecteditem, Weapon) or isinstance(selecteditem, HealingItem):
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
                            confirm = input("Would you like to close the inventory? ")
                            if confirm.upper() == "YES":
                                finish = True
                                break
                    else:
                        print(f"name) {selecteditem.name}")
                        print(f"heal amount) {selecteditem.heal}")
                        use = input("Would you like to use this item? ")
                        if use.upper() == "YES":
                            print(f"You have {player.currenthp}, and use the {selecteditem.name}")
                            player.PlayerHeal(selecteditem.heal)
                            x -= 1
                            try:
                                player.inventory.remove(selecteditem)
                                print(player.inventory)
                                inventory.remove(selecteditem)
                            except ValueError:
                                pass
                            print(f"Now you have {player.currenthp} HP! ")
                            close = input("Would you like to close the inventory? ")
                            if close.upper() == "YES":
                                finish = True
                                break
                else:
                    move = input("Press Z to move up the menu and X to move down the inventory. ")
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

            elif isinstance(selecteditem, OtherStuff):
                print(f"You are currently hovering over the Close Inventory option.")
                close = input("Do you want to close your inventory? ")
                if close.upper() == "YES":
                    finish = True
                    break
                else:
                    move = input("Press Z to move up the menu and X to move down the inventory. ")
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
        shopitems = [woodensword, stonesword, goldsword, apple, healingpotion]
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
                    move = input("Press Z to move up the menu and X to move down the shop. ")
    
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
    
    def OpenMenu(player):
        stats = OtherStuff(f'{player.name}')
        inventory = OtherStuff('Inventory')
        shop = OtherStuff('Open Shop')
        closemenu = OtherStuff('Close')
        menu = [stats, inventory, shop, closemenu]
        for item in menu:
            print(item.name)
        x = 0
        done = False
        while done == False:
            selecteditem = menu[x]
            if selecteditem == closemenu:
                confirm = input("Would you like to close the menu? ")
                if confirm.upper() == "YES":
                    done = True
                    break
            elif selecteditem == stats:
                confirm = input("Would you like to view your stats? ")
                if confirm.upper() == "YES":
                    print(f'{player.name} ) Level {player.level}')
                    print(f'{player.exp} / 75 XP')
                    print(f'{player.currenthp} / {player.maxhp} HP')
                    print(f'Strength: {player.strength}')
                    print(f'{player.gold} Gold')
                    print(player.weapon.name)
            elif selecteditem == inventory:
                confirm = input("Would you like to inspect your inventory? ")
                if confirm.upper() == "YES":
                    Menu.Inventory(player)
            elif selecteditem == shop:
                confirm = input("Would you like to inspect your shop? ")
                if confirm.upper() == "YES":
                    Menu.Shop(player)
            move = input("Press Z to move up the menu and X to move down the menu. ")
            if move.upper() == "Z":
                if x != 0:
                     x -= 1
                else:
                    x = len(menu) - 1
            elif move.upper() == "X":
                if x != len(menu) - 1:
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

woodsword = Weapon('woodsword', 10, 10, 10)
woodclub = Weapon('woodclub', 15, 5, 5)
apple = HealingItem('apple', 5, 5)
woodsword.WeaponDictionary()
woodclub.WeaponDictionary()
apple.HealingItemDictionary()

inventory = [woodsword, woodclub, apple]
player = MainCharacter('player', 100, 100, 10, woodsword, inventory, 100, 1, 9)

Menu.OpenMenu(player)