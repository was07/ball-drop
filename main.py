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
              height=random.randint(100, 8000) / 10,
              exeleration=random.randrange(10, 160) / 10,
              bounce_percentage=random.randrange(400, 1000) / 10)
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
