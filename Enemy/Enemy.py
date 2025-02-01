import pygame
import random

class Enemy:
    def __init__(self, size:tuple[int,int], pos:tuple[int, int]):
        self.pos = pos
        self.image = pygame.Rect(pos, size) #pygame.image.load("")
        self.size = size
        self.lastMoveTime = 0
        self.waitTime = 2
        self.canMove = False
        self.walkDir = 0
        self.randomWalkTime = 0
        self.startMove = 0
        
    def move(self, speed, window:pygame.Surface):
        x = 0
        y = 0
        if self.walkDir == 1:
            x = 1
        elif self.walkDir == 2:
            x = -1
        elif self.walkDir == 3:
            y = 1
        elif self.walkDir == 4:
            y = -1
        
        self.pos = (self.pos[0] + (x * speed) , self.pos[1] + (y * speed))
        self.pos = self.collisionDetection(self, self.pos, window)
        self.image.topleft = self.pos

    def moveAI(self, currentTime):
        if (currentTime - self.lastMoveTime) / 1000 > self.waitTime and not self.canMove:
            self.canMove = True
            self.walkDir = random.randint(1,4)
            self.randomWalkTime = random.randint(1,3)
            self.startMove = currentTime
        if self.canMove:
            self.move(0.02)
            if (currentTime - self.startMove)/1000 >= self.randomWalkTime:
                self.canMove = False
                self.lastMoveTime = currentTime
                return 
    
    def collisionDetection(self, pos:tuple[int,int], window:pygame.Surface):
        if self.image.right < window.get_width():
            pos = (window.get_width() - self.image.width, pos[1])
        if self.image.left < 0:
            pos = (0, pos[1])
        if self.image.top < 0:
            pos = (pos[0], 0)
        if self.image.bottom > window.get_height():
            pos = (pos[0], window.get_height() - self.image.height)
            
        return pos
        
    def draw(self,window:pygame.Surface):
        pygame.draw.rect(window, (0,0,0), self.image)
