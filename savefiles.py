import json
# from items import wooden_sword need to add the file

try:
	with open('saves.json', 'r') as file:
		savedata = json.load(file)
except(FileNotFoundError, json.JSONDecodeError):
	savedata = []
	with open('saves.json', 'w') as file:
		json.dump(savedata, file, indent=2)

class SaveFileManager:
	def __init__(self):
		pass #done so I can call this class's functions in other functions also in the class

	def save_or_load_file(self):
		#strip removes all spaces before or after the letters (not the spaces in between words)
		answer = input('Do you want to create a file or load a new one?').strip().lower()
		while True:
			if answer == 'create':
				self.create_savefile()
				break
			elif answer == 'load':
				self.load_savefile()
				break
			else:
				print('Invalid Answer. Please try again!')
				
	def dump_savefile_to_json(self, name):
		
		blank_player_data = {
			"name": name,
			"maxhp": 100,
			"currenthp": 100,
			"strength": 0,
			"weapon": "wooden_sword", 
			"inventory": ['wooden_sword'],
			"gold": 0,
			"level": 1,
			"exp": 0
		}

		savedata.append(blank_player_data)
		
		# update the json file with the new blank player data
		with open('saves.json', 'w') as file:
			json.dump(savedata, file, indent=2)
	''
	def create_savefile(self):
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
			self.dump_savefile_to_json(name)
			print('File sucessfully created')
			break
		
	def load_savefile(self):
	
		lookingforsave = True

		while lookingforsave:
			savefound = False

			print('\nHere are all the save file names:\n') 

			#prints all savefile names
			for savefile in savedata: 
				print(savefile['name'])
			
			name = input('\nWhich save would you like to open?').upper().strip() 

			for savefile in savedata:
				if savefile['name'].upper() == name:
					chosensave = savefile
					savefound = True
				else:
					print('\nInvalid Answer. Please try again.')
					self.load_savefile()
						
				if savefound == True:
					if savefile == chosensave:

						#for better formatting. format: Key: pair, with each key value pair on a new line. EX: Weapon: wooden_sword
						for key, value in chosensave.items():
						
							#converts the inventory (a list) into a string to remove the brackets and quotes when printing, aka to make it look better
							if isinstance(value, list):  
								value = ", ".join(value)  
							print(f'{key.capitalize()}: {value}')

					confirm = input('Is this the save you would like to open? Y/N')
					if confirm.upper() == 'Y':
						lookingforsave = False
						return chosensave
		#when you call this function, you set the player values, coordinates, and room number equal to the values in the save file 
		
	def update_savefile(self):
		#need to make the MainCharacter data into a dictionary to replace the savefile that has its name
		from rooms import player
		playerdict = player.__dict__
		print(playerdict)
		pass
		
		
test = SaveFileManager()

test.update_savefile()