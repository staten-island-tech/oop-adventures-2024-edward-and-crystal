from charactersitems import Character, MainCharacter, Enemy, BossEnemy, Grifter, Weapon, HealingItem
from battles import Battles
from menus import Menu
from movement import OpenWorld
from savefiles import SaveFileManager
from rooms import Room
import pygame

print('hello')

name = SaveFileManager.save_or_load_file()

loadables = SaveFileManager.convert_json_to_player_object(name)

player = loadables[0]
roomnumber = loadables[1]
player.inventory = SaveFileManager.convert_json_to_inventory(player.name)
player.weapon = Weapon(player.weapon['name'], player.weapon['strength'], player.weapon['durability'], player.weapon['cost'])

room = Room(roomnumber)
rphbi = []
number = 0
while number <= room.room_number:
    rphbi.append(number)
    number += 1

room.LoadRoom(player, rphbi)