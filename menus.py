import tkinter as tk
from charactersitems import Weapon
from charactersitems import HealingItem
from charactersitems import MainCharacter

class Menu():
    def SelectItem(item, menuvar):
        menuvar.set(item)

    def SelectConfirm(window, item):
        global confirmbuttons
        global ask
        menuvar = tk.StringVar()
        for button in menubuttons:
            button.destroy()
        ask = tk.Label(window, text=f'Would you like to select the {item.name}?')
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
            confirm = Menu.SelectConfirm(window, item)
            if confirm == "YES":
                if isinstance(item, Weapon):
                    player.weapon = item
                    outcome = tk.Label(window, text=f'You equipped the {item.name}!')
                    for button in confirmbuttons:
                        button.destroy()
                        ask.destroy()
                    outcome.pack()
                    finish = True
                if isinstance(item, HealingItem):
                    player.PlayerHeal(item.heal)
                    outcome = tk.Label(window, text=f'You consumed the {item.name}!')
                    outcome2 = tk.Label(window, text=f'You now have {player.currenthp} HP!')

                    for button in confirmbuttons:
                        button.destroy()
                        ask.destroy()
                    outcome.pack()
                    outcome2.pack()
                    finish = True
            elif confirm == 'NO':
                for button in confirmbuttons:
                    button.destroy()
                ask.destroy()
        


    
window = tk.Tk()
window.title("Menu")

weapon = Weapon('weapon', 0, 10, 10)
apple = HealingItem('apple', 10, 10)
healingpot = HealingItem('healing potion', 10, 10)

player = MainCharacter('name', 10, 10, 10, weapon, [weapon, apple], 0, 0, 0)

Menu.Inventory(window, player)
window.mainloop()