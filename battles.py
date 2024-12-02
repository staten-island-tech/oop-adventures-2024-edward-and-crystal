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
    def DrawActionButton(action, events):
        if action == 'ATTACK':
            buttonrect = pygame.Rect((220, 635, 150, 50))
        elif action == 'BLOCK':
            buttonrect = pygame.Rect((380, 635, 150, 50))
        elif action == 'FLEE (coward)':
            buttonrect = pygame.Rect((540, 635, 150, 50))
        mousepos = pygame.mouse.get_pos()
        if buttonrect.collidepoint(mousepos):
            color = (50, 50, 65)
        else:
            color = (25, 25, 32.5)
        
        pygame.draw.rect(screen, color, buttonrect)
        menufont = pygame.font.Font(None, 30)
        actiontext = menufont.render(action, True, (255, 255, 255))
        actionsurface = actiontext.get_rect(center=buttonrect.center)
        screen.blit(actiontext, actionsurface)
        
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and buttonrect.collidepoint(mousepos):
                print(action)
    
    def MakeEnemies(enemies):
        pass
    
    def BattleMenu(player, enemies):
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
            
            menufont = pygame.font.Font(None, 30)
            healthbar = pygame.Rect((10, 645, 200, 30))
            nameunderhealthbarrect = pygame.Rect((10, 675, 200, 30))
            pygame.draw.rect(screen, (75, 100, 125), (5, 640, 210, 40))
            pygame.draw.rect(screen, (25, 25, 32.5), healthbar)
            if hppercentage < .30:
                uhohtext = menufont.render("!!!!!!!!!!!!!!!!!!!!!!!!!!!", True, (120, 120, 130))
                uhohsurface = uhohtext.get_rect(center=healthbar.center)
                screen.blit(uhohtext, uhohsurface)
            
            pygame.draw.rect(screen, (100, 110, 140), (10, 645, 200*hppercentage, 30))
        
            hptext = menufont.render(f"{player.currenthp} / {player.maxhp} HP", True, (255, 255, 255))
            hpsurface = hptext.get_rect(center=healthbar.center)
            
            nameunderhealthbartext = menufont.render(player.name, True, 36)
            nameunderhbsurface = nameunderhealthbartext.get_rect(center=nameunderhealthbarrect.center)
            
            screen.blit(nameunderhealthbartext, nameunderhbsurface)
            screen.blit(hptext, hpsurface)
            
            Battles.DrawActionButton("ATTACK", events)
            Battles.DrawActionButton("BLOCK", events)
            Battles.DrawActionButton("FLEE (coward)", events)
            Battles.MakeEnemies(enemies)
            
            pygame.display.update()      
                
player = MainCharacter('edward', 100, 40, 20, 'nothing', [], 100, 10, 1) 
enemies = ['hi', 'hi', 'hi']
Battles.BattleMenu(player, enemies)