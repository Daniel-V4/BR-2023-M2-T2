import pygame

from dino_runner.utils.constants import BG, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, GAME_OVER, RESET
#from dino_runner.utils.functions import Color_loop
from dino_runner.components.Dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacleManager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
#from dino_runner.components.leaderboard.leaderboardManager import LeaderboardManager

FONT_STYLE = 'freesansbold.ttf'


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.score = 0
        self.death_count = 0
        self.last_score = 0
        #self.current_highscore = 0
        #self.leaderboard_pendant = True
        #self.name_input = str()
        
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        #self.leaderboard_manager = LeaderboardManager()
        #self.color_loop = Color_loop()

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
        self.power_up_manager.reset_power_ups()
        self.score = 0
        self.game_speed = 20
        while self.playing:
            self.events()
            self.update()
            self.draw()
    
    def reset_game(self):
        self.last_score = self.score
        #if self.score > self.current_highscore:
            #self.current_highscore = self.score
        self.score = 0
        self.game_speed = 20
        #self.leaderboard_pendant = True
        #self.name_input = str()

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
        self.power_up_manager.update(self.score, self.game_speed, self.player)

    def update_score(self):
        self.score += 1
        if self.score % 100 == 0:
            self.game_speed += 1

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255)) 
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.draw_score()
        self.draw_power_up_time()
        self.power_up_manager.draw(self.screen)
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
    #    self.print_text(f"Last score: {self.last_score}", (0, 0, 0), (1000, 75))
    #    self.print_text(f"Current best: {self.current_highscore}", (0, 0, 0), (1000, 100))


    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_up_time - pygame.time.get_ticks()) / 1000)
            if time_to_show >= 0:
                self.print_text(
                    f"{self.player.type.capitalize()} enabled for {time_to_show} seconds",
                    (0, 0, 0), (500, 40)
                )
            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE 
                self.player.hammer = False
                self.player.shield = False   

    def handle_events_on_menu(self): 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.run() 

    #def handle_events_in_leaderboard_input(self):
        #for event in pygame.event.get():
            #if event.type == pygame.QUIT:
                #self.playing = False
                #self.running = False
            #elif event.type == pygame.KEYDOWN:
                #if event.key == pygame.K_RETURN:
                    #self.leaderboard_manager.update_score(self.name_input, self.last_score)
                    #self.leaderboard_pendant = False
                #elif event.key == pygame.K_BACKSPACE:
                    #self.name_input = self.name_input[:-1]
                #elif event.unicode.isalpha() and len(self.name_input) < 7:
                    #self.name_input += event.unicode

    def show_menu(self):
        self.screen.fill((255, 255, 255))
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2

        if self.death_count == 0:
            self.print_text("Press any key to start", (0, 0, 0), (half_screen_width - 20, half_screen_height - 140))
            #self.print_text("LEADERBOARD", (0, 0, 0), (half_screen_width, half_screen_height))
            #self.show_leaderboard(half_screen_width - 100, half_screen_height + 50)
            self.handle_events_on_menu()
        #elif self.leaderboard_pendant == True:
            #self.print_text("Input your name:", (0, 0, 0), (half_screen_width - 20, half_screen_height - 140))
            #self.print_text(self.name_input, (0, 0, 0), (half_screen_width, half_screen_height))
            #self.handle_events_in_leaderboard_input()
        else:
            self.screen.blit(GAME_OVER, (half_screen_width - 170, half_screen_height - 150))
            self.screen.blit(RESET, (half_screen_width - 20, half_screen_height - 100))
            self.print_text(f"Your last score was: {self.last_score}", (0, 0, 0), (half_screen_width, half_screen_height + 25))
            self.print_text(f"You have died {self.death_count} times", (0, 0, 0), (half_screen_width, half_screen_height))
            #self.print_text(f"Your current best is: {self.current_highscore}", (0, 0, 0), (half_screen_width, half_screen_height + 50))
            #self.print_text("LEADERBOARD", (0, 0, 0), (half_screen_width, half_screen_height + 80))
            #self.show_leaderboard(half_screen_width - 100, half_screen_height + 105)
            self.handle_events_on_menu()
            
        pygame.display.update()  # .flip()
    
    #def show_leaderboard(self, x, y):
        #scores = self.leaderboard_manager.read_scores()
        #color = (self.color_loop(), (255, 215, 0), (192, 192, 192), (205, 127, 50), (0, 0, 0))
        #for i, score in enumerate(scores):
            #self.print_text(f"{i+1}. {score['name']}: {score['score']}", (color[i]), (x, y))
            #y += 30
    
    def print_text(self, text, color, position):
        font = pygame.font.Font(FONT_STYLE, 22)
        text = font.render(text, True, color)
        text_rect = text.get_rect()
        text_rect.center = position
        self.screen.blit(text, text_rect)