import pygame
import json
import random
from charactersitems import MainCharacter
from movement import OpenWorld
from savefiles import SaveFileManager

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

        total_enemies = len(current_room['rectangles'])
        while len(enemies) < total_enemies:
    
            enemy_rect = pygame.Rect(random.randint(2, 127) * 10, random.randint(2, 61) * 10, 10, 10)
            in_a_map_rect = any(pygame.Rect(rectangle).colliderect(enemy_rect) for room in rooms for rectangle in room['rectangles'] if room['id'] == self.room_number)
            enemy_collision = any(enemy.colliderect(enemy_rect) for enemy in enemies) 
            player_collision = enemy_rect.colliderect(player_rect)

            if not enemy_collision and not player_collision and in_a_map_rect: #makes sure enemy is in map and isn't colliding with the player or other enemies
              enemies.append(enemy_rect)

    def check_if_enemy_encounter(self):
        global player_rect
        for enemy in enemies:
            if player_rect.colliderect(enemy):
                enemies.remove(enemy)
                #insert actual battles code. you got this, edward!!!!

    def LoadRoom(self, player, player_coordinates=None):
        
        pygame.init()
        screen_width = 1280
        screen_height = 720
        screen = pygame.display.set_mode((screen_width,screen_height))
        running = True
        global player_rect
        room_loaded = True
        enemies_spawned = False

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
            playerinfotext = playerinfofont.render(f"{player.name}: {player.currenthp}/{player.maxhp}", True, (255, 255, 255))
            playerinfosurface = playerinfotext.get_rect(center=playerinforect.center)
            pygame.draw.rect(screen, (20, 27, 30), playerinforect)
            screen.blit(playerinfotext, playerinfosurface)
            
            pygame.draw.rect(screen, (255, 255, 255), (self.openworld.playerx, self.openworld.playery, 10, 10))

            if not enemies_spawned:
                self.spawn_enemies()
                enemies_spawned = True
                self.amount_of_rooms_user_has_been_in += 1
              
            for enemy in enemies:
               pygame.draw.rect(screen, 'red', enemy)

            self.check_if_enemy_encounter()
            pygame.display.update()
            
            
            if room_loaded and len(enemies) == 0:
                for room in rooms:
                    if room['id'] == self.room_number:
                        destinations = [exit['destination'] for exit in room['exit'] if 'destination' in exit]
                        self.room_number = random.choice(destinations)
                        room_loaded = False
                        enemies_spawned = False
                        

            elif self.amount_of_rooms_user_has_been_in == 6 and len(enemies) == 0:
                #win screen
                font = pygame.font.Font(None, 100)
                textrect = pygame.Rect(390, 330, 500, 60)
                text = font.render("GOOD JOB!!! YOU BEAT OUR GAME", True, (255, 255, 255))
                textsurface = text.get_rect(center=textrect.center)
                pygame.draw.rect(screen, (20, 27, 30), textrect)
                screen.blit(text, textsurface)


# player = MainCharacter('w', 100, 100, 10, 'hey', [], 100, 0, 0)


player = SaveFileManager.convert_json_to_player_object('j')

room = Room(1)

room.LoadRoom(player)