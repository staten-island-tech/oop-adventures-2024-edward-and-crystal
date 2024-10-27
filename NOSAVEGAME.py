from charactersitems import Character
from charactersitems import Enemy
from charactersitems import MainCharacter
from charactersitems import BossEnemy
from charactersitems import Weapon
from charactersitems import HealingItem
from battlesandmenus import BattleInteractions
from battlesandmenus import Menu

print('welcome to the dungeon. man.')
name = input('what is your name')
woodensword = Weapon('Wooden Sword', 5, 8192, 10)

player = MainCharacter(name, 100, 100, 10, woodensword, [ ], 0)

