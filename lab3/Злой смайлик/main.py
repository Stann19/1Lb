import pygame
from pygame.draw import *

pygame.init()

FPS=30
screen=pygame.display.set_mode((400, 400))
screen.fill((127, 127, 127))
circle(screen, (255, 255, 0), (200, 200), 170)
circle(screen, (0, 0, 0), (200, 200), 170, 3)
circle(screen, (255, 0, 0), (125, 140), 34)
circle(screen, (255, 0, 0), (275, 140), 28)
circle(screen, (0, 0, 0), (275, 140), 15)
circle(screen, (0, 0, 0), (125, 140), 15)
rect(screen, (0, 0, 0), (120, 285, 160, 30))
line(screen, (0, 0, 0), (183, 135), (52, 60), 10)
line(screen, (0, 0, 0), (230, 125), (350, 70), 10)



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
