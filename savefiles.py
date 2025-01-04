#TO DO: LOADING SAVE DATA TO A JSON FILE

import json
# from items import wooden_sword need to add the file

try:
	with open('saves.json', 'r') as file:
		savedata = json.load(file)
except(FileNotFoundError, json.JSONDecodeError):
	savedata = []

def make_savefile(name):
	
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
	savedata.append(blank_player_data)
    
    # Write the updated save data back to the file
	with open('saves.json', 'w') as file:
		json.dump(savedata, file, indent=2)
''
def find_savefile():
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

	#then you set the player values, coordinates, and room number equal to the values in the save file in the place where you call this function

	
	
find_savefile()