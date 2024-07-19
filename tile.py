import pygame
import os

from settings import *


class TileMap(pygame.sprite.Sprite):
    def __init__(self) -> None:
        self.tiles = []
        for row in range(20):
            for col in range(20):
                self.tiles.append(Tile([row*TILE_SIZE[0], col*TILE_SIZE[1]]))
    
    def update(self) -> None:
        for tile in self.tiles:
            tile.update()
    
    def draw(self, surface:pygame.Surface) -> None:
        for tile in self.tiles:
            tile.draw(surface)



class Tile(pygame.sprite.Sprite):
    def __init__(self, pos:list[int]) -> None:
        self.pos = pos
        self.amination_counter = FPS/4
        self.amination_counter_tmp = 0
        self.imgs = ['grass_01.png', 'grass_02.png', 'grass_03.png', 'grass_02.png']
        self.img_id = 0
        
    def update(self) -> None:
        if self.amination_counter_tmp <= 0:
            self.amination_counter_tmp = self.amination_counter
            self.img_id += 1
            if self.img_id >= len(self.imgs):
                self.img_id = 0
            
            self.img = pygame.image.load(os.path.join('img', self.imgs[self.img_id])).convert()
            self.mask = pygame.mask.from_surface(self.img)
        self.amination_counter_tmp -= 1
        
    
    def draw(self, surface:pygame.Surface) -> None:
        pygame.draw.rect(surface, 'blue', (self.pos, TILE_SIZE))
        
        surface.blit(self.img, dest=self.pos, area=((0, 0), TILE_SIZE))
        
        