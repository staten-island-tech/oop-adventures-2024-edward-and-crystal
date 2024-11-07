import tkinter as tk
from charactersitems import Weapon
from charactersitems import HealingItem
from charactersitems import MainCharacter

class Menu():
    def SelectItem(item, menuvar):
        menuvar.set(item)

    def SelectConfirm(window, selecteditem):
        menuvar = tk.StringVar()

        ask = tk.Label(window, text=f"Would you like to select the {selecteditem.name}?")
        yes_button = tk.Button(window, text="Yes", command=lambda: Menu.SelectItem('YES', menuvar))
        no_button = tk.Button(window, text="No", command=lambda: Menu.SelectItem("NO", menuvar))

        ask.pack()
        yes_button.pack()
        no_button.pack()
        window.update()
        window.wait_variable(menuvar)
        return menuvar
    
    def Inventory1(window, player):
        global menubuttons
        menuvar = tk.IntVar()
        menubuttons = [ ]

        for index, item in enumerate(player.inventory):
            menubutton = tk.Button(window, text=item.name, command=lambda i=index: Menu.SelectConfirm(i, item))
            menubutton.pack()
            menubuttons.append(menubutton)
        
        window.update()
        window.wait_variable(menuvar)
        for button in menubuttons:
            button.destroy()
        
        return menuvar.get()
    
    def Inventory2(window, player):
        item = Menu.Inventory1(window, player)
        confirm = Menu.SelectConfirm(window, item)
        if confirm == "YES":
            print('why')
        elif confirm == "NO":
            print('how')
    
window = tk.Tk()
window.title("Battle Mode")

weapon = Weapon('weapon', 0, 10, 10)
apple = HealingItem('apple', 10, 10)

player = MainCharacter('name', 10, 10, 10, weapon, [weapon, apple], 0, 0, 0)

Menu.Inventory2(window, player)
window.mainloop()