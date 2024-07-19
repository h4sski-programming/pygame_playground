import pygame


from settings import *
from flame import Flame
from tile import Tile, TileMap
from background import BackgroundLayer
from player import Player

from draw_sprite import draw_sprite


class Game():
    def __init__(self) -> None:
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode(RESOLUTION)
        pygame.display.set_caption('Arcade shooter @ h4sski')
        
        self.main_surface = pygame.Surface(RESOLUTION)
        
        self.background_layer = BackgroundLayer()
        self.tile_map = TileMap()
        self.flame = Flame()
        self.player = Player([100, 120])
        
        ## Run the game after setting up all stuff
        self.run()
    
    
    def events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    
    def update(self) -> None:
        
        self.background_layer.update(pygame.mouse.get_pos()[0])
        self.tile_map.update()
        
        self.player.update()
        
        self.flame.update()
        self.flame.pos = list(pygame.mouse.get_pos())
    
    def draw(self) -> None:
        self.window.fill(0)
        
        ### draw tile_map
        self.tile_map.draw(self.window)
        self.background_layer.draw(self.window)
        
        draw_sprite(self.player, self.window)
        
        self.flame.draw(self.window)
        
        
        pygame.display.flip()
    
    
    
    def run(self) -> None:
        self.running = True
        while self.running:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        pygame.quit()
    

if __name__ == '__main__':
    pygame.init()
    g = Game()