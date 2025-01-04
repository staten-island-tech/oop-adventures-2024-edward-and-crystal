import json



def make_savefile(name):
	try:
		with open('saves.json', 'r') as file:
			savedata = json.load(file)
	except(FileNotFoundError, json.JSONDecodeError):
		savedata = []
	
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

make_savefile('k')