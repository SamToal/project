import random
import pygame
pygame.init()
loop=1

window = pygame.display.set_mode((1600,900))
background = pygame.Surface(window.get_size())
background.fill((255,255,255))
background = background.convert()

background = pygame.image.load("menu_background.png")

window.blit(background,(0,0))

pygame.display.flip()























while loop == 1:
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                pygame.quit()
                quit()
       
