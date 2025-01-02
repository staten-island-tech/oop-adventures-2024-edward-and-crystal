import pygame
import json
import random
from charactersitems import MainCharacter
from movement import OpenWorld

pygame.init()

screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width,screen_height))
running = True
enemies = []

with open('rooms.json', 'r') as file:
    rooms = json.load(file)

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
                print('battle time!!')
                #insert actual battles code. you got this, edward!!!!

    def LoadRoom(self, player, player_coordinates=None):
        global player_rect
        room_loaded = True
        enemies_spawned = False

        if player_coordinates:
            self.openworld.playerx, self.openworld.playery = player_coordinates
        else:
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



    
player = MainCharacter('drwillfulneglect', 100, 100, 10, 'hey', [], 100, 0, 0)

room = Room(1)
room.LoadRoom(player)