import pygame
import json
import random

pygame.init()

screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width,screen_height))
gray = (169, 169, 169)
screen_color = gray
screen.fill(screen_color)
running = True
mobs = []
number_of_enemies_on_screen = 0
character_positions = []
enemy_width = 200
enemy_height = 100
def load_enemy_data():
    with open('enemies.json') as f:
        return json.load(f)

enemy_data = load_enemy_data()

#MAKE ROOMS AND SPAWN TABLES (the percent chance each enemy will spawn in a partricular area), DESIGNS
#3 rooms, 1 boss, 3 rooms, 1 boss


class Room:
    def __init__(self, room_number):
        self.room_number = room_number
        self.probabilites = self.spawn_table()
        self.max_number_of_enemies = self.get_number_of_enemies()
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
    def get_random_enemy(self): 
        names = list(self.probabilites.keys())  # Get enemy names from keys
        chances = list(self.probabilites.values())  # Get spawn probabilities from values
        selected_enemy = random.choices(names, weights=chances, k=1)  # Randomly select an enemy
        return selected_enemy
    def get_number_of_enemies(self):
        if self.room_number in [4, 8]:
            max_number_of_enemies = 1
        else:
            max_number_of_enemies = 4
        return max_number_of_enemies
    
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


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
                
        


    pygame.display.flip()