from charactersitems import Character
from charactersitems import MainCharacter
from charactersitems import Enemy
from charactersitems import BossEnemy
from charactersitems import Grifter
import pygame
pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Game')
battle = True
running = True

class Battles:
    def BattleMenu(player):
        global running
        running = False
        while battle:
            screen.fill((20, 20, 25))
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            
            pygame.draw.rect(screen, (200, 220, 240), (0, 620, 1280, 200))
            
            hppercentage = player.currenthp / player.maxhp
            
            healthbar = pygame.Rect((10, 645, 200, 30))
            nameunderhealthbarrect = pygame.Rect((10, 675, 200, 30))
            
            pygame.draw.rect(screen, (25, 25, 32.5), healthbar)
            pygame.draw.rect(screen, (100, 110, 140), (10, 645, 200*hppercentage, 30))
            
            menufont = pygame.font.Font(None, 30)
            hptext = menufont.render(f"{player.currenthp} / {player.maxhp} HP", True, (255, 255, 255))
            hpsurface = hptext.get_rect(center=healthbar.center)
            
            nameunderhealthbartext = menufont.render(player.name, True, 36)
            nameunderhbsurface = nameunderhealthbartext.get_rect(center=nameunderhealthbarrect.center)
            
            screen.blit(nameunderhealthbartext, nameunderhbsurface)
            
            screen.blit(hptext, hpsurface)
                    
            pygame.display.update()      
                
player = MainCharacter('edward', 100, 75, 20, 'nothing', [], 100, 10, 1) 
Battles.BattleMenu(player)