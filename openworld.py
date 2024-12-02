import pygame

pygame.init()

screen = pygame.display.set_mode((1280, 720))
gray = (169, 169, 169)
screen.fill(gray)
running = True

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

"""
‘id’ : 2
‘name’ : “slime”
‘maxhp’: 20
‘currenthp’: 20 (will change)
‘strength’: 5
‘golddrop’: 10
‘weapondrop’ : “nothing”

‘id’ : 3
‘name’ : “goblin”
‘maxhp’: 25
‘currenthp’: 25 (will change)
‘strength’: 10
‘golddrop’: 15
‘weapondrop’ : “badclub”

‘id’ : 4
‘name’ : “strong slime”
‘maxhp’: 40
‘currenthp’: 40 (will change)
‘strength’: 10
‘golddrop’: 25
‘weapondrop’ : “slime fist”
	
‘id’ : 5
‘name’ : “orc”
‘maxhp’: 35
‘currenthp’: 35 (will change)
‘strength’: 20
‘golddrop’: 35
‘weapondrop’ : “good club”
	
‘id’ : 6
‘name’ : “grifter”
‘maxhp’: 100
‘currenthp’: 100 (will change)
‘strength’: 0
‘golddrop’: 50
‘weapondrop’ : “nothing”
	
‘id’ : 7
‘name’ : “boss grifter”
‘maxhp’: 200
‘currenthp’: 200 (will change)
‘strength’: 5
‘golddrop’: 100
‘weapondrop’ : “grifter staff”
"""
spawn_table = [
    {'name': 'slime', 'chanceofspawning': 0.3},
    {'name': 'goblin', 'chanceofspawning': 0.3},
    {'name': 'strong slime', 'chanceofspawning': 0.2},
    {'name': 'orc', 'chanceofspawning': 0.2}
]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    pygame.display.flip()

