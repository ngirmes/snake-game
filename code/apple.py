from settings import *
from random import choice
from math import sin

class Apple:
    def __init__(self, snake) -> None:
        self.position = pygame.Vector2()
        self.display_surface = pygame.display.get_surface()
        self.snake = snake
        self.set_position()
        # Dynamic path recognition using join
        self.apple_surface = pygame.image.load(join('..', 'graphics', 'apple.png')).convert_alpha() # convert alpha converts the surface (the png in this case) into a file format that is more efficient for pygame
        self.scaled_surf = self.apple_surface.copy()
        self.scaled_rect = self.scaled_surf.get_rect(
            center = (self.position.x * CELL_SIZE + CELL_SIZE / 2, self.position.y * CELL_SIZE + CELL_SIZE / 2)
        )
    
    # Sets position for apple avoiding snake tiles
    def set_position(self):
        available_pos = [pygame.Vector2(x, y) for x in range(COLS) for y in range(ROWS) if pygame.Vector2(x, y) not in self.snake.body]
        self.position = choice(available_pos)
    
    #
    def draw(self):
        scale = 1 + sin(pygame.time.get_ticks() / 300) / 3
        self.scaled_surafce = pygame.transform.smoothscale_by(self.apple_surface, scale) # smoothscale_by params = (surface, scale factor)
        self.scaled_rect = self.scaled_surafce.get_rect(
            center = (self.position.x * CELL_SIZE + CELL_SIZE / 2, self.position.y * CELL_SIZE + CELL_SIZE / 2)) # Draws a rectangle around the surface
        self.display_surface.blit(self.scaled_surafce, self.scaled_rect)
        #rect = pygame.Rect(self.position.x * CELL_SIZE, self.position.y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        # blit stands for block image transfer (a method to put one surface on another)
        #self.display_surface.blit(self.apple_surface, rect) # blit parameters = (surface, position/rectangle)
