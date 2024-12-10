import pygame
from charactersitems import MainCharacter

pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Game')
running = True

class OpenWorld():
    def CreateMoveButton(direction, events, room, player):
        global playerx, playery, itworks # i need these variables in both this function and the load room one
        buttonfont = pygame.font.Font(None, 36)
        if direction == "LEFT":
            buttonrect = pygame.Rect(10, 640, 90, 60)
        elif direction == "UP":
            buttonrect = pygame.Rect(110, 640, 90, 60)
        elif direction == "DOWN":
            buttonrect = pygame.Rect(210, 640, 90, 60)
        elif direction == "RIGHT":
            buttonrect = pygame.Rect(310, 640, 90, 60) # loading all the buttons in
        
        mouseposition = pygame.mouse.get_pos()
        if buttonrect.collidepoint(mouseposition): # if the mouse is on one of the buttons,
            buttoncolor = (40, 54, 60) # the color is lighter
        else: # if not
            buttoncolor = (20, 27, 30) # it isnt
        
        pygame.draw.rect(screen, buttoncolor, buttonrect)  # making the buttons, this is the rectangle that the text will go on
        buttonsurface = buttonfont.render(direction, True, (245, 245, 255)) # the text
        buttontextrect = buttonsurface.get_rect(center=buttonrect.center) # placing it on the rectangle
        screen.blit(buttonsurface, buttontextrect) # uppdating the screen so its there
        
        for event in events: # notice how i use events and not pygame.event.get(), that will be important ill explain later
            if event.type == pygame.MOUSEBUTTONDOWN: # if the mouse is down and the mouse is on the button
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
                        testplayery = playery # the coordinates change, but these are just placeholder coordinates and dont change the actual ones yet
                        
                    playerlocation = (testplayerx, testplayery)
                    itworks = False
                    for rectangle in room["rectangles"]:
                        rectcoords = pygame.Rect(rectangle[0], rectangle [1], rectangle[2], rectangle[3])
                        if rectcoords.collidepoint(playerlocation):
                            itworks = True
                    # if the player's location is in at least one of the rectangles they can walk on, it does work
                    if itworks:
                        playerx = testplayerx
                        playery = testplayery # if it works then it actually changes the coordinates
                        import random
                        enemychance = random.randint(1, 18) # 1/18 chance to spawn enemy
                        if enemychance == 18:
                            print("ENEMY!") # placeholder for the function
                    else: # if the new player location is outside of the bounds, that means they walked into the wall
                        player.currenthp -= 3 # so they hit their head lolol
                        if player.currenthp < 10:
                            player.currenthp = 10 # i'm not SO evil...
    
    def CreateMenuButton(events):
        menufont = pygame.font.Font(None, 36) # this code is to open the menu from the screen
        menurect = pygame.Rect(800, 640, 180, 60) # same code to make a rectangle, get text, place text, whatever
        menutext = menufont.render("Open Menu", True, (255, 255, 255))
        menusurface = menutext.get_rect(center=menurect.center)
        if menurect.collidepoint(pygame.mouse.get_pos()): # same hover color base color code
            color = (40, 54, 60)
        else:
            color = (20, 27, 30)
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                print('menu')
            
        pygame.draw.rect(screen, color, menurect) 
        screen.blit(menutext, menusurface)
                           
    def LoadRoom(room, player):
        global playerx, playery # sets their location at the start
        playerx = 100 # may be changed but you do the function :D
        playery = 100
        while running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            
            screen.fill((20, 20, 25))
            for rect in room['rectangles']: # makes an outline to make the game look slightly nicer
                pygame.draw.rect(screen, (32, 32, 42.5), (rect[0] - 10, rect[1] - 10, rect[2] + 20, rect[3] + 20))
            for rect in room['rectangles']:
                pygame.draw.rect(screen, (60, 60, 75), rect)
            
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