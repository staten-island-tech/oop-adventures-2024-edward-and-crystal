import pygame
import json
import random
from charactersitems import MainCharacter
from movement import OpenWorld

pygame.init()

screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width,screen_height))
gray = (169, 169, 169)
screen_color = gray
screen.fill(screen_color)
enemy_width = 10
enemy_height = 10
running = True
enemies = []

with open('rooms.json', 'r') as file:
    rooms_data = json.load(file)

#MAKE ROOMS AND SPAWN TABLES (the percent chance each enemy will spawn in a partricular area), DESIGNS
#3 rooms, 1 boss, 3 rooms, 1 boss


class Room:
    def __init__(self, room_number):
        self.room_number = room_number
        self.probabilites = self.spawn_table()

    def clear(self):
        screen.fill(screen_color)
    def spawn_table(self):
        #is this balanced? probably not, but it's a problem for a wiser Crystal
        if self.room_number not in [4, 8]:
            probabilites = {
                'Goblin': 0.2 - self.room_number * 0.05,
                'Orc': 0.2 - self.room_number * 0.05,
                'Slime': 0.3 - self.room_number * 0.05,
                'Strong Slime': 0.1 + self.room_number * 0.05,
                'Strong Orc': 0.1 + self.room_number * 0.05,
                'Grifter': 0.1 + self.room_number * 0.05,
            }
        else:
            probabilites = {
            'Boss': 1 if self.room_number == 4 else 0,
            'Boss Grifter': 1 if self.room_number == 8 else 0
        }
        return probabilites
    
    def spawn_enemies(self, number_of_enemies): 
        names = list(self.probabilites.keys())  # Get enemy names from keys
        chances = list(self.probabilites.values())  # Get spawn probabilities from values
        for i in range(number_of_enemies):
          selected_enemy = random.choices(names, weights=chances, k=1)  # Randomly select an enemy
          enemies.append(selected_enemy)
        for enemy in enemies:
            enemyrect = pygame.rect(random.randint(2, 127) * 10, random.randint(2, 71) * 10, 20, 20)
            if not enemyrect.colliderect(enemy for enemy in enemies) and not enemyrect.colliderect(playerlocation): 
                pygame.draw.rect(screen, 'black', enemyrect)
            

    
    
    def draw_room(self):
        #i cant draw the enemies properly without the sprites. 
        #plus the drawing the enemy function should prob be in the enemy class, which edward has
        if number_of_enemies_on_screen < self.max_number_of_enemies:
            #makes it so the mobs are fully in the screen
            x = random.randint(0, screen_width - enemy_width)
            y = random.randint(0, screen_height - enemy_height)
            #the rectangle is a placeholder. need to add the proper sprites later
            rect = pygame.Rect(x, y, enemy_width, enemy_height)
            collision = any(rect.colliderect(character) for character in character_positions)
            if not collision:
                number_of_enemies_on_screen += 1
                pygame.draw.rect(screen, 'red', rect)
                character_positions.append(rect)
                print(Room(4).get_number_of_enemies())

    def LoadRoom(self, player):

        openworld = OpenWorld()
        playerrect = openworld.get_player_starting_pos()
        
        while running: 
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit() # if we exit out the window it closes
    
            screen.fill((20, 20, 25)) # background

            for room in rooms_data:
                if room['id'] == self.room_number:
                    for rect in room['rectangles']:  # each room has a list of rectangles, which are tuples, see the room example at the bottom
                        pygame.draw.rect(screen, (35, 35, 42.5), (rect[0] - 10, rect[1] - 10, rect[2] + 20, rect[3] + 20))
                    for rect in room['rectangles']:
                        pygame.draw.rect(screen, (40, 40, 50), rect)
            
            pygame.draw.rect(screen, (185, 220, 240), (0, 620, 1280, 100)) # this draws the light bar at the bottom that the buttons sit on
            pygame.draw.line(screen, (145, 180, 200), (0, 620), (1280, 620), 10)
            
            directions = ["LEFT", "UP", "DOWN", "RIGHT"]
            for direction in directions: # a for loop to make all the buttons to save a little code, and to make me look better in front of whalen
                openworld.CreateMoveButton(direction, events, room, player)
                openworld.CreateMenuButton(events)
            
            playerinfofont = pygame.font.Font(None, 36) # same making textbox code again, no hover color stuff bc this is not a button
            playerinforect = pygame.Rect(410, 640, 360, 60)
            playerinfotext = playerinfofont.render(f"{player.name}: {player.currenthp}/{player.maxhp}", True, (255, 255, 255))
            playerinfosurface = playerinfotext.get_rect(center=playerinforect.center)
            pygame.draw.rect(screen, (20, 27, 30), playerinforect)
            screen.blit(playerinfotext, playerinfosurface)
        
            
            pygame.draw.rect(screen, (255, 255, 255), (openworld.playerx, openworld.playery, 10, 10))
            
            pygame.display.update()
 


    
player = MainCharacter('drwillfulneglect', 100, 100, 10, 'hey', [], 100, 0, 0)

room = Room(1)
room.LoadRoom(player)
