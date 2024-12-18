import pygame
from rooms import playery, playerx

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
                        
                    playerrect = (testplayerx, testplayery)
                    itworks = False
                    for rectangle in room["rectangles"]:
                        rectcoords = pygame.Rect(rectangle[0], rectangle [1], rectangle[2], rectangle[3])
                        if rectcoords.collidepoint(playerrect):
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
                           
    
room = {
    "rectangles": [[10, 10, 100, 590],
                  [10, 10, 1220, 100],
                    [1160, 10, 100, 590],
                    [100, 500, 1150, 100],
                    [590, 10, 100, 590],
                    [10, 270, 1220, 100],
                    [590, 500, 200, 200]]

}
        
        

    
