from charactersitems import MainCharacter

class Saves:
    def PlayerSaveFileReady(player):
        return {
            'name': player.name,
            'strength': player.strength,
            'maxhp': player.maxhp,
            'currenthp': player.currenthp,
            'gold': player.gold,
            'inventory': player.inventory
        }

    def PlayerCreateSave(self):
        import json
        savefile = self.PlayerSaveFileReady()
        with open('charactersave.json', 'w') as file:
            json.dump(savefile, file)

    def PlayerLoadSave(self): 
        import json
        with open('charactersave.json', 'r') as file:
            sf = json.load(file)
            # sf is short for savefile
        player = MainCharacter(sf['name'], sf['strength'], sf['maxhp'], sf['currenthp'], sf['gold'], sf['inventory'])
        return player   
    
