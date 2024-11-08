import tkinter as tk
from charactersitems import Weapon
from charactersitems import HealingItem
from charactersitems import MainCharacter

class Menu():
    def SelectItem(item, menuvar):
        menuvar.set(item)

    def Confirm(window, item, prompt):
        global confirmbuttons
        global ask
        menuvar = tk.StringVar()
        for button in menubuttons:
            button.destroy()
        if prompt == 'select':
            ask = tk.Label(window, text=f'Would you like to select the {item.name}?')
        elif prompt == 'end':
            ask = tk.Label(window, text='Would you like to close the menu?')
        elif prompt == 'shop':
            ask = tk.Label(window, text=f'Would you like to purchase the {item.name}')
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
        global menubuttons
        menuvar = tk.IntVar()
        menubuttons = []

        for index, item in enumerate(player.inventory):
            menubutton = tk.Button(window, text=item.name, command=lambda i=index: Menu.SelectItem(i, menuvar))
            menubutton.pack()
            menubuttons.append(menubutton)
        
        window.update()
        window.wait_variable(menuvar)
        index = menuvar.get()
        item = player.inventory[index]
        return item
    
    def Inventory(window, player):
        finish = False
        while finish == False:
            item = Menu.Inventory1(window, player)
            confirm = Menu.Confirm(window, item, 'select')
            if confirm == "YES":
                if isinstance(item, Weapon):
                    player.weapon = item
                    outcome = tk.Label(window, text=f'You equipped the {item.name}!')
                    for button in confirmbuttons:
                        button.destroy()
                        ask.destroy()
                    outcome.pack()
                    confirm = Menu.Confirm(window, item, 'end')
                    if confirm == 'YES':
                        finish = True
                        for button in confirmbuttons:
                            button.destroy()
                        outcome.destroy()
                        ask.destroy()
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
                    outcome.pack()
                    outcome2.pack()
                    for button in confirmbuttons:
                        button.destroy()
                        ask.destroy()
                    confirm = Menu.Confirm(window, item, 'end')
                    if confirm == 'YES':
                        finish = True
                        for button in confirmbuttons:
                            button.destroy()
                        outcome.destroy()
                        outcome2.destroy()
                        ask.destroy()
                        break
                    elif confirm == 'NO':
                        for button in confirmbuttons:
                            button.destroy()
                        outcome.destroy()
                        outcome2.destroy()
                        ask.destroy()
            elif confirm == 'NO':
                for button in confirmbuttons:
                    button.destroy()
                ask.destroy()

    def Shop(window, player):
        global menubuttons
        woodsword = Weapon('Wooden Sword', 5, 8192, 10)
        stonesword = Weapon('Stone Sword', 10, 15, 18)
        goldsword = Weapon('Gold Sword', 35, 6, 20)
        apple = HealingItem('Apple', 10, 5)
        healingpotion = HealingItem('Healing Potion', 35, 15)
        shopitems = [woodsword, stonesword, goldsword, apple, healingpotion]
        shopvar = tk.IntVar()  # stores a specific spot in the list of enemies, so we can call it
        menubuttons = [ ]
        finish = False
        while finish == False:
            for index, shopitem in enumerate(shopitems):
                shop_button = tk.Button(window, text=shopitem.name, command=lambda i=index: Menu.SelectItem(i, shopvar))
                shop_button.pack()
                menubuttons.append(shop_button)

            window.update()
            window.wait_variable(shopvar)
            index = shopvar.get()  
            item = shopitems[index]
            confirm = Menu.Confirm(window, item, 'shop')
            if confirm == 'YES':
                if player.gold >= item.cost:
                    player.PlayerPurchaseItem(item.cost, item)
                else:
                    poorhaha = tk.Label(window, text='You cannot purchase that item.')
                    poorhaha.pack()
                for button in confirmbuttons:
                    button.destroy()
                ask.destroy()
                confirm = Menu.Confirm(window, item, 'end')
                if confirm == 'YES':
                    for button in confirmbuttons:
                        button.destroy()
                    ask.destroy()
                    try:
                        poorhaha.destroy()
                    except:
                        pass
                    finish = True
                elif confirm == 'NO':
                    for button in confirmbuttons:
                        button.destroy()
                    ask.destroy()
            elif confirm == 'NO':
                for button in confirmbuttons:
                    button.destroy()
                ask.destroy()
        



    
window = tk.Tk()
window.title("Menu")

weapon = Weapon('weapon', 0, 10, 10)
apple = HealingItem('apple', 10, 10)
healingpot = HealingItem('healing potion', 10, 10)
goblinsword = Weapon('goblin sword', 100, 10, 10000000)

player = MainCharacter('name', 10, 10, 10, weapon, [weapon, apple, healingpot, goblinsword], 100, 0, 0)

Menu.Shop(window, player)
window.mainloop()