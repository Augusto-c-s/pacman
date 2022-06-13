from operator import truediv
import pygame
import constants
import sprites
import os

class MainGame:
    def __init__(self):
        #create the screen game
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
        pygame.display.set_caption(constants.TITLE_GAME)
        self.clock = pygame.time.Clock()
        self.is_init_game = True
        # Defines the font of the words we going use
        self.font = pygame.font.match_font(constants.FONT) 
        self.load_files()

    def new_game(self):
        # this method contain the class of sprites
        self.all_sprites = pygame.sprite.Group()
        self.initiate()   

    def initiate(self):
        # loop of the game
        self.playing_game = True
        while self.playing_game:
            self.clock.tick(constants.FPS)
            self.events()
            self.update_sprites()
            self.print_sprites()

    def events(self):
        # defines the events of the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.playing_game:
                    self.playing_game = False
                self.is_init_game = False

    def update_sprites(self):
        #update all sprites
        self.all_sprites.update()
        

    def print_sprites(self):
        #print the screen with black 
        self.screen.fill(constants.BLACK)
        # now we going to draw all sprites in the screen
        self.all_sprites.draw(self.screen)
        # this will go to update the FPS into game
        pygame.display.flip()
        
    def load_files(self):
        # This method going to load the images and audios files
        directory_images = os.path.join(os.getcwd(), 'images')
        self.directory_audios = os.path.join(os.getcwd(), 'audios')
        # These attributes going to return the directory of the images and the output in string
        self.spritesheet = os.path.join(directory_images, constants.SPRITESHEET)
        self.pacman_start_logo = os.path.join(directory_images, constants.PACMANLOGO)
        self.pacman_start_logo = pygame.image.load(self.pacman_start_logo).convert() # Convert the string attribute self.pacman_start_logo into image whith the function .convert()

    def show_text(self, text, size, color, x, y):
        # Show a text into screen of game
        font = pygame.font.Font(self.font, size)
        text = font.render(text, True, color)
        text_rect = text.get_rect()
        # Position into center screen
        text_rect.midtop = (x, y)
        # Show the text into screen
        self.screen.blit(text, text_rect)
        
    def show_menu_logo(self, x, y):
        start_logo_rect = self.pacman_start_logo.get_rect()
        start_logo_rect.midtop = (x,y)
        self.scren.blit(self.pacman_start_logo, start_logo_rect)
        
    def show_start_screen(self):
        #Calling the way our song plays when the firts screen game appears
        pygame.mixer.music.load(os.path.join(os.getcwd(), constants.GAME_START_MUSIC))
        pygame.mixer.music.play()
        
        self.show_menu_logo(constants.WIDTH /2, 20)
        self.show_text(
            '-Press a button to start',
            32,
            constants.YELLOW,
            constants.WIDTH / 2,
            320
        )
        self.show_text(
            'Developed by Augusto Scafi',
            19,
            constants.WHITE,
            constants.WIDTH / 2,
            570
        )
        # To update the screen all the time when will show the text
        pygame.display.flip()
        self.waiting_player()
        
    def waiting_player(self):
        waiting = True
        while waiting:
            self.clock.tick(constants.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    self.is_init_game = False
                if event.type == pygame.KEYUP:
                    waiting = False
                    pygame.mixer.music.stop()
                    pygame.mixer.Sounds(os.path.join(self.directory_audios, constants.PRESS_BUTTON_TO_START)).play()
                
                
    def show_gameover_screen(self):
        pass

    
# Create an object of class MainGame
game = MainGame()
game.show_start_screen()

# Create while loop of the game
while game.playing_game:
    game.new_game()
    game.show_gameover_screen()
