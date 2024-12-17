import pygame
from charactersitems import MainCharacter
import json

import random

with open('rooms.json', 'r') as file:
    data = json.load(file)
    
pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Game')
running = True

class OpenWorld():
    def CreateMoveButton(direction, events, room, player):
        global playerx, playery, itworks
        buttonfont = pygame.font.Font(None, 36)
        if direction == "LEFT":
            buttonrect = pygame.Rect(10, 640, 90, 60)
        elif direction == "UP":
            buttonrect = pygame.Rect(110, 640, 90, 60)
        elif direction == "DOWN":
            buttonrect = pygame.Rect(210, 640, 90, 60)
        elif direction == "RIGHT":
            buttonrect = pygame.Rect(310, 640, 90, 60)
        
        mouseposition = pygame.mouse.get_pos()
        if buttonrect.collidepoint(mouseposition):
            buttoncolor = (40, 54, 60)
        else:
            buttoncolor = (20, 27, 30)
        
        pygame.draw.rect(screen, buttoncolor, buttonrect)     
        buttonsurface = buttonfont.render(direction, True, (245, 245, 255))
        buttontextrect = buttonsurface.get_rect(center=buttonrect.center)
        screen.blit(buttonsurface, buttontextrect)
        
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if buttonrect.collidepoint(pygame.mouse.get_pos()):
                    if direction == "LEFT":
                        testplayerx = playerx - 10
                        testplayery = playery
                    elif direction == "UP":
                        testplayery = playery - 10
                        testplayerx = playerx
                    elif direction == "DOWN":
                        testplayery = playery + 10
                        testplayerx = playerx
                    elif direction == "RIGHT":
                        testplayerx = playerx + 10
                        testplayery = playery
                        
                    playerlocation = (testplayerx, testplayery)
                    itworks = False
                    for rectangle in room["rectangles"]:
                        rectcoords = pygame.Rect(rectangle[0], rectangle [1], rectangle[2], rectangle[3])
                        if rectcoords.collidepoint(playerlocation):
                            itworks = True
                    
                    if itworks:
                        playerx = testplayerx
                        playery = testplayery
                        youareSTUPIDrect = pygame.Rect(140, 10, 1000, 30)
                        pygame.draw.rect(screen, (20, 20, 25), youareSTUPIDrect)
                        import random
                        enemychance = random.randint(1, 18)
                        if enemychance == 18:
                            print("ENEMY!")
                    else:
                        player.currenthp -= 3
                        if player.currenthp < 10:
                            player.currenthp = 10 # i'm not SO evil...
    
    def CreateMenuButton(events): # opening the menu
        menufont = pygame.font.Font(None, 36) # most of this code is the same
        menurect = pygame.Rect(800, 640, 180, 60)
        menutext = menufont.render("Open Menu", True, (255, 255, 255))
        menusurface = menutext.get_rect(center=menurect.center)
        if menurect.collidepoint(pygame.mouse.get_pos()):
            color = (40, 54, 60)
            for event in events: # if we are hovering over the button and we click it the menu gets printed
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print('menu') # sample function
        else:
            color = (20, 27, 30)
            
        pygame.draw.rect(screen, color, menurect)
        screen.blit(menutext, menusurface)
                           
    def LoadRoom(room, player):
        global playerx, playery
        
        while True: #gets the starting position of the player character
            collision = True
            playerlocation = pygame.Rect(random.randint(2, 127) * 10, random.randint(2, 71) * 10, 10, 10)
            for room in data:
                for rectangle in room['rectangles']:
                    rect = pygame.Rect(rectangle[0], rectangle[1], rectangle[2], rectangle[3])
                    if not playerlocation.colliderect(rect):
                        collision = False
                        break
                if not collision:
                    break
            if not collision:
                break                             

        while running: 
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit() # if we exit out the window it closes
            
            screen.fill((20, 20, 25)) # background
            for rect in room['rectangles']:  # each room has a list of rectangles, which are tuples, see the room example at the bottom
                pygame.draw.rect(screen, (35, 35, 42.5), (rect[0] - 10, rect[1] - 10, rect[2] + 20, rect[3] + 20))
            for rect in room['rectangles']:
                pygame.draw.rect(screen, (40, 40, 50), rect)
            
            pygame.draw.rect(screen, (185, 220, 240), (0, 620, 1280, 100)) # this draws the light bar at the bottom that the buttons sit on
            pygame.draw.line(screen, (145, 180, 200), (0, 620), (1280, 620), 10)
            
            directions = ["LEFT", "UP", "DOWN", "RIGHT"]
            for direction in directions: # a for loop to make all the buttons to save a little code, and to make me look better in front of whalen
                OpenWorld.CreateMoveButton(direction, events, room, player)
            OpenWorld.CreateMenuButton(events)
            
            playerinfofont = pygame.font.Font(None, 36) # same making textbox code again, no hover color stuff bc this is not a button
            playerinforect = pygame.Rect(410, 640, 360, 60)
            playerinfotext = playerinfofont.render(f"{player.name}: {player.currenthp}/{player.maxhp}", True, (255, 255, 255))
            playerinfosurface = playerinfotext.get_rect(center=playerinforect.center)
            pygame.draw.rect(screen, (20, 27, 30), playerinforect)
            screen.blit(playerinfotext, playerinfosurface)
            
            
            pygame.draw.rect(screen, (255, 255, 255), playerlocation)
            pygame.display.update()
 
room = {
    "rectangles": [[10, 10, 100, 590],
                  [10, 10, 1220, 100],
                    [1160, 10, 100, 590],
                    [100, 500, 1150, 100],
                    [590, 10, 100, 590],
                    [10, 270, 1220, 100],
                    [590, 500, 200, 200]]

}
        
        

    

player = MainCharacter('drwillfulneglect', 100, 100, 10, 'hey', [], 100, 0, 0)

OpenWorld.LoadRoom(room, player)