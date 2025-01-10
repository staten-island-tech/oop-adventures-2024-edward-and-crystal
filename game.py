from charactersitems import Character, MainCharacter, Enemy, BossEnemy, Grifter, Weapon, HealingItem
from battles import Battles
from menus import Menu
from movement import OpenWorld
from rooms import Room
from savefiles import SaveFileManager

name = SaveFileManager.save_or_load_file()

loadables= SaveFileManager.convert_json_to_player_object(name)
player = loadables[0]
room = loadables[1]
print(player.strength)