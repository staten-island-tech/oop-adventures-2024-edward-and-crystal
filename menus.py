from charactersitems import Character
from charactersitems import MainCharacter
from charactersitems import Weapon
from charactersitems import HealingItem
import pygame
pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Menu')

class Menu:
    def DrawButtonMainMenu(buttontitle, events):
        # draws that circle in the background
        radius = 400
        color = (20, 20, 25)
        redness = color[0]
        greenness = color[1]
        blueness = color[2]
        
        # quick maths
        # 175 - 25 = 150 / 30 = 5
        # 110 - 20 = 90 / 30 = 3
        
        for circle in range(100):
            pygame.draw.circle(screen, color, (640, 700), radius)
            radius -= 2
            redness += 0.5
            greenness += 1
            blueness += 2
            color = (redness, greenness, blueness)
            
            
        
        # draws buttons
        if buttontitle == 'YOUR   STATS':
            buttonrect = pygame.Rect(0, 110, 500, 100) 
            if buttonrect.collidepoint(pygame.mouse.get_pos()):
                color = (100, 110, 140)
            else:
                color = (50, 50, 75)
            pygame.draw.rect(screen, color, buttonrect)
        elif buttontitle == 'INVENTORY':
            buttonrect = pygame.Rect(0, 220, 400, 100) 
            if buttonrect.collidepoint(pygame.mouse.get_pos()):
                color = (100, 110, 140)
            else:
                color = (50, 50, 75)
            pygame.draw.rect(screen, color, buttonrect)
        elif buttontitle == "SHOP":
            buttonrect = pygame.Rect(0, 330, 335, 100) 
            if buttonrect.collidepoint(pygame.mouse.get_pos()):
                color = (100, 110, 140)
            else:
                color = (50, 50, 75)
            pygame.draw.rect(screen, color, buttonrect)
        elif buttontitle == "SAVE":
            buttonrect = pygame.Rect(0, 440, 270, 100) 
            if buttonrect.collidepoint(pygame.mouse.get_pos()):
                color = (100, 110, 140)
            else:
                color = (50, 50, 75)
            pygame.draw.rect(screen, color, buttonrect)
        else:
            buttonrect = pygame.Rect(0, 600, 450, 100) 
            if buttonrect.collidepoint(pygame.mouse.get_pos()):
                color = (110, 160, 185)
            else:
                color = (90, 100, 150)
            pygame.draw.rect(screen, color, buttonrect)
            
        textfont = pygame.font.SysFont(None, 90, bold = True)
        text = textfont.render(buttontitle, True, (200, 220, 255))
        textsurface = text.get_rect(left=buttonrect.left + 10, centery = buttonrect.centery)
        screen.blit(text, textsurface)
    
    def OpenMenuScreen(player):
        global menurunning
        menurunning = True
        while menurunning:
            screen.fill((20, 20, 25))
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            buttontitles = ['YOUR   STATS', 'SHOP', 'INVENTORY', 'SAVE', 'CLOSE MENU']
            for buttontitle in buttontitles:
                Menu.DrawButtonMainMenu(buttontitle, events)
            
            pygame.display.update() 

player = MainCharacter('hi', 0, 0, 0, 0, [], 0, 0, 0)
Menu.OpenMenuScreen(player)