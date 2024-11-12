import tkinter as tk
from charactersitems import Weapon
from charactersitems import HealingItem
from charactersitems import MainCharacter

class Menu():
    def SelectItem(item, menuvar):
        menuvar.set(item)

# so let me just explain how the prompt variable works
# this code does the same thing but grammar and player understanding would be weird if i dont have it
# (example, would you like to close the menu? even tho you are using an item)
# so prompt is just a variable that allows me not to recreate the function over and over again :)
# also for the prompts that dont involve fstrings i just put a random item, typically whatever is assigned to the
# item variable in the function at that point
# yeah 
# dooodledootdooooo
# do do dunn dunn duuuunn
# ba boo sh doodle loot do ! ! !! !! !!!! ! !! (BAMMM)
    def Confirm(window, item, prompt):
        global confirmbuttons
        global ask
        menuvar = tk.StringVar()
    
        for button in menubuttons:
            button.destroy()
    
        if prompt == 'selectweapon':
            ask = tk.Label(window, text=f'Would you like to equip the {item.name}?')
        elif prompt == 'selectheal':
            ask = tk.Label(window, text=f'Would you like to consume the {item.name}?')
        elif prompt == 'end':
            ask = tk.Label(window, text='Would you like to close the menu?')
        elif prompt == 'shop':
            ask = tk.Label(window, text=f'Would you like to purchase the {item.name}?')
        elif prompt == 'return':
            ask = tk.Label(window, text='Would you like to return to the main menu?')  
    
        yes_button = tk.Button(window, text="Yes", command=lambda: Menu.SelectItem('YES', menuvar))
        no_button = tk.Button(window, text="No", command=lambda: Menu.SelectItem("NO", menuvar))
    
        confirmbuttons = [yes_button, no_button]
    
        ask.pack()
        yes_button.pack()
        no_button.pack()
        window.update()

        window.wait_variable(menuvar)
        menu = menuvar.get()
        return menu
    
    def Inventory1(window, player):
        global returnbutton
        global menubuttons
        menuvar = tk.IntVar()
        menubuttons = []

        for index, item in enumerate(player.inventory):
            menubutton = tk.Button(window, text=item.name, command=lambda i=index: Menu.SelectItem(i, menuvar))
            menubutton.pack()
            menubuttons.append(menubutton)
        returnbutton = tk.Button(window, text='Return To Menu', command=lambda: Menu.ShopReturn())
        returnbutton.pack()
        
        window.update()
        window.wait_variable(menuvar)
        returnbutton.destroy()
        index = menuvar.get()
        item = player.inventory[index]
        return item
    
    def Inventory(window, player):
        window.title('Menu: Inventory')
        for button in buttons:
            button.destroy()
        finish = False
        while finish == False:
            labels = [ ]
            item = Menu.Inventory1(window, player)
            if isinstance(item, Weapon):
                label1 = tk.Label(window, text=item.name)
                label2 = tk.Label(window, text=f'Strength: {item.strength}')
                if item.durability > 8000:
                    label3 = tk.Label(window, text=f'Durability: Infinite')
                else:
                    label3 = tk.Label(window, text=f'Durability: {item.durability}')
                labels.append(label1)
                labels.append(label2)
                labels.append(label3)
                for label in labels:
                    label.pack()
                confirm = Menu.Confirm(window, item, 'selectweapon')
            elif isinstance(item, HealingItem):
                label1 = tk.Label(window, text=item.name)
                label2 = tk.Label(window, text=f'Heals {item.heal} HP')
                labels.append(label1)
                labels.append(label2)
                for label in labels:
                    label.pack()
                confirm = Menu.Confirm(window, item, 'selectheal')
            if confirm == "YES":
                for label in labels:
                    label.destroy()
                if isinstance(item, Weapon):
                    player.weapon = item
                    outcome = tk.Label(window, text=f'You equipped the {item.name}!')
                    for button in confirmbuttons:
                        button.destroy()
                    ask.destroy()
                    outcome.pack()
                    confirm = Menu.Confirm(window, item, 'return')
                    if confirm == 'YES':
                        finish = True
                        for button in confirmbuttons:
                            button.destroy()
                        outcome.destroy()
                        ask.destroy()
                        Menu.PlayerMenu(window, player)
                        break
                    elif confirm == 'NO':
                        for button in confirmbuttons:
                            button.destroy()
                        outcome.destroy()
                        ask.destroy()
                if isinstance(item, HealingItem):
                    item.UseHealingItem(player)
                    if player.currenthp > player.maxhp:
                        player.currenthp = player.maxhp
                    player.inventory.remove(item)
                    outcome = tk.Label(window, text=f'You consumed the {item.name}!')
                    outcome2 = tk.Label(window, text=f'You now have {player.currenthp} HP!')
                    for button in confirmbuttons:
                        button.destroy()
                    outcome.pack()
                    outcome2.pack()
                    ask.destroy()
                    confirm = Menu.Confirm(window, item, 'return')
                    if confirm == 'YES':
                        finish = True
                        for button in confirmbuttons:
                            button.destroy()
                        outcome.destroy()
                        outcome2.destroy()
                        ask.destroy()
                        Menu.PlayerMenu(window, player)
                        break
                    elif confirm == 'NO':
                        for button in confirmbuttons:
                            button.destroy()
                        outcome.destroy()
                        outcome2.destroy()
                        ask.destroy()
            elif confirm == 'NO':
                for label in labels:
                    label.destroy()
                for button in confirmbuttons:
                    button.destroy()
                ask.destroy()
                returnbutton.destroy()

    def Shop(window, player):
        window.title('Menu: Shop')
        for button in buttons:
            button.destroy()
    
        global shopitems
        global menubuttons
        shopitems = []  
        menubuttons = []  
    
        woodsword = Weapon('Wooden Sword', 5, 8192, 10)
        stonesword = Weapon('Stone Sword', 10, 15, 18)
        goldsword = Weapon('Gold Sword', 35, 6, 20)
        apple = HealingItem('Apple', 10, 5)
        healingpotion = HealingItem('Healing Potion', 35, 15)
    
        shopitems = [woodsword, stonesword, goldsword, apple, healingpotion]
    
        returnbutton = tk.Button(window, text='Return To Menu', command=lambda: Menu.ShopReturn())
        menubuttons.append(returnbutton)
    
        shopvar = tk.IntVar()
    
        for index, shopitem in enumerate(shopitems):
            shop_button = tk.Button(window, text=shopitem.name, command=lambda i=index: Menu.SelectItem(i, shopvar))
            shop_button.pack()
            menubuttons.append(shop_button)
        returnbutton.pack()
    
        window.update()
        window.wait_variable(shopvar)
        index = shopvar.get()  
        item = shopitems[index]
        labels = [ ]
        if isinstance(item, Weapon):
                label1 = tk.Label(window, text=item.name)
                label2 = tk.Label(window, text=f'Strength: {item.strength}')
                if item.durability > 8000:
                    label3 = tk.Label(window, text='Durability: Infinite')
                else:
                    label3 = tk.Label(window, text=f'Durability: {item.durability}')
                label4 = tk.Label(window, text=f'Costs {item.cost} Gold')
                labels.append(label1)
                labels.append(label2)
                labels.append(label3)
                labels.append(label4)
                for label in labels:
                    label.pack()
        elif isinstance(item, HealingItem):
            label1 = tk.Label(window, text=item.name)
            label2 = tk.Label(window, text=f'Heals {item.heal} HP')
            label3 = tk.Label(window, text=f'Costs {item.cost} Gold')
            labels.append(label1)
            labels.append(label2)
            labels.append(label3)
            for label in labels:
                label.pack()
        confirm = Menu.Confirm(window, item, 'shop')
        if confirm == 'YES':
            for label in labels:
                label.destroy()
            if player.gold >= item.cost:
                player.PlayerPurchaseItem(item.cost, item)
                outcome = tk.Label(window, text=f'You purchased the {item.name}!')
                outcome.pack()
                newgold = tk.Label(window, text=f'Now you have {player.gold} Gold.')
                newgold.pack()
            else:
                outcome = tk.Label(window, text='You cannot purchase that item.')
                outcome.pack()
            for button in confirmbuttons:
                button.destroy()
            ask.destroy()
            confirm = Menu.Confirm(window, item, 'return')
            if confirm == 'YES':
                for button in confirmbuttons:
                    button.destroy()
                try:
                    newgold.destroy()
                except:
                    pass
                outcome.destroy()
                ask.destroy()
                Menu.PlayerMenu(window, player)
            elif confirm == 'NO':
                for button in confirmbuttons:
                    button.destroy()
                try:
                    newgold.destroy()
                except:
                    pass
                outcome.destroy()
                ask.destroy()
                Menu.Shop(window, player)

        elif confirm == 'NO':
            for label in labels:
                label.destroy()
            for button in confirmbuttons:
                button.destroy()
            ask.destroy()
            Menu.Shop(window, player)
    
    def ShopReturn():
        for button in menubuttons:
            button.destroy()
        Menu.PlayerMenu(window, player)


    def Stats(window, player):
        window.title(f"Menu: {player.name}'s Stats")
        for button in buttons:
            button.destroy()
        global statsvar
        global statsLabels

        statsvar = tk.StringVar

        name = player.name
        currenthp = player.currenthp
        maxhp = player.maxhp
        strength = player.strength
        item = player.weapon
        gold = player.gold
        level = player.level
        exp = player.exp
        
        nameLabel = tk.Label(window, text=name)
        strengthLabel = tk.Label(window, text=f'Strength: {strength}')
        levelLabel = tk.Label(window, text=f'Level {level}')
        expLabel = tk.Label(window, text=f'{exp} / 75 EXP')
        hpLabel = tk.Label(window, text=f'{currenthp} / {maxhp} HP')
        goldLabel = tk.Label(window, text=f'{gold} Gold')
        itemLabel = tk.Label(window, text=f'Weapon: {item.name}')
        returnbutton = tk.Button(window, text='Return to Menu', command=lambda: Menu.StatsReturn(window, player))

        statsLabels = [nameLabel, strengthLabel, levelLabel, expLabel, hpLabel, goldLabel, itemLabel, returnbutton]


        nameLabel.pack()
        strengthLabel.pack()
        levelLabel.pack()
        expLabel.pack()
        hpLabel.pack()
        goldLabel.pack()
        itemLabel.pack()
        returnbutton.pack()

    def StatsReturn(window, player):
        for label in statsLabels:
            label.destroy()
        Menu.PlayerMenu(window, player)

    def PutButtonsBack():
        for button in buttons:
            button.pack()
        
    def EndMenu():
        window.title('Game')
        for button in buttons:
            button.destroy()

    def PlayerMenu(window, player):
        window.title('Menu')
        global buttons
        try:
            returnbutton.destroy()
        except:
            pass
        stats = tk.Button(window, text=player.name, command=lambda: Menu.Stats(window, player))
        inventory = tk.Button(window, text='Inventory', command=lambda: Menu.Inventory(window, player))
        shop = tk.Button(window, text='Open Shop', command=lambda: Menu.Shop(window, player))
        close = tk.Button(window, text='Close Menu', command=lambda: Menu.EndMenu())

        buttons = [stats, inventory, shop, close]

        Menu.PutButtonsBack()
    
    
window = tk.Tk()
window.title("Menu")

weapon = Weapon('weapon', 10, 10, 10)
goldensword = Weapon('weapon', 30, 8, 10)
stonesword = Weapon('weapon', 20, 15, 10)
woodensword = Weapon('woodensword', 10, 8192, 0)

player = MainCharacter('edward', 100, 100, 20, weapon, [weapon, woodensword, stonesword, goldensword], 100, 0, 70)

for i in range(100):
    player.inventory.append(weapon)

scrollbar = tk.Scrollbar(window, orient="vertical", command=window.yview)
scrollbar.pack(side="right", fill="y")

# Configure the canvas
window.configure(yscrollcommand=scrollbar.set)
window.bind("<Configure>", lambda e: window.configure(scrollregion=window.bbox("all")))


Menu.PlayerMenu(window, player)

window.mainloop()