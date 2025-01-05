import pygame
import json
import random
from charactersitems import MainCharacter
from charactersitems import Weapon
from charactersitems import Enemy
from movement import OpenWorld
from battles import Battles

pygame.init()

screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width,screen_height))
running = True
enemies = []

with open('rooms.json', 'r') as file:
    rooms = json.load(file)

#need to add this code to the rooms branch

class Room:
    def __init__(self, room_number):
        self.room_number = room_number
        self.openworld = OpenWorld(self.room_number)
        self.amount_of_rooms_user_has_been_in = 0
    
    def spawn_enemies(self): 
        global player_rect
       
        for room in rooms:
            if room['id'] == self.room_number:
                current_room = room
                break
        
        if current_room['id'] == 4:
            total_enemies = 1
            enemies.append(pygame.Rect(680, 290, 60, 60))
        else:
            total_enemies = len(current_room['rectangles'])
            while len(enemies) < total_enemies:
        
                enemy_rect = pygame.Rect(random.randint(2, 127) * 10, random.randint(2, 61) * 10, 10, 10)
                in_a_map_rect = any(pygame.Rect(rectangle).colliderect(enemy_rect) for room in rooms for rectangle in room['rectangles'] if room['id'] == self.room_number)
                enemy_collision = any(enemy.colliderect(enemy_rect) for enemy in enemies) 
                player_collision = enemy_rect.colliderect(player_rect)

                if not enemy_collision and not player_collision and in_a_map_rect: #makes sure enemy is in map and isn't colliding with the player or other enemies
                    enemies.append(enemy_rect)

    def check_if_enemy_encounter(self):
        global player_rect, battling
        for enemy in enemies:
            if player_rect.colliderect(enemy):
                battling = True
                enemies.remove(enemy)
                if self.room_number < 4:
                    fightingenemies = Battles.SpawnEnemies(self.room_number)
                    Battles.Battle(player, fightingenemies)
                else:
                    fightingenemies = Battles.SpawnBoss()
                    Battles.Battle(player, fightingenemies)
                    

    def LoadRoom(self, player, rphbi, player_coordinates=None):
        global player_rect, enemies_spawned, battling
        room_loaded = True
        enemies_spawned = False
        cangoforward = False
        battling = False
        x = 1
        
        
        if player_coordinates:
            self.openworld.playerx, self.openworld.playery = player_coordinates
        else:
            self.openworld.get_player_starting_pos()

        while running: 
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit() # if we exit out the window it closes
    
            screen.fill((20, 20, 25)) # background

            player_rect = pygame.Rect(self.openworld.playerx, self.openworld.playery, 10, 10)

            for room in rooms:
                if room['id'] == self.room_number:
                    for rect in room['rectangles']:  # each room has a list of rectangles
                        pygame.draw.rect(screen, (35, 35, 42.5), (rect[0] - 10, rect[1] - 10, rect[2] + 20, rect[3] + 20))
                    for rect in room['rectangles']:
                        pygame.draw.rect(screen, (40, 40, 50), rect)
            
            pygame.draw.rect(screen, (185, 220, 240), (0, 620, 1280, 100)) # this draws the light bar at the bottom that the buttons sit on
            pygame.draw.line(screen, (145, 180, 200), (0, 620), (1280, 620), 10)
            
            directions = ["LEFT", "UP", "DOWN", "RIGHT"]
            for direction in directions: # a for loop to make all the buttons to save a little code, and to make me look better in front of whalen
                self.openworld.CreateMoveButton(direction, events, room, player)
                self.openworld.CreateMenuButton(events)
            
            playerinfofont = pygame.font.Font(None, 36) # same making textbox code again, no hover color stuff bc this is not a button
            playerinforect = pygame.Rect(410, 640, 360, 60)
            playerinfotext = playerinfofont.render(f"{player.name}: {int(player.currenthp)}/{player.maxhp}", True, (255, 255, 255))
            playerinfosurface = playerinfotext.get_rect(center=playerinforect.center)
            pygame.draw.rect(screen, (20, 27, 30), playerinforect)
            screen.blit(playerinfotext, playerinfosurface)
            
            pygame.draw.rect(screen, (255, 255, 255), (self.openworld.playerx, self.openworld.playery, 10, 10))
            
            roominforect = pygame.Rect(1000, 632, 260, 80)
            pygame.draw.rect(screen, (20, 27, 30), roominforect)
            roominfofont = pygame.font.Font(None, 35)
            roomnumbertext = roominfofont.render(f"ROOM {self.room_number + 1}", True, (255, 255, 255))
            roomnumbersurface = roomnumbertext.get_rect(centerx = roominforect.centerx, centery = roominforect.centery - 15)
            screen.blit(roomnumbertext, roomnumbersurface)
            
            if self.room_number > 0:
                gobackrect = pygame.Rect(1010, 675, 100, 30)
                if gobackrect.collidepoint(pygame.mouse.get_pos()):
                    gobackcolor = (60, 70, 90)
                else:
                    gobackcolor = (40, 45, 50)
                pygame.draw.rect(screen, gobackcolor, gobackrect)
                gobacktext = roominfofont.render("<", True, (255, 255, 255))
                gobacksurface = gobacktext.get_rect(center=gobackrect.center)
                screen.blit(gobacktext, gobacksurface)
                
                for event in events:
                    if gobackcolor[0] == 60 and event.type == pygame.MOUSEBUTTONDOWN:
                        self.room_number -= 1
                        room = Room(self.room_number)
                        enemies.clear()
                        enemies_spawned = False
                        room.LoadRoom(player, rphbi, None)
            
            if player.currenthp <= 0 and x == 1:
                x += 1
                self.DeathScreen()
            
            if self.room_number + 1 in rphbi:
                goforwardrect = pygame.Rect(1140, 675, 100, 30)
                if goforwardrect.collidepoint(pygame.mouse.get_pos()):
                    goforwardcolor = (60, 70, 90)
                else:
                    goforwardcolor = (40, 45, 50)
                
                pygame.draw.rect(screen, goforwardcolor, goforwardrect)
                
                goforwardtext = roominfofont.render(">", True, (255, 255, 255))
                goforwardsurface = goforwardtext.get_rect(center=goforwardrect.center)
                screen.blit(goforwardtext, goforwardsurface)
                
                for event in events:
                    if goforwardcolor[0] == 60 and event.type == pygame.MOUSEBUTTONDOWN:
                        self.room_number += 1
                        room = Room(self.room_number)
                        enemies.clear()
                        enemies_spawned = False
                        room.LoadRoom(player, rphbi, None)
                
                
            if not enemies_spawned:
                self.spawn_enemies()
                enemies_spawned = True
                self.amount_of_rooms_user_has_been_in += 1
              
            for enemy in enemies:
                if self.room_number != 4:
                    pygame.draw.rect(screen, (190, 60, 38), enemy)
                else:
                    pygame.draw.rect(screen, (90, 10, 18), (enemy[0], enemy[1], enemy[2], enemy[3]))

            self.check_if_enemy_encounter()
            
            if room_loaded and len(enemies) == 0 and player.currenthp > 0:
                for room in rooms:
                    if room['id'] == self.room_number:
                        rphbi.append(self.room_number + 1)

            if 5 in rphbi:
                #win screen
                font = pygame.font.Font(None, 100)
                otherfont = pygame.font.Font(None, 60)
                textrect = pygame.Rect(0, 0, 1280, 720)
                text = font.render("GOOD JOB!!! YOU BEAT THE", True, (255, 255, 255))
                textsurface = text.get_rect(centerx=textrect.centerx, centery = textrect.centery-80)
                text2 = otherfont.render("SUPER AWESOME AND VERY REAL GAME", True, (205, 235, 245))
                text2surface = text2.get_rect(center=textrect.center)
                text3 = font.render("made by edward and crystal", True, (255, 255, 255))
                text3surface = text3.get_rect(centerx=textrect.centerx, centery = textrect.centery+80)
                
                
                pygame.draw.rect(screen, (20, 23, 35), textrect)
                pygame.draw.line(screen, (30, 45, 60), (0, 0), (1280, 760), 150)
                pygame.draw.line(screen, (60, 90, 120), (0, 0), (1280, 760), 80)
                screen.blit(text, textsurface)
                screen.blit(text2, text2surface)
                screen.blit(text3, text3surface)
                player.currenthp = player.maxhp
                
                viewstats = pygame.Rect(200, 500, 880, 200)
                if viewstats.collidepoint(pygame.mouse.get_pos()):
                    viewstatscolor = (50, 80, 90)
                    for event in events:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            print('menu')
     
                else:
                    viewstatscolor = (30, 45, 50)
                
                pygame.draw.rect(screen, viewstatscolor, viewstats)
                viewtext = font.render("VIEW YOUR STATS", True, (255, 255, 255))
                viewsurface = viewtext.get_rect(center=viewstats.center)
                screen.blit(viewtext, viewsurface)
                
            pygame.display.update()
            
    def DeathScreen(self):
        import time
        bgrect = pygame.Rect(1280, 0, 1280, 720)
        innerrect = pygame.Rect(1290, 10, 1280, 700)
        lastmovetime = time.time()
        newtime = time.time()
        
        while bgrect[0] != 0:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    quit()
            
            newtime = time.time()      
            pygame.draw.rect(screen, (10, 2, 1), bgrect)
            pygame.draw.rect(screen, (30, 4, 2), innerrect)
            
            if newtime - lastmovetime > 0.05:
                lastmovetime = newtime
                bgrect[0] -= 20
                innerrect[0] -= 20
            
            pygame.display.update()
        
        deadtime = time.time()
        currenttime = time.time()
        
        
        while currenttime - deadtime < 10:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    quit()        

            currenttime = time.time()
            screen.fill((10, 2, 1))
            
            insiderectangle = pygame.Rect(10, 10, 1260, 700)
            pygame.draw.rect(screen, (30, 4, 2), insiderectangle)
            
            fonts = pygame.font.get_fonts()
            
            textfont = pygame.font.SysFont(None, 200, bold=True)
            youdied = textfont.render('YOU DIED.', True, (255, 0, 0))
            youdiedsurface = youdied.get_rect(center=(640, 240))
            screen.blit(youdied, youdiedsurface)
            
            smallfont = pygame.font.Font(None, 100)
            youreached = smallfont.render(f"YOU REACHED ROOM {self.room_number + 1}", True, (255, 0, 0))
            youreachedsurface = youreached.get_rect(center=(640, 340))
            screen.blit(youreached, youreachedsurface)
            
            timeuntilend = int(10 - (currenttime - deadtime))
            deletingin = smallfont.render(f"DELETING YOUR DATA IN {timeuntilend}", True, (255, 0, 0))
            deletinginsurface = deletingin.get_rect(center=(640,410))
            screen.blit(deletingin, deletinginsurface)
            
            
            smallerfont = pygame.font.SysFont(None, 50, italic=True)
            youhad = smallerfont.render("You had a good run! But you are bad at video games.", True, (255, 255, 255))
            youhadsurface = youhad.get_rect(center=(640,480))
            screen.blit(youhad, youhadsurface)
            
            
            pygame.display.update()
        
        print("DATA DELETION UNDERWAY. THIS PROCESS WILL BE COMPLETED MOMENTARILY.")
        quit()
        
player = MainCharacter('edward', 1, 1, 10, Weapon("HI", 10, 100, 10), [], 0, 1, 0)

room = Room(0)
#rphbi = rooms player has been in ... duh ...

rphbi = [0, 1, 2, 3, 4]

room.LoadRoom(player, rphbi, None)