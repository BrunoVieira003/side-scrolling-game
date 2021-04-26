import pygame
from sprite import Sprite
import os
pygame.init()

class Entity:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.is_moving = False
        self.to_right = False

        self.name = name
        with open("assets\\textures.json", "r") as arq:
            self.textures = eval(arq.read())
        self.r_idle_sprites = Sprite(os.getcwd()+self.textures[name]["idle"]["right"], 2)
        self.r_run_sprites = Sprite(os.getcwd()+self.textures[name]["run"]["right"], 2)
        self.l_idle_sprites = Sprite(os.getcwd()+self.textures[name]["idle"]["left"], 2)
        self.l_run_sprites = Sprite(os.getcwd()+self.textures[name]["run"]["left"], 2)
    
    def show(self, screen):
        if not self.is_moving and self.to_right:
            self.r_idle_sprites.animate(screen, self.x, self.y)
        elif not self.is_moving and self.to_left:
            self.l_idle_sprites.animate(screen, self.x, self.y)
        elif self.to_right:
            self.r_run_sprites.animate(screen, self.x, self.y)
        elif self.to_left:
            self.l_run_sprites.animate(screen, self.x, self.y)

    def listen(self):
        pass
    