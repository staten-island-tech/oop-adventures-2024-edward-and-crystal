import pygame
import random
import json

pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Game')
running = True

playerx = None
playery = None

with open('rooms.json', 'r') as file:
    rooms_data = json.load(file)


class OpenWorld:
    def get_player_starting_pos():
        while True:
            global playerx, playery
            playerx = random.randint(2, 127) * 10
            playery = random.randint(2, 71) * 10
            playerrect = pygame.Rect(playerx, playery, 10, 10)
            #it checks if the player is in the map. did i need to format it this way? no but this is cool!!!
            if any(playerrect.colliderect(pygame.Rect(rectangle[0], rectangle[1], rectangle[2], rectangle[3])) for room in rooms_data for rectangle in room['rectangles']):
               return playerrect 

    def CreateMoveButton(direction, events, room, player):
        global playerx, playery, player_in_map
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
                        playerx -= 10
                    elif direction == "UP":
                        playery += 10
                    elif direction == "DOWN":
                        playery -= 10
                    elif direction == "RIGHT":
                        playerx += 10
                    
                        
                    playerrect = (playerx, playery)
                    player_in_map = False

                    for room in rooms_data:
                        for rectangle in room["rectangles"]:
                            rectcoords = pygame.Rect(rectangle[0], rectangle [1], rectangle[2], rectangle[3])
                            if rectcoords.collidepoint(playerrect):
                              player_in_map = True
                              break
                        if player_in_map:
                            break
                    
                    if player_in_map:
                        youareSTUPIDrect = pygame.Rect(140, 10, 1000, 30)
                        pygame.draw.rect(screen, (20, 20, 25), youareSTUPIDrect)
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
              
    
