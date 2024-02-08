import pygame

root = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Application')

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
