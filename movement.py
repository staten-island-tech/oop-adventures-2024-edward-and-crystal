import pygame
pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Game')
running = True

class OpenWorld():
    def LoadRoom(room):
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
            
            screen.fill((20, 20, 25))
            for rect in room['rectangles']:
                pygame.draw.rect(screen, (40, 40, 50), rect)
                
            pygame.draw.rect(screen, (185, 220, 240), (0, 620, 1280, 100))
            
            pygame.display.update()
            
    def Movement(player):
        pass
    
room = {
    "rectangles" : [
    (100, 100, 100, 400),
    (200, 200, 400, 50)]
    }   
    
OpenWorld.LoadRoom(room)

