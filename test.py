import pygame

pygame.init()
fonts = pygame.font.get_fonts()
if "timesnewroman" in fonts:
    print("Font is available!")
else:
    print("timesnewroman is not available. Check the available fonts:")
    print(sorted(fonts))

pygame.quit()