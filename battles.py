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
    def DrawActionButton(player, enemies, action, events):
        global wasactiondone
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
                if action == 'FLEE (coward)':
                    Battles.FleeCoward(player)
                    wasactiondone = True
                elif action == 'ATTACK':
                    Battles.Attack(player, enemies)
                    wasactiondone = True
                else:
                    Battles.Block(player, enemies)
                    wasactiondone = True
                
    def FleeCoward(player):
        global battle
        import random
        chancetoflee = 100 - (100*(player.currenthp / player.maxhp))
        if chancetoflee < 35:
            chancetoflee = 35
            
        areyarunning = random.randint(1, 100)
        if areyarunning >= chancetoflee:
            battle = False
            
    def Attack(player, enemies):
        print(player.name)
    # make a makeshift for loop that waits for confirm buttons to be pressed
    
    def Block(player, enemies):
        for enemy in enemies:
            print(enemy.name)
    
    def MakeEnemies(enemies):
        xcoordinate = 0
        for enemy in enemies:
            if isinstance(enemy, Enemy):
                pygame.draw.circle(screen, (200, 90, 75), (xcoordinate+75, 200), 50)
                pygame.draw.line(screen, (200, 90, 75), (xcoordinate+75, 225), (xcoordinate+75, 340), 35)
                pygame.draw.line(screen, (200, 90, 75), (xcoordinate+75, 340), (xcoordinate+35, 400), 30)
                pygame.draw.line(screen, (200, 90, 75), (xcoordinate+75, 340), (xcoordinate+115, 400), 30)
                pygame.draw.line(screen, (200, 90, 75), (xcoordinate+35, 400), (xcoordinate+35, 425), 30)
                pygame.draw.line(screen, (200, 90, 75), (xcoordinate+115, 400), (xcoordinate+115, 425), 30)
                pygame.draw.line(screen, (200, 90, 75), (xcoordinate+75, 225), (xcoordinate+35, 340), 27)
                pygame.draw.line(screen, (200, 90, 75), (xcoordinate+75, 225), (xcoordinate+115, 340), 27)
            elif isinstance(enemy, BossEnemy):
                xcoordinate += 30
                pygame.draw.circle(screen, (150, 50, 55), (xcoordinate+75, 150), 70)
                pygame.draw.line(screen, (150, 50, 55), (xcoordinate+75, 210), (xcoordinate+75, 320), 50)
                pygame.draw.line(screen, (150, 50, 55), (xcoordinate+75, 320), (xcoordinate+35, 405), 45)
                pygame.draw.line(screen, (150, 50, 55), (xcoordinate+75, 320), (xcoordinate+115, 405), 45)
                pygame.draw.line(screen, (150, 50, 55), (xcoordinate+35, 405), (xcoordinate+35, 435), 47)
                pygame.draw.line(screen, (150, 50, 55), (xcoordinate+115, 405), (xcoordinate+115, 435), 47)
                pygame.draw.line(screen, (150, 50, 55), (xcoordinate+75, 210), (xcoordinate+25, 360), 42)
                pygame.draw.line(screen, (150, 50, 55), (xcoordinate+75, 210), (xcoordinate+125, 360), 42)
            
            # make this its own function 
            nametagrect = pygame.Rect(xcoordinate+15, 450, 120, 40)
            listname = len((enemy.name))
            if listname < 7:
                nametagfont = pygame.font.Font(None, 36)
            elif listname > 6 and listname < 10:
                nametagfont = pygame.font.Font(None, 28)
            elif listname > 9 and listname < 15:
                nametagfont = pygame.font.Font(None, 21)
            else:
                nametagfont = pygame.font.Font(None, 16)
            nametagtext = nametagfont.render(f'{enemy.name}', True, (225, 10, 10))
            nametagsurface = nametagtext.get_rect(center=nametagrect.center)
            pygame.draw.rect(screen, (30, 30, 37.5), nametagrect)
            screen.blit(nametagtext, nametagsurface)
            xcoordinate += 150
            if isinstance(enemy, BossEnemy):
                xcoordinate +=30
    
    def BattleMenu(player, enemies):
        global wasactiondone, running
        running = False
        wasactiondone = False
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
            
            if wasactiondone == False:
                Battles.DrawActionButton(player, enemies, "ATTACK", events)
                Battles.DrawActionButton(player, enemies, "BLOCK", events)
                Battles.DrawActionButton(player, enemies, "FLEE (coward)", events)
            
            Battles.MakeEnemies(enemies)
            
            pygame.display.update()      
                
player = MainCharacter('edward', 100, 90, 20, 'nothing', [], 100, 10, 1) 
goblin = Enemy('GoblinAAA', 1, 1, 1, 1, 1, 1, 1)
goblina = Enemy('Goblin', 1, 1, 1, 1, 1, 1, 1)
goblinb = BossEnemy('GoblinAAAAAAAAAA', 1, 1, 1, 1, 1)
goblinc = Enemy('Goblin', 1, 1, 1, 1, 1, 1, 1)
goblind = Enemy('Goblin', 1, 1, 1, 1, 1, 1, 1)
enemies = [goblin, goblina, goblinb, goblinc, goblind]
Battles.BattleMenu(player, enemies)