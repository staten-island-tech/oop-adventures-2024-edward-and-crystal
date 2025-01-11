import json
from charactersitems import HealingItem, Weapon, MainCharacter

#hi, edward, the way i coded it isn't very intuitive so i put actual documentation in the form of docstrings for the functions you'll have to use

try:
	with open('saves.json', 'r') as file:
		savedata = json.load(file)
except(FileNotFoundError, json.JSONDecodeError):
	savedata = []
	with open('saves.json', 'w') as file:
		json.dump(savedata, file, indent=2)

class SaveFileManager:
	def save_or_load_file():
		'''
		Prompts the player to load a save file or create a new one

		Returns:
			-Save File Name
		'''
		#strip removes all spaces before or after the letters (not the spaces in between words)
	
		while True:
			answer = input('Do you want to create a file or load one?').strip().lower()
			if answer == 'create':
				name = SaveFileManager.create_savefile()
				break
			elif answer == 'load':
				name = SaveFileManager.load_savefile()
				break
			else:
				print('Invalid Answer. Please try again!')
		return name
	
	def dump_savefile_to_json(name):
		blank_player_data = {
			"name": name,
			"maxhp": 20,
			"currenthp": 20,
			"strength": 6,
			"weapon": Weapon('NONE', 0, 8192, 0).WeaponDictionary(),
			"inventory": [],
			"gold": 0,
			"level": 1,
			"exp": 0,
			"room": 0
		}

		savedata.append(blank_player_data)
		
		# update the json file with the new blank player data
		with open('saves.json', 'w') as file:
			json.dump(savedata, file, indent=2)
	
	''
	def create_savefile():
		while True:
			if savedata: #runs the code if the list isnt empty
				print("\nThese are the taken names. You can't name your save file any of these names\n")
				#prints all savefile names
				for savefile in savedata:
					print(savefile['name']) #\n skips a line. done for better formatting
				print() # skips a line for better formatting

			name = input('What do you want to name your save file?').strip()

			if name == '':
				print("Blank save file name. Please try again.")
				continue
			
			#checks if the chosen name matches any of savefile's names
			if any(savefile['name'].upper() == name.upper() for savefile in savedata):
				print('\nA save file already has this name. Please try again')
				continue
			
			#if it's a valid answer, make a save file
			SaveFileManager.dump_savefile_to_json(name)
			print('File sucessfully created')
			return name
		
	def load_savefile():
	
		lookingforsave = True

		while lookingforsave:
			savefound = False

			if len(savedata) == 0:
				print('There are no save files. You must create one.')
				SaveFileManager.create_savefile()
				break

			print('\nHere are all the save file names:\n') 

			#prints all savefile names
			for savefile in savedata: 
				print(savefile['name'])
			
			name = input('\nWhich save would you like to open?').strip() 

			for savefile in savedata:
				if savefile['name'].upper() == name.upper():
					chosensave = savefile
					savefound = True
					break
			if not savefound:
				print('\nInvalid Answer. Please try again.')
				
			if savefound:
				if savefile == chosensave:
					#for better formatting. format: Key: pair, with each key value pair on a new line. EX: Weapon: wooden_sword
					for key, value in chosensave.items():
						print(f'{key.capitalize()}: {value}')

				confirm = input('Is this the save you would like to open? Y/N')
				if confirm.upper() == 'Y':
					lookingforsave = False
					print("CHECK THE PYGAME WINDOW. ok thanks :)")
					return name
				
		#when you call this function, you set the MainCharacter object's values equal to the values in the savefiles 
		
	def update_savefile(playerdict, room_number):
		'''
		Updates the player's savefile from the json file
		
		Args:
			-The player's dictionary. (Do [insert whatever you named the payer object].__dict__)
			-Room Number
		'''

		savefile_dict = playerdict

		savefile_dict['room'] = room_number 
		del playerdict['dead']
		print(savefile_dict)
		found = False
		#load it as dicts
		for savefile in savedata:
			if savefile_dict['name'] == savefile['name']:
				savefile.update(savefile_dict)
				found = True
				break

			if found:
				savedata.append(playerdict)

		with open('saves.json', 'w') as file:
			json.dump(savedata, file, indent=2)
  
		#need to update the playerdata witht he new items

	def delete_savefile(playerdict):
		'''
		Deletes the player's savefile from the json file

		Arg:
			-The player's dictionary. (Do [insert whatever you named the payer object].__dict__)
		'''
		#find user save file and delete
		for savefile in savedata:
			if playerdict['name'] == savefile['name']:
				savedata.remove(savefile)
		with open('saves.json', 'w') as file:
			json.dump(savedata, file, indent=2)	

	def convert_json_to_player_object(name):
		'''
		Uses the data from player's savefile from the json file to create a player object

		Arg:
			-Save File Name
		
		Returns:
			-[player_object, room_number]
		'''
		#NAME IS THE SAVEFILE NAME
		#THIS CONVERTS THE PLAYER DICT FROM THE SAVE FILE INTO A PLAYER OBJECT
		for savefile in savedata:
			try:
				if savefile['name'].upper() == name.upper():
					playerdict = savefile
					room = savefile['room']
					del playerdict['room']
					player = MainCharacter(**playerdict)
					player.inventory = SaveFileManager.convert_json_to_inventory(name)
					return [player, room] #you have to make the room object's room number the room number in here. 
			except AttributeError:
				pass #alas, 
			
	def convert_json_to_inventory(savefile_name):
		#converts the item dicts in the savefile into objects
		for savefile in savedata:
			if savefile['name'].upper() == savefile_name.upper():
				json_inventory = savefile['inventory']
				player_object_inventory = []
				for item in json_inventory:
					print(type(item))
					if 'strength' in item:
						weapon = Weapon(**item)
						player_object_inventory.append(weapon)
					else:
						healing_item = HealingItem(**item)
						player_object_inventory.append(healing_item)
				return player_object_inventory

	def convert_inventory_to_dicts(inventory):
		dictinventory = []
		for item in inventory:
			if isinstance(item, Weapon):
				dictinventory.append({
					'name' : item.name,
                    'strength' : item.strength,
                    'durability' : item.durability,
                    'cost' : item.cost
				})
			elif isinstance(item, HealingItem):
				dictinventory.append({
					'name' : item.name,
                    'heal' : item.heal,
                    'cost' : item.cost
				})
    
		return dictinventory