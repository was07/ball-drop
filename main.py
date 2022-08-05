import sys
import random
 
import pygame
from pygame.locals import *

from ball import Ball
 
pygame.init()
 
fps = 60
fpsClock = pygame.time.Clock()
 
width, height = 650, 450
screen = pygame.display.set_mode((width, height))

balls = [Ball(screen,
              height=(random.randint(100, 600) * 100) / random.randint(90, 110),
              exeleration=(random.randrange(0, 16) * 100) / random.randint(90, 110),
              bounce_percentage=random.randrange(20, 100))
        for _ in range(10)]

 
# Game loop.
run = True
while True:
    screen.fill((0, 0, 0))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                run = not run
    
    # Update.
    if run:
        for ball in balls:
            ball.update()
    
    # Draw.
    for ball in balls:
        ball.draw()
    
    pygame.display.flip()
    fpsClock.tick(fps)
