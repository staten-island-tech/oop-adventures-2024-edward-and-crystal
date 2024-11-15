from charactersitems import MainCharacter

class Saves:
    def PlayerSaveFileReady(player):
        return {
            'name': player.name,
            'strength': player.strength,
            'maxhp': player.maxhp,
            'currenthp': player.currenthp,
            'strength': player.strength,
            'weapon': player.weapon,
            'inventory': player.inventory,
            'gold': player.gold,
            'level': player.level,
            'exp': player.exp
        }
    
    def CreateSave(player):
        import json
        playerdictionary = player.PlayerSaveFileReady()
        with open('charactersave.json', 'r') as file:
            sfl = list(json.load(file)) # sfl means save files list
        for savefile in sfl:
            if savefile['name'] == playerdictionary['name']:
                confirm = input('Would you like to save the game? ')
                if confirm.upper() == "YES":
                        try:
                            sfl.remove(savefile)
                            sfl.append(playerdictionary)
                        except ValueError:
                            pass
            else:
                confirm = input('Would you like to save the game? ')
                if confirm.upper() == "YES":
                    sfl.append(playerdictionary)
                
        with open('charactersave.json', 'w') as file:
            json.dump(sfl, file)
    
    def LoadSave(player):
        import json
        with open('charactersave.json', 'r') as file:
            sfl = list(json.load(file))
        savesmenu = []
        for savefile in sfl:
            savesmenu.append(savefile)
        for item in savesmenu:
            print(item['name'])
        finish = False
        x = 0
        while finish == False:
            selectedsave = savesmenu[x]
            print(f"You are currently hovering over {selectedsave['name']}'s save.")
            confirm = input("Would you like to load this save? ")
            if confirm.upper() == 'YES':
                finish = True
                break
            else:
                move = input("Press Z to move up the menu and X to move down the inventory. ")
                if move.upper() == "Z":
                    if x != 0:
                        x -= 1
                    else:
                        x = len(savesmenu) - 1
                elif move.upper() == "X":
                    if x != len(savesmenu) - 1:
                        x += 1
                    else:
                        x = 0
                else:
                    print("That is not a valid input.") 

        name = selectedsave['name']
        maxhp = selectedsave['maxhp']
        currenthp = selectedsave['currenthp']
        strength = selectedsave['strength']
        weapon = selectedsave['weapon']
        inventory = list(selectedsave['inventory'])
        gold = selectedsave['gold']
        level = selectedsave['level']
        exp = selectedsave['exp']

        player = MainCharacter(name, maxhp, currenthp, strength, weapon, inventory, gold, level, exp)
        print(f"You have loaded {player.name}'s savefile!")
        return player
            

class OpenWorld:
    def IDontKnowWhatThe___IAmDoing(player):
        return True