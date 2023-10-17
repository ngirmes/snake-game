from settings import *

class Main:
    def __init__(self) -> None:
        # general
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

        #game objects
        self.bg_rects = [pygame.Rect(COL * CELL_SIZE, ROW * CELL_SIZE, CELL_SIZE, CELL_SIZE) for COL in range(0, COLS, 2) for ROW in range(1, ROWS)]
        print(self.bg_rects)

    def draw_bg(self):
        for rect in self.bg_rects:
           pygame.draw.rect(self.display_surface, 'red', rect) 

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            
            self.display_surface.fill(LIGHT_GREEN)
            self.draw_bg()
            pygame.display.update()

main = Main()
main.run()