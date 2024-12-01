import pygame
from charactersitems import MainCharacter

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
    
    def CreateMenuButton(events):
        menufont = pygame.font.Font(None, 36)
        menurect = pygame.Rect(800, 640, 180, 60)
        menutext = menufont.render("Open Menu", True, (255, 255, 255))
        menusurface = menutext.get_rect(center=menurect.center)
        if menurect.collidepoint(pygame.mouse.get_pos()):
            color = (40, 54, 60)
        else:
            color = (20, 27, 30)
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                print('menu')
            
        pygame.draw.rect(screen, color, menurect)
        screen.blit(menutext, menusurface)
                           
    def LoadRoom(room, player):
        global playerx, playery
        playerx = 100
        playery = 100
        while running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            
            screen.fill((20, 20, 25))
            for rect in room['rectangles']:
                pygame.draw.rect(screen, (40, 40, 50), rect)
            
            pygame.draw.rect(screen, (185, 220, 240), (0, 620, 1280, 100))
            directions = ["LEFT", "UP", "DOWN", "RIGHT"]
            for direction in directions:
                OpenWorld.CreateMoveButton(direction, events, room, player)
            OpenWorld.CreateMenuButton(events)
            
            playerinfofont = pygame.font.Font(None, 36)
            playerinforect = pygame.Rect(410, 640, 360, 60)
            playerinfotext = playerinfofont.render(f"{player.name}: {player.currenthp}/{player.maxhp}", True, (255, 255, 255))
            playerinfosurface = playerinfotext.get_rect(center=playerinforect.center)
            pygame.draw.rect(screen, (20, 27, 30), playerinforect)
            screen.blit(playerinfotext, playerinfosurface)
            
            playerlocation = pygame.Rect(playerx, playery, 10, 10)
            pygame.draw.rect(screen, (255, 255, 255), playerlocation)
            pygame.display.update()

 
room = {
    "rectangles" : [
    (100, 100, 100, 400),
    (200, 200, 400, 50)]
    }   


player = MainCharacter('drwillfulneglect', 100, 100, 10, 'hey', [], 100, 0, 0)

OpenWorld.LoadRoom(room, player)