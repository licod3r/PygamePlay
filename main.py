import pygame

pygame.init()
width, height = 800, 600
background_color = 255, 0, 0

screen = pygame.display.set_mode((width, height))

while True:
    screen.fill(background_color)
    pygame.display.flip()