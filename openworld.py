import pygame
import json
import random

pygame.init()

screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
gray = (169, 169, 169)
screen.fill(gray)
running = True
mobs = []
number_of_mobs = 0
character_positions = []
enemy_width = 200
enemy_height = 100
def load_enemy_data():
    with open('enemies.json') as f:
        return json.load(f)

enemy_data = load_enemy_data()

#MAKE ROOMS AND SPAWN TABLES (the percent chance each enemy will spawn in a partricular area), DESIGNS
#3 rooms, 1 boss, 3 rooms, 1 boss
#movement on screen, need split the room in 3-4 
#need to account for error-- enemy cannot spawn outside the border and cannot spawn on each other

spawn_table = [
    {'name': 'slime', 'chanceofspawning': 0.3},
    {'name': 'goblin', 'chanceofspawning': 0.3},
    {'name': 'strong slime', 'chanceofspawning': 0.2},
    {'name': 'orc', 'chanceofspawning': 0.2}
]

def filler_enemies():
    rect = pygame.Rect(100, 100, 200, 150) 
    pygame.draw.rect(screen, 'red', rect)

def get_random_enemy(): 
    names = [mob['name'] for mob in spawn_table]  # List of enemy names
    chances = [mob['chanceofspawning'] for mob in spawn_table]  # List of spawn chances
    selected_enemy = random.choices(names, weights=chances, k=1)
    return selected_enemy

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        x = random.randint(0, screen_width-enemy_width)
        y = random.randint(0, screen_height-enemy_height)
        rect = pygame.Rect(x, y, enemy_width, enemy_height) 
        # for all x values in character_positions + enemy_width and for all
        for character in character_positions:
            if rect.colliderect(character):
                print('uh oh collison')
        if (x, y) not in character_positions and number_of_mobs < 4:
            number_of_mobs += 1
            #need to add the enemy sprites
            pygame.draw.rect(screen, 'red', rect)
            character_positions += (x, y)
            print(get_random_enemy())
        


    pygame.display.flip()


