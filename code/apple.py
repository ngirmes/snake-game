from settings import *
from random import choice

class Apple:
    def __init__(self, snake) -> None:
        self.position = pygame.Vector2(5, 8)
        self.display_surface = pygame.display.get_surface()
        self.snake = snake
        self.set_position()
    
    def set_position(self):
        available_pos = [pygame.Vector2(x, y) for x in range(COLS) for y in range(ROWS) if pygame.Vector2(x, y) not in self.snake.body]
        self.position = choice(available_pos)
    
    def draw(self):
        rect = pygame.Rect(self.position.x * CELL_SIZE, self.position.y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(self.display_surface, 'blue', rect)