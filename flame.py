import pygame
import random

from settings import *


class Flame(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.pos = (500, 400)
        self.radius = 30
    
    def draw(self, surface:pygame.Surface) -> None:
        colors = [RED, ORANGE, YELLOW]
        # for color in colors:
        #     pygame.draw.circle(surface, color, self.pos, self.radius)
        #     pygame.draw.circle(surface, color, self.pos, self.radius*0.85)
        #     pygame.draw.circle(surface, color, self.pos, self.radius*0.6)
        
        circles = [{'pos': self.pos, 'radius': self.radius}]
        for _ in range(2):
            rand = random.random()
            pos = (self.pos[0] + self.radius*(0.5-random.random()), self.pos[1] - self.radius*2 * rand)
            radius = self.radius * (1.00000001-rand)
            circles.append({'pos': pos, 'radius': radius})
            
        for color in colors:
            for circle in circles:
                pygame.draw.circle(surface, color, circle['pos'], circle['radius'])
                pygame.draw.circle(surface, color, circle['pos'], circle['radius']*0.85)
                pygame.draw.circle(surface, color, circle['pos'], circle['radius']*0.6)