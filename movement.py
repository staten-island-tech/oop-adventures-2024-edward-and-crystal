import pygame
import random
import json
from menus import Menu


pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width,screen_height))

with open('rooms.json', 'r') as file:
    rooms = json.load(file)


class OpenWorld:
    def __init__(self, room_number):
        self.playerx = None
        self.playery = None
        self.room_number = room_number

    def get_player_starting_pos(self):
        while True:
            if self.room_number == 4:
                self.playerx = 40
                self.playery = 300
            
            else:
                self.playerx = random.randint(2, 127) * 10
                self.playery = random.randint(2, 61) * 10

            playerrect = pygame.Rect(self.playerx, self.playery, 10, 10)
            #it checks if the player is in the map
            for room in rooms:
                if room['id'] == self.room_number:
                    for rect in room['rectangles']:
                        maprect = pygame.Rect(rect)
                        if playerrect.colliderect(maprect):
                          return #return ends the loops

           
    def CreateMoveButton(self, direction, events, room, player):
        global player_in_map
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
                        testplayerx = self.playerx - 10
                        testplayery = self.playery
                    elif direction == "UP":
                        testplayery = self.playery - 10
                        testplayerx = self.playerx 
                    elif direction == "DOWN":
                        testplayery = self.playery + 10
                        testplayerx = self.playerx
                    elif direction == "RIGHT":
                        testplayerx = self.playerx + 10
                        testplayery = self.playery

                    player_in_map = False
                    testrect = (testplayerx, testplayery, 10, 10)

                    for room in rooms:
                        for rectangle in room["rectangles"]:
                            if room['id'] == self.room_number:
                                rectcoords = pygame.Rect(rectangle[0], rectangle [1], rectangle[2], rectangle[3])
                                if rectcoords.colliderect(testrect):
                                    player_in_map = True
                                    break
                            if player_in_map:
                                break
                    
                    if player_in_map:
                        self.playery = testplayery 
                        self.playerx = testplayerx 
                        youareSTUPIDrect = pygame.Rect(140, 10, 1000, 30)
                        pygame.draw.rect(screen, (20, 20, 25), youareSTUPIDrect)
                     
                    else:
                        testplayerhealth = player.currenthp - 3
                        
                        if testplayerhealth < 10:
                            player.currenthp = player.currenthp # i'm not SO evil...
                            if player.currenthp > 10:
                                player.currenthp = 10
                        else:
                            player.currenthp = testplayerhealth
                            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    direction = "UP"
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    direction = "LEFT"
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    direction = "DOWN"
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    direction = "RIGHT"
                if direction == "LEFT":
                    testplayerx = self.playerx - 2.5
                    testplayery = self.playery
                elif direction == "UP":
                    testplayery = self.playery - 2.5
                    testplayerx = self.playerx 
                elif direction == "DOWN":
                    testplayery = self.playery + 2.5
                    testplayerx = self.playerx
                elif direction == "RIGHT":
                    testplayerx = self.playerx + 2.5
                    testplayery = self.playery

                player_in_map = False
                testrect = (testplayerx, testplayery, 10, 10)

                for room in rooms:
                    for rectangle in room["rectangles"]: 
                        if room['id'] == self.room_number:
                            rectcoords = pygame.Rect(rectangle[0], rectangle [1], rectangle[2], rectangle[3])
                            if rectcoords.colliderect(testrect):
                                player_in_map = True
                                break
                        if player_in_map:
                            break
                    
                if player_in_map:
                    self.playery = testplayery 
                    self.playerx = testplayerx 
                    youareSTUPIDrect = pygame.Rect(140, 10, 1000, 30)
                    pygame.draw.rect(screen, (20, 20, 25), youareSTUPIDrect) 
                else:
                    testplayerhealth = player.currenthp - 3
                        
                    if testplayerhealth < 10:
                        player.currenthp = player.currenthp # i'm not SO evil...
                        if player.currenthp > 10:
                            player.currenthp = 10
                    else:
                        player.currenthp = testplayerhealth
             
    def CreateMenuButton(self, events, player, room): # opening the menu
        menufont = pygame.font.Font(None, 36) # most of this code is the same
        menurect = pygame.Rect(800, 640, 180, 60)
        menutext = menufont.render("Open Menu", True, (255, 255, 255))
        menusurface = menutext.get_rect(center=menurect.center)
        if menurect.collidepoint(pygame.mouse.get_pos()):
            color = (40, 54, 60)
            for event in events: # if we are hovering over the button and we click it the menu gets printed
                if event.type == pygame.MOUSEBUTTONDOWN:
                    Menu.OpenMenuScreen(player, room.room_number) # sample function
        else:
            color = (20, 27, 30)
            
        pygame.draw.rect(screen, color, menurect)
        screen.blit(menutext, menusurface)
              