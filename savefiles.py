#TO DO: LOADING SAVE DATA TO A JSON FILE

import json
# from items import wooden_sword need to add the file

try:
	with open('saves.json', 'r') as file:
		savedata = json.load(file)
except(FileNotFoundError, json.JSONDecodeError):
	savedata = []

class SaveFileManager:
	def __init__(self):
		pass #done so I can call this class's functions in other functions also in the class

	def save_or_load_file(self):
		#strip removes all spaces before or after the letters (not the spaces in between words)
		answer = input('Do you want to create a file or load a new one?').strip().lower()

		if answer == 'create':
			name = input('What do you want to name your save file?').strip()
			self.make_savefile(name)
		elif answer == 'load':
			self.select_savefile()
		else:
			print('Invalid Answer. Please try again!')
			self.save_or_load_file() #forces them to answer load or save 

	def make_savefile(self, name):
		
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
	def select_savefile(self):

		lookingforsave = True

		while lookingforsave:
			savefound = False

			print('\nHere are all the save file names:\n') #\n skips a line. done for better formatting

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
					self.select_savefile()
						
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
		
		
test = SaveFileManager()

test.save_or_load_file()