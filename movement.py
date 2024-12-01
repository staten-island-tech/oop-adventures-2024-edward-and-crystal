import pygame
pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Game')
running = True

class OpenWorld():
    def LoadRoom(room):
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT():
                    quit()
            screen.fill((10, 10, 10))
            
    def Movement(player):
        pass