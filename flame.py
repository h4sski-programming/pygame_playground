import pygame
import random
import math

from settings import *


class Flame(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.pos = [500, 400]
        self.radius = 30
        self.flamelets = []
        self.max_flamelets = 100
        
    def update(self) -> None:
        # if len(self.flamelets) < self.max_flamelets and random.random()>0.9:
        # if random.random()>0.1:
        if len(self.flamelets) < self.max_flamelets:
            self.flamelets.append(Flamelet(self.pos[:], self.radius))
        
        for flamelet in self.flamelets[:]:
            flamelet.update()
            if not flamelet.radius > 0:
                self.flamelets.remove(flamelet)
        
    
    def draw(self, surface:pygame.Surface) -> None:
        colors = [[RED, 1], [ORANGE, 0.85], [YELLOW, 0.6], ['white', 0.2]]
        
        for color in colors:
            pygame.draw.circle(surface, color[0], self.pos, self.radius * color[1])
            for flamelet in self.flamelets:
                pygame.draw.circle(surface, color[0], flamelet.pos, flamelet.radius * color[1])
        
        # for color in colors:
        #     pygame.draw.circle(surface, color, self.pos, self.radius)
        #     pygame.draw.circle(surface, color, self.pos, self.radius*0.85)
        #     pygame.draw.circle(surface, color, self.pos, self.radius*0.6)
        
        # circles = [{'pos': self.pos, 'radius': self.radius}]
        # for _ in range(6):
        #     rand = random.random()
        #     pos = (self.pos[0] + self.radius*(0.5-random.random()), self.pos[1] - self.radius*2 * rand)
        #     radius = self.radius * (1.00000001-rand)
        #     circles.append({'pos': pos, 'radius': radius})
            
        # for color in colors:
        #     for circle in circles:
        #         pygame.draw.circle(surface, color[0], circle['pos'], circle['radius']*color[1])
                # pygame.draw.circle(surface, color, circle['pos'], circle['radius']*0.85)
                # pygame.draw.circle(surface, color, circle['pos'], circle['radius']*0.6)


class Flamelet(pygame.sprite.Sprite):
    def __init__(self, pos:list[float], radius:float):
        super().__init__()
        self.pos = pos
        self.radius = radius
        self.velocity = 2
        
        ## set self.pos/0.5 for cloud of the flame / gas
        ## or set self.pos/2 for flame type of the look
        angle_range = math.pi/1.7
        self.angle = random.random()*angle_range - math.pi/2 - angle_range/2
        
    def update(self) -> None:
        self.pos[0] += self.velocity * math.cos(self.angle)
        self.pos[1] += self.velocity * math.sin(self.angle)
        self.radius -= self.velocity * 0.3
        