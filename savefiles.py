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

with open('saves.json', 'r') as file:
	savedata = json.load(file)

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
