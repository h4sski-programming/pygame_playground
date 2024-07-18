import pygame


from settings import *
from flame import Flame


class Game():
    def __init__(self) -> None:
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode(RESOLUTION)
        pygame.display.set_caption('Arcade shooter @ h4sski')
        
        self.main_surface = pygame.Surface(RESOLUTION)
        
        self.flame = Flame()
        
        ## Run the game after setting up all stuff
        self.run()
    
    
    def events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    
    def update(self) -> None:
        pass
    
    def draw(self) -> None:
        self.window.fill(0)
        
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