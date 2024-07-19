import pygame
import os

from physic_mechanic import fall


class Player(pygame.sprite.Sprite):
    def __init__(self, pos:list[float]) -> None:
        self.pos = pos
        self.velocity_max = 5
        
        self.img = pygame.image.load(os.path.join('img', 'player_a_01.png')).convert_alpha()
        self.mask = pygame.mask.from_surface(self.img)
        self.rect = self.img.get_rect()
        
    def update(self) -> None:
        fall(self)