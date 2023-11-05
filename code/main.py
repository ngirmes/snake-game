from settings import *
from snake import Snake
from apple import Apple

class Main:
    def __init__(self) -> None:
        # general
        pygame.init() # Initializes all of the basics of pygame
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) # Creates the basic window
        pygame.display.set_caption('Doodle\'s Snake Game')

        # game objects
        self.bg_rects = [pygame.Rect((COL + int(ROW % 2 == 0)) * CELL_SIZE, ROW * CELL_SIZE, CELL_SIZE, CELL_SIZE) # pygame.Rect params = (left, top, width, height)
                          for COL in range(0, COLS, 2) for ROW in range(ROWS)]
        self.snake = Snake()
        self.apple = Apple(self.snake)

        # timer
        self.update_event = pygame.event.custom_type()
        pygame.time.set_timer(self.update_event, 150) # set_time parameters (event to trigger, time in ms)
        self.game_active = False

        # audio
        self.crunch_sound = pygame.mixer.Sound(join('..', 'audio', 'crunch.wav'))
        self.bg_music = pygame.mixer.Sound(join('..', 'audio', 'arcade.ogg'))
        self.bg_music.set_volume(0.2)
        self.bg_music.play(-1)

    # Handles drawing of display surafce
    def draw_bg(self):
        self.display_surface.fill(LIGHT_GREEN)
        for rect in self.bg_rects:
           pygame.draw.rect(self.display_surface, '#a2d149', rect) # draw.rect parameters(surface to draw on, color, what to draw)
    
    # Handles user input
    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and self.snake.direction.x != -1:
            self.snake.direction = pygame.Vector2(1, 0)
        if keys[pygame.K_LEFT] and self.snake.direction.x != 1:
            self.snake.direction = pygame.Vector2(-1, 0)
        if keys[pygame.K_UP] and self.snake.direction.y != 1:
            self.snake.direction = pygame.Vector2(0, -1)
        if keys[pygame.K_DOWN] and self.snake.direction.y != -1:
            self.snake.direction = pygame.Vector2(0, 1)
        if keys[pygame.K_ESCAPE]:
            self.quit()
        
    # Handles collisions between snake head and apple and snake body/walls
    def collision(self):
        if self.snake.body[0] == self.apple.position:
            self.snake.has_eaten = True
            self.apple.set_position() # Respawns an apple
            self.crunch_sound.play()
        if self.snake.body[0] in self.snake.body[1:] or \
            not 0 <= self.snake.body[0].x < COLS or \
            not 0 <= self.snake.body[0].y < ROWS:
            # Game resets if there is a bad collision
            self.snake.reset()       
            self.game_active = False

    # Quits pygame and ends the loop
    def quit(self):
        pygame.quit()
        exit()

    def draw_shadow(self):
        shadow_surf = pygame.Surface(self.display_surface.get_size())
        shadow_surf.fill((0, 255, 0))
        shadow_surf.set_colorkey((0, 255, 0))

        #surf
        # shadow_surf.blit(self.apple.scaled_surf, self.apple.scaled_rect.topleft + SHADOW_SIZE)
        for surf, rect in self.snake.draw_data:
            shadow_surf.blit(surf, rect.topleft + SHADOW_SIZE)

        mask = pygame.mask.from_surface(shadow_surf)
        mask.invert()
        shadow_surf = mask.to_surface()
        shadow_surf.set_colorkey((255, 255, 255))
        shadow_surf.set_alpha(SHADOW_OPACITY)

        self.display_surface.blit(shadow_surf, (0, 0))

    def run(self):
        while True:
            # An event loop that allows us to catch user input 
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    self.quit()
                
                # Updates snake if game is active
                if event.type == self.update_event and self.game_active:
                    self.snake.update()
                
                # Game is active after user presses any key
                if event.type == pygame.KEYDOWN and not self.game_active:
                    self.game_active = True

            
            # Updates
            self.input()
            self.collision()

            # Drawing (draw order matters!)
            self.draw_bg()
            self.draw_shadow()
            self.snake.draw()
            self.apple.draw()

            pygame.display.update() # Tells pygame to draw whatever is created in the while loop

if __name__ == '__main__':
    main = Main()
    main.run()