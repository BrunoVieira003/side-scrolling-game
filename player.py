import pygame
from entity import Entity
pygame.init()

class Player(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, name="player")
        self.to_right = True
    
    def listen(self):
        keys = pygame.key.get_pressed()
        self.is_moving = False
        if keys[pygame.K_RIGHT]:
            self.is_moving = True
            self.to_right = True
            self.to_left = False
            self.x += 3
        if keys[pygame.K_LEFT]:
            self.is_moving = True
            self.to_left = True
            self.to_right = False
            if self.x >= 1:
                self.x -= 3