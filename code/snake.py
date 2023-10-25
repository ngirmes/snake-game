from settings import *

class Snake:
    def __init__(self) -> None:
        self.display_surface = pygame.display.get_surface() # Pygame has a function for getting the surface even though this is a separate class
        self.body = [pygame.Vector2(START_COL - COL, START_ROW) for COL in range(START_LENGTH)] # Vector 2 parameters: (x, y)

    def draw(self):
        for point in self.body:
            rect = pygame.Rect(point.x * CELL_SIZE, point.y * CELL_SIZE, CELL_SIZE, CELL_SIZE) # (left, top, width, height)
            pygame.draw.rect(self.display_surface, 'red', rect)