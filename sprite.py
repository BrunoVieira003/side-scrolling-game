import pygame
pygame.init()

class Sprite:
    def __init__(self, file_name, repeat=1, initial=0):
        self.sprites = []
        self.index = 0
        while True:
            try:
                image = pygame.image.load(f"{file_name}{initial}.png")
                for c in range(repeat):
                    self.sprites.append(image)
            except:
                if len(self.sprites) == 0:
                    raise FileNotFoundError(f"{file_name}{initial} not found")
                break
            initial += 1
    
    def animate(self, screen, x, y):
        screen.blit(self.sprites[self.index], [x, y])
        self.index = (self.index+1)%len(self.sprites)
            