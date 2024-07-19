import pygame

def draw_sprite(sprite:pygame.sprite.Sprite, surface:pygame.Surface) -> None:
    surface.blit(sprite.img, sprite.pos)