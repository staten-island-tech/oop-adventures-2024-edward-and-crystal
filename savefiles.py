'''name, maxhp, currenthp, strength, weapon, inventory, gold, level, exp, room, coordinates
so you would need a function that converts the player object into a dictionary and then use the with open(blahblahblyuh) business to write it into a json file
and then when you load the game it makes a player object and then loads the room with those coordinates
yeah 
uh
to save me time i will just do this part in the terminal
basically a while loop that does the save data:'''

#TO DO: LOADING SAVE DATA TO A JSON FILE

import json
from charactersitems import MainCharacter
from rooms import Room
# from items import wooden_sword need to add the file
import sys




def make_savefile(name):
	
	with open('saves.json', 'r') as file:
		savedata = json.load(file)
	print('AAAAAAAAAAAAAAAAAAAAAAAA')

	blank_player_data = {
		"name": name,
		"maxhp": 100,
		"currenthp": 100,
		"strength": 0,
		"weapon": "wooden_sword", 
		"inventory": [],
		"gold": 0,
		"level": 1,
		"exp": 0
	}
	try:
		with open('saves.json', 'r') as file:
            savedata = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        # If file doesn't exist or is empty, create a new list for saves
        savedata = []

    # Append the new blank player data to the savedata list
    savedata.append(blank_player_data)
    
    # Write the updated save data back to the file
    with open('saves.json', 'w') as file:
        json.dump(savedata, file, indent=2)

    print(f"Save created for {name}")

def load_savefile():
	lookingforsave = True

	while lookingforsave:
		savefound = False
		confirmed = False

	name = input('Whose save would you like to open?')

	for savefile in savedata:
		if savefile['name'].upper() == name.upper():
				chosensave = savefile
				savefound = True
		if savefound == True:
			print()
			# print all the data of this save im too lazy to type it out
			confirm = input('Is this the save you would like to open? Y/N')
			if confirm.upper() == 'Y':
				lookingforsave = False

	player = MainCharacter(savefile['name'], savefile['maxhp'], savefile['currenthp'], savefile['strength'], savefile['weapon'], savefile['inventory'], savefile['gold'], savefile['level'], savefile['exp'])
	room = savefile['room']
	coordinates = savefile['coordinates']

	room = Room(savefile['room'])

	room.LoadRoom(player, coordinates)

make_savefile('hi')
print("Running script: script_name.py")
