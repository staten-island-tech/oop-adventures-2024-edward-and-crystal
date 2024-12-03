import pygame
import json
import random

pygame.init()

screen = pygame.display.set_mode((1280, 720))
gray = (169, 169, 169)
screen.fill(gray)
running = True
mobs = []

def load_enemy_data():
    with open('enemies.json') as f:
        return json.load(f)

enemy_data = load_enemy_data()

#MAKE ROOMS AND SPAWN TABLES (the percent chance each enemy will spawn in a partricular area), DESIGNS
#3 rooms, 1 boss, 3 rooms, 1 boss
#movement on screen, need split the room in 3-4 

class Button:
    def __init__(self, x, y, width, height, bgcolor, text, text_color, font_size=30):
        self.rect = pygame.Rect(x, y, width, height)
        self.bgcolor = bgcolor
        self.text = text
        self.text_color = text_color
        self.font = pygame.font.SysFont('Papyrus', font_size)

    def draw(self, screen):
        pygame.draw.rect(screen, self.bgcolor, self.rect)

        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)
        
    def is_hovered(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

    def is_clicked(self, mouse_pos, mouse_pressed):
        if self.is_hovered(mouse_pos) and mouse_pressed[0]:
            return True
        return False

spawn_table = [
    {'name': 'slime', 'chanceofspawning': 0.3},
    {'name': 'goblin', 'chanceofspawning': 0.3},
    {'name': 'strong slime', 'chanceofspawning': 0.2},
    {'name': 'orc', 'chanceofspawning': 0.2}
]

def get_random_enemy(enemy_data):
    total_chance = sum(mob['chanceofspawning'] for mob in enemy_data)
    random_value = random.uniform(0, total_chance)

    cumulative_chance = 0.0
    for mob in enemy_data:
        cumulative_chance += mob['chanceofspawning']
        if random_value <= cumulative_chance:
            # Load the enemy type data (health, speed, etc.)
            return mob

    return enemy_data[0] 

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        for i in range(4):
            random.choice(i['name'], weights=spawn_table['chanceofspawning'])
        if len(mobs) < max_mobs:
            selected_enemy = get_random_enemy(enemy_data)  # Get enemy data
            enemy = Enemy(
                name=selected_enemy['name'],
                color=selected_enemy['color'],
                health=selected_enemy['health'],
                speed=selected_enemy['speed']
            )
            mobs.append(enemy)


        
    pygame.display.flip()

