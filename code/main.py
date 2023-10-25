from settings import *
from snake import Snake
from apple import Apple

class Main:
    def __init__(self) -> None:
        # general
        pygame.init() # Initializes all of the basics of pygame
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) # Creates the basic window
        pygame.display.set_caption('Snake')

        #game objects
        self.bg_rects = [pygame.Rect((COL + int(ROW % 2 == 0)) * CELL_SIZE, ROW * CELL_SIZE, CELL_SIZE, CELL_SIZE) # (left, top, width, height)
                          for COL in range(0, COLS, 2) for ROW in range(ROWS)]
        self.snake = Snake()
        self.apple = Apple(self.snake)

    def draw_bg(self):
        self.display_surface.fill(LIGHT_GREEN)
        for rect in self.bg_rects:
           pygame.draw.rect(self.display_surface, '#a2d149', rect) # draw.rect parameters(surface to draw on, color, what to draw)

    def run(self):
        while True: 
            for event in pygame.event.get(): # An event loop allows us to catch use input
                if event.type == pygame.QUIT:  # User would like to quit
                    pygame.quit() # Only quitting pygame but not python
                    exit() # Exits the loop
            
            # Draw order matters!
            self.draw_bg()
            self.snake.draw()
            self.apple.draw()

            pygame.display.update() # Tells pygame to draw whatever is created in the while loop

if __name__ == '__main__':
    main = Main()
    main.run()