import json
from charactersitems import Weapon
try:
    with open('saves.json', 'r') as file:
        savedata = json.load(file)
except(FileNotFoundError, json.JSONDecodeError):
    savedata = []
    with open('saves.json', 'w') as file:
        json.dump(savedata, file, indent=2)

class SaveFileManager:
    def save_or_load_file():
        #strip removes all spaces before or after the letters (not the spaces in between words)
    
        while True:
            answer = input('Do you want to create a file or load a new one?').strip().lower()
            if answer == 'create':
                SaveFileManager.create_savefile()
                break
            elif answer == 'load':
                SaveFileManager.load_savefile()
                break
            else:
                print('Invalid Answer. Please try again!')
                
    def dump_savefile_to_json(name):

        blank_player_data = {
            "name": name,
            "maxhp": 25,
            "currenthp": 25,
            "strength": 5,
            "weapon": Weapon('NONE', 0, 8192, 0), 
            "inventory": [ ],
            "gold": 0,
            "level": 1,
            "exp": 0,
            "room": 1, 
            "coordinates": None
        }
        #depending on how the attack damage is calculated, might need to make the inventory have dicts with item stats

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
            break
        
    def load_savefile():
    
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
                    SaveFileManager.load_savefile()
                        
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
        #when you call this function, you set the MainCharacter object's values equal to the values in the savefiles 
        
    def update_savefile(playerdict, playercoords, room_number):
        #edward, in the place you run the code, write playerdict = player.__dict__ (make sure your MainCharacter object is called player)
        #i can't do it here because of import errors....

        #these two lines create key-value pairs in the playerdict (main character object aka the player doesnr have these as attributes)
        playerdict['coordinates'] = playercoords
        playerdict['room'] = room_number

        for savefile in savedata:
            if playerdict['name'] == savefile['name']:
                savefile.update(playerdict)
                break
        with open('saves.json', 'w') as file:
            json.dump(savedata, file, indent=2 ) 
        #need to update the playerdata witht he new items

    def delete_savefile(playerdict):
        #find user save file and delete
        for savefile in savedata:
            if playerdict['name'] == savefile['name']:
                savedata.remove(savefile)
        with open('saves.json', 'w') as file:
            json.dump(savedata, file, indent=2) 