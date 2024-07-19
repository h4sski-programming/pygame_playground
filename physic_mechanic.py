import pygame
import math

from settings import *


def fall(sprite:pygame.sprite.Sprite) -> None:
    if sprite.pos[1] < RESOLUTION[1] - sprite.mask.get_size()[1]:
        sprite.pos[1] += FPS/30



# def get_sprite_height(sprite:pygame.sprite.Sprite) -> int:
#     return sprite.rect.get_height()