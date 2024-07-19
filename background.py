import pygame
import os

from settings import *


class BackgroundLayer():
    def __init__(self) -> None:
        super().__init__()
        self.layers = [
            'backgroung_a_01_01.png', 
            'backgroung_a_01_02.png', 
            'backgroung_a_01_03.png',
        ]
        
        self.layers_img = []
        self.masks = []
        for layer in self.layers:
            self.layers_img.append(pygame.image.load(os.path.join('img', layer)).convert_alpha())
            self.masks = pygame.mask.from_surface(self.layers_img[-1])
        
        self.layers_replacement = [0, 0, 0]
        
        
    def update(self, x:float) -> None:
        for i in range(len(self.layers_replacement)):
            self.layers_replacement[i] = -((x/RESOLUTION[0]) * 2560) / (len(self.layers_img) - i+1)
    
    
    def draw(self, surface:pygame.Surface) -> None:
        for i, img in enumerate(self.layers_img):
            surface.blit(img, dest=[self.layers_replacement[i], 0])