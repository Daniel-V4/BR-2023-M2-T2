import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from dino_runner.components.Dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacleManager import ObstacleManager

FONT_STYLE = 'freesansbold.ttf'


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.score = 0
        self.death_count = 0
        
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()

        pygame.display.quit()
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        self.obstacle_manager.reset_obstacles()
        self.score = 0
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.update_score()

    def update_score(self):
        self.score += 1
        if self.score % 100 == 0:
            self.game_speed += 5

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255)) 
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.draw_score()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_score(self):
        self.print_text(f"Score: {self.score}", (0, 0, 0), (1000, 50))

    def handle_events_on_menu(self): 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.run() 

    def show_menu(self):
        self.screen.fill((255, 255, 255))
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2

        if self.death_count == 0:
            self.print_text("Press any key to start", (0, 0, 0), (half_screen_width - 20, half_screen_height - 140))
        else:
            self.screen.blit(ICON, (half_screen_width - 20, half_screen_height - 140))
            self.print_text(f"Your last score was: {self.score}", (0, 0, 0), (half_screen_width, half_screen_height))
            self.print_text(f"You have died {self.death_count} times", (0, 0, 0), (half_screen_width, half_screen_height + 25))
            ## mostrar mensagem "Press any key to restart"
            ## mostrar pontuação atingida
            ## mostrar contador de mortes

            ### Resetar a contagem de pontos e a velocidade quando jogo 'restartado'
            ### Criar método para remover a repetição de código para texto

        pygame.display.update()  # .flip()

        self.handle_events_on_menu()
    
    def print_text(self, text, color, place):
        font = pygame.font.Font(FONT_STYLE, 22)
        text = font.render(text, True, color)
        text_rect = text.get_rect()
        text_rect.center = place
        self.screen.blit(text, text_rect)