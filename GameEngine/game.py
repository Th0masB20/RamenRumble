import pygame
from Enemy.Enemy import *

def refreshWindow(window):
    window.fill("pink")


def runGame(width, height):

    window:pygame.Surface = pygame.display.set_mode((width, height));
    run:bool = True
    squareObject = Enemy(pos=(200,200), size=(30,30))

    pygame.init()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
        
        squareObject.moveAI(pygame.time.get_ticks())
        
        window.fill("pink")
        squareObject.draw(window)
        pygame.display.flip()
        
        
        