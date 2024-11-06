from battles import BattleInteractions
from charactersitems import Weapon
from charactersitems import BossEnemy
from charactersitems import Enemy
from charactersitems import MainCharacter

club = Weapon('club', 10, 1000, 0)
player = MainCharacter('player', 100, 100, 10, club, [], 0, 0, 10)
goblin = Enemy('GOBLIN', 15, 15, 0, club, 10, 'nothing', 10)
goblinb = Enemy('GOBLIN2', 15, 15, 0, club, 10, 'nothing', 10)
boss = Enemy('BOSS', 80, 80, 10, club, 10, 'nothing', 1000)
enemies = [boss, goblin, goblinb]

BattleInteractions.BossBattle(player, enemies)
import tkinter as tk
import random

window = tk.Tk()
window.title("MATH!")
window.geometry('400x200')

def Block(player):
    pass
def Attack(player):
    pass

button1 = tk.Button(window, text="Add", command=Block)
button1.pack(side="left")

button2 = tk.Button(window, text="Subtract", command=Attack)
button2.pack(side="left")


# i do have to recode the entire game...

# what an unfortunate time...

# born to code but not on this stupid stuff forced to code on this stupid stuff

# buttons? more like (i will finish the joke if you were to ask actually i would prefer not to bc i dont need these words coming out of my mouth in this context)