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
        print(directory_images)

    def show_start_screen(self):
        pass

    def show_gameover_screen(self):
        pass

    
# Create an object of class MainGame
game = MainGame()
game.show_start_screen()

# Create while loop of the game
while game.playing_game:
    game.new_game()
    game.show_gameover_screen()
